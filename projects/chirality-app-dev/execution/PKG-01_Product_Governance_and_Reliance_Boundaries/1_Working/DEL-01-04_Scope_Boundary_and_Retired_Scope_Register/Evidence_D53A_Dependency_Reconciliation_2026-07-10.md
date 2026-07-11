# Evidence D53A - Dependency Reconciliation - DEL-01-04 Scope Boundary and Retired Scope Register

**Date:** 2026-07-10
**Queue row:** DRQ-03 of `plans/PLAN_2026-07-10_pre_issuance_dependency_reconciliation.md`
**Authority:** D-APP-53 ruling (Option A, 2026-07-10), `execution/_Coordination/_DECISIONS/D-APP-53_RULING_2026-07-10.md`

## Epistemic status

This is derivative dependency-reconciliation evidence. It does not replace decomposition truth,
source/test evidence, decision records, or human lifecycle approvals. It authorizes no issuance, no
`CHECKING -> ISSUED` transition, no release act, and no scope change. Satisfaction of a downstream
`CONSTRAINT` row records that the constrained posture is verifiably present in the target today; it
does not waive the constraint going forward.

## Per-row reconciliation

All paths relative to `projects/chirality-app-dev/` unless rooted. Decomposition =
`execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`, re-verified live 2026-07-10.

| DependencyID | Prior | New | Basis / evidence pointer |
|---|---|---|---|
| DEP-01-04-001 | PENDING | SATISFIED | PKG-01 present in decomposition §7 Packages; DEL-01-04 deliverable row (§8) lists PKG-01. |
| DEP-01-04-002 | PENDING | SATISFIED | Decomposition §9 Scope Item Ledger row SOW-065 lists DEL-01-04. |
| DEP-01-04-003 | PENDING | SATISFIED | Decomposition §9 row SOW-076 lists DEL-01-04 (and DEL-04-02). |
| DEP-01-04-004 | PENDING | SATISFIED | Decomposition §9 row SOW-077 lists DEL-01-04 (and DEL-07-06). |
| DEP-01-04-005 | PENDING | SATISFIED | Decomposition §9 row SOW-078 lists DEL-01-04 (and DEL-09-04). |
| DEP-01-04-006 | PENDING | SATISFIED | OBJ-009 present in decomposition §6 Objectives (traces SOW-065, SOW-076-SOW-077); DEL-01-04 deliverable row lists OBJ-009. |
| DEP-01-04-007 | PENDING | SATISFIED | `_CONTEXT.md` present in this deliverable directory. |
| DEP-01-04-008 | PENDING | SATISFIED | `_REFERENCES.md` present; all REF rows MATCH re-verified by live SHA-256 recompute 2026-07-10. |
| DEP-01-04-009 | PENDING | SATISFIED | Decomposition file present in live tree with the DEL-01-04 deliverable row (§8). |
| DEP-01-04-010 | PENDING | SATISFIED | Constraint implemented in target: `frontend/src/lib/harness/sdk-options-builder.ts` defaults `settingSources` to `[]` (`parseSettingSources`) and maps `bypass` to `bypassPermissions` only behind `CHIRALITY_ALLOW_SDK_BYPASS=1`; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` asserts empty settingSources and the gated bypass. |
| DEP-01-04-011 | PENDING | SATISFIED | Constraint present in target: `execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-06_Reference_Hash_and_Snapshot_Conventions/Specification.md` out-of-scope list and DEL-07-06-REQ-012 keep retired hardening/PKG-08 scope retired. |
| DEP-01-04-012 | PENDING | SATISFIED | Constraint present in target: `execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/Specification.md` DEL-09-04-REQ-001/REQ-010 and out-of-scope list keep Windows/Linux packaging out absent a governed amendment. |
| DEP-01-04-013 | PENDING | SATISFIED | Constraint present in target: `execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/` holds the five future-boundary deliverables; decomposition §7 PKG-10 row excludes current-release domain operation execution and OI-005 requires amendment before implementation; PKG-10 Specifications record the amendment gate. |

Rows closed: 13. Rows left open: 0. For every closed row `ProposedMaturity` was set to the row's
`RequiredMaturity` (`SEMANTIC_READY`) and `LastSeen` bumped to 2026-07-10.

## Hygiene: summary/pointer repairs

- No row-level pointer repairs were needed; all TargetLocation values resolved as recorded.
  Note: `DEP-01-04-011`'s human-readable target sits under the live package directory name
  `PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies`; the row's `TargetLocation` points at the
  decomposition row (not a filesystem path) and needed no repair.
- `_DEPENDENCIES.md`: lifecycle summary updated (`SatisfactionStatus=PENDING 13` ->
  `SatisfactionStatus=SATISFIED 13`); closure-state sentence refreshed; dated run note and Run History
  row appended.

## Validation

`python3 execution/_Scripts/validate_dependencies.py <this deliverable>/Dependencies.csv` -> PASS,
13 rows, 0 errors, 0 warnings (2026-07-10).
