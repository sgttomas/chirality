# Dependencies: DEL-09-02 Section 9 Runtime Validation Additions

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows: `DEP-09-02-001`, `DEP-09-02-002`, `DEP-09-02-003`, `DEP-09-02-004`, `DEP-09-02-005`, `DEP-09-02-006`, `DEP-09-02-007`, `DEP-09-02-008`, `DEP-09-02-009`, `DEP-09-02-010`, `DEP-09-02-011`, `DEP-09-02-012`, `DEP-09-02-013`, `DEP-09-02-014`, `DEP-09-02-015`, `DEP-09-02-016`, `DEP-09-02-017`, `DEP-09-02-018`, `DEP-09-02-019`, `DEP-09-02-020`, `DEP-09-02-021`, `DEP-09-02-022`, `DEP-09-02-023`, `DEP-09-02-024`, `DEP-09-02-025`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Declared Downstream

Current extracted downstream rows: NONE. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 dependency-extract run used MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE.
- Decomposition authority loaded: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; anchor validation and target-label resolution were available.
- Source docs used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Human ruling applied: semantic lensing and P3 enrichment are skipped; `_SEMANTIC.md` was not read and was not consumed as evidence.
- Defaults applied: SOURCE_DOCS=AUTO, DOC_ROLE_MAP=DEFAULT, ANCHOR_DOC=Datasheet.md, EXECUTION_DOC_ORDER=Specification.md then Guidance.md then Procedure.md then Datasheet.md.
- [RESOLVED 2026-07-12] REF-006 docs/PRD.md is MATCH under D-APP-38; the mismatch warning remains only in dated 2026-05-20 run history.
- [WARNING] TBD_SURFACES: exact validation registry path, runner entrypoint, local validation command, summary schema path, and summary fields remain TBD in source documents.
- No `[WARNING] FLOATING_NODE`: one active `IMPLEMENTS_NODE` anchor was extracted.
- No `[WARNING] AMBIGUOUS_ANCHOR`: only one active `IMPLEMENTS_NODE` anchor was extracted.

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1

| Metric | Count |
|---|---:|
| Total rows | 25 |
| ACTIVE rows | 25 |
| RETIRED rows | 0 |
| ANCHOR rows | 13 |
| EXECUTION rows | 12 |
| IMPLEMENTS_NODE anchors | 1 |
| TRACES_TO_REQUIREMENT anchors | 12 |
| UPSTREAM execution rows | 12 |
| DOWNSTREAM execution rows | 0 |

| DependencyID | Class | Type | Direction | Target | Status |
|---|---|---|---|---|---|
| DEP-09-02-001 | ANCHOR | OTHER | UPSTREAM | PKG-09 | ACTIVE | TBD |
| DEP-09-02-002 | ANCHOR | OTHER | UPSTREAM | SOW-036 | ACTIVE | TBD |
| DEP-09-02-003 | ANCHOR | OTHER | UPSTREAM | SOW-037 | ACTIVE | TBD |
| DEP-09-02-004 | ANCHOR | OTHER | UPSTREAM | SOW-039 | ACTIVE | TBD |
| DEP-09-02-005 | ANCHOR | OTHER | UPSTREAM | SOW-045 | ACTIVE | TBD |
| DEP-09-02-006 | ANCHOR | OTHER | UPSTREAM | SOW-054 | ACTIVE | TBD |
| DEP-09-02-007 | ANCHOR | OTHER | UPSTREAM | SOW-057 | ACTIVE | TBD |
| DEP-09-02-008 | ANCHOR | OTHER | UPSTREAM | SOW-063 | ACTIVE | TBD |
| DEP-09-02-009 | ANCHOR | OTHER | UPSTREAM | OBJ-002 | ACTIVE | TBD |
| DEP-09-02-010 | ANCHOR | OTHER | UPSTREAM | OBJ-003 | ACTIVE | TBD |
| DEP-09-02-011 | ANCHOR | OTHER | UPSTREAM | OBJ-005 | ACTIVE | TBD |
| DEP-09-02-012 | ANCHOR | OTHER | UPSTREAM | OBJ-007 | ACTIVE | TBD |
| DEP-09-02-013 | ANCHOR | OTHER | UPSTREAM | OBJ-008 | ACTIVE | TBD |
| DEP-09-02-014 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-09-01 | ACTIVE | TBD |
| DEP-09-02-015 | EXECUTION | INTERFACE | UPSTREAM | DEL-03-01 | ACTIVE | TBD |
| DEP-09-02-016 | EXECUTION | INTERFACE | UPSTREAM | DEL-04-03 | ACTIVE | TBD |
| DEP-09-02-017 | EXECUTION | INTERFACE | UPSTREAM | DEL-05-02 | ACTIVE | TBD |
| DEP-09-02-018 | EXECUTION | INTERFACE | UPSTREAM | DEL-04-02 | ACTIVE | TBD |
| DEP-09-02-019 | EXECUTION | INTERFACE | UPSTREAM | DEL-06-01 | ACTIVE | TBD |
| DEP-09-02-020 | EXECUTION | INTERFACE | UPSTREAM | DEL-06-03 | ACTIVE | TBD |
| DEP-09-02-021 | EXECUTION | INTERFACE | UPSTREAM | DEL-06-04 | ACTIVE | TBD |
| DEP-09-02-022 | EXECUTION | INTERFACE | UPSTREAM | DEL-06-06 | ACTIVE | TBD |
| DEP-09-02-023 | EXECUTION | INTERFACE | UPSTREAM | DEL-05-05 | ACTIVE | TBD |
| DEP-09-02-024 | EXECUTION | INTERFACE | UPSTREAM | DEL-08-04 | ACTIVE | TBD |
| DEP-09-02-025 | EXECUTION | INTERFACE | UPSTREAM | DEL-08-05 | ACTIVE | TBD |

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ActiveRows |
|---|---|---|---|---|---:|
| 2026-05-20T20:54:54-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` loaded | PRD_HASH_MISMATCH; TBD_SURFACES | 25 |

## Lifecycle Summary

Current descriptive counts from unchanged `Dependencies.csv` (2026-09-22); this projection does not change satisfaction or maturity.

| Field | Count |
|---|---:|
| ACTIVE | 25 |
| RequiredMaturity=SEMANTIC_READY | 25 |
| ProposedMaturity=TBD | 25 |
| SatisfactionStatus=TBD | 25 |

## D-APP-56 R5 P40 register annotation (2026-07-12)

REF-006 is MATCH under D-APP-38. Any HASH_MISMATCH token retained in the dated Run History is extraction provenance, not current dependency state. Structured-row status and summary counts above reflect Dependencies.csv after UPD-077..079.

## Current record interpretation — 2026-09-22

Earlier extraction notes, counts, source states and file citations retain their dated basis. Current production claims live in `ScopeOfWork.md`; removed four-document files are historical evidence. D-GOV-43/D-APP-127 make the App-owned Runtime/Codex path current; SDK MCP/hooks and daemon proofs are compatibility history. Formal row mutations require the owning dependency pass; this descriptive update grants none.

## Current residual-specific interpretation — 2026-09-22

TBD_SURFACES is an obsolete extraction warning for selected paths; ScopeOfWork.md now names current harness manifest/runner hooks. Actual satisfaction of the Runtime/Codex coverage still requires candidate-bound results against governing ScopeOfWork.md.

## Current evidence-locator refresh — 2026-09-22

19 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=25; RETIRED=0; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_SOURCE_09_PREVIEW.csv`; current rows: ACTIVE=25, RETIRED=0. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.
