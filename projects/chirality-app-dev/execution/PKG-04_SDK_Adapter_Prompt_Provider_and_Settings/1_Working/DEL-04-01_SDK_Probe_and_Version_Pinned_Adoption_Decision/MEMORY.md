# MEMORY - DEL-04-01

## Decisions And Evidence

- 2026-06-16 - Human project authority advanced this deliverable lifecycle from SEMANTIC_READY to IN_PROGRESS because active code implementation is underway. This does not imply CHECKING, ISSUED, release readiness, dependency satisfaction, professional approval, certification, sealing, authentication, or code-compliance acceptance.
- 2026-05-24 - Added `@anthropic-ai/claude-agent-sdk@0.3.150` as the pinned first-adapter probe dependency.
- 2026-05-24 - Upgraded direct `@anthropic-ai/sdk` to `0.93.0` to satisfy the Claude Agent SDK peer dependency while keeping the existing direct adapter selectable.
- 2026-05-24 - Added opt-in SDK provider mode `CHIRALITY_HARNESS_PROVIDER=agentSdk`; default provider behavior remains unchanged.
- 2026-05-24 - SDK options builder defaults to `settingSources: []`, exposes no built-in tools for CODEV-001, and accepts only explicit `CHIRALITY_SDK_SETTING_SOURCES=project` as a development override.
- 2026-05-24 - first-adapter probe evidence recorded in `Evidence_CODEV-001_SDK_Probe_Record.md`.
- 2026-05-24 - Dependency closure assessment set `DEP-04-01-008` to `SATISFIED`; follow-up DepClosure blocker-subset scan is acyclic.

## Open Items

- Claude Code subprocess version remains `BLOCKED_TBD` pending live SDK init event.
- Live SDK session/resume behavior remains partially evidenced by metadata fields and tests, but requires controlled probe.
- Interrupt/cancel subprocess behavior remains partially evidenced by adapter control calls, but requires controlled probe.
- Electron packaging result remains `BLOCKED_TBD`.
- Adoption verdict remains `BLOCKED_TBD`; this tranche does not decide `ADOPT`, `ADOPT_WITH_RESIDUAL_RISK`, or `FALLBACK`.
- REF-006 `docs/PRD.md` hash mismatch remains a closure caveat.
- Strict all-active FULL_GRAPH closure remains open outside this deliverable.

## Dependency Note

`DEP-04-01-008` is now `SATISFIED`. No rows were waived, retired, or marked not applicable.
