# Specification: DEL-042-05_vendor-document-turnover-package

## Scope

This specification governs the Package Vendor-authored Vendor Document Turnover Package for `PKG-042`, the Control Room Building. The deliverable is the vendor document register, vendor document submittals, source-required vendor documentation, and turnover records, with EPC Integrator interface/integration review.

The package is a vendor-owned Electrical package under WBS 03, CoA 26020-03-39-010. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- EPC-authored deliverables (Scope of Work `DEL-042-01`, Package Datasheet `DEL-042-02`, Construction Work Package `DEL-042-03`, EPC Vendor Package Review and Acceptance `DEL-042-06`) and the Vendor Engineered Equipment Package (`DEL-042-04`) are not produced by this deliverable.
- The detailed vendor document list, format, numbering convention, and turnover record templates are `TBD` because the accessible source set does not include a PKG-042 vendor-document specification.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-042-05-001 | The Vendor Document Turnover Package shall identify `PKG-042`, workbook row 44, WBS 03, CoA tracking number 26020-03-39-010, discipline Electrical, and package name "Control Room Building." Source: Workbook Packages row 44; `PACKAGE_REGISTER.csv`. | Identification review against workbook row and Gate 7 registers. |
| REQ-042-05-002 | The Vendor Document Turnover Package shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces and performs vendor-document interface/integration review. Source: `PACKAGE_REGISTER.csv` row `PKG-042`; `DELIVERABLE_REGISTER.csv` row `DEL-042-05`. | Responsibility statement review. |
| REQ-042-05-003 | The Vendor Document Turnover Package shall include the anticipated artifact set: vendor document register, vendor document submittals, source vendor document table rows as artifacts where available, and turnover records. Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`. | Artifact-set completeness review. |
| REQ-042-05-004 | The vendor document register shall, at minimum, enumerate the package deliverable items called out in the DBM mechanical-package deliverable paragraph that are applicable to a Control Room Building package: datasheets, utility load summaries, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access content, shipped-loose item lists, and the vendor document register itself. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617. ASSUMPTION: filtered to electrical-building applicability; relief/load data and cause-and-effect inputs may be non-applicable (see Conflict Table HRR-042-05-001). | Register completeness review against the cited DBM paragraph. |
| REQ-042-05-005 | The Vendor Document Turnover Package shall preserve all eleven PKG-042 interface facts (Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports) and provide vendor documentation supporting each applicable interface. Source: Workbook Packages row 44; `INTERFACE_REGISTER.csv` rows for `PKG-042`. | Interface coverage check against `INTERFACE_REGISTER.csv`. |
| REQ-042-05-006 | The Vendor Document Turnover Package shall record source gaps as `TBD` rather than invented requirements. Items where source slices do not define content (document numbering scheme, turnover record templates, submittal acceptance criteria, vendor sparing list specifics) shall be `TBD` until vendor data or accepted source resolves them. Source: `ARTIFACT_REGISTER.csv` row `ART-F6E4C1C060`; `_REFERENCES.md`. | Gap review before turnover acceptance. |
| REQ-042-05-007 | Individual source vendor document table rows shall be captured as artifacts/evidence and not promoted to separate deliverables. Source: `_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv` Notes column. | Artifact-versus-deliverable check. |
| REQ-042-05-008 | The Vendor Document Turnover Package shall be subject to EPC Integrator interface/integration review and shall feed `DEL-042-06_epc-vendor-package-review-and-acceptance`. Source: `DELIVERABLE_REGISTER.csv` rows `DEL-042-05`, `DEL-042-06`. | Handoff review against `DEL-042-06`. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| DBM mechanical-package deliverable paragraph | Defines the minimum package deliverable set including vendor document registers. | Applicable; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617. |
| Project vendor document control specification | Governs vendor document numbering, submittal workflow, and turnover format. | ASSUMPTION: applicable; document location TBD (no accessible source slice). |
| Canadian Electrical Code (CEC) | Electrical equipment installation basis referenced by DBM electrical sections; vendor documentation shall demonstrate compliance where applicable. | Applicable as source-supported design basis; specific clause locations TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare turnover package identification to workbook row 44 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Artifact-set completeness | Confirm the four anticipated artifact categories (register, submittals, source rows, turnover records) are present. | All four categories are produced or explicitly marked `TBD` with rationale. |
| DBM deliverable coverage | Compare vendor document register against the DBM mechanical-package deliverable paragraph items applicable to a building package. | All applicable items are listed or explicitly excluded with rationale. |
| Interface coverage | Compare vendor documents to `INTERFACE_REGISTER.csv` rows for `PKG-042`. | All eleven interface facts have corresponding vendor documentation or a recorded gap. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |
| EPC review handoff | Confirm the turnover package is presented to the EPC vendor-package review and acceptance flow (`DEL-042-06`). | Handoff evidence recorded. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor document register.
- Vendor document submittals.
- Source vendor document table rows captured as artifacts where available.
- Turnover records.
- Source-gap / `TBD` list for vendor or human resolution (linked to `ART-F6E4C1C060`).

The deliverable shall cite the Gate 7 snapshot, workbook row 44, applicable Gate 7 registers, and the DBM electrical and mechanical-package source slices used for vendor-document scope basis.
