# Specification: DEL-005-01_scope-of-work - Scope of Work

## Scope

This specification governs the contents of the `PKG-005 Site Grading` Scope of Work deliverable for WBS 03. The deliverable must state the package scope, package identity, source basis, boundaries, responsibility assignment, and whole-facility integration narrative for the Civil Site Grading package.

Included scope:

- Package scope of work for `PKG-005 - Site Grading`.
- Tagged equipment and package identity list where source-supported; for this package, available identity data includes package name, workbook ID, CoA tracking number, WBS, discipline, and interface facts.
- Package function and integration narrative.
- Responsibility assignment record.
- Source-supported interface facts for Drain / Containment and Grading / Site Drainage / Spill Containment.

Excluded or deferred scope:

- Detailed construction workface planning, inspection, turnover, and tie-in sequencing are assigned to sibling deliverable `DEL-005-03_construction-work-package`.
- Technical handoff data, interface requirements matrix, and detailed design criteria are assigned to sibling deliverable `DEL-005-02_package-datasheet`.
- Detailed Civil production drawings/calculations are assigned to sibling deliverable `DEL-005-04_epc-civil-discipline-production-package`.
- Package-specific exclusions are `TBD`; the Gate 7 package register states no package-specific exclusions in current source materials.

Sources: Gate 7 `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and DBM 03-25 `SEC-11`.

## Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| SOW-REQ-001 | The Scope of Work shall identify the deliverable as `DEL-005-01_scope-of-work`, parent package `PKG-005`, package name `Site Grading`, WBS `03`, discipline `Civil`, and responsible party `EPC Integrator`. | `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv`; Gate 7 `PACKAGE_REGISTER.csv` | Confirm all identity fields appear in `Datasheet.md` and the issued scope document. |
| SOW-REQ-002 | The Scope of Work shall carry `SOW-0005` as the governed scope item and preserve the package as a distinct flat project package for WBS 03. | Gate 7 `SCOPE_LEDGER.csv`, `SOW-0005` | Confirm `SOW-0005` and WBS 03 are present. |
| SOW-REQ-003 | The Scope of Work shall describe the package as a workbook-defined Civil Site Grading package with recorded physical interfaces. | Gate 7 `PACKAGE_REGISTER.csv`, `PKG-005` | Confirm package narrative matches the register without adding unsupported design detail. |
| SOW-REQ-004 | The Scope of Work shall include the interface types `Drain / Containment` and `Grading / Site Drainage / Spill Containment`. | Gate 7 `INTERFACE_REGISTER.csv`, `PKG-005`; Gate 7 `ARTIFACT_REGISTER.csv`, rows for interface facts | Confirm both interface types appear consistently in Datasheet, Specification, Guidance, and Procedure. |
| SOW-REQ-005 | The Scope of Work shall identify the responsibility model as source-dependent EPC Integrator or discipline subcontractor responsibility, and shall not infer a separate vendor-package ownership model. | Gate 7 `PACKAGE_REGISTER.csv`, `PKG-005`; Gate 7 `ARTIFACT_REGISTER.csv`, responsibility assignment record | Confirm no vendor ownership model is asserted for this Civil package. |
| SOW-REQ-006 | The Scope of Work shall state that civil design relevant to this package covers grading, drainage, roads, surface-water management, retention pond, foundations/supports, building foundations, fencing, and security where applicable to the package boundary. | DBM 03-25 `SEC-11 - Site and Civil Conditions` | Confirm coverage is framed as package-relevant context, not a complete design package. |
| SOW-REQ-007 | The Scope of Work shall state that surface-water management must prevent uncontrolled offsite discharge, protect process areas, and support construction and operations access. | DBM 03-25 `SEC-11 - Surface Water and Drainage` | Confirm drainage and containment narrative includes these outcomes. |
| SOW-REQ-008 | The Scope of Work shall preserve the current hydrology uncertainty: drainage, retention pond sizing, and surface-water management use current precipitation/storm basis until hydrology is updated. | DBM 03-25 `SEC-02 - rainfall basis`; `SEC-11 - Surface Water and Drainage` | Confirm final hydrology is not presented as closed. |
| SOW-REQ-009 | The Scope of Work shall state that process-contaminated drainage is routed to the appropriate drain or containment system rather than surface-water discharge. | DBM 03-25 `SEC-11 - Surface Water and Drainage` | Confirm contaminated drainage is not assigned to uncontrolled or normal surface-water discharge. |
| SOW-REQ-010 | The Scope of Work shall carry geotechnical closure as pending final geotechnical report acceptance. | DBM 03-25 `SEC-02 - Geotechnical and Seismic Basis`; `SEC-11 - Site and Civil Conditions` | Confirm final geotechnical values are not treated as closed construction criteria. |
| SOW-REQ-011 | The Scope of Work shall identify applicable objective context as OBJ-002, OBJ-007, OBJ-008, and OBJ-009. | `_CONTEXT.md`; Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`; Gate 7 `PROJECT_DECOMP.md` objective table | Confirm objectives are treated as context and not expanded into unsupported package requirements. |

## Standards

| Standard / authority | Applicability | Status / location |
|---|---|---|
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package, deliverable, artifacts, interfaces, objectives, and scope item | Accessible locally at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` |
| DBM 03-25 Compressor Station and Liquids Hub | Source basis for civil/site/drainage/geotechnical/regulatory context | Accessible locally at `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| NBCC | Civil/structural governing content and rainfall proxy reference | Mentioned in DBM 03-25 `SEC-02` and `SEC-15`; clause-level standard text not available in deliverable folder |
| Final geotechnical report | Required for foundation design closure | Not available; `TBD` |
| Civil drawings and equipment layout | Required for plot plan and spacing verification before final issue | Not available; `TBD` |
| Applicable BC water legislation and regulator requirements | Applies to stormwater management and related water activities | Mentioned in DBM 03-25 `SEC-15 - BC Water Regulations`; detailed regulatory review remains required |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity and source basis | Register cross-check | Matches Gate 7 `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, and `_CONTEXT.md`. |
| Interface scope | Register cross-check | Both Gate 7 interface rows for `PKG-005` are included and no undeclared interface type is presented as authoritative. |
| Civil/drainage context | Source slice review | DBM 03-25 `SEC-11` and `SEC-02` statements are represented without closing pending hydrology/geotechnical items. |
| Responsibility assignment | Register cross-check | Responsibility remains source-dependent and no separate vendor-package model is inferred. |
| Cross-document consistency | Four-document review | Terminology, objectives, WBS, package ID, interface names, and `TBD` items align across all four documents. |

## Documentation

The completed Scope of Work package should include or reference:

- Package scope of work.
- Tagged equipment and package identity list. For this deliverable, tagged equipment details are `TBD` unless supported by source; package identity fields are available from Gate 7 registers.
- Package function and whole-facility integration narrative.
- Responsibility assignment record.
- Interface statement for Drain / Containment and Grading / Site Drainage / Spill Containment.
- Source basis and open-item list for hydrology, geotechnical report, civil drawings/equipment layout, package-specific exclusions, and detailed regulatory review.
