# Guidance: DEL-009-02_package-datasheet — Package Datasheet

## Purpose

The package datasheet exists to turn the accepted PKG-009 controls scope into a usable EPC handoff artifact. It should preserve package identity, controls architecture basis, and interface facts so controls, instrumentation, electrical, safety, vendor-package, and construction stakeholders can integrate against the same source-supported basis.

Sources: Gate 7 DELIVERABLE_REGISTER.csv row DEL-009-02_package-datasheet; Gate 7 PACKAGE_REGISTER.csv row PKG-009; DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, SEC-13 and SEC-14.

## Principles

- Keep package identity and workbook traceability explicit. The package is PKG-009, WBS 02, CoA tracking number 26020-01-32-001, sourced to workbook Packages row 10.
- Treat Gate 7 interface rows as required interface facts for this datasheet. The Gate 6 disposition says controls power-panel interfaces remain package datasheet/interface facts rather than becoming a separate package or deliverable.
- Separate source-supported controls architecture from unresolved detailed design. BPCS platform, Remote I/O family, network segmentation, and Modbus limitations are source-supported; final maps, logic, priorities, and detector settings remain `TBD`.
- Do not use Modbus as a process-control basis. The DBM supports Modbus for monitoring and data collection only.
- Preserve cross-facility utility assumptions. Instrument air is supplied from 04-25 and no local 03-25 instrument-air compressor controls are added.

## Considerations

| Topic | Guidance | Source |
|---|---|---|
| Vendor/package interface data | Capture both hardwired signal requirements and communication protocol expectations; classify by criticality where the project/vendor basis supports it. | DBM SEC-13 |
| Network architecture | Distinguish PCN, I/O Network, IDMZ, and Enterprise Network content; leave detailed IDMZ policies, firewall rules, IP addressing, and VLAN segmentation as detailed-design/client IT/OT coordination items. | DBM SEC-13 |
| Remote I/O placement | Use the DBM principle that process and safety devices associated with BPCS are wired to the nearest Remote I/O control panel where practical. | DBM SEC-13/SEC-14 |
| Fire and gas detection | Detector quantity, tag list, set points, voting logic, placement, and calibration remain `TBD`; do not invent them from package type alone. | DBM SEC-14 |
| Electrical interface | Power/control separation and electrical interface requirements should align with project electrical specifications; exact specification identifiers are `TBD` in the accessible source slice. | DBM SEC-12/SEC-15 |
| Design ambient | The -40 deg C to +35 deg C facility envelope should be reflected where controls panels, field devices, buildings, or exposed instruments are included in the datasheet. | DBM site/design ambient basis |

## Trade-offs

- A concise datasheet is easier to use, but this deliverable must carry interface facts because the accepted decomposition intentionally does not split those facts into standalone deliverables.
- Early vendor handoff benefits from identifying known BPCS/RIO/protocol architecture, but unsupported detailed values should remain `TBD` to avoid false precision.
- Package-level boundaries should be clear enough for procurement and vendor coordination while leaving final detailed design responsibilities with the appropriate EPC, vendor, safety, and client IT/OT workflows.

## Examples

- Source-supported entry: "BPCS controller platform: Allen-Bradley ControlLogix 1756-L8x series; controller quantity and sizing TBD by detailed design."
- Source-supported entry: "Modbus: monitoring and data collection only; process control not carried over Modbus."
- Unsupported entry to avoid: exact detector counts, set points, voting logic, IP addresses, VLAN identifiers, trip priorities, or final package data maps without detailed design/vendor source.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HRR-009-02-001 | Final standards/specification identifiers for controls, instrumentation, and electrical interfaces are not available in the accessible source slice. | DBM SEC-15 says applicable project specifications and standards apply, exact latest index to be verified. | Deliverable source folder has no copied specification index for this datasheet. | Specification > Standards; Datasheet > References; Procedure > Verification | Use DBM discipline basis for Phase 2.2 and keep exact document numbers as `TBD` until the project specification index is available. | TBD |
