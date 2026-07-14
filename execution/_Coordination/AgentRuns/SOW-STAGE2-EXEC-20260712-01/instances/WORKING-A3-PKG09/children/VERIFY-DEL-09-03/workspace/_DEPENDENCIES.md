# Dependencies: DEL-09-03 Unit and Integration Test Expansion

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

TBD - no accepted dependency edges have been extracted yet.

## Declared Downstream

TBD - no accepted dependency edges have been extracted yet.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 dependency-extract update applied current human ruling: semantic lensing and P3 enrichment skipped; `_SEMANTIC.md` is invalid evidence and was not read or consumed.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and decomposition authority `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Defaults and overrides: `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`; `SOURCE_DOCS=AUTO`; `DOC_ROLE_MAP=DEFAULT`; `ANCHOR_DOC=Datasheet.md`; `EXECUTION_DOC_ORDER=Procedure.md, Guidance.md, Specification.md`.
- [WARNING] PRD_HASH_MISMATCH: `_REFERENCES.md` reports REF-006 expected SHA does not match observed SHA. Existing source files treat this as a warning, not a blocker.
- [WARNING] SOURCE_CONFLICT_SUPERSEDED: earlier four-document initialization text said `Dependencies.csv` must not be created yet; current human dependency-recording ruling superseded that deferral for this run.
- Conservative extraction emitted explicit anchors and one explicit execution interface only. Implementation-surface prerequisites remain `TBD` where not directly stated as accepted dependency edges.
- 2026-07-10 correction (D-APP-53 reconciliation): the 2026-05-20 `[WARNING] PRD_HASH_MISMATCH` above is stale and no longer describes live state — `_REFERENCES.md` line 12 now records REF-006 (`docs/PRD.md`) expected SHA `ac35fba4...` matching observed SHA, Status MATCH. The historical warning is retained above for provenance; it should not be relied on.

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1

| Class | Type / AnchorType | Status | Count |
|---|---:|---|---:|
| ANCHOR | IMPLEMENTS_NODE | ACTIVE | 1 |
| ANCHOR | TRACES_TO_REQUIREMENT | ACTIVE | 11 |
| EXECUTION | INTERFACE | ACTIVE | 1 |

| DependencyID | Class | Type / AnchorType | Direction | Target | Status |
|---|---|---|---|---|---|
| DEP-09-03-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | PKG-09 Validation, Packaging, Security, and Release | ACTIVE |
| DEP-09-03-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | SOW-011 SSE turn stream and session locking | ACTIVE |
| DEP-09-03-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | SOW-012 Interrupt/cancel/failure cleanup | ACTIVE |
| DEP-09-03-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | SOW-014 Persist accepted user input before execution | ACTIVE |
| DEP-09-03-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | SOW-015 Persist terminal turn outcomes | ACTIVE |
| DEP-09-03-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | SOW-022 Attachment resolver validation | ACTIVE |
| DEP-09-03-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | SOW-028 Status lifecycle and approval SHA | ACTIVE |
| DEP-09-03-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | SOW-029 Dependencies CSV v3.1 | ACTIVE |
| DEP-09-03-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OBJ-002 Runtime architecture objective | ACTIVE |
| DEP-09-03-010 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OBJ-003 Audit and session objective | ACTIVE |
| DEP-09-03-011 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OBJ-006 Filesystem governance objective | ACTIVE |
| DEP-09-03-012 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OBJ-008 Release readiness objective | ACTIVE |
| DEP-09-03-013 | EXECUTION | INTERFACE | UPSTREAM | DEL-09-02 Section 9 Runtime Validation Additions | ACTIVE |

## Run History

- 2026-05-20 21:02 MDT — `TASK + dependency-extract`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, decomposition found and used at `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; warnings: PRD hash mismatch, superseded dependency deferral note; ACTIVE counts: ANCHOR 12, EXECUTION 1.
- 2026-07-10 — D-APP-53 reconciliation (DRQ-05, `plans/PLAN_2026-07-10_pre_issuance_dependency_reconciliation.md`): all 13 rows re-verified against live evidence and moved `SatisfactionStatus` TBD -> SATISFIED; 12 stale decomposition line pointers refreshed (+6 offset; PKG-09 anchor 350->269); stale PRD_HASH_MISMATCH warning corrected with dated note. Reconciliation record: `Evidence_D53A_Dependency_Reconciliation_2026-07-10.md`. Linter PASS (13 rows, 0 errors, 0 warnings). No lifecycle transition; `_STATUS.md` untouched.

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 13 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 13 |
| TBD | 0 |
