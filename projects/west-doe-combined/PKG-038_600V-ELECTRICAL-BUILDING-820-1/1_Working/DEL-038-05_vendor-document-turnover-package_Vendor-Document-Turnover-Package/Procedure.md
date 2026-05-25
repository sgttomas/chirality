# Procedure: DEL-038-05 — Vendor Document Turnover Package

## Prerequisites

- Accepted upstream decomposition snapshot: Gate 7 (`_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`).
- Package context confirmed: PKG-038 (600V ELECTRICAL BUILDING 820-1), workbook row 40, discipline Electrical, WBS 01.
- Sibling deliverables available for cross-reference when authored: DEL-038-01 SOW; DEL-038-02 Package Datasheet; DEL-038-03 CWP; DEL-038-04 Vendor Engineered Equipment Package; DEL-038-06 EPC Vendor Package Review and Acceptance.
- Reference materials: `_REFERENCES.md`; DBM electrical sections (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`).
- Declared upstream/downstream dependencies: none declared (`_DEPENDENCIES.md`); blockers advisory only.
- TBD: PKG-038-specific row in `26020-Package_Requirements.docx` is not locally located; resolve before finalizing the register.

## Steps

1. **Initialize the Vendor Document Register.** Create a register with at minimum: document number, title, discipline/class, revision, submittal status, EPC review status, due date, current holder, and turnover status. Seed entries from the workbook package-requirements row when located. (TBD: the locked column schema once the EPC Integrator's submittal procedure is published.)
2. **Identify source-required documents.** From the workbook package-requirements basis (`26020-Package_Requirements.docx`) and any vendor purchase-order document lists, enumerate every document the Package Vendor must supply for PKG-038. Carry source vendor document table rows as artifacts where available.
3. **Plan submittals.** For each required document, assign issue revisions (e.g., IFR/IFA/IFC) and due dates aligned with the EPC schedule. (ASSUMPTION pending project submittal procedure.)
4. **Produce vendor documents.** The Package Vendor authors documents in accordance with: governing electrical codes/standards (CSA C22.1-21, BC codes, CSA/API/IEEE/ISA/NEMA); the prefabricated electrical-building construction basis; and PKG-038 interface types listed in the package register row.
5. **Submit and track.** Transmit each document through the EPC submittal workflow; record submittal number, date, reviewer, disposition (e.g., approved / approved as noted / revise and resubmit), and disposition date in the register.
6. **EPC interface/integration review.** EPC Integrator reviews against DEL-038-01 SOW, DEL-038-02 Package Datasheet, DEL-038-03 CWP, and the package's declared interfaces. Comments are returned to the Package Vendor for resolution.
7. **Resolve comments and re-issue.** Package Vendor revises documents, updates revisions in the register, and re-submits until disposition is acceptable.
8. **Assemble turnover records.** Compile certified test reports, factory/site acceptance evidence, inspection certificates, IOM/O&M manuals, spares lists, warranty documents, and as-built drawings into the turnover set. (TBD: exact composition aligned to DEL-038-06.)
9. **Transfer to EPC Integrator.** Issue the turnover package with a transmittal listing every included document; obtain EPC receipt acknowledgement; update the register to show turnover-complete.

## Verification

- Vendor Document Register exists, is current, and reconciles to all submittals and dispositions.
- Every required document has either an accepted submittal or a documented exception with EPC ruling.
- EPC interface/integration review entries exist for each document.
- Turnover-record set is complete against the DEL-038-06 acceptance checklist (when DEL-038-06 is authored).
- Documentation cites and complies with the governing electrical codes/standards.
- No silent change to PKG-038 declared interfaces; deviations are recorded in the review record.

## Records

- Final Vendor Document Register (locked at turnover).
- Submittal log with dispositions and dates.
- EPC Integrator review records.
- Turnover transmittal and EPC receipt acknowledgement.
- Set of source vendor document artifacts carried into the deliverable folder.
- All TBD/Conflict-Table closure rulings recorded against the Conflict IDs in `Guidance.md`.
