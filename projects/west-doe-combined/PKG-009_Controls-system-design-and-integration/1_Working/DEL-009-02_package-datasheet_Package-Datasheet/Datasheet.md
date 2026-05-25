# Datasheet: DEL-009-02_package-datasheet — Package Datasheet

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-009-02_package-datasheet |
| Deliverable name | Package Datasheet |
| Parent package | PKG-009 — Controls system design and integration |
| Workbook ID / row | 9 / 10 |
| WBS | 02 |
| CoA tracking number | 26020-01-32-001 |
| Discipline | Controls |
| Type | EPC Package Datasheet |
| Responsible party | EPC Integrator |
| Source basis | Gate 7 DELIVERABLE_REGISTER.csv row DEL-009-02_package-datasheet; Gate 7 PACKAGE_REGISTER.csv row PKG-009; workbook Packages row 10 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package scope | Workbook-defined Controls package for controls system design and integration under WBS 02 with recorded physical interfaces. | Gate 7 PACKAGE_REGISTER.csv, PKG-009 |
| Datasheet purpose | Mandatory EPC Integrator technical handoff deliverable containing package data required for third-party vendor or discipline package engineering and design. | Gate 7 DELIVERABLE_REGISTER.csv, DEL-009-02_package-datasheet |
| Anticipated artifacts | Package technical datasheet; vendor engineering handoff basis; package interface requirements matrix; source-supported equipment and design criteria. | Gate 7 DELIVERABLE_REGISTER.csv, DEL-009-02_package-datasheet |
| Responsibility model | EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred from current sources. | Gate 7 PACKAGE_REGISTER.csv, PKG-009 |
| BPCS platform | Allen-Bradley ControlLogix 1756-L8x series; simplex in current basis; final controller quantity and sizing by detailed design. | _Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, SEC-13 |
| Remote I/O | Allen-Bradley Flex5000 I/O; RIO connects to I/O Network via PRP. | _Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, SEC-13 |
| Network basis | Multi-level architecture with Process Control Network, segregated I/O Network, IDMZ, and Enterprise Network interfaces. | _Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, SEC-13 |
| Package interface protocol basis | Defined communication protocols and hardwired signals according to criticality; Modbus is for monitoring/data collection only and not process control. | _Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, SEC-13 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Facility design ambient envelope | -40 deg C to +35 deg C unless a stricter package-specific basis applies. | _Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, site/design ambient basis |
| Winterization implication | -40 deg C minimum governs exposed equipment, package buildings, control panels, instrumentation, and field devices unless a more severe condition applies. | _Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, site basis |
| Instrument-air interface | Instrument air is supplied from 04-25; no local 03-25 instrument-air compressor package is retained. | _Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, SEC-07 and SEC-13 |
| Safety interface | Fire, gas, H2S, LEL, methyl mercaptan, ESD, and unit shutdown interfaces are coordinated with BPCS, Remote I/O, package controls, electrical area classification, and HAZOP/SIL outcomes. | _Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, SEC-14 |
| Detailed design TBDs | Final package data maps, permissive logic, trip interfaces, alarm priorities, detector quantities, set points, voting logic, placement, and calibration requirements remain TBD. | _Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, SEC-13 and SEC-14 |

## Construction

| Interface type | Applicability | Notes | Source |
|---|---|---|---|
| Process Piping | YES | Interface fact carried in package datasheet; no separate deliverable created. | Gate 7 INTERFACE_REGISTER.csv, PKG-009 |
| Utility Piping | YES | Interface fact carried in package datasheet; no separate deliverable created. | Gate 7 INTERFACE_REGISTER.csv, PKG-009 |
| Relief / Flare / Vent | YES | Interface fact carried in package datasheet; no separate deliverable created. | Gate 7 INTERFACE_REGISTER.csv, PKG-009 |
| Electrical Power | YES | Controls power-panel interfaces remain datasheet/interface facts. | Gate 7 INTERFACE_REGISTER.csv, PKG-009 |
| I&C / Control Cabling | YES | Field safety and process devices should wire to nearest Remote I/O where practical. | Gate 7 INTERFACE_REGISTER.csv, PKG-009; DBM SEC-13/SEC-14 |
| Communications / Network | YES | PCN/I/O/IDMZ/Enterprise segmentation and vendor data maps require detailed-design coordination. | Gate 7 INTERFACE_REGISTER.csv, PKG-009; DBM SEC-13 |
| Building HVAC / Services | YES | Package buildings and electrical buildings require controls coordination. | Gate 7 INTERFACE_REGISTER.csv, PKG-009; DBM SEC-11/SEC-13 |
| Fire & Gas / Safety Systems | YES | Safety devices include fire detection, LEL, H2S, ESD buttons, and other process-related safety items. | Gate 7 INTERFACE_REGISTER.csv, PKG-009; DBM SEC-13/SEC-14 |

## References

- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_DELIVERABLE_MAP.csv
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx, Packages row 10
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, SEC-07, SEC-11, SEC-12, SEC-13, SEC-14, SEC-15
