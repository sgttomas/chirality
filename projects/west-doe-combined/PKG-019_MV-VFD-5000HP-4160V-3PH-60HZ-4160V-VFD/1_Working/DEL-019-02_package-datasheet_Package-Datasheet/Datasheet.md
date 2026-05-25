# Datasheet: DEL-019-02_package-datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-019-02_package-datasheet` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 97 |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 97 |
| Parent package | `PKG-019` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 21 |
| Package name | MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD | Workbook Packages row 21; `PACKAGE_REGISTER.csv` row 21 |
| Workbook ID / row | 19 / row 21 | Workbook Packages row 21; `PACKAGE_REGISTER.csv` row 21 |
| WBS | 02 | Workbook Packages row 21; `PACKAGE_REGISTER.csv` row 21 |
| CoA tracking number | 26020-02-30-009 | Workbook Packages row 21; `PACKAGE_REGISTER.csv` row 21 |
| Discipline | Electrical | Workbook Packages row 21; `_CONTEXT.md` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 97 |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 97 |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-019` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-019` |
| Package function | Medium-voltage variable frequency drive (VFD) package, 4160 V output class, sized at nominal 5000 HP, three-phase, 60 Hz. PROPOSAL: serves as a starting/operating VFD for a large MV motor in the Comp_and_Liquids facility scope. | Workbook Packages row 21 (package name); `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 324-326, 752-756 (VFD basis for MV inlet compressor motors) |
| Driven motor basis (per DBM) | Inlet compressor motors are 4,000 V, three-phase, 60 Hz, rated 3,878 kW / 5,200 hp, NEMA MG1 compliant, TEFC or WPII enclosure, Class F insulation with Class B rise, ~891 rpm 8-pole, continuous inverter-duty service, with a starting VFD. SCA-001 VE #34 governs the starting VFD basis (KM-2150 and KM-2250). | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 324-326, 533, 756 |
| Allocation of PKG-019 to specific motor tag | TBD. PKG-018 (workbook row 20) and PKG-019 (workbook row 21) both carry the identical package name "MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD" and identical CoA tracking number 26020-02-30-009. The DBM identifies two inlet-compressor VFDs (KM-2150 and KM-2250) requiring starting VFDs; the workbook-to-tag allocation between PKG-018 and PKG-019 is not stated in accessible sources. | `PACKAGE_REGISTER.csv` rows 20 and 21; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 326 |
| Voltage / horsepower nameplate (5000 HP, 4160 V) vs. DBM motor basis (5,200 hp, 4,000 V) | CONFLICT: Workbook package name states 5000 HP, 4160 V; accessible DBM source states 5,200 hp, 4,000 V for the driven MV inlet compressor motors. Authoritative reconciliation pending. | Workbook Packages row 21; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 324 |
| Service basis | Starting VFD for medium-voltage inlet compressor motor. Soft starts are not the current basis (SCA-001 VE #34). | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 326, 756 |
| MV source bus | 4160V MCC fed from a 13.8 kV to 4.16 kV, 12 MVA transformer; provides field-fused contactors, motor protection relays, EtherNet communication to plant PLC. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 744, 752-754 |
| Capacitor / harmonics interaction | SCA-001 VE #37 removes capacitor banks from the synchronous bus on MCC-8200 where VFDs are present. Harmonic and reactive-power mitigation to be determined by detailed electrical studies. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 756 |
| VFD sizing detail | ASSUMPTION: detailed VFD sizing is an electrical detailed-design item, not fixed by the workbook line item. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 326 |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-019; carried in the package interface requirements matrix. | Workbook Packages row 21; `INTERFACE_REGISTER.csv` `IFC-63D8BC58F2` |
| Grounding / Bonding | Interface fact applies to PKG-019; carried in the package interface requirements matrix. | Workbook Packages row 21; `INTERFACE_REGISTER.csv` `IFC-6119784E41` |
| I&C / Control Cabling | Interface fact applies to PKG-019; carried in the package interface requirements matrix. | Workbook Packages row 21; `INTERFACE_REGISTER.csv` `IFC-4C2D177FE7` |
| Communications / Network | Interface fact applies to PKG-019; EtherNet communication to plant PLC central control panel is identified for the 4160V MCC serving these motors. | Workbook Packages row 21; `INTERFACE_REGISTER.csv` `IFC-18DDF1CC28`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 754 |
| Maintenance Access | Interface fact applies to PKG-019; cable tray and conduit routing shall not interfere with maintenance access. | Workbook Packages row 21; `INTERFACE_REGISTER.csv` `IFC-031AC14F4D` |
| Structural / Foundations / Supports | Interface fact applies to PKG-019; package-specific support basis is TBD. | Workbook Packages row 21; `INTERFACE_REGISTER.csv` `IFC-FABC00F58B` |
| Exclusions / package-specific exclusions | TBD; no package-specific exclusions stated in source materials. | `PACKAGE_REGISTER.csv` row `PKG-019` |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-019` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-019` |
| Installation location | TBD. DBM identifies a 4160V MCC and MV inlet compressor motors but does not assign PKG-019 to a specific building, room, skid, or outdoor location. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 744-756 |
| Cooling, enclosure rating, ambient design | TBD; no package-specific environmental envelope is defined in accessible sources. | Source gap |
| Output filter, dv/dt or sine-wave filter, transformer arrangement | TBD; topology selection is a detailed-design / vendor decision. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 326 (sizing is detailed-design) |
| Harmonic mitigation provisions | TBD pending detailed electrical study under SCA-001 VE #37. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 756 |
| Package-requirements document mapping | TBD. No PKG-019-specific match was located in `_Sources/26020-Package_Requirements.docx` during this run. | Source gap |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` (row 21, `PKG-019`)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (row 97, `DEL-019-02_package-datasheet`)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/ARTIFACT_REGISTER.csv` (rows for `DEL-019-02_package-datasheet`: `ART-5A37F6237F`, `ART-80FE29D4E9`, `ART-0FE791170D`, interface-fact ART rows)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv` (`IFC-63D8BC58F2`, `IFC-6119784E41`, `IFC-4C2D177FE7`, `IFC-18DDF1CC28`, `IFC-031AC14F4D`, `IFC-FABC00F58B`)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (lines 324-326, 533, 744-760)
