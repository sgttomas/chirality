# Specification: DEL-025-05_vendor-document-turnover-package

## Scope

This specification governs the Package Vendor-authored Vendor Document Turnover Package for `PKG-025`, the MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD package. The deliverable is an additional Gate 5 deliverable that aggregates the vendor document register, vendor document submittals, source-required vendor documentation, and turnover records for the package, with EPC Integrator interface and integration review.

The package is a vendor-owned Electrical package under WBS 01, CoA 26020-01-30-016. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. The downstream EPC review/acceptance evidence is collected under `DEL-025-06_epc-vendor-package-review-and-acceptance`.

Exclusions:

- Vendor detailed engineering, design, fabrication, and the physical equipment package are scoped to `DEL-025-04_vendor-engineered-equipment-package`, not this deliverable.
- EPC Integrator scope-of-work, datasheet, construction work package, and vendor review/acceptance content are scoped to `DEL-025-01`, `DEL-025-02`, `DEL-025-03`, and `DEL-025-06`, respectively.
- Detailed per-document content (vendor-specific drawing list, revision plan, transmittal IDs, hold codes, turnover record specifics) is `TBD` because no package-specific source slice is locally accessible.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-025-05-001 | The Vendor Document Turnover Package shall identify `PKG-025`, workbook row 27, WBS 01, CoA tracking number 26020-01-30-016, discipline Electrical, and package name "MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD." Source: Workbook Packages row 27; `PACKAGE_REGISTER.csv` row `PKG-025`. | Identity review against workbook row and Gate 7 registers. |
| REQ-025-05-002 | The deliverable shall state the accepted responsibility split: Package Vendor owns the vendor documentation and turnover records; EPC Integrator performs interface/integration review. Source: `PACKAGE_REGISTER.csv` row `PKG-025`; `DELIVERABLE_REGISTER.csv` row `DEL-025-05`. | Responsibility statement review against Gate 7 registers. |
| REQ-025-05-003 | The deliverable shall include the four register-recognised artifact classes: vendor document register, vendor document submittals, source vendor document table rows as artifacts where available, and turnover records. Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-025-05`. | Artifact-class presence check against `DELIVERABLE_REGISTER.csv`. |
| REQ-025-05-004 | The vendor document register shall list each vendor document with at least: identifier, title, revision, status (e.g., for review, code 1/2/3, approved, turnover), submittal date, and turnover state. Source: derived from DBM mechanical packages organisation paragraph requiring a vendor document register. Inferred field-level schema labelled `ASSUMPTION` where source does not enumerate fields. | Register schema review; record schema source gaps as `TBD`. |
| REQ-025-05-005 | The vendor document register shall cover, where applicable to a 6.9 kV MV VFD package, the DBM mechanical packages content categories: datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, and a vendor document register. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, mechanical packages organisation paragraph. Items not applicable to an Electrical VFD package shall be marked N/A with reason. | Cross-check vendor register against DBM category list. |
| REQ-025-05-006 | The deliverable shall preserve the six `PKG-025` applicable interface facts in the vendor documentation set: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 27; `INTERFACE_REGISTER.csv` rows `IFC-812CB082EA`, `IFC-3BE8D26B6B`, `IFC-949E34ECEA`, `IFC-EF46C006CC`, `IFC-3A60522074`, `IFC-FB81FE736B`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-025`. |
| REQ-025-05-007 | Vendor document submittals shall be transmittable and reviewable against the EPC Scope of Work (`DEL-025-01`), Package Datasheet (`DEL-025-02`), and Construction Work Package (`DEL-025-03`), and shall feed the EPC Vendor Package Review and Acceptance deliverable (`DEL-025-06`). Source: `DELIVERABLE_REGISTER.csv` rows `DEL-025-01`, `DEL-025-02`, `DEL-025-03`, `DEL-025-06`. | Cross-deliverable traceability review. |
| REQ-025-05-008 | Turnover records shall be assembled per project turnover requirements; specific record types (FAT, SAT, certifications, calibrations, spare parts, training, as-builts) are `TBD` pending source-supported turnover requirement set. | TBD/open-item review; track as source gap. |
| REQ-025-05-009 | The deliverable shall identify all `TBD` items (detailed register schema, per-document list, turnover record schedule, hold/code list) explicitly rather than inventing values. Source: `ARTIFACT_REGISTER.csv` row `ART-5D23A5F2CB`; source gap review. | Gap review before turnover acceptance. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Project document-control / vendor-document-management standard | Governs vendor document numbering, revisions, transmittals, hold codes, and submittal cycles. | Applicable; document location TBD. |
| EPC turnover standard / handover specification | Governs turnover record content, completion checks, and handover acceptance. | Applicable; document location TBD. |
| DBM mechanical packages organisation paragraph | Establishes the content category set vendor documentation should address. | Source-supported design basis. |
| Project electrical specifications | Govern voltage, grounding, cable/raceway, and MV equipment installation bases referenced by DBM electrical section. | Applicable to documents supporting the Electrical interfaces; document location TBD. |
| Canadian Electrical Code (CEC) | Electrical installation, grounding, and conduit support basis referenced by DBM electrical section. | Applicable to documents supporting the Electrical interfaces; clause locations TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare deliverable identity fields to workbook row 27 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Artifact-class completeness | Compare delivered artifact set to the four `DELIVERABLE_REGISTER.csv` artifact classes. | Vendor document register, submittals, source-vendor-document artifacts, and turnover records are all present or explicitly marked N/A with reason. |
| Interface preservation | Compare vendor documentation interface coverage to `INTERFACE_REGISTER.csv` rows for `PKG-025`. | All six interface facts are represented in the documentation set. |
| Source fidelity | Check every non-trivial requirement or value against cited source slices. | Unsupported values remain `TBD` or `ASSUMPTION`, not treated as confirmed. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv` and `DELIVERABLE_REGISTER.csv`. | Vendor documentation responsibilities and EPC review responsibilities are not conflated. |
| Cross-deliverable traceability | Confirm vendor documents and turnover records align with `DEL-025-01`, `DEL-025-02`, `DEL-025-03`, and `DEL-025-06`. | No orphaned or contradictory references. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and `TBD` items. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor document register.
- Vendor document submittals (transmittals).
- Source vendor document table rows as artifacts where available (vendor documentation gap evidence preserved per `ARTIFACT_REGISTER.csv` row `ART-5D23A5F2CB`).
- Turnover records.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 27, applicable Gate 7 registers, the DBM mechanical packages organisation paragraph, and the DBM electrical source slices applicable to the package's interface facts.
