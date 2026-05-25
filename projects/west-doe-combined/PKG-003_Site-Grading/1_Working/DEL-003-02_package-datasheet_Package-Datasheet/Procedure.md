# Procedure: DEL-003-02_package-datasheet — Package Datasheet

## Purpose

Define the bounded procedure for producing and checking the `PKG-003` Site Grading Package Datasheet from the accepted Gate 7 decomposition truth and accessible civil/grading source materials.

## Prerequisites

| Prerequisite | Current status |
|---|---|
| Accepted decomposition basis | Gate 7 final published PROJECT_DECOMP snapshot accepted on 2026-05-24 |
| Deliverable-local context | `_CONTEXT.md` available |
| Deliverable-local references | `_REFERENCES.md` available |
| Deliverable-local dependencies | `_DEPENDENCIES.md` available; no declared upstream dependencies |
| Workbook package source | `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages row with ID #3 / workbook row 4 available |
| Civil source slice | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 available |
| Supporting civil context | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-11 available as supporting context |

## Steps

1. Confirm `_STATUS.md` permits drafting.
   - Current allowed states for this run: `OPEN`, `INITIALIZED`, `SEMANTIC_READY`.
   - If the state is outside that set, stop and do not overwrite production documents.

2. Read the deliverable-local truth set.
   - Read `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and existing primary artifacts if present.
   - Record missing primary artifacts as initial-production gaps, not as source conflicts.

3. Confirm accepted decomposition identity.
   - Verify `DEL-003-02_package-datasheet` belongs to `PKG-003` Site Grading.
   - Verify it is an EPC Package Datasheet owned by the EPC Integrator.
   - Verify it covers `SOW-0003` and supports `OBJ-001`, `OBJ-007`, `OBJ-008`, and `OBJ-009` as accepted Gate 7 context.

4. Extract workbook row data.
   - Confirm WBS `01`, CoA tracking number `26020-01-42-003`, package name Site Grading, and discipline Civil.
   - Extract only workbook interface columns marked for the row: Drain / Containment and Grading / Site Drainage / Spill Containment.

5. Extract DBM civil/grading source slices.
   - Use DBM-Deepcut SEC-11 as the primary source for civil scope, governing standards, site grading, surface-water management, external dependencies, and source-declared TBDs.
   - Use DBM-Comp_and_Liquids SEC-11 only as supporting cross-facility context unless a later accepted source assigns 03-25-specific values to this package.

6. Populate the datasheet.
   - Enter identity and package attributes from `_CONTEXT.md`, workbook row 4, and Gate 7 registers.
   - Enter grading and drainage values only where present in the DBM source slice.
   - Mark unresolved values as `TBD` or `ASSUMPTION`.

7. Populate the specification.
   - Convert source-supported datasheet obligations into requirements.
   - Tie each requirement to a source and verification method.
   - Do not introduce clause-level requirements for standards whose detailed text is not included in the accessible source set.

8. Populate guidance.
   - Explain how to use the datasheet conservatively.
   - Record source-declared open items as design-development considerations.
   - Add a conflict-table entry only when two accessible sources disagree.

9. Perform P2 consistency checks.
   - Confirm datasheet values match specification requirements.
   - Confirm requirements have procedure verification hooks.
   - Confirm guidance does not overstate source support.
   - Confirm all unsupported details remain `TBD`, `ASSUMPTION`, or conflict-table entries.

10. Update status if safe.
   - If drafting succeeds and the prior state is still `OPEN`, update `_STATUS.md` to `INITIALIZED`.
   - Do not update any other metadata file.

## Verification

| Verification item | Method |
|---|---|
| Four documents exist | Confirm `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Status transition safety | Confirm `_STATUS.md` was `OPEN` before changing it to `INITIALIZED`. |
| Source grounding | Check every non-TBD design value against workbook row 4, Gate 7 registers, or DBM SEC-11 source slices. |
| Interface consistency | Confirm Drain / Containment and Grading / Site Drainage / Spill Containment appear consistently where interface facts are discussed. |
| TBD consistency | Confirm geotechnical, topographical, hydrology, retention pond, and detailed drainage closure items remain open unless a source closes them. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md`
- `_run_records/TASK_RUN_2026-05-24_1635.md`
