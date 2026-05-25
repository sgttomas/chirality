# Datasheet: DEL-014-03_construction-work-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-014-03_construction-work-package` | `_CONTEXT.md` |
| Deliverable name | Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-014` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | CONTACTOR PANELS - LIGHTING / EXHAUST FAN CONTACTOR PANELS - LOW VOLTAGE | Workbook Packages row 16; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 14 / row 16 | Workbook Packages row 16; `PACKAGE_REGISTER.csv` |
| WBS | 02 | Workbook Packages row 16; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-02-30-005 | Workbook Packages row 16; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 16; `_CONTEXT.md` |
| Deliverable type | EPC Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-014` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-014` |
| Package function | Low-voltage contactor panels providing lighting and exhaust fan contactor control. | Workbook Packages row 16 |
| Construction responsibility (field) | Field construction (including electrical terminations, area lighting, home-run cabling, and installation of shipped-loose components) is in the Tourmaline field construction scope under the project DBM. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section |
| Lighting service basis | 120/208 V, 3 phase, 4 wire, 60 Hz solid grounded — serves lighting, receptacles, heat trace, small motors, and UPS 10 kVA or smaller. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, voltage/service table (line ~735) |
| Low-voltage service basis | 600 V, 3 phase, 3 wire, 60 Hz HRG with 5 A continuous resistor — serves motors 3/4 hp through 250 hp, DOL starting, lighting transformers, building heaters, and UPS larger than 10 kVA. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, voltage/service table (line ~734) |
| Exhaust fan controls interface | Building exhaust fan and heater controls may be supported by Remote I/O nodes at the nearest RIO panel. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Remote I/O paragraph (line ~804) |
| Package physical configuration (panel count, contactor rating, enclosure type, panel location) | TBD. No accessible source slice defines panel quantity, contactor ratings, panel construction (free-standing vs. wall-mount), enclosure NEMA/CEC rating, or assigned installation location for this package. | Source gap; `26020-Package_Requirements.docx` not parsed for a PKG-014 package match in this run |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-014 and must be reflected in construction tie-in scope. | Workbook Packages row 16; `INTERFACE_REGISTER.csv` `IFC-78CF31138D` |
| Grounding / Bonding | Interface fact applies to PKG-014. Major electrical equipment shall be directly connected to the ground grid at two points; distribution transformers, panelboards, and three-phase motors larger than 100 hp require separate copper ground conductors per CEC sizing. Applicability of specific items to this package shall be confirmed by detailed design. | Workbook Packages row 16; `INTERFACE_REGISTER.csv` `IFC-31C88BB424`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs |
| Area / Exterior Lighting | Area lighting installation is in field construction scope. Lighting service is 120/208 V solidly grounded. | Workbook Packages row 16; `INTERFACE_REGISTER.csv` `IFC-EF784327FA`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Construction Responsibility (line ~120) |
| I&C / Control Cabling | Control cabling for contactor panels and exhaust fan/heater controls must coordinate with Remote I/O panel placement and home-run cabling assignments. | Workbook Packages row 16; `INTERFACE_REGISTER.csv` `IFC-C715E9AA3E`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Remote I/O paragraph |
| Communications / Network | Network/communications interfaces required to support controls integration; specific protocol/topology TBD. | Workbook Packages row 16; `INTERFACE_REGISTER.csv` `IFC-2D60238809` |
| Maintenance Access | Cable tray and conduit routing shall not interfere with maintenance access. Panel clearances and operator access shall be preserved. | Workbook Packages row 16; `INTERFACE_REGISTER.csv` `IFC-52B07B0D36`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, cable tray/conduit paragraphs |
| Structural / Foundations / Supports | Foundations and structural supports for panels (free-standing) or wall/skid mounts shall be coordinated with civil/structural design. | Workbook Packages row 16; `INTERFACE_REGISTER.csv` `IFC-53646D26A1` |
| Site / environmental envelope | Site basis includes -40 deg C minimum ambient governing exposed equipment, package buildings, control panels, instrumentation, and field devices unless a more severe condition applies. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, site basis (line ~145) |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-014` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility, executed as Tourmaline field construction scope where applicable. | `PACKAGE_REGISTER.csv` row `PKG-014`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility |
| Off-loading, setting, and mechanical hookup | Off-loading and setting modules/equipment on foundations, mechanical hookup of equipment and interconnecting piping/cabling, and installation of shipped-loose components are in field construction scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility (lines ~111-115) |
| Field installation of home-run cables | Home-run cabling and electrical terminations are in field construction scope. Local control stations adjacent to motors are hard-wired back to the motor starter circuit in the MCC by the field construction contractor (analogous practice; specific applicability to this lighting/exhaust-fan contactor package TBD). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility (line ~118); `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 600V MCC paragraph (line ~760) |
| Area lighting installation | Area lighting is part of field construction scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility (line ~120) |
| Building / electrical-building integration | Electrical buildings may house MCCs, switchgear, and distribution equipment. Whether the PKG-014 contactor panels are housed in an electrical building or in field/exterior locations is TBD. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings paragraph (line ~766) |
| Inspection / commissioning / turnover | Turnover and acceptance evidence shall be captured per the package construction interface and turnover checklist artifact. Detailed inspection test plans, hold points, and turnover certificates are TBD pending construction execution planning. | `ARTIFACT_REGISTER.csv` rows `ART-46CD09710D`, `ART-497FADDF9B` |
| Demolition / removal of pre-existing infrastructure | Field construction scope where required by the project; PKG-014-specific demolition needs TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility (line ~125) |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-014-03_construction-work-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-014`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-014-03_construction-work-package` (`ART-6B7A89231D`, `ART-46CD09710D`, `ART-497FADDF9B`).
- `INTERFACE_REGISTER.csv`, rows for `PKG-014` (`IFC-78CF31138D`, `IFC-31C88BB424`, `IFC-EF784327FA`, `IFC-C715E9AA3E`, `IFC-2D60238809`, `IFC-52B07B0D36`, `IFC-53646D26A1`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-014-03_construction-work-package`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 16.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility, site basis, and electrical design basis source slices.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical voltage/service table, MCC, Remote I/O, electrical buildings, and cable tray/conduit source slices.
- `_Sources/26020-Package_Requirements.docx`, package-specific PKG-014 requirements: not parsed/matched during this run; content treated as gap.
