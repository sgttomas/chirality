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
- [RESOLVED] SOURCE_STATE: D-APP-38 current authority-corpus reconciliation supersedes the prior REF-006 source-state warning; PRD-derived runtime details are accepted for this tranche.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` anchor was recorded.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE `IMPLEMENTS_NODE` anchor was recorded.
- 2026-06-16 SCC-SAFE-MOVES-001 decomposed `DEP-03-01-005` from a coarse deliverable edge into document-scoped conformance/interface evidence; the row remains active and in objective.

## Extracted Dependency Register

`Dependencies.csv` v3.1 contains 8 ACTIVE rows.

| DependencyID | Class | Type | Direction | Target | Status | Satisfaction |
|---|---:|---:|---:|---|---:|---:|
| DEP-03-01-001 | ANCHOR | OTHER | UPSTREAM | SOW-037 Product-owned engine contract | ACTIVE | SATISFIED |
| DEP-03-01-002 | ANCHOR | OTHER | UPSTREAM | OBJ-002 Runtime architecture objective | ACTIVE | SATISFIED |
| DEP-03-01-003 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-04-01 SDK Probe and Version-Pinned Adoption Decision | ACTIVE | PENDING |
| DEP-03-01-004 | EXECUTION | CONSTRAINT | UPSTREAM | REF-006 `docs/PRD.md` | ACTIVE | SATISFIED |
| DEP-03-01-005 | EXECUTION | INTERFACE | UPSTREAM | DOCUMENT DEL-03-03-SPEC-SCOPE Harness API/SSE compatibility adapter scope | ACTIVE | PENDING |
| DEP-03-01-006 | EXECUTION | INTERFACE | UPSTREAM | DEL-03-04 Interrupt Cancel and Terminal Outcome Handling | ACTIVE | PENDING |
| DEP-03-01-007 | EXECUTION | INTERFACE | UPSTREAM | DEL-01-02 Reliance Boundary Register | ACTIVE | PENDING |
| DEP-03-01-008 | EXECUTION | HANDOVER | DOWNSTREAM | DEL-09-02 Section 9 Runtime Validation Additions | ACTIVE | PENDING |

## Lifecycle Summary

| Measure | Count |
|---|---:|
| ACTIVE rows | 8 |
| RETIRED rows | 0 |
| ANCHOR rows | 2 |
| EXECUTION rows | 6 |
| SATISFIED rows | 3 |
| PENDING rows | 5 |
| TBD satisfaction rows | 0 |

## Run History

| Timestamp | Mode | Strictness | Decomposition Status | ACTIVE Count | Warnings |
|---|---|---|---|---:|---|
| 2026-06-21T03:00:20-0600 | ADQ-05 | CONSERVATIVE | D-APP-38 current authority corpus and D-APP-40 runtime taxonomy applied | 8 | none |
| 2026-05-20T19:30:46-0600 | UPDATE | CONSERVATIVE | FOUND: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | 8 | superseded source-state warning |
