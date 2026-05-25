# Specification: DEL-001-01 Scope of Work

## Scope

This deliverable shall define the EPC Scope of Work for PKG-001, "Earthworks for foundations," as a distinct Civil package under WBS 01. It shall include the package identity, source basis, boundaries, source-supported interfaces, whole-facility integration narrative, and responsibility assignment record.

The scope shall cover SOW-0001 from the accepted Gate 7 decomposition basis: carry the workbook-defined Civil package "Earthworks for foundations" as a distinct flat project package for WBS 01. Source: Gate 7 `SCOPE_LEDGER.csv`, SOW-0001.

The scope excludes package-specific earthwork quantities, final geotechnical values, final survey values, final plot-plan coordinates, and final detailed design criteria unless those inputs are provided by authoritative sources. These items are currently `TBD`.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| SOW-REQ-001 | The Scope of Work shall identify PKG-001 as "Earthworks for foundations," Discipline Civil, WBS 01, CoA tracking number 26020-01-42-001. Source: Gate 7 `PACKAGE_REGISTER.csv`, PKG-001; workbook Packages row 2. | Confirm identity fields match Datasheet and Gate 7 package row. |
| SOW-REQ-002 | The Scope of Work shall state that the package is a distinct flat project package and is not merged with the duplicate tracking-number WBS 02 package. Source: Gate 7 `SCOPE_LEDGER.csv`, SOW-0001. | Confirm SOW-0001 is cited and no merge with PKG-002 is implied. |
| SOW-REQ-003 | The Scope of Work shall include the source-supported interfaces marked for Workbook Packages row 2: Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports. Source: Gate 7 `INTERFACE_REGISTER.csv`, PKG-001; `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages row 2. | Confirm both interface types appear in the package boundary and integration sections. |
| SOW-REQ-004 | The Scope of Work shall identify tagged equipment as `TBD` unless a source-supported equipment list is provided for this civil package. Source: Gate 7 `DELIVERABLE_REGISTER.csv`, DEL-001-01; workbook Packages row 2. | Confirm no unsupported equipment tags are introduced. |
| SOW-REQ-005 | The Scope of Work shall preserve the current civil basis that geotechnical assessment and topographical survey inputs are required before final foundation, grading, drainage, and road design closure. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Geotechnical and Topographical Assumptions. | Confirm required external inputs and open TBDs are listed. |
| SOW-REQ-006 | The Scope of Work shall state that site grading and drainage are to prevent off-site surface overflow from entering the expansion facility and direct/contain on-site overflow into a retention pond. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Site Grading and Surface Water Management. | Confirm grading/drainage narrative includes the surface-water intent. |
| SOW-REQ-007 | The Scope of Work shall carry driven steel piles as the default foundation support basis for buildings, equipment, towers, tanks, modules, pipe racks, and similar structures unless detailed engineering confirms a different support requirement. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Piles and Foundations. | Confirm foundation narrative is marked as current basis and not final design. |
| SOW-REQ-008 | The Scope of Work shall distinguish EPC Integrator scope definition from field construction responsibility. Field construction including grading, piling, and foundation work is assigned to Tourmaline field construction scope in the DBM. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility. | Confirm responsibility assignment record separates scope definition from field construction execution. |

## Standards

| Standard or basis | Applicability | Source |
|---|---|---|
| National Building Code of Canada | Building, structural, foundation, snow/rain/wind/seismic loading, and egress basis where applicable | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Governing Civil and Structural Basis |
| CAN/CSA-S16 Design of Steel Structures | Steel design basis where structural steel is implicated by supports | Same as above |
| CAN/CSA A23.3 Design of Concrete Structures | Concrete design basis where concrete foundations or bearing elements are implicated | Same as above |
| Canadian Foundation Engineering Manual | Foundation engineering basis | Same as above |
| CSA G40.20/G40.21 | Structural steel material basis | Same as above |
| CSA A23.1/A23.2 | Concrete materials, construction, and testing basis | Same as above |
| Rational Method, Q = CIA | Runoff calculation basis | Same as above |
| Manning's equation | Ditch and culvert sizing basis | Same as above |

## Verification

- Verify the package identity against Gate 7 `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, and workbook Packages row 2.
- Verify that only the two source-supported interface types are claimed unless additional source evidence is added.
- Verify that all final design parameters depending on geotechnical assessment, topographical survey, plot plan, detailed engineering drainage design, or dynamic analysis remain `TBD` until source-supported.
- Verify that responsibility language does not assign vendor-package ownership; the accepted package row states EPC Integrator or discipline subcontractor responsibility is source-dependent.
- Verify that civil standards are cited as governing basis without inventing clause-level requirements.

## Documentation

The completed Scope of Work shall include:

- package scope of work;
- tagged equipment and package identity list, with tagged equipment marked `TBD` if not source-supported;
- package function and integration narrative;
- responsibility assignment record;
- interface basis for Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports;
- list of open inputs and `TBD` items requiring later closure.
