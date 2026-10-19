<!--
SPDX-FileCopyrightText: 2026 Alphin Tom / Mycel UG (haftungsbeschränkt)

SPDX-License-Identifier: CC-BY-SA-4.0
-->

# AP Worksheet

A one-page version of the [measurement protocol](../docs/measurement.md) for a single role. It works on paper or in a spreadsheet; the same arithmetic is in `agentpower estimate`.

---

## Part A. Capacity (AP-C): what could the role produce?

List the role's main task types, the share of baseline working time each took, and the time per task with and without AI. AI time includes checking and fixing the output.

| Task type | Time share `w` | Baseline hours | AI hours | Speed-up `S = base / AI` | `w / S` |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| **Total** | **1.00** | | | | **Σ = ____** |

```
AP-C = 1 / Σ(w / S) = ____
```

Worked example (a contracts team, [tasks.csv](tasks.csv)):

| Task type | w | Base h | AI h | S | w / S |
|---|---|---|---|---|---|
| First drafts of client letters | 0.20 | 1.5 | 0.6 | 2.50 | 0.080 |
| Contract clause review | 0.25 | 3.0 | 2.1 | 1.43 | 0.175 |
| Research and precedent search | 0.15 | 2.0 | 1.1 | 1.82 | 0.083 |
| Client calls and meetings | 0.20 | 1.0 | 1.0 | 1.00 | 0.200 |
| Internal coordination | 0.10 | 1.0 | 0.95 | 1.05 | 0.095 |
| Final sign-off and filing | 0.10 | 0.5 | 0.5 | 1.00 | 0.100 |
| **Total** | 1.00 | | | | **0.733** |

AP-C = 1 / 0.733 = **1.37**. Drafting got 2.5× faster, yet the role as a whole is capped at 1.37×, because half the time sits in tasks AI barely touches.

## Part B. Realised (AP-Q): what did it deliver?

| | Baseline period | Current period |
|---|---|---|
| FTE in the role | | |
| Effort-weighted deliverables `V` | | |
| Mean audit score `q` (≥ 40, ideally 80 blind-reviewed items) | | |
| Control group's change in output per FTE `D` | — | |

```
AP-Q = (V_now / FTE_now) / (V_base / FTE_base) × (q_now / q_base) / D = ____
```

No control group? Set D = 1 and write the result as **AP-Q\***. Expect it to overstate the gain.

## Part C. Read the pair

```
Absorption = (AP-Q − 1) / (AP-C − 1) = ____
```

In the example, a measured AP-Q of 1.12 gives absorption of 33%: two thirds of the saved time is not becoming delivered value. That points to demand, review queues or coordination rather than to the tools.

## Part D. Cost of the next AP

```
Added AI cost per FTE per year (spend + enablement):   € ____
Cost per extra AP = added cost / (AP-Q − 1):            € ____
Fully loaded cost of one hire:                          € ____
```

Example: €2,400 spend, AP-Q 1.12 → €20,000 per extra AP, against roughly €85,000 for a hire in Germany.

---

## Notes

- **Don't skip Part B.** Asking "how many people would we need without AI?" is not a measurement; in simulation it overstates the gain more than threefold.
- **Quality is measured, not assumed.** A split deliverable scores lower in the audit; that is what keeps the number honest.
- **Revisit twice a year.** Capabilities and prices move fast. Your baseline does not, so keep a control group if you can.

*From the [Agentpower](https://github.com/MycelAI/agentpower) project by Mycel UG.*
