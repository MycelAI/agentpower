<!--
SPDX-FileCopyrightText: 2026 Alphin Tom / Mycel UG (haftungsbeschränkt)

SPDX-License-Identifier: CC-BY-SA-4.0
-->

# Contributing to Agentpower

Agentpower is an open framework. The goal is adoption, not ownership. Contributions that make the concept more precise, more measurable, and more useful are welcome.

By taking part you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md). Report security problems privately as described in [SECURITY.md](SECURITY.md), not in issues.

## What We're Looking For

### Role-level baselines and audit rubrics
AP-Q needs an agreed deliverable list, effort weights and a value rubric per role. Portable versions for common roles (claims handling, contract review, software engineering, financial analysis, grant writing) are the most useful contribution right now.

### Measured cases
AP-Q and AP-C pairs from real teams, with method code, interval and baseline type as in [definition.md](docs/definition.md) §3. Anonymous is fine. Self-estimates and revenue-per-head figures are not AP measurements and will not be added as cases. Use the **Measured case** issue form.

### Evidence
New controlled or population studies on AI and knowledge-work output, especially on agentic delegation. Corrections to [evidence.md](docs/evidence.md) with sources. Use the **Evidence or correction** issue form.

### Simulation
Better calibrations, new gaming channels, alternative measurement methods to score in experiment E1. Pull requests should include the regenerated `docs/simulation-results.md`, `docs/figures/` and `results/results.json`, and keep `uv run pytest` passing.

### Translations
The term "agentpower" stays untranslated, like "horsepower".

### Critiques
Serious critiques of the assumptions. The 2.0 rebuild came from taking 1.0's weaknesses seriously; the next one will too. Use the **Critique or proposal** issue form.

## What We're Not Looking For

- Marketing content or promotional material
- Vendor-specific tool recommendations
- Content that frames AI as purely positive or purely negative (the essay deliberately holds both)

## Development setup

You need Python 3.10 or newer and [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/MycelAI/agentpower.git
cd agentpower
uv sync --extra plots
uv run pytest
```

| Task | Command |
|---|---|
| Run the tests | `uv run pytest` |
| Capacity AP from a task sheet | `uv run agentpower estimate examples/tasks.csv --realised 1.12 --cost 2400` |
| Regenerate results, report and figures (~10–20 s, fixed seed) | `uv run --extra plots agentpower simulate --report docs/simulation-results.md --figures docs/figures` |
| Check licensing metadata | `uvx --from "reuse[charset-normalizer]" reuse lint` |
| Validate `CITATION.cff` | `uvx cffconvert --validate` |
| Build the wheel and sdist | `uv build` |

Do not edit `docs/simulation-results.md`, `docs/figures/` or `results/results.json` by hand. Change the code in `src/agentpower/` and regenerate them. The run is deterministic, so the diff shows exactly what your change moved.

## How to Contribute

1. Fork the repository, or open an issue first if the change is large or changes the specification.
2. Create a branch (`feature/legal-ap-benchmark` or `critique/output-measurement`).
3. Make the change. Keep the checks above passing and add an entry under `## [Unreleased]` in [CHANGELOG.md](CHANGELOG.md).
4. Open a pull request and fill in the template.

`main` is protected: every change goes through a pull request and needs one approving review.

### Licensing of contributions

Text, figures and data contributions are licensed under CC BY-SA 4.0; code contributions under MIT. The rule is the license of the file you change; [LICENSE](LICENSE) has the full map. Only contribute material you have the right to license this way.

Every new original file starts with an SPDX header in its comment syntax, for example:

```python
# SPDX-FileCopyrightText: 2026 Your Name
#
# SPDX-License-Identifier: MIT
```

```markdown
<!--
SPDX-FileCopyrightText: 2026 Your Name

SPDX-License-Identifier: CC-BY-SA-4.0
-->
```

If you add substantial original material to a file, add your own `SPDX-FileCopyrightText` line. Files that cannot carry a comment, or that are generated, are covered in [REUSE.toml](REUSE.toml). Material copied from elsewhere keeps its original license and notice, and must be listed in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Content under licenses incompatible with the file it lands in cannot be accepted.

## Ownership and decisions

The project is maintained by Mycel UG (haftungsbeschränkt). [CODEOWNERS](.github/CODEOWNERS) lists who reviews which paths. Maintainers decide on changes to the specification (definition, measures, bands) after public discussion in an issue, and record them in the changelog.

## Versioning

The specification and the Python package share one version number under [Semantic Versioning](https://semver.org/spec/v2.0.0.html). A major version is reserved for changes that make AP figures non-comparable or break the API or CLI. The [CHANGELOG](CHANGELOG.md) explains the rule in full.

## Releases

Maintainers only. There is no hosted CI, so run every step locally.

1. On a release branch, set the version in `pyproject.toml`, `src/agentpower/__init__.py` and `CITATION.cff` (`version`, `date-released`). Then move the `[Unreleased]` changelog entries under a dated version heading and update the compare links.
2. Run the checks: `uv run pytest`, `reuse lint`, `cffconvert --validate`, and the simulation command. The simulation must give no diff unless the release intends one.
3. Build and inspect the packages: `uv build`, then confirm that the wheel and sdist contain `LICENSE`, `LICENSE-CODE` and `LICENSES/`.
4. Produce the SBOM from the lock file:
   ```bash
   uv lock
   uv export --format cyclonedx1.5 --no-dev --extra plots -o dist/agentpower-X.Y.Z.cdx.json
   ```
5. Open a pull request and merge it after review. Then tag `vX.Y.Z` on `main` and create the GitHub release, attaching the wheel, the sdist and the `.cdx.json` SBOM.

For discussions and questions, open an issue.
