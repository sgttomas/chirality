# Specification: DEL-025-03_construction-work-package

## Scope

This specification governs the EPC Integrator-authored Construction Work Package for `PKG-025`, the "MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD" package. The Construction Work Package is a mandatory Gate 5 EPC anchor deliverable and shall describe how the package is physically installed, built, inspected, turned over, and tied into the larger facility systems.

The package is a vendor-owned Electrical package under WBS 01. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration, and is the construction-facing author of this deliverable.

Exclusions:

- Vendor detailed engineering, factory fabrication, factory acceptance testing, and certified-equipment selections are excluded from the EPC Construction Work Package except as inputs that the construction scope must accept and install.
- Package-specific lift plans, ITPs, hold points, MV pre-energization tests, foundation/support detail, feeder/cable sizing, ground-conductor sizing, conduit routing, termination details, building/room assignment, network port and PRP/DLR assignments, control schematics, and turnover-checklist line items are `TBD` because the accessible source set does not provide confirmed package-specific values.
- Vendor document review and final EPC package acceptance are out of scope here and are carried by `DEL-025-05` (Vendor Document Turnover Package) and `DEL-025-06` (EPC Vendor Package Review and Acceptance).

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-025-03-001 | The Construction Work Package shall identify `PKG-025`, workbook row 27, WBS 01, CoA tracking number 26020-01-30-016, discipline Electrical, and package name "MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD." Source: Workbook Packages row 27; `PACKAGE_REGISTER.csv`. | Identity review against workbook row and Gate 7 registers. |
| REQ-025-03-002 | The Construction Work Package shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Source: `PACKAGE_REGISTER.csv` row `PKG-025`. | Responsibility statement review against Gate 7 package register. |
| REQ-025-03-003 | The Construction Work Package shall include the three artifacts required by Gate 7 for `DEL-025-03`: construction work package, installation and tie-in workface plan, and construction interface and turnover checklist. Source: `ARTIFACT_REGISTER.csv` rows `ART-15E3B51A2A`, `ART-26C6F26015`, `ART-F23C60D66E`. | Artifact-completeness check against Gate 7 artifact register. |
| REQ-025-03-004 | The Construction Work Package shall represent the six applicable package interfaces (Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports) as construction-facing tie-in scope items. Source: Workbook Packages row 27; `INTERFACE_REGISTER.csv` rows for `PKG-025`. | Interface matrix check against `INTERFACE_REGISTER.csv`. |
| REQ-025-03-005 | The installation and tie-in workface plan shall describe how `PKG-025` is set, connected, and energized into adjacent process, utility, electrical, controls, civil, structural, and safety systems as applicable, consistent with the workface-planning artifact intent. Source: `ARTIFACT_REGISTER.csv` row `ART-26C6F26015`. | Workface-plan content review. |
| REQ-025-03-006 | The Construction Work Package shall require medium-voltage electrical installation work (home-run cabling, terminations, field interconnections, conduit, and grounding tie-ins) to comply with the DBM electrical design basis and the applicable Canadian Electrical Code grounding rules referenced therein. 6.9 kV medium-voltage cable shall be three-conductor copper TECK rated 8 kV with 100 percent insulation and shielded; low-voltage power cable fed from the VFD shall be copper TECK. Package-specific feeder, conductor, and conduit details remain `TBD` until detailed design. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MV cable, VFD-fed cable, construction scope, and grounding paragraphs. | Source citation review; unsupported values remain `TBD`. |
| REQ-025-03-007 | The Construction Work Package shall require foundation, pile, settlement, frost protection, site preparation, and structural support requirements to be confirmed against the final geotechnical report before construction issue. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, geotechnical paragraph. | Geotechnical confirmation check before issue for construction. |
| REQ-025-03-008 | The Construction Work Package shall require cable tray and conduit routing, and equipment placement, to preserve maintenance access in accordance with the DBM electrical routing and maintenance-access basis. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray/conduit paragraphs. | Routing/access review against package interface matrix. |
| REQ-025-03-009 | The Construction Work Package shall require I&C / control cabling and communications/network cabling tie-ins between the VFD/MV MCC and the plant PLC central control panel, including the Ethernet communication port required by DBM for the 6.9 kV MCC and any remote I/O network connections (PRP or DLR) per detailed design. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 6.9 kV MCC and remote I/O paragraphs. | Controls/network tie-in coverage review. |
| REQ-025-03-010 | The Construction Work Package shall require that grounding installation for the 6.9 kV transformer associated with `PKG-025` accept the DBM neutral grounding basis: each 6.9 kV transformer is grounded through a 100 A, 10 s neutral grounding resistor and operates as a tripping system; major electrical equipment is connected to the ground grid at two points. Package-specific tie-in details remain `TBD`. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs. | Grounding installation basis review. |
| REQ-025-03-011 | The Construction Work Package shall require area-classification-respecting installation, including marking and temperature-code selection for VFD-fed motors located in Zone 2 areas in accordance with the area-classification drawing or fugitive-emissions study. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, area classification and VFD/motor paragraphs. | Area classification installation review. |
| REQ-025-03-012 | The Construction Work Package shall be aligned to the plot plan, equipment list, and construction work package register before issue for construction. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, miscellaneous facilities/issue-for-construction paragraph. | Pre-issue alignment review. |
| REQ-025-03-013 | The construction interface and turnover checklist shall provide construction-facing interface, tie-in, inspection, and turnover evidence sufficient to support the downstream EPC Vendor Package Review and Acceptance (`DEL-025-06`). Source: `ARTIFACT_REGISTER.csv` row `ART-F23C60D66E`; `DELIVERABLE_REGISTER.csv` row `DEL-025-06`. | Turnover-checklist completeness review. |
| REQ-025-03-014 | The Construction Work Package shall identify source gaps (installation location/building assignment, modularization, lifting plan, ITPs, hold points, MV pre-energization tests, package-specific feeder and grounding details, control schematics, network port assignments, and detailed turnover-checklist content) as `TBD` rather than inventing values. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search. | Gap review before vendor handoff and construction issue. |
| REQ-025-03-015 | The Construction Work Package shall accept the Package Datasheet (`DEL-025-02`) as the technical handoff basis and shall not redefine package design values. Source: `DELIVERABLE_REGISTER.csv` row `DEL-025-02_package-datasheet`. | Cross-deliverable consistency check. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, conduit support, and electrical installation basis referenced by the DBM electrical section. | Applicable as source-supported design/installation basis; clause locations TBD. |
| Project electrical specifications | Medium-voltage service, MV MCC, VFD, grounding, cable, and raceway basis referenced by the DBM electrical section; governs construction installation methods for `PKG-025`. | Applicable; document location TBD. |
| Area classification standards (e.g., API RP 505 as referenced by DBM) | Apply to electrical equipment, conduit sealing, VFD-fed motor temperature-code marking, and installation classification where hazardous or non-hazardous areas are defined. | Applicable; package-specific location/classification TBD. |
| Final geotechnical report | Governs foundation, pile, settlement, frost protection, and structural support requirements for `PKG-025` installation. | Required input before issue for construction; package-specific values TBD. |
| Project plot plan, equipment list, and construction work package register | Governs alignment of `PKG-025` construction work package before issue for construction. | Required pre-issue alignment basis. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare construction work package identity fields to workbook row 27 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Artifact completeness | Compare authored artifacts to Gate 7 `ARTIFACT_REGISTER.csv` rows for `DEL-025-03_construction-work-package`. | All three artifacts (`ART-15E3B51A2A`, `ART-26C6F26015`, `ART-F23C60D66E`) are present in the deliverable. |
| Interface completeness | Compare construction-facing interface coverage to `INTERFACE_REGISTER.csv` rows for `PKG-025`. | Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports are present. |
| Source fidelity | Check every non-trivial installation, grounding, routing, foundation, control/network, or area-classification statement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as construction requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv` row `PKG-025`. | Vendor package design responsibilities are not conflated with EPC construction-facing responsibilities. |
| Pre-issue alignment | Confirm construction work package is aligned to plot plan, equipment list, and construction work package register. | Alignment evidence is recorded before issue for construction. |
| Geotechnical dependency | Confirm package-specific foundation/support content depends on the final geotechnical report or is held `TBD`. | No unsupported foundation/support criteria are stated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package identity, IDs, interfaces, artifacts, and `TBD` items. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Construction work package (`ART-15E3B51A2A`).
- Installation and tie-in workface plan (`ART-26C6F26015`).
- Construction interface and turnover checklist (`ART-F23C60D66E`).
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 27, applicable Gate 7 registers, and the DBM construction and electrical source slices used as installation basis. It shall reference the upstream Package Datasheet (`DEL-025-02`) and Scope of Work (`DEL-025-01`) as inputs, and the downstream `DEL-025-05` and `DEL-025-06` deliverables as consumers of turnover evidence.
