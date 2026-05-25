# Datasheet: DEL-036-04_vendor-engineered-equipment-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-036-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Engineered Equipment Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-036` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1) | Workbook Packages row 38; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 36 / row 38 | Workbook Packages row 38; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 38; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-027 | Workbook Packages row 38; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 38; `_CONTEXT.md` |
| Deliverable type | Vendor Package Production Unit | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-036` |
| Production-unit anchor inputs | EPC Scope of Work (`DEL-036-01`) and EPC Package Datasheet (`DEL-036-02`) | `DELIVERABLE_REGISTER.csv`; `_CONTEXT.md` Notes |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package; production-unit output is the vendor engineered physical equipment package and the vendor design basis/datasheet set. | `PACKAGE_REGISTER.csv` row `PKG-036`; `ARTIFACT_REGISTER.csv` rows `ART-5464B33F42`, `ART-4CFD465CF3` |
| Facility distribution context | Facility electrical backbone steps 25 kV utility down to a 13.8 kV main switchgear and radially distributes power through step-down transformers to medium-voltage electrical buildings including a "6.9 kV Inlet/Sales Compressor Electrical Building". | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, lines 2917-2925 |
| Medium-voltage service basis | 6.9 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded; serves facility process AC inverter-drive motors rated 5,500 hp and above. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2935 |
| Medium-voltage transformer grounding | Each 6.9 kV transformer shall be grounded using a 100 A, 10 s neutral grounding resistor operating as a tripping system. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2985 |
| Medium-voltage cable standard | 6.9 kV medium-voltage cables: three-conductor copper TECK rated 8 kV with 100 percent insulation; shielded. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 3008 |
| Electrical building services housed | Electrical buildings shall house, as required by detailed design, 13.8 kV main switchgear, medium-voltage MCCs, medium-voltage RVSS, medium-voltage VFDs, 600 V MCCs, 120 V AC UPS systems, 125 V DC UPS systems, distribution transformers and panelboards, contactor panels, plant PLC control panels, and network racks. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2973 |
| Electrical-building HVAC | Electrical buildings shall be climate controlled with HVAC sized as an n + 1 system so that one HVAC unit failure or maintenance does not affect heating/cooling. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2975 |
| Electrical-building cable entry | Designed for bottom entry of incoming and outgoing power cables; elevated and installed on piles to provide cable-tray space beneath. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2977 |
| Building 830-1 designation in source | DBM equipment list line 2813 records "830-1 4.16kV Acid Gas / Overheads Compressor Electrical Building", and line 2812 records "820-1 6.9kV Inlet / Sales Compressor Electrical Building". The package name combines a 6.9 kV qualifier with building number 830-1; the building-number-to-voltage assignment is therefore not source-consistent. See Conflict Table in `Guidance.md` (CT-036-04-001). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, lines 2811-2816 |
| Switchgear quantity reference | Source equipment list line 2880 records "Medium Voltage Switchgear" quantity 1 for the facility. Allocation of that single MV switchgear to PKG-036 is not confirmed by a package-specific source slice. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2880 |
| Vendor design basis content | Vendor package design basis and datasheet set; detailed rating, autonomy, panel schedules, and protection settings are source-specific where available. | `ARTIFACT_REGISTER.csv` row `ART-4CFD465CF3` |
| Detailed switchgear ratings (kA, BIL, bus rating, frame sizes, breakers, relays) | TBD. No package-specific 6.9 kV switchgear datasheet was located in accessible sources for PKG-036. | Source gap; `_Sources/26020-Package_Requirements.docx` was not parsed into a PKG-036-specific match |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Utility Piping | Interface fact applies to PKG-036 and must be represented in the package interface requirements matrix. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-9188C9FD26` |
| Drain / Containment | Interface fact applies to PKG-036 and must be represented in the package interface requirements matrix. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-628EF275F0` |
| Electrical Power | Interface fact applies to PKG-036 and must be represented in the package interface requirements matrix. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-3B6012818E` |
| Grounding / Bonding | Interface fact applies to PKG-036; major electrical equipment shall be directly connected to the ground grid at two points; distribution transformers, panelboards, and three-phase motors larger than 100 hp require separate copper ground conductors per CEC sizing. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-B6F77BBE8A`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs |
| Area / Exterior Lighting | Interface fact applies to PKG-036 and must be represented in the package interface requirements matrix. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-D49FB38D6F` |
| I&C / Control Cabling | Interface fact applies to PKG-036; MV protection/metering Ethernet ports tie back to plant PLC central control panels for data acquisition (DBM convention). | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-972B08F285`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2955 |
| Communications / Network | Interface fact applies to PKG-036 and must be represented in the package interface requirements matrix. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-349D2200D1` |
| Building HVAC / Services | n + 1 HVAC sizing applies to the electrical building housing this switchgear. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-C81A342112`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2975 |
| Fire & Gas / Safety Systems | Interface fact applies to PKG-036 and must be represented in the package interface requirements matrix. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-2C313DA749` |
| Maintenance Access | Cable tray and conduit routing shall not interfere with maintenance access. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-21B90D3691`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs |
| Grading / Site Drainage / Spill Containment | Interface fact applies to PKG-036 and must be represented in the package interface requirements matrix. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-DC7DB17C89` |
| Structural / Foundations / Supports | Interface fact applies to PKG-036; electrical buildings are elevated and installed on piles per DBM convention. | Workbook Packages row 38; `INTERFACE_REGISTER.csv` `IFC-BDE626F7DD`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2977 |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering, design, fabrication, and physical equipment | Package Vendor responsibility, performed against the EPC Scope of Work and EPC Package Datasheet. | `PACKAGE_REGISTER.csv` row `PKG-036`; `DELIVERABLE_REGISTER.csv` rows `DEL-036-01`, `DEL-036-02`, `DEL-036-04` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-036` |
| Installation location | Prefabricated, modular electrical building shop-built per source `Shop` row entries (lines 2811-2816). Specific building number assignment depends on resolution of CT-036-04-001. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, lines 2811-2816, 2971-2977 |
| Foundations / supports | Elevated, pile-supported electrical building with bottom-entry cable provisions. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2977 |
| Switchgear assembly (bus, breakers, relays, instrumentation, control wiring) | Vendor design responsibility; specific ratings, breaker frames, protection scheme, and Ethernet integration are TBD pending vendor datasheet and EPC Package Datasheet (`DEL-036-02`). | Source gap; `ARTIFACT_REGISTER.csv` row `ART-4CFD465CF3` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-036-04_vendor-engineered-equipment-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-036`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-036-04_vendor-engineered-equipment-package` (`ART-5464B33F42`, `ART-4CFD465CF3`).
- `INTERFACE_REGISTER.csv`, rows for `PKG-036`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, package-grouped objectives for `PKG-036` (recorded as ASSUMPTION per `PACKAGE_HEURISTIC`).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 38.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices for 6.9 kV service, medium-voltage cable, MV transformer grounding, electrical-building housing/HVAC/cable-entry, and equipment-list quantities.
- `_Sources/26020-Package_Requirements.docx`, no PKG-036 package-specific match parsed.
