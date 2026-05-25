# Specification: DEL-031-02_package-datasheet

## Scope

This specification governs the EPC Integrator-authored Package Datasheet for `PKG-031`, the Transformer TXP-8500-1 STEP DOWN DISTRIBUTION TRANSFORMER (3 MVA, 13.8 kV / 600 V / 347 V) package. The datasheet is a mandatory Gate 5 EPC anchor deliverable and shall provide the technical handoff basis required for third-party vendor or discipline package engineering and design.

The package is a vendor-owned Electrical package under WBS 01. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, factory test reports, and final equipment selections are excluded from this EPC datasheet unless later provided as vendor data.
- Package-specific transformer construction type (oil-filled vs. dry-type), impedance, vector group, tap range, BIL, cooling class, no-load and load losses, audible-noise rating, sound power level, secondary containment outcome, and final installation location are `TBD` because the accessible source set does not provide confirmed package-specific values for TXP-8500-1.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-031-02-001 | The Package Datasheet shall identify `PKG-031`, workbook row 33, WBS 01, CoA tracking number 26020-01-30-022, discipline Electrical, equipment tag TXP-8500-1, and package name "Transformer TXP-8500-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 3MVA 13.8kV/600/347V." Source: Workbook Packages row 33; `PACKAGE_REGISTER.csv`. | Datasheet identification review against workbook row and Gate 7 registers. |
| REQ-031-02-002 | The Package Datasheet shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-031`. | Responsibility statement review against Gate 7 package register. |
| REQ-031-02-003 | The Package Datasheet shall include the seven applicable interface facts: Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. Source: Workbook Packages row 33; `INTERFACE_REGISTER.csv`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-031`. |
| REQ-031-02-004 | The Package Datasheet shall identify the primary system as 13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded, fed radially from the plant 13.8 kV switchgear. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical systems and System Voltages table. | Source citation review. |
| REQ-031-02-005 | The Package Datasheet shall identify the secondary as 600 V, 3 phase, 3 wire, 60 Hz, high-resistance grounded with a 5 A continuous resistor, with 347 V line-to-neutral available from the 600 V system. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, System Voltages table; `PACKAGE_REGISTER.csv` package name "600/347V." | Source citation review; cross-check against package name. |
| REQ-031-02-006 | The Package Datasheet shall require the 600 V secondary feeder to plant 600 V MCC to be ACWU; single-conductor cables shall be avoided. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cable, Wire, and Raceways table. | Cable specification review. |
| REQ-031-02-007 | The Package Datasheet shall require the 13.8 kV primary feeder to be three-conductor copper TECK, 15 kV rated, 133 percent insulation, shielded. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cable, Wire, and Raceways table. | Cable specification review. |
| REQ-031-02-008 | The Package Datasheet shall require grounding consistent with the facility basis: direct two-point connection of major electrical equipment to the ground grid; separate copper ground conductor for distribution transformers sized per CEC; ground wells at power transformers for maintenance and operational testing. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Grounding and Bonding paragraphs. | Electrical interface review. |
| REQ-031-02-009 | The Package Datasheet shall require transformer spacing in accordance with CEC, structural-steel transformer base on a precast concrete bearing foundation as the general basis, and secondary-containment review with selection biased to limit containment where practical. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Transformers paragraph; Foundations table row "Transformers." | Foundation / containment review. |
| REQ-031-02-010 | The Package Datasheet shall require cable tray and conduit routing not to interfere with maintenance access for the transformer. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs. | Layout/interface review against the package interface matrix. |
| REQ-031-02-011 | The Package Datasheet shall identify source gaps for transformer construction class, impedance, vector group, tap range, BIL, cooling class, losses, noise rating, secondary containment outcome, protective relaying/coordination, and installation location as `TBD` instead of invented values. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search. | Gap review before vendor handoff. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, transformer spacing and installation, conductor sizing, and conduit support referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage class, MCC, grounding, cable, and raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable to transformer location, conduit sealing, and installation classification where hazardous/non-hazardous areas are defined. | Applicable; package location/classification TBD. |
| Transformer industry standards (e.g., CSA C88, IEEE C57 series) | Likely applicable to a 3 MVA 13.8 kV/600 V distribution transformer. | ASSUMPTION: likely applicable; specific clauses TBD pending vendor data and detailed engineering specification. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare datasheet identity fields to workbook row 33 and Gate 7 registers. | All fields match accepted source spelling and IDs, including tag TXP-8500-1 and ratings 3 MVA / 13.8 kV / 600 V / 347 V. |
| Interface completeness | Compare datasheet matrix to `INTERFACE_REGISTER.csv` rows for `PKG-031`. | All seven applicable interfaces are present (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports). |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, ratings, interfaces, and TBDs. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Package technical datasheet.
- Vendor engineering handoff basis.
- Package interface requirements matrix.
- Source-supported equipment and design criteria.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 33, applicable Gate 7 registers, and the DBM electrical source slices used for transformer/electrical design basis.
