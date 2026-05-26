# Package Datasheet — Flare KO Drum (High Pressure) 4-25 (PKG-054)

> Deliverable: `DEL-054-02_package-datasheet` — EPC Integrator technical handoff datasheet for the High-Pressure Flare Knock-Out (KO) Drum package serving the 04-25 (Deepcut) facility. Package equipment list and tags are taken from the accepted decomposition snapshot (GATE-07) and the Deepcut DBM (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`).

## Identification

| Field | Value | Source |
|---|---|---|
| Package ID | `PKG-054` | `_CONTEXT.md`; GATE-07 `PACKAGE_REGISTER.csv` |
| Package Name | Flare KO Drum (High Pressure) 4-25 | `_CONTEXT.md` |
| Facility | 04-25 (Deepcut) | DBM-Deepcut Sec. Flare Systems Basis (lines 2019-2046) |
| Workbook Row | 55 | `_CONTEXT.md` Source Reference |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Tagged Equipment | V-4100-1 (H.P. FLARE K.O. DRUM); P-4100-1 (HP FLARE K.O. DRUM TRANSFER PUMP) | DBM-Deepcut tag table (lines 2579-2580) |
| Modular Designation | 410-1 HP / Cryo Flare KO Drum Module (shop-built) | DBM-Deepcut module table (line 2784) |
| Service | High-pressure flare relief and blowdown liquid knock-out for 04-25 balance-of-plant outside the cryogenic unit and for low-pressure equipment routed to HP flare | DBM-Deepcut Flare Equipment and Routing (line 2028) |

ASSUMPTION: The decomposition row name "Flare KO Drum (High Pressure) 4-25" maps to the Deepcut tag table entry "Flare KO Drum (High Pressure) 2" (which carries V-4100-1 and P-4100-1 under the 4-25 Deepcut column). Confirmed by tag location column "4-25 (Deepcut)".

## Attributes

| Attribute | Value | Source / Note |
|---|---|---|
| Primary vessel tag | V-4100-1 | DBM-Deepcut line 2580 |
| Primary vessel description | H.P. FLARE K.O. DRUM | DBM-Deepcut line 2580 |
| Transfer pump tag | P-4100-1 | DBM-Deepcut line 2579 |
| Transfer pump description | HP FLARE K.O. DRUM TRANSFER PUMP | DBM-Deepcut line 2579 |
| Transfer pump sparing | One per KO drum, 1 x 100 percent (per Comp_and_Liquids DBM, parallel basis) | DBM-Comp_and_Liquids line 583 (ASSUMPTION: same 1 x 100% basis applies to 04-25 HP KO drum pump) |
| Module assembly | Shop-built (Module 410-1 HP / Cryo Flare KO Drum Module) | DBM-Deepcut line 2784 |
| Co-located equipment in module | Cryogenic flare KO drum V-4110-1 (sister vessel in same shop module) | DBM-Deepcut lines 2578, 2784 |
| Liquid disposition | Truck-out via transfer pump P-4100-1 | DBM-Deepcut line 2028 |
| Vessel dimensions (ID x S/S) | TBD | Source slice does not state V-4100-1 dimensions |
| Design pressure | TBD | Not in available source |
| Design temperature | TBD | Not in available source |
| MOC (vessel shell) | TBD (carbon steel assumed for HP service consistent with SA-333 header material) | ASSUMPTION; not stated in source for vessel itself |
| MAWP / hydrotest | TBD | Not in available source |
| Insulation / heat tracing | HP flare headers outside heated buildings are electrically heat traced and insulated for freeze protection except PSV outlets that free-drain into the flare header. Vessel insulation per detailed design. | DBM-Deepcut line 2033 |
| Internals / demister | TBD | Not in available source |

## Conditions

| Condition | Value | Source |
|---|---|---|
| HP flare relief header size at vessel | 508 mm (20 in) | DBM-Deepcut line 2028 |
| HP flare main header (downstream) | 762 mm (SA-333), 280 m / 10 m basis | DBM-Deepcut line 2039 |
| Estimated peak built-up backpressure (HP / cryogenic) | 695 kPag (100 psig) during peak blowdown coinciding with the highest fire-zone load | DBM-Deepcut line 2044 |
| PSV maximum total backpressure at flange | < 1172 kPag (170 psig) under 150# flange rating | DBM-Deepcut line 2044 |
| Connected service envelope | Balance of plant outside the cryogenic unit and low-pressure equipment routed to HP flare | DBM-Deepcut line 2028 |
| Combined routing downstream | HP flare combines with cryogenic flare downstream of both KO drums before the common HP/cryo stack | DBM-Deepcut lines 2027-2028 |
| Common stack reference (downstream) | HP/cryo element 660 mm (26 in) OD x 200 ft tall (TBC), sonic tip, pilot, pilot proving, auto-ignition, smokeless | DBM-Deepcut line 2030 |
| Minimum LHV of any blended gas to flare | >= 20 MJ/Sm3 | DBM-Deepcut line 2033 |
| Relief volumes / sizing flows | TBD pending detailed design; preliminary Aspen Flare System Analyzer models support current header sizing | DBM-Deepcut line 2021 |
| Spacing — flare KO drums to vegetation / fire hazards | 10 m (32 ft) | DBM-Deepcut line 287 (OGAOM Sec. 9.6.15) |

## Construction

| Item | Basis | Source |
|---|---|---|
| Modular delivery | Shop-fabricated module 410-1 (combined HP / Cryo Flare KO Drum Module) | DBM-Deepcut line 2784 |
| HP flare header material | SA-333 (low-temperature carbon steel) | DBM-Deepcut line 2039 |
| Header sizing basis | 762 mm HP flare main header, 280 m / 10 m run; 508 mm relief lead at vessel | DBM-Deepcut lines 2028, 2039 |
| Freeze protection | Electrical heat tracing and insulation of HP flare headers outside heated buildings (except PSV outlets that free-drain) | DBM-Deepcut line 2033 |
| Layout/spacing | Flare KO drums sited at min. 10 m (32 ft) from vegetation/fire hazards; package spacing per DBM Flare and Incinerator Spacing table | DBM-Deepcut lines 276-289 |
| Foundations | Equipment-specific foundation and anchorage to be designed per final geotechnical report, equipment loads, snow/wind/seismic, frost, vibration, settlement, and maintenance access | DBM-Comp_and_Liquids line 700 (ASSUMPTION: same project-wide basis applies) |
| Pump basis (P-4100-1) | Liquid transfer with truck-out option | DBM-Deepcut line 2028 |
| Vessel internals (demister, vortex breaker, boot) | TBD | Not in available source |
| Nozzle schedule | TBD | Not in available source |

## References

- `_CONTEXT.md` — deliverable identity, package mapping, scope items, supported objectives
- `_REFERENCES.md` — authoritative decomposition basis and Shared Source Root
- GATE-07 PROJECT_DECOMP snapshot — `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `DELIVERABLE_REGISTER.csv` (DEL-054-02 row)
  - `PACKAGE_REGISTER.csv`
  - `OBJECTIVE_DELIVERABLE_MAP.csv`
- DBM-Deepcut — `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
  - Sec. Flare and Incinerator Spacing (lines 276-289)
  - Sec. Flare Systems Basis → Equipment and Routing (lines 2019-2034)
  - Sec. Flare Header and Backpressure Basis (lines 2035-2046)
  - Tag tables (lines 2533-2535, 2577-2582)
  - Module table (lines 2783-2784)
- DBM-Comp_and_Liquids — `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
  - Sec. Flare and Blowdown (lines 495-499)
  - Pump sparing table (lines 583-584)
- 26020-Package_Requirements.docx — package heading 9 (location TBD; native .docx not parsed in this pass)
- 26020-Packages_Interfaces_4_export.xlsx (location TBD; native .xlsx not parsed in this pass)

## Open Items / TBD

- Vessel V-4100-1 mechanical datasheet values (dimensions, design P/T, MOC, MAWP, hydrotest, internals, nozzle schedule): TBD — not present in accessible sources.
- Pump P-4100-1 hydraulic datasheet values (flow, head, NPSHr, driver type, seal plan): TBD — not present in accessible sources.
- Relief load case set and per-case rates feeding V-4100-1: TBD — Aspen Flare System Analyzer outputs not in source slice.
- Package interface requirements matrix (electrical, instrument air, fuel gas purge, drain, controls): TBD — to be developed from 26020-Packages_Interfaces_4_export.xlsx once parsed.
