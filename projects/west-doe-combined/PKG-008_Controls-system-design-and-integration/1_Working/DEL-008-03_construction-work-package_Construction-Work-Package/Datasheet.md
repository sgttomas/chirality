# Datasheet: Construction Work Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-008-03_construction-work-package |
| Deliverable name | Construction Work Package |
| Parent package | PKG-008 - Controls system design and integration |
| Discipline | Controls |
| Type | EPC Construction Work Package |
| Responsible party | EPC Integrator |
| Scope item | SOW-0008 |
| Source basis | Gate 7 PROJECT_DECOMP snapshot; Workbook Packages row 9; DBM-Deepcut SEC-12, SEC-13, SEC-14 |

## Attributes

| Attribute | Value / Basis | Source |
|---|---|---|
| Package function | Controls system design and integration under WBS 01 with recorded physical interfaces. | Gate 7 `PACKAGE_REGISTER.csv`, PKG-008 |
| Construction work package purpose | Describe physical installation, construction, tie-in, inspection, and turnover into larger systems. | Gate 7 `PROJECT_DECOMP.md` section 7 |
| Required package artifacts | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist. | Deliverable `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv`, DEL-008-03 |
| Interface types to plan | Process piping; utility piping; relief / flare / vent; electrical power; I&C / control cabling; communications / network; building HVAC / services; fire & gas / safety systems. | Gate 7 `PACKAGE_REGISTER.csv`, PKG-008 |
| Controls topology basis | Field devices, control processors, supervisory/operator systems, site operations, IDMZ, and optional enterprise levels. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-13 Controls Topology |
| Physical controls layout | Control room for operator/engineering workstations, primary servers, and core switches; MCC for Level 1 controls and secondary servers; remote I/O cabinets in process areas. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-13 Physical Layout and Equipment Placement |
| Network basis | PCN, I/O Network, Controller Network, IDMZ Network, and Enterprise Network. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-13 Network Basis |
| Controls hardware | Allen-Bradley ControlLogix 1756-L8x process and unit controllers; Flex5000 or ControlLogix remote I/O. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-13 Controls System Hardware |
| Modbus basis | Modbus data integrated through KepserverEX; Modbus used for monitoring and data collection only, not process control. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-13 Modbus Data Basis |
| Cable/raceway basis | Field-run communications cables are armored and cable-tray rated; instrumentation cable basis is ACIC; conduit and cable tray must respect area classification and maintenance access. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 Cable, Wire, and Raceways |
| Fire and gas basis | Fire, gas, H2S, methyl mercaptan, alarms, ESD pushbuttons, and unit shutdown interfaces are included in the protection basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-14 Instrumented Protection Basis |

## Conditions

| Condition | Value / Basis | Source |
|---|---|---|
| Current deliverable maturity before this run | OPEN. | `_STATUS.md` before TASK+four-documents |
| Declared upstream dependencies | None declared. | `_DEPENDENCIES.md` |
| Declared downstream dependencies | None declared. | `_DEPENDENCIES.md` |
| Blocker threshold | INITIALIZED; blockers advisory and only from declared dependency edges. | `_DEPENDENCIES.md`; `_Coordination/_COORDINATION.md` |
| Detailed-design items | Remote I/O cabinet locations, DLR versus PRP selection, controller sizing, unit controller sizing, workstation technology, historian product, and application-specific VM requirements remain to be resolved during detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-13 Interfaces, Assumptions, and Open Design Development |
| Construction-source specificity | No deliverable-specific construction source slice was copied during PREPARATION; package-specific installation sequencing and workface boundaries are `TBD`. | `_REFERENCES.md` |

## Construction

| Construction subject | Draft basis |
|---|---|
| Work package boundary | Covers the construction planning and turnover package for the controls system design and integration package, including controls cabinets, remote I/O, network/cabling interfaces, fire/gas and ESD interfaces, electrical power/building service interfaces, and related tie-ins where source-supported. |
| Installation planning | Must include workface planning for controls equipment placement, cable tray/conduit routing, communications cabling, remote I/O cabinets, alarm devices, detector interfaces, ESD pushbuttons, and package control handoffs. Exact sequencing is `TBD`. |
| Tie-in planning | Must address the package interface types listed in Gate 7: process/utility/relief interfaces where controls tie-ins are affected, electrical power, I&C/control cabling, communications/network, building HVAC/services, and fire/gas/safety systems. |
| Inspection and verification | Must verify installation against DBM SEC-12 cable/raceway constraints, SEC-13 controls topology/network/hardware basis, and SEC-14 detection/alarm/shutdown interface basis. |
| Turnover | Must produce a construction interface and turnover checklist, including unresolved `TBD` items and client IT/OT/network configuration dependencies. |

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PROJECT_DECOMP.md`, section 7 Gate 5 Accepted Basis.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`, DEL-008-03.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`, PKG-008.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_DELIVERABLE_MAP.csv`, DEL-008-03 rows.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 Cable, Wire, and Raceways; SEC-13 Controls System Basis; SEC-14 Instrumented Protection Basis.
