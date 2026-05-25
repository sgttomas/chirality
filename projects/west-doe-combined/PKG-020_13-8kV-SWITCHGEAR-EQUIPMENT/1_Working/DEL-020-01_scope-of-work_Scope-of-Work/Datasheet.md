# Datasheet: DEL-020-01 Scope of Work

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-020-01_scope-of-work | `_CONTEXT.md` Identity |
| Deliverable name | Scope of Work | `_CONTEXT.md` Identity; Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-020-01 |
| Parent package | PKG-020 | `_CONTEXT.md` Identity; Gate 7 `PACKAGE_REGISTER.csv` row PKG-020 |
| Package name | 13.8kV SWITCHGEAR EQUIPMENT | Gate 7 `PACKAGE_REGISTER.csv` row PKG-020; Workbook Packages row 22 |
| Workbook ID / row | ID 20 / row 22 | Gate 7 `PACKAGE_REGISTER.csv` row PKG-020; `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 22 |
| WBS | 01 | Gate 7 `PACKAGE_REGISTER.csv` row PKG-020 |
| CoA tracking number | 26020-01-30-011 | Gate 7 `PACKAGE_REGISTER.csv` row PKG-020 |
| Discipline | Electrical | `_CONTEXT.md` Identity; Gate 7 `PACKAGE_REGISTER.csv` row PKG-020 |
| Deliverable type | EPC Scope of Work | `_CONTEXT.md` Identity; Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-020-01 |
| Responsible party | EPC Integrator | `_CONTEXT.md` Identity; Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-020-01 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package execution model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-020 |
| Mandatory EPC anchor deliverable | Scope of Work is one of the mandatory EPC Integrator deliverables for every approved package. | Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis; `_CONTEXT.md` Notes |
| Scope item | SOW-0021 | `_CONTEXT.md` Covers Scope Items; Gate 7 `SCOPE_LEDGER.csv` row SOW-0021 |
| Supported objectives | OBJ-001; OBJ-004; OBJ-005; OBJ-006; OBJ-008; OBJ-009; OBJ-010 | `_CONTEXT.md` Supports Objectives; Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv` rows for DEL-020-01 |
| Anticipated artifacts | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. | `_CONTEXT.md` Anticipated Artifacts; Gate 7 `ARTIFACT_REGISTER.csv` rows for DEL-020-01 |
| Package function | Plant main power distribution center: 13.8 kV switchgear bus, sized for the full facility scope, fed from the 25 kV to 13.8 kV / 50 MVA utility-supplied transformer downstream of the BC Hydro 25 kV utility supply. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Power System section (utility supply paragraph and "13.8 kV switchgear" paragraph) |
| Tagged equipment | TBD; the accessible workbook row and Gate 7 PKG-020 row do not expose a discrete 13.8 kV switchgear tag. The DBM identifies "Medium Voltage Switchgear, quantity 1" (`ELC-QAS-000007-001`) and an "810-1 13.8kV Switchgear Electrical Building", but allocation of these specific tags to PKG-020 is not explicitly confirmed in the accessible sources. See Conflict Table HR-020-01-02. | Workbook Packages row 22; Gate 7 `PACKAGE_REGISTER.csv` row PKG-020; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` electrical equipment list and electrical building list |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Utility supply context | BC Hydro utility power supplies the facility; main incoming utility voltage 25 kV (TBC); 25 kV / 13.8 kV / 50 MVA utility-supplied transformer steps down to the local 13.8 kV switchgear. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Power System section, utility supply paragraph |
| 13.8 kV system basis | 13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded; serves as facility backbone distribution to other electrical buildings. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Power System / System Voltages table |
| Downstream radial distribution | The 13.8 kV switchgear shall distribute power radially through step-down transformers to: 6.9 kV Inlet/Sales Compressor Electrical Building; 4.16 kV Acid Gas/Overheads Compressor Electrical Building; 600 V Acid Gas Compressor Electrical Building; 600 V Sales/Overheads Compressor Electrical Building; 4.16 kV/600 V General Area/Tank Farm/Process Electrical Building. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Power System section, radial-distribution bullet list |
| Cable basis | 13.8 kV medium-voltage cables: three-conductor copper TECK cable rated 15 kV with 133 percent insulation; shielded. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Cable Specifications table |
| Grounding context | BC Hydro utility transformer is grounded with a 200 A, 10 s neutral grounding resistor operating as a tripping system; major electrical equipment shall be connected to the ground grid at two points. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Grounding and Bonding section |
| Standby power context | The 13.8 kV centralized emergency-generator concept has been replaced by TOU standby generators connected at the 600 V MCC level via transfer switches. The 13.8 kV switchgear is not the standby-power tie-in point for this facility scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Power System / Standby Power paragraph |
| Housing | 13.8 kV main switchgear may be housed in prefabricated, modular electrical buildings in general purpose areas as required by detailed design; the DBM Trace Appendix identifies an "810-1 13.8kV Switchgear Electrical Building" delivered shop-built. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings section; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Trace Appendix line "810-1 13.8kV Switchgear Electrical Building" |
| Package interfaces | Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | Workbook Packages row 22; Gate 7 `PACKAGE_REGISTER.csv` row PKG-020; Gate 7 `INTERFACE_REGISTER.csv` rows for PKG-020 (`IFC-611474D99C`, `IFC-F3098CE7CD`, `IFC-8BF7209227`, `IFC-340091634A`, `IFC-2FB786FC10`, `IFC-08E563D004`) |
| Package-specific exclusions | TBD; no package-specific exclusions stated in source materials (Gate 7 record). | Gate 7 `PACKAGE_REGISTER.csv` row PKG-020 |
| Switchgear ratings (bus continuous current, short-circuit interrupting, BIL, enclosure rating, dimensions, weights, breaker count, bus configuration, lineup arrangement, control voltage source) | TBD; not present in accessible source slices for this deliverable. Detailed values shall come from vendor package data and detailed electrical studies. | Workbook Packages row 22; Gate 7 PKG-020 rows; DBM electrical sections; no accessible PKG-020 match in `_Sources/26020-Package_Requirements.docx` |
| Protection, relaying, arc-flash, and coordination basis | TBD; the DBM lists "Relay coordination and arc-flash energy study" and "Load-flow study" as required studies but does not state PKG-020 switchgear relay settings, coordination tables, or arc-flash boundaries. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` electrical studies paragraphs |

## Construction

| Construction / integration topic | Scope-of-work treatment |
|---|---|
| EPC integration boundary | Include facility-level integration, tie-ins, constructability, procurement/construction coordination, and interface management; do not assign vendor package engineering, package design, vendor documentation, or physical equipment package supply to the EPC Integrator. |
| Electrical Power | Identify PKG-020 as the plant 13.8 kV main power distribution center receiving the 50 MVA utility-transformer secondary feeder and distributing radially through step-down transformers to the named electrical buildings; detailed feeder ratings, breaker assignments, and protection coordination are TBD. |
| Grounding / Bonding | Carry grounding/bonding as an interface requiring EPC review and construction coordination at the switchgear lineup; reflect the DBM low-resistance grounding scheme and the two-point ground-grid connection requirement at facility-integration level only. |
| I&C / Control Cabling | Carry control and monitoring cabling between switchgear, the plant PLC central control panel, and protection/metering devices as an interface; specific I/O list, control voltage source (120 VAC / 125 VDC), and control philosophy are TBD pending vendor data. |
| Communications / Network | Carry communications/network as an interface (consistent with the DBM EtherNet basis for plant-PLC data acquisition from MCC/switchgear lineups); specific protocols, ports, and addressing are TBD. |
| Maintenance Access | Carry maintenance access as an interface requiring layout, clearance, breaker-removal, and bottom-entry cable coordination per the DBM electrical-building basis. |
| Structural / Foundations / Supports | Carry structural/support requirements as interface scope; package-specific loads, footprint, support details, and electrical-building accommodation are TBD pending vendor data. |

## References

- `_CONTEXT.md`, DEL-020-01 identity, scope, artifacts, objective context.
- `_DEPENDENCIES.md`, declared dependency state (none declared during PREPARATION).
- `_REFERENCES.md`, Gate 7 source pointers and shared source root.
- Gate 7 `PROJECT_DECOMP.md`, mandatory EPC anchor deliverable basis.
- Gate 7 `PACKAGE_REGISTER.csv`, row PKG-020.
- Gate 7 `DELIVERABLE_REGISTER.csv`, row DEL-020-01_scope-of-work.
- Gate 7 `SCOPE_LEDGER.csv`, row SOW-0021.
- Gate 7 `ARTIFACT_REGISTER.csv`, rows for DEL-020-01.
- Gate 7 `INTERFACE_REGISTER.csv`, PKG-020 rows.
- Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for DEL-020-01.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages row 22.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Power System, System Voltages, Standby Power, Transformers, Motor Control, Electrical Buildings, Grounding and Bonding, Cable Specifications, and Trace Appendix sections.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific 13.8 kV switchgear content; no PKG-020 match accessible in this run.
