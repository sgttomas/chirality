# Datasheet: DEL-010-03 Construction Work Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-010-03_construction-work-package |
| Deliverable name | Construction Work Package |
| Parent package | PKG-010 - Controls system design and integration |
| Workbook ID / row | ID 10 / Workbook Packages row 11 |
| WBS | 03 |
| CoA tracking number | 26020-01-32-001 |
| Discipline | Controls |
| Type | EPC Construction Work Package |
| Responsible party | EPC Integrator |
| Source basis | Gate 7 PROJECT_DECOMP snapshot; workbook packages/interfaces export; 03-25 DBM controls and construction sections |

## Attributes

| Attribute | Source-grounded value |
|---|---|
| Package function | Controls system design and integration for WBS 03. Source: PACKAGE_REGISTER.csv, PKG-010. |
| Construction deliverable purpose | Describe physical installation, construction, tie-ins, inspection, turnover, and integration into larger facility systems. Source: DELIVERABLE_REGISTER.csv, DEL-010-03. |
| Required artifacts | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist. Source: DELIVERABLE_REGISTER.csv and ARTIFACT_REGISTER.csv, DEL-010-03. |
| Applicable interface types | Process Piping; Utility Piping; Relief / Flare / Vent; Electrical Power; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems. Source: INTERFACE_REGISTER.csv, PKG-010. |
| Controls architecture basis | BPCS centralized monitoring/control for the 03-25 Compressor Station and Liquids Hub; compression unit controls are standalone Unit Control Systems integrated for monitoring and alarming. Source: 3-25_Comp_and_Liquids_DBM.md, SEC-13. |
| Remote I/O basis | Remote I/O uses Allen-Bradley Flex5000 I/O and connects to the I/O Network via PRP network configuration; remote distribution centres include Remote I/O nodes. Source: 3-25_Comp_and_Liquids_DBM.md, SEC-13. |
| Modbus basis | Modbus is integrated using Kepware KepserverEX for monitoring and data collection only; process control is not carried over Modbus. Source: 3-25_Comp_and_Liquids_DBM.md, SEC-13. |
| Instrument air controls basis | 03-25 instrument-air interface is monitored and alarmed/tripped per final cause-and-effect logic; no local 03-25 instrument-air compressor controls are added. Source: 3-25_Comp_and_Liquids_DBM.md, SEC-13. |

## Conditions

| Condition | Value / status |
|---|---|
| Declared upstream dependencies | None declared during PREPARATION. Source: _DEPENDENCIES.md. |
| Declared downstream dependencies | None declared during PREPARATION. Source: _DEPENDENCIES.md. |
| Default blocker threshold | INITIALIZED, advisory only from declared dependency edges. Source: _DEPENDENCIES.md and _Coordination/_COORDINATION.md. |
| Construction scope context | Construction includes construction management, grading, piling, foundations, roads, field buildings, offloading/setting modules, mechanical hookups, shipped-loose instrument/valve installation, supports, interconnecting piping, home-run cabling, terminations, lighting, fencing, security, control room/maintenance systems, utilities, and demolition/removal where required for tie-ins. Source: 3-25_Comp_and_Liquids_DBM.md, SEC-01. |
| Detailed construction sequence | TBD. No package-specific sequence is present in accessible source slices. |
| Final alarm philosophy and shutdown logic | TBD; final alarm philosophy, tone mapping, beacon layout, operator notification logic, trip lists, shutdown levels, cause-and-effect actions, and reset responsibilities remain detailed-design deliverables. Source: 3-25_Comp_and_Liquids_DBM.md, SEC-14. |

## Construction

| Construction element | Source-grounded treatment |
|---|---|
| Workface plan | Must address installation/building of the controls package and tie-ins to applicable process, utility, electrical, controls, civil/structural, and safety systems. Source: ARTIFACT_REGISTER.csv, ART-A754BC7D21. |
| Interface checklist | Must track construction-facing interfaces, tie-ins, inspection, and turnover for the approved package. Source: ARTIFACT_REGISTER.csv, ART-12A3A019E9. |
| Physical controls layout | Central control room contains operator workstations, engineering workstations, primary servers, and core network switches; MCC contains Level 1 components, secondary servers, and distribution network switches; remote I/O cabinets are located in process areas. Source: 4-25_Deepcut_DBM.md, SEC-13; used as relevant controls-system architecture context. |
| Network segregation | I/O network is segregated from other networks; PCN restricts outside access using IDMZ; IDMZ layout requires IT/OT coordination. Source: 4-25_Deepcut_DBM.md, SEC-13. |
| Package/building coordination | Package buildings, self-framing enclosures, MCC interfaces, RIO interfaces, heat tracing, HVAC, fire/gas detection, and drain/vent tie-ins shall be coordinated with civil, electrical, controls, and instrumentation sections. Source: 3-25_Comp_and_Liquids_DBM.md, SEC-09. |

## References

- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/ARTIFACT_REGISTER.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_DELIVERABLE_MAP.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx, Packages sheet, workbook row 11
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, SEC-01, SEC-09, SEC-13, SEC-14
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md, SEC-13
