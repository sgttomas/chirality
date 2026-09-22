# Dependencies: DEL-07-02 Execution Root Scaffolding from Decomposition

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows: `DEP-07-02-001`, `DEP-07-02-002`, `DEP-07-02-003`, `DEP-07-02-004`, `DEP-07-02-005`, `DEP-07-02-006`, `DEP-07-02-007`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Declared Downstream

Current extracted downstream rows: NONE. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Extracted Dependency Register

Active extracted rows: 7.

| DependencyID | Class | Type | Direction | Target | Status |
|---|---|---|---|---|---|
| DEP-07-02-001 | ANCHOR | OTHER | UPSTREAM | PKG-07 | ACTIVE | TBD |
| DEP-07-02-002 | ANCHOR | OTHER | UPSTREAM | SOW-024 | ACTIVE | TBD |
| DEP-07-02-003 | ANCHOR | OTHER | UPSTREAM | SOW-025 | ACTIVE | TBD |
| DEP-07-02-004 | EXECUTION | PREREQUISITE | UPSTREAM | execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md | ACTIVE | TBD |
| DEP-07-02-005 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-07-01 | ACTIVE | TBD |
| DEP-07-02-006 | EXECUTION | CONSTRAINT | UPSTREAM | REF-002 | ACTIVE | TBD |
| DEP-07-02-007 | EXECUTION | PREREQUISITE | UPSTREAM | _REFERENCES.md | ACTIVE | TBD |

## Run Notes

- Runtime overrides: `SCOPE=DEL-07-02`, `RUN_ROOT=/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution`, `DECOMPOSITION_PATH=/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Human ruling applied: semantic lensing and P3 enrichment are skipped; `_SEMANTIC.md` was not read or consumed.
- Anchor doc selection: `Datasheet.md` with validation against the provided decomposition path.
- Execution doc order: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`.
- Decomposition status: found and used for DEL-07-02, SOW-024, SOW-025, and DEL-07-01 target resolution.
- No `[WARNING] FLOATING_NODE`: exactly one ACTIVE `IMPLEMENTS_NODE` anchor was extracted.
- No `[WARNING] AMBIGUOUS_ANCHOR`: only one ACTIVE `IMPLEMENTS_NODE` anchor was extracted.
- [RESOLVED 2026-07-12] REF-006 docs/PRD.md is MATCH under D-APP-38; the mismatch warning remains only in dated 2026-05-20 run history.
- Conservative extraction retained unresolved lifecycle values as `TBD` where source evidence does not prove satisfaction or proposed maturity.

## Run History

- 2026-05-20 19:54 MDT - `TASK + dependency-extract`, mode `UPDATE`, strictness `CONSERVATIVE`, decomposition path found, semantic lensing skipped by human ruling, ACTIVE counts: ANCHOR 3, EXECUTION 4, warnings: REF-006 hash mismatch; no floating/ambiguous anchor.

## Lifecycle Summary

Current descriptive counts from unchanged `Dependencies.csv` (2026-09-22); this projection does not change satisfaction or maturity.

| Field | Count |
|---|---:|
| ACTIVE | 7 |
| RequiredMaturity=SEMANTIC_READY | 4 |
| RequiredMaturity=TBD | 3 |
| ProposedMaturity=TBD | 7 |
| SatisfactionStatus=TBD | 7 |

## D-APP-56 R5 P40 register annotation (2026-07-12)

REF-006 is MATCH under D-APP-38. Any HASH_MISMATCH token retained in the dated Run History is extraction provenance, not current dependency state. Structured-row status and summary counts above reflect Dependencies.csv after UPD-077..079.

## Current record interpretation — 2026-09-22

Earlier extraction notes, counts, source states and file citations retain their dated basis. Current production claims live in `ScopeOfWork.md`; removed four-document files are historical evidence. D-GOV-43/D-APP-127 make the App-owned Runtime/Codex path current; SDK MCP/hooks and daemon proofs are compatibility history. Formal row mutations require the owning dependency pass; this descriptive update grants none.

## Current evidence-locator refresh — 2026-09-22

6 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=7; RETIRED=0; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

## Current evidence-locator refresh — 2026-09-22

1 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_EXTRA_3_PREVIEW.csv`; current rows: ACTIVE=7, RETIRED=0. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.
