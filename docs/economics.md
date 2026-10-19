<!--
SPDX-FileCopyrightText: 2026 Alphin Tom / Mycel UG (haftungsbeschränkt)

SPDX-License-Identifier: CC-BY-SA-4.0
-->

# The Economics of Agentpower

Specification 2.0 · replaces the 1.0 "EUR/AP" token methodology.

---

## What 1.0 said, and why it was wrong

Version 1.0 assumed that 200,000 tokens a day for 250 working days (50 million tokens a year) would deliver one additional AP, then priced those tokens: €16 a year on a budget model, €560 on a frontier model. Five AP, it concluded, cost one salary plus €64–€2,240.

Three problems:

1. **No evidence links a token volume to an output quantity.** Tokens are fuel. How much work a million tokens does depends on the model, the task, caching, and whether an agent loop is productive or spinning. Across organisations it varies by two orders of magnitude. The Jellyfish data on engineers make the point: the top decile uses about ten times the tokens of the median for about twice the output.
2. **The volume is far too low and the price is not the constraint.** Heavy agentic users consume millions of tokens a day, mostly cache reads. Enterprise Claude Code users average about $150–250 a month. Even so, the token bill is small next to the real bottleneck, which is the human time AI cannot replace.
3. **It ignored Amdahl.** An extra AP means AI must remove half of a person's working time and the organisation must turn all of it into output (definition §5). No token budget does that on its own.

In the simulation the 1.0 conversion overstated gains 143-fold (E1).

## The 2.0 method

```
Cost per additional AP = (AI spend per FTE + enablement per FTE) / (AP-Q − 1)
```

- **AI spend**: seats, API tokens, agent platforms, per FTE per year.
- **Enablement**: training, workflow redesign, evaluation and governance time. The simulation uses €700 per FTE per year (about 40 hours of onboarding spread over three years, plus ongoing support). Change programmes often cost more.
- **AP-Q − 1**: the *measured* realised gain, not a vendor's estimate.

Review time is already inside AP-Q: time spent checking AI output is time not spent producing.

## What it comes to

From the calibrated simulation (E5):

| Scenario | AI spend per FTE per year | Median AP gain | Cost per additional AP |
|---|---|---|---|
| Typical 2026 | €360 | +0.02 | ~€45,000 (€35–60K) |
| Integrated team | €2,400 | +0.14 | ~€23,000 (€21–26K) |
| Agentic frontier | €12,000 | +0.75 | ~€17,000 (€15–19K) |
| *Hiring, for comparison* | | +1.0 | ~€85,000 |

The hiring figure is the German full-time mean salary (€62,235, Destatis 2024) plus about 21% employer social contributions and 10–15% overhead. The EU full-time adjusted mean is €39,800 (Eurostat 2024); scale accordingly.

So:

- **AI is two to five times cheaper per unit of output than hiring.** That is a structural shift and the core of the original argument survives.
- **It is not a hundred times cheaper.** The 1.0 contrast of "5 AP for one salary plus a few hundred euros" does not hold. Five AP today means five people, or two to three people in an agentic frontier team.
- **Cheap tools buy little.** At typical 2026 spend, the gain per worker is so small that the cost per AP is highest. Spending more on AI, together with the work to redesign workflows around it, is what moves a team up the curve.

## The spend curve

![Cost curve](figures/cost-curve.svg)

Along an illustrative spend-response curve, the marginal cost of an extra AP falls while AI extends into new tasks, bottoms out at about €24,000 per AP when spend reaches about €12,000 per FTE per year, then rises steeply. Past about €24,000 per FTE, further spend buys almost nothing: the remaining time sits in tasks AI does not touch. The exact curve depends on an assumption about how quickly spend opens up exposure and adoption (a half-saturation parameter in [`experiments.py`](../src/agentpower/experiments.py)). Across values from €2,000 to €15,000 per FTE, the cheapest marginal AP costs roughly €8,000 to €60,000: at least fifteen times the top of the 1.0 range.

## Prices, October 2026

For orientation only; AP does not depend on them. Per million input/output tokens, USD: Claude Opus 5.5 $4/$20, Sonnet 5.5 $2/$10, Haiku 5.5 $0.10/$0.50; OpenAI gpt-6.1-sol $2/$10, gpt-6-luna $0.10/$0.50; Gemini 3.1 Pro $2/$12, Gemini 3.8 Flash $0.75/$3.75; DeepSeek V4.1-Flash $0.30/$1.20. Cache reads cost a tenth or less of input prices. ECB reference rate 16 October 2026: $1.1253 per euro.

Token prices have fallen by more than an order of magnitude since 2023 and will keep falling. That lowers the AI-spend line in the formula. It does not move the Amdahl ceiling, which is set by how work is organised.
