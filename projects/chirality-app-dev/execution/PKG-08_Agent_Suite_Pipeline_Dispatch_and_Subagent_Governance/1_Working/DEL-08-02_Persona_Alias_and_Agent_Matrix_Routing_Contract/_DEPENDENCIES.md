# Dependencies: DEL-08-02 Persona Alias and Agent Matrix Routing Contract

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows: `DEP-08-02-001`, `DEP-08-02-002`, `DEP-08-02-003`, `DEP-08-02-004`, `DEP-08-02-005`, `DEP-08-02-006`, `DEP-08-02-007`, `DEP-08-02-008`, `DEP-08-02-009`, `DEP-08-02-010`, `DEP-08-02-011`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Declared Downstream

Current extracted downstream rows: `DEP-08-02-012`, `DEP-08-02-013`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Extracted Dependency Register

`Dependencies.csv` was created in v3.1 format with 13 ACTIVE extracted rows.

| Count | Class | Type | Status | Notes |
|---:|---|---|---|---|
| 6 | ANCHOR | OTHER | ACTIVE | One parent package anchor plus five trace anchors to SOW/objective identifiers. |
| 5 | EXECUTION | PREREQUISITE | ACTIVE | Document prerequisites grounded in deliverable-local source summaries and `_REFERENCES.md`. |
| 2 | EXECUTION | INTERFACE | ACTIVE | Explicit interface boundaries with DEL-04-04 and DEL-08-03. |

### Compact Register

| DependencyID | Class | Type | Direction | TargetType | Target | Status |
|---|---|---|---|---|---|---|
| DEP-08-02-001 | ANCHOR | OTHER | UPSTREAM | PACKAGE | PKG-08 Agent Suite, Pipeline Dispatch, and Subagent Governance | ACTIVE |
| DEP-08-02-002 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | SOW-005 Matrix rendering and routing | ACTIVE |
| DEP-08-02-003 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | SOW-006 Workbench context | ACTIVE |
| DEP-08-02-004 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | SOW-017 Persona resolution and prompt composition | ACTIVE |
| DEP-08-02-005 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | OBJ-001 Governed local desktop harness objective | ACTIVE |
| DEP-08-02-006 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | OBJ-007 Agent-suite integrity objective | ACTIVE |
| DEP-08-02-007 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | REF-004 docs/TYPES.md | ACTIVE |
| DEP-08-02-008 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | REF-006 docs/PRD.md | ACTIVE |
| DEP-08-02-009 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | REF-003 docs/SPEC.md | ACTIVE |
| DEP-08-02-010 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | REF-002 docs/CONTRACT.md | ACTIVE |
| DEP-08-02-011 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | REF-001 docs/DIRECTIVE.md | ACTIVE |
| DEP-08-02-012 | EXECUTION | INTERFACE | DOWNSTREAM | DELIVERABLE | DEL-04-04 PersonaComposer from Instruction Root | ACTIVE |
| DEP-08-02-013 | EXECUTION | INTERFACE | DOWNSTREAM | DELIVERABLE | DEL-08-03 Pipeline Category and Task Scope Dispatch | ACTIVE |

## Run Notes

- Run timestamp: 2026-05-20T20:54:44-0600.
- TaskSkill: `dependency-extract`; mode `UPDATE`; strictness `CONSERVATIVE`; consumer context `NONE`.
- Decomposition authority: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Human ruling applied: semantic lensing and P3 enrichment are skipped; `_SEMANTIC.md` is invalid evidence and was not read or consumed.
- Defaults applied: `SOURCE_DOCS=AUTO`, `DOC_ROLE_MAP=DEFAULT`, `ANCHOR_DOC=Datasheet.md`, `EXECUTION_DOC_ORDER=Specification.md -> Guidance.md -> Procedure.md -> _REFERENCES.md`.
- `[RESOLVED] SOURCE_STATE`: D-APP-38 authority corpus v2 supersedes the prior PRD hash warning; `_REFERENCES.md` now records REF-006 as MATCH.
- `[RESOLVED] LOOP_FIRST_CONTRACT`: ADQ-12 records the current Type 0/1 loop-persona alias and matrix contract; old `AGGREGATE`/`RECONCILING` alias requirements are not preserved as compatibility behavior.
- `[RESOLVED] IMPLEMENTATION_PATHS`: ADQ-12 evidence records the persona-resolution, matrix-cell, matrix-launch, and Pipeline component/test paths used for this tranche.
- Non-emitted edge note: shared SOW ownership with DEL-02-01 and DEL-02-02 was not converted into execution edges because the allowed source documents do not state a concrete handoff or interface contract to those deliverables.
- Non-emitted edge note: REF-005 `docs/PLAN.md` and REF-007 `AGENT_SOFTWARE_DECOMP.md` were not emitted as dependency rows because evidence only identifies them as context/method references, not execution prerequisites for this deliverable.

## Run History

| Timestamp | Mode | Strictness | Decomposition | Validator | ACTIVE Rows | Warnings |
|---|---|---|---|---|---:|---|
| 2026-06-21T05:00:00-0600 | ADQ-12 | CONSERVATIVE | D-APP-38 current authority corpus, loop-first alias contract, and implementation-path evidence applied | PASS: focused PKG-08 tests | 13 | none |
| 2026-05-20T20:54:44-0600 | UPDATE | CONSERVATIVE | v3.2 found | PASS: 29 columns, 13 rows | 13 | superseded PRD_HASH_MISMATCH; superseded implementation-path TBDs |

## Lifecycle Summary

Current descriptive counts from unchanged `Dependencies.csv` (2026-09-22); this projection does not change satisfaction or maturity.

| Field | Count |
|---|---:|
| ACTIVE | 13 |
| RequiredMaturity=SEMANTIC_READY | 13 |
| ProposedMaturity=TBD | 13 |
| SatisfactionStatus=PENDING | 5 |
| SatisfactionStatus=SATISFIED | 6 |
| SatisfactionStatus=TBD | 2 |

## Current record interpretation — 2026-09-22

Earlier extraction notes, counts, source states and file citations retain their dated basis. Current production claims live in `ScopeOfWork.md`; removed four-document files are historical evidence. D-GOV-43/D-APP-127 make the App-owned Runtime/Codex path current; SDK MCP/hooks and daemon proofs are compatibility history. Formal row mutations require the owning dependency pass; this descriptive update grants none.

## Current evidence-locator refresh — 2026-09-22

9 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

2 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

2 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.
