# Specification: DEL-027-05_vendor-document-turnover-package

## Scope

This specification governs the Vendor Document Turnover Package for `PKG-027`, the Transformer TXP-8301-1 step-down distribution transformer (20/26 MVA, 13.8 kV / 6.9 kV / 0.4 kV). The deliverable is a Package Vendor production unit comprising the vendor document register, vendor document submittals, source-required vendor documentation, and turnover records, subject to EPC Integrator interface/integration review.

The package is a vendor-owned Electrical package under WBS 01. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor engineering, design, and physical-equipment fabrication are governed by `DEL-027-04_vendor-engineered-equipment-package` and are not duplicated here; this deliverable governs the documentation set and turnover evidence.
- EPC review and acceptance of the vendor package is governed by `DEL-027-06_epc-vendor-package-review-and-acceptance` and is not this deliverable's scope.
- Detailed vendor-document content and register schema specific to PKG-027 are `TBD` because the accessible source set does not enumerate them (`ARTIFACT_REGISTER.csv` row `ART-AACDC8D0FF`).

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-027-05-001 | The deliverable shall produce a vendor document register identifying `PKG-027`, workbook row 29, WBS 01, CoA tracking number 26020-01-30-018, discipline Electrical, and package name "Transformer TXP-8301-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 20/26MVA 13.8kV/6.9kV/0.4kV." Source: Workbook Packages row 29; `PACKAGE_REGISTER.csv`. | Register identity review against the workbook row and Gate 7 registers. |
| REQ-027-05-002 | The deliverable shall preserve the accepted responsibility split: Package Vendor authors the vendor documentation; EPC Integrator performs interface/integration review. Source: `PACKAGE_REGISTER.csv` row `PKG-027`; `DELIVERABLE_REGISTER.csv` row `DEL-027-05_vendor-document-turnover-package`. | Responsibility statement review against the Gate 7 registers. |
| REQ-027-05-003 | The vendor document register shall include entries that evidence each applicable package interface fact: Electrical Power (`IFC-7FDEAE3A5F`), Grounding / Bonding (`IFC-868150D715`), Area / Exterior Lighting (`IFC-A7AA374E9F`), I&C / Control Cabling (`IFC-A771D8D087`), Communications / Network (`IFC-41603B3260`), Maintenance Access (`IFC-6D508F385A`), and Structural / Foundations / Supports (`IFC-1B8FDDED83`). Source: `INTERFACE_REGISTER.csv` rows for `PKG-027`. | Cross-check vendor documents against the interface register for `PKG-027`. |
| REQ-027-05-004 | Vendor documentation for grounding shall reflect the DBM grounding/bonding basis (two-point ground-grid connections at major electrical equipment; ground wells at power transformers; copper ground conductors at distribution transformers per CEC). ASSUMPTION: clause-level applicability to TXP-8301-1 confirmed by detailed design. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs. | Grounding documentation review against DBM source slice. |
| REQ-027-05-005 | Vendor documentation for neutral grounding on the 6.9 kV winding shall reflect a 100 A, 10 s neutral grounding resistor operating as a tripping system, unless an accepted ruling supersedes this basis. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, neutral grounding paragraph. | Neutral grounding documentation review against DBM source slice and any accepted ruling. |
| REQ-027-05-006 | Vendor documentation for foundations/installation shall reflect transformer installation on a structural steel base on a precast concrete bearing foundation with CEC-compliant spacing and secondary containment review where applicable. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers and foundations sections. | Foundation documentation review against DBM source slice. |
| REQ-027-05-007 | The deliverable shall produce vendor document submittals; the submittal list and return-code workflow shall be defined by the vendor and confirmed by EPC review. Specific submittal contents are `TBD` because the accessible source set does not enumerate them. Source: `ARTIFACT_REGISTER.csv` row `ART-AACDC8D0FF`; `_REFERENCES.md`. | Submittal-completeness review against the agreed submittal list. |
| REQ-027-05-008 | The deliverable shall produce turnover records (e.g., factory test reports, oil quality reports, nameplate data, as-built drawings, O&M manuals, spare parts list, warranty documents); detailed content and acceptance criteria are `TBD` and shall be defined during detailed engineering and vendor handoff. Source: source gap; `ARTIFACT_REGISTER.csv` row `ART-AACDC8D0FF`. | Turnover-package completeness review at handoff. |
| REQ-027-05-009 | The deliverable shall identify source gaps explicitly as `TBD` instead of inventing vendor-document requirements not supported by source. Source: `_REFERENCES.md`; `ARTIFACT_REGISTER.csv` row `ART-AACDC8D0FF`. | Source-fidelity check at QA. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Grounding, conduit, spacing, and installation basis referenced by DBM electrical section; vendor documentation shall be consistent with CEC where applicable. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage, MCC, grounding, cable, and raceway basis referenced by DBM electrical section; vendor documentation shall be consistent. | Applicable; document location TBD. |
| Transformer industry standards (e.g., CSA / IEEE / IEC for power transformers, factory tests, oil quality) | Vendor documentation for power transformer testing and certification typically references such standards. | ASSUMPTION: likely applicable; specific standards and clause locations TBD pending vendor selection and source confirmation. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare vendor document register identity fields to Workbook Packages row 29 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface evidence completeness | Compare vendor document register to `INTERFACE_REGISTER.csv` rows for `PKG-027`. | All seven applicable interface facts are evidenced by at least one vendor document entry. |
| Source fidelity | Check every non-trivial claim or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as confirmed requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv` and `DELIVERABLE_REGISTER.csv`. | Vendor authorship and EPC review roles are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |
| Turnover completeness | Compare turnover records to the agreed turnover-records list at handoff. | All agreed turnover items are present and traceable. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor document register (TBD content schema; see `ART-AACDC8D0FF`).
- Vendor document submittals (TBD list).
- Source-required vendor documentation (TBD list; source-grounded where possible).
- Turnover records (TBD content; source gap).
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, Workbook Packages row 29, applicable Gate 7 registers, and the DBM electrical source slices used for transformer, grounding, and foundation basis.
