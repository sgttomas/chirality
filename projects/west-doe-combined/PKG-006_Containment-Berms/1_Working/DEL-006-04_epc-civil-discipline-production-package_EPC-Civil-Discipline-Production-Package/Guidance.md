# Guidance: EPC / Civil Discipline Production Package

## Purpose

This guidance supports production of the Civil discipline package for PKG-006 Containment Berms. The package exists to turn accepted Gate 7 package/interface truth and available civil DBM source slices into a controlled discipline production basis without inventing missing detailed engineering criteria.

## Principles

- Treat Gate 7 registers as accepted upstream truth for package identity, deliverable identity, objectives, artifacts, and interface facts.
- Treat DBM civil source slices as the governing source for civil grading, drainage, retention pond, and surface-control requirements.
- Keep unsupported detailed requirements as `TBD` rather than inferring final design values from package name alone.
- Preserve the distinction between package interface facts and final design deliverables: the workbook establishes Drain / Containment and Grading / Site Drainage / Spill Containment applicability, while detailed drainage and containment design remain dependent on later inputs.
- Use declared dependencies only when assessing blockers; this deliverable currently has no declared upstream or downstream dependencies in `_DEPENDENCIES.md`.

## Considerations

- The source set supports a containment-berm production basis, but not a final construction-ready civil design package. Gate 7 explicitly records that detailed discipline requirements are source-limited and remain open.
- Hydrology is not closed: the current rainfall basis uses NBCC 2020 Dawson Creek IDF data as a proxy pending site-specific update.
- The geotechnical assessment, topographical survey, grade surface file, plot plan, and detailed drainage design remain external inputs for final civil design.
- The DBM requires preventing uncontrolled offsite discharge and routing process-contaminated drainage to the proper drain or containment system, so production package content should not imply that contaminated drainage can discharge through surface-water paths.
- The NGL storage area containment language is a consideration requirement, not a finalized berm geometry. The package should carry it as a design consideration unless later detailed engineering assigns exact geometry, capacity, and location.

## Trade-offs

| Topic | Trade-off | Current treatment |
|---|---|---|
| Early production basis vs. final design closure | The package can define scope, interfaces, design criteria, and open inputs, but cannot close details that depend on missing survey, geotechnical, plot-plan, hydrology, or detailed drainage information. | Use a source-limited requirements closure record. |
| Containment functionality vs. surface-water management | Berms and surface controls must contain or redirect potential releases while still supporting drainage and operations access. | Maintain separate clean surface-water and process-contaminated drainage logic. |
| Workbook interface facts vs. civil DBM detail | Workbook facts establish that the interfaces apply; DBM slices define the available civil basis. | Cite both, and avoid adding unreferenced design values. |

## Examples

- Supported statement: "Drain / Containment applies to PKG-006." Source: INTERFACE_REGISTER.csv, IFC-62ACD644F9.
- Supported statement: "Facility pad grading slopes down from pipe racks at 1.5%, with possible reduction to 1.0% where required." Source: 4-25_Deepcut_DBM.md, Site Grading and Surface Water Management.
- Unsupported statement unless later evidence is added: "The containment berm height is [specific value]." Current treatment: `TBD`.
- Unsupported statement unless later evidence is added: "The retention pond capacity is [specific volume]." Current treatment: `TBD`.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HRR-006-04-001 | Responsible party is not fully assigned. | _CONTEXT.md, Identity: "TBD; EPC Integrator or discipline subcontractor as assigned" | PACKAGE_REGISTER.csv, PKG-006: responsibility is source-dependent | Datasheet Identification; Procedure Prerequisites; Specification Scope | Treat EPC Integrator as coordination owner until a discipline subcontractor is assigned. | TBD |
| HRR-006-04-002 | Detailed discipline deliverable register is not available. | _CONTEXT.md, Anticipated Artifacts | ARTIFACT_REGISTER.csv, ART-5AEDE189AA: detailed discipline requirements are not present and remain open | Specification Documentation; Procedure Records | Carry a TBD discipline deliverable register and source-limited closure record. | TBD |
| HRR-006-04-003 | Final drainage/containment design inputs are incomplete. | 4-25_Deepcut_DBM.md, External Dependencies | 3-25_Comp_and_Liquids_DBM.md, rainfall basis: hydrology uncertainty remains | Datasheet Conditions; Specification Requirements; Procedure Verification | Keep final hydrology, geotechnical, topographical, plot-plan, and detailed drainage values open until source inputs are accepted. | TBD |
