# TASK-PKG02-API-KEY-STATUS-CONSUMER-REVIEW-01 — Sealed Launch Brief

- **RequestedBy:** `WI-PKG02-API-KEY-PRECEDENCE-01`
- **RunID:** `APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20`
- **ParentInstanceID:** `WI-PKG02-API-KEY-PRECEDENCE-01`
- **ChildInstanceID:** `TASK-PKG02-API-KEY-STATUS-CONSUMER-REVIEW-01`
- **Role:** TASK / Agent 2 (no delegation)
- **TaskSkill:** `software-code-review`
- **TaskProfile:** `NONE`
- **ApplyEdits:** `false`
- **ScopePath:** `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback`
- **PROFILE_PATH:** `projects/chirality-app-dev/software-workflow.json`

## Objective

Perform a fresh independent review of the frozen N2 API-key status consumer
candidate and DEL-02-05 R03 calibration. Determine whether the return is valid
for manager fan-in. Report only actionable findings with exact locations,
impact, evidence, and remediation; do not edit the candidate.

## ImplementationBrief

`instances/TASK-PKG02-API-KEY-STATUS-CONSUMER-IMPLEMENT-01/LAUNCH_BRIEF.md`
and `RETURN.md`.

## AcceptedBasis and DiffBasis

- Git basis: `6710ee6354debc201f6a454e2802897026cd4b38`.
- Accepted amended N1:
  `instances/WI-PKG04-API-KEY-PRECEDENCE-01/HANDOFF_STATE_V2.md`.
- Frozen identity:
  `instances/WI-PKG02-API-KEY-PRECEDENCE-01/FROZEN_DIFF_MANIFEST.md`.
- Review the exact N2 path diff against the Git basis and account for the
  accepted N1 dependency separately.

## Required review coverage

1. Verify every frozen hash before substantive review; any mismatch is FAIL.
2. Run scope validation first and affected-check selection using only the
   code-review skill allowlist.
3. Read 100% of `api-key-ipc.ts`, its full focused test, and the accepted N1
   storage source/test. Trace daemon client callers/serialization and settings
   UI consumption sufficiently to rule on compatibility.
4. Confirm no IPC environment re-inference remains; accepted order and source
   semantics are safeStorage/UI > canonical env > alias; malformed responses
   fail closed; no credential material can cross the status surface.
5. Confirm unavailable, store/remove, unsupported-provider, oMLX isolation,
   public/runtime contract, dependency/lockfile, and lifecycle behavior are
   preserved.
6. Inspect all four DEL-02-05 calibration records in full. Confirm they do not
   overclaim beyond R03, preserve the historical assessment, and leave state
   `IN_PROGRESS`, Remaining empty, dependencies unchanged, and Checking
   Approval SHA `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec` unchanged.
7. Audit focused/full/typecheck/build/harness/APP-HOLD/secret/scope/whitespace
   evidence for completeness and consistency.

## AllowedWriteTargets

Only this review instance's `STATUS.json` and `RETURN.md`.

## VerificationEvidence

All evidence paths and hashes listed in `FROZEN_DIFF_MANIFEST.md`, plus the
accepted N1 v2 return/handoff and the DEL-02-05 ScopeOfWork R02/R03/R08.

## ExpectedReturn

PASS or FAIL; frozen identity count; full-source coverage statement;
scope/affected-check assessment; actionable findings or explicit zero
findings; contract/security/lifecycle/calibration assessment; residual risk;
fan-in recommendation; tool-policy and read-only confirmation.

## Prohibitions

No candidate, deliverable, manager, shared, Git, lifecycle, commit, push, PR,
merge, release, or delegation write/action. Do not rerun arbitrary tests or
use tools outside the software-code-review skill allowlist.
