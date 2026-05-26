# Datasheet — DEL-057-04 Vendor Engineered Equipment Package (Stabilizers)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-057-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable Name | Vendor Engineered Equipment Package | `_CONTEXT.md` |
| Parent Package | `PKG-057` — Stabilizers | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-057 |
| Workbook Row | 82; WBS 01 | `PACKAGE_REGISTER.csv` row PKG-057 |
| Package Tag | `26020-01-17-005` (RFQ tag `26020-01-PT-17-005 - Inlet Stabilizers`) | `PACKAGE_REGISTER.csv` row PKG-057 |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable Type | Vendor Package Production Unit | `_CONTEXT.md` |
| Responsible Party | Package Vendor (engineering / design / equipment) with EPC Integrator integration review | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Scope SOW IDs | SOW-0177, SOW-0178, SOW-0179, SOW-0180 | `_CONTEXT.md`; `SCOPE_LEDGER.csv` |
| Objectives (ASSUMPTION, package-heuristic) | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md`; OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC |

## Attributes — Stabilizer Package

| Attribute | Value | Source |
|---|---|---|
| Service | Inlet Stabilizer Package; receives raw condensate from MPFF bottoms via stabilizer flash feed separator, pumps liquid hydrocarbon through feed/bottoms exchanger, heats and feeds stabilizer tower to strip butanes/light ends for stabilized C5+ product | SOW-0178; `DBM-Deepcut/4-25_Deepcut_DBM.md` §SEC-04 "Stabilizer Design and Operating Basis" L676–L710 |
| Quantity / sparing | Three (3) Inlet Stabilizer Packages installed at 04-25; design basis 3 × 40 %; future fourth-unit plot provision | SOW-0179; DBM L682–L684, L612 |
| Unit design rate | 1,272 m³/d (8,000 bbl/d) per package | SOW-0179, SOW-0180; DBM L683 |
| Turndown | 3 : 1 | SOW-0180; DBM L678 (column turndown) |
| Tower type | Trayed, reboiled distillation column; 20 conventional floating-valve trays | SOW-0179; DBM L678 |
| Feed pumps driver | Electric motor; VFD compatible (multistage horizontal centrifugal, 2 × 100 %) | SOW-0180; DBM L706 |
| Product cooler fan driver | Electric motor; VFD compatible | SOW-0180 |
| Instrumentation (named in SOW) | One (1) LIT; one (1) TIT (further instrumentation TBD pending vendor selection) | SOW-0179 |

## Conditions — Operating and Design

| Parameter | Operating | Design | Source |
|---|---|---|---|
| Flash Feed Separator pressure | 345 kPag (50 psig) | 1,724 kPag inlet | SOW-0180; DBM L704 (operating 50 psig) |
| Flash Feed Separator temperature | 30.6 °C | 60 °C inlet | SOW-0180; DBM L704 ("~87 °F" operating, ≈30.6 °C) |
| Flash Feed Separator retention time | ~15 min (TBC); ≥10 min between LLL and HLL | — | SOW-0180; DBM L704 |
| Stabilizer Column inlet temperature (post feed/bottoms exchanger) | 71 °C (160 °F) | — | SOW-0180; DBM L678 |
| Stabilizer Column minimum pressure | — | 793 kPag (min) | SOW-0180 |
| Feed/Bottoms Exchanger approach | — | 16.7 °C (30 °F) minimum approach | SOW-0180; DBM L706 (30 °F minimum approach) |
| Stabilizer inlet (upstream of inlet LCV) temperature | 60 °C (140 °F) | — | DBM L702 |
| Stabilizer inlet pressure (upstream of inlet LCV) | 1,724 kPag (250 psig) | — | DBM L702 |
| Final product temperature (after product cooler) | 43.3 °C (110 °F) | — | DBM L708 |
| Product cooler excess area | 130 % at design point | — | SOW-0180; DBM L708 |
| Stabilizer feed pump configuration | 2 × 100 % | — | DBM L706 |
| Reboiler heat source | Hot heat medium (temperature TBD pending detailed engineering) | — | DBM L706 |

## Capacity — Per Stabilizer Package Inlet (Winter Design)

| Case | Low | Expected normal | Expected high | Design | Source |
|---|---:|---:|---:|---:|---|
| Total two-phase flow, MMSCFD | 0 | < 2.821 | 2.821 | 2.821 | DBM L697 |
| Liquid inlet, m³/h | 0 | < 11.97 | 11.97 | 11.97 | DBM L699 |
| Vapour inlet, MMSCFD | 0 | < 0.6412 | 0.6412 | 0.6412 | DBM L700 |

Summer two-phase / liquid inlet basis is "Minimal" per DBM L696–L698; design retains the winter values.

## Product Specifications

| Specification | Value | Source |
|---|---|---|
| Product vapour pressure | < 85 kPaa by ASTM D6377 | DBM L685 |
| Product density | 650 to 775 kg/m³ | DBM L686 |
| Product C4- basis | (C3- × 3 + C4) < 5 liquid vol % | DBM L687 |
| CAPP butane equivalent | 3·(C1+C2+C3) + iC4 + nC4 < 5.0 % liquid volume, with 12 psia (82.75 kPaa) RVP | DBM L484 |

## Construction — Major Included Equipment (Vendor Scope)

| Sub-item | Basis / Note | Source |
|---|---|---|
| Stabilizer flash/feed separator | Operates 50 psig / ~87 °F; ~15 min retention (TBC); LCV with low-select on high level, high pressure, or high overhead flow; LP fuel-gas drive/sweet purge; relief/blowdown to HP flare; internal coating Devchem 253 | DBM L704 |
| Basket strainers | Upstream of stabilizer feed pumps; mesh TBD | SOW-0178; DBM L706 |
| Stabilizer feed pumps | Multistage horizontal centrifugal; 2 × 100 %; VFD-compatible electric motor; seals TBD | SOW-0180; DBM L706 |
| Feed/bottoms exchanger | Shell-and-tube BEU; inlet liquids on shell side for cleanability; 30 °F minimum approach | DBM L706 |
| Stabilizer column | Trayed reboiled distillation column with 20 floating-valve trays; 3:1 turndown | SOW-0179; DBM L678 |
| Stabilizer reboiler | Vertical NEN single-pass thermosiphon shell-and-tube; process fluid on tube side; mounted external to stabilizer building wall; reboiler tubes seal-welded to tubesheet; hot heat-medium service | DBM L706 |
| Stabilizer product cooler | Aerial cooler with single fan and VFD electric motor; 130 % excess area; cools product to 110 °F (43.3 °C); elevation TBD pending flare-loading review | SOW-0180; DBM L708 |
| Overhead pressure control | Stabilizer overhead vapour pressure-controlled to SOC second-stage suction; flash/feed overhead pressure-controlled to SOC first-stage suction | DBM L678, L704 |
| Indicators called out in SOW | One (1) LIT; one (1) TIT (further instrumentation TBD) | SOW-0179 |

## Scope by Others (Not Vendor Supply)

- Interconnecting piping at skid edge; DCS integration; foundations; electrical power supply from plant MCC; installation/erection. Source: SOW-0180.

## Boundary and Routing Notes

- Normal stabilizer feed source: MPFF bottoms (DBM L702).
- Stabilizer overhead vapour route: SOC second-stage suction (DBM L678).
- Stabilizer flash/feed overhead route: SOC first-stage suction (DBM L704).
- Stabilized product (C5+/NGL) routing: level-controlled from tower bottoms through feed/bottoms exchanger and product cooler to NGL mercaptan treating unit as primary feed; manual diversion to condensate slop tank available (DBM L710).
- C3/C4 LPG separation is out of scope (depropanizer retired) (DBM L702).

## TBD / Open Items

- Detailed sparing philosophy and operating split across the three units (DBM L612).
- Reboiler heat-medium temperature pending detailed engineering (DBM L706).
- Strainer mesh and pump seal type pending pump selection (DBM L706).
- Stabilizer overhead gas disposition under revised downstream configuration (DBM L690).
- Product cooler elevation (25 ft above grade vs. grade) pending flare-loading review (DBM L708).
- Direct clause-level slices of `26020-Package_Requirements.docx` package heading 12: **location TBD** (binary source not directly accessible; surfaced through SOW-0177/0178/0179/0180 extracts).

## References

- `_CONTEXT.md` (deliverable identity).
- `_REFERENCES.md` (authoritative basis pointers).
- `GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` row PKG-057.
- `GATE-07_Final_Published_2026-05-24/SCOPE_LEDGER.csv` rows SOW-0177, SOW-0178, SOW-0179, SOW-0180.
- `GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row DEL-057-04.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §SEC-04 "Stabilizer Design and Operating Basis" (lines 676–710); related "MPFF and Stabilizer Train Relationship" (lines 608–612).
- `_Sources/26020-Package_Requirements.docx` package heading 12 — binary; clause text not directly accessible in markdown. **location TBD** for direct clause references.
