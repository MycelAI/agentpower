# Agentpower: Formal Definition

Version 1.0 · April 2026

---

## Definition

**Agentpower (AP)** is a unit of cognitive work output.

> **1 AP = the total cognitive output of one knowledge worker, working full-time for one year, without AI assistance.**

## Core Properties

### What it measures
The combined cognitive output of a human-AI system. Not the AI's contribution alone. Not the human's contribution alone. The system output.

### What it benchmarks against
The unaided human baseline. 1 AP is the work one person produces without AI tools: the contracts drafted, the analyses completed, the decisions made, the reports written, the patients seen, the designs reviewed, the problems solved.

### What it does not measure
- Token consumption (input metric, not output metric)
- Revenue per employee (conflates pricing, market conditions, and productivity)
- Hours worked (measures time, not output)

## The AP Ratio

```
AP Ratio = Total Cognitive Output ÷ Human Headcount
```

The AP Ratio measures the average amplification factor across a team, department, or organisation.

### Interpretation

| AP Ratio | Stage | Description |
|----------|-------|-------------|
| 1.0 | Baseline | No AI amplification. Pre-2023 norm. |
| 1.5–2.0 | Early | Selective AI use for routine tasks. |
| 2.0–3.0 | Adopted | Systematic AI integration. Workflow changes beginning. |
| 3.0–5.0 | Integrated | AI embedded across most knowledge work. Roles redesigned. |
| 5.0–8.0 | Advanced | Deep human-AI collaboration. Significant workflow redesign. |
| 8.0+ | Expert | Skilled operators with full AI stack. Uncommon in 2026. |

## The Production Function

Classical knowledge-work production function:

```
Y = f(L)
```

Where Y is output and L is labour (headcount).

AI-augmented production function:

```
Y = f(L × T)
```

Where T is token fuel expenditure, directed by human judgement.

The key insight: the relationship between L and T is multiplicative, not additive. Tokens without human direction produce noise. Humans without tokens produce at baseline. The product of the two is where the amplification occurs.

## Cost Structure

```
Cost of 1 AP (old model):  1 full-time salary
                           EU median: ~€48,000 gross / ~€62,000 total employer cost/year

Cost of 1 AP (new model):  Fraction of salary + token fuel
                           Marginal AP cost: €16–€560/year in tokens depending on model tier
                           (Standard Cognitive Workday: 200K tokens/day × 250 working days)
                           (at April 2026 published API pricing, converted at €1 = $1.09)
```

The first AP still costs a salary — you need the human operator. Each additional AP costs only tokens. This is the structural economic shift.

See the [EUR/AP pricing table](index.html) for the full per-model breakdown and methodology.

## Scope

Agentpower applies to **cognitive work**: any professional activity where the primary output is produced by thinking, analysing, writing, communicating, calculating, diagnosing, designing, advising, or deciding.

It does not directly apply to physical labour, though the framework could be extended as AI-driven robotics matures.

## Limitations

1. **Cognitive output is hard to measure.** Unlike horsepower, which maps to a precise physical quantity (33,000 foot-pounds per minute), cognitive output varies by profession and context. The AP framework is directional, not exact.

2. **Quality matters.** 5 AP of mediocre output is worth less than 2 AP of excellent output. The framework assumes that AI-augmented output meets or exceeds baseline quality, which requires competent human oversight.

3. **Not all tasks amplify equally.** Routine, structured tasks (drafting, summarising, data processing) amplify more readily than novel, creative, or interpersonal tasks. An organisation's achievable AP ratio depends on its task mix.

4. **Token costs are falling.** The economics described here reflect 2026 pricing. As token costs continue to decline, the marginal cost of additional AP will decrease further, likely accelerating adoption.

## Historical Parallel

| Attribute | Horsepower (1782) | Agentpower (2026) |
|---|---|---|
| Named after | The thing being replaced (horse) | The role being amplified (agent) |
| Measures | Mechanical work output | Cognitive work output |
| Fuel | Coal | AI tokens |
| Baseline unit | 1 horse, 1 year | 1 knowledge worker, 1 year |
| Initial multiplier | ~20× per steam engine | ~3–10× per human-AI system |
| Cost advantage | Steam at 25–30% cost of horses by 1850 | Marginal AP at ~5% cost of additional hire |
| Key insight | Measure output, not fuel burned | Measure output, not tokens consumed |

---

*Agentpower is released into the public domain. No trademark is claimed. Build on it.*
