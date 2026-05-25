# Datasheet: DEL-010-02_package-datasheet — Package Datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-010-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` row for `DEL-010-02_package-datasheet` |
| Parent package | `PKG-010` — Controls system design and integration | `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` |
| Discipline | Controls | `_CONTEXT.md`; `26020-Packages_Interfaces_4_export.xlsx` sheet1 row 11 |
| Responsible party | EPC Integrator | `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` |
| Scope item | `SOW-0010` | `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` |

## Attributes

| Attribute | Current basis | Source |
|---|---|---|
| Datasheet purpose | Technical handoff package containing data required for third-party vendor or discipline package engineering and design. | Gate 7 `DELIVERABLE_REGISTER.csv` row for `DEL-010-02_package-datasheet` |
| Required artifact content | Package technical datasheet; vendor engineering handoff basis; package interface requirements matrix; source-supported equipment and design criteria. | `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv`; Gate 7 `ARTIFACT_REGISTER.csv` rows for `DEL-010-02_package-datasheet` |
| Package interface categories marked for the controls package | Process Piping; Utility Piping; Relief / Flare / Vent; Electrical Power; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems. | `26020-Packages_Interfaces_4_export.xlsx` sheet1 row 11; Gate 7 `INTERFACE_REGISTER.csv` rows `IFC-D8F0EE6268`, `IFC-B417C160D6`, `IFC-0F29FF779E`, `IFC-7692ABF6DF`, `IFC-0594D83117`, `IFC-BBCAEE6BE3`, `IFC-E721E064DB`, `IFC-84EB36C954` |
| Interface note disposition | Controls power-panel interface question is retained as interface facts/artifacts under the package datasheet; no separate package or deliverable is created. | Gate 7 `ARTIFACT_REGISTER.csv` rows `ART-6EDAB0188D` through `ART-27D9FD5E81`; Gate 7 `INTERFACE_REGISTER.csv` rows 32-39 |
| Control-system architecture basis | BPCS provides centralized monitoring/control for the 03-25 Compressor Station and Liquids Hub; compression unit controls are standalone Unit Control Systems integrated for monitoring and alarming. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-13 "Control System Basis" and "Unit Control Systems and Package Interfaces" |
| BPCS controller platform | Allen-Bradley ControlLogix 1756-L8x series; BPCS is simplex in current basis. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-13 "BPCS and Remote I/O" |
| Remote I/O platform | Allen-Bradley Flex5000 I/O connected to the I/O Network using PRP network configuration. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-13 "BPCS and Remote I/O" |
| Package communication basis | Defined communication protocols and hardwired signals by criticality; Modbus via Kepware KepserverEX for monitoring/data collection only, not process control. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-13 "Unit Control Systems and Package Interfaces" |
| Environmental/design envelope | Design ambient temperature range is -40 deg C to +35 deg C for equipment and facilities unless package-specific basis is stricter. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-02 "Design Ambient Temperature" |

## Conditions

| Condition | Current basis | Source |
|---|---|---|
| Data completeness | Final package data maps, permissive logic, trip interfaces, and alarm priorities remain detailed-design/vendor-integration items. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-13 "Unit Control Systems and Package Interfaces" |
| Network detail maturity | IDMZ layout, policies, firewall rules, IP addressing, and VLAN segmentation remain detailed-design/client IT/OT coordination items. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-13 "Topology and Networks" |
| Fire and gas data maturity | Detector quantity, tag list, set points, voting logic, placement, and calibration requirements remain TBD pending detailed design and safety studies. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-14 "LEL, H2S, Methyl Mercaptan, and Fire Detection" |
| Instrument air interface | 03-25 instrument-air demand is carried as 393 SCFM TBC; combined 03-25/04-25 demand is 1,113 SCFM TBC. No local 03-25 instrument-air compressor controls are to be added. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-13 "Instrument Air Interface" |
| Declared blockers | None declared. | `_DEPENDENCIES.md` |

## Construction

The package datasheet shall be constructed as a handoff record that preserves package identity, source basis, package interface categories, controls architecture basis, network/interface constraints, and unresolved detailed-design fields as `TBD`.

Minimum datasheet content:

| Section | Required content | Source |
|---|---|---|
| Package identity | Package ID, WBS/workbook row, discipline, responsible party, deliverable ID, Gate 7 snapshot reference. | `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv`; `26020-Packages_Interfaces_4_export.xlsx` sheet1 row 11 |
| Interface matrix | The eight active interface categories listed above, plus interface IDs where available. | Gate 7 `INTERFACE_REGISTER.csv`; `26020-Packages_Interfaces_4_export.xlsx` sheet1 row 11 |
| Controls data basis | BPCS, RIO, network, package communication, standalone Unit Control System integration, and Modbus monitoring-only constraints. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-13 |
| Safety/interface data | Fire/gas/ESD/RIO interface requirements and unresolved detector/cause-and-effect fields. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-14 |
| Open fields | Any unsupported value, tag list, model, set point, data map, trip list, network address, VLAN, alarm priority, or vendor-specific item. | Source-grounding rule from `four-documents` skill; source gaps above |

## References

- `_CONTEXT.md`
- `_DEPENDENCIES.md`
- `_REFERENCES.md`
- Gate 7 `DELIVERABLE_REGISTER.csv`
- Gate 7 `ARTIFACT_REGISTER.csv`
- Gate 7 `INTERFACE_REGISTER.csv`
- Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx`, `xl/worksheets/sheet1.xml`, row 11
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-02, SEC-09, SEC-12, SEC-13, SEC-14
