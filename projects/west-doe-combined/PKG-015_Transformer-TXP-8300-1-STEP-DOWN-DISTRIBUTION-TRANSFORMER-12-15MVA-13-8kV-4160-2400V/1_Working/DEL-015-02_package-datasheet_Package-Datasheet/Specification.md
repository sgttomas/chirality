# Specification: DEL-015-02_package-datasheet

## Scope

This specification governs the EPC Integrator-authored Package Datasheet for `PKG-015`, the "Transformer TXP-8300-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 12/15MVA 13.8kV/4160/2400V" package. The datasheet is a mandatory Gate 5 EPC anchor deliverable and shall provide the technical handoff basis required for third-party vendor or discipline package engineering and design.

The package is a vendor-owned Electrical package under WBS 02. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, type-test certificates, and final equipment selections are excluded from this EPC datasheet unless later provided as vendor data.
- Transformer-specific values not present in the accessible source set (cooling class, BIL, insulation level, vector group, impedance, tap range, audible noise, weight/footprint, dielectric fluid type, bushings/radiator/conservator details, on-load tap changer details) are `TBD`.
- The 15 MVA forced-air (FA) rating and 2400 V tertiary winding present in the package title are not confirmed by the accessible DBM source slice and are carried as `ASSUMPTION` until source-confirmed.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-015-02-001 | The Package Datasheet shall identify `PKG-015`, workbook row 17, WBS 02, CoA tracking number 26020-02-30-006, discipline Electrical, equipment tag TXP-8300-1, and the package name as spelled in the workbook. Source: Workbook Packages row 17; `PACKAGE_REGISTER.csv`. | Datasheet identification review against workbook row and Gate 7 registers. |
| REQ-015-02-002 | The Package Datasheet shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-015`. | Responsibility statement review against Gate 7 package register. |
| REQ-015-02-003 | The Package Datasheet shall include all seven applicable interface facts: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 17; `INTERFACE_REGISTER.csv`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-015`. |
| REQ-015-02-004 | The Package Datasheet shall identify primary voltage as 13.8 kV, 3 phase, 3 wire, 60 Hz LRG, and confirmed secondary as 4.16 kV, 3 phase, 3 wire, 60 Hz LRG, in agreement with the DBM System Voltages table and Incoming Power and Transformers table. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 Electrical Basis. | Voltage values reviewed against the DBM source slice. |
| REQ-015-02-005 | The Package Datasheet shall record the 12 MVA rating from the DBM Incoming Power and Transformers table as the source-confirmed nameplate basis, and shall carry the "15 MVA" forced-air rating and "2400 V" tertiary as `ASSUMPTION` derived from the package title until vendor data or additional source confirms them. Source: Workbook Packages row 17; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Incoming Power and Transformers table. | Source citation review; unsupported values remain `TBD`/`ASSUMPTION`. |
| REQ-015-02-006 | The Package Datasheet shall identify the served load as the 4160V MCC and large 4000V motors (including inlet compressors KM-2150 and KM-2250) without assigning unsupported transformer-specific protection, tap, or impedance values. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160V MCC section. | Load assignment review against the source. |
| REQ-015-02-007 | The Package Datasheet shall require power-circuit separation from control and instrument circuits by distance, shielding, or routing, consistent with the DBM raceway basis. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings, Raceways, Lighting, and Heat Tracing section. | Layout/interface review against the package interface matrix. |
| REQ-015-02-008 | The Package Datasheet shall require foundation design to address final geotechnical report, equipment loads, snow/wind/seismic criteria, frost protection, vibration, settlement, and maintenance access. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Foundations paragraph. | Foundation requirement review against the source. |
| REQ-015-02-009 | The Package Datasheet shall identify source gaps for cooling class, insulation/BIL, vector group, impedance, tap range, bushings, radiator/conservator/fan details, on-load tap changer details, dielectric fluid, dimensions/weights, and physical installation location as `TBD` instead of invented values. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search. | Gap review before vendor handoff. |
| REQ-015-02-010 | The Package Datasheet shall reflect the package's communications interface basis: vendor data may be integrated via Modbus through Kepware KepserverEX for monitoring only; process control shall not be carried over Modbus. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Unit Control Systems and Package Interfaces section. | Communications interface review. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, conduit support, and electrical installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards (API RP 505 referenced for adjacent process modules) | Applicable to electrical equipment installation classification where hazardous/non-hazardous areas are defined; transformer-specific applicability shall be confirmed by detailed area classification drawings. | Applicable; package classification confirmation TBD. |
| Transformer industry standards (e.g., CSA C88, IEEE C57 series) | Likely applicable to MV step-down distribution transformers of this rating; specific clauses cannot be cited without accessible standard texts. | ASSUMPTION: likely applicable; not derivable from accessible source. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare datasheet identity fields to workbook row 17 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare datasheet matrix to `INTERFACE_REGISTER.csv` rows for `PKG-015`. | All seven applicable interface facts are present with matching `IFC-*` IDs. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, ratings, interfaces, and TBDs. | No unresolved internal inconsistency. |
| Rating/voltage handling | Confirm 12 MVA and 4.16 kV are cited from the DBM Incoming Power and Transformers table; confirm 15 MVA FA and 2400 V tertiary are marked `ASSUMPTION`. | Source-grounding rule preserved. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Package technical datasheet.
- Vendor engineering handoff basis.
- Package interface requirements matrix.
- Source-supported equipment and design criteria.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 17, applicable Gate 7 registers, and the DBM electrical source slices used for the transformer service basis and facility integration.
