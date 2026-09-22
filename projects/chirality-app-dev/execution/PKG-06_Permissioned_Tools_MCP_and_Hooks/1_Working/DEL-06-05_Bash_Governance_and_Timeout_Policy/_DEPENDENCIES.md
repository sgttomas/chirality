# Dependencies: DEL-06-05 Bash Governance and Timeout Policy

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. DEP-06-05-001, DEP-06-05-002, DEP-06-05-003, DEP-06-05-004, DEP-06-05-005, DEP-06-05-006, DEP-06-05-007, DEP-06-05-008

## Declared Downstream

Current extracted downstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. Consult the structured register; no new edge is inferred.

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

Descriptive mirror of current `Dependencies.csv`; no formal field is changed.

| DependencyID | Class | Direction | Type | Target | Status | Satisfaction |
|---|---|---|---|---|---|---|
| DEP-06-05-001 | ANCHOR | OTHER | UPSTREAM | SOW-062 | ACTIVE | NOT_APPLICABLE |
| DEP-06-05-002 | EXECUTION | INTERFACE | UPSTREAM | DEL-06-01 | ACTIVE | TBD |
| DEP-06-05-003 | EXECUTION | CONSTRAINT | UPSTREAM | DEL-06-04 | ACTIVE | TBD |
| DEP-06-05-004 | EXECUTION | INTERFACE | UPSTREAM | DEL-06-06 | ACTIVE | TBD |
| DEP-06-05-005 | EXECUTION | PREREQUISITE | UPSTREAM | REF-002 | ACTIVE | TBD |
| DEP-06-05-006 | EXECUTION | PREREQUISITE | UPSTREAM | REF-004 | ACTIVE | TBD |
| DEP-06-05-007 | EXECUTION | PREREQUISITE | UPSTREAM | REF-003 | ACTIVE | TBD |
| DEP-06-05-008 | EXECUTION | PREREQUISITE | UPSTREAM | REF-005 | ACTIVE | TBD |

Counts: ACTIVE=8; satisfaction NOT_APPLICABLE=1, TBD=7.

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

## Current descriptive index — 2026-09-22

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

Current consumer/verification locus: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App retained `frontend/src/lib/harness/tool-shell-policy.ts`, `frontend/src/__tests__/lib/chirality-hooks.test.ts`; Runtime event/artifact owners. The current topology is application-owned Runtime; older daemon/SDK file names and retired kit-file citations in dated Run Notes are historical source references, not fresh implementation prerequisites. A proposed change to a formal row, satisfaction or accepted dependency basis must be applied by its owner; this index does not enact it.

## Current evidence-locator refresh — 2026-09-22

4 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=8; RETIRED=0; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.
