# Procedure — DEL-095-05 Vendor Document Turnover Package

## Purpose

Operational steps to **produce** and **maintain** the Vendor Document Turnover Package for PKG-095 (Tanks, Slop / API 650) from initiation through acceptance-ready turnover.

## Prerequisites

- Accepted upstream snapshot: `GATE-07_Final_Published_2026-05-24` (PROJECT_DECOMP).
- `DEL-095-01_scope-of-work` (EPC Scope of Work) issued.
- `DEL-095-02_package-datasheet` (EPC Package Datasheet) issued — defines vendor engineering handoff basis.
- `DEL-095-04_vendor-engineered-equipment-package` underway — produces the vendor content that flows into the register.
- Access to source vendor document table at `26020-Package_Requirements.docx` heading 47 (TBD: requires markdown extraction or vendor-provided equivalent).
- Project document control basis (numbering, revision, status conventions) — TBD if not yet published.

Declared dependencies note: `_DEPENDENCIES.md` lists no human-declared upstream/downstream edges. Prerequisites above are inferred from `_CONTEXT.md` ParentPackageID and sibling deliverables in PKG-095. Treat as ASSUMPTION until declared.

## Steps

1. **Initialize the Vendor Document Register.**
   - Create the register seeded from the heading-47 source vendor document table rows.
   - If heading-47 rows are not yet extracted, seed from API 650 tank-package convention (GA drawings, nozzle schedules, MTRs, weld/NDE, hydrotest, coating, calibration, IOM) and mark the seed rows as ASSUMPTION pending source confirmation.
   - For each row, capture: document number, title, revision, status, planned issue date, equipment tag, SOW linkage.

2. **Tag the register to package scope.**
   - Associate every row to one or more of SOW-0213..SOW-0216 and to the equipment list anchored by the slop tank (TK-9130-2 as ASSUMPTION until confirmed per SOW-0216).

3. **Issue submittals under controlled revisions.**
   - Vendor issues each document at its planned revision/status milestones.
   - Each issuance updates the register row (revision, status, date, submittal artifact path).

4. **Carry source-required documents as artifacts.**
   - Preserve heading-47 source-table rows as evidence within this deliverable; do not promote them to separate deliverables (per `_CONTEXT.md` Notes).

5. **EPC Integrator interface review.**
   - EPC Integrator performs interface/integration review via `DEL-095-06`.
   - Findings/dispositions are captured in DEL-095-06 and back-referenced from the register's status column or a parallel review-log column.
   - Resolve or escalate disagreements via the Guidance Conflict Table (HRR rows).

6. **Iterate to acceptance-ready state.**
   - Drive every register row to a closed-out final-revision state (e.g., IFC/IFA-equivalent per project document-control basis).
   - Close all DEL-095-06 review findings, or carry them as documented dispositions.

7. **Assemble the turnover record.**
   - Snapshot the final register state.
   - Compile transmittal log + document completeness checklist + EPC acceptance sign-off references + source-row evidence index.
   - Attach the turnover record to `DEL-095-06` for the EPC review-and-acceptance closure.

## Verification

| Check | Method |
|---|---|
| Register completeness against heading-47 source rows | Row-by-row reconciliation once heading-47 slice is extracted; gap report. |
| One-to-one register-row ↔ submittal-artifact mapping | Audit of the register's submittal-path column against the actual artifact store. |
| Scope-tag traceability (every row → SOW + equipment tag) | Trace report; missing-tag report. |
| API 650 evidence coverage (MTRs, weld/NDE, hydrotest, coating) | Confirm presence in the register; cross-check with the Vendor Engineered Equipment Package (DEL-095-04). |
| Conflict Table dispositions | Human ruling recorded for each HRR item before turnover-record sign-off. |
| Turnover record acceptance-readiness | DEL-095-06 acceptance log references this turnover record and records closure. |

## Records

- The Vendor Document Register (current state) — maintained throughout the project.
- All controlled-revision vendor document submittals — referenced from the register.
- The heading-47 source vendor document table rows — preserved as artifacts.
- The final Turnover Record (snapshot + transmittal log + completeness checklist + sign-off references).
- HRR ruling records — closed Conflict Table entries.

ASSUMPTION: Exact record-storage format and document-control numbering scheme are TBD pending project document-control basis publication.
