# Specification: DEL-023-02_package-datasheet

## Scope

This specification governs the EPC Integrator-authored Package Datasheet for `PKG-023`, the "MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD" package. The datasheet is a mandatory Gate 5 EPC anchor deliverable and shall provide the technical handoff basis required for third-party vendor or discipline package engineering and design.

The package is a vendor-owned Electrical package under WBS 01. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, and final equipment selections are excluded from this EPC datasheet unless later provided as vendor data.
- Identification of the specific driven equipment (load served) and the final VFD topology, harmonic mitigation, isolation transformer, bypass, and cooling configuration are `TBD` because the accessible source set defers 4.16 kV VFD and soft-starter requirements and does not identify a 1500 hp / 4160 V driven service.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-023-02-001 | The Package Datasheet shall identify `PKG-023`, workbook row 25, WBS 01, CoA tracking number 26020-01-30-014, discipline Electrical, and package name "MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD." Source: Workbook Packages row 25; `PACKAGE_REGISTER.csv`. | Datasheet identification review against workbook row and Gate 7 registers. |
| REQ-023-02-002 | The Package Datasheet shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-023`. | Responsibility statement review against Gate 7 package register. |
| REQ-023-02-003 | The Package Datasheet shall include the six applicable interface facts: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 25; `INTERFACE_REGISTER.csv`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-023`. |
| REQ-023-02-004 | The Package Datasheet shall preserve the nominal nameplate basis from the package name (1500 hp, 4160 V, 3-phase, 60 Hz, 4160 V VFD output) and shall mark the driven service, final ratings, and continuous/intermittent duty as `TBD` where accessible source does not confirm them. Source: Workbook Packages row 25; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Prime Mover and Major Driver Inventory. | Source citation review; unsupported values remain `TBD`. |
| REQ-023-02-005 | The Package Datasheet shall reflect the DBM position that VFD and soft-starter requirements for 4.16 kV motors are `TBD`, and shall not invent VFD topology, transformer arrangement, cooling configuration, harmonic mitigation, or bypass requirements unsupported by source. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 4.16 kV motor control center and 4.16 kV motor starting paragraphs. | TBD/open-item review. |
| REQ-023-02-006 | The Package Datasheet shall require VFD-fed motors located in Zone 2 areas to be marked accordingly and supplied with a temperature code lower than the area-classification temperature code, applied to the driven motor served by this package as confirmed at detailed design. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, motor selection paragraph. | Electrical/area-classification review. |
| REQ-023-02-007 | The Package Datasheet shall require coordination with facility grounding/bonding basis (two-point connection to ground grid for major electrical equipment; separate copper ground conductors per CEC for distribution transformers, panelboards, and three-phase motors larger than 100 hp) without overstating package-specific conductor sizing. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs. | Grounding interface review. |
| REQ-023-02-008 | The Package Datasheet shall require cable tray and conduit routing to preserve maintenance access; the MV cable type between the VFD output and the driven motor remains `TBD` at this datasheet stage. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable schedule and cable tray/conduit paragraphs. | Layout/interface review against the package interface matrix. |
| REQ-023-02-009 | The Package Datasheet shall identify source gaps for driven equipment service, VFD topology, isolation transformer, harmonic mitigation, bypass, cooling, building/room assignment, and supports as `TBD` instead of invented values. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search. | Gap review before vendor handoff. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Grounding sizing, conduit support, and electrical installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| NEMA MG 1 | Referenced by DBM for medium-voltage motor testing/labeling on related compressor drivers; applicability to the driven motor served by PKG-023 is `TBD` pending driven-equipment identification. | Conditionally applicable; package location TBD. |
| Project electrical specifications | Voltage class assignment, MCC, grounding, cable/raceway, and VFD application basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable to electrical equipment and the driven motor where the installation is in a Zone-classified area. | Applicable; package location/classification TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare datasheet identity fields to workbook row 25 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare datasheet matrix to `INTERFACE_REGISTER.csv` rows for `PKG-023`. | Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports are present. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |
| TBD discipline | Confirm 4.16 kV VFD topology, driven service identification, and cooling/transformer/bypass are not invented. | DBM-supported deferral language preserved. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Package technical datasheet.
- Vendor engineering handoff basis.
- Package interface requirements matrix.
- Source-supported equipment and design criteria.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 25, applicable Gate 7 registers, and the DBM electrical source slices used for MV VFD design basis.
