# Package Datasheet Procedure

## Purpose

This procedure defines the controlled steps to produce and verify the `PKG-001 - Earthworks for foundations` package datasheet for EPC Integrator handoff.

## Prerequisites

- Access to the deliverable-local truth set: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, and `_DEPENDENCIES.md`.
- Access to Gate 7 PROJECT_DECOMP snapshot registers:
  - `PACKAGE_REGISTER.csv`
  - `DELIVERABLE_REGISTER.csv`
  - `ARTIFACT_REGISTER.csv`
  - `INTERFACE_REGISTER.csv`
  - `OBJECTIVE_DELIVERABLE_MAP.csv`
- Access to source workbook `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx`.
- Access to DBM civil source slice `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Civil Scope through Assumptions, TBDs, and Design Development Requirements.
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm deliverable identity from `_CONTEXT.md`.
   - Verify deliverable ID `DEL-001-02_package-datasheet`.
   - Verify parent package `PKG-001 - Earthworks for foundations`.
   - Verify discipline Civil and responsible party EPC Integrator.

2. Confirm overwrite eligibility from `_STATUS.md`.
   - Proceed with drafting only if the current state is within the allowed overwrite states for the run.
   - For this Pass 1/2 run, OPEN is eligible for drafting and safe transition to INITIALIZED.

3. Read the authoritative reference set.
   - Read workbook row 2 from `26020-Packages_Interfaces_4_export.xlsx`.
   - Read Gate 7 register rows for `PKG-001`, `DEL-001-02_package-datasheet`, and the two PKG-001 interface records.
   - Read DBM-Deepcut civil source sections for civil scope, standards, geotechnical/topographical assumptions, grading/drainage, roads, piles/foundations, buildings, external dependencies, and open assumptions.

4. Populate datasheet identity and attributes.
   - Enter workbook ID, WBS, CoA tracking number, package name, discipline, responsibility model, inclusion criteria, exclusions, and source basis.
   - Use `TBD` for missing package-specific exclusions or detailed equipment lists.

5. Populate design-basis conditions and construction criteria.
   - Include only source-supported civil criteria and units.
   - Preserve geotechnical, topographical, plot-plan, drainage, and dynamic-analysis dependencies as `TBD` or "to be confirmed" according to source wording.

6. Populate the interface requirements matrix.
   - Include `IFC-293AF03D4E` for Grading / Site Drainage / Spill Containment.
   - Include `IFC-1E47AB3801` for Structural / Foundations / Supports.
   - Do not add unmarked interface types without new source evidence.

7. Cross-check the four documents.
   - Confirm consistent use of package ID, package name, deliverable ID, interface names, and source paths.
   - Confirm datasheet criteria appear in the specification verification table where appropriate.
   - Confirm unresolved items appear as `TBD`, `ASSUMPTION`, or guidance open items rather than unsupported requirements.

8. Update status only when safe.
   - If the pre-run state is OPEN and Pass 1/2 completed, update `_STATUS.md` to INITIALIZED using the approved status helper or equivalent safe update.
   - Do not regress status if it is already beyond OPEN.

## Verification

| Check | Acceptance criterion |
|---|---|
| Identity verification | Datasheet identity matches `_CONTEXT.md`, Workbook row 2, and Gate 7 package/deliverable registers. |
| Interface verification | Interface matrix contains the two applicable PKG-001 interface records and no unsupported additional interface facts. |
| Source-grounding verification | Non-trivial design criteria cite workbook, Gate 7 registers, or DBM-Deepcut civil source sections. |
| TBD verification | Missing final values remain marked TBD or to be confirmed. |
| Cross-document verification | Datasheet, Specification, Guidance, and Procedure use consistent terminology and values. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` history entry for safe transition to INITIALIZED, if applied
- `_run_records/TASK_RUN_*.md`
