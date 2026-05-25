# Datasheet — DEL-025-04 Vendor Engineered Equipment Package (PKG-025 MV VFD)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-025-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable Name | Vendor Engineered Equipment Package | `_CONTEXT.md` |
| ParentPackageID | `PKG-025` | `_CONTEXT.md` |
| Package Name | MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD | PACKAGE_REGISTER.csv row PKG-025 |
| Discipline | Electrical | PACKAGE_REGISTER.csv row PKG-025 |
| WBS | 01 | PACKAGE_REGISTER.csv row PKG-025 |
| Deliverable Type | Vendor Package Production Unit | `_CONTEXT.md` |
| Responsible Party | Package Vendor (engineering/design/equipment); EPC Integrator integration review | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Covers Scope Items | SOW-0026 | `_CONTEXT.md` |
| Supports Objectives (PACKAGE_HEURISTIC, ASSUMPTION) | OBJ-001; OBJ-004; OBJ-005; OBJ-006; OBJ-008; OBJ-009; OBJ-010 | `_CONTEXT.md`; OBJECTIVE_DELIVERABLE_MAP.csv |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Functional role | Starting VFD for KM-2150/2250 Inlet/Sales Gas Compressor motors with synchronous transfer to a normal-service 6.9 kV bus after reaching full speed | DBM-Deepcut/4-25_Deepcut_DBM.md §"Motor Control and Motor Specifications" (line 2955); §Compression (line 893) |
| Driven equipment service | Inlet/Sales Gas Compressor motors (KM-2150, KM-2250) | DBM-Deepcut/4-25_Deepcut_DBM.md §2955 |
| Bus voltage class (output) | 6.9 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded | DBM-Deepcut/4-25_Deepcut_DBM.md System Voltages table (line 2935) |
| Application voltage policy | 6.9 kV medium-voltage services serve AC inverter-drive motors rated 5,500 hp and above | DBM-Deepcut/4-25_Deepcut_DBM.md line 2935 |
| Driven-motor nameplate horsepower | Title basis: 5000 HP (PACKAGE_REGISTER.csv row PKG-025). CONFLICT: DBM cites 6,700 hp current driver basis with unresolved 7,000 hp legacy (line 893; line 2196). Final motor rating TBD — see Guidance Conflict Table. | PACKAGE_REGISTER.csv; DBM lines 893, 1086, 2196 |
| Start method | Starting VFD with synchronous transfer to normal-service bus at full speed | DBM line 893; line 2955 |
| Bus arrangement | Connected through MCC-8200 6.9 kV motor control center; power-factor-correction capacitor banks shall NOT be installed on the MCC-8200 synchronous-transfer bus | DBM line 2955 |
| Quantity (units) | TBD (DBM identifies five Inlet/Sales Compressor units at line 2196; per-unit VFD allocation not stated for 5000HP package basis) | DBM line 2196 |
| Cable from VFD output | Copper TECK cable | DBM Cable Specifications table line 3013 |
| 6.9 kV medium-voltage cable basis | Three-conductor copper TECK cable rated 8 kV with 100 percent insulation; shielded | DBM line 3008 |
| Area classification accommodations | If VFD-fed motor is located in a Zone 2 area, motor shall be marked and supplied with a temperature code lower than the area-classification or fugitive-emissions study basis | DBM line 2961 |
| Housing | VFD housed in a prefabricated, modular medium-voltage electrical building (6.9 kV Inlet/Sales Compressor Electrical Building) | DBM lines 2921, 2973 |
| HVAC basis for housing | Climate-controlled, n+1 HVAC | DBM line 2975 |
| Communications | Ethernet communication port to plant PLC central control panel for data acquisition (applies to associated 6.9 kV MCC; VFD interface TBD) | DBM line 2955 |
| Grounding | 6.9 kV transformer system: 100 A, 10 s neutral grounding resistor, tripping system | DBM line 2985 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Frequency | 60 Hz | DBM line 2935 |
| Phases | 3-phase, 3-wire | DBM line 2935 |
| System grounding | Low-resistance grounded | DBM line 2935 |
| Building location | General purpose area, elevated on piles for bottom-entry cable runs | DBM lines 2973, 2977 |
| Ambient / climate | TBD (covered by building HVAC; outdoor design temperatures not extracted in source slice) | location TBD |
| Harmonic / power quality limits | TBD (not stated in accessible DBM slice) | location TBD |
| Synchronous transfer logic | Synchronous transfer to normal-service bus after motor reaches full speed | DBM line 893 |

## Construction

| Aspect | Basis | Source |
|---|---|---|
| Package boundary | Vendor-engineered physical equipment package, vendor package design basis and datasheet set | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv DEL-025-04 |
| Vendor scope | Package engineering, package design, fabrication/supply of physical equipment, vendor documentation | PACKAGE_REGISTER.csv row PKG-025 |
| EPC integration scope | Integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration | PACKAGE_REGISTER.csv row PKG-025 |
| Applicable interface types | Electrical Power; Grounding/Bonding; I&C/Control Cabling; Communications/Network; Maintenance Access; Structural/Foundations/Supports | PACKAGE_REGISTER.csv row PKG-025 |
| Shop-fabrication wiring basis | Shop-fabricated packages wired using conduit and wire methods suitable for area classification; control signals to skid-mounted remote I/O panels where applicable | DBM line 2997 |
| Removal access | Building equipment doors sized for (or include removable transom sections to allow) removal of largest equipment | DBM line 2979 |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- PACKAGE_REGISTER.csv (Gate 7 snapshot) row `PKG-025`
- DELIVERABLE_REGISTER.csv (Gate 7 snapshot) row `DEL-025-04_vendor-engineered-equipment-package`
- OBJECTIVE_DELIVERABLE_MAP.csv (Gate 7 snapshot)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (§Motor Control and Motor Specifications; §System Voltages; §Compression; §Electrical Buildings; §Cable Specifications; §Grounding and Bonding)
- `_Sources/26020-Package_Requirements.docx` — referenced but binary `.docx`; locally inaccessible as readable text. Vendor-facing package requirements content TBD pending text-extracted slice.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — referenced but binary `.xlsx`; locally inaccessible as readable text. Interface matrix content TBD.
