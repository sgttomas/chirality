# Dependencies: DEL-05-04 Runtime Replay and Transcript View

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. DEP-05-04-001, DEP-05-04-002, DEP-05-04-003, DEP-05-04-004, DEP-05-04-005, DEP-05-04-006, DEP-05-04-007, DEP-05-04-008, DEP-05-04-009

## Declared Downstream

Current extracted downstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. Consult the structured register; no new edge is inferred.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- This run used only `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Human ruling applied: semantic lensing and P3 enrichment were skipped; `_SEMANTIC.md` was not read and is not evidence for this register.
- Chosen anchor document: `Datasheet.md` plus `_CONTEXT.md` identity/traceability fields.
- Chosen execution document order: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`.
- Decomposition validation: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` located and used for PKG, SOW, objective, and deliverable target labels.
- `[RETIRED] SOURCE_STATE_PRD_HASH_MISMATCH`: D-APP-38 authority corpus v2 and `_REFERENCES.md` now report `docs/PRD.md` REF-006 as `MATCH`.
- `[SATISFIED] ASSUMPTION_EDGE`: DEP-05-04-006 remains targeted at DEL-05-02, now with ADQ-09 evidence for replay-facing schema/writer behavior.
- `[SATISFIED] UNRESOLVED_TARGET`: DEP-05-04-008 keeps `TargetType=UNKNOWN` because it names the redaction helper/policy rather than a deliverable, but ADQ-09 added read-time replay redaction evidence.
- Parent anchor check: PASS, exactly one ACTIVE `IMPLEMENTS_NODE` anchor.

## Extracted Dependency Register

Descriptive mirror of current `Dependencies.csv`; no formal field is changed.

| DependencyID | Class | Direction | Type | Target | Status | Satisfaction |
|---|---|---|---|---|---|---|
| DEP-05-04-001 | ANCHOR | OTHER | UPSTREAM | PKG-05 | ACTIVE | SATISFIED |
| DEP-05-04-002 | ANCHOR | OTHER | UPSTREAM | SOW-042 | ACTIVE | SATISFIED |
| DEP-05-04-003 | ANCHOR | OTHER | UPSTREAM | SOW-046 | ACTIVE | SATISFIED |
| DEP-05-04-004 | ANCHOR | OTHER | UPSTREAM | OBJ-003 | ACTIVE | SATISFIED |
| DEP-05-04-005 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-05-01 | ACTIVE | PENDING |
| DEP-05-04-006 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-05-02 | ACTIVE | SATISFIED |
| DEP-05-04-007 | EXECUTION | INTERFACE | UPSTREAM | DEL-04-01 | ACTIVE | SATISFIED |
| DEP-05-04-008 | EXECUTION | CONSTRAINT | UPSTREAM | Redaction helper or policy | ACTIVE | PENDING |
| DEP-05-04-009 | EXECUTION | INTERFACE | UPSTREAM | DEL-05-05 | ACTIVE | SATISFIED |

Counts: ACTIVE=9; satisfaction SATISFIED=9.

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE Rows |
|---|---|---|---|---|---:|
| 2026-05-20T19:41:21-06:00 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | SOURCE_STATE_PRD_HASH_MISMATCH; ASSUMPTION_EDGE; UNRESOLVED_TARGET | 9 |
| 2026-06-21T03:46:09-06:00 | EVIDENCE_UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | D-APP-38 corpus v2 MATCH; ADQ-09 transcript/replay evidence applied | 9 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 9 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 9 |

## Current descriptive index — 2026-09-22

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

Current consumer/verification locus: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App `frontend/src/components/woven-dialogue/selected-session-replay-lens.tsx`, right-panel Session view and selected-session/shell tests. The current topology is application-owned Runtime; older daemon/SDK file names and retired kit-file citations in dated Run Notes are historical source references, not fresh implementation prerequisites. A proposed change to a formal row, satisfaction or accepted dependency basis must be applied by its owner; this index does not enact it.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=9; RETIRED=0; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

## Current evidence-locator refresh — 2026-09-22

3 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_QUOTE_04_06_SUPPORTED_APPROVED.csv`; current rows: ACTIVE=9, RETIRED=0. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_SEMANTIC_19_PREVIEW.csv`; current rows: ACTIVE=9, RETIRED=0. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.
