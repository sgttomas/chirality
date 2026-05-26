# Guidance — DEL-047-02 Package Datasheet (Vapour Recovery Unit 4-25)

> Directional rationale, design considerations, and trade-offs for the PKG-047 VRU package datasheet. Source-grounded against the West Doe 04-25 Deepcut DBM (DBM-Deepcut). Items beyond source are marked `TBD` or `ASSUMPTION`.

## Purpose

The Package Datasheet exists so that a third-party vendor (or sister discipline) can engineer and supply the 04-25 VRU to the EPC Integrator’s basis without negotiating fundamental scope. It carries (a) the equipment selection and design point, (b) the inlet-pressure action philosophy that governs the safety/flare interface, and (c) the interface matrix that links the VRU to upstream tanks and reciprocating-compressor packing-vent recovery and to downstream SOC first-stage suction. Decomposition explicitly directs that interface facts are carried here as evidence rather than as standalone deliverables (`_CONTEXT.md` Notes).

## Principles

- **Two 100 % trains, lead-lag.** Recovery duty must continue while one train is unavailable, because alternative routings open atmospheric venting paths (thief hatches, PVRVs) and the bypass-to-flare path consumes flare capacity. [DBM §VRU Configuration]
- **Pressure-led control, not flow-led.** The 1/2/2.5/3/5/8/16 oz action table sequences VRU start, make-up, second-train start, flare bypass, and finally thief-hatch relief. Suction pressure is the master variable. [DBM §VRU Configuration]
- **Recover wherever practical; flare only when necessary.** The suction-header-to-flare V-ball valve exists to keep tank pressures intact when VRUs are offline, not as a routine relief path. Its check valve (<0.25 psid at design) and pipe-rack location follow from this principle. [DBM §VRU Scrubbing…]
- **Recompress packing-vent recovery streams.** SOC, sales, booster, and acid-gas reciprocating compressors collect packing-drain/vent vapours to a common seal pot and route the vapour to the VRU suction header. This protects the wet-seal environment without venting sour gas. [DBM §SOC, §Booster, §Acid Gas]

## Considerations

- **Heavy composition / condensation risk.** Summer VRU inlet contains 4.3 % iC4, 2.7 % iC5, plus C6–C8 traces. First-stage cooler discharge (48.9 °C) is below dewpoint (52.7 °C), so condensation is expected at the first-stage intercooler outlet. Scrubber sizing and cooler controls must account for this; manual warm-air recirculation is the base design with automatic recirculation flagged for evaluation. [DBM §VRU Scrubbing…]
- **Sour service.** H2S (0.3557 mol%), mercaptans, CS2 and sulphides are present; package must be designed accordingly. Specific NACE basis is `location TBD` in the extracted source set. [DBM §VRU Inlet Composition]
- **Combined 04-25 / 03-25 discharge to 04-25 SOC.** Both VRUs land on the 04-25 SOC first-stage suction, so SOC suction-side hydraulics and unavailability of the SOC affect the VRU operating envelope. [DBM §VRU; §SOC Interfaces]
- **TEG still overheads and stripping-gas mixing.** TEG regeneration still emissions are recovered to the VRU suction header at ≈<0.5 psig backpressure; BTEX is mixed with stripping gas and recompressed to plant inlet. The VRU recycle path therefore returns BTEX-bearing vapour to the gas processing train. [DBM §TEG dehydration]
- **No bundle temperature control on coolers.** Selecting automatic warm-air recirculation is the lever available to suppress condensation if the manual base design proves marginal. [DBM §VRU Scrubbing…]
- **Make-up gas comes from LP fuel gas.** The blanket-pressure setpoint at 2 oz draws LP fuel gas into the VRU envelope under low-source conditions; gas-balance work in detailed engineering must account for this. [DBM §VRU Configuration; §VRU action table]

## Trade-offs

| Decision point | Option A | Option B | Source-stated direction |
|---|---|---|---|
| Cooler control | Manual warm-air recirculation louvers (base) | Automatic warm-air recirculation | Base design A; evaluate B to reduce condensation risk (TBC) [DBM §VRU Scrubbing…] |
| Compressor motor | 200 hp (TBC) | 300 hp | CONFLICT — DBM lists both values (see Conflict Table) |
| Suction-header bypass routing | V-ball to LP flare via pipe rack with check valve | Direct tank PVRVs / thief hatches | A is selected; B is acceptance-of-loss only (16 oz thief setpoint) [DBM §VRU Scrubbing…; §VRU action table] |
| Sour-service material standard | NACE MR0175 (ASSUMPTION) | Other / vendor-default | Direction not in extracted source slices; needs explicit specification ruling |
| Building HVAC | Per vendor standard | Specified by EPC | TBC in source [DBM §VRU Configuration] |

## Examples

Two illustrative source-grounded scenarios:

1. **Steady-state, summer, both trains available.** Lead VRU operates near the expected-summer stage flows (Stage 1 0.5794 MMSCFD; Stage 2 0.5638 MMSCFD). Suction pressure held at 3 oz control setpoint; LP fuel gas make-up active intermittently to defend the 2 oz floor. First-stage intercooler condensate is captured by the suction scrubber. Discharge enters 04-25 SOC first-stage suction together with the 03-25 VRU contribution.
2. **Lead unit trips during winter.** Suction pressure rises through 5 oz, second train auto-starts and ramps. If the second train cannot recover within the available pressure margin, at 8 oz the suction-header V-ball opens to the LP flare via the pipe-rack header. Tank-farm pressure measurement plus first-stage suction measurement keep tank vapour-space pressure inside the thief-hatch (16 oz) envelope. [DBM §VRU Configuration; §VRU Scrubbing…]

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-VRU-01 | Compressor motor power — "200 hp TBC" vs "300 hp" both stated for the same compressor | DBM-Deepcut §VRU Configuration and Design Parameters (line listing motor power) | DBM-Deepcut §VRU Configuration and Design Parameters (same line) | `Datasheet.md` Attributes → Compressor and Driver; `Specification.md` REQ-VRU-005; vendor procurement | Hold at TBD until ruling; vendor to size against design point (1.5 MMSCFD, 483 kPag discharge, 0.9 kPag suction) and confirm motor rating | TBD |
| CONF-VRU-02 | VRU Stage 1/Stage 2 design capacity stated as "1.5 MMSCFD (TBC)" without firm confirmation | DBM-Deepcut §VRU Configuration | DBM-Deepcut §VRU inlet capacity table (Stage 1 design 1.5 TBC; Stage 2 design 1.5 TBC) | `Datasheet.md` Capacity table; `Specification.md` REQ-VRU-004 | Carry 1.5 MMSCFD as design pending confirmation; vendor to flag any deviation | TBD |
| CONF-VRU-03 | Inlet-source flow table is preliminary ("to be reviewed during detailed engineering") yet drives total VRU capacity adequacy | DBM-Deepcut §VRU Configuration (gas-source table) | Same table footnote | `Datasheet.md` Inlet Source Inventory | Treat table as best-available baseline; revisit at FEED close-out | TBD |
| CONF-VRU-04 | Sour-service material/inspection standard not explicitly named in extracted source slice despite H2S/mercaptan content | DBM-Deepcut §VRU Inlet Composition (composition only) | (no explicit NACE clause located in extracted slices) | `Specification.md` REQ-VRU-014; Standards table | Apply NACE MR0175/ISO 15156 as ASSUMPTION pending explicit specification ruling | TBD |
| CONF-VRU-05 | Suction-stage MAWPs and design temperatures listed as TBC | DBM-Deepcut §VRU Configuration | Same | `Datasheet.md` MAWP table; `Specification.md` REQ-VRU-013 | Vendor to propose values against compressor settle-out / blocked-discharge cases | TBD |
| CONF-VRU-06 | 26020-Package_Requirements.docx (binary) not extracted, so any package-requirement clauses unique to it are not reflected in this datasheet | `_REFERENCES.md` (lists docx) | (binary not parsed) | All sections that should cite package-requirement clauses | Extract docx via `tools/pdf2md` equivalent or vendor-provided text; rerun four-documents | TBD |
