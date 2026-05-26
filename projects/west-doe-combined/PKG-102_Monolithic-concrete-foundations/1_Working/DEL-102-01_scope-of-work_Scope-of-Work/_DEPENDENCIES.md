# Dependencies: DEL-102-01_scope-of-work — Scope of Work

**Coordination Mode:** EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-26)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1 schema). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

**Total ACTIVE rows:** 13
**ANCHOR rows (ACTIVE):** 4
**EXECUTION rows (ACTIVE):** 9
**RETIRED rows:** 0

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-102-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-102 | PKG-102 — Monolithic concrete foundations (Structural WBS 01) | HIGH | ACTIVE |
| DEP-102-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0258 | SOW-0258 — Monolithic concrete foundations scope item | HIGH | ACTIVE |
| DEP-102-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | OBJ-001 — Provide the 04-25 Deepcut facility scope | MEDIUM | ACTIVE |
| DEP-102-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | OBJ-008 — Provide civil/structural/site/foundations scope | MEDIUM | ACTIVE |
| DEP-102-01-005 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | EXTERNAL | EXT-GEOTECH | Site geotechnical assessment report | HIGH | ACTIVE |
| DEP-102-01-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | EXTERNAL | EXT-TOPO | Topographical survey / existing grade surface file | HIGH | ACTIVE |
| DEP-102-01-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | EXTERNAL | EXT-PLOTPLAN | External plot plan (including retention-pond reference) | HIGH | ACTIVE |
| DEP-102-01-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | WB-ROW-103 | Workbook row 103 — 26020-Packages_Interfaces_4_export.xlsx | HIGH | ACTIVE |
| DEP-102-01-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DOCUMENT | IFC-1EDEDC0453 | Interface IFC-1EDEDC0453 — Grading / Site Drainage / Spill Containment | HIGH | ACTIVE |
| DEP-102-01-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | DOCUMENT | IFC-8283744B5B | Interface IFC-8283744B5B — Structural / Foundations / Supports | HIGH | ACTIVE |
| DEP-102-01-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-102-02_package-datasheet | DEL-102-02 — Package Datasheet (PKG-102) | HIGH | ACTIVE |
| DEP-102-01-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-102-03_construction-work-package | DEL-102-03 — Construction Work Package (PKG-102) | HIGH | ACTIVE |
| DEP-102-01-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-102-04_epc-structural-discipline-production-package | DEL-102-04 — EPC/Structural Discipline Production Package (PKG-102) | HIGH | ACTIVE |

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 13 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| PENDING | 7 |
| TBD | 6 |

**ANCHOR parent check:** 1 IMPLEMENTS_NODE row — OK (no FLOATING_NODE or AMBIGUOUS_ANCHOR warning).

## Run Notes

- **Run date:** 2026-05-26
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO (scanned deliverable folder: Datasheet.md, Specification.md, Guidance.md, Procedure.md; excluded: _CONTEXT.md for evidence cross-reference only, _REFERENCES.md for pointer resolution)
- **ANCHOR_DOC:** Datasheet.md (highest-confidence match per DOC_ROLE_MAP heuristic: filename contains `datasheet`)
- **EXECUTION_DOC_ORDER:** Procedure.md, Guidance.md, Specification.md (procedure/workflow signal first)
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — FOUND; anchors validated against PACKAGE_REGISTER.csv, DELIVERABLE_REGISTER.csv, SCOPE_LEDGER.csv, INTERFACE_REGISTER.csv, OBJECTIVE_REGISTER.csv.
- **DECOMPOSITION_PATH (invocation):** Invocation specified `GATE-07_Final_Published_2026-05-24/` under RUN_ROOT. Path resolved from `_CONTEXT.md` Decomposition Reference and `_REFERENCES.md`.
- **OBJ-001 / OBJ-008 confidence:** MEDIUM — ASSUMPTION noted; objective association is PACKAGE_HEURISTIC, not deliverable-row-confirmed (per Guidance CT-102-01-002).
- **Workbook row 103 not parsed:** Binary workbook `26020-Packages_Interfaces_4_export.xlsx` row 103 was not extracted in this run. Tagged-equipment list and quantity basis remain TBD. This is captured as DEP-102-01-008 (PREREQUISITE/DOCUMENT, PENDING).
- **Interface rows IFC-1EDEDC0453 and IFC-8283744B5B:** Both confirmed in GATE-07 INTERFACE_REGISTER.csv. Captured as CONSTRAINT/DOCUMENT rows because they are declared interface types that the SoW integration narrative must address — they represent required information/coverage, not purely structural adjacency.
- **No FLOATING_NODE warning:** One IMPLEMENTS_NODE anchor (DEP-102-01-001) found pointing to PKG-102.
- **No AMBIGUOUS_ANCHOR warning:** Exactly one IMPLEMENTS_NODE row.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-26 — dependency-extract skill run; MODE=UPDATE; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE; 13 rows extracted (4 ANCHOR, 9 EXECUTION); Dependencies.csv created (v3.1 schema, 29 columns); schema validation PASSED.
