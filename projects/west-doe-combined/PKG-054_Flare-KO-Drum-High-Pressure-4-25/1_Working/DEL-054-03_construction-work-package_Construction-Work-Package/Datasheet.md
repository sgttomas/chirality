# Datasheet — Construction Work Package (DEL-054-03)

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-054-03_construction-work-package |
| Name | Construction Work Package |
| ParentPackageID | PKG-054 |
| PackageName | Flare KO Drum (High Pressure) 4-25 |
| Discipline | Mechanical |
| Type | EPC Construction Work Package |
| ResponsibleParty | EPC Integrator |
| Decomposition Basis | PROJECT_DECOMP GATE-07_Final_Published_2026-05-24 |
| Primary Source Slice | DBM-Deepcut/4-25_Deepcut_DBM.md, Flare Systems Basis; Modularization table (`410-1 HP / Cryo Flare KO Drum Module`) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Major Equipment Tag (HP Flare KO Drum) | V-4100-1 | 4-25_Deepcut_DBM.md, Flare Equipment and Routing table |
| KO Drum Transfer Pump Tag | P-4100-1 | 4-25_Deepcut_DBM.md, Flare Equipment and Routing table |
| Module Identifier | 410-1 HP / Cryo Flare KO Drum Module | 4-25_Deepcut_DBM.md, Modularization table |
| Module Assembly Location | Shop | 4-25_Deepcut_DBM.md, Modularization table |
| HP Relief Header (inlet to KO Drum) | 508 mm (20 in) | 4-25_Deepcut_DBM.md, Flare Equipment and Routing table |
| HP Flare Header (outside cryo combination) | 762 mm SA-333 | 4-25_Deepcut_DBM.md, Flare Header and Backpressure Basis |
| HP/Cryo Built-up Backpressure (peak) | 695 kPag (100 psig) estimated | 4-25_Deepcut_DBM.md, Flare Header and Backpressure Basis |
| Maximum Total PSV Flange Backpressure (150# basis) | <1172 kPag (170 psig) | 4-25_Deepcut_DBM.md, Flare Header and Backpressure Basis |
| Heat Tracing — HP Flare Headers Outside Heated Buildings | Required (electric, insulated; PSV outlets that free-drain to header exempted) | 4-25_Deepcut_DBM.md, Flare Equipment and Routing |
| Spacing — Flare/KO Drum to Vegetation/Fire Hazards | 10 m (32 ft) | 4-25_Deepcut_DBM.md, Flare and Incinerator Spacing |
| Common HP/Cryo Stack Location | 03-25 shared with 04-25 | 4-25_Deepcut_DBM.md, Flare Equipment and Routing |
| Module Color — Flashing/Doors/Trim | Cloverdale #2593 "Safety Green" | 4-25_Deepcut_DBM.md, Building colors table |
| Module Color — Exterior Walls/Roof | Galvanized metal with pre-painted trim | 4-25_Deepcut_DBM.md, Building colors table |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | High-pressure flare relief and blowdown collection from balance-of-plant outside cryogenic unit | 4-25_Deepcut_DBM.md, Flare Equipment and Routing |
| HP Header Freeze Protection | Required outside heated buildings | 4-25_Deepcut_DBM.md, Flare Equipment and Routing |
| Truck-Out of KO Liquids | Provided via P-4100-1 plus truck-out | 4-25_Deepcut_DBM.md, Flare Equipment and Routing |
| Site Spacing | Per OGAOM Sec. 9.6.15 distances (location TBD in package context) | 4-25_Deepcut_DBM.md, Flare and Incinerator Spacing |
| Radiation Criteria | BCER Appendix 1, Schedule 1, Sec. 7(4); 9.788 kW/m2 sterile, 5.788 kW/m2 outer including solar allowance | 4-25_Deepcut_DBM.md, Flare Radiation Criteria |

## Construction

| Construction Item | Value | Source |
|---|---|---|
| Assembly Mode | Shop-fabricated module (410-1) shipped to site | 4-25_Deepcut_DBM.md, Modularization table |
| Site Activities | Set module on foundation, tie-in relief header, tie-in transfer-pump discharge to truck-out connections, electrical/instrumentation tie-ins, heat trace energize, insulation completion, commissioning support | ASSUMPTION (standard modular EPC sequence; not explicitly itemized in source) |
| Pre-Set Civil/Foundation Scope | Provided by upstream civil packages (PKG-001..PKG-005 family Earthworks/Grading) | Decomposition: DELIVERABLE_REGISTER.csv (civil packages exist as separate units) |
| Tie-In Points (process) | HP relief inlet header (508 mm); KO drum pump discharge / truck-out connection; combined HP/cryo header to stack | 4-25_Deepcut_DBM.md, Flare Equipment and Routing |
| Tie-In Points (utility) | Electric heat trace power; instrument air to vent/purge points (location TBD); fuel gas pilot/purge supply (location TBD) | ASSUMPTION (standard utility set; specific routes location TBD) |
| Inspection Hold Points | TBD — to be set by EPC inspection plan, including pressure test, weld NDE, heat-trace continuity, instrument loop checks | TBD |
| Turnover Documents | Vendor data book; weld and NDE records; pressure-test records; heat-trace verification; instrument calibration; punch list | ASSUMPTION (standard EPC turnover set; itemized list TBD) |

## References

- DBM-Deepcut/4-25_Deepcut_DBM.md — Flare Systems Basis, Flare Equipment and Routing, Flare Header and Backpressure Basis, Flare Radiation Criteria, Flare and Incinerator Spacing, Modularization table, Building colors table
- _CONTEXT.md (this deliverable)
- _REFERENCES.md (this deliverable)
- PROJECT_DECOMP GATE-07_Final_Published_2026-05-24 DELIVERABLE_REGISTER.csv (row DEL-054-03)
- 26020-Package_Requirements.docx package heading 9 — location TBD (binary source; text slice not accessible to this run)
