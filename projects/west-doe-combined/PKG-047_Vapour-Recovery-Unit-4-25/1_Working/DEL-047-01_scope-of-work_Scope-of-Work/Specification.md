# Specification — DEL-047-01 Scope of Work (PKG-047 Vapour Recovery Unit 4-25)

> Normative document. Requirements derive from accessible sources; inferred requirements are labeled `ASSUMPTION`; missing values marked `TBD`. Source-grounding: see `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (the "DBM"); `_REFERENCES.md`.

## Scope

### In Scope

This Scope of Work covers the **EPC Integrator** scope for Package PKG-047 (Vapour Recovery Unit, 04-25 facility), addressing the full package scope items SOW-0253, SOW-0254, SOW-0255, and SOW-0256, including:

- Two (2) 100% Ro-Flo 17S / 217M two-stage rotary VRU compressor packages with individual buildings and associated utilities (DBM lines 1687, 1692).
- Two-phase suction scrubbers upstream of each compression stage (DBM line 1768).
- Inter-stage and after-coolers with manual warm-air recirculation louvers (DBM line 1772).
- Capacity-control recycle, make-up/blanket gas regulator, blowdown to LP flare, VRU-suction-to-flare V-ball control valve, and sweep/purge connections (DBM lines 1781-1791).
- Tagged equipment list (TBD — see Datasheet), package function description, source basis citations, package physical and functional boundaries, and whole-facility integration narrative (per `_CONTEXT.md` Anticipated Artifacts and DBM §Vapour Recovery Unit).
- Responsibility assignment record covering EPC Integrator, Package Vendor, and downstream/upstream interfacing parties (per decomposition register rows 570-575).

### Out of Scope (carried by sibling deliverables or other packages)

- Vendor package internal engineering, design, and equipment supply — `DEL-047-04_vendor-engineered-equipment-package`.
- Vendor document submittals and turnover — `DEL-047-05_vendor-document-turnover-package`.
- EPC vendor review/acceptance evidence — `DEL-047-06_epc-vendor-package-review-and-acceptance`.
- Package datasheet (technical handoff) — `DEL-047-02_package-datasheet`.
- Construction installation/tie-in workface plan — `DEL-047-03_construction-work-package`.
- Stabilizer Overheads Compressor scope (downstream interface only) — separate SEC-04 SOC package.
- LP and HP flare systems, fuel gas system, produced water systems — separate facility utilities packages.

## Requirements

### REQ-VRU-001 — Quantity and Sparing
Two (2) VRU packages shall be provided, configured as 2 x 100% with lead-lag capability and the second unit normally on standby at design conditions.
- Source: DBM line 1687.
- Verification: design document review against vendor scope.

### REQ-VRU-002 — Compressor Type and Capacity Control
Each VRU shall use a Ro-Flo 17S / 217M two-stage rotary compressor with speed control plus an automated recycle valve for capacity control.
- Source: DBM lines 1692-1693.
- Verification: vendor data sheet review.

### REQ-VRU-003 — Design Performance Envelope
Each VRU shall be designed to (TBC where indicated):

| Parameter | Value |
|---|---|
| Design capacity | 1.5 MMSCFD / 42 e3m3/d (TBC) |
| Design suction pressure | 0.9 kPag / 2 oz/in² |
| Design discharge pressure | 483 kPag / 70 psig |
| Driver speed range | 310-760 rpm (TBC) |
| Driver turndown | 3:1 on inverter duty |

- Source: DBM lines 1694-1700.
- Verification: vendor performance curves and factory acceptance test (FAT) data.

### REQ-VRU-004 — Electrical Driver
Driver shall be a 4,000 V, 3-phase motor.
- Motor power: `TBD`. **CONFLICT:** DBM line 1698 records "200 hp TBC and 300 hp conflict requires ruling." Final power rating is `NEEDS_HUMAN_RULING` (see `Guidance.md` Conflict Table CT-01).
- Source: DBM lines 1697-1698.
- Verification: electrical load list reconciliation; motor nameplate verification at FAT.

### REQ-VRU-005 — Mechanical Sealing
Each compressor shall use a dual mechanical pressurized barrier seal with barrier-fluid alarm. Primary seal vent shall be routed to LP flare.
- Source: DBM lines 1701-1702.
- Verification: vendor seal certification; routing P&ID review.

### REQ-VRU-006 — Pressure Containment / MAWP (minimum)
Minimum MAWP shall be:

| Location | MAWP (kPag) |
|---|---:|
| First-stage discharge | 552 |
| Second-stage discharge | 1,034 |
| First-stage suction | TBC |
| Second-stage suction | TBC |

Design temperatures TBC.
- Source: DBM lines 1732-1737.
- Verification: vendor pressure-test certificates per applicable code (`ASSUMPTION:` ASME B31.3 / ASME Section VIII Division 1, `location TBD`).

### REQ-VRU-007 — Suction Scrubbers
Each compression stage shall be preceded by a two-phase suction scrubber with mist pad (not mesh/vane). Sizing basis: K factor ≤ 0.25 (Imperial) de-rated for operating pressure. Inlet liquid SG assumed ≥ 0.61 (TBR). Off-design conditions (low compression ratio, high package capacity, high suction pressure, low discharge pressure during startup) shall be evaluated.
- Source: DBM lines 1768-1770.
- Verification: scrubber sizing calc review; vendor data sheet.

### REQ-VRU-008 — Cooling and Condensation Management
- Cooler base design shall include manual warm-air recirculation louvers; automatic recirculation to be considered to reduce condensation risk.
- No bundle temperature control provision.
- First-stage cooler discharge: 48.9 °C; dewpoint 52.7 °C → condensation expected at first-stage intercooler outlet; scrubber and cooler controls must accommodate.
- Source: DBM lines 1772, 1774-1779.
- Verification: thermal/hydraulic check by detailed engineering; condensation rate review.

### REQ-VRU-009 — Inlet Pressure Setpoint Schedule
The VRU control logic shall implement the inlet-pressure setpoint schedule:

| Inlet pressure | Action |
|---|---|
| 1 oz | Shutdown VRU |
| 2 oz | Make-up fuel-gas control setpoint (= design suction pressure at VRU inlet flange) |
| 2.5 oz | Shut down second VRU if already operating |
| 3 oz | VRU control setpoint |
| 5 oz | Start second VRU package |
| 8 oz | Open suction valve / regulator to flare |
| 16 oz | Thief hatch setpoint (atmospheric tanks) |

- Source: DBM lines 1722-1730.
- Verification: control narrative review; FAT functional testing.

### REQ-VRU-010 — Recycle Valve
A capacity-control recycle valve shall route from second-stage discharge to first-stage suction, sized for 100% flow at minimum driver speed and lowest operating discharge pressure, sufficient to maintain first-stage suction pressure.
- Source: DBM line 1783.
- Verification: valve sizing calc review.

### REQ-VRU-011 — Make-up / Blanket Gas
A make-up/blanket gas regulator supplied from the LP fuel gas system shall maintain minimum suction pressure at maximum turndown.
- Source: DBM line 1785.
- Verification: regulator sizing and tie-in review.

### REQ-VRU-012 — VRU Suction Header to Flare
A V-ball control valve shall be provided on the VRU suction header, bypassing the VRU system directly to LP flare when the VRU packages are not operational, operating on VRU suction pressure. Discharge of the valve shall include a check valve with ≤ 0.25 psid pressure drop at design conditions to prevent backflow to tanks. The valve shall be located in the pipe rack; the header shall free-drain (no traps or pockets) and slope toward the LP flare knock-out. Pressure measurement shall include first-stage suction pressure and tank-farm VRU header pressure so VRU and flare PCV controls maintain tank vapour-space pressure despite suction-header pressure drop. Valve capacity is at minimum the maximum VRU flow condition (TBC).
- Source: DBM lines 1787-1789.
- Verification: P&ID review; header hydraulic check; valve sizing calc.

### REQ-VRU-013 — Blowdown
VRU package blowdown valves shall route to LP flare under compressor unit control-panel control.
- Source: DBM line 1781.
- Verification: blowdown logic review and FAT testing.

### REQ-VRU-014 — Maintenance Sweep / Purge
A manual sweet-gas purge connection shall be provided at first-stage suction, immediately downstream of the inlet manual isolation valve.
- Source: DBM line 1791.
- Verification: P&ID and piping review.

### REQ-VRU-015 — Discharge Routing Interface
Each VRU discharge shall be routed to the 04-25 Stabilizer Overheads Compressor first-stage suction header. The 03-25 VRU discharge shall also be tied into the same 04-25 SOC suction.
- Source: DBM lines 1683, 1373.
- Verification: interface document review with SOC package; P&ID tie-point review.

### REQ-VRU-016 — Source-Side Connectivity
The VRU header shall collect vapours from the sources listed in the Datasheet (storage tanks for produced water, C5+ slop, C5+ storage; amine slop and surge tanks; TEG regeneration overheads after upstream water condensation, with BTEX recompressed to plant inlet and recovered liquids pumped to produced water tanks; compressor packing drain/vent seal-pot vapours from sour inlet, booster, and SOC packages). Fresh caustic tank and TEG make-up storage tank shall NOT be connected to the VRU header.
- Source: DBM lines 1373, 1562, 1232, 1663, 928, 967, 1029, 1074, 1709-1720, 1781.
- Verification: P&ID coverage check; tank-vapour routing review.

### REQ-VRU-017 — Scope of Work Document Contents
The Scope of Work deliverable shall, at minimum, contain:

1. Package identity (name, ID, parent package, facility, location).
2. Package function statement.
3. Tagged equipment list (compressors, scrubbers, coolers, key valves, drivers).
4. Package physical and functional boundaries.
5. Source basis citations (DBM section, workbook row, package requirements heading).
6. Whole-facility integration narrative including upstream sources and downstream discharge.
7. Responsibility assignment record.
8. Coverage map to SOW items SOW-0253..SOW-0256 and objectives OBJ-001, OBJ-003..OBJ-010.

- Source: `_CONTEXT.md` Anticipated Artifacts; decomposition register row 570.
- Verification: deliverable QA checklist review (see `Procedure.md`).

## Standards

| Standard | Applicability | Source / location |
|---|---|---|
| API 2000 | Used for blanket gas rates on condensate tanks tied to VRU header | DBM line 1663 |
| NEMA MG 1 | Compressor motor compliance (referenced for SOC; `ASSUMPTION:` applicable to VRU motors of similar class — `location TBD`) | DBM line 828 (SOC), inferred |
| ASME B31.3 | Process piping design (`ASSUMPTION:` applicable; `location TBD`) | inferred |
| ASME Section VIII Div. 1 | Pressure vessel design (scrubbers, separators) (`ASSUMPTION:` applicable; `location TBD`) | inferred |
| CSA Z662 / B51 | Canadian jurisdictional piping/pressure equipment (`ASSUMPTION:` applicable for BC facility; `location TBD`) | inferred |
| Provincial / BC OGC regulations | Site / emissions / venting regulations (`ASSUMPTION:` applicable; `location TBD`) | inferred |

Inferences above are explicit assumptions pending confirmation from `26020-Package_Requirements.docx` heading 2 source extraction.

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-VRU-001..003, 005, 010 | Vendor data sheet / curve review; FAT |
| REQ-VRU-004 | Conflict ruling required; load list and nameplate verification |
| REQ-VRU-006 | Pressure-test certificate review per applicable code |
| REQ-VRU-007 | Scrubber sizing calc audit |
| REQ-VRU-008 | Thermal/hydraulic check; commissioning observation of condensation behaviour |
| REQ-VRU-009, 013 | Control narrative review; FAT functional test |
| REQ-VRU-011, 012, 014 | P&ID/sizing review; tie-in verification |
| REQ-VRU-015, 016 | Cross-package interface review (SOC, tanks, flare, fuel gas) |
| REQ-VRU-017 | Deliverable QA gate (this Scope of Work artifact set) |

## Documentation (anticipated artifacts produced under this Scope)

- Package scope of work narrative (this Specification + Datasheet excerpts).
- Tagged equipment and package identity list (Datasheet §Tagged Equipment List — currently `TBD`).
- Package function and integration narrative (Datasheet §Attributes, §Boundaries).
- Responsibility assignment record (Datasheet §Responsibility Assignment Record).
- Coverage / traceability matrix to SOW-0253..SOW-0256 and OBJ-001, OBJ-003..OBJ-010.
- Conflict log: see `Guidance.md` §Conflict Table.
