# Datasheet: DEL-015-02_package-datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-015-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-015` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8300-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 12/15MVA 13.8kV/4160/2400V | Workbook Packages row 17; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 15 / row 17 | Workbook Packages row 17; `PACKAGE_REGISTER.csv` |
| WBS | 02 | Workbook Packages row 17; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-02-30-006 | Workbook Packages row 17; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 17; `_CONTEXT.md` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-015` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-015` |
| Package function | Step-down distribution transformer package serving the 4160V MCC for 4000V process motors at the 03-25 Compressor and Liquids facility. | Workbook Packages row 17; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "Incoming Power and Transformers" table |
| Equipment tag | TXP-8300-1 | Workbook Packages row 17; `PACKAGE_REGISTER.csv` |
| Primary (HV) voltage | 13.8 kV, 3 phase, 3 wire, 60 Hz | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, System Voltages table ("Incoming power from 04-25") and Incoming Power and Transformers table |
| Secondary voltage(s) | 4.16 kV confirmed by source; 2400 V tertiary appears in the package name but is not corroborated by the accessible DBM source slice. Treat 2400 V as `ASSUMPTION` pending source confirmation. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Incoming Power and Transformers table; Workbook Packages row 17 (package title) |
| Rating | DBM lists "13.8 kV to 4.16 kV, 12 MVA transformer"; package title carries "12/15 MVA" (likely OA/FA dual rating). The 12 MVA value is source-supported; the 15 MVA forced-air rating is `ASSUMPTION` derived from the package title. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Incoming Power and Transformers table; Workbook Packages row 17 |
| Grounding regime (primary) | 13.8 kV system is Low-Resistance Grounded (LRG). | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, System Voltages table |
| Grounding regime (4.16 kV secondary) | 4.16 kV medium-voltage service is Low-Resistance Grounded (LRG). | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, System Voltages table |
| Loads served | 4160V MCC, serving large 4000V motors including inlet compressors KM-2150 and KM-2250. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Incoming Power and Transformers and 4160V MCC sections |
| Insulation / cooling class | TBD. The accessible DBM source slice does not specify ONAN/ONAF/OFAF, winding insulation, or BIL ratings. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (gap); `26020-Package_Requirements.docx` (no PKG-015 match identified) |
| Vector group / impedance / tap range | TBD. Not stated in accessible sources. | Source gap |
| Quantity | TBD. Single tagged unit TXP-8300-1 is identified; package quantity not separately stated. | Workbook Packages row 17 |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-015 and must be represented in the package interface requirements matrix. | Workbook Packages row 17; `INTERFACE_REGISTER.csv` `IFC-E8F09F1065` |
| Grounding / Bonding | Interface fact applies to PKG-015 and must be represented in the package interface requirements matrix. | Workbook Packages row 17; `INTERFACE_REGISTER.csv` `IFC-073273FE3A` |
| Area / Exterior Lighting | Interface fact applies to PKG-015 and must be represented in the package interface requirements matrix. | Workbook Packages row 17; `INTERFACE_REGISTER.csv` `IFC-677CA55221` |
| I&C / Control Cabling | Interface fact applies to PKG-015 and must be represented in the package interface requirements matrix. | Workbook Packages row 17; `INTERFACE_REGISTER.csv` `IFC-99831AAF77` |
| Communications / Network | Interface fact applies to PKG-015 and must be represented in the package interface requirements matrix. | Workbook Packages row 17; `INTERFACE_REGISTER.csv` `IFC-6582D48513` |
| Maintenance Access | Interface fact applies to PKG-015 and must be represented in the package interface requirements matrix. | Workbook Packages row 17; `INTERFACE_REGISTER.csv` `IFC-B9C22F51DB` |
| Structural / Foundations / Supports | Interface fact applies to PKG-015 and must be represented in the package interface requirements matrix. | Workbook Packages row 17; `INTERFACE_REGISTER.csv` `IFC-2646D74297` |
| Area classification | Outdoor pipe-rack areas are general purpose non-hazardous unless detailed classification drawings identify otherwise; transformer installation classification shall be confirmed by detailed area classification drawings. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Area Classification section |
| Cable / raceway separation | Power circuits at 13.8 kV, 4,160 V, and 600 V shall be separated from control and instrument circuits by distance, shielding, or routing as required to minimize interference. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings, Raceways, Lighting, and Heat Tracing section |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-015` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-015` |
| Foundations / supports | Structural / Foundations / Supports interface applies; foundations shall be designed for the final geotechnical report, equipment loads, snow/wind/seismic design criteria, frost protection, vibration, settlement, and maintenance access. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Foundations paragraph; `INTERFACE_REGISTER.csv` |
| Installation location | TBD. DBM identifies a "4.16 kV inlet/overheads compressor electrical building" as a known electrical building interface but does not assign TXP-8300-1 to a specific outdoor pad, yard, or building location. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Buildings section |
| Bushings, radiators, conservator, cooling fans, on-load tap changer | TBD. Not specified in accessible sources. | Source gap; vendor package data required |
| Protective relaying interface | Transformer protection coordinates with the 4160V MCC, which provides motor protection relays and an EtherNet communication port to the plant PLC; transformer-specific relays (87T, 50/51, 63, 49) are TBD pending vendor data and detailed protection studies. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160V MCC section |
| Communications / data | Modbus or other vendor protocols may be integrated via Kepware KepserverEX for monitoring only; control is not carried over Modbus. Detailed transformer data map is TBD. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Unit Control Systems and Package Interfaces section |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-015-02_package-datasheet`.
- `PACKAGE_REGISTER.csv`, row `PKG-015`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-015-02_package-datasheet`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-015` (`IFC-E8F09F1065`, `IFC-073273FE3A`, `IFC-677CA55221`, `IFC-99831AAF77`, `IFC-6582D48513`, `IFC-B9C22F51DB`, `IFC-2646D74297`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-015-02_package-datasheet`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 17.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 Electrical Basis source slices: System Voltages table, Incoming Power and Transformers table, 4160V MCC, Electrical Buildings/Raceways, Area Classification, Foundations, Buildings.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific transformer content; no confirmed PKG-015 match identified in this run.
