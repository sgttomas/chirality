# TASK-SW-REVIEW Return

RUN_STATUS: `SUCCESS`

ControlSurface: `FILE`

TaskProfile: `NONE`

TaskSkill: `software-code-review`

ScopePath: `~/projects/chirality-app-dev/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01-C2A/instances/TASK-SW-REVIEW`

ResolvedSkillPath: `~/skills/software-code-review`

ResolvedSkillVersion: `1`

ResolvedTaskProfileRequirement: `NONE`

CompanionFiles: `BRIEF_SCHEMA.md (found), TOOL_POLICY.md (found), QA_CHECKS.md (found)`

AllowedTools: `python3 tools/software_workflow/select_affected_checks.py:*`, `python3 tools/software_workflow/validate_change_scope.py:*`, `python3 tools/software_workflow/compare_structured.py:*`, `python3 tools/software_workflow/verify_generated_manifest.py:*`

RuntimeOverrides: `none`

WriteAuthorization: `ALLOWED_WRITE_TARGETS` — source remained read-only; writes were confined to this child instance evidence directory.

## Verdict

`PASS_AFTER_REPAIR` for manager fan-in. Exact source containment passes and the sole fail-closed correctness finding is closed.

## Correction backcheck

### CLOSED — `INVALID` can no longer be returned with `valid: true`

- Location: `projects/chirality-app-dev/frontend/src/lib/workspace/filesystem.ts:978-991` and `projects/chirality-app-dev/frontend/src/__tests__/lib/workspace-deliverable-contract-scanner.test.ts:278-297`.
- Backcheck: `hasSelectableProductionFormat` is true only for `LEGACY_FOUR_DOC`, `SOW_V1`, and `MIGRATION_DUAL`; `valid` now requires that predicate plus zero errors. `INVALID` and `AMBIGUOUS` therefore remain invalid even when their findings are warning/info-only.
- Regression: the added `OPEN`/no-format case asserts `documentFormat: 'INVALID'`, `errorCount: 0`, `valid: false`, and `selectedProductionDocuments: []`.
- Verification evidence: parent rerun reports the exact frozen focused suite PASS at 7 files / 70 tests and `npm run typecheck` PASS.
- Remaining blocker: none.

## Confirmed review results

- Scope containment: PASS. The four candidate paths are within the nine exact allowed roots; `SCOPE_VALIDATION.json` records `violations: []`.
- `SOW_V1` and `LEGACY_FOUR_DOC`: select `ScopeOfWork.md` and the four legacy documents respectively.
- `MIGRATION_DUAL`: requires the literal mode, `isolatedWorkspace: true`, a lowercase-hex `D-GOV-16@` authority, exact resolved deliverable path membership, a structurally accepted Scope of Work, and matching embedded authority text. Normal route scans supply no migration activation and remain ambiguous.
- Invalid/unreadable Scope of Work, partial legacy, unauthorized dual, authority mismatch, requested-format mismatch, and missing format at or beyond `INITIALIZED` produce errors and no selected production documents.
- `DocumentView` removes the feature flag, consumes scanner-selected production documents, keeps `_STATUS.md` as default, resets the file on explicit deliverable selection, and retains the listed control-plane choices.
- DOMAIN/KTY detection and its independent source scans are not subjected to the PROJECT/SOFTWARE format resolver by this diff.
- The five unchanged frozen callers/tests remained source-compatible under the supplied 7-file/69-test and typecheck evidence.

## Tools Used

- `python3 tools/software_workflow/validate_change_scope.py`
- `python3 tools/software_workflow/select_affected_checks.py`

ToolPolicyCompliance: `PASS`

## Outputs

- `SCOPE_VALIDATION.json`
- `_run_records/TASK_RUN_2026-07-13_0709.md`
- `RETURN.md`
- `STATUS.json`

## Residual risks and evidence gaps

- Affected-check selection returned `frontend-test`, `frontend-typecheck`, and the always-selected `harness-self-check`; the supplied evidence covers the first two but not `harness-self-check`.
- Supplied evidence does not include a build or rendered-view check. The parent brief says broader fan-in gates will be rerun independently.
- No direct component test demonstrates that `DocumentView` renders only scanner-selected production options or preserves safe default/reset behavior; this remains a UI regression risk even though the source path is straightforward.

## Missing

- `harness-self-check`, build, and rendered-view evidence from this child; parent broader fan-in is still required.

## Needs Human Ruling

none

## Dependency Notes

none

## Applied Changes

- Evidence files only; no source edits.
