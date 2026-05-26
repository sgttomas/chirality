# Dependencies: DEL-029-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (v3.1 register produced by dependency-extract)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the authoritative register; this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` produced by `TASK + dependency-extract` (2026-05-25). Schema version: v3.1. Data rows: 14.

### Compact Summary Table

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-029-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0030 | Scope Ledger node SOW-0030 — PKG-029 WBS 01 | ACTIVE |
| DEP-029-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Objective OBJ-001 — Provide 04-25 Deepcut facility scope | ACTIVE |
| DEP-029-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Objective OBJ-004 — Execute vendor-owned electrical/mechanical equipment packages | ACTIVE |
| DEP-029-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Objective OBJ-005 — Provide and integrate facility electrical power basis | ACTIVE |
| DEP-029-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Objective OBJ-006 — Provide and integrate controls | ACTIVE |
| DEP-029-02-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Objective OBJ-008 — Provide civil | ACTIVE |
| DEP-029-02-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Objective OBJ-009 — Carry sour-service safety | ACTIVE |
| DEP-029-02-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Objective OBJ-010 — Maintain operability | ACTIVE |
| DEP-029-02-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-029-01_scope-of-work | Scope of Work — DEL-029-01 | ACTIVE |
| DEP-029-02-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | GATE-07_Final_Published_2026-05-24 | Gate 7 PROJECT_DECOMP Snapshot | ACTIVE |
| DEP-029-02-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | IFC-717D0187BA; IFC-C49653E450; IFC-DFC1A10C2D; IFC-A5C9438164; IFC-81CFD2A32C; IFC-2C14FA1228; IFC-380F4773FB | INTERFACE_REGISTER rows for PKG-029 — seven applicable interfaces | ACTIVE |
| DEP-029-02-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-029-03_construction-work-package | Construction Work Package — DEL-029-03 | ACTIVE |
| DEP-029-02-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-029-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package — DEL-029-04 | ACTIVE |
| DEP-029-02-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-029-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance — DEL-029-06 | ACTIVE |

**Counts:** 14 ACTIVE rows (8 ANCHOR, 6 EXECUTION). 0 RETIRED rows.

## Run Notes

- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source documents scanned (AUTO):** Datasheet.md, Specification.md, Guidance.md, Procedure.md
- **ANCHOR_DOC (AUTO):** Datasheet.md (contains `datasheet` keyword; highest-confidence anchor signal)
- **EXECUTION_DOC_ORDER (AUTO):** Procedure.md (prerequisite list), Specification.md (scope/requirements), Guidance.md (considerations), Datasheet.md (construction section)
- **Decomposition path:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — used to resolve anchor IDs (SOW-0030, OBJ-001/004/005/006/008/009/010) and sibling deliverable IDs (DEL-029-01 through DEL-029-06). NOTE: BRIEF specified `GATE-07_Final_Published_2026-05-24` under a non-existent top-level path; actual snapshot located at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` and confirmed via `_REFERENCES.md` pointer.
- **_REFERENCES.md:** Read and used to confirm decomposition snapshot path and Gate 7 register locations.
- **Tree x DAG integrity:** 1 IMPLEMENTS_NODE row (DEP-029-02-001, SOW-0030). Parent anchor check: PASS.
- **No warnings:** Schema valid; all ACTIVE rows cite EvidenceFile and SourceRef.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full extraction run (dependency-extract, MODE=UPDATE, STRICTNESS=CONSERVATIVE). 14 ACTIVE rows written (8 ANCHOR + 6 EXECUTION). Schema: VALID. Decomposition: GATE-07_Final_Published_2026-05-24. No warnings.

## Lifecycle Summary

| Dimension | Count |
|---|---|
| ACTIVE | 14 |
| RETIRED | 0 |
| ANCHOR rows (ACTIVE) | 8 |
| EXECUTION rows (ACTIVE) | 6 |
| UPSTREAM (ACTIVE) | 11 |
| DOWNSTREAM (ACTIVE) | 3 |
| SatisfactionStatus = SATISFIED | 5 |
| SatisfactionStatus = TBD | 9 |
