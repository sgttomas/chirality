# Datasheet: DEL-024-04_vendor-engineered-equipment-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-024-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Engineered Equipment Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-024` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD | Workbook Packages row 26; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 24 / row 26 | Workbook Packages row 26; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 26; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-015 | Workbook Packages row 26; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 26; `_CONTEXT.md` |
| Deliverable type | Vendor Package Production Unit | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (engineering / design / equipment) with EPC Integrator integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement / construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-024` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-024` |
| Package function | Medium-voltage variable frequency drive (MV VFD) sized at 2,000 HP, 4,160 V, 3-phase, 60 Hz, with 4,160 V output. | Workbook Packages row 26 (package name) |
| Driven motor service | TBD. Source materials do not identify the specific driven motor tag, service, or process unit allocated to PKG-024. The decomposition records the package only as a 2,000 HP MV VFD without naming a downstream motor. | Workbook Packages row 26; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Facility electrical context | Motors 100 hp and larger shall be fed from soft starters or VFDs as required by the process; larger motors on this facility shall be 4,000 V or 13.2 kV; "VFD and soft-starter requirements for 4.16 kV motors are TBD." | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Motor Control and Motor Specifications |
| Housing context | Electrical buildings shall be prefabricated, modular buildings located in general-purpose areas; they shall house, as required by detailed design, medium-voltage VFDs (among other equipment). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Area / classification | TBD. VFD-fed motors located in Zone 2 areas have temperature-code requirements; the area classification of the PKG-024 VFD itself is not asserted by source. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, motor specifications |
| Cabling basis (downstream) | Low-voltage power cable fed from VFDs shall be Copper TECK cable. Applicability to the 4,160 V output side is TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable table |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to `PKG-024` and must be represented in the package interface requirements matrix carried in `DEL-024-02_package-datasheet`. | `INTERFACE_REGISTER.csv` `IFC-68C5E24846`; Workbook Packages row 26 |
| Grounding / Bonding | Interface fact applies to `PKG-024`; major electrical equipment shall be directly connected to the ground grid at two points. Applicability to this VFD package shall be confirmed by detailed design. | `INTERFACE_REGISTER.csv` `IFC-F8A6E25E1C`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` grounding paragraphs |
| I&C / Control Cabling | Interface fact applies to `PKG-024`; control / data interface to the plant PLC and motor protection chain is required. | `INTERFACE_REGISTER.csv` `IFC-8062D6F881` |
| Communications / Network | Interface fact applies to `PKG-024`; Ethernet communication to plant PLC central control panel is the facility convention for MV motor control. | `INTERFACE_REGISTER.csv` `IFC-22E88310C9`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 4.16 kV MCC paragraph |
| Maintenance Access | Interface fact applies to `PKG-024`; cable tray and conduit routing shall not interfere with maintenance access. | `INTERFACE_REGISTER.csv` `IFC-DD889EF8E3`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray paragraphs |
| Structural / Foundations / Supports | Interface fact applies to `PKG-024`; package-specific support basis is TBD. | `INTERFACE_REGISTER.csv` `IFC-850A8082BB`; Workbook Packages row 26 |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering, design, fabrication / supply, and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-024`; `_CONTEXT.md` |
| Facility integration, interfaces, tie-ins, constructability, procurement / construction coordination | EPC Integrator responsibility (integration review only on this deliverable). | `PACKAGE_REGISTER.csv` row `PKG-024`; `_CONTEXT.md` |
| Drive topology, harmonic mitigation, output filter, bypass arrangement | TBD. Source material confirms only that 4.16 kV VFD/soft-starter requirements are TBD; no specific topology, filter, or bypass requirement is asserted for PKG-024. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, lines 2957 and 3088 |
| Cooling, enclosure, and environmental rating | TBD. Source confirms electrical buildings may house MV VFDs; standalone outdoor / skid-mounted vs. building-housed placement for PKG-024 is not asserted. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Installation location | TBD. No source slice assigns PKG-024 to a specific electrical building, room, skid, or outdoor location. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Vendor design basis and datasheet set | Anticipated artifact: vendor package design basis and datasheet set developed by the Package Vendor from the EPC Scope of Work (`DEL-024-01`) and EPC Package Datasheet (`DEL-024-02`). | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-024-04` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `_DEPENDENCIES.md`, declared upstream / downstream lists (none declared).
- `DELIVERABLE_REGISTER.csv`, row `DEL-024-04_vendor-engineered-equipment-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-024`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-024-01_scope-of-work` and `DEL-024-02_package-datasheet` (upstream EPC inputs).
- `INTERFACE_REGISTER.csv`, rows `IFC-68C5E24846`, `IFC-F8A6E25E1C`, `IFC-8062D6F881`, `IFC-22E88310C9`, `IFC-DD889EF8E3`, `IFC-850A8082BB` for `PKG-024`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows associating `DEL-024-04` to `OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010` (PACKAGE_HEURISTIC association; ASSUMPTION).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 26.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices for motor control / MV VFD context, electrical buildings, grounding, and cable.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific MV VFD content; no PKG-024 package match accessible.
