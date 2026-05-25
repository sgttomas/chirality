# Datasheet: DEL-023-03_construction-work-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-023-03_construction-work-package` | `_CONTEXT.md` |
| Deliverable name | Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-023` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD | Workbook Packages row 25; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 23 / row 25 | Workbook Packages row 25; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 25; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-014 | Workbook Packages row 25; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 25; `_CONTEXT.md` |
| Deliverable type | EPC Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-023` |
| Covers scope | `SOW-0024` | `_CONTEXT.md`; `SCOPE_LEDGER.csv` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-023` |
| Package function | Medium-voltage variable frequency drive at 1500 HP, 4160 V, 3-phase, 60 Hz (4160 V VFD) — package title carried as workbook spelling. | Workbook Packages row 25 |
| Facility voltage system applicable to 4160 V VFDs | 4.160 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded; serves facility process AC inverter-drive motors rated 250 hp up to 5,500 hp. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, medium-voltage services table |
| 4.16 kV motor starting basis | "VFD and soft-starter requirements for 4.16 kV motors are TBD." | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 4.16 kV MCC paragraph |
| Anticipated installation location | Electrical buildings may house medium-voltage VFDs as part of the electrical-building line-up; specific building/room/skid assignment is `TBD`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Field construction responsibility | Field construction is assigned to Tourmaline Oil Corporation, including grading, foundations, setting modules/equipment on foundations, mechanical hookup, electrical terminations, and field installation of home-run cables. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section |
| Tie-in coordination | Joint planning is required for tie-ins to existing or related facilities; tie-in timing shall be established as the project progresses. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section |
| Driven motor identity / load | `TBD`. No accessible source slice identifies the specific 1,500 hp motor or driven load that PKG-023 serves. | Source gap; `26020-Package_Requirements.docx` not opened for PKG-023 match in this run |
| VFD topology, harmonic filtering, output filtering | `TBD`. Source does not specify topology, isolation transformer, harmonic mitigation, or output filter requirements for the 1500 HP 4160 V VFD. | Source gap |

## Conditions

| Interface / condition | Construction-work-package basis | Source |
|---|---|---|
| Electrical Power | Applicable interface fact for `PKG-023`; construction shall provide tie-in to the 4.16 kV bus and home-run cabling to the VFD. | Workbook Packages row 25; `INTERFACE_REGISTER.csv` `IFC-2F6B2D3B80` |
| Grounding / Bonding | Applicable interface fact; major electrical equipment shall be directly connected to the ground grid at two points, with separate copper ground conductors per CEC sizing where applicable. Package-specific grounding details are subject to detailed design. | Workbook Packages row 25; `INTERFACE_REGISTER.csv` `IFC-CEF43B776E`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs |
| I&C / Control Cabling | Applicable interface fact; control cabling shall connect VFD control I/O to the plant control system. Specific signal lists are `TBD`. | Workbook Packages row 25; `INTERFACE_REGISTER.csv` `IFC-488756F914` |
| Communications / Network | Applicable interface fact; Ethernet/communications integration to plant PLC/network expected (analogous to MCC integration pattern). Specific protocol and port topology are `TBD`. | Workbook Packages row 25; `INTERFACE_REGISTER.csv` `IFC-FF4188D90D` |
| Maintenance Access | Applicable interface fact; cable tray and conduit routing shall not interfere with maintenance access; physical clearances shall preserve withdrawal and service envelope. | Workbook Packages row 25; `INTERFACE_REGISTER.csv` `IFC-38BEE3F6CC`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs |
| Structural / Foundations / Supports | Applicable interface fact; grading, piling, foundation work, setting equipment on foundations, and installation of miscellaneous structural supports are Tourmaline field construction scope. | Workbook Packages row 25; `INTERFACE_REGISTER.csv` `IFC-0AED039BBE`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section |
| Medium-voltage cable basis | 4.160 kV medium-voltage cables: three-conductor copper TECK cable rated 5 kV with 100 percent insulation. Low-voltage power cable fed from VFDs: copper TECK cable. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable schedule |
| Area classification | VFD-fed motors located in Zone 2 areas shall be marked accordingly and supplied with a temperature code lower than that on the area-classification drawing or fugitive-emissions study. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, motors / area classification paragraph |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-023` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-023` |
| Module / equipment shipping and off-load | Tourmaline field construction scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section |
| Setting equipment on foundations | Tourmaline field construction scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section |
| Mechanical hookup and structural supports | Tourmaline field construction scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section |
| Electrical terminations and home-run cables | Tourmaline field construction scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section |
| Tie-in to ISBL/OSBL interfaces | External interface responsibility to be confirmed per tie-in. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section |
| Local control station | A motor local control station shall be installed adjacent to each motor; default is Hand-Off-Auto or On-Off; hard-wired to the motor starter circuit by the field construction contractor (pattern applies where the VFD drives a motor with a local control requirement). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MCC / local control station paragraph |
| Construction interface and turnover checklist scope | Anticipated artifact per `_CONTEXT.md`; specific checklist content is `TBD` until vendor data and integration design are accepted. | `_CONTEXT.md` Anticipated Artifacts; `ARTIFACT_REGISTER.csv` |
| Lift plan, rigging, crane sizing | `TBD`. Source confirms equipment is set on foundations as field construction scope but does not give 1500 HP 4160 V VFD-specific lift weights or rigging plans. | Source gap |
| Commissioning and energization sequence | `TBD`. No source slice gives package-specific energization, motor solo run, or string-test sequence for this VFD. | Source gap |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-023-03_construction-work-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-023`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-023-03_construction-work-package`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-023` (`IFC-2F6B2D3B80`, `IFC-CEF43B776E`, `IFC-488756F914`, `IFC-FF4188D90D`, `IFC-38BEE3F6CC`, `IFC-0AED039BBE`).
- `OBJECTIVE_DELIVERABLE_MAP.csv` / `OBJECTIVE_REGISTER.csv`, supported objectives: `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010`.
- `SCOPE_LEDGER.csv`, `SOW-0024`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 25.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, source slices: medium-voltage services table, 4.16 kV MCC paragraph, electrical buildings paragraph, motors / area classification paragraph, cable schedule, cable tray and conduit paragraphs, grounding and bonding paragraphs, Construction Responsibility section.
- `_Sources/26020-Package_Requirements.docx`, not opened for PKG-023-specific match in this run; recorded as source gap.
