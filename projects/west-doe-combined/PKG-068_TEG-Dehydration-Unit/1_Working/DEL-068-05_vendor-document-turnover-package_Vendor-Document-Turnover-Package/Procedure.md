# Procedure — DEL-068-05 Vendor Document Turnover Package (PKG-068 TEG Dehydration Unit)

## Purpose

Define the operational steps to produce, control, submit, review, and finally turn over the Vendor Document Turnover Package for PKG-068 — TEG Dehydration Unit (CoA 26020-01-PT-22-001).

This Procedure addresses how to **produce** the deliverable (Package Vendor activities) and how the **EPC Integrator interfaces** with that production (review and acceptance activities). It is not the vendor's internal engineering procedure.

## Prerequisites

- Issued Scope of Work for PKG-068 (DEL-068-01).
- Issued EPC Package Datasheet (DEL-068-02) defining the design basis the vendor is engineering against.
- Vendor engineering kickoff / award (precondition for the Vendor Engineered Equipment Package, DEL-068-04).
- Accessible authoritative reference: `26020-Package_Requirements.docx` package heading 23 — vendor documentation requirements (read via text-extracted slice for this draft).
- Vendor-issued DOC-008 Vendor Document Control Procedure in place (governs submittal mechanics).
- Project document control procedure (EPC-side controlling instance) identified and in force — TBD (not in locally accessible sources).
- Declared upstream/downstream dependencies confirmed in `_DEPENDENCIES.md` (currently none declared during PREPARATION).

## Steps

1. **Issue DOC-008 and initialize PRQ-009 Vendor Document Index.**
   - Package Vendor issues DOC-008 (Vendor Document Control Procedure) defining submittal format, file naming, transmittal codes, and review cycles.
   - Package Vendor creates the controlled PRQ-009 register listing every required document per `26020-Package_Requirements.docx` package heading 23 (twelve grouped subsections) and the vendor-doc columns of Workbook Packages row 97 (location TBD).
   - Register columns at minimum (ASSUMPTION; DOC-008 governs final form): Document Number, Title, Subsection (per heading 23 grouping), Discipline, Equipment Tag(s) (TEG Contactor / Glycol Flash Tank / Glycol Circulation Pumps / etc.), Required-By Date, Planned Submittal Rev., Status, EPC Review Code, Resubmittal Count, Final-for-Turnover flag.
2. **Submit documents per the agreed schedule.**
   - Submittals are transmitted under DOC-008 with sequential transmittal numbers.
   - Each submittal updates the register Status and links the artifact.
3. **EPC Integrator interface/integration review.**
   - EPC reviews each submittal for interface/integration fit (not for vendor internal design correctness).
   - EPC issues a review code per the project review-code matrix (TBD — location TBD).
   - Resubmittals as required; register Resubmittal Count incremented.
4. **Track required pressure-equipment documentation for the static vessels.**
   - For each static pressure item (TEG Contactor; Glycol Flash Tank; Fuel Gas Scrubber; TEG Make-up Tank where applicable): ensure MEC-005, MEC-009, REG-022 are produced, including ASME / jurisdictional data reports, MTRs (QLT-013), NDE records, and code stamping documentation (ASSUMPTION on ASME applicability — TBD pending source confirmation).
5. **Track rotating-equipment documentation for the Glycol Circulation Pumps.**
   - Ensure MEC-004, MEC-007, MEC-019, PRO-013, ELE-011 (motor starting study) are produced and routed.
6. **Track heat-transfer-equipment documentation.**
   - For Inlet Air Cooler, Gas/Glycol Exchanger, Air/Glycol Exchanger, and Glycol Reboiler/Still Column: ensure MEC-010 data sheets and the relevant MEC-014 calculation package sections.
7. **Track Burner Control Panel and fired-equipment safety documentation.**
   - Ensure CTL-003 (Control Narrative / Functional Specification), CTL-005 (Cause and Effect Matrix), CTL-026 (Package Vendor Interface Specification), TSF-009, TSF-011, TSF-013 are produced for the BMS and reboiler-related safety functions.
8. **Conduct Factory Acceptance Test (FAT) and record results.**
   - Vendor performs FAT per MEC-021 (Equipment FAT / Performance Test Procedure).
   - FAT results recorded in MEC-022 (Equipment FAT / Performance Test Report); ELE-029/ELE-030 cover electrical FAT/SAT and test/energization records.
   - FAT records are added as artifacts and linked to register rows.
9. **Issue as-built / final-revision documents.**
   - Vendor revises drawings, datasheets, and calculations to as-built/as-shipped status after fabrication completion and FAT, producing PRO-028 (Process As-Built PFD/P&ID Package), PIP-028 (Piping As-Built Drawings), and INS-029 (Instrument As-Built Drawings) among the final as-built set.
   - Register Final-for-Turnover flag is set when each document reaches its turnover revision and EPC review code allows it.
10. **Assemble the turnover document set.**
    - Compile the electronic data book(s) covering all register rows flagged Final-for-Turnover, consolidating per the project doc-control choice into PRQ-016 (Vendor Data Book / Final Supplier Documentation), QLT-021 (Manufacturing Record Book / Vendor Data Book), and/or MEC-023 (Vendor Data Book / Mechanical Final Documentation). Paper originals provided where jurisdictionally required for pressure-equipment registration (REG-022 supporting originals — ASSUMPTION).
    - Include MEC-025 (Mechanical Equipment IOM Manual) and PRQ-015 (SPIR).
11. **Issue final turnover transmittal/manifest.**
    - Vendor issues a final transmittal listing every turnover document with its final revision and confirming completeness against PRQ-009.
    - EPC Integrator records acceptance (signature/electronic acceptance per project doc-control procedure — location TBD).
12. **Close-out and handoff.**
    - The accepted turnover set becomes the input to DEL-068-06 (EPC Vendor Package Review and Acceptance).
    - Update `_STATUS.md` (deliverable lifecycle managed via `tools/scaffolding/write_status.sh`).

## Verification

- DOC-008 issued; PRQ-009 Vendor Document Index initialized and maintained.
- PRQ-009 is complete: every required document line per heading 23 has a row with current status and final-for-turnover disposition (or an EPC-concurred non-applicability note).
- Every submitted document has an EPC review code recorded.
- Static pressure-vessel code documentation (MEC-009, REG-022, QLT-013) is present for each static vessel in the package.
- Rotating-equipment documentation (MEC-007, MEC-019, PRO-013, ELE-011) is present for the Glycol Circulation Pumps.
- Heat-exchanger data sheets (MEC-010) are present for each heat-transfer item.
- BMS / fired-equipment safety records (CTL-003, CTL-005, TSF-011) are present.
- FAT records (MEC-022; ELE-030) and as-built revisions (PRO-028, PIP-028, INS-029) are present in the final set.
- Final turnover transmittal/manifest is issued and EPC acceptance is recorded.
- Workbook Packages row 97 vendor-doc rows (location TBD) are each traceable to a register row.

## Records

The following records evidence successful execution and constitute the deliverable's audit trail:

- PRQ-009 Vendor Document Index (controlled, final revision at turnover)
- DOC-008 Vendor Document Control Procedure
- All vendor document submittals at their final revisions across the twelve subsections enumerated in `26020-Package_Requirements.docx` package heading 23
- Transmittal log with EPC review codes
- Final turnover deliverables: PRQ-016 Vendor Data Book / Final Supplier Documentation; QLT-021 Manufacturing Record Book / Vendor Data Book; MEC-023 Vendor Data Book / Mechanical Final Documentation
- Final turnover transmittal/manifest and EPC acceptance record
- MEC-025 Mechanical Equipment IOM Manual; PRQ-015 SPIR
- Updated `_STATUS.md` reflecting lifecycle progression
- This deliverable's `_run_records/` entries
