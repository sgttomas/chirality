# Specification — DEL-047-02 Package Datasheet (Vapour Recovery Unit 4-25)

> Normative requirements derived from the West Doe 04-25 Deepcut DBM (DBM-Deepcut) for the PKG-047 Vapour Recovery Unit. Items not directly supported by accessible source are marked `TBD` or `ASSUMPTION`.

## Scope

### In scope

This datasheet specifies the EPC Integrator technical handoff data for the 04-25 Vapour Recovery Unit (PKG-047) consisting of two 100 % rotary-compressor trains used to recover hydrocarbon vapours from storage tanks and low-pressure process vapour sources and to discharge recovered vapour to the 04-25 Stabilizer Overheads Compressor (SOC) first-stage suction. The datasheet covers SOW-0253, SOW-0254, SOW-0255, SOW-0256.

The scope includes the VRU compressor packages, integral suction scrubbers, coolers, recycle and make-up gas controls, blowdown to LP flare, suction-header-to-flare bypass, primary mechanical-seal vent to LP flare, manual sweet-gas purge connections, and the individual VRU buildings with their associated utilities. [DBM-Deepcut §Vapour Recovery Unit]

### Out of scope

- Detailed engineering of items the DBM lists as TBC/TBD (e.g., final motor power selection, suction-scrubber capacity range, MAWP envelope for suction stages, bundle temperature control on coolers).
- Sales gas, NGL treating/dehydration, cryogenic, amine, and TEG packages, except where their vapour streams interface to the VRU.
- The 03-25 VRU (different facility); its discharge into the 04-25 SOC first-stage suction is recognized as a boundary condition only.

## Requirements

### REQ-VRU-001 — Sparing and arrangement
Two 100 % VRU trains shall be supplied, capable of lead-lag operation with the standby unit normally idle at design conditions. Each train shall be installed in an individual building with associated utilities. [DBM §VRU Configuration]

### REQ-VRU-002 — Compressor selection
Each train shall use a Ro-Flo 17S / 217M two-stage rotary compressor. [DBM §VRU Configuration]

### REQ-VRU-003 — Capacity control
Capacity control shall be by variable-speed driver plus an automated recycle valve from second-stage discharge to first-stage suction. The recycle valve shall be sized for 100 % flow at minimum driver speed and lowest operating discharge pressure. [DBM §VRU Configuration; §VRU Scrubbing…]

### REQ-VRU-004 — Design point
Each train shall be sized for 1.5 MMSCFD / 42 e3m3/d (TBC), with suction at 0.9 kPag (2 oz/in²) and discharge at 483 kPag (70 psig). [DBM §VRU Configuration]

### REQ-VRU-005 — Driver
Driver shall be 4,000 V, 3-phase, with speed range 310–760 rpm (TBC) and 3:1 turndown on inverter duty. Motor power is **TBD**; the source lists both 200 hp (TBC) and 300 hp — a CONFLICT requiring human ruling (see `Guidance.md` Conflict Table). [DBM §VRU Configuration]

### REQ-VRU-006 — Sealing and seal vent
The compressor shall be fitted with a dual mechanical pressurized barrier seal with a barrier-fluid alarm; primary seal vent shall route to the LP flare. [DBM §VRU Configuration]

### REQ-VRU-007 — Suction scrubbers
Each compression stage shall be preceded by a two-phase suction scrubber sized to handle off-design operation including low compression ratio, high package capacity, high suction pressure, and low discharge pressure during initial start-up. Scrubbers shall use mist pads (not mesh/vane). Sizing shall use K-factor 0.25 maximum (Imperial) with de-rating for operating pressure. Inlet liquid SG shall be assumed ≥ 0.61 (ASSUMPTION; TBC). Final capacity range to be confirmed in detailed engineering. [DBM §VRU Scrubbing…]

### REQ-VRU-008 — Cooling and condensation control
Each cooler shall include manual warm-air recirculation louvers as the base design. Automatic warm-air recirculation shall be evaluated to reduce hydrocarbon-condensation risk arising from the heavy VRU composition. No bundle temperature control is included. The first-stage intercooler shall be designed to handle condensation, since the stated first-stage cooler-discharge temperature (48.9 °C) is below the stated dewpoint (52.7 °C). [DBM §VRU Scrubbing…]

### REQ-VRU-009 — Make-up / blanket gas
A make-up / blanket gas regulator shall maintain minimum suction pressure at maximum turndown using low-pressure fuel gas. The make-up setpoint shall align with the 2 oz inlet-pressure action. [DBM §VRU Scrubbing…; §VRU action table]

### REQ-VRU-010 — Pressure-action sequencing
Controls shall implement the VRU inlet-pressure action table (1 oz shutdown; 2 oz make-up setpoint and design suction; 2.5 oz shut down second VRU if running; 3 oz VRU control setpoint; 5 oz start second VRU; 8 oz open suction valve/regulator to flare; 16 oz thief-hatch setpoint). [DBM §VRU Configuration]

### REQ-VRU-011 — Blowdown
Each VRU package shall be provided with a blowdown valve routing blowdown gas to the LP flare under compressor-unit control-panel control. [DBM §VRU Scrubbing…]

### REQ-VRU-012 — Suction-header bypass to flare
A V-ball control valve shall bypass the VRU suction header directly to the LP flare when VRU trains are not operational, controlling on VRU suction pressure. A check valve on the discharge of this control valve shall prevent backflow to tanks, with less than 0.25 psid pressure drop at design conditions. The valve shall be located in the pipe rack; the header shall free-drain (no traps/pockets) sloping toward the LP flare knock-out. Header capacity shall at minimum handle the maximum VRU flow condition (final capacity TBC). Pressure measurement shall include both first-stage suction pressure and tank-farm VRU header pressure so VRU and flare PCV controls maintain tank vapour-space pressure despite suction-header pressure drop. Piping fittings and length shall be minimized. [DBM §VRU Scrubbing…]

### REQ-VRU-013 — MAWP envelope
The package shall meet the stated discharge MAWPs (first-stage discharge ≥ 552 kPag; second-stage discharge ≥ 1,034 kPag). Suction-side MAWPs are TBC and shall be confirmed in detailed engineering. [DBM §VRU Configuration]

### REQ-VRU-014 — Sour service
The package shall be designed for sour service consistent with the stated inlet composition (H2S 0.3557 mol%, mercaptans, DiM-sulphide, CS2, M-E sulphide). Specific material/inspection requirements (NACE MR0175/ISO 15156 application) — **location TBD** (not in extracted source slices). [DBM §VRU Inlet Composition; ASSUMPTION on NACE applicability]

### REQ-VRU-015 — Maintenance purge
A manual sweet-gas purge connection shall be provided at first-stage suction immediately downstream of the inlet manual isolation valve. [DBM §VRU Scrubbing…]

### REQ-VRU-016 — Interfaces
The package shall provide the interfaces enumerated in `Datasheet.md` §Construction → Interfaces, including discharge to 04-25 SOC first-stage suction, receipt of TEG still overheads (~<0.5 psig backpressure), receipt of reciprocating-compressor packing-vent recovery streams from SOC / sales / booster / acid-gas trains, and the tank-vapour collection set (excluding fresh-caustic tank). [DBM §SOC, §Booster, §Acid Gas, §TEG, §Caustic Storage, §Condensate Storage]

### REQ-VRU-017 — Building and utilities
Each VRU shall be housed in an individual building. Building HVAC/utility details are **TBC** in source. [DBM §VRU Configuration]

## Standards

| Standard / Code | Applicability | Location in source |
|---|---|---|
| OGAOM (Oil and Gas Above-ground Operations Manual), Sec. 9.6.15 | Spacing of fired heaters to vapour-release sources (informational; not a VRU package requirement) | DBM §Spacing table |
| API 2000 | Tank blanket-gas rates used for tanks connected to the VRU header | DBM §Condensate Storage |
| NACE MR0175 / ISO 15156 | Sour-service materials | `location TBD` — not in extracted source slices (ASSUMPTION: applicable based on H2S/mercaptan content) |
| API 11P / API 618 / ISO 13631 (rotary/reciprocating compressor packages) | Package design and testing | `location TBD` — not in extracted source slices (ASSUMPTION) |
| Local electrical code / hazardous-area classification | Electrical area classification of VRU building | `location TBD` |

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-VRU-001 | Vendor general arrangement drawings; building layout; functional spec showing lead-lag philosophy |
| REQ-VRU-002 | Vendor data sheet showing Ro-Flo 17S / 217M selection |
| REQ-VRU-003 | Compressor performance curves at min driver speed and lowest operating discharge pressure; recycle-valve sizing calculation |
| REQ-VRU-004 | Performance test at design point per vendor procedure; site capacity test |
| REQ-VRU-005 | Motor nameplate review against ruled motor power; VFD turndown test |
| REQ-VRU-006 | Seal arrangement drawing; barrier-fluid alarm function test |
| REQ-VRU-007 | Scrubber sizing calculation against K-factor and SG basis; mist-pad selection record |
| REQ-VRU-008 | Cooler heat-balance review at first-stage outlet; demonstration of condensation handling in suction scrubber |
| REQ-VRU-009 | Loop check on make-up regulator; setpoint verification at 2 oz |
| REQ-VRU-010 | Cause-and-effect / SAT showing each pressure action |
| REQ-VRU-011 | Blowdown valve stroke test; LP flare load reconciliation |
| REQ-VRU-012 | Suction-header bypass loop check; check-valve dP measurement at design; constructability walkdown for free-drain slope |
| REQ-VRU-013 | Hydrotest / PWHT records against stated MAWPs |
| REQ-VRU-014 | NACE material certificates and weld-procedure qualification — pending ruling on standard applicability |
| REQ-VRU-015 | Walkdown of purge connection at first-stage suction |
| REQ-VRU-016 | Interface tie-in punch list against `Datasheet.md` interface matrix |
| REQ-VRU-017 | Building/HVAC design submission once basis is confirmed |

## Documentation

Per `_CONTEXT.md` anticipated artifacts and decomposition row `DEL-047-02_package-datasheet`:

- Package technical datasheet (this `Datasheet.md`).
- Vendor engineering handoff basis (this Specification plus Guidance).
- Package interface requirements matrix (Datasheet → Construction → Interfaces).
- Source-supported equipment and design criteria (Attributes/Conditions tables; references).
- Conflict Table for items requiring human ruling (`Guidance.md`).
