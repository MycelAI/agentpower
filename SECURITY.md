<!--
SPDX-FileCopyrightText: 2026 Alphin Tom / Mycel UG (haftungsbeschränkt)

SPDX-License-Identifier: CC-BY-SA-4.0
-->

# Security Policy

## Supported versions

| Version | Supported |
|---|---|
| 2.0.x | Yes |
| 1.0 | No (specification only, no code) |

Fixes are released as a new patch version of the latest release.

## What to report here

Security issues in the `agentpower` Python package: anything that lets crafted input (a task CSV, CLI arguments, simulation parameters) run code, read or write unexpected files, or crash the tool in a way that someone could exploit. Problems with the dependency versions the package allows also belong here.

Flaws in the method itself, such as a way to game AP-Q, are not security issues. Open a [critique or proposal issue](https://github.com/MycelAI/agentpower/issues/new/choose) for those, because the specification is improved in public.

## How to report

Please do not open a public issue for a security problem.

1. **Preferred:** [report a vulnerability privately on GitHub](https://github.com/MycelAI/agentpower/security/advisories/new).
2. **Or email** [dev@mycel-ai.de](mailto:dev@mycel-ai.de) with "agentpower security" in the subject.

Include the affected version (`agentpower --version`), steps or input to reproduce, and the impact you expect. A small maintainer team handles reports on a best-effort basis. You will get an acknowledgement and updates until the issue is resolved. Credit in the advisory and the changelog is offered unless you prefer to stay anonymous.
