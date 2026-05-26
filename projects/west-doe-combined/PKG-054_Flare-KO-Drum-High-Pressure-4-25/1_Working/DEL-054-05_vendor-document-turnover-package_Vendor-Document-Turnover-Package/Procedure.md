# Procedure — DEL-054-05 Vendor Document Turnover Package (PKG-054 Flare KO Drum (High Pressure) 4-25)

## Purpose

Define the operational steps to produce, control, submit, review, and finally turn over the Vendor Document Turnover Package for PKG-054 (HP flare KO drum `V-4100-1` and HP flare KO drum transfer pump `P-4100-1`).

This Procedure addresses how to **produce** the deliverable (Package Vendor activities) and how the **EPC Integrator interfaces** with that production (review and acceptance activities). It is not the vendor's internal engineering procedure.

## Prerequisites

- Issued Scope of Work for PKG-054 (DEL-054-01).
- Issued EPC Package Datasheet (DEL-054-02) defining the design basis the vendor is engineering against.
- Vendor engineering kickoff / award (precondition for the Vendor Engineered Equipment Package, DEL-054-04).
- Accessible authoritative reference: `26020-Package_Requirements.docx` package heading 9 — vendor documentation requirements (location TBD; binary source not yet converted).
- Project document control procedure identified and in force (TBD — not in locally accessible sources).
- Declared upstream/downstream dependencies confirmed in `_DEPENDENCIES.md` (currently none declared during PREPARATION).

## Steps

1. **Initialize the Vendor Document Register.**
   - Package Vendor creates the controlled register listing every required document per `26020-Package_Requirements.docx` package heading 9 (location TBD) and the vendor-doc columns of Workbook Packages row 55 (location TBD).
   - Register columns at minimum (ASSUMPTION; project doc-control procedure governs): Document Number, Title, Discipline, Equipment Tag (`V-4100-1` / `P-4100-1`), Required-By Date, Planned Submittal Rev., Status, EPC Review Code, Resubmittal Count, Final-for-Turnover flag.
2. **Submit documents per the agreed schedule.**
   - Submittals are transmitted under the project document control procedure (TBD) with sequential transmittal numbers.
   - Each submittal updates the register Status and links the artifact.
3. **EPC Integrator interface/integration review.**
   - EPC reviews each submittal for interface/integration fit (not for vendor internal design correctness).
   - EPC issues a review code per the project review-code matrix (TBD — location TBD).
   - Resubmittals as required; register Resubmittal Count incremented.
4. **Track required pressure-vessel and rotating-equipment code documentation.**
   - For `V-4100-1`: ensure ASME / jurisdictional data report (e.g., U-1A), MTRs, NDE records, and code stamping documentation are produced and routed to the register (ASSUMPTION on ASME applicability — TBD pending source confirmation).
   - For `P-4100-1`: ensure pump shop performance/test records, materials documentation, and OEM manuals are produced and routed.
5. **Conduct Factory Acceptance Test (FAT) and record results.**
   - Vendor performs FAT per the package's QA/FAT plan (location TBD).
   - FAT records are added as artifacts and linked to register rows.
6. **Issue as-built / final-revision documents.**
   - Vendor revises drawings, datasheets, and calculations to as-built/as-shipped status after fabrication completion and FAT.
   - Register Final-for-Turnover flag is set when each document reaches its turnover revision and EPC review code allows it.
7. **Assemble the turnover document set.**
   - Compile electronic data book (and paper originals where jurisdictionally required, e.g., U-1A originals — ASSUMPTION) covering all register rows flagged Final-for-Turnover.
8. **Issue final turnover transmittal/manifest.**
   - Vendor issues a final transmittal listing every turnover document with its final revision and confirming completeness against the register.
   - EPC Integrator records acceptance (signature/electronic acceptance per project doc-control procedure — location TBD).
9. **Close-out and handoff.**
   - The accepted turnover set becomes the input to DEL-054-06 (EPC Vendor Package Review and Acceptance).
   - Update `_STATUS.md` (deliverable lifecycle managed via `tools/scaffolding/write_status.sh`).

## Verification

- Vendor Document Register is complete: every required document line per source has a row with current status and final-for-turnover disposition.
- Every submitted document has an EPC review code recorded.
- Pressure-vessel and rotating-equipment code documentation is present for `V-4100-1` and `P-4100-1`.
- FAT records and as-built revisions are present in the final set.
- Final turnover transmittal/manifest is issued and EPC acceptance is recorded.
- Workbook Packages row 55 vendor-doc rows (location TBD) are each traceable to a register row.

## Records

The following records evidence successful execution and constitute the deliverable's audit trail:

- Vendor Document Register (controlled, final revision at turnover)
- All vendor document submittals at their final revisions (datasheets, drawings, calculations, MTRs, NDE records, code certifications, FAT records, OEM manuals, spare-parts lists — exact list per `26020-Package_Requirements.docx` package heading 9, location TBD)
- Transmittal log with EPC review codes
- Final turnover transmittal/manifest
- EPC acceptance record
- Updated `_STATUS.md` reflecting lifecycle progression
- This deliverable's `_run_records/` entries
