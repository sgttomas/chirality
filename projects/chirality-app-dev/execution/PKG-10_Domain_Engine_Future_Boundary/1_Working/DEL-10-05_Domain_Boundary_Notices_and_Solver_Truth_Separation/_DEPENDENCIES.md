# Dependencies: DEL-10-05 Domain Boundary Notices and Solver Truth Separation

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Descriptive mirror of `Dependencies.csv` (2026-09-22; no formal edge or basis change):

- `DEP-10-05-001` — OTHER; Domain Engine Future Boundary; SATISFIED.
- `DEP-10-05-002` — OTHER; Domain professional boundary; SATISFIED.
- `DEP-10-05-003` — OTHER; Preserve professional boundary, product identity, and reliance-boundary ownership in docs, UI, runtime, and release behavior.; SATISFIED.
- `DEP-10-05-004` — OTHER; Preserve future domain-engine compatibility without turning domain solvers into Chirality core.; SATISFIED.
- `DEP-10-05-005` — PREREQUISITE; docs/DIRECTIVE.md; SATISFIED.
- `DEP-10-05-006` — PREREQUISITE; docs/CONTRACT.md; SATISFIED.
- `DEP-10-05-007` — PREREQUISITE; docs/SPEC.md; SATISFIED.
- `DEP-10-05-008` — PREREQUISITE; docs/TYPES.md; SATISFIED.
- `DEP-10-05-009` — PREREQUISITE; docs/PRD.md; SATISFIED.
- `DEP-10-05-010` — PREREQUISITE; Chirality App vNext SOFTWARE_DECOMP v3.2; SATISFIED.

## Declared Downstream

No downstream-directed row is recorded in this local structured register; this does not assert absence of consumers elsewhere.

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
| DEP-10-05-001 | ANCHOR | OTHER | UPSTREAM | PKG-10 | ACTIVE | SATISFIED |
| DEP-10-05-002 | ANCHOR | OTHER | UPSTREAM | SOW-071 | ACTIVE | SATISFIED |
| DEP-10-05-003 | ANCHOR | OTHER | UPSTREAM | OBJ-009 | ACTIVE | SATISFIED |
| DEP-10-05-004 | ANCHOR | OTHER | UPSTREAM | OBJ-010 | ACTIVE | SATISFIED |
| DEP-10-05-005 | EXECUTION | PREREQUISITE | UPSTREAM | REF-001 | ACTIVE | SATISFIED |
| DEP-10-05-006 | EXECUTION | PREREQUISITE | UPSTREAM | REF-002 | ACTIVE | SATISFIED |
| DEP-10-05-007 | EXECUTION | PREREQUISITE | UPSTREAM | REF-003 | ACTIVE | SATISFIED |
| DEP-10-05-008 | EXECUTION | PREREQUISITE | UPSTREAM | REF-004 | ACTIVE | SATISFIED |
| DEP-10-05-009 | EXECUTION | PREREQUISITE | UPSTREAM | REF-006 | ACTIVE | SATISFIED |
| DEP-10-05-010 | EXECUTION | PREREQUISITE | UPSTREAM | DECOMP-v3.2 | ACTIVE | SATISFIED |

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE counts |
|---|---|---|---|---|---|
| 2026-05-20T21:07:19-0600 | UPDATE | CONSERVATIVE | `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` available | `SOURCE_HASH_MISMATCH` for REF-006; `_SEMANTIC.md` ignored by ruling; PKG-10 future-boundary/gated | ANCHOR 4; EXECUTION 6; TOTAL 10 |
| 2026-07-10 | RECONCILIATION (D-APP-53) | n/a | available; anchors re-verified | 10 rows SATISFIED; REF-006 HASH_MISMATCH resolved (now MATCH); linter PASS 0/0 | ANCHOR 4; EXECUTION 6; TOTAL 10 |

## Lifecycle Summary

Current structured-register mirror: 10 SATISFIED. Lifecycle labels and SatisfactionStatus are distinct; the complete formal register remains unchanged. Earlier run summaries below describe their dated basis.

## Current evidence navigation — 2026-09-22

Current contract carrier: `ScopeOfWork.md`; former Datasheet/Specification/Procedure/Guidance labels and old line anchors in formal rows are retained historical evidence locators. Current generic type source is `projects/chirality-runtime/packages/contracts/src/harness/domain-profile.ts`, consumed as `@chirality/runtime-contracts`; D-APP-118 retires the App facade. Retained registry/proposal tests are not proof of live Codex exposure. Formal row evidence/pin/LastSeen changes require the owning dependency reconciliation and are outside this record repair.

## Current evidence-locator refresh — 2026-09-22

2 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

4 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=10; RETIRED=0; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.
