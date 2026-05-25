# Specification: DEL-009-04 EPC / Controls Discipline Production Package

## Scope

This specification covers the EPC / Controls Discipline Production Package for `PKG-009 - Controls system design and integration`, WBS 02. It is a source-limited production unit for the non-vendor package scope, carried from the accepted Gate 7 decomposition and locally accessible controls source material.

The package shall produce a controls discipline production basis, a discipline deliverable register, and a source-limited requirements closure record for `SOW-0009`.

Exclusions and limits:

- This document does not reinterpret the raw project source corpus.
- Detailed non-vendor package deliverable requirements remain open for Gate 5 disposition unless supported by the accepted package context and cited source slices.
- Vendor package control logic, package data maps, permissive logic, trip interfaces, and alarm priorities are not finalized here where the source states they remain vendor-integration or detailed-design items.

Sources: `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` row for DEL-009-04.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-001 | The production package shall preserve the Gate 7 identity: DEL-009-04, PKG-009, WBS 02, Controls discipline, SOW-0009. | `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` row for DEL-009-04 |
| REQ-002 | The package shall account for the workbook-flagged interface categories: Process Piping, Utility Piping, Relief / Flare / Vent, Electrical Power, I&C / Control Cabling, Communications / Network, Building HVAC / Services, and Fire & Gas / Safety Systems. | `_Sources/26020-Packages_Interfaces_4_export.xlsx`, sheet `Packages`, row with `ID #` 9 |
| REQ-003 | The package shall carry the workbook interface review note requiring confirmation whether controls power-panel interfaces should be tracked separately. | `_Sources/26020-Packages_Interfaces_4_export.xlsx`, sheet `Packages`, row with `ID #` 9 |
| REQ-004 | The BPCS shall be treated as the primary process control system for facility process inputs and outputs, except compression unit controls, which are handled by standalone Unit Control Systems and integrated for monitoring and alarming. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, `SEC-13 - Control System Basis` / `Control System Overview` |
| REQ-005 | The Process Control Network shall connect Level 1 industrial equipment to Level 2 and Level 3 networking equipment and servers, with outside access restricted through an IDMZ. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, `Topology and Networks` |
| REQ-006 | The I/O Network shall be segregated from other networks and dedicated to I/O node communication. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, `Topology and Networks` |
| REQ-007 | The control system shall use at least two physical servers for primary server functions, designed for fault-tolerant operation. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, `Servers and Virtualization` |
| REQ-008 | The BPCS controller platform shall be Allen-Bradley ControlLogix 1756-L8x series. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, `BPCS and Remote I/O` |
| REQ-009 | Remote I/O shall use Allen-Bradley Flex5000 I/O and connect to the I/O Network via PRP network configuration for the 03-25 basis. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, `BPCS and Remote I/O` |
| REQ-010 | Process and safety devices associated with the BPCS shall be wired to the nearest Remote I/O control panel where practical, including ESD buttons, fire detection, LEL detection, H2S detection, and other process-related safety items. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, `BPCS and Remote I/O` |
| REQ-011 | Modbus data shall be used for monitoring and data collection only; process control shall not be performed over Modbus. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, `Unit Control Systems and Package Interfaces` |
| REQ-012 | The controls basis shall monitor the 03-25 instrument-air interface and alarm or trip according to final cause-and-effect logic; no local 03-25 instrument-air compressor controls shall be added. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, `Instrument Air Interface` |
| REQ-013 | Fire detection instrumentation shall be connected to the facility Controls System; no dedicated fire alarm protection system is provided by the cited basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `Detection Systems` / `Fire Detection` |
| REQ-014 | ESD pushbuttons shall be located outside all building exterior doors, and unit control panel pushbuttons shall trip the local unit emergency shutdown mode. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `Shutdown Interfaces`; `Table 14-3 - ESD and Unit Shutdown Basis` |
| REQ-015 | Power circuits at 13.8 kV, 4,160 V, and 600 V shall be separated from control and instrument circuits by distance, shielding, or routing as required to minimize interference. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, `Electrical Buildings, Raceways, Lighting, and Heat Tracing` |

## Standards

| Standard or basis | Applicability | Status |
|---|---|---|
| Gate 7 PROJECT_DECOMP snapshot | Authoritative package, scope, objective, deliverable, artifact, and interface basis for this run. | Accessible. |
| 26020 Packages Interfaces workbook | Workbook row authority for package identity and interface categories. | Accessible. |
| 03-25 Compressor Station and Liquids Hub DBM controls sections | Controls basis for WBS 02 where applicable to PKG-009. | Accessible. |
| 04-25 Deepcut DBM controls/protection sections | Cross-facility controls topology and protection-interface basis where applicable to shared controls architecture. | Accessible. |
| Project electrical specifications | Referenced by DBM for cable tray, conduit, grounding, and bonding compliance. | Location TBD; not available as a controlled source slice in this run. |
| Client IT/OT policies | Govern IDMZ layout, enterprise-network requirements, network hardware selection, and industrial networking policy compliance. | Location TBD; detailed coordination required. |

## Verification

| Requirement group | Verification approach |
|---|---|
| Identity and scope | Check DEL-009-04 against `_CONTEXT.md`, Gate 7 `DELIVERABLE_REGISTER.csv`, and `SCOPE_LEDGER.csv`. |
| Workbook interface categories | Check package workbook row `ID #` 9 and confirm each flagged interface category is either addressed or intentionally deferred in the deliverable register/closure record. |
| Controls architecture | Review BPCS, RIO, PCN, I/O Network, IDMZ, server, and workstation design outputs against cited DBM sections. |
| Package and third-party interfaces | Confirm hardwired versus protocol-based signals are assigned by criticality and that Modbus is not used for process control. |
| Safety and protection interfaces | Confirm fire detection, LEL, H2S, ESD pushbutton, beacon/horn, and unit shutdown interfaces are represented in controls deliverables and cause-and-effect development. |
| Electrical/control separation | Check raceway/cable routing design for separation of power circuits from control and instrument circuits. |
| Open detailed-design items | Track TBDs in the source-limited requirements closure record until resolved by accepted source updates or human ruling. |

## Documentation

The production package shall include or reference the following records:

- Discipline production package basis.
- Discipline deliverable register, currently TBD.
- Source-limited requirements closure record.
- Interface category matrix for workbook row `ID #` 9.
- Controls architecture basis covering BPCS, networks, servers, Remote I/O, and package interfaces.
- Open-items list for design-development items and unavailable standards/policies.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HRR-001 | Workbook note asks whether controls power-panel interfaces should be tracked separately. | `_Sources/26020-Packages_Interfaces_4_export.xlsx`, sheet `Packages`, row with `ID #` 9 | No separate deliverable-local dependency/register entry exists yet. | Scope, Requirements, Documentation | Treat as an open interface-tracking decision for Gate 5/dependency extraction. | TBD |
| HRR-002 | 03-25 source states RIO connects via PRP; 04-25 source allows PRP or DLR and says DLR versus PRP is detailed-design dependent. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, `BPCS and Remote I/O` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `Controls System Hardware`; `Interfaces, Assumptions, and Open Design Development` | Requirements, Verification | Use the 03-25 source for WBS 02 where directly applicable; keep cross-facility DLR/PRP selection open where the applicable network is not fixed. | TBD |
