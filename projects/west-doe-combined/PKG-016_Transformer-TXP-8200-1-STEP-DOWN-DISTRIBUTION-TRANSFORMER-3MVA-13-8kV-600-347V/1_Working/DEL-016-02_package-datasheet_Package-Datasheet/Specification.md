# Specification: DEL-016-02_package-datasheet

## Scope

This specification governs the EPC Integrator-authored Package Datasheet for `PKG-016`, the Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 3MVA 13.8kV/600/347V package. The datasheet is a mandatory Gate 5 EPC anchor deliverable and shall provide the technical handoff basis required for third-party vendor or discipline package engineering and design.

The package is a vendor-owned Electrical package under WBS 02. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, and final equipment selections are excluded from this EPC datasheet unless later provided as vendor data.
- Insulation/cooling type, BIL, impedance, tap configuration, winding configuration, losses, sound level, enclosure type, and physical installation location are `TBD` because the accessible source set does not provide confirmed package-specific values.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-016-02-001 | The Package Datasheet shall identify `PKG-016`, workbook row 18, WBS 02, CoA tracking number 26020-02-30-007, discipline Electrical, and package name "Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 3MVA 13.8kV/600/347V." Source: Workbook Packages row 18; `PACKAGE_REGISTER.csv`. | Datasheet identification review against workbook row and Gate 7 registers. |
| REQ-016-02-002 | The Package Datasheet shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-016`. | Responsibility statement review against Gate 7 package register. |
| REQ-016-02-003 | The Package Datasheet shall include the seven applicable interface facts: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 18; `INTERFACE_REGISTER.csv`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-016`. |
| REQ-016-02-004 | The Package Datasheet shall identify primary voltage 13.8 kV and secondary 600 V / 347 V and rated capacity 3 MVA, consistent with workbook row 18 and the DBM Incoming Power and Transformers feeder list entry "13.8 kV to 600V, 3 MVA transformer." Source: Workbook Packages row 18; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`. | Cross-check datasheet voltage and rating against DBM and workbook. |
| REQ-016-02-005 | The Package Datasheet shall reflect the DBM grounding basis: 13.8 kV primary is LRG; 600 V LV service is HRG with 5 A continuous resistor. Final transformer secondary winding/neutral treatment shall be determined by vendor data and detailed electrical study and shall be carried as `TBD` until then. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, System Voltages. | Source citation review; unsupported values remain `TBD`. |
| REQ-016-02-006 | The Package Datasheet shall describe the downstream service as the 600 V MCC for LV loads at 03-25 and identify the upstream source as the 04-25 13.8 kV Main Switchgear Electrical Building. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Incoming Power and Transformers; 600V MCC and Standby Power. | Service-description review against DBM. |
| REQ-016-02-007 | The Package Datasheet shall require 13.8 kV and 600 V power circuits to be separated from control and instrument circuits by distance, shielding, or routing per DBM, and shall not overstate package-specific routing rules. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings/Raceways. | Routing/interface review against DBM. |
| REQ-016-02-008 | The Package Datasheet shall identify source gaps for insulation/cooling type, BIL, impedance, tap configuration, winding configuration, losses, sound level, enclosure type, and physical installation location as `TBD` instead of invented values. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search. | Gap review before vendor handoff. |
| REQ-016-02-009 | The Package Datasheet shall acknowledge facility area classification basis (Class I Zone 2, Gas Groups IIA/IIB) without assigning a package-specific area classification absent source confirmation. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Area Classification. | Area-classification review. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, conduit support, and electrical installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards (e.g., API RP 505 as referenced by DBM) | Applicable to electrical equipment, conduit sealing, and installation classification where hazardous/non-hazardous areas are defined. | Applicable; package location/classification TBD. |
| Distribution transformer standards (e.g., CSA / IEEE / IEC families for power and distribution transformers) | ASSUMPTION: likely applicable to a 13.8 kV / 600 V, 3 MVA distribution transformer. Specific standard family and clause locations TBD pending vendor data. | ASSUMPTION; document location TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare datasheet identity fields to workbook row 18 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare datasheet matrix to `INTERFACE_REGISTER.csv` rows for `PKG-016`. | All seven applicable interfaces are present. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Voltage/rating consistency | Cross-check datasheet voltage and MVA rating against workbook row 18 and DBM transformer feeder list. | Datasheet matches 13.8 kV primary, 600 V / 347 V secondary, 3 MVA. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Package technical datasheet.
- Vendor engineering handoff basis.
- Package interface requirements matrix.
- Source-supported equipment and design criteria.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 18, applicable Gate 7 registers, and the DBM electrical source slices used for transformer/electrical design basis.
