# Datasheet: DEL-101-01 Scope of Work

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-101-01_scope-of-work |
| Deliverable name | Scope of Work |
| Parent package | PKG-101 |
| Package name | Precast concrete foundations |
| Workbook ID / row | 101 / row 102 |
| WBS | 01 |
| CoA tracking number | 26020-01-36-001 |
| Discipline | Structural |
| Deliverable type | EPC Scope of Work |
| Responsible party | EPC Integrator |
| Source basis | Workbook Packages row 102; Gate 7 PROJECT_DECOMP snapshot |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function | Precast concrete foundations as a distinct Structural package under WBS 01 | Gate 7 `SCOPE_LEDGER.csv`, SOW-0257; `PACKAGE_REGISTER.csv`, PKG-101 |
| Package responsibility model | EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred from current sources | Gate 7 `PACKAGE_REGISTER.csv`, PKG-101 |
| Mandatory anchor deliverable | Package Scope of Work identifying package scope, source basis, boundaries, tagged equipment, and whole-facility integration narrative | Gate 7 `DELIVERABLE_REGISTER.csv`, DEL-101-01 |
| Source-supported interface types | Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | Gate 7 `INTERFACE_REGISTER.csv`, PKG-101 (IFC-26343B703C, IFC-BED3DE4194); `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages row 102 |
| Tagged equipment | TBD; the accessible workbook row and Gate 7 package row do not enumerate package-specific equipment tags for this structural package. The DBM identifies precast concrete bearing foundations as the supported foundation basis for transformers and precast concrete blocks (on driven steel piles) for compressors, but does not assign equipment tags to PKG-101. | Workbook Packages row 102; Gate 7 `PACKAGE_REGISTER.csv`, PKG-101; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Piles and Foundations |
| Package-specific exclusions | TBD; no package-specific exclusions are stated in accessible source materials | Gate 7 `PACKAGE_REGISTER.csv`, PKG-101 |
| Supports objectives | OBJ-001 (04-25 Deepcut facility scope); OBJ-008 (civil/structural/site/foundation scope) | Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`, DEL-101-01 |

## Conditions

| Condition | Current basis | Source |
|---|---|---|
| Structural / civil scope applicability | The civil/structural basis applies to facility pad, drainage system, retention pond, roads, foundations, process and utility modules, permanent buildings, and ancillary buildings. Precast concrete foundations sit within this basis as a specific support concept. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Civil Scope |
| Default foundation support basis | Driven steel piles are the default support basis for buildings, equipment, towers, tanks, modules, pipe racks, and similar structures unless a more specific foundation basis is listed or detailed engineering confirms otherwise. Precast concrete elements are used in combination with this default. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Piles and Foundations |
| Precast concrete application — transformers | Generally supported on precast concrete bearing foundations. No open requirement identified in the DBM. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Piles and Foundations |
| Precast concrete application — compressors | Precast concrete block supported on driven steel piles, subject to dynamic analysis. Dynamic analysis results are TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Piles and Foundations |
| Compressor skid/foundation interaction | Foundation/skid design shall consider containment and management of oil leaks from on-skid equipment. Detailed arrangement is TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Piles and Foundations |
| Alternate compressor support concept | Propak will verify whether the steel skid can be welded directly to piles instead of using concrete; this is considered unlikely for this compressor size. Verification is TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Piles and Foundations |
| Geotechnical inputs | Bearing capacity, LPILE load-deflection curves, dynamic design criteria, and related parameters are TBD pending completion and review of the geotechnical assessment report. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Geotechnical and Topographical Assumptions; External Dependencies |
| Topographical inputs | Existing grade surface file is required for plant-site grading and drainage design; final format and contents are TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Geotechnical and Topographical Assumptions |
| Governing concrete design code | CAN/CSA A23.3 Design of Concrete Structures (latest edition) governs concrete design; CSA A23.1/A23.2 governs concrete materials, construction, and testing. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Governing Civil and Structural Basis |
| Governing building code | National Building Code of Canada governs building, structural, and snow/wind/seismic loading basis where applicable. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Governing Civil and Structural Basis |
| Surface-water containment context | Site grading and drainage shall prevent off-site surface overflow from entering the expansion facility and shall direct and contain on-site overflow into a retention pond. Foundation grading interfaces with this containment intent. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Site Grading and Surface Water Management |

## Construction

| Construction item | Current basis | Source |
|---|---|---|
| Construction responsibility | Field construction, including grading, piling, and foundation work, and setting of modules, pipe racks, and equipment on foundations, is assigned to Tourmaline field construction scope. EPC Integrator scope is definition of the Scope of Work, not field execution. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Construction Scope Summary (rows: grading/piling/foundation work; setting modules/pipe racks/equipment on foundations) |
| Scope-of-work outputs | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record | Gate 7 `DELIVERABLE_REGISTER.csv`, DEL-101-01 |
| Detailed quantities | TBD; accessible sources do not provide precast element counts, dimensions, reinforcement schedules, or pour quantities for PKG-101 | Workbook Packages row 102; DBM SEC-11 source slices |
| Plot-plan tie-in | TBD; final foundation layout, equipment coordinates, and grading interface depend on the plot plan and detailed engineering | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 External Dependencies |
| Compressor dynamic analysis dependency | TBD; compressor foundation design depends on dynamic analysis results that are not currently available | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 External Dependencies, Assumptions/TBDs |

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/SCOPE_LEDGER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_DELIVERABLE_MAP.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages row 102
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 (Civil Scope, Governing Civil and Structural Basis, Geotechnical and Topographical Assumptions, Site Grading and Surface Water Management, Piles and Foundations, External Dependencies, Assumptions/TBDs)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Construction Scope Summary
