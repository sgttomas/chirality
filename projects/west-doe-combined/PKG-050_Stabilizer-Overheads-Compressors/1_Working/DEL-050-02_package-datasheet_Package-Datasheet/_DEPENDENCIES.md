# Dependencies: DEL-050-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** DECLARED + EXTRACTED
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` produced by `TASK + dependency-extract` run 2026-05-25. Schema version: v3.1.

**Total rows:** 6  
**ACTIVE rows:** 6  
**RETIRED rows:** 0

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-050-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | PACKAGE | PKG-050 | Stabilizer Overheads Compressors | HIGH | ACTIVE |
| DEP-050-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | OBJ-001 (Project Objectives — primary mandate; full set OBJ-001/003–010) | HIGH | ACTIVE |
| DEP-050-02-003 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-050-01_scope-of-work | Scope of Work | HIGH | ACTIVE |
| DEP-050-02-004 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-050-03_construction-work-package | Construction Work Package | HIGH | ACTIVE |
| DEP-050-02-005 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-050-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | HIGH | ACTIVE |
| DEP-050-02-006 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | INTERFACE | DELIVERABLE | DEL-050-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; source documents found: `Datasheet.md` (ANCHOR_DOC), `Guidance.md`, `Procedure.md`, `Specification.md` (EXECUTION_DOCS).
- **ANCHOR_DOC:** `Datasheet.md` (contains Identification table with ParentPackageID and WBS fields — highest-confidence anchor signal).
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — decomposition present; used for anchor validation and label resolution.
- **Registers consulted:** `PACKAGE_REGISTER.csv` (row PKG-050), `DELIVERABLE_REGISTER.csv` (row DEL-050-02), `OBJECTIVE_DELIVERABLE_MAP.csv`, `INTERFACE_REGISTER.csv`.
- **`_REFERENCES.md`:** Read; used to resolve decomposition path. No document-pointer dependency rows emitted (none explicitly stated as required inputs in source text — only referenced as documentation basis).
- **Interface rows (IFC-*):** 13 interface IDs appear in Datasheet.md Battery-Limit table. These are NOT emitted as dependency rows because they represent interface inventory facts carried in this datasheet by design (`_CONTEXT.md` directive), not information flows FROM other deliverables. They represent outbound interface declarations, not upstream inputs.
- **Parent anchor check:** 1 ACTIVE ANCHOR IMPLEMENTS_NODE row found (DEP-050-02-001). PASS.
- **Floating node warning:** None — parent anchor present.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 6 |
| RETIRED | 0 |
| **Total** | **6** |

| SatisfactionStatus | Count |
|---|---|
| SATISFIED | 2 (anchor rows — structural, not workflow-gated) |
| TBD | 4 (execution rows — open until downstream deliverables reach required maturity) |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition present. 6 rows extracted (2 ANCHOR, 4 EXECUTION). All ACTIVE. Schema: v3.1.
