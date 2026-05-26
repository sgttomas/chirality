# Procedure — DEL-078-05 Vendor Document Turnover Package

## Purpose

Operational steps for the Package Vendor to produce the Vendor Document Turnover Package for `PKG-078` (Pig Receivers (Inlet) 4-25, equipment tag `26020-01-PT-35-001`), and for EPC Integrator to receive and verify it prior to handoff into `DEL-078-06`.

## Prerequisites

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` read.
- Vendor purchase order and EPC Package Scope of Work (`DEL-078-01`) and Package Datasheet (`DEL-078-02`) issued for construction / fabrication.
- Vendor engineered equipment package (`DEL-078-04`) drafting underway or complete.
- Access to source `_Sources/26020-Package_Requirements.docx` (`26020-01-PT-35-001`) and `_Sources/26020-Packages_Interfaces_4_export.xlsx`.
- Acceptance code scheme and project documentation standard: TBD prerequisite — resolution required before Step 9 acceptance dispositions are issued. Source: not in accessible references.

## Steps

### Production steps (Package Vendor)

1. **Initialize the vendor document register.** Create the register with one row per planned document (number, title, discipline, planned revision, planned issue date, status = PLANNED). Anchor to source list when available (see Step 2).
2. **Reconcile against source-required list.** Compare planned register against `_Sources/26020-Package_Requirements.docx` (`26020-01-PT-35-001 / Vendor Engineering Deliverables`). If source body is empty (current state), open a clarification request to populate it; pending that, mark the register's source-coverage column `TBD` per Conflict Table C-01.
3. **Add equipment-driven documents.** For each item in Major Included Equipment (3x pig receiver assemblies; HIPPS package with PCV, outlet PT, primary and redundant pneumatic hi-low shutdown valves, upstream ESDV; sour-service materials; sweet-gas purge; HP-flare vent), add the corresponding engineering, QA/QC, and O&M document rows. Source: `_Sources/26020-Package_Requirements.docx` Major Included Equipment.
4. **Add safety and code documentation rows.** HIPPS SIL verification, proof-test procedure, pressure-vessel code documentation (code TBD), NACE/MR0175 compliance statement (ASSUMPTION), material test reports, NDE and hydrotest records, welding procedures and PWHT records as applicable to sour service.
5. **Issue documents under controlled transmittals.** For each transmittal, record transmittal number, date, included document numbers and revisions, and intended recipient. Update register status (PLANNED → ISSUED).
6. **Maintain revision discipline.** On each revision, retain prior revisions in the register with status SUPERSEDED and mark the new revision CURRENT.
7. **Include interface evidence.** Cross-reference each interface-bearing document to the relevant rows of `_Sources/26020-Packages_Interfaces_4_export.xlsx` (rows TBD until interface register slice is identified).
8. **Assemble turnover bundle.** Compile the current-revision document set with an index, register snapshot, and transmittal log into the turnover bundle for EPC review.

### Use / verification steps (EPC Integrator)

9. **Receive bundle and record acceptance dispositions.** For each document, assign acceptance disposition under the project's acceptance code scheme (scheme: TBD; see Conflict Table C-04). Record disposition date and reviewer.
10. **Coverage check.** Verify every document class required by source (when populated) appears in the register at current revision with disposition ACCEPTED (or equivalent).
11. **Interface check.** Confirm vendor drawings and interface schedules reconcile with `26020-Packages_Interfaces_4_export.xlsx` and with the EPC Package Datasheet (`DEL-078-02`).
12. **Safety documentation check.** Confirm HIPPS SIL verification, proof-test procedure, and pressure-containing-equipment code documentation are accepted.
13. **Sour-service check.** Confirm material certifications and welding records substantiate the 1.0 mol% sour-service basis (species ASSUMPTION; see Conflict Table C-02).
14. **Final turnover acceptance.** Issue a final turnover acceptance record listing the accepted bundle contents and any open items carried into `DEL-078-06`.

## Verification

| Check | Pass criterion |
|---|---|
| Register exists and is current | Register file present; CURRENT revision flagged per document. |
| Source coverage | Every class in source `Vendor Engineering Deliverables` is in the register (pending population of source list). |
| Equipment coverage | Every Major Included Equipment item has at least one engineering, QA/QC, and O&M document. |
| HIPPS documentation | SIL verification + proof-test docs accepted. |
| Sour-service documentation | Material certs and NACE compliance statement accepted. |
| Interface reconciliation | No unresolved mismatches between vendor drawings and interface register. |
| Acceptance dispositions | Every transmittal disposed under project code scheme (scheme TBD). |
| Final acceptance | Final turnover record issued and signed. |

## Records

- Vendor document register (latest controlled copy).
- Transmittal log.
- Acceptance disposition records per document.
- Final turnover acceptance record.
- Open-items list handed to `DEL-078-06_epc-vendor-package-review-and-acceptance`.
