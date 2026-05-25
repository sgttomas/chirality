# Specification: DEL-038-03_construction-work-package

## Scope

This specification governs the EPC Integrator-authored Construction Work Package for `PKG-038`, the 600V ELECTRICAL BUILDING (820-1) package. The Construction Work Package is a mandatory Gate 5 EPC anchor deliverable and shall describe how the package is physically installed, built, inspected, turned over, and tied into the larger facility systems.

The package is a vendor-owned Electrical package under WBS 01 with CoA tracking number 26020-01-30-029. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package (a prefabricated, modular electrical building). The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration, and is the construction-facing author of this deliverable.

Exclusions:

- Vendor detailed engineering, factory fabrication, factory acceptance testing, and certified-equipment selections are excluded from the EPC Construction Work Package except as inputs that the construction scope must accept and install.
- Package-specific lift plans, ITPs, hold points, foundation/pile/settlement detail, feeder/cable sizing, ground-conductor sizing, conduit and tray routing, exact plot location, building-internal equipment quantities, HVAC equipment selection, and turnover-checklist line items are `TBD` because the accessible source set does not provide confirmed package-specific values.
- Vendor document review and final EPC package acceptance are out of scope here and are carried by `DEL-038-05` (Vendor Document Turnover Package) and `DEL-038-06` (EPC Vendor Package Review and Acceptance).

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-038-03-001 | The Construction Work Package shall identify `PKG-038`, workbook row 40, WBS 01, CoA tracking number 26020-01-30-029, discipline Electrical, and package name "600V ELECTRICAL BUILDING (820-1)." Source: Workbook Packages row 40; `PACKAGE_REGISTER.csv`. | Identity review against workbook row and Gate 7 registers. |
| REQ-038-03-002 | The Construction Work Package shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Source: `PACKAGE_REGISTER.csv` row `PKG-038`. | Responsibility statement review against Gate 7 package register. |
| REQ-038-03-003 | The Construction Work Package shall include the three artifacts required by Gate 7 for `DEL-038-03`: construction work package, installation and tie-in workface plan, and construction interface and turnover checklist. Source: `ARTIFACT_REGISTER.csv` rows `ART-9F12F8D18F`, `ART-A7B67360EB`, `ART-C554CB9646`. | Artifact-completeness check against Gate 7 artifact register. |
| REQ-038-03-004 | The Construction Work Package shall represent the twelve applicable package interfaces (Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports) as construction-facing tie-in scope items. Source: Workbook Packages row 40; `INTERFACE_REGISTER.csv` rows for `PKG-038`. | Interface matrix check against `INTERFACE_REGISTER.csv`. |
| REQ-038-03-005 | The installation and tie-in workface plan shall describe how `PKG-038` is set, connected, energized, climate-controlled, and tied into adjacent utility, electrical, controls, communications, civil, structural, HVAC, fire & gas, and lighting systems, consistent with the workface-planning artifact intent. Source: `ARTIFACT_REGISTER.csv` row `ART-A7B67360EB`. | Workface-plan content review. |
| REQ-038-03-006 | The Construction Work Package shall require the electrical building to be installed as a prefabricated, modular building, elevated on piles with bottom entry for incoming and outgoing power cables. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section. | Construction-method check against DBM Electrical Buildings basis. |
| REQ-038-03-007 | The Construction Work Package shall require electrical installation work (home-run cabling, terminations, field interconnections, conduit, and grounding tie-ins) to use TECK 90 / ACWU / ACIC tray cable rated for -40 deg C with HL-rated aluminum interlocking armor, copper conductors up to #1/0 AWG and ACWU aluminum cables above #1/0 AWG, and EMT conduit between adjacent equipment, in accordance with the DBM cable basis and the Canadian Electrical Code grounding rules referenced therein. Package-specific feeder, conductor, and conduit details remain `TBD` until detailed design. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cable Wire and Raceways and Grounding and Bonding sections. | Source citation review; unsupported values remain `TBD`. |
| REQ-038-03-008 | The Construction Work Package shall require building grounding to include direct ground-grid connections at two points for major equipment, ground wells at the electrical building with bolted ground connections, and separate copper ground conductors for distribution transformers, panelboards, and three-phase motors larger than 100 hp sized per CEC. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Grounding and Bonding section. | Grounding-installation check against DBM grounding basis. |
| REQ-038-03-009 | The Construction Work Package shall require foundation, pile, settlement, frost protection, site preparation, and structural support requirements to be confirmed against the final geotechnical report before construction issue. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section (pile-elevated requirement); facility geotechnical basis. | Geotechnical confirmation check before issue for construction. |
| REQ-038-03-010 | The Construction Work Package shall require the building to be located in a general-purpose (non-hazardous) area per DBM area classification, with construction installation methods, conduit sealing, and material selection respecting the area classification assigned by the detailed area-classification drawings. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Area Classification section. | Area-classification consistency check. |
| REQ-038-03-011 | The Construction Work Package shall require cable tray and conduit routing, and equipment placement, to preserve maintenance access and to allow removal of the largest equipment through doors or removable transom sections. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings and Cable Wire and Raceways sections. | Routing/access review against package interface matrix. |
| REQ-038-03-012 | The Construction Work Package shall require the building HVAC to be installed and commissioned as an n + 1 redundant system; electric building heaters shall be applied where heat-medium heaters are not practical. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings and building-heater sections. | HVAC redundancy check at construction completion. |
| REQ-038-03-013 | The Construction Work Package shall be aligned to the plot plan, equipment list, and construction work package register before issue for construction. Source: Facility plot plan and construction work package register (location TBD); `_REFERENCES.md`. | Pre-issue alignment review. |
| REQ-038-03-014 | The construction interface and turnover checklist shall provide construction-facing interface, tie-in, inspection, and turnover evidence sufficient to support the downstream EPC Vendor Package Review and Acceptance (`DEL-038-06`). Source: `ARTIFACT_REGISTER.csv` row `ART-C554CB9646`; `DELIVERABLE_REGISTER.csv` row for `DEL-038-06`. | Turnover-checklist completeness review. |
| REQ-038-03-015 | The Construction Work Package shall identify source gaps (exact plot location, modularization/shipping splits, lift plan, ITPs, hold points, package-specific feeder and grounding details, building-internal equipment quantities, HVAC equipment selection, and detailed turnover-checklist content) as `TBD` rather than inventing values. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` not opened in this run. | Gap review before vendor handoff and construction issue. |
| REQ-038-03-016 | The Construction Work Package shall accept the Package Datasheet (`DEL-038-02`) as the technical handoff basis and shall not redefine package design values. Source: `DELIVERABLE_REGISTER.csv` row for `DEL-038-02_package-datasheet`. | Cross-deliverable consistency check. |
| REQ-038-03-017 | The Construction Work Package shall record, but not resolve, the apparent identity conflict between the workbook designation "600V ELECTRICAL BUILDING (820-1)" and the DBM electrical-buildings list entry "820-1 6.9 kV Inlet / Sales Compressor Electrical Building" (Guidance Conflict Table item HRR-038-03-001), and shall hold this identity for human ruling. Source: Workbook Packages row 40; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings table. | Conflict-Table presence and human-ruling status check. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, conduit support, and electrical installation basis referenced by the DBM electrical section. | Applicable as source-supported design/installation basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by the DBM electrical section; governs construction installation methods for `PKG-038`. | Applicable; document location TBD. |
| Area classification standards (e.g., API RP 505 as referenced by DBM convention) | Apply to electrical equipment, conduit sealing, and installation classification in general-purpose vs. hazardous areas. | Applicable; package-specific area-classification drawing reference TBD. |
| OGAOM, Sec. 9.6.15 (spacing of electrical buildings from fired heaters) | DBM cites a 25 m (82 ft) minimum spacing between fired heaters and electrical buildings; applicable as a siting constraint when the building is located near fired heaters. | Applicable as siting constraint; specific plot-plan distance check TBD. |
| Final geotechnical report | Governs foundation, pile, settlement, frost protection, and structural support requirements for the elevated, pile-supported electrical building. | Required input before issue for construction; package-specific values TBD. |
| Project plot plan, equipment list, and construction work package register | Governs alignment of `PKG-038` construction work package before issue for construction. | Required pre-issue alignment basis; document locations TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare construction work package identity fields to workbook row 40 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Artifact completeness | Compare authored artifacts to Gate 7 `ARTIFACT_REGISTER.csv` rows for `DEL-038-03_construction-work-package`. | All three artifacts (`ART-9F12F8D18F`, `ART-A7B67360EB`, `ART-C554CB9646`) are present in the deliverable. |
| Interface completeness | Compare construction-facing interface coverage to `INTERFACE_REGISTER.csv` rows for `PKG-038`. | All twelve applicable interfaces are present. |
| Source fidelity | Check every non-trivial installation, grounding, routing, cable, HVAC, foundation, or area-classification statement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as construction requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv` row `PKG-038`. | Vendor package design responsibilities are not conflated with EPC construction-facing responsibilities. |
| Pre-issue alignment | Confirm construction work package is aligned to plot plan, equipment list, and construction work package register. | Alignment evidence is recorded before issue for construction. |
| Geotechnical dependency | Confirm package-specific foundation/pile/settlement content depends on the final geotechnical report or is held `TBD`. | No unsupported foundation/support criteria are stated. |
| Identity conflict logged | Confirm the workbook-vs-DBM identity discrepancy for tag 820-1 is captured in the Guidance Conflict Table and surfaced for human ruling. | Conflict Table entry HRR-038-03-001 present with status TBD. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package identity, IDs, interfaces, artifacts, and `TBD` items. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Construction work package (`ART-9F12F8D18F`).
- Installation and tie-in workface plan (`ART-A7B67360EB`).
- Construction interface and turnover checklist (`ART-C554CB9646`).
- Source-gap / `TBD` list for vendor or human resolution, including the identity conflict for tag 820-1.

The deliverable shall cite the Gate 7 snapshot, workbook row 40, applicable Gate 7 registers, and the DBM-Deepcut electrical source slices used as installation basis. It shall reference the upstream Package Datasheet (`DEL-038-02`) and Scope of Work (`DEL-038-01`) as inputs, and the downstream `DEL-038-05` and `DEL-038-06` deliverables as consumers of turnover evidence.
