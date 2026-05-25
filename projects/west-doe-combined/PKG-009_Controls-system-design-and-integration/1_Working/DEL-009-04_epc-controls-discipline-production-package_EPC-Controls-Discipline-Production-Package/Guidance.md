# Guidance: DEL-009-04 EPC / Controls Discipline Production Package

## Purpose

This guidance explains how to use the EPC / Controls Discipline Production Package for `PKG-009 - Controls system design and integration`. The package exists to convert the accepted Gate 7 controls package basis and accessible controls source slices into a bounded production package for WBS 02.

The deliverable should remain source-limited. Where the accepted package and accessible DBM/workbook sources do not define a value, the production package should preserve `TBD` rather than invent design criteria.

## Principles

1. Preserve the accepted package identity.
   Use DEL-009-04, PKG-009, WBS 02, SOW-0009, and CoA tracking number 26020-01-32-001 exactly as carried by `_CONTEXT.md`, Gate 7 registers, and the Packages workbook.

2. Treat the workbook row as the package interface trigger.
   The workbook row flags interface categories that the controls production package must consider: process piping, utility piping, relief/flare/vent, electrical power, I&C/control cabling, communications/network, building HVAC/services, and fire/gas/safety systems.

3. Keep controls architecture and package control boundaries distinct.
   The BPCS is the primary facility process-control system, while compression unit controls are standalone Unit Control Systems integrated into the BPCS for monitoring and alarming. Vendor integration details remain detailed-design or vendor-integration work unless supported by accepted source updates.

4. Do not use monitoring protocols for control functions.
   The cited DBM basis states that Modbus data is for monitoring and data collection only and not for process control.

5. Carry unresolved design-development items visibly.
   RIO locations, controller sizing, network selection where not fixed, historian product, IDMZ implementation, firewall rules, IP addressing, and VLAN segmentation should stay as tracked open items until resolved by accepted authority.

Sources: `_CONTEXT.md`; `_Sources/26020-Packages_Interfaces_4_export.xlsx`, sheet `Packages`, row with `ID #` 9; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, `SEC-13 - Control System Basis`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `Controls Topology`.

## Considerations

- The deliverable should align BPCS, Remote I/O, safety-device wiring, fire/gas interfaces, ESD pushbuttons, and package interfaces so that requirements and verification hooks remain traceable.
- The interface review note about controls power-panel interfaces is an explicit human-ruling item. It should be resolved before the package is treated as closed for interface tracking.
- The 03-25 source is more directly applicable to WBS 02 for PRP-connected Flex5000 RIO. The 04-25 source is useful for shared controls architecture but allows DLR or PRP in some places; do not flatten those two bases into a single universal rule.
- Client IT/OT input is required for IDMZ, enterprise-network details, network hardware selection, and industrial networking policy compliance. These details should not be closed from the DBM alone.
- Project electrical specifications are referenced by the DBM for tray, conduit, grounding, and bonding, but the controlled specification text was not available to this run.

## Trade-offs

| Topic | Trade-off | Guidance |
|---|---|---|
| Source completeness vs. production readiness | The deliverable can initialize a production package, but several detailed-design and source-location items remain unresolved. | Initialize with traceable TBDs and a closure record instead of filling gaps from convention. |
| 03-25-specific basis vs. shared 04-25 architecture | Shared architecture helps frame the controls system, but WBS 02 needs the directly applicable 03-25 basis where it exists. | Prefer 03-25 source slices for WBS 02-specific requirements; cite 04-25 only for shared topology/protection/interface context. |
| Protocol integration vs. process control | Protocols such as Modbus support monitoring/data collection, but the source prohibits process control over Modbus. | Require hardwired or appropriate criticality-based interfaces for control/trip functions. |
| Early package closure vs. interface accuracy | Closing interface tracking before resolving controls power-panel treatment risks missing scope boundaries. | Keep the workbook note open as HRR-001. |

## Examples

- Example source-grounded requirement: "Modbus data shall be used for monitoring and data collection only; process control shall not be performed over Modbus." Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, `Unit Control Systems and Package Interfaces`.
- Example source-grounded TBD: "Process controller sizing and quantity are TBD during detailed design." Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `Interfaces, Assumptions, and Open Design Development`.
- Example interface carry-forward: "Confirm whether controls power-panel interfaces should be tracked separately." Source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, sheet `Packages`, row with `ID #` 9.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HRR-001 | Workbook note asks whether controls power-panel interfaces should be tracked separately. | `_Sources/26020-Packages_Interfaces_4_export.xlsx`, sheet `Packages`, row with `ID #` 9 | No separate deliverable-local dependency/register entry exists yet. | Datasheet Attributes; Specification Requirements and Documentation; Procedure Steps | Treat as an open interface-tracking decision for Gate 5/dependency extraction. | TBD |
| HRR-002 | 03-25 source states RIO connects via PRP; 04-25 source allows PRP or DLR and says DLR versus PRP is detailed-design dependent. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, `BPCS and Remote I/O` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `Controls System Hardware`; `Interfaces, Assumptions, and Open Design Development` | Datasheet Construction; Specification Requirements and Verification | Use the 03-25 source for WBS 02 where directly applicable; keep cross-facility DLR/PRP selection open where the applicable network is not fixed. | TBD |
