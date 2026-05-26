# Datasheet — DEL-047-01 Scope of Work (PKG-047 Vapour Recovery Unit 4-25)

> Descriptive document. Values are sourced from accessible references; unknowns are marked `TBD`; inferences are labeled `ASSUMPTION`.

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-047-01_scope-of-work` |
| Deliverable Name | Scope of Work |
| ParentPackageID | `PKG-047` |
| Package Name | Vapour Recovery Unit 4-25 |
| Discipline | Mechanical |
| Type | EPC Scope of Work |
| Responsible Party | EPC Integrator |
| Facility | West Doe Deepcut expansion (04-25); LSD 04-25-80-15W6 (`SourcePath: _Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `SectionRef: §Facility Identity`, lines 7,16) |
| Covers Scope Items | SOW-0253, SOW-0254, SOW-0255, SOW-0256 |
| Supports Objectives | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 |

## Attributes (Package Identity)

| Attribute | Value | Source |
|---|---|---|
| Package function | Capture hydrocarbon vapours from storage tanks and low-pressure process vapour sources, compress and cool them, and discharge recovered vapour to the stabilizer overheads compressor (SOC) suction system | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Vapour Recovery Unit (line 1683) |
| Quantity / sparing | 2 x 100% (lead-lag with standby) | DBM §VRU Configuration and Design Parameters (line 1687,1691) |
| Compressor type | Ro-Flo 17S / 217M two-stage rotary compressor | DBM line 1692 |
| Capacity control | Speed control plus automated recycle valve | DBM line 1693 |
| Housing | Each VRU installed in an individual building with associated utilities | DBM line 1687 |
| Discharge routing | Both 04-25 and 03-25 VRU discharges routed to the 04-25 SOC first-stage suction | DBM line 1683 |

## Design Conditions

| Parameter | Value | Source |
|---|---|---|
| Design capacity | 1.5 MMSCFD / 42 e3m3/d, TBC | DBM line 1694 |
| Design suction pressure | 0.9 kPag / 2 oz/in² | DBM line 1695 |
| Design discharge pressure | 483 kPag / 70 psig | DBM line 1696 |
| Motor voltage | 4,000 V, 3-phase | DBM line 1697 |
| Motor power | TBD; 200 hp TBC and 300 hp conflict requires ruling (see Conflict Table in `Guidance.md`) | DBM line 1698 |
| Driver speed range | 310–760 rpm, TBC | DBM line 1699 |
| Driver turndown | 3:1 on inverter duty | DBM line 1700 |
| Mechanical seal | Dual mechanical pressurized barrier seal with barrier-fluid alarm | DBM line 1701 |
| Primary seal vent | LP flare | DBM line 1702 |
| First-stage discharge MAWP (min) | 552 kPag | DBM line 1735 |
| Second-stage discharge MAWP (min) | 1,034 kPag | DBM line 1737 |
| Other MAWP/temperatures | TBC | DBM lines 1734-1737 |

### VRU Inlet Pressure Control Setpoints (Source: DBM lines 1722-1730)

| Inlet pressure | Action |
|---|---|
| 1 oz | Shutdown VRU |
| 2 oz | Make-up fuel gas control setpoint; design suction pressure at VRU inlet flange |
| 2.5 oz | Shut down second VRU if already operating |
| 3 oz | VRU control setpoint |
| 5 oz | Start second VRU package |
| 8 oz | Open suction valve/regulator to flare |
| 16 oz | Thief hatch setpoint |

### VRU Inlet Capacity (Source: DBM line 1704-1707)

| Stage | Low | Expected winter | Expected summer | High | Design | Excess |
|---|---:|---:|---:|---:|---:|---:|
| Stage 1 (MMSCFD) | TBC | 0.4213 | 0.5794 | TBC | 1.5 TBC | TBC |
| Stage 2 (MMSCFD) | TBC | 0.4182 | 0.5638 | TBC | 1.5 TBC | TBC |

### Cooler Discharge vs Dewpoint (Source: DBM lines 1774-1778)

| Parameter | First stage (°C) | Second stage (°C) |
|---|---:|---:|
| Cooler discharge temperature | 48.9 | 60.0 |
| Dewpoint temperature | 52.7 | 55.8 |

Note: First-stage cooler discharge below dewpoint — condensation expected at the first-stage intercooler outlet (DBM line 1779).

## Construction / Configuration

- Each VRU is provided with a two-phase suction scrubber upstream of each compression stage; scrubbers include mist pads (not mesh/vane assemblies); K factor 0.25 maximum (Imperial) with de-rating for operating pressure; inlet liquid SG ≥ 0.61 assumed and TBR (DBM lines 1768, 1770).
- Cooler base design includes manual warm-air recirculation louvers; automatic warm-air recirculation under consideration; no bundle temperature control on the VRU (DBM line 1772).
- VRU package blowdown valves route to LP flare under compressor unit control-panel control (DBM line 1781).
- Capacity-control recycle valve from second-stage discharge to first-stage suction, sized for 100% flow at minimum driver speed and lowest operating discharge pressure (DBM line 1783).
- Make-up/blanket gas regulator supplied from low-pressure fuel gas system; maintains minimum suction pressure at maximum turndown (DBM line 1785).
- VRU suction header to flare valve: V-ball control valve bypassing VRU to LP flare when units not operational; operates on VRU suction pressure; discharge check valve with <0.25 psid drop at design; pipe-rack location; header must free-drain toward LP flare knock-out (DBM line 1787).
- Manual sweet-gas purge connection at first-stage suction immediately downstream of inlet manual isolation valve for maintenance (DBM line 1791).

## VRU Inlet Composition (Summer, mol%) — DBM lines 1742-1764

| Compound | mol% | Compound | mol% |
|---|---:|---|---:|
| Water | 4.5690 | Hydrogen sulfide | 0.3557 |
| CO2 | 0.9434 | C1RSH | 0.3854 |
| Methane | 70.4400 | C2RSH | 1.7050 |
| Ethane | 8.2100 | DiM-sulphide | 0.2333 |
| Propane | 1.5460 | CS2 | 0.1317 |
| Isobutane | 4.3460 | C3RSH | 0.3007 |
| n-Butane | 0.7000 | M-E sulphide | 0.3851 |
| Isopentane | 2.6600 | C6H6 | 0.3700 |
| n-Pentane | 0.4150 | Trace other | 1.6000 |
| n-Hexane | 0.2156 | Nitrogen | 0.3700 |
| n-Heptane | 0.1675 | | |
| n-Octane | 0.0490 | | |

## VRU Gas Sources (Preliminary; under detailed engineering review — DBM line 1709-1720)

| Source | Module | Winter (MMSCFD) | Summer (MMSCFD) | High | Design |
|---|---|---:|---:|---:|---:|
| Compressor sweep and purge gas | 210/540/750 | 0.15 | 0.15 | TBC | TBC |
| Sales booster compressor sweep/purge | 340 | TBC | TBC | TBC | TBC |
| TEG regeneration overheads | 570 | 0.17 | 0.18 | 0.35 | 0.35 |
| Produced water tanks | 900 | TBC | TBC | TBC | TBC |
| C5+ slop tanks | 910 | TBC | TBC | TBC | TBC |
| C5+ storage tanks | 930 | TBC | TBC | TBC | TBC |
| Amine slop and surge tanks | 530 | TBC | TBC | TBC | TBC |
| Remainder | – | 0.10 | 0.24 | – | – |

## Boundaries and Whole-Facility Integration

- Discharge boundary: SOC first-stage suction header at 04-25 (both 04-25 and 03-25 VRU discharges) (DBM line 1683).
- Upstream tank-side boundary: Atmospheric/low-pressure vapour sources including condensate tanks (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 1663), TEG still overheads (DBM line 1227), amine surge tank vapours (DBM line 1373), seal-pot vapours from sour inlet/booster/SOC packing drain/vent recovery (DBM lines 928, 967, 1029, 1074), pressurized caustic drain drum NGL vapours (DBM line 1560 — note: this routes to SOC, not VRU; included for boundary clarity).
- Flare interface: LP flare (blowdown, primary seal vent, suction-header bypass), HP flare for other systems (DBM lines 1702, 1729, 1781, 1787).
- Fuel gas interface: LP fuel gas system for make-up/blanket (DBM line 1785).
- Items explicitly NOT connected to VRU header: fresh caustic tank (DBM line 1562), TEG make-up storage tank (DBM line 1232).

## Tagged Equipment List

`TBD` — Specific equipment tag numbers for VRU compressors, scrubbers, coolers, and valves are not enumerated in the accessible DBM source slice. Tag list to be confirmed from package equipment list / P&ID issue (source `location TBD`).

## Responsibility Assignment Record

| Role | Party | Source |
|---|---|---|
| Package EPC integration, Scope of Work authorship, integration into 04-25 | EPC Integrator | `_CONTEXT.md` (ResponsibleParty); decomposition register row 570 |
| Package vendor engineering, design, fabrication/supply | Package Vendor | Decomposition register row 573 (DEL-047-04) |
| Vendor documentation submittals | Package Vendor | Decomposition register row 574 (DEL-047-05) |
| EPC vendor review and acceptance | EPC Integrator | Decomposition register row 575 (DEL-047-06) |
| Construction installation, tie-in, turnover | EPC Integrator (Construction Work Package) | Decomposition register row 572 (DEL-047-03) |

## References

- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — primary technical source slices: §Vapour Recovery Unit (line 1681 ff), §SEC-04 (line 569 ff), §SEC-07 (line 1397 ff), §VRU row in summary table (line 750).
- `_Sources/26020-Package_Requirements.docx` — package-requirements source for SOW items SOW-0253..SOW-0256; not extracted as locally accessible markdown (`location TBD`).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — workbook Packages row 101 source; not parsed in this pass (`location TBD`).
- Decomposition: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row 570.
