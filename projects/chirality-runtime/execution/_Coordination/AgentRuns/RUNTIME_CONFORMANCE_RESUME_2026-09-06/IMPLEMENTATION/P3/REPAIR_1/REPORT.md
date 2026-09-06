# P3 classifier repair 1

RUN_STATUS: SUCCESS — bounded fixture repair; supplier execution pending parent and independent backcheck.
ControlSurface: MERGED (original sealed brief plus parent exact repair instruction).
TaskProfile: NONE; TaskSkill: NONE.
ToolPolicyCompliance: PASS. Tools: zsh/python3/local vitest and tsc through exec_command; parent messages.
WriteAuthorization: ALLOWED_WRITE_TARGETS — same test source and P3/REPAIR_1 only.

OpenAI GPT-6; exact serving model ID unavailable. Agent2 role/nondelegation instruction-asserted. No delegation, supplier, account/provider, Git or operational action occurred.

## Finding and repair

Read frozen REVIEW_P3/REPORT.md and CLASSIFIER_REPRO.json. The original denial classifier could count a missing/context error as denial merely because its path contained `protected`. Both reported false-positive inputs are now explicit pure regressions.

The repaired classifier accepts the complete known outside-project/user-approval rejection line, or narrowly structured terminal `Permission denied` (optional os error13) / `Operation not permitted` (optional os error1) messages with known read/write/create/delete/open/apply_patch prefixes. It no longer treats words `protected`, `denied`, or `not permitted` appearing anywhere in a pathname/message as permission evidence. Unknown wording remains false, preserving the bounded raw output for parent diagnosis. It adds ten negative controls (including the review reproductions, quoted/unknown messages, incidental protected/permission text, and mismatched errno) and five positive forms. No compiler policy, shell/patch action, watchdog or evidence-acceptance requirement changed.

## Validation and freeze

Focused final Vitest: 2 pure tests passed; 4 exact profiles skipped. Strict standalone tsc passed. These checks do not establish actual protected-path conformance. CHECKS.log records exact commands.

Original source/evidence remain unchanged under P3; REPAIR_1 contains a byte-identical original preimage and a new nondiscovered `.source` snapshot. SOURCE_HASHES.json cites original evidence/review hashes and current imported source hashes separately. Original source SHA256: `4daffb1c5631734489a9bee9dc136a015bd43ca44991dd5216ebb85d14d1a569`.
New source SHA256: `540fd7ecc7909ec6c9327be8e4dbfc544babd65ed4645af51de1f7d4489e2f60`.

Current import pins at this repair freeze:

- `projects/chirality-runtime/packages/daemon/src/codex-containment.ts`: `1bfb5d8a007061a7bceab4e2906df4095f6169170664257e77fb2edc3f090179`
- `projects/chirality-runtime/packages/daemon/src/codex-session.ts`: `868c4fb4e5500a1cd47ac93f553de9dd4bd0ad469fc2d972632ca2a9658e46f8`
- `projects/chirality-runtime/packages/core/src/exact-supply.ts`: `579de962f095db69082f28e9212d63af59b44a1979c32598fc82c11039a2952e`
- `projects/chirality-runtime/tests/fixtures/response-provider.mjs`: `0db5b30fb0511285675f23962a66a9f991f126f69f844381a406c34d8fdc59ef`

## Handoff state

Accepted upstream remains original BRIEF/BASIS and its accepted authority pointers; this is derivative repair evidence, not decomposition/supplier/conformance acceptance. Closure: bounded repair complete; independent reviewer backcheck and parent actual four-family execution remain open. Rerun the same parent family-by-family commands in P3/REPORT.md with this new frozen source and current import generation, truthful exact supplier identity, and new evidence directories. Preserve unknown actual rejection outputs and investigate them rather than broadening this classifier automatically.

Outputs: repaired test, preimage/source copies, SOURCE_HASHES.json, CHECKS.log, this report and OUTPUTS.sha256.
MISSING: independent backcheck and all actual P3 supplier evidence.
NEEDS_HUMAN_RULING: none for bounded repair.
DEPENDENCY_NOTES: no cycle; parent controls combined-source freeze and supplier runs.
