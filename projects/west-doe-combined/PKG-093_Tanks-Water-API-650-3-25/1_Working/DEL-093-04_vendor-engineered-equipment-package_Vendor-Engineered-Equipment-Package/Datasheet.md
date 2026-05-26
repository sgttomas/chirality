# Datasheet: DEL-093-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-093-04_vendor-engineered-equipment-package` |
| Name | Vendor Engineered Equipment Package |
| ParentPackageID | `PKG-093` |
| ParentWorkbookID | 93 |
| PackageName | Tanks, Water (API 650) 3-25 |
| Discipline | Mechanical |
| Type | Vendor Package Production Unit |
| ResponsibleParty | Package Vendor (engineering / design / equipment) with EPC Integrator integration review |
| WBS | 03 |
| Project / Facility | 03-25 West Doe Compressor Station and Liquids Hub |
| Facility Location | LSD 03-25-80-15 W6M, north of Dawson Creek, BC (per `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §SEC-01) |

## Attributes — Tagged Equipment Covered by Vendor Engineered Package

| Tag / Item | Description | Source |
|---|---|---|
| Item No. 1 | Two (2) 3,800 bbl Sweet Produced Water Storage Tanks; tags `TK-9060-2`, `TK-9070-2` | `SCOPE_LEDGER.csv` rows SOW-0230, SOW-0231 (26020-Package_Requirements.docx package heading 45) |
| Item No. 2 | Additional tank scope referenced under SOW-0232; design flow `TBD`; operating temperature `TBD` in source | `SCOPE_LEDGER.csv` row SOW-0232 |

ASSUMPTION: The package title "Tanks, Water (API 650) 3-25" plus the Major Equipment line indicate this vendor package covers only the Sweet Produced Water tanks within the 03-25 facility. The broader 03-25 Liquids Hub produced-water tank population (seven 3,800 bbl tanks: five sour + two sweet) described in `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 421) is surrounding context, not vendor scope under this row.

## Attributes — Process and Service

| Attribute | Value | Source |
|---|---|---|
| Service | Sweet Produced Water & Process Water | SOW-0230 |
| Fluid character | Non-sour produced water | SOW-0231 |
| Tank count (Item No. 1) | 2 x 3,800 bbl | SOW-0230 |
| Nominal capacity per tank | 3,800 bbl | SOW-0230 |
| Pressure class | Atmospheric | SOW-0232 |
| Operating temperature (Item No. 1) | 5 °C | SOW-0232 |
| Operating temperature (Item No. 2) | TBD | SOW-0232 |
| Design temperature range | -40 °C (min) to 60 °C (max) | SOW-0232 |
| Design test pressure | 32 oz (per SOW-0232 wording) | SOW-0232 |
| Design Flow (Item No. 1) | 15,300 kg/h / 3,584 Am³/d from compressor station + 240 Am³/d from cryo | SOW-0232 |
| Design Flow (Item No. 2) | TBD | SOW-0232 |
| Produced-water density (facility basis) | 1.18 SG (pump basis); tank design SG 1.25 TBC | `3-25_Comp_and_Liquids_DBM.md` §SEC-03 (line 176); §SEC-06 (line 421) |

## Attributes — Construction

| Attribute | Value | Source |
|---|---|---|
| Design code | API 650 (Modified) | SOW-0231; `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 421) |
| Volume | TBD (per SOW-0231 wording; Item No. 1 nominal 3,800 bbl per SOW-0230) | SOW-0231, SOW-0230 |
| External insulation | Required | SOW-0231 |
| External heating | Heater required to prevent freezing | SOW-0231 |
| Blanket gas | LP fuel gas, vacuum prevention in winter per API-2000 | SOW-0231 |
| Internal coating (floor, walls, roof) | Devchem 253 | SOW-0231; `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 421) |
| Skim system | Kennilworth-type HCL float skim, one per tank | SOW-0231 |
| Skim float design SG | ≤ 0.67 | SOW-0231 |
| Vapour interface | Tank vapours routed to facility VRU suction | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (lines 436, 422) |
| Vacuum-truck connection | 2.75 m³/min per tank assumed (facility basis) | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 430) |

## Conditions — Site / Ambient

| Condition | Value | Source |
|---|---|---|
| Minimum ambient | -40 °C | `3-25_Comp_and_Liquids_DBM.md` §SEC-02 (lines 96, 145); SOW-0232 |
| Maximum ambient | 35 °C (facility design basis); 60 °C tank-design max per SOW-0232 | `3-25_Comp_and_Liquids_DBM.md` §SEC-02 (line 96); SOW-0232 |
| Service classification | Non-sour (sweet) produced water | SOW-0231 |

## Vendor-Scope Boundaries (By Others)

| Item Excluded From Vendor Package | Source |
|---|---|
| Foundations | SOW-0232 |
| Mounting tanks at site | SOW-0232 |
| Electrical / instrumentation | SOW-0232 |
| Platforms, staircase, etc. | SOW-0232 |

## Anticipated Artifacts

- Vendor engineered physical equipment package (fabricated tanks ready for site delivery).
- Vendor package design basis and datasheet set (per `_CONTEXT.md` Anticipated Artifacts).

## References

- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (SEC-01, SEC-02, SEC-03, SEC-06)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/SCOPE_LEDGER.csv` rows SOW-0229, SOW-0230, SOW-0231, SOW-0232
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row DEL-093-04
- `26020-Package_Requirements.docx` package heading 45 (location TBD — local DOCX text slice not extracted; SOW-row text used as the proxy source slice)
