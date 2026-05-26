# Datasheet — DEL-058-04 Vendor Engineered Equipment Package (Medium Pressure Flash Feed Separator)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-058-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Name | Vendor Engineered Equipment Package | `_CONTEXT.md` |
| ParentPackageID | `PKG-058` | `_CONTEXT.md` |
| Package Name | Medium Pressure Flash Feed Separator | `_CONTEXT.md` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | Vendor Package Production Unit | `_CONTEXT.md` |
| Responsible Party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md` |
| Tagged Equipment | MEDIUM PRESSURE FLASH FEED SEPARATOR (x2); MEDIUM PRESSURE F.F. HCL HEATER BUNDLE (x2) | DBM-Deepcut `4-25_Deepcut_DBM.md` (Equipment Schedule, Workbook Packages row 71) |
| Vessel tags | V-7110-1, V-7310-1 (and stabilizer flash feed V-7210-1 / V-7410-1, downstream — not in scope of this vessel set) | DBM-Deepcut `4-25_Deepcut_DBM.md` (Equipment list and Equipment Schedule line 52-53) |
| Heater bundle tag | E-7120-1 (and parallel) | DBM-Deepcut `4-25_Deepcut_DBM.md` (Equipment Schedule line 53) |
| Modules | 710-1 Medium Pressure Flash Feed Module; 730-1 Medium Pressure Flash Feed Module | DBM-Deepcut `4-25_Deepcut_DBM.md` (Module/Shop assignment table) |
| Sparing Basis | 2 x 100% normal operating sparing; no sparing for off-design line-pack maximum-flow case | DBM-Deepcut `4-25_Deepcut_DBM.md` (MPFF and Stabilizer Train Relationship; Sparing table "Medium Pressure Flash Feed Packages: 2, 100%, 200%") |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| MPFF design pressure (kPag) | 1724 | DBM-Deepcut `4-25_Deepcut_DBM.md` (MPFF Operating and Capacity Basis) |
| MPFF expected normal operating pressure (kPag) | 1724 | DBM-Deepcut `4-25_Deepcut_DBM.md` (MPFF Operating and Capacity Basis) |
| MPFF low operating pressure (kPag) | TBD | DBM-Deepcut `4-25_Deepcut_DBM.md` (MPFF Operating and Capacity Basis) |
| MPFF expected high operating pressure (kPag) | TBD | DBM-Deepcut `4-25_Deepcut_DBM.md` (MPFF Operating and Capacity Basis) |
| MPFF assumed design operating temperature (deg C) | 40 (ASSUMPTION: pending detailed engineering confirmation) | DBM-Deepcut `4-25_Deepcut_DBM.md` (MPFF feed conditions) |
| Internals | Mistex (no internal coating specified) | DBM-Deepcut `4-25_Deepcut_DBM.md` (MPFF feed conditions) |
| Minimum liquid residence time | At least 10 minutes between weir height and NLL-interface | DBM-Deepcut `4-25_Deepcut_DBM.md` (MPFF feed conditions) |
| Overhead vapour disposition | Pressure-regulated to SOC third-stage suction | DBM-Deepcut `4-25_Deepcut_DBM.md` (MPFF feed conditions) |
| Purge gas service | LP fuel gas (post fuel-gas scrubber), regulated to maintain MPFF pressure above downstream stabilizer flash/feed separator; available for sour-gas sweeping | DBM-Deepcut `4-25_Deepcut_DBM.md` (MPFF feed conditions) |
| Blowdown | Automated blowdown valve required; relief/blowdown route TBD (note: stabilizer flash/feed routes to HP flare; MPFF relief routing not explicitly stated) | DBM-Deepcut `4-25_Deepcut_DBM.md` (MPFF feed conditions; Relief and blowdown paragraph) |
| Building enclosure | Self-framing building enclosing instrumentation and one end of the vessel (configured similarly to inlet separator) | DBM-Deepcut `4-25_Deepcut_DBM.md` (MPFF feed conditions) |
| Site basis — minimum ambient | -40 deg C minimum (governs exposed equipment, package buildings, control panels, instrumentation, field devices) | DBM-Comp_and_Liquids `3-25_Comp_and_Liquids_DBM.md` (Site basis section) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Feed source | High-pressure hydrocarbon liquid from inlet separators via common header, level-controlled into MPFF vessels, pre-heated through upstream inlet-separator liquid outlet heater before MPFF LCV | DBM-Deepcut `4-25_Deepcut_DBM.md` (MPFF feed conditions) |
| MPFF inlet temperatures | TBD/TBC following upstream HEX installation and thermal reassessment | DBM-Deepcut `4-25_Deepcut_DBM.md` (MPFF feed conditions) |
| Methanol injection upstream of MPFF inlet LCV | Retained as safeguard pending confirmation of upstream HEX outlet temperatures vs hydrate suppression margins | DBM-Deepcut `4-25_Deepcut_DBM.md` (MPFF feed conditions) |
| Flow values (per separator) | Low/Expected normal/Design/Maximum — values TBD in source table (per-MPFF basis) | DBM-Deepcut `4-25_Deepcut_DBM.md` (MPFF Operating and Capacity Basis) |
| Heater bundle status | Under evaluation after upstream HEX installation; if retained, U-bundle / BKU-type with heat medium tube-side. Original sizing target: maintain 140 deg F in MPFF and 87 deg F at 50 psig downstream LP flash feed, 10% excess surface area margin (line-pack scenario). 350 deg F heat-medium supply basis TBC; tube-sheet seal-weld requirements TBC; vessel nozzle provisions to be preserved until disposition confirmed. | DBM-Deepcut `4-25_Deepcut_DBM.md` (MPFF feed conditions) |

## Construction

| Item | Value | Source |
|---|---|---|
| Fabrication/supply scope | Vendor-engineered, fabricated, and supplied as a packaged production unit (vessel, heater bundle if retained, building, instrumentation, internals) | `_CONTEXT.md`; DBM-Deepcut `4-25_Deepcut_DBM.md` |
| Equipment metallurgy where affected by low temperature | Governed by -40 deg C minimum ambient unless more severe process or vendor condition applies | DBM-Comp_and_Liquids `3-25_Comp_and_Liquids_DBM.md` (Site basis) |
| Isolation philosophy | Multiple parallel packages isolated on a unit basis so each can be removed from service for maintenance while remaining units operate (MPFF named explicitly) | DBM-Deepcut `4-25_Deepcut_DBM.md` (parallel-package isolation paragraph) |
| Coating/internal coating | None specified for MPFF internals (compare: stabilizer flash/feed separator is Devchem 253) | DBM-Deepcut `4-25_Deepcut_DBM.md` |
| Anticipated artifacts | Vendor engineered physical equipment package; vendor package design basis and datasheet set | `_CONTEXT.md` |

## References

- DBM-Deepcut: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
- DBM-Comp_and_Liquids: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
- Workbook Packages row 71; `26020-Package_Requirements.docx` package heading 13 (location TBD — source not converted to locally accessible text)
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local)
- GATE-07 PROJECT_DECOMP snapshot (DELIVERABLE_REGISTER, OBJECTIVE_DELIVERABLE_MAP)
