# Datasheet: DEL-038-02_package-datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-038-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-038` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 600V ELECTRICAL BUILDING (820-1) | Workbook Packages row 40; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 38 / row 40 | Workbook Packages row 40; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 40; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-029 | Workbook Packages row 40; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 40; `_CONTEXT.md` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-038` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-038` |
| Package function | 600 V electrical building (prefabricated, modular) serving facility low-voltage distribution, motor control, and ancillary electrical loads at building identifier 820-1. | Workbook Packages row 40; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Building construction basis | Electrical buildings shall be prefabricated, modular buildings located in general purpose areas. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Possible housed equipment | As required by detailed design: 600 V MCCs; 120 V AC UPS systems with battery banks and distribution panels; 125 V DC UPS systems with battery banks and distribution panels; 600 V to 208/120 V distribution transformers and panelboards; 208/120 V contactor panels; plant PLC control panels; network racks. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Low-voltage service basis | 600 V, 3 phase, 3 wire, 60 Hz, high-resistance grounded with 5 A continuous resistor. Serves motors 3/4 hp to 250 hp with direct-on-line starting, lighting and utility distribution transformers, building heaters, and UPS systems larger than 10 kVA. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical services / voltage table |
| 600 V MCC basis | 600 V MCCs shall be traditional MCCs with electronic motor overload relays. 600 V VFDs shall be provided as part of the 600 V MCC lineup. Standalone 600 V VFDs are not allowed unless dedicated to large motors. 600 V SCR heater-control panels shall be provided in the electrical building to supply heaters requiring process temperature control; SCR panels shall be supplied by feeder breakers in the 600 V MCC. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Motor Control and Motor Specifications; SCR panel paragraph |
| HVAC basis | Electrical buildings shall be climate controlled with HVAC sized as an n + 1 system so the cooling system can tolerate failure or maintenance shutdown of one HVAC unit without affecting building heating and cooling. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Cable entry basis | Electrical buildings shall be designed for bottom entry of incoming and outgoing power cables. Buildings shall be elevated on piles to provide space beneath for MCC incoming cables in trays to the 600 V MCC main incoming section; outgoing cables to facility 600 V loads shall also be bottom entry. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Internal wiring basis | Electrical buildings shall be wired with TECK and ACIC cables. EMT conduit shall be used for equipment located adjacent to each other (e.g., control panels to contactor panels). An outdoor GFI receptacle shall be provided for exterior maintenance. Equipment doors shall be sized for, or include removable transom sections to allow, removal of the largest equipment. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Building heaters | Electric building heaters shall be provided as 600 V, 3 phase rated equipment. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Building Heaters section |
| Building identifier mapping for 820-1 | CONFLICT. Workbook row 40 names the package "600V ELECTRICAL BUILDING (820-1)". The DBM Electrical Buildings list identifies 820-1 as "6.9 kV Inlet / Sales Compressor Electrical Building" and identifies the 600 V buildings as 840-1, 850-1, and 860-1. See Guidance Conflict Table (HRR-038-02-001). | Workbook Packages row 40; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings list (lines 2811-2816) |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Utility Piping | Interface fact applies to PKG-038 and shall be represented in the package interface requirements matrix. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-592E5CCFE2` |
| Drain / Containment | Interface fact applies to PKG-038 and shall be represented in the package interface requirements matrix. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-EA9C0A8BD1` |
| Electrical Power | Interface fact applies to PKG-038 and shall be represented in the package interface requirements matrix. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-C7243E4F80` |
| Grounding / Bonding | Interface fact applies to PKG-038 and shall be represented in the package interface requirements matrix. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-065DD9678E` |
| Area / Exterior Lighting | Interface fact applies to PKG-038 and shall be represented in the package interface requirements matrix. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-8D5F57505E` |
| I&C / Control Cabling | Interface fact applies to PKG-038 and shall be represented in the package interface requirements matrix. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-33A55B6DBB` |
| Communications / Network | Interface fact applies to PKG-038 and shall be represented in the package interface requirements matrix. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-6F5BF129A3` |
| Building HVAC / Services | Interface fact applies to PKG-038 and shall be represented in the package interface requirements matrix. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-F3F5DA500E` |
| Fire & Gas / Safety Systems | Interface fact applies to PKG-038 and shall be represented in the package interface requirements matrix. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-C4BE8B720F` |
| Maintenance Access | Interface fact applies to PKG-038 and shall be represented in the package interface requirements matrix. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-B981842FD5` |
| Grading / Site Drainage / Spill Containment | Interface fact applies to PKG-038 and shall be represented in the package interface requirements matrix. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-7D68588C25` |
| Structural / Foundations / Supports | Interface fact applies to PKG-038 and shall be represented in the package interface requirements matrix. Buildings shall be elevated and installed on piles. | Workbook Packages row 40; `INTERFACE_REGISTER.csv` `IFC-846DEC98C2`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Grounding design basis | All major electrical equipment shall be directly connected to the ground grid at two points. Ground wells at power transformers or electrical buildings shall be provided for maintenance and operational testing. Each 600 V transformer shall be grounded by a 5 A continuous high-resistance grounding resistor; 600 V MCCs shall include power metering and ground/resistor fault detection. Ground-fault protection on 600 V systems shall be alarm-only to maintain continuity of operations. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Grounding and Bonding section |
| Cable / conduit routing | Cable tray routing shall not interfere with maintenance access. Conduit shall not interfere with maintenance access. Conduit shall be sealed where it crosses a change in area classification. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cable Tray and Conduit section |
| Area classification | Electrical buildings shall be located in general purpose areas. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Area classification paragraph |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering, design, vendor documentation, and physical equipment | Package Vendor responsibility. Electrical buildings shall be prefabricated, modular. | `PACKAGE_REGISTER.csv` row `PKG-038`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-038` |
| Foundations / supports | Buildings shall be elevated and installed on piles. Pipe racks and skids shall be welded to piles; additional bonding conductors from cable tray down to piles are not required. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings; Grounding and Bonding |
| Cable entry orientation | Bottom entry for incoming and outgoing cables, with space beneath the building for MCC incoming cable trays. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Shop fabrication scope | Shop-fabricated packages shall be wired using conduit and wire methods suitable for the area classification. Where a building is shop erected, lighting and other building electrical wiring shall be installed and wired to a junction box at skid edge. The DBM electrical buildings list identifies building 820-1 as a Shop-fabricated unit. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cable, Wire, and Raceways; electrical buildings list (line 2812) |
| Specific equipment count, ratings, sizing, and physical layout | TBD. The accessible source set does not provide PKG-038-specific quantities for MCCs, UPS, transformers, panels, or HVAC units; `26020-Package_Requirements.docx` has not been processed to extract a package-specific PKG-038 requirements slice. | Source gap; `_REFERENCES.md` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-038-02_package-datasheet`.
- `PACKAGE_REGISTER.csv`, row `PKG-038`.
- `ARTIFACT_REGISTER.csv`, checked for `DEL-038-02_package-datasheet`; no deliverable-local artifact rows are present in the accepted Gate 7 register.
- `INTERFACE_REGISTER.csv`, rows for `PKG-038` (twelve interface facts).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-038-02_package-datasheet`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 40.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices: low-voltage services, 600 V MCC and SCR control, Electrical Buildings, Grounding and Bonding, Cable Tray and Conduit, Building Heaters, and electrical buildings list.
- `_Sources/26020-Package_Requirements.docx`, no PKG-038-specific slice extracted in this run (source gap).
