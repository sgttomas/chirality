# Dependencies: DEL-07-06 Reference Hash and Snapshot Conventions

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows: `DEP-07-06-001`, `DEP-07-06-002`, `DEP-07-06-003`, `DEP-07-06-004`, `DEP-07-06-005`, `DEP-07-06-006`, `DEP-07-06-007`, `DEP-07-06-008`, `DEP-07-06-009`, `DEP-07-06-010`, `DEP-07-06-011`, `DEP-07-06-012`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Declared Downstream

Current extracted downstream rows: NONE. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 dependency-recording run used `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority at `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Human ruling applied: semantic lensing and P3 enrichment were skipped; `_SEMANTIC.md` was not read or consumed and is not evidence for this register.
- Anchor doc selected: `Datasheet.md` with `_CONTEXT.md` and decomposition authority for validation.
- Execution doc order selected: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`, `_REFERENCES.md`, `_CONTEXT.md`, `_DEPENDENCIES.md`.
- [RESOLVED 2026-07-12] REF-006 docs/PRD.md is MATCH under D-APP-38; the mismatch warning remains only in dated 2026-05-20 run history.
- `[WARNING] TARGET_NOT_READ: _STATUS.md is an explicit Procedure prerequisite target, but it was not read or consumed because the dependency-recording ruling restricted evidence sources. Satisfaction remains TBD.`
- `[WARNING] DEPENDENCY_EDGES_TBD: Procedure names accepted dependency edges as a prerequisite, while existing _DEPENDENCIES.md declares no accepted upstream/downstream edges yet.`
- Parent anchor check: one ACTIVE `IMPLEMENTS_NODE` row found; no `FLOATING_NODE` or `AMBIGUOUS_ANCHOR` warning.

## Extracted Dependency Register

Current register: `Dependencies.csv` v3.1.

| Count Type | Value |
|---|---:|
| Total rows | 13 |
| ACTIVE rows | 12 |
| RETIRED rows | 1 |
| ANCHOR rows | 6 |
| EXECUTION rows | 7 |
| Parent anchors (`IMPLEMENTS_NODE`) | 1 |
| Trace anchors (`TRACES_TO_REQUIREMENT`) | 5 |

| DependencyID | Class | Type | Direction | Target | Status | Evidence |
|---|---|---|---|---|---|---|
| DEP-07-06-001 | ANCHOR | OTHER | UPSTREAM | PKG-07 | ACTIVE | TBD |
| DEP-07-06-002 | ANCHOR | OTHER | UPSTREAM | SOW-032 | ACTIVE | TBD |
| DEP-07-06-003 | ANCHOR | OTHER | UPSTREAM | SOW-033 | ACTIVE | TBD |
| DEP-07-06-004 | ANCHOR | OTHER | UPSTREAM | SOW-034 | ACTIVE | TBD |
| DEP-07-06-005 | ANCHOR | OTHER | UPSTREAM | OBJ-006 | ACTIVE | TBD |
| DEP-07-06-006 | ANCHOR | OTHER | UPSTREAM | OBJ-009 | ACTIVE | TBD |
| DEP-07-06-007 | EXECUTION | PREREQUISITE | UPSTREAM | LOCAL-CONTEXT | ACTIVE | TBD |
| DEP-07-06-008 | EXECUTION | PREREQUISITE | UPSTREAM | LOCAL-REFERENCES | ACTIVE | TBD |
| DEP-07-06-009 | EXECUTION | PREREQUISITE | UPSTREAM | LOCAL-DEPENDENCIES | ACTIVE | TBD |
| DEP-07-06-010 | EXECUTION | PREREQUISITE | UPSTREAM | LOCAL-STATUS | ACTIVE | TBD |
| DEP-07-06-011 | EXECUTION | PREREQUISITE | UPSTREAM | DECOMPOSITION-v3.2 | ACTIVE | TBD |
| DEP-07-06-012 | EXECUTION | PREREQUISITE | UPSTREAM | REF-001-REF-007 | ACTIVE | TBD |
| DEP-07-06-013 | EXECUTION | CONSTRAINT | UPSTREAM | REF-006 | RETIRED | NOT_APPLICABLE |

## Lifecycle Summary

Current descriptive counts from unchanged `Dependencies.csv` (2026-09-22); this projection does not change satisfaction or maturity.

| Field | Count |
|---|---:|
| ACTIVE | 12 |
| RETIRED | 1 |
| RequiredMaturity=SEMANTIC_READY | 13 |
| ProposedMaturity=TBD | 13 |
| SatisfactionStatus=NOT_APPLICABLE | 1 |
| SatisfactionStatus=TBD | 12 |

## Run History

| Timestamp | Mode | Strictness | Decomposition Path / Status | Warnings | ACTIVE Counts |
|---|---|---|---|---|---|
| 2026-05-20T19:54:22-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` / found and used | `SOURCE_HASH_MISMATCH`, `TARGET_NOT_READ`, `DEPENDENCY_EDGES_TBD` | 13 total: 6 ANCHOR, 7 EXECUTION |

## D-APP-56 R5 P40 register annotation (2026-07-12)

REF-006 is MATCH under D-APP-38. Any HASH_MISMATCH token retained in the dated Run History is extraction provenance, not current dependency state. Structured-row status and summary counts above reflect Dependencies.csv after UPD-077..079.

## Current record interpretation — 2026-09-22

Earlier extraction notes, counts, source states and file citations retain their dated basis. Current production claims live in `ScopeOfWork.md`; removed four-document files are historical evidence. D-GOV-43/D-APP-127 make the App-owned Runtime/Codex path current; SDK MCP/hooks and daemon proofs are compatibility history. Formal row mutations require the owning dependency pass; this descriptive update grants none.

## Current evidence-locator refresh — 2026-09-22

7 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=12; RETIRED=1; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

## Current evidence-locator refresh — 2026-09-22

2 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

1 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.
