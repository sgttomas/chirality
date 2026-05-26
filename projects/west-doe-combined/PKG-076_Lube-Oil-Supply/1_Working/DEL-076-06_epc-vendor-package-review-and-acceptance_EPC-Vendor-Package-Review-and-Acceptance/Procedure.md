# Procedure: DEL-076-06 — EPC Vendor Package Review and Acceptance

**Interpretation:** This Procedure describes the steps to **produce** the deliverable (i.e., to perform the EPC review and acceptance and assemble the acceptance record set). Operating/using the lube oil package itself is out of scope here; that belongs to commissioning/operations procedures downstream.

## Prerequisites

- Sibling baselines reached (each at INITIALIZED or better):
  - DEL-076-01 Scope of Work
  - DEL-076-02 Package Datasheet
  - DEL-076-03 Construction Work Package
  - DEL-076-04 Vendor Engineered Equipment Package (vendor supply available for review)
  - DEL-076-05 Vendor Document Turnover Package (vendor documentation available for review)
  Note: `_DEPENDENCIES.md` declares no upstream edges at PREPARATION; the above are semantic prerequisites surfaced here (ASSUMPTION).
- Access to the Gate 7 PROJECT_DECOMP snapshot under `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Access to `26020-Package_Requirements.docx` (package heading 30) and the DBM-Deepcut source as a converted/extracted reference for detailed acceptance criteria (currently `location TBD`; resolve before final acceptance).
- Designated EPC Integrator reviewer; designated Package Vendor counterpart for input.

## Steps

1. **Establish the acceptance baseline.**
   - Open the accepted DEL-076-01 Scope of Work, DEL-076-02 Package Datasheet, and DEL-076-03 Construction Work Package.
   - Extract the binding requirements, datasheet values, and construction interface/turnover items.
   - Output: working acceptance baseline (internal worksheet).

2. **Build the vendor document review log.**
   - Retrieve the Vendor Document Register from DEL-076-05.
   - For each vendor document, record: document ID, revision, EPC reviewer, review date, comment disposition (Accepted / Accepted with comment / Rejected), and re-submission status.
   - Output: `Vendor document review and comment log` (ART-CE37DAAF83).

3. **Populate the package acceptance and turnover checklist.**
   - Generate checklist rows for: each of the eight PKG-076 interfaces (Utility Piping; Drain/Containment; Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Maintenance Access; Structural/Foundations/Supports); each item in the major equipment baseline (P-9240-1, P-9250-1, horizontal split storage tank, electric motor drives, sweet+sour service materials); each documentation deliverable in (2); turnover-readiness items per project turnover policy (TBD).
   - For each row, record disposition (Accept / Accept with conditions / Reject / Open) with evidence pointer.
   - Output: `Vendor package acceptance and turnover checklist` (ART-36208600FC).

4. **Assemble factory/shop test and inspection evidence.**
   - Collect from the vendor: factory acceptance test reports, shop hydrotest records, NDE reports, electrical motor test records, painting/coating reports, packaging/preservation records — to the extent required (specific test/inspection requirements: `location TBD`, `26020-Package_Requirements.docx` package heading 30).
   - Cross-reference each test/inspection record to the corresponding Specification requirement (R-076-06-03, R-076-06-05).
   - Output: `Factory/shop test and inspection evidence` (ART-F44CA74291).

5. **Confirm interface integration acceptance.**
   - For each of the eight INTERFACE_REGISTER.csv rows for PKG-076, confirm vendor-supplied interface points match EPC-side tie-in design and that the responsibility split at the battery limit is documented.
   - Record interface disposition on the checklist row from Step 3.

6. **Compile turnover evidence.**
   - Collect spare parts list, vendor as-built documentation, operating & maintenance manuals, warranty letters, training records, and preservation/storage documentation as required (specifics: TBD).
   - Output: turnover evidence dossier.

7. **EPC Integrator acceptance disposition.**
   - Review the consolidated record set (Steps 2-6).
   - Issue one of: Full acceptance / Conditional acceptance (with open items list) / Non-acceptance (with required corrective actions).
   - Sign and date the acceptance record. (Per K-AUTH-1, this is a human authorization step; the deliverable file set records the disposition, the human signs.)

8. **Update deliverable status.**
   - Update `_STATUS.md` per the deliverable lifecycle: from INITIALIZED to subsequent states only by authorized agents/humans per project governance.

## Verification

- All eight PKG-076 interfaces have a recorded disposition (Step 5).
- Every major equipment item in the baseline (Step 3) has a checklist row with evidence pointer.
- Every vendor document in the DEL-076-05 register appears in the review log (Step 2).
- Required factory/shop test records (set: TBD) are present and cross-referenced (Step 4).
- An EPC Integrator signature is captured on the acceptance disposition (Step 7).

## Records

- Vendor document review and comment log (ART-CE37DAAF83)
- Package acceptance and turnover checklist (ART-36208600FC)
- Factory/shop test and inspection evidence dossier (ART-F44CA74291)
- Turnover evidence dossier
- Signed EPC Integrator acceptance disposition (artifact ID: TBD)
- Run records for any TASK-driven assembly steps under `_run_records/`
