# Procedure — EPC Vendor Package Review and Acceptance (DEL-099-06)

> Operational document. How the EPC Integrator produces the review and acceptance evidence package for the Truck Product Loading vendor package serving Unit 3-25.

## Purpose

Define the sequence of actions the EPC Integrator follows to review the vendor-engineered Truck Product Loading package (DEL-099-04) and the Vendor Document Turnover (DEL-099-05), and to produce the acceptance evidence (DEL-099-06) against the EPC SOW (DEL-099-01), Package Datasheet (DEL-099-02), and Construction Work Package (DEL-099-03).

## Prerequisites

- Sibling deliverables available or in progress:
  - DEL-099-01 EPC Scope of Work
  - DEL-099-02 EPC Package Datasheet
  - DEL-099-03 EPC Construction Work Package
  - DEL-099-04 Vendor Engineered Equipment Package
  - DEL-099-05 Vendor Document Turnover Package
- Local references identified in `_REFERENCES.md`, including the DBM `3-25_Comp_and_Liquids_DBM.md` (SEC-03, SEC-04, SEC-06, SEC-08, SEC-09, SEC-13, SEC-16, SEC-17, SEC-18).
- Declared upstream/downstream dependencies (none formally declared as of `_DEPENDENCIES.md` 2026-05-24; ASSUMPTION: DEL-099-01..05 are *de facto* upstream).
- Truck rack permit status (BCER 100120203 amendment) confirmed or recorded as outstanding (DBM SEC-18).
- Identified EPC Integrator review lead and assigned discipline reviewers (Process, Mechanical, Piping, Electrical, Instrumentation, Controls, Civil, HSE) — TBD assignment.

## Steps

1. **Initiate acceptance package.**
   - Create or maintain the four artifacts listed under Records (review log, checklist, test/inspection index, turnover index) in this deliverable folder.
   - Record reviewers and roles.

2. **Vendor document review.**
   - For each document delivered under DEL-099-05, open a row in the review log: document ID, revision, reviewer, comments, disposition (Approved / Approved with comments / Revise and resubmit / Rejected), and date.
   - Verify completeness of the vendor document register against the EPC SOW (DEL-099-01) and Package Datasheet (DEL-099-02).

3. **Scope conformance check (REQ-1 ... REQ-3).**
   - Confirm three product truck-loading stations and three condensate loading pumps (one per station) per DBM SEC-06.
   - Confirm per-station loading capacity 103 m3/h at 345 kPad differential, or document deviation.
   - Confirm custody/interface boundary: LACT is third-party NRM scope; facility scope terminates at the tie-in flange.

4. **Site basis conformance check (REQ-4 ... REQ-7).**
   - Confirm -40 deg C ambient design provisions (winterization, heating, materials) per DBM SEC-04.
   - Confirm fire/gas detection coverage (LEL, H2S, methyl mercaptan, fire) per DBM SEC-16.
   - Confirm shutdown coordination with BPCS / RIO / ESD per DBM SEC-17.
   - Confirm civil interface (truck-loading slab, spill control, access/turning/queuing) per DBM SEC-13.

5. **Test and inspection evidence collection (REQ-10).**
   - Index FAT, SAT, hydrotest, NDE, electrical loop checks, fire/gas verification, and ESD verification records as applicable.
   - Record any witnessed-test attendance and outcomes.
   - For deferred or not-applicable items, record rationale.

6. **Punchlist management (REQ-13).**
   - Capture any open items as punchlist entries with owner, target date, and severity.
   - Cross-link each punchlist entry to the originating review-log row, checklist item, or test record.

7. **Turnover evidence assembly (REQ-11).**
   - Collect Mechanical Completion records, Pre-Commissioning records, and Commissioning / Operational Acceptance records produced by the EPC and vendor teams.
   - Verify completeness against the Construction Work Package (DEL-099-03) turnover plan.

8. **Permit and external-dependency status (REQ-14).**
   - Record current truck rack permit amendment status (BCER 100120203) per DBM SEC-18.
   - Record any other regulatory or interface conditions outstanding.

9. **Draft acceptance memorandum.**
   - Summarize scope, requirements coverage, outstanding punchlist, residual risks, recommended acceptance status (Full / Conditional / Not Recommended).
   - Cite each requirement to the supporting evidence row(s).

10. **Human approval (REQ-12).**
    - Route the acceptance memorandum to the EPC Integrator approver (and Owner approver where required).
    - Capture signatures and date.
    - Agents shall not sign or certify (K-AUTH-1).

11. **Status update.**
    - On completion of human approval, update `_STATUS.md` per the project lifecycle (state advance to be performed by an authorized agent shell or human; this skill only safely advances OPEN→INITIALIZED).

## Verification

| Check | Method |
|---|---|
| Each REQ-* in `Specification.md` has at least one evidence reference in the review log, checklist, or test index | Manual cross-reference review |
| All vendor documents from DEL-099-05 are dispositioned in the review log | Row-count and status audit |
| All punchlist items have owner and target date | Punchlist audit |
| All turnover certificates required by DEL-099-03 are present or explicitly waived | Turnover index audit |
| Acceptance memorandum signed by an authorized human approver | Signature review |
| No agent signature appears on any acceptance record | Signature review |

## Records

- `vendor_document_review_log` (per-document disposition log; CSV or Markdown table)
- `package_acceptance_checklist` (REQ-by-REQ checklist with evidence pointers)
- `test_inspection_evidence_index` (index of FAT/SAT/hydrotest/NDE/electrical/fire-gas/ESD records)
- `turnover_evidence_index` (MC / Pre-Comm / Comm / Operational Acceptance certificates)
- `punchlist` (open items with owner, date, severity)
- `acceptance_memorandum` (signed; human approver)
- `_run_records/` task run reports for each agent-assisted pass on this deliverable
