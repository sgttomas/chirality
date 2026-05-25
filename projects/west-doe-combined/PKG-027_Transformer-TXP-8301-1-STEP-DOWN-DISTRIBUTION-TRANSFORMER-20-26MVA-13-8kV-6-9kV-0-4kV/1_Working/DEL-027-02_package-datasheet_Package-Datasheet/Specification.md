# Specification: DEL-027-02_package-datasheet

## Scope

This specification governs the EPC Integrator-authored Package Datasheet for `PKG-027`, the Transformer TXP-8301-1 STEP DOWN DISTRIBUTION TRANSFORMER, 20/26 MVA, 13.8 kV / 6.9 kV / 0.4 kV. The datasheet is a mandatory Gate 5 EPC anchor deliverable and shall provide the technical handoff basis required for third-party vendor or discipline package engineering and design.

The package is a vendor-owned Electrical package under WBS 01 (CoA 26020-01-30-018). The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, type tests, routine tests, and final equipment selections are excluded from this EPC datasheet unless later issued as vendor data.
- Package-specific impedance, BIL, vector group, tap range, sound level, temperature rise, accessories, cooling stage interpretation (e.g., ONAN/ONAF), insulating medium, exact installation location, and foundation design are `TBD` because the accessible source set does not provide confirmed package-specific values.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-027-02-001 | The Package Datasheet shall identify `PKG-027`, workbook row 29, WBS 01, CoA tracking number 26020-01-30-018, discipline Electrical, and package name "Transformer TXP-8301-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 20/26MVA 13.8kV/6.9kV/0.4kV." Source: Workbook Packages row 29; `PACKAGE_REGISTER.csv`. | Datasheet identification review against workbook row and Gate 7 registers. |
| REQ-027-02-002 | The Package Datasheet shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-027`. | Responsibility statement review against Gate 7 package register. |
| REQ-027-02-003 | The Package Datasheet shall include the seven applicable interface facts for PKG-027: Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. Source: Workbook Packages row 29; `INTERFACE_REGISTER.csv`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-027`. |
| REQ-027-02-004 | The Package Datasheet shall identify primary voltage as 13.8 kV, 3 phase, 3 wire, 60 Hz, LRG and secondary voltage as 6.9 kV, 3 phase, 3 wire, 60 Hz, LRG, consistent with the DBM electrical service table. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage and service table. | Source citation review. |
| REQ-027-02-005 | The Package Datasheet shall require that the 6.9 kV secondary neutral be grounded through a 100 A, 10 s neutral grounding resistor operating as a tripping system. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding-resistor paragraph. | Cross-check against DBM grounding paragraph. |
| REQ-027-02-006 | The Package Datasheet shall require that the package be coordinated with the facility ground grid including two-point connection of major electrical equipment, provision of a ground well at the power transformer, and separate copper ground conductor sized per CEC for distribution transformers. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs. | Grounding interface review. |
| REQ-027-02-007 | The Package Datasheet shall require installation in accordance with CEC spacing for large oil-filled transformers, generally on structural steel transformer bases over precast concrete bearing foundations, with secondary containment reviewed and selection biased to avoid or limit containment where practical. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformer installation and foundations paragraphs. | Civil/structural and electrical installation review. |
| REQ-027-02-008 | The Package Datasheet shall require MV cable basis: 13.8 kV primary side using 3-conductor copper TECK cable rated 15 kV with 133 percent shielded insulation; 6.9 kV secondary side using 3-conductor copper TECK cable rated 8 kV with 100 percent shielded insulation. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MV cable table. | MV cable specification review. |
| REQ-027-02-009 | The Package Datasheet shall require that cable tray and conduit routing for primary feeders, secondary feeders, grounding conductors, control cabling, and communications cabling shall not interfere with transformer maintenance access. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs; `INTERFACE_REGISTER.csv` PKG-027 Maintenance Access. | Layout/interface review against the package interface matrix. |
| REQ-027-02-010 | The Package Datasheet shall identify source gaps for transformer impedance, BIL, vector group, tap range, sound level, temperature rise, insulating medium, accessories, cooling-stage interpretation, foundation design, and exact installation location as `TBD` instead of invented values. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search (no accessible match copied). | Gap review before vendor handoff. |
| REQ-027-02-011 | The Package Datasheet shall represent the 0.4 kV tertiary/auxiliary voltage as carried from the package name with service basis and connected load marked `TBD`, because the DBM electrical service table does not enumerate a 0.4 kV distribution service. Source: Workbook Packages row 29; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage and service table. | TBD/open-item review; see Guidance Conflict Table. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Transformer spacing, grounding, conduit support, and electrical installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable to electrical equipment, conduit sealing, and installation classification where hazardous/non-hazardous areas are defined. | Applicable; package location/classification TBD. |
| Transformer industry standards (e.g., IEEE C57 / IEC 60076 family) | Likely applicable to transformer type tests, routine tests, ratings, and accessories for a 20/26 MVA oil-filled MV transformer. | ASSUMPTION: applicable per industry convention; not cited in accessible DBM slices; clauses TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare datasheet identity fields to workbook row 29 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare datasheet matrix to `INTERFACE_REGISTER.csv` rows for `PKG-027`. | All seven applicable interfaces are present (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports). |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| Grounding scheme | Confirm 6.9 kV secondary grounding requirement matches DBM grounding-resistor paragraph (100 A, 10 s, tripping). | Datasheet language matches DBM. |
| MV cable basis | Confirm primary and secondary cable specifications match DBM MV cable table. | Datasheet language matches DBM. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, ratings, interfaces, and `TBD` items. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts (per `ARTIFACT_REGISTER.csv` for `DEL-027-02_package-datasheet`):

- Package technical datasheet (`ART-8487DC3F33`).
- Vendor engineering handoff basis (`ART-98B0F520D0`).
- Package interface requirements matrix (`ART-19B0A38DDB`).
- Interface fact evidence rows for Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 29, applicable Gate 7 registers, and the DBM electrical source slices used for voltage basis, grounding, transformer installation, and MV cable basis.
