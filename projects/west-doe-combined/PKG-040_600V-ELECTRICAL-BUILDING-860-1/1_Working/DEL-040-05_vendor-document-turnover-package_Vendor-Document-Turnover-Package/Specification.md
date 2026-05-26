# Specification: DEL-040-05_vendor-document-turnover-package

## Scope

This specification governs the Package Vendor-authored Vendor Document Turnover Package for `PKG-040`, the 600V ELECTRICAL BUILDING (860-1), identified in DBM-Deepcut as the "600V General Area / Tank Farm Electrical Building." The deliverable consists of the vendor document register, vendor document submittals, source-required vendor documentation, and turnover records, with EPC Integrator interface/integration review.

The package is a vendor-owned Electrical package under WBS 01 (CoA 26020-01-30-031). The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- EPC-authored deliverables for this package (Scope of Work, Package Datasheet, Construction Work Package, EPC Vendor Package Review and Acceptance) are not produced by this deliverable; they are covered by their own `DEL-040-*` entries.
- The detailed vendor document list, numbering scheme, submittal workflow, and turnover record templates are `TBD` because the accessible source set does not include a PKG-040 vendor-document specification.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-040-05-001 | The Vendor Document Turnover Package shall identify `PKG-040`, workbook row 42, WBS 01, CoA tracking number 26020-01-30-031, discipline Electrical, and package name "600V ELECTRICAL BUILDING (860-1)." Source: Workbook Packages row 42; `PACKAGE_REGISTER.csv`. | Identification review against workbook row and Gate 7 registers. |
| REQ-040-05-002 | The Vendor Document Turnover Package shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces and performs vendor-document interface/integration review. Source: `PACKAGE_REGISTER.csv` row `PKG-040`; `DELIVERABLE_REGISTER.csv` row `DEL-040-05`. | Responsibility statement review. |
| REQ-040-05-003 | The Vendor Document Turnover Package shall include the anticipated artifact set: vendor document register, vendor document submittals, source vendor document table rows as artifacts where available, and turnover records. Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`. | Artifact-set completeness review. |
| REQ-040-05-004 | The vendor document register shall enumerate the package deliverable items warranted by the SEC-12 Electrical Basis scope applicable to a 600V general-area / tank-farm electrical building: equipment datasheets (transformers, MCC, distribution, UPS as installed), area-classification basis, load and short-circuit / coordination / arc-flash / load-flow study inputs, grounding and bonding details, cable and raceway design, lighting/receptacles, electric heat tracing, electric building heater data, building HVAC coordination, maintenance access, shipped-loose item lists, and the vendor document register itself. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-12 §"Discipline Scope" (line 2860) and §"Governing Codes, Standards, Specifications, and Studies" (lines 2864–2901). | Register completeness review against the cited SEC-12 source slices. |
| REQ-040-05-005 | The Vendor Document Turnover Package shall preserve all twelve PKG-040 interface facts (Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports) and provide vendor documentation supporting each applicable interface. Source: Workbook Packages row 42; `INTERFACE_REGISTER.csv` rows for `PKG-040`. | Interface coverage check against `INTERFACE_REGISTER.csv`. |
| REQ-040-05-006 | The Vendor Document Turnover Package shall demonstrate that supplied electrical equipment, ratings, and installation provisions are consistent with the project electrical and instrumentation specifications listed in DBM Table 12-1 (ELC-QAS-000001-001 through ELC-QAS-000018-001), in particular ELC-QAS-000003-001 "Electrical Requirements for Packaged Equipment," and with CSA C22.1-21 (Canadian Electrical Code) and applicable BC provincial/local codes. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2864–2892. | Cross-check vendor documents against Table 12-1 specifications and the governing electrical code citation. |
| REQ-040-05-007 | The Vendor Document Turnover Package shall record source gaps as `TBD` rather than invented requirements. Items where source slices do not define content (document numbering scheme, turnover record templates, submittal acceptance criteria, vendor sparing-list specifics) shall remain `TBD` until vendor data or accepted source resolves them. Source: `ARTIFACT_REGISTER.csv` row `ART-EF224E6F34`; `_REFERENCES.md`. | Gap review before turnover acceptance. |
| REQ-040-05-008 | Individual source vendor document table rows shall be captured as artifacts/evidence and not promoted to separate deliverables. Source: `_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv` Notes column. | Artifact-versus-deliverable check. |
| REQ-040-05-009 | The Vendor Document Turnover Package shall be subject to EPC Integrator interface/integration review and shall feed `DEL-040-06_epc-vendor-package-review-and-acceptance`. Source: `DELIVERABLE_REGISTER.csv` rows `DEL-040-05`, `DEL-040-06`. | Handoff review against `DEL-040-06`. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| SEC-12 Electrical Basis (DBM-Deepcut) | Defines the discipline scope, governing codes, electrical specifications, studies, and area-classification basis for electrical packages on this facility. | Applicable; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2856–2913. |
| Project electrical specifications (Table 12-1) | ELC-QAS-000001-001 .. ELC-QAS-000018-001 govern electrical distribution design and equipment procurement; ELC-QAS-000003-001 specifically governs Electrical Requirements for Packaged Equipment. | Applicable; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2872–2892. |
| CSA C22.1-21 (Canadian Electrical Code) | Governing electrical installation code for the project; applicable BC provincial and local electrical codes apply additionally. | Applicable; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2866. |
| Project vendor document control specification | Would govern vendor document numbering, submittal workflow, and turnover format. | ASSUMPTION: applicable; document identity and location `TBD` (no accessible source slice). |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare turnover package identification to workbook row 42 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Artifact-set completeness | Confirm the four anticipated artifact categories (register, submittals, source rows, turnover records) are present. | All four categories are produced or explicitly marked `TBD` with rationale. |
| SEC-12 coverage | Compare vendor document register against the SEC-12 Discipline Scope and Table 12-1 specifications applicable to a 600V general-area/tank-farm building. | All applicable items are listed or explicitly excluded with rationale. |
| Interface coverage | Compare vendor documents to `INTERFACE_REGISTER.csv` rows for `PKG-040`. | All twelve interface facts have corresponding vendor documentation or a recorded gap. |
| Code compliance evidence | Confirm vendor documents cite CSA C22.1-21 and ELC-QAS-000003-001 compliance where applicable. | Compliance statements or test/inspection records present. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |
| EPC review handoff | Confirm the turnover package is presented to the EPC vendor-package review and acceptance flow (`DEL-040-06`). | Handoff evidence recorded. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor document register.
- Vendor document submittals.
- Source vendor document table rows captured as artifacts where available.
- Turnover records.
- Source-gap / `TBD` list for vendor or human resolution (linked to `ART-EF224E6F34`).

The deliverable shall cite the Gate 7 snapshot, workbook row 42, applicable Gate 7 registers, and the DBM-Deepcut SEC-12 source slices used for vendor-document scope basis.
