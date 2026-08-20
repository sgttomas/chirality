# TASK-PKG02-CLOSEOUT-WHITESPACE-REVIEW-03 — Sealed Launch Brief

- **RequestedBy:** `WI-PKG02-API-KEY-PRECEDENCE-01`
- **RunID:** `APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20`
- **ParentInstanceID:** `WI-PKG02-API-KEY-PRECEDENCE-01`
- **ChildInstanceID:** `TASK-PKG02-CLOSEOUT-WHITESPACE-REVIEW-03`
- **Role:** TASK / Agent 2, no delegation
- **TaskSkill:** `software-code-review`
- **TaskProfile:** `NONE`
- **ApplyEdits:** `false`
- **ScopePath:** `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/instances/WI-PKG02-API-KEY-PRECEDENCE-01`
- **PROFILE_PATH:** `projects/chirality-app-dev/software-workflow.json`

## Objective

Freshly review the exact CHANGE-discovered N2 closeout whitespace remediation.
Confirm it removes only one redundant terminal newline from Review-01
`RETURN.md`, that every complete N2/candidate artifact is whitespace-clean,
and that all accepted product/test/deliverable identities and gates remain
valid. Return PASS or exact discrepancy; do not edit the candidate.

## AcceptedBasis and DiffBasis

- Accepted N2 terminal handoff:
  `instances/WI-PKG02-API-KEY-PRECEDENCE-01/HANDOFF_STATE.md`.
- Accepted N2 Review 02 PASS:
  `instances/TASK-PKG02-API-KEY-STATUS-CONSUMER-REVIEW-02/RETURN.md`.
- Current frozen remediation:
  `instances/WI-PKG02-API-KEY-PRECEDENCE-01/CLOSEOUT_REMEDIATION_MANIFEST.md`.
- Before bytes are reconstructable by appending one LF to the current target;
  verify both declared before and after hashes independently.

## Required coverage

1. Verify the target after hash and reconstructed before hash; prove the only
   byte change is removal of one terminal LF and the current file ends in
   exactly one LF.
2. Confirm the Git index is empty and no Git mutation is performed.
3. Independently run/check tracked whitespace and per-file untracked-aware
   whitespace for the complete N2 scope, including the new manifest and this
   review instance inputs. Any additional discrepancy is FAIL.
4. Parse all N2 JSON artifacts and validate exact remediation-path
   containment.
5. Verify every preservation hash in the manifest, DEL-02-05 lifecycle,
   Remaining, dependency, and Checking Approval SHA preservation.
6. Parse and confirm fresh APP-HOLD reliance is ALLOW. Confirm the accepted
   registered/focused evidence remains applicable because product/test/DEL
   bytes did not change; do not rerun product tests.
7. Inspect the complete current remediation target and all relevant terminal
   N2 handoff/review records. Report only actionable discrepancies.

## AllowedWriteTargets

Only this review instance's `STATUS.json` and `RETURN.md`.

## ExpectedReturn

PASS or FAIL; exact before/after hashes and byte proof; complete whitespace
file count; JSON/containment/preservation/APP-HOLD result; findings; whether
CHANGE may restage N2; read-only/tool-policy confirmation.

## Prohibitions

No candidate, product, test, deliverable, manager, shared, Git, staging,
commit, push, PR, merge, release, lifecycle, receipt, completion-log, or
delegation write/action. No product test rerun.
