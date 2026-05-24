# Dependencies: DEL-07-05 Dependencies.csv v3.1 Reader, Writer, and Linter

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

TBD - no accepted declared dependency edges have been provided. Current register rows are `Origin=EXTRACTED`.

## Declared Downstream

TBD - no accepted declared dependency edges have been provided. Current register rows are `Origin=EXTRACTED`.

## Extracted Dependency Register

`Dependencies.csv` was created with 26 ACTIVE extracted rows.

| Count Type | Count |
|---|---:|
| Total rows | 26 |
| ACTIVE rows | 26 |
| RETIRED rows | 0 |
| ANCHOR rows | 20 |
| EXECUTION rows | 6 |
| Parent anchors (`IMPLEMENTS_NODE`) | 1 |
| Requirement/objective trace anchors | 19 |

### Counts by Dependency Type

| DependencyType | Count |
|---|---:|
| OTHER | 20 |
| PREREQUISITE | 3 |
| CONSTRAINT | 2 |
| INTERFACE | 1 |

### Counts by Status

| Status | Count |
|---|---:|
| ACTIVE | 26 |
| RETIRED | 0 |

### Compact Register

| DependencyID | Class | Direction | Type | Target | Status |
|---|---|---|---|---|---|
| DEP-07-05-001 | ANCHOR | UPSTREAM | OTHER | SOW-029 Dependencies CSV v3.1 | ACTIVE |
| DEP-07-05-002 | ANCHOR | UPSTREAM | OTHER | OBJ-006 Filesystem governance objective | ACTIVE |
| DEP-07-05-003 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-001 | ACTIVE |
| DEP-07-05-004 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-002 | ACTIVE |
| DEP-07-05-005 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-003 | ACTIVE |
| DEP-07-05-006 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-004 | ACTIVE |
| DEP-07-05-007 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-005 | ACTIVE |
| DEP-07-05-008 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-006 | ACTIVE |
| DEP-07-05-009 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-007 | ACTIVE |
| DEP-07-05-010 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-008 | ACTIVE |
| DEP-07-05-011 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-009 | ACTIVE |
| DEP-07-05-012 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-010 | ACTIVE |
| DEP-07-05-013 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-011 | ACTIVE |
| DEP-07-05-014 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-012 | ACTIVE |
| DEP-07-05-015 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-013 | ACTIVE |
| DEP-07-05-016 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-014 | ACTIVE |
| DEP-07-05-017 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-015 | ACTIVE |
| DEP-07-05-018 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-016 | ACTIVE |
| DEP-07-05-019 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-017 | ACTIVE |
| DEP-07-05-020 | ANCHOR | UPSTREAM | OTHER | REQ-DEL-07-05-018 | ACTIVE |
| DEP-07-05-021 | EXECUTION | UPSTREAM | PREREQUISITE | Accepted source references | ACTIVE |
| DEP-07-05-022 | EXECUTION | UPSTREAM | PREREQUISITE | v3.1 schema and enum vocabulary | ACTIVE |
| DEP-07-05-023 | EXECUTION | UPSTREAM | PREREQUISITE | Dependency authority model | ACTIVE |
| DEP-07-05-024 | EXECUTION | UPSTREAM | CONSTRAINT | Working-root write policy | ACTIVE |
| DEP-07-05-025 | EXECUTION | DOWNSTREAM | INTERFACE | Dependency API and MCP contract surfaces | ACTIVE |
| DEP-07-05-026 | EXECUTION | UPSTREAM | CONSTRAINT | docs/PRD.md hash mismatch warning | ACTIVE |

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- TASK run `TASK_RUN_2026-05-20_1954.md` used `TaskSkill=dependency-extract`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, and `CONSUMER_CONTEXT=NONE`.
- Decomposition authority used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Source document selection: `ANCHOR_DOC=Datasheet.md`; `EXECUTION_DOC_ORDER=Specification.md, Guidance.md, Procedure.md`; `_CONTEXT.md`, `_REFERENCES.md`, and existing `_DEPENDENCIES.md` were used for identity, reference, and declared-edge context.
- Human ruling applied: semantic lensing and P3 enrichment were skipped; `_SEMANTIC.md` was invalid evidence and was not read or consumed.
- Parent anchor check passed: one ACTIVE `IMPLEMENTS_NODE` row was found for `SOW-029`.
- No declared rows were present to preserve or merge. All rows in this run are extracted rows.
- [WARNING] OBJECTIVE_TARGET_TYPE_UNAVAILABLE: `OBJ-006` is explicit evidence, but the v3.1 `TargetType` enum has no `OBJECTIVE`; the row preserves `TargetType=UNKNOWN`.
- [WARNING] UNKNOWN_INTERFACE_CONSUMER: the API/MCP dependency surface is explicit, but no consumer deliverable ID is explicitly named in the evidence; the row preserves `TargetType=UNKNOWN`.
- [WARNING] SOURCE_HASH_MISMATCH: `_REFERENCES.md` records `REF-006` / `docs/PRD.md` as `HASH_MISMATCH`; the warning is preserved as an execution constraint.

## Run History

| Timestamp | Mode | Strictness | Decomposition Status | Warnings | ACTIVE Rows |
|---|---|---|---|---|---:|
| 2026-05-20 19:54 | UPDATE | CONSERVATIVE | Found v3.2 decomposition authority | OBJECTIVE_TARGET_TYPE_UNAVAILABLE; UNKNOWN_INTERFACE_CONSUMER; SOURCE_HASH_MISMATCH | 26 |

## Lifecycle Summary

| Field | Count |
|---|---:|
| ACTIVE | 26 |
| RETIRED | 0 |
| RequiredMaturity=SEMANTIC_READY | 26 |
| ProposedMaturity=TBD | 26 |
| SatisfactionStatus=TBD | 26 |

No downstream handoff section was added because `CONSUMER_CONTEXT=NONE`.
