# Datasheet: DEL-033-04_vendor-engineered-equipment-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-033-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Engineered Equipment Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-033` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 4160V SWITCHGEAR ELECTRICAL BUILDING (830-2) | Workbook Packages row 35; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 33 / row 35 | Workbook Packages row 35; `PACKAGE_REGISTER.csv` |
| WBS | 02 | Workbook Packages row 35; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-02-30-024 | Workbook Packages row 35; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 35; `_CONTEXT.md` |
| Deliverable type | Vendor Package Production Unit | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-033` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Production unit class | Vendor-owned Electrical package — engineering, design, fabrication/supply, and physical equipment package for a 4160 V switchgear electrical building. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-033-04_vendor-engineered-equipment-package` |
| Package function | 4160 V switchgear electrical building serving the 03-25 facility under WBS 02; building tag suffix "830-2". | Workbook Packages row 35 |
| Medium-voltage service basis | 4,160 V, 3 phase, 3 wire, 60 Hz, low-resistance grounded; intended for process AC inverter-drive motors from 250 hp to 5,500 hp. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 System Voltages table |
| Upstream incoming basis | The 03-25 medium-voltage service is sub-fed from the 04-25 13.8 kV Main Switchgear Electrical Building, stepped down through a 13.8 kV to 4.16 kV, 12 MVA transformer that feeds the 4160 V MCC for 4000 V motors. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Incoming Power and Transformers |
| 4160 V MCC characteristics | The 4160 V MCC provides field-fused contactors, motor protection relays, and an EtherNet communication port to the plant PLC central control panel for data acquisition; serves large 4000 V motors including inlet compressors KM-2150 and KM-2250. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160V MCC |
| Building content basis | Electrical buildings shall house MCCs, switchgear, distribution equipment, and associated HVAC/ventilation systems. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings, Raceways, Lighting, and Heat Tracing |
| Building location and area class | Electrical buildings are located in general-purpose (non-hazardous) areas for convenient power distribution; area classification, building HVAC, and remote distribution centres shall be coordinated with the hazardous area classification and controls architecture. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Area Classification; Electrical Buildings |
| Circuit segregation | Power circuits at 13.8 kV, 4,160 V, and 600 V shall be separated from control and instrument circuits by distance, shielding, or routing as required to minimize interference. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings, Raceways, Lighting, and Heat Tracing |
| Cable / conduit / grounding basis | Cable tray, conduit, grounding, and bonding shall comply with project electrical specifications and detailed design. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings, Raceways, Lighting, and Heat Tracing |
| Building HVAC basis (cross-facility) | Where 04-25 (Deepcut) practice applies, electrical buildings are climate controlled with HVAC sized as an n+1 system. Applicability to 03-25 building "830-2" is `TBD` pending project electrical specification confirmation. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph |
| Building tag (830-2) basis | Workbook row 35 names the package "4160V SWITCHGEAR ELECTRICAL BUILDING (830-2)". No accessible source slice in the 03-25 DBM enumerates an "830-2" tag explicitly; the 04-25 (Deepcut) Buildings schedule lists "830-1 4.16kV Acid Gas / Overheads Compressor Electrical Building". The "830-2" tag is therefore the authoritative package identity from workbook row 35; the cross-facility tag relationship is `TBD`. | Workbook Packages row 35; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Buildings schedule |
| Switchgear count / lineup / rating detail | TBD. The 03-25 DBM does not provide bus rating, short-circuit rating, breaker count, frame size, or arc-flash class specific to the 830-2 building. Vendor data shall close these values. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings (no package-specific lineup detail) |
| Vendor engineering inputs | EPC Scope of Work (`DEL-033-01`) and Package Datasheet (`DEL-033-02`) form the vendor engineering basis. | `_CONTEXT.md`, Scope; `DELIVERABLE_REGISTER.csv` rows `DEL-033-01_scope-of-work`, `DEL-033-02_package-datasheet` |
| Vendor engineering outputs | Vendor engineered physical equipment package; vendor package design basis and datasheet set. | `_CONTEXT.md`, Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-033-04` |

## Conditions

| Interface / condition | Vendor package basis | Source |
|---|---|---|
| Utility Piping | Vendor package shall coordinate with the EPC-defined Utility Piping interface at the building boundary. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-C55D5117E0` |
| Drain / Containment | Vendor package shall coordinate with the EPC-defined Drain / Containment interface. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-6D41E81E9D` |
| Electrical Power | Vendor package shall be engineered to the EPC-defined Electrical Power interface (incoming 13.8 kV-to-4.16 kV feeder per the 03-25 incoming-power basis). | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-87E42C897B`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Incoming Power and Transformers |
| Grounding / Bonding | Vendor package shall be engineered to the EPC-defined Grounding / Bonding interface, compatible with two-point ground-grid connection of major electrical equipment. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-68149F738F`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |
| Area / Exterior Lighting | Vendor package shall coordinate building exterior lighting provisions with the EPC-defined Area / Exterior Lighting interface. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-DEF85D9CD6` |
| I&C / Control Cabling | Vendor package shall coordinate the I&C / Control Cabling interface, preserving segregation from 13.8 kV / 4.16 kV / 600 V power circuits as required by the DBM. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-34A8619308`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings, Raceways, Lighting, and Heat Tracing |
| Communications / Network | Vendor package shall coordinate the EtherNet/plant-network interface for the 4160 V MCC data link to the plant PLC central control panel. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-F6B851FF9C`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160V MCC |
| Building HVAC / Services | Vendor package shall coordinate building HVAC and services with the EPC-defined Building HVAC / Services interface. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-F6FC5D19F9`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings, Raceways, Lighting, and Heat Tracing |
| Fire & Gas / Safety Systems | Vendor package shall coordinate the Fire & Gas / Safety Systems interface for the building. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-BED07EB56D` |
| Maintenance Access | Vendor package layout and supply shall preserve the EPC-defined Maintenance Access interface, including door sizing or transom provision for the largest equipment removal where the 04-25 practice applies. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-73858A4A80`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Grading / Site Drainage / Spill Containment | Vendor package shall coordinate building grading and site drainage with the EPC-defined Grading / Site Drainage / Spill Containment interface. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-9AEF468935` |
| Structural / Foundations / Supports | Vendor package skid/frame/foundation provisions shall be coordinated with the EPC-defined Structural / Foundations / Supports interface; electrical-building foundation/anchorage requires equipment-specific checks. | Workbook Packages row 35; `INTERFACE_REGISTER.csv` `IFC-D7C1CC054F`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Foundations paragraph |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility — engineering, design, fabrication/supply, vendor documentation, and the physical equipment package (4160 V switchgear electrical building). | `PACKAGE_REGISTER.csv` row `PKG-033`; `DELIVERABLE_REGISTER.csv` row `DEL-033-04` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility (subject to integration review of the vendor package). | `PACKAGE_REGISTER.csv` row `PKG-033` |
| Building type | Electrical building housing 4160 V switchgear and associated distribution and HVAC equipment; modular/prefabricated configuration is the 04-25 default and is `ASSUMPTION` for 03-25 building "830-2" unless project electrical specifications direct otherwise. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings |
| Installation location | TBD. The 03-25 DBM places electrical buildings in general-purpose areas but does not assign building "830-2" to a specific plot location. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Area Classification; Electrical Buildings |
| Foundations / supports | Foundations shall be designed for the final geotechnical report, equipment loads, snow/wind/seismic design criteria, frost protection, vibration, settlement, and maintenance access; electrical buildings require equipment-specific foundation and anchorage checks. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Foundations |
| Cable entry / raceway | Cable tray, conduit, grounding, and bonding shall comply with project electrical specifications and detailed design; segregation between 13.8 kV / 4.16 kV / 600 V power circuits and control/instrument circuits shall be preserved. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings, Raceways, Lighting, and Heat Tracing |
| Vendor documentation set | Captured separately by `DEL-033-05_vendor-document-turnover-package`; this deliverable supplies the engineering, design basis, datasheet set, and physical equipment. | `DELIVERABLE_REGISTER.csv` rows `DEL-033-04`, `DEL-033-05` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-033-04_vendor-engineered-equipment-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-033`.
- `ARTIFACT_REGISTER.csv`, rows for `PKG-033`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-033` (12 interface rows; all `Applicable=YES`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-033-04_vendor-engineered-equipment-package`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 35.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 Electrical Basis (System Voltages, Incoming Power and Transformers, 4160V MCC, 600V MCC and Standby Power, Electrical Buildings/Raceways/Lighting/Heat Tracing) and SEC Civil / Buildings / Foundations paragraphs.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings, Grounding and Bonding, Cable/Raceway slices and Buildings schedule (including the related "830-1 4.16kV Acid Gas / Overheads Compressor Electrical Building" tag).
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific 830-2 / 4160 V switchgear building content; no PKG-033-specific package row was found in the accessible sources.
- Sibling EPC deliverables: `DEL-033-01_scope-of-work`, `DEL-033-02_package-datasheet` (vendor engineering inputs); `DEL-033-05_vendor-document-turnover-package`, `DEL-033-06_epc-vendor-package-review-and-acceptance` (downstream integration).
