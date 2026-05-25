# Datasheet: DEL-039-02_package-datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-039-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-039` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 600V ELECTRICAL BUILDING (850-1) | Workbook Packages row 41; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 39 / row 41 | Workbook Packages row 41; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 41; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-030 | Workbook Packages row 41; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 41; `_CONTEXT.md` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-039` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-039` |
| Package function | 600 V electrical building serving the Inlet / Sales Compressor area (Building 850-1). | Workbook Packages row 41; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, building list row "850-1 600V Inlet / Sales Compressor Electrical Building" |
| Building type | Prefabricated, modular electrical building located in a general-purpose area; shop-erected with shop-installed building electrical wiring landed at skid-edge junction boxes. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings; Cable, Wire, and Raceways |
| Low-voltage service basis | 600 V, 3 phase, 3 wire, 60 Hz, high-resistance grounded with 5 A continuous resistor. Used for motors 3/4 hp through 250 hp with direct-on-line starting, lighting/utility distribution transformers, building heaters, and UPS systems larger than 10 kVA. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage and service table |
| Incoming feed | 600 V supply derived from step-down transformers fed radially from the 13.8 kV main switchgear; bottom-entry incoming cables on piles. The 850-1 building is one of the 600 V electrical buildings stationed across the facility. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 13.8 kV switchgear and Electrical Buildings paragraphs |
| Standby power interface | Standby power is provided by TOU low-voltage standby generators connected at the 600 V MCC level via transfer switches. Standby generator sizing, number of connection points, transfer-switch ratings, automatic vs manual transfer, paralleling, and load-shedding/sequencing are `TBD` pending electrical studies and TOU standard confirmation. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Standby Power |
| Housed equipment (as required by detailed design) | 600 V MCCs; 120 V AC UPS systems with battery banks and distribution panels; 125 V DC UPS systems with battery banks and distribution panels; 600 V to 208/120 V distribution transformers and panelboards; 208/120 V contactor panels; plant PLC control panels; network racks. Building-specific population is `TBD`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings |
| UPS service basis | 120 VAC / 125 VDC UPS services support the control system, selected emergency or critical lighting, MV breaker control circuits, and MV protective relays. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage and service table |
| HVAC | Climate-controlled, with HVAC sized as an n + 1 system so the cooling system can tolerate failure or maintenance shutdown of one HVAC unit without affecting building heating and cooling. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings |
| Building heat | Electric building heaters where heat-medium-type building heaters are not practical; MCC building heat and HVAC addressed by the electrical-building HVAC basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Heat Medium / Building Heat paragraph |
| Lighting | LED fixtures; MCC-room lighting uses flat-panel LED fixtures; emergency lighting using LED fixtures with battery backup, with at least two emergency fixtures per building. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Lighting and Receptacles |
| Receptacles | 120 V receptacles; UPS-fed 120 VAC receptacles identified in orange; outdoor receptacles fed from GFI breakers or integral-GFI devices; outdoor GFI receptacle for exterior maintenance. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Lighting and Receptacles; Electrical Buildings |
| Exterior color basis | Flashing/doors/trim: Cloverdale #2593 "Safety Green". Exterior walls and roof: galvanized metal with pre-painted trim. Interior walls: Bright White QC8783. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, building colors table |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Utility Piping | Interface fact applies to PKG-039; carried as evidence in the package interface requirements matrix. | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-A257E2C89C` |
| Drain / Containment | Interface fact applies to PKG-039. | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-5C80D8C3EC` |
| Electrical Power | Interface fact applies to PKG-039; 600 V building is fed via step-down transformer from 13.8 kV main switchgear. | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-C1DF6B8DD9`; DBM 13.8 kV switchgear paragraph |
| Grounding / Bonding | Interface fact applies to PKG-039; building grounding tied into facility ground grid with two-point connection for major equipment and ground wells at electrical buildings. | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-9653B84E14`; DBM Grounding and Bonding |
| Area / Exterior Lighting | Interface fact applies to PKG-039; exterior LED lighting per area-classification and light-pollution provisions. | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-4BC9BD20C1`; DBM Lighting and Receptacles |
| I&C / Control Cabling | Interface fact applies to PKG-039; ACIC instrumentation cabling and skid-edge termination provisions. | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-3F18DB0D3A`; DBM Cable, Wire, and Raceways |
| Communications / Network | Interface fact applies to PKG-039; field-run communications cables (Ethernet, ControlNet, DeviceNet, fiber, twisted pair) armored and rated for tray installation; network racks may be housed inside the building. | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-B95212AB85`; DBM Cable, Wire, and Raceways; Electrical Buildings |
| Building HVAC / Services | Interface fact applies to PKG-039; n + 1 HVAC sizing per DBM. | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-D8A8F7FEBC`; DBM Electrical Buildings |
| Fire & Gas / Safety Systems | Interface fact applies to PKG-039; package-specific fire-and-gas device population is `TBD` pending detailed design. | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-9C0AFE36A2` |
| Maintenance Access | Interface fact applies to PKG-039; cable tray and conduit routing shall not interfere with maintenance access; equipment doors sized for or with removable transoms for largest equipment. | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-D971A17948`; DBM Cable, Wire, and Raceways; Electrical Buildings |
| Grading / Site Drainage / Spill Containment | Interface fact applies to PKG-039; building is elevated on piles allowing space beneath for incoming cable trays; package-specific grading/spill containment basis is `TBD`. | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-50A5B3F280`; DBM Electrical Buildings |
| Structural / Foundations / Supports | Interface fact applies to PKG-039; building elevated and installed on piles with bottom-entry cable provisions; package-specific foundation design is `TBD`. | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-E3D0A5A836`; DBM Electrical Buildings |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-039` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-039` |
| Fabrication method | Prefabricated, modular shop-erected building; lighting and building electrical wiring installed in shop with wiring landed at a skid-edge junction box; bottom entry of incoming and outgoing power cables. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings; Cable, Wire, and Raceways |
| Installation location | Building 850-1 supports the 600 V Inlet / Sales Compressor area. Specific siting, orientation, and adjacent process equipment placement are `TBD` pending plot-plan confirmation. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, building list row 850-1 |
| Foundations / supports | Elevated on piles to provide space beneath the building for incoming 600 V MCC cable tray; CEC-compliant grounding to ground grid via two-point connection. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings; Grounding and Bonding |
| Internal raceway | EMT conduit may be used for equipment located adjacent to each other (e.g., control panels to contactor panels). Cable trays where used shall be ventilated/ladder type, Class E aluminum, sized for ≥30% future growth. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cable, Wire, and Raceways |
| Internal equipment population | 600 V MCC, 120 V AC and 125 V DC UPS systems, 600 V to 208/120 V distribution transformers and panelboards, 208/120 V contactor panels, PLC panels, network racks as required by detailed design. Specific lineup for 850-1 is `TBD`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-039-02_package-datasheet`.
- `PACKAGE_REGISTER.csv`, row `PKG-039`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-039-02_package-datasheet`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-039`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-039-02_package-datasheet`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 41.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices for low-voltage services, standby power, electrical buildings, grounding and bonding, cable/raceway, lighting, HVAC, and building list row 850-1.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific 600 V building requirements; no PKG-039 package-specific match identified during this run.
