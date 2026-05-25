# Datasheet: DEL-009-04 EPC / Controls Discipline Production Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-009-04_epc-controls-discipline-production-package |
| Deliverable name | EPC / Controls Discipline Production Package |
| Parent package | PKG-009 - Controls system design and integration |
| Workbook row | Packages row 10 |
| WBS | 02 |
| CoA tracking number | 26020-01-32-001 |
| Discipline | Controls |
| Type | EPC/Discipline Production Unit |
| Responsible party | TBD; EPC Integrator or discipline subcontractor as assigned |
| Covers scope item | SOW-0009 |

Sources: `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` row for DEL-009-04; `_Sources/26020-Packages_Interfaces_4_export.xlsx`, sheet `Packages`, row with `ID #` 9.

## Attributes

| Attribute | Source-supported value |
|---|---|
| Package function | Controls system design and integration for WBS 02. |
| Interface categories flagged by package workbook | Process Piping; Utility Piping; Relief / Flare / Vent; Electrical Power; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems. |
| Interface review note | Confirm whether controls power-panel interfaces should be tracked separately. |
| Primary controls architecture basis | Centralized BPCS monitoring and control for 03-25 Compressor Station and Liquids Hub, with standalone Unit Control Systems for compression unit controls integrated for monitoring and alarming. |
| BPCS controller platform | Allen-Bradley ControlLogix 1756-L8x series. |
| Remote I/O basis | Allen-Bradley Flex5000 I/O; RIO connected to I/O Network via PRP network configuration for 03-25 basis. |
| Package and third-party data integration | Defined communication protocols and hardwired signals according to criticality; Modbus integrated using Kepware KepserverEX and used for monitoring/data collection only, not process control. |
| Instrument-air controls interface | Monitor 03-25 instrument-air interface and alarm or trip according to final cause-and-effect logic; no local 03-25 instrument-air compressor controls are to be added. |

Sources: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` sections `SEC-13 - Control System Basis`, `Instrument Air Interface`; `_Sources/26020-Packages_Interfaces_4_export.xlsx`, sheet `Packages`, row with `ID #` 9.

## Conditions

| Condition | Source-supported value |
|---|---|
| Electrical/control circuit coordination | Power circuits at 13.8 kV, 4,160 V, and 600 V are to be separated from control and instrument circuits by distance, shielding, or routing as required to minimize interference. |
| Hazardous-area/building interface | Forced ventilation for process modules or buildings requiring ventilation to maintain classification is to be controlled and monitored; plant control interlocks are to be initiated where needed. |
| UPS service basis | 120 VAC / 125 VDC UPS services support the control system, selected emergency/critical lighting, MV breaker control, and MV protective relay. |
| Fire detection interface | Fire detection instrumentation is connected to the facility Controls System; a dedicated fire alarm protection system is not provided in the cited basis. |
| ESD and unit shutdown interface | Building ESD pushbuttons and unit control panel pushbuttons are part of the instrumented protection interface; large-module ESD pushbutton locations remain TBD during detailed engineering. |

Sources: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` sections `Area Classification`, `System Voltages`, `Electrical Buildings, Raceways, Lighting, and Heat Tracing`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` sections `Detection Systems`, `Shutdown Interfaces`, `Supported Tables`.

## Construction

| Production package component | Status |
|---|---|
| Discipline production package basis | Required anticipated artifact. |
| Discipline deliverable register | TBD; anticipated artifact, not yet resolved in the accepted package context. |
| Source-limited requirements closure record | Required anticipated artifact. |
| RIO cabinet locations | TBD during detailed design. |
| DLR versus PRP selection across applicable I/O and controller networks | TBD during detailed design where not fixed by a source section. |
| Process controller sizing and quantity | TBD during detailed design. |
| Unit controller sizing | TBD during detailed design. |
| Historian product | TBD; select Canary Labs or Rockwell Historian during controls implementation. |
| IDMZ/firewall rules/IP addressing/VLAN segmentation | TBD; final details are client IT/OT coordination items. |

Sources: `_CONTEXT.md`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` section `Interfaces, Assumptions, and Open Design Development`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` section `Topology and Networks`.

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/SCOPE_LEDGER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
