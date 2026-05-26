# Dependencies: DEL-004-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

13 rows extracted (all ACTIVE). Schema version: v3.1.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | SatisfactionStatus |
|---|---|---|---|---|---|---|---|---|---|
| DEP-004-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0004 | Scope decision SOW-0004 — Site Grading (WBS 02) | HIGH | TBD |
| DEP-004-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | Project Objective OBJ-002 | HIGH | TBD |
| DEP-004-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | Project Objective OBJ-007 | HIGH | TBD |
| DEP-004-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 — Civil/structural/site scope | HIGH | TBD |
| DEP-004-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 | HIGH | TBD |
| DEP-004-02-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | — | Gate 7 DELIVERABLE_REGISTER / PACKAGE_REGISTER / ARTIFACT_REGISTER / INTERFACE_REGISTER | HIGH | SATISFIED |
| DEP-004-02-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | — | Workbook Packages row 5 — 26020-Packages_Interfaces_4_export | HIGH | SATISFIED |
| DEP-004-02-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Final geotechnical report | HIGH | PENDING |
| DEP-004-02-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Site-specific hydrology / rainfall IDF update | HIGH | PENDING |
| DEP-004-02-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Civil drawings / plot plan | MEDIUM | PENDING |
| DEP-004-02-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DELIVERABLE | DEL-004-01_scope-of-work | Scope of Work | HIGH | TBD |
| DEP-004-02-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-004-03_construction-work-package | Construction Work Package | HIGH | TBD |
| DEP-004-02-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-004-04_epc-civil-discipline-production-package | EPC / Civil Discipline Production Package | MEDIUM | TBD |

## Lifecycle Summary

- ACTIVE: 13
- RETIRED: 0
- ANCHOR rows (ACTIVE): 5 (1 IMPLEMENTS_NODE + 4 TRACES_TO_REQUIREMENT)
- EXECUTION rows (ACTIVE): 8 (5 UPSTREAM + 3 DOWNSTREAM)
- SatisfactionStatus breakdown: SATISFIED=2, PENDING=3, TBD=8

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; primary source documents: `Datasheet.md` (ANCHOR_DOC), `Guidance.md`, `Procedure.md` (EXECUTION_DOC candidates)
- **ANCHOR_DOC:** `Datasheet.md` — contains Identification table with parent package, scope item, WBS, and objective mappings
- **EXECUTION_DOC_ORDER:** `Procedure.md`, `Guidance.md`, `Datasheet.md`
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — used; anchor identifiers validated against SCOPE_LEDGER.csv, DELIVERABLE_REGISTER.csv, and OBJECTIVE_DELIVERABLE_MAP.csv.
- **RUN_ROOT:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined`
- **BRIEF-specified DECOMPOSITION_PATH:** `GATE-07_Final_Published_2026-05-24/` — resolved to full path via `_CONTEXT.md` Decomposition Reference; no GATE-07 folder exists at the run-root level; decomposition path resolved from `_CONTEXT.md`.
- **Parent anchor:** 1 IMPLEMENTS_NODE row (DEP-004-02-001) for SOW-0004. No `[WARNING] FLOATING_NODE`.
- **Open prerequisites:** 3 PENDING rows (geotechnical report, hydrology update, civil drawings/plot plan) — these are explicitly identified open inputs in source documents; not blockers at INITIALIZED threshold.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract skill run; MODE=UPDATE STRICTNESS=CONSERVATIVE; decomposition path resolved via _CONTEXT.md; 13 rows extracted (5 ANCHOR + 8 EXECUTION), all ACTIVE; no RETIRED rows; schema validation VALID.
