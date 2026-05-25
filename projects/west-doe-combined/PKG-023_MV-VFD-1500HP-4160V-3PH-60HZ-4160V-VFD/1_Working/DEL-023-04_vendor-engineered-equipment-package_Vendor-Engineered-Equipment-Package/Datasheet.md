# Datasheet: DEL-023-04_vendor-engineered-equipment-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-023-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Engineered Equipment Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-023` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD | Workbook Packages row 25; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 23 / row 25 | Workbook Packages row 25; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 25; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-014 | Workbook Packages row 25; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 25; `_CONTEXT.md` |
| Deliverable type | Vendor Package Production Unit | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-023` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-023` |
| Package function | Medium-voltage variable frequency drive package — nominal motor service 1500 HP, 4160 V, 3-phase, 60 Hz, with 4160 V VFD output | Workbook Packages row 25 (package title) |
| Drive output voltage class | 4160 V (medium-voltage VFD output) | Workbook Packages row 25 (package title) |
| Driven-motor rating basis | 1500 HP, 4160 V, 3-phase, 60 Hz (per package title); detailed motor data, service class, duty, and starting/transient duty are TBD pending vendor selection and acceptable source slice. | Workbook Packages row 25; no detailed PKG-023 motor data slice located in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Driven service identity | TBD. The DBM's MV-VFD references (e.g., starting VFDs for KM-2150/2250 Inlet/Sales Gas Compressors; air-cooler fan VFDs; general 4.16 kV VFD requirements) do not explicitly bind to the PKG-023 1500 HP package; the DBM explicitly records `VFD and soft-starter requirements for 4.16 kV motors are TBD`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, lines 2957, 3088 |
| Supply-side bus / source | TBD. No PKG-023-specific feeder, switchgear assignment, or upstream bus slice is available. | Source gap; `26020-Package_Requirements.docx` not parsed for a PKG-023-specific match |
| Drive topology / harmonic mitigation | TBD. ASSUMPTION: a 4.16 kV class MV-VFD typically requires harmonic mitigation (multi-pulse transformer or active front end), but no PKG-023 source slice fixes the topology. | ASSUMPTION; no source slice |
| Cooling method | TBD pending vendor design. | Source gap |
| Enclosure / area classification | TBD. DBM notes VFD-fed motors located in Zone 2 areas shall be marked accordingly and supplied with a temperature code lower than that on the area-classification drawing; PKG-023's installation zone is not fixed. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2961 |
| Housing context | DBM allows medium-voltage VFDs to be housed in prefabricated, modular electrical buildings as required by detailed design; assignment for PKG-023 is TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2973 |
| Cable type to driven motor | DBM specifies copper TECK cable for low-voltage power cable fed from VFDs; medium-voltage VFD-fed motor cable type for 4.16 kV is not specified in the available slice and is TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 3013 |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface applies to PKG-023 and must appear in the vendor package interface basis. | `INTERFACE_REGISTER.csv` `IFC-2F6B2D3B80` |
| Grounding / Bonding | Interface applies to PKG-023. DBM grounding rules (major equipment connected at two points; separate copper ground per CEC for distribution transformers, panelboards, and three-phase motors >100 HP) are directionally applicable; package-specific basis confirmed at detailed design. | `INTERFACE_REGISTER.csv` `IFC-CEF43B776E`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding slice |
| I&C / Control Cabling | Interface applies to PKG-023; vendor package shall expose control I/O and signaling needed by plant control system. | `INTERFACE_REGISTER.csv` `IFC-488756F914` |
| Communications / Network | Interface applies to PKG-023. ASSUMPTION: by analogy with DBM's 6.9 kV MCC requirement for an Ethernet port to the plant PLC central control panel for data acquisition, the MV-VFD vendor package likely needs an equivalent communications interface; the PKG-023-specific requirement is TBD. | `INTERFACE_REGISTER.csv` `IFC-FF4188D90D`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2955 (analogy) |
| Maintenance Access | Interface applies to PKG-023. DBM general rule: cable tray and conduit routing shall not interfere with maintenance access. | `INTERFACE_REGISTER.csv` `IFC-38BEE3F6CC`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable/conduit slice |
| Structural / Foundations / Supports | Interface applies to PKG-023; vendor package shall define lifting, anchoring, and foundation loads for EPC integration. | `INTERFACE_REGISTER.csv` `IFC-0AED039BBE` |
| Hazardous-area marking | Where the PKG-023 VFD or VFD-fed motor is installed in a Zone 2 area, marking and temperature code shall conform to the DBM rule. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2961 |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering, design, fabrication/supply, and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-023`; `_CONTEXT.md` Scope |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility, with integration review of the vendor package. | `PACKAGE_REGISTER.csv` row `PKG-023`; `_CONTEXT.md` |
| Anchoring deliverables for vendor scope | Vendor scope is anchored by the EPC Scope of Work (`DEL-023-01`) and Package Datasheet (`DEL-023-02`). | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Installation location | TBD. DBM permits MV-VFDs in prefabricated electrical buildings as required by detailed design; PKG-023 placement is not fixed. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2973 |
| Foundations / supports | Structural / foundations / supports interface applies; vendor package shall provide load and anchorage data; package-specific loads are TBD. | `INTERFACE_REGISTER.csv` `IFC-0AED039BBE` |
| Vendor package deliverable set | Vendor engineered physical equipment package; vendor package design basis and datasheet set. | `ARTIFACT_REGISTER.csv` rows `ART-21EF7BEFD2`, `ART-B3660C159F` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-023-04_vendor-engineered-equipment-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-023`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-023-04_vendor-engineered-equipment-package`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-023` (`IFC-2F6B2D3B80`, `IFC-CEF43B776E`, `IFC-488756F914`, `IFC-FF4188D90D`, `IFC-38BEE3F6CC`, `IFC-0AED039BBE`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-023-04_vendor-engineered-equipment-package`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 25.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis slices: medium-voltage MCC/VFD/MV-soft-starter (lines 2955-2957), motor voltage classes and Zone 2 marking (line 2961), motor sizing and starting (line 2963), electrical buildings (line 2973), low-voltage VFD cable type (line 3013), 4.16 kV starting TBD (line 3088).
- `_Sources/26020-Package_Requirements.docx`, not parsed for a PKG-023-specific match; treat as deferred.
