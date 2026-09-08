# D-PEC-84 scanner repair — independent verification review

RunID: `D84_SCANNER_REPAIR_2026-09-05`

Role: fresh evidence-only verifier, attempt 2

Status: `PASS`

## Milestone basis

The fixed diff was minimally inspected before this milestone. It contains exactly these three product postimages:

- `projects/pec/v2/tools/check_service_core_posture.py`
- `projects/pec/v2/tests/enforcement/test_dependency_assertion.py`
- `projects/pec/v2/tests/enforcement/test_locality_assertion.py`

The retained author evidence under `AUTHOR/` and `CHECKS/` was minimally inspected at the milestone. Its claims were subsequently checked against independent attempt-2 computations and reruns as recorded below.

## Attempt history

Verifier attempt 1 independently completed all required checks with zero findings but was interrupted before writing any verification file. No product file changed afterward. This attempt preserves that history only; it will record as independent evidence solely the commands and computations actually executed during attempt 2.

## Independent result

No actionable finding was found in the bounded three-file repair.

- Branch `codex/pec-d83-d84-execution-20260907`, HEAD `14f42e9ce17effa52e6415cc205a2df969b1256d`, and observable `origin/main` `62636f3a1ccc247af8c598b3c0a74ce9179d1fd3` match the activation basis. The live `IN_PROGRESS` status hash is `7d3eeb9888f10f6e938c7a0c08ff22ee1907df89812064ee76a95e0fdaeae60c`.
- The exact postimage hashes independently reproduce as checker `03be20a5d54551d7c01e1ce2ef1c36c4f2435c1a66809116dd4555cef0588f89`, dependency tests `8b686f4ed2b1729575d1961ff8bef7cfc4218795f816f4bb2b614d05510019c0`, and locality tests `54bb589632f764e9bdbd537e5f29ca75678bfd99492d4eea4467f2245f762bed`.
- All six fresh per-product `candidate-validation` and `rely-for-production` hold checks returned `ALLOW` with exit 0.
- The dependency repair derives aliases from imports, computes bindings once per module, emits one canonical dynamic-import finding per recognized call, preserves direct spellings and conservative blocking for every argument class, and leaves unrelated local callables unclassified.
- The UDP repair covers bound/unbound overload indexing, module/class/instance/callable/inline aliases, payload-independent IPv4/IPv6/Unix classification, the address-only keyword convention, and fail-closed missing/starred/`**kwargs`/excess/duplicate/unresolved/multiple-binding cases. Concrete external endpoints are reported when available; otherwise the endpoint is `UNRESOLVED`.
- The exact probes independently reproduced SHA-256 `b9bf8faa1bc575f9e5ffe3fb680a7bccc03c57681612fc94931f5666304eeeb2` and `75257d5cfcdd23d0ae7876478652af2257d79af5f08e1da4a9f1f7bb1ea760f3`, each with the required `BLOCK` diagnostic. The focused 23-test matrix and full 28-test enforcement discovery passed.
- Registered `v2-core-posture` passed with core/config/workflow hashes `2c830d1fe9bc7f550c47d5f22223f330a3a95118360e61bb6d9c785b47c151ca`, `20d64ff38122fa2f7b4bbe6478e42450ce6f9c8b03dc91c90b5095393ef309ed`, and `cad1d94bff71ffbefae9e550f847a2bc2cabd2a2a090536d22210838b8760c0b`; registered `v2-api-contract` passed 6 tests; registered `harness-self-check` exited 0 with its existing repository findings.
- One initial verifier harness invocation used `projects/pec` instead of the registered repository-root cwd and exited 2 before the check ran. The exact registered invocation was then run from `../..` and passed; this was a verifier invocation error, not a product failure.
- Scope validation and `git diff --check` passed. Exact preimage copies matched accepted-base bytes. No source-fixture, ignored-state, bytecode, config, workflow, core, service, database, or Git mutation was observed from verification.

Verdict: `PASS_FOR_MANAGER_FAN_IN` with zero findings.

Passing checks are finite evidence only. This verifier makes no artifact-acceptance, lifecycle, release, universal-confinement, `VER-004`/`OI-009` closure, or Remaining-application claim.
