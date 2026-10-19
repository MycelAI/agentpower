"""Candidate ways to measure an organisation's AP ratio.

Each method sees only what a real organisation could observe, with the
noise, confounders and gaming channels that come with it. The experiments
score each one against the simulated truth.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .model import Workers

YEARS = 3.0  # baseline to measurement period
V1_TOKENS_PER_AP = 200_000 * 250  # v1.0 "SCW": 200K tokens/day x 250 days = 1 extra AP
EUR_PER_MTOK = 3.0  # blended EUR per million tokens, cache-heavy agentic use, Oct 2026


@dataclass(frozen=True)
class Context:
    """Organisation-level confounders that are not AI."""

    drift: float  # background productivity drift over the period
    market: float  # price and demand effect on revenue
    outsourcing: float  # headcount moved to contractors (revenue/head inflation)
    gaming: float  # 0 = no incentive, 1 = the metric is a target
    token_intensity: float = 1.0  # model tier, caching and agent-loop style


def draw_context(rng: np.random.Generator, gaming: float = 0.0) -> Context:
    drift = rng.lognormal(0.015 * YEARS, 0.03 * np.sqrt(YEARS))
    market = rng.lognormal(0.02 * YEARS, 0.15 * np.sqrt(YEARS))
    outsourcing = rng.uniform(1.0, 1.35) if rng.random() < 0.3 else 1.0
    # Price per token differs ~40x across tiers and usage style ~10x (Jellyfish: top decile
    # uses ~10x the tokens for ~2x the output), so tokens per unit of work vary widely.
    token_intensity = rng.lognormal(0.0, 0.9)
    return Context(drift, market, outsourcing, gaming, token_intensity)


def _fte_weights(w: Workers) -> np.ndarray:
    return w.fte * w.base_output


def m_self_estimate(w: Workers, c: Context, rng) -> float:
    """S: managers estimate 'headcount needed without AI / current headcount'.

    Anchors on perceived time savings (capacity), with optimism bias. METR 2025:
    developers believed +20% while measured -19%.
    """
    bias = rng.normal(0.20, 0.15) + 0.15 * c.gaming
    return float(w.org_capacity * np.exp(bias))


def m_revenue_per_head(w: Workers, c: Context, rng) -> float:
    """R: revenue per headcount now / baseline (the v1.0 Klarna method)."""
    wt = _fte_weights(w)
    heads = np.ones_like(w.fte)
    value = np.sum(wt * w.ap) / np.sum(wt)
    fte_share = np.sum(w.fte) / heads.sum()
    return float(value * c.drift * c.market * c.outsourcing * fte_share / 0.92)


def m_tokens(w: Workers, c: Context, rng) -> float:
    """T: 1 + tokens per FTE / tokens-per-AP (the v1.0 EUR/AP method)."""
    spend = w.spend * (1.0 + 2.0 * c.gaming)  # idle sessions, tokenmaxxing
    tokens = spend / EUR_PER_MTOK * 1e6 * c.token_intensity
    return float(1.0 + np.sum(tokens) / np.sum(w.fte) / V1_TOKENS_PER_AP)


def m_deliverable_count(w: Workers, c: Context, rng) -> float:
    """D: deliverables per FTE now / baseline, no quality check."""
    wt = _fte_weights(w)
    volume = np.sum(wt * w.volume) / np.sum(wt)
    split = 1.0 + c.gaming * rng.uniform(0.2, 0.6)
    return float(volume * c.drift * rng.lognormal(0, 0.08) * split)


def m_task_capacity(
    w: Workers, c: Context, rng, n_workers: int = 12, tasks_each: int = 5
) -> float:
    """C: task-based capacity AP (Amdahl) from timed task samples.

    Samples workers, times a few tasks each (drawn by time share), computes a
    capacity per worker and aggregates as a ratio of totals.
    """
    wt = _fte_weights(w)
    who = rng.choice(wt.size, size=n_workers, replace=False, p=wt / wt.sum())
    caps = np.empty(n_workers)
    for j, i in enumerate(who):
        k = rng.choice(w.time_shares.shape[1], size=tasks_each, p=w.time_shares[i])
        t = w.task_time[i, k] * rng.lognormal(0.0, 0.30, tasks_each)
        caps[j] = 1.0 / t.mean()
    caps = caps * (1.0 + 0.08 * c.gaming)  # slow-walked baseline timings
    return float(caps.mean())


def m_quality_adjusted(
    w: Workers, c: Context, rng, n_audit: int = 40, control: bool = True, mix_noise: float = 0.08
) -> float:
    """Q: deliverables x blind-audited value per deliverable, vs a control group.

    The audit scores value relative to a typical baseline deliverable, so
    splitting work is mostly caught; 20% of the inflation leaks through.
    """
    wt = _fte_weights(w)
    volume = np.sum(wt * w.volume) / np.sum(wt)
    quality = np.sum(wt * w.volume * w.quality) / np.sum(wt * w.volume)
    split = 1.0 + c.gaming * rng.uniform(0.2, 0.6)
    count = volume * c.drift * rng.lognormal(0, mix_noise) * split
    item_value = quality / split * (1.0 + 0.2 * (split - 1.0))
    sd = 0.25
    q_now = rng.normal(item_value, sd, n_audit).mean()
    q_base = rng.normal(1.0, sd, n_audit).mean()
    drift_hat = c.drift * rng.lognormal(0, 0.04) if control else 1.0
    return float(count * q_now / q_base / drift_hat)


METHODS = {
    "S self-estimate (v1 calculator)": m_self_estimate,
    "R revenue per head (v1 table)": m_revenue_per_head,
    "T token conversion (v1 EUR/AP)": m_tokens,
    "D deliverable count": m_deliverable_count,
    "C task capacity (AP-C)": m_task_capacity,
    "Q quality-adjusted, no control": lambda w, c, r: m_quality_adjusted(w, c, r, control=False),
    "Q quality-adjusted + control, 40 audits": m_quality_adjusted,
    "Q spec protocol (AP-Q)": lambda w, c, r: m_quality_adjusted(w, c, r, n_audit=80, mix_noise=0.04),
}
