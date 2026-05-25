# Datasheet: DEL-001-01 Scope of Work

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-001-01_scope-of-work |
| Deliverable name | Scope of Work |
| Parent package | PKG-001 |
| Package name | Earthworks for foundations |
| Workbook ID / row | 1 / row 2 |
| WBS | 01 |
| CoA tracking number | 26020-01-42-001 |
| Discipline | Civil |
| Deliverable type | EPC Scope of Work |
| Responsible party | EPC Integrator |
| Source basis | Workbook Packages row 2; Gate 7 PROJECT_DECOMP snapshot |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function | Earthworks for foundations as a distinct Civil package under WBS 01 | Gate 7 `SCOPE_LEDGER.csv`, SOW-0001 |
| Package responsibility model | EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred | Gate 7 `PACKAGE_REGISTER.csv`, PKG-001 |
| Mandatory anchor deliverable | Package Scope of Work identifying package scope, source basis, boundaries, and whole-facility integration narrative | Gate 7 `DELIVERABLE_REGISTER.csv`, DEL-001-01 |
| Source-supported interface types | Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | Gate 7 `INTERFACE_REGISTER.csv`, PKG-001; `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages row 2 |
| Tagged equipment | TBD; none identified in the accessible workbook row or Gate 7 package row for this civil package | Workbook Packages row 2; Gate 7 `PACKAGE_REGISTER.csv`, PKG-001 |
| Package-specific exclusions | TBD; no package-specific exclusions stated in accessible source materials | Gate 7 `PACKAGE_REGISTER.csv`, PKG-001 |

## Conditions

| Condition | Current basis | Source |
|---|---|---|
| Civil scope applicability | Civil, structural, site-grading, drainage, road, foundation, building, and miscellaneous-facility basis applies to facility pad, drainage system, retention pond, roads, foundations, process and utility modules, permanent buildings, and ancillary buildings | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Civil Scope |
| Geotechnical inputs | Bearing capacity, lateral pile data, dynamic design criteria, pavement parameters, and related parameters are TBD pending geotechnical assessment | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Geotechnical and Topographical Assumptions |
| Topographical inputs | Existing grade surface file is required for plant-site grading and drainage design; final format and contents are TBD | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Geotechnical and Topographical Assumptions |
| Drainage and surface water | Site grading and drainage shall prevent off-site surface overflow entering the expansion facility and direct/contain on-site overflow into a retention pond | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Site Grading and Surface Water Management |
| Foundation support basis | Driven steel piles are the default support basis for buildings, equipment, towers, tanks, modules, pipe racks, and similar structures unless detailed engineering confirms otherwise | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Piles and Foundations |

## Construction

| Construction item | Current basis | Source |
|---|---|---|
| Construction responsibility | Field construction, including grading, piling, and foundation work, is assigned to Tourmaline field construction scope | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility |
| Scope-of-work output | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record | Gate 7 `DELIVERABLE_REGISTER.csv`, DEL-001-01 |
| Detailed quantities | TBD; accessible sources do not provide earthwork quantities for PKG-001 | Workbook Packages row 2; DBM SEC-11 source slices |
| Plot-plan tie-in | TBD; final civil layout and retention pond location depend on plot plan and detailed engineering | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 External Dependencies |

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/SCOPE_LEDGER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages row 2
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 and Construction Responsibility
