# TASK-PKG02-API-KEY-STATUS-CONSUMER-REVIEW-02 — Sealed Launch Brief

- **RequestedBy:** `WI-PKG02-API-KEY-PRECEDENCE-01`
- **RunID:** `APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20`
- **ParentInstanceID:** `WI-PKG02-API-KEY-PRECEDENCE-01`
- **ChildInstanceID:** `TASK-PKG02-API-KEY-STATUS-CONSUMER-REVIEW-02`
- **Role:** TASK / Agent 2 (no delegation)
- **TaskSkill:** `software-code-review`
- **TaskProfile:** `NONE`
- **ApplyEdits:** `false`
- **ScopePath:** `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback`
- **PROFILE_PATH:** `projects/chirality-app-dev/software-workflow.json`

## Objective

Perform a fresh independent review of frozen N2 candidate v3. Backcheck
Review-01's single evidence finding against the new complete normalized
registered-check evidence, then independently determine whether the unchanged
product/test and DEL-02-05 R03 calibration are valid for manager fan-in.

## ImplementationBrief

`instances/TASK-PKG02-API-KEY-STATUS-CONSUMER-IMPLEMENT-01/LAUNCH_BRIEF.md`
and `RETURN.md`.

## AcceptedBasis and DiffBasis

- Git basis: `6710ee6354debc201f6a454e2802897026cd4b38`.
- Accepted amended N1:
  `instances/WI-PKG04-API-KEY-PRECEDENCE-01/HANDOFF_STATE_V2.md`.
- Current frozen identity only:
  `instances/WI-PKG02-API-KEY-PRECEDENCE-01/FROZEN_DIFF_MANIFEST.md`,
  frozen at 2026-08-20T16:17:00Z.
- Prior review finding:
  `instances/TASK-PKG02-API-KEY-STATUS-CONSUMER-REVIEW-01/RETURN.md`.

## Required review coverage

1. Verify all 14 current frozen hashes before substantive review; any mismatch
   is FAIL. Ignore earlier manifest versions.
2. Run scope validation first and affected-check selection with correct
   project-relative inputs using only the code-review skill allowlist.
3. Read 100% of N2 IPC source/test and accepted N1 storage source/test; trace
   serialization/callers/settings consumption sufficiently for compatibility.
4. Confirm daemon-owned source semantics, UI > canonical env > alias order,
   fail-closed malformed status, non-disclosure, unavailable/store/remove,
   unsupported-provider, and oMLX isolation behavior.
5. Inspect all four DEL-02-05 calibration records; confirm R03-only claims,
   historical preservation, `IN_PROGRESS`, empty Remaining, unchanged
   dependencies and Checking Approval SHA.
6. Backcheck Review-01 F1: parse and inspect
   `N2_MANAGER_REGISTERED_CHECKS.json`; confirm frontend test/typecheck/build,
   harness-pytest, harness-self-check, and APP-HOLD all persist PASS and agree
   with the frozen bytes. Audit focused and secret/scope/whitespace evidence.

## AllowedWriteTargets

Only this review instance's `STATUS.json` and `RETURN.md`.

## VerificationEvidence

The current frozen manifest and every path it lists; accepted N1 v2 handoff;
Review-01 return; DEL-02-05 ScopeOfWork R02/R03/R08.

## ExpectedReturn

PASS or FAIL; frozen identity count; 100% source coverage; Review-01 backcheck;
scope/affected checks; actionable findings or explicit zero; contract,
security, lifecycle, and calibration assessment; residual risk; fan-in
recommendation; tool-policy and read-only confirmation.

## Prohibitions

No candidate/deliverable/manager/shared/Git/lifecycle/commit/push/PR/merge/
release/delegation action. No arbitrary test rerun or tool outside the
software-code-review skill allowlist.
