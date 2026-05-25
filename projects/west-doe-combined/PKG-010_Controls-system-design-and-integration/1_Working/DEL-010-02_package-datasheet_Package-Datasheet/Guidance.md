# Guidance: DEL-010-02_package-datasheet — Package Datasheet

## Purpose

This deliverable exists to provide the EPC Integrator's technical handoff datasheet for `PKG-010`, Controls system design and integration. It carries package data, interface facts, and design criteria needed by third-party vendor or discipline package engineering and design.

Gate 7 intentionally keeps controls power-panel interface facts under this package datasheet instead of creating a separate package or deliverable.

## Principles

1. Use the accepted Gate 7 snapshot for identity, scope, artifact, objective, and interface truth.
2. Use accessible source material for requirements and values. In this run, the directly used sources are workbook row 11 from `26020-Packages_Interfaces_4_export.xlsx`, Gate 7 registers, and DBM SEC-09/SEC-12/SEC-13/SEC-14.
3. Do not infer vendor-specific data maps, trip lists, alarm priorities, network addressing, VLANs, detector counts, set points, voting logic, or model selections where the source states they remain detailed-design items.
4. Keep interface categories visible. The controls package has active source-marked interfaces with process piping, utility piping, relief/flare/vent, electrical power, I&C/control cabling, communications/network, building HVAC/services, and fire/gas/safety systems.
5. Treat Modbus as monitoring/data collection only unless later accepted authority changes the basis. Process control over Modbus is not supported by the current DBM source.

## Considerations

| Topic | Guidance | Source |
|---|---|---|
| Datasheet maturity | The Phase 2.2 draft should be usable as a source-grounded skeleton. Final issue requires vendor and detailed-design data. | Gate 7 `ARTIFACT_REGISTER.csv`; DBM SEC-13 and SEC-14 |
| BPCS/RIO integration | The datasheet should separate BPCS process control, Remote I/O wiring, and standalone Unit Control System integration. | DBM SEC-13 "Control System Basis", "BPCS and Remote I/O", "Unit Control Systems and Package Interfaces" |
| Network information | Network topology can state PCN, I/O Network, IDMZ, Enterprise Network, PRP, and dual uplinks where sourced. IP addresses, VLANs, firewall rules, and policies remain `TBD`. | DBM SEC-13 "Topology and Networks" |
| Safety interfaces | Include ESD, fire detection, LEL, H2S, methyl mercaptan, fire/gas, and unit shutdown interface topics, but leave final placement, set points, voting, and cause/effect fields `TBD`. | DBM SEC-14 |
| Electrical and building interfaces | Include electrical power, MCC, UPS, cable-separation, electrical-building HVAC/ventilation, heat tracing, and building service coordination when applicable. | DBM SEC-12; DBM SEC-09 |
| Objective association | Objectives `OBJ-002`, `OBJ-003`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-009`, and `OBJ-010` are explicitly listed for this deliverable in Gate 7 and can be treated as accepted context, not newly derived requirements. | `_CONTEXT.md`; Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv` |

## Trade-offs

| Trade-off | Preferred handling |
|---|---|
| Completeness vs. source fidelity | Prefer `TBD` over invented values. A partial datasheet with traceable gaps is better than a complete-looking datasheet with unsupported data. |
| Package-level vs. separate deliverable handling | Keep controls power-panel interface facts in this datasheet because Gate 7 explicitly disposed the issue that way. |
| Communication convenience vs. control criticality | Record Modbus/Kepware monitoring where supported, but require hardwired signals or defined protocols according to criticality where the source requires that distinction. |
| Current basis vs. future detailed design | Use current DBM values and mark final detailed-design/vendor integration items as open. Do not pre-close detailed-design decisions. |

## Examples

| Datasheet field | Example entry pattern |
|---|---|
| Interface category | `Electrical Power — active interface; source: workbook row 11; Gate 7 interface ID IFC-7692ABF6DF; detailed load/interface value: TBD.` |
| Package communication | `Modbus via Kepware KepserverEX for monitoring/data collection only; process control not over Modbus; final data map: TBD.` |
| Safety device wiring | `Safety devices associated with BPCS wired to nearest Remote I/O control panel where practical; final detector tag list/set points/voting: TBD.` |

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-010-02-001 | Workbook row note asks whether controls power-panel interfaces should be tracked separately, while Gate 7 disposition says they remain under this datasheet. This is resolved for Phase 2.2 by Gate 7, but final packaging should retain the ruling visibly. | `26020-Packages_Interfaces_4_export.xlsx`, sheet1 row 11, column X | Gate 7 `INTERFACE_REGISTER.csv` rows 32-39 and `ARTIFACT_REGISTER.csv` rows 149-157 | `Datasheet.md` Attributes/Conditions; `Specification.md` Requirements; `Procedure.md` Steps | Gate 7 final published snapshot governs; keep as datasheet interface facts, not separate package/deliverable. | TBD |
