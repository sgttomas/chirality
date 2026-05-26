# Datasheet — DEL-055-04 Vendor Engineered Equipment Package (Flare KO Drum, Low Pressure, 4-25)

> Descriptive datasheet for the Package Vendor production unit. Captures the
> physical equipment package identity, attributes, design conditions, and
> construction basis as evidenced by accessible source slices. Numeric values
> not present in accessible sources are marked `TBD`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-055-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable Name | Vendor Engineered Equipment Package | `_CONTEXT.md` |
| Parent Package ID | `PKG-055` | `_CONTEXT.md` |
| Parent Workbook Row | 57 | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Package Name | Flare KO Drum (Low Pressure) 4-25 | `_CONTEXT.md` |
| Facility | West Doe Deepcut expansion, 04-25 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §"Facility Identity" |
| Discipline | Mechanical | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Production Unit Type | Vendor Package Production Unit | `_CONTEXT.md` |
| Responsible Party | Package Vendor (engineering / design / equipment) with EPC Integrator integration review | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Tag — Drum | V-3900-1 (LP Flare KO Drum) | `4-25_Deepcut_DBM.md` line 2029, 2582 |
| Tag — Transfer Pump | P-3900-1 (LP Flare KO Drum Transfer Pump) | `4-25_Deepcut_DBM.md` line 2029, 2581 |
| Module Identifier | 390-1 LP Flare KO Drum Module | `4-25_Deepcut_DBM.md` line 2783 |
| Module Construction Basis | Shop-built module | `4-25_Deepcut_DBM.md` line 2783 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Service | Low-pressure flare knock-out (separates entrained liquids from LP flare relief/blowdown vapours upstream of LP flare stack element) | `4-25_Deepcut_DBM.md` lines 2029, 2042 |
| Connected Service Sources | Amine regeneration, TEG regeneration, VRU, reciprocating compressor seal pot, VRU package blowdown, VRU suction header bypass, primary seal vent, contaminated mole-sieve regen gas blowdown | `4-25_Deepcut_DBM.md` lines 2029, 1781, 1787, 1801, 1702 |
| Downstream Routing | Routes vapours to LP flare stack (piggy-back element on common HP/cryo stack); separated liquids handled by P-3900-1 transfer pump with truck-out provision; LP header sources can also route via condensate slop tank low-pressure pump header | `4-25_Deepcut_DBM.md` lines 2029, 1665 |
| LP Flare Header Material | SA-106 | `4-25_Deepcut_DBM.md` line 2042 |
| LP Flare Relief Header Size at Drum | 508 mm (20 in) | `4-25_Deepcut_DBM.md` line 2029 |
| LP Flare Header Run Lengths (basis) | 270 m / 50 m (heated / unheated basis) | `4-25_Deepcut_DBM.md` line 2042 |
| LP Flare Stack Element Material | SA-106 (header basis) | `4-25_Deepcut_DBM.md` line 2042 |
| LP Flare Stack Element OD | 324 mm header; element OD on common stack TBD | `4-25_Deepcut_DBM.md` lines 2031, 2042 |
| Drum Quantity at 4-25 | 1 (V-3900-1) | `4-25_Deepcut_DBM.md` line 2582 |
| Transfer Pump Quantity at 4-25 | 1 (P-3900-1) | `4-25_Deepcut_DBM.md` line 2581 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Backpressure basis (HP/cryo system) | Up to 695 kPag (100 psig) built-up backpressure at peak coincident fire-zone load (HP/cryo system reference; LP-specific built-up backpressure not stated in accessible slice) | `4-25_Deepcut_DBM.md` line 2044 |
| LP-specific built-up backpressure | TBD (not stated in accessible source slice) | — |
| Typical PSV maximum total backpressure at PSV flange | < 1172 kPag (170 psig) under 150# flange rating | `4-25_Deepcut_DBM.md` line 2044 |
| Relief volumes (LP flare) | TBD; to be determined during detailed design; preliminary Aspen Flare System Analyzer models support current header sizing | `4-25_Deepcut_DBM.md` lines 2021, 2046 |
| Freeze protection (LP flare headers outside heated buildings) | Electrically heat traced and insulated; PSV outlets that free-drain into the flare header are exempt (HP rule explicit; LP heat-trace requirement: ASSUMPTION based on HP rule and free-drain configuration) | `4-25_Deepcut_DBM.md` line 2033 |
| Supplemental fuel gas to LP flare stack | Required for complete combustion of hydrocarbons and sulphur compounds; any blended gas mixture to flare LHV >= 20 MJ/Sm3 | `4-25_Deepcut_DBM.md` line 2033 |
| LP stack smokeless basis | Air blower for smokeless operation; Ringelmann 1 at approximately 5% (TBC) of emergency design case flare loads | `4-25_Deepcut_DBM.md` line 2031 |
| LP flare stack pilot and purge gas | TBC | `4-25_Deepcut_DBM.md` line 1892 |
| LP Flare Pilot — published source-level estimate (e3m3/d / m3/d / etc.) | 37.18 / 6.29 / 0.02 / 43.48 / 0 / 0 (units per source table) | `4-25_Deepcut_DBM.md` line 2250 |
| LP Flare Purge — published source-level estimate | 523 / 88.87 / 0.26 / 612.4 / 0 / 0.002 | `4-25_Deepcut_DBM.md` line 2251 |
| Radiation criteria at grade | BCER Oil and Gas Processing Facility Regulation App. 1, Sch. 1, §7(4); design limits include 0.7888 kW/m2 solar allowance | `4-25_Deepcut_DBM.md` lines 2050-2057 |
| Distance between flare tanks (including KO drums) and vegetation or other fire hazards | 10 m (32 ft) | `4-25_Deepcut_DBM.md` line 287 (OGAOM §9.6.15) |
| Drum design pressure | TBD (not in accessible source slice) | — |
| Drum design temperature | TBD | — |
| Drum minimum design metal temperature (MDMT) | TBD | — |
| Drum nominal dimensions (D x L/L) | TBD | — |
| Drum orientation | TBD (typical industry practice is horizontal for KO duty: ASSUMPTION) | — |
| Drum corrosion allowance | TBD | — |
| Drum service classification (sour / sweet) | Sour service exposure expected (facility is sour gas; LP flare receives amine regen and VRU streams) — ASSUMPTION for materials selection until vendor confirms | `4-25_Deepcut_DBM.md` lines 5, 7, 2029 |
| Transfer pump P-3900-1 type | Truck-out service — type TBD | `4-25_Deepcut_DBM.md` line 2029 |
| Transfer pump flow / head | TBD | — |
| Transfer pump driver | TBD | — |
| Area electrical classification | TBD; package vendor coordinate with EPC area classification basis | — |

## Construction

| Construction Item | Value | Source |
|---|---|---|
| Module identifier | 390-1 LP Flare KO Drum Module | `4-25_Deepcut_DBM.md` line 2783 |
| Construction approach | Shop-built module | `4-25_Deepcut_DBM.md` line 2783 |
| Vendor scope (per package register) | Package engineering, package design, vendor documentation, and physical equipment package | PACKAGE_REGISTER.csv row PKG-055 |
| EPC Integrator scope | Integration into the process facility, including interfaces, tie-ins, constructability, procurement / construction coordination, and facility-level integration | PACKAGE_REGISTER.csv row PKG-055 |
| Applicable interface types | Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports | PACKAGE_REGISTER.csv row PKG-055 |
| Pressure equipment code | TBD (ASSUMPTION: ASME Section VIII Div. 1 with CRN registration for BC; not stated in accessible source slice) | — |
| Welding / NDE / PWHT requirements | TBD | — |
| External painting / coating | TBD | — |
| Insulation / heat tracing | EHT applicable to LP flare headers outside heated buildings per design basis; drum / pump insulation TBD | `4-25_Deepcut_DBM.md` line 2033 |
| Skid / foundation interface | TBD; structural / foundation interfaces declared in PACKAGE_REGISTER.csv row PKG-055 |
| Nameplate language and units | TBD |

## References

- `_CONTEXT.md` (this deliverable folder)
- `_REFERENCES.md` (this deliverable folder)
- `_DEPENDENCIES.md` (this deliverable folder)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (accessed slices: lines 2020-2057, 2027-2031, 2042-2044, 2250-2272, 2533-2582, 2783)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (row `DEL-055-04_vendor-engineered-equipment-package`)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` (row `PKG-055`)
- `26020-Package_Requirements.docx` package heading 10 — **location TBD** (binary .docx not accessible as text in this run)
- `Workbook Packages` row 57 from `26020-Packages_Interfaces_4_export.xlsx` — **location TBD** (binary .xlsx not accessible as text in this run)
- `Bid Docs/Budgetary/brief.md` and `24292-02-PT-ENR-17-201_HP FKOD_R2.pdf` — **location TBD** (HP FKOD budgetary go-by; not located in accessible _Sources tree)
