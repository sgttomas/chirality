# Specification: DEL-036-02_package-datasheet

## Scope

This specification governs the EPC Integrator-authored Package Datasheet for `PKG-036`, the 6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1) package. The datasheet is a mandatory Gate 5 EPC anchor deliverable and shall provide the technical handoff basis required for third-party vendor or discipline package engineering and design.

The package is a vendor-owned Electrical package under WBS 01. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, and final equipment selections are excluded from this EPC datasheet unless later provided as vendor data.
- Package-specific switchgear ratings (interrupting/withstand), bus sizing, lineup counts, transformer feed sizing, MCC frame ratings, UPS sizing, building dimensions, and a confirmed building location are `TBD` because the accessible source set does not provide confirmed package-specific values.
- The package-specific exclusion list in `PACKAGE_REGISTER.csv` is `TBD; no package-specific exclusions stated in source materials.`

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-036-02-001 | The Package Datasheet shall identify `PKG-036`, workbook row 38, WBS 01, CoA tracking number 26020-01-30-027, discipline Electrical, and package name "6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1)." Source: Workbook Packages row 38; `PACKAGE_REGISTER.csv`. | Datasheet identification review against workbook row and Gate 7 registers. |
| REQ-036-02-002 | The Package Datasheet shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-036`. | Responsibility statement review against Gate 7 package register. |
| REQ-036-02-003 | The Package Datasheet shall include the twelve applicable interface facts as carried evidence (not separate deliverables): Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. Source: Workbook Packages row 38; `INTERFACE_REGISTER.csv`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-036`. |
| REQ-036-02-004 | The Package Datasheet shall identify the medium-voltage service basis as 6.9 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded, and shall not assign unsupported package-specific switchgear or transformer ratings. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2935. | Source citation review; unsupported values remain `TBD`. |
| REQ-036-02-005 | The Package Datasheet shall require the electrical building to be a prefabricated, modular building located in a general purpose area, climate-controlled with HVAC sized as n + 1, designed for bottom cable entry, elevated on piles, and wired with TECK and ACIC cables; equipment doors shall accommodate removal of the largest equipment. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2911, L2973-2979. | Source citation review against drawings and datasheet attribute table. |
| REQ-036-02-006 | The Package Datasheet shall require grounding of major electrical equipment to the ground grid at two points and grounding of each 6.9 kV transformer using a 100 A, 10 s neutral grounding resistor operating as a tripping system, without overstating package-specific grounding details not present in source. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2985, L2989. | Electrical interface review. |
| REQ-036-02-007 | The Package Datasheet shall require cable tray and conduit routing to preserve maintenance access, and shall require interconnecting trays between main pipe racks, process skids, and electrical buildings to be field-run consistent with facility cable routing basis. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2979, L2999. | Layout/interface review against the package interface matrix. |
| REQ-036-02-008 | The Package Datasheet shall require 6.9 kV medium-voltage cable to be three-conductor copper TECK cable rated 8 kV with 100 percent insulation, shielded, where MV cabling is within EPC scope for the building feeders. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L3008. | Cable schedule and BOM review. |
| REQ-036-02-009 | The Package Datasheet shall preserve a minimum 25 m (82 ft) separation between fired heaters and electrical buildings for facility integration of the building location. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L298 (OGAOM Sec. 9.6.15). | Plot-plan review for the EPC building placement. |
| REQ-036-02-010 | The Package Datasheet shall identify source gaps for switchgear ratings, bus sizing, transformer feed sizing, MCC frame ratings, UPS sizing, building dimensions, and final building location/coordinates as `TBD` rather than as invented values. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search. | Gap review before vendor handoff. |
| REQ-036-02-011 | The Package Datasheet shall preserve the workbook-given package name "6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1)" and shall flag the conflict between the workbook identity (6.9 kV at 830-1) and the DBM electrical-building list (830-1 = 4.16 kV; 820-1 = 6.9 kV) for human ruling without silently re-naming. Source: Workbook Packages row 38; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2811-2816, L2921. | Conflict-table review against Gate 7 register spellings. |
| REQ-036-02-012 | The Package Datasheet shall list this package's support of `OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010` per the objective-deliverable map, treated as `ASSUMPTION` per `PACKAGE_HEURISTIC` until human-confirmed. Source: `OBJECTIVE_DELIVERABLE_MAP.csv`. | Objective-association review. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, conduit support, and electrical installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| OGAOM Sec. 9.6.15 | Minimum facility separation between fired heater and electrical buildings (25 m / 82 ft). | Applicable; cited in DBM L298. |
| Project electrical specifications | Voltage/switchgear/MCC/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable to electrical buildings located in general-purpose areas and to equipment classification where required. | Applicable; building location to be confirmed. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare datasheet identity fields to workbook row 38 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare datasheet matrix to `INTERFACE_REGISTER.csv` rows for `PKG-036`. | All twelve interface facts are present. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and `TBD` items. | No unresolved internal inconsistency. |
| Conflict surfacing | Confirm building-identity conflict (workbook 830-1 6.9 kV vs DBM 830-1 4.16 kV / 820-1 6.9 kV) is captured in the Guidance Conflict Table. | Conflict entry exists with both source locations and a proposed authority. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Package technical datasheet.
- Vendor engineering handoff basis.
- Package interface requirements matrix.
- Source-supported equipment and design criteria.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 38, applicable Gate 7 registers, and the DBM electrical source slices used for medium-voltage, electrical-building, grounding, cable/raceway, and building-placement basis.
