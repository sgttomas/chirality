# Dependencies: DEL-08-05 Subagent Child Run Records and Artifacts

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

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1

Extraction timestamp: 2026-05-20T20:55:00-0600

| Count Type | Value |
|---|---:|
| Total rows | 10 |
| ACTIVE rows | 10 |
| RETIRED rows | 0 |
| ANCHOR rows | 3 |
| EXECUTION rows | 7 |
| Parent anchors (`IMPLEMENTS_NODE`) | 1 |
| Trace anchors (`TRACES_TO_REQUIREMENT`) | 2 |

| DependencyID | Class | Type / Anchor | Direction | TargetType | Target | Status |
|---|---|---|---|---|---|---|
| DEP-08-05-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | WBS_NODE | SOW-063 Governed subagent runtime | ACTIVE |
| DEP-08-05-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-003 Auditable Chirality-owned session records | ACTIVE |
| DEP-08-05-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | OBJ-007 Agent-suite integrity and governed subagent delegation | ACTIVE |
| DEP-08-05-004 | EXECUTION | PREREQUISITE | UPSTREAM | DELIVERABLE | DEL-08-04 Type 2 Subagent Governance Bridge | ACTIVE |
| DEP-08-05-005 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | Runtime event schema and HarnessEvent | ACTIVE |
| DEP-08-05-006 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | Artifact storage policy | ACTIVE |
| DEP-08-05-007 | EXECUTION | CONSTRAINT | UPSTREAM | DOCUMENT | Runtime redaction policy | ACTIVE |
| DEP-08-05-008 | EXECUTION | CONSTRAINT | UPSTREAM | DOCUMENT | SDK transcript metadata boundary | ACTIVE |
| DEP-08-05-009 | EXECUTION | CONSTRAINT | UPSTREAM | DOCUMENT | Retired unified pipeline run record boundary | ACTIVE |
| DEP-08-05-010 | EXECUTION | CONSTRAINT | UPSTREAM | DOCUMENT | D-APP-40 denied child-run allocation boundary | ACTIVE |

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- TASK + dependency-extract run on 2026-05-20T20:55:00-0600 with `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Decomposition authority used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Human ruling honored: `_SEMANTIC.md` was not read or consumed; semantic lensing and P3 enrichment were skipped.
- `ANCHOR_DOC=AUTO` selected `_CONTEXT.md` and `Datasheet.md` traceability fields for explicit identifiers.
- `EXECUTION_DOC_ORDER=AUTO` used `Procedure.md`, `Specification.md`, `Guidance.md`, and `Datasheet.md` for execution prerequisites and constraints.
- No `[WARNING] FLOATING_NODE`: one ACTIVE parent anchor was found.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE parent anchor was found.
- `[RESOLVED] SOURCE_STATE`: D-APP-38 current authority-corpus reconciliation supersedes the prior PRD source-state warning for this tranche.
- `[RESOLVED] HUMAN_RULING_APPLIED`: D-APP-40 resolves denied child-run allocation semantics; denied `ChildRunRecord` evidence is required only after the runtime reaches the child-run record layer.
- Schema validation passed: 29 required columns and 10 data rows.

## Run History

| Timestamp | Mode | Strictness | Decomposition Status | ACTIVE Rows | Warnings |
|---|---|---|---|---:|---|
| 2026-06-21T03:00:20-0600 | ADQ-05 | CONSERVATIVE | D-APP-38 current authority corpus and D-APP-40 child-run taxonomy applied | 10 | none |
| 2026-05-20T20:55:00-0600 | UPDATE | CONSERVATIVE | Found and used explicit path | 10 | superseded source-state warning; superseded denied-allocation ruling request |

## Lifecycle Summary

| Group | ACTIVE | RETIRED |
|---|---:|---:|
| All rows | 10 | 0 |
| ANCHOR | 3 | 0 |
| EXECUTION | 7 | 0 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 4 |
| TBD | 6 |
