# Procedure: DEL-020-05_vendor-document-turnover-package

## Purpose

Produce, control, and turn over the PKG-020 13.8kV switchgear vendor document set — register, submittals, source-required vendor documentation, and turnover records — as a single Package Vendor deliverable with EPC Integrator interface and integration review.

## Prerequisites

- `DEL-020-01_scope-of-work` (EPC Scope of Work) issued or available in working state, to scope what vendor documentation is required.
- `DEL-020-02_package-datasheet` (EPC Package Datasheet) issued or available in working state, to define the technical handoff context.
- `DEL-020-04_vendor-engineered-equipment-package` underway; vendor engineering is the documentation source.
- Access to the project document-control procedure (TBD; currently a gap).
- Access to `_Sources/26020-Package_Requirements.docx` PKG-020 slice (currently not parsed; TBD).
- Confirmation of declared dependency edges in `_DEPENDENCIES.md` (none declared during PREPARATION).
- The package interface set in `INTERFACE_REGISTER.csv` (PKG-020 rows) is available.

## Steps

1. **Initialize the vendor document register.** Establish the register with columns at minimum: document number, title, document type, revision, status, transmittal reference, planned issue date, actual issue date, EPC review status. Seed it from the EPC Scope of Work and Package Datasheet requirements (REQ-020-05-01, REQ-020-05-02).
2. **Resolve the required submittal list.** Parse `_Sources/26020-Package_Requirements.docx` for the PKG-020 vendor-document section; reconcile with the EPC SoW and Package Datasheet; freeze the required submittal list in the register (REQ-020-05-02, REQ-020-05-03). If the source slice cannot be accessed, surface the gap and proceed under documented ASSUMPTION.
3. **Produce vendor submittals.** The Package Vendor produces each required submittal (datasheets, GA/outline drawings, schematics, wiring/termination drawings, BOMs, FAT/SAT plans, manuals, spare-parts lists, etc.). Each submittal is logged in the register at issue and at each revision (REQ-020-05-01, REQ-020-05-06).
4. **Execute factory tests and capture records.** Execute FAT per the vendor's FAT plan; capture FAT reports, factory test certificates, and inspection releases; log each in the register and add to the turnover set (REQ-020-05-04).
5. **Capture shipping, site receipt, SAT, and as-built records.** Generate shipping release, site receipt and inspection records, SAT records, calibration records, and final as-built documentation; log each in the register and add to the turnover set (REQ-020-05-04).
6. **Transmit through project document-control.** Each submittal and turnover record is transmitted to the EPC Integrator through the project document-control route. Numbering, revisions, and transmittal references conform to the project document-control procedure (REQ-020-05-06).
7. **Demonstrate interface coverage.** For each PKG-020 interface row (`IFC-611474D99C`, `IFC-F3098CE7CD`, `IFC-8BF7209227`, `IFC-340091634A`, `IFC-2FB786FC10`, `IFC-08E563D004`), record at least one vendor document in the register that supports that interface (REQ-020-05-05).
8. **Carry source vendor document rows as artifacts.** Any required vendor-document rows traced from `_Sources/26020-Package_Requirements.docx` are recorded as artifacts/evidence on this deliverable, not promoted to separate deliverables (REQ-020-05-08).
9. **Maintain register status through gates.** As each document moves from open → submitted → under review → accepted/superseded, update the register field and preserve the audit trail (REQ-020-05-09).
10. **Hand off to EPC review and acceptance.** Provide the complete and current turnover set to `DEL-020-06_epc-vendor-package-review-and-acceptance` for EPC review and integration acceptance (REQ-020-05-07).

## Verification

- The vendor document register is complete, current, and consistent with the EPC Scope of Work, the EPC Package Datasheet, and the resolved PKG-020 slice of `26020-Package_Requirements.docx`.
- Each PKG-020 interface row is covered by at least one vendor document in the register.
- The turnover set includes the FAT/factory-test/inspection/shipping/site/SAT/calibration/as-built record classes (specific list TBD against project quality-assurance standards).
- Each transmittal can be traced from document-control records back to a register row and forward to an EPC review disposition.
- `DEL-020-06` reviewer can complete its acceptance checklist using only the turnover documentation set without requesting documents that should have been in the register.

## Records

- Vendor document register (`ART-FA0DE34BAB` once produced).
- Vendor document submittals (datasheets, drawings, schematics, manuals, BOMs, plans — specific list TBD).
- Source vendor document rows carried as artifacts/evidence.
- Turnover records: FAT reports, factory test certificates, inspection releases, shipping releases, site receipt inspection records, SAT records, calibration records, final as-built documentation.
- Document-control transmittal records.
- Register-status audit trail from open through accepted/superseded.
