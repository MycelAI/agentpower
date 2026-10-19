# Agentpower: Formal Definition

Specification 2.0 · October 2026 · supersedes 1.0 (April 2026)

---

## 1. The unit

> **1 AP = the quality-adjusted output of one full-time-equivalent (FTE) year of knowledge work in a given role, at that role's productivity without generative AI.**

Three things changed from 1.0, and each closes a hole the simulation found:

- **FTE, not "a worker".** Headcount mixes part-time and full-time staff and drifts with contracting. Counting FTE removes a ±7% error (simulation E2).
- **Per role.** One AP of a tax adviser and one AP of a software engineer are not the same quantity of work, just as one horsepower of a pump and one of a winch lift different loads. AP is a ratio *within* a role; it is never summed across roles as if it were a physical quantity.
- **Quality-adjusted.** Output counts at its audited value, not its volume. 1.0 treated quality as a "precondition"; in practice it is where AI gains and losses hide (−19 pp accuracy outside the frontier in Dell'Acqua et al. 2026).

## 2. The two measures

Agentpower is reported as a pair. One tells you what happened; the other tells you why.

### AP-Q: realised agentpower (the headline)

```
AP-Q = (V_now / FTE_now) / (V_base / FTE_base) × (q_now / q_base) ÷ D_control
```

| Symbol | Meaning |
|---|---|
| V | Effort-weighted count of the role's agreed deliverables in the period |
| q | Mean blind-audit value score of a random sample of those deliverables |
| FTE | Contracted full-time equivalents who produced them |
| D_control | Productivity drift of a comparable group without the AI change over the same period (1.0 if none is available, which must be disclosed) |

AP-Q answers: *how much more value does each FTE now deliver than the same role delivered without AI?*

### AP-C: capacity agentpower (the diagnostic)

```
AP-C = 1 / Σ_i ( w_i / S_i )
```

where `w_i` is the share of baseline working time spent on task type *i* and `S_i` is the measured speed-up on that task type (baseline time ÷ AI-assisted time, including the time spent checking AI output). This is Amdahl's law applied to a job. It answers: *if all freed time became output, how far could this role go?*

### Absorption

```
Absorption = (AP-Q − 1) / (AP-C − 1)
```

The share of freed capacity that became delivered value. In the calibrated scenarios it runs from about 50% (typical 2026 organisation) to 85% (agentic frontier team). A low absorption means the bottleneck is no longer the task; it is demand, coordination, review, or the habit of spending saved time on other things.

## 3. Reporting standard

An AP figure is incomplete without its method, interval and baseline. Write it like this:

```
AP-Q 1.14 [90% CI 1.02–1.27] · DiD control · 80 audits · FY2025 vs FY2022 · role: claims handling
AP-C 1.19 · 12 workers × 5 timed tasks
```

Method codes:

| Code | Method | Status |
|---|---|---|
| AP-Q | Quality-adjusted output with control group | **Standard.** Headline figure. |
| AP-Q* | Quality-adjusted output, no control | Acceptable; flag it. Overstates gains by ~35% (E1). |
| AP-C | Task-based capacity | **Standard.** Diagnostic, never the headline. |
| AP-S | Self or manager estimate | Not an AP measurement. Overstates gains 3.4× (E1). |
| — | Revenue per employee | Not an AP measurement. Overstates gains 2.5×, rank correlation 0.26 (E1). |
| — | Token consumption | Not an AP measurement. Overstates gains >100×, +184% when gamed (E1). |

## 4. Stage bands

Calibrated to the 2026 evidence and the simulation (E3). Single-team AP-Q has a precision of about ±12% at the recommended audit size (E7), so a band is a claim only when the whole confidence interval sits inside it.

| AP | Stage | Where it is seen |
|---|---|---|
| < 0.98 | Below baseline | Real: ~15% of individual workers in a typical 2026 organisation lose time to AI (METR 2025; frontier misses). |
| 0.98–1.02 | Baseline | Within noise of no effect. |
| 1.02–1.10 | Assisted | Typical 2026 organisation: chat tools, partial adoption. Matches measured economy-wide time savings of 3–5%. |
| 1.10–1.35 | Integrated | Teams with high adoption and redesigned workflows in exposed roles. |
| 1.35–2.0 | Redesigned | Agentic frontier teams; whole tasks delegated and reviewed. |
| 2.0–4.0 | Delegated | Not yet observed organisation-wide with rigorous measurement. Requires AI to remove 50–75% of baseline time. |
| ≥ 4.0 | Speculative | Requires AI to remove over 80% of baseline time *and* the organisation to turn nearly all of it into output. |

Version 1.0 called 3–10 "typical" for adopters. No controlled study, firm panel or national statistic supports that (see [evidence.md](evidence.md)).

## 5. The production function

1.0 wrote `Y = f(L × T)`. That says an organisation with no tokens produces nothing, which contradicts its own baseline of 1.0. The corrected form is task-based:

```
Y = Σ_roles  FTE_r × b_r × A_r(T, H, M)

A_r = 1 + ρ_r · ( 1 / Σ_i w_ri / S_ri(T, H) − 1 ) × Q_r
```

| Symbol | Meaning |
|---|---|
| b_r | Baseline output per FTE in role r |
| S_ri | Speed-up on task i, a function of AI capability and spend T and of operator skill H |
| ρ_r | Reallocation: share of freed time that becomes output, set by management M and demand |
| Q_r | Quality multiplier |

With `T = 0`, every `S = 1` and `A = 1`: the baseline is recovered. Tokens enter through the speed-up on each task, with diminishing returns, and the human remains the binding constraint through the time shares that AI cannot touch. That is the honest version of the original insight: tokens multiply the work, the operator bounds it.

The identity that follows is worth memorising. To reach a given AP, AI must remove this share of baseline time (E8):

| AP | 1.25 | 1.5 | 2 | 3 | 5 | 10 |
|---|---|---|---|---|---|---|
| Time removed, all of it reused | 20% | 33% | 50% | 67% | 80% | 90% |
| Time removed, half of it reused | 33% | 50% | 67% | 80% | 89% | 95% |

## 6. Cost of agentpower

```
Cost per additional AP = Added cost per FTE (AI spend + enablement) ÷ (AP-Q − 1)
```

In the calibrated scenarios one additional AP costs **€17,000–€45,000 per year**, against about €85,000 for a fully loaded hire in Germany (E5). AI is two to five times cheaper per unit of output than hiring, which is a structural shift. It is not the 100- to 5,000-fold gap that 1.0 claimed (€16–€560), and the marginal cost rises steeply once a role approaches its Amdahl ceiling. See [economics.md](economics.md).

## 7. Scope

Agentpower applies to cognitive work: professional activity whose output is produced by analysing, writing, calculating, diagnosing, designing, advising or deciding. For roles where human presence is the product (therapy, nursing, teaching young children), it applies to the cognitive components only and should be reported for those components.

## 8. Limitations

1. **Output definitions are local.** AP-Q needs a deliverable type and an audit rubric agreed per role. Cross-organisation comparison is only as good as that agreement.
2. **Precision is limited.** One team in one period: about ±12% at 80 audits with effort-weighted counts, and no better than about ±10% however many audits (E7), because deliverable mix and baseline drift cannot be audited away. Pool teams and periods for finer claims.
3. **Baselines age.** A 2022 baseline gets harder to defend each year. A contemporaneous control group (a team, site or period without the change) is preferred.
4. **Quality audits can be gamed too.** Keep reviewers blind to period and AI use, and rotate them.
5. **Not all effects are productivity.** Deskilling (Budzyń et al. 2025), workslop and changes in job quality are real and outside this unit. Report them alongside.

## 9. Historical parallel

| | Horsepower (1783) | Agentpower (2026) |
|---|---|---|
| Defined by | Watt and Boulton, 33,000 ft·lbf/min, to sell engines to people who owned horses | An open specification, to compare human–AI systems with the unaided worker |
| Measures | Mechanical power | Quality-adjusted cognitive output per FTE |
| Fuel | Coal | Compute and tokens |
| Lesson | Measure the work, not the coal | Measure the work, not the tokens |

Watt's figure was a translation layer, and it was refined for decades after. This one will be too.

---

*The word "agentpower" and the ideas in this specification are free for anyone to use. The text is CC BY-SA 4.0; the reference code is MIT.*
