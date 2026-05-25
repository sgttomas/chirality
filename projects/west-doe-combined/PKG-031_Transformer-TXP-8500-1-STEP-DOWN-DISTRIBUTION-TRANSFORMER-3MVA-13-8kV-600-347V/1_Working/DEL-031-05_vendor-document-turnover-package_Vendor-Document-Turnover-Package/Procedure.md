# Procedure: DEL-031-05 — Vendor Document Turnover Package

## Purpose

Produce and operate the vendor document register, submittals, source-required vendor documentation, and turnover records for PKG-031 (Transformer TXP-8500-1, 3 MVA, 13.8 kV / 600/347 V step-down distribution transformer), and hand the complete, reconciled set off to DEL-031-06 (EPC Vendor Package Review and Acceptance).

## Prerequisites

- Accepted Gate 7 snapshot present: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- DEL-031-01 (Scope of Work) and DEL-031-02 (Package Datasheet) available as the EPC anchor inputs for vendor scope confirmation.
- DEL-031-04 (Vendor Engineered Equipment Package) underway or accepted, supplying the vendor design content the documents describe.
- PKG-031 source slice from `_Sources/26020-Package_Requirements.docx` captured into `0_References/` (TBD — see HRR-031-05-001).
- Declared dependencies (per `_DEPENDENCIES.md`): none currently declared upstream or downstream. Confirm with WORKING_ITEMS before turnover.
- Required references: `_CONTEXT.md`, `_REFERENCES.md`, Gate 7 DELIVERABLE_REGISTER.csv row DEL-031-05.

## Steps

1. **Capture source slice.** Extract the PKG-031 section and vendor-documentation tables from `_Sources/26020-Package_Requirements.docx` into `0_References/` so REQ-031-05-03 can be satisfied with source grounding (closes HRR-031-05-001).
2. **Build the vendor document register.** Create the register seeded from the captured source slice; one row per required vendor document with document number, title, revision, transmittal ID, status, and turnover state. Add vendor-scope-specific rows beyond the source minimum where the vendor's supply produces additional documents.
3. **Confirm fluid type and other configuration parameters** that determine the document set (see HRR-031-05-002); update the register accordingly.
4. **Receive vendor submittals.** For each register row, receive the vendor's transmittal, file the submittal artifact, and update register status and revision.
5. **Route for EPC interface/integration review.** Notify the EPC Integrator (per the project document control protocol — see HRR-031-05-003) and log review disposition against each register row (input to DEL-031-06).
6. **Track open items and holds.** Maintain an open-item log linked to register rows; pursue closure through revised submittals or accepted dispositions (REQ-031-05-07).
7. **Reconcile.** When all required rows are at accepted/closed status, reconcile the register against the source vendor-documentation table to confirm completeness.
8. **Issue turnover records.** Produce the final turnover transmittal, completeness sign-off, and acceptance evidence package; hand off to DEL-031-06.

## Verification

- Register completeness check: every row required by the PKG-031 source vendor-documentation table is present in the register.
- Submittal completeness check: every register row at accepted status has an associated submittal artifact at the registered revision.
- Disposition completeness check: every open item is either closed or has an accepted-disposition record.
- EPC review check: every register row has a logged EPC review disposition.
- Authorship check (REQ-031-05-06): no register row lists EPC Integrator as author.
- Turnover sign-off check: final turnover transmittal exists and is signed by the Package Vendor; acceptance under DEL-031-06 is recorded.

## Records

- Vendor document register (current and snapshotted at turnover).
- Submittal artifact set (all revisions, with the final accepted revision marked).
- Source vendor-document table slice (artifact retained in `0_References/`).
- Transmittal log.
- EPC review disposition log.
- Open-item / hold log with closure evidence.
- Final turnover transmittal and completeness sign-off.
- Cross-reference to DEL-031-06 acceptance record.
