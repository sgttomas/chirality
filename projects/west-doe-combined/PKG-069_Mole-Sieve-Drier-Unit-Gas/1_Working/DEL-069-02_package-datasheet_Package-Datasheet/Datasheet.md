# Datasheet — DEL-069-02 Package Datasheet (Mole Sieve Drier Unit, Gas)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-069-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable Name | Package Datasheet | `_CONTEXT.md` |
| Parent Package ID | `PKG-069` | `_CONTEXT.md` |
| Package Name | Mole Sieve Drier Unit (Gas) | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-069 |
| Workbook Row | 73 | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| Deliverable Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` (EPC Integrator owns facility-level integration; Package Vendor owns package engineering/design/equipment) |
| Covers Scope Item | `SOW-0144` | `_CONTEXT.md` |
| Supports Objectives | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md`; `OBJECTIVE_DELIVERABLE_MAP.csv` (ASSUMPTION: package-grouped via `OBJECTIVE_ASSOCIATION_MODE = PACKAGE_HEURISTIC`) |
| Gate-6 Disposition Note | Gas Mole Sieve scope is included with the Cryogenic Unit package scope; NGL Mole Sieve remains a distinct package. | `PACKAGE_REGISTER.csv` Notes column |

## Attributes (Package Function)

| Attribute | Value | Source |
|---|---|---|
| Process role | Final dehydration of high-pressure sour gas upstream of cryogenic recovery | DBM-Deepcut `4-25_Deepcut_DBM.md` SEC-06 Molecular-Sieve Dehydration and Mercury Removal Basis |
| Adsorbent | 3A molecular sieve (mandatory); 4A/5A not permitted (adsorb H2S → sulphur spikes in regeneration loop) | DBM-Deepcut SEC-06 §Molecular-Sieve Bed and Regeneration Basis |
| Protective media | Silica gel layer for upstream liquid carryover protection | DBM-Deepcut SEC-06 §Molecular-Sieve Bed and Regeneration Basis |
| Configuration | Three adsorber towers: 2 in adsorption, 1 in standby/regeneration/cooling | DBM-Deepcut SEC-06 |
| Flow direction | Downflow through adsorption beds | DBM-Deepcut SEC-06 |
| Location | Outdoor multilevel module adjacent to cryogenic modules; inlet filter coalescers on a separate module/building | DBM-Deepcut SEC-06 §Molecular-Sieve Design Values |

## Conditions (Process Design Values)

| Parameter | Value | Source / Status |
|---|---|---|
| Inlet capacity (total) | 332.6 MMSCFD adsorption + 25.45 MMSCFD regeneration | DBM-Deepcut SEC-06 |
| Per-bed adsorption flow | Bed 1 / Bed 2: 166.3 MMSCFD each | DBM-Deepcut SEC-06 |
| Per-bed regeneration flow | Bed 3: 25.45 MMSCFD | DBM-Deepcut SEC-06 |
| Normal inlet pressure | 1078 psig (TBC during detailed engineering) | DBM-Deepcut SEC-06 |
| Inlet temperature (summer) | 40.6 °C (105 °F), subject to final inlet temperature estimates | DBM-Deepcut SEC-06 |
| Inlet temperature (winter) | 16 °C (61 °F), subject to final inlet temperature estimates | DBM-Deepcut SEC-06 |
| Inlet water content (expected) | ≤4 lb H2O/MMSCF at 333 MMSCFD | DBM-Deepcut SEC-06 |
| Inlet water content (design) | 10 lb H2O/MMSCF at 333 MMSCFD | DBM-Deepcut SEC-06 |
| Outlet water content (expected) | <0.1 ppmv H2O; dewpoint <-90 °C | DBM-Deepcut SEC-06 |
| Outlet water content (maximum) | <1 ppmv H2O; dewpoint -75 °C | DBM-Deepcut SEC-06 |
| Required outlet value | TBD | DBM-Deepcut SEC-06 |
| Cryogenic dewpoint limit | <-75 °C at highest operating pressure (downstream cryogenic protection) | DBM-Deepcut SEC-06 |
| Adsorption turndown | 2:1 (further turndown by single-bed adsorption; excessive turndown risks channeling and premature breakthrough) | DBM-Deepcut SEC-06 |
| Adsorbent life (typical) | 3 years (TBC by vendor); 5-year alignment with turnaround under review | DBM-Deepcut SEC-06 |
| BAHX temperature protection | New-bed bring-online gas temperature must not exceed 66 °C (downstream BAHX design temperature); exceedance trips facility | DBM-Deepcut SEC-06 |

## Cycle and Bed Sizing

| Item | Value | Source / Status |
|---|---|---|
| Adsorption time | 54 h (preliminary) | DBM-Deepcut SEC-06 |
| Heating ramp | 0.2 h (preliminary) | DBM-Deepcut SEC-06 |
| Regeneration preheat/hold | 1 h (preliminary) | DBM-Deepcut SEC-06 |
| Heating ramp (2) | 0.4 h (preliminary) | DBM-Deepcut SEC-06 |
| Heating | 3 h (preliminary) | DBM-Deepcut SEC-06 |
| Cooling | 3 h (preliminary) | DBM-Deepcut SEC-06 |
| Standby | 38.8 h (preliminary); minimum 12 h per tower at 4 lb H2O loading | DBM-Deepcut SEC-06 |
| Total regeneration cycle | 7.6 h (preliminary) | DBM-Deepcut SEC-06 |
| Adsorber bed ID | 9.5 ft (basis) | DBM-Deepcut SEC-06 |
| Regeneration tower size (vertical) | 8 ft × 20 ft | DBM-Deepcut SEC-06 |
| Regeneration thermal efficiency target | <40 % | DBM-Deepcut SEC-06 |
| Bed pressure drop, start-of-life | <4 psid | DBM-Deepcut SEC-06 |
| Bed pressure drop, end-of-life (incl. nozzles) | <10 psid | DBM-Deepcut SEC-06 |

## Construction (Equipment, Controls, Protection)

| Equipment / Function | Basis | Source |
|---|---|---|
| Inlet filter/coalescers | 2 × 100 % (1 operating, 1 standby); 328 MMSCFD HP dehydrated gas basis; assume no bulk free liquids; TEG carryover possible during upset; clean ΔP <2 psid; blowdown valves on each separator; liquids dumped to slop tank header | DBM-Deepcut SEC-06 |
| Adsorber vessels | 3 driers (2 adsorption / 1 standby-regen-cool); flange rating 900# (per SEC-04 process-gas mole sieve flange basis) | DBM-Deepcut SEC-06; SEC-04 pressure basis |
| Regeneration gas compressor | Single-stage vertical inline centrifugal slipstream downstream of mole-sieve dust filter; 25 MMSCFD basis; 2 × 100 % with installed standby; final capacity TBC; assumed design ΔP 100 psid (loop-table totals 79.5 psid) | DBM-Deepcut SEC-06 |
| Regeneration gas heater | BEU heat-medium / process-gas shell-and-tube exchanger; regeneration temperature basis unresolved (450 °F system overview vs 460 °F heater detail) — CONFLICT, see Guidance | DBM-Deepcut SEC-06 |
| Regeneration gas cooler | Aerial cooler; cools to 110 °F at design while maintaining ≥15 °F above HC dewpoint and/or hydrate point; automated warm-air recirculation, intake louvers, split-header | DBM-Deepcut SEC-06 |
| Regeneration gas scrubber | Two-phase with mist pad; separated water gap-level controlled to produced-water drain; peak regen water drain capacity TBC; installed inside building | DBM-Deepcut SEC-06 |
| Recycle return | Normally upstream of TEG inlet coalescer; normally-closed alternate path upstream of mole-sieve coalescers | DBM-Deepcut SEC-06 |
| Blowdown | Operator-initiated HMI only; no auto-blowdown with rest of facility; 2 blowdown valves (adsorption and regen loops); 50 psi/min depressurization limit at maximum inlet pressure; regen compressor bypass prevents reverse rotation | DBM-Deepcut SEC-06; §Process Controls and Protective Functions |
| Dry-out header | Low-pressure dry sales-gas recycle for cryogenic dry-out; ~250 psig initial operating pressure assumption; header MAWP and sales-compressor discharge pressure assumptions TBC | DBM-Deepcut SEC-06 |
| Mole-sieve dust filter | 1 × 100 %; capacity = main gas + regen gas flow; 2 psid clean ΔP; manual bypass for online change-out | DBM-Deepcut SEC-06 |
| Mercury Recovery Unit (MRU) | 1 × 100 % current; reserved space for one future additional MRU vessel; sulphur-impregnated activated carbon; media life ≥6 years; inlet ≤~100 µgHg/Nm³; outlet ≤0.01 µgHg/Nm³; EOL ΔP <6 psi | DBM-Deepcut SEC-06 |
| MRU dust filter | 1 × 100 %; 2 psid clean ΔP; manual bypass | DBM-Deepcut SEC-06 |
| Heat medium / regen gas heating | Mole-sieve regeneration gas heating removed from heat medium loop; served by a separate direct-fired heater | DBM-Deepcut SEC-09 (Heat Medium) |

## Package Interfaces (workbook-defined)

| Interface Type | Applicable | Source |
|---|---|---|
| Process Piping | YES | `INTERFACE_REGISTER.csv` IFC-8863228D03 |
| Relief / Flare / Vent | YES | IFC-DB1A71F6DF |
| Drain / Containment | YES | IFC-9479DAC2A5 |
| Electrical Power | YES | IFC-1D3E18B0BE |
| EHT (Electric Heat Trace) | YES | IFC-BA6F4E6AB5 |
| Grounding / Bonding | YES | IFC-8AEB17AA5C |
| Area / Exterior Lighting | YES | IFC-F72C2E190F |
| I&C / Control Cabling | YES | IFC-14518427AC |
| Building HVAC / Services | YES | IFC-DA19470A67 |
| Fire & Gas / Safety Systems | YES | IFC-C2918ADF74 |
| Maintenance Access | YES | IFC-0F979B5E62 |
| Structural / Foundations / Supports | YES | IFC-0B1DEDEC2D |

## Process Interfaces (functional)

| Interface | Basis | Source |
|---|---|---|
| Upstream — TEG dehydration (process-gas) | Receives HP dehydrated gas from TEG contactor outlet via TEG/inlet cross-exchanger | DBM-Deepcut SEC-06 |
| Downstream — Mercury Recovery Unit / BAHX inlet | Dried gas → mole-sieve dust filter → MRU → MRU dust filter → UltraTEF cryogenic unit | DBM-Deepcut SEC-06 |
| Regeneration gas loop (recycle return) | Saturated regen gas to upstream TEG inlet coalescer (normal); alternate to mole-sieve coalescers | DBM-Deepcut SEC-06 |
| Produced-water / drain | Coalescer liquids to slop tank header; regen scrubber water to produced water | DBM-Deepcut SEC-06 |
| HP flare | Blowdown routing per §Process Controls and Protective Functions | DBM-Deepcut SEC-06 |
| Heat medium | Mole-sieve regen heater is a separate direct-fired heater (removed from unified heat medium loop) | DBM-Deepcut SEC-09 |
| Fuel gas | LP fuel gas blanket / purge to applicable vessels (general utility) | DBM-Deepcut SEC-08 (general fuel-gas basis) |

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — SEC-06 Molecular-Sieve Dehydration and Mercury Removal Basis (lines 1239–1291); §Process Controls and Protective Functions; §Interfaces; §Assumptions/TBDs.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` — PKG-069 row.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv` — PKG-069 interface rows.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_DELIVERABLE_MAP.csv` — package-grouped objective mappings (ASSUMPTION; PACKAGE_HEURISTIC).
- Deliverable-local: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`.

## Open Items / TBDs (carried)

- Normal inlet pressure 1078 psig — TBC during detailed engineering. (SEC-06)
- Final inlet temperatures (summer/winter) — TBC. (SEC-06)
- Required outlet water content value — TBD. (SEC-06)
- Cycle times (adsorption/heating/cooling/standby) — preliminary. (SEC-06)
- Adsorbent life (3 yr typical; 5 yr alignment) — TBC by vendor. (SEC-06)
- Regeneration gas compressor final capacity and design differential — TBC. (SEC-06)
- Regeneration heater temperature basis — CONFLICT (450 °F vs 460 °F) — see Guidance Conflict Table. (SEC-06)
- Regeneration gas scrubber peak drain sizing — TBC. (SEC-06)
- Dry-out header operating pressure (~250 psig assumed); MAWP and sales-compressor discharge basis — TBC. (SEC-06)
- Gate-6 disposition note: "Gas Mole Sieve scope is included with the Cryogenic Unit package scope" — package-boundary clarification needed for vendor-package contracting. ASSUMPTION: this datasheet remains the EPC handoff basis for the Mole Sieve scope element even if commercially packaged with the Cryogenic Unit. (PACKAGE_REGISTER.csv Notes)
