# TASK return — cleanup refusal evidence remediation

RUN_STATUS: SUCCESS

ControlSurface: FILE

TaskProfile: NONE

TaskSkill: software-bounded-implementation

ScopePath: `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity`

ResolvedSkillPath: `/Users/ryan/.codex/worktrees/ef5e/chirality/skills/software-bounded-implementation`

ResolvedSkillVersion: `1`

ResolvedTaskProfileRequirement: `NONE`

CompanionFiles: `BRIEF_SCHEMA.md (found), TOOL_POLICY.md (found), QA_CHECKS.md (found)`

AllowedTools: `python3 tools/software_workflow/select_affected_checks.py:*`, `python3 tools/software_workflow/run_registered_checks.py:*`, `python3 tools/software_workflow/validate_change_scope.py:*`, `python3 tools/software_workflow/verify_generated_manifest.py:*`, `python3 tools/software_workflow/compare_structured.py:*`

RuntimeOverrides: none

WriteAuthorization: ALLOWED_WRITE_TARGETS — the two product paths and this
instance's runtime-owned `RETURN.md` / `STATUS.json`.

## Implemented fix

`cleanupProof()` now isolates `assertProofOwnedLoadedJob()` behind its own
validation catch. Every exception from that ownership-validation boundary sets
`jobMutationRefused: true`, records the error, and exits before `bootout`.
State-query and bootout failures retain their prior retry/error behavior. The
evidence classification no longer depends on an exception message prefix.

The focused matrix gained two regressions:

- duplicate top-level `program` identity makes `parseLaunchctlJob()` reject the
  loaded job, leaves it loaded, issues zero `bootout` calls, and records
  `jobMutationRefused: true`;
- executable inspection failure leaves the job loaded, issues zero `bootout`
  calls, and records `jobMutationRefused: true`.

All prior safety cases remain passing.

## Checks

- APP-HOLD-1 reliance preflight for `DEL-09-04`: `ALLOW`.
- `node --check scripts/run-packaged-launchagent-login-proof.mjs`: `PASS`.
- `npm exec vitest -- run src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`:
  `PASS` — 1 file, 13 tests, 516 ms (the existing 11 plus 2 regressions).
- Exact two-path `validate_change_scope.py`: `PASS` — zero violations.

## Final product snapshot

- `frontend/scripts/run-packaged-launchagent-login-proof.mjs`: 877 lines;
  SHA-256 `b7694d5cfb27a4c17fa1b692c989aa35749ea2d77999d6b6eafa817d9dccdcfb`.
- `frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`:
  447 lines; SHA-256
  `ad58fc182f5632ba83c52699309eb541ff7d5728308c5f2ac347a52a1e5dccc8`.

ToolsUsed:

- `python3 execution/_Scripts/app_hold.py`
- `node frontend/scripts/run-packaged-launchagent-login-proof.mjs`
- `npm exec vitest`
- `python3 tools/software_workflow/validate_change_scope.py`
- repository-native targeted reads and `apply_patch`

ToolPolicyCompliance: PASS — only the mandatory APP-HOLD preflight, the sealed
brief's syntax and focused test checks, the declared scope validator, and
targeted read/edit operations were used. No live harness, LaunchAgent, host,
Git, network, release, install, or destructive action ran.

Outputs:

- Remediated login-proof harness and focused regressions at the two authorized
  product paths.
- This `RETURN.md` and terminal `STATUS.json`.

MISSING:

- Owner-gated logout/login and on-host LaunchAgent proof remain intentionally
  unexecuted and unproved.

NEEDS_HUMAN_RULING:

- none

DEPENDENCY_NOTES:

- Fresh read-only product-source review remains the manager's next fan-in gate.
- No dependency cycle was observed.

AppliedChanges:

- Replaced message-prefix-dependent refusal evidence with validation-boundary
  classification.
- Added parse-ambiguity and executable-inspection-failure regressions.
