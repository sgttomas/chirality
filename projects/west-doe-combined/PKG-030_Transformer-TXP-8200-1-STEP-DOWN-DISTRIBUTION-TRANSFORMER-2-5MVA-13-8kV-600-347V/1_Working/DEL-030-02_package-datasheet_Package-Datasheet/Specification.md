# Specification: DEL-030-02_package-datasheet

## Scope

This specification governs the EPC Integrator-authored Package Datasheet for `PKG-030`, the Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V package. The datasheet is a mandatory Gate 5 EPC anchor deliverable and shall provide the technical handoff basis required for third-party vendor or discipline package engineering and design.

The package is a vendor-owned Electrical package under WBS 01. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, and final equipment selections are excluded from this EPC datasheet unless later provided as vendor data.
- Detailed transformer nameplate parameters (cooling class, impedance, BIL, tap range, vector group, winding material, temperature rise), final construction type (oil-filled vs. dry-type), secondary containment sizing, primary/secondary cable schedule, and protection/relay settings are `TBD` because the accessible source set does not provide confirmed package-specific values for TXP-8200-1.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-030-02-001 | The Package Datasheet shall identify `PKG-030`, workbook row 32, WBS 01, CoA tracking number 26020-01-30-021, discipline Electrical, and package name "Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V." Source: Workbook Packages row 32; `PACKAGE_REGISTER.csv`. | Datasheet identification review against workbook row and Gate 7 registers. |
| REQ-030-02-002 | The Package Datasheet shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-030`. | Responsibility statement review against Gate 7 package register. |
| REQ-030-02-003 | The Package Datasheet shall include the seven applicable interface facts: Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. Source: Workbook Packages row 32; `INTERFACE_REGISTER.csv`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-030`. |
| REQ-030-02-004 | The Package Datasheet shall state primary service basis as 13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded and secondary service basis as 600 V, 3 phase, 3 wire, 60 Hz, high-resistance grounded with 5 A continuous resistor, per the DBM System Voltages table. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, System Voltages table. | Source citation review against DBM. |
| REQ-030-02-005 | The Package Datasheet shall require transformer foundations to be designed as precast concrete bearing foundations / structural-steel transformer bases, with CEC spacing for large oil-filled transformers respected where applicable, and shall require secondary containment requirements to be reviewed. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Foundations table and Transformers paragraph. | Foundations / containment design review against DBM. |
| REQ-030-02-006 | The Package Datasheet shall require grounding consistent with the DBM: two-point connection to the ground grid for major electrical equipment, ground well at the transformer with bolted ground connections for testing, separate copper ground conductor to ground sized per CEC for distribution transformers, and 600 V secondary high-resistance grounding using a 5 A continuous resistor. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs. | Grounding-scheme review against DBM. |
| REQ-030-02-007 | The Package Datasheet shall require maintenance-access preservation: cable tray and conduit routing shall not interfere with maintenance; CEC spacing for the transformer shall be confirmed; ground wells shall be accessible. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Transformers and cable-tray paragraphs. | Layout/interface review against the package interface matrix. |
| REQ-030-02-008 | The Package Datasheet shall require the secondary cable from the 600 V transformer secondary to plant 600 V MCCs to use ACWU cable with single-conductor cables avoided. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable schedule table. | Cable-schedule review. |
| REQ-030-02-009 | The Package Datasheet shall mark transformer nameplate parameters (cooling class, impedance, BIL, tap range, vector group, winding material, temperature rise), construction type (oil-filled vs. dry-type), final installation location, secondary containment dimensions, primary/secondary cable schedule, and protection-relay settings as `TBD` where not source-supported, rather than inventing values. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search; vendor data not available. | Gap review before vendor handoff. |
| REQ-030-02-010 | The Package Datasheet shall preserve all seven workbook interface facts as datasheet evidence rather than as separate deliverables, consistent with the Gate 7 artifact register treatment for `DEL-030-02_package-datasheet`. Source: `ARTIFACT_REGISTER.csv`, rows for `DEL-030-02_package-datasheet`. | Artifact-register cross-check. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical equipment spacing (large oil-filled transformers), grounding conductor sizing, and electrical installation basis referenced by DBM. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable to the transformer installation area, conduit sealing, and area-classification interface where hazardous/non-hazardous areas are defined. | Applicable; package location/classification TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare datasheet identity fields to workbook row 32 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare datasheet matrix to `INTERFACE_REGISTER.csv` rows for `PKG-030`. | All seven applicable interfaces are present. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, voltages, interfaces, and TBDs. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Package technical datasheet.
- Vendor engineering handoff basis.
- Package interface requirements matrix.
- Source-supported equipment and design criteria.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 32, applicable Gate 7 registers, and the DBM-Deepcut electrical source slices used for the voltage, transformer, grounding, foundation, and cable basis.
