# Datasheet: DEL-024-03_construction-work-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-024-03_construction-work-package` | `_CONTEXT.md` |
| Deliverable name | Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-024` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD | Workbook Packages row 26; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 24 / row 26 | Workbook Packages row 26; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 26; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-015 | Workbook Packages row 26; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 26; `_CONTEXT.md` |
| Deliverable type | EPC Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-024` |
| Covers scope items | `SOW-0025` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supports objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION: package-grouping heuristic; objective-to-deliverable map associates by parent package) | `_CONTEXT.md`; `OBJECTIVE_DELIVERABLE_MAP.csv` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-024` |
| Package function | Medium-voltage (4.16 kV) variable frequency drive for a 2000 HP, 3-phase, 60 Hz motor application | Workbook Packages row 26; `PACKAGE_REGISTER.csv` |
| Field construction responsibility | Tourmaline Oil Corporation field construction scope: setting modules and equipment on foundations, mechanical hookup of modules and interconnecting piping, installation of shipped-loose instruments/valves/components, installation of miscellaneous structural supports, field installation of home-run cables, and electrical terminations. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section |
| Tie-in scope marker | Installation of interconnecting piping/cable to ISBL/OSBL tie-in points is flagged as an external interface responsibility marker; responsibility is to be confirmed for each tie-in. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section |
| 4.16 kV motor starting basis | VFD and soft-starter requirements for 4.16 kV motors are TBD in the DBM electrical section. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical section (4.16 kV MCC and motor starting paragraphs) |
| MV VFD housing context | Medium-voltage VFDs may be housed in prefabricated modular electrical buildings located in general purpose areas, as required by detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Construction phasing | One phase, single train, nominal 300 MMSCFD facility expansion | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction phasing field |

## Conditions

| Interface / condition | Construction-package basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-024; the construction work package shall include tie-in to MV feeder, electrical termination, and energization scope. | Workbook Packages row 26; `INTERFACE_REGISTER.csv` `IFC-68C5E24846` |
| Grounding / Bonding | Interface fact applies to PKG-024; the construction work package shall include connection to facility ground grid per DBM grounding basis (two-point grounding for major electrical equipment; separate copper ground conductors per CEC sizing for applicable equipment). | Workbook Packages row 26; `INTERFACE_REGISTER.csv` `IFC-F8A6E25E1C`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs |
| I&C / Control Cabling | Interface fact applies to PKG-024; construction shall include field installation of home-run control cables and terminations to the plant PLC / control system per DBM electrical/I&C basis. | Workbook Packages row 26; `INTERFACE_REGISTER.csv` `IFC-8062D6F881`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical/MCC paragraphs |
| Communications / Network | Interface fact applies to PKG-024; construction shall include Ethernet/network connection to the plant PLC for data acquisition (consistent with DBM MCC communication-port basis; applicability to this VFD package per detailed design). | Workbook Packages row 26; `INTERFACE_REGISTER.csv` `IFC-22E88310C9`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MCC Ethernet paragraphs |
| Maintenance Access | Interface fact applies to PKG-024; construction shall preserve maintenance access. Cable tray and conduit routing shall not interfere with maintenance access. | Workbook Packages row 26; `INTERFACE_REGISTER.csv` `IFC-DD889EF8E3`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs |
| Structural / Foundations / Supports | Interface fact applies to PKG-024; construction shall include grading/piling/foundation work (Tourmaline field scope) and setting of modules/equipment on foundations; package-specific support basis is TBD. | Workbook Packages row 26; `INTERFACE_REGISTER.csv` `IFC-850A8082BB`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section |
| Hazardous-area marking | VFD-fed motors in Zone 2 areas shall be marked accordingly and supplied with a temperature code lower than that specified on the area-classification drawing or fugitive-emissions study; applicability to this package's driven motor is TBD pending area classification. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, motor/VFD paragraphs |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility (out of EPC construction scope except interface). | `PACKAGE_REGISTER.csv` row `PKG-024` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-024` |
| Shipping and off-loading | Shipping of modules to site and off-loading of modules and equipment at site are Tourmaline field construction scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section |
| Setting equipment on foundations | Setting modules, pipe racks, and equipment on foundations is Tourmaline field construction scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section |
| Mechanical hookup | Mechanical hookup of modules, equipment, and interconnecting piping is Tourmaline field construction scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section |
| Installation of shipped-loose components | Installation of shipped-loose instruments, valves, and components is Tourmaline field construction scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section |
| Home-run cables and terminations | Field installation of home-run cables and electrical terminations is Tourmaline field construction scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section |
| Installation location | TBD. DBM source indicates MV VFDs may be housed in prefabricated electrical buildings but does not assign PKG-024 to a specific building, room, skid, or outdoor location. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Driven motor identification | TBD. The accessible source set does not unambiguously identify the specific 2000 HP, 4160 V motor application driven by this VFD; allocation requires confirmation. | Workbook Packages row 26; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, motor/VFD paragraphs |
| Tie-in points (ISBL/OSBL) | External interface responsibility marker; responsibility per tie-in is to be confirmed. Joint planning is required for tie-ins to existing or related facilities. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section |
| Turnover and inspection checklist content | TBD. The DBM does not contain a package-level turnover checklist template; package-specific inspection and turnover items shall be developed at detailed engineering with vendor input. | Source gap; `26020-Package_Requirements.docx` has no accessible PKG-024 match |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-024-03_construction-work-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-024`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-024` (`IFC-68C5E24846`, `IFC-F8A6E25E1C`, `IFC-8062D6F881`, `IFC-22E88310C9`, `IFC-DD889EF8E3`, `IFC-850A8082BB`).
- `ARTIFACT_REGISTER.csv`, rows for `DEL-024-03_construction-work-package`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, package-grouping heuristic mapping for `PKG-024`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 26.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section, electrical/MCC/VFD paragraphs, electrical buildings paragraph, grounding/bonding paragraphs, cable tray and conduit paragraphs.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific MV VFD construction content; no PKG-024 match found.
