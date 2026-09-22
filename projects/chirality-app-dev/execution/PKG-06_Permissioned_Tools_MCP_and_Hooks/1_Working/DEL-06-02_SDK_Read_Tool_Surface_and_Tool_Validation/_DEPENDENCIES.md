# Dependencies: DEL-06-02 SDK Read Tool Surface and Tool Validation

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. DEP-06-02-001, DEP-06-02-002, DEP-06-02-003, DEP-06-02-004, DEP-06-02-005, DEP-06-02-006, DEP-06-02-007, DEP-06-02-008, DEP-06-02-009, DEP-06-02-010, DEP-06-02-011

## Declared Downstream

Current extracted downstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. Consult the structured register; no new edge is inferred.

## Current ADQ-11 Reconciliation Note

ADQ-11/D-APP-43 updates the active structured register. `DEP-06-02-011` is now
`SATISFIED` because `_REFERENCES.md` records REF-006 `docs/PRD.md` as `MATCH` under
the D-APP-38 authority corpus v2. Historical 2026-05-20 run warnings remain extraction
history and no longer describe the active source-state posture.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 TASK dependency-extract run used `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Semantic lensing and P3 enrichment were skipped by human ruling; `_SEMANTIC.md` was not read or consumed.
- Decomposition authority was available and used for anchor validation and canonical target labels.
- Anchor document selected by AUTO/default heuristic: `Datasheet.md` with confirmation from `_CONTEXT.md` and decomposition authority.
- Execution document order selected by AUTO/default heuristic: `Procedure.md`, `Guidance.md`, `Specification.md`, `Datasheet.md`.
- [HISTORICAL WARNING] PRD_HASH_MISMATCH: the 2026-05-20 extraction saw REF-006 as `HASH_MISMATCH`; ADQ-11 records the current REF-006 state as `MATCH` under D-APP-38 corpus v2, and `DEP-06-02-011` is now `SATISFIED`.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` parent anchor is present.
- No `[WARNING] AMBIGUOUS_ANCHOR`: only one ACTIVE `IMPLEMENTS_NODE` parent anchor is present.

## Extracted Dependency Register

Descriptive mirror of current `Dependencies.csv`; no formal field is changed.

| DependencyID | Class | Direction | Type | Target | Status | Satisfaction |
|---|---|---|---|---|---|---|
| DEP-06-02-001 | ANCHOR | OTHER | UPSTREAM | PKG-06 | ACTIVE | TBD |
| DEP-06-02-002 | ANCHOR | OTHER | UPSTREAM | SOW-047 | ACTIVE | TBD |
| DEP-06-02-003 | ANCHOR | OTHER | UPSTREAM | SOW-049 | ACTIVE | TBD |
| DEP-06-02-004 | ANCHOR | OTHER | UPSTREAM | SOW-050 | ACTIVE | TBD |
| DEP-06-02-005 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-06-01 | ACTIVE | TBD |
| DEP-06-02-006 | EXECUTION | INTERFACE | UPSTREAM | DEL-06-03 | ACTIVE | TBD |
| DEP-06-02-007 | EXECUTION | PREREQUISITE | UPSTREAM | REF-003 | ACTIVE | TBD |
| DEP-06-02-008 | EXECUTION | PREREQUISITE | UPSTREAM | REF-004 | ACTIVE | TBD |
| DEP-06-02-009 | EXECUTION | PREREQUISITE | UPSTREAM | REF-002 | ACTIVE | TBD |
| DEP-06-02-010 | EXECUTION | PREREQUISITE | UPSTREAM | REF-005 | ACTIVE | TBD |
| DEP-06-02-011 | EXECUTION | CONSTRAINT | UPSTREAM | REF-006 | ACTIVE | SATISFIED |

Counts: ACTIVE=11; satisfaction SATISFIED=1, TBD=10.

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE Rows |
|---|---|---|---|---|---:|
| 2026-05-20T19:47:21-06:00 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` available | Historical PRD_HASH_MISMATCH, later reconciled by D-APP-38 corpus v2 | 11 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 11 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 1 |
| TBD | 10 |

Closure state: dependency register populated but not closed at project FULL_GRAPH level until aggregation/cycle checks are run.

## Current descriptive index — 2026-09-22

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

Current consumer/verification locus: Runtime `packages/daemon/src/application-tools.ts`, `packages/contracts/src/harness/tool-catalog.ts`, `tests/application-tools.test.ts`, `tests/codex-application-tools.test.ts`; App `frontend/src/lib/harness/tool-pool.ts`; D-APP-132. The current topology is application-owned Runtime; older daemon/SDK file names and retired kit-file citations in dated Run Notes are historical source references, not fresh implementation prerequisites. A proposed change to a formal row, satisfaction or accepted dependency basis must be applied by its owner; this index does not enact it.

## Current evidence-locator refresh — 2026-09-22

2 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

5 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=11; RETIRED=0; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.
