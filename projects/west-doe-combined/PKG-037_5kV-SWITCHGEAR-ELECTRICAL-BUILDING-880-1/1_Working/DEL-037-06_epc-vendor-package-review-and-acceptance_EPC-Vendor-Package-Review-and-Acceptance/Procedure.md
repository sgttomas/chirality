# Procedure: DEL-037-06 — EPC Vendor Package Review and Acceptance

## Purpose

Operational procedure for producing the EPC Integrator acceptance record for `PKG-037` (5kV SWITCHGEAR ELECTRICAL BUILDING 880-1): vendor document review log, package acceptance checklist, test/inspection evidence, and turnover evidence.

## Prerequisites

- `DEL-037-01` Scope of Work — accepted version available.
- `DEL-037-02` Package Datasheet — accepted version available.
- `DEL-037-03` Construction Work Package — accepted version available.
- `DEL-037-04` Vendor Engineered Equipment Package — vendor outputs available for review.
- `DEL-037-05` Vendor Document Turnover Package — vendor document register and submittals available.
- Gate 7 PROJECT_DECOMP snapshot accessible.
- DBM source (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`) available for building-electrical cross-checks.

Note: `_DEPENDENCIES.md` does not declare these upstream items; this list is the working prerequisite per `DELIVERABLE_REGISTER.csv` row 209 narrative (ASSUMPTION pending Conflict CONF-037-06-002 ruling).

## Steps

1. **Establish the acceptance baseline.**
   - Extract requirement IDs and acceptance criteria from `DEL-037-01` (SOW) and `DEL-037-02` (Package Datasheet).
   - Extract construction and turnover criteria from `DEL-037-03` (Construction Work Package).
   - Record the baseline as the spine of the acceptance checklist (one row per requirement).

2. **Build the vendor document review log.**
   - Enumerate every vendor submittal from `DEL-037-05`.
   - For each submittal, record: vendor document ID, title, revision, EPC reviewer, disposition (Accepted / Accepted-with-comment / Rejected / Pending), comment IDs, and closure status.
   - Defects must be itemized as vendor actions; EPC does not edit vendor documents.

3. **Populate the package acceptance checklist.**
   - For each baseline requirement row, link the supporting vendor evidence (document IDs from Step 2; test records from Step 4; turnover records from Step 5).
   - Assign acceptance status: Accept / Accept-with-comment / Reject / TBD / Pending.
   - Add one row per interface type from `PACKAGE_REGISTER.csv` row 39: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports.

4. **Compile test and inspection evidence.**
   - Collect Factory Acceptance Test (FAT) records, Site Acceptance Test (SAT) records, and pre-energization inspection records furnished by the vendor.
   - Cross-check against acceptance-checklist requirements that mandate test evidence (R-3).
   - Where the EPC SOW/Datasheet has invoked DBM building-electrical provisions (HVAC n+1, bottom-entry cabling, building grounding, cable types), verify the vendor evidence demonstrates compliance.

5. **Compile turnover evidence.**
   - Collect signed turnover packages, system handover records, and the deficiency/punchlist set.
   - Confirm that all open deficiencies have an owner and target closure date.

6. **Run cross-document consistency checks.**
   - Confirm every acceptance-checklist row points to a real review-log entry, test record, or turnover record.
   - Confirm no acceptance row is silently cleared from `TBD`/`Pending` without supporting evidence.
   - Confirm objective coverage: each `OBJ-001/004/005/006/007/008/009/010` has at least one supporting acceptance entry (ASSUMPTION: package-grouping heuristic, see `_CONTEXT.md`).

7. **Flag unresolved items.**
   - Items lacking source-grounded evidence remain `TBD`.
   - Source disagreements feed the Conflict Table in `Guidance.md`.
   - Items requiring human ruling are escalated through the normal governance path.

8. **Issue the acceptance record.**
   - Package the vendor document review log, acceptance checklist, test/inspection evidence, and turnover evidence as the deliverable artifact set.
   - Record EPC Integrator sign-off scope and any explicit exclusions.

## Verification

- Each baseline requirement (Step 1) has a corresponding acceptance checklist row.
- Each vendor submittal (Step 2) has a disposition and reviewer.
- Each interface type (Step 3) has an acceptance row.
- Test/inspection and turnover records (Steps 4-5) are linked to their checklist rows.
- Consistency checks (Step 6) produce no unresolved discrepancies, or such discrepancies are captured in `Guidance.md` Conflict Table.

## Records

- `Vendor_Document_Review_Log` (per submittal)
- `Package_Acceptance_Checklist` (per requirement + per interface type)
- `Test_Inspection_Evidence` (FAT/SAT/pre-energization)
- `Turnover_Evidence` (signed turnover + deficiency log)
- This Procedure run records and revisions in `_run_records/`.
