# Procedure — DEL-097-03 Construction Work Package (Tanks, Condensate, API 650, 3-25)

## Purpose

This procedure governs the production of the Construction Work Package deliverable for PKG-097 (four 3800 bbl modified API 650 condensate storage tanks in the 3-25 area), and outlines the construction-execution steps that the CWP itself must direct.

## Prerequisites

- `_CONTEXT.md`, `_REFERENCES.md`, and `_DEPENDENCIES.md` populated for DEL-097-03 (already seeded by PREPARATION).
- PKG-097 source slice in `26020-Package_Requirements.docx` (§`26020-03-PT-19-006`) accessible. (Confirmed.)
- Interface source `26020-Packages_Interfaces.3.xlsx` available (referenced by PKG-097 source slice; specific PKG-097 rows TBD).
- Vendor engineering output from `DEL-097-04` available before field erection. (ASSUMPTION: standard EPC sequencing; explicit gate **TBD**.)
- Civil scopes (foundations, containment berms, grading) at sufficient maturity to support tank erection. **TBD** until `Dependencies.csv` is generated.
- Project basis-of-design documents (ambient, seismic, wind) accessible. **TBD** (not opened in this pass).

## Steps

### A. Producing the CWP deliverable

1. **Confirm package scope.** Reconcile `_CONTEXT.md` with `26020-Package_Requirements.docx` §`26020-03-PT-19-006` and the Gate 7 DELIVERABLE_REGISTER row for `DEL-097-03`. Record any drift.
2. **Resolve interfaces.** Extract the PKG-097 rows from `26020-Packages_Interfaces.3.xlsx` and load them into the CWP's interface / tie-in matrix. Open issues become punch-list candidates. (Step pending source access — **TBD** in this pass.)
3. **Confirm vendor scope boundary.** Verify the split between `DEL-097-04` (vendor engineered package) and `DEL-097-03` (field installation, tie-ins, turnover). Record the boundary in the CWP.
4. **Assemble the CWP master document.** Sections: scope, references, organization & responsibilities, sequencing, discipline procedures, NDE & hydrotest plan, coating QC, relief device installation & testing, blanket-gas commissioning, interface / tie-in matrix, punch-list & turnover, and records index. (ASSUMPTION: typical EPC structure.)
5. **Assemble the installation and tie-in workface plan.** Per-tank workface packages plus per-interface workface tasks (fill, suction, drain, VRU header, blanket gas, instrumentation, electrical).
6. **Assemble the construction interface and turnover checklist.** One row per tank-level and per-interface item; signoff lines for QA/QC, EPC, and commissioning.
7. **Internal review.** Cross-check Datasheet ↔ Specification ↔ Guidance ↔ this Procedure for consistent values, terminology, and references. Open conflicts go into the Conflict Table in `Guidance.md`.
8. **Issue for human review.** Submit CWP, workface plan, and turnover checklist for human approval (no agent may certify; per K-AUTH-1).

### B. Construction execution directed by the CWP (summary)

These steps are what the CWP, once approved, instructs the field to perform. They are listed here so that the deliverable's structure is procedurally complete; detailed methods are out of scope for this skill run.

1. Verify civil readiness (foundations, anchor bolts, containment berm). Sign civil-to-mechanical handoff.
2. Erect each of the four 3800 bbl tanks per modified API 650. Perform welding, NDE, dimensional checks.
3. Confirm internal Devchem 253 coating system on floor, walls, and roof — inspect DFT, holidays, cure. Field touch-up per coating-manufacturer instructions. (ASSUMPTION: inspection regime not detailed in PKG-097 source slice.)
4. Install and test PVRV and EPRV on each tank; record set pressures and function tests.
5. Tie in blanket-gas supply per API 2000; pressure / leak test.
6. Tie in VRU header connection at each tank; leak test.
7. Tie in fill, suction, drain, and instrument nozzles; loop-check level instrumentation and 90% high-level shutdown.
8. Perform tank hydrotest per modified API 650; drain, dry, and prepare for service. (Sequencing vs. coating — see Guidance Trade-offs.)
9. Strap / calibrate each tank. (ASSUMPTION: not stated in PKG-097 source slice.)
10. Complete punch-list closure; sign mechanical completion certificate per tank; release to commissioning.

## Verification

- A. Steps 1–6: each deliverable section maps back to `_CONTEXT.md` Anticipated Artifacts and Gate 7 DELIVERABLE_REGISTER. Internal review (Step 7) records the mapping.
- A. Step 7: consistency sweep recorded in the run record; conflicts surfaced in `Guidance.md` Conflict Table.
- A. Step 8: human approval is the only binding signoff (K-AUTH-1).
- B. Steps 1–10: each construction-execution step has a corresponding verification line in `Specification.md` §Verification.

## Records

- Approved Construction Work Package (master)
- Approved installation and tie-in workface plan
- Approved construction interface and turnover checklist
- NDE / weld / hydrotest reports per tank
- Coating QC records per tank
- Relief device installation and function-test records (PVRV, EPRV) per tank
- Blanket-gas system commissioning record
- VRU header tie-in and leak-test records
- Level / overfill loop-check and function-test records
- Tank strapping / calibration certificates (per tank)
- Punch list and mechanical completion certificates (per tank, per interface)
- Run record for this skill invocation: `_run_records/TASK_RUN_2026-05-25_<HHMM>.md`
