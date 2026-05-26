# Datasheet — DEL-047-04 Vendor Engineered Equipment Package (VRU 4-25)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-047-04_vendor-engineered-equipment-package | _CONTEXT.md |
| Deliverable Name | Vendor Engineered Equipment Package | _CONTEXT.md |
| Parent Package | PKG-047 Vapour Recovery Unit 4-25 | _CONTEXT.md; PACKAGE_REGISTER.csv |
| Workbook Packages Row | 101 | PACKAGE_REGISTER.csv |
| Package Tag | 26020-01-PT-12-002 — Vapour Recovery Unit | PACKAGE_REGISTER.csv |
| Discipline | Mechanical | PACKAGE_REGISTER.csv; _CONTEXT.md |
| Deliverable Type | Vendor Package Production Unit | DELIVERABLE_REGISTER.csv |
| Responsible Party | Package Vendor (engineering, design, equipment) with EPC Integrator integration review | DELIVERABLE_REGISTER.csv |
| Facility | West Doe Deepcut expansion, 04-25 (LSD 04-25-80-15W6) | DBM-Deepcut/4-25_Deepcut_DBM.md SEC-01 |

## Attributes (Package Configuration)

Two (2) complete 100% capacity VRU compressor packages in a lead-lag configuration for sour service, both housed in one building. (Source: PACKAGE_REGISTER.csv summary, 26020-Package_Requirements.docx package heading 2; location TBD.)

Per train:

| Attribute | Value | Source |
|---|---|---|
| Quantity / sparing | 2 x 100% (lead-lag); second normally standby at design | DBM-Deepcut/4-25_Deepcut_DBM.md, SEC "VRU Configuration and Design Parameters" |
| Compressor type | Ro-Flo 17S / 217M, two-stage rotary vane, positive displacement | DBM 4-25, VRU Configuration; PACKAGE_REGISTER.csv |
| Capacity control | Speed control plus automated recycle valve (second-stage discharge to first-stage suction) | DBM 4-25, VRU Configuration; VRU Scrubbing/Cooling/Blowdown/Controls |
| Design capacity (per train) | 1.5 MMSCFD / 42 e3m3/d, TBC | DBM 4-25, VRU Configuration |
| Driver | 200 hp VFD motor (per PACKAGE_REGISTER) — CONFLICT: DBM notes "200 hp TBC and 300 hp conflict requires ruling" | PACKAGE_REGISTER.csv; DBM 4-25, VRU Configuration |
| Motor voltage | 4,000 V, 3 phase | DBM 4-25, VRU Configuration |
| Driver speed range | 310 to 760 rpm, TBC | DBM 4-25, VRU Configuration |
| Driver turndown | 3:1 on inverter duty | DBM 4-25, VRU Configuration |
| Mechanical seal | Dual mechanical pressurized barrier seal with barrier-fluid alarm | DBM 4-25, VRU Configuration |
| Primary seal vent | Routed to LP flare | DBM 4-25, VRU Configuration |
| Housing | Each VRU installed in an individual building with associated utilities | DBM 4-25, VRU Configuration |

## Process Conditions

### Design Pressures

| Parameter | Value | Source |
|---|---|---|
| Design suction pressure | 0.9 kPag / 2 oz/in2 | DBM 4-25, VRU Configuration |
| Design discharge pressure | 483 kPag / 70 psig | DBM 4-25, VRU Configuration |
| 1st-stage discharge MAWP (min) | 552 kPag | DBM 4-25, VRU system MAWP table |
| 2nd-stage discharge MAWP (min) | 1,034 kPag | DBM 4-25, VRU system MAWP table |
| 1st-stage suction MAWP | TBC | DBM 4-25, VRU system MAWP table |
| 2nd-stage suction MAWP | TBC | DBM 4-25, VRU system MAWP table |
| Design temperatures (all VRU system points) | TBC | DBM 4-25, VRU system MAWP table |

### Inlet Pressure Action Setpoints

| Inlet pressure | Action | Source |
|---|---|---|
| 1 oz | Shutdown VRU | DBM 4-25, VRU inlet pressure table |
| 2 oz | Make-up fuel gas control setpoint; design suction pressure at VRU inlet flange | DBM 4-25 |
| 2.5 oz | Shut down second VRU if already operating | DBM 4-25 |
| 3 oz | VRU control setpoint | DBM 4-25 |
| 5 oz | Start second VRU package | DBM 4-25 |
| 8 oz | Open suction valve/regulator to flare | DBM 4-25 |
| 16 oz | Thief hatch setpoint | DBM 4-25 |

### Inlet Capacity (per stage)

| Stage | Low MMSCFD | Winter MMSCFD | Summer MMSCFD | High | Design |
|---|---:|---:|---:|---:|---:|
| 1 | TBC | 0.4213 | 0.5794 | TBC | 1.5 TBC |
| 2 | TBC | 0.4182 | 0.5638 | TBC | 1.5 TBC |

Source: DBM 4-25, VRU inlet capacity table.

### Cooler Discharge / Dewpoint

| Parameter | 1st stage, °C | 2nd stage, °C |
|---|---:|---:|
| Cooler discharge temperature | 48.9 | 60.0 |
| Dewpoint temperature | 52.7 | 55.8 |

Source: DBM 4-25, VRU Scrubbing/Cooling/Blowdown/Controls. Note: first-stage cooler discharge is below dewpoint; condensation expected at first-stage intercooler outlet.

### Inlet Composition (Summer)

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
| n-Heptane | 0.1675 | n-Octane | 0.0490 |

Source: DBM 4-25, VRU Inlet Composition (Summer). Service is sour (H2S, mercaptans, sulphides).

## Construction

| Item | Value | Source |
|---|---|---|
| Suction scrubber | Two-phase, one upstream of each compression stage; mist pad internals (no mesh/vane); K-factor 0.25 max (Imperial) plus operating-pressure de-rating | DBM 4-25, VRU Scrubbing/Cooling/Blowdown/Controls |
| Scrubber liquid density basis | ≥ 0.61 SG, to be reviewed | DBM 4-25 |
| Cooler | Air-cooled with manual warm-air recirculation louvers (base); automatic recirculation to be considered; no bundle temperature control provision | DBM 4-25 |
| Recycle valve | Second-stage discharge to first-stage suction; sized for 100% flow at minimum driver speed and lowest operating discharge pressure | DBM 4-25 |
| Make-up / blanket gas | LP fuel gas regulator at suction; maintains minimum suction pressure at maximum turndown | DBM 4-25 |
| Sweet-gas purge | Manual purge connection at first-stage suction immediately downstream of inlet manual isolation valve | DBM 4-25 |
| Blowdown | Package blowdown valves route to LP flare under compressor unit control-panel control | DBM 4-25 |
| Building | One building houses both trains (per package summary in PACKAGE_REGISTER); DBM also states each VRU installed in an individual building. CONFLICT — see Guidance.md | PACKAGE_REGISTER.csv; DBM 4-25 |
| Service classification | Sour | PACKAGE_REGISTER.csv; DBM 4-25 inlet composition |

## Applicable Interfaces

From PACKAGE_REGISTER.csv applicable interface types for PKG-047:

- Process Piping
- Utility Piping
- Relief / Flare / Vent
- Drain / Containment
- Electrical Power
- EHT (electric heat tracing)
- Grounding / Bonding
- Area / Exterior Lighting
- I&C / Control Cabling
- Building HVAC / Services
- Fire & Gas / Safety Systems
- Maintenance Access
- Structural / Foundations / Supports

## References

- _REFERENCES.md (this deliverable)
- _CONTEXT.md (this deliverable)
- DBM-Deepcut/4-25_Deepcut_DBM.md — sections: "Vapour Recovery Unit" (VRU Configuration and Design Parameters; VRU Inlet Composition; VRU Scrubbing, Cooling, Blowdown, and Controls); Interfaces, Controls, Safeguards, and Open Design Development.
- PACKAGE_REGISTER.csv (GATE-07 snapshot) — row PKG-047.
- DELIVERABLE_REGISTER.csv (GATE-07 snapshot) — row DEL-047-04.
- 26020-01-PT-RFQ-12-002_VRU_2_R0.docx — cited as Word Source Basis in PACKAGE_REGISTER but not locally accessible (location TBD; clause-level requirements TBD).
- 26020-Package_Requirements.docx package heading 2 — not locally accessible (location TBD).
