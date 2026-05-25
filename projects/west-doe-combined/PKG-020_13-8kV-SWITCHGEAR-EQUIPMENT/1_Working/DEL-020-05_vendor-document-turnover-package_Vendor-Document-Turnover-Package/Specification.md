# Specification: DEL-020-05_vendor-document-turnover-package

## Scope

This specification governs the Vendor Document Turnover Package for `PKG-020` 13.8kV Switchgear Equipment. The deliverable comprises:

- the vendor document register;
- vendor document submittals;
- source-required vendor documentation produced for the package;
- turnover records assembled by the Package Vendor.

EPC Integrator interface/integration review is in scope as a review function over the vendor's documentation; EPC ownership of the vendor documentation itself is **out of scope** — that responsibility belongs to the Package Vendor per `PACKAGE_REGISTER.csv` row `PKG-020`.

Excluded:
- Other packages' vendor-document deliverables (`PKG-011`, `PKG-015`, `PKG-016`, `PKG-021`, etc., each have their own turnover deliverable).
- EPC-authored scope, datasheet, construction work package, or acceptance deliverables (`DEL-020-01`, `DEL-020-02`, `DEL-020-03`, `DEL-020-06`).
- Vendor package engineering, design, fabrication, and supply work (covered by `DEL-020-04_vendor-engineered-equipment-package`).

## Requirements

| ID | Requirement | Source / status |
|---|---|---|
| REQ-020-05-01 | The Package Vendor shall produce a vendor document register that lists each vendor document by number, title, type, revision, and status, and shall maintain the register through detailed engineering, fabrication, FAT, shipment, site receipt, SAT, and turnover. | ASSUMPTION (industry-standard practice for MV switchgear vendor documentation); no PKG-020-specific source slice is currently accessible to anchor this requirement. |
| REQ-020-05-02 | The vendor document register shall reflect all submittals required by the EPC Scope of Work (`DEL-020-01`) and Package Datasheet (`DEL-020-02`), and shall reflect all submittals required by `26020-Package_Requirements.docx` once that slice is resolved. | `DELIVERABLE_REGISTER.csv` rows `DEL-020-01`, `DEL-020-02`; `_Sources/26020-Package_Requirements.docx` (location TBD). |
| REQ-020-05-03 | Vendor submittals shall include, at minimum, the documentation classes required to support EPC integration review, factory inspection and test, site receipt, installation, commissioning, operation, and maintenance of the package. Specific list TBD pending the `26020-Package_Requirements.docx` slice and the EPC Package Datasheet. | ASSUMPTION; specific list TBD. |
| REQ-020-05-04 | Turnover records shall include FAT reports, factory test certificates, inspection releases, shipping releases, site receipt inspection records, SAT records, calibration records, and final as-built documentation for the supplied PKG-020 equipment. | ASSUMPTION (industry-standard MV switchgear turnover content); not anchored to PKG-020 source slice. |
| REQ-020-05-05 | The Package Vendor shall provide vendor documentation that demonstrates the package supports the declared package interfaces: Electrical Power, Grounding/Bonding, I&C/Control Cabling, Communications/Network, Maintenance Access, and Structural/Foundations/Supports. | `INTERFACE_REGISTER.csv` PKG-020 rows. |
| REQ-020-05-06 | Vendor documentation shall be transmitted through the project document-control route and shall be controlled by document number, revision, and transmittal record. | ASSUMPTION; project document-control procedure not present in accessible source slice. |
| REQ-020-05-07 | The vendor documentation set shall be sufficient for `DEL-020-06_epc-vendor-package-review-and-acceptance` to perform EPC review and integration acceptance. | `DELIVERABLE_REGISTER.csv` row `DEL-020-06`. |
| REQ-020-05-08 | Source vendor document rows that originate from `_Sources/26020-Package_Requirements.docx` shall be carried as artifacts/evidence on this deliverable, not promoted to standalone deliverables. | `DELIVERABLE_REGISTER.csv` notes column for `DEL-020-05`. |
| REQ-020-05-09 | The vendor document register shall identify each document's status (open / submitted / under review / accepted / superseded) and shall remain auditable through the turnover gate. | ASSUMPTION; no PKG-020-specific source slice currently anchors register-status taxonomy. |

## Standards

| Standard / governing instrument | Applicability | Source / location |
|---|---|---|
| Project document-control procedure | Governs document numbering, transmittal, revision, and acceptance workflows. | TBD; not present in accessible source slice. |
| `26020-Package_Requirements.docx` | Project-issued package-requirements document; expected to define the required vendor-document set for each package. | `_Sources/26020-Package_Requirements.docx` (location TBD; not parsed by this run). |
| Vendor and project quality-assurance standards governing FAT, SAT, and turnover content | Applicable to factory test, site test, and turnover record content. | TBD; not enumerated in the accessible DBM slice. |
| `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` | Project Design Basis Memorandum; does not establish PKG-020 vendor-documentation requirements directly, but is the project-basis context. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`. |

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-020-05-01 | Inspect the vendor document register; confirm presence of number, title, type, revision, status columns; confirm register-update entries through each project gate. |
| REQ-020-05-02 | Cross-walk the register against `DEL-020-01` and `DEL-020-02`, and (when accessible) `26020-Package_Requirements.docx`; record gaps. |
| REQ-020-05-03 | Confirm submittal classes present in the register cover engineering, FAT, SAT, O&M, and as-built scope. |
| REQ-020-05-04 | Inspect the turnover record set against the FAT/factory-test/inspection/shipping/site/SAT/calibration/as-built checklist. |
| REQ-020-05-05 | Trace each PKG-020 interface row in `INTERFACE_REGISTER.csv` to one or more vendor documents in the register; record uncovered interfaces. |
| REQ-020-05-06 | Inspect transmittal records and confirm consistent application of project document-control numbering. |
| REQ-020-05-07 | Confirm `DEL-020-06` reviewer can complete its acceptance checklist using only the turnover documentation set. |
| REQ-020-05-08 | Confirm source vendor document rows from `26020-Package_Requirements.docx` appear as artifacts on this deliverable, not as standalone deliverables. |
| REQ-020-05-09 | Inspect register status field on a sample of documents; confirm an audit trail from open through accepted/superseded. |

## Documentation

The deliverable shall produce or assemble:
- the vendor document register itself (`ART-FA0DE34BAB` once produced, replacing the current "TBD vendor document register" placeholder);
- the body of vendor document submittals (datasheets, drawings, schematics, manuals, BOMs, FAT/SAT records, etc. — specific list TBD);
- source-required vendor documentation rows carried as artifacts/evidence;
- turnover records (FAT, inspection, shipping, SAT, calibration, as-built — specific list TBD).
