# Specification: DEL-037-03_construction-work-package

## Scope

This specification governs the EPC Integrator-authored Construction Work Package for `PKG-037`, the 5kV SWITCHGEAR ELECTRICAL BUILDING (880-1). The Construction Work Package is a mandatory Gate 5 EPC anchor deliverable and shall describe how the package will be physically installed, built, inspected, turned over, and tied into the larger facility systems.

The package is a vendor-owned Electrical package under WBS 01. The Package Vendor delivers the prefabricated electrical building and its housed equipment; the EPC Integrator executes site installation, tie-ins, constructability coordination, and facility-level integration.

Exclusions:

- Vendor detailed engineering of the building and switchgear (covered by `DEL-037-04_vendor-engineered-equipment-package`).
- Vendor document register and submittals (covered by `DEL-037-05_vendor-document-turnover-package`).
- EPC vendor package review and acceptance (covered by `DEL-037-06_epc-vendor-package-review-and-acceptance`).
- Detailed construction schedule, manpower loading, and lift plans are `TBD` pending EPC Integrator construction execution planning and confirmed vendor delivery dates.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-037-03-001 | The Construction Work Package shall identify `PKG-037`, workbook row 39, WBS 01, CoA tracking number 26020-01-30-028, discipline Electrical, and package name "5kV SWITCHGEAR ELECTRICAL BUILDING (880-1)." Source: Workbook Packages row 39; `PACKAGE_REGISTER.csv`. | Identity review against workbook row and Gate 7 registers. |
| REQ-037-03-002 | The Construction Work Package shall state the accepted responsibility split: Package Vendor delivers the engineered electrical building and physical equipment; EPC Integrator executes site installation, tie-ins, constructability, and facility-level integration. Source: `PACKAGE_REGISTER.csv` row `PKG-037`. | Responsibility statement review against Gate 7 package register. |
| REQ-037-03-003 | The Construction Work Package shall plan for installation of a prefabricated, modular electrical building, elevated on piles with bottom-entry cable provisions and n+1 HVAC. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings section. | Installation plan review against the DBM electrical buildings source slice. |
| REQ-037-03-004 | The Construction Work Package shall identify and plan tie-ins for all twelve applicable interfaces: Utility Piping, Drain/Containment, Electrical Power, Grounding/Bonding, Area/Exterior Lighting, I&C/Control Cabling, Communications/Network, Building HVAC/Services, Fire & Gas/Safety Systems, Maintenance Access, Grading/Site Drainage/Spill Containment, and Structural/Foundations/Supports. Source: Workbook Packages row 39; `INTERFACE_REGISTER.csv`. | Tie-in checklist review against `INTERFACE_REGISTER.csv` rows for `PKG-037`. |
| REQ-037-03-005 | Grounding installation shall connect all major electrical equipment to the facility ground grid at two points, with ground wells at the electrical building for maintenance and operational testing; above-grade ground conductors shall be green insulated, in PVC conduit where mechanical protection is required, with compression connections. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding section. | Construction inspection of grounding installation against the DBM grounding source slice. |
| REQ-037-03-006 | Cable installation within the building shall use TECK and ACIC cables; EMT conduit shall be used between adjacent panels; an outdoor GFI receptacle shall be provided for exterior maintenance; equipment doors or removable transom sections shall accommodate removal of the largest housed equipment. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings section. | Walkdown inspection against the DBM electrical buildings source slice. |
| REQ-037-03-007 | The construction turnover checklist shall capture grounding test records, HVAC functional checks, verified bottom-entry cable provisions, and maintenance-access verification. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings and grounding sections. | Turnover package review against the construction interface and turnover checklist artifact. |
| REQ-037-03-008 | The Construction Work Package shall mark detailed construction schedule, lift plans, manpower loading, and final installation coordinates as `TBD` until vendor delivery, site readiness, and facility-level schedule integration are confirmed. Source: Source gap; `PACKAGE_REGISTER.csv` row `PKG-037`. | Gap review before construction mobilization. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical installation, grounding, and conduit basis for the electrical building and its housed equipment. | Applicable per DBM electrical design basis; clause locations `TBD`. |
| Project electrical specifications | Voltage, MCC, grounding, cable, and raceway basis referenced by the DBM electrical section. | Applicable; document location `TBD`. |
| Area classification standards | Electrical buildings shall be located in general purpose areas; classification of adjacent areas governs cable sealing and equipment ratings. | Applicable; specific classification documentation `TBD`. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare construction work package identity fields to workbook row 39 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface coverage | Compare tie-in checklist to `INTERFACE_REGISTER.csv` rows for `PKG-037`. | All twelve applicable interface facts are addressed by a tie-in or coordination action. |
| Source fidelity | Check every non-trivial installation requirement against cited DBM source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not asserted as fact. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC construction scopes are not conflated. |
| Turnover readiness | Construction interface and turnover checklist completed with grounding tests, HVAC checks, and access verification recorded. | Checklist signed by EPC Integrator construction lead before handoff to commissioning. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Construction work package narrative.
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.
- Grounding test records and HVAC functional check records.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 39, applicable Gate 7 registers, and the DBM electrical building / grounding source slices used.
