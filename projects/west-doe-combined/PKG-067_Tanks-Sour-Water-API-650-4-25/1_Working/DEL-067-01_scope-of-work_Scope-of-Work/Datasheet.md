# Datasheet — DEL-067-01 Scope of Work

> Descriptive datasheet for the EPC Scope of Work deliverable covering PKG-067 "Tanks, Sour Water (API 650) 4-25". Values are sourced from the GATE-07 PROJECT_DECOMP snapshot, 26020-Package_Requirements.docx (heading "26020-01-PT-19-005 - Tanks, Sour Water"), and DBM-Deepcut/4-25_Deepcut_DBM.md. Unknown values are recorded as `TBD`; inferences are labeled `ASSUMPTION`.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-067-01_scope-of-work` | `_CONTEXT.md` |
| Deliverable Name | Scope of Work | `_CONTEXT.md` |
| Parent Package | `PKG-067` — Tanks, Sour Water (API 650) 4-25 | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 94 |
| Package Source Heading | `26020-01-PT-19-005 - Tanks, Sour Water` | `26020-Package_Requirements.docx` heading 276 |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable Type | EPC Scope of Work | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 528 |
| Responsible Party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Decomposition Snapshot | GATE-07_Final_Published_2026-05-24 | `_REFERENCES.md` |
| Covered Scope Items | `SOW-0225`, `SOW-0226`, `SOW-0227`, `SOW-0228` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supported Objectives | `OBJ-001`, `OBJ-003`–`OBJ-010` (ASSUMPTION: PACKAGE_HEURISTIC) | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |

## Attributes (Package Subject)

| Attribute | Value | Source |
|---|---|---|
| Package Service | Produced-water / sour-water atmospheric storage for 4-25 (Deepcut) plant | `26020-Package_Requirements.docx` Basic Scope; DBM §"Produced Water" |
| Tag Set | `TK-9010-1`, `TK-9020-1` (two tanks) | `26020-Package_Requirements.docx` Major Included Equipment; DBM table row 2627 |
| Quantity | 2 tanks | `PACKAGE_REGISTER.csv`; DBM row 2559 |
| Governing Standard | API 650 (modified atmospheric) | `26020-Package_Requirements.docx`; DBM §"Produced Water" (analog "Condensate tank specification: Modified API 650") |
| Capacity (nominal per tank) | 2,000 bbl (per DBM facility totals table row 493) | DBM line 493 |
| Tank Specification Class | Modified API 650 (ASSUMPTION by analogy with condensate tank line 1646; sour-water-specific clause text TBD) | DBM line 1646 |
| Design Specific Gravity | 1.25 (TBC) | DBM line 508 |
| Operating Service Fluid | Produced water (may contain trace lube oils, hydrocarbons, TEG, amine, H2S, caustic, mercaptans — non-exhaustive, TBC) | DBM line 508 |
| Average accumulation rate at 04-25 | 60 m3/d continuous | DBM line 506 |
| Batch pump-out rate to 03-25 Liquids Hub | ~240 m3/d | DBM line 506 |
| Retention (per facility table) | ~8.9 days based on 380 bbl/d / 2 x 2,000 bbl | DBM line 493 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Location | West Doe Deepcut facility, LSD 04-25-80-15W6, ~22.2 km N of Dawson Creek, BC | DBM lines 7, 19 |
| Ambient temperature (historical) | -19 °C min; 22.2 °C max | DBM line 196 |
| Vapour handling | LP fuel gas blanket; VRU suction/header connection as applicable | `26020-Package_Requirements.docx` Major Included Equipment |
| Pressure / vacuum protection | PVRV; EPRV sizing — review during detailed engineering | DBM line 524; `26020-Package_Requirements.docx` |
| Tank isolation philosophy | Review in context of potential sour vapours (TBD) | DBM line 524 |
| Inter-tank spacing | NFPA 30 Table 22.4.2.1 — informational | DBM line 268 |

## Construction (as defined in source)

| Item | Provision | Source |
|---|---|---|
| Internal coating | Devchem 253 on floor, walls, and roof | DBM line 524 |
| External insulation | Externally insulated | DBM line 524 |
| Heating | Electric/heated (where required) | DBM line 524; `26020-Package_Requirements.docx` |
| Hydrocarbon skim | Kennilworth-type hydrocarbon skim float system | DBM line 524 |
| Relief | At least one PVRV per tank; EPRV sizing TBD | DBM line 524 |
| Instrumentation / appurtenances | Tank instrumentation and standard tank appurtenances | `26020-Package_Requirements.docx` |
| Tank dimensions (diameter, height, shell, roof) | TBD | not specified in available sources |
| Capacity at maximum operating level | TBC (DBM facility table indicates 2 x 2,000 bbl) | DBM line 493 |

## Package Boundary (high level)

| Boundary | Provision | Source |
|---|---|---|
| Tie-in: Produced water transfer pumps | Suction taken from these tanks by 2 x 100% produced water transfer pumps (located in Tank Farm Pump Building 2 / PKG-060) | DBM lines 521, 2555 |
| Tie-in: Outlet | New pipeline to 03-25 Liquids Hub; truck-out for emergency/local handling | DBM line 493, 506 |
| Tie-in: VRU | Vapour to VRU package suction header (where applicable) | `26020-Package_Requirements.docx`; DBM line 1683 |
| Drain/coalesced water sources received | NGL water-wash recycle drain (line 1558); mole-sieve inlet coalescer (line 1602); regeneration gas scrupper drain (line 1621); compressor stage-1 scrubber liquid (line 1025); various 300# ANSI produced-water drain header sources (line 2013) | DBM as cited |
| Pipeline beyond facility battery limit | Designed/installed by others | DBM line 506 |

## Interface Types (per PACKAGE_REGISTER row 94)

- Process Piping
- Relief / Flare / Vent
- Drain / Containment
- Grounding / Bonding
- Area / Exterior Lighting
- Cathodic Protection
- I&C / Control Cabling
- Grading / Site Drainage / Spill Containment
- Structural / Foundations / Supports

## References

- `_REFERENCES.md` — full reference register for this deliverable
- `_CONTEXT.md` — deliverable identity and scope items
- GATE-07 PROJECT_DECOMP snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `PACKAGE_REGISTER.csv` row 94 (PKG-067)
  - `DELIVERABLE_REGISTER.csv` row 528 (DEL-067-01)
- `_Sources/26020-Package_Requirements.docx` — heading "26020-01-PT-19-005 - Tanks, Sour Water" (paragraph 276 ff.)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — Produced Water section (§ lines 502–525); facility design tables (lines 268, 493, 1646, 1714, 2013, 2555–2559, 2627)
- Analog: `26020-03-PT-19-007 - Tanks, Sour Water` (Word source basis cited in PACKAGE_REGISTER row 94 for 3-25 analog)
