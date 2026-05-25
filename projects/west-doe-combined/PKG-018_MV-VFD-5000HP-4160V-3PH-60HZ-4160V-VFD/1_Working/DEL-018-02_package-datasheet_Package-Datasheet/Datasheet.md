# Datasheet: DEL-018-02_package-datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-018-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-018` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD | Workbook Packages row 20; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 18 / row 20 | Workbook Packages row 20; `PACKAGE_REGISTER.csv` |
| WBS | 02 | Workbook Packages row 20; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-02-30-009 | Workbook Packages row 20; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 20; `_CONTEXT.md` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-018` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-018` |
| Package function | Medium-voltage Variable Frequency Drive package; per workbook identity, rated 5,000 HP / 4,160 V / 3-phase / 60 Hz, providing 4,160 V VFD output to an MV motor load. | Workbook Packages row 20 |
| Driven load (apparent intent) | ASSUMPTION: workbook identity (5,000 HP class, 4,160 V, starting VFD context) is consistent with MV starting/driving service for inlet/sales-gas compressor motors KM-2150 and KM-2250, for which Starting VFDs are explicitly required by SCA-001 VE #34. The package row does not name a tagged driven motor, so the assignment is not confirmed. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 324, 326, 752-760; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 893, 2955 |
| Motor / drive basis (source) | Inlet compressor motor basis in Comp_and_Liquids DBM: 4,000 V, 3-phase, 60 Hz, 3,878 kW / 5,200 hp, NEMA MG1 compliant, TEFC or WPII, Class F insulation with Class B rise, ~891 rpm 8-pole, continuous inverter duty, with starting VFD. Deepcut DBM further references 6,700 hp electric drive (TBD; unresolved legacy conflict against 7,000 hp). | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 324, 533; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 893 |
| Drive mode | Starting VFD with synchronous transfer to a normal-service bus after the motor reaches full speed (inlet/sales compressor application). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 893 |
| Source MCC voltage | 4.16 kV MCC serves large 4000 V motors including KM-2150 and KM-2250. VFD and soft-starter requirements for 4.16 kV motors are TBD per Deepcut DBM. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 752; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2957, 3088 |
| Capacitor bank constraint | Power-factor-correction capacitor banks shall not be installed on the MCC-8200 synchronous-transfer bus where VFDs are present (SCA-001 VE #37). Harmonic and reactive-power mitigation shall be determined by detailed electrical studies. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 756; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2955 |
| Speed / turndown reference | For acid-gas compressor service (separate package), driver basis cites 8-pole induction motor, 900 rpm on VFD at full speed, minimum 3:1 speed turndown by inverter. Applicability to PKG-018 driven load is TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 1004, 1027 |
| Hazardous-area marking | VFD-fed motors located in Zone 2 areas shall be marked accordingly and supplied with a temperature code lower than the temperature code specified on the area-classification drawing or fugitive-emissions study. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2961 |
| Voltage conflict (package title vs. motor basis) | CONFLICT: Workbook row 20 names PKG-018 as "5000HP, 4160V" / "4160V VFD". Source motor basis (Comp_and_Liquids DBM) describes 4,000 V / 5,200 hp inlet compressor motors served by a 4,160 V MCC. The exact MV VFD output rating, output-voltage class (4,000 V vs. 4,160 V), and HP basis (5,000 HP vs. 5,200 HP) for this package are not reconciled in accessible source. See Guidance Conflict Table CT-018-02-01. | Workbook Packages row 20; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 324, 752 |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-018 and must be represented in the package interface requirements matrix. | Workbook Packages row 20; `INTERFACE_REGISTER.csv` `IFC-81D9418AA1` |
| Grounding / Bonding | Interface fact applies to PKG-018; major electrical equipment shall be directly connected to the ground grid at two points. | Workbook Packages row 20; `INTERFACE_REGISTER.csv` `IFC-20754345F3`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` grounding paragraphs |
| I&C / Control Cabling | Interface fact applies to PKG-018; MCC tie includes EtherNet communication port to the plant PLC central control panel for data acquisition. | Workbook Packages row 20; `INTERFACE_REGISTER.csv` `IFC-EF82F842B4`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 754 |
| Communications / Network | Interface fact applies to PKG-018; Ethernet/PLC communication interface basis as above. | Workbook Packages row 20; `INTERFACE_REGISTER.csv` `IFC-DC83D04DC5` |
| Maintenance Access | Interface fact applies to PKG-018; cable tray and conduit routing shall not interfere with maintenance access. | Workbook Packages row 20; `INTERFACE_REGISTER.csv` `IFC-35F60961CA`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` cable tray paragraphs |
| Structural / Foundations / Supports | Interface fact applies to PKG-018; package-specific support basis is TBD pending vendor package data. | Workbook Packages row 20; `INTERFACE_REGISTER.csv` `IFC-87DE46369F` |
| Low-voltage power cable from VFD | Low-voltage power cable fed from VFDs shall be Copper TECK cable. (Applicability to MV VFD output cabling is TBD; cited as drive-related cable basis.) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 3013 |
| Harmonic / reactive mitigation | Harmonic and reactive-power mitigation shall be determined by detailed electrical studies. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 756 |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-018` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-018` |
| Installation location (probable) | Electrical buildings (prefabricated, modular, general-purpose area) may house medium-voltage VFDs as required by detailed design. PKG-018 location is not assigned in source; ASSUMPTION: housed within an electrical building near the 4.16 kV MCC. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2973 |
| Foundations / supports | Structural / foundations / supports interface applies; package-specific support basis is TBD. | Workbook Packages row 20; `INTERFACE_REGISTER.csv` `IFC-87DE46369F` |
| Cooling, enclosure rating, harmonic filters, isolation/bypass switchgear | TBD unless defined by vendor package data and detailed electrical design. | Source gap; `_Sources/26020-Package_Requirements.docx` not opened in this run (no PKG-018-specific slice extracted) |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-018-02_package-datasheet`.
- `PACKAGE_REGISTER.csv`, row `PKG-018`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-018-02_package-datasheet`.
- `INTERFACE_REGISTER.csv`, rows `IFC-81D9418AA1`, `IFC-20754345F3`, `IFC-EF82F842B4`, `IFC-DC83D04DC5`, `IFC-35F60961CA`, `IFC-87DE46369F` for `PKG-018`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-018-02_package-datasheet` (OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 20.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, inlet compressor motor and MV MCC source slices (lines 324, 326, 533, 744-760).
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MV motor, MCC, VFD, electrical buildings, hazardous-area, and cable basis source slices (lines 893, 1004, 1027, 2955-2973, 3013, 3088).
- `_Sources/26020-Package_Requirements.docx`, not opened in this run; no PKG-018-specific match extracted.
