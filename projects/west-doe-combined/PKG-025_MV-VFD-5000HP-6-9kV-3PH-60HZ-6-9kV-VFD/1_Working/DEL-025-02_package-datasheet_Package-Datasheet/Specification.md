# Specification: DEL-025-02_package-datasheet

## Scope

This specification governs the EPC Integrator-authored Package Datasheet for `PKG-025`, the "MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD" package. The datasheet is a mandatory Gate 5 EPC anchor deliverable and shall provide the technical handoff basis required for third-party vendor or discipline package engineering and design.

The package is a vendor-owned Electrical package under WBS 01 (CoA 26020-01-30-016). The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, harmonic studies, and final equipment selections are excluded from this EPC datasheet unless later provided as vendor data.
- Package-specific VFD ratings (output current/kVA, drive topology beyond the DBM Starting VFD basis, harmonic class, cooling method, enclosure type, isolation/phase-shift transformer arrangement), quantity allocation to PKG-025, motor identity binding, installation building assignment, and feeder sizing are `TBD` because the accessible source set does not provide confirmed package-specific values.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-025-02-001 | The Package Datasheet shall identify `PKG-025`, workbook row 27, WBS 01, CoA tracking number 26020-01-30-016, discipline Electrical, and package name "MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD." Source: Workbook Packages row 27; `PACKAGE_REGISTER.csv`. | Datasheet identification review against workbook row and Gate 7 registers. |
| REQ-025-02-002 | The Package Datasheet shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-025`. | Responsibility statement review against Gate 7 package register. |
| REQ-025-02-003 | The Package Datasheet shall include all six applicable interface facts: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. Source: Workbook Packages row 27; `INTERFACE_REGISTER.csv`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-025`. |
| REQ-025-02-004 | The Package Datasheet shall declare the VFD service voltage class as 6.9 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded MV service, and shall not assign unsupported package-specific drive ratings. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage/service table. | Source citation review; unsupported values remain `TBD`. |
| REQ-025-02-005 | The Package Datasheet shall record that DBM applies the 6.9 kV service to AC inverter-drive motors rated 5,500 hp and above, and shall flag the mismatch with the 5,000 hp workbook nomenclature as a human-ruling item rather than silently reconciling it. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage/service table; Workbook Packages row 27. | Open-item review; HRR captured in Guidance Conflict Table. |
| REQ-025-02-006 | Where PKG-025 is used as a Starting VFD (per DBM KM-2150/2250 basis), the Package Datasheet shall require synchronous transfer to the MCC-8200 normal-service bus after reaching full speed, and shall prohibit power-factor-correction capacitor banks on that bus. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 6.9 kV MCC paragraph; inlet/sales compressor start-method paragraph. | Cross-check against Datasheet Attributes and Guidance; verification in commissioning records. |
| REQ-025-02-007 | The Package Datasheet shall require 6.9 kV motor feeder cable to be three-conductor copper TECK, rated 8 kV with 100 percent insulation, shielded; and VFD-fed low-voltage power cable to be copper TECK. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MV cable table. | Cable schedule review against DBM cable table. |
| REQ-025-02-008 | The Package Datasheet shall require Zone 2 marking and reduced temperature-code rating on VFD-fed motors located in Zone 2 areas, in alignment with the area classification drawing or fugitive-emissions study. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, motor voltage/Zone 2 paragraph. | Hazardous-area compliance review. |
| REQ-025-02-009 | The Package Datasheet shall require the VFD package's MV breaker control and protective-relay interfaces to be compatible with the 120 VAC / 125 VDC UPS service basis. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, UPS services row. | Control/protection interface review against the package interface matrix. |
| REQ-025-02-010 | The Package Datasheet shall require an Ethernet (or DBM-equivalent) communications interface to the plant PLC central control panel for data acquisition, consistent with the 6.9 kV MCC integration model. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 6.9 kV MCC paragraph. | Communications/Network interface review. |
| REQ-025-02-011 | The Package Datasheet shall capture grounding/bonding requirements applicable to MV equipment (two-point ground-grid connection for major electrical equipment; 100 A 10 s neutral grounding resistor on each 6.9 kV transformer) without overstating package-specific grounding details not present in source. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs. | Electrical interface review. |
| REQ-025-02-012 | The Package Datasheet shall require cable tray and conduit routing to preserve maintenance access. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs. | Layout/interface review against the package interface matrix. |
| REQ-025-02-013 | The Package Datasheet shall identify source gaps for PKG-025 quantity allocation, motor identity binding, VFD topology details, harmonic class, cooling, enclosure, isolation/phase-shift transformer, building assignment, and physical supports as `TBD` instead of invented values. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search. | Gap review before vendor handoff. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, conduit support, and electrical installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations `TBD`. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location `TBD`. |
| Area classification standards | Applicable to VFD-fed motors, conduit sealing, and installation classification where Zone 2 or other hazardous areas are defined. | Applicable; package location/classification `TBD`. |
| Harmonic / power-quality standards (e.g., IEEE 519-class) | Applicable in principle to MV VFD installations; not cited in DBM source slice for this package. | `ASSUMPTION: likely applicable`; clause/location `TBD`. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare datasheet identity fields to workbook row 27 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare datasheet matrix to `INTERFACE_REGISTER.csv` rows for `PKG-025`. | All six interface types (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) are present. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| Starting-VFD basis (if confirmed) | Compare synchronous-transfer and PF-correction-capacitor prohibition to DBM 6.9 kV MCC paragraph. | Matches DBM language; HRR-025-02-002 disposition recorded. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and `TBD`s. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Package technical datasheet.
- Vendor engineering handoff basis.
- Package interface requirements matrix.
- Source-supported equipment and design criteria.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 27, applicable Gate 7 registers, and the DBM electrical source slices used for MV service basis, 6.9 kV MCC / Starting VFD basis, motor/Zone 2 basis, UPS service basis, electrical-building context, grounding basis, and MV cable basis.
