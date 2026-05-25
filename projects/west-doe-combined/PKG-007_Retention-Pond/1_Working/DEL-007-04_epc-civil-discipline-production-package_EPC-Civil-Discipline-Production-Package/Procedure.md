# Procedure: EPC / Civil Discipline Production Package

## Purpose

Define the bounded procedure for producing and checking the `PKG-007` Retention Pond EPC / Civil Discipline Production Package using accepted Gate 7 decomposition truth and accessible civil source slices.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- Accessible source materials include Gate 7 registers, workbook row 8 from `_Sources/26020-Packages_Interfaces_4_export.xlsx`, and DBM civil source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` and `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md`.
- External design inputs remain required before final detailed civil design closure: geotechnical assessment, topographical survey / grade surface file, plot plan, and detailed engineering drainage design.

## Steps

1. Confirm package identity against Gate 7 registers.
   - Verify `DEL-007-04`, `PKG-007`, Retention Pond, WBS 02, Civil discipline, and CoA tracking number `26020-02-42-007`.
   - Source: Gate 7 `DELIVERABLE_REGISTER.csv`; Gate 7 `PACKAGE_REGISTER.csv`; workbook row 8.

2. Establish the source-supported civil interface basis.
   - Carry Drain / Containment and Grading / Site Drainage / Spill Containment as applicable interface facts.
   - Do not add undeclared interface facts without source support or human ruling.
   - Source: Gate 7 `INTERFACE_REGISTER.csv`; workbook row 8.

3. Establish the civil design basis.
   - Use the DBM civil basis for grading, drainage, retention pond, roads, foundations, and ancillary civil scope.
   - Carry listed governing standards and methods.
   - Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `SEC-11 - Civil, Buildings, and Miscellaneous Facilities Basis`.

4. Capture grading, drainage, and retention pond requirements.
   - Include the requirement to prevent off-site surface overflow from entering the facility and direct/contain on-site overflow into a retention pond.
   - Include preliminary design principles for pad slope, grade slope, ditch slope, culvert slope, and ditch/culvert storm basis.
   - Mark final IDF duration, ditch/culvert sizing, retention pond capacity, and final pond location as TBD pending detailed engineering where not closed by source.

5. Record external inputs and blockers for final design closure.
   - Record geotechnical assessment report, topographical survey / grade surface file, plot plan including `CIV-235633-5002-001`, and detailed engineering drainage design.
   - Treat them as production-package open items unless current source evidence closes them.

6. Build the requirements closure record.
   - Map each production requirement to source, verification approach, status, and open item if applicable.
   - Use `TBD` for missing values and `ASSUMPTION` for any inference.

7. Check cross-document consistency.
   - Confirm Datasheet attributes align with Specification requirements.
   - Confirm Specification requirements have Procedure verification hooks.
   - Confirm Guidance does not overstate preliminary or external-input-dependent values.

8. Prepare records for handoff.
   - Include the discipline production package basis.
   - Include the source-limited requirements closure record.
   - Include a TBD discipline deliverable register or an explicit deferral until human assignment and design closure inputs are available.

## Verification

| Check | Acceptance basis |
|---|---|
| Identity check | `PKG-007`, `DEL-007-04`, Retention Pond, Civil, WBS 02, and CoA tracking number match Gate 7 registers and workbook row 8. |
| Interface check | Drain / Containment and Grading / Site Drainage / Spill Containment are carried; no unsupported interface facts are added. |
| Source-grounding check | Each non-trivial design requirement cites Gate 7 registers, workbook row 8, or DBM civil source sections. |
| Open-item check | Final pond capacity, final pond location, final IDF duration, detailed drainage sizing, geotechnical inputs, and topographical inputs remain TBD unless source evidence is later added. |
| Dependency check | Declared upstream blockers are checked against `_DEPENDENCIES.md`; none are currently declared. |

## Records

- Discipline production package basis.
- Source-limited requirements closure record.
- TBD discipline deliverable register.
- Interface closure evidence for Drain / Containment and Grading / Site Drainage / Spill Containment.
- External-input / open-item register for geotechnical, topographical, plot-plan, hydrology, and detailed-drainage items.
- Human ruling log for unresolved assignment and final design-closure items.
