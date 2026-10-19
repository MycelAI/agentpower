<!--
SPDX-FileCopyrightText: 2026 Alphin Tom / Mycel UG (haftungsbeschränkt)

SPDX-License-Identifier: CC-BY-SA-4.0
-->

# Notes for coding agents

Agentpower is a specification (Markdown in `docs/`) with a small Python reference package (`src/agentpower/`). Read [CONTRIBUTING.md](CONTRIBUTING.md) first; this file only adds what an automated contributor tends to get wrong.

## Commands

```bash
uv run pytest
uv run --extra plots agentpower simulate --report docs/simulation-results.md --figures docs/figures
uvx --from "reuse[charset-normalizer]" reuse lint
uvx cffconvert --validate
uv build
```

## Rules

- `docs/simulation-results.md`, `docs/figures/` and `results/results.json` are generated. Never edit them by hand. Regenerate them after any change under `src/agentpower/`, and commit them with the change. The run is deterministic, so an unexpected diff is a real change.
- Numbers in the docs come from `docs/evidence.md` or the simulation. Do not introduce figures without a source, and keep README, `docs/definition.md` and the CHANGELOG consistent with each other.
- Licensing: text, figures and data are CC-BY-SA-4.0; code and repository configuration are MIT. Every new original file needs an SPDX header (see CONTRIBUTING.md), or an entry in `REUSE.toml` if it cannot carry one. Do not change licenses or copyright holders without the maintainer's explicit approval.
- Version numbers live in `pyproject.toml`, `src/agentpower/__init__.py` and `CITATION.cff`, and must match. Record user-visible changes under `## [Unreleased]` in `CHANGELOG.md`.
- `main` is protected and needs a reviewed pull request. Open the PR and stop: a maintainer merges, tags and releases.
- Do not add AI attribution, co-author trailers or tool names to commit messages, pull requests or release notes.
