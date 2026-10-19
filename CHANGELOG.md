<!--
SPDX-FileCopyrightText: 2026 Alphin Tom / Mycel UG (haftungsbeschränkt)

SPDX-License-Identifier: CC-BY-SA-4.0
-->

# Changelog

All notable changes to the Agentpower specification and the `agentpower` Python package are recorded here. The format follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/).

The specification and the package share one version number and follow [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html): a **major** version changes the definition, the measures or the bands so that AP figures are no longer comparable, or breaks the Python API or CLI; a **minor** version adds methods, evidence or features without invalidating existing measurements; a **patch** fixes errors, wording or documentation.

## [Unreleased]

### Added
- `CODE_OF_CONDUCT.md` (Contributor Covenant 3.0), `SECURITY.md`, `THIRD_PARTY_NOTICES.md`, `AGENTS.md`, issue forms, a pull request template and `CODEOWNERS`.
- REUSE-compliant licensing: SPDX headers in every original file, full license texts in `LICENSES/`, and `REUSE.toml` for generated and data files.
- Dark-mode variants of the generated figures (`docs/figures/*-dark.svg`), with alt text, embedded through `<picture>` elements in `docs/simulation-results.md`.
- A release checklist in `CONTRIBUTING.md`, with a CycloneDX SBOM for each release.

### Changed
- `LICENSE` now states the complete project terms: which license covers which files. The licenses themselves are unchanged: CC BY-SA 4.0 for text, figures and data, MIT for code.
- The wheel and sdist ship `LICENSE`, `LICENSE-CODE` and `LICENSES/`.
- README rewritten: quickstart, requirements, limitations, figures and governance links.
- Project contact is now dev@mycel-ai.de in `CITATION.cff`, the package metadata, the Code of Conduct and the security policy.
- Figures keep their text as text (`svg.fonttype: none`) and use transparent backgrounds. Simulation numbers are unchanged.

## [2.0.0] - 2026-10-19

A rebuild of the measurement after a review of the evidence (October 2026) and a Monte Carlo study of eight candidate methods. The idea is unchanged; the numbers and the method are not.

### Breaking changes
- AP ratios computed under 1.0 (headcount counterfactual, "3–10 typical") are not comparable with 2.0 AP-Q or AP-C values.
- The 1.0 stage bands are replaced. Names that survive have new ranges: "Integrated" was 3.0–5.0 and is now 1.10–1.35.
- The token-based EUR/AP cost figures (€16–€560) are withdrawn.

### Migration from 1.x
- Re-measure rather than convert: fix the role, deliverables and baseline, then compute AP-Q with a control group and AP-C from task timings ([measurement.md](docs/measurement.md)).
- Report figures in the 2.0 format, e.g. `AP-Q 1.14 [90% CI 1.02–1.27] · DiD control · 80 audits · FY2025 vs FY2022 · role: claims handling`.
- Replace token-cost estimates with added AI cost per FTE divided by the measured AP gain ([economics.md](docs/economics.md)).
- Cite specification 2.0 (`CITATION.cff`). The 1.0 essay remains the origin of the idea, not the reference for numbers.

### Changed
- **Definition.** 1 AP is now the *quality-adjusted* output of one *FTE*-year in a *given role* without generative AI. 1.0 used "one knowledge worker", headcount and quality-as-precondition.
- **Measurement.** Two standard measures replace the headcount-counterfactual worksheet: **AP-Q** (audited output per FTE against a control group, with a confidence interval) as the headline, and **AP-C** (task-based Amdahl capacity) as the diagnostic. Their ratio is reported as **absorption**. A reporting format with method codes is defined.
- **Stage bands.** Recalibrated to the evidence: a typical 2026 organisation sits at 1.02–1.10, not 3–10. New bands: Below baseline, Baseline, Assisted, Integrated, Redesigned, Delegated, Speculative.
- **Production function.** `Y = f(L × T)` predicted zero output without tokens. Replaced by a task-based form that reduces to the baseline when AI is absent.
- **Economics.** The token-based EUR/AP method (€16–€560 per extra AP) is withdrawn. The new method divides added AI cost per FTE by the measured AP gain: €17,000–€45,000 per extra AP in the calibrated scenarios, against ~€85,000 for a hire.
- **Calculator.** Rewritten as a worksheet for AP-C, AP-Q, absorption and cost.
- **Licensing.** Text stays CC BY-SA 4.0. The new code is MIT (CC licences are not meant for software). The "public domain" wording for the term is replaced by a plain statement that the word and ideas are free to use.

### Added
- `docs/measurement.md`: step-by-step protocol.
- `docs/evidence.md`: state of research, with corrections to every 1.0 reference point.
- `docs/simulation.md` and generated `docs/simulation-results.md`, `docs/figures/`, `results/results.json`.
- `docs/economics.md`.
- Python package `agentpower` (estimators, synthetic-world model, experiments, CLI) with tests.
- `examples/tasks.csv`.

### Fixed
- Klarna: −49% headcount and +104% revenue imply 4.0, not 3.5, and cover Q4 2022 to Q4 2025, not "2022→2026". Moved out of the reference table; revenue per head is not an AP measure.
- "€62,000 EU knowledge-worker salary" is the German full-time mean; the EU mean is €39,800.
- Meta CTO quote is "5x to 10x", a self-reported anecdote; the token leaderboard was reported in April 2026, not March.
- Removed unsourced claims ("steam at 25–30% of the cost of horses by 1850", "~20× per steam engine", "marginal AP at ~5% of a hire").
- `CITATION.cff`: removed the empty `orcid` (invalid under CFF 1.2.0), updated version, date and type.
- `references.bib`: removed the reference to a non-existent `docs/references.md`; updated publication status of Brynjolfsson et al. (QJE 2025) and Dell'Acqua et al. (Organization Science 2026); added the 2024–2026 sources.

## 1.0.0 - 2026-04-14

Initial release: definition, AP ratio, production function, EUR/AP economics, FAQ and worksheet.

[Unreleased]: https://github.com/MycelAI/agentpower/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/MycelAI/agentpower/releases/tag/v2.0.0
