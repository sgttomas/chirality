# Dependencies: DEL-06-01 ChiralityPermissionOverlay and Mode Mapping

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. DEP-06-01-001, DEP-06-01-002, DEP-06-01-003, DEP-06-01-004, DEP-06-01-005, DEP-06-01-006, DEP-06-01-007, DEP-06-01-008, DEP-06-01-009, DEP-06-01-010, DEP-06-01-011, DEP-06-01-012, DEP-06-01-013, DEP-06-01-014

## Declared Downstream

Current extracted downstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. Consult the structured register; no new edge is inferred.

## Current ADQ-11 Reconciliation Note

ADQ-11/D-APP-43 updates the active structured register. `DEP-06-01-010` is now
`SATISFIED` because `_REFERENCES.md` records REF-006 `docs/PRD.md` as `MATCH` under
the D-APP-38 authority corpus v2. Historical 2026-05-20 run warnings remain extraction
history and no longer describe the active source-state posture.

## Extracted Dependency Register

Descriptive mirror of current `Dependencies.csv`; no formal field is changed.

| DependencyID | Class | Direction | Type | Target | Status | Satisfaction |
|---|---|---|---|---|---|---|
| DEP-06-01-001 | ANCHOR | OTHER | UPSTREAM | PKG-06 | ACTIVE | SATISFIED |
| DEP-06-01-002 | ANCHOR | OTHER | UPSTREAM | SOW-054 | ACTIVE | SATISFIED |
| DEP-06-01-003 | ANCHOR | OTHER | UPSTREAM | SOW-055 | ACTIVE | SATISFIED |
| DEP-06-01-004 | ANCHOR | OTHER | UPSTREAM | SOW-056 | ACTIVE | SATISFIED |
| DEP-06-01-005 | ANCHOR | OTHER | UPSTREAM | SOW-058 | ACTIVE | SATISFIED |
| DEP-06-01-006 | EXECUTION | PREREQUISITE | UPSTREAM | REF-004 | ACTIVE | PENDING |
| DEP-06-01-007 | EXECUTION | PREREQUISITE | UPSTREAM | REF-002 | ACTIVE | PENDING |
| DEP-06-01-008 | EXECUTION | PREREQUISITE | UPSTREAM | REF-003 | ACTIVE | PENDING |
| DEP-06-01-009 | EXECUTION | PREREQUISITE | UPSTREAM | REF-005 | ACTIVE | PENDING |
| DEP-06-01-010 | EXECUTION | CONSTRAINT | UPSTREAM | REF-006 | ACTIVE | SATISFIED |
| DEP-06-01-011 | EXECUTION | INTERFACE | UPSTREAM | DEL-06-04 | RETIRED | NOT_APPLICABLE |
| DEP-06-01-012 | EXECUTION | INTERFACE | UPSTREAM | DEL-06-02 | RETIRED | NOT_APPLICABLE |
| DEP-06-01-013 | EXECUTION | INTERFACE | UPSTREAM | DEL-06-03 | RETIRED | NOT_APPLICABLE |
| DEP-06-01-014 | EXECUTION | INTERFACE | UPSTREAM | TBD | ACTIVE | PENDING |

Counts: ACTIVE=11, RETIRED=3; satisfaction NOT_APPLICABLE=3, PENDING=5, SATISFIED=6.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 TASK dependency-extract run used RuntimeOverrides: `SCOPE=DEL-06-01`, `RUN_ROOT=/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution`, `DECOMPOSITION_PATH=/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority. `_SEMANTIC.md` was not read or consumed per human ruling.
- Anchor doc selection: `Datasheet.md` plus `_CONTEXT.md` and decomposition traceability fields.
- Execution doc order: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`.
- Decomposition validation status: available; parent anchor resolves to `PKG-06`; SOW trace anchors resolve to SOW-054, SOW-055, SOW-056, and SOW-058.
- Parent anchor check: PASS. One ACTIVE `IMPLEMENTS_NODE` anchor exists.
- [HISTORICAL WARNING] SOURCE_STATE: the 2026-05-20 extraction saw REF-006 as `HASH_MISMATCH`; ADQ-11 records the current REF-006 state as `MATCH` under D-APP-38 corpus v2, and `DEP-06-01-010` is now `SATISFIED`.
- [WARNING] TARGET_TBD: Event writer/session JSONL append API dependency is explicit in `Procedure.md` as an assumption, but exact target deliverable and call path remain `TBD`; row DEP-06-01-014 preserves `TargetType=UNKNOWN`.

## Run History

| Timestamp | Mode | Strictness | Decomposition path/status | ACTIVE counts | Warnings |
|---|---|---|---|---|---|
| 2026-05-20T19:41:28-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` / available | 14 total: 5 ANCHOR, 9 EXECUTION | Historical SOURCE_STATE REF-006 HASH_MISMATCH, later reconciled by D-APP-38 corpus v2; TARGET_TBD DEP-06-01-014 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 11 |
| RETIRED | 3 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 6 |
| PENDING | 5 |
| NOT_APPLICABLE | 3 |

## D-APP-56 R5 P45 current register summary (2026-07-12)

- **Source:** UPD-127
- **Current counts:** ACTIVE 11; RETIRED 3; NOT_APPLICABLE=3; PENDING=5; SATISFIED=6.
- **Correction:** DEP-06-01-014 now names the appendHarnessEvent call path; upstream deliverable identity remains unassigned.
- Earlier extraction and reconciliation history is preserved as dated evidence; this block is the current structured-register mirror.

## Current descriptive index — 2026-09-22

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

Current consumer/verification locus: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App `frontend/src/__tests__/components/live-session-requests.test.tsx`; legacy `frontend/src/lib/harness/permission-overlay.ts` and fixtures. The current topology is application-owned Runtime; older daemon/SDK file names and retired kit-file citations in dated Run Notes are historical source references, not fresh implementation prerequisites. A proposed change to a formal row, satisfaction or accepted dependency basis must be applied by its owner; this index does not enact it.

## Current evidence-locator refresh — 2026-09-22

5 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=11; RETIRED=3; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_SOURCE_04_06_APPROVED.csv`; current rows: ACTIVE=11, RETIRED=3. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_QUOTE_04_06_SUPPORTED_APPROVED.csv`; current rows: ACTIVE=11, RETIRED=3. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.
