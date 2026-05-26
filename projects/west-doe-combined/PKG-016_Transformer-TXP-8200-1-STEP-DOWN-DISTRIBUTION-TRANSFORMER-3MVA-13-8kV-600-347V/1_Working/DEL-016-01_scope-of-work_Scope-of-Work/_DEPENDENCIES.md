# Dependencies: DEL-016-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

**Schema version:** v3.1
**Total rows:** 14
**ACTIVE:** 14 | **RETIRED:** 0

### ANCHOR rows (8 ACTIVE)

| DependencyID | AnchorType | TargetRefID | TargetName | Confidence |
|---|---|---|---|---|
| DEP-016-01-001 | IMPLEMENTS_NODE | SOW-0017 | Scope decision SOW-0017 — Transformer TXP-8200-1 (WBS 02) | HIGH |
| DEP-016-01-002 | TRACES_TO_REQUIREMENT | OBJ-002 | Project Objective OBJ-002 — 03-25 compressor station and liquids hub scope | HIGH |
| DEP-016-01-003 | TRACES_TO_REQUIREMENT | OBJ-004 | Project Objective OBJ-004 — vendor-owned electrical and mechanical equipment packages | HIGH |
| DEP-016-01-004 | TRACES_TO_REQUIREMENT | OBJ-005 | Project Objective OBJ-005 — facility electrical power and infrastructure | HIGH |
| DEP-016-01-005 | TRACES_TO_REQUIREMENT | OBJ-006 | Project Objective OBJ-006 — controls instrumentation communications | HIGH |
| DEP-016-01-006 | TRACES_TO_REQUIREMENT | OBJ-008 | Project Objective OBJ-008 — civil structural site buildings foundations | HIGH |
| DEP-016-01-007 | TRACES_TO_REQUIREMENT | OBJ-009 | Project Objective OBJ-009 — sour-service safety relief regulatory | HIGH |
| DEP-016-01-008 | TRACES_TO_REQUIREMENT | OBJ-010 | Project Objective OBJ-010 — operability maintainability vendor documentation | HIGH |

### EXECUTION rows (6 ACTIVE)

| DependencyID | Direction | DependencyType | TargetType | TargetID / TargetName | Confidence |
|---|---|---|---|---|---|
| DEP-016-01-009 | UPSTREAM | PREREQUISITE | DOCUMENT | DBM-Comp_and_Liquids SEC-12 Electrical Basis | HIGH |
| DEP-016-01-010 | UPSTREAM | PREREQUISITE | DOCUMENT | DBM-Comp_and_Liquids SEC-08 Buildings and Foundations | HIGH |
| DEP-016-01-011 | UPSTREAM | PREREQUISITE | DOCUMENT | INTERFACE_REGISTER.csv — 7 PKG-016 interface rows | HIGH |
| DEP-016-01-012 | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-016-02_package-datasheet (Package Datasheet) | HIGH |
| DEP-016-01-013 | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-016-04_vendor-engineered-equipment-package (Vendor Engineered Equipment Package) | HIGH |
| DEP-016-01-014 | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-016-03_construction-work-package (Construction Work Package) | HIGH |

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; primary evidence sources: `Specification.md`, `Procedure.md`
- **ANCHOR_DOC:** `Specification.md` (contains explicit WBS, SOW, and objective references)
- **EXECUTION_DOCS:** `Procedure.md`, `Specification.md`
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — used to validate SOW-0017, OBJ-* identifiers, and resolve canonical labels. Confirmed present.
- **Parent anchor:** DEP-016-01-001 implements SOW-0017 (single IMPLEMENTS_NODE; no AMBIGUOUS_ANCHOR warning).
- **Objective traces:** 7 objective trace anchors extracted from DELIVERABLE_REGISTER.csv OBJ column (OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010).
- **EXECUTION edges:** 3 upstream PREREQUISITE (DBM SEC-12, DBM SEC-08, INTERFACE_REGISTER.csv) extracted from Specification.md and Procedure.md explicit citations. 3 downstream HANDOVER edges to DEL-016-02, DEL-016-03, DEL-016-04 extracted from Specification.md out-of-scope section and Procedure.md Step 9.
- **No coordination-only edges emitted** per information-flow-only constraint.
- **No invented targets:** All TargetDeliverableIDs confirmed in DELIVERABLE_REGISTER.csv; all TargetRefIDs confirmed in SCOPE_LEDGER.csv and OBJECTIVE_REGISTER.csv.
- **Tree x DAG integrity:** IMPLEMENTS_NODE count = 1 (PASS). No FLOATING_NODE warning. No AMBIGUOUS_ANCHOR warning.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First EXTRACTED run via dependency-extract skill. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. 14 rows written (8 ANCHOR, 6 EXECUTION), all ACTIVE. Decomposition path confirmed at GATE-07_Final_Published_2026-05-24. No warnings.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 14 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 14 |
