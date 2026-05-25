# Datasheet: DEL-017-02_package-datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-017-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-017` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | MV VFD - 600HP, 4160V, 3PH, 60HZ - 4160V VFD | Workbook Packages row 19; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 17 / row 19 | Workbook Packages row 19; `PACKAGE_REGISTER.csv` |
| WBS | 02 | Workbook Packages row 19; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-02-30-008 | Workbook Packages row 19; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 19; `_CONTEXT.md` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-017` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-017` |
| Package function | Medium-voltage variable frequency drive (VFD) package, titled as a 600 HP, 4160 V, 3-phase, 60 Hz, 4160 V VFD. | Workbook Packages row 19 |
| Driven load | TBD. The package title implies a 600 HP application, but no accessible source slice identifies which facility motor or service this VFD drives. | Source gap; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` and `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` do not name a 600 HP MV VFD load. |
| Medium-voltage service basis | The facility medium-voltage service is 4,160 V, 3-phase, 3-wire, 60 Hz LRG and is identified as the bus for "process AC inverter-drive motors from 250 hp to 5,500 hp." | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical voltage and service table |
| MV VFD presence in facility electrical buildings | Electrical buildings may house medium-voltage VFDs together with 13.8 kV main switchgear, MV motor control centers, MV reduced-voltage soft starters, 600 V MCCs, UPS systems, distribution transformers, and panelboards. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Other documented VFD use in source set | DBM sources document "starting VFDs" for KM-2150 and KM-2250 inlet compressors (5,200 HP, 4,000 V class) under SCA-001 VE #34, and 600 V VFDs built into the 600 V MCC for low-voltage loads. Neither matches the 600 HP MV VFD title for `PKG-017`. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electric driver / starting basis and 4160V/600V MCC paragraphs |
| Rated motor HP | TBD. The package title carries "600HP," but no accessible source slice confirms VFD output rating, continuous/intermittent duty, starting basis, or motor data sheet linkage for this package. | Source gap; package-specific `26020-Package_Requirements.docx` slice not extracted to source root. |
| Rated input voltage | 4,160 V, 3-phase, 60 Hz (matches the documented MV service bus). | Workbook Packages row 19; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, MV service row |
| Rated output voltage | 4,160 V per package title; final voltage match to driven motor TBD pending motor data and detailed electrical study. | Workbook Packages row 19; source gap for confirmation |
| Harmonic and reactive-power mitigation | Harmonic and reactive-power mitigation shall be determined by detailed electrical studies. SCA-001 VE #37 removes capacitor banks from the synchronous bus on MCC-8200 where VFDs are present. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160V MCC and SCA-001 paragraphs |
| Standards alignment | NEMA MG1 motor compliance, Class F insulation with Class B rise, and continuous inverter-duty service basis is the documented motor pairing class for MV inverter-driven motors at the facility. Applicability to the specific PKG-017 driven motor is TBD pending motor-VFD pair confirmation. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electric driver basis |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-017 and must be represented in the package interface requirements matrix. | Workbook Packages row 19; `INTERFACE_REGISTER.csv` `IFC-5E50E5F700` |
| Grounding / Bonding | Interface fact applies to PKG-017 and must be represented in the package interface requirements matrix. | Workbook Packages row 19; `INTERFACE_REGISTER.csv` `IFC-1340C6D795` |
| I&C / Control Cabling | Interface fact applies to PKG-017 and must be represented in the package interface requirements matrix. | Workbook Packages row 19; `INTERFACE_REGISTER.csv` `IFC-6ECD9C92A1` |
| Communications / Network | Interface fact applies to PKG-017 and must be represented in the package interface requirements matrix. | Workbook Packages row 19; `INTERFACE_REGISTER.csv` `IFC-FB4034716A` |
| Maintenance Access | Interface fact applies to PKG-017 and must be represented in the package interface requirements matrix. | Workbook Packages row 19; `INTERFACE_REGISTER.csv` `IFC-A807F5E0B3` |
| Structural / Foundations / Supports | Interface fact applies to PKG-017 and must be represented in the package interface requirements matrix. | Workbook Packages row 19; `INTERFACE_REGISTER.csv` `IFC-34EB597147` |
| Grounding design basis | Major electrical equipment shall be directly connected to the ground grid at two points; distribution transformers, panelboards, and three-phase motors larger than 100 hp require separate copper ground conductors per CEC sizing. Applicability to this MV VFD package shall be confirmed by detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |
| Cable / conduit routing | Power circuits at 13.8 kV, 4,160 V, and 600 V shall be separated from control and instrument circuits by distance, shielding, or routing as required to minimize interference. Cable tray, conduit, grounding, and bonding shall comply with project electrical specifications and detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable and conduit paragraphs |
| Maintenance access | Cable tray and conduit routing shall not interfere with maintenance access. Physical placement of the MV VFD shall preserve maintenance clearances per detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray / maintenance paragraphs |
| Ambient design | Site basis carries a -40 deg C minimum ambient governing exposed equipment, package buildings, control panels, instrumentation, and field devices unless a more severe condition applies. Indoor electrical-building placement is the documented MV-VFD context. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, site basis paragraph; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-017` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-017` |
| Installation location | Likely indoor placement in a prefabricated, modular electrical building consistent with the documented MV-VFD housing context. Specific building/room assignment for `PKG-017` is TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Foundations / supports | Structural / Foundations / Supports interface applies; package-specific support basis (skid, anchor, seismic, equipment pad, isolation) is TBD pending vendor data and detailed design. | Workbook Packages row 19; `INTERFACE_REGISTER.csv` |
| Driven-motor identification, VFD output curve, control profile, harmonic filters, line/load reactors, output filter, cooling, enclosure rating | TBD unless defined by vendor package data and detailed design. | Source gap; `26020-Package_Requirements.docx` has no extracted PKG-017 package match in source root. |
| Communications / control integration | The MV electrical bus context establishes EtherNet communication to the plant PLC central control panel for data acquisition at the 4160V MCC; coordination of PKG-017 status, control, and protection signaling with the plant PLC is required at detailed design. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160V MCC paragraph |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-017-02_package-datasheet`.
- `PACKAGE_REGISTER.csv`, row `PKG-017`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-017-02_package-datasheet`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-017` (`IFC-5E50E5F700`, `IFC-1340C6D795`, `IFC-6ECD9C92A1`, `IFC-FB4034716A`, `IFC-A807F5E0B3`, `IFC-34EB597147`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-017-02_package-datasheet`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 19.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical voltage/service table, electric driver basis, 4160V MCC paragraph, SCA-001 paragraphs, and site basis.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph, grounding/bonding paragraphs, cable/conduit paragraphs.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific MV VFD content; no extracted PKG-017 match available in source root.
