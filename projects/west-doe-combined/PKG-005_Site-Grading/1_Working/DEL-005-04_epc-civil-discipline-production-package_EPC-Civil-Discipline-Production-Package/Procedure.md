# Procedure: EPC / Civil Discipline Production Package

## Purpose

Define the working procedure for producing and checking the PKG-005 Site Grading civil discipline production package from accepted Gate 7 truth and accessible civil/site source basis.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- Workbook row 6 package/interface data is accessible through `_Sources/26020-Packages_Interfaces_4_export.xlsx`.
- Civil/site source basis is accessible in `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` and `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- No declared upstream dependencies are listed in `_DEPENDENCIES.md`.
- Responsible party assignment remains TBD; obtain human ruling before assigning to a specific EPC organization or subcontractor.

## Steps

1. Confirm deliverable identity.
   - Verify deliverable ID, package ID, WBS, CoA tracking number, discipline, type, and scope item against `_CONTEXT.md`, `DELIVERABLE_REGISTER.csv`, and `PACKAGE_REGISTER.csv`.

2. Confirm applicable interfaces.
   - Verify Drain / Containment and Grading / Site Drainage / Spill Containment are marked applicable for workbook row 6.
   - Record both interfaces in the discipline package basis and requirements closure record.

3. Establish the civil production basis.
   - Use the accepted artifact set: discipline production package basis, TBD discipline deliverable register, and source-limited requirements closure record.
   - Do not add unsupported discipline artifacts.

4. Extract source-supported civil criteria.
   - Include surface-water management, process-contaminated drainage routing, site grading principles, external input requirements, and open assumptions from the accessible DBM civil sections.
   - Mark any unavailable final design input as `TBD`.

5. Build the source-limited requirements closure record.
   - List each requirement with source path and section reference.
   - List unresolved inputs, including geotechnical report, topographical survey/grade surface file, plot plan/retention-pond reference, detailed drainage engineering, responsible party assignment, and detailed discipline deliverable register contents.

6. Check cross-document consistency.
   - Confirm Datasheet attributes appear in Specification requirements where appropriate.
   - Confirm Specification requirements have Procedure verification hooks.
   - Confirm Guidance does not overstate source-supported requirements.
   - Confirm terminology is consistent: "Site Grading", "Drain / Containment", "Grading / Site Drainage / Spill Containment", and "source-limited requirements closure record".

7. Prepare handoff package.
   - Include the production package basis, requirements closure record, open-input list, applicable interface list, and source citations.
   - Surface HRR-001 and HRR-002 for human ruling.

## Verification

| Check | Acceptance criterion |
|---|---|
| Identity check | Deliverable and package fields match Gate 7 registers and workbook row 6. |
| Interface check | Only source-supported applicable interfaces are included for PKG-005. |
| Civil criteria check | Grading/drainage/containment statements cite accessible DBM civil sections or are marked TBD. |
| Closure check | Detailed discipline requirements absent from sources remain open in the closure record. |
| Dependency check | No blockers are asserted unless declared in `_DEPENDENCIES.md`; current declared upstream/downstream lists are empty. |
| Human ruling check | Responsible party assignment and discipline deliverable register contents remain marked for ruling. |

## Records

- Discipline production package basis.
- Source-limited requirements closure record.
- TBD discipline deliverable register placeholder or ruling request.
- Applicable interface evidence for Drain / Containment and Grading / Site Drainage / Spill Containment.
- Open-input list for geotechnical, topographical, plot-plan, and detailed drainage closure.
- Human ruling log for HRR-001 and HRR-002.
