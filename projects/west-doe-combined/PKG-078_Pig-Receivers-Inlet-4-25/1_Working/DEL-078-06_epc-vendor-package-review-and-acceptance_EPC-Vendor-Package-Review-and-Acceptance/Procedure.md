# Procedure — DEL-078-06: EPC Vendor Package Review and Acceptance

## Purpose

Operational procedure for the EPC Integrator to execute review and acceptance of the Pig Receivers (Inlet) 4-25 vendor package and produce the four anticipated acceptance artifacts: vendor document review log, package acceptance checklist, test/inspection evidence, and turnover evidence.

## Prerequisites

Declared upstream dependencies (per `_DEPENDENCIES.md`):
- None declared during PREPARATION. (Run `TASK + dependency-extract` to populate when a critical edge is required.)

Working prerequisites (ASSUMPTION, from `_CONTEXT.md` scope and `DELIVERABLE_REGISTER.csv`):
- DEL-078-01 EPC Scope of Work — accepted revision available.
- DEL-078-02 EPC Package Datasheet — accepted revision available.
- DEL-078-03 EPC Construction Work Package — accepted revision available.
- DEL-078-04 Vendor Engineered Equipment Package — at least one vendor submittal received.
- DEL-078-05 Vendor Document Turnover Package — vendor document register received with at least preliminary submittals.

Required reference materials (from `_REFERENCES.md`):
- DBM-Deepcut accessible reference: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- Owner / EPC project specification set (TBD locally; required for finalizing document review coding, NDE program, and area-classification compliance criteria).
- 26020-Package_Requirements.docx package heading 31 (TBD locally).

## Steps

### Step 1 — Initiate Acceptance Workspace

1.1 Confirm the accepted revisions of DEL-078-01, DEL-078-02, DEL-078-03 and capture revision tags in the acceptance memo.
1.2 Receive the vendor document register from DEL-078-05 and lock the baseline revision used to initialize the review log.
1.3 Create empty placeholders for: vendor document review log, package acceptance checklist, test/inspection evidence index, turnover evidence index, interface acceptance record, acceptance memo.

### Step 2 — Build the Vendor Document Review Log

2.1 Import every document number/revision from the vendor document register.
2.2 Assign EPC reviewers per discipline (mechanical, piping, process safety, instrumentation/controls, materials).
2.3 Define the owner's document review code system (TBD pending owner standard). Default ASSUMPTION: three-tier code (accepted / accepted with comments / not accepted, resubmit).
2.4 For each document, complete the review and record: reviewer, code, date, comment-disposition reference, link to the comment file. Records SHALL persist within deliverable-local scope.

### Step 3 — Walk the Package Acceptance Checklist

For each item in the Specification.md R3 list, verify and record evidence:
3.1 Inlet pipeline OD 610 mm (24 in.) at pig receiver interface — verify on vendor general arrangement/piping isometric.
3.2 Upstream skid isolation full-port confirmation — verify on vendor valve list/datasheet.
3.3 Barred tees — verify on downstream piping isometric and walkdown record.
3.4 LP fuel gas purge connection — verify on vendor P&ID and tie-in list.
3.5 HP flare vent connection — verify on vendor P&ID and confirm pressure rating and slope direction.
3.6 Piggable ESDV at inlet skid — verify ESDV datasheet, valve full-port status, position transmitter spec.
3.7 Design pressure alignment — verify pig receiver pressure rating against the inlet pipeline MAWP basis (consistent with 1,440 psig TBC upstream MAOP basis).
3.8 Equipment population — record accepted tag list. Note CONF-DEL-078-06-001 (Guidance Conflict Table) until ruled.

### Step 4 — Assemble Test and Inspection Evidence

4.1 Retrieve vendor records: pressure test certificate, NDE reports, CMTRs, PMI (if applicable), welding documentation, FAT report.
4.2 For each record, link to the corresponding document-review-log entry (Step 2).
4.3 Identify gaps; raise as comment-disposition items against the relevant vendor document.

### Step 5 — Confirm Interface and Integration Acceptance

5.1 Confirm inlet pipeline tie-in design with the pipeline owner/EPC pipeline lead.
5.2 Confirm HP flare connection with the flare-system lead, including KO drum drainage path.
5.3 Confirm LP fuel-gas connection with utilities lead.
5.4 Confirm grounding, anchorage, and area-classification design with electrical/civil leads. Acceptance criteria — TBD pending owner spec.
5.5 Re-confirm the TBD items called out in the DBM body (second pig receiver provision, delivery-point ESDV setpoint, HIPPS requirement) — record current status and target-close path; do not silently close.

### Step 6 — Turnover Evidence Package

6.1 Issue and complete Mechanical Completion checklist.
6.2 Capture punch list (A/B/C — taxonomy to be confirmed against owner standard).
6.3 Finalize the vendor data book index and confirm storage location.
6.4 Capture redline as-built drawings at vendor scope boundary.
6.5 Confirm spare-parts list and recommended-spares inventory.
6.6 Sign turnover handover to commissioning.

### Step 7 — Acceptance Memo

7.1 Draft acceptance memo: revision basis (DEL-078-01/02/03 revisions cited), scope, acceptance basis, summary of evidence by category, outstanding deviations and rulings (linked to Guidance Conflict Table), and explicit statement of acceptance status (accepted / accepted with conditions / not accepted).
7.2 EPC Integrator signs. Vendor counter-acknowledges where contractually required.

## Verification

| Check | Pass criterion |
|---|---|
| Vendor document review log | 100% of vendor document register entries reviewed with disposition codes recorded |
| Package acceptance checklist | Every R3 item has an evidence link or an explicit `TBD` with unblock action |
| Test/inspection evidence | All required record categories present or explicitly waived with EPC Integrator ruling |
| Interface acceptance | Each interface in R6 has signature acceptance or open-item linkage |
| Conflict Table | Every entry has either a recorded human ruling or an explicit deferral with target date |
| Acceptance memo | Signed; cites all evidence; carries explicit acceptance status |
| Source fidelity audit | Every acceptance entry cites the source artifact and revision relied upon |

## Records

Records produced (all stored within this deliverable folder, or referenced by absolute path to a controlled location):
- `vendor-document-review-log` (final, signed)
- `package-acceptance-checklist` (final, signed)
- `test-and-inspection-evidence` index and folder
- `turnover-evidence` index and folder (MC certificate, punch list, vendor data book index)
- `interface-acceptance-record`
- `acceptance-memo` (signed by EPC Integrator)
- Updates to `MEMORY.md` capturing rulings, deferrals, and changed assumptions

Storage locations and exact filenames will be confirmed at the start of execution (TBD — owner controlled documentation system not specified in accessible sources).
