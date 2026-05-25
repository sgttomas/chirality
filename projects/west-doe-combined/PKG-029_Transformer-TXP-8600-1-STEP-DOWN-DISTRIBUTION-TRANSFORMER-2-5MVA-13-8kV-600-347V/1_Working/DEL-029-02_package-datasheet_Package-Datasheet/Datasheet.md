# Datasheet: DEL-029-02_package-datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-029-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-029` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8600-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V | Workbook Packages row 31; `PACKAGE_REGISTER.csv` |
| Equipment tag | TXP-8600-1 | Workbook Packages row 31; package name |
| Workbook ID / row | 29 / row 31 | Workbook Packages row 31; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` row `PKG-029` |
| CoA tracking number | 26020-01-30-020 | `PACKAGE_REGISTER.csv` row `PKG-029` |
| Discipline | Electrical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-029` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-029` |
| Package function | Step-down distribution transformer feeding low-voltage services from the 13.8 kV facility backbone. | Workbook Packages row 31; package name; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical distribution paragraphs (rows ~2917-2919) |
| Equipment tag | TXP-8600-1 | Package name (Workbook Packages row 31) |
| Nameplate rating (ASSUMPTION from package name) | 2.5 MVA. The accessible DBM source does not explicitly state a 2.5 MVA rating for TXP-8600-1; the rating is taken from the package title in the workbook row and Gate 7 registers. | ASSUMPTION based on `PACKAGE_REGISTER.csv` row `PKG-029` package name; no corroborating DBM clause located |
| Primary voltage | 13.8 kV (medium-voltage backbone). 3 phase, 3 wire, 60 Hz, low-resistance grounded per DBM facility basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, System Voltages table |
| Secondary voltage (ASSUMPTION from package name) | 600 V line-to-line / 347 V line-to-neutral (i.e., 600Y/347V wye secondary). The package name carries the "600/347V" notation; the DBM low-voltage service basis is stated as "600 V, 3 phase, 3 wire, 60 Hz, high-resistance grounded with 5 A continuous resistor" and does not describe a 600Y/347V wye distribution. See `HRR-029-02-001` in the Guidance Conflict Table. | ASSUMPTION (package title); DBM `4-25_Deepcut_DBM.md` System Voltages table does not corroborate a 600Y/347V wye secondary |
| Phases / frequency | 3 phase, 60 Hz | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, System Voltages table |
| Insulation / cooling medium | TBD. DBM states that "large oil-filled transformers shall be spaced in accordance with CEC requirements" and shall be installed on structural steel transformer bases; the source does not designate TXP-8600-1 specifically as oil-filled or dry-type. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Transformers paragraph |
| Secondary grounding | TBD. DBM states that "Each 600 V transformer shall be grounded by a 5 A continuous high-resistance grounding resistor" (3-wire HRG basis). Applicability to a 600/347V wye secondary is not addressed by source. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraph |
| Loads served | TBD package-specific load list. DBM identifies typical 600 V loads (motors 3/4 hp through 250 hp DOL, lighting and utility distribution transformers, building heaters, UPS systems larger than 10 kVA) but does not allocate specific loads to TXP-8600-1. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, System Voltages table |
| Source feeder | TBD. DBM states distribution is radial from the 13.8 kV switchgear to facility electrical buildings; the specific upstream feeder/breaker for TXP-8600-1 is not identified in accessible source. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, distribution paragraph |
| Installation location | TBD. DBM identifies the facility electrical building set but does not assign TXP-8600-1 to a specific building or pad. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, distribution and Transformers paragraphs |
| Quantity | 1 (per package; the package register lists TXP-8600-1 as a single tagged unit). | `PACKAGE_REGISTER.csv` row `PKG-029`; Workbook Packages row 31 |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-029 and must be represented in the package interface requirements matrix. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-717D0187BA` |
| Grounding / Bonding | Interface fact applies to PKG-029 and must be represented in the package interface requirements matrix. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-C49653E450` |
| Area / Exterior Lighting | Interface fact applies to PKG-029 and must be represented in the package interface requirements matrix. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-DFC1A10C2D` |
| I&C / Control Cabling | Interface fact applies to PKG-029 and must be represented in the package interface requirements matrix. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-A5C9438164` |
| Communications / Network | Interface fact applies to PKG-029 and must be represented in the package interface requirements matrix. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-81CFD2A32C` |
| Maintenance Access | Interface fact applies to PKG-029 and must be represented in the package interface requirements matrix. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-2C14FA1228` |
| Structural / Foundations / Supports | Interface fact applies to PKG-029 and must be represented in the package interface requirements matrix. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-380F4773FB` |
| Transformer spacing / containment | Large oil-filled transformers shall be spaced in accordance with CEC requirements; secondary containment requirements shall be reviewed, and selection shall avoid or limit containment requirements where practical. Applicability depends on whether TXP-8600-1 is oil-filled (TBD). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Transformers paragraph |
| Transformer base | Generally installed on structural steel transformer bases (oil-filled basis); a precast concrete bearing foundation is identified for transformers in the foundations section. Package-specific basis TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Transformers paragraph and foundations table |
| Grounding design basis | Major electrical equipment shall be directly connected to the ground grid at two points; distribution transformers, panelboards, and three-phase motors larger than 100 hp require a separate copper ground conductor sized per CEC. Ground wells at power transformers shall be provided for maintenance/testing. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |
| Cable / conduit routing | Cable tray and conduit routing shall not interfere with maintenance access. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-029` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-029` |
| Installation location | TBD. DBM confirms electrical-building and outdoor transformer scenarios but does not assign TXP-8600-1 to a specific location. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings and Transformers paragraphs |
| Foundations / supports | Structural / foundations / supports interface applies; oil-filled transformer foundation basis is structural steel transformer bases per DBM, with precast concrete bearing foundations also identified for transformers. Package-specific foundation type TBD until oil-filled vs dry-type and location are confirmed. | Workbook Packages row 31; `INTERFACE_REGISTER.csv`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, foundations table and Transformers paragraph |
| Containment | TBD pending oil-filled determination; if oil-filled, secondary containment review per DBM. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Transformers paragraph |
| Bushings, tap changer, accessories, protection devices | TBD unless defined by vendor package data and detailed design. | Source gap; no package-specific source slice located in accessible material |
| Acceptance / commissioning evidence | Construction acceptance and turnover evidence are produced by `DEL-029-03_construction-work-package` and `DEL-029-06_epc-vendor-package-review-and-acceptance`; this Datasheet provides the technical handoff basis only. | `DELIVERABLE_REGISTER.csv` rows for PKG-029 |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-029-02_package-datasheet`.
- `PACKAGE_REGISTER.csv`, row `PKG-029`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-029-02_package-datasheet` (ART-AEC54E64E4, ART-5F81FC4944, ART-0F9B7246EF, ART-B3B2E9B601, ART-5234544025, ART-43E140B73E, ART-3F9FB53D1F, ART-4240FAFE96, ART-1FB7865C91, ART-613D831688).
- `INTERFACE_REGISTER.csv`, rows for `PKG-029` (IFC-717D0187BA, IFC-C49653E450, IFC-DFC1A10C2D, IFC-A5C9438164, IFC-81CFD2A32C, IFC-2C14FA1228, IFC-380F4773FB).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-029-02_package-datasheet`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 31.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices for facility distribution, System Voltages, Standby Power, Transformers, grounding/bonding, cable tray, conduit, and electrical buildings.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific TXP-8600-1 content; no PKG-029 match was located in this run.
