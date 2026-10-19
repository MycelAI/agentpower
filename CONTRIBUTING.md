# Contributing to Agentpower

Agentpower is an open framework. The goal is adoption, not ownership. Contributions that make the concept more precise, more measurable, and more useful are welcome.

## What We're Looking For

### Role-level baselines and audit rubrics
AP-Q needs an agreed deliverable list, effort weights and a value rubric per role. Portable versions for common roles (claims handling, contract review, software engineering, financial analysis, grant writing) are the most useful contribution right now.

### Measured cases
AP-Q and AP-C pairs from real teams, with method code, interval and baseline type as in [definition.md](docs/definition.md) §3. Anonymous is fine. Self-estimates and revenue-per-head figures are not AP measurements and will not be added as cases.

### Evidence
New controlled or population studies on AI and knowledge-work output, especially on agentic delegation. Corrections to [evidence.md](docs/evidence.md) with sources.

### Simulation
Better calibrations, new gaming channels, alternative measurement methods to score in experiment E1. Pull requests should include the regenerated `docs/simulation-results.md` and `results/results.json`, and keep `uv run pytest` passing.

### Translations
The term "agentpower" stays untranslated, like "horsepower".

### Critiques
Serious critiques of the assumptions. The 2.0 rebuild came from taking 1.0's weaknesses seriously; the next one will too.

## How to Contribute

1. Fork the repository
2. Create a branch (`feature/legal-ap-benchmark` or `critique/output-measurement`)
3. Submit a pull request with a clear description

For discussions and questions, open an issue.

## What We're Not Looking For

- Marketing content or promotional material
- Vendor-specific tool recommendations
- Content that frames AI as purely positive or purely negative (the essay deliberately holds both)

## Code of Conduct

Be constructive, be honest, be rigorous. The essay argues that the engine doesn't have a moral compass but the operator does. Same applies here.

## License

Text contributions are licensed under CC BY-SA 4.0; code contributions under MIT.
