# P4 repair 1 independent backcheck

RUN_STATUS: SUCCESS (bounded review; diagnostic execution admission only)
ControlSurface: MERGED; TaskProfile: NONE; TaskSkill: NONE.
ScopePath: /Users/ryan/.codex/worktrees/341e/chirality/projects/chirality-runtime/execution/_Coordination/AgentRuns/RUNTIME_CONFORMANCE_RESUME_2026-09-06/IMPLEMENTATION/REVIEW_P4/REPAIR_1
Attribution: OpenAI GPT-6; exact serving model ID unavailable. Agent2 role and nondelegation instruction-asserted. No delegation.

## Verdict

Both prior findings P4-R1 and P4-R2 are resolved for frozen role fixture `153df38bd56b9dcae9cc1a446ce0e803b50e4885987cb01cf1ff59e279f00965`. Limited admission: parent may run a separately verified Candidate1 diagnostic against this exact fixture with fresh evidence. This is not role conformance acceptance, production role-envelope proof, or supplier acceptance.

## P4-R1 backcheck

The public DelegatedRuntime binding now accurately selects controlled-worker. Production preflight remains unchanged; the pure regression uses the real controlled factory and verifies that provider-observed admission still rejects with zero launches. Invalid compatibility still rejects. There is no no-op hosted verification method.

The public controlled seam emits raw prompts. Its test adapter explicitly maps known fixture worker IDs to roles and constructs Codex envelopes. The returned evidence distinguishes `brokerInputs` with raw prompt digests from `adapterEnvelopes` with `origin=trusted-test-adapter`, and sets `bindingEvidenceClass=controlled-worker`, `productionRoleEnvelopeProven=false`, and `adapterEvidence=trusted-test-adapter-role-mapping`. Adapter/public role-policy equality supports this configured test composition only. It does not claim production broker envelope propagation. The forged mechanical label is sent directly to the actual private supervisor, independent of the adapter.

Five public requested-role responses and durable retirement policy/identity binding remain tested. Native child identity/parent-source corroboration, standalone read/denial markers, sentinel stability, no-account observations, actual native policy digest, strict existing budgets and source/supply stability checks remain. No role label or containment claim was broadened. The test-only identity/digest remains calibrated.

## P4-R2 backcheck

The selected compiled client pin now references existing `packages/client/dist/src/client.js`, and a pure check resolves every pin. Initial source pin reads, supplier verification and scratch setup are inside try/finally. The scratch cleanup registers immediately after mkdtemp and before realpath; final pin failures set sourceStable=false/sourcePinFailure without suppressing evidence publication. Invocation-shape rejection still occurs before scratch work. Evidence publication can itself fail on an unavailable/unwritable target, but owned cleanup has already run; the parent must record command/log failure separately and supply a fresh writable directory.

## Checks and scope

Default-skip Vitest passed 4 pure tests and skipped the actual supplier test. Targeted TypeScript noEmit exited0. Selected production source and compiled hashes are unchanged from the original independent review; only the fixture hash changed. SOURCE_HASHES.json records the exact read basis. No source modifications, supplier launches, account access, network activity or user-server operation occurred. The network fixture remained excluded.

## Handoff

Accepted upstream: manager BASIS.json/PLAN.md, predecessor accepted SPEC_FAN_IN and owner grants routed by the sealed P4 brief, plus parent repair instruction and P4/REPAIR_1 frozen return. This is derivative review evidence, not decomposition authority. Review closure: P4-R1/P4-R2 closed at source/backcheck level; actual conformance OPEN. Next: parent uses fresh evidence and separately verified Candidate1 bytes to execute the repaired role diagnostic, requiring all fixture pass controls and accurate controlled-adapter evidence labels. Any failure requires phase-specific diagnosis; a passing controlled diagnostic still does not prove production private-envelope transport or hosted account acceptance. No lifecycle, hold/release or governed pointer act is inferred.

ToolsUsed: functions exec/exec_command (read-only Git/diff and source reads, Python3 hashes/evidence, Vitest default-skip, TypeScript noEmit); parent messages.
ToolPolicyCompliance: PASS. WriteAuthorization: REVIEW_P4/REPAIR_1/** only.
Outputs: REPORT.md, CHECKS.json, SOURCE_HASHES.json, OUTPUT_HASHES.json.
MISSING: actual parent Candidate1 diagnostic and broader production conformance evidence.
NEEDS_HUMAN_RULING: none for this authorized diagnostic.
DEPENDENCY_NOTES: parent owns supplier execution; P4 owns source; network excluded.
