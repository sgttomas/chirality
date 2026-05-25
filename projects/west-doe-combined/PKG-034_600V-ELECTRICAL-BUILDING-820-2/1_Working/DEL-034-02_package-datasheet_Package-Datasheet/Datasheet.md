# Datasheet: DEL-034-02_package-datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-034-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-034` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 600V ELECTRICAL BUILDING (820-2) | Workbook Packages row 36; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 34 / row 36 | Workbook Packages row 36; `PACKAGE_REGISTER.csv` |
| WBS | 02 | Workbook Packages row 36; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-02-30-025 | Workbook Packages row 36; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 36; `_CONTEXT.md` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-034` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-034` |
| Package function | 600 V electrical building (workbook tag 820-2) providing prefabricated modular housing for low-voltage electrical equipment serving the assigned facility area. | Workbook Packages row 36; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Building construction basis | Prefabricated, modular building located in a general-purpose area; climate controlled with HVAC sized as n+1 so that failure or maintenance shutdown of one HVAC unit does not affect building heating and cooling. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Cable entry | Bottom entry of incoming and outgoing power cables; building elevated and installed on piles to provide space beneath the building for MCC incoming cables running in trays to the 600 V MCC main incoming section; outgoing cables from 600 V MCCs to facility 600 V loads also bottom entry. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Internal wiring basis | Buildings shall be wired with TECK and ACIC cables. EMT conduit shall be used for equipment located adjacent to each other (e.g., control panels to contactor panels). An outdoor GFI receptacle shall be provided for exterior maintenance. Equipment doors shall be sized for, or include removable transom sections to allow, removal of the largest equipment. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Equipment that may be housed (as required by detailed design) | 600 V MCCs; 600 V to 208/120 V distribution transformers and panelboards; 208/120 V contactor panels; 120 V AC UPS systems with battery banks and distribution panels; 125 V DC UPS systems with battery banks and distribution panels; plant PLC control panels; network racks. Inclusion and quantity of any specific item in PKG-034 is to be confirmed by detailed design and vendor data. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Incoming power | 600 V class building supplied from upstream medium-voltage distribution through step-down transformer per facility radial distribution; precise feeder source, transformer rating, and bus configuration for PKG-034 are TBD pending detailed electrical studies and the project single-line for the 820-2 building. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical distribution section; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 600V MCC and Standby Power section |
| Standby power interface | Emergency power is supplied at the 600 V MCC level via low-voltage standby natural-gas generators with transfer switch. Transfer switch type, emergency bus configuration, generator count, rating, and load-shedding/critical-load list remain TBD. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 600V MCC and Standby Power section |
| Building location / area classification | TBD. DBM states electrical buildings shall be located in general-purpose areas; the specific location, plot coordinates, and final area classification for the 820-2 building are not assigned by accessible sources. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings and area-classification sections |
| 820-2 tag interpretation | The workbook tag "820-2" identifies a specific 600 V electrical building instance within the WBS 02 electrical scope. Accessible DBM source slices describe building tags 810-1, 820-1, 830-1, 840-1, 850-1, and 860-1 but do not separately enumerate a "820-2" building. Treat "820-2" as workbook-assigned identity only until source-supported building scope is confirmed. | Workbook Packages row 36; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-building enumeration |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Utility Piping | Interface fact applies to PKG-034 and must be represented in the package interface requirements matrix. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-FC0F34096E` |
| Drain / Containment | Interface fact applies to PKG-034 and must be represented in the package interface requirements matrix. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-E270A479B8` |
| Electrical Power | Interface fact applies to PKG-034 and must be represented in the package interface requirements matrix. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-0E87B7BCE6` |
| Grounding / Bonding | Interface fact applies to PKG-034 and must be represented in the package interface requirements matrix. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-46D2497CB7` |
| Area / Exterior Lighting | Interface fact applies to PKG-034 and must be represented in the package interface requirements matrix. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-63A70A25C3` |
| I&C / Control Cabling | Interface fact applies to PKG-034 and must be represented in the package interface requirements matrix. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-5EA9F4B39F` |
| Communications / Network | Interface fact applies to PKG-034 and must be represented in the package interface requirements matrix. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-1333B6962E` |
| Building HVAC / Services | Interface fact applies to PKG-034 and must be represented in the package interface requirements matrix. Building HVAC shall be sized n+1 per DBM electrical-building basis. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-DA391B1AF1`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Fire & Gas / Safety Systems | Interface fact applies to PKG-034 and must be represented in the package interface requirements matrix. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-94BF4E7C7C` |
| Maintenance Access | Interface fact applies to PKG-034. Cable tray and conduit routing shall not interfere with maintenance access; equipment doors shall be sized for, or include removable transom sections to allow, removal of the largest equipment. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-CAE509DDFA`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings and raceway sections |
| Grading / Site Drainage / Spill Containment | Interface fact applies to PKG-034 and must be represented in the package interface requirements matrix. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-7BD20E62E6` |
| Structural / Foundations / Supports | Interface fact applies to PKG-034. Foundations shall be designed for the final geotechnical report, equipment loads, snow/wind/seismic design criteria, frost protection, vibration, settlement, and maintenance access; electrical buildings require equipment-specific foundation and anchorage checks. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-EC6DF8B5D4`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, foundations section |
| Grounding design basis | Major electrical equipment shall be directly connected to the ground grid at two points. Ground wells at power transformers or electrical buildings shall be provided for maintenance and operational testing, with bolted ground connections at test points in the ground wells. Above-grade grounding conductors shall be green-insulated ground wires run in PVC conduit where mechanical protection is required; ground connections shall be compression type. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility (prefabricated modular building and its housed electrical equipment as assigned). | `PACKAGE_REGISTER.csv` row `PKG-034` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-034` |
| Installation location | TBD. DBM places electrical buildings in general-purpose areas but does not assign PKG-034 to specific plot coordinates. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Foundations / supports | Pile-elevated foundation per DBM electrical-building basis; loads, geotechnical parameters, and anchorage checks per detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, foundations section |
| Internal equipment list / ratings / quantities | TBD unless defined by vendor package data and detailed design. The accessible source set establishes equipment that may be housed but does not enumerate the as-built equipment list for PKG-034. | Source gap; `26020-Package_Requirements.docx` not confirmed to contain a PKG-034 / 820-2 package-specific match in this run |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-034-02_package-datasheet`.
- `PACKAGE_REGISTER.csv`, row `PKG-034`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-034-02_package-datasheet`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-034`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-034-02_package-datasheet`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 36.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices for electrical buildings, distribution, grounding/bonding, cable tray, conduit, and area classification.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 600V MCC and standby power, electrical-building, and foundations source slices.
- `_Sources/26020-Package_Requirements.docx`, searched for PKG-034 / 820-2 building-specific content; no confirmed package-specific match was located in this run.
