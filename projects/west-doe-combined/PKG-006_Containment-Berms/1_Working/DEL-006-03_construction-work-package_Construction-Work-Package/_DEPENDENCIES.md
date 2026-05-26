# Dependencies: DEL-006-03_construction-work-package — Construction Work Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

13 rows extracted (all ACTIVE). Schema version: v3.1.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-006-03-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0006 | Scope decision SOW-0006 — Containment Berms (WBS 03) | HIGH | ACTIVE |
| DEP-006-03-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | Project Objective OBJ-002 | HIGH | ACTIVE |
| DEP-006-03-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | Project Objective OBJ-007 | HIGH | ACTIVE |
| DEP-006-03-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 | HIGH | ACTIVE |
| DEP-006-03-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 | HIGH | ACTIVE |
| DEP-006-03-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 | HIGH | ACTIVE |
| DEP-006-03-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-006-01_scope-of-work | Scope of Work — PKG-006 | MEDIUM | ACTIVE |
| DEP-006-03-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-006-02_package-datasheet | Package Datasheet — PKG-006 | HIGH | ACTIVE |
| DEP-006-03-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | EXTERNAL | — | Final geotechnical report | HIGH | ACTIVE |
| DEP-006-03-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | EXTERNAL | — | Final hydrology input | HIGH | ACTIVE |
| DEP-006-03-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | EXTERNAL | — | Approved IFC civil drawings and specifications | HIGH | ACTIVE |
| DEP-006-03-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-62ACD644F9 | Drain / Containment interface — PKG-006 | HIGH | ACTIVE |
| DEP-006-03-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-2A535A882C | Grading / Site Drainage / Spill Containment interface — PKG-006 | HIGH | ACTIVE |

**ANCHOR rows:** 6 (1 IMPLEMENTS_NODE + 5 TRACES_TO_REQUIREMENT)
**EXECUTION rows:** 7 (2 DELIVERABLE prerequisites, 2 EXTERNAL constraints, 1 EXTERNAL prerequisite, 2 DOCUMENT interfaces)
**Total ACTIVE:** 13 | **RETIRED:** 0

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder. Sources used: `_CONTEXT.md`, `Datasheet.md`, `Specification.md`, `Procedure.md`, `Guidance.md`, `_REFERENCES.md`.
- **ANCHOR_DOC (AUTO):** `Datasheet.md` selected as primary anchor document (contains identity, SOW reference, objective traces).
- **EXECUTION_DOC_ORDER (AUTO):** `Procedure.md`, `Specification.md`, `Guidance.md`.
- **DECOMPOSITION_PATH:** GATE-07 snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` used for anchor validation. Note: brief specified `GATE-07_Final_Published_2026-05-24/` as a direct path but that path does not exist as a standalone directory; the correct path under `_GateSnapshots/` was used. No MISSING_DECOMPOSITION warning applies — snapshot was resolved successfully.
- **ID format:** DependencyID format DEP-006-03-NNN applied throughout.
- **Tree x DAG integrity:** 1 IMPLEMENTS_NODE parent anchor found (DEP-006-03-001 → SOW-0006). No FLOATING_NODE or AMBIGUOUS_ANCHOR warnings.
- **Declared edges:** None were declared in PREPARATION; all 13 rows are EXTRACTED.
- Pass 1 (ANCHOR) completed before Pass 2 (EXECUTION) per skill discipline.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 13 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 11 |
| PENDING | 2 |

PENDING rows: DEP-006-03-009 (final geotechnical report), DEP-006-03-010 (final hydrology input), DEP-006-03-011 (IFC civil drawings). Note: DEP-006-03-011 is marked PENDING; counted above as TBD/PENDING — correction: 10 TBD + 3 PENDING = 13 total. See Dependencies.csv for authoritative values.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract skill run; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition: GATE-07_Final_Published_2026-05-24 snapshot resolved under _GateSnapshots/. 13 rows extracted (all ACTIVE). No prior Dependencies.csv existed; file created fresh. No FLOATING_NODE, AMBIGUOUS_ANCHOR, or MISSING_DECOMPOSITION warnings.
