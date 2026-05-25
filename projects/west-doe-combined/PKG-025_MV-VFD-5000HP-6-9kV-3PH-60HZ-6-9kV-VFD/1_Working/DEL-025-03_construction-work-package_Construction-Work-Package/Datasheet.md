# Datasheet: DEL-025-03_construction-work-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-025-03_construction-work-package` | `_CONTEXT.md` |
| Deliverable name | Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-025` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD | Workbook Packages row 27; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 25 / row 27 | Workbook Packages row 27; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 27; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-016 | Workbook Packages row 27; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 27; `_CONTEXT.md` |
| Deliverable type | EPC Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-025` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Construction scope role | EPC Integrator construction-facing deliverable for physically installing, building, inspecting, turning over, and tying the `PKG-025` MV VFD package into the larger facility systems. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-025-03_construction-work-package` |
| Artifact set | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist. | `_CONTEXT.md`; `ARTIFACT_REGISTER.csv` rows `ART-15E3B51A2A`, `ART-26C6F26015`, `ART-F23C60D66E` |
| Package class | Vendor-owned Electrical package installed by EPC construction scope. | `PACKAGE_REGISTER.csv` row `PKG-025` |
| Package function | Medium-voltage variable frequency drive package at 6.9 kV, 3-phase, 60 Hz, nominally rated for a 5000 HP driven load. | Workbook Packages row 27 |
| MV VFD service basis (for installation context) | DBM electrical basis identifies 6.9 kV, 3-phase, 3-wire, 60 Hz, low-resistance grounded medium-voltage services feeding facility AC inverter-drive motors rated 5,500 hp and above, with starting VFDs provided for the KM-2150/2250 Inlet/Sales Gas Compressor motors. The exact correspondence of `PKG-025` (workbook "5000HP") to the KM-2150/2250 starting-VFD scope is not stated explicitly and is carried as `ASSUMPTION` (directional only). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MV services table; MV MCC paragraph |
| Installation location | TBD. DBM states that electrical buildings may house medium-voltage VFDs but does not assign `PKG-025` to a specific building, room, skid, or outdoor location. The 820-1 6.9 kV Inlet/Sales Compressor Electrical Building is identified as MV-related infrastructure but is not bound to `PKG-025` in source. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph; 820-1 building list entry |
| Modularization basis | TBD. No package-specific modularization, shipping-split, prefab-skid, or self-framing-enclosure decision for `PKG-025` is recorded in accessible source material; DBM only notes that electrical buildings are prefabricated and modular. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph; source gap |
| Construction scope alignment | Civil and infrastructure include electrical buildings; construction scope includes electrical buildings, offloading/setting of modules, home-run cabling, terminations, and field interconnections. Applicability to `PKG-025` installation shall be confirmed by detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, construction scope and civil/infrastructure paragraphs |

## Conditions

| Interface / condition | Construction-facing basis | Source |
|---|---|---|
| Electrical Power | Applicable interface for `PKG-025`; installation must respect facility 6.9 kV medium-voltage feeder, distribution, and ground-grid interfaces. | Workbook Packages row 27; `INTERFACE_REGISTER.csv` `IFC-812CB082EA` |
| Grounding / Bonding | Applicable interface for `PKG-025`; major electrical equipment shall be directly connected to the ground grid at two points; each 6.9 kV transformer is grounded through a 100 A, 10 s neutral grounding resistor and operates as a tripping system; distribution transformers, panelboards, and three-phase motors larger than 100 hp require separate copper ground conductors per CEC sizing. Package-specific conductor sizes and tie-in points are TBD. | Workbook Packages row 27; `INTERFACE_REGISTER.csv` `IFC-3BE8D26B6B`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs |
| I&C / Control Cabling | Applicable interface for `PKG-025`; control cabling shall tie the VFD into the plant PLC central control panel via the MV MCC Ethernet communication port and applicable control loops. Package-specific cable schedules, control schematics, and I/O assignments are TBD. | Workbook Packages row 27; `INTERFACE_REGISTER.csv` `IFC-949E34ECEA`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 6.9 kV MCC paragraph |
| Communications / Network | Applicable interface for `PKG-025`; network connection from the MV MCC/VFD to the plant PLC central control panel uses an Ethernet communication port. Detailed network architecture, ports, and PRP/DLR alignment are TBD pending detailed design. | Workbook Packages row 27; `INTERFACE_REGISTER.csv` `IFC-EF46C006CC`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 6.9 kV MCC and remote I/O paragraphs |
| Maintenance Access | Applicable interface for `PKG-025`; cable tray, conduit routing, and equipment placement shall not interfere with maintenance access. Detailed clearances remain TBD. | Workbook Packages row 27; `INTERFACE_REGISTER.csv` `IFC-3A60522074`; DBM cable tray and conduit paragraphs |
| Structural / Foundations / Supports | Applicable interface for `PKG-025`; foundation, pile, settlement, frost protection, site preparation, and structural-support requirements shall be confirmed against the final geotechnical report. | Workbook Packages row 27; `INTERFACE_REGISTER.csv` `IFC-FB81FE736B`; DBM geotechnical paragraph |
| Construction sequencing | Construction work package shall align to the plot plan, equipment list, and construction work package register before issue for construction. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, miscellaneous facilities/issue-for-construction paragraph |
| Area classification / hazardous-area constraints | Outdoor pipe racks and general areas are non-hazardous unless detailed area classification drawings identify otherwise; VFD-fed motors located in Zone 2 areas shall be marked accordingly and supplied with a temperature code lower than the temperature code specified on the area-classification drawing or fugitive-emissions study. Installation methods, conduit sealing, and material selection shall respect the area classification assigned at detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, area classification and VFD/motor paragraphs |
| Climate / environmental basis | Roads and site-handling provisions shall accommodate the facility winter operation basis; installation method and material selection shall respect this basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, roads/environment paragraph |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package fabrication and supply | Package Vendor responsibility (vendor-owned Electrical package). | `PACKAGE_REGISTER.csv` row `PKG-025` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-025` |
| Construction work package artifact | Integrator-authored construction work package for physical installation, construction, and tie-in to larger systems. | `ARTIFACT_REGISTER.csv` row `ART-15E3B51A2A` |
| Installation and tie-in workface plan | Workface-planning evidence for installing/building the package and connecting it to adjacent process, utility, electrical, controls, civil, structural, and safety systems as applicable. | `ARTIFACT_REGISTER.csv` row `ART-26C6F26015` |
| Construction interface and turnover checklist | Construction-facing interface, tie-in, inspection, and turnover evidence for the approved package. | `ARTIFACT_REGISTER.csv` row `ART-F23C60D66E` |
| Civil / foundations / supports | Site grading, foundations, electrical buildings, pipe racks, and field interconnections are inside construction scope; package-specific foundation and support detail is TBD pending detailed design and geotechnical confirmation. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, civil/infrastructure and geotechnical paragraphs |
| Electrical installation work | Home-run cabling, terminations, and field interconnections fall inside construction scope. 6.9 kV medium-voltage cables are three-conductor copper TECK cable rated 8 kV with 100 percent insulation, shielded; low-voltage power cables fed from VFDs are copper TECK cable. Package-specific feeder routing, cable sizing, ground-conductor sizing, conduit, and termination details are TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MV cable and VFD-fed cable rows; construction scope summary |
| Controls / network tie-in | EPC construction scope shall pull and terminate I&C/control and communications/network cabling between the VFD/MV MCC and the plant PLC central control panel and associated remote I/O. Specific cable schedule, port assignments, and PRP/DLR alignment are TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 6.9 kV MCC and remote I/O paragraphs |
| Module set / hookup | Offloading and setting of modules and mechanical/electrical hookups are in construction scope. Package-specific shipping splits, lifting plans, and hookup steps for the MV VFD package are TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, construction scope summary |
| Inspection and test | Inspection scope shall confirm installation against the construction work package, the package interface requirements matrix, and vendor turnover documentation. Specific QA/QC checklists, ITPs, hold points, and any pre-energization MV testing (e.g., insulation resistance, hi-pot, phasing, grounding-resistor checks) are TBD pending vendor and EPC inspection plans. | Source gap; `_REFERENCES.md` |
| Turnover and acceptance | Construction interface and turnover checklist supports the downstream EPC Vendor Package Review and Acceptance (`DEL-025-06`). Turnover content depends on vendor document turnover (`DEL-025-05`) and package datasheet (`DEL-025-02`). | `DELIVERABLE_REGISTER.csv` rows `DEL-025-05`, `DEL-025-06`; `ARTIFACT_REGISTER.csv` row `ART-F23C60D66E` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-025-03_construction-work-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-025`.
- `ARTIFACT_REGISTER.csv`, rows `ART-15E3B51A2A`, `ART-26C6F26015`, `ART-F23C60D66E` for `DEL-025-03_construction-work-package`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-025` (`IFC-812CB082EA`, `IFC-3BE8D26B6B`, `IFC-949E34ECEA`, `IFC-EF46C006CC`, `IFC-3A60522074`, `IFC-FB81FE736B`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-025-03_construction-work-package` (OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 27.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, construction scope, civil/infrastructure, MV services table, 6.9 kV MCC, electrical buildings, grounding (including 100 A 10 s NGR for 6.9 kV transformers), cable tray, conduit, MV cable (TECK 8 kV), VFD-fed cable, area classification (Zone 2 VFD-fed motor marking), remote I/O network, geotechnical, and issue-for-construction source slices.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific MV VFD construction content; no `PKG-025`-specific match was found in the accessible package-requirements set.
