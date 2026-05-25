# Procedure: DEL-001-04_epc-civil-discipline-production-package

## Purpose

This procedure defines a conservative workflow to produce and verify the EPC / Civil Discipline Production Package for PKG-001, Earthworks for foundations, using the locally accessible workbook, Gate 7 decomposition basis, and DBM civil source slices.

## Prerequisites

- Current deliverable-local context files: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`.
- Accepted Gate 7 PROJECT_DECOMP snapshot at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`.
- Workbook source `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx`, `Packages` sheet row 2.
- DBM source `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, especially SEC-02 and SEC-11.
- No declared upstream dependencies are listed in `_DEPENDENCIES.md` as of PREPARATION.
- External inputs remain required for closure: geotechnical assessment report, topographical survey and grade-surface file, plot plan CIV-235633-5002, detailed engineering drainage design, and applicable dynamic analysis.

## Steps

1. Confirm package identity from workbook row 2: WBS 01, CoA tracking number 26020-01-42-001, package name Earthworks for foundations, and Civil discipline.
2. Confirm package interface flags from workbook row 2: Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports.
3. Confirm deliverable identity from Gate 7 `DELIVERABLE_REGISTER.csv`: DEL-001-04, EPC / Civil Discipline Production Package, type EPC/Discipline Production Unit, and anticipated artifacts.
4. Confirm package basis from Gate 7 `PACKAGE_REGISTER.csv`: PKG-001 scope description, responsibility model, source references, and objective support.
5. Extract applicable DBM civil basis from SEC-11, including civil scope, governing standards, geotechnical/topographical assumptions, grading and drainage principles, roads, piles/foundations, and external dependencies.
6. Build the discipline production package basis using only supported source content. Mark missing values as `TBD`; label inferred items as `ASSUMPTION`.
7. Prepare the TBD discipline deliverable register. At this source maturity, include a placeholder register if the discipline deliverables are not assigned by an accepted source.
8. Prepare the source-limited requirements closure record. Include at minimum the open geotechnical, topographical, plot-plan, detailed drainage, pavement, geotextile, retention pond, and dynamic-analysis inputs identified by DBM SEC-11.
9. Cross-check the draft against the Specification requirements and Datasheet attributes. Resolve mismatches from the workbook, Gate 7 registers, or DBM slices before issuing.
10. Surface any unresolved contradiction in the Guidance conflict table for human ruling.

## Verification

| Check | Acceptance Criteria |
|---|---|
| Identity check | Package and deliverable IDs, name, WBS, CoA tracking number, discipline, and responsible party match workbook row 2 and Gate 7 registers. |
| Interface check | Workbook interface flags are present and consistently named across Datasheet, Specification, Guidance, and Procedure. |
| Source basis check | DBM SEC-11 civil scope and governing basis are referenced for civil criteria. |
| TBD discipline check | Missing or unresolved detailed discipline requirements are not replaced by invented values. |
| External input check | Geotechnical, topographical, plot-plan, drainage, pavement, retention pond, and dynamic-analysis dependencies are recorded as open until accepted. |
| Cross-document check | Requirement IDs in Specification have corresponding production or verification hooks in Procedure. |

## Records

- Discipline production package basis.
- TBD discipline deliverable register.
- Source-limited requirements closure record.
- Workbook row 2 identity and interface evidence.
- Gate 7 register traceability evidence.
- DBM SEC-11 civil basis evidence.
- Human-ruling log for unresolved conflicts, if any.
