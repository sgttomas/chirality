# Procedure — DEL-067-05 Vendor Document Turnover Package (PKG-067 Tanks, Sour Water (API 650) 4-25)

## Purpose

Define the operational steps to produce, control, submit, review, and finally turn over the Vendor Document Turnover Package for PKG-067 (sour-water / produced-water atmospheric storage tanks `TK-9010-1` and `TK-9020-1` — ASSUMPTION on tag mapping).

This Procedure addresses how to **produce** the deliverable (Package Vendor activities) and how the **EPC Integrator interfaces** with that production (review and acceptance activities). It is not the vendor's internal engineering or fabrication procedure.

## Prerequisites

- Issued Scope of Work for PKG-067 (DEL-067-01).
- Issued EPC Package Datasheet (DEL-067-02) defining the design basis the vendor is engineering against.
- Vendor engineering kickoff / award (precondition for the Vendor Engineered Equipment Package, DEL-067-04).
- Accessible authoritative reference: `26020-Package_Requirements.docx` package heading 22 — vendor documentation requirements (location TBD; binary source not yet converted).
- Project document control procedure identified and in force (TBD — not in locally accessible sources).
- Declared upstream/downstream dependencies confirmed in `_DEPENDENCIES.md` (currently none declared during PREPARATION).

## Steps

1. **Initialize the Vendor Document Register.**
   - Package Vendor creates the controlled register listing every required document per `26020-Package_Requirements.docx` package heading 22 (location TBD) and the vendor-doc columns of Workbook Packages row 94 (location TBD).
   - Register columns at minimum (ASSUMPTION; project doc-control procedure governs): Document Number, Title, Discipline, Equipment Tag (`TK-9010-1` / `TK-9020-1`), Required-By Date, Planned Submittal Rev., Status, EPC Review Code, Resubmittal Count, Final-for-Turnover flag.
2. **Submit documents per the agreed schedule.**
   - Submittals are transmitted under the project document control procedure (TBD) with sequential transmittal numbers.
   - Each submittal updates the register Status and links the artifact.
3. **EPC Integrator interface/integration review.**
   - EPC reviews each submittal for interface/integration fit (foundation interface, nozzle schedule, drainage / containment, grounding/CP, lighting, I&C — not for vendor internal design correctness).
   - EPC issues a review code per the project review-code matrix (TBD — location TBD).
   - Resubmittals as required; register Resubmittal Count incremented.
4. **Track required API-650 tank code documentation per tag.**
   - For each tank (`TK-9010-1` and `TK-9020-1`): ensure API-650 Manufacturer's data report, plate/shell/bottom MTRs, weld procedure / PQR records, NDE records (shell weld inspection, bottom weld vacuum-box test), hydrostatic test record, and nameplate documentation are produced and routed to the register.
   - Where sour-service material / weld qualification (e.g., NACE MR0175 / ISO 15156) is applicable (ASSUMPTION — TBD pending source confirmation), include qualification and certification records.
5. **Track coating / lining and CP documentation as applicable.**
   - If interior coating / lining is specified for sour-water service: record surface preparation, DFT, holiday-test, and cure documentation.
   - If cathodic protection is within vendor scope (TBD interface boundary): record CP installation and commissioning evidence.
6. **Conduct shop / field testing and record results.**
   - Vendor performs shop tests (and field erection tests where applicable) per the package's QA plan (location TBD), culminating in hydrostatic testing.
   - Test records are added as artifacts and linked to register rows.
7. **Issue as-built / final-revision documents.**
   - Vendor revises drawings, datasheets, and calculations to as-built/as-shipped (or as-erected) status after fabrication/erection completion and hydrostatic testing.
   - Register Final-for-Turnover flag is set when each document reaches its turnover revision and EPC review code allows it.
8. **Assemble the turnover document set.**
   - Compile electronic data book (and paper originals where jurisdictionally required, e.g., API-650 data report originals — ASSUMPTION) covering all register rows flagged Final-for-Turnover.
9. **Issue final turnover transmittal/manifest.**
   - Vendor issues a final transmittal listing every turnover document with its final revision and confirming completeness against the register.
   - EPC Integrator records acceptance (signature/electronic acceptance per project doc-control procedure — location TBD).
10. **Close-out and handoff.**
    - The accepted turnover set becomes the input to DEL-067-06 (EPC Vendor Package Review and Acceptance).
    - Update `_STATUS.md` (deliverable lifecycle managed via `tools/scaffolding/write_status.sh`).

## Verification

- Vendor Document Register is complete: every required document line per source has a row with current status and final-for-turnover disposition.
- Every submitted document has an EPC review code recorded.
- API-650 tank code documentation (data report, MTRs, weld records, NDE, hydrostatic test) is present for both `TK-9010-1` and `TK-9020-1`.
- Coating/lining and CP documentation, where applicable, are present.
- As-built revisions are present in the final set.
- Final turnover transmittal/manifest is issued and EPC acceptance is recorded.
- Workbook Packages row 94 vendor-doc rows (location TBD) are each traceable to a register row.

## Records

The following records evidence successful execution and constitute the deliverable's audit trail:

- Vendor Document Register (controlled, final revision at turnover)
- All vendor document submittals at their final revisions (datasheets, drawings, calculations, MTRs, weld procedures/PQRs, NDE records, hydrostatic test records, coating/lining QA records, API-650 data reports, OEM manuals, spare-parts lists — exact list per `26020-Package_Requirements.docx` package heading 22, location TBD)
- Transmittal log with EPC review codes
- Final turnover transmittal/manifest
- EPC acceptance record
- Updated `_STATUS.md` reflecting lifecycle progression
- This deliverable's `_run_records/` entries
