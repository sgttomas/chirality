# Procedure — DEL-064-05 Vendor Document Turnover Package (PKG-064 Tanks, Water (API 650) 4-25)

## Purpose

Define the operational steps to produce, control, submit, review, and finally turn over the Vendor Document Turnover Package for PKG-064 (Process Water Storage Tanks `TK-5317-1` and `TK-5318-1`).

This Procedure addresses how to **produce** the deliverable (Package Vendor activities) and how the **EPC Integrator interfaces** with that production (review and acceptance activities). It is not the vendor's internal engineering procedure.

## Prerequisites

- Issued Scope of Work for PKG-064 (DEL-064-01).
- Issued EPC Package Datasheet (DEL-064-02) defining the design basis the vendor is engineering against.
- Vendor engineering kickoff / award (precondition for the Vendor Engineered Equipment Package, DEL-064-04).
- Accessible authoritative reference: `26020-Package_Requirements.docx` package heading 19 — vendor documentation requirements (location TBD; binary source not yet converted).
- Project document control procedure identified and in force (TBD — not in locally accessible sources).
- Declared upstream/downstream dependencies confirmed in `_DEPENDENCIES.md` (currently none declared during PREPARATION).

## Steps

1. **Initialize the Vendor Document Register.**
   - Package Vendor creates the controlled register listing every required document per `26020-Package_Requirements.docx` package heading 19 (location TBD) and the vendor-doc columns of Workbook Packages row 96 (location TBD).
   - Register columns at minimum (ASSUMPTION; project doc-control procedure governs): Document Number, Title, Discipline, Equipment Tag (`TK-5317-1` / `TK-5318-1` / COMMON), Required-By Date, Planned Submittal Rev., Status, EPC Review Code, Resubmittal Count, Final-for-Turnover flag.
2. **Submit documents per the agreed schedule.**
   - Submittals are transmitted under the project document control procedure (TBD) with sequential transmittal numbers.
   - Each submittal updates the register Status and links the artifact.
3. **EPC Integrator interface/integration review.**
   - EPC reviews each submittal for interface/integration fit (not for vendor internal design correctness).
   - EPC issues a review code per the project review-code matrix (TBD — location TBD).
   - Resubmittals as required; register Resubmittal Count incremented.
4. **Track API-650 design and fabrication documentation.**
   - Issue design calculations (shell, bottom, roof, anchorage, settlement, seismic, wind as applicable) per the modified API-650 basis (16 oz test pressure per DBM).
   - Issue welding procedure specifications and qualification records (WPS/PQR/WPQ).
   - Issue materials test reports (MTRs) and code certifications per tank.
   - Source: `4-25_Deepcut_DBM.md` line 518.
5. **Track field erection, NDE, and hydrotest records.**
   - For each tank (`TK-5317-1`, `TK-5318-1`): collect NDE records (RT/UT/PT/MT/VT as applicable) and hydrotest / leak-test records; link to register rows.
6. **Track coating, insulation, and heat-trace records.**
   - Internal coating: Devchem 253 on floor, walls, and roof — collect surface-prep, application, DFT/holiday-test inspection records per tank.
   - External insulation: collect installation records per tank.
   - Heat tracing: collect circuit drawings, installation records, and commissioning records per tank to evidence freeze-protection requirement.
   - Sources: `4-25_Deepcut_DBM.md` lines 524, 2509.
7. **Track appurtenance documentation.**
   - PVRV (each tank has at least one per DBM) sizing and certification.
   - EPRV sizing documentation (DBM notes EPRV sizing is to be reviewed during detailed engineering — record the as-finalized basis).
   - Kennilworth-type hydrocarbon skim float system documentation.
   - Nozzles, manways, ladders/platforms, gauging/level instruments, isolation valves.
   - Source: `4-25_Deepcut_DBM.md` line 524.
8. **Issue as-built / final-revision documents.**
   - Vendor revises drawings, datasheets, and calculations to as-built status after field erection, hydrotest, coating, insulation, and heat-trace commissioning are complete.
   - Register Final-for-Turnover flag is set when each document reaches its turnover revision and EPC review code allows it.
9. **Assemble the turnover document set.**
   - Compile electronic data book (and paper originals where jurisdictionally required — ASSUMPTION) covering all register rows flagged Final-for-Turnover, organized per tank where applicable.
10. **Issue final turnover transmittal/manifest.**
    - Vendor issues a final transmittal listing every turnover document with its final revision and confirming completeness against the register.
    - EPC Integrator records acceptance (signature/electronic acceptance per project doc-control procedure — location TBD).
11. **Close-out and handoff.**
    - The accepted turnover set becomes the input to DEL-064-06 (EPC Vendor Package Review and Acceptance).
    - Update `_STATUS.md` (deliverable lifecycle managed via `tools/scaffolding/write_status.sh`).

## Verification

- Vendor Document Register is complete: every required document line per source has a row with current status and final-for-turnover disposition.
- Every submitted document has an EPC review code recorded.
- API-650 design package, WPS/PQR/WPQ, MTRs, NDE, and hydrotest records are present for both `TK-5317-1` and `TK-5318-1`.
- Internal coating (Devchem 253), insulation, and heat-trace records are present per tank.
- PVRV/EPRV documentation, skim float system documentation, and appurtenance records are present per tank.
- As-built revisions are present in the final set.
- Final turnover transmittal/manifest is issued and EPC acceptance is recorded.
- Workbook Packages row 96 vendor-doc rows (location TBD) are each traceable to a register row.

## Records

The following records evidence successful execution and constitute the deliverable's audit trail:

- Vendor Document Register (controlled, final revision at turnover)
- All vendor document submittals at their final revisions (design calcs, drawings, WPS/PQR/WPQ, MTRs, NDE records, hydrotest records, coating records, insulation records, heat-trace records, PVRV/EPRV documentation, OEM manuals, spare-parts lists — exact list per `26020-Package_Requirements.docx` package heading 19, location TBD)
- Transmittal log with EPC review codes
- Final turnover transmittal/manifest
- EPC acceptance record
- Updated `_STATUS.md` reflecting lifecycle progression
- This deliverable's `_run_records/` entries
