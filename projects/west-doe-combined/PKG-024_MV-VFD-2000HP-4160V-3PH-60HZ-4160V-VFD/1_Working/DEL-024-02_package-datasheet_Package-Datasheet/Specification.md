# Specification: DEL-024-02_package-datasheet

## Scope

This specification governs the EPC Integrator-authored Package Datasheet for `PKG-024`, the "MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD" package. The datasheet is a mandatory Gate 5 EPC anchor deliverable and shall provide the technical handoff basis required for third-party vendor or discipline package engineering and design.

The package is a vendor-owned Electrical package under WBS 01. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, and final equipment selections are excluded from this EPC datasheet unless later provided as vendor data.
- Package-specific MV VFD topology (cell count, isolation transformer, output filter, cooling configuration), driven-motor tag/service, harmonic mitigation, installation location, and area-classification assignment are `TBD` because the accessible source set does not provide confirmed package-specific values for PKG-024.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-024-02-001 | The Package Datasheet shall identify `PKG-024`, workbook row 26, WBS 01, CoA tracking number 26020-01-30-015, discipline Electrical, and package name "MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD." Source: Workbook Packages row 26; `PACKAGE_REGISTER.csv`. | Datasheet identification review against workbook row and Gate 7 registers. |
| REQ-024-02-002 | The Package Datasheet shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-024`. | Responsibility statement review against Gate 7 package register. |
| REQ-024-02-003 | The Package Datasheet shall include the six applicable interface facts: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. Source: Workbook Packages row 26; `INTERFACE_REGISTER.csv`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-024`. |
| REQ-024-02-004 | The Package Datasheet shall identify the MV supply basis as facility 4.160 kV, three-phase, three-wire, 60 Hz, low-resistance grounded service serving inverter-drive motors rated 250 hp to 5,500 hp, and shall not assign unsupported package-specific ratings or topology. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MV services table. | Source citation review; unsupported values remain `TBD`. |
| REQ-024-02-005 | The Package Datasheet shall preserve 4.16 kV MV VFD/soft-starter selection, harmonic mitigation, reactive-power treatment, and isolation-transformer arrangement as `TBD` pending detailed electrical studies and vendor data. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 4.16 kV MCC paragraph; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160V MCC paragraph. | TBD/open-item review. |
| REQ-024-02-006 | The Package Datasheet shall require VFD-fed motors located in Zone 2 areas to be marked accordingly and supplied with a temperature code lower than the temperature code specified on the area-classification drawing or fugitive-emissions study. Package-area assignment shall be marked `TBD`. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, motor/area-classification paragraph. | Area-classification cross-check against detailed design when issued. |
| REQ-024-02-007 | The Package Datasheet shall capture grounding/bonding requirements applicable to MV equipment without overstating package-specific grounding details not present in source (two-point grounding for major electrical equipment; separate copper ground conductors per CEC sizing for transformers, panelboards, and three-phase motors larger than 100 hp). Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs. | Electrical interface review. |
| REQ-024-02-008 | The Package Datasheet shall reflect the facility MV cable basis (4.160 kV TECK cable rated 5 kV with 100% insulation; LV power cable fed from VFDs is copper TECK) for tie-in cable selection, while leaving package-internal cable selection to the vendor. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable schedule. | Cable schedule review at interface boundary. |
| REQ-024-02-009 | The Package Datasheet shall require cable tray and conduit routing into and within the package footprint to preserve maintenance access. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs. | Layout/interface review against the package interface matrix. |
| REQ-024-02-010 | The Package Datasheet shall identify source gaps for driven-motor identity/service, MV VFD topology, output filter, cooling, communications protocol, installation location, and support requirements as `TBD` instead of invented values. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search. | Gap review before vendor handoff. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, conduit support, MV installation, and cable basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations `TBD`. |
| NEMA MG1 / inverter-duty motor practice | Inverter-duty motor basis referenced by DBM for 4160 V process inverter-driven motors. | Applicable to driven motor; package-internal selection is vendor scope. Clause locations `TBD`. |
| Project electrical specifications | MV voltage/MCC/VFD/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location `TBD`. |
| Area classification standards | Applicable to electrical equipment, conduit sealing, and installation classification where hazardous/non-hazardous areas are defined; relevant to VFD-fed motors in Zone 2. | Applicable; package location/classification `TBD`. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare datasheet identity fields to workbook row 26 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare datasheet matrix to `INTERFACE_REGISTER.csv` rows for `PKG-024`. | Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports are present. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and `TBD`s. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Package technical datasheet.
- Vendor engineering handoff basis.
- Package interface requirements matrix.
- Source-supported equipment and design criteria.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 26, applicable Gate 7 registers, and the DBM electrical source slices used for MV VFD/MV service/electrical building/cable/grounding basis.
