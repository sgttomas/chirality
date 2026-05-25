# Procedure: DEL-036-03_construction-work-package

## Purpose

Operational procedure to **produce** the Construction Work Package artifact set for `PKG-036` (6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1)). The procedure organizes EPC Integrator activity from source ingestion through turnover-checklist sign-off. It does not describe field installation procedures of the vendor-supplied equipment itself; those are Package Vendor / detailed-design scope.

## Prerequisites

- Accepted Gate 7 decomposition snapshot at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` is available.
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` exist in the deliverable folder.
- Accessible source materials: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `_Sources/26020-Packages_Interfaces_4_export.xlsx` (Packages row 38), `_Sources/26020-Package_Requirements.docx` (project-wide; no `PKG-036`-specific slice located).
- Sibling deliverables `DEL-036-01` (Scope of Work) and `DEL-036-02` (Package Datasheet) provide upstream scope and technical handoff context where available; no human-declared upstream dependencies recorded in `_DEPENDENCIES.md`.

## Steps

1. **Read upstream context.** Read `_CONTEXT.md`, Gate 7 `DELIVERABLE_REGISTER.csv` and `PACKAGE_REGISTER.csv` rows for `DEL-036-03` / `PKG-036`, `ARTIFACT_REGISTER.csv` rows for `DEL-036-03`, `INTERFACE_REGISTER.csv` rows for `PKG-036`, and `OBJECTIVE_DELIVERABLE_MAP.csv` rows for `DEL-036-03`.
2. **Resolve identity discrepancies.** Confirm package identity (name, workbook row, WBS, CoA) against `PACKAGE_REGISTER.csv`. Log any source mismatches (see Guidance Conflict Table HRR-036-03-001) for human ruling; do not silently reconcile.
3. **Draft construction work package narrative (`ART-5AF99634D9`).** Cover package identity, EPC vs. Vendor responsibility split, building basis (prefabricated, modular, elevated on piles, bottom-entry, n+1 HVAC), grounding basis, internal wiring basis, and turnover gate. Cite `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` slices for every non-trivial claim.
4. **Draft installation and tie-in workface plan (`ART-0CFB00EEF8`).** Create one workface plan section per declared interface type from `INTERFACE_REGISTER.csv` for `PKG-036` (12 sections). Each section shall identify: the tie-in scope, the discipline counterpart, the sequencing relative to building set and energization, and the inspection or test that closes the tie-in.
5. **Draft construction interface and turnover checklist (`ART-A5CFBCEAB9`).** Build a line-item checklist that maps one or more verification items to each requirement in `Specification.md` (REQ-036-03-001 through REQ-036-03-010), and that records sign-off by the EPC Integrator and acceptance by commissioning.
6. **Internal cross-check.** Verify that the three artifacts are consistent: every workface plan section is reflected by a turnover checklist line item, and every Specification requirement traces to at least one checklist line item.
7. **Mark unresolved items.** Apply `TBD` where source evidence is unavailable (e.g., detailed ITP per REQ-036-03-010, schedule sequencing). Apply `ASSUMPTION` where inference was unavoidable (e.g., package-heuristic objective mapping). Do not invent values.
8. **Issue for review.** Place the three artifacts and this procedure record under EPC Integrator review. Capture review comments and re-issue. Defer turnover-checklist sign-off until field acceptance.

## Verification

- Each of the three mandatory artifacts exists in the deliverable folder or its designated output location.
- Each declared interface type from `INTERFACE_REGISTER.csv` for `PKG-036` is addressed in the workface plan.
- Each requirement in `Specification.md` traces to at least one turnover-checklist line item.
- Identity fields in the artifacts match `PACKAGE_REGISTER.csv` row `PKG-036`.
- `TBD` and `ASSUMPTION` markers remain explicit; no values were invented.

## Records

- Construction work package narrative (`ART-5AF99634D9`).
- Installation and tie-in workface plan (`ART-0CFB00EEF8`).
- Construction interface and turnover checklist (`ART-A5CFBCEAB9`), signed at field acceptance.
- Conflict Table entries in `Guidance.md` for any unresolved source disagreements.
- TASK run record in `_run_records/`.
