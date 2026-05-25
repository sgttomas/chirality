# Guidance: Construction Work Package

## Purpose

The Construction Work Package turns the accepted Containment Berms package basis into construction-facing instructions, checks, and turnover evidence. Its purpose is to show how `PKG-006` will be physically installed, built, inspected, turned over, and tied into facility drain/containment and grading/site drainage/spill containment systems.

Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-006-03_construction-work-package`; `ARTIFACT_REGISTER.csv` rows for `DEL-006-03_construction-work-package`.

## Principles

- Keep package identity and source basis visible. The construction package should carry `PKG-006`, workbook row 7, WBS 03, CoA tracking number `26020-03-42-006`, Civil discipline, and source references forward into the workface plan.
- Treat the Gate 7 registers as accepted decomposition truth for package identity, deliverable intent, artifacts, objectives, and interface labels.
- Treat DBM source slices as authority for facility-level construction, drainage, surface-water, geotechnical, environmental, and standards constraints.
- Preserve uncertainty. Hydrology, final geotechnical parameters, detailed civil specifications, and unavailable standards should remain `TBD` until accepted source material closes them.
- Do not infer vendor scope for this Civil package. Current package truth says EPC Integrator or discipline subcontractor responsibility is source-dependent and no separate vendor-package ownership model is inferred.

## Considerations

The most important package-specific construction controls are the two declared interface types: Drain / Containment and Grading / Site Drainage / Spill Containment. The DBM requires surface-water management to prevent uncontrolled offsite discharge, protect process areas, and support construction and operations access; process-contaminated drainage must route to the appropriate drain or containment system rather than surface-water discharge.

Construction planning should account for the broader 03-25 construction scope, including grading, piling, foundations, roads, buildings, module setting, mechanical hookups, interconnecting piping, cabling, lighting, fencing, security, and tie-in demolition/removal where required. Only the portions that affect Containment Berms should be carried into this deliverable as requirements.

Hydrology and geotechnical data are not fully closed. The DBM uses NBCC 2020 Dawson Creek IDF data as a rainfall proxy pending site-specific update, and it requires the final geotechnical report before foundation design closure. Construction work should therefore include readiness gates for final hydrology and geotechnical acceptance before treating berm construction criteria as final.

Standards and regulatory references are not fully available in the current source set. The CWP should carry verification requirements for civil/structural, environmental, water, and surface-water-management obligations rather than claiming final compliance from unavailable citations.

## Trade-offs

| Topic | Trade-off | Guidance |
|---|---|---|
| Early construction planning vs. final design certainty | Early CWP drafting helps define workface controls, but hydrology, geotechnical, and detailed civil criteria are incomplete. | Use `TBD` readiness gates instead of final acceptance claims. |
| Drainage control vs. surface-water discharge | Process-contaminated drainage cannot be treated as ordinary surface water. | Separate clean surface-water management from drain/containment routing in the checklist. |
| Package-local focus vs. facility integration | Containment Berms are a package, but their function depends on site drainage and spill containment interfaces. | Keep interface signoffs explicit and avoid isolated workface closure. |
| Source-limited standards vs. construction readiness | The DBM references standards and regulatory content that are not fully available. | Require verification of current project specifications, permits, and regulatory triggers before IFC/field release. |

## Examples

TBD - no source-provided Containment Berms installation example, berm detail, or completed turnover checklist is available in the current deliverable source set.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HRR-006-03-001 | The current source set identifies Containment Berms and two interface types, but does not provide detailed berm geometry, material/liner/coating requirements, or inspection acceptance criteria. | `PACKAGE_REGISTER.csv` row `PKG-006`; `INTERFACE_REGISTER.csv` rows for `PKG-006` | Missing IFC civil drawings / project civil specifications / detailed construction specifications | `Datasheet.md` Construction; `Specification.md` Requirements, Standards, Verification; `Procedure.md` Steps, Verification | Carry detailed criteria as `TBD` until accepted civil design/specification sources are available. | TBD |
| HRR-006-03-002 | Responsibility is assigned to EPC Integrator for this deliverable, while package execution responsibility is source-dependent between EPC Integrator and discipline subcontractor. | `_CONTEXT.md` Identity; `DELIVERABLE_REGISTER.csv` row `DEL-006-03` | `PACKAGE_REGISTER.csv` row `PKG-006` ResponsibilityModel | `Specification.md` Scope; `Procedure.md` Prerequisites, Steps | Treat EPC Integrator as deliverable owner; require human/project assignment for field execution/subcontractor responsibility before work release. | TBD |
