# SPDX-FileCopyrightText: 2026 Alphin Tom / Mycel UG (haftungsbeschränkt)
#
# SPDX-License-Identifier: MIT

"""Synthetic world for the Agentpower simulations.

A worker splits baseline time across task types. On each task AI may be
used; inside the "jagged frontier" it saves time (net of review) and can
raise quality, outside it costs time and quality. Freed time only becomes
output to the extent it is reallocated to productive work. Every parameter
is a scenario assumption, calibrated in docs/evidence.md and varied in the
sensitivity experiment.
"""

from __future__ import annotations

from dataclasses import dataclass, replace

import numpy as np

N_TASKS = 10


@dataclass(frozen=True)
class Scenario:
    name: str
    exposure: float  # mean share of a task's time AI can address
    adoption: float  # mean probability AI is actually used on a task
    saving: float  # mean time saving on the exposed part when it works
    frontier_miss: float  # probability a use falls outside the frontier
    miss_time: float  # extra time on the exposed part after a miss
    miss_quality: float  # quality loss on the task after a miss
    quality_gain: float  # quality gain on the task inside the frontier
    review: float  # share of the saved time spent checking AI output
    reallocation: float  # mean share of freed time turned into output
    spend_eur: float  # annual AI spend per FTE (seats + tokens)
    conc: float = 6.0  # Beta concentration: lower means more heterogeneity

    def with_(self, **kw) -> "Scenario":
        return replace(self, **kw)


# Calibrated to the evidence in docs/evidence.md (October 2026).
SCENARIOS: dict[str, Scenario] = {
    "typical-2026": Scenario(
        "typical-2026", exposure=0.45, adoption=0.40, saving=0.45, frontier_miss=0.15,
        miss_time=0.25, miss_quality=0.15, quality_gain=0.05, review=0.30,
        reallocation=0.50, spend_eur=360,
    ),
    "integrated-team": Scenario(
        "integrated-team", exposure=0.60, adoption=0.65, saving=0.60, frontier_miss=0.12,
        miss_time=0.20, miss_quality=0.12, quality_gain=0.06, review=0.25,
        reallocation=0.70, spend_eur=2400,
    ),
    "agentic-frontier": Scenario(
        "agentic-frontier", exposure=0.80, adoption=0.90, saving=0.85, frontier_miss=0.10,
        miss_time=0.30, miss_quality=0.10, quality_gain=0.05, review=0.15,
        reallocation=0.85, spend_eur=12000,
    ),
}

# Not calibrated: what it would take to reach the AP 3-10 claimed in v1.0.
SPECULATIVE = Scenario(
    "speculative-delegation", exposure=0.92, adoption=0.97, saving=0.95, frontier_miss=0.04,
    miss_time=0.30, miss_quality=0.08, quality_gain=0.05, review=0.08,
    reallocation=0.95, spend_eur=40000, conc=20.0,
)


def beta(rng: np.random.Generator, mean, conc: float, size) -> np.ndarray:
    mean = np.clip(mean, 1e-3, 1 - 1e-3)
    return rng.beta(mean * conc, (1 - mean) * conc, size=size)


@dataclass
class Workers:
    """Per-worker truth for one simulated population."""

    time_shares: np.ndarray  # (n, K)
    task_time: np.ndarray  # (n, K) AI-era time per unit, baseline = 1
    task_quality: np.ndarray  # (n, K) quality multiplier per task
    assisted: np.ndarray  # (n, K) bool
    capacity: np.ndarray  # (n,) Amdahl capacity AP
    volume: np.ndarray  # (n,) realised volume multiplier
    quality: np.ndarray  # (n,) quality multiplier
    ap: np.ndarray  # (n,) true quality-adjusted AP
    fte: np.ndarray  # (n,) contracted FTE
    base_output: np.ndarray  # (n,) baseline output per FTE (role heterogeneity)
    adoption: np.ndarray  # (n,)
    spend: np.ndarray  # (n,) actual AI spend, EUR/year

    @property
    def org_ap(self) -> float:
        w = self.fte * self.base_output
        return float(np.sum(w * self.ap) / np.sum(w))

    @property
    def org_volume(self) -> float:
        w = self.fte * self.base_output
        return float(np.sum(w * self.volume) / np.sum(w))

    @property
    def org_capacity(self) -> float:
        w = self.fte * self.base_output
        return float(np.sum(w * self.capacity) / np.sum(w))


def simulate_workers(s: Scenario, n: int, rng: np.random.Generator) -> Workers:
    k = N_TASKS
    shares = rng.dirichlet(np.full(k, 1.2), size=n)
    exposure = beta(rng, s.exposure, s.conc, (n, k))
    adoption = beta(rng, s.adoption, s.conc, n)
    assisted = rng.random((n, k)) < adoption[:, None]
    base_output = rng.lognormal(0.0, 0.3, n)
    # Skill compression: lower-output workers gain more (Brynjolfsson et al. 2025, Cui et al.).
    saving = np.clip(beta(rng, s.saving, s.conc, (n, k)) * base_output[:, None] ** -0.35, 0.0, 0.97)
    miss = rng.random((n, k)) < s.frontier_miss

    hit_delta = saving * (1.0 - s.review)  # net time saved on the exposed part
    delta = np.where(miss, -s.miss_time, hit_delta)
    task_time = 1.0 - assisted * exposure * delta
    q_delta = np.where(miss, -s.miss_quality, s.quality_gain)
    task_quality = 1.0 + assisted * exposure * q_delta

    capacity = 1.0 / np.sum(shares * task_time, axis=1)
    realloc = beta(rng, s.reallocation, s.conc, n)
    # Freed time is partly absorbed; lost time always costs output.
    volume = np.where(capacity >= 1.0, 1.0 + realloc * (capacity - 1.0), capacity)
    quality = np.sum(shares * task_time * task_quality, axis=1) / np.sum(shares * task_time, axis=1)
    ap = volume * quality

    fte = np.where(rng.random(n) < 0.8, 1.0, rng.uniform(0.5, 0.9, n))
    spend = s.spend_eur * adoption / max(s.adoption, 1e-6) * rng.lognormal(-0.5, 1.0, n)
    return Workers(shares, task_time, task_quality, assisted, capacity, volume, quality, ap,
                   fte, base_output, adoption, spend)


def draw_org_scenario(rng: np.random.Generator) -> Scenario:
    """A random organisation spanning the 2026 range of AI maturity."""
    t = rng.random()
    lo, mid, hi = (SCENARIOS[k] for k in ("typical-2026", "integrated-team", "agentic-frontier"))
    a, b = (lo, mid) if t < 0.75 else (mid, hi)
    u = rng.random() if t < 0.75 else rng.random() ** 2
    fields = ("exposure", "adoption", "saving", "frontier_miss", "miss_time", "miss_quality",
              "quality_gain", "review", "reallocation", "spend_eur")
    mix = {f: getattr(a, f) + u * (getattr(b, f) - getattr(a, f)) for f in fields}
    return Scenario("org", **mix)
