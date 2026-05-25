# Datasheet: DEL-039-04_vendor-engineered-equipment-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-039-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Engineered Equipment Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-039` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 600V ELECTRICAL BUILDING (850-1) | Workbook Packages row 41; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 39 / row 41 | Workbook Packages row 41; `PACKAGE_REGISTER.csv` |
| WBS | per `PACKAGE_REGISTER.csv` row `PKG-039` | `PACKAGE_REGISTER.csv` |
| CoA tracking number | per `PACKAGE_REGISTER.csv` row `PKG-039` | `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 41; `_CONTEXT.md` |
| Deliverable type | Vendor Package Production Unit | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-039` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Production unit class | Vendor-owned Electrical package — engineering, design, fabrication/supply, and physical equipment package. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-039-04_vendor-engineered-equipment-package` |
| Package function | 600 V electrical building serving the Inlet / Sales Compressor area, building tag 850-1. | Workbook Packages row 41; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings list ("850-1 600V Inlet / Sales Compressor Electrical Building"). |
| Building class | Prefabricated, modular electrical building located in a general-purpose (unclassified) area. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" section and area-classification paragraph. |
| Building procurement basis | Shop-built building. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings table row "850-1 ... Shop". |
| Service voltage class (building backbone) | 600 V building distribution served from upstream switchgear / step-down transformers; building also distributes 208/120 V via 600 V to 208/120 V transformers and panelboards as required by detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings paragraph and power-distribution radial-feed list. |
| Incoming feeder source | Radial feed from upstream switchgear stepped down to 600 V; the DBM lists "600 V Sales/Overheads Compressor Electrical Building" as a destination of radial step-down feeds from the 13.8 kV switchgear backbone. Mapping of that DBM phrasing to building tag 850-1 (Inlet / Sales Compressor) is `ASSUMPTION` and confirmed by vendor data during package engineering. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, power-distribution paragraph |
| Building equipment population (as required by detailed design) | May house: 600 V MCCs (traditional MCCs with electronic motor overload relays); 600 V VFDs as part of the 600 V MCC lineup; 600 V SCR heater-control panels; 600 V to 208/120 V distribution transformers and panelboards; 208/120 V contactor panels; 120 V AC UPS systems with battery banks and distribution panels; 125 V DC UPS systems with battery banks and distribution panels; plant PLC control panels; network racks. Inclusion of medium-voltage gear is `TBD` for a 600 V building of this tag and is not asserted here. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" paragraph; 600 V MCC paragraphs |
| Standby power interface | Standby power is supplied via TOU standby generators connected at the 600 V MCC level through transfer switches. Generator sizing, transfer-switch configuration, load shedding, and sequencing remain EPC integration scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, standby-power paragraph |
| HVAC basis | Climate-controlled, HVAC sized as an n + 1 system so cooling can tolerate failure or maintenance shutdown of one HVAC unit without affecting building heating and cooling. Building heat by electric heaters (e.g., Ruffneck-type) where heat-medium heating is not practical. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, HVAC paragraph; building-heaters paragraph |
| Cable entry | Bottom entry of incoming and outgoing power cables; building elevated on piles to provide space beneath the building for MCC incoming cables running in trays to the 600 V MCC main incoming section. Outgoing cables from 600 V MCCs to facility 600 V loads are also bottom entry. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings cable-entry paragraph |
| Internal wiring | TECK and ACIC cables; EMT conduit for adjacent equipment such as control panels to contactor panels. An outdoor GFI receptacle is provided for exterior maintenance. Equipment doors are sized for (or include removable transom sections to allow) removal of the largest equipment. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings wiring paragraph |
| Vendor engineering inputs | EPC Scope of Work (`DEL-039-01`) and EPC Package Datasheet (`DEL-039-02`) form the vendor engineering basis. | `_CONTEXT.md`, Scope; `DELIVERABLE_REGISTER.csv` rows `DEL-039-01_scope-of-work`, `DEL-039-02_package-datasheet` |
| Vendor engineering outputs | Vendor engineered physical equipment package (the shop-built modular building, complete with internal equipment, wiring, HVAC, and lighting per the design basis); vendor package design basis and datasheet set. | `_CONTEXT.md`, Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-039-04` |
| Detailed equipment count / ratings | `TBD`. No package-specific equipment list, MCC sizing, transformer rating, UPS rating, VFD list, or PLC/network rack count is confirmed for `PKG-039` by an accessible source slice; the vendor shall resolve these in vendor data during package engineering. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings paragraph |
| Installation location coordinate | `TBD`. Source confirms electrical buildings shall be located in general-purpose areas, but no PKG-039 site-coordinate, plot-plan, or elevation assignment is available. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, area-classification paragraph |

## Conditions

| Interface / condition | Vendor package basis | Source |
|---|---|---|
| Utility Piping | Vendor building shall accommodate the EPC-defined Utility Piping interface (utility services entering or leaving the building envelope, e.g., utility water/air where required by detailed design). | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-A257E2C89C` |
| Drain / Containment | Vendor building drain and any required containment provisions shall be coordinated with the EPC-defined Drain / Containment interface. | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-5C80D8C3EC` |
| Electrical Power | Vendor building shall be engineered to the EPC-defined Electrical Power interface (incoming 600 V feeder from upstream switchgear via step-down transformer; outgoing 600 V feeders to facility loads). Cable entry shall be bottom entry per DBM. | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-C1DF6B8DD9`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings cable-entry paragraph |
| Grounding / Bonding | Vendor building grounding system shall be engineered to the EPC-defined Grounding / Bonding interface. Major equipment shall be directly connected to the ground grid at two points; distribution transformers, panelboards, and three-phase motors larger than 100 hp require separate copper ground conductors per CEC sizing where applicable. | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-9653B84E14`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |
| Area / Exterior Lighting | Vendor scope of exterior building lighting and receptacles shall be coordinated with the EPC-defined Area / Exterior Lighting interface. An outdoor GFI receptacle is provided for exterior maintenance per DBM. | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-4BC9BD20C1`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings wiring paragraph |
| I&C / Control Cabling | Vendor building shall accommodate the EPC-defined I&C / Control Cabling interface (hard-wired motor local control stations to MCC starter circuits; control cabling to plant PLC control panels and contactor panels housed in the building). | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-3F18DB0D3A`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 600 V MCC and electrical-buildings paragraphs |
| Communications / Network | Vendor building shall accommodate the EPC-defined Communications / Network interface (network racks housed in the building per DBM). | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-B95212AB85`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings paragraph |
| Building HVAC / Services | Vendor building HVAC shall be n + 1 sized so the cooling system tolerates failure or maintenance shutdown of one HVAC unit without affecting building heating and cooling. Electric building heaters (e.g., Ruffneck-type) provide heat where heat-medium heating is impractical. | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-D8A8F7FEBC`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, HVAC and building-heaters paragraphs |
| Fire & Gas / Safety Systems | Vendor building shall accommodate the EPC-defined Fire & Gas / Safety Systems interface; detailed F&G device list and routing are EPC integration scope. | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-9C0AFE36A2` |
| Maintenance Access | Vendor building layout shall preserve the EPC-defined Maintenance Access interface. Equipment doors are sized for (or include removable transom sections to allow) removal of the largest equipment per DBM. | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-D971A17948`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings wiring paragraph |
| Grading / Site Drainage / Spill Containment | Vendor building foundation/pile elevation and ground-level provisions shall be coordinated with the EPC-defined Grading / Site Drainage / Spill Containment interface. | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-50A5B3F280` |
| Structural / Foundations / Supports | Vendor building skid/frame and pile-elevation provisions shall be coordinated with the EPC-defined Structural / Foundations / Supports interface. Buildings are elevated on piles to provide space beneath the building for incoming/outgoing MCC cabling. | Workbook Packages row 41; `INTERFACE_REGISTER.csv` `IFC-E3D0A5A836`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings cable-entry paragraph |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility — shop fabrication of the modular electrical building including internal MCCs/transformers/UPS/panels/HVAC/lighting per the design basis, vendor documentation, and the physical equipment package. | `PACKAGE_REGISTER.csv` row `PKG-039`; `DELIVERABLE_REGISTER.csv` row `DEL-039-04`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings table row "850-1 ... Shop" |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility (subject to integration review of the vendor package). | `PACKAGE_REGISTER.csv` row `PKG-039` |
| Installation location | `TBD`. Source confirms general-purpose-area placement and elevated/pile installation but does not assign PKG-039 to a specific plot-plan coordinate. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings paragraph |
| Foundations / supports | Building is elevated and installed on piles to provide space beneath for MCC incoming cable trays; pile design and foundation interface coordination remain EPC scope per the Structural / Foundations / Supports interface. | `INTERFACE_REGISTER.csv` `IFC-E3D0A5A836`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings cable-entry paragraph |
| Vendor documentation set | Captured separately by `DEL-039-05_vendor-document-turnover-package`; this deliverable supplies the engineering, design basis, datasheet set, and physical equipment. | `DELIVERABLE_REGISTER.csv` rows `DEL-039-04`, `DEL-039-05` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-039-04_vendor-engineered-equipment-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-039`.
- `ARTIFACT_REGISTER.csv`, rows for `PKG-039`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-039` (12 applicable interfaces).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-039-04_vendor-engineered-equipment-package`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 41.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings list (850-1 row), electrical-buildings paragraph, HVAC and heaters paragraphs, 600 V MCC paragraphs, power-distribution paragraph, standby-power paragraph, grounding and bonding paragraphs, area-classification paragraph.
- Sibling EPC deliverables: `DEL-039-01_scope-of-work`, `DEL-039-02_package-datasheet` (vendor engineering inputs); `DEL-039-05_vendor-document-turnover-package`, `DEL-039-06_epc-vendor-package-review-and-acceptance` (downstream integration).
