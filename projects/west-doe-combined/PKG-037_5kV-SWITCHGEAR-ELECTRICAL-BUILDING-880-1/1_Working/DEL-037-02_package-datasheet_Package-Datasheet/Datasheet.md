# Datasheet: DEL-037-02_package-datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-037-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-037` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 5kV SWITCHGEAR ELECTRICAL BUILDING (880-1) | Workbook Packages row 39; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 37 / row 39 | Workbook Packages row 39; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` row `PKG-037` |
| CoA tracking number | 26020-01-30-028 | `PACKAGE_REGISTER.csv` row `PKG-037` |
| Discipline | Electrical | Workbook Packages row 39; `_CONTEXT.md` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-037` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package (electrical building containing switchgear). | `PACKAGE_REGISTER.csv` row `PKG-037` |
| Package function | Prefabricated electrical building (`880-1`) housing medium-voltage switchgear and associated electrical distribution equipment. | Workbook Packages row 39; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph |
| Switchgear voltage class | TBD. Package name carries "5kV" identifier; accessible DBM source slices identify 13.8 kV, 4.16 kV, and 600 V switchgear/MCC voltage classes and TECK cables "rated 5 kV with 100 percent insulation" associated with 4.16 kV medium-voltage cabling, but do not establish a discrete "5 kV" switchgear bus rating for the `880-1` building. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltage/service table and medium-voltage cable table |
| Building identifier `880-1` | TBD. DBM Electrical Buildings list enumerates `810-1` (13.8 kV), `820-1` (6.9 kV), `830-1` (4.16 kV), `840-1` (600 V), `850-1` (600 V), and `860-1` (600 V) buildings; `880-1` is not enumerated in the accessible source slice. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings building list |
| Building type | Prefabricated, modular building located in a general purpose area, designed for bottom entry of incoming and outgoing power cables, elevated and installed on piles. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraphs |
| Building HVAC | Climate-controlled with HVAC sized as an n + 1 system. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph |
| Internal equipment population | Electrical buildings may house, as required by detailed design, main switchgear, medium-voltage MCCs, MV reduced-voltage soft starters, MV VFDs, 600 V MCCs, 120 V AC and 125 V DC UPS systems with battery banks and distribution panels, 600 V to 208/120 V distribution transformers and panelboards, contactor panels, PLC control panels, and network racks; PKG-037 specific population is TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph |
| Cable system | TECK and ACIC cables; EMT conduit used between adjacent equipment such as control panels and contactor panels. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph |
| Outdoor service receptacle | GFI receptacle provided for exterior maintenance. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Utility Piping | Interface fact applies to PKG-037 and must be represented in the package interface requirements matrix. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-524BC4670F` |
| Drain / Containment | Interface fact applies to PKG-037 and must be represented in the package interface requirements matrix. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-A8DC0D3056` |
| Electrical Power | Interface fact applies to PKG-037 and must be represented in the package interface requirements matrix. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-35A170DE7F` |
| Grounding / Bonding | Interface fact applies to PKG-037 and must be represented in the package interface requirements matrix. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-E26DA604FB` |
| Area / Exterior Lighting | Interface fact applies to PKG-037 and must be represented in the package interface requirements matrix. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-8F0D1E29F1` |
| I&C / Control Cabling | Interface fact applies to PKG-037 and must be represented in the package interface requirements matrix. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-F5B78B59CE` |
| Communications / Network | Interface fact applies to PKG-037 and must be represented in the package interface requirements matrix. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-1ECBDB6397` |
| Building HVAC / Services | Interface fact applies to PKG-037 and must be represented in the package interface requirements matrix; HVAC sized n + 1. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-D6D4CB07AF`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph |
| Fire & Gas / Safety Systems | Interface fact applies to PKG-037 and must be represented in the package interface requirements matrix. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-4D8A22B2CA` |
| Maintenance Access | Interface fact applies to PKG-037; cable tray and conduit routing shall not interfere with maintenance access; doors shall be sized for (or include removable transom sections to allow) removal of the largest equipment. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-CE2AC83D1D`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray, conduit, and Electrical Buildings paragraphs |
| Grading / Site Drainage / Spill Containment | Interface fact applies to PKG-037 and must be represented in the package interface requirements matrix. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-65DF6F2E88` |
| Structural / Foundations / Supports | Interface fact applies to PKG-037; building shall be elevated and installed on piles to provide bottom-entry cable space. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-8012069CE2`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph |
| Grounding design basis | Major electrical equipment shall be directly connected to the ground grid at two points; ground wells at electrical buildings shall be provided for maintenance and operational testing with bolted ground connections at test points; above-grade ground conductors shall be green insulated in PVC conduit where mechanical protection is required and shall use compression-type connections. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |
| Area classification | Electrical buildings shall be located in general purpose (unclassified) areas. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, area classification / electrical buildings paragraph |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility (engineering, design, vendor documentation, physical equipment package). | `PACKAGE_REGISTER.csv` row `PKG-037` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-037` |
| Building construction | Prefabricated, modular electrical building, shop-fabricated; designed for bottom entry of incoming and outgoing power cables; elevated and installed on piles. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraphs and electrical buildings list (`Shop`) |
| Cabling / raceway | TECK and ACIC cables; EMT conduit between adjacent panels; bottom-entry cable arrangement; cable tray and conduit shall not interfere with maintenance access. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings, cable tray, and conduit paragraphs |
| Foundations / supports | Pile-supported elevated building structure consistent with interface `Structural / Foundations / Supports`. | Workbook Packages row 39; `INTERFACE_REGISTER.csv`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph |
| Installation location | TBD. DBM confirms electrical buildings are located in general purpose areas for convenient power distribution but does not assign building `880-1` to a specific area or coordinates. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph |
| Switchgear, MCC, UPS, transformer, panel, and network rack content | TBD per detailed design and vendor package data; the source enumerates allowable internal equipment classes but does not list a confirmed PKG-037 equipment population. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph; `26020-Package_Requirements.docx` had no accessible PKG-037 package match |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-037-02_package-datasheet`.
- `PACKAGE_REGISTER.csv`, row `PKG-037`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-037-02_package-datasheet`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-037` (twelve applicable interfaces).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-037-02_package-datasheet` (OBJ-001, OBJ-004 through OBJ-010).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 39.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices: voltage and service table, Electrical Buildings paragraphs, electrical buildings list, grounding and bonding paragraphs, cable tray, conduit, and area classification paragraphs.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, supporting electrical building, foundations, and building HVAC source slices.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific switchgear / electrical-building requirements; no PKG-037 match was found.
