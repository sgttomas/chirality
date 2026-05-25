# Specification: EPC / Civil Discipline Production Package

## Scope

This specification covers the source-limited EPC / Civil Discipline Production Package for `PKG-007` Retention Pond, deliverable `DEL-007-04_epc-civil-discipline-production-package`.

The package is limited to the workbook-defined Civil retention pond package under WBS 02 and the accepted Gate 7 decomposition basis. The package includes civil production-package basis development for retention pond, drainage, containment, grading, and spill-containment interface requirements supported by the accessible sources.

Exclusions:

- Vendor-engineered equipment package production is not inferred for this package. Source: Gate 7 `PACKAGE_REGISTER.csv`, `PKG-007`, responsibility model.
- Final pond location, pond capacity, final IDF duration, ditch and culvert sizing, geotechnical design parameters, and topographical ground model remain TBD pending external inputs. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `External Dependencies`.
- Discipline deliverable register contents beyond the Gate 7 artifact expectations are TBD.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-00704-001 | The package shall preserve `PKG-007` as the workbook-defined Civil package "Retention Pond" under WBS 02 and CoA tracking number `26020-02-42-007`. | Gate 7 `PACKAGE_REGISTER.csv`, `PKG-007`; `_Sources/26020-Packages_Interfaces_4_export.xlsx`, sheet `Packages`, row 8. |
| REQ-00704-002 | The production package shall include a discipline production package basis and a source-limited requirements closure record. | Gate 7 `DELIVERABLE_REGISTER.csv`, `DEL-007-04`; Gate 7 `ARTIFACT_REGISTER.csv`, artifacts `ART-544A9E5234` and `ART-7E195464D1`. |
| REQ-00704-003 | The civil production basis shall address the applicable interface facts: Drain / Containment and Grading / Site Drainage / Spill Containment. | Gate 7 `INTERFACE_REGISTER.csv`, `IFC-AB14FD2A67` and `IFC-1B8CFB3D40`; workbook row 8. |
| REQ-00704-004 | Civil grading and drainage shall prevent off-site surface overflow from entering the expansion facility and shall direct and contain on-site overflow into a retention pond. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `Site Grading and Surface Water Management`. |
| REQ-00704-005 | The retention pond shall be an on-site retention pond with berm to capture natural runoff, with location and capacity established during detailed engineering. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `Site Grading and Surface Water Management`. |
| REQ-00704-006 | Surface-control features shall be considered within the facility and around selected equipment to prevent on-site releases from discharging outside the facility boundaries. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `Site Grading and Surface Water Management`. |
| REQ-00704-007 | General site grading and drainage engineering shall apply the DBM design principles for pad slope, grade slope, ditch slope, culvert slope, and ditch/culvert storm basis unless replaced by geotechnical report, topographical survey, plot plan, or detailed engineering analysis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `Governing Civil and Structural Basis` and `Site Grading and Surface Water Management`. |
| REQ-00704-008 | Retention pond sizing and drainage design shall carry hydrology uncertainty until final hydrology inputs are confirmed. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, `SEC-02` rainfall basis; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `External Dependencies`. |
| REQ-00704-009 | The production package shall identify the required external inputs for detailed civil design: geotechnical assessment, topographical survey / grade surface file, plot plan with retention pond reference, and detailed engineering drainage design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `External Dependencies`. |
| REQ-00704-010 | Detailed design values not supported by accessible source slices shall remain `TBD` and shall not be invented in the discipline production package. | Gate 7 `DELIVERABLE_REGISTER.csv`, `DEL-007-04`, notes; four-documents skill source-grounding rule. |

## Standards

| Standard / basis | Treatment |
|---|---|
| National Building Code of Canada | Governing civil/structural basis; exact edition/clause location TBD. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `Governing Civil and Structural Basis`. |
| CAN/CSA-S16 Design of Steel Structures | Governing basis for steel design where civil/structural supports are in package scope; exact edition/clause location TBD. |
| CAN/CSA A23.3 Design of Concrete Structures | Governing basis for concrete design; exact edition/clause location TBD. |
| Canadian Foundation Engineering Manual | Governing basis for foundation engineering; exact edition/clause location TBD. |
| CSA G40.20/G40.21 | Structural steel material basis: 350W for W-flange and HSS; 300W for channels, plates, and angles. |
| CSA A23.1/A23.2 | Concrete materials, construction, and testing basis. |
| Rational Method, Q = CIA | Runoff calculation basis. |
| Manning's equation | Ditch and culvert sizing basis. |
| NBCC 2020 Dawson Creek IDF proxy | Current rainfall basis proxy pending site-specific hydrology update. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, `SEC-02` rainfall basis. |

## Verification

| Requirement(s) | Verification approach |
|---|---|
| REQ-00704-001 to REQ-00704-003 | Check package identity, artifacts, and interface facts against Gate 7 registers and workbook row 8. |
| REQ-00704-004 to REQ-00704-007 | Review civil production package narrative, drawings/register, and calculations for DBM-consistent grading, drainage, containment, and retention pond treatment. |
| REQ-00704-008 | Confirm retention pond sizing and drainage design notes identify the hydrology basis and open site-specific update dependency. |
| REQ-00704-009 | Confirm the requirements closure record lists external inputs and disposition status. |
| REQ-00704-010 | Review all unsupported values for `TBD`, `ASSUMPTION`, or human-ruling disposition rather than unmarked design assertions. |

## Documentation

The completed production package should include or explicitly defer:

- Discipline production package basis.
- Discipline deliverable register: TBD.
- Source-limited requirements closure record.
- Retention pond / containment basin design basis and calculations: TBD pending detailed engineering.
- Grading and drainage coordination inputs.
- Interface closure evidence for Drain / Containment and Grading / Site Drainage / Spill Containment.
- External-input register for geotechnical report, topographical survey, plot plan, and detailed drainage design.
