# Specification — DEL-102-01 Scope of Work (PKG-102 Monolithic concrete foundations)

> Normative scope-of-work specification for the EPC Integrator delivery of PKG-102 "Monolithic concrete foundations" within the West Doe Deepcut expansion (WBS 01).

## Scope

### In scope

- EPC Integrator definition and management of the monolithic (cast-in-place) concrete foundations package for PKG-102 within WBS 01 of the West Doe Deepcut expansion. (Source: `SCOPE_LEDGER.csv` SOW-0258; `PACKAGE_REGISTER.csv` PKG-102.)
- Statement of package function, identity, and boundaries for the structural foundations sub-scope listed under Workbook Packages row 103. (Source: `_CONTEXT.md`; `PACKAGE_REGISTER.csv` PKG-102.)
- Identification of tagged equipment and structures supported by monolithic concrete foundations in this package (list TBD pending workbook row 103 extraction). (Source: `_CONTEXT.md` Anticipated Artifacts; ASSUMPTION on completeness.)
- Whole-facility integration narrative covering interfaces to:
  - Grading / Site Drainage / Spill Containment (IFC-1EDEDC0453);
  - Structural / Foundations / Supports (IFC-8283744B5B).
  (Source: `INTERFACE_REGISTER.csv` PKG-102 rows.)
- Responsibility assignment for engineering, procurement, and construction coordination of the monolithic-foundation sub-scope under EPC Integrator ownership. (Source: `DELIVERABLE_REGISTER.csv` DEL-102-01 row.)

### Out of scope

- Vendor-package equipment engineering and design (carried in the applicable vendor-engineered-equipment packages). (Source: GATE-07 snapshot vendor-package deliverable rows; project convention per `DELIVERABLE_REGISTER.csv`.)
- Detailed civil pavement, roadway, and ditch/culvert design (separate Civil packages). (Source: DBM-Deepcut SEC-11 "Roads"; `PACKAGE_REGISTER.csv` Civil packages.)
- Driven-steel-pile foundation design as the project default for buildings, modules, pipe racks, tanks, and similar structures except where a monolithic concrete foundation is the established basis. (Source: DBM-Deepcut SEC-11 "Piles and Foundations".)
- Geotechnical assessment, topographical survey, and plot plan (external inputs). (Source: DBM-Deepcut SEC-11 "External Dependencies".)
- Discipline production engineering output is carried in DEL-102-04 (EPC / Structural Discipline Production Package). (Source: `DELIVERABLE_REGISTER.csv` PKG-102 rows.)

## Requirements

| ReqID | Requirement | Source |
|---|---|---|
| R-102-01-001 | The Scope of Work shall identify PKG-102 by `PackageID`, `WorkbookID` (102), `WBS` (01), `Discipline` (Structural), `PackageName` ("Monolithic concrete foundations"), and `ResponsibleParty` (EPC Integrator). | `PACKAGE_REGISTER.csv` PKG-102; `_CONTEXT.md` |
| R-102-01-002 | The Scope of Work shall reference and remain consistent with the Workbook Packages row 103 source basis. | `_CONTEXT.md` Source Reference; `SCOPE_LEDGER.csv` SOW-0258 |
| R-102-01-003 | The Scope of Work shall list the tagged equipment and structures within PKG-102 that the EPC Integrator will support via monolithic concrete foundations. List is TBD pending workbook row 103 extraction. | `_CONTEXT.md` Anticipated Artifacts; ASSUMPTION |
| R-102-01-004 | The Scope of Work shall state the package function: provide cast-in-place reinforced concrete foundations within PKG-102 scope to support tagged structures/equipment in accordance with the project structural basis. | DBM-Deepcut SEC-11 "Civil Scope"; `PACKAGE_REGISTER.csv` PKG-102 description |
| R-102-01-005 | The Scope of Work shall cite the governing structural and material basis: CAN/CSA A23.3 (design), CSA A23.1/A23.2 (materials/construction/testing), National Building Code of Canada (loads), and the Canadian Foundation Engineering Manual (foundation engineering reference). | DBM-Deepcut SEC-11 "Governing Civil and Structural Basis" |
| R-102-01-006 | The Scope of Work shall define package boundaries against the default driven-steel-pile foundation basis used elsewhere on the facility (i.e., identify which structures in PKG-102 are monolithic-concrete-supported vs. pile-supported). Specific assignments are TBD pending workbook row 103 and detailed engineering. | DBM-Deepcut SEC-11 "Piles and Foundations"; ASSUMPTION |
| R-102-01-007 | The Scope of Work shall describe the whole-facility integration narrative covering the Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports interfaces declared for PKG-102. | `INTERFACE_REGISTER.csv` IFC-1EDEDC0453, IFC-8283744B5B |
| R-102-01-008 | The Scope of Work shall record the responsibility assignment: EPC Integrator owns scope definition, integration, and oversight of execution for PKG-102 monolithic foundation deliverables. | `DELIVERABLE_REGISTER.csv` DEL-102-01 row |
| R-102-01-009 | The Scope of Work shall identify external dependencies necessary for downstream design closure: geotechnical assessment report, topographical survey/grade surface file, and plot plan (including retention-pond reference drawing). | DBM-Deepcut SEC-11 "External Dependencies" |
| R-102-01-010 | The Scope of Work shall flag open issues consistent with the source basis: bearing capacity, LPILE curves, dynamic design criteria, and compressor foundation dynamic analysis are TBD pending external inputs. | DBM-Deepcut SEC-11 "Assumptions, TBDs, and Design Development Requirements" |
| R-102-01-011 | The Scope of Work shall traceably support Objectives OBJ-001 and OBJ-008 via the PKG-102 package-grouping mapping. | `OBJECTIVE_REGISTER.csv` OBJ-001, OBJ-008; `DELIVERABLE_REGISTER.csv` PKG-102 row (ASSUMPTION: PACKAGE_HEURISTIC association) |

## Standards

| Standard | Role | Source (local accessibility) |
|---|---|---|
| CAN/CSA A23.3 (latest edition) — Design of Concrete Structures | Governing design code for monolithic concrete foundations | DBM-Deepcut SEC-11 "Governing Civil and Structural Basis" (standard text not locally accessible — location TBD) |
| CSA A23.1/A23.2 | Concrete materials, construction, and testing | DBM-Deepcut SEC-11 "Governing Civil and Structural Basis" (standard text not locally accessible — location TBD) |
| National Building Code of Canada (latest edition) | Loading (snow, rain, wind, seismic) and building code basis | DBM-Deepcut SEC-11 "Governing Civil and Structural Basis"; "Buildings and Miscellaneous Facilities" (standard text not locally accessible — location TBD) |
| Canadian Foundation Engineering Manual | Foundation engineering reference | DBM-Deepcut SEC-11 "Governing Civil and Structural Basis" (manual text not locally accessible — location TBD) |
| CSA G40.20/G40.21 (350W; 300W) | Structural steel material grades (applies only at embedded/anchor connections, not to monolithic concrete itself) | DBM-Deepcut SEC-11 "Governing Civil and Structural Basis"; ASSUMPTION on applicability scope to embedments |

## Verification

| ReqID | Verification approach |
|---|---|
| R-102-01-001 | Review SoW identification block against `PACKAGE_REGISTER.csv` PKG-102 row and `_CONTEXT.md`. |
| R-102-01-002 | Cross-check SoW against Workbook Packages row 103 (requires workbook extraction; TBD until extracted). |
| R-102-01-003 | Review tagged equipment list against the workbook row 103 source slice (TBD). |
| R-102-01-004 | Review SoW package-function statement against DBM-Deepcut SEC-11 and PKG-102 description. |
| R-102-01-005 | Review SoW standards block against the standards table in DBM-Deepcut SEC-11 "Governing Civil and Structural Basis". |
| R-102-01-006 | Review SoW boundary statements against DBM-Deepcut SEC-11 "Piles and Foundations" table; capture deviations as Open Issues. |
| R-102-01-007 | Review integration narrative against `INTERFACE_REGISTER.csv` rows IFC-1EDEDC0453 and IFC-8283744B5B; confirm both interface types are addressed. |
| R-102-01-008 | Review responsibility assignment against `DELIVERABLE_REGISTER.csv` PKG-102 rows and sibling deliverables (DEL-102-02..04). |
| R-102-01-009 | Verify each external dependency from DBM-Deepcut SEC-11 "External Dependencies" appears in the SoW external-input list. |
| R-102-01-010 | Verify each TBD/open issue from DBM-Deepcut SEC-11 "Assumptions, TBDs, and Design Development Requirements" is reflected in the SoW open-issues section. |
| R-102-01-011 | Trace SoW objective support to `OBJECTIVE_REGISTER.csv` (OBJ-001, OBJ-008) via the `OBJECTIVE_DELIVERABLE_MAP.csv` / `OBJECTIVE_PACKAGE_MAP.csv` entry for PKG-102. |

## Documentation

Anticipated artifacts that this Scope of Work shall produce or directly enable (per `_CONTEXT.md` Anticipated Artifacts):

- Package Scope of Work document (this deliverable's primary artifact).
- Tagged equipment and package identity list (data table; TBD source slice).
- Package function and integration narrative (prose).
- Responsibility assignment record (table).
