# Datasheet: DEL-031-04_vendor-engineered-equipment-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-031-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Engineered Equipment Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-031` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8500-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 3MVA 13.8kV/600/347V | Workbook Packages row 33; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 31 / row 33 | Workbook Packages row 33; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` row `PKG-031` |
| CoA tracking number | 26020-01-30-022 | `PACKAGE_REGISTER.csv` row `PKG-031` |
| Discipline | Electrical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable type | Vendor Package Production Unit | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-031` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-031` |
| Package function | Step-down distribution transformer (single transformer, equipment tag TXP-8500-1) feeding a 600 V MCC for low-voltage facility loads. | Workbook Packages row 33; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "Incoming Power and Transformers" table (line ~745: "13.8 kV to 600V, 3 MVA transformer — 600V MCC for LV loads") |
| Nameplate rating (workbook title) | 3 MVA, 13.8 kV primary, 600/347 V secondary | Workbook Packages row 33; `PACKAGE_REGISTER.csv` row `PKG-031` |
| Equipment tag | TXP-8500-1 | Workbook Packages row 33 |
| Service basis (general) | Radial step-down from the 13.8 kV plant distribution bus to a 600 V low-voltage system serving facility low-voltage loads (motors 3/4 hp to 250 hp DOL, lighting/utility distribution transformers, building heaters, UPS larger than 10 kVA). 347 V is the line-to-neutral derivative of the 600 V, 3-phase wye system used for lighting service. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis voltage/service table (lines ~2917-2937); `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "Incoming Power and Transformers" and LV service table |
| Likely facility allocation | PROPOSAL: PKG-031 / TXP-8500-1 corresponds to the 03-25 "13.8 kV to 600V, 3 MVA transformer" feeding the 03-25 600 V MCC (the only 3 MVA 13.8/600 V transformer named in accessible DBM source slices). The DBM does not state the equipment tag, so this is an ASSUMPTION pending EPC Package Datasheet (`DEL-031-02`) confirmation. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "Incoming Power and Transformers" table |
| Upstream supply | 13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded (LRG) feed from the 04-25 13.8 kV Main Switchgear Electrical Building (sub-fed to 03-25 for the 3 MVA transformer use case). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, medium-voltage services and 13.8 kV switchgear distribution paragraphs; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "Incoming Power and Transformers" |
| Downstream load | 600 V MCC (LV loads), with 347 V available as line-to-neutral on the secondary wye for facility lighting and utility distribution feeds. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "Incoming Power and Transformers" and "600V MCC and Standby Power" |
| Winding configuration / impedance / cooling class | TBD. Not stated in accessible source slices; defer to vendor data and the EPC Package Datasheet (`DEL-031-02`). | Source gap |
| Insulation type (oil-filled vs dry-type) | TBD. DBM notes large transformers are generally oil-filled, that LACT-area transformers may be dry-type, and lists a 480 V dry-type transformer for the LACT facility-side feed; the source set does not classify TXP-8500-1. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "Incoming Power and Transformers" |
| Secondary grounding | Each 600 V transformer secondary shall be grounded by a 5 A continuous high-resistance grounding resistor; 600 V MCCs shall include ground/resistor fault detection; ground-fault protection on 600 V systems shall be alarm-only to maintain continuity of operations. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |
| Standby / emergency power interaction | Standby power on this facility is provided by LV standby natural-gas generators connected at the 600 V MCC with transfer switches; transformer secondary 600 V bus may interact with that standby scheme. Generator count/rating, transfer-switch type, emergency bus configuration, and load-shedding/critical-load list remain `TBD`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, standby power paragraph; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "600V MCC and Standby Power" |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-031 and must be represented in the package interface requirements matrix. | Workbook Packages row 33; `INTERFACE_REGISTER.csv` `IFC-E6C51663E5` |
| Grounding / Bonding | Interface fact applies to PKG-031 and must be represented in the package interface requirements matrix. | Workbook Packages row 33; `INTERFACE_REGISTER.csv` `IFC-2DE626B361` |
| Area / Exterior Lighting | Interface fact applies to PKG-031 and must be represented in the package interface requirements matrix. Secondary 347 V is consistent with 600/347 V lighting service derivation; package-specific lighting tie-in is `TBD`. | Workbook Packages row 33; `INTERFACE_REGISTER.csv` `IFC-9BF05B6DCC` |
| I&C / Control Cabling | Interface fact applies to PKG-031 and must be represented in the package interface requirements matrix. | Workbook Packages row 33; `INTERFACE_REGISTER.csv` `IFC-5DCD93CE40` |
| Communications / Network | Interface fact applies to PKG-031 and must be represented in the package interface requirements matrix. | Workbook Packages row 33; `INTERFACE_REGISTER.csv` `IFC-452A0203CB` |
| Maintenance Access | Interface fact applies to PKG-031 and must be represented in the package interface requirements matrix. | Workbook Packages row 33; `INTERFACE_REGISTER.csv` `IFC-3A6221E4CB` |
| Structural / Foundations / Supports | Interface fact applies to PKG-031 and must be represented in the package interface requirements matrix. Large oil-filled transformers (if used) shall be spaced per CEC requirements and generally installed on structural-steel transformer bases or precast concrete bearing foundations; secondary containment shall be reviewed. | Workbook Packages row 33; `INTERFACE_REGISTER.csv` `IFC-15FCC571C7`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph and foundations table |
| Grounding design basis | Major electrical equipment shall be directly connected to the ground grid at two points; ground wells at power transformers and electrical buildings shall be provided for maintenance and operational testing with bolted ground connections at test points; distribution transformers and panelboards shall have a separate copper ground conductor sized per CEC. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs (incl. line ~2991) |
| Cable / conduit basis | Secondary feeder from the 600 V transformer secondary to the 600 V MCC shall use ACWU cable; single-conductor cables avoided. Medium-voltage primary feeder (13.8 kV) basis is three-conductor copper TECK rated 15 kV with 133 percent insulation, shielded, where supplied or terminated at this package. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable type table and MV cable paragraph |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering, design, vendor documentation, physical equipment supply | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-031` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-031` |
| Installation location | TBD. Source material describes electrical buildings that may house 13.8 kV switchgear, 600 V MCCs, and distribution transformers; it does not assign TXP-8500-1 to a specific electrical building, transformer pad, or facility (working ASSUMPTION: 03-25 facility based on the DBM 3 MVA transformer entry). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "Incoming Power and Transformers" |
| Foundations / supports | Generally structural-steel transformer bases or precast concrete bearing foundations; secondary containment shall be reviewed. Package-specific foundation design is `TBD`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph and foundations table |
| Vendor-engineered equipment package contents (windings, bushings, tap changer, cooling system, accessories, protection, monitoring) | TBD; vendor scope. | Source gap; no `26020-Package_Requirements.docx` heading for PKG-031 / TXP-8500-1 confirmed accessible in this run |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-031-04_vendor-engineered-equipment-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-031`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-031` (`IFC-E6C51663E5`, `IFC-2DE626B361`, `IFC-9BF05B6DCC`, `IFC-5DCD93CE40`, `IFC-452A0203CB`, `IFC-3A6221E4CB`, `IFC-15FCC571C7`).
- `ARTIFACT_REGISTER.csv`, rows for `PKG-031` (vendor engineered physical equipment package; vendor package design basis and datasheet set).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, association of `SOW-0032` / PKG-031 with OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 33.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices for distribution transformers, grounding/bonding, electrical buildings, standby power, cable/conduit, and foundations.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "Incoming Power and Transformers" (line ~745) and "600V MCC and Standby Power" source slices.
- `_Sources/26020-Package_Requirements.docx`, searched for a PKG-031 / TXP-8500-1 heading; no confirmed match accessed in this run.
- Sibling EPC deliverables: `DEL-031-01_scope-of-work`, `DEL-031-02_package-datasheet` (vendor engineering inputs); `DEL-031-03_construction-work-package` (installation/turnover); `DEL-031-05_vendor-document-turnover-package`, `DEL-031-06_epc-vendor-package-review-and-acceptance` (downstream integration).
