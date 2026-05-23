# Dependencies: DEL-05-03 Redacted RunLogger and Secret Hygiene

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
- TASK dependency-extract run on 2026-05-20 used MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE.
- Decomposition authority: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` located and used for anchor and target resolution.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Human ruling applied: semantic lensing and P3 enrichment skipped; `_SEMANTIC.md` was not read or consumed as evidence.
- `[WARNING] REF-006_HASH_MISMATCH`: `_REFERENCES.md` reports `docs/PRD.md` hash mismatch. Rows using PRD-derived requirements retain the source-state warning and are not sole-authority closure evidence.
- `[WARNING] UNKNOWN_TBD_RETAINED`: final redaction helper path, run logger path, configured-secret schema, replacement token, and exact policy integration point remain TBD in source documents.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` parent anchor is present.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE parent anchor is present.

## Extracted Dependency Register

| DependencyID | Class | Type | Direction | Target | Status | Satisfaction |
|---|---|---|---|---|---|---|
| DEP-DEL-05-03-001 | ANCHOR | OTHER | UPSTREAM | PKG-05 Session Audit, Replay, and Tool Result Records | ACTIVE | SATISFIED |
| DEP-DEL-05-03-002 | ANCHOR | OTHER | UPSTREAM | SOW-021 Provider error classification | ACTIVE | SATISFIED |
| DEP-DEL-05-03-003 | ANCHOR | OTHER | UPSTREAM | SOW-041 Runtime redaction | ACTIVE | SATISFIED |
| DEP-DEL-05-03-004 | ANCHOR | OTHER | UPSTREAM | OBJ-003 Chirality-owned session auditability | ACTIVE | SATISFIED |
| DEP-DEL-05-03-005 | ANCHOR | OTHER | UPSTREAM | OBJ-008 Repeatable validation/key/security checks | ACTIVE | SATISFIED |
| DEP-DEL-05-03-006 | EXECUTION | PREREQUISITE | UPSTREAM | REF-002 `docs/CONTRACT.md` | ACTIVE | SATISFIED |
| DEP-DEL-05-03-007 | EXECUTION | PREREQUISITE | UPSTREAM | REF-003 `docs/SPEC.md` | ACTIVE | SATISFIED |
| DEP-DEL-05-03-008 | EXECUTION | PREREQUISITE | UPSTREAM | REF-005 `docs/PLAN.md` | ACTIVE | SATISFIED |
| DEP-DEL-05-03-009 | EXECUTION | CONSTRAINT | UPSTREAM | REF-006 `docs/PRD.md` hash-mismatch warning | ACTIVE | PENDING |
| DEP-DEL-05-03-010 | EXECUTION | INTERFACE | UPSTREAM | DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge | ACTIVE | PENDING |
| DEP-DEL-05-03-011 | EXECUTION | INTERFACE | UPSTREAM | DEL-05-02 HarnessEvent Schema and Append-Only JSONL | ACTIVE | PENDING |
| DEP-DEL-05-03-012 | EXECUTION | CONSTRAINT | DOWNSTREAM | DEL-05-05 ToolResultStore and Session Artifacts | ACTIVE | PENDING |
| DEP-DEL-05-03-013 | EXECUTION | CONSTRAINT | UPSTREAM | UNKNOWN/TBD final module paths and configured-secret schema | ACTIVE | PENDING |

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE rows |
|---|---|---|---|---|---:|
| 2026-05-20T19:41:22-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | REF-006_HASH_MISMATCH; UNKNOWN_TBD_RETAINED | 13 |

## Lifecycle Summary

| Metric | Count |
|---|---:|
| ACTIVE rows | 13 |
| RETIRED rows | 0 |
| ANCHOR rows | 5 |
| EXECUTION rows | 8 |
| UPSTREAM rows | 12 |
| DOWNSTREAM rows | 1 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 8 |
| PENDING | 5 |
