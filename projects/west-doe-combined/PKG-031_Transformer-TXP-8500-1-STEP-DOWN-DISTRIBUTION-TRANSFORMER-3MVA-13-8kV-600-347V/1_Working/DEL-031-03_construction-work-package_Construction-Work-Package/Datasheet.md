# Datasheet: DEL-031-03_construction-work-package — Construction Work Package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-031-03_construction-work-package` | `_CONTEXT.md` |
| Deliverable name | Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-031` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8500-1 — STEP DOWN DISTRIBUTION TRANSFORMER — 3MVA 13.8kV/600/347V | Workbook Packages row 33; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 31 / row 33 | `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-022 | `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable type | EPC Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Covers scope items | `SOW-0032` | `DELIVERABLE_REGISTER.csv` |
| Supports objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION: package-grouping heuristic) | `DELIVERABLE_REGISTER.csv`; `OBJECTIVE_DELIVERABLE_MAP.csv` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, and procurement/construction coordination. | `PACKAGE_REGISTER.csv` row `PKG-031` |
| Package function | 3 MVA, 13.8 kV / 600 V step-down distribution transformer feeding the 600 V MCC for low-voltage loads. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 745 ("13.8 kV to 600V, 3 MVA transformer → 600V MCC for LV loads"); Workbook Packages row 33 |
| Tagged equipment | TXP-8500-1 | Workbook Packages row 33 (package name) |
| Construction scope basis | Field construction assigned to Tourmaline Oil Corporation: includes off-loading, setting on foundations, mechanical hookup, installation of shipped-loose items, electrical terminations, home-run cabling, structural supports, and demolition where required. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section (lines 101-125) |
| Cross-discipline coordination | Package buildings, MCC interfaces, RIO interfaces, heat tracing, HVAC, fire/gas detection, and drain/vent tie-ins shall be coordinated with civil, electrical, controls, and instrumentation sections of the DBM. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 619 |
| Tie-in coordination | Joint planning required for tie-ins to existing or related facilities; tie-in timing to be established as the project progresses. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 127 |
| Construction work package register alignment | Final miscellaneous facilities list shall be aligned to plot plan, equipment list, and construction work package register before issue for construction. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 661 |

## Conditions

| Interface / condition | Datasheet basis | Source |
|---|---|---|
| Electrical Power | Tie-in to 13.8 kV primary feeder and 600 V MCC secondary feeder. | `INTERFACE_REGISTER.csv` `IFC-E6C51663E5`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 745 |
| Grounding / Bonding | Major electrical equipment shall be directly connected to the ground grid at two points; distribution transformers require separate copper ground conductors per CEC sizing. | `INTERFACE_REGISTER.csv` `IFC-2DE626B361`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |
| Area / Exterior Lighting | Construction-managed area lighting interface applies. | `INTERFACE_REGISTER.csv` `IFC-9BF05B6DCC`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 120 |
| I&C / Control Cabling | Control and instrument circuits shall be separated from 13.8 kV / 4,160 V / 600 V power circuits by distance, shielding, or routing per project electrical specifications. | `INTERFACE_REGISTER.csv` `IFC-5DCD93CE40`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 768 |
| Communications / Network | Network/comm cabling tie-in required; detailed routing TBD. | `INTERFACE_REGISTER.csv` `IFC-452A0203CB` |
| Maintenance Access | Cable tray and conduit routing shall not interfere with maintenance access. | `INTERFACE_REGISTER.csv` `IFC-3A6221E4CB`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs |
| Structural / Foundations / Supports | Foundation selection, pile design, settlement criteria, frost protection, and structural support requirements shall be confirmed against final geotechnical report. | `INTERFACE_REGISTER.csv` `IFC-15FCC571C7`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 141 |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Off-loading and setting | Tourmaline field construction scope: off-loading at site; setting on foundations. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, lines 112-113 |
| Mechanical hookup | Field-construction hookup of equipment and interconnecting piping (cooling, grounding rails as applicable). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 114 |
| Shipped-loose installation | Installation of shipped-loose instruments, valves, components. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 115 |
| Home-run cabling and terminations | Field installation of home-run cables; electrical terminations to 13.8 kV primary and 600 V secondary. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, lines 118-119 |
| Local control stations | One local control station shall be installed adjacent to each motor (downstream MCC scope); hard-wired back to MCC starter circuit by field construction contractor. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 760 |
| Demolition / removal | Performed by Tourmaline field construction where required by tie-ins. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 125 |
| Installation location | TBD. Source confirms 13.8 kV → 600 V transformer feeds 600 V MCC, but specific outdoor/skid/electrical-building assignment for TXP-8500-1 is not identified in accessible source slices. | Source gap |
| Foundation / pad design | TBD pending acceptance of final geotechnical report; treat geotechnical values as design placeholders until accepted. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 141 |
| Construction-particulate filtration | TBD; not explicitly defined for this package. | Source gap |
| Inspection and turnover | TBD; vendor factory/shop test and inspection evidence is produced by `DEL-031-06`; package-acceptance and turnover checklist artifact (`ART-273816BADA`) is the in-scope evidence for this deliverable. | `ARTIFACT_REGISTER.csv` rows for `DEL-031-03` and `DEL-031-06` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-031-03_construction-work-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-031`.
- `ARTIFACT_REGISTER.csv`, rows `ART-7627442199`, `ART-F476EFD32E`, `ART-273816BADA`.
- `INTERFACE_REGISTER.csv`, rows `IFC-E6C51663E5`, `IFC-2DE626B361`, `IFC-9BF05B6DCC`, `IFC-5DCD93CE40`, `IFC-452A0203CB`, `IFC-3A6221E4CB`, `IFC-15FCC571C7`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-031-03` (package-grouping heuristic).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 33.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility (lines 101-127); electrical 13.8 kV / 600 V transformer slice (line 745); MCC and local control stations (line 760); power/control cable separation (line 768); grounding and cable tray paragraphs.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Construction Scope Summary (line 73-75); geotechnical placeholder (line 141); package coordination (line 619); CWP register alignment (line 661).
- `_Sources/26020-Package_Requirements.docx`, no PKG-031-specific package-requirements slice was identified during this run.
