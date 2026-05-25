# Specification: DEL-013-03_construction-work-package

## Scope

This specification governs the EPC Integrator-authored Construction Work Package for `PKG-013`, the 100A DC UNINTERUPTIBLE POWER SUPPLY package. The Construction Work Package is a mandatory Gate 5 EPC anchor deliverable and shall describe how the package is physically installed, built, inspected, turned over, and tied into the larger facility systems.

The package is a vendor-owned Electrical package under WBS 02. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration, and is the construction-facing author of this deliverable.

Exclusions:

- Vendor detailed engineering, factory fabrication, factory acceptance testing, and certified-equipment selections are excluded from the EPC Construction Work Package except as inputs that the construction scope must accept and install.
- Package-specific lift plans, ITPs, hold points, foundation/support detail, feeder/cable sizing, ground-conductor sizing, conduit routing, termination details, building/room assignment, and turnover-checklist line items are `TBD` because the accessible source set does not provide confirmed package-specific values.
- Vendor document review and final EPC package acceptance are out of scope here and are carried by `DEL-013-05` (Vendor Document Turnover Package) and `DEL-013-06` (EPC Vendor Package Review and Acceptance).

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-013-03-001 | The Construction Work Package shall identify `PKG-013`, workbook row 15, WBS 02, CoA tracking number 26020-02-30-004, discipline Electrical, and package name "100A DC UNINTERUPTIBLE POWER SUPPLY." Source: Workbook Packages row 15; `PACKAGE_REGISTER.csv`. | Identity review against workbook row and Gate 7 registers. |
| REQ-013-03-002 | The Construction Work Package shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Source: `PACKAGE_REGISTER.csv` row `PKG-013`. | Responsibility statement review against Gate 7 package register. |
| REQ-013-03-003 | The Construction Work Package shall include the three artifacts required by Gate 7 for `DEL-013-03`: construction work package, installation and tie-in workface plan, and construction interface and turnover checklist. Source: `ARTIFACT_REGISTER.csv` rows `ART-66584B5974`, `ART-614F88809C`, `ART-D370CE5716`. | Artifact-completeness check against Gate 7 artifact register. |
| REQ-013-03-004 | The Construction Work Package shall represent the four applicable package interfaces (Electrical Power, Grounding / Bonding, Maintenance Access, Structural / Foundations / Supports) as construction-facing tie-in scope items. Source: Workbook Packages row 15; `INTERFACE_REGISTER.csv` rows for `PKG-013`. | Interface matrix check against `INTERFACE_REGISTER.csv`. |
| REQ-013-03-005 | The installation and tie-in workface plan shall describe how `PKG-013` is set, connected, and energized into adjacent process, utility, electrical, controls, civil, structural, and safety systems as applicable, consistent with the workface-planning artifact intent. Source: `ARTIFACT_REGISTER.csv` row `ART-614F88809C`. | Workface-plan content review. |
| REQ-013-03-006 | The Construction Work Package shall require electrical installation work (home-run cabling, terminations, field interconnections, conduit, and grounding tie-ins) to comply with the DBM electrical design basis and the applicable Canadian Electrical Code grounding rules referenced therein. Package-specific feeder, conductor, and conduit details remain `TBD` until detailed design. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, construction scope summary; DBM grounding and bonding paragraphs. | Source citation review; unsupported values remain `TBD`. |
| REQ-013-03-007 | The Construction Work Package shall require foundation, pile, settlement, frost protection, site preparation, and structural support requirements to be confirmed against the final geotechnical report before construction issue. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, geotechnical paragraph. | Geotechnical confirmation check before issue for construction. |
| REQ-013-03-008 | The Construction Work Package shall require cable tray and conduit routing, and equipment placement, to preserve maintenance access in accordance with the DBM electrical routing and maintenance-access basis. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, cable tray/conduit paragraphs. | Routing/access review against package interface matrix. |
| REQ-013-03-009 | The Construction Work Package shall be aligned to the plot plan, equipment list, and construction work package register before issue for construction. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, miscellaneous facilities/issue-for-construction paragraph. | Pre-issue alignment review. |
| REQ-013-03-010 | The construction interface and turnover checklist shall provide construction-facing interface, tie-in, inspection, and turnover evidence sufficient to support the downstream EPC Vendor Package Review and Acceptance (`DEL-013-06`). Source: `ARTIFACT_REGISTER.csv` row `ART-D370CE5716`; `DELIVERABLE_REGISTER.csv` row `DEL-013-06`. | Turnover-checklist completeness review. |
| REQ-013-03-011 | The Construction Work Package shall identify source gaps (modularization basis, installation location, lifting plan, ITPs, hold points, package-specific feeder and grounding details, and detailed turnover-checklist content) as `TBD` rather than inventing values. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search. | Gap review before vendor handoff and construction issue. |
| REQ-013-03-012 | The Construction Work Package shall accept the Package Datasheet (`DEL-013-02`) as the technical handoff basis and shall not redefine package design values. Source: `DELIVERABLE_REGISTER.csv` row `DEL-013-02_package-datasheet`. | Cross-deliverable consistency check. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, conduit support, and electrical installation basis referenced by the DBM electrical section. | Applicable as source-supported design/installation basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by the DBM electrical section; governs construction installation methods for `PKG-013`. | Applicable; document location TBD. |
| Area classification standards (e.g., API RP 505 as referenced by DBM) | Apply to electrical equipment, conduit sealing, and installation classification where hazardous or non-hazardous areas are defined. | Applicable; package-specific location/classification TBD. |
| Final geotechnical report | Governs foundation, pile, settlement, frost protection, and structural support requirements for `PKG-013` installation. | Required input before issue for construction; package-specific values TBD. |
| Project plot plan, equipment list, and construction work package register | Governs alignment of `PKG-013` construction work package before issue for construction. | Required pre-issue alignment basis. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare construction work package identity fields to workbook row 15 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Artifact completeness | Compare authored artifacts to Gate 7 `ARTIFACT_REGISTER.csv` rows for `DEL-013-03_construction-work-package`. | All three artifacts (`ART-66584B5974`, `ART-614F88809C`, `ART-D370CE5716`) are present in the deliverable. |
| Interface completeness | Compare construction-facing interface coverage to `INTERFACE_REGISTER.csv` rows for `PKG-013`. | Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports are present. |
| Source fidelity | Check every non-trivial installation, grounding, routing, foundation, or area-classification statement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as construction requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv` row `PKG-013`. | Vendor package design responsibilities are not conflated with EPC construction-facing responsibilities. |
| Pre-issue alignment | Confirm construction work package is aligned to plot plan, equipment list, and construction work package register. | Alignment evidence is recorded before issue for construction. |
| Geotechnical dependency | Confirm package-specific foundation/support content depends on the final geotechnical report or is held `TBD`. | No unsupported foundation/support criteria are stated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package identity, IDs, interfaces, artifacts, and `TBD` items. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Construction work package (`ART-66584B5974`).
- Installation and tie-in workface plan (`ART-614F88809C`).
- Construction interface and turnover checklist (`ART-D370CE5716`).
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 15, applicable Gate 7 registers, and the DBM construction and electrical source slices used as installation basis. It shall reference the upstream Package Datasheet (`DEL-013-02`) and Scope of Work (`DEL-013-01`) as inputs, and the downstream `DEL-013-05` and `DEL-013-06` deliverables as consumers of turnover evidence.
