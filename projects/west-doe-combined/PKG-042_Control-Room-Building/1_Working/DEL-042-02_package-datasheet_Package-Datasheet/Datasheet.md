# Datasheet — DEL-042-02 Package Datasheet (PKG-042 Control Room Building)

> Descriptive document. Source-anchored values only; missing values are `TBD`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-042-02_package-datasheet` | `_CONTEXT.md` |
| Name | Package Datasheet | `_CONTEXT.md` |
| ParentPackageID | `PKG-042` | `_CONTEXT.md` |
| Package | Control Room Building | `_CONTEXT.md` |
| Discipline | Electrical (with multi-discipline interfaces) | `_CONTEXT.md` (Discipline=Electrical); ASSUMPTION: multi-discipline interfaces required (controls, civil/structural, HVAC, F&G) based on building scope |
| Type | EPC Package Datasheet | `_CONTEXT.md` |
| ResponsibleParty | EPC Integrator | `_CONTEXT.md` |
| Covers Scope Items | `SOW-0043` | `_CONTEXT.md` |
| Supports Objectives | `OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010` | `_CONTEXT.md` (ASSUMPTION: package-grouping heuristic per skill default) |
| Decomposition Source | Workbook Packages row 44 | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 235 |

## Attributes

### Functional Role

| Attribute | Value | Source |
|---|---|---|
| Function | Central operations control room: house operator workstations, engineering workstations, primary controls servers, and core network switches | DBM-Deepcut `4-25_Deepcut_DBM.md` §controls (lines ~3119, 3141) |
| Operating Mode | Manned during operations; environment that limits need for physical interaction in the process facility | DBM-Deepcut §3119 |
| Primary Tenants | Operations personnel; engineering workstations; primary server hosts | DBM-Deepcut §3141, §3165 |

### Equipment Hosted (Initial Design Basis)

| Item | Quantity / Configuration | Source |
|---|---|---|
| Operator workstations | Three workstation sets (initial design basis); each workstation has four monitors in 2x2 arrangement; monitors ≥ 24 in, 1920x1080 minimum unless HMI requires otherwise | DBM-Deepcut §3184 |
| Engineering workstations | Present (count TBD) | DBM-Deepcut §3141 |
| Primary controls servers | Two physical servers, fault-tolerant, multiple VMs; primary host located in control room; secondary host in MCC (Deepcut) / low-voltage MCC room (Comp_and_Liquids) | DBM-Deepcut §3165; DBM-Comp_and_Liquids §796 |
| Core network switches | Present in control room | DBM-Deepcut §3141 |
| Operator workstation OS | Microsoft Windows; thin-client or thick-client (selection deferred to detailed design) | DBM-Deepcut §3184 |

### Building Envelope and Construction

| Attribute | Value | Source |
|---|---|---|
| Construction location | Install on site or modify if already existing (Office/Control Room Building) | DBM-Deepcut §2759 |
| Shop/Field designation | 800-1 Office/Control Building — Shop | DBM-Deepcut §2810 |
| Building wiring method | EMT permitted in non-process locations such as MCC buildings, control rooms, offices, warehouses; rigid conduit where building fabricated/erected in assembly shop before shipment | DBM-Deepcut §3025 |
| Minimum conduit size | 21 mm (3/4 in) | DBM-Deepcut §3025 |
| Electrical code compliance | Canadian Electrical Code (CEC) and applicable area classification | DBM-Deepcut §3025 |
| Building dimensions (L x W x H) | TBD | (no accessible source slice) |
| HVAC capacity | TBD | (no accessible source slice; ASSUMPTION: conditioned office environment required for IT/controls equipment) |
| Fire protection | TBD | location TBD; expected per facility F&G basis |

### Spacing / Siting

| Attribute | Value | Source |
|---|---|---|
| Spacing from pressurized bullets / process building | 15.24 m (50 ft) minimum | DBM-Deepcut §254 (API 2510) |
| Spacing from fired heater to control room / electrical buildings | 25 m (82 ft) minimum | DBM-Deepcut §298 (OGAOM Sec. 9.6.15) |
| Frost depth / live load for foundations | TBD | DBM-Deepcut §700 (foundations per final geotech report; building-specific values TBD) |

### Alarm and Indication Interfaces

| Attribute | Value | Source |
|---|---|---|
| Beacon group on control room exterior | Required; visual indication of facility alarm status | DBM-Deepcut §3262, §3293 |
| Audible horns | Co-located with beacon groups as part of facility alarm strategy | DBM-Deepcut §3262 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Area classification | Non-hazardous (general purpose) | ASSUMPTION based on DBM-Deepcut §3025 (EMT permitted in control rooms as non-process location) |
| Design ambient temperature range | TBD | location TBD |
| Snow / wind / seismic | Per project design basis; building-specific values TBD | DBM-Deepcut §700 (criteria invoked for building foundations) |
| Vibration / settlement constraints | Foundation design must address | DBM-Deepcut §700 |
| Operating staffing | Manned operations control room | DBM-Deepcut §3119 |

## Construction

| Item | Value | Source |
|---|---|---|
| Fabrication mode | Shop-fabricated (Building 800-1 designated "Shop") | DBM-Deepcut §2810 |
| Onsite work | Install on site or modify if existing | DBM-Deepcut §2759 |
| Foundation basis | Final geotechnical report; equipment-specific foundation/anchorage checks for control room | DBM-Deepcut §700 (Comp_and_Liquids) |
| Interface coordination | Area classification, ventilation, heating, emergency egress, F&G detection, ESD pushbutton placement, RIO panel locations, power distribution, maintenance access | DBM-Comp_and_Liquids §704 |
| Tie-ins to other systems | Home-run cabling, terminations, area lighting; potable/septic utilities | DBM-Comp_and_Liquids §75 |

## Interface Requirements Matrix (Initial)

| Interface | Counterpart | Requirement | Source |
|---|---|---|---|
| Controls network | Plant-wide controls/PLC network | Core switches in control room; redundant fault-tolerant servers | DBM-Deepcut §3141, §3165 |
| Secondary controls host | MCC / low-voltage MCC room | Secondary server hosted outside control room | DBM-Deepcut §3165; DBM-Comp_and_Liquids §796 |
| Packaged equipment monitoring | Each packaged unit | Process monitoring available at central control room | DBM-Deepcut §3121 |
| Alarm beaconing | Outdoor piperacks; building containing main BoP control PLCs; NGL storage; atm storage tank area | Beacon groups also on control room exterior | DBM-Deepcut §3262, §3293 |
| Power distribution | Plant electrical | TBD (loads, redundancy) | location TBD |
| HVAC | Building services | TBD | location TBD |
| F&G | Facility F&G system | TBD | location TBD |
| Telecom / security | Site IT/security | TBD | location TBD |
| Civil/structural | Foundations, grading | Final geotech report basis | DBM-Comp_and_Liquids §700 |

## References

- `_REFERENCES.md` (this deliverable)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
- `DELIVERABLE_REGISTER.csv` row 235 (Gate 7 snapshot)
- Workbook Packages row 44 (xlsx — not text-readable; values TBD)
- 26020-Package_Requirements.docx (not text-readable; values TBD)
- API 2510 (cited via DBM-Deepcut §254; location TBD)
- OGAOM Sec. 9.6.15 (cited via DBM-Deepcut §298; location TBD)
- Canadian Electrical Code (cited via DBM-Deepcut §3025; location TBD)
