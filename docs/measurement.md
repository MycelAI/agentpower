<!--
SPDX-FileCopyrightText: 2026 Alphin Tom / Mycel UG (haftungsbeschränkt)

SPDX-License-Identifier: CC-BY-SA-4.0
-->

# Measuring Agentpower: Protocol

Specification 2.0 · the procedure behind AP-Q and AP-C in [definition.md](definition.md).

This takes a team of 10–100 people about two working weeks the first time and two to three days per repeat. The numbers in brackets refer to the simulation experiments in [simulation.md](simulation.md).

---

## Step 1. Fix the role and the deliverables

Pick one role (claims handlers, contract lawyers, backend engineers). List the deliverables that make up most of its value: closed claims, reviewed contracts, merged changes, finished analyses.

Give each deliverable type an **effort weight**: the typical baseline hours it took before AI. A complex contract might weigh 6, a standard NDA 0.5. Effort weighting absorbs shifts in deliverable mix and cuts AP-Q's error from ±16% to ±12% at the same audit size (E7).

## Step 2. Fix the baseline and the control

Best to worst:

1. **Contemporaneous control.** A comparable team, site or rota without the AI change over the same period. This removes background drift: other tools, learning, demand. Without it, AP-Q overstates the gain by about 35% (E1).
2. **Staggered rollout.** Teams adopting at different dates act as each other's controls.
3. **Pre-period only.** Your own team before the change. Allowed, reported as AP-Q*, and widen your interpretation accordingly.

## Step 3. Count FTE and output

For the baseline period and the current period, record:

- contracted FTE in the role (not headcount, never including contractors on one side only),
- the number of each deliverable type, multiplied by its effort weight and summed: this is **V**.

## Step 4. Audit value

Draw **at least 80** deliverables at random from each period (40 is the minimum; below that the interval is wider than most real effects; E7).

- Reviewers score each one for value relative to a typical baseline deliverable of the same type (1.0 = typical). Include correctness, completeness and rework caused downstream.
- Reviewers are blind to the period and to whether AI was used. Strip dates and tool traces.
- A deliverable that was split into several smaller ones scores lower each. This is what keeps AP-Q resistant to gaming (+8% when gamed, against +40% for raw counts; E1).

The mean scores are **q_base** and **q_now**.

## Step 5. Compute AP-Q with an interval

```python
from agentpower import quality_adjusted_ap

est = quality_adjusted_ap(
    count_now=1830, count_base=1410,          # effort-weighted V
    quality_now=scores_now, quality_base=scores_base,
    fte_now=21.5, fte_base=22.0,
    control_drift=1.04,                         # control team's own change
)
print(est)  # with equal audit means and 80 scores (sd 0.25) per period: ~1.28 [90% CI 1.19-1.37]
```

The interval is a percentile bootstrap over the audit scores. It does not include deliverable-mix noise, so treat it as a lower bound on uncertainty.

## Step 6. Measure AP-C

1. List the role's task types and their share of baseline time (`w_i`). A two-week time diary from 5–10 people is enough.
2. Time a sample of real tasks with and without AI. 12 people × 5 tasks gives AP-C to within about ±10% (E1). Include the time spent checking and fixing AI output in the AI-assisted time.
3. Compute `S_i = baseline time / AI time` per task type and `AP-C = 1 / Σ w_i / S_i`.

```
agentpower estimate examples/tasks.csv --realised 1.27 --cost 2400
```

## Step 7. Read the pair

| AP-Q | AP-C | Absorption | Reading |
|---|---|---|---|
| ≈ 1 | ≈ 1 | – | No effect yet. Adoption or exposure is the constraint (E6: these two move AP most). |
| ≈ 1 | > 1.2 | low | Time is being saved but not turned into value. Look at demand, review queues, coordination. |
| > 1.2 | > 1.2 | high | Real amplification. Protect quality and watch for deskilling. |
| > AP-C | – | > 100% | Usually quality gains, or a measurement problem. Check the audit. |

## Do not

- **Do not use self-estimates as AP.** Managers asked "how many people would you need without AI?" overstate the gain by a factor of 3.4 (E1). In the METR 2025 trial developers believed they were 20% faster while measuring 19% slower.
- **Do not use revenue per employee.** It moves with prices, demand and outsourcing. Rank correlation with true AP: 0.26 (E1).
- **Do not use token consumption.** Tokens per unit of work vary by two orders of magnitude between models and working styles. The 1.0 conversion overstated gains more than a hundredfold, and almost tripled once it became a leaderboard (E1; the Meta "Claudeonomics" episode, April 2026).
- **Do not count heads.** Use FTE in a ratio of totals. Headcount adds up to ±7% error when the part-time share moves (E2). Averaging individual ratios is a smaller error in the simulation (+0.3%) but has no upside.
