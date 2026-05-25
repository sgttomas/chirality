# Datasheet: EPC / Controls Discipline Production Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-008-04_epc-controls-discipline-production-package |
| Deliverable name | EPC / Controls Discipline Production Package |
| Parent package | PKG-008 - Controls system design and integration |
| Workbook basis | Workbook Packages row 9; WBS 01; CoA tracking number 26020-01-32-001 |
| Discipline | Controls |
| Type | EPC/Discipline Production Unit |
| Responsible party | TBD; EPC Integrator or discipline subcontractor as assigned |
| Scope item | SOW-0008 |
| Source basis | Gate 7 PROJECT_DECOMP snapshot; 26020-Packages_Interfaces_4_export.xlsx; DBM controls sections listed in References |

## Attributes

| Attribute | Source-grounded value |
|---|---|
| Package function | Workbook-defined Controls package for controls system design and integration. |
| Production package role | Discipline production package basis and source-limited requirements closure record for non-vendor controls scope. Detailed discipline deliverable register remains TBD. |
| Operating philosophy | Controls system operation is from a central operations control room; packaged equipment uses dedicated control equipment, with process monitoring available at the central control room. |
| Controls topology | Multi-level topology from field devices through enterprise networks: Level 0 field instrumentation, Level 1 controllers/processors, Level 2 supervisory control, Level 3 site operations/control, IDMZ, and optional enterprise Levels 4 and 5. |
| Network basis | PCN, I/O Network, Controller Network, IDMZ, and Enterprise Network are part of the controls architecture. I/O and controller redundancy topology is PRP or DLR as resolved during detailed design. |
| Controller basis | Process control system controller: Allen-Bradley ControlLogix 1756-L8x series. Unit control systems: Allen-Bradley ControlLogix 1756-L8x series in simplex configuration. |
| Remote I/O basis | Remote I/O modules: Allen-Bradley Flex5000 I/O or Allen-Bradley ControlLogix I/O, connected by PRP or DLR as applicable. |
| Configuration basis | Propak Systems standard library; PLC library release 5.2 in the mapped authority; latest Propak Systems standard FactoryTalk Library with Tourmaline operations, maintenance, and engineering input. |
| Modbus basis | KepserverEX integrates Modbus data; Modbus is for monitoring and data collection only, not process control. |
| Safety interface basis | Fire detection instrumentation connects to the facility Controls System; ESD buttons, fire detection, LEL detection, H2S detection, and other process-related safety items are wired to nearby Remote I/O where practical. |

## Conditions

| Condition | Value |
|---|---|
| Declared upstream dependencies | None declared during PREPARATION. |
| Declared downstream dependencies | None declared during PREPARATION. |
| Interface types recorded for PKG-008 | Process Piping; Utility Piping; Relief / Flare / Vent; Electrical Power; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems. |
| Interface note | Confirm whether controls power-panel interfaces should be tracked separately. Gate 6 disposition carries controls power-panel interfaces as package datasheet interface facts/artifacts, with no separate package or deliverable created. |
| Open production-package condition | Detailed non-vendor controls discipline deliverable requirements are source-limited and remain open for Gate 5 disposition. |

## Construction

| Production element | Basis |
|---|---|
| Discipline production package basis | Must be assembled from Gate 7 accepted package/deliverable/interface registers and the controls DBM source slices listed in References. |
| Discipline deliverable register | TBD; source set confirms the need for a register but does not enumerate DEL-008-04 internal drawings, indices, or calculation deliverables. |
| Requirements closure record | Must identify source-supported requirements, TBD detailed-design items, and any scope gaps rather than converting decomposition narrative into unsupported requirements. |
| Interface closure | Must carry the PKG-008 interface types and the controls power-panel note until resolved by assigned Gate 5 or detailed-design authority. |

## References

- Gate 7 PROJECT_DECOMP snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`
- `DELIVERABLE_REGISTER.csv`, row for DEL-008-04.
- `PACKAGE_REGISTER.csv`, row for PKG-008.
- `ARTIFACT_REGISTER.csv`, rows for DEL-008-04 and PKG-008 interface facts.
- `INTERFACE_REGISTER.csv`, rows for PKG-008.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for DEL-008-04.
- `SCOPE_LEDGER.csv`, row SOW-0008.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 9.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-13 Controls System Basis; SEC-14 instrumented protection basis; SEC-12 electrical/control interfaces.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-13 Control System Basis.
