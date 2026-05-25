# Datasheet: DEL-023-02_package-datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-023-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-023` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD | Workbook Packages row 25; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 23 / row 25 | Workbook Packages row 25; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 25; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-014 | Workbook Packages row 25; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 25; `_CONTEXT.md` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-023` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-023` |
| Package function | Medium-voltage variable frequency drive package, nominal 1500 hp at 4160 V, 3-phase, 60 Hz, with a 4160 V VFD output. | Workbook Packages row 25 (package title); `PACKAGE_REGISTER.csv` row `PKG-023` |
| Driven service / load | TBD. The DBM Electric Compressor Drivers inventory does not list a 1500 hp / 4160 V service; the specific driven equipment served by this MV VFD package is not identified by an accessible source slice. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Prime Mover and Major Driver Inventory section |
| Voltage class basis | The facility electrical basis assigns motors up to 250 hp to 575 V and larger motors to 4,000 V or 13.2 kV; VFD-fed motors in Zone 2 areas shall be marked accordingly and supplied with a temperature code lower than the area-classification temperature code. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltage levels and motor selection paragraphs |
| MV VFD requirements basis | The 4.16 kV MCC paragraph states "VFD and soft-starter requirements for 4.16 kV motors are TBD." Package-specific VFD topology, harmonic filtering, isolation transformer, bypass, and cooling are therefore TBD pending detailed electrical design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 4.16 kV motor control center paragraph; 4.16 kV motor starting table row |
| Starting / control method | TBD at the package level. The DBM identifies "Starting VFDs" only for the KM-2150/2250 Inlet/Sales Gas Compressor motors with synchronous transfer; whether the PKG-023 MV VFD is a starting VFD with transfer, a continuous-duty drive, or another topology is not stated in accessible source. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MCC-8200 / Starting VFD paragraphs |
| Housing / installation | Electrical buildings may house medium-voltage VFDs as required by detailed design. Building/room assignment for PKG-023 is not stated in the accessible source set. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| VFD-fed cable basis | Low-voltage power cable fed from VFDs is copper TECK cable. Cable basis for the 4.16 kV VFD output is not explicitly stated in the accessible source slice (MV cable type TBD). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable schedule paragraph |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-023 and must be represented in the package interface requirements matrix. | Workbook Packages row 25; `INTERFACE_REGISTER.csv` `IFC-2F6B2D3B80` |
| Grounding / Bonding | Interface fact applies to PKG-023 and must be represented in the package interface requirements matrix. Major electrical equipment shall be directly connected to the ground grid at two points; distribution transformers, panelboards, and three-phase motors larger than 100 hp require separate copper ground conductors per CEC sizing. | Workbook Packages row 25; `INTERFACE_REGISTER.csv` `IFC-CEF43B776E`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |
| I&C / Control Cabling | Interface fact applies to PKG-023 and must be represented in the package interface requirements matrix. | Workbook Packages row 25; `INTERFACE_REGISTER.csv` `IFC-488756F914` |
| Communications / Network | Interface fact applies to PKG-023; the MV MCC arrangement uses an Ethernet communication port to the plant PLC central control panel for data acquisition where applicable. | Workbook Packages row 25; `INTERFACE_REGISTER.csv` `IFC-FF4188D90D`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MCC communications paragraphs |
| Maintenance Access | Interface fact applies to PKG-023; cable tray and conduit routing shall not interfere with maintenance access. | Workbook Packages row 25; `INTERFACE_REGISTER.csv` `IFC-38BEE3F6CC`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs |
| Structural / Foundations / Supports | Interface fact applies to PKG-023 and must be represented in the package interface requirements matrix. | Workbook Packages row 25; `INTERFACE_REGISTER.csv` `IFC-0AED039BBE` |
| Anti-condensation heaters | Motors 100 hp and larger shall be fed from soft starters or VFDs as required by the process; anti-condensation space heaters shall be connected on motors greater than 100 hp for critical service. Applicability to the driven motor served by PKG-023 shall be confirmed at detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, motor selection and space-heater paragraphs |
| Area-classification marking | VFD-fed motors located in Zone 2 areas shall be marked accordingly and supplied with a temperature code lower than the area-classification temperature code. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, motor selection paragraph |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-023` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-023` |
| Installation location | TBD. The DBM allows MV VFDs to be housed in electrical buildings but does not assign PKG-023 to a specific building, room, skid, or outdoor location. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Foundations / supports | Structural / Foundations / Supports interface applies; package-specific support basis is TBD. | Workbook Packages row 25; `INTERFACE_REGISTER.csv` |
| Cooling, harmonic mitigation, isolation transformer, bypass | TBD; the DBM explicitly defers 4.16 kV VFD and soft-starter requirements to later detailed engineering. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 4.16 kV MCC and 4.16 kV motor starting paragraphs |
| Driven equipment make/model and final rating | TBD; no accessible source slice identifies the driven equipment served by this PKG-023 MV VFD or confirms a 1500 hp / 4160 V driven service in the major driver inventory. | Source gap; `26020-Package_Requirements.docx` searched, no PKG-023 package match accessed |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-023-02_package-datasheet`.
- `PACKAGE_REGISTER.csv`, row `PKG-023`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-023-02_package-datasheet`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-023` (`IFC-2F6B2D3B80`, `IFC-CEF43B776E`, `IFC-488756F914`, `IFC-FF4188D90D`, `IFC-38BEE3F6CC`, `IFC-0AED039BBE`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-023-02_package-datasheet`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 25.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices for MV motor voltage selection, 4.16 kV MCC, VFD/soft-starter requirements, Starting VFDs, electrical buildings, grounding/bonding, cable tray, conduit, motor space heaters, and VFD-fed motor area-classification marking.
- `_Sources/26020-Package_Requirements.docx`, searched for PKG-023 package-specific content; no PKG-023 match accessed during this run.
