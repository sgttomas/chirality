# Return — TASK-INTEGRATED-REMEDIATION-01

RUN_STATUS: SUCCESS

ControlSurface: FILE

TaskProfile: NONE

TaskSkill: software-bounded-implementation

ScopePath: `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev`

ResolvedSkillPath: `/Users/ryan/.codex/worktrees/ef5e/chirality/skills/software-bounded-implementation`

ResolvedSkillVersion: `1`

ResolvedTaskProfileRequirement: NONE

CompanionFiles: `BRIEF_SCHEMA.md (found), TOOL_POLICY.md (found), QA_CHECKS.md (found)`

AllowedTools: `python3 tools/software_workflow/run_registered_checks.py`, `python3 tools/software_workflow/validate_change_scope.py`

RuntimeOverrides: PATH resolved `python3` to `/Users/ryan/.local/share/mise/installs/python/3.13/bin/python3` (Python 3.13.14)

WriteAuthorization: ALLOWED_WRITE_TARGETS

## Outputs Produced

- Removed exactly the 15 trailing blanks cited by integrated Review 01 from
  `WORK_GRAPH.md`, `WORK_GRAPH_V2.md`, `N1_MANAGER_VALIDATION_V2.md`, and
  `RETURN_V2.md`; wording is unchanged.
- Calibrated DEL-09-06 REQ015 so compact `summary.json` binds artifacts,
  assertions, and results, while `_run_records/TASK_RUN_2026-08-20_1630.md`
  is the separate citation for exact host commands.
- Persisted normalized registered-check evidence at
  `instances/WI-PKG09-API-KEY-PRECEDENCE-01/N3_MANAGER_REGISTERED_CHECKS.json`,
  SHA-256 `e89bf83dc90073f775b8a80a1216b9bd68a0f4157928ddd866e6b30363c175ed`.
  `harness-pytest` passed with exit 0 in 25.520 seconds and `350 passed in
  25.35s`; `harness-self-check` passed with exit 0 in 7.810 seconds. The JSON
  retains normalized command, cwd, timeout, duration, stdout, and stderr.
- APP-HOLD reliance returned `ALLOW` for DEL-09-04 and DEL-09-06. Exact-path
  validation covered all eight written paths and passed with zero violations.
- Final complete tracked-plus-untracked candidate inspection covered 94 paths:
  zero trailing-whitespace findings, 27 JSON files parsed, and zero JSON
  errors. Final exact-path validation covered all eight written paths and
  passed with zero violations.

## Identity preservation

- Before remediation: frozen Review 01 candidate identity was 86 subjects at
  aggregate SHA-256 `ee2623a620af684ed6b67a678466d46db186b4e590c9dd606f61542ff322acec`.
- After F1-F3 remediation: 87 candidate subjects (the original candidate plus
  normalized check evidence, excluding the manifest and review/remediation
  runtime controls) have aggregate SHA-256
  `d2e9c575c1265552b09fd56c17f294a0323fd35299ba555eb2ab056bfc565dd6`.
- Product/test SHA-256 values remain exactly `d810b1ef...1444db`,
  `c9cadac3...17dac4`, `3293cbf1...ed3cb`, and `818b7424...74b1a6`.
- Compact proof identities remain exactly `0ec3c501...82df3` for
  `summary.json` and `4fe82d2b...ffc6` for `SUMMARY.md`.
- Raw host proof anchors remain exactly `016f26c4...471` for raw
  `summary.json` and `7293f98c...fa00` for the final secret scan, matching
  Review 01. No raw proof byte or host artifact was written or rerun.

## Tools Used

- `python3 tools/software_workflow/run_registered_checks.py`
- `python3 tools/software_workflow/validate_change_scope.py`
- Mandatory project preflight: `python3 execution/_Scripts/app_hold.py`
- Brief-required read-only Git, hash, JSON, and whitespace primitives

## Tool Policy Compliance

PASS. Method-tool use stayed within the sealed allowlist. The APP-HOLD command
was the higher-level project-mandated reliance preflight and was also expressly
required by the sealed brief's candidate audit.

## Write Authorization

All writes are confined to the eight explicit `AllowedWriteTargets`. No local
TASK run record was created because the sealed custom instructions exclude run
records; this managed child uses `LAUNCH_BRIEF.md`, `STATUS.json`, and this
`RETURN.md` as its durable record.

## Applied Changes

- Four whitespace-only control/evidence edits.
- One evidence-claim calibration edit.
- One normalized registered-check JSON addition.
- This instance's runtime-owned status and return terminalization.

No product, test, deliverable state, Remaining, lifecycle, compact proof,
dependency, lockfile, SOW, receipt, completion log, host artifact, or Git state
was changed. No host product proof was rerun.

## Missing

none

## Needs Human Ruling

none

## Dependency Notes

- Fresh independent integrated review remains the parent-manager fan-in gate.

## Proposed Changes

none
