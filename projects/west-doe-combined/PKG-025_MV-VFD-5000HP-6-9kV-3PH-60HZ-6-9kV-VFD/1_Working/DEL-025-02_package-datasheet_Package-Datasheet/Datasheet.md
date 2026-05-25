# Datasheet: DEL-025-02_package-datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-025-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-025` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD | Workbook Packages row 27; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 25 / row 27 | Workbook Packages row 27; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 27; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-016 | Workbook Packages row 27; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 27; `_CONTEXT.md` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-025` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-025` |
| Package function | Medium-voltage Variable Frequency Drive (VFD) supplying a 5,000 hp class, 6.9 kV, 3-phase, 60 Hz motor; designated 6.9 kV VFD package per workbook nomenclature. | Workbook Packages row 27 |
| Nominal voltage class | 6.9 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded medium-voltage service. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage and service table (line ~2935) |
| Nominal motor rating | 5,000 hp per workbook package name. The DBM medium-voltage application threshold is "facility process AC inverter-drive motors rated 5,500 hp and above," so the 5,000 hp workbook label and the 5,500 hp DBM threshold do not exactly coincide. See Guidance Conflict Table HRR-025-02-001. | Workbook Packages row 27; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage and service table |
| Application context (candidate) | DBM identifies "Starting VFDs ... for the KM-2150/2250 Inlet/Sales Gas Compressor motors" fed from the 6.9 kV MCC with synchronous transfer to the MCC-8200 synchronous-transfer bus. Direct assignment of PKG-025 to this duty is `ASSUMPTION` pending human confirmation; see HRR-025-02-002. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 6.9 kV MCC paragraph (line ~2955) |
| Drive topology / synchronous transfer | Where supplied as a Starting VFD per DBM, the drive shall accelerate the motor and effect synchronous transfer to a normal-service bus (MCC-8200) after reaching full speed; standalone continuous-duty VFD operation is not stated by DBM for this voltage class. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 6.9 kV MCC paragraph; inlet/sales compressor start-method paragraph (line ~893) |
| Power-factor correction | Power-factor-correction capacitor banks shall not be installed on the MCC-8200 synchronous-transfer bus. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 6.9 kV MCC paragraph |
| Motor feeder cable basis | 6.9 kV medium-voltage cables shall be three-conductor copper TECK cable rated 8 kV with 100 percent insulation; shielded. Low-voltage power cable fed from VFDs shall be copper TECK cable. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MV cable table (lines ~3008, ~3013) |
| Hazardous-area considerations | VFD-fed motors located in Zone 2 areas shall be marked accordingly and supplied with a temperature code lower than the temperature code specified on the area-classification drawing or fugitive-emissions study. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, motor voltage/Zone 2 paragraph (line ~2961) |
| Building / housing context | Electrical buildings (prefabricated, modular, in general-purpose areas) may house medium-voltage VFDs as required by detailed design; DBM identifies a "6.9 kV Inlet/Sales Compressor Electrical Building" as the corresponding facility space. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph (line ~2973); 6.9 kV Inlet/Sales Compressor Electrical Building reference (line ~2921, ~2812) |
| Quantity allocated to PKG-025 | `TBD`. The accessible sources do not explicitly state how many MV VFD units are assigned to PKG-025; DBM names KM-2150 and KM-2250 starting VFDs without enumerating PKG-025 scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; Workbook Packages row 27 |
| Detailed VFD ratings (output current, kVA, harmonic class, cooling, enclosure) | `TBD`. No accessible package-specific source slice defines these ratings. `_Sources/26020-Package_Requirements.docx` was searched and no PKG-025-specific match was found. | `_REFERENCES.md`; `_Sources/26020-Package_Requirements.docx` |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-025 and must be represented in the package interface requirements matrix. | Workbook Packages row 27; `INTERFACE_REGISTER.csv` `IFC-812CB082EA` |
| Grounding / Bonding | Interface fact applies to PKG-025 and must be represented in the package interface requirements matrix. | Workbook Packages row 27; `INTERFACE_REGISTER.csv` `IFC-3BE8D26B6B` |
| I&C / Control Cabling | Interface fact applies to PKG-025 and must be represented in the package interface requirements matrix. | Workbook Packages row 27; `INTERFACE_REGISTER.csv` `IFC-949E34ECEA` |
| Communications / Network | Interface fact applies to PKG-025 and must be represented in the package interface requirements matrix. The 6.9 kV MCC requires an Ethernet communication port for connection to the plant PLC central control panel for data acquisition; equivalent integration is expected of the MV VFD. | Workbook Packages row 27; `INTERFACE_REGISTER.csv` `IFC-EF46C006CC`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 6.9 kV MCC paragraph |
| Maintenance Access | Interface fact applies to PKG-025 and must be represented in the package interface requirements matrix. Cable tray and conduit routing shall not interfere with maintenance access. | Workbook Packages row 27; `INTERFACE_REGISTER.csv` `IFC-3A60522074`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs |
| Structural / Foundations / Supports | Interface fact applies to PKG-025 and must be represented in the package interface requirements matrix. | Workbook Packages row 27; `INTERFACE_REGISTER.csv` `IFC-FB81FE736B` |
| Grounding design basis | Major electrical equipment shall be directly connected to the ground grid at two points; each 6.9 kV transformer shall be grounded using a 100 A, 10 s neutral grounding resistor and shall operate as a tripping system. Applicability to PKG-025 grounding shall be confirmed by detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs (line ~2985) |
| MV breaker / protection control | UPS services at 120 VAC / 125 VDC support medium-voltage breaker control circuits and medium-voltage protective relays; the VFD package's supervisory control and protection interfaces shall be compatible with this service basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, UPS services row (line ~2939) |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-025` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-025` |
| Installation location | Likely housed in a prefabricated, modular electrical building (e.g., "6.9 kV Inlet/Sales Compressor Electrical Building" if assigned to that duty); specific assignment for PKG-025 is `TBD` until human-confirmed. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph; building list |
| Foundations / supports | Structural / foundations / supports interface applies; package-specific support basis is `TBD`. | Workbook Packages row 27; `INTERFACE_REGISTER.csv` |
| Cable, conduit, raceway | 6.9 kV three-conductor copper TECK cable rated 8 kV, 100 percent insulation, shielded; VFD-fed low-voltage cabling copper TECK; routing preserves maintenance access. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MV cable and cable tray paragraphs |
| Drive cooling, enclosure type, harmonic filter, transformer arrangement | `TBD` pending vendor data and detailed design. | Source gap; `_Sources/26020-Package_Requirements.docx` has no accessible PKG-025 package match |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-025-02_package-datasheet`.
- `PACKAGE_REGISTER.csv`, row `PKG-025`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-025-02_package-datasheet`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-025` (`IFC-812CB082EA`, `IFC-3BE8D26B6B`, `IFC-949E34ECEA`, `IFC-EF46C006CC`, `IFC-3A60522074`, `IFC-FB81FE736B`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-025-02_package-datasheet`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 27.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices: voltage/service table, 6.9 kV MCC paragraph (Starting VFD KM-2150/2250 and MCC-8200), motor voltage and Zone 2 paragraph, electrical buildings paragraph, building list, grounding paragraphs, MV cable table, cable tray/conduit paragraphs, UPS services row, inlet/sales compressor start-method paragraph.
- `_Sources/26020-Package_Requirements.docx`, searched for PKG-025 package-specific content; no PKG-025 match found.
