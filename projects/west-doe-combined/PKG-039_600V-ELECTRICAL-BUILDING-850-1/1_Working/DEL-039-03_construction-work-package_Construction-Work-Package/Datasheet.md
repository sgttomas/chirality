# Datasheet: DEL-039-03_construction-work-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-039-03_construction-work-package` | `_CONTEXT.md` |
| Deliverable name | Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-039` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 600V ELECTRICAL BUILDING (850-1) | Workbook Packages row 41; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 39 / row 41 | Workbook Packages row 41; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 41; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-030 | Workbook Packages row 41; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 41; `_CONTEXT.md` |
| Deliverable type | EPC Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-039` |
| Scope of work covered | `SOW-0040` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supported objectives | OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (PACKAGE_HEURISTIC, ASSUMPTION) | `OBJECTIVE_DELIVERABLE_MAP.csv` rows for `DEL-039-03_construction-work-package` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package; facility integration by EPC Integrator | `PACKAGE_REGISTER.csv` row `PKG-039` |
| Package function | 600 V electrical building serving the 850-1 (Inlet/Sales Compressor) area | Workbook Packages row 41; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-building enumeration ("850-1 600V Inlet / Sales Compressor Electrical Building") |
| Building form | Prefabricated, modular electrical building located in a general-purpose area | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" paragraph |
| Equipment housed (as required by detailed design) | 600 V MCCs, 600 V to 208/120 V distribution transformers and panelboards, 208/120 V contactor panels, plant PLC control panels, network racks, 120 V AC UPS systems with battery banks and distribution panels, 125 V DC UPS systems with battery banks and distribution panels | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" paragraph |
| Building HVAC | Climate-controlled; HVAC sized as an n + 1 system so failure or maintenance of one HVAC unit does not affect building heating/cooling | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings HVAC sentence |
| Cable entry | Bottom entry for incoming and outgoing power cables; building elevated on piles to provide space for incoming/outgoing cable trays | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings cable-entry paragraph |
| Cable system basis | TECK and ACIC cables; EMT conduit between adjacent equipment (e.g., control panel to contactor panel); outdoor GFI receptacle for exterior maintenance; equipment doors sized for, or with removable transoms allowing, removal of the largest equipment | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings wiring paragraph |
| Field construction responsibility | Tourmaline field construction scope includes grading, piling, foundation work, field-erected buildings, shipping of modules to site, off-loading at site, setting modules on foundations, mechanical hookup, installation of shipped-loose items, structural supports, home-run cables, and electrical terminations | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Construction Responsibility" table |
| Tie-in joint planning | Joint planning is required for tie-ins to existing or related facilities; tie-in timing established as the project progresses | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, construction-responsibility paragraph |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Utility Piping | Interface fact applies to PKG-039 and must be represented in the construction tie-in/workface plan | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-A257E2C89C` |
| Drain / Containment | Interface fact applies to PKG-039 and must be represented in the construction tie-in/workface plan | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-5C80D8C3EC` |
| Electrical Power | Interface fact applies to PKG-039 and must be represented in the construction tie-in/workface plan | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-C1DF6B8DD9` |
| Grounding / Bonding | Major electrical equipment shall be directly connected to the ground grid at two points; ground wells at electrical buildings shall be provided for maintenance and operational testing with bolted ground connections at test points | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-9653B84E14`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraph |
| Area / Exterior Lighting | Area lighting is part of Tourmaline field construction scope; lighting tie-in to PKG-039 to be coordinated with construction package | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-4BC9BD20C1`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, construction-responsibility table |
| I&C / Control Cabling | Field installation of home-run cables is in Tourmaline construction scope; cable routing must preserve maintenance access | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-3F18DB0D3A`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, construction-responsibility table and cable-tray paragraph |
| Communications / Network | Network rack housing and communications tie-ins coordinated through the construction work package | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-B95212AB85`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings equipment list |
| Building HVAC / Services | Building HVAC tie-in coordinated as n + 1 system per DBM electrical-building basis | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-D8A8F7FEBC`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings HVAC sentence |
| Fire & Gas / Safety Systems | Interface fact applies to PKG-039; package-specific F&G/safety tie-in details to be confirmed by detailed design | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-9C0AFE36A2` |
| Maintenance Access | Cable tray and conduit routing shall not interfere with maintenance access; equipment doors sized for largest-equipment removal | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-D971A17948`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings doors paragraph |
| Grading / Site Drainage / Spill Containment | Grading, piling, and foundation work are Tourmaline field construction scope; spill containment around the building to be coordinated with civil scope | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-50A5B3F280`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, construction-responsibility table |
| Structural / Foundations / Supports | Building elevated and installed on piles; piling, foundation work, setting modules on foundations, and miscellaneous structural supports are Tourmaline field construction scope | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-E3D0A5A836`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings cable-entry paragraph and construction-responsibility table |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility | `PACKAGE_REGISTER.csv` row `PKG-039` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility | `PACKAGE_REGISTER.csv` row `PKG-039` |
| Site receiving and setting | Off-loading at site and setting the modular electrical building on foundations are Tourmaline field construction scope | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, construction-responsibility table |
| Mechanical hookup | Mechanical hookup of the modular electrical building and interconnecting piping is Tourmaline field construction scope | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, construction-responsibility table |
| Cable installation and termination | Field installation of home-run cables and electrical terminations are Tourmaline field construction scope; bottom-entry routing under elevated building | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, construction-responsibility table; electrical-buildings cable-entry paragraph |
| Inspection regime | Electrical materials and equipment shall be designed, fabricated, installed, tested, and inspected per applicable codes/standards and the inspection authority designated by Tourmaline Oil Corp. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical inspection paragraph |
| Construction-installation location | 850-1 area position (coordinates and plot reference) | TBD. Plot plan drawing CIV-235633-5002 is not available in the publication input package; coordinate-level layout is `TBD`. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, plot-plan gap paragraph |
| Turnover/commissioning detail | Package-specific turnover checklist content (mechanical completion criteria, test records, punch list closeout) | TBD. The accessible DBM source describes general installation/inspection responsibilities but does not provide a package-specific turnover checklist for PKG-039. |
| Detailed workface plan inputs | Vendor IFC drawings, lift plans, scaffolding plans, sequencing, manpower loading | TBD. No vendor data set is locally accessible for PKG-039; `26020-Package_Requirements.docx` had no PKG-039-specific extraction copied to the deliverable folder. |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-039-03_construction-work-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-039`.
- `ARTIFACT_REGISTER.csv`, rows `ART-298F584585`, `ART-93DCDB7068`, `ART-17C0FB26AE`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-039` (twelve interface facts, all marked `YES`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-039-03_construction-work-package` (OBJ-001, OBJ-004 through OBJ-010).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 41.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis (electrical-building configuration, cable basis, grounding, inspection) and Construction Responsibility table.
- `_Sources/26020-Package_Requirements.docx`, searched for PKG-039 construction-specific content; no accessible PKG-039 extraction copied to deliverable folder.
