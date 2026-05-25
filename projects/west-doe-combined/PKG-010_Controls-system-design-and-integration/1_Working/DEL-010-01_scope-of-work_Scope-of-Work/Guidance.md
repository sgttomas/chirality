# Guidance: DEL-010-01_scope-of-work - Scope of Work

## Purpose

This Scope of Work exists to define the EPC Integrator work boundary for the `PKG-010` WBS 03 Controls system design and integration package. It should give downstream package datasheet, construction package, discipline-production, interface, and review workflows a stable package identity, function statement, integration boundary, and responsibility basis.

Sources: `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, and `ARTIFACT_REGISTER.csv`.

## Principles

- Keep the SOW package-scoped. It should define the controls system design and integration boundary for `PKG-010`; it should not become a complete detailed control-system design package.
- Preserve the accepted source basis. Workbook row 11 and Gate 7 registers are authoritative for package identity, discipline, WBS, CoA tracking number, and applicable interface types.
- Treat DBM controls text as the functional integration basis. DBM SEC-13 supports centralized monitoring and control, BPCS role, standalone compression Unit Control Systems, segregated I/O network, redundant Ethernet, PRP, and vendor package interface resolution.
- Keep deferred vendor/detailed-design items visible. Package data maps, permissive logic, trip interfaces, alarm priorities, shutdown levels, cause-and-effect actions, and reset responsibilities should be listed as deferred/TBD instead of invented.
- Do not over-split controls power-panel scope. The Gate 6 disposition carried in the interface register says controls power-panel interfaces remain interface facts/artifacts under the package datasheet and do not create a separate package or deliverable.

## Considerations

The SOW should be useful as an integration anchor for controls, instrumentation, communications, electrical power, HVAC/building services, process/utility/relief interfaces, and fire and gas/safety systems. The interface list is broader than control cabling alone, so the narrative should explain why those interfaces matter to controls integration without assigning unsupported design values.

The package responsibility model is source-dependent. The Gate 7 package register does not establish a separate vendor-package ownership model for `PKG-010`; it states EPC Integrator or discipline subcontractor responsibility is source-dependent. The SOW should therefore avoid assigning vendor ownership unless a later source or human ruling supplies it.

Objective associations are useful context for why this SOW matters to the facility outcome. Under `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`, OBJ-002, OBJ-003, OBJ-005, OBJ-006, OBJ-007, OBJ-009, and OBJ-010 are directional context, not hard requirements by themselves.

## Trade-offs

| Topic | Trade-off | Recommended handling |
|---|---|---|
| Scope completeness vs. source fidelity | The SOW needs enough controls integration detail to be actionable, but the current source set does not provide all final control logic and shutdown values. | Include source-supported DBM controls basis and mark final logic/data-map/trip details `TBD` or deferred. |
| Interface breadth vs. package focus | Workbook row 11 records multiple physical and facility interfaces, some outside strict controls cabling. | Preserve the full source-supported interface list and explain their controls-integration relevance. |
| EPC vs. subcontractor responsibility | Gate 7 says responsibility is source-dependent. | Use EPC Integrator as deliverable responsible party while leaving execution assignment to EPC/subcontractor as `TBD` where needed. |
| Controls power-panel tracking | The interface note asks whether controls power-panel interfaces should be tracked separately, but Gate 6 already disposed them as facts/artifacts under package datasheet. | Do not create a separate package/deliverable; keep as an interface fact and mark any residual assignment detail `TBD`. |

## Examples

- Source-supported interface statement: "`PKG-010` includes Process Piping, Utility Piping, Relief / Flare / Vent, Electrical Power, I&C / Control Cabling, Communications / Network, Building HVAC / Services, and Fire & Gas / Safety Systems interfaces." Source: workbook row 11 and Gate 7 `INTERFACE_REGISTER.csv` rows for `PKG-010`.
- Source-supported controls function statement: "The control system provides centralized monitoring and control for the 03-25 Compressor Station and Liquids Hub, with compression unit controls handled by standalone Unit Control Systems and integrated for monitoring and alarming." Source: DBM SEC-13.
- Deferred-value statement: "Final package data maps, permissive logic, trip interfaces, alarm priorities, trip lists, shutdown levels, cause-and-effect actions, and reset responsibilities are detailed-design/vendor-integration deliverables." Source: DBM SEC-13 and SEC-14.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HRR-010-01 | Package execution responsibility is not fully resolved: deliverable responsible party is EPC Integrator, while package register says EPC Integrator or discipline subcontractor responsibility is source-dependent. | `_CONTEXT.md` Identity; Gate 7 `DELIVERABLE_REGISTER.csv` row `DEL-010-01_scope-of-work` | Gate 7 `PACKAGE_REGISTER.csv` row `PKG-010` | Specification Scope, Requirements, Procedure Prerequisites/Steps | Treat EPC Integrator as accountable deliverable owner; keep execution assignment between EPC Integrator and discipline subcontractor as `TBD` pending human ruling or later source. | TBD |
| HRR-010-02 | Controls power-panel interface ownership/detail remains open even though no separate package/deliverable is created. | Gate 7 `INTERFACE_REGISTER.csv` rows for `PKG-010` notes | Gate 6 disposition embedded in same register notes | Datasheet Construction, Specification Scope/Requirements, Procedure Verification | Retain controls power-panel interfaces as facts/artifacts under package datasheet; request human ruling only for responsibility/detail tracking. | TBD |
