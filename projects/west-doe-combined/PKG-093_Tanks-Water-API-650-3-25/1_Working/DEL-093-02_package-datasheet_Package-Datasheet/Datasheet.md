# Datasheet — DEL-093-02 Package Datasheet (Tanks, Water (API 650) 3-25)

> SCOPE NOTE (authoritative companion register): Per `PACKAGE_REGISTER.csv` row `PKG-093`, this package is **Item No. 1: Two (2) 3,800 bbl Sweet Produced Water Storage Tanks — TK-9060-2 and TK-9070-2** at the 03-25 Liquids Hub. Process function: Sweet Produced Water and Process Water. These two tanks are the package boundary. The remaining five sour produced-water tanks and the eleven condensate tanks described in the DBM are out of scope for `PKG-093`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-093-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable Name | Package Datasheet | `_CONTEXT.md` |
| Parent Package | `PKG-093` — Tanks, Water (API 650) 3-25 | `_CONTEXT.md` |
| Package RFQ Number | `26020-03-PT-19-001 — Tanks, Water` | `PACKAGE_REGISTER.csv` row PKG-093 (`Bid_Doc_Number`) |
| Equipment Tags | TK-9060-2; TK-9070-2 | `PACKAGE_REGISTER.csv` row PKG-093 (Process Mechanical Scope) |
| Process Function | Sweet Produced Water and Process Water | `PACKAGE_REGISTER.csv` row PKG-093 |
| Facility | 03-25 West Doe Compressor Station and Liquids Hub | `3-25_Comp_and_Liquids_DBM.md` §SEC-01 (line 7) |
| Site | LSD 03-25-80-15 W6M, north of Dawson Creek, BC | `3-25_Comp_and_Liquids_DBM.md` §SEC-02 (line 85, 89) |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-093 |
| Deliverable Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` (EPC Integrator owns integration; Package Vendor owns package engineering/design/documentation/equipment) |
| Anchoring Source Reference | Workbook Packages row 95; 26020-Package_Requirements.docx package heading 45; `Bid Docs/Budgetary/26020-03-PT-RFQ-19-001 - Water Tanks.docx` | `_CONTEXT.md`, `_REFERENCES.md`, `PACKAGE_REGISTER.csv` (.docx/.xlsx not locally rendered — `location TBD` for clause-level cites) |

## Attributes (Equipment Constituents)

| Item | Quantity | Service | Source |
|---|---|---|---|
| Sweet produced-water storage tanks (TK-9060-2, TK-9070-2) | 2 x 3,800 bbl | Sweet produced water and process water | `PACKAGE_REGISTER.csv` row PKG-093; `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 421, 425-426) |
| Tank type / code basis | API-650 Modified, atmospheric | All package tanks | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 421) |
| External insulation and heating | Required (both tanks) | -40 deg C ambient service | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 421), §SEC-02 (line 145) |
| Internal coating | Devchem 253 | All produced-water tanks (per DBM, applies to entire 7-tank family; carried into this 2-tank scope) | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 421) |
| Vacuum-truck connection | 2.75 m3/min per tank (ASSUMPTION — source labels "assumed") | Truck-out fallback | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 430) |
| Tank vapour service | Routed to facility VRU system | Vapour collection from tank vents | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 436) |

## Process / Design Conditions

| Parameter | Value | Source |
|---|---|---|
| Service fluid | Sweet produced water / process water | `PACKAGE_REGISTER.csv` row PKG-093 |
| Produced-water tank design SG | 1.25 (TBC in source) | `3-25_Comp_and_Liquids_DBM.md` §SEC-04 (line 176), §SEC-06 (line 421) |
| Pump fluid SG basis (downstream transfer pumps) | 1.18 (open discrepancy vs. tank design SG; to be closed during detailed design) | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 421) |
| Minimum ambient design temperature | -40 deg C | `3-25_Comp_and_Liquids_DBM.md` §SEC-02 (line 145) |
| Pressure class | Atmospheric (API-650 Modified) | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 421) |
| Sour-service classification | Sweet service (per package scope label "Sweet Produced Water") — sour-service rules ASSUMPTION TBD pending `26020-Package_Requirements.docx` heading 45 clause review | `PACKAGE_REGISTER.csv`; clause TBD |
| Disposition routing | Pipeline (primary) or truck-out (fallback); pipeline downstream of facility riser by others | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 432) |
| Upstream allocation context | Facility produced-water design 3,600 m3/d; sweet allocation 2 of 7 tanks | `3-25_Comp_and_Liquids_DBM.md` §SEC-03 (line 161, 188); §SEC-06 (line 425-426) |

## Construction / Materials

| Item | Value | Source |
|---|---|---|
| Tank design code | API 650 Modified | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 421) |
| Internal coating | Devchem 253 | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 421) |
| External insulation | Required | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 421) |
| External heating | Required | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 421) |
| Tank shell metallurgy | location TBD — clause not locally available; subject to API 650 Modified + sweet-service rules in `26020-Package_Requirements.docx` heading 45 | TBD |
| Foundations | TBD — site basis drives foundation design (`3-25_Comp_and_Liquids_DBM.md` line 145); detailed foundation specification TBD |
| Allowable materials exclusions | location TBD (aluminum exclusion in DBM is stated for caustic building, not produced-water tanks) | TBD |
| Cathodic protection | Required (per `PACKAGE_REGISTER.csv` applicable interfaces) | `PACKAGE_REGISTER.csv` row PKG-093 (Applicable interface types) |

## Interfaces (Package Boundary)

| Interface | Counterparty | Direction | Source |
|---|---|---|---|
| Produced-water inlet | 03-25 produced-water collection / 04-25 transfer | Into tanks | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 419-421); `PACKAGE_REGISTER.csv` (Process Piping interface) |
| Tank vapour vent | VRU system (2 x 200 hp packages) | Out to VRU suction header | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 436); `PACKAGE_REGISTER.csv` (Relief/Flare/Vent interface) |
| Treatment package interface | H2O2 treatment package (1 x, 3,840 m3/d TBC) | Bi-directional | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 427) |
| Transfer outlet | Produced-water transfer pumps (2 x 100%) | Out to pipeline / truck-loading | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 429, 432); `PACKAGE_REGISTER.csv` (Process Piping) |
| Truck-out interface | Vacuum truck connection per tank | Out | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 430) |
| Drain / containment | Facility drain and spill-containment systems | Out | `PACKAGE_REGISTER.csv` (Drain/Containment; Grading/Site Drainage/Spill Containment) |
| Grounding / bonding | Facility grounding grid | Tied | `PACKAGE_REGISTER.csv` (Grounding/Bonding) |
| Cathodic protection | Facility CP system | Tied | `PACKAGE_REGISTER.csv` (Cathodic Protection) |
| Area / exterior lighting | Facility electrical | In | `PACKAGE_REGISTER.csv` (Area/Exterior Lighting) |
| I&C / control cabling | Facility BPCS / ESD | Tied | `PACKAGE_REGISTER.csv` (I&C/Control Cabling) |
| Structural / foundations / supports | EPC civil / structural | Tied | `PACKAGE_REGISTER.csv` (Structural/Foundations/Supports) |
| Power / heat tracing / building heat | Facility utilities | In | `3-25_Comp_and_Liquids_DBM.md` §SEC-02 (line 145) |

## References

- `PACKAGE_REGISTER.csv` row `PKG-093` (GATE-07 Final Published snapshot) — authoritative companion register, identifies tag numbers TK-9060-2 / TK-9070-2 and applicable interface types.
- `DELIVERABLE_REGISTER.csv` row `DEL-093-02_package-datasheet` (GATE-07 Final Published snapshot).
- `3-25_Comp_and_Liquids_DBM.md` (DBM-Comp_and_Liquids) — primary source slices: §SEC-01, SEC-02, SEC-03, SEC-04, SEC-06.
- `26020-Package_Requirements.docx` package heading 45 — clause-level location TBD (binary .docx not locally rendered).
- `26020-Packages_Interfaces_4_export.xlsx` Packages row 95 — clause-level location TBD (binary .xlsx not locally rendered).
- `Bid Docs/Budgetary/26020-03-PT-RFQ-19-001 - Water Tanks.docx` — location TBD (binary .docx not locally accessible).

## Open Items / TBD

- TBD: Sour-service materials and welding clauses from `26020-Package_Requirements.docx` heading 45 (clause text not locally accessible). Note PKG-093 service is labeled "Sweet" but produced-water service typically still warrants H2S contingency review.
- TBD: Close design SG (1.25 tank vs. 1.18 pump basis) — flagged in `3-25_Comp_and_Liquids_DBM.md` §SEC-06.
- TBD: Tank foundation, anchorage, and seismic design parameters.
- TBD: Pipeline tie-in flange location and class for produced-water transfer interface.
- TBD: Confirm whether "process water" service (per PACKAGE_REGISTER process function) imposes any non-produced-water duty that affects coating selection or cleanliness criteria.
