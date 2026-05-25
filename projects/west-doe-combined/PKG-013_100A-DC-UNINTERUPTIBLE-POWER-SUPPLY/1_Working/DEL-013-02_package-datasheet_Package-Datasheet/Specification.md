# Specification: DEL-013-02_package-datasheet

## Scope

This specification governs the EPC Integrator-authored Package Datasheet for `PKG-013`, the 100A DC UNINTERUPTIBLE POWER SUPPLY package. The datasheet is a mandatory Gate 5 EPC anchor deliverable and shall provide the technical handoff basis required for third-party vendor or discipline package engineering and design.

The package is a vendor-owned Electrical package under WBS 02. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, and final equipment selections are excluded from this EPC datasheet unless later provided as vendor data.
- Package-specific UPS ratings, autonomy, charger data, battery type, feeder sizing, distribution-panel assignments, and installation location are `TBD` because the accessible source set does not provide confirmed package-specific values.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-013-02-001 | The Package Datasheet shall identify `PKG-013`, workbook row 15, WBS 02, CoA tracking number 26020-02-30-004, discipline Electrical, and package name "100A DC UNINTERUPTIBLE POWER SUPPLY." Source: Workbook Packages row 15; `PACKAGE_REGISTER.csv`. | Datasheet identification review against workbook row and Gate 7 registers. |
| REQ-013-02-002 | The Package Datasheet shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-013`. | Responsibility statement review against Gate 7 package register. |
| REQ-013-02-003 | The Package Datasheet shall include the four applicable interface facts: Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports. Source: Workbook Packages row 15; `INTERFACE_REGISTER.csv`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-013`. |
| REQ-013-02-004 | The Package Datasheet shall identify UPS service basis as 120 VAC / 125 VDC where supported by the DBM electrical design basis, and shall not assign unsupported package-specific ratings. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltage/service table. | Source citation review; unsupported values remain `TBD`. |
| REQ-013-02-005 | The Package Datasheet shall preserve standby power requirements as an interface and mark generator sizing, transfer-switch configuration, load shedding, sequencing, and TOU standard confirmation as `TBD` unless later source material resolves them. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, standby power paragraph. | TBD/open-item review. |
| REQ-013-02-006 | The Package Datasheet shall capture grounding/bonding requirements applicable to electrical equipment without overstating package-specific grounding details not present in source. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs. | Electrical interface review. |
| REQ-013-02-007 | The Package Datasheet shall require cable tray and conduit routing to preserve maintenance access. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs. | Layout/interface review against the package interface matrix. |
| REQ-013-02-008 | The Package Datasheet shall identify source gaps for UPS count/rating, battery, charger, feeder, distribution, physical location, and support requirements as `TBD` instead of invented values. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search. | Gap review before vendor handoff. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, conduit support, and electrical installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable to electrical equipment, conduit sealing, and installation classification where hazardous/non-hazardous areas are defined. | Applicable; package location/classification TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare datasheet identity fields to workbook row 15 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare datasheet matrix to `INTERFACE_REGISTER.csv` rows for `PKG-013`. | Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports are present. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Package technical datasheet.
- Vendor engineering handoff basis.
- Package interface requirements matrix.
- Source-supported equipment and design criteria.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 15, applicable Gate 7 registers, and the DBM electrical source slices used for UPS/electrical design basis.
