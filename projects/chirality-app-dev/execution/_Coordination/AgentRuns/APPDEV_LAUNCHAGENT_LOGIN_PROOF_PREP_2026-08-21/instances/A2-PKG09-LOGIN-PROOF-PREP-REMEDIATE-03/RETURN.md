# TASK return — install-attempt cleanup remediation

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

WriteAuthorization: ALLOWED_WRITE_TARGETS — the exact script, focused test,
and this instance's runtime-owned `RETURN.md` / `STATUS.json`.

## Implemented fix

Preparation now assumes cleanup responsibility immediately before invoking the
packaged CLI. Any rejection after that point — including a timeout after side
effects and a later plist-validation failure — runs identity-gated cleanup of
the exact proof job, plist, and runtime-data targets.

The thrown preparation error preserves the redacted primary error and appends
an explicit `complete` or `incomplete` cleanup verdict with job, mutation
refusal, plist, runtime-data, and cleanup-error evidence. Ambiguous loaded-job
identity still prevents `bootout`; residue is reported rather than silently
mutated or omitted.

The focused suite gained two regressions:

- install writes the proof plist and then rejects as a timeout: plist and
  runtime data are absent, no `bootout` occurs, and cleanup is reported
  complete;
- install succeeds but the written plist fails validation: the same bounded
  cleanup and explicit verdict are proved.

## Checks

- APP-HOLD-1 accepted-dependency-consumption preflight for `DEL-09-04`: `ALLOW`.
- `node --check scripts/run-packaged-launchagent-login-proof.mjs`: `PASS`.
- `npm exec vitest -- run src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`:
  `PASS` — 1 file, 15 tests, 498 ms (the prior 13 plus 2 regressions).
- Exact two-path `validate_change_scope.py`: `PASS` — zero violations.

## Final product snapshot

- `frontend/scripts/run-packaged-launchagent-login-proof.mjs`: 902 lines;
  SHA-256 `980e2e710ab66006baeefc14d400584bc8837f3ea3b35390db94b879413e2c20`.
- `frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`:
  484 lines; SHA-256
  `f168e7d18326a536ff07b4e3a82019904bc43753fa3999acd439b8353171f01a`.

ToolsUsed:

- `python3 execution/_Scripts/app_hold.py`
- `node frontend/scripts/run-packaged-launchagent-login-proof.mjs`
- `npm exec vitest`
- `python3 tools/software_workflow/validate_change_scope.py`
- repository-native targeted reads and `apply_patch`

ToolPolicyCompliance: PASS — only the mandatory APP-HOLD preflight, sealed
syntax/focused-test checks, declared scope validator, and targeted read/edit
operations were used. No live harness, LaunchAgent, host, Git, network,
install, release, or destructive action ran.

Outputs:

- Remediated login-proof harness and two focused regressions at the exact
  authorized product paths.
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

- Moved cleanup responsibility before the awaited install command.
- Surfaced complete/incomplete cleanup and residual state on prepare failure.
- Added timeout-after-side-effect and post-install-validation regressions.
