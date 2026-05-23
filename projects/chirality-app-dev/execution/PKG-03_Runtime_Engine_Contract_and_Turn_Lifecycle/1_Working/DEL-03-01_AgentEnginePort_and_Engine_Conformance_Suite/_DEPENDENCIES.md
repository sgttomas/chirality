# Dependencies: DEL-03-01 AgentEnginePort and Engine Conformance Suite

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
- 2026-05-20 TASK dependency-extract run used `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Decomposition authority: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` located and used to validate target IDs and labels.
- Source selection: `ANCHOR_DOC=Datasheet.md`; `EXECUTION_DOC_ORDER=Specification.md, Procedure.md, Guidance.md`; `_CONTEXT.md`, `_REFERENCES.md`, and this file were used as local metadata inputs.
- Human ruling applied: semantic lensing and P3 enrichment were skipped; `_SEMANTIC.md` was not read and was not used as evidence.
- Existing `Dependencies.csv` was absent before this run; a new v3.1 register was created.
- [WARNING] REF-006_HASH_MISMATCH: `_REFERENCES.md` reports `docs/PRD.md` as `HASH_MISMATCH`; PRD-derived dependency evidence remains active but requires human confirmation before acceptance closure.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` anchor was recorded.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE `IMPLEMENTS_NODE` anchor was recorded.

## Extracted Dependency Register

`Dependencies.csv` v3.1 contains 8 ACTIVE rows.

| DependencyID | Class | Type | Direction | Target | Status | Satisfaction |
|---|---:|---:|---:|---|---:|---:|
| DEP-DEL-03-01-001 | ANCHOR | OTHER | UPSTREAM | SOW-037 Product-owned engine contract | ACTIVE | SATISFIED |
| DEP-DEL-03-01-002 | ANCHOR | OTHER | UPSTREAM | OBJ-002 Runtime architecture objective | ACTIVE | SATISFIED |
| DEP-DEL-03-01-003 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-04-01 SDK Probe and Version-Pinned Adoption Decision | ACTIVE | PENDING |
| DEP-DEL-03-01-004 | EXECUTION | CONSTRAINT | UPSTREAM | REF-006 `docs/PRD.md` | ACTIVE | PENDING |
| DEP-DEL-03-01-005 | EXECUTION | INTERFACE | UPSTREAM | DEL-03-03 Harness API and SSE Compatibility Adapter | ACTIVE | PENDING |
| DEP-DEL-03-01-006 | EXECUTION | INTERFACE | UPSTREAM | DEL-03-04 Interrupt Cancel and Terminal Outcome Handling | ACTIVE | PENDING |
| DEP-DEL-03-01-007 | EXECUTION | INTERFACE | UPSTREAM | DEL-01-02 Reliance Boundary Register | ACTIVE | PENDING |
| DEP-DEL-03-01-008 | EXECUTION | HANDOVER | DOWNSTREAM | DEL-09-02 Section 9 Runtime Validation Additions | ACTIVE | PENDING |

## Lifecycle Summary

| Measure | Count |
|---|---:|
| ACTIVE rows | 8 |
| RETIRED rows | 0 |
| ANCHOR rows | 2 |
| EXECUTION rows | 6 |
| SATISFIED rows | 2 |
| PENDING rows | 6 |
| TBD satisfaction rows | 0 |

## Run History

| Timestamp | Mode | Strictness | Decomposition Status | ACTIVE Count | Warnings |
|---|---|---|---|---:|---|
| 2026-05-20T19:30:46-0600 | UPDATE | CONSERVATIVE | FOUND: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | 8 | REF-006_HASH_MISMATCH |
