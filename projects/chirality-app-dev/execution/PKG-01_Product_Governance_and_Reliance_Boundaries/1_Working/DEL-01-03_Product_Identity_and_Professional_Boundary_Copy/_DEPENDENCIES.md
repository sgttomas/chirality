# Dependencies: DEL-01-03 Product Identity and Professional Boundary Copy

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

See `Dependencies.csv` for the derivative dependency-extract register. No dependency row is satisfied
by this documentation reconciliation.

## Declared Downstream

No downstream deliverable edge is accepted in the derivative register.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 TASK + dependency-extract ran in `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Runtime override `SCOPE=DEL-01-03`; `RUN_ROOT=/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution`.
- Decomposition authority used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; anchor validation was available.
- Source document defaults: `SOURCE_DOCS=AUTO`, `DOC_ROLE_MAP=DEFAULT`, `ANCHOR_DOC=Datasheet.md`, `EXECUTION_DOC_ORDER=Procedure.md, Guidance.md, Specification.md, Datasheet.md`.
- Human ruling applied: semantic lensing and P3 enrichment are skipped; existing `_SEMANTIC.md` output is invalid evidence and was not read or consumed.
- Conservative extraction emitted only explicit anchors and explicit upstream information-flow prerequisites. No inferred cross-deliverable execution edges were emitted.
- `[RECONCILED] REF-006`: D-APP-38 corpus `v1` reconciled `docs/PRD.md`; `_REFERENCES.md` now reports `MATCH`. Row `DEP-01-03-011` remains an active prerequisite until dependency/evidence disposition, but it is no longer blocked by a PRD hash mismatch.
- 2026-07-10 (D-APP-53 reconciliation): all 12 open rows re-verified against the live tree and moved `TBD -> SATISFIED` under `PLAN_2026-07-10_pre_issuance_dependency_reconciliation.md` (DRQ-02). Anchor targets (PKG-01, SOW-071, SOW-074, OBJ-009, OBJ-010) confirmed in decomposition v3.2 with DEL-01-03 still listed; REF-001..REF-006 MATCH re-verified by live SHA-256 recompute; decomposition prerequisite present. Responsible-party/owner-authority TBD fields remain out of this queue's scope per the plan §3.5. See `Evidence_D53A_Dependency_Reconciliation_2026-07-10.md`. Derivative evidence only; no lifecycle transition and no issuance.

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1

| Metric | Count |
|---|---:|
| Total rows | 12 |
| ACTIVE rows | 12 |
| RETIRED rows | 0 |
| ANCHOR rows | 5 |
| EXECUTION rows | 7 |

| DependencyID | Class | Type | Direction | Target | Status |
|---|---|---|---|---|---|
| DEP-01-03-001 | ANCHOR | OTHER | UPSTREAM | PKG-01 Product Governance and Reliance Boundaries | ACTIVE |
| DEP-01-03-002 | ANCHOR | OTHER | UPSTREAM | SOW-071 Domain professional boundary | ACTIVE |
| DEP-01-03-003 | ANCHOR | OTHER | UPSTREAM | SOW-074 Human authority/professional boundaries | ACTIVE |
| DEP-01-03-004 | ANCHOR | OTHER | UPSTREAM | OBJ-009 Governance identity objective | ACTIVE |
| DEP-01-03-005 | ANCHOR | OTHER | UPSTREAM | OBJ-010 Future domain-engine compatibility objective | ACTIVE |
| DEP-01-03-006 | EXECUTION | PREREQUISITE | UPSTREAM | REF-001 `docs/DIRECTIVE.md` | ACTIVE |
| DEP-01-03-007 | EXECUTION | PREREQUISITE | UPSTREAM | REF-002 `docs/CONTRACT.md` | ACTIVE |
| DEP-01-03-008 | EXECUTION | PREREQUISITE | UPSTREAM | REF-003 `docs/SPEC.md` | ACTIVE |
| DEP-01-03-009 | EXECUTION | PREREQUISITE | UPSTREAM | REF-004 `docs/TYPES.md` | ACTIVE |
| DEP-01-03-010 | EXECUTION | PREREQUISITE | UPSTREAM | REF-005 `docs/PLAN.md` | ACTIVE |
| DEP-01-03-011 | EXECUTION | PREREQUISITE | UPSTREAM | REF-006 `docs/PRD.md` | ACTIVE |
| DEP-01-03-012 | EXECUTION | PREREQUISITE | UPSTREAM | DECOMP-v3.2 decomposition authority | ACTIVE |

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE counts |
|---|---|---|---|---|---|
| 2026-05-20T19:24:25-0600 | UPDATE | CONSERVATIVE | `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` available | `SOURCE_HASH_MISMATCH` for REF-006 at extraction time; later reconciled by D-APP-38 corpus `v1`; `_SEMANTIC.md` ignored by ruling | ANCHOR 5; EXECUTION 7; TOTAL 12 |
| 2026-07-10 (D-APP-53 reconciliation) | RECONCILE | CONSERVATIVE | `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` re-verified | none; `validate_dependencies.py` PASS (12 rows, 0 errors, 0 warnings) | ANCHOR 5; EXECUTION 7; TOTAL 12 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 12 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 12 |

Closure state: dependency register schema-valid and all 12 rows `SATISFIED` under the D-APP-53 reconciliation (2026-07-10). `ProposedMaturity` mirrors each row's `RequiredMaturity` (`TBD` at extraction) per the plan's maturity rule. This is derivative dependency evidence, not lifecycle closure; issuance-gate sign-off fields remain owner-gated.

## Current Source Migration Annotation

2026-07-19 — D-GOV-16/D-APP-68: the four-document source names above describe
the 2026-05-20 extraction and remain historical. Current live evidence pointers
are maintained in `Dependencies.csv` against consolidated `ScopeOfWork.md` CLM
anchors. This migration changed no dependency identity, status, satisfaction,
or lifecycle meaning.
