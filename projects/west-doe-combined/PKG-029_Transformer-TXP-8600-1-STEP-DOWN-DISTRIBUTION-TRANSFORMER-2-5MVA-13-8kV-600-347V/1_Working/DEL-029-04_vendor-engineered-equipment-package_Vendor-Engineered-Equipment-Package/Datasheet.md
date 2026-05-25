# Datasheet: DEL-029-04_vendor-engineered-equipment-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-029-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Engineered Equipment Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-029` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8600-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V | Workbook Packages row 31; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 29 / row 31 | Workbook Packages row 31; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` row `PKG-029` |
| CoA tracking number | 26020-01-30-020 | `PACKAGE_REGISTER.csv` row `PKG-029` |
| Discipline | Electrical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable type | Vendor Package Production Unit | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-029` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-029` |
| Package function | Step-down distribution transformer (single transformer, equipment tag TXP-8600-1) | Workbook Packages row 31 |
| Nameplate rating (workbook title) | 2.5 MVA, 13.8 kV primary, 600/347 V secondary | Workbook Packages row 31; `PACKAGE_REGISTER.csv` row `PKG-029` |
| Equipment tag | TXP-8600-1 | Workbook Packages row 31 |
| Service basis (general) | Radial step-down from the 13.8 kV plant distribution bus to a 600 V low-voltage system serving facility low-voltage loads (motors 3/4 hp to 250 hp DOL, lighting/utility distribution transformers, building heaters, UPS larger than 10 kVA). 347 V is the line-to-neutral derivative of a 600 V, 3-phase wye system used for lighting service. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis and voltage/service table; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "Incoming Power and Transformers" and LV service table |
| Allocation to facility (04-25 vs 03-25) | TBD. Accessible DBM source slices reference 13.8 kV→600 V step-down transformers generally and a "13.8 kV to 600V, 3 MVA" transformer for 03-25; neither DBM names tag `TXP-8600-1` nor a 2.5 MVA unit explicitly. Allocation to a specific electrical building or facility (04-25 Deepcut or 03-25 Comp and Liquids) is not confirmed by accessible source slices. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical building paragraphs; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "Incoming Power and Transformers" |
| Winding configuration / impedance / cooling class | TBD. Not stated in accessible source slices; defer to vendor data and Package Datasheet (`DEL-029-02`, if produced). | Source gap |
| Insulation type (oil-filled vs dry-type) | TBD. DBM notes large transformers are generally oil-filled and that LACT-area transformers may be dry-type, but the source set does not classify TXP-8600-1. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph |
| Secondary grounding | Each 600 V transformer shall be grounded by a 5 A continuous high-resistance grounding resistor; 600 V MCCs shall include power metering and ground/resistor fault detection; ground-fault protection on 600 V systems shall be alarm-only to maintain continuity of operations. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |
| Standby / emergency power interaction | Standby power on this facility is provided by LV standby generators connected at the 600 V MCC with transfer switches; transformer secondary is a 600 V bus that may interact with that standby scheme. Generator count/rating/load-shedding are TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, standby power paragraph; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "600V MCC and Standby Power" |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-029 and must be represented in the package interface requirements matrix. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-717D0187BA` |
| Grounding / Bonding | Interface fact applies to PKG-029 and must be represented in the package interface requirements matrix. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-C49653E450` |
| Area / Exterior Lighting | Interface fact applies to PKG-029 and must be represented in the package interface requirements matrix. (Secondary 347 V is consistent with 600/347 V lighting service derivation; package-specific lighting tie-in is TBD.) | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-DFC1A10C2D` |
| I&C / Control Cabling | Interface fact applies to PKG-029 and must be represented in the package interface requirements matrix. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-A5C9438164` |
| Communications / Network | Interface fact applies to PKG-029 and must be represented in the package interface requirements matrix. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-81CFD2A32C` |
| Maintenance Access | Interface fact applies to PKG-029 and must be represented in the package interface requirements matrix. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-2C14FA1228` |
| Structural / Foundations / Supports | Interface fact applies to PKG-029 and must be represented in the package interface requirements matrix. Large oil-filled transformers (if used) shall be spaced per CEC requirements and generally installed on structural steel transformer bases or precast concrete bearing foundations. Secondary containment requirements shall be reviewed. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` `IFC-380F4773FB`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph and foundations table |
| Grounding design basis | Major electrical equipment shall be directly connected to the ground grid at two points; ground wells at power transformers and electrical buildings shall be provided for maintenance and operational testing with bolted ground connections at test points; distribution transformers and panelboards shall have a separate copper ground conductor sized per CEC. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs |
| Cable / conduit routing | Secondary feeder from 600 V transformer secondary to plant 600 V MCC shall use ACWU; single-conductor cables avoided. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable type table |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering, design, vendor documentation, physical equipment supply | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-029` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-029` |
| Installation location | TBD. Source material describes electrical buildings that may house 13.8 kV switchgear and 600 V MCCs; it does not assign TXP-8600-1 to a specific electrical building, transformer pad, or facility. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Foundations / supports | Generally structural steel transformer bases or precast concrete bearing foundations; secondary containment shall be reviewed. Package-specific foundation design is TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph and foundations table |
| Vendor-engineered equipment package contents (windings, bushings, tap changer, cooling system, accessories, protection, monitoring) | TBD; vendor scope. | Source gap; no `26020-Package_Requirements.docx` heading for PKG-029 / TXP-8600-1 confirmed accessible in this run |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-029-04_vendor-engineered-equipment-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-029`.
- `ARTIFACT_REGISTER.csv`, rows `ART-D86EE0EF6E` and `ART-F831FA81A1` for `DEL-029-04_vendor-engineered-equipment-package`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-029` (`IFC-717D0187BA`, `IFC-C49653E450`, `IFC-DFC1A10C2D`, `IFC-A5C9438164`, `IFC-81CFD2A32C`, `IFC-2C14FA1228`, `IFC-380F4773FB`).
- `OBJECTIVE_DELIVERABLE_MAP.csv` / `OBJECTIVE_SCOPE_MAP.csv`, association of SOW-0030 / PKG-029 with OBJ-001 and supporting objectives.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 31.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices for distribution transformers, grounding/bonding, electrical buildings, standby power, cable/conduit, and foundations.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "Incoming Power and Transformers" and "600V MCC and Standby Power" source slices.
- `_Sources/26020-Package_Requirements.docx`, searched for a PKG-029 / TXP-8600-1 heading; no confirmed match accessed in this run.
