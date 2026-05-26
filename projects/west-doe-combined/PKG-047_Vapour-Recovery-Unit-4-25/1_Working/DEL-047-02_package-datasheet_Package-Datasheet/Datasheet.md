# Datasheet — DEL-047-02 Package Datasheet (Vapour Recovery Unit 4-25)

> Source-grounded EPC Package Datasheet. Values cite the West Doe 04-25 Deepcut DBM ("DBM-Deepcut") where present; unresolved items are marked `TBD`/`TBC` consistent with the source. Decomposition narrative is used only for scope routing.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-047-02_package-datasheet | `_CONTEXT.md` |
| Deliverable Name | Package Datasheet | `_CONTEXT.md` |
| Parent Package ID | PKG-047 | `_CONTEXT.md` |
| Package Name | Vapour Recovery Unit 4-25 | `_CONTEXT.md` |
| Facility | West Doe Deepcut 04-25 | DBM-Deepcut §Vapour Recovery Unit |
| Discipline | Mechanical (rotating equipment / vapour handling) | `_CONTEXT.md` |
| Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Covers SOW | SOW-0253; SOW-0254; SOW-0255; SOW-0256 | `_CONTEXT.md` |
| Supports Objectives | OBJ-001, OBJ-003..OBJ-010 (PACKAGE_HEURISTIC, ASSUMPTION) | `_CONTEXT.md`; objective association mode |
| Authoritative Source | DBM-Deepcut `4-25_Deepcut_DBM.md` §Vapour Recovery Unit (lines ~1681–1791); 26020-Package_Requirements.docx package heading 2 (`location TBD`, binary not extracted) | `_REFERENCES.md` |

## Attributes

### Package Function

Capture hydrocarbon vapours from storage tanks and low-pressure process vapour sources, compress and cool them, and discharge the recovered vapour to the 04-25 stabilizer overheads compressor (SOC) first-stage suction. Both 04-25 and 03-25 VRU discharges route to the 04-25 SOC first-stage suction. [DBM-Deepcut §Vapour Recovery Unit]

### Quantity / Sparing / Arrangement

| Attribute | Value | Source |
|---|---|---|
| Trains | 2 × 100 % | DBM-Deepcut §VRU Configuration and Design Parameters |
| Operating philosophy | Lead-lag; standby unit normally idle at design conditions | DBM §VRU Configuration |
| Housing | Each VRU installed in an individual building with associated utilities | DBM §VRU Configuration |

### Compressor and Driver

| Attribute | Value | Source |
|---|---|---|
| Compressor type | Ro-Flo 17S / 217M two-stage rotary | DBM §VRU Configuration |
| Capacity control | Speed control plus automated recycle valve | DBM §VRU Configuration |
| Design capacity | 1.5 MMSCFD / 42 e3m3/d (TBC) | DBM §VRU Configuration |
| Design suction pressure | 0.9 kPag (2 oz/in²) | DBM §VRU Configuration |
| Design discharge pressure | 483 kPag (70 psig) | DBM §VRU Configuration |
| Motor voltage | 4,000 V, 3-phase | DBM §VRU Configuration |
| Motor power | TBD — 200 hp (TBC) vs 300 hp; CONFLICT requires human ruling | DBM §VRU Configuration |
| Driver speed | 310–760 rpm (TBC) | DBM §VRU Configuration |
| Driver turndown | 3:1 on inverter duty | DBM §VRU Configuration |
| Mechanical seal | Dual mechanical pressurized barrier seal with barrier-fluid alarm | DBM §VRU Configuration |
| Primary seal vent | LP flare | DBM §VRU Configuration |

### Capacity (per stage)

| Stage | Low (MMSCFD) | Expected winter (MMSCFD) | Expected summer (MMSCFD) | High (MMSCFD) | Design (MMSCFD) | Excess capacity |
|---|---:|---:|---:|---:|---:|---:|
| Stage 1 | TBC | 0.4213 | 0.5794 | TBC | 1.5 (TBC) | TBC |
| Stage 2 | TBC | 0.4182 | 0.5638 | TBC | 1.5 (TBC) | TBC |

Source: DBM-Deepcut §VRU Configuration and Design Parameters.

### Inlet Source Inventory (preliminary; to be reviewed in detailed engineering)

| VRU gas source | Module | Expected winter (MMSCFD) | Expected summer (MMSCFD) | High (MMSCFD) | Design (MMSCFD) |
|---|---|---:|---:|---:|---:|
| Compressor sweep and purge gas | 210/540/750 | 0.15 | 0.15 | TBC | TBC |
| Sales booster compressor sweep and purge gas | 340 | TBC | TBC | TBC | TBC |
| TEG regeneration overheads | 570 | 0.17 | 0.18 | 0.35 | 0.35 |
| Produced water tanks | 900 | TBC | TBC | TBC | TBC |
| C5+ slop tanks | 910 | TBC | TBC | TBC | TBC |
| C5+ storage tanks | 930 | TBC | TBC | TBC | TBC |
| Amine slop and surge tanks | 530 | TBC | TBC | TBC | TBC |
| Remainder | — | 0.10 | 0.24 | — | — |

Source: DBM-Deepcut §VRU Configuration (gas-source table; preliminary).

### Inlet Composition (summer, mol%)

| Compound | mol% | Compound | mol% |
|---|---:|---|---:|
| Water | 4.5690 | n-Octane | 0.0490 |
| CO2 | 0.9434 | Nitrogen | 0.3700 |
| Methane | 70.4400 | Hydrogen sulfide | 0.3557 |
| Ethane | 8.2100 | C1RSH | 0.3854 |
| Propane | 1.5460 | C2RSH | 1.7050 |
| Isobutane | 4.3460 | DiM-sulphide | 0.2333 |
| n-Butane | 0.7000 | CS2 | 0.1317 |
| Isopentane | 2.6600 | C3RSH | 0.3007 |
| n-Pentane | 0.4150 | M-E sulphide | 0.3851 |
| n-Hexane | 0.2156 | C6H6 | 0.3700 |
| n-Heptane | 0.1675 | Trace other | 1.6000 |

Source: DBM-Deepcut §VRU Inlet Composition. Note presence of H2S and sulphur species drives sour-service classification.

## Conditions

### VRU Inlet-Pressure Action Table

| VRU inlet pressure | Action |
|---|---|
| 1 oz | Shutdown VRU |
| 2 oz | Make-up fuel gas control setpoint; design suction pressure at VRU inlet flange |
| 2.5 oz | Shut down second VRU if already operating |
| 3 oz | VRU control setpoint |
| 5 oz | Start second VRU package |
| 8 oz | Open suction valve/regulator to flare |
| 16 oz | Thief hatch setpoint |

Source: DBM-Deepcut §VRU Configuration and Design Parameters.

### MAWP / Design Temperature Envelope

| VRU system point | Minimum MAWP (kPag) | Design temperature |
|---|---:|---|
| First-stage suction | TBC | TBC |
| First-stage discharge | 552 | TBC |
| Second-stage suction | TBC | TBC |
| Second-stage discharge | 1,034 | TBC |

Source: DBM-Deepcut §VRU Configuration.

### Cooling / Condensation Conditions

| Parameter | First stage (°C) | Second stage (°C) |
|---|---:|---:|
| Cooler discharge temperature | 48.9 | 60.0 |
| Dewpoint temperature | 52.7 | 55.8 |

Note: First-stage cooler discharge is **below** dewpoint, so first-stage intercooler-outlet condensation is expected. Suction-scrubber sizing and cooler controls must account for this. Source: DBM-Deepcut §VRU Scrubbing, Cooling, Blowdown, and Controls.

## Construction

### Equipment List (per train, source-stated)

| Item | Basis | Source |
|---|---|---|
| Two-phase suction scrubber (one per stage) | Sized for off-design ops (low ratio, high capacity, high suction P, low discharge P at startup); mist pads (not mesh/vane); K-factor 0.25 max Imperial with pressure derating; inlet liquid SG ≥ 0.61 assumed (TBC) | DBM §VRU Scrubbing… |
| Two-stage rotary compressor | Ro-Flo 17S / 217M | DBM §VRU Configuration |
| Interstage / discharge cooler | Manual warm-air recirculation louvers (base design); automatic warm-air recirculation to be considered; no bundle temperature control | DBM §VRU Scrubbing… |
| Capacity-control recycle valve | Second-stage discharge to first-stage suction; sized for 100 % flow at minimum driver speed and lowest operating discharge pressure | DBM §VRU Scrubbing… |
| Make-up / blanket gas regulator | Maintains minimum suction pressure at max turndown; supplied from LP fuel gas | DBM §VRU Scrubbing… |
| VRU-suction-header-to-flare V-ball control valve | Bypasses VRU to LP flare when units down; check valve on discharge (<0.25 psid at design); pipe-rack location; header free-draining toward LP flare KO | DBM §VRU Scrubbing… |
| Package blowdown valve | Routes to LP flare under compressor-package controls | DBM §VRU Scrubbing… |
| Manual sweet-gas purge connection | At first-stage suction immediately downstream of inlet manual isolation valve | DBM §VRU Scrubbing… |

### Service Classification

- **Sour service** — H2S and mercaptans present in inlet composition (see Attributes). Material/sour-service requirements: `location TBD` (full sour-service basis not in extracted source slices).
- **Cryogenic-adjacent** — No (vapour-recovery duty; not in cryogenic block).
- **Electrical area classification** — `TBD` (not in extracted source slice).

### Interfaces (carried as evidence here per `_CONTEXT.md` Notes)

| Interface | Direction | Basis | Source |
|---|---|---|---|
| 04-25 SOC first-stage suction | Out (discharge) | VRU discharge routes to 04-25 SOC first-stage suction; receives both 04-25 and 03-25 VRU streams | DBM §Vapour Recovery Unit |
| 03-25 VRU discharge | In (combined header) | 03-25 VRU also discharges into the 04-25 SOC first-stage suction | DBM §Vapour Recovery Unit |
| Storage tanks (produced water, C5+ slop, C5+ storage, condensate, amine slop/surge, fresh-caustic tank excluded) | In | Tank vapour spaces routed to VRU suction header; fresh-caustic tank not connected | DBM §VRU; §Caustic storage; §Condensate storage |
| LP flare | Out (bypass / blowdown / seal vent) | Header bypass V-ball; package blowdown; primary mechanical seal vent | DBM §VRU; §Configuration |
| LP fuel gas | In (utility) | Make-up/blanket gas; manual sweet-gas purge for maintenance | DBM §VRU |
| TEG regeneration still overheads | In | Still emissions recovered to VRU suction; normal backpressure ≈ <0.5 psig | DBM §TEG dehydration table |
| Reciprocating compressor packing-vent / seal-pot vapours | In | SOC, sales/booster/acid-gas compressor packing-drain/vent recovery routed to VRU suction header | DBM §SOC, §Booster, §Acid gas compression |
| Electric power | In (utility) | 4,000 V, 3-phase to motor | DBM §VRU |
| Building HVAC / utilities | In (utility) | Each VRU in individual building with utilities; details TBC | DBM §VRU |

## References

- DBM-Deepcut: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — primary source slice §Vapour Recovery Unit (lines ~1681–1791) plus interface mentions across §SOC, §TEG dehydration, §Storage, §Booster, §Acid Gas Compression.
- 26020-Package_Requirements.docx (package heading 2) — listed in `_REFERENCES.md` but binary not extracted; `location TBD`.
- 26020-Packages_Interfaces_4_export.xlsx — listed in shared source root; binary not extracted; `location TBD`.
- Decomposition (routing only): GATE-07 PROJECT_DECOMP snapshot DELIVERABLE_REGISTER.csv row `DEL-047-02_package-datasheet`.
- DBM-Comp_and_Liquids: not consulted for this deliverable (out-of-train basis for 03-25; VRU 03-25 cross-reference is informational only).
