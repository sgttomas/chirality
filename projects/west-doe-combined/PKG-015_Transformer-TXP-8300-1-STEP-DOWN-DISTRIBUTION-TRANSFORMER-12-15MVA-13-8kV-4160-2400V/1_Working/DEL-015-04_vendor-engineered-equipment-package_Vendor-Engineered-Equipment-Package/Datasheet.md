# Datasheet: DEL-015-04_vendor-engineered-equipment-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-015-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Engineered Equipment Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-015` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8300-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 12/15MVA 13.8kV/4160/2400V | Workbook Packages row 17; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 15 / row 17 | Workbook Packages row 17; `PACKAGE_REGISTER.csv` |
| WBS | 02 | Workbook Packages row 17; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-02-30-006 | Workbook Packages row 17; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 17; `_CONTEXT.md` |
| Deliverable type | Vendor Package Production Unit | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-015` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package tag | TXP-8300-1 | Workbook Packages row 17; `PACKAGE_REGISTER.csv` |
| Equipment class | Step-down distribution transformer (vendor-owned Electrical package) | `PACKAGE_REGISTER.csv` row `PKG-015` |
| Rated capacity | 12/15 MVA (as carried in the package name) | Workbook Packages row 17; `PACKAGE_REGISTER.csv` |
| Primary voltage | 13.8 kV (as carried in the package name) | Workbook Packages row 17; `PACKAGE_REGISTER.csv` |
| Secondary voltage(s) | 4160 V and 2400 V (as carried in the package name) | Workbook Packages row 17; `PACKAGE_REGISTER.csv` |
| Source feed basis | Incoming power from 04-25 is 13.8 kV, 3-phase, 3-wire, 60 Hz LRG; main supply to 03-25 is sub-fed from the 04-25 13.8 kV Main Switchgear Electrical Building. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, voltage/service table; Incoming Power and Transformers section |
| Medium-voltage service basis | 4,160 V, 3-phase, 3-wire, 60 Hz LRG serves process AC inverter-drive motors from 250 hp to 5,500 hp via the 4160V MCC. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, voltage/service table; 4160V MCC section |
| Cooling class | TBD. The accessible source set does not state the transformer cooling class (e.g., ONAN/ONAF). | Source gap |
| Winding configuration / vector group | TBD. No vector group or winding configuration stated in accessible sources. | Source gap |
| Impedance, BIL, tap changer | TBD. No impedance, basic insulation level, or tap-changer configuration stated in accessible sources. | Source gap |
| Insulating medium | TBD. The accessible source set does not state whether the transformer is liquid-filled or dry-type. | Source gap |
| Quantity per package | 1 (as carried by package tag TXP-8300-1) | Workbook Packages row 17; ASSUMPTION based on single tag |
| 2400 V service basis | TBD. The DBM voltage/service table does not separately list a 2400 V service; the 2400 V secondary in the package name is not further defined by the accessible source slices. | Source gap; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, voltage/service table |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-015; vendor package shall accept 13.8 kV primary feed from upstream switchgear and deliver 4160 V and 2400 V secondary services per facility integration design. | Workbook Packages row 17; `INTERFACE_REGISTER.csv` `IFC-E8F09F1065`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Incoming Power and Transformers |
| Grounding / Bonding | Interface fact applies to PKG-015. Major electrical equipment shall be directly connected to the ground grid at two points; distribution transformers, panelboards, and three-phase motors larger than 100 hp require separate copper ground conductors per CEC sizing. | Workbook Packages row 17; `INTERFACE_REGISTER.csv` `IFC-073273FE3A`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` grounding/bonding paragraphs |
| Area / Exterior Lighting | Interface fact applies to PKG-015. Package shall coordinate exterior lighting tie-ins per facility lighting design. | Workbook Packages row 17; `INTERFACE_REGISTER.csv` `IFC-677CA55221` |
| I&C / Control Cabling | Interface fact applies to PKG-015. Power circuits at 13.8 kV, 4,160 V, and 600 V shall be separated from control and instrument circuits by distance, shielding, or routing as required to minimize interference. | Workbook Packages row 17; `INTERFACE_REGISTER.csv` `IFC-99831AAF77`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` power/control separation paragraph |
| Communications / Network | Interface fact applies to PKG-015. Communications/network tie-ins shall be coordinated through facility network design. | Workbook Packages row 17; `INTERFACE_REGISTER.csv` `IFC-6582D48513` |
| Maintenance Access | Interface fact applies to PKG-015. Cable tray and conduit routing shall not interfere with maintenance access. | Workbook Packages row 17; `INTERFACE_REGISTER.csv` `IFC-B9C22F51DB`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` cable/conduit paragraph |
| Structural / Foundations / Supports | Interface fact applies to PKG-015. Vendor shall provide transformer loading data sufficient for EPC foundation/support design. | Workbook Packages row 17; `INTERFACE_REGISTER.csv` `IFC-2646D74297` |
| Site environmental conditions | TBD. Site ambient temperature range, altitude, seismic, and wind/snow loading were not located in the accessible source slices for this deliverable. | Source gap |
| Hazardous-area classification | TBD. Area classification at the transformer location is not stated in the accessible source slices. | Source gap |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering, design, fabrication/supply, and the physical equipment package | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-015`; `DELIVERABLE_REGISTER.csv` row `DEL-015-04` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility (integration review on this deliverable). | `PACKAGE_REGISTER.csv` row `PKG-015`; `DELIVERABLE_REGISTER.csv` row `DEL-015-04` |
| Installation location | TBD. Accessible sources locate the broader 03-25 / 04-25 electrical buildings and switchgear but do not assign TXP-8300-1 to a specific pad, building, or yard location. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Incoming Power and Transformers |
| Foundations / supports | Structural / foundations / supports interface applies; transformer-specific foundation loads, anchor bolting, and oil-containment requirements are TBD pending vendor loading data and EPC civil/structural design. | Workbook Packages row 17; `INTERFACE_REGISTER.csv` `IFC-2646D74297` |
| Bushings, accessories, protective devices | TBD unless defined by vendor package data sheets and detailed design. | Source gap; no PKG-015-specific entry located in `_Sources/26020-Package_Requirements.docx` during this run. |
| Testing and factory acceptance | TBD. Factory routine, type, and special tests are not enumerated in accessible source slices and will be carried by the vendor design basis and datasheet set artifact. | Source gap; expected `ART-96A2C9D72C` content |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-015-04_vendor-engineered-equipment-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-015`.
- `ARTIFACT_REGISTER.csv`, rows `ART-365325DAB5` (Vendor engineered physical equipment package) and `ART-96A2C9D72C` (Vendor package design basis and datasheet set).
- `INTERFACE_REGISTER.csv`, rows for `PKG-015` (`IFC-E8F09F1065`, `IFC-073273FE3A`, `IFC-677CA55221`, `IFC-99831AAF77`, `IFC-6582D48513`, `IFC-B9C22F51DB`, `IFC-2646D74297`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-015-04_vendor-engineered-equipment-package` (OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 — ASSUMPTION via PACKAGE_HEURISTIC).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 17.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical voltage/service table, Incoming Power and Transformers, 4160V MCC, power/control separation, grounding/bonding, cable tray/conduit slices.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific transformer content; no PKG-015-specific match located during this run.
- Sibling deliverables `DEL-015-01_scope-of-work` (EPC Scope of Work) and `DEL-015-02_package-datasheet` (EPC Package Datasheet) are the cited upstream EPC anchors for this vendor production unit.
