# TASK return — login-proof blocking review remediation

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

WriteAuthorization: ALLOWED_WRITE_TARGETS

## Objective result

Both blocking P1 findings from review 01 are remediated within the two-file
product/test fence.

- Prepare now requires a trimmed, path-free, non-placeholder source revision
  before it creates the proof session root or performs any packaged install.
  Capture revalidates the bound source revision and cannot publish `PASS` for
  missing, blank, placeholder, or inconsistent source identity.
- Cleanup now parses and proves the currently loaded same-label job's running
  state, exact program, exact `--runtime-daemon` argv, valid PID, and unique
  packaged process-executable identity immediately before every `bootout`.
  Missing, mismatched, or ambiguous identity refuses job mutation, leaves
  `jobAbsent: false`, records `jobMutationRefused: true` plus the cleanup
  error, and therefore cannot reach `PASS`.

## Regression evidence

The focused suite now has 11 passing tests. New or strengthened coverage
proves:

- absent, whitespace-only, and placeholder (`unknown`) source revisions fail
  before owner-state mutation or session creation;
- missing loaded argv refuses bootout;
- mismatched program refuses bootout;
- mismatched argv refuses bootout;
- ambiguous process-executable identity refuses bootout;
- every ambiguous case leaves the loaded fixture unchanged and records an
  incomplete cleanup rather than claiming success.

## Checks

- APP-HOLD-1 reliance preflight for `DEL-09-04`: `ALLOW`.
- `node --check scripts/run-packaged-launchagent-login-proof.mjs`: `PASS`.
- `npm exec vitest -- run src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`:
  `PASS` — 1 file, 11 tests, 487 ms.
- Exact two-path `validate_change_scope.py`: `PASS` — zero violations.

## Final product snapshot

- `frontend/scripts/run-packaged-launchagent-login-proof.mjs`: 875 lines;
  SHA-256 `4c524234788cc2e0963dab2e9417475da0b2843f22fdb7f9fca898f57ef370a0`.
- `frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`:
  437 lines; SHA-256
  `434406fee9bf15b80e46f60a043d953fc0ab45b8aa8928a705f606f4d16b09d4`.

ToolsUsed:

- `python3 execution/_Scripts/app_hold.py`
- `node frontend/scripts/run-packaged-launchagent-login-proof.mjs`
- `npm exec vitest`
- `python3 tools/software_workflow/validate_change_scope.py`
- repository-native targeted reads and `apply_patch`

ToolPolicyCompliance: PASS — only the required APP-HOLD preflight, the sealed
brief's direct focused checks, the declared deterministic scope validator, and
targeted read/edit operations were used. No live, network, release, install,
or destructive command ran.

Outputs:

- Remediated product script.
- Expanded focused regression suite.
- This runtime-owned `RETURN.md` and terminal `STATUS.json`.

AppliedChanges:

- Required concrete source identity at the earliest prepare boundary and
  revalidated it at capture.
- Added exact loaded-job ownership validation before bootout and accurate
  mutation-refusal evidence.
- Added focused source-identity and no-bootout regressions.

MISSING: none within the sealed remediation node

NEEDS_HUMAN_RULING: none

DEPENDENCY_NOTES: fresh independent full-diff re-review remains the manager's
next gate; no dependency cycle was observed.

ResidualRisk: mocked tests do not establish macOS launchd timing. The actual
logout/login proof remains intentionally unexecuted and owner-gated. No proof,
acceptance, merge, issuance, or lifecycle claim is made.

LiveHostBoundary: no prepare/capture invocation, LaunchAgent mutation,
bootstrap, kickstart, logout/login, launcher mutation, or host proof occurred.
