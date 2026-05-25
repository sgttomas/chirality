# Datasheet: DEL-031-02_package-datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-031-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-031` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8500-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 3MVA 13.8kV/600/347V | Workbook Packages row 33; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 31 / row 33 | Workbook Packages row 33; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 33; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-022 | Workbook Packages row 33; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 33; `_CONTEXT.md` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-031` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-031` |
| Package function | Step-down distribution transformer, tag TXP-8500-1, transforming 13.8 kV to 600 V / 347 V at 3 MVA nameplate rating. | Workbook Packages row 33 (package name); `PACKAGE_REGISTER.csv` row `PKG-031` |
| Primary system voltage | 13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded (medium-voltage services backbone). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, System Voltages table |
| Secondary system voltage | 600 V, 3 phase, 3 wire, 60 Hz, high-resistance grounded with 5 A continuous resistor (low-voltage services); 347 V line-to-neutral derived from the 600 V system. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, System Voltages table; package name 600/347 V (PACKAGE_REGISTER.csv) |
| Rated capacity | 3 MVA nameplate. | Workbook Packages row 33 (package name) |
| Upstream source | Fed radially from the plant 13.8 kV switchgear, which distributes through step-down transformers to facility electrical buildings. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Systems / 13.8 kV distribution paragraph |
| Transformer construction class | TBD. DBM addresses large oil-filled transformers on structural steel transformer bases with CEC spacing and notes "transformer selection shall avoid or limit containment requirements where practical." Selection of oil-filled vs. dry-type for TXP-8500-1 is not stated in the accessible source set. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Transformers paragraph |
| Neutral grounding (secondary) | 600 V transformer secondary shall be grounded by a 5 A continuous high-resistance grounding resistor. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Grounding and Bonding paragraph |
| Cable / feeder type (secondary) | Single-conductor cables shall be avoided for 600 V transformer secondary to plant 600 V MCCs; ACWU is the basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cable, Wire, and Raceways table |
| Cable type (primary) | 13.8 kV medium-voltage cables: three-conductor copper TECK cable rated 15 kV with 133 percent insulation; shielded. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cable, Wire, and Raceways table |
| Quantity allocated to this package | One transformer (tag TXP-8500-1). DBM equipment list identifies "Oil-Filled Transformers" quantity 2 at the facility level; package-specific allocation to TXP-8500-1 vs. other transformer tags is not confirmed in the accessible source set. | Workbook Packages row 33 (tag in name); `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, equipment list (ELC-QAS-000011-001) |
| Service location | TBD. DBM lists 600 V electrical buildings (840-1, 850-1, 860-1) as candidate served buildings, but the accessible source set does not assign TXP-8500-1 to a specific building, pad, or outdoor location. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings list |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-031 and must be represented in the package interface requirements matrix. | Workbook Packages row 33; `INTERFACE_REGISTER.csv` `IFC-E6C51663E5` |
| Grounding / Bonding | Interface fact applies to PKG-031 and must be represented in the package interface requirements matrix. | Workbook Packages row 33; `INTERFACE_REGISTER.csv` `IFC-2DE626B361` |
| Area / Exterior Lighting | Interface fact applies to PKG-031 and must be represented in the package interface requirements matrix. | Workbook Packages row 33; `INTERFACE_REGISTER.csv` `IFC-9BF05B6DCC` |
| I&C / Control Cabling | Interface fact applies to PKG-031 and must be represented in the package interface requirements matrix. | Workbook Packages row 33; `INTERFACE_REGISTER.csv` `IFC-5DCD93CE40` |
| Communications / Network | Interface fact applies to PKG-031 and must be represented in the package interface requirements matrix. | Workbook Packages row 33; `INTERFACE_REGISTER.csv` `IFC-452A0203CB` |
| Maintenance Access | Interface fact applies to PKG-031 and must be represented in the package interface requirements matrix. | Workbook Packages row 33; `INTERFACE_REGISTER.csv` `IFC-3A6221E4CB` |
| Structural / Foundations / Supports | Interface fact applies to PKG-031 and must be represented in the package interface requirements matrix. | Workbook Packages row 33; `INTERFACE_REGISTER.csv` `IFC-15FCC571C7` |
| Grounding design basis | All major electrical equipment shall be directly connected to the ground grid at two points. All distribution transformers shall have a separate copper ground conductor sized per CEC, in addition to the conductor run with power wiring. Ground wells at power transformers shall be provided for maintenance and operational testing. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Grounding and Bonding paragraphs |
| Transformer spacing and foundation | Large oil-filled transformers shall be spaced in accordance with CEC requirements and shall generally be installed on structural steel transformer bases on precast concrete bearing foundations. Secondary containment requirements shall be reviewed. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Transformers paragraph; Foundations table row "Transformers" |
| Cable / conduit routing | Cable tray and conduit routing shall not interfere with maintenance access. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-031` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-031` |
| Foundation | Precast concrete bearing foundations are the general basis for transformers; structural steel transformer base on top of foundation. Package-specific foundation drawing is TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Foundations table; Transformers paragraph |
| Containment | Secondary containment shall be reviewed and transformer selection shall avoid or limit containment requirements where practical. Containment outcome for TXP-8500-1 is TBD pending detailed design and final fluid-fill decision. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Transformers paragraph |
| Installation location | TBD. 600 V electrical buildings (840-1 Acid Gas Compressor; 850-1 Inlet/Sales Compressor; 860-1 General Area/Tank Farm) are candidate served buildings; assignment of TXP-8500-1 to a specific building or outdoor pad is not stated in the accessible source set. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings list |
| Primary feeder | 13.8 kV three-conductor copper TECK, 15 kV rated, 133 percent insulation, shielded, from the 13.8 kV switchgear. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cable, Wire, and Raceways table |
| Secondary feeder | 600 V transformer secondary to plant 600 V MCC via ACWU cable; single-conductor cables avoided. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cable, Wire, and Raceways table |
| Protective relaying, tap settings, impedance | TBD pending vendor data sheet and detailed electrical studies. The accessible source set does not specify package-specific impedance, vector group, tap range, or relay coordination for TXP-8500-1. | Source gap; `26020-Package_Requirements.docx` searched, no PKG-031 package-specific match identified in the accessible material |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-031-02_package-datasheet`.
- `PACKAGE_REGISTER.csv`, row `PKG-031`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-031-02_package-datasheet`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-031`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-031-02_package-datasheet`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 33.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis slices for system voltages, transformers, grounding and bonding, cable/wire/raceways, electrical buildings, and foundations.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific transformer content; no confirmed PKG-031 / TXP-8500-1 package-specific match identified in accessible material.
