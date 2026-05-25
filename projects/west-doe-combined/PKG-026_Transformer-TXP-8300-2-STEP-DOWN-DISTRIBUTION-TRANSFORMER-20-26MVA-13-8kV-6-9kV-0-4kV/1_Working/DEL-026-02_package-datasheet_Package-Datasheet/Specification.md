# Specification: DEL-026-02_package-datasheet

## Scope

This specification governs the EPC Integrator-authored Package Datasheet for `PKG-026`, the Transformer TXP-8300-2 - STEP DOWN DISTRIBUTION TRANSFORMER - 20/26MVA 13.8kV/6.9kV/0.4kV package. The datasheet is a mandatory Gate 5 EPC anchor deliverable and shall provide the technical handoff basis required for third-party vendor or discipline package engineering and design.

The package is a vendor-owned Electrical package under WBS 02. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, factory test reports, and final equipment selections are excluded from this EPC datasheet unless later provided as vendor data.
- Vector group, impedance, tap range, BIL, cooling class designation, loss values, sound levels, monitoring instrumentation, and tertiary 0.4 kV winding loading/grounding basis are `TBD` because the accessible source set does not provide confirmed package-specific values.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-026-02-001 | The Package Datasheet shall identify `PKG-026`, workbook row 28, WBS 02, CoA tracking number 26020-02-30-017, discipline Electrical, and package name "Transformer TXP-8300-2 - STEP DOWN DISTRIBUTION TRANSFORMER - 20/26MVA 13.8kV/6.9kV/0.4kV." Source: Workbook Packages row 28; `PACKAGE_REGISTER.csv`. | Datasheet identification review against workbook row and Gate 7 registers. |
| REQ-026-02-002 | The Package Datasheet shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-026`. | Responsibility statement review against Gate 7 package register. |
| REQ-026-02-003 | The Package Datasheet shall include the seven applicable interface facts: Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. Source: Workbook Packages row 28; `INTERFACE_REGISTER.csv`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-026`. |
| REQ-026-02-004 | The Package Datasheet shall state primary 13.8 kV and secondary 6.9 kV ratings consistent with the DBM electrical voltage/service basis (3-phase, 3-wire, 60 Hz, low-resistance grounded medium-voltage services). Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage and service table. | Source citation review of medium-voltage rating fields. |
| REQ-026-02-005 | The Package Datasheet shall preserve the secondary (6.9 kV) neutral grounding basis as a 100 A, 10 s neutral grounding resistor operating as a tripping system. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraph. | Grounding interface review. |
| REQ-026-02-006 | The Package Datasheet shall mark the tertiary 0.4 kV winding purpose, loading, vector group, and grounding basis as `TBD` because the DBM voltage/service table does not establish a facility 0.4 kV service class. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage and service table. | TBD/open-item review; carry as human-ruling item. |
| REQ-026-02-007 | The Package Datasheet shall capture CEC spacing, secondary containment review, two-point ground-grid connection, and ground-well provisions consistent with the DBM transformer/grounding basis without overstating package-specific values not present in source. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers and grounding paragraphs. | Electrical/civil interface review. |
| REQ-026-02-008 | The Package Datasheet shall align medium-voltage cable interface basis with project conventions: 13.8 kV TECK 15 kV / 133% insulation shielded on the primary side; 6.9 kV TECK 8 kV / 100% insulation shielded on the secondary side. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable types table. | Cable interface review against the package interface matrix. |
| REQ-026-02-009 | The Package Datasheet shall identify source gaps for cooling class, ambient basis, impedance, BIL, tap range, vector group, monitoring instrumentation, foundation type, exact physical location, and tertiary winding service as `TBD` instead of invented values. Source: `_REFERENCES.md`; accessible source set. | Gap review before vendor handoff. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Transformer spacing, grounding sizing, conduit support, and electrical installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations `TBD`. |
| Project electrical specifications | Voltage class, medium-voltage cable, grounding/resistor, and raceway basis referenced by DBM electrical section. | Applicable; document locations `TBD`. |
| Oil-filled transformer QAS line item | `ELC-QAS-000011-001` "Oil-Filled Transformers" recorded as 2 in the DBM QAS table; specific application to TXP-8300-2 is `ASSUMPTION` pending confirmation. | Applicable as ASSUMPTION; quantity allocation `TBD`. |
| Area classification standards | Applicable where the transformer pad/yard area classification is defined. | Applicable; package location/classification `TBD`. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare datasheet identity fields to workbook row 28 and Gate 7 registers. | All fields match accepted source spelling and IDs (including dual-rating and tri-voltage designation). |
| Interface completeness | Compare datasheet matrix to `INTERFACE_REGISTER.csv` rows for `PKG-026`. | All seven applicable interfaces (Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports) are present. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Grounding correctness | Compare 6.9 kV neutral grounding text to DBM grounding paragraph. | 100 A, 10 s NGR operating as a tripping system stated consistently. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, ratings, and `TBD` items. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Package technical datasheet.
- Vendor engineering handoff basis.
- Package interface requirements matrix.
- Source-supported equipment and design criteria.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 28, applicable Gate 7 registers, and the DBM electrical source slices used for transformer, grounding, cable, and electrical-building basis.
