# TASK return — fresh login-proof product review

RUN_STATUS: FAILED

ControlSurface: FILE

TaskProfile: NONE

TaskSkill: software-code-review

ScopePath: `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity`

ResolvedSkillPath: `/Users/ryan/.codex/worktrees/ef5e/chirality/skills/software-code-review`

ResolvedSkillVersion: `1`

ResolvedTaskProfileRequirement: `NONE`

CompanionFiles: `BRIEF_SCHEMA.md (found), TOOL_POLICY.md (found), QA_CHECKS.md (found)`

AllowedTools: `python3 tools/software_workflow/select_affected_checks.py:*`, `python3 tools/software_workflow/validate_change_scope.py:*`, `python3 tools/software_workflow/compare_structured.py:*`, `python3 tools/software_workflow/verify_generated_manifest.py:*`

RuntimeOverrides: none

WriteAuthorization: runtime-owned `RETURN.md` / `STATUS.json` only

## Terminal verdict

`FAIL` — two actionable blocking findings. The candidate is not valid for manager fan-in and must be remediated and reviewed again over a newly frozen complete diff.

## Hash verification and review coverage

- `frontend/scripts/run-packaged-launchagent-login-proof.mjs`: 794 lines read (100%); SHA-256 `c1c06d88308b14aefe43ad4732148063e5f8f62233029bd4b56bc67035e73361`, exactly matching `FROZEN_PRODUCT_DIFF_01.md`.
- `frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`: 370 lines read (100%); SHA-256 `71e0fb41da5a3dcb41de690943f17ba5b116da88db096c9f3f3326c4e74aa218`, exactly matching `FROZEN_PRODUCT_DIFF_01.md`.
- Both paths were reviewed in full against `/dev/null` as new files.

## Scope and evidence audit

- Deterministic exact two-path scope validation: `PASS`; no violations.
- Affected-check selection: `app-hold-integrity`, `frontend-test`, `frontend-typecheck`, and `harness-self-check`. The sealed evidence reports focused Vitest `1 file / 7 tests PASS` and manager-reproduced `node --check PASS`; the selected full/always checks remain manager fan-in gates.
- The implementation issues no `bootstrap` or `kickstart` command in either phase, performs no logout/login, installs only a validated non-default proof label, sets `CHIRALITY_SKIP_CLI_LAUNCHER=1`, and records the default job/plist without naming it as a mutation target.
- Public `prepared.json`, `summary.json`, and `evidence-package.json` use redacted path tokens; absolute host paths are retained only in the private consumed capture state, which is excluded from `evidence.files`.
- No live harness, LaunchAgent, host, Git, network, or release action was invoked by this review.

## Actionable findings

### [P1] Require a concrete source revision before a proof can pass

Location: `frontend/scripts/run-packaged-launchagent-login-proof.mjs:277-282`, propagated at `:467-515` and accepted again at `:597`.

`validateSourceRevision()` substitutes the syntactically valid literal `unavailable` when `--source-revision` is omitted. Consequently a successful prepare/login/capture sequence can emit `status: PASS` while its claimed source identity is explicitly unknown. This violates the sealed criteria that evidence bind exact source identity and that incomplete evidence fail closed. Several negative-path tests deliberately prepare without a revision (`frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts:243-304`), but no test asserts that an otherwise successful capture rejects an absent/unknown revision.

Remediation: make `--source-revision` mandatory for `prepare` (reject absent, blank, and sentinel/unknown values), preserve the bound value through capture, and add a focused test proving that missing source identity cannot reach `PREPARED` or `PASS`. If source identity must be stronger than an operator-supplied token, bind it to a verifiable packaged-artifact field in the same remediation.

### [P1] Do not boot out a service after its job identity has failed validation

Location: `frontend/scripts/run-packaged-launchagent-login-proof.mjs:348-391`, especially the classification-only inspection at `:354-360`; unconditional failure-path call at `:697-710`. Relevant mismatch checks occur at `:669-690`.

When capture observes a loaded service whose program, arguments, PID, or executable identity is missing or mismatched, the proof correctly records an error, but `cleanupProof()` then re-queries only whether that label is loaded and unconditionally executes `launchctl bootout <service>`. It never proves that the currently loaded job is the prepared packaged daemon before mutating it. A replaced or colliding service under the proof label therefore fails evidence validation but is still terminated, contrary to the required fail-closed behavior for missing identity evidence and proof-owned-only cleanup. The focused tests cover missing arguments but use a mock `bootout` that always mutates the fixture; they do not assert that ambiguous/mismatched service identity blocks service mutation.

Remediation: pass the expected executable/argument identity into cleanup, parse and validate the live job before any `bootout`, and refuse service mutation when identity is absent, ambiguous, or mismatched. Preserve a clear cleanup-incomplete failure for manual owner handling, and add focused program/argument/executable mismatch tests that assert no `bootout` occurs.

## Residual risks

- Actual logout/login, launchd login discovery, auto-start, capture, and evidence packaging remain unexecuted. They are owner-gated and this review makes no proof or lifecycle claim.
- The manager still owes the exact minimal owner procedure and all selected registered fan-in checks.
- Mocked tests cannot establish macOS timing behavior (including process-exit timing after `bootout`); that remains an on-host proof risk after the blocking findings are corrected.

ToolsUsed:

- `python3 tools/software_workflow/validate_change_scope.py`
- `python3 tools/software_workflow/select_affected_checks.py`
- direct read-only source inspection (`sed`, `nl`, `rg`)
- read-only hash/line verification (`shasum`, `wc`)

ToolPolicyCompliance: PASS — the declared deterministic review tools were used in required order; remaining commands were direct read-only code/evidence inspection. No unregistered product command or check was executed.

Outputs:

- This `RETURN.md`
- Runtime-owned terminal `STATUS.json`

MISSING:

- Remediation and fresh independent re-review.
- Owner-gated on-host proof, intentionally not executed.

NEEDS_HUMAN_RULING:

- none

DEPENDENCY_NOTES:

- Manager fan-in is blocked on both findings; no dependency cycle was observed.

ProposedChanges:

- Require and bind a concrete source revision.
- Make service cleanup identity-gated and add mismatch/no-bootout tests.
