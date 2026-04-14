# Agentpower (AP)

**A unit of cognitive work output for the AI age.**

> **One agentpower (AP)** equals the total cognitive output of one knowledge worker, working full-time for one year, without AI assistance.

---

## Why This Exists

For 250 years, **horsepower** has been the universal unit for mechanical work output. James Watt invented it in 1782 not as a physics term, but as a translation layer: a way to help factory owners compare steam engines to the horses they already understood.

We need the same thing for cognitive work.

AI tokens are transforming the economics of knowledge work the way coal transformed the economics of physical work. But we're measuring the wrong thing. Token consumption tells you how much fuel was burned, not how much work was done. That's like measuring a factory by its coal bill.

**Agentpower** measures what matters: the total cognitive output of a human-AI system, benchmarked against what one unaided human produces.

---

## The Definition

```
Agentpower (AP)

Unit:    1 AP = the annual cognitive output of one full-time knowledge worker,
         unaided by AI.

Scope:   Measures the combined output of a human operator + AI tools,
         not the AI alone.

Baseline: A knowledge worker without AI assistance operates at 1.0 AP.
```

## The AP Ratio

```
AP Ratio = Total Cognitive Output ÷ Human Headcount
```

| AP Ratio | What It Means |
|----------|---------------|
| 1.0 | No AI amplification. Pre-2023 baseline. |
| 2.0–3.0 | Early AI adoption. Routine tasks augmented. |
| 3.0–5.0 | Systematic AI integration across workflows. |
| 5.0–8.0 | Deep human-AI collaboration. Workflow redesign. |
| 8.0–10.0+ | Expert operator with full AI stack. Rare today. |

## The Formula

The old production function:

```
Output ≈ Labour
```

The new production function:

```
Output ≈ Labour × Fuel
```

Where **Labour** is human headcount and **Fuel** is AI token expenditure directed by human judgement.

## The Economics

```
Old model:  5 AP = 5 salaries            → ~€310,000/year
New model:  5 AP = 1 salary + token fuel  → ~€62,000/year
```

The additional agentpower (AP 2 through AP N) comes from tokens. The EUR/AP methodology shows the annual token cost for one full additional AP ranges from **€16 to €560/year** depending on model tier — at the Standard Cognitive Workday (200K tokens/day, 250 working days). The human operator remains essential: they provide judgement, direction, context, and accountability. The AI provides scale.

See [EUR/AP Pricing →](docs/index.html) for the full per-model breakdown.

---

## Real-World Reference Points

| Organisation | Headcount Change | Revenue Change | Implied AP Ratio |
|---|---|---|---|
| Klarna (2022→2026) | −49% | +104% | ~3.5 |
| AI-native SaaS companies (2025) | Lean teams | €0.9M–€3.7M rev/employee | 4.0–8.0 |
| Meta top engineer (2026, per CTO) | 1 person | ~10× normal output | ~10.0 |
| Pre-AI knowledge work baseline | — | ~€138K–€276K rev/employee | 1.0 |

---

## Etymology

**Agent** from Latin *agere*: to do, to act.

The word carries a double meaning that maps precisely onto this transition:

- **Old meaning:** A person who acts on behalf of another (lawyer, broker, consultant, administrator)
- **New meaning:** An AI system that acts autonomously to complete tasks

Agentpower measures what the two produce together.

---

## Origin

The concept was introduced in the essay ["Horsepower Then, Agentpower Now"](https://medium.com/alphin-pale-blue-dot/horsepower-then-agentpower-now-5bbeffabf3ef) published in *Pale Blue Dot* on Medium in April 2026.

The core argument: AI tokens are to knowledge work what coal was to physical work — a cheap, abundant fuel that transforms the economics of production from linear (output proportional to headcount) to multiplicative (output proportional to human judgement × token fuel).

---

## How to Use This

### For organisations
Calculate your AP ratio. If it's 1.0, you're operating without amplification. Estimate what a token budget starting at €16–€112/year per knowledge worker (budget to mid-tier models) would do to your output. Even at premium frontier models, one additional full AP costs under €560/year in tokens — a fraction of a salary. That's your path to 2.0+. Use the [AP Calculator](examples/ap-calculator.md) to run the numbers.

### For policymakers
Track AP ratios across sectors and regions as a leading indicator of economic transformation. Invest in training and institutional support — the constraint is no longer access to the engine, but the ability to operate it.

### For individuals
Your value is shifting from raw output to judgement, direction, and the ability to operate AI systems effectively. A professional at 5 AP is not five times busier. They're five times more capable.

### For researchers
We need better methods for measuring cognitive output across professions. The AP framework is intentionally simple — it's a starting point, not an endpoint. Contributions toward domain-specific AP benchmarks are welcome.

---

## Project Structure

```
agentpower/
├── README.md              ← You are here
├── LICENSE                 ← CC BY-SA 4.0
├── CITATION.cff            ← How to cite this work
├── CONTRIBUTING.md         ← How to contribute
├── references.bib          ← Full BibTeX reference library (16 sources)
├── docs/
│   ├── essay.md            ← Links to Medium publication (canonical)
│   ├── definition.md       ← Formal definition and specification
│   ├── faq.md              ← Common questions and critiques
│   └── index.html          ← EUR/AP pricing methodology (interactive)
└── examples/
    └── ap-calculator.md    ← Simple worksheet for estimating AP ratio
```

---

## Citation

```bibtex
@article{tom2026agentpower,
  title     = {Horsepower Then, Agentpower Now},
  author    = {Tom, Alphin},
  journal   = {Pale Blue Dot},
  year      = {2026},
  month     = {April},
  url       = {https://medium.com/alphin-pale-blue-dot/horsepower-then-agentpower-now-5bbeffabf3ef}
}
```

---

## License

This work is licensed under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).

You are free to share, adapt, and build upon this work, including for commercial purposes, as long as you give appropriate credit and distribute your contributions under the same license.

The term "agentpower" and the AP ratio framework are released into the public domain for universal use. No trademark is claimed or intended. The goal is adoption, not ownership.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). We welcome domain-specific AP benchmarks, translations, case studies, and critiques.

---

**Agentpower** is a project of [Mycel UG](https://mycel-ai.de), Berlin.

*The engine doesn't have a moral compass. The operator does.*
