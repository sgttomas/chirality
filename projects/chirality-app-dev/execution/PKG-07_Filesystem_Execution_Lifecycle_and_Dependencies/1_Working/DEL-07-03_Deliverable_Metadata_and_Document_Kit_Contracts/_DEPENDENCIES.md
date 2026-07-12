# Dependencies: DEL-07-03 Deliverable Metadata and Document Kit Contracts

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

TBD - no declared upstream dependency edges have been accepted by a human.

## Declared Downstream

TBD - no declared downstream dependency edges have been accepted by a human.

## Extracted Dependency Register

| Metric | Count |
|---|---:|
| ACTIVE rows | 10 |
| RETIRED rows | 0 |
| ANCHOR rows | 2 |
| EXECUTION rows | 8 |
| UPSTREAM rows | 10 |
| DOWNSTREAM rows | 0 |

| DependencyID | Class | Type | Target | Status | Evidence |
|---|---|---|---|---|---|
| DEP-07-03-001 | ANCHOR | IMPLEMENTS_NODE / OTHER | SOW-026 Metadata files and document kit | ACTIVE | `Datasheet.md` / Identification |
| DEP-07-03-002 | ANCHOR | TRACES_TO_REQUIREMENT / OTHER | OBJ-006 filesystem project truth objective | ACTIVE | `Datasheet.md` / Identification |
| DEP-07-03-003 | EXECUTION | PREREQUISITE | Accepted decomposition entry for DEL-07-03 | ACTIVE | `Procedure.md` / Prerequisites |
| DEP-07-03-004 | EXECUTION | PREREQUISITE | `docs/SPEC.md` | ACTIVE | `Procedure.md` / Prerequisites |
| DEP-07-03-005 | EXECUTION | PREREQUISITE | `docs/PRD.md` | ACTIVE | `Procedure.md` / Prerequisites |
| DEP-07-03-006 | EXECUTION | PREREQUISITE | `docs/TYPES.md` | ACTIVE | `Procedure.md` / Prerequisites |
| DEP-07-03-007 | EXECUTION | PREREQUISITE | `docs/DIRECTIVE.md` | ACTIVE | `Procedure.md` / Prerequisites |
| DEP-07-03-008 | EXECUTION | PREREQUISITE | `docs/CONTRACT.md` | ACTIVE | `Procedure.md` / Prerequisites |
| DEP-07-03-009 | EXECUTION | CONSTRAINT | DEL-07-04 Status Transition API and MCP Tool | ACTIVE | `Procedure.md` / Steps |
| DEP-07-03-010 | EXECUTION | CONSTRAINT | DEL-07-05 Dependencies.csv v3.1 Reader Writer and Linter | ACTIVE | `Procedure.md` / Steps |

## Run Notes

- Run timestamp: 2026-05-20T19:54:16-0600.
- Mode: UPDATE.
- Strictness: CONSERVATIVE.
- Consumer context: NONE.
- Scope: DEL-07-03.
- Decomposition path: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; status: located and used for anchor/target validation.
- Source documents read for extraction: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Human ruling honored: semantic lensing and P3 enrichment are skipped; `_SEMANTIC.md` was not read or consumed as dependency evidence.
- Anchor document selected: `Datasheet.md`.
- Execution document order selected: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`.
- Existing `Dependencies.csv`: absent before this run; created with v3.1 schema.
- [RESOLVED 2026-07-12] REF-006 docs/PRD.md is MATCH under D-APP-38; the mismatch warning remains only in dated 2026-05-20 run history.
- Implementation location remains TBD in source procedure; no dependency edge was inferred from that unknown.
- Scanner output schema remains TBD in source procedure; no dependency edge was inferred from that unknown.

## Run History

| Timestamp | Mode | Strictness | Decomposition status | Warnings | ACTIVE rows |
|---|---|---|---|---|---:|
| 2026-05-20T19:54:16-0600 | UPDATE | CONSERVATIVE | located: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | SOURCE_HASH_MISMATCH REF-006 | 10 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 10 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| TBD | 10 |

| RequiredMaturity | Count |
|---|---:|
| SEMANTIC_READY | 10 |


## D-APP-56 R5 P40 register annotation (2026-07-12)

REF-006 is MATCH under D-APP-38. Any HASH_MISMATCH token retained in the dated Run History is extraction provenance, not current dependency state. Structured-row status and summary counts above reflect Dependencies.csv after UPD-077..079.
