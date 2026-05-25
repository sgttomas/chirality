# Datasheet: DEL-016-02_package-datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-016-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-016` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 3MVA 13.8kV/600/347V | Workbook Packages row 18; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 16 / row 18 | Workbook Packages row 18; `PACKAGE_REGISTER.csv` |
| WBS | 02 | Workbook Packages row 18; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-02-30-007 | Workbook Packages row 18; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 18; `_CONTEXT.md` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-016` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-016` |
| Package function | Step-down distribution transformer, identified as TXP-8200-1, transforming 13.8 kV primary to 600 V / 347 V secondary, rated 3 MVA. | Workbook Packages row 18; `PACKAGE_REGISTER.csv` |
| Primary voltage | 13.8 kV (matches DBM Incoming Power & Transformers row "13.8 kV to 600V, 3 MVA transformer"). | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, System Voltages and Incoming Power and Transformers sections |
| Secondary voltage | 600 V / 347 V (600 V three-phase phase-to-phase with 347 V phase-to-neutral implied by 600 V three-phase 60 Hz LV service). Phase/wire/neutral configuration TBD pending vendor data. | Workbook Packages row 18; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, System Voltages |
| Rated capacity | 3 MVA. | Workbook Packages row 18; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Incoming Power and Transformers |
| Service description | Feeds the 600 V MCC for LV loads at 03-25 (Comp & Liquids); cross-facility incoming power originates at 04-25 13.8 kV Main Switchgear Electrical Building. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Incoming Power and Transformers, 600V MCC and Standby Power |
| LV service grounding basis | 600 V LV service is 3 phase / 3 wire / 60 Hz HRG with 5 A continuous resistor per DBM System Voltages. Transformer secondary winding configuration and neutral treatment TBD pending vendor data and detailed electrical study. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, System Voltages |
| Primary feed grounding basis | 13.8 kV incoming is LRG per DBM System Voltages. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, System Voltages |
| Insulation / cooling type | TBD. No accessible source slice specifies dry-type vs. liquid-filled, insulation class, BIL, impedance, or cooling class for TXP-8200-1. | Source gap; `26020-Package_Requirements.docx` has no accessible PKG-016 package-specific match |
| Tap configuration | TBD. No accessible source slice specifies primary/secondary tap range or operation. | Source gap |
| Enclosure / installation | TBD. DBM states electrical buildings house MCCs, switchgear, and distribution equipment; assignment of TXP-8200-1 to indoor/outdoor or specific electrical building is not stated. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings, Raceways, Lighting, and Heat Tracing |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-016 and must be represented in the package interface requirements matrix. | Workbook Packages row 18; `INTERFACE_REGISTER.csv` `IFC-0C63CABBEC` |
| Grounding / Bonding | Interface fact applies to PKG-016 and must be represented in the package interface requirements matrix. | Workbook Packages row 18; `INTERFACE_REGISTER.csv` `IFC-C4343B4BCA` |
| Area / Exterior Lighting | Interface fact applies to PKG-016 and must be represented in the package interface requirements matrix. | Workbook Packages row 18; `INTERFACE_REGISTER.csv` `IFC-C649F648C5` |
| I&C / Control Cabling | Interface fact applies to PKG-016 and must be represented in the package interface requirements matrix. | Workbook Packages row 18; `INTERFACE_REGISTER.csv` `IFC-AC26461656` |
| Communications / Network | Interface fact applies to PKG-016 and must be represented in the package interface requirements matrix. | Workbook Packages row 18; `INTERFACE_REGISTER.csv` `IFC-D3B7348DC6` |
| Maintenance Access | Interface fact applies to PKG-016 and must be represented in the package interface requirements matrix. | Workbook Packages row 18; `INTERFACE_REGISTER.csv` `IFC-4A94795733` |
| Structural / Foundations / Supports | Interface fact applies to PKG-016 and must be represented in the package interface requirements matrix. | Workbook Packages row 18; `INTERFACE_REGISTER.csv` `IFC-E3BE98E89B` |
| Area classification | Facility general classification basis is Class I Zone 2, Gas Groups IIA and IIB; package-specific area classification (indoor electrical building vs. outdoor) TBD. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Area Classification |
| Cable / conduit separation | Power circuits at 13.8 kV and 600 V shall be separated from control and instrument circuits by distance, shielding, or routing as required to minimize interference. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings, Raceways, Lighting, and Heat Tracing |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-016` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-016` |
| Installation location | TBD. DBM acknowledges electrical buildings house distribution equipment but does not assign TXP-8200-1 to a specific building, pad, or yard location. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings |
| Foundations / supports | Structural / foundations / supports interface applies; package-specific support basis (pad type, anchor, seismic, load) is TBD pending vendor data. | Workbook Packages row 18; `INTERFACE_REGISTER.csv` |
| Containment / spill (if liquid-filled) | TBD pending insulation/cooling type confirmation. | Source gap |
| Winding configuration, BIL, impedance, losses, sound level, fan/cooling stages | TBD unless defined by vendor package data and detailed design. | Source gap; `26020-Package_Requirements.docx` has no accessible PKG-016 package match |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-016-02_package-datasheet`.
- `PACKAGE_REGISTER.csv`, row `PKG-016`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-016-02_package-datasheet`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-016`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-016-02_package-datasheet`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 18.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, System Voltages, Incoming Power and Transformers, 600V MCC and Standby Power, Electrical Buildings/Raceways, Area Classification source slices.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific transformer content; no PKG-016 match found.
