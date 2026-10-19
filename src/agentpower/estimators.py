"""Reference estimators for the Agentpower (AP) framework, specification v2.0.

All functions are plain numpy so they can be copied into a spreadsheet or
notebook without this package. See docs/measurement.md for the protocol.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# Stage bands (lower bound inclusive). Calibrated by the 2026 simulation,
# see docs/simulation.md, experiment E4.
BANDS: tuple[tuple[float, str], ...] = (
    (0.0, "Below baseline"),
    (0.98, "Baseline"),
    (1.02, "Assisted"),
    (1.10, "Integrated"),
    (1.35, "Redesigned"),
    (2.0, "Delegated"),
    (4.0, "Speculative"),
)


@dataclass(frozen=True)
class Estimate:
    """A point estimate with a percentile bootstrap interval."""

    value: float
    low: float
    high: float
    level: float = 0.90

    def __str__(self) -> str:
        pct = round(self.level * 100)
        return f"{self.value:.2f} [{pct}% CI {self.low:.2f}-{self.high:.2f}]"


def capacity_ap(time_shares, speedups) -> float:
    """Capacity AP (AP-C): the Amdahl bound on output per FTE.

    time_shares: share of baseline working time spent on each task type (sums to 1).
    speedups:    baseline time / AI-assisted time for each task type. 1.0 means
                 no change, values below 1.0 mean AI made the task slower.
    """
    w = np.asarray(time_shares, dtype=float)
    s = np.asarray(speedups, dtype=float)
    if w.shape != s.shape:
        raise ValueError("time_shares and speedups must have the same shape")
    if np.any(w < 0) or np.any(s <= 0):
        raise ValueError("time shares must be >= 0 and speedups > 0")
    w = w / w.sum()
    return float(1.0 / np.sum(w / s))


def ap_ratio(output_now, fte_now, output_base, fte_base, control_drift: float = 1.0) -> float:
    """Realised AP ratio as a ratio of totals.

    Output per FTE now over output per FTE in the baseline, divided by the
    productivity drift of a comparable group without the AI change
    (difference-in-differences). Use FTE, never headcount.
    """
    if min(fte_now, fte_base, output_base) <= 0 or control_drift <= 0:
        raise ValueError("FTE, baseline output and control drift must be positive")
    return float((output_now / fte_now) / (output_base / fte_base) / control_drift)


def quality_adjusted_ap(
    count_now: float,
    count_base: float,
    quality_now,
    quality_base,
    fte_now: float,
    fte_base: float,
    control_drift: float = 1.0,
    n_boot: int = 4000,
    level: float = 0.90,
    seed: int | None = 0,
) -> Estimate:
    """Quality-adjusted realised AP (AP-Q), the headline measure.

    count_*:   number of deliverables of the agreed type in each period.
    quality_*: blind-review value scores for a random sample of deliverables
               from each period (same rubric, reviewers blind to period and
               AI use). A score is value relative to a typical baseline
               deliverable, so splitting work into smaller pieces lowers it.
    """
    qn = np.asarray(quality_now, dtype=float)
    qb = np.asarray(quality_base, dtype=float)
    if qn.size < 2 or qb.size < 2:
        raise ValueError("need at least two audited deliverables per period")
    volume = ap_ratio(count_now, fte_now, count_base, fte_base, control_drift)
    point = volume * qn.mean() / qb.mean()
    rng = np.random.default_rng(seed)
    bn = rng.choice(qn, size=(n_boot, qn.size)).mean(axis=1)
    bb = rng.choice(qb, size=(n_boot, qb.size)).mean(axis=1)
    boots = volume * bn / bb
    alpha = (1.0 - level) / 2.0
    lo, hi = np.quantile(boots, [alpha, 1.0 - alpha])
    return Estimate(float(point), float(lo), float(hi), level)


def absorption(realised_ap: float, capacity: float) -> float:
    """Share of the capacity gain that shows up as realised output."""
    if capacity == 1.0:
        return float("nan")
    return float((realised_ap - 1.0) / (capacity - 1.0))


def cost_per_ap(added_cost_per_fte: float, ap: float) -> float:
    """Annual cost of one additional AP: added cost per FTE / AP gained per FTE."""
    gain = ap - 1.0
    return float("inf") if gain <= 0 else float(added_cost_per_fte / gain)


def band(ap: float) -> str:
    """Stage label for an AP ratio."""
    label = BANDS[0][1]
    for lower, name in BANDS:
        if ap >= lower:
            label = name
    return label
