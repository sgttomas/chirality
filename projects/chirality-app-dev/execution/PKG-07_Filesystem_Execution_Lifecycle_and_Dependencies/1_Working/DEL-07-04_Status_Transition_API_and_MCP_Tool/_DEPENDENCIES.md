# Dependencies: DEL-07-04 Status Transition API and MCP Tool

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
- Source set used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Source set excluded by human ruling: `_SEMANTIC.md` was not read or consumed; semantic lensing and P3 enrichment are skipped.
- Anchor doc selection: `Datasheet.md` plus `_CONTEXT.md` traceability and decomposition validation.
- Execution doc order: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`, `_REFERENCES.md`.
- Decomposition status: available; DEL-07-04, SOW-028, OBJ-006, PKG-07, and referenced document metadata were validated against allowed evidence.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` parent anchor exists.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE `IMPLEMENTS_NODE` parent anchor exists.
- `[WARNING] PRD_HASH_MISMATCH`: `_REFERENCES.md` lists `docs/PRD.md` as `HASH_MISMATCH`; PRD-derived acceptance details remain warned evidence.
- `[WARNING] IMPLEMENTATION_LOCATION_TBD`: allowed evidence names no implementation module path; dependency row DEL-07-04-DEP-008 preserves the target as `UNKNOWN` / `TBD`.

## Extracted Dependency Register

`Dependencies.csv` v3.1 was populated on 2026-05-20 in `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.

| DependencyID | Class | Type | Direction | TargetType | TargetRefID | TargetName | Status |
|---|---|---|---|---|---|---|---|
| DEL-07-04-DEP-001 | ANCHOR | OTHER | UPSTREAM | WBS_NODE | SOW-028 | Status lifecycle and approval SHA | ACTIVE |
| DEL-07-04-DEP-002 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | OBJ-006 | Preserve filesystem project truth through working-root containment | ACTIVE |
| DEL-07-04-DEP-003 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | REF-003 | docs/SPEC.md | ACTIVE |
| DEL-07-04-DEP-004 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | REF-002 | docs/CONTRACT.md | ACTIVE |
| DEL-07-04-DEP-005 | EXECUTION | CONSTRAINT | UPSTREAM | DOCUMENT | REF-006 | docs/PRD.md | ACTIVE |
| DEL-07-04-DEP-006 | EXECUTION | CONSTRAINT | UPSTREAM | DOCUMENT | REF-001 | docs/DIRECTIVE.md | ACTIVE |
| DEL-07-04-DEP-007 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | REF-004 | docs/TYPES.md | ACTIVE |
| DEL-07-04-DEP-008 | EXECUTION | PREREQUISITE | UPSTREAM | UNKNOWN | TBD | Implementation module location | ACTIVE |

Counts:

| Group | Count |
|---|---:|
| ACTIVE rows | 8 |
| RETIRED rows | 0 |
| ANCHOR rows | 2 |
| EXECUTION rows | 6 |
| OTHER rows | 2 |
| PREREQUISITE rows | 4 |
| CONSTRAINT rows | 2 |

## Run History

| Timestamp | Mode | Strictness | Decomposition path/status | Warnings | ACTIVE rows |
|---|---|---|---|---|---:|
| 2026-05-20T19:54:21-06:00 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` / available | PRD_HASH_MISMATCH; IMPLEMENTATION_LOCATION_TBD | 8 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 8 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| NOT_APPLICABLE | 2 |
| PENDING | 4 |
| TBD | 2 |
