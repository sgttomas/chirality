# P3 repair 2: exact exec advertisement

RUN_STATUS: SUCCESS — bounded fixture repair; independent review and actual rerun pending.
ControlSurface: MERGED (original brief and parent exact same-file repair).
TaskProfile: NONE; TaskSkill: NONE.
ToolPolicyCompliance: PASS. Tools: zsh/python3/local vitest and tsc through exec_command; parent messages.
WriteAuthorization: ALLOWED_WRITE_TARGETS — same test and P3/REPAIR_2 only.

OpenAI GPT-6; exact serving model ID unavailable. Native Agent2 role/nondelegation instruction-asserted. No delegation, supplier execution/build/source modification, account/provider use, Git or operational act occurred.

## Observed cause

Parent P3_CANDIDATE1_STAR_01 failed in2636ms with no issued call/probe, peer error `Explicit shell/login advertisement required`, unchanged host/source, and cleanup0. Candidate1 SHA is retained in PARENT_FAILURE_SUMMARY.json. This was a fixture schema assumption before any attempted canary, not a protected-rule enforcement finding.

Read retained exact supplier shell_spec.rs and spec_plan_tests.rs. The source includes `login` only when the active environment allows login shells; `shell` is controlled by a separate optional inclusion flag. Supplier tests assert this conditional login visibility. Runtime trusted config/readback pins allow_login_shell=false. Requiring login in public tool metadata therefore rejected the expected restricted profile. The successful P1/P2 peers already construct only advertised optional arguments.

The historical actual Candidate1 PATCHED_1/RESULT.json at `$.requests[0].tools[0]` records exec_command with shell/workdir/yield_time_ms but no login. OBSERVED_EXEC_SCHEMA.json preserves the full exact advertised object, source JSON location and hash. This same extracted object is embedded verbatim in the pure regression, not synthesized as a desired schema. The retained source excerpts and full-file hashes corroborate the conditional property logic; they are read-only source evidence and no supplier was executed here.

## Repair and checks

New protectedExecArguments always supplies the required command, then supplies only actually advertised workdir, shell=/bin/sh, login=false and yield_time_ms=1000. It never invents missing shell/login properties. checkedProtectedExecArguments validates actual tool identity/schema, advertised keys/types, required fields and a closed safe option set. Even advertised escalation, additional permissions, alternate environment, justification, prefix, tty or unknown supplied options are forbidden. Login=true, another shell, altered yield budget and unknown required arguments fail. Trusted policy compile/readback remains unchanged and still enforces login-shell prohibition when the public tool omits login.

The peer now retains actual exec schemas with who/hash before attempting argument construction, including failed-schema cases. Other action, timing, denial-classification and host-evidence semantics are unchanged.

Focused final checks:4 pure tests passed,4 actual profiles skipped; strict standalone tsc passed. New regressions use the extracted actual advertisement, omission of shell, conditional false login, unknown/forbidden supplied fields, unsafe values, unknown required keys, wrong schema types and absent tool. These are fixture-only checks; no skipped profile is a conformance pass.

## Frozen source and imports

Source before: `540fd7ecc7909ec6c9327be8e4dbfc544babd65ed4645af51de1f7d4489e2f60`.
Source after: `e3482593af7c0dc031a91f157165a1c3c031bd59426c48b3217a9f1a02965942`.
Original failed parent evidence and earlier P3 seals remain unchanged. New `.source` preimage/output snapshots are nondiscovered evidence. SOURCE_HASHES.json records current imports and read-only source inputs separately.

- `projects/chirality-runtime/packages/daemon/src/codex-containment.ts`: `1bfb5d8a007061a7bceab4e2906df4095f6169170664257e77fb2edc3f090179`
- `projects/chirality-runtime/packages/daemon/src/codex-session.ts`: `868c4fb4e5500a1cd47ac93f553de9dd4bd0ad469fc2d972632ca2a9658e46f8`
- `projects/chirality-runtime/packages/core/src/exact-supply.ts`: `579de962f095db69082f28e9212d63af59b44a1979c32598fc82c11039a2952e`
- `projects/chirality-runtime/tests/fixtures/response-provider.mjs`: `0db5b30fb0511285675f23962a66a9f991f126f69f844381a406c34d8fdc59ef`
- `projects/chirality-runtime/tests/fixtures/boundary-response-provider.mjs`: `48055c740343bf0b3ff443aa9a3f2478c15d6bd28239e91a74e95a6a5c2ff588`
- `projects/chirality-runtime/tests/fixtures/process-response-provider.mjs`: `57e3c4e09183a0cebe825ca41fb5892f3a8836c635227d27aa1d7ce526e87a81`

## Handoff state

Accepted authority remains original BRIEF/BASIS and its accepted upstream pointers. This derivative repair does not accept supplier bytes, conformance, lifecycle, holds or release. Closure: implementation ready for independent backcheck; parent star rerun and subsequent globstar/question/class remain pending. Use existing family-by-family parent commands with truthful exact supplier SHA/size, fresh evidence directory and this coherent source/import generation. Record unknown actual schemas/denials as failures; do not infer enforcement from this repaired metadata boundary.

Outputs: repaired test, preimage/source copies, actual extracted schema/provenance, retained source excerpts, parent failure summary, SOURCE_HASHES.json, CHECKS.log, this report, OUTPUTS.sha256.
MISSING: independent backcheck and actual protected action evidence.
NEEDS_HUMAN_RULING: none for this bounded fixture repair.
DEPENDENCY_NOTES: parent owns stable-generation supplier runs; no cycle identified.
