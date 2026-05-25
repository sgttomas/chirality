# Guidance: DEL-002-01_scope-of-work — Scope of Work

## Purpose

This deliverable anchors the EPC Integrator's scope definition for PKG-002, Earthworks for foundations. It should make the package boundary, workbook identity, physical interfaces, civil/foundation basis, and responsibility assumptions clear enough for downstream package datasheet, construction work package, and civil discipline production work.

Source: `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, and `ARTIFACT_REGISTER.csv`.

## Principles

- Treat Gate 7 as the accepted decomposition truth for package identity, deliverable identity, scope item, objective association, and artifact expectations.
- Treat workbook row 3 as the direct package/interface source for PKG-002 identity and interface flags.
- Treat DBM civil/site sections as source material for civil design basis, geotechnical limitations, surface-water management, and foundation-design conditions.
- Do not convert preliminary geotechnical values into closed construction criteria; keep values marked TBC or dependent on the final geotechnical report as open.
- Keep this document at scope-of-work level. Detailed calculations, IFC drawings, procurement packages, and construction turnover records should be referenced as downstream or sibling outputs unless a human ruling assigns them here.

## Considerations

The package is a Civil package with physical interfaces to grading/site drainage/spill containment and structural/foundations/supports. The scope should therefore bridge civil surface works and foundation support requirements without over-claiming detailed design closure.

The DBM source establishes that civil design covers grading, drainage, roads, surface-water management, retention pond, piling/foundations, module supports, tank foundations, pipe rack supports, truck-loading slabs, building foundations, fencing, and security. The same source states that the final geotechnical report is required before foundation design closure.

The site-specific basis includes elevation 673 m AMSL and design ambient temperature -40 deg C to +35 deg C. These values may be included as current basis values, but the scope should also preserve the source's warning that snow, wind, precipitation, seismic, and geotechnical assumptions are not fully closed where marked TBC.

ASSUMPTION: The scope-of-work deliverable should identify affected facility systems and civil interfaces, but should not assign detailed design responsibilities between EPC Integrator and discipline subcontractor beyond the source-supported statement that package responsibility is source-dependent.

## Trade-offs

| Topic | Conservative drafting position |
|---|---|
| Geotechnical criteria | Include current source values only as current/preliminary basis; defer closed criteria to final geotechnical report. |
| Responsibility assignment | State EPC Integrator ownership of this deliverable; leave execution responsibility as source-dependent where the Gate 7 package row does not close it. |
| Interface breadth | Include the two workbook-marked interface types; avoid adding unmarked utility, electrical, or controls interfaces unless needed for civil support context and supported by DBM text. |
| Scope level | State required scope content and verification checks; do not write detailed construction methods as if they are issued requirements. |

## Examples

TBD: No source-specific completed Scope of Work example was available in the deliverable-local truth set or accessible references.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-001 | Package execution responsibility is not fully closed: deliverable owner is EPC Integrator, while package responsibility may be EPC Integrator or discipline subcontractor. | `_CONTEXT.md`, Identity; Gate 7 `DELIVERABLE_REGISTER.csv`, DEL-002-01 row | Gate 7 `PACKAGE_REGISTER.csv`, PKG-002 row | Datasheet Attributes; Specification Requirements; Procedure Responsibility Assignment | Use EPC Integrator for deliverable ownership and mark package execution responsibility as source-dependent until assignment is confirmed. | TBD |
