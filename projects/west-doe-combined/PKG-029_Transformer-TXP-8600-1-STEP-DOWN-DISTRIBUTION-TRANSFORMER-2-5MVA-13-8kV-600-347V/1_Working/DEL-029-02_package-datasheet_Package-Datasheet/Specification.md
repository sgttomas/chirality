# Specification: DEL-029-02_package-datasheet

## Scope

This specification governs the EPC Integrator-authored Package Datasheet for `PKG-029`, the Transformer TXP-8600-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V package. The datasheet is a mandatory Gate 5 EPC anchor deliverable and shall provide the technical handoff basis required for third-party vendor or discipline package engineering and design.

The package is a vendor-owned Electrical package under WBS 01 (Deepcut 04-25 facility scope). The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, impedance values, loss values, sound levels, tap configurations, and final equipment selections are excluded from this EPC datasheet unless later provided as vendor data.
- Package-specific insulation/cooling type (oil-filled vs dry-type), secondary winding configuration (wye vs delta), secondary grounding method for a 600/347V secondary, installation location, source feeder, and connected load list are `TBD` because the accessible source set does not provide confirmed package-specific values for TXP-8600-1.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-029-02-001 | The Package Datasheet shall identify `PKG-029`, workbook row 31, WBS 01, CoA tracking number 26020-01-30-020, discipline Electrical, equipment tag TXP-8600-1, and package name "Transformer TXP-8600-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V." Source: Workbook Packages row 31; `PACKAGE_REGISTER.csv`. | Datasheet identification review against workbook row and Gate 7 registers. |
| REQ-029-02-002 | The Package Datasheet shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-029`. | Responsibility statement review against Gate 7 package register. |
| REQ-029-02-003 | The Package Datasheet shall include the seven applicable interface facts: Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. Source: Workbook Packages row 31; `INTERFACE_REGISTER.csv` rows for `PKG-029`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-029`. |
| REQ-029-02-004 | The Package Datasheet shall identify the primary voltage as 13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded, consistent with the DBM medium-voltage backbone basis. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, System Voltages table. | Source citation review. |
| REQ-029-02-005 | The Package Datasheet shall carry the secondary voltage from the package title as 600 V line-to-line / 347 V line-to-neutral and shall mark the secondary winding configuration (wye vs delta) and the secondary grounding method as `TBD` until reconciled with the DBM low-voltage basis (600 V, 3-wire, high-resistance grounded). See `HRR-029-02-001`. Source: `PACKAGE_REGISTER.csv` row `PKG-029` package name; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, System Voltages and grounding paragraphs. | Source-conflict review; cross-reference to Guidance Conflict Table. |
| REQ-029-02-006 | The Package Datasheet shall mark insulation/cooling type (oil-filled vs dry-type), foundation type, secondary containment requirement, and installation location as `TBD` until source or vendor data resolves them. The DBM paragraph on transformers shall be cited for the spacing, base, and containment basis. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Transformers paragraph. | TBD/open-item review. |
| REQ-029-02-007 | The Package Datasheet shall require grounding/bonding consistent with the DBM facility grounding basis: two-point ground-grid connection for major electrical equipment, separate copper ground conductor for distribution transformers sized per CEC, and ground wells at power transformers for maintenance/testing. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs. | Electrical interface review. |
| REQ-029-02-008 | The Package Datasheet shall require cable tray and conduit routing to preserve maintenance access. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs. | Layout/interface review against the package interface matrix. |
| REQ-029-02-009 | The Package Datasheet shall identify source gaps for nameplate rating corroboration, secondary configuration, impedance, taps, losses, sound level, accessories, protection, connected loads, source feeder, and physical location as `TBD` instead of invented values. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search (no PKG-029 match located). | Gap review before vendor handoff. |
| REQ-029-02-010 | The Package Datasheet shall be consistent with the Gate 7 artifact set for this deliverable: package technical datasheet, vendor engineering handoff basis, package interface requirements matrix, and interface fact evidence for each of the seven `PKG-029` interface rows. Source: `ARTIFACT_REGISTER.csv` rows for `DEL-029-02_package-datasheet`. | Artifact-coverage review against Gate 7 artifact register. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Transformer spacing, foundation/bonding, conductor sizing, grounding installations referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Transformer industry standards (CSA C88 / IEEE C57 series — ASSUMPTION) | Distribution transformer rating, testing, and construction. The accessible source set does not name specific transformer construction standards; standard selection is TBD. | ASSUMPTION until source confirms. |
| Area classification standards | Applicable to electrical equipment, conduit sealing, and installation classification where hazardous/non-hazardous areas are defined. | Applicable; package location/classification TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare datasheet identity fields to workbook row 31 and Gate 7 registers. | All fields (PKG-029, TXP-8600-1, WBS 01, CoA 26020-01-30-020, package name) match accepted source spelling and IDs. |
| Interface completeness | Compare datasheet matrix to `INTERFACE_REGISTER.csv` rows for `PKG-029`. | Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports are present. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Voltage-basis consistency | Reconcile package-title secondary voltage notation "600/347V" against DBM low-voltage service basis. | Discrepancy is captured in Guidance Conflict Table (HRR-029-02-001) and is not silently resolved. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Package technical datasheet.
- Vendor engineering handoff basis.
- Package interface requirements matrix.
- Source-supported equipment and design criteria.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 31, applicable Gate 7 registers, and the DBM electrical source slices used for transformer, voltage, grounding, and routing design basis.
