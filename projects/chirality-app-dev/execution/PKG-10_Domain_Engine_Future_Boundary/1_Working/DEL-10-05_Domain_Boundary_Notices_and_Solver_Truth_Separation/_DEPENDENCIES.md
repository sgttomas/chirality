# Dependencies: DEL-10-05 Domain Boundary Notices and Solver Truth Separation

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
- 2026-05-20 TASK + dependency-extract ran in `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Runtime override `SCOPE=DEL-10-05`; `RUN_ROOT=/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution`.
- Decomposition authority used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; anchor validation was available.
- Source document defaults: `SOURCE_DOCS=AUTO`, `DOC_ROLE_MAP=DEFAULT`, `ANCHOR_DOC=Datasheet.md`, `EXECUTION_DOC_ORDER=Procedure.md, Guidance.md, Specification.md, Datasheet.md`.
- Human ruling applied: semantic lensing and P3 enrichment are skipped; existing `_SEMANTIC.md` output is invalid evidence and was not read or consumed.
- Future-boundary ruling applied: PKG-10 remains gated; no domain-engine activation or implementation dependency edges were inferred.
- Conservative extraction emitted only explicit anchors and explicit upstream information-flow prerequisites. No inferred cross-deliverable execution edges were emitted.
- `[WARNING] SOURCE_HASH_MISMATCH`: `_REFERENCES.md` records `REF-006` / `docs/PRD.md` as `HASH_MISMATCH`; retained as an active prerequisite because `Procedure.md` says to treat the mismatch as a warning only for this run.
- 2026-07-10 D-APP-53 reconciliation (plan DRQ-10; authority `execution/_Coordination/_DECISIONS/D-APP-53_RULING_2026-07-10.md`, Option A): all 10 rows re-verified live and moved `TBD -> SATISFIED` (`LastSeen=2026-07-10`; `ProposedMaturity` left `TBD` matching `RequiredMaturity` per plan §3.4). Anchors PKG-10/SOW-071/OBJ-009/OBJ-010 live in the decomposition; REF-001..REF-004 doc prerequisites `MATCH`; DECOMP v3.2 present. Dated correction: the `SOURCE_HASH_MISMATCH` warning above is resolved — `_REFERENCES.md` line 12 now records REF-006 `docs/PRD.md` Status MATCH (SHA `ac35fba4...`). See `Evidence_D53A_Dependency_Reconciliation_2026-07-10.md`. No lifecycle transition; `_STATUS.md` stays CHECKING (F-APP-4).

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1

| Metric | Count |
|---|---:|
| Total rows | 10 |
| ACTIVE rows | 10 |
| RETIRED rows | 0 |
| ANCHOR rows | 4 |
| EXECUTION rows | 6 |

| DependencyID | Class | Type | Direction | Target | Status |
|---|---|---|---|---|---|
| DEP-10-05-001 | ANCHOR | OTHER | UPSTREAM | PKG-10 Domain Engine Future Boundary | ACTIVE |
| DEP-10-05-002 | ANCHOR | OTHER | UPSTREAM | SOW-071 Domain professional boundary | ACTIVE |
| DEP-10-05-003 | ANCHOR | OTHER | UPSTREAM | OBJ-009 Governance identity objective | ACTIVE |
| DEP-10-05-004 | ANCHOR | OTHER | UPSTREAM | OBJ-010 Future domain-engine compatibility objective | ACTIVE |
| DEP-10-05-005 | EXECUTION | PREREQUISITE | UPSTREAM | REF-001 `docs/DIRECTIVE.md` | ACTIVE |
| DEP-10-05-006 | EXECUTION | PREREQUISITE | UPSTREAM | REF-002 `docs/CONTRACT.md` | ACTIVE |
| DEP-10-05-007 | EXECUTION | PREREQUISITE | UPSTREAM | REF-003 `docs/SPEC.md` | ACTIVE |
| DEP-10-05-008 | EXECUTION | PREREQUISITE | UPSTREAM | REF-004 `docs/TYPES.md` | ACTIVE |
| DEP-10-05-009 | EXECUTION | PREREQUISITE | UPSTREAM | REF-006 `docs/PRD.md` | ACTIVE |
| DEP-10-05-010 | EXECUTION | PREREQUISITE | UPSTREAM | DECOMP-v3.2 decomposition authority | ACTIVE |

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE counts |
|---|---|---|---|---|---|
| 2026-05-20T21:07:19-0600 | UPDATE | CONSERVATIVE | `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` available | `SOURCE_HASH_MISMATCH` for REF-006; `_SEMANTIC.md` ignored by ruling; PKG-10 future-boundary/gated | ANCHOR 4; EXECUTION 6; TOTAL 10 |
| 2026-07-10 | RECONCILIATION (D-APP-53) | n/a | available; anchors re-verified | 10 rows SATISFIED; REF-006 HASH_MISMATCH resolved (now MATCH); linter PASS 0/0 | ANCHOR 4; EXECUTION 6; TOTAL 10 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 10 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 10 |

(Synced to CSV state 2026-07-10, D-APP-53 reconciliation; previously TBD 10.)

Closure state: dependency register created and schema-valid; satisfaction lifecycle remains `TBD` pending downstream FULL_GRAPH/cycle checks and any human closure decisions.

Closure state update (2026-07-10, D-APP-53 reconciliation): all 10 rows SATISFIED on live evidence; the project-level FULL_GRAPH snapshot over the reconciled registers is queued as plan DRQ-11 and is tracked at project level, not by a row in this register.
