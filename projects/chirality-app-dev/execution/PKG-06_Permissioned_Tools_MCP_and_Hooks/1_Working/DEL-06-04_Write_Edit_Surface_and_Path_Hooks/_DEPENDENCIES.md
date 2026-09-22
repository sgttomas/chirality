# Dependencies: DEL-06-04 Write/Edit Surface and Path Hooks

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. DEP-06-04-001, DEP-06-04-002, DEP-06-04-003, DEP-06-04-004, DEP-06-04-005, DEP-06-04-006, DEP-06-04-007, DEP-06-04-008, DEP-06-04-009, DEP-06-04-010

## Declared Downstream

Current extracted downstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. Consult the structured register; no new edge is inferred.

## Current ADQ-11 Reconciliation Note

ADQ-11/D-APP-43 updates the active structured register. `DEP-06-04-010` is now
`SATISFIED` because `_REFERENCES.md` records REF-006 `docs/PRD.md` as `MATCH` under
the D-APP-38 authority corpus v2. Historical 2026-05-20 run warnings remain extraction
history and no longer describe the active source-state posture. External upstream edges
remain pending unless separately closed by their owning deliverables.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 dependency-extract run used `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, and `CONSUMER_CONTEXT=NONE`.
- Source documents scanned: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and decomposition authority `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Human ruling applied: semantic lensing and P3 enrichment were skipped; `_SEMANTIC.md` was not read and is not evidence for this register.
- Anchor document selection: `Datasheet.md` and `Specification.md` traceability sections.
- Execution document order: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`.
- Decomposition validation: available and used for package, deliverable, SOW, and objective target resolution.
- `[HISTORICAL WARNING] PRD_HASH_MISMATCH`: the 2026-05-20 extraction saw REF-006 as `HASH_MISMATCH`; ADQ-11 records the current REF-006 state as `MATCH` under D-APP-38 corpus v2, and `DEP-06-04-010` is now `SATISFIED`.
- `[WARNING] HUMAN_RULING_SEMANTIC_SKIPPED`: inherited `SatisfactionThreshold=SEMANTIC_READY` is not used as evidence in this extraction because semantic lensing was explicitly skipped.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` parent anchor is present.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE `IMPLEMENTS_NODE` parent anchor is present.

## Extracted Dependency Register

Descriptive mirror of current `Dependencies.csv`; no formal field is changed.

| DependencyID | Class | Direction | Type | Target | Status | Satisfaction |
|---|---|---|---|---|---|---|
| DEP-06-04-001 | ANCHOR | OTHER | UPSTREAM | PKG-06 | ACTIVE | NOT_APPLICABLE |
| DEP-06-04-002 | ANCHOR | OTHER | UPSTREAM | SOW-027 | ACTIVE | NOT_APPLICABLE |
| DEP-06-04-003 | ANCHOR | OTHER | UPSTREAM | SOW-057 | ACTIVE | NOT_APPLICABLE |
| DEP-06-04-004 | ANCHOR | OTHER | UPSTREAM | SOW-060 | ACTIVE | NOT_APPLICABLE |
| DEP-06-04-005 | ANCHOR | OTHER | UPSTREAM | OBJ-005 | ACTIVE | NOT_APPLICABLE |
| DEP-06-04-006 | ANCHOR | OTHER | UPSTREAM | OBJ-006 | ACTIVE | NOT_APPLICABLE |
| DEP-06-04-007 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-06-01 | ACTIVE | PENDING |
| DEP-06-04-008 | EXECUTION | INTERFACE | UPSTREAM | DEL-07-01 | ACTIVE | PENDING |
| DEP-06-04-009 | EXECUTION | INTERFACE | UPSTREAM | DEL-06-06 | RETIRED | NOT_APPLICABLE |
| DEP-06-04-010 | EXECUTION | CONSTRAINT | UPSTREAM | REF-006 | ACTIVE | SATISFIED |

Counts: ACTIVE=9, RETIRED=1; satisfaction NOT_APPLICABLE=7, PENDING=2, SATISFIED=1.

## Run History

| Timestamp | Mode | Strictness | Decomposition path/status | Warnings | ACTIVE counts |
|---|---|---|---|---|---|
| 2026-05-20T19:47:30-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` / available | Historical PRD_HASH_MISMATCH, later reconciled by D-APP-38 corpus v2; HUMAN_RULING_SEMANTIC_SKIPPED | ANCHOR=6; EXECUTION=4; TOTAL=10 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 9 |
| RETIRED | 1 |

| SatisfactionStatus | Count |
|---|---:|
| NOT_APPLICABLE | 7 |
| PENDING | 2 |
| SATISFIED | 1 |

Closure state: dependency register initialized. ADQ-11 closes the REF-006 source-state row and records
exact-edit/atomic evidence, but external execution edges remain `PENDING` unless separately closed by
their owning deliverables.

## Current descriptive index — 2026-09-22

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

Current consumer/verification locus: Runtime `packages/daemon/src/codex-supervisor.ts`, `tests/codex-supervisor.test.ts`; App governed mutation routes and retained `frontend/src/lib/harness/tool-path-policy.ts`, write/edit hooks and tests. The current topology is application-owned Runtime; older daemon/SDK file names and retired kit-file citations in dated Run Notes are historical source references, not fresh implementation prerequisites. A proposed change to a formal row, satisfaction or accepted dependency basis must be applied by its owner; this index does not enact it.

## Current evidence-locator refresh — 2026-09-22

1 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

5 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

1 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=9; RETIRED=1; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_SOURCE_04_06_APPROVED.csv`; current rows: ACTIVE=9, RETIRED=1. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.
