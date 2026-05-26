# Dependencies: DEL-005-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED
**Dependency tracking mode:** EXTRACTED (dependency-extract run completed)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

13 rows extracted (all ACTIVE). Counts by class:

| DependencyClass | AnchorType | Direction | Count |
|---|---|---|---|
| ANCHOR | IMPLEMENTS_NODE | UPSTREAM | 1 |
| ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | 4 |
| EXECUTION | NOT_APPLICABLE | UPSTREAM | 5 |
| EXECUTION | NOT_APPLICABLE | DOWNSTREAM | 3 |

Compact table (ACTIVE rows):

| DependencyID | Class | AnchorType | Dir | Type | TargetType | TargetRefID / TargetDeliverableID | Statement (summary) |
|---|---|---|---|---|---|---|---|
| DEP-005-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0005 | DEL-005-01 implements SOW-0005: Site Grading WBS 03 |
| DEP-005-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | Traces to OBJ-002: 03-25 compressor station and liquids hub |
| DEP-005-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | Traces to OBJ-007: shared utilities and ancillary support |
| DEP-005-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Traces to OBJ-008: civil/structural/site/grading scope |
| DEP-005-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Traces to OBJ-009: safety/regulatory requirements |
| DEP-005-01-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Final geotechnical report required before foundation design closure |
| DEP-005-01-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Site-specific hydrology/IDF data required before drainage/retention-pond closure |
| DEP-005-01-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Plot plan/civil drawings required before final issue (layout/spacing verification) |
| DEP-005-01-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | — | Gate 7 registers (DELIVERABLE_REGISTER, PACKAGE_REGISTER, SCOPE_LEDGER, INTERFACE_REGISTER) |
| DEP-005-01-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | — | Workbook Packages row 5 — 26020-Packages_Interfaces_4_export |
| DEP-005-01-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-005-02_package-datasheet | SOW enables Package Datasheet |
| DEP-005-01-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-005-03_construction-work-package | SOW enables Construction Work Package |
| DEP-005-01-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-005-04_epc-civil-discipline-production-package | SOW enables EPC/Civil Discipline Production Package |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE — ANCHOR rows emitted only when identifiers appear explicitly in source; EXECUTION rows emitted only for explicit information/artifact transfer signals.
- **DECOMPOSITION_PATH used:** `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — anchor IDs (SOW-0005, OBJ-002, OBJ-007, OBJ-008, OBJ-009) confirmed in SCOPE_LEDGER.csv and DELIVERABLE_REGISTER.csv.
- **ANCHOR_DOC:** `Datasheet.md` (contains "scope-of-work" and identification fields; highest confidence match per DEFAULT heuristic).
- **EXECUTION_DOCS order:** `Specification.md`, `Procedure.md`, `Datasheet.md` (Conditions section), supplemented by `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-02 and SEC-11.
- **SOURCE_DOCS:** AUTO — scanned all four deliverable documents plus DBM 03-25 source referenced in Datasheet.md References section. `_REFERENCES.md` reviewed but contains no document pointers that add new execution dependencies beyond those identified in the four deliverable documents.
- **CONSUMER_CONTEXT:** NONE — no downstream handoff notes section required.
- **Tree x DAG integrity:** 1 IMPLEMENTS_NODE anchor found — no FLOATING_NODE warning. No AMBIGUOUS_ANCHOR.
- **TargetLocation for DOCUMENT rows:** paths set where source file is locally accessible (_Sources/ and _Decomposition/); set to blank where document is not yet in _Sources (geotechnical report, hydrology data, plot plan/civil drawings).
- **Normalization:** No legacy Direction values encountered.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 13 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 8 |
| PENDING | 3 |
| SATISFIED | 2 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract run: UPDATE / CONSERVATIVE / decomposition GATE-07_Final_Published_2026-05-24 confirmed. 13 rows extracted (5 ANCHOR, 8 EXECUTION). 0 retired. No FLOATING_NODE. No AMBIGUOUS_ANCHOR. Schema validation: VALID.
