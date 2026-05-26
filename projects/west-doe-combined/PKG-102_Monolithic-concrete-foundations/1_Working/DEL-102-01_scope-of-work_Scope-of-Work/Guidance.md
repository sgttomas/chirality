# Guidance — DEL-102-01 Scope of Work (PKG-102 Monolithic concrete foundations)

> Directional guidance for drafting and reviewing the PKG-102 monolithic-concrete-foundations Scope of Work as a Gate 5 EPC anchor deliverable.

## Purpose

This Scope of Work is the EPC Integrator's authoritative statement of what PKG-102 "Monolithic concrete foundations" covers, what it does not cover, who is responsible, and how it integrates into the larger West Doe Deepcut facility. It is the mandatory Gate 5 EPC anchor deliverable for PKG-102 (Source: `_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv` DEL-102-01 row).

It exists to:

- Establish a single, source-traceable definition of the PKG-102 sub-scope so downstream EPC and discipline production deliverables (DEL-102-02 package datasheet, DEL-102-03 construction work package, DEL-102-04 discipline production package) can build on a stable scope statement. (Source: `DELIVERABLE_REGISTER.csv` PKG-102 rows.)
- Anchor the package within the project structural and civil basis (CAN/CSA A23.3; CSA A23.1/A23.2; National Building Code of Canada; Canadian Foundation Engineering Manual) without restating discipline-level design content. (Source: DBM-Deepcut SEC-11 "Governing Civil and Structural Basis".)
- Carry forward the workbook-row-103 origin (Source: `_CONTEXT.md` Source Reference; `SCOPE_LEDGER.csv` SOW-0258).

## Principles

- **Source over convention.** Tagged equipment, applicable standards, and interface types must come from the workbook row 103 and DBM-Deepcut SEC-11, not from generic foundation-engineering convention.
- **Conservative default of TBD.** When workbook row 103 is not extracted or when the source is silent, list the item as TBD with a pointer to the source slice required to resolve it. Do not invent quantities, dimensions, or pour schedules.
- **Project default is pile, not monolithic.** The Deepcut DBM identifies driven steel piles as the default support basis for buildings, equipment, towers, tanks, modules, and pipe racks. Monolithic concrete foundations apply only where the workbook or detailed engineering establishes them as the basis. PKG-102 carries the workbook-defined Structural package for monolithic concrete foundations; the population of structures supported by this package is governed by the workbook row, not by generalization. (Source: DBM-Deepcut SEC-11 "Piles and Foundations".)
- **Integration narrative is mandatory.** PKG-102 has two declared interface types (Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports). The integration narrative must address both. (Source: `INTERFACE_REGISTER.csv` IFC-1EDEDC0453, IFC-8283744B5B.)
- **Responsibility is EPC Integrator.** This package is not a vendor-engineered scope. Engineering and design responsibility resides with the EPC Integrator (or assigned discipline subcontractor under EPC ownership). (Source: `_CONTEXT.md` ResponsibleParty; `PACKAGE_REGISTER.csv` PKG-102 row.)

## Considerations

- **Workbook-row-103 dependency.** The complete and authoritative list of equipment, structures, and quantities supported by PKG-102 monolithic concrete foundations lives in the binary workbook (`26020-Packages_Interfaces_4_export.xlsx`) row 103 and the `26020-Package_Requirements.docx` companion. Until those source slices are extracted into deliverable-local form, the tagged-equipment list and quantitative basis in this SoW remain TBD. Do not substitute decomposition prose for the workbook row.
- **External-input dependence.** The geotechnical report, topographical survey, and plot plan are external inputs that drive concrete-foundation sizing and bearing assumptions. Until they are available, the SoW should explicitly note the open issues without anchoring design values. (Source: DBM-Deepcut SEC-11 "External Dependencies"; "Assumptions, TBDs, and Design Development Requirements".)
- **Boundary against PKG-101.** PKG-101 is the workbook-defined "Precast concrete foundations" companion Structural package (workbook row 102). The SoW must not absorb scope that belongs to PKG-101; references to precast-supported equipment (transformers; compressor blocks on piles) belong to PKG-101 or other packages where applicable. (Source: `PACKAGE_REGISTER.csv` PKG-101 row; `INTERFACE_REGISTER.csv` PKG-101 rows; DBM-Deepcut SEC-11 "Piles and Foundations".)
- **Boundary against Civil packages.** Pad grading, roadway design, ditches, culverts, retention pond, and earthworks are carried in distinct Civil packages (e.g., PKG-001..PKG-007 in the SCOPE_LEDGER). The integration narrative should describe the interface to these works but not re-scope them. (Source: `SCOPE_LEDGER.csv`; DBM-Deepcut SEC-11.)
- **Objective association is heuristic.** OBJ-001 and OBJ-008 are carried via the package-grouping heuristic at the deliverable level. Treat them as directional, not as binding requirements at the SoW-row level, unless human ruling confirms otherwise. (Source: `OBJECTIVE_REGISTER.csv`; brief `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`.)

## Trade-offs

- **Specificity vs. fidelity.** A more specific SoW (listing equipment tags, pour counts, concrete volumes) requires workbook-row-103 and detailed-engineering inputs. Until those are available, the trade-off must favor fidelity (TBD with source pointers) over apparent completeness.
- **Anchor-deliverable breadth vs. discipline-deliverable depth.** The SoW is the EPC anchor; it should remain breadth-oriented. Pour sequencing, mix designs, and rebar schedules belong in DEL-102-04 (Discipline Production Package) and DEL-102-03 (Construction Work Package), not in this SoW.
- **Monolithic vs. precast boundary.** Where source materials describe a "precast concrete bearing foundation" (e.g., transformers) or a "precast concrete block" (e.g., compressors on driven piles), do not migrate that scope into PKG-102 even if a monolithic interpretation might appear technically reasonable. (Source: DBM-Deepcut SEC-11 "Piles and Foundations" table.)

## Examples

- *Example structural basis statement (source-grounded):* "Reinforced concrete elements within PKG-102 shall be designed in accordance with CAN/CSA A23.3 and constructed and tested in accordance with CSA A23.1/A23.2; loading shall comply with the National Building Code of Canada; foundation engineering shall reference the Canadian Foundation Engineering Manual." (Source: DBM-Deepcut SEC-11 "Governing Civil and Structural Basis".)
- *Example integration-narrative pointer:* "Top-of-foundation elevations within PKG-102 shall be coordinated with the facility-pad grading basis (1.5% nominal slope from pipe-rack ridges, reducible to 1.0% to maintain reasonable top-of-pile-cap elevations) and with on-site surface-control features used for spill containment." (Source: DBM-Deepcut SEC-11 "Site Grading and Surface Water Management".)
- *Example open-issue statement:* "Bearing capacity, LPILE load-deflection curves, dynamic design criteria, and compressor foundation dynamic analysis remain TBD pending the site geotechnical report." (Source: DBM-Deepcut SEC-11 "Assumptions, TBDs, and Design Development Requirements".)

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-102-01-001 | Package name "Monolithic concrete foundations" implies cast-in-place monolithic scope, but DBM-Deepcut SEC-11 "Piles and Foundations" identifies only precast concrete applications (transformers, compressor blocks) and otherwise defaults to driven steel piles; no monolithic-concrete instances are explicitly enumerated in SEC-11. | `PACKAGE_REGISTER.csv` PKG-102 (Workbook row 103) | DBM-Deepcut `4-25_Deepcut_DBM.md` SEC-11 "Piles and Foundations" | Datasheet "Attributes" (monolithic-concrete application instances); Specification R-102-01-003, R-102-01-006; Guidance "Principles" (PKG-101 boundary) | Workbook row 103 (PROPOSAL): the workbook is the authoritative package-scope source and must enumerate the structures supported by PKG-102 monolithic foundations; the DBM is a basis-of-design narrative and does not override the workbook scope. Workbook extraction required to close the conflict. | TBD |
| CT-102-01-002 | Objective association (OBJ-001; OBJ-008) is carried at the package level via PACKAGE_HEURISTIC; whether each objective applies to every PKG-102 deliverable (including DEL-102-01 SoW) at the deliverable-row level has not been ruled. | `DELIVERABLE_REGISTER.csv` DEL-102-01 row (OBJ-001; OBJ-008) | `OBJECTIVE_DELIVERABLE_MAP.csv` (mapping granularity); brief `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC` | Datasheet "Identification"; Specification R-102-01-011 | Treat as directional context only (PROPOSAL); record as ASSUMPTION until human confirms deliverable-row association. | TBD |
| CT-102-01-003 | Tagged equipment list (R-102-01-003) cannot be populated without workbook row 103 extraction; binary workbook is not parsed in this run, so the SoW's anticipated artifact "tagged equipment and package identity list" remains TBD. | `_CONTEXT.md` Anticipated Artifacts | `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 103 (binary; not extracted) | Datasheet "Attributes"; Specification R-102-01-003; Procedure Step 4 | Workbook row 103 extraction (PROPOSAL): run a workbook extraction task or have the EPC Integrator provide the tagged-equipment slice in deliverable-local form. | TBD |
