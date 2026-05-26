# Guidance — DEL-069-04 Vendor Engineered Equipment Package (Mole Sieve Drier Unit, Gas)

## Purpose

This deliverable is the Package Vendor's production unit for the PKG-069 "Mole Sieve Drier Unit (Gas)" — engineering, design, fabrication/supply, and physical equipment package — developed from the EPC Integrator's Scope of Work (DEL-069-01) and Package Datasheet (DEL-069-02). It supplies the process-gas final dehydration and mercury-protection equipment that conditions sweet, TEG-dehydrated gas to cryogenic service quality before the UltraTEF cryogenic unit. Source: `_CONTEXT.md`; 4-25 Deepcut DBM SEC-06.

## Principles

- **Cryogenic-protection priority.** The package exists primarily to protect the downstream BAHX and cryogenic recovery from water (hydrate/ice) and mercury (amalgamation). Outlet water-content limits and BAHX temperature protection are the dominant constraints, not regeneration efficiency. Source: SEC-06 / Design Values.
- **3A only.** Adsorbent chemistry is non-negotiable. Larger-pore sieves (4A/5A) co-adsorb H2S, contaminating the regeneration return loop. Source: SEC-06 / Bed and Regeneration Basis.
- **Three-bed lead/lag/regen.** Two adsorbing, one in standby/regen/cooling. Sparing decisions outside this triplet (e.g., spare bed for 5-year life) require explicit life-cycle justification. Source: SEC-06.
- **Operator-initiated blowdown.** This unit deliberately is *not* part of automatic facility blowdown; operator HMI control is required. Source: SEC-06 / Equipment, Controls, and Protection.
- **Inlet filter/coalescer is the first defense.** TEG carryover during upset is the foreseeable hazard the inlet coalescer must absorb. Source: SEC-06.
- **Integration is bidirectional.** Vendor engineering must respect upstream TEG-outlet conditions and the downstream BAHX 66 degC online-bed temperature ceiling, and the regeneration recycle path must reconcile with TEG inlet coalescer routing. Source: SEC-06.

## Considerations

- **Outlet specification is partially TBD.** Expected (<0.1 ppmv) and maximum (<1 ppmv) are stated, but the contractually required outlet value remains TBD. Vendor proposals should make the assumed contractual outlet value explicit and call out the cryogenic dewpoint constraint at the operating pressure. Source: SEC-06.
- **Inlet pressure and temperature carry TBC tags.** Normal inlet pressure 1078 psig and inlet temperature 40.6 degC summer / 16 degC winter are explicitly TBC. Vendor sizing margins should be transparent about which sizing case dominates (summer high-pressure water-loading vs. winter operating envelope). Source: SEC-06.
- **Regeneration cooler winter operation.** The aerial cooler must maintain >= 15 degF above HC dewpoint / hydrate point; recirculation louvers exist precisely for cold-weather cases. Vendor design should not silently disable recirculation logic. Source: SEC-06.
- **Adsorbent life vs. turnaround alignment.** The 3-year vendor-typical life vs. 5-year turnaround alignment is a deliberate open trade-off; vendor input on whether 5 years is achievable with the proposed bed sizing, cycle, and inlet loading is requested. Source: SEC-06.
- **Mercury removal life and reserve space.** 6-year MRU media life is a guaranteed minimum; reserved space for one additional future MRU vessel implies vendor layout must not occupy that reserve. Source: SEC-06.
- **Turndown.** 2:1 on the adsorption side is the documented envelope; single-bed adsorption extends turndown but at channeling/early-breakthrough risk. Vendor should specify the minimum stable flow per bed. Source: SEC-06.

## Trade-offs

| Trade-off | Direction | Rationale (source) |
|---|---|---|
| Cycle time vs. bed life | Longer adsorption cycle reduces thermal stress on adsorbent but increases bed inventory and risk of breakthrough on upset; preliminary 54 h adsorption is a balance | SEC-06 |
| Adsorbent life vs. CAPEX | 5-year life may require larger or extra bed (CAPEX) but reduces turnaround pressure | SEC-06 |
| Regen heater set-point | Higher temperature (460 degF detail) gives faster, more complete regen; lower (450 degF overview) reduces thermal cycling — basis is currently unresolved | SEC-06; Conflict C-1 |
| Operator-only blowdown vs. plant ESD integration | Operator-only protects adsorbent from thermal-shock fragmentation; trade-off is slower depressuring in true emergencies | SEC-06 |
| Recycle return path | Normal return upstream of TEG coalescer protects mole-sieve coalescer from saturated regen gas; NC alternate exists for special ops | SEC-06 |

## Examples

- **BAHX protection trip.** During first-bed-online sequence after regen, if outlet gas to BAHX trends toward 66 degC, the C&E must trip — this is a documented facility-shutdown event, not a vendor warning condition. Source: SEC-06.
- **Upset TEG carryover.** During TEG flooding, the inlet filter/coalescer level reaches HLL; gravity-dump to slop tank header maintains drier inlet quality. Source: SEC-06.
- **Single-bed turndown.** At extreme low flow, the unit may operate with one bed in adsorption. Vendor should advise the minimum stable single-bed flow. Source: SEC-06 / Design Values; turndown note.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| C-1 | Regeneration gas heater design temperature | 4-25 Deepcut DBM SEC-06 — "Regeneration gas heater ... 450 degF system overview" | 4-25 Deepcut DBM SEC-06 — "...460 degF heater detail" | Specification R-9; Datasheet (Regeneration gas heater); Procedure regeneration step | PROPOSAL: vendor design to 460 degF (heater-level detail), with operating set-point default 450 degF; reconcile in vendor package design basis | TBD |
| C-2 | Regeneration gas compressor design differential | 4-25 Deepcut DBM SEC-06 — "assumed design differential 100 psid" | 4-25 Deepcut DBM SEC-06 — "detailed equipment-loop table totals 79.5 psid" | Specification R-9; Datasheet (Regen gas compressor) | PROPOSAL: design 100 psid; rate per loop-table 79.5 psid; vendor to confirm with final tie-in pressures | TBD |
| C-3 | Required outlet water content (contractual value) | 4-25 Deepcut DBM SEC-06 — expected < 0.1 ppmv, max < 1 ppmv | (no source specifies contractual value) | Specification R-3; Datasheet (Outlet water content); Procedure verification | PROPOSAL: contract value 1 ppmv H2O max, with expected operating value < 0.1 ppmv | TBD |
| C-4 | Objective association (OBJ-001, 003-010) for DEL-069-04 | `_CONTEXT.md` Supports Objectives list | GATE-07 OBJECTIVE_DELIVERABLE_MAP.csv — not individually re-verified at deliverable-ID level | All four docs (context) | PROPOSAL: retain decomposition list as ASSUMPTION under PACKAGE_HEURISTIC | TBD |
