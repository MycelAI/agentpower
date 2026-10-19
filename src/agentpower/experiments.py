# SPDX-FileCopyrightText: 2026 Alphin Tom / Mycel UG (haftungsbeschränkt)
#
# SPDX-License-Identifier: MIT

"""Monte Carlo experiments behind docs/simulation.md."""

from __future__ import annotations

import numpy as np

from . import estimators
from .methods import METHODS, draw_context, m_quality_adjusted
from .model import SCENARIOS, SPECULATIVE, Scenario, draw_org_scenario, simulate_workers

WORKERS_PER_ORG = 60
LOADED_COST_EUR = 85_000  # fully loaded annual cost of one German knowledge worker
TRAINING_EUR = 700  # per FTE and year: ~40 h onboarding amortised over 3 years + enablement


def spearman(a, b) -> float:
    ra = np.argsort(np.argsort(a))
    rb = np.argsort(np.argsort(b))
    return float(np.corrcoef(ra, rb)[0, 1])


def e1_methods(n_orgs: int, seed: int) -> list[dict]:
    """Score every measurement concept against the simulated truth."""
    rng = np.random.default_rng(seed)
    truth = np.empty(n_orgs)
    est = {k: np.empty(n_orgs) for k in METHODS}
    gamed = {k: np.empty(n_orgs) for k in METHODS}
    for i in range(n_orgs):
        workers = simulate_workers(draw_org_scenario(rng), WORKERS_PER_ORG, rng)
        truth[i] = workers.org_ap
        ctx = draw_context(rng)
        for k, fn in METHODS.items():
            state = rng.bit_generator.state
            est[k][i] = fn(workers, ctx, rng)
            rng.bit_generator.state = state  # same noise, gaming switched on
            gamed[k][i] = fn(workers, ctx.__class__(**{**ctx.__dict__, "gaming": 1.0}), rng)
    true_band = np.array([estimators.band(x) for x in truth])
    rows = []
    for k in METHODS:
        e = est[k]
        log_err = np.log(e / truth)
        moved = truth - 1 > 0.05
        rows.append({
            "method": k,
            "bias_pct": 100 * (np.exp(np.median(log_err)) - 1),
            "mae_ap": float(np.mean(np.abs(e - truth))),
            "gain_ratio": float(np.median((e[moved] - 1) / (truth[moved] - 1))),
            "rmse_log": float(np.sqrt(np.mean(log_err**2))),
            "p90_abs_err_pct": 100 * (np.exp(np.quantile(np.abs(log_err), 0.9)) - 1),
            "spearman": spearman(e, truth),
            "band_accuracy": float(np.mean([estimators.band(x) for x in e] == true_band)),
            "gaming_inflation_pct": 100 * (np.exp(np.median(np.log(gamed[k] / e))) - 1),
        })
    return rows


def e2_aggregation(n_orgs: int, seed: int) -> list[dict]:
    """Ratio of totals over FTE vs. the shortcuts people use."""
    rng = np.random.default_rng(seed)
    errs = {"mean of individual ratios": [], "ratio of totals, headcount": [],
            "ratio of totals, FTE (spec)": []}
    for _ in range(n_orgs):
        w = simulate_workers(draw_org_scenario(rng), WORKERS_PER_ORG, rng)
        truth = w.org_ap
        base_fte_share = rng.uniform(0.88, 0.96)  # FTE per head in the baseline period
        now_fte_share = np.mean(w.fte)
        errs["mean of individual ratios"].append(np.mean(w.ap) / truth)
        errs["ratio of totals, headcount"].append(truth * now_fte_share / base_fte_share / truth)
        errs["ratio of totals, FTE (spec)"].append(1.0)
    rows = []
    for k, v in errs.items():
        le = np.log(v)
        rows.append({"aggregation": k, "bias_pct": 100 * (np.exp(np.median(le)) - 1),
                     "p90_abs_err_pct": 100 * (np.exp(np.quantile(np.abs(le), 0.9)) - 1)})
    return rows


def _quantiles(x) -> dict:
    q = np.quantile(x, [0.1, 0.5, 0.9])
    return {"p10": q[0], "median": q[1], "p90": q[2]}


def e3_calibration(n_workers: int, n_orgs: int, seed: int) -> list[dict]:
    """Where AP ratios actually sit under each calibrated scenario."""
    rng = np.random.default_rng(seed)
    rows = []
    for s in [*SCENARIOS.values(), SPECULATIVE]:
        w = simulate_workers(s, n_workers, rng)
        orgs = [simulate_workers(s, WORKERS_PER_ORG, rng) for _ in range(n_orgs)]
        org_ap = np.array([o.org_ap for o in orgs])
        org_cap = np.array([o.org_capacity for o in orgs])
        org_vol = np.array([o.org_volume for o in orgs])
        rows.append({
            "scenario": s.name,
            "worker": _quantiles(w.ap),
            "worker_below_1_pct": 100 * float(np.mean(w.ap < 1.0)),
            "org_ap": _quantiles(org_ap),
            "org_capacity": _quantiles(org_cap),
            "absorption": float(np.median((org_vol - 1) / (org_cap - 1))),
        })
    return rows


def _spend_scenario(base: Scenario, spend: float, b0: float) -> Scenario:
    """Illustrative response of exposure, adoption and saving to AI spend."""
    u = 1.0 - np.exp(-spend / b0)
    return base.with_(
        exposure=0.40 + 0.45 * u, adoption=0.35 + 0.60 * u, saving=0.40 + 0.45 * u,
        reallocation=0.50 + 0.35 * u, review=0.30 - 0.12 * u, spend_eur=spend,
    )


def _curve(base: Scenario, b0: float, rng, n_orgs: int = 40) -> list[dict]:
    curve, prev = [], None
    for spend in (0, 240, 600, 1200, 2400, 6000, 12000, 24000, 48000):
        s = _spend_scenario(base, spend, b0)
        ap = float(np.median([simulate_workers(s, 400, rng).org_ap for _ in range(n_orgs)]))
        row = {"spend_eur": spend, "ap": ap,
               "avg_cost_per_ap": estimators.cost_per_ap(spend + (TRAINING_EUR if spend else 0), ap)}
        if prev is not None and ap > prev[1]:
            row["marginal_cost_per_ap"] = (spend - prev[0]) / (ap - prev[1])
        curve.append(row)
        prev = (spend, ap)
    return curve


def e5_economics(n_orgs: int, seed: int, b0: float = 6000.0) -> dict:
    """Cost of an additional AP, per scenario and along a spend curve."""
    rng = np.random.default_rng(seed)
    per_scenario = []
    for s in SCENARIOS.values():
        aps = np.array([simulate_workers(s, WORKERS_PER_ORG, rng).org_ap for _ in range(n_orgs)])
        cost = s.spend_eur + TRAINING_EUR
        cpa = np.array([estimators.cost_per_ap(cost, a) for a in aps])
        per_scenario.append({
            "scenario": s.name, "spend_eur": s.spend_eur, "added_cost_eur": cost,
            "ap_gain_median": float(np.median(aps - 1)),
            "cost_per_ap": _quantiles(np.minimum(cpa, 1e7)),
            "share_cheaper_than_hire_pct": 100 * float(np.mean(cpa < LOADED_COST_EUR)),
        })
    base = SCENARIOS["typical-2026"]
    curve = _curve(base, b0, rng)
    sensitivity = []
    for alt in (2000.0, 6000.0, 15000.0):
        c = _curve(base, alt, rng, n_orgs=20)
        sensitivity.append({"b0": alt, "min_marginal_cost_per_ap": min(
            x["marginal_cost_per_ap"] for x in c if "marginal_cost_per_ap" in x),
            "max_ap": max(x["ap"] for x in c)})
    return {"per_scenario": per_scenario, "curve": curve, "b0": b0, "b0_sensitivity": sensitivity,
            "loaded_cost_eur": LOADED_COST_EUR}


SENSITIVE = ("exposure", "adoption", "saving", "frontier_miss", "review", "reallocation",
             "quality_gain", "miss_quality")


def e6_sensitivity(n_workers: int, seed: int) -> list[dict]:
    """One-at-a-time +/-25% on each parameter, integrated-team scenario."""
    base = SCENARIOS["integrated-team"]
    ref = simulate_workers(base, n_workers, np.random.default_rng(seed)).org_ap
    rows = []
    for p in SENSITIVE:
        v = getattr(base, p)
        lo = simulate_workers(base.with_(**{p: v * 0.75}), n_workers, np.random.default_rng(seed)).org_ap
        hi = simulate_workers(base.with_(**{p: min(v * 1.25, 0.99)}), n_workers,
                              np.random.default_rng(seed)).org_ap
        rows.append({"parameter": p, "low": lo, "high": hi, "swing": abs(hi - lo), "ref": ref})
    rows.sort(key=lambda r: -r["swing"])
    return rows


def e7_audit_size(seed: int, reps: int = 2000) -> list[dict]:
    """How many audited deliverables AP-Q needs for a given precision."""
    rng = np.random.default_rng(seed)
    w = simulate_workers(SCENARIOS["integrated-team"], 400, rng)
    rows = []
    for n in (10, 20, 40, 80, 160, 320):
        row = {"n_audit": n}
        for label, mix in (("raw_count", 0.08), ("effort_weighted", 0.04), ("audit_only", 0.0)):
            draws = np.array([m_quality_adjusted(w, draw_context(rng), rng, n_audit=n, mix_noise=mix)
                              for _ in range(reps)])
            lo, hi = np.quantile(draws / w.org_ap, [0.05, 0.95])
            row[f"ci90_half_width_pct_{label}"] = 100 * (hi - lo) / 2
        rows.append(row)
    return rows


def e8_requirements() -> list[dict]:
    """Share of baseline time AI must remove for a given AP (Amdahl identity)."""
    rows = []
    for target in (1.1, 1.25, 1.5, 2.0, 3.0, 5.0, 10.0):
        rows.append({"ap": target,
                     **{f"time_removed_at_realloc_{r}": (1 - 1 / (1 + (target - 1) / r))
                        for r in (1.0, 0.8, 0.5)}})
    return rows


def run_all(seed: int = 20261019, quick: bool = False) -> dict:
    n = 300 if quick else 1500
    return {
        "seed": seed,
        "e1": e1_methods(n, seed + 1),
        "e2": e2_aggregation(n, seed + 2),
        "e3": e3_calibration(5000 if quick else 40000, 100 if quick else 500, seed + 3),
        "e5": e5_economics(100 if quick else 400, seed + 5),
        "e6": e6_sensitivity(5000 if quick else 40000, seed + 6),
        "e7": e7_audit_size(seed + 7, 300 if quick else 2000),
        "e8": e8_requirements(),
    }
