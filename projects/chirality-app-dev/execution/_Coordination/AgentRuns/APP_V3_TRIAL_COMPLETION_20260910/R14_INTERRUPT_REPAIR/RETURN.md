# R14 interruption repair return

Source repair complete; native qualification pending. This is derivative implementation/test evidence against the BRIEF source basis, not accepted decomposition truth or native closure proof.

## Reproduction and correction

The controlled production composition's public user interrupt did not reach `turn/interrupt` before repair: regression failed because `interrupt-1` was absent. Existing path retired the live session, whose failure callback revoked authority and advanced the durable account epoch. The next candidate could then fail its unchanged admission comparison.

Added an optional bounded supervisor interrupt operation and private IPC forwarding. Delegated Runtime uses native interruption when available and retains force-retirement for generic supervisors without support. Codex supervisor requests interruption and waits for its existing terminal/retirement result. Session latches an early request until turn/start identifies the active turn, sends native turn/interrupt, and gives the supplier one request budget to produce its terminal. An acknowledgement alone is not terminal evidence. No arbitrary sleep or retry-until-success was added. Existing force-retire and revocation code remains unchanged.

Native terminal projection uses actual worker exit/signal evidence rather than interruption intent. A stronger public regression then exposed a second gap: delegated-engine-adapter dropped the genuine interrupted terminal and emitted only exit130, causing TurnCoordinator's correct `Engine exited without terminal failure evidence` rejection. The adapter now projects the verified interrupted event into the existing harness:event envelope before process:exit. This is limited to interruption and does not change failed-turn policy.

## Verification

- Prepatch public-composition regression failed: no native interruption request. `/tmp/r14-interrupt-repair/prepatch.log`.
- Source-resolved initial focused suites: 199 passed across delegated Runtime, supplier session/supervisor, private production composition, and private supervisor IPC. `/tmp/r14-interrupt-repair/focused-suite.log`.
- Final session safety tests: 86 passed, including early/active interruption, acknowledgement-without-terminal timeout, and provider crash. Private supervisor IPC: 17 passed, including distinct native routing, generic fallback and malformed generation denial. `/tmp/r14-interrupt-repair/safety-tests.log` (its composition failure was the subsequently repaired missing terminal projection).
- Final production composition regression passed: interrupt1 -> real interrupted terminal -> release1 -> fresh candidate2, identical accountId/accountEpoch1, no fence; then controlled candidate3 acknowledges interruption but emits no terminal -> bounded timeout -> fence3, no release3, explicit turn:error. `/tmp/r14-interrupt-repair/final-composition.log`.
- No-emit source TypeScript check passed after final edit; git diff --check passed. `/tmp/r14-interrupt-repair/typecheck-final.log`. A supplementary test-file typecheck reported two pre-existing fixture typing issues at hosted-private-composition.test.ts (untyped reason callback and optional conformance); production-source check is clean.

Tests resolve workspace package imports to source through `/tmp/r14-interrupt-repair/vitest.config.mjs`; this agent did not rebuild dist. All processes/account identities in these tests are controlled fixtures. No native supplier/provider execution or protected real account/session state access.

## Handoff

Modified: contracts/src/delegated.ts; core/src/delegated-runtime.ts and delegated-engine-adapter.ts; daemon/src/codex-session.ts, codex-supervisor.ts, supervisor-server.ts; tests/codex-session.test.ts, hosted-private-composition.test.ts, supervisor-server.test.ts. Other concurrent tranche files belong to parent/other authors. No commit.

Closure verdict: bounded implementation and focused verification complete. Remaining: independent consolidated review and full-suite integration by parent; packaging/release actions under owning scope; native interruption followed by resumed ordinary turn on the next signed candidate. Actual protocol/transport failure and timeout still fence; existing account identity/epoch comparisons are untouched. No further source writes planned by this worker.
