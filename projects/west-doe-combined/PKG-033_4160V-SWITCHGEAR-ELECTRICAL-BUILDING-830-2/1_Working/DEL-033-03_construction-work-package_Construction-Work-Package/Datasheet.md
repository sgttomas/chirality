# Datasheet: DEL-033-03_construction-work-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-033-03_construction-work-package` | `_CONTEXT.md` |
| Deliverable name | Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-033` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 4160V SWITCHGEAR ELECTRICAL BUILDING (830-2) | Workbook Packages row 35; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 33 / row 35 | Workbook Packages row 35; `PACKAGE_REGISTER.csv` |
| WBS | 02 | Workbook Packages row 35; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-02-30-024 | Workbook Packages row 35; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 35; `_CONTEXT.md` |
| Deliverable type | EPC Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-033` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-033` |
| Package function | 4160 V (medium-voltage) switchgear and associated electrical building (designator 830-2). | Workbook Packages row 35; `PACKAGE_REGISTER.csv` |
| Construction work package purpose | Describe how the package will be physically installed, built, inspected, turned over, and tied into the larger facility systems. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-033-03_construction-work-package` |
| Medium-voltage service basis | 4.160 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded; serves facility process AC inverter-drive motors rated 250 hp up to 5,500 hp. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage and service table |
| Medium-voltage cable basis | 4.160 kV medium-voltage cables shall be three-conductor copper TECK cable rated 5 kV with 100 percent insulation. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable table |
| 4.16 kV motor starting | VFD and soft-starter requirements for 4.16 kV motors are TBD per the DBM source. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, motor starting table |
| Electrical building housing scope | Electrical buildings shall be prefabricated, modular buildings located in general purpose areas, and may house 13.8 kV main switchgear, MV MCCs, MV soft starters, MV VFDs, 600 V MCCs, 120 V AC and 125 V DC UPS systems with battery banks and distribution panels, distribution transformers, panelboards, contactor panels, plant PLC control panels, and network racks, as required by detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Building HVAC basis | Electrical buildings shall be climate controlled with HVAC sized as an n + 1 system so cooling can tolerate failure or maintenance shutdown of one HVAC unit. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Cable entry basis | Electrical buildings shall be designed for bottom entry of incoming and outgoing power cables; buildings shall be elevated on piles for cable tray access beneath. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| 830-2 building location / siting | TBD. Accessible DBM source slices reference an `830-1 4.16 kV Acid Gas / Overheads Compressor Electrical Building`, but do not separately confirm a 830-2 variant location, room layout, or process assignment for `PKG-033`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical building list; Workbook Packages row 35 |
| Detailed switchgear bus, breaker count, protection scheme | TBD pending vendor package data and detailed design. | Source gap; no `26020-Package_Requirements.docx` accessible package-specific PKG-033 match read for this run |
| Construction sequence / schedule windows | TBD pending project schedule and tie-in window confirmation. | Source gap |

## Conditions

| Interface / condition | Construction-package basis | Source |
|---|---|---|
| Utility Piping | Interface fact applies to `PKG-033`; construction package shall coordinate utility piping tie-ins. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-C55D5117E0` |
| Drain / Containment | Interface fact applies to `PKG-033`; construction package shall coordinate drains and containment around the electrical building. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-6D41E81E9D` |
| Electrical Power | Interface fact applies to `PKG-033`; construction package shall coordinate incoming and outgoing power tie-ins, including medium-voltage feeders. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-87E42C897B` |
| Grounding / Bonding | Interface fact applies. Major electrical equipment shall be directly connected to the ground grid at two points; ground wells at power transformers or electrical buildings shall be provided with bolted test connections. Above-grade grounding conductors shall be green insulated ground wires run in PVC conduit where mechanical protection is required; connections shall be compression type. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-68149F738F`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs |
| Area / Exterior Lighting | Interface fact applies; construction package shall coordinate area lighting integration around the building. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-DEF85D9CD6` |
| I&C / Control Cabling | Interface fact applies; construction package shall coordinate I&C and control cable terminations and tray entry. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-34A8619308` |
| Communications / Network | Interface fact applies; construction package shall coordinate plant network and communications cabling to PLC/network racks in the building. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-F6B851FF9C` |
| Building HVAC / Services | Interface fact applies; construction package shall coordinate HVAC commissioning per the n+1 building HVAC basis. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-F6FC5D19F9`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Fire & Gas / Safety Systems | Interface fact applies; construction package shall coordinate F&G detection, alarms, and life-safety tie-ins. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-BED07EB56D` |
| Maintenance Access | Interface fact applies; cable tray and conduit routing shall not interfere with maintenance access; equipment doors and removal access shall be preserved. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-73858A4A80`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs |
| Grading / Site Drainage / Spill Containment | Interface fact applies; construction package shall coordinate site grading and drainage around the elevated building. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-9AEF468935` |
| Structural / Foundations / Supports | Interface fact applies; building shall be elevated and installed on piles to allow bottom-entry cable trays beneath. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-D7C1CC054F`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Building delivery basis | Prefabricated modular electrical building per DBM; shop-fabricated and shipped per DBM electrical building list convention. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph; electrical building list table |
| Foundations and supports | Building shall be elevated on piles to allow bottom-entry cable tray access; package-specific pile design and foundation loads are TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph; `INTERFACE_REGISTER.csv` `IFC-D7C1CC054F` |
| Cable entry and tray routing | Bottom entry for incoming and outgoing power cables; cable tray and conduit routing shall preserve maintenance access. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings and cable tray paragraphs |
| Grounding and bonding installation | Two-point ground grid connection for major electrical equipment; ground wells provided at electrical buildings/transformers; compression-type ground connections; PVC-conducted above-grade ground wires where mechanical protection is required. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs |
| Wiring conventions | TECK and ACIC cables; EMT conduit between adjacent equipment such as control panels to contactor panels. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Receptacle | Outdoor GFI receptacle for exterior maintenance. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Equipment removal | Equipment doors sized for, or include removable transom sections to allow, removal of the largest equipment. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| HVAC commissioning | Confirm n+1 HVAC arrangement so loss of one HVAC unit does not affect building heating/cooling. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Tie-ins and turnover | Construction package shall include installation and tie-in workface plan and construction interface and turnover checklist (per anticipated artifacts). | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-033-03_construction-work-package` |
| Package vendor scope boundary | Vendor package engineering/design/equipment supply remains a Package Vendor responsibility and is not redefined by this construction work package. | `PACKAGE_REGISTER.csv` row `PKG-033` |
| Installation location confirmation | TBD. The DBM lists `830-1` electrical building variant but does not separately confirm a `830-2` variant location or process service assignment for this package. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical building list; Workbook Packages row 35 |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-033-03_construction-work-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-033`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-033-03_construction-work-package` (anticipated artifacts as listed in `_CONTEXT.md`).
- `INTERFACE_REGISTER.csv`, rows for `PKG-033` (twelve applicable interface facts).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-033-03_construction-work-package` (objectives OBJ-002, OBJ-004..OBJ-010 carried as package-grouped ASSUMPTION per heuristic).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 35.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices for medium-voltage service, electrical buildings, grounding, cable tray, conduit, and motor starting.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160V MCC / 4.16 kV service context source slices.
- `_Sources/26020-Package_Requirements.docx`, not searched for a PKG-033 package-specific match during this run; recorded as a source gap.
