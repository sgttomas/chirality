# Guidance — DEL-106-03 Construction Work Package (Yard Lighting)

> Directional guidance for the EPC Integrator producing the Construction Work Package. Rationale is drawn from the GATE-07 accepted decomposition snapshot and from the responsibility-model and objective set associated with `PKG-106`.

## Purpose

The Construction Work Package translates the vendor-engineered yard-lighting package and the EPC Scope of Work / Package Datasheet into a buildable, inspectable, and turnover-ready installation plan that integrates the package into the operating facility. It is the construction-facing anchor between vendor delivery (`DEL-106-04`/`DEL-106-05`) and EPC acceptance (`DEL-106-06`). Source: `DELIVERABLE_REGISTER.csv` (`DEL-106-03` Description, Notes); `PACKAGE_REGISTER.csv` (ResponsibilityModel).

## Principles

- **Responsibility fidelity.** Preserve the Package-Vendor / EPC-Integrator split throughout: vendor designs/supplies the lighting package; EPC plans the installation, tie-ins, inspections, and turnover. (Source: `PACKAGE_REGISTER.csv`; OBJ-004.)
- **Interface-led construction.** Treat the three applicable PKG-106 interfaces — Electrical Power, Grounding/Bonding, Area/Exterior Lighting — as the spine of the workface plan. (Source: `INTERFACE_REGISTER.csv` PKG-106.)
- **Source-grounded values.** Do not invent loads, classifications, fixture data, or code citations. If the value is not in an accessible source slice, mark `TBD` and surface it. (Source: `four-documents` skill constraint; `_REFERENCES.md`.)
- **Gate 5 anchor.** Treat the construction work package as a Gate-5 deliverable whose downstream is `DEL-106-06` acceptance and operations turnover. (Source: `_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv`.)

## Considerations

- **Civil/structural coupling.** Yard-lighting installation typically requires pole foundations, trenching, conduit routing, and access. OBJ-008 explicitly covers civil/structural/site/construction support; coordinate with the relevant civil/structural packages even though they are out of `DEL-106-03` scope. (Source: `OBJECTIVE_REGISTER.csv` OBJ-008.)
- **Sour-service & area classification.** The 04-25 facility processes sour gas (OBJ-001, OBJ-009). Exterior lighting in or adjacent to classified areas requires fixture suitability and bonding/grounding rigor. Specific classification boundaries and fixture suitability are `TBD` pending DBM-Deepcut SEC-12/SEC-15 and area-classification documents being accessible as deliverable-local slices.
- **Power & grounding tie-in.** Coordinate with the facility electrical basis (DBM SEC-12). Distribution panel source, breaker coordination, lighting-circuit topology, and grounding-grid connection points are `TBD` here.
- **Commissioning, turnover, and operability.** Per OBJ-010, sparing, isolation, winterization, commissioning, and turnover evidence should be reflected in the checklist artifact (`ART-FC16B15401`).
- **Vendor handoff timing.** Construction sequencing depends on vendor-package availability (`DEL-106-04`) and vendor documentation (`DEL-106-05`). Treat their accepted snapshots as construction inputs.

## Trade-offs

- **Detail vs source fidelity.** Adding plausible-sounding construction steps without source backing is forbidden by the skill. Where source slices are not deliverable-local, prefer fewer steps marked `TBD` over more steps that overstate the source. (Source: `four-documents` skill, Authority hierarchy.)
- **Workface granularity vs maintainability.** Excessively granular workface tasks can outpace package-vendor design lockdown; coarse workface tasks risk missing tie-in detail. Decision deferred until vendor handoff basis is available — `TBD`.
- **Construction-led vs operations-led turnover.** OBJ-010 favors maintainability/operability evidence at turnover; balance against construction completion pressure. Document the chosen point of demarcation in the checklist.

## Examples

- No source-grounded worked examples are available in deliverable-local slices. Examples deferred — `TBD`.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFL-001 | OBJ-008 (civil/structural/site/construction-support) is mapped to `DEL-106-03` via the objective-deliverable map, but `_CONTEXT.md` Scope and `PACKAGE_REGISTER.csv` ResponsibilityModel locate civil/structural ownership outside the vendor-electrical package responsibility. Question: does `DEL-106-03` author civil tie-in content, or only coordinate with civil/structural packages? | `OBJECTIVE_DELIVERABLE_MAP.csv` (OBJ-008 → DEL-106-03) | `_CONTEXT.md` Scope; `PACKAGE_REGISTER.csv` (PKG-106 ResponsibilityModel — Electrical discipline, vendor-owned package) | Specification R-6; Guidance Considerations (civil/structural coupling); Procedure prerequisites | PROPOSAL: `DEL-106-03` documents coordination requirements and tie-in interfaces to civil/structural packages but does not author civil/structural design content. | TBD |
| CFL-002 | OBJ-008 mapping is recorded against `DEL-106-03` in `OBJECTIVE_DELIVERABLE_MAP.csv` but `DELIVERABLE_REGISTER.csv` `SupportsObjectives` column for `DEL-106-03` reads `OBJ-001; OBJ-004; OBJ-005; OBJ-009; OBJ-010` (omits OBJ-008). `_CONTEXT.md` Supports Objectives includes OBJ-008. Which objective set governs? | `DELIVERABLE_REGISTER.csv` (`DEL-106-03` row, SupportsObjectives) | `OBJECTIVE_DELIVERABLE_MAP.csv` (OBJ-008 → DEL-106-03); `_CONTEXT.md` Supports Objectives | Datasheet Identification; Specification R-6 | PROPOSAL: treat OBJ-008 as supported (per `_CONTEXT.md` and the objective map), and reconcile `DELIVERABLE_REGISTER.csv` `SupportsObjectives` text in a separate decomposition update. | TBD |
| CFL-003 | Deliverable-local source slices for technical values (DBM-Deepcut sections, Workbook row 12 detailed content, `26020-Package_Requirements.docx` package-specific rows) have not been copied per `_REFERENCES.md` Missing/Deferred References. Many requirement details cannot be grounded. | `_REFERENCES.md` (Missing / Deferred References) | `OBJECTIVE_REGISTER.csv` (OBJ-005, OBJ-008, OBJ-009, OBJ-010 source citations) | All four documents | PROPOSAL: stage the relevant source slices into `_Sources` deliverable-local pointers and rerun `four-documents` Pass 3 after `_SEMANTIC_LENSING.md` is generated. | TBD |
