# Datasheet: DEL-027-02_package-datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-027-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-027` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8301-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 20/26MVA 13.8kV/6.9kV/0.4kV | Workbook Packages row 29; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 27 / row 29 | Workbook Packages row 29; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 29; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-018 | Workbook Packages row 29; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 29; `_CONTEXT.md` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-027` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-027` |
| Package function | Step-down distribution transformer TXP-8301-1, 20/26 MVA, primary 13.8 kV, secondary 6.9 kV, tertiary/auxiliary 0.4 kV. | Workbook Packages row 29; `PACKAGE_REGISTER.csv` |
| Primary voltage | 13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded (facility MV backbone). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, facility voltage and service table; package name from Workbook Packages row 29 |
| Secondary voltage | 6.9 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded (process AC inverter-drive motors 5,500 hp and above). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, medium-voltage services; package name from Workbook Packages row 29 |
| Tertiary / auxiliary voltage | 0.4 kV, identified in package name. Service basis, configuration (winding vs auxiliary tap), and connected load are TBD; the DBM electrical service table does not enumerate a 0.4 kV distribution service for this facility. | Package name from Workbook Packages row 29; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage and service table |
| Rated capacity | 20/26 MVA (dual rating, presumed ONAN/ONAF or equivalent two-stage cooling rating per industry convention). The dual-rating designation is taken from the package name; the cooling-stage interpretation is ASSUMPTION until vendor data confirms. | Package name from Workbook Packages row 29 |
| Quantity | 1 transformer (TXP-8301-1 is a single tag identifier). Allocation against the DBM equipment-list "Oil-Filled Transformers" count of 2 is not confirmed at the package-row level. | Workbook Packages row 29; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, equipment list |
| Insulating medium | TBD. The DBM equipment list identifies "Oil-Filled Transformers" at the facility level; the assignment to TXP-8301-1 is plausible but not confirmed in the source slices accessible to this deliverable. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, equipment list |
| Service to | 6.9 kV switchgear/MCC supplying the Inlet/Sales Compressor 6.9 kV electrical building, including KM-2150/2250 Inlet/Sales Gas Compressor motor loads via the 6.9 kV MCC (MCC-8200 synchronous-transfer bus). Package-specific feeder assignment is TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 6.9 kV inlet/sales compressor building and 6.9 kV MCC paragraphs |
| Neutral grounding (6.9 kV secondary) | Each 6.9 kV transformer shall be grounded using a 100 A, 10 s neutral grounding resistor and shall operate as a tripping system. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding-resistor paragraph |
| Impedance, BIL, vector group, taps, sound level, temperature rise | TBD. No accessible source slice provides package-specific transformer impedance, BIL, vector group, tap range, sound level, or temperature-rise data. | Source gap; `26020-Package_Requirements.docx` has no accessible PKG-027 match copied into deliverable |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-027 and must be represented in the package interface requirements matrix. | Workbook Packages row 29; `INTERFACE_REGISTER.csv` `IFC-7FDEAE3A5F` |
| Grounding / Bonding | Interface fact applies to PKG-027 and must be represented in the package interface requirements matrix. | Workbook Packages row 29; `INTERFACE_REGISTER.csv` `IFC-868150D715` |
| Area / Exterior Lighting | Interface fact applies to PKG-027 and must be represented in the package interface requirements matrix. | Workbook Packages row 29; `INTERFACE_REGISTER.csv` `IFC-A7AA374E9F` |
| I&C / Control Cabling | Interface fact applies to PKG-027 and must be represented in the package interface requirements matrix. | Workbook Packages row 29; `INTERFACE_REGISTER.csv` `IFC-A771D8D087` |
| Communications / Network | Interface fact applies to PKG-027 and must be represented in the package interface requirements matrix. | Workbook Packages row 29; `INTERFACE_REGISTER.csv` `IFC-41603B3260` |
| Maintenance Access | Interface fact applies to PKG-027 and must be represented in the package interface requirements matrix. Cable tray and conduit routing shall not interfere with maintenance access. | Workbook Packages row 29; `INTERFACE_REGISTER.csv` `IFC-6D508F385A`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs |
| Structural / Foundations / Supports | Interface fact applies to PKG-027. Large oil-filled transformers shall be spaced in accordance with CEC requirements and generally installed on structural steel transformer bases. Secondary containment requirements shall be reviewed, and transformer selection shall avoid or limit containment requirements where practical. | Workbook Packages row 29; `INTERFACE_REGISTER.csv` `IFC-1B8FDDED83`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformer installation paragraph |
| Grounding design basis | Major electrical equipment shall be directly connected to the ground grid at two points. Ground wells at power transformers shall be provided for maintenance and operational testing. Distribution transformers shall have a separate copper ground conductor connected directly to ground, sized per CEC. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |
| MV cable basis (13.8 kV primary side) | Three-conductor copper TECK cable rated 15 kV with 133 percent insulation; shielded. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MV cable table |
| MV cable basis (6.9 kV secondary side) | Three-conductor copper TECK cable rated 8 kV with 100 percent insulation; shielded. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MV cable table |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-027` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-027` |
| Foundation | Generally precast concrete bearing foundations supporting structural steel transformer base, subject to CEC spacing requirements for large oil-filled transformers. Package-specific foundation design is TBD pending vendor weights and structural design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, foundations and transformers paragraphs |
| Installation location | Adjacent/feeding the 820-1 6.9 kV Inlet / Sales Compressor Electrical Building. The DBM identifies the 6.9 kV electrical building and the 6.9 kV MCC service basis; specific physical location of TXP-8301-1 (yard, pad, building proximity) is TBD pending plot plan. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings list and 6.9 kV building paragraphs |
| Secondary containment | Reviewed per DBM; transformer selection should avoid or limit containment requirements where practical. Package-specific containment decision is TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformer installation paragraph |
| Bushings, surge arresters, cooling fans/radiators, oil preservation, monitoring, accessories | TBD pending vendor selection and detailed engineering. | Source gap |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-027-02_package-datasheet`.
- `PACKAGE_REGISTER.csv`, row `PKG-027`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-027-02_package-datasheet`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-027` (`IFC-7FDEAE3A5F`, `IFC-868150D715`, `IFC-A7AA374E9F`, `IFC-A771D8D087`, `IFC-41603B3260`, `IFC-6D508F385A`, `IFC-1B8FDDED83`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-027-02_package-datasheet`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 29.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices: voltage and service table, 6.9 kV inlet/sales compressor building, 6.9 kV MCC, transformer installation, secondary containment, grounding resistors, ground grid, MV cable basis, cable tray and conduit.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, cross-facility 13.8 kV feed context.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific transformer content; no accessible PKG-027 match copied into the deliverable folder during PREPARATION.
