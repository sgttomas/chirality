# Datasheet: EPC / Controls Discipline Production Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-010-04_epc-controls-discipline-production-package |
| Deliverable name | EPC / Controls Discipline Production Package |
| Parent package | PKG-010 - Controls system design and integration |
| Workbook row / WBS | Row 11 / WBS 03 |
| Discipline | Controls |
| Type | EPC/Discipline Production Unit |
| Responsible party | TBD; EPC Integrator or discipline subcontractor as assigned |
| Scope item | SOW-0010 |
| Source basis | Workbook Packages row 11; Gate 7 PROJECT_DECOMP snapshot; DBM-Comp_and_Liquids SEC-13 |

## Attributes

| Attribute | Source-grounded value |
|---|---|
| Package role | Workbook-defined Controls package for "Controls system design and integration" under WBS 03. Source: PACKAGE_REGISTER.csv, PKG-010. |
| Responsibility model | EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred. Source: PACKAGE_REGISTER.csv, PKG-010. |
| Production package evidence | Discipline production package basis and source-limited requirements closure record. Source: ARTIFACT_REGISTER.csv, DEL-010-04. |
| BPCS platform | Allen-Bradley ControlLogix 1756-L8x series; BPCS is simplex in the current basis, with controller quantity and sizing to be determined during detailed design. Source: 3-25_Comp_and_Liquids_DBM.md, SEC-13 Control System Basis. |
| Remote I/O platform | Allen-Bradley Flex5000 I/O over redundant Ethernet with Parallel Redundancy Protocol. Source: 3-25_Comp_and_Liquids_DBM.md, SEC-13 Control System Basis. |
| Network basis | Process Control Network, segregated I/O Network, IDMZ, and Enterprise Network interfaces; final IDMZ layout, policies, firewall rules, IP addressing, and VLAN segmentation remain detailed-design/client IT-OT coordination items. Source: 3-25_Comp_and_Liquids_DBM.md, SEC-13 Control System Basis. |
| Package controls boundary | Compression unit controls are standalone Unit Control Systems; values and general alarms are replicated to the BPCS. Final data maps, permissive logic, trip interfaces, and alarm priorities remain vendor integration items. Source: 3-25_Comp_and_Liquids_DBM.md, SEC-13 Unit Control Systems and Package Interfaces. |
| Modbus use | Modbus is for monitoring and data collection only; process control is not carried over Modbus. Source: 3-25_Comp_and_Liquids_DBM.md, SEC-13 Unit Control Systems and Package Interfaces. |

## Conditions

| Condition | Value |
|---|---|
| Ambient basis affecting controls equipment | -40 deg C minimum ambient governs exposed equipment, package buildings, control panels, instrumentation, and field devices unless a more severe process or vendor condition applies. Source: 3-25_Comp_and_Liquids_DBM.md, SEC-02 site/design basis. |
| Instrument air interface | Instrument air is supplied from 04-25; no local 03-25 instrument-air compressor controls are to be added. 03-25 instrument-air demand is carried as 393 SCFM TBC. Source: 3-25_Comp_and_Liquids_DBM.md, SEC-13. |
| Safety-device wiring | Process and safety devices associated with BPCS are wired to the nearest Remote I/O control panel where practical, including ESD buttons, fire detection, LEL detection, H2S detection, and other process-related safety items. Source: 3-25_Comp_and_Liquids_DBM.md, SEC-13. |
| Declared dependencies | None declared during PREPARATION. Source: _DEPENDENCIES.md. |

## Construction

| Construction/interface item | Basis |
|---|---|
| Applicable package interfaces | Process Piping; Utility Piping; Relief / Flare / Vent; Electrical Power; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems. Source: PACKAGE_REGISTER.csv and INTERFACE_REGISTER.csv, PKG-010. |
| Control/instrument segregation | Power circuits at 13.8 kV, 4,160 V, and 600 V shall be separated from control and instrument circuits by distance, shielding, or routing as required to minimize interference. Source: 3-25_Comp_and_Liquids_DBM.md, SEC-12 Electrical System Basis. |
| Building coordination | Electrical/control buildings and package buildings require coordination with area classification, ventilation, heating, emergency egress, fire and gas detection, ESD pushbutton placement, RIO panel locations, power distribution, and maintenance access. Source: 3-25_Comp_and_Liquids_DBM.md, SEC-08/SEC-12. |
| Detailed discipline deliverable register | TBD. Gate 7 states detailed non-vendor package deliverable requirements are source-limited and remain open for Gate 5 disposition. |

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/ARTIFACT_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
