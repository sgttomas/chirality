# P4 repair 2 — advertised exec arguments

RUN_STATUS: SUCCESS (bounded source repair/local verification only).
ControlSurface: MERGED; TaskProfile: NONE; TaskSkill: NONE.
ScopePath: /Users/ryan/.codex/worktrees/341e/chirality/projects/chirality-runtime/execution/_Coordination/AgentRuns/RUNTIME_CONFORMANCE_RESUME_2026-09-06/IMPLEMENTATION/P4/REPAIR_2
Attribution: OpenAI GPT-6; exact serving model ID unavailable. Ephemeral Agent2/nondelegation instruction-asserted. No delegation or actual supplier execution.

## Actual checkpoint and diagnosis
Parent `PARENT_CHECKS/P4_CANDIDATE1_01` used role source `153df38bd56b9dcae9cc1a446ce0e803b50e4885987cb01cf1ff59e279f00965` with separately identified Candidate1. Its first actual model request failed inside the test peer's schema guard, before any read issuance: Unknown actual exec schema. One supplier process closed, cleanupFailures=0, sourceStable=true, elapsed2616ms. This actual failure remains unmodified. No read/role conformance followed.

Retained supplier source HEAD is `758ef40f50c1a458425c7cfbf1eb12cbc07af0b0`. Read-only git diff for shell_spec.rs and unified_exec/exec_command.rs was empty. `shell_spec.rs` SHA256 is `39e2d837cc76a1a2822363eb0932a8b1e2ac1188ee0fb38df9d57958e0b85320`; exact source is retained as .source evidence. Lines69–77 conditionally advertise login:

```rust
if options.allow_login_shell {
    properties.insert(
        "login".to_string(),
        JsonSchema::boolean(Some(
            "True runs the shell with -l/-i semantics; false disables them. Defaults to true."
                .to_string(),
        )),
    );
}
```

Runtime prepares allow_login_shell=false and the actual actor verifies that immutable setting. P4 unconditionally included login:false then rejected its own unadvertised argument. Established successful P1/P2 helpers only include login when present in the advertisement. The historical failed result did not retain property names, so the exact omitted field is inferred from matching retained supplier source/config; the next result now records bounded actual property/required names to confirm.

## Change and checks
The read adapter now starts with required cmd and includes known optional workdir/login/yield_time_ms/max_output_tokens only when actually advertised. Every unknown/unmapped required field still rejects; every supplied field must exist in the advertisement. No environment_id, permissions or other guessed field is added. No policy, shell command, callback, supplier or production file changed. Schema diagnostics retain bounded property/required names, tool name/namespace and role only; no descriptions, raw command, prompt or credentials.

Pure regression models the supplier disabled-login advertisement, checks conditional login=false when advertised, and rejects an unknown required field. CHECK.log: five passed/one actual supplier test skipped. TYPECHECK.log: targeted noEmit exit0. Git diff --check passed. This is adapter readiness evidence, not an actual supplier/read success.

Frozen role source SHA256: `4b72276d15f58899e0cdbc0f82fa8b082f04b975e95275d7d8104ffbe5b8dd30`. INPUT_HASHES, OUTPUT_HASHES and byte-identical incoming .source preserve source transitions. Earlier repair reports/seals and actual failed evidence remain historical. Network fixture was untouched in this repair.

## Parent handoff
After independent backcheck, repeat the prior exact parent invocation using fresh evidence and independently verified Candidate1 or separately completed/verified Candidate2 identity. Inspect execSchemas together with six issued/first-return read outcomes, five public role/retirement observations, native metadata, account-null, unchanged host sentinels, source/supply pins and cleanup/budget fields. The explicit controlled-worker adapter calibration and productionRoleEnvelopeProven=false remain required. No successful production role transport, hosted account, supplier acceptance, native-role obedience, lifecycle/hold/release act is claimed.

Closure: bounded repair prepared, actual P4 conformance OPEN. Accepted upstream: parent sealed P4 brief, REPAIR_2 instruction, manager BASIS and predecessor accepted specification/owner direction. This is derivative evidence; no governed pointer changed.
ToolsUsed: functions exec/exec_command (read-only git, Python3, Vitest default-skip, TypeScript), parent messages. ToolPolicyCompliance: PASS. WriteAuthorization: exact role test and P4/REPAIR_2 evidence.
MISSING: independent backcheck and parent actual run. NEEDS_HUMAN_RULING: none. DEPENDENCY_NOTES: parent owns supplier execution and fan-in.
