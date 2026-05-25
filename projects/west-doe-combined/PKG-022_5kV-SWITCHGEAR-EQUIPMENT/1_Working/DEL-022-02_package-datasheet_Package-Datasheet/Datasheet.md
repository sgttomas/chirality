# Datasheet: DEL-022-02_package-datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-022-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-022` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 5kV SWITCHGEAR EQUIPMENT | Workbook Packages row 24; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 22 / row 24 | Workbook Packages row 24; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 24; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-013 | Workbook Packages row 24; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 24; `_CONTEXT.md` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-022` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package under WBS 01 | `PACKAGE_REGISTER.csv` row `PKG-022` |
| Package function | Medium-voltage switchgear equipment package serving the facility electrical distribution scope. | Workbook Packages row 24 |
| Governing equipment specification | Medium Voltage Switchgear specification `ELC-QAS-000007-001`, Revision 1, listed in DBM Table 12-1 as governing electrical equipment procurement basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical and instrumentation specifications table |
| Equipment-list count | DBM equipment list identifies "Medium Voltage Switchgear" quantity 1 and includes "810-1 13.8kV Switchgear Electrical Building" (shop). Allocation of these line items to `PKG-022` is not confirmed by an accessible source slice. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, equipment list and electrical building list |
| Nominal voltage rating | TBD. The package title "5kV SWITCHGEAR EQUIPMENT" is not literally reproduced in the accessible DBM source slices. The DBM medium-voltage backbone is 13.8 kV; medium-voltage process services are 6.9 kV and 4.160 kV; only 4.160 kV cables are rated at "5 kV with 100 percent insulation" in the DBM cable table. See Guidance Conflict Table. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, system voltages and cable specifications tables |
| Service basis | Medium-voltage switchgear (per ELC-QAS-000007-001 designation) provides medium-voltage power distribution; specific bus assignment, ampacity, short-circuit rating, configuration, and electrical-building assignment for `PKG-022` are TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, plant power distribution and electrical buildings paragraphs |
| Electrical building interface | Electrical buildings may house "13.8 kV main switchgear, medium-voltage motor control centers, medium-voltage reduced-voltage soft starters, medium-voltage VFDs, 600 V MCCs, …", as required by detailed design. Assignment of `PKG-022` to a specific electrical building is TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Protective relay / control power interface | Medium-voltage breaker control circuits and medium-voltage protective relays are fed from the facility 120 VAC / 125 VDC UPS services. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, UPS services row of system voltages table |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-022 and must be represented in the package interface requirements matrix. | Workbook Packages row 24; `INTERFACE_REGISTER.csv` `IFC-FAD0C5C924` |
| Grounding / Bonding | Interface fact applies to PKG-022 and must be represented in the package interface requirements matrix. | Workbook Packages row 24; `INTERFACE_REGISTER.csv` `IFC-291807A33B` |
| I&C / Control Cabling | Interface fact applies to PKG-022 and must be represented in the package interface requirements matrix. | Workbook Packages row 24; `INTERFACE_REGISTER.csv` `IFC-FFD6E87354` |
| Communications / Network | Interface fact applies to PKG-022 and must be represented in the package interface requirements matrix. | Workbook Packages row 24; `INTERFACE_REGISTER.csv` `IFC-652BE03197` |
| Maintenance Access | Interface fact applies to PKG-022 and must be represented in the package interface requirements matrix. | Workbook Packages row 24; `INTERFACE_REGISTER.csv` `IFC-53BEFBC3CA` |
| Structural / Foundations / Supports | Interface fact applies to PKG-022 and must be represented in the package interface requirements matrix. | Workbook Packages row 24; `INTERFACE_REGISTER.csv` `IFC-ED54C3FD1A` |
| Grounding design basis | All major electrical equipment shall be directly connected to the ground grid at two points; ground wells at electrical buildings shall be provided; distribution transformers, panelboards, and three-phase motors larger than 100 hp require separate copper ground conductors per CEC sizing. Package-specific grounding shall be coordinated with the facility basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |
| Cable / conduit routing | Cable tray and conduit routing shall not interfere with maintenance access. MV power cables shall use shielded three-conductor copper TECK cable per DBM cable specification table (insulation class TBD pending nominal voltage confirmation for `PKG-022`). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable, wire, and raceways section and cable specifications table |
| Control / network connectivity | Switchgear protection and control shall provide control and communication connectivity consistent with the facility controls architecture (DBM identifies Ethernet ports on MV MCCs to the plant PLC central control panel; switchgear-specific provisions are TBD). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, motor control and motor specifications paragraphs |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-022` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-022` |
| Installation location | TBD. Source identifies multiple electrical buildings that house switchgear (for example, "810-1 13.8kV Switchgear Electrical Building", "830-1 4.16kV Acid Gas / Overheads Compressor Electrical Building"), but does not assign `PKG-022` to a specific building, lineup, or room. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings list |
| Foundations / supports | Structural / foundations / supports interface applies; package-specific support basis is TBD. Electrical buildings are elevated on piles with bottom-entry cabling per DBM electrical building basis. | Workbook Packages row 24; `INTERFACE_REGISTER.csv`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Bus configuration, ratings, breaker complement, protection scheme | TBD unless defined by vendor package data, detailed engineering, and the governing medium-voltage switchgear specification. | Source gap; `26020-Package_Requirements.docx` package-specific match for PKG-022 not confirmed accessible |
| Shop versus field execution | DBM equipment-building list flags switchgear electrical buildings as "Shop". Package-specific shop/field execution for `PKG-022` to be confirmed during detailed engineering. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical building shop/field list |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-022-02_package-datasheet`.
- `PACKAGE_REGISTER.csv`, row `PKG-022`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-022-02_package-datasheet`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-022`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-022-02_package-datasheet`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 24.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices for plant power distribution, system voltages, standby power, electrical buildings, grounding/bonding, cable/wire/raceways, motor control, and the governing electrical specifications table.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, cross-facility electrical interface context (03-25 sub-feed from 04-25 13.8 kV Main Switchgear).
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific MV switchgear content; no `PKG-022` package-specific match has been confirmed accessible.
