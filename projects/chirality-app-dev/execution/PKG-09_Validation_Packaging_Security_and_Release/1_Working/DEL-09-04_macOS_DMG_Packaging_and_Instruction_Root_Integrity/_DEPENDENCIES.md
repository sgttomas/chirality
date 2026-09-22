# Dependencies: DEL-09-04 macOS DMG Packaging and Instruction Root Integrity

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows: `DEP-09-04-001`, `DEP-09-04-002`, `DEP-09-04-003`, `DEP-09-04-004`, `DEP-09-04-005`, `DEP-09-04-006`, `DEP-09-04-007`, `DEP-09-04-008`, `DEP-09-04-009`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Declared Downstream

Current extracted downstream rows: NONE. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- TASK + dependency-extract updated this register on 2026-05-20T21:02:18-0600 with `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, and `CONSUMER_CONTEXT=NONE`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Human ruling applied: semantic lensing and P3 enrichment are skipped; `_SEMANTIC.md` outputs are invalid evidence and were not read or consumed.
- Anchor document selection: `_CONTEXT.md` and `Datasheet.md`; execution document order: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`, `_REFERENCES.md`.
- Decomposition status: available and used to validate PKG-09, DEL-09-04, SOW-030, SOW-072, SOW-073, OI-003, and OI-004.
- [RESOLVED 2026-07-12] REF-006 docs/PRD.md is MATCH under D-APP-38; the mismatch warning remains only in dated 2026-05-20 run history.
- [WARNING] OPEN_ISSUE_TARGET_TYPE: OI-003 and OI-004 were preserved as `TargetType=UNKNOWN` because `OPEN_ISSUE` is not a Dependencies.csv v3.1 target enum.
- No `[WARNING] FLOATING_NODE`: one ACTIVE parent anchor (`DEP-09-04-001`) exists.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE parent anchor exists.

## Extracted Dependency Register

`Dependencies.csv` v3.1 contains 9 ACTIVE rows.

### Counts

| Dimension | Counts |
|---|---|
| DependencyClass | ANCHOR=4; EXECUTION=5 |
| DependencyType | OTHER=4; PREREQUISITE=2; CONSTRAINT=3 |
| Status | ACTIVE=9 |
| SatisfactionStatus | NOT_APPLICABLE=3; TBD=6 |
| TargetType | PACKAGE=1; REQUIREMENT=4; EXTERNAL=2; UNKNOWN=2 |

### Compact Register

| DependencyID | Class | Type | Direction | Target | Status | Satisfaction |
|---|---|---|---|---|---|---|
| DEP-09-04-001 | ANCHOR | OTHER | UPSTREAM | PKG-09 | ACTIVE | NOT_APPLICABLE |
| DEP-09-04-002 | ANCHOR | OTHER | UPSTREAM | SOW-030 | ACTIVE | NOT_APPLICABLE |
| DEP-09-04-003 | ANCHOR | OTHER | UPSTREAM | SOW-072 | ACTIVE | NOT_APPLICABLE |
| DEP-09-04-004 | ANCHOR | OTHER | UPSTREAM | SOW-073 | ACTIVE | TBD |
| DEP-09-04-005 | EXECUTION | PREREQUISITE | UPSTREAM | Node.js and frontend npm dependencies | ACTIVE | TBD |
| DEP-09-04-006 | EXECUTION | PREREQUISITE | UPSTREAM | Pre-packaging local validation commands | ACTIVE | TBD |
| DEP-09-04-007 | EXECUTION | CONSTRAINT | UPSTREAM | OI-004 | ACTIVE | TBD |
| DEP-09-04-008 | EXECUTION | CONSTRAINT | UPSTREAM | OI-003 | ACTIVE | TBD |
| DEP-09-04-009 | EXECUTION | CONSTRAINT | UPSTREAM | DEL-09-04-REQ-009 | ACTIVE | TBD |

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE Rows |
|---|---|---|---|---|---|
| 2026-05-20T21:02:18-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` available | REF-006_HASH_MISMATCH; OPEN_ISSUE_TARGET_TYPE | 9 |

## Lifecycle Summary

Current descriptive counts from unchanged `Dependencies.csv` (2026-09-22); this projection does not change satisfaction or maturity.

| Field | Count |
|---|---:|
| ACTIVE | 9 |
| RequiredMaturity=SEMANTIC_READY | 9 |
| ProposedMaturity=SEMANTIC_READY | 4 |
| ProposedMaturity=TBD | 5 |
| SatisfactionStatus=NOT_APPLICABLE | 3 |
| SatisfactionStatus=TBD | 6 |

## D-APP-56 R5 P40 register annotation (2026-07-12)

REF-006 is MATCH under D-APP-38. Any HASH_MISMATCH token retained in the dated Run History is extraction provenance, not current dependency state. Structured-row status and summary counts above reflect Dependencies.csv after UPD-077..079.

## Current record interpretation — 2026-09-22

Earlier extraction notes, counts, source states and file citations retain their dated basis. Current production claims live in `ScopeOfWork.md`; removed four-document files are historical evidence. D-GOV-43/D-APP-127 make the App-owned Runtime/Codex path current; SDK MCP/hooks and daemon proofs are compatibility history. Formal row mutations require the owning dependency pass; this descriptive update grants none.

## Current evidence-locator refresh — 2026-09-22

1 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

1 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=9; RETIRED=0; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_SOURCE_09_PREVIEW.csv`; current rows: ACTIVE=9, RETIRED=0. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.
