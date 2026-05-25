# Specification: DEL-029-03_construction-work-package

## Scope

This specification governs the EPC Integrator-authored Construction Work Package for `PKG-029`, the "Transformer TXP-8600-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V" package. The Construction Work Package is a mandatory Gate 5 EPC anchor deliverable and shall describe how the package is physically installed, built, inspected, turned over, and tied into the larger facility systems.

The package is a vendor-owned Electrical package under WBS 01. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration, and is the construction-facing author of this deliverable.

Exclusions:

- Vendor detailed engineering, factory fabrication, factory acceptance testing, and certified-equipment selections are excluded from the EPC Construction Work Package except as inputs that the construction scope must accept and install.
- Package-specific lift plans, ITPs, hold points, foundation/pad/anchor detail, feeder/cable sizing, ground-conductor sizing, conduit routing, termination details, building/pad assignment, oil-handling plan (if oil-filled), secondary containment detail, and turnover-checklist line items are `TBD` because the accessible source set does not provide confirmed package-specific values.
- Vendor document review and final EPC package acceptance are out of scope here and are carried by `DEL-029-05` (Vendor Document Turnover Package) and `DEL-029-06` (EPC Vendor Package Review and Acceptance).

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-029-03-001 | The Construction Work Package shall identify `PKG-029`, workbook row 31, WBS 01, CoA tracking number 26020-01-30-020, discipline Electrical, and package name "Transformer TXP-8600-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V." Source: Workbook Packages row 31; `PACKAGE_REGISTER.csv`. | Identity review against workbook row and Gate 7 registers. |
| REQ-029-03-002 | The Construction Work Package shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Source: `PACKAGE_REGISTER.csv` row `PKG-029`. | Responsibility statement review against Gate 7 package register. |
| REQ-029-03-003 | The Construction Work Package shall include the three artifacts required by Gate 7 for `DEL-029-03`: construction work package, installation and tie-in workface plan, and construction interface and turnover checklist. Source: `ARTIFACT_REGISTER.csv` rows `ART-C18BB35507`, `ART-A14748BEA0`, `ART-15977E3467`. | Artifact-completeness check against Gate 7 artifact register. |
| REQ-029-03-004 | The Construction Work Package shall represent the seven applicable package interfaces (Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports) as construction-facing tie-in scope items. Source: Workbook Packages row 31; `INTERFACE_REGISTER.csv` rows for `PKG-029`. | Interface matrix check against `INTERFACE_REGISTER.csv`. |
| REQ-029-03-005 | The installation and tie-in workface plan shall describe how `PKG-029` is set, connected, and energized into adjacent process, utility, electrical, controls, civil, structural, and safety systems as applicable, consistent with the workface-planning artifact intent. Source: `ARTIFACT_REGISTER.csv` row `ART-A14748BEA0`. | Workface-plan content review. |
| REQ-029-03-006 | The Construction Work Package shall require electrical installation work (MV 13.8 kV primary cabling, LV 600 V secondary cabling, terminations, field interconnections, conduit, and grounding tie-ins) to comply with the DBM electrical design basis and the applicable Canadian Electrical Code grounding and spacing rules referenced therein. Package-specific feeder, conductor, conduit, and termination details remain `TBD` until detailed design. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, construction scope summary; DBM grounding/cable/transformer paragraphs. | Source citation review; unsupported values remain `TBD`. |
| REQ-029-03-007 | The Construction Work Package shall require foundation, pile, settlement, frost protection, site preparation, secondary containment review, and structural support requirements to be confirmed against the final geotechnical report before construction issue, recognizing that transformers are generally installed on precast concrete bearing foundations or structural steel transformer bases. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformer foundations and geotechnical paragraphs. | Geotechnical confirmation check before issue for construction. |
| REQ-029-03-008 | The Construction Work Package shall require cable tray and conduit routing, equipment placement, and CEC transformer spacing to preserve maintenance access in accordance with the DBM electrical routing and maintenance-access basis. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformer spacing and cable tray/conduit paragraphs. | Routing/access review against package interface matrix. |
| REQ-029-03-009 | The Construction Work Package shall be aligned to the plot plan, equipment list, and construction work package register before issue for construction. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, miscellaneous facilities/issue-for-construction paragraph. | Pre-issue alignment review. |
| REQ-029-03-010 | The construction interface and turnover checklist shall provide construction-facing interface, tie-in, inspection, and turnover evidence sufficient to support the downstream EPC Vendor Package Review and Acceptance (`DEL-029-06`). Source: `ARTIFACT_REGISTER.csv` row `ART-15977E3467`; `DELIVERABLE_REGISTER.csv` row `DEL-029-06`. | Turnover-checklist completeness review. |
| REQ-029-03-011 | The Construction Work Package shall identify source gaps (transformer construction class — oil-filled vs dry-type, installation location, modularization basis, lifting plan, ITPs, hold points, package-specific feeder/ground-conductor/conduit detail, secondary-containment detail, oil-handling plan, and turnover-checklist line items) as `TBD` rather than inventing values. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search. | Gap review before vendor handoff and construction issue. |
| REQ-029-03-012 | The Construction Work Package shall accept the Package Datasheet (`DEL-029-02`) as the technical handoff basis and shall not redefine package design values. Source: `DELIVERABLE_REGISTER.csv` row `DEL-029-02_package-datasheet`. | Cross-deliverable consistency check. |
| REQ-029-03-013 | Where the transformer is oil-filled, the Construction Work Package shall require CEC-compliant spacing, secondary-containment review, and oil-handling/testing steps (insulation resistance, turns ratio, oil dielectric) as installation/test prerequisites; applicability shall be confirmed by vendor data. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph. | Field-test inclusion check; ASSUMPTION on oil-filled construction pending vendor confirmation. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, transformer spacing, conduit support, and electrical installation basis referenced by the DBM electrical section. | Applicable as source-supported design/installation basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by the DBM electrical section; governs construction installation methods for `PKG-029`. | Applicable; document location TBD. |
| Area classification standards (e.g., API RP 505 as referenced by DBM) | Apply to electrical equipment, conduit sealing, and installation classification where hazardous or non-hazardous areas are defined. | Applicable; package-specific location/classification TBD. |
| Final geotechnical report | Governs foundation, pile, settlement, frost protection, and structural support requirements for `PKG-029` installation, including transformer pad/base design. | Required input before issue for construction; package-specific values TBD. |
| Project plot plan, equipment list, and construction work package register | Governs alignment of `PKG-029` construction work package before issue for construction. | Required pre-issue alignment basis. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare construction work package identity fields to workbook row 31 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Artifact completeness | Compare authored artifacts to Gate 7 `ARTIFACT_REGISTER.csv` rows for `DEL-029-03_construction-work-package`. | All three artifacts (`ART-C18BB35507`, `ART-A14748BEA0`, `ART-15977E3467`) are present in the deliverable. |
| Interface completeness | Compare construction-facing interface coverage to `INTERFACE_REGISTER.csv` rows for `PKG-029`. | All seven applicable interfaces are present. |
| Source fidelity | Check every non-trivial installation, grounding, routing, foundation, or area-classification statement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as construction requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv` row `PKG-029`. | Vendor package design responsibilities are not conflated with EPC construction-facing responsibilities. |
| Pre-issue alignment | Confirm construction work package is aligned to plot plan, equipment list, and construction work package register. | Alignment evidence is recorded before issue for construction. |
| Geotechnical dependency | Confirm package-specific foundation/support/pad/anchor content depends on the final geotechnical report or is held `TBD`. | No unsupported foundation/support criteria are stated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package identity, IDs, interfaces, artifacts, and `TBD` items. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Construction work package (`ART-C18BB35507`).
- Installation and tie-in workface plan (`ART-A14748BEA0`).
- Construction interface and turnover checklist (`ART-15977E3467`).
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 31, applicable Gate 7 registers, and the DBM-Deepcut construction, transformer, and electrical source slices used as installation basis. It shall reference the upstream Package Datasheet (`DEL-029-02`) and Scope of Work (`DEL-029-01`) as inputs, and the downstream `DEL-029-05` and `DEL-029-06` deliverables as consumers of turnover evidence.
