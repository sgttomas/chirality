# Fresh P4 role review

RUN_STATUS: SUCCESS (review completed; fixture admission blocked)
ControlSurface: MERGED; TaskProfile: NONE; TaskSkill: NONE.
ScopePath: /Users/ryan/.codex/worktrees/341e/chirality/projects/chirality-runtime/execution/_Coordination/AgentRuns/RUNTIME_CONFORMANCE_RESUME_2026-09-06/IMPLEMENTATION/REVIEW_P4
Attribution: OpenAI GPT-6; exact serving model ID unavailable. Fresh ephemeral Agent2; role and nondelegation instruction-asserted. No delegation.

## Verdict

DO NOT ADMIT frozen role fixture `9b200f51b63a45fae6d3057ecda9ea41fe7f4e19ae1cfaae15b79ef30c258ea0` for parent Candidate1 role execution. Two blocking fixture defects remain. The changing network fixture is excluded.

## P4-R1 — controlled supervisor cannot pass public hosted preflight

The fixture creates `CodexSupervisor.controlledForTests` then binds it as `provider-observed` (exact-role-conformance.test.ts:177), forwarding `verifyHostedBoundary` through SupervisorClient (line171). `grantDelegatedConsent` requires preflight before actual role turns. The private broker forwards to the controlled supervisor, which unconditionally rejects controlled launchers (`codex-supervisor.ts:99`); `delegated-runtime.ts:73-74` reports `Verified hosted worker, account continuity or operator provider consent is unavailable`.

REPRO.mjs.source exercises the actual compiled supervisor and DelegatedRuntime with the same composition without sockets or supplier launches. REPRO.json confirms rejection and zero launches. The corrected compatibility identity clears only the previous historical failure. The current pure test stubs successful hosted verification, so it misses this integration defect.

The existing `controlled-worker` seam may lawfully calibrate a test composition while leaving production hosted/account/supply/conformance gates intact. Switching that enum alone will not work: `delegated-runtime.ts:356` sends raw prompt for controlled-worker, while the fixture wrapper JSON-parses input and needs real role envelope/evidence equality. The author must resolve test transport explicitly and accurately limit claims. Do not install a no-op hosted verifier or weaken production verification. Preserve an independent actual controlled-supervisor hosted rejection regression.

## P4-R2 — missing source pin fails outside cleanup/evidence guard

Line65 pins `packages/client/dist/client.js`, which does not exist in this checkout. The actual client build is `packages/client/dist/src/client.js`. `sourcesBefore = await pins()` at line67 executes after creating the temporary root and before the try/finally (line75). Therefore this frozen exact fixture would first fail ENOENT, leave its owned temporary directory, and omit EXACT_ROLE_CANARY.json. Correct the resolved module pin and put fallible source/evidence setup inside the cleanup/reporting guard. Pure default-skip and noEmit do not execute this code.

## Other checks

The corrected root-runtime-1 grammar and explicitly test-only digest are appropriate fixture metadata; neither asserts accepted production authority. Production preflight validation is unchanged. Historical ROLE_1 actual evidence retains invalid compatibility failure with zero processes and model requests.

Five public roles, broker envelope equality, durable retirement identity/policy binding, retirement thread ID, forged mechanical-label rejection, namespace discovery and lineage corroboration are present. Native-role conclusions are scoped to the tested composition; role/nondelegation enforcement stays instruction-asserted. Native and declared role policy digests remain distinct. No model-obedience or owner-live proof is claimed.

Read probes require standalone allowed/denied markers and unchanged synthetic sentinels; repeated history does not double count an issued read. Scratch-only execution of the exact shell command produced the expected markers; no shell escaping defect was found. The scratch negative path was absent only to check command encoding, not to claim containment.

Default-skip Vitest: 3 passed, 1 actual test skipped. Targeted noEmit TypeScript: exit0. No supplier, account, user server or network activity. The fixture encodes 10-second read/probe pass budgets and 60-second profile pass budget, source pins, cleanup and failure fields; those exact-run controls remain unverified while setup/preflight blocks. SOURCE_HASHES.json pins selected reviewed source and compiled dependencies, not complete runtime dependency closure.

## Handoff

Accepted upstream: manager BASIS.json and PLAN.md, predecessor accepted SPEC_FAN_IN and owner amendments routed by sealed brief. This is derivative review evidence, not decomposition authority or acceptance. Closure: review complete with P4-R1 and P4-R2 OPEN; implementation/actual conformance remains OPEN. Rerun: author repairs and freezes fixture, fresh bounded review, then parent separately verified Candidate1 role run. No supplier acceptance, release, hold, lifecycle or governed pointer update follows.

ToolsUsed: functions exec/exec_command (read-only Git, Python3, Node pure repro, Vitest default-skip, TypeScript noEmit); parent messages.
ToolPolicyCompliance: PASS. WriteAuthorization: ALLOWED_WRITE_TARGETS.
Outputs: REPORT.md, SOURCE_HASHES.json, CHECKS.json, REPRO.json, REPRO.mjs.source.
MISSING: repaired composition and source/evidence guard; actual parent run.
NEEDS_HUMAN_RULING: none; manager can route bounded fixture repair.
DEPENDENCY_NOTES: P4 owns fixture source; parent owns supplier execution; network fixture excluded.
