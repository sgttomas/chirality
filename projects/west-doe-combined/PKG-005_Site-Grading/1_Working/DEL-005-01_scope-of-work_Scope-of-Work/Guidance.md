# Guidance: DEL-005-01_scope-of-work - Scope of Work

## Purpose

The `PKG-005 Site Grading` Scope of Work exists to give the EPC Integrator a governed, source-traceable package boundary for the WBS 03 Civil Site Grading scope. It should explain what the package does, what source basis controls it, which physical interfaces are known, what remains open, and how the package integrates into the 03-25 compressor station and liquids hub.

Sources: Gate 7 `DELIVERABLE_REGISTER.csv` row for `DEL-005-01_scope-of-work`; Gate 7 `SCOPE_LEDGER.csv` row for `SOW-0005`; Gate 7 `PROJECT_DECOMP.md` objectives OBJ-002, OBJ-007, OBJ-008, OBJ-009.

## Principles

- Preserve the Gate 7 package identity exactly: `PKG-005`, Site Grading, Civil, WBS 03, CoA tracking number `26020-01-42-003`.
- Treat the workbook row and Gate 7 registers as the accepted decomposition basis for package/deliverable identity.
- Use the 03-25 DBM as the source basis for civil, drainage, hydrology, geotechnical, and regulatory context where it is locally accessible.
- Keep the Scope of Work at boundary-definition level. Do not turn it into the package datasheet, construction work package, or discipline production package.
- Use `TBD` for unavailable values such as package-specific exclusions, final hydrology inputs, final geotechnical report outcomes, civil drawing references, equipment layout references, and detailed regulatory deliverables.
- State assumptions explicitly. Do not infer vendor-package ownership for this Civil package.

## Considerations

The package has two declared interface types in Gate 7: `Drain / Containment` and `Grading / Site Drainage / Spill Containment`. These should drive the integration narrative and open-item tracking. They do not, by themselves, define complete engineering criteria.

The DBM civil basis says civil design covers grading, drainage, roads, surface-water management, retention pond, piling/foundations, supports, slabs, building foundations, fencing, and security. For this Scope of Work, use that list to frame likely boundary topics, but keep detailed design criteria in downstream technical documents unless directly required for the scope boundary.

Hydrology and geotechnical maturity are important open controls. The DBM identifies current rainfall, precipitation, snow, seismic, and site basis values, but it also states that rainfall uses a Dawson Creek NBCC 2020 proxy pending site-specific update and that final geotechnical design parameters remain to be confirmed. The Scope of Work should therefore preserve these as constraints and open issues rather than closed construction criteria.

Stormwater and contaminated drainage should be separated in the narrative. DBM 03-25 requires surface-water management to prevent uncontrolled offsite discharge and protect process areas, and it requires process-contaminated drainage to be routed to the appropriate drain or containment system rather than surface-water discharge.

## Trade-offs

| Topic | Practical trade-off | Recommended handling |
|---|---|---|
| Boundary completeness vs. unsupported detail | The Scope of Work needs enough detail to guide downstream work, but the source set does not provide full package-specific design criteria. | Include package identity, interfaces, civil/drainage context, and open items; keep detailed values as `TBD` unless directly sourced. |
| EPC Integrator vs. discipline subcontractor responsibility | Gate 7 says responsibility is source-dependent. | Assign the deliverable to EPC Integrator while noting package execution may involve a discipline subcontractor as assigned. |
| Surface-water drainage vs. contaminated drainage | Treating all drainage as one system could hide containment requirements. | Keep surface-water management and process-contaminated drainage routing distinct. |
| Current basis vs. final design closure | DBM provides current basis values but flags hydrology and geotechnical items as not fully closed. | Present current basis as context and preserve final hydrology/geotechnical closure as `TBD`. |

## Examples

Example boundary statement:

> `PKG-005 Site Grading` covers the WBS 03 Civil site grading scope and its source-supported interfaces to Drain / Containment and Grading / Site Drainage / Spill Containment. The package scope must support surface-water collection, segregation, retention, construction and operations access, and protection of process areas, with final hydrology and geotechnical closure pending accepted source updates.

Example open item:

> Final hydrology inputs and final geotechnical report are not available in the current deliverable folder. Keep drainage, retention pond sizing, and foundation-related grading assumptions as `TBD` or current-basis placeholders until accepted source documents are issued.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-001 | Package-specific exclusions are not defined. | Gate 7 `PACKAGE_REGISTER.csv`, `PKG-005` says exclusions are `TBD`; no package-specific exclusions stated. | No deliverable-specific source slice copied during PREPARATION (`_REFERENCES.md`). | Datasheet Conditions; Specification Scope; Procedure Steps | Keep exclusions as `TBD` until a human or accepted source defines them. | TBD |
| HRR-002 | Final hydrology and geotechnical closure are pending. | DBM 03-25 `SEC-02` and `SEC-11` carry rainfall/geotechnical uncertainty and require final geotechnical confirmation. | No final hydrology update or final geotechnical report is available in the deliverable folder. | Datasheet Conditions; Specification Requirements; Procedure Verification | Use DBM current basis as context only; do not close design criteria. | TBD |
