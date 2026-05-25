# Procedure: DEL-005-02_package-datasheet - Package Datasheet

## Purpose

This procedure defines how to produce and verify the PKG-005 Site Grading package datasheet from the accepted Gate 7 decomposition truth and accessible source materials.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages row 6.
- DBM source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-02 and SEC-11.
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md`.
- Final hydrology inputs: TBD.
- Final geotechnical report: TBD.
- Package-specific civil grading/drainage design package: TBD.

## Steps

1. Confirm deliverable identity from `_CONTEXT.md` and Gate 7 DELIVERABLE_REGISTER row DEL-005-02_package-datasheet.
2. Confirm package identity from Gate 7 PACKAGE_REGISTER row PKG-005 and workbook Packages row 6.
3. Populate datasheet identification fields: package ID, workbook ID/row, WBS, CoA tracking number, discipline, responsible party, and source scope item.
4. Extract interface applicability from workbook Packages row 6 and Gate 7 INTERFACE_REGISTER.
5. Populate the interface requirements matrix with Drain / Containment and Grading / Site Drainage / Spill Containment as applicable.
6. Extract civil/site constraints from DBM SEC-02 and SEC-11, including surface-water management, contaminated drainage routing, preliminary hydrology basis, and geotechnical uncertainty.
7. Enter unsupported design values as `TBD`; do not infer final grading elevations, drainage sizing, retention volumes, or geotechnical design closure.
8. Cross-check the datasheet against Specification, Guidance, and Procedure for consistent terminology and values.
9. Record unresolved design-basis gaps in the Guidance conflict table or open items list for human/design-team ruling.

## Verification

| Check | Acceptance criterion |
|---|---|
| Identity check | Datasheet identity matches `_CONTEXT.md`, workbook row 6, and Gate 7 registers. |
| Interface check | Only source-supported applicable row-6 interfaces are listed as applicable. |
| Source-grounding check | Non-trivial civil/site/drainage claims cite workbook row 6, Gate 7 registers, or DBM SEC-02/SEC-11. |
| TBD check | Missing package-specific design values remain `TBD`. |
| Dependency check | Declared dependencies remain "none declared"; no advisory blocker is invented from undeclared relationships. |
| Consistency check | Datasheet, Specification, Guidance, and Procedure use the same names, IDs, and interface labels. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state transition record
- `_run_records/TASK_RUN_*.md`
