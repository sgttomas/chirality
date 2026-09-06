# P2 REPAIR_1 fresh backcheck

RUN_STATUS: SUCCESS — both review findings closed for bounded fixture execution.
ControlSurface: MERGED (original REVIEW_P2 brief plus parent repair backcheck dispatch).
TaskProfile: NONE
TaskSkill: NONE
ScopePath: /Users/ryan/.codex/worktrees/341e/chirality/projects/chirality-runtime/execution/_Coordination/AgentRuns/RUNTIME_CONFORMANCE_RESUME_2026-09-06/IMPLEMENTATION/REVIEW_P2/REPAIR_1
ToolsUsed: zsh read/diff; python3 hash/evidence writes; Vitest with --no-cache and actual supplier disabled.
ToolPolicyCompliance: PASS
WriteAuthorization: ALLOWED_WRITE_TARGETS — new REVIEW_P2/REPAIR_1 evidence only.
Attribution: OpenAI GPT-6; exact serving model ID unavailable. Native ephemeral Agent2 role and nondelegation instruction-asserted, not mechanically enforced. No delegation.

## Finding closure

**Timeout cause — closed.** Test lines39-52 classify the actual imported RuntimeError by code ENGINE_UNAVAILABLE, status503, reason CODEX_PROTOCOL_FAILURE and exact message Codex turn timed out. The producer is the same imported RuntimeError in daemon codex-session.ts:27, and its configured turn timer at line451 emits that exact error. `fail` at lines94-104 rejects waitTurn with the same object, so this is a legitimate local actor timeout discriminator. Unrelated session rejection and a plain Error with matching message fail the pure controls. Actual timeout branches now require the classified cause and elapsed interval [configuredMs-25,10000] at test:245-248. configuredMs is 5000 for timeout scenarios; actionStartedAt precedes startTurn timer arming, so [4975,10000] is a conservative timer-consistency check, not a substitute for exact cause. No new authority is inferred from the 25ms tolerance. Timestamp evidence records the calculation. Like existing timing checks this uses wall clock; no clock-jump precision claim is made.

**Stale census — closed.** Test:174-181 reconcileFresh validates snapshot.failure absent and stale-census limitation absent, persists the entire rejected snapshot with phase, then rethrows. All lifecycle and cleanup reconciliations now use that wrapper: identity/disappearance, cleanup-before, polling, final. Any retained census failure forces failed verdict (line319), and cleanup errors continue through the remaining steps. The new pure control uses the actual DescendantTracker with injected failure after empty current census and proves both stale-empty and retained-failure recovery cannot pass. No process identity or signal authority was broadened.

## Regression and validation

Compared the repaired live test to original P2 postimage and read the exact error producer/rejection path and contracts error class. Changes are confined to timeout cause/timing evidence and census rejection/control tests. Host marker, signal attempt/denial, sibling pre/post controls, first-return identity/timing, owned group/sibling cleanup, 7-second natural sleep, interrupted no-finish and <=10s/<=60s assertions remain. No new blocking cleanup/probe defect found in this bounded backcheck. A normal or lifetime actual run may still expose supplier behavior or an observation race; passing pure controls is not actual process evidence.

All REPAIR_1 output-package hashes verified. Test SHA256 cbe619b3b1c3e4c02b630bf76b74c4be53dfc97a2794f6cf6bae1871ca2f2e0a; helper SHA256 57e3c4e09183a0cebe825ca41fb5892f3a8836c635227d27aa1d7ce526e87a81. All six source hashes identical before/after. Independent no-cache default-skip Vitest: eight passed, actual supplier profile skipped, exit0. No actual supplier/provider listener/account/oMLX/network or signal canary executed. No implementation file edited.

## Parent admission and handoff

Admit parent bounded normal then cancel-primary/cancel-child/timeout-primary/timeout-child execution against these frozen six sources and separately verified exact supplier, each in a fresh evidence directory. Require exact PROFILE_PASS_NOT_FULL_G_SBX, absent failure, empty provider/cleanup/census failures, trustworthy process snapshots, standalone and host marker evidence, sibling/sentinel controls, correct scenario terminal, sourceBefore==sourceAfter, exact supply verification and original timing/cleanup bounds. Timeout evidence additionally requires configuredTurnTimeoutMs5000, terminal.error.cause CONFIGURED_TURN_TIMEOUT, and timeoutObservedElapsedMs in[4975,10000] equal terminalReceivedAt-actionStartedAt.

Closure: review findings resolved at fixture-source level; parent actual evidence remains required. This derivative review cites original REVIEW_P2 report and P2/REPAIR_1 output package, whose accepted upstream basis remains OWNER_DIRECTION/SPEC_FAN_IN through manager BASIS.json. Original failed attempt and prior sealed review are unchanged. No public Runtime cancellation, full G-SBX/orphan proof, supplier acceptance, client/release/lifecycle or hold decision is established. No active child-owned process or cleanup responsibility remains.

Outputs: REPORT.md; CHECKS.log; SOURCE_BEFORE.json; SOURCE_AFTER.json; INPUT_PACKAGE_VERIFICATION.json; RUN_RECORD.md; OUTPUTS.json.
MISSING: actual five-profile parent evidence.
NEEDS_HUMAN_RULING: none for authorized execution.
DEPENDENCY_NOTES: parent execution and evidence fan-in; no cycle.
