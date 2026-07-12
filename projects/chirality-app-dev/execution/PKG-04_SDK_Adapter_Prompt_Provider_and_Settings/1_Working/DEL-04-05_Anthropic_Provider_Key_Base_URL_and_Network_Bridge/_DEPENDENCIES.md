# Dependencies: DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge

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
- 2026-05-20 dependency-extract UPDATE run used `Datasheet.md` as the anchor document and `Specification.md`, `Guidance.md`, and `Procedure.md` as execution documents.
- Decomposition authority used: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; anchor label resolution succeeded.
- Human ruling applied: semantic lensing and P3 enrichment are skipped; `_SEMANTIC.md` was not read or consumed.
- Strictness: CONSERVATIVE. Unknown implementation paths, SDK error shapes, and Node/SDK network enforcement mechanisms remain `TBD`.
- [RESOLVED 2026-07-12] REF-006 docs/PRD.md is MATCH under D-APP-38; the mismatch warning remains only in dated 2026-05-20 run history.

## Extracted Dependency Register

| DependencyID | Class | Type | Direction | Target | Status | Evidence |
|---|---|---|---|---|---|---|
| DEP-04-05-001 | ANCHOR | OTHER | UPSTREAM | PKG-04 | ACTIVE | `_CONTEXT.md` |
| DEP-04-05-002 | ANCHOR | OTHER | UPSTREAM | SOW-019 | ACTIVE | `Datasheet.md` |
| DEP-04-05-003 | ANCHOR | OTHER | UPSTREAM | SOW-020 | ACTIVE | `Datasheet.md` |
| DEP-04-05-004 | ANCHOR | OTHER | UPSTREAM | SOW-021 | ACTIVE | `Datasheet.md` |
| DEP-04-05-005 | ANCHOR | OTHER | UPSTREAM | OBJ-004 | ACTIVE | `Datasheet.md` |
| DEP-04-05-006 | ANCHOR | OTHER | UPSTREAM | OBJ-008 | ACTIVE | `Datasheet.md` |
| DEP-04-05-007 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-04-01 | ACTIVE | `Procedure.md` |
| DEP-04-05-008 | EXECUTION | INTERFACE | UPSTREAM | DEL-04-02 | ACTIVE | `Specification.md` |
| DEP-04-05-009 | EXECUTION | INTERFACE | DOWNSTREAM | DEL-04-03 | ACTIVE | `Specification.md` |
| DEP-04-05-010 | EXECUTION | INTERFACE | UPSTREAM | DEL-02-05 | ACTIVE | `Specification.md` |
| DEP-04-05-011 | EXECUTION | INTERFACE | UPSTREAM | DEL-05-03 | ACTIVE | `Specification.md` |
| DEP-04-05-012 | EXECUTION | CONSTRAINT | UPSTREAM | REF-006 | RETIRED | `Procedure.md` |

Counts: 12 ACTIVE rows; 6 ANCHOR, 6 EXECUTION.

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 10 |
| RETIRED | 2 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 6 |
| TBD | 4 |

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE Counts |
|---|---|---|---|---|---|
| 2026-05-20T19:35:58-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | SOURCE_STATE REF-006 HASH_MISMATCH | ANCHOR=6; EXECUTION=6 |

## D-APP-56 R5 P40 register annotation (2026-07-12)

REF-006 is MATCH under D-APP-38. Any HASH_MISMATCH token retained in the dated Run History is extraction provenance, not current dependency state. Structured-row status and summary counts above reflect Dependencies.csv after UPD-077..079.
