## What and why

<!-- What does this change, and which issue does it address? -->

## Type

- [ ] Specification (definition, measures, bands): does it keep existing AP figures comparable?
- [ ] Evidence or correction (sources cited)
- [ ] Code or simulation
- [ ] Documentation or project setup

## Checklist

- [ ] `uv run pytest` passes
- [ ] If code under `src/agentpower/` changed: results, report and figures regenerated with `uv run --extra plots agentpower simulate --report docs/simulation-results.md --figures docs/figures`
- [ ] `reuse lint` passes; new files carry SPDX headers or are covered in `REUSE.toml`
- [ ] Entry added under `## [Unreleased]` in `CHANGELOG.md`
- [ ] I have the right to contribute this under the license of the files it changes (CC BY-SA 4.0 for text and data, MIT for code)
