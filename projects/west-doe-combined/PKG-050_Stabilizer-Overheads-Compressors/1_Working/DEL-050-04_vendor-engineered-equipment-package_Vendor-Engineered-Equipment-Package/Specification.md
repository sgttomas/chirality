# Specification — DEL-050-04 Vendor Engineered Equipment Package (Stabilizer Overheads Compressors)

## Scope

### In scope (Package Vendor responsibility)
- Engineering, design, fabrication/supply, and delivery of two (2) identical 100 %-capacity Stabilizer Overheads Compressor (SOC) packages for the West Doe Deepcut (04-25) facility. Source: `_CONTEXT.md`; SOW-0173, SOW-0174.
- Package design basis and datasheet set covering compressor frame and cylinders, driver, intercoolers, scrubbers, separation pot, vacuum pump, seal-pot transfer pump, package control panel, and self-framing building. Source: SOW-0175; DBM §SEC-04 L728, L815, L824, L828.
- Vendor documentation supporting subsequent EPC integration review (DEL-050-06) and document turnover (DEL-050-05). Source: `PACKAGE_REGISTER.csv` row PKG-050.

### Out of scope (by others — EPC Integrator)
- Shipping of packages to site; foundation/pile installation; tie-in piping; site electrical connections; mounting platforms and stairs. Source: SOW-0176.
- Facility-level integration, interfaces, constructability, and procurement/construction coordination. Source: `PACKAGE_REGISTER.csv` row PKG-050.

## Requirements

### R-1 — Configuration
The Vendor shall supply two (2) identical Ariel KBC/6 four-stage separable reciprocating compressor packages, each rated for 100 % capacity (operating + standby). Source: SOW-0174, SOW-0175; DBM L718–L720.

### R-2 — Process duty
Each package shall compress combined flashed and stabilizer overhead streams from 345 kPag (50 psig) suction to 7,585 kPag (1,100 psig) final discharge, with discharge routed to amine inlet filter/coalescers or recycled to 1st-stage suction. Source: SOW-0174; DBM L714, L725–L726.

### R-3 — Stage capacities and pressures
Stage design capacities and operating pressures shall meet the values tabulated in Datasheet "Conditions" (Stages 1–4 at 2.5 / 5 / 17 / 17 MMSCFD design; stage suction/discharge pressures per DBM L741–L742). Source: SOW-0176; DBM L734–L742.

### R-4 — Mechanical design margins (MAWP)
Minimum MAWP at 1st-stage suction shall be 1,723 kPag (at 149 °C design temperature) and at 4th-stage final discharge 9,101 kPag (at 177 °C). MAWPs for intermediate stages are TBC and shall be confirmed by the Vendor during detailed engineering. Source: SOW-0176; DBM L766–L773. **ASSUMPTION:** intermediate-stage MAWPs to be set by Vendor analysis bounded by the two confirmed end-point MAWPs.

### R-5 — Driver
Each package driver shall be:
- 4,000 V, 3-phase, 60 Hz electric induction motor; 8-pole; ~891 rpm.
- Rated 2,700 hp (2,013 kW), inclusive of approximately 10 % excess power.
- Equipped with VFD-based speed control supporting 3 : 1 turndown.
- NEMA MG 1 compliant; Class F insulation with Class B rise at full load.
- Non-sparking bidirectional cooling fans; enclosure TBD (TEFC quote requested); explicitly not Toshiba.

Source: SOW-0175, SOW-0176; DBM L721–L724, L828.

### R-6 — Aerial intercoolers
Each stage shall be followed by an aerial intercooler, common-frame AP-661 (modified) configuration, with:
- Warm-air recirculation;
- Plenum heater / heating coil for winter stability;
- Automated louver control with electro-pneumatic transducers and temperature elements integrated to the SOC control system;
- Non-sparking bidirectional cooling.
Cooler discharge temperatures shall be no lower than 65.56 / 87.78 / 65.56 / 77.35 °C (Stages 1–4) and shall remain above the corresponding hydrocarbon dewpoints (53.44 / 85.31 / 58.41 / 71.79 °C). Stage 2 margin to dewpoint is narrow and shall be re-checked. Source: SOW-0175, SOW-0176; DBM L817–L824.

### R-7 — Suction scrubbers
- 1st-stage scrubber shall be two-phase with cyclonic element; remaining stages two-phase with demister.
- All scrubbers shall use mist pads (not mesh / vane assemblies).
- Sizing shall use imperial K factor ≤ 0.25 with applicable pressure deration; vendor confirms sizing for off-design conditions.
- Inlet liquid density assumption 0.61 SG to be reviewed during detailed engineering.

Source: SOW-0175; DBM L815.

### R-8 — Suction pressure control
A dedicated SOC suction PCV shall be provided for each side-stream service in addition to the 1st-stage inlet PCV. Valves shall be ET-type (preferred), shall provide <2 psid differential at 100 % open, and shall fail closed. Source: DBM L815.

### R-9 — Recycle and start-up
- One recycle valve sized for 100 % recycle at 40 % speed and low discharge pressure; supplemental recycle may be added subject to cylinder selection; full-port manual isolation valve on outlet; fail position TBC.
- Automated quarter-turn full-port ball valve for start-up bypass.
- Package shall be capable of start without prior blowdown; equalized-start vs. normal-pressure start is to be evaluated during detailed engineering.

Source: DBM L826.

### R-10 — Packing vents, seal pots, drains
- Cylinder packing drains and vents shall be collected to a header and seal pot.
- Packing vent vapour shall be routed to the VRU suction header.
- Collected liquids shall be removed by local truck-out.
- Suction-scrubber liquid drains shall route to the H2O/HCL drain header.

Source: DBM L714, L828.

### R-11 — Lube oil and purge
- Electric circulating lube-oil heater shall be provided to maintain frame oil temperature for quick start.
- Supplemental lube-oil pump provisions shall be included where required by the compressor OEM.
- A manual sweet-gas purge connection shall be provided at 1st-stage suction immediately downstream of the inlet PCV.

Source: DBM L828.

### R-12 — Building and shipment
The package shall be enclosed in a self-framing building covering instrumentation, designed for modular shop assembly and disassembly into three pieces for shipping. Whether the package may ship as a single assembly is TBC. Source: DBM L728.

### R-13 — Control allocation
- Compressor unit control panel shall manage package-internal control and SOC package blowdown.
- SOC suction-header blowdowns upstream of side-stream suction PCVs shall be wired to and controlled by the balance-of-plant control system (Vendor shall accommodate the interface). Specific blowdown valve locations are TBC during detailed engineering.

Source: DBM L813.

### R-14 — Gas composition basis
The Vendor shall design for the SOC normal-winter composition tabulated in DBM §SEC-04 L779–L805 (notably Stage 1 H2S 1.37 mol %, water 1.15 mol %, mercaptans/CS2/BTEX present in trace amounts). Composition is flagged TBC due to transient inlet streams; Vendor shall confirm material selection and corrosion allowance accordingly. Source: DBM L777–L805.

### R-15 — Exclusions surfaced
No package-specific exclusions are stated in source materials beyond the "by others" items in R-Scope and SOW-0176. Source: `PACKAGE_REGISTER.csv` row PKG-050 (`TBD; no package-specific exclusions stated in source materials.`).

## Standards

| Standard | Application | Location |
|---|---|---|
| NEMA MG 1 | Motor tested/labelled to this standard | SOW-0176; DBM L828 |
| Ariel KBC/6 OEM standards | Compressor frame/cylinder design basis | SOW-0175; DBM L719 |
| Owner / EPC project specifications | General mechanical, electrical area classification, fire & gas, structural, HVAC, EHT, grounding, lighting | `PACKAGE_REGISTER.csv` row PKG-050 — interface types list; **location TBD** for specific specification documents (not present in locally accessible source set) |
| CSA / provincial pressure-equipment codes (BC) | Pressure-containing components — registration jurisdiction | **ASSUMPTION — likely applicable**; **location TBD** (not stated in accessible source slice) |
| API 618 / API 11P (reciprocating compressors) | Reciprocating compressor package design | **ASSUMPTION — likely applicable for an Ariel KBC/6 reciprocating package**; **location TBD** (not stated in accessible source slice) |

## Verification

| Requirement | Verification approach |
|---|---|
| R-1 / R-2 / R-3 | Vendor performance data, OEM proof-test results, capacity curves cross-checked against DBM stage tables. |
| R-4 | Pressure-vessel registrations / U-stamps / CSA registrations + hydrotest records for scrubbers and separation pot; package MAWP datasheet. |
| R-5 | Motor test certificates (NEMA MG 1), VFD compatibility / motor + drive harmonics study, name-plate inspection. |
| R-6 | Cooler thermal performance test; field check of louver / plenum-heater controls; winter operability narrative review. |
| R-7 | Scrubber sizing calculations and mist-pad datasheets; capacity-range turn-down review. |
| R-8 | Valve datasheets confirming ET type, ΔP-at-open, fail action. |
| R-9 | Recycle valve sizing and stroke test; start-up philosophy walk-through. |
| R-10 / R-11 | P&ID review of vent / drain routing; lube-oil heater functional test; sweet-gas purge ISO. |
| R-12 | Shop-assembly inspection; ship-loose list; transportation study. |
| R-13 | Control-philosophy document review; FAT of unit control panel including BoP interface I/O. |
| R-14 | Materials selection report; corrosion allowance review against NACE-equivalent practice for sour service. |

## Documentation

Documentation delivered by the Vendor through this deliverable supports DEL-050-05 (Vendor Document Turnover Package). Anticipated artifacts:

- Vendor engineered physical equipment package (the equipment itself). Source: `_CONTEXT.md`.
- Vendor package design basis and datasheet set. Source: `_CONTEXT.md`.
- Supporting items expected (per `PACKAGE_REGISTER.csv` interface types list and standard mechanical-package practice): equipment datasheets, P&IDs, GA drawings, electrical one-lines, area-classification drawings, motor and VFD datasheets, control narrative, cause-and-effect, materials of construction list, weld map, hydrotest records, FAT/SAT procedures, O&M manuals, spare-parts lists. **ASSUMPTION** — specific deliverable list to be confirmed against the package vendor documentation requirements (referenced in `26020-Package_Requirements.docx`; **location TBD** for clause-level list).
