# Dependencies: DEL-02-02 Workbench and Pipeline Selection UX

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
- 2026-05-20 TASK + dependency-extract ran with `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Decomposition path used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (found).
- Source docs used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority. `_SEMANTIC.md` was not read or consumed per human ruling.
- Anchor doc selected: `Datasheet.md`; execution doc order selected: `Specification.md`, `Guidance.md`, `Procedure.md`.
- [WARNING] PRD_HASH_MISMATCH: `_REFERENCES.md` records a hash mismatch for `docs/PRD.md`; dependency extraction treated this as a source warning, not a blocker.
- [WARNING] SOW_007_OWNER_OVERLAP: `_CONTEXT.md` and the deliverable ledger list SOW-007 under DEL-02-02, while the scope ledger marks PKG-08 / DEL-08-03 as primary owner for Pipeline selectors. Rows preserve this as conflict/TBD rather than resolving it.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` anchor is present.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present.

## Extracted Dependency Register

`Dependencies.csv` v3.1 now contains 9 ACTIVE extracted rows.

| DependencyID | Class | Type | Direction | Target | Status | Note |
|---|---|---|---|---|---|---|
| DEP-02-02-001 | ANCHOR | OTHER | UPSTREAM | PKG-02 | ACTIVE | Parent package anchor. |
| DEP-02-02-002 | ANCHOR | OTHER | UPSTREAM | SOW-006 | ACTIVE | Workbench context trace. |
| DEP-02-02-003 | ANCHOR | OTHER | UPSTREAM | SOW-007 | ACTIVE | Pipeline selector trace with ownership warning. |
| DEP-02-02-004 | ANCHOR | OTHER | UPSTREAM | OBJ-001 | ACTIVE | Objective trace; target type kept `UNKNOWN` because schema has no objective enum. |
| DEP-02-02-005 | EXECUTION | INTERFACE | UPSTREAM | DEL-02-01 | ACTIVE | Matrix routing interface. |
| DEP-02-02-006 | EXECUTION | INTERFACE | UPSTREAM | DEL-02-03 | ACTIVE | Scope scan / stale selection interface. |
| DEP-02-02-007 | EXECUTION | INTERFACE | UPSTREAM | DEL-07-04 | ACTIVE | Status summary interface. |
| DEP-02-02-008 | EXECUTION | INTERFACE | UPSTREAM | DEL-07-05 | ACTIVE | Dependency summary interface. |
| DEP-02-02-009 | EXECUTION | CONSTRAINT | UPSTREAM | DEL-08-03 | ACTIVE | Dispatch semantics ownership constraint. |

## Run History

| Timestamp | Mode | Strictness | Decomposition Status | Active Rows | Warnings |
|---|---|---|---|---:|---|
| 2026-05-20T19:24:27-0600 | UPDATE | CONSERVATIVE | found | 9 | PRD_HASH_MISMATCH; SOW_007_OWNER_OVERLAP |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 9 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| TBD | 9 |

Closure note: dependency rows are evidence-backed but not satisfaction-closed. All `RequiredMaturity` values are `SEMANTIC_READY`; `ProposedMaturity` remains `TBD`.
