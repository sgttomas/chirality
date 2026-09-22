# Dependencies: DEL-01-04 Scope Boundary and Retired Scope Register

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

See `Dependencies.csv` for downstream `CONSTRAINT` rows. They remain derivative dependency evidence,
not closure approval.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 dependency-extract run:
  - Runtime overrides: `SCOPE=DEL-01-04`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
  - Decomposition authority: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` located and used.
  - Source docs used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and decomposition authority.
  - `ANCHOR_DOC=AUTO` resolved to `Datasheet.md`; execution docs were read as `Procedure.md`, `Specification.md`, `Guidance.md`, `_CONTEXT.md`, `_REFERENCES.md`.
  - Human ruling applied: semantic lensing and P3 enrichment skipped; `_SEMANTIC.md` was not read or consumed as evidence.
  - Existing declared dependency lists remain `TBD`; no declared edges were promoted without evidence.
  - `[RECONCILED] REF-006`: D-APP-38 corpus `v1` reconciled `docs/PRD.md`; `_REFERENCES.md` now reports `MATCH`. This does not satisfy dependency rows.
  - `[WARNING] HUMAN_RULING_TBD`: `Guidance.md` contains conflict-table rulings with `Human ruling (TBD)`; no dependency edge depends on those unresolved rulings.
- 2026-07-10 (D-APP-53 reconciliation): all 13 open rows re-verified against the live tree and moved `PENDING -> SATISFIED` under `PLAN_2026-07-10_pre_issuance_dependency_reconciliation.md` (DRQ-03). Anchor targets (PKG-01, SOW-065, SOW-076, SOW-077, SOW-078, OBJ-009) confirmed in decomposition v3.2 with DEL-01-04 still listed; local prerequisites and decomposition present; downstream `CONSTRAINT` content verified live (settings isolation and gated bypass in `frontend/src/lib/harness/sdk-options-builder.ts` with tests; DEL-07-06 and DEL-09-04 Specifications preserve the retired/packaging boundaries; PKG-10 remains future-amendment scope). See `Evidence_D53A_Dependency_Reconciliation_2026-07-10.md`. Derivative evidence only; no lifecycle transition and no issuance.

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1.

| DependencyID | Class | Type | Direction | Target | Status |
|---|---|---|---|---|---|
| DEP-01-04-001 | ANCHOR | OTHER | UPSTREAM | PKG-01 | ACTIVE | SATISFIED |
| DEP-01-04-002 | ANCHOR | OTHER | UPSTREAM | SOW-065 | ACTIVE | SATISFIED |
| DEP-01-04-003 | ANCHOR | OTHER | UPSTREAM | SOW-076 | ACTIVE | SATISFIED |
| DEP-01-04-004 | ANCHOR | OTHER | UPSTREAM | SOW-077 | ACTIVE | SATISFIED |
| DEP-01-04-005 | ANCHOR | OTHER | UPSTREAM | SOW-078 | ACTIVE | SATISFIED |
| DEP-01-04-006 | ANCHOR | OTHER | UPSTREAM | OBJ-009 | ACTIVE | SATISFIED |
| DEP-01-04-007 | EXECUTION | PREREQUISITE | UPSTREAM | _CONTEXT.md | ACTIVE | SATISFIED |
| DEP-01-04-008 | EXECUTION | PREREQUISITE | UPSTREAM | _REFERENCES.md | ACTIVE | SATISFIED |
| DEP-01-04-009 | EXECUTION | PREREQUISITE | UPSTREAM | DECOMP-v3.2 | ACTIVE | SATISFIED |
| DEP-01-04-010 | EXECUTION | CONSTRAINT | DOWNSTREAM | DEL-04-02 | ACTIVE | PENDING |
| DEP-01-04-011 | EXECUTION | CONSTRAINT | DOWNSTREAM | DEL-07-06 | ACTIVE | SATISFIED |
| DEP-01-04-012 | EXECUTION | CONSTRAINT | DOWNSTREAM | DEL-09-04 | ACTIVE | SATISFIED |
| DEP-01-04-013 | EXECUTION | CONSTRAINT | DOWNSTREAM | PKG-10 | ACTIVE | SATISFIED |

## Lifecycle Summary

| Metric | Count |
|---|---:|
| Total rows | 13 |
| ACTIVE rows | 13 |
| RETIRED rows | 0 |
| ANCHOR rows | 6 |
| EXECUTION rows | 7 |
| OTHER rows | 6 |
| PREREQUISITE rows | 3 |
| CONSTRAINT rows | 4 |
| `SatisfactionStatus=SATISFIED` | 13 |

Closure state: dependency register schema-valid and all 13 rows `SATISFIED` under the D-APP-53 reconciliation (2026-07-10). This is derivative dependency evidence, not closure approval; lifecycle state and issuance remain untouched.

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE Counts |
|---|---|---|---|---|---|
| 2026-05-20T19:24:28-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | SOURCE_HASH_MISMATCH at extraction time, later reconciled by D-APP-38 corpus `v1`; HUMAN_RULING_TBD | ANCHOR=6; EXECUTION=7; TOTAL=13 |
| 2026-07-10 (D-APP-53 reconciliation) | RECONCILE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` re-verified | none; `validate_dependencies.py` PASS (13 rows, 0 errors, 0 warnings) | ANCHOR=6; EXECUTION=7; TOTAL=13 |

---

**Addendum (2026-07-18 — D-APP-62 scoped interpretation):** Under the
D-APP-62 ruling (O-A, 2026-07-18), the assertion above that `_SEMANTIC.md`
is invalid evidence / was not read or consumed is scoped to
dependency-extraction evidence: it bars `_SEMANTIC.md` from serving as
evidence for dependency rows. Its recorded consumption as the primary input
to `_SEMANTIC_LENSING.md` is a different act, outside that scope and
consistent with it. See
`execution/_Coordination/_DECISIONS/D-APP-62_PACKET_SEMANTIC_ADMISSIBILITY_SCOPE_2026-07-18.md`.

## Current Source Migration Annotation

2026-07-19 — D-GOV-16/D-APP-68: the four-document source names above describe
the 2026-05-20 extraction and remain historical. Current live evidence pointers
are maintained in `Dependencies.csv` against consolidated `ScopeOfWork.md` CLM
anchors. This migration changed no dependency identity, status, satisfaction,
or lifecycle meaning.

## Current Reliance Annotation (2026-09-22)

D-APP-53 results and earlier MATCH notes above are dated evidence, not a fresh verification of changed source bytes. Formal row identity, status, satisfaction and accepted basis remain unchanged. Current source support is rechecked under D-APP-38; D-GOV-43/D-APP-127 governs current Codex/runtime/settings/policy applicability. REF-007 now names `workflows/software-decomp/WORKFLOW.md`; the descriptive locator now agrees with REF-007; formal edge identity, status and satisfaction remain unchanged.

## Current evidence-locator refresh — 2026-09-22

4 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=13; RETIRED=0; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.
