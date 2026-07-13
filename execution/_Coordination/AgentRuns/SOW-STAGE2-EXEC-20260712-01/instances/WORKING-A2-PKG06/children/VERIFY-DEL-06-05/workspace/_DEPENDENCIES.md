# Dependencies: DEL-06-05 Bash Governance and Timeout Policy

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

## Current ADQ-11 Reconciliation Note

ADQ-11/D-APP-43 does not add a PRD-only dependency target for this deliverable, but it retires the
active source-state warning for PKG-06 review: `_REFERENCES.md` records REF-006 `docs/PRD.md` as
`MATCH` under the D-APP-38 authority corpus v2. Historical 2026-05-20 run warnings remain extraction
history and no longer describe the active source-state posture.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 dependency-extract run used MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE.
- Source selection: `Datasheet.md` was used as the primary anchor document; execution evidence came from `Specification.md`, `Guidance.md`, and `Procedure.md`; `_CONTEXT.md`, `_REFERENCES.md`, and this file were read for identity, reference resolution, and existing dependency state.
- Decomposition authority: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` was available and used to validate `PKG-06`, `DEL-06-05`, `SOW-062`, and target deliverable labels.
- Human ruling applied: semantic lensing and P3 enrichment skipped; `_SEMANTIC.md` was not read or consumed as evidence.
- `[HISTORICAL WARNING] SOURCE_STATE_PRD_HASH_MISMATCH`: the 2026-05-20 extraction saw REF-006 as `HASH_MISMATCH`; ADQ-11 records the current REF-006 state as `MATCH` under D-APP-38 corpus v2. No dependency target was created solely from PRD evidence.
- Conservative extraction preserved unknown closure fields as `TBD`; no inferred downstream consumers were added.

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1

| DependencyID | Class | Type | Direction | Target | Status | Evidence |
|---|---|---|---|---|---|---|
| DEP-06-05-001 | ANCHOR | OTHER | UPSTREAM | SOW-062 Bash denied by default and governed when enabled | ACTIVE | `_CONTEXT.md#Traceability` |
| DEP-06-05-002 | EXECUTION | INTERFACE | UPSTREAM | DEL-06-01 ChiralityPermissionOverlay and Mode Mapping | ACTIVE | `Specification.md#Scope` |
| DEP-06-05-003 | EXECUTION | CONSTRAINT | UPSTREAM | DEL-06-04 Write/Edit Surface and Path Hooks | ACTIVE | `Specification.md#Scope` |
| DEP-06-05-004 | EXECUTION | INTERFACE | UPSTREAM | DEL-06-06 Hook Lifecycle and Compaction Mirror | ACTIVE | `Specification.md#Scope` |
| DEP-06-05-005 | EXECUTION | PREREQUISITE | UPSTREAM | `docs/CONTRACT.md` | ACTIVE | `Procedure.md#Prerequisites` |
| DEP-06-05-006 | EXECUTION | PREREQUISITE | UPSTREAM | `docs/TYPES.md` | ACTIVE | `Procedure.md#Prerequisites` |
| DEP-06-05-007 | EXECUTION | PREREQUISITE | UPSTREAM | `docs/SPEC.md` | ACTIVE | `Procedure.md#Prerequisites` |
| DEP-06-05-008 | EXECUTION | PREREQUISITE | UPSTREAM | `docs/PLAN.md` | ACTIVE | `Procedure.md#Prerequisites` |

Counts:

| Dimension | Count |
|---|---:|
| ACTIVE rows | 8 |
| RETIRED rows | 0 |
| ANCHOR rows | 1 |
| EXECUTION rows | 7 |
| UPSTREAM rows | 8 |
| DOWNSTREAM rows | 0 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 8 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| NOT_APPLICABLE | 1 |
| TBD | 7 |

Closure state: dependency register initialized, but dependency satisfaction remains open because extracted execution rows retain `TBD` maturity and satisfaction fields.

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE counts |
|---|---|---|---|---|---|
| 2026-05-20T19:47:22-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` available | Historical SOURCE_STATE_PRD_HASH_MISMATCH, later reconciled by D-APP-38 corpus v2 | ANCHOR=1; EXECUTION=7; TOTAL=8 |

## D-APP-56 R5 P45 current register summary (2026-07-12)

- **Source:** UPD-129
- **Current counts:** ACTIVE 8; RETIRED 0; NOT_APPLICABLE=1; TBD=7.
- **Correction:** DEP-06-05-008 now records REF-006 MATCH; dated corpus-vintage history remains.
- Earlier extraction and reconciliation history is preserved as dated evidence; this block is the current structured-register mirror.
