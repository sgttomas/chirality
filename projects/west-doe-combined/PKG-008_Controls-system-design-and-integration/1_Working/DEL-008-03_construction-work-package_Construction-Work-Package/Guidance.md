# Guidance: Construction Work Package

## Purpose

The Construction Work Package exists to turn the accepted PKG-008 controls system design and integration basis into a bounded field-execution and turnover package. It should help the EPC Integrator plan installation, tie-ins, inspection, and handoff for controls-related physical interfaces without inventing unresolved detailed-design values.

## Principles

1. Preserve the Gate 7 boundary. DEL-008-03 is the Construction Work Package for PKG-008 and should stay aligned to the accepted Gate 7 registers rather than broadening into sibling deliverables.
2. Treat the Construction Work Package as an integration document. The strongest source-supported content is the interface set: electrical power, I&C/control cabling, communications/network, building HVAC/services, fire/gas/safety systems, and controls impacts on process/utility/relief interfaces.
3. Use DBM sections as the technical authority for controls, protection, and cabling. The decomposition tells what the deliverable is; DBM SEC-12, SEC-13, and SEC-14 govern the source-supported technical constraints.
4. Keep detailed-design decisions open where the sources leave them open. Remote I/O cabinet locations, DLR versus PRP selection, controller sizing, unit controller sizing, historian product selection, detector coverage, and ESD pushbutton locations should remain `TBD` until resolved.
5. Separate monitoring integration from process control. Modbus is source-supported for monitoring and data collection only; do not let field execution or tie-in planning imply Modbus-based process control.

## Considerations

The work package should be arranged around field-verifiable checks: equipment placement boundaries, cable/raceway installation, network tie-ins, remote I/O interfaces, fire/gas detector and alarm interfaces, ESD pushbuttons, package control handoffs, and turnover evidence.

Client IT/OT coordination is a construction readiness issue, not only a design issue. Network hardware selection, IDMZ layout, enterprise-network requirements, switch configuration, policies, addressing, and segmentation should be visible as prerequisites or hold points where they affect installation or turnover.

Fire/gas and shutdown interfaces should be tracked with explicit open confirmations. The admitted DBM source sets several final quantities, coverage decisions, and placement decisions as detailed-engineering outcomes; the Construction Work Package should carry them as unresolved until the governing safety studies and detailed design artifacts are available.

## Trade-offs

| Topic | Trade-off |
|---|---|
| Early workface planning vs. source fidelity | The work package can define structure and checklists now, but exact installation sequence, Remote I/O locations, and detector placement must remain `TBD` where detailed design is unavailable. |
| Network completeness vs. client governance | The CWP can identify PCN/I/O/Controller/IDMZ/Enterprise interfaces, but client IT/OT input controls final IDMZ layout, policies, hardware requirements, and switch configuration. |
| Integration detail vs. deliverable boundary | The CWP should reference controls, electrical, fire/gas, and package control interfaces without absorbing the sibling controls discipline production package or package datasheet scope. |

## Examples

| Example check | Source-grounded basis |
|---|---|
| Include a Modbus tie-in checklist that states "monitoring/data collection only." | DBM-Deepcut SEC-13 Modbus Data Basis. |
| Include a cable tray inspection step for maintenance-access interference. | DBM-Deepcut SEC-12 Cable Tray and Conduit. |
| Include a turnover line item for unresolved Remote I/O cabinet locations. | DBM-Deepcut SEC-13 Interfaces, Assumptions, and Open Design Development. |
| Include a fire/gas/ESD interface checklist with detector quantities and final locations marked `TBD` where unresolved. | DBM-Deepcut SEC-14 Detection Systems and Supported Tables. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HRR-001 | PKG-008 package register says controls power-panel interfaces may need separate tracking, but the current deliverable context has no separate declared dependency or source slice resolving that tracking. | Gate 7 `PACKAGE_REGISTER.csv`, PKG-008 InterfaceReviewNotes | Deliverable `_DEPENDENCIES.md`, no declared dependencies; `_REFERENCES.md`, no copied deliverable-specific source slices | Datasheet Conditions; Specification Requirements CWP-003; Procedure Steps | Treat as an open interface-review item in the CWP and do not create a separate dependency or deliverable without human/source confirmation. | TBD |
