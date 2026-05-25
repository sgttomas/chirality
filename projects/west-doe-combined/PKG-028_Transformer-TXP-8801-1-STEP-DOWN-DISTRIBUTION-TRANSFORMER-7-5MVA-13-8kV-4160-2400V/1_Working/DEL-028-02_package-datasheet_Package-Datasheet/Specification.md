# Specification: DEL-028-02_package-datasheet

## Scope

This specification governs the EPC Integrator-authored Package Datasheet for `PKG-028`, the Transformer TXP-8801-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 7.5MVA 13.8kV/4160/2400V package. The datasheet is a mandatory Gate 5 EPC anchor deliverable and shall provide the technical handoff basis required for third-party vendor or discipline package engineering and design.

The package is a vendor-owned Electrical package under WBS 01. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, and final equipment selections are excluded from this EPC datasheet unless later provided as vendor data.
- Package-specific transformer construction details (oil-filled vs dry-type, cooling class, BIL, impedance, tap range, vector group, neutral grounding scheme, bushings, surge arresters, monitoring scope, and installation location) are `TBD` because the accessible source set does not provide confirmed package-specific values.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-028-02-001 | The Package Datasheet shall identify `PKG-028`, workbook row 30, WBS 01, CoA tracking number 26020-01-30-019, discipline Electrical, and package name "Transformer TXP-8801-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 7.5MVA 13.8kV/4160/2400V." Source: Workbook Packages row 30; `PACKAGE_REGISTER.csv`. | Identification review against workbook row and Gate 7 registers. |
| REQ-028-02-002 | The Package Datasheet shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-028`. | Responsibility statement review against Gate 7 package register. |
| REQ-028-02-003 | The Package Datasheet shall include the seven applicable interface facts: Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. Source: Workbook Packages row 30; `INTERFACE_REGISTER.csv`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-028`. |
| REQ-028-02-004 | The Package Datasheet shall require the primary 13.8 kV side to align with the facility medium-voltage service basis: 13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded, fed radially from the 13.8 kV switchgear. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical system overview and voltage/service table. | Source citation review. |
| REQ-028-02-005 | The Package Datasheet shall require 13.8 kV primary cable to be 3-conductor copper TECK rated 15 kV with 133% insulation, shielded, consistent with the DBM medium-voltage cable basis. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable table. | Cable specification review. |
| REQ-028-02-006 | The Package Datasheet shall require grounding to satisfy the facility basis: major electrical equipment connected to the ground grid at two points, ground wells provided at power transformers for maintenance and operational testing, and a separate copper ground conductor sized per CEC for the distribution transformer. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs. | Grounding/bonding interface review. |
| REQ-028-02-007 | The Package Datasheet shall require, if oil-filled, CEC-compliant spacing and a documented review of secondary containment, with selection preferring designs that avoid or limit containment where practical. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Transformers subsection. | Source citation review; containment status marked `TBD` if construction type is unconfirmed. |
| REQ-028-02-008 | The Package Datasheet shall require foundations consistent with the DBM convention (precast concrete bearing foundations for transformers), with package-specific loading, anchorage, and containment features captured as `TBD`. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, foundations table. | Civil/structural interface review. |
| REQ-028-02-009 | The Package Datasheet shall preserve the secondary voltage description (4160/2400 V) carried by the workbook title and shall mark winding configuration, neutral treatment, impedance, BIL, cooling class, vector group, tap range, monitoring scope, bushings, and surge arresters as `TBD` unless a source-supported package-specific basis is established. Source: `_REFERENCES.md`; DBM source gap. | TBD/open-item review prior to vendor handoff. |
| REQ-028-02-010 | The Package Datasheet shall identify source gaps for installation location, physical orientation, oil/coolant volume, sound power, transport limits, and protective relaying coordination as `TBD` instead of invented values. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search. | Gap review before vendor handoff. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Distribution transformer installation, grounding, spacing for oil-filled equipment, and conduit/cable installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage levels, switchgear, cable, raceway, and grounding basis referenced by DBM electrical section. | Applicable; document locations TBD. |
| Area classification standards | Applicable where transformer location and surrounding equipment classification require it. | Applicable; package location/classification TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare datasheet identity fields to workbook row 30 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare datasheet matrix to `INTERFACE_REGISTER.csv` rows for `PKG-028`. | All seven interface facts (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) are present. |
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

The deliverable shall cite the Gate 7 snapshot, workbook row 30, applicable Gate 7 registers, and the DBM electrical source slices used as design basis.
