# Dependencies: DEL-05-05 ToolResultStore and Session Artifacts

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. DEP-05-05-001, DEP-05-05-002, DEP-05-05-003, DEP-05-05-004, DEP-05-05-005, DEP-05-05-006, DEP-05-05-007, DEP-05-05-008, DEP-05-05-009, DEP-05-05-010

## Declared Downstream

Current extracted downstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. Consult the structured register; no new edge is inferred.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 19:41 dependency-extract run used `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and decomposition authority `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Human ruling applied: semantic lensing and P3 enrichment were skipped; `_SEMANTIC.md` was not read or consumed as evidence.
- Anchor doc selection: `Datasheet.md` and `_CONTEXT.md` for deliverable identity/traceability, validated against the decomposition authority.
- Execution doc order: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`.
- [RETIRED] SOURCE_STATE_PRD_HASH_MISMATCH: D-APP-38 authority corpus v2 and `_REFERENCES.md` now report `docs/PRD.md` REF-006 as `MATCH`.
- [WARNING] UNKNOWN_TARGETS: Objective IDs are anchored with `TargetType=UNKNOWN` because the v3.1 schema has no `OBJECTIVE` target enum.
- [RETIRED] TBD_POLICY_INPUTS: ADQ-10 records the `ToolResultStore` artifact implementation path and D-APP-42 checksum/retention policy. Thresholds, preview length, and artifact naming remain the existing descriptor/artifact-writer policy and are unchanged by D-APP-42.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` anchor exists.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE `IMPLEMENTS_NODE` anchor exists.

## Extracted Dependency Register

Descriptive mirror of current `Dependencies.csv`; no formal field is changed.

| DependencyID | Class | Direction | Type | Target | Status | Satisfaction |
|---|---|---|---|---|---|---|
| DEP-05-05-001 | ANCHOR | OTHER | UPSTREAM | PKG-05 | ACTIVE | SATISFIED |
| DEP-05-05-002 | ANCHOR | OTHER | UPSTREAM | SOW-053 | ACTIVE | SATISFIED |
| DEP-05-05-003 | ANCHOR | OTHER | UPSTREAM | SOW-059 | ACTIVE | SATISFIED |
| DEP-05-05-004 | ANCHOR | OTHER | UPSTREAM | OBJ-003 | ACTIVE | SATISFIED |
| DEP-05-05-005 | ANCHOR | OTHER | UPSTREAM | OBJ-005 | ACTIVE | SATISFIED |
| DEP-05-05-006 | EXECUTION | PREREQUISITE | UPSTREAM | REF-003 | ACTIVE | SATISFIED |
| DEP-05-05-007 | EXECUTION | PREREQUISITE | UPSTREAM | REF-002 | ACTIVE | SATISFIED |
| DEP-05-05-008 | EXECUTION | PREREQUISITE | UPSTREAM | REF-006 | ACTIVE | SATISFIED |
| DEP-05-05-009 | EXECUTION | PREREQUISITE | UPSTREAM | projects/chirality-runtime/packages/core/src/session-store.ts; projects/chirality-runtime/packages/contracts/src/harness/tool-descriptor.ts | ACTIVE | SATISFIED |
| DEP-05-05-010 | EXECUTION | CONSTRAINT | UPSTREAM | D-APP-42 | ACTIVE | SATISFIED |

Counts: ACTIVE=10; satisfaction SATISFIED=10.

## Lifecycle Summary

| Class | Type | Status | Count |
|---|---|---|---:|
| ANCHOR | OTHER | ACTIVE | 5 |
| EXECUTION | PREREQUISITE | ACTIVE | 4 |
| EXECUTION | CONSTRAINT | ACTIVE | 1 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 10 |

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE rows |
|---|---|---|---|---|---:|
| 2026-05-20 19:41 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` validated | SOURCE_STATE, UNKNOWN_TARGETS, TBD_POLICY_INPUTS | 10 |
| 2026-06-21 ADQ-10 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` unchanged | SOURCE_STATE retired; TBD_POLICY_INPUTS retired for ADQ-10; UNKNOWN_TARGETS retained by schema | 10 |

## Current descriptive index — 2026-09-22

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

Current consumer/verification locus: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App preview consumers; legacy `frontend/src/lib/harness/tool-result-artifacts.ts` and fixtures. The current topology is application-owned Runtime; older daemon/SDK file names and retired kit-file citations in dated Run Notes are historical source references, not fresh implementation prerequisites. A proposed change to a formal row, satisfaction or accepted dependency basis must be applied by its owner; this index does not enact it.

## Current evidence-locator refresh — 2026-09-22

3 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

1 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=10; RETIRED=0; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_QUOTE_04_06_SUPPORTED_APPROVED.csv`; current rows: ACTIVE=10, RETIRED=0. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.
