# Datasheet — Package Datasheet (PKG-074 Caustic Treating, NGL Mercaptan Removal)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-074-02_package-datasheet | `_CONTEXT.md` |
| Parent Package ID | PKG-074 | `_CONTEXT.md` |
| Package Tag (workbook) | 26020-01-27-002 | PACKAGE_REGISTER.csv row 51 |
| Equipment Tag | 26020-01-PT-27-002 - Caustic Treating (NGL Mercaptan Removal) | PACKAGE_REGISTER.csv row 51 |
| Package Name | Caustic Treating (NGL Mercaptan Removal) | PACKAGE_REGISTER.csv row 51 |
| Discipline | Mechanical | PACKAGE_REGISTER.csv row 51 |
| WBS | 01 | PACKAGE_REGISTER.csv row 51 |
| Workbook Row | 51 | PACKAGE_REGISTER.csv row 51 |
| Word Source Heading | 26020-Package_Requirements.docx package heading 28 | PACKAGE_REGISTER.csv row 51 |
| Responsible Party (EPC handoff) | EPC Integrator | `_CONTEXT.md` |
| Package Vendor scope | Package engineering, package design, vendor documentation, and physical equipment package | PACKAGE_REGISTER.csv row 51 |

## Attributes (Process Function)

| Attribute | Value | Source |
|---|---|---|
| Unit type | Non-regenerative caustic treating (no on-site regeneration column in current basis) | DBM-Deepcut/4-25_Deepcut_DBM.md `## Current-Scope NGL Mercaptan Treating` (lines 1509-1513, 1519) |
| Service | C3+ NGL mercaptan extraction downstream of the de-ethanizer | DBM-Deepcut/4-25_Deepcut_DBM.md lines 1511, 1521 |
| Process provider | Third-party proprietary process provider (selection TBD in detailed engineering) | DBM-Deepcut/4-25_Deepcut_DBM.md lines 1511, 1548 |
| Downstream routing | Treated NGL to filtration, water wash, molecular-sieve dehydration, NGL storage | DBM-Deepcut/4-25_Deepcut_DBM.md line 1513 |
| Caustic disposition | Rich caustic to caustic heating and spent-caustic storage/handling; spent caustic and DSO trucked off site | DBM-Deepcut/4-25_Deepcut_DBM.md lines 1513, 528-530 |

## Conditions (Design Parameters)

| Parameter | Value | Source |
|---|---|---|
| Governing design rate | 2,385 m3/d (15,000 bbl/d) | DBM-Deepcut/4-25_Deepcut_DBM.md `### NGL Mercaptan Treating Design Parameters` line 1520 |
| Inlet service fluid | Cooled C3+ NGL from de-ethanizer outlet path | DBM-Deepcut/4-25_Deepcut_DBM.md line 1521 |
| Inlet pressure, design | 2,213 kPag | DBM-Deepcut/4-25_Deepcut_DBM.md line 1522 |
| Outlet pressure, design | 1,978 kPag | DBM-Deepcut/4-25_Deepcut_DBM.md line 1523 |
| Pressure low/high cases | TBC | DBM-Deepcut/4-25_Deepcut_DBM.md line 1524 |
| Inlet temperature, low | 26.7 deg C | DBM-Deepcut/4-25_Deepcut_DBM.md line 1525 |
| Inlet temperature, design | 43.3 deg C | DBM-Deepcut/4-25_Deepcut_DBM.md line 1525 |
| Inlet temperature, high | 48.8 deg C | DBM-Deepcut/4-25_Deepcut_DBM.md line 1525 |
| Downstream caustic-solution minimum temperature | 80 deg F (26.7 deg C) | DBM-Deepcut/4-25_Deepcut_DBM.md line 1338 |
| Fresh caustic concentration | 50 wt% NaOH | DBM-Deepcut/4-25_Deepcut_DBM.md line 1526 |
| Circulating process caustic concentration | 14.7 wt% NaOH (ASSUMPTION: to be confirmed per source) | DBM-Deepcut/4-25_Deepcut_DBM.md line 1527 |
| Number of contactor stages | TBD (detailed-engineering item) | DBM-Deepcut/4-25_Deepcut_DBM.md line 1548 |
| Winter vapour pressure values | TBD | DBM-Deepcut/4-25_Deepcut_DBM.md line 1548 |
| High-ethane case review | TBD | DBM-Deepcut/4-25_Deepcut_DBM.md line 1548 |

### Mercaptan Extraction Performance (assumed stage extraction)

| Component | Stage 1, % | Stage 2, % | Total, % | Source |
|---|---:|---:|---:|---|
| C1RSH | 98.84 | 50.00 | 99.42 | DBM-Deepcut/4-25_Deepcut_DBM.md line 1534 |
| C2RSH | 98.93 | 84.61 | 99.84 | DBM-Deepcut/4-25_Deepcut_DBM.md line 1535 |
| C3RSH | 89.63 | 60.00 | 95.85 | DBM-Deepcut/4-25_Deepcut_DBM.md line 1536 |
| C4RSH | 45.76 | 17.65 | 55.33 | DBM-Deepcut/4-25_Deepcut_DBM.md line 1537 |

### Treated NGL Sulphur Cases (governing performance)

| Case | Upstream C3+ | Treated C3+ | Source |
|---|---|---|---|
| Total C1-C3 RSH as S, with caustic treating, 1 mol% H2S inlet gas | 3,240 ppmw S / 411.3 lb/h S | 203.7 ppmw S / 25.71 lb/h S | DBM-Deepcut/4-25_Deepcut_DBM.md line 1541 |
| Total sulphur, with caustic treating, 1 mol% H2S inlet gas | 4,166 ppmw S / 528.8 lb/h S | 970 ppmw S / 122.5 lb/h S | DBM-Deepcut/4-25_Deepcut_DBM.md line 1544 |

## Construction (Equipment and Storage)

| Item | Basis | Source |
|---|---|---|
| Caustic NGL contactor | Mixes NGL with circulating caustic to extract mercaptans; sweetened NGL flows to filtration and water wash | DBM-Deepcut/4-25_Deepcut_DBM.md line 1554 |
| NGL contactor caustic outlet filters | Independent vessels from the contactor; 2 x 100% sparing | DBM-Deepcut/4-25_Deepcut_DBM.md line 1554 |
| Water wash recycle pumps | Single-stage vertical inline centrifugal pumps; single mechanical seals; 2 x 100% sparing | DBM-Deepcut/4-25_Deepcut_DBM.md line 1558 |
| Pressurized caustic drain drum (V-6940-1) | Heated, insulated, demister element, K factor < 0.2; NGL vapours route to SOC first-stage suction; caustic level-controlled to spent caustic tank | DBM-Deepcut/4-25_Deepcut_DBM.md lines 748, 1560 |
| Fresh caustic tank | 1 x 400 bbl atmospheric, heated, insulated, truck-in capable, fuel-gas blanket; not connected to VRU header; design SG 1.75 TBC | DBM-Deepcut/4-25_Deepcut_DBM.md lines 1528, 1562 |
| Spent caustic tank | 1 x 400 bbl atmospheric, heated, insulated, truck-out capable, connected to incinerator header with flame arrestor, LP fuel-gas blanket | DBM-Deepcut/4-25_Deepcut_DBM.md lines 530, 1529, 1562 |
| Disulphide oil (DSO) tank | 1 x 400 bbl atmospheric, heated, insulated, truck-out capable, connected to incinerator header with flame arrestor, LP fuel-gas blanket; design SG 1.75 TBC | DBM-Deepcut/4-25_Deepcut_DBM.md lines 528, 1530, 1564 |
| Make-up water | From process water storage tank (upset operation only); routing TBC | DBM-Deepcut/4-25_Deepcut_DBM.md line 1556 |
| Building location | All caustic treating equipment installed indoors (caustic freeze/crystallization risk); segregated to Mercaptan Treating Unit building or immediately adjacent area | DBM-Deepcut/4-25_Deepcut_DBM.md line 1552 |
| Safety showers | Water safety showers required; shower quantity and location TBD; activation must trigger discrete control-room alert | DBM-Deepcut/4-25_Deepcut_DBM.md line 1552 |
| Materials prohibition | No aluminum materials in caustic building; insulation cladding/straps in caustic-exposure areas are stainless steel | DBM-Deepcut/4-25_Deepcut_DBM.md line 1566 |
| Caustic tank materials | Polymer or other caustic-compatible materials; specific selection TBD | DBM-Deepcut/4-25_Deepcut_DBM.md line 1566 |
| Building floor material | TBD (detailed-engineering item) | DBM-Deepcut/4-25_Deepcut_DBM.md line 1566 |
| Incinerator | Located at 3-25 facility near flare stacks; services 4-25 NGL mercaptan treating system; KO drum upstream | DBM-Deepcut/4-25_Deepcut_DBM.md line 1570 |
| Supplemental fuel gas rate to incinerator | TBD | DBM-Deepcut/4-25_Deepcut_DBM.md line 1572 |

## Interface Summary (Package Interface Requirements Matrix)

Applicable interface types declared in the package register row for PKG-074:

| Interface | Notes | Source |
|---|---|---|
| Process Piping | NGL feed from de-ethanizer cooler outlet; treated NGL to filtration / water wash / mol sieve / NGL storage | PACKAGE_REGISTER.csv row 51; DBM-Deepcut/4-25_Deepcut_DBM.md lines 1338, 1513 |
| Utility Piping | Caustic make-up/transfer, process water make-up | PACKAGE_REGISTER.csv row 51; DBM-Deepcut/4-25_Deepcut_DBM.md line 1556 |
| Relief / Flare / Vent | Tank/header vapours routed to incinerator header via 3-25; flare interface TBD | PACKAGE_REGISTER.csv row 51; DBM-Deepcut/4-25_Deepcut_DBM.md lines 1562, 1570 |
| Drain / Containment | Pressurized caustic drain drum V-6940-1; caustic-compatible containment | PACKAGE_REGISTER.csv row 51; DBM-Deepcut/4-25_Deepcut_DBM.md line 1560 |
| Electrical Power | Building, pumps, instrumentation; details TBD | PACKAGE_REGISTER.csv row 51 |
| EHT | Heating for caustic-containing tanks and lines (freeze protection) | PACKAGE_REGISTER.csv row 51; DBM-Deepcut/4-25_Deepcut_DBM.md line 1552 |
| Grounding / Bonding | Standard package grounding; specifics TBD | PACKAGE_REGISTER.csv row 51 |
| Area / Exterior Lighting | Building exterior and access; specifics TBD | PACKAGE_REGISTER.csv row 51 |
| I&C / Control Cabling | Safety-shower alarm to control room; package controls integration | PACKAGE_REGISTER.csv row 51; DBM-Deepcut/4-25_Deepcut_DBM.md line 1552 |
| Building HVAC / Services | Indoor installation due to freeze/crystallization risk | PACKAGE_REGISTER.csv row 51; DBM-Deepcut/4-25_Deepcut_DBM.md line 1552 |
| Fire & Gas / Safety Systems | Building F&G coverage; water safety showers with control-room alert | PACKAGE_REGISTER.csv row 51; DBM-Deepcut/4-25_Deepcut_DBM.md line 1552 |
| Maintenance Access | Truck-in/out access for caustic and DSO tanks | PACKAGE_REGISTER.csv row 51; DBM-Deepcut/4-25_Deepcut_DBM.md lines 1562, 1564 |
| Structural / Foundations / Supports | Building foundation, tank supports; details TBD | PACKAGE_REGISTER.csv row 51 |

## Covers Scope Items / Supports Objectives

- Covers: SOW-0059, SOW-0060, SOW-0061, SOW-0062 (`_CONTEXT.md`)
- Supports objectives (ASSUMPTION: PACKAGE_HEURISTIC mapping from PACKAGE_REGISTER.csv row 51): OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010

## References

- DBM-Deepcut: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (sections `## Current-Scope NGL Mercaptan Treating`, lines 1509-1572; SOC inlet basis lines 748, 760; de-ethanizer interface lines 1337-1338; waste streams lines 526-532)
- PACKAGE_REGISTER (Gate 7): `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` row 51
- Word source (location TBD; not locally parsed): `26020-Package_Requirements.docx` package heading 28
- Workbook source (location TBD; not locally parsed): `26020-Packages_Interfaces_4_export.xlsx` Packages row 51
- Trace appendix: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/Trace_Appendix.md`
