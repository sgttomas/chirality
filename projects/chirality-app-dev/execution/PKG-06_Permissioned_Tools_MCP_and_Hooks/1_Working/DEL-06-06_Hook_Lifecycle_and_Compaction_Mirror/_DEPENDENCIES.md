# Dependencies: DEL-06-06 Hook Lifecycle and Compaction Mirror

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

## Prior Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.

## Extracted Dependency Register

Run timestamp: 2026-05-20T19:47:33-0600

| Metric | Count |
|---|---:|
| Total rows | 8 |
| ACTIVE rows | 8 |
| RETIRED rows | 0 |
| ANCHOR rows | 3 |
| EXECUTION rows | 5 |

| DependencyID | Class | Type | Direction | Target | Status | Evidence |
|---|---|---|---|---|---|---|
| DEP-06-06-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | PKG-06 Permissioned Tools, MCP, and Hooks | ACTIVE | `_CONTEXT.md` |
| DEP-06-06-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | SOW-057 Hooks and fail-closed behavior | ACTIVE | `Specification.md` |
| DEP-06-06-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | SOW-061 Compaction mirror | ACTIVE | `Specification.md` |
| DEP-06-06-004 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-05-02 HarnessEvent Schema and Append-Only JSONL | ACTIVE | `Specification.md` |
| DEP-06-06-005 | EXECUTION | INTERFACE | UPSTREAM | DEL-06-04 Write/Edit Surface and Path Hooks | ACTIVE | `Specification.md` |
| DEP-06-06-006 | EXECUTION | INTERFACE | UPSTREAM | DEL-03-04 Interrupt, Cancel, and Terminal Outcome Handling | ACTIVE | `Guidance.md` |
| DEP-06-06-007 | EXECUTION | HANDOVER | DOWNSTREAM | DEL-09-02 Section 9 Runtime Validation Additions | ACTIVE | `Procedure.md` |
| DEP-06-06-008 | EXECUTION | CONSTRAINT | UPSTREAM | REF-006 `docs/PRD.md` HASH_MISMATCH | ACTIVE | `Specification.md` |

## Run Notes

- MODE: UPDATE.
- STRICTNESS: CONSERVATIVE.
- CONSUMER_CONTEXT: NONE.
- SCOPE: DEL-06-06.
- RUN_ROOT: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution`.
- DECOMPOSITION_PATH: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Source documents read for dependency extraction: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Existing `_SEMANTIC.md` was not read or consumed per human ruling; semantic lensing and P3 enrichment were skipped.
- `Dependencies.csv` was missing at run start and was created with v3.1 schema columns.
- Anchor document selection: `Datasheet.md` plus `_CONTEXT.md` traceability fields; decomposition used to validate PKG-06, DEL-06-06, SOW-057, and SOW-061.
- Execution document order: `Specification.md`, `Guidance.md`, `Procedure.md`.
- Parent anchor check: PASS; one ACTIVE `IMPLEMENTS_NODE` anchor is present.
- [WARNING] SOURCE_HASH_MISMATCH_REF-006: `_REFERENCES.md` marks `docs/PRD.md` as HASH_MISMATCH; PRD-only compaction payload specifics remain warning-qualified.
- Exact implementation module paths, test fixture paths, payload fields, event writer API path, and parent/child event relation remain `TBD`.

## Run History

| Timestamp | Mode | Strictness | Decomposition status | Warnings | ACTIVE ANCHOR | ACTIVE EXECUTION |
|---|---|---|---|---|---:|---:|
| 2026-05-20T19:47:33-0600 | UPDATE | CONSERVATIVE | Provided and used: `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | SOURCE_HASH_MISMATCH_REF-006 | 3 | 5 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 8 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| NOT_APPLICABLE | 3 |
| PENDING | 5 |
