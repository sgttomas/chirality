# MEMORY - DEL-06-04

## Decisions And Evidence

- 2026-06-21 - ADQ-11/D-APP-43 closed the exact-edit precondition and controlled-write atomicity residuals. Hook-side `Edit.old_string` checks are the canonical pre-SDK stale-edit guard, and Chirality-owned controlled writers use same-directory atomic rename. REF-006 is now `MATCH` under D-APP-38 corpus v2 for active review. This does not imply CHECKING, ISSUED, release readiness, dependency satisfaction, professional approval, certification, sealing, authentication, or code-compliance acceptance.
- 2026-06-21 - ADQ-11 added hook-side `Edit.old_string` precondition checks before SDK execution and records allow/deny evidence for the precondition result. Chirality-owned controlled status/dependency writes now use same-directory atomic rename. Evidence: `../Evidence_ADQ-11_Permission_Tool_Residuals.md`. This does not imply CHECKING, ISSUED, release readiness, dependency satisfaction, professional approval, certification, sealing, authentication, or code-compliance acceptance.
- 2026-06-16 - Human project authority advanced this deliverable lifecycle from SEMANTIC_READY to IN_PROGRESS because active code implementation is underway. This does not imply CHECKING, ISSUED, release readiness, dependency satisfaction, professional approval, certification, sealing, authentication, or code-compliance acceptance.
- 2026-07-12 - D-APP-56 R5 P40 executed UPD-071: REF-006 current-state kit/register wording now agrees with D-APP-38 MATCH; dated source-warning and assessment history is preserved. No lifecycle transition.
