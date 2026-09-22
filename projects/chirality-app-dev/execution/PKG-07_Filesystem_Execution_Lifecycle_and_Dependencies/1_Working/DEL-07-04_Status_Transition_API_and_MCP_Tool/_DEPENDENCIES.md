# Dependencies: DEL-07-04 Status Transition API and MCP Tool

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows: `DEP-07-04-001`, `DEP-07-04-002`, `DEP-07-04-003`, `DEP-07-04-004`, `DEP-07-04-006`, `DEP-07-04-007`, `DEP-07-04-008`. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Declared Downstream

Current extracted downstream rows: NONE. These are existing register projections, not newly accepted human edges. `Dependencies.csv` and the accepted closure pointer control selectability; no status, target, maturity or satisfaction is changed.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- Source set used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Source set excluded by human ruling: `_SEMANTIC.md` was not read or consumed; semantic lensing and P3 enrichment are skipped.
- Anchor doc selection: `Datasheet.md` plus `_CONTEXT.md` traceability and decomposition validation.
- Execution doc order: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`, `_REFERENCES.md`.
- Decomposition status: available; DEL-07-04, SOW-028, OBJ-006, PKG-07, and referenced document metadata were validated against allowed evidence.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` parent anchor exists.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE `IMPLEMENTS_NODE` parent anchor exists.
- [RESOLVED 2026-07-12] REF-006 docs/PRD.md is MATCH under D-APP-38; the mismatch warning remains only in dated 2026-05-20 run history.
- `[WARNING] IMPLEMENTATION_LOCATION_TBD`: allowed evidence names no implementation module path; dependency row DEP-07-04-008 preserves the target as `UNKNOWN` / `TBD`.

## Extracted Dependency Register

`Dependencies.csv` v3.1 was populated on 2026-05-20 in `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.

| DependencyID | Class | Type | Direction | TargetType | TargetRefID | TargetName | Status |
|---|---|---|---|---|---|---|---|
| DEP-07-04-001 | ANCHOR | OTHER | UPSTREAM | WBS_NODE | SOW-028 | Status lifecycle and approval SHA | ACTIVE |
| DEP-07-04-002 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | OBJ-006 | Preserve filesystem project truth through working-root containment | ACTIVE |
| DEP-07-04-003 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | REF-003 | docs/SPEC.md | ACTIVE |
| DEP-07-04-004 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | REF-002 | docs/CONTRACT.md | ACTIVE |
| DEP-07-04-005 | EXECUTION | CONSTRAINT | UPSTREAM | DOCUMENT | REF-006 | docs/PRD.md | RETIRED |
| DEP-07-04-006 | EXECUTION | CONSTRAINT | UPSTREAM | DOCUMENT | REF-001 | docs/DIRECTIVE.md | ACTIVE |
| DEP-07-04-007 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | REF-004 | docs/TYPES.md | ACTIVE |
| DEP-07-04-008 | EXECUTION | PREREQUISITE | UPSTREAM | UNKNOWN | TBD | Implementation module location | ACTIVE |

Counts:

| Group | Count |
|---|---:|
| ACTIVE rows | 7 |
| RETIRED rows | 1 |
| ANCHOR rows | 2 |
| EXECUTION rows | 6 |
| OTHER rows | 2 |
| PREREQUISITE rows | 4 |
| CONSTRAINT rows | 2 |

## Run History

| Timestamp | Mode | Strictness | Decomposition path/status | Warnings | ACTIVE rows |
|---|---|---|---|---|---:|
| 2026-05-20T19:54:21-06:00 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` / available | PRD_HASH_MISMATCH; IMPLEMENTATION_LOCATION_TBD | 8 |

## Lifecycle Summary

Current descriptive counts from unchanged `Dependencies.csv` (2026-09-22); this projection does not change satisfaction or maturity.

| Field | Count |
|---|---:|
| ACTIVE | 7 |
| RETIRED | 1 |
| RequiredMaturity=SEMANTIC_READY | 8 |
| ProposedMaturity=SATISFIED | 1 |
| ProposedMaturity=SEMANTIC_READY | 2 |
| ProposedMaturity=TBD | 5 |
| SatisfactionStatus=NOT_APPLICABLE | 3 |
| SatisfactionStatus=PENDING | 4 |
| SatisfactionStatus=SATISFIED | 1 |

## D-APP-56 R5 P40 register annotation (2026-07-12)

REF-006 is MATCH under D-APP-38. Any HASH_MISMATCH token retained in the dated Run History is extraction provenance, not current dependency state. Structured-row status and summary counts above reflect Dependencies.csv after UPD-077..079.

## D-APP-56 R5 P45 current register summary (2026-07-12)

- **Source:** UPD-132
- **Current counts:** ACTIVE 7; RETIRED 1; NOT_APPLICABLE=3; PENDING=4; SATISFIED=1.
- **Correction:** DEP-07-04-008 resolves to landed implementation modules and is SATISFIED; ResponsibleParty remains separate.
- Earlier extraction and reconciliation history is preserved as dated evidence; this block is the current structured-register mirror.

## Current record interpretation — 2026-09-22

Earlier extraction notes, counts, source states and file citations retain their dated basis. Current production claims live in `ScopeOfWork.md`; removed four-document files are historical evidence. D-GOV-43/D-APP-127 make the App-owned Runtime/Codex path current; SDK MCP/hooks and daemon proofs are compatibility history. Formal row mutations require the owning dependency pass; this descriptive update grants none.

## Current evidence-locator refresh — 2026-09-22

4 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

1 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.
