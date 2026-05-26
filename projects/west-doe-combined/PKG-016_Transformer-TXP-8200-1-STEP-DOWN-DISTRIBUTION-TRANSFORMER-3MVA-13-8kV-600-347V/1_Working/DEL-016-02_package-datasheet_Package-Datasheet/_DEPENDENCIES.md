# Dependencies: DEL-016-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1); this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

12 rows extracted (all ACTIVE). Schema version: v3.1.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-016-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0017 | Scope decision SOW-0017 — Transformer TXP-8200-1 (WBS 02) | HIGH | ACTIVE |
| DEP-016-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | Project Objective OBJ-002 — 03-25 compressor station and liquids hub scope | HIGH | ACTIVE |
| DEP-016-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 — Vendor-owned package execution | HIGH | ACTIVE |
| DEP-016-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 — Facility electrical power basis | HIGH | ACTIVE |
| DEP-016-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 — Controls instrumentation communications | HIGH | ACTIVE |
| DEP-016-02-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 — Civil structural site and construction-support | HIGH | ACTIVE |
| DEP-016-02-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 — Safety relief and regulatory requirements | HIGH | ACTIVE |
| DEP-016-02-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 — Operability vendor documentation and turnover | HIGH | ACTIVE |
| DEP-016-02-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-016-01_scope-of-work | Scope of Work — PKG-016 | HIGH | ACTIVE |
| DEP-016-02-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | DBM 03-25 Comp and Liquids Design Basis Memorandum | HIGH | ACTIVE |
| DEP-016-02-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | — | INTERFACE_REGISTER.csv PKG-016 interface facts (7 IFC records) | HIGH | ACTIVE |
| DEP-016-02-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-016-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package — PKG-016 | HIGH | ACTIVE |

**ANCHOR rows:** 8 (1 IMPLEMENTS_NODE + 7 TRACES_TO_REQUIREMENT)
**EXECUTION rows:** 4 (2 UPSTREAM PREREQUISITE + 1 UPSTREAM INTERFACE + 1 DOWNSTREAM HANDOVER)

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 12 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 8 |
| PENDING | 3 |
| SATISFIED | 1 |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; primary source documents identified: `Datasheet.md` (ANCHOR_DOC by filename heuristic), `_CONTEXT.md`
- **ANCHOR_DOC:** `Datasheet.md` (contains datasheet in filename — highest-confidence ANCHOR_DOC match)
- **EXECUTION_DOC_ORDER:** `Datasheet.md`, `_CONTEXT.md`, `_REFERENCES.md`
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — used to validate anchors and resolve canonical labels
- **Parent anchor check:** 1 IMPLEMENTS_NODE row found (DEP-016-02-001 → SOW-0017). No FLOATING_NODE or AMBIGUOUS_ANCHOR warnings.
- **Decomposition validation:** SOW-0017 confirmed in SCOPE_LEDGER.csv; DEL-016-02 row confirmed in DELIVERABLE_REGISTER.csv with OBJ traces OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010.
- **Source gaps noted in Datasheet.md:** Insulation/cooling type, tap configuration, enclosure/installation, winding configuration, BIL, impedance TBD — no dependency edges emitted for TBD gaps (CONSERVATIVE strictness; evidence not present).
- **Existing Dependencies.csv:** None (first extraction run; file created).

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition: GATE-07_Final_Published_2026-05-24. 12 rows extracted (8 ANCHOR + 4 EXECUTION), all ACTIVE. No warnings. Schema validation: VALID.
