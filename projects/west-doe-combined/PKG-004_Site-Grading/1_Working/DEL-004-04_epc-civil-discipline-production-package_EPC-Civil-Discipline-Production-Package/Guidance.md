# Guidance: EPC / Civil Discipline Production Package

## Purpose

This deliverable exists to provide a bounded Civil production package for `PKG-004 - Site Grading`, WBS 02. It should make the accepted Gate 7 package basis usable by an EPC Integrator or assigned discipline subcontractor without overstating source-limited details that are not yet present in the accepted package.

## Principles

- Preserve package identity exactly: `PKG-004`, Site Grading, WBS 02, Civil discipline, workbook row 5, CoA tracking number `26020-01-42-003`.
- Treat workbook row 5 and the accepted Gate 7 registers as the controlling package identity and interface basis.
- Treat DBM 3-25 civil, surface-water, regulatory, and standards sections as the available source slices for civil/site design intent.
- Keep final design values, deliverable lists, and closure criteria as `TBD` where the current source set does not provide them.
- Use the interface facts as coordination anchors, not as standalone proof that all detailed civil deliverables are complete.

## Considerations

The Site Grading production package is tied to the 03-25 compressor station and liquids hub scope. DBM 3-25 states that civil design covers grading, drainage, roads, surface-water management, retention pond, piling/foundations, module supports, tank foundations, pipe rack supports, truck-loading slabs, building foundations, fencing, and security. For this deliverable, only the Site Grading subset and its two recorded interfaces should be treated as in scope unless later human direction or source material expands the package.

The rainfall basis is provisional. DBM 3-25 uses NBCC 2020 Dawson Creek intensity-duration-frequency data as a proxy pending any site-specific update, and it explicitly carries uncertainty for civil drainage, retention pond sizing, and surface-water management until final hydrology inputs are confirmed. This package should therefore distinguish current-basis design work from final closure.

The geotechnical basis is also provisional. DBM 3-25 states that final geotechnical reporting is required before foundation design closure. If Site Grading production outputs rely on final elevations, slopes, pavement sections, foundation-adjacent grading, or support conditions, the package should show the geotechnical status instead of implying closure.

## Trade-offs

| Topic | Guidance |
|---|---|
| Current storm basis vs final hydrology | Use the current precipitation and storm basis for preliminary production alignment, but mark final hydrology-dependent closure as `TBD` until confirmed. |
| Site grading vs broader civil scope | Keep this package focused on Site Grading. Reference adjacent civil topics only where they affect grading, drainage, surface-water, access, or containment interfaces. |
| Workbook interface flags vs detailed interface requirements | Carry `Drain / Containment` and `Grading / Site Drainage / Spill Containment` as accepted interface facts. Do not infer detailed pipe, ditch, pond, berm, or containment geometry without source support. |
| EPC Integrator vs subcontractor ownership | The responsible party remains `TBD; EPC Integrator or discipline subcontractor as assigned`. Do not assign final accountability without human ruling. |

## Examples

- Source-supported interface entry: `Grading / Site Drainage / Spill Containment` applies to `PKG-004` from workbook row 5 and Gate 7 interface row `IFC-D2D12F4CA2`.
- Source-supported design-basis note: retention pond sizing and drainage design use the current precipitation and storm basis until hydrology is updated, per DBM 3-25 SEC-11.
- Unsupported detail that must remain `TBD`: final civil drawing list, grading drawing numbers, drainage calculation identifiers, and final discipline subcontractor ownership.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HRR-001 | Responsible party is not finally assigned between EPC Integrator and discipline subcontractor. | `_CONTEXT.md`, Identity | `DELIVERABLE_REGISTER.csv` row `DEL-004-04` | Datasheet Identification; Specification Requirements; Procedure Prerequisites | Keep as `TBD; EPC Integrator or discipline subcontractor as assigned` until project assignment. | TBD |
| HRR-002 | Discipline deliverable register content is anticipated but not source-enumerated. | `_CONTEXT.md`, Anticipated Artifacts | `ARTIFACT_REGISTER.csv`, no rows for `DEL-004-04` | Datasheet Construction; Specification Documentation; Procedure Records | Initialize a placeholder register requirement only; do not invent drawing/calculation list. | TBD |
| HRR-003 | Final hydrology inputs are not confirmed for drainage and surface-water closure. | DBM 3-25 rainfall-basis paragraph and SEC-11 Surface Water and Drainage | Current deliverable context has no hydrology update source | Specification Requirements; Procedure Verification | Use current precipitation/storm basis for preliminary work; require hydrology update status before final closure. | TBD |
