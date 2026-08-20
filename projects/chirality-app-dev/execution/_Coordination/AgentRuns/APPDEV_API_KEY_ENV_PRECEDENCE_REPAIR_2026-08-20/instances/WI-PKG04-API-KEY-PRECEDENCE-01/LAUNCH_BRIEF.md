# WI-PKG04-API-KEY-PRECEDENCE-01 — activation brief

- RequestedBy: `HELP_HUMAN`
- RunID: `APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20`
- InstanceID: `WI-PKG04-API-KEY-PRECEDENCE-01`
- Role: `WORKING_ITEMS` Agent 1
- PackageID: `PKG-04`
- DeliverableIDs: `DEL-04-05`
- Branch: `codex/app-api-key-precedence-20260820`
- AcceptedBasis: `6710ee6354debc201f6a454e2802897026cd4b38` (PR #586 head)
- Objective: repair the Electron Anthropic credential fallback to UI
  safeStorage, then `ANTHROPIC_API_KEY`, then
  `CHIRALITY_ANTHROPIC_API_KEY`; replace the expected-failure with positive
  regression coverage; validate and truthfully calibrate DEL-04-05 evidence.
- Dependencies: none; this is N1 and gates N2.
- WriteOwnership: the two N1 product/test files, DEL-04-05 evidence/state, and
  this instance's run-local control records.
- Exclusions: provider or network expansion; storage, persistence, error, or
  public-contract changes; dependency/lock changes; lifecycle transition;
  Checking Approval SHA mutation; shared receipt/completion-log/fan-in writes;
  Git commit, push, or PR operations.
- ReturnContract: terminal validated handoff naming changed bytes, exact
  checks, review verdict, DEL-04-05 calibration, blockers, reruns, derivative
  status, and release posture for N2.
- SelectionAuthority: `HUMAN+AGENT_0`
- Posture: serialized N1 implementation followed by fresh read-only review.
- ModelAttribution: OpenAI Codex; exact model build not exposed.

APP-HOLD dispatch preflight at `2026-08-20T15:10:03Z`: `ALLOW` for
`DEL-04-05`; active/scanned held sets empty; register SHA-256
`e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f`;
scan fingerprint
`8df9d9bd5151935d593ea5e6b51393aa31ed29d036dd15d9c1be476115d83c66`.
