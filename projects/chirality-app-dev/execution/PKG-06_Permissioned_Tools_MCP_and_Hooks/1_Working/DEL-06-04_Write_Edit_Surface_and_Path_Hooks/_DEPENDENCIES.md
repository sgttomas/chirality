# Dependencies: DEL-06-04 Write/Edit Surface and Path Hooks

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
- 2026-05-20 dependency-extract run used `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, and `CONSUMER_CONTEXT=NONE`.
- Source documents scanned: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and decomposition authority `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Human ruling applied: semantic lensing and P3 enrichment were skipped; `_SEMANTIC.md` was not read and is not evidence for this register.
- Anchor document selection: `Datasheet.md` and `Specification.md` traceability sections.
- Execution document order: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`.
- Decomposition validation: available and used for package, deliverable, SOW, and objective target resolution.
- `[WARNING] PRD_HASH_MISMATCH`: REF-006 `docs/PRD.md` is source-accessible but hash-mismatched in `_REFERENCES.md`; PRD-derived controlled-write details remain warning-qualified until reconciled.
- `[WARNING] HUMAN_RULING_SEMANTIC_SKIPPED`: inherited `SatisfactionThreshold=SEMANTIC_READY` is not used as evidence in this extraction because semantic lensing was explicitly skipped.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` parent anchor is present.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE `IMPLEMENTS_NODE` parent anchor is present.

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1

| Metric | Count |
|---|---:|
| Total rows | 10 |
| ACTIVE rows | 10 |
| RETIRED rows | 0 |
| ANCHOR rows | 6 |
| EXECUTION rows | 4 |
| IMPLEMENTS_NODE anchors | 1 |
| TRACES_TO_REQUIREMENT anchors | 5 |

| DependencyID | Class | Type | Direction | Target | Status | Satisfaction |
|---|---|---|---|---|---|---|
| DEP-DEL-06-04-001 | ANCHOR | OTHER | UPSTREAM | PKG-06 | ACTIVE | NOT_APPLICABLE |
| DEP-DEL-06-04-002 | ANCHOR | OTHER | UPSTREAM | SOW-027 | ACTIVE | NOT_APPLICABLE |
| DEP-DEL-06-04-003 | ANCHOR | OTHER | UPSTREAM | SOW-057 | ACTIVE | NOT_APPLICABLE |
| DEP-DEL-06-04-004 | ANCHOR | OTHER | UPSTREAM | SOW-060 | ACTIVE | NOT_APPLICABLE |
| DEP-DEL-06-04-005 | ANCHOR | OTHER | UPSTREAM | OBJ-005 | ACTIVE | NOT_APPLICABLE |
| DEP-DEL-06-04-006 | ANCHOR | OTHER | UPSTREAM | OBJ-006 | ACTIVE | NOT_APPLICABLE |
| DEP-DEL-06-04-007 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-06-01 | ACTIVE | PENDING |
| DEP-DEL-06-04-008 | EXECUTION | INTERFACE | UPSTREAM | DEL-07-01 | ACTIVE | PENDING |
| DEP-DEL-06-04-009 | EXECUTION | INTERFACE | UPSTREAM | DEL-06-06 | ACTIVE | PENDING |
| DEP-DEL-06-04-010 | EXECUTION | CONSTRAINT | UPSTREAM | REF-006 | ACTIVE | PENDING |

## Run History

| Timestamp | Mode | Strictness | Decomposition path/status | Warnings | ACTIVE counts |
|---|---|---|---|---|---|
| 2026-05-20T19:47:30-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` / available | PRD_HASH_MISMATCH; HUMAN_RULING_SEMANTIC_SKIPPED | ANCHOR=6; EXECUTION=4; TOTAL=10 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 10 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| NOT_APPLICABLE | 6 |
| PENDING | 4 |

Closure state: dependency register initialized, but execution edges remain `PENDING` because upstream maturity and PRD hash reconciliation are not yet accepted in this local evidence set.
