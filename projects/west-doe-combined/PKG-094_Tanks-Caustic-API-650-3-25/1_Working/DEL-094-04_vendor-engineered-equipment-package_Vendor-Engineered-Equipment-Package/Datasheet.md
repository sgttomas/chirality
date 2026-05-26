# Datasheet: DEL-094-04 — Vendor Engineered Equipment Package

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-094-04_vendor-engineered-equipment-package` |
| Name | Vendor Engineered Equipment Package |
| ParentPackageID | `PKG-094` |
| PackageName | Tanks, Caustic (API 650) 3-25 |
| Discipline | Mechanical |
| Type | Vendor Package Production Unit |
| ResponsibleParty | Package Vendor (engineering/design/equipment) with EPC Integrator integration review |
| Covers Scope Items | `SOW-0193`, `SOW-0194`, `SOW-0195`, `SOW-0196` |
| Supports Objectives | `OBJ-002`–`OBJ-010` (ASSUMPTION: package-grouping heuristic) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package subject (per package title) | Caustic tanks designed/supplied to API 650 family | `_CONTEXT.md`; PackageName |
| Service category (per DBM) | Non-regenerative caustic mercaptan treating tankage and ancillary storage in the 03-25 Liquids Hub | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (caustic treating basis) |
| Caustic solution basis | 50 wt% NaOH/H2O; SG 1.75 TBC | DBM 3-25 (caustic basis); marked TBC in source |
| Caustic tank size class (basis) | 400 bbl atmospheric tanks for fresh caustic, spent caustic, caustic process-water, and H2O2 | DBM 3-25 (liquids hub equipment basis) |
| Tank construction class (per source) | 32 oz atmospheric tanks with LP fuel-gas blanket, heating, and insulation | DBM 3-25 (fresh and spent caustic tanks) |
| Aluminum prohibition | Aluminum shall not be used in the caustic building | DBM 3-25 |
| Tank material/coating details | TBC in source | DBM 3-25 |
| Spent caustic tank venting | Vents through flame arrestor to incinerator header; supports truck-out | DBM 3-25 |
| Fresh caustic VRU connection | Not connected to VRU | DBM 3-25 |
| Minimum ambient design temperature | -40 deg C governs exposed equipment unless a more severe process or vendor condition applies | DBM 3-25 (site basis) |
| Drain interface — caustic drain | 300# ANSI flange minimum; max temp 121 deg C / 250 deg F TBC; min drain tank temp 80 deg F | DBM 3-25 (drain systems) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Ambient minimum | -40 deg C | DBM 3-25 |
| Tank atmospheric service | LP fuel-gas blanketed | DBM 3-25 |
| Heat tracing concept (caustic drain) | 37.8 deg C / 100 deg F with redundant circuits (under consideration) | DBM 3-25 |
| Caustic oxidation demand (03-25) | 214 SCFM TBC | DBM 3-25 |

## Construction

| Item | Value | Source |
|---|---|---|
| Code family | API 650 (per package title); detailed code application | Package title `_CONTEXT.md`; specific edition/appendices TBD |
| Insulation / heat | Externally insulated and heated (atmospheric caustic family) | DBM 3-25 |
| Internal coating | TBD for caustic tanks (DBM specifies Devchem 253 for produced-water tanks; caustic coating TBC) | DBM 3-25 |
| Material of construction | TBD (caustic service material selection requires detailed review; aluminum prohibited in caustic building) | DBM 3-25 |
| Foundations / structural / module layout | Site basis drives winterization, foundations, structural steel, equipment metallurgy; detail TBD | DBM 3-25 |
| Nozzles, manways, gauging | TBD | — |
| Pressure/vacuum protection | Flame arrestor on spent caustic vent; details TBD | DBM 3-25 |

## Anticipated Artifacts (per `_CONTEXT.md`)

- Vendor engineered physical equipment package
- Vendor package design basis and datasheet set

## References

- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (caustic treating basis; tank basis; site basis; drain systems)
- `_REFERENCES.md` (this deliverable)
- Workbook Packages row 86 (location TBD — workbook not converted to locally accessible source slice)
- 26020-Package_Requirements.docx package heading 46 (location TBD — docx not converted to locally accessible source slice)
- Gate 7 final published PROJECT_DECOMP snapshot — DELIVERABLE_REGISTER.csv row for DEL-094-04
