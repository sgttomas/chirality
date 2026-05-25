# Specification: Construction Work Package

## Scope

This specification defines the minimum content and source-grounded requirements for the Construction Work Package for DEL-008-03_construction-work-package, the EPC Integrator construction deliverable for PKG-008 Controls system design and integration.

The Construction Work Package covers physical installation planning, construction execution boundaries, tie-in planning, inspection, turnover, and integration of the controls package into facility systems. The Gate 7 accepted basis states that package Construction Work Package deliverables describe physical installation, construction, tie-in, inspection, and turnover into larger systems.

Excluded from this document are final detailed-design values that the admitted source set leaves unresolved, including final Remote I/O cabinet locations, DLR versus PRP selections, controller sizing and quantity, unit controller sizing, historian product selection, application-specific virtual-machine requirements, and package-specific workface sequencing. These remain `TBD` until detailed design or source admission resolves them.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| CWP-001 | The Construction Work Package shall identify DEL-008-03 as the Construction Work Package for PKG-008 Controls system design and integration and shall preserve the EPC Integrator responsibility boundary. | Gate 7 `DELIVERABLE_REGISTER.csv`, DEL-008-03; `PACKAGE_REGISTER.csv`, PKG-008 |
| CWP-002 | The Construction Work Package shall include, at minimum, a construction work package, installation and tie-in workface plan, and construction interface and turnover checklist. | Deliverable `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv`, DEL-008-03 |
| CWP-003 | The Construction Work Package shall plan for the PKG-008 interface types recorded in Gate 7: process piping, utility piping, relief / flare / vent, electrical power, I&C / control cabling, communications / network, building HVAC / services, and fire & gas / safety systems. | Gate 7 `PACKAGE_REGISTER.csv`, PKG-008 |
| CWP-004 | The Construction Work Package shall preserve the central operations control-room operating philosophy and shall not require routine physical interaction in the process facility where DBM controls philosophy intends monitoring and control from the control room. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-13 Operating Philosophy |
| CWP-005 | The Construction Work Package shall coordinate installation boundaries for central control room equipment, MCC-based Level 1 components, and remote I/O cabinets in process areas. Remote I/O locations are `TBD` and must be finalized during detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-13 Physical Layout and Equipment Placement; SEC-13 Interfaces, Assumptions, and Open Design Development |
| CWP-006 | The Construction Work Package shall include network construction and tie-in checks for PCN, I/O Network, Controller Network, IDMZ Network, and Enterprise Network interfaces where the work package touches those systems. IDMZ layout and enterprise requirements require Tourmaline IT/OT coordination. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-13 Network Basis; SEC-13 Interfaces, Assumptions, and Open Design Development |
| CWP-007 | The Construction Work Package shall verify that Modbus data connections are installed for monitoring and data collection only and are not used for process control. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-13 Modbus Data Basis |
| CWP-008 | The Construction Work Package shall include cable tray, conduit, armored cable, instrumentation cable, fiber cable, and communications cable installation checks consistent with the DBM cable, wire, and raceway basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 Cable, Wire, and Raceways |
| CWP-009 | The Construction Work Package shall confirm cable tray routing does not interfere with maintenance access for exchanger bundle removal, cranes or hoists, pumps, valves, or similar requirements. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 Cable Tray and Conduit |
| CWP-010 | The Construction Work Package shall include fire, gas, H2S, methyl mercaptan, audible/visual alarm, ESD pushbutton, and local unit shutdown interfaces where applicable to the controls package installation. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-14 Instrumented Protection Basis |
| CWP-011 | The Construction Work Package shall preserve SEC-14 open confirmations as `TBD` where detector quantity, final coverage, additional outdoor detection, large-module ESD pushbutton locations, or hazard-analysis-driven locations remain unresolved. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-14 Detection Systems; SEC-14 Supported Tables |
| CWP-012 | The Construction Work Package shall record no declared dependency blockers unless the deliverable-local dependency view declares them. | `_DEPENDENCIES.md`; `_Coordination/_COORDINATION.md` |

## Standards

| Standard / Authority | Applicability | Location |
|---|---|---|
| Gate 7 final PROJECT_DECOMP snapshot | Accepted upstream decomposition truth for package identity, deliverable identity, objective mapping, and mandatory EPC anchor deliverables. | `DECOMPOSITION_REF` folder |
| Canadian Electrical Code | Cable/conduit compliance, grounding, branch-circuit and area-classification installation constraints where cited by the DBM. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 Cable Tray and Conduit; SEC-15 code table |
| NEMA VE2 | Cable tray support where drawing package details are not included. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 Cable Tray and Conduit |
| Tourmaline IT/OT requirements | IDMZ, enterprise-network requirements, network hardware selection, industrial networking policies, and switch configuration responsibility. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-13 Network Basis and Interfaces |
| Propak Systems controls libraries | PLC and HMI configuration basis for controls implementation. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-13 Configuration Basis |

## Verification

| Requirement IDs | Verification approach |
|---|---|
| CWP-001, CWP-002 | Confirm document identification, responsible party, required artifacts, and turnover checklist against `_CONTEXT.md` and Gate 7 registers. |
| CWP-003 | Check the construction interface matrix against PKG-008 interface types in `PACKAGE_REGISTER.csv`. |
| CWP-004, CWP-005 | Review installation drawings/workface plan for control room, MCC, and remote I/O scope boundaries; confirm unresolved locations remain tracked as `TBD`. |
| CWP-006, CWP-007 | Review network tie-in checklist, Modbus data list, and IT/OT coordination records; confirm no process control is assigned over Modbus. |
| CWP-008, CWP-009 | Inspect cable tray, conduit, cable type, support, routing, area classification, and maintenance-access checks against SEC-12. |
| CWP-010, CWP-011 | Review fire/gas/alarm/ESD interface checklist and verify unresolved detector/ESD details are carried as detailed-design `TBD` items. |
| CWP-012 | Confirm `_DEPENDENCIES.md` remains the source for declared blockers; current declared blockers are none. |

## Documentation

The Construction Work Package shall include or reference the following records:

- Construction work package.
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.
- Interface matrix covering the Gate 7 PKG-008 interface types.
- Cable tray, conduit, armored cable, instrumentation cable, fiber cable, and communications cable inspection checklist.
- Network, Remote I/O, Modbus, and IT/OT coordination checklist.
- Fire/gas/alarm/ESD/unit-shutdown interface checklist.
- `TBD` register for unresolved detailed-design items and source gaps.
- Turnover evidence showing inspection status, open items, and responsible owner for each unresolved item.
