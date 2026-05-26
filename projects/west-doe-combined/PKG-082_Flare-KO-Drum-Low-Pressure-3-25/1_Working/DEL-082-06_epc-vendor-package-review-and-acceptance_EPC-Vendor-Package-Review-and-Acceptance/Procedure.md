# Procedure — EPC Vendor Package Review and Acceptance (DEL-082-06)

Operational steps the EPC Integrator follows to produce review-and-acceptance evidence for the PKG-082 Flare KO Drum (Low Pressure) 3-25 vendor package.

## Purpose

Produce the four acceptance-evidence artifacts identified in `_CONTEXT.md`:
- Vendor document review log
- Package acceptance checklist
- Test/inspection evidence
- Turnover evidence

The procedure operates on (uses) the vendor package; it does not produce the vendor package itself.

## Prerequisites

- DEL-082-01 (Scope of Work) issued and accessible.
- DEL-082-02 (Package Datasheet) issued and accessible.
- DEL-082-03 (Construction Work Package) issued and accessible.
- DEL-082-04 (Vendor Engineered Equipment Package) received from Package Vendor.
- DEL-082-05 (Vendor Document Turnover Package) received from Package Vendor.
- Reference materials accessible: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`; `_Sources/26020-Package_Requirements.docx`; `_Sources/26020-Packages_Interfaces_4_export.xlsx`.
- Reviewer roles assigned: Mechanical lead, Process Safety, Pumps SME (see Guidance — Trade-offs). Specific role-to-name mapping: TBD (project-controlled).

Declared upstream dependencies: none recorded in `_DEPENDENCIES.md` at PREPARATION. Acceptance work nonetheless depends on the peer deliverables listed above; this is functional, not blocking, until dependencies are formally declared.

## Steps

1. **Establish the baseline.**
   1. Confirm latest issued revisions of DEL-082-01, DEL-082-02, DEL-082-03 are in hand.
   2. Confirm the vendor package (DEL-082-04) revision and turnover package (DEL-082-05) revision under review.
   3. Open the DBM source slices (SEC-06, SEC-07, SEC-09) for reference.

2. **Build the vendor document review log.**
   1. List every document in DEL-082-05 (one row per document, with vendor doc number, title, revision).
   2. Assign reviewer per document class.
   3. For each document: review against the controlling authority (SOW item, Datasheet attribute, CWP step, DBM clause).
   4. Record disposition: Accepted / Accepted with Comment / Revise and Resubmit / Rejected (ASSUMPTION: vocabulary; see Guidance C-082-06-01).
   5. Record disposition rationale citing the controlling authority.

3. **Build the package acceptance checklist.**
   1. Create one row per SOW item (SOW-0079, SOW-0080, SOW-0081, SOW-0082).
   2. Create additional rows for each Package Datasheet attribute that requires verification against the vendor package.
   3. Create CWP-alignment rows for: skid-edge isolation, vent/drain routing class, maintenance access, sour-service isolation (double block/bleed or equivalent), free-drain/slope toward the flare KO interface (DBM SEC-06).
   4. Create LP-relief and blowdown rows: LP header size compatibility, staggered blowdown assumption, sequencing per W242510-PRC-REP-000003-001 (mark `location TBD` if document is not accessible).
   5. For each row, record reviewer, evidence reference, finding, and closure status.

4. **Collect test and inspection evidence.**
   1. Identify code-required tests from the Package Datasheet (specific test list: TBD per source access).
   2. Verify hydrotest, NDE, and sour-service material verification records are present and signed (specific code clauses: TBD pending DEL-082-02).
   3. Verify functional test of LP flare KO drum transfer pump P-3900-2 per 1 x 100 percent configuration (DBM SEC-09).
   4. File each evidence record with a pointer in the checklist row it supports.

5. **Verify turnover completeness.**
   1. Cross-check DEL-082-05 document register against the turnover index requirement.
   2. Confirm latest revisions are present.
   3. Record any missing documents as open items (`TBD` or `NEEDS_HUMAN_RULING`).

6. **Sweep open items.**
   1. List every `TBD`, ASSUMPTION, and unresolved deviation across the review log and checklist.
   2. Decide for each: closed (with evidence), deferred (with owner + due date), or escalated (NEEDS_HUMAN_RULING).
   3. Update Conflict Table in `Guidance.md` if a new conflict surfaces.

7. **Finalize evidence package.**
   1. Confirm the four artifacts are complete: review log, acceptance checklist, test/inspection evidence, turnover evidence.
   2. Confirm no agent or non-human approval has been recorded (K-AUTH-1).
   3. Prepare the package for human approver review.

8. **Record handoff.**
   1. Update `_STATUS.md` only through the deliverable lifecycle policy (do not advance state without authorization).
   2. Capture run-level decisions in `MEMORY.md` if introduced.
   3. Notify the human approver that acceptance evidence is ready for binding ruling.

## Verification

- Each of the four artifacts exists and is internally complete.
- Each acceptance decision in the checklist cites a controlling authority.
- Every `TBD` is either closed with evidence or carried into the open-items list with owner and disposition.
- No binding approval has been issued by the deliverable itself.
- Sour-service isolation, LP relief sizing, and staggered blowdown rows in the checklist are explicitly evaluated, not implicitly accepted.

## Records

- `vendor_document_review_log` (per REQ-082-06-01)
- `package_acceptance_checklist` (per REQ-082-06-02 through REQ-082-06-04, REQ-082-06-08, REQ-082-06-09)
- `test_inspection_evidence` (per REQ-082-06-05, REQ-082-06-06)
- `turnover_evidence` (per REQ-082-06-07)
- Open-items list (per REQ-082-06-10) — captured in the checklist's open-status rows or in `MEMORY.md`.

Records file-naming convention: TBD pending project documentation control plan.
