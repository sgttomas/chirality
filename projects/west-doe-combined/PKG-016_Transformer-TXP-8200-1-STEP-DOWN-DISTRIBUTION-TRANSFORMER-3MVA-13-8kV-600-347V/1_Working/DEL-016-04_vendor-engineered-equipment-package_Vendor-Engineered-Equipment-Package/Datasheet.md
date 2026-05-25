# Datasheet: DEL-016-04_vendor-engineered-equipment-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-016-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Engineered Equipment Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-016` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 3MVA 13.8kV/600/347V | Workbook Packages row 18; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 16 / row 18 | Workbook Packages row 18; `PACKAGE_REGISTER.csv` |
| WBS | 02 | Workbook Packages row 18; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-02-30-007 | Workbook Packages row 18; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 18; `_CONTEXT.md` |
| Deliverable type | Vendor Package Production Unit | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-016` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package tag | TXP-8200-1 | Workbook Packages row 18; `PACKAGE_REGISTER.csv` |
| Equipment class | Step-down distribution transformer (vendor-owned Electrical package) | `PACKAGE_REGISTER.csv` row `PKG-016` |
| Rated capacity | 3 MVA (as carried in the package name) | Workbook Packages row 18; `PACKAGE_REGISTER.csv`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Incoming Power and Transformers ("13.8 kV to 600V, 3 MVA transformer") |
| Primary voltage | 13.8 kV (as carried in the package name) | Workbook Packages row 18; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` voltage/service table; Incoming Power and Transformers |
| Secondary voltage(s) | 600 V / 347 V (as carried in the package name) | Workbook Packages row 18; `PACKAGE_REGISTER.csv` |
| Source feed basis | Incoming power from 04-25 is 13.8 kV, 3-phase, 3-wire, 60 Hz LRG; main supply to 03-25 is sub-fed from the 04-25 13.8 kV Main Switchgear Electrical Building. The 13.8 kV to 600 V, 3 MVA transformer feeds the 600 V MCC for LV loads. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, voltage/service table; Incoming Power and Transformers section |
| Low-voltage service basis | 600 V, 3 phase, 3 wire, 60 Hz HRG with 5 A continuous resistor; serves motors 3/4 hp through 250 hp, DOL starting, lighting transformers, building heaters, and UPS larger than 10 kVA. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, voltage/service table |
| 347 V service basis | TBD. The DBM voltage/service table does not separately enumerate a 347 V service. ASSUMPTION: 347 V represents the line-to-neutral derivation of a 600 V system, consistent with Canadian distribution practice, but the configuration is not stated in the accessible source slices. | Source gap; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, voltage/service table |
| Cooling class | TBD. The accessible source set does not state the transformer cooling class (e.g., ONAN/ONAF or dry-type AN/AFA). | Source gap |
| Insulating medium | TBD. The accessible source set does not state whether the transformer is liquid-filled or dry-type. | Source gap |
| Winding configuration / vector group | TBD. No vector group or winding configuration stated in accessible sources. | Source gap |
| Impedance, BIL, tap changer | TBD. No impedance, basic insulation level, or tap-changer configuration stated in accessible sources. | Source gap |
| Quantity per package | 1 (as carried by package tag TXP-8200-1) | Workbook Packages row 18; ASSUMPTION based on single tag |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-016; vendor package shall accept 13.8 kV primary feed from upstream switchgear and deliver 600 V (and 347 V) secondary service per facility integration design. | Workbook Packages row 18; `INTERFACE_REGISTER.csv` `IFC-0C63CABBEC`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Incoming Power and Transformers |
| Grounding / Bonding | Interface fact applies to PKG-016. Major electrical equipment shall be directly connected to the ground grid at two points; distribution transformers, panelboards, and three-phase motors larger than 100 hp require separate copper ground conductors per CEC sizing. | Workbook Packages row 18; `INTERFACE_REGISTER.csv` `IFC-C4343B4BCA`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` grounding/bonding paragraphs |
| Area / Exterior Lighting | Interface fact applies to PKG-016. Package shall coordinate exterior lighting tie-ins per facility lighting design. | Workbook Packages row 18; `INTERFACE_REGISTER.csv` `IFC-C649F648C5` |
| I&C / Control Cabling | Interface fact applies to PKG-016. Power circuits at 13.8 kV, 4,160 V, and 600 V shall be separated from control and instrument circuits by distance, shielding, or routing as required to minimize interference. | Workbook Packages row 18; `INTERFACE_REGISTER.csv` `IFC-AC26461656`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` power/control separation paragraph |
| Communications / Network | Interface fact applies to PKG-016. Communications/network tie-ins (e.g., monitoring, alarming) shall be coordinated through facility network design. | Workbook Packages row 18; `INTERFACE_REGISTER.csv` `IFC-D3B7348DC6` |
| Maintenance Access | Interface fact applies to PKG-016. Cable tray and conduit routing shall not interfere with maintenance access. | Workbook Packages row 18; `INTERFACE_REGISTER.csv` `IFC-4A94795733`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` cable/conduit paragraph |
| Structural / Foundations / Supports | Interface fact applies to PKG-016. Vendor shall provide transformer loading data sufficient for EPC foundation/support design. | Workbook Packages row 18; `INTERFACE_REGISTER.csv` `IFC-E3BE98E89B` |
| Site environmental conditions | TBD. Site ambient temperature range, altitude, seismic, and wind/snow loading were not located in the accessible source slices for this deliverable. | Source gap |
| Hazardous-area classification | TBD. Area classification at the transformer location is not stated in the accessible source slices. General DBM basis is Class I Zone 2, Gas Groups IIA and IIB for the facility, with non-process areas treated as general-purpose unless drawings classify otherwise. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Area Classification |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering, design, fabrication/supply, and the physical equipment package | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-016`; `DELIVERABLE_REGISTER.csv` row `DEL-016-04` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility (integration review on this deliverable). | `PACKAGE_REGISTER.csv` row `PKG-016`; `DELIVERABLE_REGISTER.csv` row `DEL-016-04` |
| Installation location | TBD. Accessible sources locate the broader 03-25 / 04-25 electrical buildings and switchgear but do not assign TXP-8200-1 to a specific pad, building, or yard location. The 600 V MCC fed by this transformer is associated with the LV loads of 03-25. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Incoming Power and Transformers; 600V MCC and Standby Power |
| Foundations / supports | Structural / foundations / supports interface applies; transformer-specific foundation loads, anchor bolting, and (if liquid-filled) oil-containment requirements are TBD pending vendor loading data and EPC civil/structural design. | Workbook Packages row 18; `INTERFACE_REGISTER.csv` `IFC-E3BE98E89B` |
| Bushings, accessories, protective devices | TBD unless defined by vendor package data sheets and detailed design. | Source gap; no PKG-016-specific entry located in `_Sources/26020-Package_Requirements.docx` during this run. |
| Testing and factory acceptance | TBD. Factory routine, type, and special tests are not enumerated in accessible source slices and will be carried by the vendor design basis and datasheet set artifact. | Source gap; expected `ART-13F6F3D6B6` content |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-016-04_vendor-engineered-equipment-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-016`.
- `ARTIFACT_REGISTER.csv`, rows `ART-AC4469EC25` (Vendor engineered physical equipment package) and `ART-13F6F3D6B6` (Vendor package design basis and datasheet set).
- `INTERFACE_REGISTER.csv`, rows for `PKG-016` (`IFC-0C63CABBEC`, `IFC-C4343B4BCA`, `IFC-C649F648C5`, `IFC-AC26461656`, `IFC-D3B7348DC6`, `IFC-4A94795733`, `IFC-E3BE98E89B`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-016-04_vendor-engineered-equipment-package` (OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 — ASSUMPTION via PACKAGE_HEURISTIC).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 18.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical voltage/service table, Incoming Power and Transformers (13.8 kV to 600 V, 3 MVA transformer), 600V MCC and Standby Power, Area Classification, power/control separation, grounding/bonding, cable tray/conduit slices.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific transformer content; no PKG-016-specific match located during this run.
- Sibling deliverables `DEL-016-01_scope-of-work` (EPC Scope of Work) and `DEL-016-02_package-datasheet` (EPC Package Datasheet) are the cited upstream EPC anchors for this vendor production unit.
