# Datasheet: DEL-038-01 Scope of Work

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-038-01_scope-of-work | `_CONTEXT.md` Identity |
| Deliverable name | Scope of Work | `_CONTEXT.md` Identity; Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-038-01_scope-of-work |
| Parent package | PKG-038 | `_CONTEXT.md` Identity; Gate 7 `PACKAGE_REGISTER.csv` row PKG-038 |
| Package name | 600V ELECTRICAL BUILDING (820-1) | Gate 7 `PACKAGE_REGISTER.csv` row PKG-038; `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 40 |
| Workbook ID / row | ID 38 / row 40 | Workbook Packages row 40; Gate 7 `PACKAGE_REGISTER.csv` row PKG-038 |
| WBS | 01 | Workbook Packages row 40; Gate 7 `PACKAGE_REGISTER.csv` row PKG-038 |
| CoA tracking number | 26020-01-30-029 | Workbook Packages row 40; Gate 7 `PACKAGE_REGISTER.csv` row PKG-038 |
| Discipline | Electrical | Workbook Packages row 40; `_CONTEXT.md` Identity |
| Deliverable type | EPC Scope of Work | `_CONTEXT.md` Identity; Gate 7 `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md` Identity; Gate 7 `DELIVERABLE_REGISTER.csv` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package execution model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-038 |
| Mandatory EPC anchor deliverable | Scope of Work is the mandatory Gate 5 EPC anchor deliverable for each approved package. | `_CONTEXT.md` Notes; Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis |
| Scope item | SOW-0039 | `_CONTEXT.md` Covers Scope Items; Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-038-01_scope-of-work |
| Supported objectives | OBJ-001; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 | `_CONTEXT.md` Supports Objectives; Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-038-01_scope-of-work; Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv` rows for DEL-038-01_scope-of-work |
| Anticipated artifacts | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. | `_CONTEXT.md` Anticipated Artifacts; Gate 7 `ARTIFACT_REGISTER.csv` rows ART-6F1522B9E8, ART-C01B3E1EDE, ART-C80EB8F110, ART-458B21AA61 |
| Package class | Workbook-defined vendor-owned Electrical package. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-038 |
| Package function | Prefabricated, climate-controlled electrical building intended to house facility low-voltage (600 V) distribution equipment per the DBM electrical buildings basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2971-2979 |
| Tagged equipment | TBD; the accessible workbook row and Gate 7 PKG-038 row do not expose specific equipment tags. The DBM identifies three 600 V electrical buildings by site number (840-1 600V Acid Gas Compressor Electrical Building; 850-1 600V Inlet/Sales Compressor Electrical Building; 860-1 600V General Area/Tank Farm Electrical Building), and lists 820-1 as the 6.9 kV Inlet/Sales Compressor Electrical Building. Allocation of PKG-038 to a specific building tag is not confirmed; see Conflict Table HR-038-01-01. | Workbook Packages row 40; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2811-2816, 2921-2925 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Facility LV electrical context | DBM defines the low-voltage service as 600 V, 3 phase, 3 wire, 60 Hz, high-resistance grounded with a 5 A continuous resistor; 600 V is used for motors 3/4 hp through 250 hp DOL, lighting and utility distribution transformers, building heaters, and UPS systems larger than 10 kVA. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2934-2937 |
| Power distribution basis | The 13.8 kV switchgear distributes radially through step-down transformers to three 600 V electrical buildings (Acid Gas Compressor; Sales/Overheads Compressor; General Area/Tank Farm/Process) and to the 6.9 kV and 4.16 kV electrical buildings. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2917-2925 |
| 600 V MCC basis | 600 V MCCs are traditional MCCs with electronic motor overload relays, ground/resistor fault detection (alarm-only), and power metering; 600 V VFDs are provided as part of the 600 V MCC lineup; standalone 600 V VFDs are not allowed unless dedicated to large motors. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2959, 2985 |
| Electrical building housing scope | Electrical buildings may house, as required by detailed design, 13.8 kV switchgear, MV MCCs, MV soft starters, MV VFDs, 600 V MCCs, 120 V AC UPS with battery banks, 125 V DC UPS with battery banks, 600 V to 208/120 V distribution transformers and panelboards, 208/120 V contactor panels, plant PLC control panels, and network racks. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2971 |
| HVAC basis | Electrical buildings shall be climate-controlled with HVAC sized as an n+1 system so the cooling system can tolerate failure or maintenance shutdown of one HVAC unit without affecting building heating and cooling. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2975 |
| Cable entry basis | Electrical buildings shall be designed for bottom entry of incoming and outgoing power cables; buildings shall be elevated on piles to provide space beneath for incoming cables in trays to the 600 V MCC main incoming section; outgoing 600 V MCC cables to facility 600 V loads shall also be bottom entry. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2977 |
| Cable types | Electrical buildings shall be wired with TECK and ACIC cables; EMT conduit shall be used for adjacent equipment such as control panels to contactor panels; an outdoor GFI receptacle shall be provided for exterior maintenance; equipment doors shall be sized for, or include removable transoms for, removal of the largest equipment. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2979 |
| Standby power interface | Standby power is provided by TOU low-voltage standby generators connected at the 600 V MCC level with transfer switches, supplying both 04-25 and 03-25 critical loads. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2076, 2080, 2084, 2943 |
| Grounding basis | Each 600 V transformer shall be grounded by a 5 A continuous high-resistance grounding resistor; 600 V MCCs shall include power metering and ground/resistor fault detection; ground-fault protection on 600 V systems shall be alarm-only to maintain continuity of operations; all major electrical equipment shall be directly connected to the ground grid at two points; ground wells at power transformers or electrical buildings shall be provided for maintenance and operational testing. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2985, 2989 |
| Hazardous area basis | Electrical buildings shall be located in general purpose areas for convenient power distribution. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2911 |
| Spacing basis | Distance between fired heater and electrical buildings is 25 m (82 ft) per OGAOM Sec. 9.6.15; distance between MCC and process equipment is 7.5 m per CEC. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 298, 306 |
| Package interfaces | Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | Workbook Packages row 40; Gate 7 `PACKAGE_REGISTER.csv` row PKG-038; Gate 7 `INTERFACE_REGISTER.csv` PKG-038 rows IFC-592E5CCFE2, IFC-EA9C0A8BD1, IFC-C7243E4F80, IFC-065DD9678E, IFC-8D5F57505E, IFC-33A55B6DBB, IFC-6F5BF129A3, IFC-F3F5DA500E, IFC-C4BE8B720F, IFC-B981842FD5, IFC-7D68588C25, IFC-846DEC98C2 |
| Package-specific exclusions | TBD; no package-specific exclusions stated in Gate 7 PKG-038 source material. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-038 |
| Equipment selection, sizing, and footprint | TBD; the accessible sources do not assign a specific MCC count, UPS count/rating, transformer ratings, panel schedule, building dimensions, weight, or footprint to PKG-038. | Workbook Packages row 40; Gate 7 PKG-038 rows; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` electrical buildings paragraphs |

## Construction

| Construction / integration topic | Scope-of-work treatment |
|---|---|
| EPC integration boundary | Include facility-level integration, tie-ins, constructability, procurement/construction coordination, and interface management; do not assign vendor package engineering, package design, vendor documentation, or physical equipment package supply to the EPC Integrator. |
| Utility Piping | Carry as an interface for piping services entering or leaving the electrical building envelope (e.g., HVAC, drain piping); specific tie-in scope is TBD pending detailed design. |
| Drain / Containment | Carry as an interface for building drains and any required containment under the elevated building; specifics TBD. |
| Electrical Power | Identify the package as a 600 V class electrical building tied into the 13.8 kV / step-down 600 V distribution backbone per the DBM; coordinate incoming cable trays and bottom-entry routing; detailed feeder sizing is TBD. |
| Grounding / Bonding | Carry grounding/bonding as an interface requiring EPC review and construction coordination for ground grid connections at two points, ground wells, and 5 A high-resistance grounding for the 600 V transformer per the DBM. |
| Area / Exterior Lighting | Carry exterior building lighting and area-lighting interfaces to the building; specifics TBD pending lighting design. |
| I&C / Control Cabling | Carry control and monitoring cabling between equipment housed in the building (PLC panels, MCCs, contactor panels) and field instrumentation; specific I/O is TBD. |
| Communications / Network | Carry communications/network interfaces consistent with the DBM network rack and Ethernet basis; specifics TBD. |
| Building HVAC / Services | Carry HVAC as an interface to the n+1 climate-controlled building basis per the DBM; building service piping/utilities specifics TBD. |
| Fire & Gas / Safety Systems | Carry fire and gas detection and life-safety system interfaces to the building; specifics TBD. |
| Maintenance Access | Carry maintenance access as an interface requiring layout, clearance, equipment-door sizing, and 7.5 m MCC-to-process equipment spacing per CEC; further clearances TBD. |
| Grading / Site Drainage / Spill Containment | Carry site grading and drainage interfaces around the elevated, pile-supported building; specifics TBD. |
| Structural / Foundations / Supports | Carry structural/support requirements as interface scope (pile foundations, elevated platform, bottom-entry trays beneath); package-specific loads, footprint, and support details are TBD pending vendor data. |

## References

- `_CONTEXT.md`, DEL-038-01 identity, scope, artifacts, objective context.
- `_DEPENDENCIES.md`, declared dependency state.
- `_REFERENCES.md`, Gate 7 source pointers and accessible source root.
- Gate 7 `PROJECT_DECOMP.md`, mandatory EPC anchor deliverable basis.
- Gate 7 `PACKAGE_REGISTER.csv`, row PKG-038.
- Gate 7 `DELIVERABLE_REGISTER.csv`, row DEL-038-01_scope-of-work.
- Gate 7 `ARTIFACT_REGISTER.csv`, rows ART-6F1522B9E8, ART-C01B3E1EDE, ART-C80EB8F110, ART-458B21AA61.
- Gate 7 `INTERFACE_REGISTER.csv`, PKG-038 rows (twelve interface facts).
- Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for DEL-038-01_scope-of-work.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages row 40.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis lines 2076, 2080, 2084, 2811-2816, 2911, 2917-2925, 2934-2937, 2943, 2959, 2971-2979, 2985, 2989, 298, 306.
- `_Sources/26020-Package_Requirements.docx`, package-specific PKG-038 clauses not parsed in this run (source-gap; see Missing in run record).
