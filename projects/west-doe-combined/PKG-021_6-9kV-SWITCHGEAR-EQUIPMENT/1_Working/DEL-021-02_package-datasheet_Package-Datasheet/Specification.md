# Specification: DEL-021-02_package-datasheet

## Scope

This specification governs the EPC Integrator-authored Package Datasheet for `PKG-021`, the 6.9kV SWITCHGEAR EQUIPMENT package. The datasheet is a mandatory Gate 5 EPC anchor deliverable and shall provide the technical handoff basis required for third-party vendor or discipline package engineering and design.

The package is a vendor-owned Electrical package under WBS 01 (CoA 26020-01-30-012). The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, and final equipment selections are excluded from this EPC datasheet unless later provided as vendor data.
- Package-specific bus current, short-circuit withstand, breaker continuous/interrupting ratings, cubicle and lineup configuration, arc-resistance class, protective relay schemes/settings, control-power feeder origin/sizing, and installation location are `TBD` because the accessible source set does not provide confirmed package-specific values.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-021-02-001 | The Package Datasheet shall identify `PKG-021`, workbook row 23, WBS 01, CoA tracking number 26020-01-30-012, discipline Electrical, and package name "6.9kV SWITCHGEAR EQUIPMENT." Source: Workbook Packages row 23; `PACKAGE_REGISTER.csv`. | Datasheet identification review against workbook row and Gate 7 registers. |
| REQ-021-02-002 | The Package Datasheet shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-021`. | Responsibility statement review against Gate 7 package register. |
| REQ-021-02-003 | The Package Datasheet shall include the six applicable interface facts: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. Source: Workbook Packages row 23; `INTERFACE_REGISTER.csv`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-021`. |
| REQ-021-02-004 | The Package Datasheet shall identify the 6.9 kV facility service basis as 6.9 kV, 3-phase, 3-wire, 60 Hz, low-resistance grounded, and shall reference the DBM stated application to inverter-drive motors 5,500 hp and above. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MV voltage/service table. | Source citation review. |
| REQ-021-02-005 | The Package Datasheet shall capture the facility neutral-grounding basis (100 A, 10 s NGR per 6.9 kV transformer, tripping system) as an interface design input to switchgear protection and shall not assign unsupported package-specific relay or coordination settings. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraph. | TBD/open-item review. |
| REQ-021-02-006 | The Package Datasheet shall require switchgear cable terminations to accommodate the facility 6.9 kV cable basis: three-conductor copper TECK cable rated 8 kV with 100 percent insulation, shielded. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MV cable table. | Cable-termination interface review. |
| REQ-021-02-007 | The Package Datasheet shall require control power (120 VAC and/or 125 VDC) for breaker control and protective relaying to be coordinated with facility UPS services. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, UPS services table. | Control-power interface review against UPS packages. |
| REQ-021-02-008 | The Package Datasheet shall require communications hooks (Ethernet to plant PLC central control panel) for switchgear protective relays and metering data acquisition consistent with the 6.9 kV MCC pattern described in the DBM. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 6.9 kV MCC paragraph. | Communications interface review. |
| REQ-021-02-009 | The Package Datasheet shall require cable tray and conduit routing to preserve maintenance access. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs. | Layout/interface review against the package interface matrix. |
| REQ-021-02-010 | The Package Datasheet shall identify source gaps (bus/breaker ratings, short-circuit withstand, arc-resistance class, relay schemes/settings, lineup configuration, physical location, support requirements, arc-flash/coordination study values) as `TBD` instead of invented values. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search. | Gap review before vendor handoff. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, conduit support, and installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| MV switchgear product standards (e.g., IEEE/IEC/CSA series applicable to indoor metal-clad medium-voltage switchgear) | `ASSUMPTION: likely applicable` to 6.9 kV switchgear; specific standards/editions are not enumerated in accessible source. | Treat as `ASSUMPTION` pending source-supported confirmation. |
| Area classification standards | Applicable to electrical equipment, conduit sealing, and installation classification where hazardous/non-hazardous areas are defined. | Applicable; package location/classification TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare datasheet identity fields to workbook row 23 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare datasheet matrix to `INTERFACE_REGISTER.csv` rows for `PKG-021`. | Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports are present. |
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

The deliverable shall cite the Gate 7 snapshot, workbook row 23, applicable Gate 7 registers, and the DBM electrical source slices used for facility MV electrical, grounding, MV cable, UPS service basis, electrical buildings, 6.9 kV MCC, and cable tray/conduit routing.
