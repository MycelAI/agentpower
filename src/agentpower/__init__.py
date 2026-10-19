# SPDX-FileCopyrightText: 2026 Alphin Tom / Mycel UG (haftungsbeschränkt)
#
# SPDX-License-Identifier: MIT

"""Agentpower (AP): reference estimators and simulation, specification v2.0."""

from .estimators import (
    BANDS,
    Estimate,
    absorption,
    ap_ratio,
    band,
    capacity_ap,
    cost_per_ap,
    quality_adjusted_ap,
)

__version__ = "2.0.0"

__all__ = [
    "BANDS",
    "Estimate",
    "absorption",
    "ap_ratio",
    "band",
    "capacity_ap",
    "cost_per_ap",
    "quality_adjusted_ap",
]
