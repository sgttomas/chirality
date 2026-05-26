# Procedure — DEL-098-06 EPC Vendor Package Review and Acceptance

## Purpose

To produce the EPC Integrator's acceptance evidence for the PKG-098 Tanks, Sour Water (API 650) — 3-25 vendor package: a reviewable, traceable record demonstrating that the vendor scope satisfies the EPC Scope of Work, Package Datasheet, Construction Work Package, and turnover requirements.

## Prerequisites

- **Upstream deliverables available.** The vendor must have submitted (and the EPC must have received) the deliverables enumerated in heading 50 of `_Sources/26020-Package_Requirements.docx` (Vendor Engineered Equipment Package, DEL-098-04; Vendor Document Turnover Package, DEL-098-05).
- **EPC reference deliverables published.** DEL-098-01 (Scope of Work), DEL-098-02 (Package Datasheet), DEL-098-03 (Construction Work Package) must be at a maturity sufficient to serve as acceptance criteria. (No formal upstream dependencies are declared in `_DEPENDENCIES.md`; declared dependencies should be added by `dependency-extract` before acceptance close-out.)
- **Source slices accessible.** `_Sources/26020-Package_Requirements.docx` (heading 50) and `_Sources/26020-Packages_Interfaces_4_export.xlsx` (row 93). Appendix A of heading 50 and `Bid Docs/Budgetary/26020-03-PT-RFQ-19-007 - Sour Water Tanks.docx` should be located if available (TBD).
- **Reviewer authorizations.** Discipline reviewers (mechanical lead, process lead, QA/QC lead, construction lead) named and available.

## Steps

1. **Assemble the canonical checklist.**
   - Extract the vendor deliverable list from heading 50, "Vendor Engineering Deliverables" (PRQ-009 through PIP-009 as drafted in Specification REQ-098-06-01).
   - Create the Vendor Document Review Log with one row per deliverable; columns: Deliverable ID, Deliverable Name, Vendor doc number, Rev, Date received, Reviewer, Disposition, Comment-resolution status, Evidence pointer.

2. **Receive and log vendor documents (DEL-098-05 input).**
   - For each entry in the log, record receipt and route to the appropriate discipline reviewer. Flag missing entries.

3. **Conformance review against Package Datasheet (DEL-098-02).**
   - Build the Datasheet-vs-vendor reconciliation table for each of the seven tanks (TK-9010-1, TK-9020-1, TK-9010-2, TK-9020-2, TK-9030-2, TK-9040-2, TK-9050-2). Record deltas.

4. **Operating-conditions reconciliation.**
   - Reconcile vendor-supplied operating and design conditions against heading 50 ("Atmospheric pressure; 10 °C; further TBD"). Resolve TBDs from vendor data book; escalate any that remain.

5. **MTR traceability (REQ-098-06-04).**
   - Build the MTR traceability matrix: tank-tag × component × heat number × MTR document ID. Verify per-tank coverage at minimum.

6. **ITP / IRC reconciliation (REQ-098-06-03).**
   - Walk each ITP (QLT-003) hold and witness point against IRC (QLT-020) line entries and the Manufacturing Record Book (QLT-021 / PRQ-016 / MEC-023). Flag gaps.

7. **Interface walkdown (REQ-098-06-06).**
   - For each interface row in Package Interfaces row 93, confirm vendor scope matches the Yes/No determination. Record verification evidence (drawing references, tie-in lists from PIP-004, GA from MEC-016 / PIP-006).

8. **FAT review (REQ-098-06-07).**
   - Review FAT procedure (MEC-021) and FAT report (MEC-022); confirm witness signatures and disposition. Note any deferred site tests (hydrotest, settlement, coating) and assign responsibility.

9. **Relief / flare / vent round-trip (REQ-098-06-09).**
   - Cross-reference vendor PRO-015..PRO-018 outputs against EPC PRO-014 inputs; record consistency or escalate divergences.

10. **Logistics, spares, IOM check (REQ-098-06-08).**
    - Confirm receipt and acceptability of Logistics / Shipping Plan (PRQ-013), Spare Parts Interchangeability Record (PRQ-015), Mechanical Spares / Special Tools Requirements (MEC-024), and Equipment IOM Manual (MEC-025).

11. **Compile Package Acceptance Checklist.**
    - Mirror REQ-098-06-01..REQ-098-06-10 with pass/fail/TBD entries and evidence pointers to the artifacts produced in Steps 1-10.

12. **Open-items log and disposition routing (REQ-098-06-10).**
    - Capture every remaining TBD, comment, or conditional disposition with proposed closure path; route per EPC change-management procedure (TBD — location of governing procedure to be confirmed).

13. **Assemble Turnover Evidence.**
    - Bundle Vendor Data Book receipts (PRQ-016 / MEC-023), shipping confirmations (PRQ-013), spares acceptance (PRQ-015 / MEC-024), and IOM manuals (MEC-025) into the turnover evidence set.

14. **Human ruling on Conflict Table.**
    - Surface the Conflict Table from `Guidance.md` to the authorized human approver. Do not self-resolve.

15. **Issue acceptance package.**
    - Authorized human (not the agent) records the binding acceptance disposition. Update `_STATUS.md` per project governance.

## Verification

- Vendor Document Review Log row count equals the heading-50 deliverable count (no missing rows).
- Every requirement REQ-098-06-01..REQ-098-06-10 has a corresponding pass/fail/TBD entry in the Package Acceptance Checklist.
- Every "Yes" interface in Package Interfaces row 93 has a verification evidence pointer; every "No" interface is confirmed absent in vendor scope.
- MTR traceability matrix has at least one MTR document ID per tank in scope.
- ITP/IRC reconciliation shows no unaccounted hold/witness points.
- FAT report is present and signed (or deferred-to-site item is logged with owner).
- Conflict Table conflicts have either a human ruling or a documented deferral.
- Open-items log has a closure plan and owner for every entry.

## Records

- `VendorDocumentReviewLog.md` (or .csv) — REQ-098-06-01.
- `PackageAcceptanceChecklist.md` — mirrors REQ-098-06-01..REQ-098-06-10.
- `Test_Inspection_Evidence/` — MTRs (QLT-013), ITP (QLT-003), IRC (QLT-020), MRB (QLT-021), FAT report (MEC-022), third-party inspection records.
- `Turnover_Evidence/` — Vendor Data Book (PRQ-016 / MEC-023), Logistics Plan (PRQ-013), SPIR (PRQ-015), Special Tools (MEC-024), IOM (MEC-025).
- `OpenItemsLog.md` — REQ-098-06-10.
- `AcceptanceDisposition.md` — human-signed acceptance record.
- Run record under `_run_records/` for each task execution.
