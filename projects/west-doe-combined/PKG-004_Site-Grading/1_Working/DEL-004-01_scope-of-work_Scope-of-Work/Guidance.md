# Guidance: Scope of Work

## Purpose

The PKG-004 Site Grading scope of work is the EPC Integrator's anchor document for defining the package boundary, source basis, interfaces, and integration narrative for Civil site grading. It should make the package executable without overstating final engineering values that remain dependent on geotechnical, survey, hydrology, plot-plan, and detailed engineering inputs.

Sources: `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` row `DEL-004-01_scope-of-work`; Gate 7 `PACKAGE_REGISTER.csv` row `PKG-004`.

## Principles

- Treat the Gate 7 snapshot as the accepted decomposition truth for package identity, deliverable artifacts, objective mapping, and registered interfaces.
- Treat the workbook package row as the source for WBS, CoA tracking number, package name, discipline, and interface flags.
- Treat DBM grading/drainage source slices as the source for civil design principles and numerical grading/drainage basis.
- Preserve `TBD` where the DBM assigns closure to the geotechnical report, topographical survey, plot plan, or detailed engineering.
- Keep Drain / Containment and Grading / Site Drainage / Spill Containment visible as the active interface basis.
- Use objectives OBJ-002, OBJ-007, OBJ-008, and OBJ-009 as context for why the package matters, not as a substitute for source-supported requirements.

## Considerations

Site grading is an integration-heavy Civil package. The scope of work should be structured around what the package must define, what inputs it depends on, and what cannot be closed until later design phases.

Important considerations include:

- The topographical survey and grade surface file are prerequisites for final grading and drainage design.
- Geotechnical report outputs remain open for bearing capacity, LPILE curves, dynamic criteria, road granular pavement design parameters, pavement layer thicknesses, and geotextile need.
- Drainage design must prevent off-site surface overflow from entering the expansion facility and direct/contain on-site overflow into a retention pond.
- Surface-control features may be needed around selected equipment to prevent on-site releases from discharging outside facility boundaries.
- Retention pond location and capacity are not final; they depend on detailed engineering and plot plan development.
- NGL storage area grading and surface-control provisions should be considered for accidental leak or spill containment where they intersect this package boundary.

Sources: `4-25_Deepcut_DBM.md`, `Geotechnical and Topographical Assumptions`, `Site Grading and Surface Water Management`; `3-25_Comp_and_Liquids_DBM.md`, civil design slices at lines 124 and 688.

## Trade-offs

| Trade-off | Guidance |
|---|---|
| Early scope clarity vs. final engineering values | Define the package boundary and required studies now; leave report-dependent values as `TBD`. |
| Drainage containment vs. grading constructability | Retain DBM slopes and storm basis; allow detailed engineering/geotechnical report to justify specifically engineered exceptions. |
| Package-specific scope vs. whole-facility integration | Keep package identity local to PKG-004 while explicitly naming facility-level interfaces that affect drainage and spill containment. |
| Objective alignment vs. requirement inflation | Reference objectives as directional context only unless the requirement is independently supported by the workbook, Gate 7 register, or DBM source slice. |

## Examples

Appropriate source-grounded wording:

- "The package carries Drain / Containment and Grading / Site Drainage / Spill Containment interfaces from workbook row 5 and Gate 7 `INTERFACE_REGISTER.csv`."
- "Retention pond location and capacity are TBD pending detailed engineering and plot plan development."
- "Facility pad grading shall use 1.5% slopes down from pipe racks to each side, with reduction to 1.0% only where required to maintain reasonable top-of-pile-cap elevations."

Wording to avoid:

- "All grading design is complete."
- "Tagged equipment list: none." Use `TBD` unless the source explicitly states there is no tagged equipment.
- Clause-level external code requirements not present in the accessible source slices.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-001 | Package responsibility is assigned to EPC Integrator in the deliverable context, while the package register says EPC Integrator or discipline subcontractor responsibility is source-dependent. | `_CONTEXT.md` Identity; Gate 7 `DELIVERABLE_REGISTER.csv` row `DEL-004-01_scope-of-work` | Gate 7 `PACKAGE_REGISTER.csv` row `PKG-004` | Datasheet Attributes; Specification Scope; Procedure Prerequisites | Use EPC Integrator as deliverable owner and retain discipline subcontractor as possible execution support until responsibility assignment is ruled. | TBD |
