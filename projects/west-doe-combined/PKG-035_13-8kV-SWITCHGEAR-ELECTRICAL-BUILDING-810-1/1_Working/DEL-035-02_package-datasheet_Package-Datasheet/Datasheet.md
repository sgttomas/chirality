# Datasheet: DEL-035-02_package-datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-035-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-035` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 13.8kV SWITCHGEAR ELECTRICAL BUILDING (810-1) | Workbook Packages row 37; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 35 / row 37 | Workbook Packages row 37; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 37; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-026 | Workbook Packages row 37; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 37; `_CONTEXT.md` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-035` |
| Building tag | 810-1 13.8kV Switchgear Electrical Building (Shop-fabricated) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, building/module list (line 2811) |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-035` |
| Package function | Plant main power distribution center: 13.8 kV switchgear housed in a prefabricated, modular electrical building. The 13.8 kV switchgear shall be designed, purchased, and installed as the plant main power distribution center with sufficient capacity to distribute power to facility electrical buildings. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Power System section (lines 2917-2919); Electrical Buildings section (line 2973) |
| Bus voltage class | 13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded (medium-voltage facility backbone) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, System Voltages table (line 2934) |
| Source of incoming power | Fed from a 25 kV to 13.8 kV, 50 MVA utility-supplied transformer downstream of BC Hydro 25 kV (TBC) utility supply. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Power System (line 2917) |
| Bus sizing basis | The 13.8 kV switchgear bus shall be sized for the full facility scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Power System (line 2917) |
| Downstream distribution | Radial distribution through step-down transformers to: 6.9 kV Inlet/Sales Compressor Electrical Building; 4.16 kV Acid Gas/Overheads Compressor Electrical Building; 600 V Acid Gas Compressor Electrical Building; 600 V Sales/Overheads Compressor Electrical Building; 4.16 kV/600 V General Area/Tank Farm/Process Electrical Building. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Power System (lines 2919-2925) |
| Cross-facility distribution | Power distribution is shared between the 04-25 and 03-25 facilities; main power supply to 03-25 is sub-fed from the 04-25 13.8 kV Main Switchgear Electrical Building. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Power System (line 2927); `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 740 |
| Building construction | Prefabricated, modular electrical building located in a general purpose area, climate-controlled with n+1 HVAC, elevated on piles with bottom entry for incoming and outgoing power cables. Building shall be wired with TECK and ACIC cables; equipment doors sized for or with removable transoms for largest equipment removal. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings (lines 2973, 2975, 2977, 2979) |
| Building housed equipment scope | May house 13.8 kV main switchgear and, per detailed design, MV MCCs, MV reduced-voltage soft starters, MV VFDs, 600 V MCCs, 120 V AC UPS systems, 125 V DC UPS systems, 600 V to 208/120 V distribution transformers and panelboards, contactor panels, plant PLC control panels, and network racks. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings (line 2973) |
| Area classification | Electrical buildings shall be located in general purpose areas. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Area Classification (line 2911) |
| Standby power interface | Standby power for facility is supplied at the 600 V MCC level via TOU standby generators and transfer switches; the prior centralized 13.8 kV emergency-generator concept has been eliminated for this facility scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Standby Power (line 2943) |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Utility Piping | Interface fact applies to PKG-035 and must be represented in the package interface requirements matrix. | Workbook Packages row 37; `INTERFACE_REGISTER.csv` `IFC-C8A7133D59` |
| Drain / Containment | Interface fact applies to PKG-035 and must be represented in the package interface requirements matrix. | Workbook Packages row 37; `INTERFACE_REGISTER.csv` `IFC-231DB0CBFA` |
| Electrical Power | Interface fact applies to PKG-035 and must be represented in the package interface requirements matrix. | Workbook Packages row 37; `INTERFACE_REGISTER.csv` `IFC-A5EF521315` |
| Grounding / Bonding | Interface fact applies to PKG-035 and must be represented in the package interface requirements matrix. | Workbook Packages row 37; `INTERFACE_REGISTER.csv` `IFC-C11BBF56CD` |
| Area / Exterior Lighting | Interface fact applies to PKG-035 and must be represented in the package interface requirements matrix. | Workbook Packages row 37; `INTERFACE_REGISTER.csv` `IFC-EB2FA7BDE6` |
| I&C / Control Cabling | Interface fact applies to PKG-035 and must be represented in the package interface requirements matrix. | Workbook Packages row 37; `INTERFACE_REGISTER.csv` `IFC-9214AEAF28` |
| Communications / Network | Interface fact applies to PKG-035 and must be represented in the package interface requirements matrix. | Workbook Packages row 37; `INTERFACE_REGISTER.csv` `IFC-00317770B3` |
| Building HVAC / Services | Interface fact applies to PKG-035 and must be represented in the package interface requirements matrix. HVAC shall be sized n+1 so cooling can tolerate failure or maintenance of one unit without affecting building heating and cooling. | Workbook Packages row 37; `INTERFACE_REGISTER.csv` `IFC-73CF283A27`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2975 |
| Fire & Gas / Safety Systems | Interface fact applies to PKG-035 and must be represented in the package interface requirements matrix. | Workbook Packages row 37; `INTERFACE_REGISTER.csv` `IFC-C00E60F032` |
| Maintenance Access | Interface fact applies to PKG-035 and must be represented in the package interface requirements matrix. Cable tray and conduit routing shall not interfere with maintenance access. | Workbook Packages row 37; `INTERFACE_REGISTER.csv` `IFC-A3B2DADC44`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs |
| Grading / Site Drainage / Spill Containment | Interface fact applies to PKG-035 and must be represented in the package interface requirements matrix. | Workbook Packages row 37; `INTERFACE_REGISTER.csv` `IFC-589CAC7BC6` |
| Structural / Foundations / Supports | Interface fact applies to PKG-035 and must be represented in the package interface requirements matrix. Building shall be elevated and installed on piles to provide space beneath the building for bottom-entry incoming and outgoing cables. | Workbook Packages row 37; `INTERFACE_REGISTER.csv` `IFC-A5DBFBF436`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2977 |
| Grounding design basis | Major electrical equipment shall be directly connected to the ground grid at two points; ground wells at power transformers or electrical buildings shall be provided for maintenance and operational testing, with bolted ground connections at test points. Plant grounding uses driven piles as electrodes interconnected by a main #2/0 green insulated grounding conductor in the highest-voltage carrying tray. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Grounding and Bonding (lines 2987, 2989) |
| Cable specification | 13.8 kV medium-voltage cables shall be three-conductor copper TECK cable rated 15 kV with 133 percent insulation, shielded. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cable Specifications (line 3007) |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility (switchgear lineup and electrical building, including pre-installed equipment). | `PACKAGE_REGISTER.csv` row `PKG-035` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-035` |
| Fabrication mode | Shop-fabricated 810-1 electrical building. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2811 |
| Foundations / supports | Building shall be elevated and installed on piles; piles are also used as ground electrodes interconnected by the main grounding conductor. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, lines 2977, 2987 |
| Cable entry | Bottom entry of incoming and outgoing power cables; outgoing cables from 600 V MCCs to facility 600 V loads also bottom entry. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2977 |
| Internal wiring | Building wired with TECK and ACIC cables; EMT conduit used between adjacent equipment such as control panels to contactor panels; outdoor GFI receptacle for exterior maintenance. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2979 |
| Equipment access | Equipment doors sized for, or with removable transom sections to allow, removal of the largest equipment. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2979 |
| Switchgear sizing / one-line | Specific bus rating (A), short-circuit rating (kA), number of breakers, breaker types, metering, protective relaying scheme, and arc-flash mitigation strategy. | TBD. The DBM identifies sizing basis ("full facility scope") and need for relay coordination/arc-flash study (lines 2900-2902), but does not give numeric values. |
| Installation location | Specific plot-plan coordinates for the 810-1 electrical building. | TBD. DBM places electrical buildings in general purpose areas but does not provide plot-plan location for 810-1. |
| Detailed equipment population inside building | Final list and ratings of MV MCCs, soft starters, VFDs, 600 V MCCs, UPS systems, distribution transformers, panelboards, PLC panels, and network racks housed in this specific 810-1 building. | TBD. DBM enumerates equipment that electrical buildings may house "as required by detailed design" (line 2973). |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-035-02_package-datasheet`.
- `PACKAGE_REGISTER.csv`, row `PKG-035`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-035-02_package-datasheet`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-035` (12 applicable interface facts).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-035-02_package-datasheet` (OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010).
- `SCOPE_LEDGER.csv`, row `SOW-0036`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 37.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Power System, Standby Power, Electrical Buildings, Grounding and Bonding, Cable Specifications, Cable Tray and Conduit, and building/module list (line 2811) source slices.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, cross-facility 13.8 kV feed and electrical building source slices.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific 13.8 kV switchgear / 810-1 content; no PKG-035 detailed-requirements match accessible.
