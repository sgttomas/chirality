# Dependencies: DEL-06-06 Hook Lifecycle and Compaction Mirror

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. DEP-06-06-001, DEP-06-06-002, DEP-06-06-003, DEP-06-06-004, DEP-06-06-005, DEP-06-06-006, DEP-06-06-008

## Declared Downstream

Current extracted downstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. DEP-06-06-007

## Current ADQ-11 Reconciliation Note

ADQ-11/D-APP-43 updates the active structured register. `DEP-06-06-008` is now
`SATISFIED` because `_REFERENCES.md` records REF-006 `docs/PRD.md` as `MATCH` under
the D-APP-38 authority corpus v2. Historical 2026-05-20 run warnings remain extraction
history and no longer describe the active source-state posture. External lifecycle and
handover rows remain pending unless separately closed by their owning deliverables.

## Prior Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.

## Extracted Dependency Register

Descriptive mirror of current `Dependencies.csv`; no formal field is changed.

| DependencyID | Class | Direction | Type | Target | Status | Satisfaction |
|---|---|---|---|---|---|---|
| DEP-06-06-001 | ANCHOR | OTHER | UPSTREAM | PKG-06 | ACTIVE | NOT_APPLICABLE |
| DEP-06-06-002 | ANCHOR | OTHER | UPSTREAM | SOW-057 | ACTIVE | NOT_APPLICABLE |
| DEP-06-06-003 | ANCHOR | OTHER | UPSTREAM | SOW-061 | ACTIVE | NOT_APPLICABLE |
| DEP-06-06-004 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-05-02 | ACTIVE | PENDING |
| DEP-06-06-005 | EXECUTION | INTERFACE | UPSTREAM | DEL-06-04 | ACTIVE | PENDING |
| DEP-06-06-006 | EXECUTION | INTERFACE | UPSTREAM | DEL-03-04 | ACTIVE | PENDING |
| DEP-06-06-007 | EXECUTION | HANDOVER | DOWNSTREAM | DEL-09-02 | ACTIVE | PENDING |
| DEP-06-06-008 | EXECUTION | CONSTRAINT | UPSTREAM | REF-006 | ACTIVE | SATISFIED |

Counts: ACTIVE=8; satisfaction NOT_APPLICABLE=3, PENDING=4, SATISFIED=1.

## Run Notes

- MODE: UPDATE.
- STRICTNESS: CONSERVATIVE.
- CONSUMER_CONTEXT: NONE.
- SCOPE: DEL-06-06.
- RUN_ROOT: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution`.
- DECOMPOSITION_PATH: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Source documents read for dependency extraction: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Existing `_SEMANTIC.md` was not read or consumed per human ruling; semantic lensing and P3 enrichment were skipped.
- `Dependencies.csv` was missing at run start and was created with v3.1 schema columns.
- Anchor document selection: `Datasheet.md` plus `_CONTEXT.md` traceability fields; decomposition used to validate PKG-06, DEL-06-06, SOW-057, and SOW-061.
- Execution document order: `Specification.md`, `Guidance.md`, `Procedure.md`.
- Parent anchor check: PASS; one ACTIVE `IMPLEMENTS_NODE` anchor is present.
- [HISTORICAL WARNING] SOURCE_HASH_MISMATCH_REF-006: the 2026-05-20 extraction saw REF-006 as `HASH_MISMATCH`; ADQ-11 records the current REF-006 state as `MATCH` under D-APP-38 corpus v2, and `DEP-06-06-008` is now `SATISFIED`.
- Exact implementation module paths, test fixture paths, payload fields, event writer API path, and parent/child event relation remain `TBD`.

## Run History

| Timestamp | Mode | Strictness | Decomposition status | Warnings | ACTIVE ANCHOR | ACTIVE EXECUTION |
|---|---|---|---|---|---:|---:|
| 2026-05-20T19:47:33-0600 | UPDATE | CONSERVATIVE | Provided and used: `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Historical SOURCE_HASH_MISMATCH_REF-006, later reconciled by D-APP-38 corpus v2 | 3 | 5 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 8 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| NOT_APPLICABLE | 3 |
| PENDING | 4 |
| SATISFIED | 1 |

## Current descriptive index — 2026-09-22

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

Current consumer/verification locus: Runtime `packages/daemon/src/codex-supervisor.ts`, `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; `tests/codex-supervisor.test.ts`; App `scripts/validate-harness-section9.mjs` as a coverage mapping hook, not proof of live reach. The current topology is application-owned Runtime; older daemon/SDK file names and retired kit-file citations in dated Run Notes are historical source references, not fresh implementation prerequisites. A proposed change to a formal row, satisfaction or accepted dependency basis must be applied by its owner; this index does not enact it.

## Current evidence-locator refresh — 2026-09-22

2 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

1 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

1 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=8; RETIRED=0; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_SOURCE_04_06_APPROVED.csv`; current rows: ACTIVE=8, RETIRED=0. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.
