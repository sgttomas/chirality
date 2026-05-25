# Specification: DEL-037-02_package-datasheet

## Scope

This specification governs the EPC Integrator-authored Package Datasheet for `PKG-037`, the 5kV SWITCHGEAR ELECTRICAL BUILDING (880-1) package. The datasheet is a mandatory Gate 5 EPC anchor deliverable and shall provide the technical handoff basis required for third-party vendor or discipline package engineering and design.

The package is a vendor-owned Electrical package under WBS 01, CoA tracking number 26020-01-30-028. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package (the prefabricated electrical building and its installed electrical equipment). The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, and final equipment selections are excluded from this EPC datasheet unless later provided as vendor data.
- Confirmed bus voltage rating for the "5kV" identifier, building `880-1` siting coordinates, switchgear lineup, MCC lineup, UPS lineup, transformer/distribution lineup, control and network rack content, and detailed bill of material are `TBD` because the accessible source set does not establish PKG-037-specific values.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-037-02-001 | The Package Datasheet shall identify `PKG-037`, workbook row 39, WBS 01, CoA tracking number 26020-01-30-028, discipline Electrical, and package name "5kV SWITCHGEAR ELECTRICAL BUILDING (880-1)" exactly as carried in `PACKAGE_REGISTER.csv`. Source: Workbook Packages row 39; `PACKAGE_REGISTER.csv`. | Datasheet identification review against workbook row and Gate 7 registers. |
| REQ-037-02-002 | The Package Datasheet shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-037`. | Responsibility statement review against Gate 7 package register. |
| REQ-037-02-003 | The Package Datasheet shall include all twelve applicable interface facts: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. Source: Workbook Packages row 39; `INTERFACE_REGISTER.csv`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-037`. |
| REQ-037-02-004 | The Package Datasheet shall represent the building as a prefabricated, shop-fabricated modular electrical building, located in a general purpose area, designed for bottom entry of cables, elevated and installed on piles, with HVAC sized as an n + 1 system. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraphs and electrical buildings list. | Source citation review against DBM Electrical Buildings section. |
| REQ-037-02-005 | The Package Datasheet shall identify the building's switchgear voltage class as `TBD` until reconciled with the accepted DBM voltage classes (13.8 kV, 4.16 kV, 600 V) or vendor data; the workbook name string "5kV" shall not be asserted as a confirmed bus voltage. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltage/service and medium-voltage cable tables. | TBD / source-citation review; conflict carried in Guidance Conflict Table. |
| REQ-037-02-006 | The Package Datasheet shall identify the building identifier `880-1` as `TBD` against the DBM Electrical Buildings list (which enumerates `810-1`, `820-1`, `830-1`, `840-1`, `850-1`, `860-1`) until reconciled by detailed design or by an accepted updated source. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings list. | TBD / source-citation review; conflict carried in Guidance Conflict Table. |
| REQ-037-02-007 | The Package Datasheet shall require grounding consistent with DBM: major electrical equipment connected to the ground grid at two points; ground wells at electrical buildings; compression-type ground connections; above-grade green insulated ground wires in PVC conduit where mechanical protection is required. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs. | Electrical interface review. |
| REQ-037-02-008 | The Package Datasheet shall require TECK and ACIC cabling for power, EMT conduit for adjacent panel runs, bottom-entry cable arrangement, and cable tray/conduit routing that does not interfere with maintenance access. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings, cable tray, and conduit paragraphs. | Layout/interface review against the package interface matrix. |
| REQ-037-02-009 | The Package Datasheet shall require building doors sized for, or include removable transom sections to allow, removal of the largest installed equipment, and shall provide an outdoor GFI receptacle for exterior maintenance. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph. | Maintenance access verification. |
| REQ-037-02-010 | The Package Datasheet shall identify the following items as `TBD` instead of invented values: confirmed bus voltage rating, building siting coordinates, switchgear lineup, MCC lineup, UPS lineup, transformer/distribution lineup, network/PLC content, and any quantity, rating, or BoM information not supported by an accessible source slice. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search. | Gap review before vendor handoff. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, conduit support, and electrical installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/switchgear/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable to building siting; electrical buildings shall be located in general purpose (unclassified) areas. | Applicable; package siting confirmation TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare datasheet identity fields to workbook row 39 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare datasheet matrix to `INTERFACE_REGISTER.csv` rows for `PKG-037`. | All twelve applicable interfaces are present. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| Voltage and building identifier | Confirm "5kV" and `880-1` are carried as identity but flagged for reconciliation against DBM voltage classes and electrical buildings list. | Items appear in Conflict Table; no unsupported numerical bus voltage is asserted. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Package technical datasheet.
- Vendor engineering handoff basis.
- Package interface requirements matrix.
- Source-supported equipment and design criteria.
- Interface fact evidence rows for the twelve applicable interfaces.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 39, applicable Gate 7 registers, and the DBM electrical source slices used for the electrical building, grounding, cable tray, conduit, voltage, and area classification basis.
