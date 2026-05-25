# Procedure: EPC / Civil Discipline Production Package

## Purpose

Define the source-limited procedure for producing and checking the Civil discipline production package for `PKG-004 - Site Grading`, WBS 02.

## Prerequisites

- Accepted Gate 7 decomposition snapshot is available.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- Gate 7 package row `PKG-004`, deliverable row `DEL-004-04_epc-civil-discipline-production-package`, scope row `SOW-0004`, and interface rows `IFC-FA26BF6895` and `IFC-D2D12F4CA2` are available.
- DBM 3-25 civil/site source slices are available for rainfall basis, SEC-11 civil and surface-water requirements, and SEC-15 standards/regulatory context.
- Declared upstream dependencies: none declared during PREPARATION.
- Final responsible party, civil drawing list, final hydrology update, and final geotechnical-report status are TBD.

## Steps

1. Confirm package identity against Gate 7:
   - Package: `PKG-004 - Site Grading`.
   - WBS: `02`.
   - Discipline: Civil.
   - CoA tracking number: `26020-01-42-003`.
   - Scope item: `SOW-0004`.
2. Confirm the production-package boundary:
   - Include the Site Grading production basis, discipline deliverable register placeholder, and source-limited requirements closure record.
   - Exclude final discipline deliverable lists and sealed design outputs until source material or human ruling supplies them.
3. Carry accepted interface facts into the package basis:
   - `Drain / Containment`.
   - `Grading / Site Drainage / Spill Containment`.
4. Establish the current civil design-basis assumptions:
   - Use the current site data and precipitation/storm basis from DBM 3-25.
   - Record that final hydrology inputs are required before final drainage, retention pond, or surface-water closure.
   - Record that final geotechnical reporting is required before foundation-dependent closure.
5. Draft or update the discipline production package basis:
   - Identify the Site Grading scope and WBS 02 boundary.
   - List source-supported civil topics: grading, drainage, roads/access interface, surface-water management, retention pond interface, and drain/containment routing.
   - Mark unsupported drawing numbers, calculation identifiers, quantities, elevations, slopes, and final ownership fields as `TBD`.
6. Draft or update the source-limited requirements closure record:
   - Link each requirement to Gate 7 register rows, workbook row 5, or DBM 3-25 source slices.
   - Label inferences as `ASSUMPTION`.
   - Send unresolved ownership, hydrology, geotechnical, and deliverable-register content to the human-ruling list.
7. Perform a consistency check:
   - Confirm package identity is identical across datasheet, specification, guidance, procedure, and the package basis.
   - Confirm interface terms match Gate 7 interface rows.
   - Confirm no unsupported final design values have been introduced.

## Verification

| Check | Acceptance criterion |
|---|---|
| Identity check | `PKG-004`, Site Grading, WBS 02, Civil, workbook row 5, and `26020-01-42-003` are consistently stated |
| Interface check | `Drain / Containment` and `Grading / Site Drainage / Spill Containment` are present and no additional interface type is invented |
| Source-grounding check | Non-trivial package requirements cite Gate 7 rows, workbook row 5, or DBM 3-25 source slices |
| Hydrology/geotechnical check | Current-basis work is separated from final closure and unresolved inputs are marked `TBD` |
| Artifact check | Discipline deliverable register remains `TBD` until source material or human ruling enumerates it |
| Dependency check | No blocker is asserted because no declared upstream dependencies exist for this deliverable |

## Records

- Discipline production package basis.
- TBD discipline deliverable register.
- Source-limited requirements closure record.
- Interface evidence for `IFC-FA26BF6895` and `IFC-D2D12F4CA2`.
- Human ruling log for responsible party, deliverable-register content, final hydrology inputs, and final geotechnical status.
