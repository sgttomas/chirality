# Datasheet — DEL-104-03 Construction Work Package

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-104-03_construction-work-package` |
| Name | Construction Work Package |
| ParentPackageID | `PKG-104` |
| ParentWorkbookID | 104 (workbook tracking row 105) |
| Package Name | Structural steel - outside of modules |
| WBS | 01 (Workbook row 105 — `SCOPE_LEDGER.csv`) |
| CoA Tracking Number | 26020-01-36-004 (`PACKAGE_REGISTER.csv`) |
| Discipline | Structural |
| Type | EPC Construction Work Package |
| Responsible Party | EPC Integrator (`_CONTEXT.md`); field construction execution assigned to Tourmaline Oil Corporation per `DBM-Deepcut/4-25_Deepcut_DBM.md` Construction Responsibility |
| Scope Item Covered | `SOW-0260` |
| Objectives Supported | `OBJ-001`, `OBJ-008`, `OBJ-010` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function | Structural steel - outside of modules (field-erected structural steel scope for the PKG-104 boundary) | `PACKAGE_REGISTER.csv` PKG-104 row; `SCOPE_LEDGER.csv` SOW-0260 |
| Construction execution model | Field construction by Tourmaline Oil Corporation, including installation of miscellaneous structural supports and mechanical hookup of modules, equipment, and interconnecting piping | `4-25_Deepcut_DBM.md` Construction Responsibility |
| Foundation default basis | Driven steel piles for buildings, equipment, towers, tanks, modules, pipe racks, and similar structures unless detailed engineering establishes otherwise | `4-25_Deepcut_DBM.md` Piles and Foundations |
| Structural steel material | CSA G40.20/G40.21 350W for W-flange and HSS; 300W for channels, plates, and angles | `4-25_Deepcut_DBM.md` Governing Civil and Structural Basis |
| Steel design code | CAN/CSA-S16 Design of Steel Structures | `4-25_Deepcut_DBM.md` Governing Civil and Structural Basis |
| Concrete design code | CAN/CSA A23.3 Design of Concrete Structures (where foundations require concrete) | `4-25_Deepcut_DBM.md` Governing Civil and Structural Basis |
| Concrete materials/construction/testing | CSA A23.1/A23.2 | `4-25_Deepcut_DBM.md` Governing Civil and Structural Basis |
| Building code | National Building Code of Canada | `4-25_Deepcut_DBM.md` Governing Civil and Structural Basis |
| Foundation engineering reference | Canadian Foundation Engineering Manual | `4-25_Deepcut_DBM.md` Governing Civil and Structural Basis |
| Declared interfaces | Grading / Site Drainage / Spill Containment (`IFC-CCDE4B56CA`); Structural / Foundations / Supports (`IFC-ECDD4D3A15`) | `INTERFACE_REGISTER.csv` PKG-104 rows |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Construction phasing | One phase, single train, nominal 300 MMSCFD facility | `4-25_Deepcut_DBM.md` Facility Identity |
| Tie-in execution | Joint planning required for tie-ins to existing or related facilities; tie-in timing to be established as project progresses | `4-25_Deepcut_DBM.md` Construction Responsibility |
| Interconnecting piping to ISBL/OSBL tie-ins | External interface responsibility; responsibility to be confirmed per tie-in | `4-25_Deepcut_DBM.md` Construction Responsibility |
| Geotechnical inputs | Bearing capacity, LPILE load-deflection curves, dynamic design criteria — TBD pending geotechnical report | `4-25_Deepcut_DBM.md` Geotechnical and Topographical Assumptions |
| Site grading at pipe racks | High equal-elevation ridges along main pipe racks; pad slopes from pipe racks at 1.5% per side (1.0% allowance where top-of-pile-cap dictates) | `4-25_Deepcut_DBM.md` Site Grading and Surface Water Management |
| Maintenance/erection access | Layout shall preserve access routes, maintainability envelopes, modular construction requirements, emergency response access, hazardous-area separation, and future plot provisions | `4-25_Deepcut_DBM.md` General Layout Basis |

## Construction

| Item | Value | Source |
|---|---|---|
| Anticipated artifacts | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist | `_CONTEXT.md`; `ARTIFACT_REGISTER.csv` rows `ART-9478B627E2`, `ART-A0BC38D152`, `ART-8131641C3B` |
| Erection method (default) | Field installation of structural steel members, supports, and tie-ins by Tourmaline field construction; modules set on foundations and mechanically hooked up | `4-25_Deepcut_DBM.md` Construction Responsibility |
| Quantity take-off, structural member schedule, weld procedures, NDE plan, bolt-up torque values | TBD — not present in accessible source slices for PKG-104; require detailed structural deliverables (DEL-104-04 production package) and geotechnical/IFC drawings | `_REFERENCES.md` Missing/Deferred References |
| Inspection hold points | TBD — not specified in DBM at package scope; ASSUMPTION: inspection plan follows EPC Integrator's standard ITP keyed to CAN/CSA-S16 fabrication/erection requirements | ASSUMPTION (no source slice) |
| Turnover acceptance basis | TBD — handoff readiness evidence required per `OBJ-010` (controlled open-item closure evidence for package procurement and downstream facility handoff) | `OBJECTIVE_REGISTER.csv` OBJ-010 |

## References

- `_REFERENCES.md` (deliverable reference index)
- `_CONTEXT.md` (deliverable identity and scope)
- `_DEPENDENCIES.md` (no upstream/downstream declared)
- Decomposition snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `PACKAGE_REGISTER.csv` (PKG-104 row)
  - `DELIVERABLE_REGISTER.csv` (DEL-104-03 row)
  - `ARTIFACT_REGISTER.csv` (PKG-104 artifacts)
  - `INTERFACE_REGISTER.csv` (PKG-104 interfaces)
  - `SCOPE_LEDGER.csv` (SOW-0260)
  - `OBJECTIVE_REGISTER.csv` (OBJ-001, OBJ-008, OBJ-010)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` sections: Construction Responsibility; General Layout Basis; Civil Scope; Governing Civil and Structural Basis; Geotechnical and Topographical Assumptions; Site Grading and Surface Water Management; Piles and Foundations; Buildings and Miscellaneous Facilities
- Inaccessible: `26020-Package_Requirements.docx` and `26020-Packages_Interfaces_4_export.xlsx` were not opened as source slices during this run — items dependent on those carry `TBD` (location TBD)
