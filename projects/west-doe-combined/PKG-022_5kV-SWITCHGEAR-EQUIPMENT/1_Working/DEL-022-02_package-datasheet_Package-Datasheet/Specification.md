# Specification: DEL-022-02_package-datasheet

## Scope

This specification governs the EPC Integrator-authored Package Datasheet for `PKG-022`, the 5kV SWITCHGEAR EQUIPMENT package. The datasheet is a mandatory Gate 5 EPC anchor deliverable and shall provide the technical handoff basis required for third-party vendor or discipline package engineering and design.

The package is a vendor-owned Electrical package under WBS 01. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, short-circuit and coordination studies, and final equipment selections are excluded from this EPC datasheet unless later provided as vendor data.
- Package-specific nominal voltage rating, bus ampacity, short-circuit withstand, breaker complement, protection-and-control configuration, electrical-building assignment, and physical arrangement are `TBD` because the accessible source set does not provide confirmed package-specific values.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-022-02-001 | The Package Datasheet shall identify `PKG-022`, workbook row 24, WBS 01, CoA tracking number 26020-01-30-013, discipline Electrical, and package name "5kV SWITCHGEAR EQUIPMENT." Source: Workbook Packages row 24; `PACKAGE_REGISTER.csv`. | Datasheet identification review against workbook row and Gate 7 registers. |
| REQ-022-02-002 | The Package Datasheet shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-022`. | Responsibility statement review against Gate 7 package register. |
| REQ-022-02-003 | The Package Datasheet shall include the six applicable interface facts: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. Source: Workbook Packages row 24; `INTERFACE_REGISTER.csv`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-022`. |
| REQ-022-02-004 | The Package Datasheet shall identify `ELC-QAS-000007-001` Medium Voltage Switchgear (Revision 1) as a governing equipment specification. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical and instrumentation specifications table. | Source citation review. |
| REQ-022-02-005 | The Package Datasheet shall surface and not silently resolve the discrepancy between the workbook package name "5kV SWITCHGEAR EQUIPMENT" and the DBM medium-voltage levels (13.8 kV main, 6.9 kV process, 4.160 kV process; "5 kV" appears only as cable insulation class for 4.160 kV TECK cable). Nominal voltage rating for the package shall remain `TBD` until human ruling. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, system voltages and cable specifications tables. | Conflict-table review; `TBD` retained until resolved. |
| REQ-022-02-006 | The Package Datasheet shall require switchgear control and protection power to be coordinated with the facility 120 VAC / 125 VDC UPS services that feed MV breaker control circuits and MV protective relays. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, UPS services row of system voltages table. | Cross-package interface review. |
| REQ-022-02-007 | The Package Datasheet shall capture grounding/bonding requirements applicable to electrical equipment (two-point connection to ground grid, ground wells at electrical buildings, CEC-sized separate copper ground conductors where applicable) without overstating package-specific grounding details not present in source. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs. | Electrical interface review. |
| REQ-022-02-008 | The Package Datasheet shall require cable tray and conduit routing to preserve maintenance access and shall align MV cable selection with the DBM cable specifications table (insulation class TBD pending nominal voltage confirmation). Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable, wire, and raceways section. | Layout/interface review against the package interface matrix. |
| REQ-022-02-009 | The Package Datasheet shall identify source gaps for nominal voltage, bus ampacity, short-circuit rating, breaker complement, protection scheme, communications topology, physical location, and support requirements as `TBD` instead of invented values. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search status. | Gap review before vendor handoff. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| `ELC-QAS-000007-001` Medium Voltage Switchgear (Rev 1) | Governing equipment specification for medium-voltage switchgear. | Applicable as identified by DBM electrical and instrumentation specifications table; specification document location TBD in deliverable folder. |
| `ELC-QAS-000003-001` Electrical Requirements for Packaged Equipment (Rev 2) | Governing requirements applicable to packaged electrical equipment. | Applicable per DBM Table 12-1; document location TBD. |
| `ELC-QAS-000002-001` Electrical Design (Rev 1); `ELC-QAS-000001-001` Electrical Construction (Rev 1) | Project electrical design and construction basis. | Applicable per DBM Table 12-1; document location TBD. |
| Canadian Electrical Code (CEC) | Electrical grounding, conduit, installation, and clearance basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Area classification standards | Applicable where equipment, conduit sealing, or installation is in classified locations. | Applicable; package location/classification TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare datasheet identity fields to workbook row 24 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare datasheet matrix to `INTERFACE_REGISTER.csv` rows for `PKG-022`. | Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports are all present. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Voltage-class conflict | Confirm the package nominal voltage is not silently set from the package title. | Nominal voltage remains `TBD` and conflict appears in Guidance conflict table and run record. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, governing specifications, and `TBD` items. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Package technical datasheet.
- Vendor engineering handoff basis.
- Package interface requirements matrix (six interface facts).
- Source-supported equipment and design criteria.
- Source-gap / `TBD` list for vendor or human resolution, including voltage-class disambiguation.

The deliverable shall cite the Gate 7 snapshot, workbook row 24, applicable Gate 7 registers, and the DBM electrical source slices used for the medium-voltage switchgear basis.
