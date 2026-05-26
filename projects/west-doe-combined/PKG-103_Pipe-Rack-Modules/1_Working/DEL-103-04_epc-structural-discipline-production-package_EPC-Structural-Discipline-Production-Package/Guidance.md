# Guidance: EPC / Structural Discipline Production Package — PKG-103 Pipe Rack Modules

## Purpose

This guidance supports production of the Structural discipline package for PKG-103 Pipe Rack Modules. The package exists to turn accepted Gate 7 package/interface truth and the available DBM structural/civil source slices into a controlled discipline production basis without inventing missing detailed engineering criteria.

## Principles

- Treat the Gate 7 PROJECT_DECOMP snapshot as accepted upstream truth for package identity, deliverable identity, objectives, artifacts, and interface facts.
- Treat the structural/civil DBM source slices (DBM-Deepcut SEC "Civil Scope" through "External Dependencies"; DBM-Comp_and_Liquids "Foundations and Structural Supports", "Site and Civil Conditions", "Area Classification") as the governing source for design basis, codes, materials, and foundation default.
- Respect the Gate 6 disposition that "pipe racks and pipe rack modules are designed exclusively by the EPC Integrator." Do not introduce a vendor-package design model for the rack steel.
- Keep unsupported detailed design values (rack geometry, member sizes, pile design parameters, anchor loads, shop/field split) as `TBD` rather than inferring them from package name alone.
- Preserve the distinction between accepted interface facts and final design deliverables: the workbook establishes that the nine interfaces apply to PKG-103; detailed design of each interface remains dependent on other disciplines and on later inputs (plot plan, P&IDs, 3D model, pipe stress, electrical schedules, EHT/I&C schedules).
- Use declared dependencies only when assessing blockers; this deliverable currently has no declared upstream or downstream dependencies in `_DEPENDENCIES.md`.

## Considerations

- The source set supports a structural production basis (codes, materials, foundation default, site/environmental basis, interface list) but does not support a final detailed rack design package. Gate 7 explicitly records that detailed discipline requirements are source-limited and remain open.
- Geotechnical inputs are not closed: bearing capacity, LPILE curves, dynamic design criteria, and pavement design are all `TBD` pending the geotechnical report.
- The topographical survey and grade surface file remain external inputs; final pad/pile-cap elevations and the high-ridge along the pipe rack depend on those inputs.
- The DBM module/erection table does not enumerate pipe rack modules individually; shop-vs-field split for the rack modules is not directly source-supported.
- Pipe rack loading inputs (commodity list, pipe sizes, anchor/guide loads) come from the piping discipline and from the plot plan/3D model; the structural package should not freeze rack loading without those inputs.
- The DBM treats outdoor pipe racks as general-purpose non-hazardous unless detailed classification drawings identify otherwise. The structural production basis should carry this baseline but not over-extend it.
- The nine accepted interfaces are interface facts (applicability), not design loads or routing. Each interface still requires a detailed counterpart-discipline deliverable to close.

## Trade-offs

| Topic | Trade-off | Current treatment |
|---|---|---|
| Early production basis vs. final design closure | The package can define codes, materials, foundation default, site basis, and the interface matrix, but cannot close member sizing, connection design, or final pile parameters without geotechnical, plot-plan, and piping inputs. | Use a source-limited requirements closure record. |
| Shop-fabricated rack modules vs. field-erected racks | The DBM lists shop/field split for process and utility modules but not for pipe rack modules; rack modularization choice affects logistics, foundation tolerances, and connection design. | Carry shop/field split as `TBD`; do not infer from analogous process modules. |
| Default driven steel piles vs. alternative foundations | The default is driven steel piles, but the geotechnical report could direct otherwise; locking in pile sizes too early risks rework. | State driven steel piles as the default basis and list the geotechnical report as the required input before sizing. |
| EPC Integrator exclusive design vs. discipline subcontractor execution | Gate 6 places rack design under the EPC Integrator, while `_CONTEXT.md` and Responsibility row leave subcontractor assignment open. | Treat EPC Integrator as the design-authority owner; carry subcontractor assignment as `TBD` for execution. |

## Examples

- Supported statement: "Structural / Foundations / Supports applies to PKG-103." Source: `INTERFACE_REGISTER.csv`, IFC-BC9813EE49.
- Supported statement: "Structural steel for pipe rack W-flange and HSS members is CSA G40.20/G40.21 350W." Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Governing Civil and Structural Basis."
- Supported statement: "Default foundation for pipe racks is driven steel piles unless detailed engineering confirms otherwise." Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Piles and Foundations."
- Unsupported statement unless later evidence is added: "Pipe rack bay spacing is [specific value]." Current treatment: `TBD`.
- Unsupported statement unless later evidence is added: "Pile design length is [specific value]." Current treatment: `TBD pending geotechnical report`.
- Unsupported statement unless later evidence is added: "Pipe rack modules are shop-erected." Current treatment: `TBD` (not enumerated in DBM erection table).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HRR-103-04-001 | Responsible party is not fully assigned. | `_CONTEXT.md`, Identity: "TBD; EPC Integrator or discipline subcontractor as assigned" | `PACKAGE_REGISTER.csv`, PKG-103 ResponsibilityModel: "EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred." | Datasheet Identification; Specification Scope; Procedure Prerequisites | Treat EPC Integrator as the design-authority owner per Gate 6 disposition; carry discipline-subcontractor execution assignment as `TBD`. | TBD |
| HRR-103-04-002 | Detailed discipline deliverable register is not available. | `_CONTEXT.md`, Anticipated Artifacts: "TBD discipline deliverable register" | `DELIVERABLE_REGISTER.csv` Notes, DEL-103-04: "Detailed non-vendor package deliverable requirements are source-limited and remain open for Gate 5 disposition." | Specification Documentation; Procedure Records | Carry a `TBD` discipline deliverable register together with a source-limited requirements closure record until Gate 5 closes it. | TBD |
| HRR-103-04-003 | Final structural design inputs are incomplete. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, External Dependencies (geotechnical report, topographical survey, plot plan TBD) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "Foundations and Structural Supports" (final geotechnical report required before foundation closure) | Datasheet Conditions; Specification Requirements; Procedure Verification | Keep geotechnical, topographical, plot-plan, piping-load, and shop/field split values open until external source inputs are accepted. | TBD |
| HRR-103-04-004 | Pipe rack module shop/field erection split is not enumerated in the DBM module/erection table. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Buildings and Miscellaneous Facilities (module list does not include rack modules) | Decomposition Notes: PKG-103 conservatively carried from workbook and DBM support. | Datasheet Construction (module erection basis); Specification REQ-103-04-013 | Carry shop/field split as `TBD` for rack modules; do not infer from analogous process modules. | TBD |
| HRR-103-04-005 | Rack-supported commodities are not closed at this gate. | `INTERFACE_REGISTER.csv` Note column for PKG-103: "Rack-supported commodities should be confirmed against plot plan/model." | Decomposition: detailed non-vendor requirements are source-limited. | Specification REQ-103-04-012; Procedure Steps; Datasheet Conditions | Keep commodity list, rack loading, and routing dependent on plot-plan, P&IDs, and 3D model deliverables. | TBD |
