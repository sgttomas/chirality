# Dependencies: DEL-07-06 Reference Hash and Snapshot Conventions

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
- 2026-05-20 dependency-recording run used `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority at `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Human ruling applied: semantic lensing and P3 enrichment were skipped; `_SEMANTIC.md` was not read or consumed and is not evidence for this register.
- Anchor doc selected: `Datasheet.md` with `_CONTEXT.md` and decomposition authority for validation.
- Execution doc order selected: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`, `_REFERENCES.md`, `_CONTEXT.md`, `_DEPENDENCIES.md`.
- `[WARNING] SOURCE_HASH_MISMATCH: REF-006 docs/PRD.md remains HASH_MISMATCH in _REFERENCES.md; PRD-derived dependency statements stay warning-qualified until reconciled or accepted.`
- `[WARNING] TARGET_NOT_READ: _STATUS.md is an explicit Procedure prerequisite target, but it was not read or consumed because the dependency-recording ruling restricted evidence sources. Satisfaction remains TBD.`
- `[WARNING] DEPENDENCY_EDGES_TBD: Procedure names accepted dependency edges as a prerequisite, while existing _DEPENDENCIES.md declares no accepted upstream/downstream edges yet.`
- Parent anchor check: one ACTIVE `IMPLEMENTS_NODE` row found; no `FLOATING_NODE` or `AMBIGUOUS_ANCHOR` warning.

## Extracted Dependency Register

Current register: `Dependencies.csv` v3.1.

| Count Type | Value |
|---|---:|
| Total rows | 13 |
| ACTIVE rows | 13 |
| RETIRED rows | 0 |
| ANCHOR rows | 6 |
| EXECUTION rows | 7 |
| Parent anchors (`IMPLEMENTS_NODE`) | 1 |
| Trace anchors (`TRACES_TO_REQUIREMENT`) | 5 |

| DependencyID | Class | Type | Direction | Target | Status | Evidence |
|---|---|---|---|---|---|---|
| DEL-07-06-DEP-001 | ANCHOR | OTHER | UPSTREAM | DEL-07-06 | ACTIVE | `_CONTEXT.md#Identity`; decomposition DEL-07-06 |
| DEL-07-06-DEP-002 | ANCHOR | OTHER | UPSTREAM | SOW-032 | ACTIVE | `Datasheet.md#Attributes`; decomposition SOW-032 |
| DEL-07-06-DEP-003 | ANCHOR | OTHER | UPSTREAM | SOW-033 | ACTIVE | `Datasheet.md#Attributes`; decomposition SOW-033 |
| DEL-07-06-DEP-004 | ANCHOR | OTHER | UPSTREAM | SOW-034 | ACTIVE | `Datasheet.md#Attributes`; decomposition SOW-034 |
| DEL-07-06-DEP-005 | ANCHOR | OTHER | UPSTREAM | OBJ-006 | ACTIVE | `_CONTEXT.md#Traceability`; decomposition OBJ-006 |
| DEL-07-06-DEP-006 | ANCHOR | OTHER | UPSTREAM | OBJ-009 | ACTIVE | `_CONTEXT.md#Traceability`; decomposition OBJ-009 |
| DEL-07-06-DEP-007 | EXECUTION | PREREQUISITE | UPSTREAM | `_CONTEXT.md` | ACTIVE | `Procedure.md#Prerequisites` |
| DEL-07-06-DEP-008 | EXECUTION | PREREQUISITE | UPSTREAM | `_REFERENCES.md` | ACTIVE | `Procedure.md#Steps` |
| DEL-07-06-DEP-009 | EXECUTION | PREREQUISITE | UPSTREAM | `_DEPENDENCIES.md` | ACTIVE | `Procedure.md#Prerequisites` |
| DEL-07-06-DEP-010 | EXECUTION | PREREQUISITE | UPSTREAM | `_STATUS.md` | ACTIVE | `Procedure.md#Prerequisites`; target not read |
| DEL-07-06-DEP-011 | EXECUTION | PREREQUISITE | UPSTREAM | decomposition v3.2 | ACTIVE | `Procedure.md#Steps` |
| DEL-07-06-DEP-012 | EXECUTION | PREREQUISITE | UPSTREAM | authoritative source corpus | ACTIVE | `Procedure.md#Prerequisites` |
| DEL-07-06-DEP-013 | EXECUTION | CONSTRAINT | UPSTREAM | REF-006 `docs/PRD.md` | ACTIVE | `Specification.md#Requirements`; `_REFERENCES.md` REF-006 |

## Lifecycle Summary

| Dimension | Count |
|---|---:|
| ACTIVE | 13 |
| RETIRED | 0 |
| Satisfaction `TBD` | 13 |
| Satisfaction `PENDING` | 0 |
| Satisfaction `IN_PROGRESS` | 0 |
| Satisfaction `SATISFIED` | 0 |
| Satisfaction `WAIVED` | 0 |
| Satisfaction `NOT_APPLICABLE` | 0 |

## Run History

| Timestamp | Mode | Strictness | Decomposition Path / Status | Warnings | ACTIVE Counts |
|---|---|---|---|---|---|
| 2026-05-20T19:54:22-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` / found and used | `SOURCE_HASH_MISMATCH`, `TARGET_NOT_READ`, `DEPENDENCY_EDGES_TBD` | 13 total: 6 ANCHOR, 7 EXECUTION |
