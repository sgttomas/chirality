# Guidance: EPC / Civil Discipline Production Package

## Purpose

This document guides production of the civil discipline package for `PKG-007` Retention Pond. The purpose is to convert the accepted Gate 7 package basis and accessible DBM civil requirements into a bounded civil production package without inventing final design values that depend on external inputs.

## Principles

- Preserve the package as a workbook-defined Civil package: "Retention Pond", WBS 02, CoA tracking number `26020-02-42-007`. Source: Gate 7 `PACKAGE_REGISTER.csv`, `PKG-007`; workbook row 8.
- Treat Drain / Containment and Grading / Site Drainage / Spill Containment as the source-supported physical interfaces for this package. Source: Gate 7 `INTERFACE_REGISTER.csv`; workbook row 8.
- Ground civil requirements in the DBM civil basis. The 4-25 DBM states that civil scope applies to facility pad, drainage system, retention pond, roads, foundations, process and utility modules, permanent buildings, and ancillary buildings. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `SEC-11 - Civil, Buildings, and Miscellaneous Facilities Basis`.
- Keep detailed design values open where the source says they depend on geotechnical, topographical, plot-plan, hydrology, or detailed-engineering inputs.

## Considerations

The retention pond production package should be developed as a civil integration package, not as a vendor equipment package. Gate 7 identifies EPC Integrator or discipline subcontractor responsibility as source-dependent and does not infer a separate vendor-package ownership model for `PKG-007`.

The site grading and drainage source basis requires the design to prevent off-site surface overflow from entering the expansion facility while directing and containing on-site overflow into a retention pond. This creates a strong interface between grading, drainage, containment, and operating release-control practices. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `Site Grading and Surface Water Management`.

The preliminary DBM values are useful as starting design constraints, but they are not final closure values where the DBM names external dependencies. In particular, final retention pond capacity and location depend on detailed engineering drainage design and plot-plan coordination. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `External Dependencies`.

Hydrology remains uncertain. The 3-25 DBM states that the current rainfall basis uses NBCC 2020 Dawson Creek IDF data as a proxy and that civil drainage, retention pond sizing, and surface-water management must carry the uncertainty until final hydrology inputs are confirmed. This package should therefore expose the hydrology basis and not silently close it. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, `SEC-02` rainfall basis.

## Trade-offs

| Topic | Trade-off / treatment |
|---|---|
| Preliminary DBM values vs. final engineering | Use DBM values to structure the production basis, but mark final pond capacity, final pond location, final IDF duration, and final ditch/culvert sizing as TBD until detailed inputs are available. |
| Package self-containment vs. external dependencies | The production package should be usable as a civil work package basis while clearly identifying geotechnical, topographical, plot-plan, and detailed-drainage dependencies. |
| Interface completeness vs. source fidelity | Only two interface facts are source-supported for workbook row 8. Additional interfaces should not be added without source support or human ruling. |

## Examples

Source-supported examples to carry into the package:

- Interface fact: Drain / Containment = applicable. Source: workbook row 8; Gate 7 `INTERFACE_REGISTER.csv`, `IFC-AB14FD2A67`.
- Interface fact: Grading / Site Drainage / Spill Containment = applicable. Source: workbook row 8; Gate 7 `INTERFACE_REGISTER.csv`, `IFC-1B8CFB3D40`.
- External dependency: plot plan including `CIV-235633-5002-001` retention-pond reference for approximate location and civil layout coordination. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `External Dependencies`.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-00704-001 | Responsible party is not closed: the deliverable is assigned to "TBD; EPC Integrator or discipline subcontractor as assigned." | Gate 7 `DELIVERABLE_REGISTER.csv`, `DEL-007-04` | `_CONTEXT.md`, Identity | Datasheet Identification; Specification Scope; Procedure Prerequisites | Keep responsible party as TBD until assignment is made. | TBD |
| HRR-00704-002 | Discipline deliverable register contents are not source-defined. | Gate 7 `DELIVERABLE_REGISTER.csv`, `DEL-007-04` anticipated artifacts | Gate 7 `ARTIFACT_REGISTER.csv`, `DEL-007-04` artifacts | Specification Documentation; Procedure Records | Produce a placeholder register requirement only; do not invent deliverable list. | TBD |
| HRR-00704-003 | Final retention pond capacity, location, and detailed drainage sizing are unresolved external-input items. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `Site Grading and Surface Water Management` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `External Dependencies` | Datasheet Conditions; Specification Requirements; Procedure Steps | Carry DBM preliminary basis and mark final values TBD pending detailed engineering inputs. | TBD |
