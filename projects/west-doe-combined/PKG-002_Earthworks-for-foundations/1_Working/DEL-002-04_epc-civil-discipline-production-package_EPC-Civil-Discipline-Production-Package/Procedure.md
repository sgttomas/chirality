# Procedure: EPC / Civil Discipline Production Package

## Purpose

This procedure describes how to produce and check the source-limited EPC / Civil Discipline Production Package for `DEL-002-04` without overstating unsupported design detail.

## Prerequisites

- Accepted Gate 7 decomposition snapshot for PROJECT_DECOMP.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Accessible workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, `Packages` sheet row ID # 2.
- Accessible DBM source slices: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-01, SEC-02, and SEC-11.
- Accessible package coordination source: `_Sources/26020-Package_Requirements.docx`.
- Final geotechnical report: TBD; required before foundation design closure.
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm the deliverable identity from `_CONTEXT.md` and Gate 7 `DELIVERABLE_REGISTER.csv`.
2. Confirm the package identity from Gate 7 `PACKAGE_REGISTER.csv` and workbook `Packages` sheet row ID # 2.
3. Build the package interface matrix from workbook row ID # 2 and Gate 7 `INTERFACE_REGISTER.csv`.
4. Carry only the two applicable package interfaces unless later accepted source material adds more: Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports.
5. Extract Civil basis topics from DBM SEC-11 Site and Civil Conditions and Surface Water and Drainage.
6. Extract site/design condition values from DBM SEC-02 only with their source status, including `TBD`, `TBC`, placeholder, and current-basis labels.
7. Create or update the source-limited requirements closure record. Mark the final geotechnical report, discipline deliverable register, and any unstated civil code/specification details as `TBD`.
8. ASSUMPTION: If EPC execution requires drawing/calculation/model registers, create placeholders only after the responsible party confirms the required discipline deliverable list.
9. Cross-check the production package against the Datasheet, Specification, and Guidance documents for consistent package identity, interface names, source statuses, and `TBD` items.
10. Record unresolved conflicts or source gaps in the Guidance Conflict Table rather than resolving by engineering judgment alone.

## Verification

| Check | Expected result |
|---|---|
| Identity check | Deliverable ID, package ID, WBS, CoA tracking number, name, and discipline match `_CONTEXT.md`, Gate 7 registers, and workbook row ID # 2. |
| Interface check | Interface list includes Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports, with no unsupported additions. |
| Source-grounding check | Non-trivial requirements cite Gate 7, workbook, DOCX, or DBM source slices. |
| Geotechnical status check | Final geotechnical report remains required before foundation design closure. |
| TBD/ASSUMPTION check | Unsupported details are marked `TBD` or `ASSUMPTION`; no invented quantities, tolerances, drawing lists, or foundation types are included. |
| Cross-document consistency check | Datasheet, Specification, Guidance, and Procedure use the same package identity, source names, interface names, and open-item language. |

## Records

- Discipline production package basis.
- Package identity and interface matrix.
- Civil/site/foundation/drainage requirement summary.
- Source-limited requirements closure record.
- Geotechnical closure input status.
- Conflict Table entries and human rulings when available.
- TBD discipline deliverable register.
