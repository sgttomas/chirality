# Specification: DEL-037-05_vendor-document-turnover-package

## Scope

This specification governs the Vendor Document Turnover Package for `PKG-037`, the 5kV SWITCHGEAR ELECTRICAL BUILDING (880-1) package. The deliverable is a Gate 5 vendor-owned package deliverable consisting of the vendor document register, vendor document submittals, source-required vendor document table rows carried as artifacts where available, and final turnover records, with EPC Integrator interface/integration review.

The package is a vendor-owned Electrical package under WBS 01. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. EPC acceptance of the vendor package as a whole is the separate deliverable `DEL-037-06_epc-vendor-package-review-and-acceptance`.

Exclusions:

- Vendor detailed-design content (calculations, certified drawings, equipment selections) is conveyed *through* this deliverable as documents but is not itself authored by this deliverable; the deliverable is the document register, submittals, and turnover record set.
- Detailed package-specific vendor document indices, hold/issue codes, submittal-stage definitions, and turnover acceptance criteria are `TBD` because the accessible source set does not provide confirmed package-specific values.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-037-05-001 | The deliverable shall identify `PKG-037`, workbook row 39, WBS 01, CoA tracking number 26020-01-30-028, discipline Electrical, and package name "5kV SWITCHGEAR ELECTRICAL BUILDING (880-1)." Source: Workbook Packages row 39; `PACKAGE_REGISTER.csv`. | Identity review against workbook row and Gate 7 registers. |
| REQ-037-05-002 | The deliverable shall state the accepted responsibility split: Package Vendor owns vendor documentation and physical equipment; EPC Integrator performs interface/integration review. Source: `PACKAGE_REGISTER.csv` row `PKG-037`; `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`. | Responsibility statement review against Gate 7 register. |
| REQ-037-05-003 | The deliverable shall include a vendor document register covering all vendor-produced documents required to design, fabricate, ship, install, commission, and operate the package. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, mechanical package deliverables paragraph (line 617). | Register existence and completeness review. |
| REQ-037-05-004 | The deliverable shall include vendor submittals tracked by the document register, with revision and transmittal control. Source: `_CONTEXT.md`, anticipated artifacts. | Submittal log/transmittal review. |
| REQ-037-05-005 | Where individual source vendor-document table rows are available, the deliverable shall carry them as artifacts/evidence rather than as separate deliverables. Source: `_CONTEXT.md`, notes; `DELIVERABLE_REGISTER.csv` row `DEL-037-05`. | Artifact register cross-check. |
| REQ-037-05-006 | The deliverable shall include final turnover records covering documentation required for handover to operations. Source: `_CONTEXT.md`, anticipated artifacts. | Turnover record completeness review. |
| REQ-037-05-007 | The deliverable shall represent the twelve applicable interface facts for `PKG-037` (Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports) within the vendor documentation that crosses each interface. Source: Workbook Packages row 39; `INTERFACE_REGISTER.csv`. | Interface matrix check. |
| REQ-037-05-008 | The deliverable shall identify source gaps for vendor document register schema, hold/issue codes, submittal stages, and turnover acceptance criteria as `TBD` instead of invented values. Source: `_REFERENCES.md`; `ARTIFACT_REGISTER.csv` `ART-8E3FB7B466` (Vendor Documentation Gap Evidence). | Gap review before vendor handoff and EPC acceptance. |
| REQ-037-05-009 | The deliverable shall preserve source spelling and identity (package name including the parenthetical "(880-1)") as recorded in Workbook row 39 and `PACKAGE_REGISTER.csv`. Source: Workbook Packages row 39. | Spelling/identity review. |
| REQ-037-05-010 | The deliverable shall not duplicate or supersede `DEL-037-06_epc-vendor-package-review-and-acceptance`; EPC acceptance of the overall vendor package is a separate deliverable. Source: `DELIVERABLE_REGISTER.csv` rows `DEL-037-05` and `DEL-037-06`. | Scope-boundary review. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Governs electrical installation basis referenced by DBM electrical section and applicable to MV switchgear electrical buildings. | Applicable; clause locations TBD. |
| Project medium-voltage cable / insulation basis | 5 kV insulation class for 4.160 kV MV TECK cable; aligns with the "5kV" package naming. Vendor documentation shall reflect facility MV class. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MV cable table (line 3009). |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable to electrical equipment installation classification where hazardous/non-hazardous areas are defined. | Applicable; package location/classification TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare deliverable identity fields to workbook row 39 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Vendor document register presence | Confirm a vendor document register is part of the turnover package. | Register exists and is referenced by `ARTIFACT_REGISTER.csv` row `ART-8E3FB7B466` (initially `TBD` content). |
| Interface completeness | Compare vendor document/turnover content to `INTERFACE_REGISTER.csv` rows for `PKG-037`. | All twelve interface facts are represented in vendor documentation that crosses each interface. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv` and `_CONTEXT.md`. | Vendor and EPC scopes are not conflated; EPC acceptance is routed to `DEL-037-06`. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and `TBD` items. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor document register (initial scope per `ART-8E3FB7B466`; detailed content `TBD`).
- Vendor document submittals (transmittals and revision control).
- Source vendor document table rows carried as artifacts/evidence (where available).
- Final turnover records.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 39, applicable Gate 7 registers, and the DBM source slices used for package-deliverable basis and 5 kV insulation class.
