# Procedure: DEL-003-04_epc-civil-discipline-production-package

## Purpose

Define the working procedure to produce and verify the EPC / Civil Discipline Production Package for `PKG-003` Site Grading using accessible source materials, accepted Gate 7 decomposition truth, and explicit `TBD` treatment for unsupported detail.

## Prerequisites

- Accepted Gate 7 decomposition snapshot: `GATE-07_Final_Published_2026-05-24`.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, sheet `Packages`, workbook row 4.
- Package requirements source: `_Sources/26020-Package_Requirements.docx`, civil grading / spill containment interface entries.
- DBM civil basis sources:
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11.
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-02 and SEC-11.
- Required external inputs for final design closure:
  - Geotechnical assessment report.
  - Topographical survey and grade surface file.
  - Plot plan including retention pond reference.
  - Detailed engineering drainage design.

## Steps

1. Confirm package identity.
   - Verify deliverable ID, package ID, package name, discipline, type, responsible party, scope item, and objectives against `_CONTEXT.md` and Gate 7 `DELIVERABLE_REGISTER.csv`.

2. Confirm source availability.
   - Read workbook row 4 in `_Sources/26020-Packages_Interfaces_4_export.xlsx`.
   - Read the civil grading / spill containment interface entries in `_Sources/26020-Package_Requirements.docx`.
   - Read the DBM civil grading, drainage, surface-water, external-dependency, and rainfall-basis sections.

3. Build the production package index.
   - Include the discipline production package basis.
   - Include a discipline deliverable register or mark it `TBD`.
   - Include candidate artifacts `CIV-003`, `CIV-004`, `CIV-015`, and `CIV-019` only as source-supported candidate entries until approved.

4. Establish active interfaces.
   - Record Drain / Containment and Grading / Site Drainage / Spill Containment as active workbook interfaces.
   - Leave unmarked workbook interface columns out of the active interface set unless another accepted source adds them.

5. Compile civil grading and drainage criteria.
   - Carry source-supported criteria for pipe rack ridges, pad slope, maximum grade slope, ditch slope, culvert slope, storm basis, retention pond intent, and surface-control intent.
   - Mark final IDF duration, retention pond location, retention pond capacity, survey data, and geotechnical parameters as `TBD` where not closed.

6. Compile the requirements closure record.
   - For each requirement, record source path and section reference.
   - For each missing value, record `TBD`.
   - For each inferred item, label `ASSUMPTION`.
   - For unresolved authority or register questions, add or update the Conflict Table in `Guidance.md`.

7. Prepare discipline production outputs.
   - Produce or collect the Grading Plan, Drainage / Stormwater Management Report, Retention Pond / Containment Basin Design, and Civil MTO / Quantity Take-Off if authorized by the discipline scope.
   - If the final discipline deliverable register is not approved, keep the package at source-limited status.

8. Perform cross-document consistency checks.
   - Confirm terms, package identity, interface names, values, and `TBD` items are consistent across the datasheet, specification, guidance, procedure, and production package index.

## Verification

| Check | Acceptance Basis |
|---|---|
| Identity check | Matches `_CONTEXT.md` and Gate 7 `DELIVERABLE_REGISTER.csv` row `DEL-003-04`. |
| Interface check | Matches workbook row 4 active marks for Drain / Containment and Grading / Site Drainage / Spill Containment. |
| Criteria check | Grading and drainage values match DBM SEC-11 source slices or are marked `TBD`. |
| Dependency check | Geotechnical, topographical, plot-plan, retention pond, and detailed drainage inputs are listed as open until accepted. |
| Conflict check | Candidate discipline deliverable register uncertainty is surfaced for human ruling. |

## Records

- Discipline production package basis.
- Discipline deliverable register or `TBD` register placeholder.
- Requirements closure record.
- Source trace list.
- Grading Plan (`CIV-003`) if approved for this package.
- Drainage / Stormwater Management Report (`CIV-004`) if approved for this package.
- Retention Pond / Containment Basin Design (`CIV-015`) if approved for this package.
- Civil MTO / Quantity Take-Off (`CIV-019`) if approved for this package.
- Conflict Table entries requiring human ruling.
