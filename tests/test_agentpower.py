# SPDX-FileCopyrightText: 2026 Alphin Tom / Mycel UG (haftungsbeschränkt)
#
# SPDX-License-Identifier: MIT

import math

import numpy as np
import pytest

from agentpower import (
    absorption,
    ap_ratio,
    band,
    capacity_ap,
    cost_per_ap,
    quality_adjusted_ap,
)
from agentpower.cli import main
from agentpower.experiments import e8_requirements, run_all
from agentpower.model import SCENARIOS, simulate_workers


def test_capacity_amdahl():
    assert capacity_ap([0.4, 0.3, 0.3], [2.0, 1.2, 1.0]) == pytest.approx(1 / 0.75)
    assert capacity_ap([1.0], [1.0]) == 1.0
    assert capacity_ap([0.5, 0.5], [1e9, 1.0]) == pytest.approx(2.0, rel=1e-6)  # Amdahl ceiling


def test_capacity_rejects_bad_input():
    with pytest.raises(ValueError):
        capacity_ap([0.5, 0.5], [1.0])
    with pytest.raises(ValueError):
        capacity_ap([0.5, 0.5], [0.0, 1.0])


def test_ap_ratio_uses_fte_and_control():
    assert ap_ratio(120, 10, 100, 10) == pytest.approx(1.2)
    assert ap_ratio(120, 10, 100, 10, control_drift=1.2) == pytest.approx(1.0)
    assert ap_ratio(60, 5, 100, 10) == pytest.approx(1.2)


def test_quality_adjusted_interval_contains_point():
    rng = np.random.default_rng(1)
    est = quality_adjusted_ap(1300, 1000, rng.normal(1.1, 0.2, 80), rng.normal(1.0, 0.2, 80),
                              fte_now=20, fte_base=20)
    assert est.low < est.value < est.high
    assert 1.3 < est.value < 1.6
    assert "CI" in str(est)


def test_absorption_cost_band():
    assert absorption(1.1, 1.2) == pytest.approx(0.5)
    assert math.isnan(absorption(1.1, 1.0))
    assert cost_per_ap(2400, 1.12) == pytest.approx(20000)
    assert cost_per_ap(2400, 0.99) == float("inf")
    assert band(1.0) == "Baseline"
    assert band(1.05) == "Assisted"
    assert band(1.2) == "Integrated"
    assert band(5) == "Speculative"
    assert band(0.9) == "Below baseline"


def test_model_reduces_to_baseline_without_ai():
    s = SCENARIOS["integrated-team"].with_(adoption=1e-4)
    w = simulate_workers(s, 2000, np.random.default_rng(0))
    assert w.org_ap == pytest.approx(1.0, abs=0.01)


def test_typical_scenario_matches_measured_time_savings():
    # Calibration anchor: 3-5% of hours saved economy-wide (Humlum & Vestergaard; Bick et al.).
    w = simulate_workers(SCENARIOS["typical-2026"], 20000, np.random.default_rng(0))
    assert 1.02 < w.org_capacity < 1.07


def test_amdahl_identity():
    row = next(r for r in e8_requirements() if r["ap"] == 3.0)
    assert row["time_removed_at_realloc_1.0"] == pytest.approx(2 / 3)


def test_quick_run_ranks_methods_as_documented():
    r = run_all(quick=True)
    by = {m["method"]: m for m in r["e1"]}
    spec = by["Q spec protocol (AP-Q)"]
    assert 0.8 < spec["gain_ratio"] < 1.25
    assert spec["gaming_inflation_pct"] < 15
    assert by["T token conversion (v1 EUR/AP)"]["gain_ratio"] > 20
    assert by["S self-estimate (v1 calculator)"]["gain_ratio"] > 2
    assert by["D deliverable count"]["gaming_inflation_pct"] > 25


def test_cli_estimate(tmp_path, capsys):
    f = tmp_path / "t.csv"
    f.write_text("task,time_share,baseline_hours,ai_hours\na,0.5,2,1\nb,0.5,1,1\n")
    assert main(["estimate", str(f), "--realised", "1.1", "--cost", "1000"]) == 0
    out = capsys.readouterr().out
    assert "AP-C (capacity): 1.33" in out
    assert "10,000" in out
