# Procedure: DEL-001-03_construction-work-package — Construction Work Package

## Purpose

Define a conservative procedure for producing and using the PKG-001 Construction Work Package for Earthworks for foundations from the accepted Gate 7 basis and locally accessible civil source material.

## Prerequisites

- Accepted Gate 7 decomposition snapshot is available.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, and `_DEPENDENCIES.md` have been read.
- Workbook source row is available: `26020-Packages_Interfaces_4_export.xlsx`, `Packages` row 2.
- DBM civil/construction source slices are available: `DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility and SEC-11.
- Declared upstream dependencies: none declared during PREPARATION.
- Required but unresolved construction inputs: geotechnical assessment report, topographical survey/grade surface file, detailed drainage design, plot plan/retention pond coordination, approved construction drawings, and approved inspection/turnover forms.

## Steps

1. Confirm package identity.
   - Verify deliverable ID, package ID, WBS, CoA tracking number, discipline, scope item, responsible party, and objective mapping against `_CONTEXT.md`, workbook row 2, and Gate 7 registers.

2. Establish construction scope boundary.
   - Include physical installation, construction, inspection, turnover, and tie-in planning for PKG-001 Earthworks for foundations.
   - Record exclusions as `TBD` where no source-supported package-specific exclusion exists.

3. Build the interface checklist.
   - Add the PKG-001 interface categories from workbook row 2 and `INTERFACE_REGISTER.csv`: Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports.
   - Add detailed checklist line items only where supported by approved drawings, DBM basis, or project forms; otherwise mark as `TBD`.

4. Build the workface plan.
   - Include applicable field construction activities from the 04-25 DBM construction responsibility basis, including grading, piling, foundation work, plant roads, field-erected buildings, off-loading and setting modules/equipment on foundations, structural supports, field cables, and terminations where applicable.
   - Distinguish EPC Integrator deliverable ownership from Tourmaline field construction execution responsibility.

5. Carry civil basis requirements into the package.
   - Include governing civil and structural standards listed in DBM-Deepcut SEC-11.
   - Include DBM grading, drainage, road, and foundation basis values only with source citation.
   - Keep geotechnical, topographical, survey, drainage-design, and construction drawing gaps as `TBD` until accepted inputs are available.

6. Prepare inspection and turnover records.
   - Name required record categories: grading/drainage inspection records, pile/foundation installation records, interface sign-off, open item log, and turnover checklist.
   - Leave final form numbers and acceptance criteria as `TBD` unless approved project forms are available.

7. Run cross-document consistency check.
   - Confirm that Datasheet attributes appear in Specification requirements where applicable.
   - Confirm that every Specification requirement has a corresponding Procedure verification or record hook.
   - Confirm that unsupported values remain `TBD`, `ASSUMPTION`, or conflict-table entries.

8. Route unresolved conflicts for human ruling.
   - Use the Guidance conflict table when source roles or requirements conflict.
   - Do not resolve responsibility conflicts without an accepted project RACI or human ruling.

## Verification

- Package identity matches workbook row 2 and Gate 7.
- Interface checklist includes both PKG-001 workbook interface facts.
- Civil basis values match DBM-Deepcut SEC-11 and are not overstated as final construction criteria where DBM says TBD or pending detailed engineering.
- Construction execution responsibility is not collapsed into deliverable ownership.
- All missing quantities, drawings, form IDs, and final construction criteria are marked `TBD`.

## Records

- Construction Work Package.
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.
- Open input / TBD register.
- Responsibility matrix or RACI reference: TBD.
- Inspection records: TBD final forms.
- Turnover package index: TBD final form/index structure.
