# Specification: EPC / Controls Discipline Production Package

## Scope

This specification governs DEL-008-04, the EPC / Controls Discipline Production Package for PKG-008 Controls system design and integration. The package is a controls discipline production unit for the non-vendor scope carried by the accepted Gate 7 decomposition.

The deliverable covers:

- discipline production package basis;
- TBD discipline deliverable register;
- source-limited requirements closure record;
- controls interface basis for PKG-008 interface types recorded in Gate 7 registers.

The deliverable excludes:

- creation of a separate controls power-panel package or deliverable, because Gate 6 disposition keeps those interfaces as package datasheet interface facts/artifacts;
- unsupported internal discipline drawing lists, calculations, or detailed deliverable registers not present in the accepted source set;
- raw source reinterpretation beyond accepted Gate 7 truth and accessible controls source slices.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-001 | The production package shall identify DEL-008-04 as a controls discipline production package under PKG-008 and SOW-0008. | Gate 7 `DELIVERABLE_REGISTER.csv`; `SCOPE_LEDGER.csv` |
| REQ-002 | The production package shall carry PKG-008 interface types: Process Piping, Utility Piping, Relief / Flare / Vent, Electrical Power, I&C / Control Cabling, Communications / Network, Building HVAC / Services, and Fire & Gas / Safety Systems. | Gate 7 `PACKAGE_REGISTER.csv`; `INTERFACE_REGISTER.csv`; workbook Packages row 9 |
| REQ-003 | The production package shall retain the controls power-panel interface note until resolved by the proper project authority; no separate package or deliverable shall be inferred from it. | Gate 7 `ARTIFACT_REGISTER.csv`; `INTERFACE_REGISTER.csv` |
| REQ-004 | Controls-system design shall support central operations control room monitoring/control and packaged-equipment monitoring at the central control room. | `4-25_Deepcut_DBM.md`, SEC-13 Operating Philosophy |
| REQ-005 | The controls architecture shall include PCN, I/O Network, Controller Network, IDMZ, and Enterprise Network functions as applicable to the final topology. | `4-25_Deepcut_DBM.md`, SEC-13 Network Basis |
| REQ-006 | The PCN shall restrict outside access using an IDMZ and be designed for continuous operation through redundant installation. | `4-25_Deepcut_DBM.md`, SEC-13 Network Basis |
| REQ-007 | I/O and controller network topology shall use DLR or PRP where applicable; final selection remains detailed design. | `4-25_Deepcut_DBM.md`, SEC-13 Network Basis; SEC-13 Interfaces, Assumptions, and Open Design Development |
| REQ-008 | The process control system controller shall be Allen-Bradley ControlLogix 1756-L8x series; controller sizing and quantity remain detailed-design items. | `4-25_Deepcut_DBM.md`, SEC-13 Controls System Hardware |
| REQ-009 | Remote I/O modules shall use Allen-Bradley Flex5000 I/O or Allen-Bradley ControlLogix I/O. | `4-25_Deepcut_DBM.md`, SEC-13 Controls System Hardware |
| REQ-010 | Each package or unit designed to operate as a standalone machine shall have a standalone unit control system; the unit control system HMI shall be integrated into the BPCS rather than maintained as a standalone HMI. | `4-25_Deepcut_DBM.md`, SEC-13 Controls System Hardware |
| REQ-011 | Modbus data shall be integrated using KepserverEX and used for monitoring and data collection only, not process control. | `4-25_Deepcut_DBM.md`, SEC-13 Modbus Data Basis |
| REQ-012 | Fire detection instrumentation shall be connected to the facility Controls System; no dedicated fire alarm protection system is provided. | `4-25_Deepcut_DBM.md`, SEC-14 Fire Detection |
| REQ-013 | Safety devices associated with the BPCS system shall be wired to the nearest Remote I/O control panel where practical. | `3-25_Comp_and_Liquids_DBM.md`, SEC-13 BPCS and Remote I/O |
| REQ-014 | The requirements closure record shall preserve detailed-design TBDs, including Remote I/O cabinet locations, DLR versus PRP selection, process controller sizing and quantity, final package data maps, permissive logic, trip interfaces, and alarm priorities. | `4-25_Deepcut_DBM.md`, SEC-13 Interfaces, Assumptions, and Open Design Development; `3-25_Comp_and_Liquids_DBM.md`, SEC-13 Unit Control Systems and Package Interfaces |

## Standards

| Standard or specification | Applicability | Source |
|---|---|---|
| CSA C22.1-21 Canadian Electrical Code | Electrical installation and control/electrical interface basis. | `4-25_Deepcut_DBM.md`, SEC-12 Governing Codes, Standards, Specifications, and Studies |
| Applicable BC provincial/local electrical codes and regulations | Electrical and instrumentation installation context. | `4-25_Deepcut_DBM.md`, SEC-12 |
| CSA, API, IEEE, ISA, NEMA, WorkSafeBC, Technical Safety BC, BCER | Applicable standards/regulatory bodies for electrical and instrumentation interfaces. | `4-25_Deepcut_DBM.md`, SEC-12 |
| ELC-QAS-000013-001 Control Panel Specification, Rev. 2 | Control panel specification. | `4-25_Deepcut_DBM.md`, Table 12-1 |
| ELC-QAS-000014-001 Instrumentation General, Rev. 1 | Instrumentation basis. | `4-25_Deepcut_DBM.md`, Table 12-1 |
| ELC-QAS-000015-001 Instrumentation for Packaged Equipment, Rev. 1 | Packaged-equipment instrumentation. | `4-25_Deepcut_DBM.md`, Table 12-1 |
| ELC-QAS-000016-001 Combustible and Toxic Gas Detection Design, Rev. 1 | Gas detection interface basis. | `4-25_Deepcut_DBM.md`, Table 12-1 |
| ELC-QAS-000017-001 Fire Detection Design, Rev. 1 | Fire detection interface basis. | `4-25_Deepcut_DBM.md`, Table 12-1 |
| ELC-QAS-000018-001 Vibration Instrumentation, Rev. 1 | Vibration instrumentation. | `4-25_Deepcut_DBM.md`, Table 12-1 |

## Verification

| Requirement(s) | Verification approach |
|---|---|
| REQ-001 through REQ-003 | Check deliverable identity, SOW linkage, interface list, and controls power-panel note against Gate 7 registers. |
| REQ-004 through REQ-011 | Review production package basis against DBM SEC-13 controls architecture, hardware, configuration, and data integration sections. |
| REQ-012 through REQ-013 | Review fire/gas/ESD and BPCS Remote I/O interfaces against DBM SEC-14 and 3-25 SEC-13. |
| REQ-014 | Confirm closure record lists all TBD detailed-design items and does not silently close them. |
| Standards table | Verify cited project specifications and codes against the latest project specification index before IFC or procurement release. |

## Documentation

The production package shall include or explicitly defer:

- discipline production package basis;
- discipline deliverable register, currently TBD;
- source-limited requirements closure record;
- PKG-008 interface basis and controls power-panel note disposition;
- references to Gate 7 registers and controls DBM source slices;
- list of remaining detailed-design TBD items and required human/project authority decisions.
