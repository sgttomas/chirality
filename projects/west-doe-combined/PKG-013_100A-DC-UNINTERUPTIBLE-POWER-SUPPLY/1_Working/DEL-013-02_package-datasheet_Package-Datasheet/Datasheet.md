# Datasheet: DEL-013-02_package-datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-013-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-013` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 100A DC UNINTERUPTIBLE POWER SUPPLY | Workbook Packages row 15; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 13 / row 15 | Workbook Packages row 15; `PACKAGE_REGISTER.csv` |
| WBS | 02 | Workbook Packages row 15; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-02-30-004 | Workbook Packages row 15; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 15; `_CONTEXT.md` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-013` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-013` |
| Package function | 100A DC uninterruptible power supply package | Workbook Packages row 15 |
| UPS service basis | 120 VAC / 125 VDC UPS services support the control system, selected emergency or critical lighting, medium-voltage breaker control circuits, and medium-voltage protective relays. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis, voltage and service table |
| UPS count / rating | TBD. The source table identifies an "Uninterruptible Power Supply" quantity of 2, but the package-specific allocation to PKG-013 and rating details are not confirmed by an accessible package-specific source slice. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, equipment list; Workbook Packages row 15 |
| Source power supply | TBD. DBM states low-voltage and lighting/utility service bases, but no package-specific feeder, charger, battery, autonomy, or distribution data is available for this deliverable. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis |
| Standby power interface | Standby power shall support critical systems during an outage or turnaround, including UPS systems; detailed generator, transfer, load-shedding, and sequencing requirements are TBD pending electrical studies and TOU standard confirmation. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, standby power paragraph |
| Electrical building interface | Electrical buildings may house 120 V AC UPS systems with battery banks and distribution panels and 125 V DC UPS systems with battery banks and distribution panels, as required by detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-013 and must be represented in the package interface requirements matrix. | Workbook Packages row 15; `INTERFACE_REGISTER.csv` `IFC-3B1ED82A25` |
| Grounding / Bonding | Interface fact applies to PKG-013 and must be represented in the package interface requirements matrix. | Workbook Packages row 15; `INTERFACE_REGISTER.csv` `IFC-8093ECDA51` |
| Maintenance Access | Interface fact applies to PKG-013 and must be represented in the package interface requirements matrix. | Workbook Packages row 15; `INTERFACE_REGISTER.csv` `IFC-DA9E0BAB70` |
| Structural / Foundations / Supports | Interface fact applies to PKG-013 and must be represented in the package interface requirements matrix. | Workbook Packages row 15; `INTERFACE_REGISTER.csv` `IFC-CAE19AED68` |
| Grounding design basis | Major electrical equipment shall be directly connected to the ground grid at two points; distribution transformers, panelboards, and three-phase motors larger than 100 hp require separate copper ground conductors per CEC sizing. Applicability to this UPS package shall be confirmed by detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |
| Cable / conduit routing | Cable tray and conduit routing shall not interfere with maintenance access. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-013` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-013` |
| Installation location | TBD. Source material confirms possible electrical-building UPS systems but does not assign PKG-013 to a specific building, room, skid, or outdoor location. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |
| Foundations / supports | Structural / foundations / supports interface applies; package-specific support basis is TBD. | Workbook Packages row 15; `INTERFACE_REGISTER.csv` |
| Battery bank, charger, distribution panels, protective devices | TBD unless defined by vendor package data and detailed design. | Source gap; `26020-Package_Requirements.docx` has no accessible PKG-013 package match |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-013-02_package-datasheet`.
- `PACKAGE_REGISTER.csv`, row `PKG-013`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-013-02_package-datasheet`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-013`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-013-02_package-datasheet`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 15.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis source slices for UPS services, standby power, electrical buildings, grounding, cable tray, and conduit.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical package deliverable and utility interface source slices.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific UPS content; no PKG-013 match found.
