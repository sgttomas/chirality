# Procedure: DEL-091-06 — EPC Vendor Package Review and Acceptance

## Purpose

Operational procedure to produce the EPC Integrator acceptance evidence set for the Tank Farm Pump Building 3-25 vendor package: vendor document review log, package acceptance checklist, test/inspection evidence reconciliation, and turnover evidence (`_CONTEXT.md` Anticipated Artifacts; `Specification.md` Documentation).

## Prerequisites

- Accepted EPC anchor deliverables available:
  - DEL-091-01 EPC Scope of Work (PKG-091)
  - DEL-091-02 EPC Package Datasheet (PKG-091)
  - DEL-091-03 Construction Work Package (PKG-091)
- Vendor inputs available:
  - DEL-091-04 Vendor Engineered Equipment Package
  - DEL-091-05 Vendor Document Turnover Package (includes vendor document register, FAT/inspection records, certifications)
- Access to the source set:
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Liquids Hub equipment basis)
  - `_Sources/26020-Package_Requirements.docx` heading 44 (location TBD — not locally accessible as text)
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 84 (location TBD)
- `_REFERENCES.md` and `_CONTEXT.md` reviewed.
- No upstream declared dependencies in `_DEPENDENCIES.md`; sibling DEL-091-04/05 inputs are required in practice (TBD whether to declare formally).

## Steps

1. **Establish review baseline.** Open DEL-091-01, DEL-091-02, DEL-091-03 and extract the binding acceptance basis (scope items SOW-0185..SOW-0188; pump count and duty values per `3-25_Comp_and_Liquids_DBM.md` lines 412-414, 526, 575-583; LACT exclusion per lines 54, 417). Confirm the acceptance basis snapshot reference (Gate 7 PROJECT_DECOMP).
2. **Build vendor document review log.** Initialize one row per document in the vendor turnover register (DEL-091-05). Columns (ASSUMPTION pending `26020-Package_Requirements.docx` heading 44): document ID, title, revision, EPC reviewer, review date, status, comments, disposition (accept / accept-with-comment / reject / rework), disposition date, source clause traceability.
3. **Build acceptance checklist.** For each SOW item (SOW-0185, SOW-0186, SOW-0187, SOW-0188) create checklist rows mapped to anchor-doc clauses; for each Specification requirement (R-01..R-10 in `Specification.md`) record evidence pointer, reviewer, date, and disposition. Clause-level rows beyond R-01..R-10 are TBD pending source access (see Guidance Conflict Table C-03).
4. **Reconcile test and inspection evidence.** Cross-check vendor FAT, hydrostatic, NDE, and instrumentation calibration records against the vendor document register (DEL-091-05). Witness records, where applicable, attach to the corresponding pump or piping subsystem. Specifically verify condensate booster pump performance against 165 m3/h at 35 m TDH per pump (`3-25_Comp_and_Liquids_DBM.md` line 413).
5. **Verify scope alignment.** Confirm pump count and configuration: 2 x 100% condensate booster pumps; three condensate loading pumps; 2 x 100% produced-water transfer pumps; plus sour condensate recycle, condensate skim, product recycle, and sales condensate booster pumps as listed in `3-25_Comp_and_Liquids_DBM.md` (lines 40, 412-414, 526, 575-583).
6. **Verify interfaces.** Walk down P&IDs and IFA drawings at facility/vendor boundary; explicitly confirm the LACT tie-in boundary (facility-side only; LACT internals are NRM scope per `3-25_Comp_and_Liquids_DBM.md` lines 54, 417).
7. **Verify sour-service classification.** Cross-check vendor datasheets and material certifications against sour-service applicability for each in-scope component (`Specification.md` R-09; ASSUMPTION on per-equipment classification until vendor datasheet review).
8. **Track non-conformances.** Open a non-conformance log; for each rejected or accept-with-comment item, record requirement reference, source clause, disposition, owner, and target close date.
9. **Assemble turnover evidence.** Compile turnover index linking each EPC anchor requirement to: (a) vendor turnover document(s), (b) test/inspection record(s), (c) checklist row(s), and (d) non-conformance disposition. Confirm sign-off authority.
10. **Issue acceptance package.** EPC Integrator signs the acceptance checklist cover sheet. Distribute to Construction (DEL-091-03 owners) and commissioning. Update sibling deliverables' dependency references if formal upstream/downstream edges are added.

## Verification

| Step | Verification |
|---|---|
| 1 | Anchor doc snapshot references recorded; acceptance basis baseline approved by EPC Integrator. |
| 2 | Review log row count equals vendor register row count (DEL-091-05); all disposition columns populated. |
| 3 | Checklist covers SOW-0185..SOW-0188 and Specification R-01..R-10; gaps recorded as TBD with traceability. |
| 4 | All required FAT, hydrostatic, NDE, and calibration records linked; missing records logged as non-conformances. |
| 5 | Equipment count and duty values reconcile with `3-25_Comp_and_Liquids_DBM.md`. |
| 6 | LACT boundary confirmed on stamped P&ID set; no LACT internals carried inside acceptance scope. |
| 7 | Sour-service classification confirmed against vendor datasheets/certifications. |
| 8 | Non-conformance log closed or transferred with explicit ownership before acceptance gate. |
| 9 | Turnover index complete; every anchor requirement maps to at least one evidence artifact. |
| 10 | Acceptance package signed; distribution recorded. |

## Records

- Vendor document review log (per Step 2)
- Package acceptance checklist with dispositions (per Step 3)
- Test and inspection evidence reconciliation report (per Step 4)
- Interface walkdown record at LACT and other facility-side boundaries (per Step 6)
- Sour-service verification record (per Step 7)
- Non-conformance log with closures (per Step 8)
- Turnover index and signed acceptance cover sheet (per Steps 9-10)

All records retained under the deliverable folder or its successor controlled-document location (location TBD pending project document control convention).
