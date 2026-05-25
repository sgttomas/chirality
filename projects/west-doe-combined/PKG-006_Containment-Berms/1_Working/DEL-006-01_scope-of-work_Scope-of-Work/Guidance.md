# Guidance: DEL-006-01_scope-of-work — Scope of Work

## Purpose

This guidance supports drafting and review of the `PKG-006 — Containment Berms` EPC scope of work. The deliverable exists to turn the accepted decomposition basis for SOW-0006 into a bounded Civil package scope with clear interfaces, source basis, responsibility assignment, and integration narrative.

## Principles

- Preserve the Gate 7 package identity exactly: `PKG-006`, `Containment Berms`, Civil, WBS 03, CoA tracking number `26020-03-42-006` (`PACKAGE_REGISTER.csv`, PKG-006).
- Treat the workbook row and Gate 7 registers as the authoritative decomposition truth for package membership and deliverable identity.
- Treat the 03-25 DBM civil and drainage sections as source context for civil, site, surface-water, and process-contaminated drainage requirements (`3-25_Comp_and_Liquids_DBM.md`, SEC-11).
- Use `TBD` for package-specific design values not present in accessible sources. Do not infer berm capacity, dimensions, slopes, liner details, or materials from package name alone.
- Keep responsibility assignment conservative: EPC Integrator or discipline subcontractor responsibility is source-dependent; no vendor package ownership model is inferred (`PACKAGE_REGISTER.csv`, PKG-006).

## Considerations

The Containment Berms scope is primarily an interface and civil-integration deliverable at this phase. The package has two declared physical interface types: Drain / Containment and Grading / Site Drainage / Spill Containment. These interfaces should drive the scope-of-work table, boundary narrative, and verification checklist.

The 03-25 DBM establishes that civil design covers grading, drainage, roads, surface-water management, retention pond, foundations/supports, slabs, buildings, fencing, and security. For this deliverable, only the containment berm and directly related drainage/grading interfaces should be claimed unless the detailed civil design expands the boundary.

Surface-water language should distinguish clean stormwater management from process-contaminated drainage. The DBM requires process-contaminated drainage to route to the appropriate drain or containment system rather than surface-water discharge. The scope should therefore identify the interface to drain/containment systems but avoid naming a final drain destination unless detailed design confirms it.

## Trade-offs

| Topic | Guidance |
|---|---|
| Early scope completeness vs source fidelity | Include the required EPC scope-of-work structure now, but leave unsupported design values as `TBD`. |
| General civil basis vs package-specific detail | Use SEC-11 to define civil and drainage obligations; do not convert general civil text into berm geometry or quantities. |
| Responsibility assignment | Record EPC Integrator / civil discipline subcontractor as source-dependent and request final assignment instead of choosing one. |
| Hydrology and geotechnical closure | Carry current DBM basis as provisional and require final hydrology/geotechnical confirmation before final construction criteria. |

## Examples

- Acceptable wording: "The package includes Drain / Containment and Grading / Site Drainage / Spill Containment interfaces, per Gate 7 interface register."
- Acceptable wording: "Berm dimensions and containment volume are TBD pending detailed civil design."
- Avoid: "The berm shall provide [specific volume] containment" unless a cited source provides that value.
- Avoid: "The package is vendor supplied" because the source does not infer a separate vendor ownership model for PKG-006.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-006-01 | Final responsible party is source-dependent: EPC Integrator vs discipline subcontractor assignment is not closed. | `DELIVERABLE_REGISTER.csv`, DEL-006-01_scope-of-work lists EPC Integrator | `PACKAGE_REGISTER.csv`, PKG-006 says EPC Integrator or discipline subcontractor responsibility is source-dependent | Datasheet Identification; Specification Requirements; Procedure Prerequisites | Use EPC Integrator as deliverable owner and carry final execution assignment as TBD. | TBD |
| HRR-006-02 | Package-specific berm criteria are not available in accessible source slices. | `PACKAGE_REGISTER.csv`, PKG-006 gives interface types only | `3-25_Comp_and_Liquids_DBM.md`, SEC-11 gives general civil/drainage basis but not berm dimensions or capacity | Datasheet Construction; Specification Requirements; Procedure Steps | Mark berm geometry, containment volume, materials, liner system, and coordinates as TBD pending detailed civil design/human ruling. | TBD |
