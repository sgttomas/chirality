# Procedure — DEL-048-06 EPC Vendor Package Review and Acceptance

**Interpretation:** This procedure describes the steps to PRODUCE the EPC review-and-acceptance evidence artifacts (the deliverable outputs). Operating the compressor package itself is out of scope.

## Prerequisites

- Vendor Engineered Equipment Package available (DEL-048-04 at sufficient maturity). Declared upstream deps: none registered in `_DEPENDENCIES.md` (TBD — declared dependency list is empty; relationship inferred from PKG-048 deliverable grouping).
- Vendor Document Turnover Package available (DEL-048-05).
- EPC Scope of Work (DEL-048-01), Package Datasheet (DEL-048-02), and Construction Work Package (DEL-048-03) at INITIALIZED or later.
- Reviewer access to:
  - GATE-07 PROJECT_DECOMP snapshot (`SCOPE_LEDGER.csv`, `ARTIFACT_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`),
  - `26020-Package_Requirements.docx` (binary source under `_Sources/`),
  - `26020-Packages_Interfaces_4_export.xlsx` (binary source under `_Sources/`).
- Acceptance criteria for any TBD items in Specification resolved (or ruling captured in Guidance Conflict Table).

## Steps

1. **Establish review baseline.** Open Specification.md and confirm the requirement set (REQ-1..REQ-15) against `_CONTEXT.md` scope, the GATE-07 SCOPE_LEDGER rows for SOW-0115..SOW-0118, and the Package Datasheet (DEL-048-02). Resolve TBD requirement values (notably REQ-8 driver rated power via CFLT-1 ruling) before opening the vendor review.

2. **Build the document review log (ART-F8E220700B).** For each vendor document in DEL-048-05:
   - Record document ID, title, revision, and date.
   - Map document content to applicable REQ-* items.
   - Record comments (acceptance, conditional acceptance, non-conformance) with citation back to the controlling source slice.
   - Capture vendor disposition for each comment.

3. **Verify equipment conformance (REQ-4..REQ-7, REQ-10..REQ-12).** Compare vendor data sheets and nameplate schedules against the Datasheet attribute and condition rows. Record findings in the review log; escalate non-conformances to the acceptance checklist.

4. **Verify driver conformance (REQ-7..REQ-9).** After CFLT-1 ruling, verify motor nameplate rated power matches the ruled value and that 5-unit aggregate matches the 26,100 kW (35,000 HP) connected-load constraint.

5. **Verify scope-split discipline (REQ-13).** Confirm that "by-others" items (shipping, pile install, tie-in piping, electrical connections, mounting platform/stairs) are not asserted as in-vendor-scope acceptance items. Record any leakage as a non-conformance.

6. **Collect test and inspection evidence (REQ-3, ART-00AE5AE3CA).** Receive, review, and file:
   - Factory acceptance test (FAT) reports — specific tests TBD (not extracted in GATE-07; defer to vendor ITP and DEL-048-04 content).
   - Shop inspection reports.
   - Non-destructive examination records as applicable.
   Record witness/review evidence.

7. **Complete the acceptance checklist (ART-7862D9EB63).** Walk the checklist line-by-line; mark each item PASS, CONDITIONAL (with punchlist reference), or FAIL. Attach evidence pointers (review log entries, test reports).

8. **Build the traceability matrix (REQ-15).** Map each REQ-* and each acceptance-checklist line to the supported objectives (OBJ-001, OBJ-003..OBJ-010) per OBJECTIVE_DELIVERABLE_MAP.

9. **Assemble turnover evidence (REQ-14).** Package the review log, completed checklist, test/inspection evidence, and traceability matrix into a turnover bundle for handoff. Exact bundle structure: TBD (artifact not separately registered in GATE-07).

10. **Issue acceptance disposition.** EPC Integrator records the acceptance decision (ACCEPT / ACCEPT WITH PUNCH / REJECT) with reference to the assembled evidence. Per project governance, no agent may issue this disposition; it is a human/Type-1 ruling.

## Verification

- **V-1:** All vendor documents in DEL-048-05 appear in the review log (REQ-1).
- **V-2:** Every Specification REQ-* item has at least one acceptance-checklist line and at least one evidence pointer (REQ-2, REQ-15).
- **V-3:** All non-conformances either have closed-loop dispositions or are recorded on the punchlist (Guidance principle: acceptance vs. punchlist).
- **V-4:** Driver rated power on nameplate aligns with CFLT-1 ruled value and with the 26,100 kW connected-load figure (REQ-8, REQ-9).
- **V-5:** Traceability matrix covers all listed objectives (REQ-15).
- **V-6:** Scope-split items are NOT recorded as vendor acceptance criteria (REQ-13).

## Records

- Vendor document review and comment log — ART-F8E220700B
- Vendor package acceptance and turnover checklist — ART-7862D9EB63
- Factory/shop test and inspection evidence — ART-00AE5AE3CA
- Traceability matrix (REQ ↔ objective) — embedded in checklist or appended (location TBD)
- Turnover evidence bundle — TBD artifact ID
- Acceptance disposition memo signed by EPC Integrator — TBD (not registered in GATE-07; required for project governance closeout)
