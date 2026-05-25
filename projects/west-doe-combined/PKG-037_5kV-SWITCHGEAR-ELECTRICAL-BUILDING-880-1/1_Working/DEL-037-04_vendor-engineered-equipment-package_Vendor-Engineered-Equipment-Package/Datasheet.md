# Datasheet: DEL-037-04_vendor-engineered-equipment-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-037-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Engineered Equipment Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-037` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 5kV SWITCHGEAR ELECTRICAL BUILDING (880-1) | Workbook Packages row 39; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 37 / row 39 | Workbook Packages row 39; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` row `PKG-037` |
| CoA tracking number | 26020-01-30-028 | `PACKAGE_REGISTER.csv` row `PKG-037` |
| Discipline | Electrical | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| Deliverable type | Vendor Package Production Unit | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-037` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-037` |
| Package function | Prefabricated electrical building (880-1) housing medium-voltage switchgear and associated electrical equipment, engineered and supplied as a vendor package. | Workbook Packages row 39; `_CONTEXT.md` |
| Title voltage class | Package title designates "5kV" switchgear class. ASSUMPTION: this refers to the medium-voltage switchgear nameplate insulation class associated with 4.160 kV facility services per the DBM electrical voltage table; no source slice explicitly maps the workbook "5kV" label to a specific facility voltage for building 880-1. | Workbook Packages row 39; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltage and service table |
| Medium-voltage service basis | DBM defines medium-voltage services at 13.8 kV (facility backbone), 6.9 kV (process AC inverter-drive motors rated 5,500 hp and above), and 4.160 kV (process AC inverter-drive motors rated 250 hp up to 5,500 hp), all 3-phase, 3-wire, 60 Hz, low-resistance grounded. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltage and service table |
| Electrical building constituents | Electrical buildings may house, as required by detailed design: 13.8 kV main switchgear, medium-voltage motor control centers, medium-voltage reduced-voltage soft starters, medium-voltage VFDs, 600 V MCCs, 120 V AC UPS systems with battery banks and distribution panels, 125 V DC UPS systems with battery banks and distribution panels, 600 V to 208/120 V distribution transformers and panelboards, 208/120 V contactor panels, plant PLC control panels, and network racks. Vendor scope for PKG-037 shall include the building-specific subset confirmed by detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Building delivery mode | Prefabricated, modular electrical building located in a general-purpose area. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| UPS / control power interface | 120 VAC / 125 VDC UPS services support the control system, selected emergency or critical lighting, medium-voltage breaker control circuits, and medium-voltage protective relays. Vendor package shall accommodate UPS-fed breaker control and protective relay supply in accordance with detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, UPS services row |
| Medium-voltage cable basis (downstream of vendor switchgear) | 6.9 kV: three-conductor copper TECK cable rated 8 kV with 100 percent insulation, shielded. 4.160 kV: three-conductor copper TECK cable rated 5 kV with 100 percent insulation. Cable selection for circuits originating in this building shall conform to the DBM cable basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, medium-voltage cable table |
| Anticipated artifacts | Vendor engineered physical equipment package; vendor package design basis and datasheet set. | `_CONTEXT.md`; `ARTIFACT_REGISTER.csv` rows `ART-7491C7E69C`, `ART-8870C8E2DE` |

## Conditions

| Interface / condition | Datasheet basis | Source |
|---|---|---|
| Utility Piping | Interface fact applies to PKG-037 and must be represented in the package interface requirements matrix. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-524BC4670F` |
| Drain / Containment | Interface fact applies to PKG-037 and must be represented in the package interface requirements matrix. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-A8DC0D3056` |
| Electrical Power | Interface fact applies to PKG-037 and must be represented in the package interface requirements matrix. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-35A170DE7F` |
| Grounding / Bonding | Interface fact applies to PKG-037 and must be represented in the package interface requirements matrix. Major electrical equipment shall be directly connected to the ground grid at two points; distribution transformers, panelboards, and three-phase motors larger than 100 hp require separate copper ground conductors per CEC sizing. Applicability to the vendor switchgear lineup shall be confirmed by detailed design. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-E26DA604FB`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |
| Area / Exterior Lighting | Interface fact applies to PKG-037 and must be represented in the package interface requirements matrix. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-8F0D1E29F1` |
| I&C / Control Cabling | Interface fact applies to PKG-037 and must be represented in the package interface requirements matrix. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-F5B78B59CE` |
| Communications / Network | Interface fact applies to PKG-037 and must be represented in the package interface requirements matrix. Plant PLC control panels and network racks may be housed inside electrical buildings per the DBM electrical buildings paragraph. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-1ECBDB6397`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Building HVAC / Services | Interface fact applies to PKG-037 and must be represented in the package interface requirements matrix. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-D6D4CB07AF` |
| Fire & Gas / Safety Systems | Interface fact applies to PKG-037 and must be represented in the package interface requirements matrix. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-4D8A22B2CA` |
| Maintenance Access | Interface fact applies to PKG-037; cable tray and conduit routing shall not interfere with maintenance access. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-CE2AC83D1D`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs |
| Grading / Site Drainage / Spill Containment | Interface fact applies to PKG-037 and must be represented in the package interface requirements matrix. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-65DF6F2E88` |
| Structural / Foundations / Supports | Interface fact applies to PKG-037 and must be represented in the package interface requirements matrix. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-8012069CE2` |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering, design, fabrication / supply | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-037`; `_CONTEXT.md` |
| Building module | Prefabricated, modular electrical building per DBM electrical-buildings basis; shop-fabricated delivery is consistent with the DBM shop/field assembly convention for electrical buildings (e.g., 810-1, 820-1, 830-1, 840-1, 850-1, 860-1 are listed as shop). The 880-1 building is not explicitly listed in the DBM shop/field table; ASSUMPTION: shop-fabricated delivery applies. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, shop/field assembly table; electrical buildings paragraph |
| Switchgear lineup | Medium-voltage switchgear lineup engineered by the Package Vendor for the workbook-defined 5kV switchgear electrical building. Bus rating, breaker count, breaker frame, withdrawable / non-withdrawable arrangement, arc-flash mitigation, control voltage, and protective relay scheme are `TBD` pending vendor data and detailed design. | Workbook Packages row 39; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Facility integration, interfaces, tie-ins, constructability | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-037`; `_CONTEXT.md` |
| Installation location | `TBD`. Source materials do not assign building 880-1 to a specific plant location, foundation pad, or grading elevation. | Source gap |
| Foundations / supports | Structural / foundations / supports interface applies; package-specific support basis is `TBD` pending vendor module weight and footprint and EPC structural design. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-8012069CE2` |
| Vendor design basis and datasheet set | Vendor shall produce a package design basis and equipment datasheet set covering the building enclosure, switchgear lineup, auxiliary equipment, control power, grounding, lighting, HVAC, fire & gas, and cable terminations. | `ARTIFACT_REGISTER.csv` row `ART-8870C8E2DE` |
| Package-specific source slice | `26020-Package_Requirements.docx` was searched for package-specific switchgear / 880-1 / PKG-037 content; no accessible PKG-037 package match was found during this run. Package-specific requirements not in DBM remain `TBD`. | `_Sources/26020-Package_Requirements.docx`; source gap |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-037-04_vendor-engineered-equipment-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-037`.
- `ARTIFACT_REGISTER.csv`, rows `ART-7491C7E69C` and `ART-8870C8E2DE` for `DEL-037-04_vendor-engineered-equipment-package`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-037` (twelve interface types).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-037-04_vendor-engineered-equipment-package` (OBJ-001, OBJ-004–OBJ-010).
- `SCOPE_LEDGER.csv`, row `SOW-0038`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 39.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices for medium-voltage services, electrical buildings, UPS services, grounding, cable tray, conduit, and medium-voltage cables.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific 5kV switchgear / PKG-037 / 880-1 content; no match found.
