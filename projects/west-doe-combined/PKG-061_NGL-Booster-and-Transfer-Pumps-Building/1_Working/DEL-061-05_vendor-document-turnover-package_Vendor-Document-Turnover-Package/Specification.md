# Specification — DEL-061-05 Vendor Document Turnover Package

## Scope

### In scope
- Single Package Vendor deliverable producing, controlling, transmitting, and turning over the vendor document set for PKG-061 (NGL Booster and Transfer Pumps Building) to the EPC Integrator.
- Vendor document register listing every document the vendor will submit for the package.
- Vendor document submittals through the project document control workflow.
- Source-required vendor documentation (the documents listed under the Mechanical/rotating-equipment "Vendor Engineering Deliverables" set — see Datasheet "Construction" table).
- Turnover records demonstrating completion of the document set and acceptance by the EPC Integrator.
- EPC Integrator review at the package interface (review/comment cycles, acceptance gates).

### Out of scope
- The engineered equipment itself (covered by `DEL-061-04`).
- EPC vendor package review/acceptance closeout (covered by `DEL-061-06`).
- Standalone document rows are evidence artifacts, not separate deliverables (per decomposition note, register row 418).
- Interface types not flagged on Workbook row 75: Cathodic Protection; Communications/Network; Grading/Site Drainage/Spill Containment; Product Loading; Pipeline/Pigging (`_Sources/26020-Packages_Interfaces_4_export.xlsx` row 75).

## Requirements

| Req ID | Requirement | Source / Basis |
|---|---|---|
| R-01 | The vendor SHALL produce a Vendor Document Index (PRQ-009) enumerating every document in the turnover scope, with document number, revision, status, and planned issue date. | `_Sources/26020-Package_Requirements.docx` Tank Pumps "Vendor Engineering Deliverables" → PRQ-009. ASSUMPTION applies to PKG-061. |
| R-02 | The vendor SHALL operate per a Vendor Document Control Procedure (DOC-008) for numbering, revision, transmittal, and status tracking. | ibid. → DOC-008. |
| R-03 | The vendor SHALL submit each document group listed in the Datasheet "Construction" table at the revisions required by the project document workflow (e.g., IFR / IFA / IFC / AB). | ibid. (set membership). Workflow stages: ASSUMPTION — specific revision matrix location TBD. |
| R-04 | Documents covering interfaces flagged `X` on Workbook row 75 SHALL be included; documents addressing non-applicable interfaces (Cathodic Protection; Communications/Network; Grading/Drainage/Spill; Product Loading; Pipeline/Pigging) SHALL be marked N/A unless explicitly required by EPC. | `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 75. |
| R-05 | The vendor SHALL deliver a final Vendor Data Book / Manufacturing Record Book (PRQ-016 / QLT-021 / MEC-023) at turnover, consolidating final-issue documents, certificates, and test records. | `_Sources/26020-Package_Requirements.docx` Tank Pumps "Vendor Engineering Deliverables" → PRQ-016, QLT-021, MEC-023. |
| R-06 | The vendor SHALL provide turnover records (transmittal log, document status report at handover, sign-off acceptance) for EPC Integrator review. | Decomposition row 418 (`turnover records`). |
| R-07 | The vendor document set SHALL include Inspection and Test Plan (QLT-003), Material Test Reports (QLT-013), Inspection Release Certificate (QLT-020), and FAT/Performance reports (MEC-021, MEC-022). | `_Sources/26020-Package_Requirements.docx` Tank Pumps "Vendor Engineering Deliverables". |
| R-08 | The EPC Integrator SHALL review submitted documents at the interfaces enumerated in the Datasheet "Conditions" table (Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety; Maintenance Access; Structural/Foundations/Supports). | `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 75. |
| R-09 | Spare Parts Interchangeability Record (PRQ-015) and Logistics/Shipping Plan (PRQ-013) SHALL be issued in time to support EPC procurement and site logistics. | `_Sources/26020-Package_Requirements.docx` Tank Pumps "Vendor Engineering Deliverables" → PRQ-013, PRQ-015. |

## Standards

| Standard | Applicability | Location |
|---|---|---|
| Project document control procedure (DOC-008 as governed) | Document numbering, revisioning, transmittal | `_Sources/26020-Package_Requirements.docx` reference; full text location TBD |
| Project Quality Plan basis (QLT-006) | Vendor supplier quality plan compliance | ibid.; location TBD |
| Equipment-specific codes (e.g., API for rotating equipment, electrical/IEC, NFPA for fire & gas) | Apply through the underlying engineering documents (MEC-004, ELE-*, TSF-*) | Standards list TBD — not enumerated in accessible source slice |

## Verification

| Req | Verification approach |
|---|---|
| R-01 | Document review: confirm PRQ-009 is issued and matches the set in this Specification + Datasheet Construction table. |
| R-02 | Document review: DOC-008 issued and applied to subsequent submittals. |
| R-03 | Submittal log review: each listed document submitted at required revisions; gaps reported. |
| R-04 | Cross-check against Workbook row 75: any document for a non-applicable interface is marked N/A or justified. |
| R-05 | Inspection of final Vendor Data Book at handover; verify consolidation completeness. |
| R-06 | Turnover record inspection (transmittal log, document status report, sign-off). |
| R-07 | Quality records inspection (ITP/MTR/IRC/FAT records present). |
| R-08 | EPC Integrator review log shows interface reviews performed and dispositioned. |
| R-09 | Schedule check: PRQ-013/PRQ-015 issued ahead of relevant downstream needs. |

## Documentation

Artifacts produced under this deliverable:
- Vendor Document Register (the index — PRQ-009 instance for PKG-061).
- Vendor Document Submittals (transmittals + revisions through life of package).
- Source-required vendor documentation (all documents listed in Datasheet Construction table; the documents themselves are artifacts/evidence, not separate deliverables).
- Turnover Records (transmittal log, final status report, EPC acceptance sign-off, Vendor Data Book).
