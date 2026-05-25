# Guidance: DEL-010-03 Construction Work Package

## Purpose

The Construction Work Package turns the `PKG-010 - Controls system design and integration` basis into construction-facing installation, tie-in, inspection, and turnover work. It should preserve the accepted Gate 7 package identity while making field execution risks visible before issue for construction.

## Principles

- Use the Gate 7 registers for package identity, deliverable identity, required artifacts, and objective associations.
- Use accessible DBM sections and workbook interface rows for construction and controls-system constraints.
- Treat decomposition rows as routing and scope authority, not as a source of detailed construction values.
- Keep unsupported field details as `TBD` rather than filling gaps from convention.
- Keep controls boundaries explicit: BPCS, Unit Control Systems, RIO, network layers, Modbus monitoring, fire/gas, and shutdown interfaces should not blur during construction planning.
- Treat dependency blockers as advisory and only from declared dependency edges; none are declared for this deliverable at initialization.

## Considerations

The CWP should be especially careful with cross-discipline interfaces because the accepted `PKG-010` interface register marks eight applicable interface types. These interface facts are evidence carried under the package datasheet, but they directly affect construction workface planning and turnover checks for this CWP.

The 03-25 DBM requires mechanical package boundaries to coordinate package buildings, MCC interfaces, RIO interfaces, heat tracing, HVAC, fire/gas detection, and drain/vent tie-ins with civil, electrical, controls, and instrumentation sections. Source: 3-25_Comp_and_Liquids_DBM.md, SEC-09.

The 03-25 controls basis states that compression unit controls are standalone Unit Control Systems, with values and general alarms replicated to the BPCS. Final package data maps, permissive logic, trip interfaces, and alarm priorities are detailed-design/vendor integration items. Source: 3-25_Comp_and_Liquids_DBM.md, SEC-13.

The construction work package should not close alarm philosophy, shutdown, horn tone, beacon, reset, bypass, permissive, or trip-list details unless the final cause-and-effect and shutdown philosophy documents are available. Source: 3-25_Comp_and_Liquids_DBM.md, SEC-14.

## Trade-offs

| Topic | Trade-off |
|---|---|
| Completeness vs source fidelity | It is better to issue a CWP skeleton with `TBD` placeholders than to invent field sequencing, inspection forms, or turnover requirements that are not in the accessible source set. |
| Interface breadth vs construction focus | The full interface list should remain visible, but only interfaces with actual construction scope should be converted into workface steps. Others should remain TBD or "not applicable by field scope" with evidence. |
| Controls integration vs safety boundaries | Construction planning should enable integrated commissioning, but it must preserve BPCS, Unit Control System, Modbus, fire/gas, and shutdown boundaries from the DBM. |

## Examples

TBD. No source-provided example CWP, workface plan, inspection checklist, or turnover dossier was available in the accessible source set.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-010-03-001 | Controls power-panel interfaces are flagged for confirmation; Gate 6 disposition says they remain interface facts/artifacts under the package datasheet with no separate deliverable. Construction workface treatment is still not explicitly defined. | INTERFACE_REGISTER.csv, PKG-010 notes | PACKAGE_REGISTER.csv, PKG-010 InterfaceReviewNotes | Datasheet Construction; Specification R003; Procedure Steps | Treat as an interface-checklist item in this CWP, but do not create a separate package or deliverable. | TBD |
