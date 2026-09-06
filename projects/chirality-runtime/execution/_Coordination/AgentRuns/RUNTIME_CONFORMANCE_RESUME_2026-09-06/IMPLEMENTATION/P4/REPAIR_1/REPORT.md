# P4 repair 1 — reviewer blockers

RUN_STATUS: SUCCESS (bounded implementation and local checks only).
ControlSurface: MERGED; TaskProfile: NONE; TaskSkill: NONE.
ScopePath: /Users/ryan/.codex/worktrees/341e/chirality/projects/chirality-runtime/execution/_Coordination/AgentRuns/RUNTIME_CONFORMANCE_RESUME_2026-09-06/IMPLEMENTATION/P4/REPAIR_1
Attribution: OpenAI GPT-6; exact serving model ID unavailable. Ephemeral Agent2/nondelegation instruction-asserted. No delegation or actual supplier execution.

## Authority and preserved history
Sealed P4 brief, parent repair instruction after frozen REVIEW_P4, manager BASIS.json and predecessor accepted specification/owner grants. This is derivative implementation evidence. Previous REPORT.md/OUTPUT_HASHES and rejected `9b200f51b63a45fae6d3057ecda9ea41fe7f4e19ae1cfaae15b79ef30c258ea0` remain historical; byte-identical preimage and INPUT_HASHES are local to this repair. No production or governed state changes.

## P4-R1 composition correction
The reviewer correctly identified the next blocker: `CodexSupervisor.controlledForTests` deliberately cannot establish a production hosted boundary. The prior provider-observed binding was invalid and its fake successful hosted check in the metadata unit test concealed that mismatch.

The actual fixture now explicitly uses the established controlled-worker seam. The public broker really receives/returns requested roles and records their roleEvidence in retirement state, but this seam transports a raw prompt to its worker. A trusted test adapter maps each sealed worker ID to its predetermined requested role, creates the private Codex role envelope, and sends it through the actual authenticated supervisor. Incoming raw broker input hashes are recorded in `brokerInputs`; synthetic test adapter envelopes are separately labelled `adapterEnvelopes` with `origin=trusted-test-adapter`. The result explicitly states `bindingEvidenceClass=controlled-worker` and `productionRoleEnvelopeProven=false`. Equality of adapter and public roleEvidence checks configured composition; it is not proof that the production broker emitted the private envelope. No no-op verifier was introduced.

The metadata regression now uses a real controlled supervisor. Valid controlled compatibility passes; old malformed identity fails; upgrading the same fixture to provider-observed still rejects before any launch. Actual exact/no-account supplier factory, policy verification, five-role/read and native-lineage checks remain as before. The forged mechanical label check goes directly to the real private supervisor, independent of the adapter.

## P4-R2 source and failure guard
Correct compiled client pin is `packages/client/dist/src/client.js`. A default unit check resolves every selected source pin. Fallible initial pins, supplier verification, scratch setup and project creation now live inside try/finally. Cleanup is registered immediately after mkdtemp, before realpath. Final pin failures become explicit sourceStable=false/sourcePinFailure evidence instead of aborting evidence publication. Invalid user invocation parameters still fail before any scratch or supplier work. No full dependency-closure claim is made.

The reviewer's scratch command repro found no shell escaping defect; shell encoding was retained unchanged.

## Validation and handoff
CHECK.log: four passed, one actual supplier test skipped. TYPECHECK.log: targeted TypeScript noEmit exit0. Git diff --check passed.

Frozen test SHA256: `153df38bd56b9dcae9cc1a446ce0e803b50e4885987cb01cf1ff59e279f00965`. OUTPUT_HASHES.json pins this repair and the test. Parent must obtain fresh independent backcheck before an actual separately verified supplier canary. Use the exact invocation in prior P4 REPORT.md with fresh evidence and verified supply identity. Require calibrated controlled-worker/raw-prompt and adapter-origin fields, five public role probes/retirements, six real read+denial outputs, native supplier metadata, null-account observations, source/supply stability, unchanged host sentinels and complete owned cleanup within existing 10s probe/60s profile limits. No actual execution was performed by this Agent2.

Source repair closure: proposed reviewer blockers addressed, pending independent backcheck; actual conformance OPEN. No supplier acceptance, production role transport, model obedience, native registry universality, hosted account proof, hold/release/lifecycle authority follows.

Read-only network continuation inspection: already controlled-worker and its source pin paths exist; no analogous hosted blocker. It still hashes sources after scratch creation outside try/finally and has an unguarded final pin read, a latent cleanup/evidence risk if a pin disappears. That issue exceeds the narrow compatibility amendment and was reported to manager without network edits. Its previously frozen SHA remains `6129245278caf1eb4094db6fd640a7fa9f6c0ccf6f3ff2940f6a79cf8402fd6f`.

ToolsUsed: functions exec/exec_command (Python3, Vitest default-skip, TypeScript noEmit, read-only Git), parent messages.
ToolPolicyCompliance: PASS. WriteAuthorization: exact P4 role test plus P4/REPAIR_1 evidence.
MISSING: independent backcheck and parent supplier run. NEEDS_HUMAN_RULING: none. DEPENDENCY_NOTES: parent owns supplier identity/execution and fan-in.
