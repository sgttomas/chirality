# Specification — DEL-069-02 Package Datasheet (Mole Sieve Drier Unit, Gas)

## Scope

This specification defines the EPC Integrator handoff requirements that the PKG-069 Mole Sieve Drier Unit (Gas) Package Datasheet must satisfy so that a Package Vendor can engineer, design, document, and deliver the package equipment, and so the EPC Integrator can complete facility-level integration.

**Included:**
- Process design conditions and adsorption/regeneration performance requirements for the process-gas mole-sieve unit downstream of TEG dehydration and upstream of mercury removal and cryogenic recovery.
- Equipment requirements for adsorber vessels, inlet filter/coalescers, regeneration gas compressor, regeneration heater, regeneration cooler, regeneration scrubber, mole-sieve dust filter, MRU and MRU dust filter, dry-out header, and recycle return path.
- Interface requirements (process, utilities, safety, structural) per `INTERFACE_REGISTER.csv` rows for PKG-069.
- Documentation/verification requirements for vendor handoff.

**Excluded:**
- NGL molecular-sieve dehydration (handled separately under the NGL mole-sieve scope per Gate-6 disposition; reference DBM-Deepcut SEC-07).
- TEG dehydration package upstream and UltraTEF cryogenic package downstream (interface only).
- Detailed-engineering deliverables that are out of scope of the Package Datasheet (covered by separate DEL-069-XX deliverables).

## Requirements

| Req ID | Requirement | Source / Status |
|---|---|---|
| R-PROC-01 | Provide final gas dehydration upstream of cryogenic recovery, delivering outlet water content sufficient to keep cryogenic-unit water dewpoint <-75 °C at the highest operating pressure. | DBM-Deepcut SEC-06 |
| R-PROC-02 | Design inlet capacity: 332.6 MMSCFD adsorption + 25.45 MMSCFD regeneration flow. | DBM-Deepcut SEC-06 |
| R-PROC-03 | Inlet design conditions: 1078 psig (TBC); summer 40.6 °C / winter 16 °C inlet temperature (TBC). | DBM-Deepcut SEC-06 |
| R-PROC-04 | Inlet water content: expected ≤4 lb H2O/MMSCF; design 10 lb H2O/MMSCF (at 333 MMSCFD). | DBM-Deepcut SEC-06 |
| R-PROC-05 | Outlet water content: expected <0.1 ppmv and dewpoint <-90 °C; maximum <1 ppmv and dewpoint -75 °C. Required outlet contractual value TBD. | DBM-Deepcut SEC-06 |
| R-PROC-06 | Adsorption turndown ratio ≥2:1; ASSUMPTION: vendor to confirm acceptable single-bed turndown floor to avoid channeling/premature breakthrough. | DBM-Deepcut SEC-06 |
| R-EQP-01 | Three (3) adsorber driers in 2-adsorption / 1-standby-regen-cool configuration, downflow adsorption. | DBM-Deepcut SEC-06 |
| R-EQP-02 | Adsorbent shall be 3A molecular sieve; 4A and 5A are not permitted. Include a silica-gel protective layer for upstream liquid carryover protection. | DBM-Deepcut SEC-06 |
| R-EQP-03 | Bed pressure drop: <4 psid start-of-life; <10 psid end-of-life including vessel nozzles. | DBM-Deepcut SEC-06 |
| R-EQP-04 | Adsorber flange rating shall meet the SEC-04 pressure basis requirement (900# flanges in the molecular-sieve system). | DBM-Deepcut SEC-04 (line 628) |
| R-EQP-05 | Inlet filter/coalescers: 2 × 100 % (1 operating, 1 standby); 328 MMSCFD HP dehydrated gas basis; clean ΔP <2 psid; blowdown valves per separator; liquids to slop tank header; assume no bulk free liquids at inlet. | DBM-Deepcut SEC-06 |
| R-EQP-06 | Regeneration gas compressor: single-stage vertical inline centrifugal, slipstream downstream of mole-sieve dust filter; 25 MMSCFD basis; 2 × 100 % installed standby; final capacity and design differential TBC; design differential 100 psid assumed (loop-table 79.5 psid). | DBM-Deepcut SEC-06 |
| R-EQP-07 | Regeneration gas heater: BEU heat-medium / process-gas shell-and-tube exchanger. Regeneration temperature basis: CONFLICT — 450 °F (system overview) vs 460 °F (heater detail). Vendor shall resolve before final design. | DBM-Deepcut SEC-06 (CONFLICT) |
| R-EQP-08 | Mole-sieve regeneration gas heating shall be served by a separate direct-fired heater; not connected to the unified heat-medium loop. | DBM-Deepcut SEC-09 |
| R-EQP-09 | Regeneration gas cooler: aerial cooler; cools to 110 °F at design conditions; maintain ≥15 °F above HC dewpoint and/or hydrate point; automated warm-air recirculation, intake louvers, split-header. | DBM-Deepcut SEC-06 |
| R-EQP-10 | Regeneration gas scrubber: two-phase with mist pad; gap-level water control to produced-water drain; peak regen water drain capacity TBC; installed inside building. | DBM-Deepcut SEC-06 |
| R-EQP-11 | Mole-sieve dust filter: 1 × 100 %; capacity = main + regen gas flow; 2 psid clean ΔP; manual bypass for online change-out. | DBM-Deepcut SEC-06 |
| R-EQP-12 | Mercury Recovery Unit (MRU): 1 × 100 % current with reserved space for one additional future MRU vessel; sulphur-impregnated activated carbon; media life ≥6 years; allowable inlet ~100 µgHg/Nm³; required outlet ≤0.01 µgHg/Nm³; EOL ΔP <6 psi. | DBM-Deepcut SEC-06 |
| R-EQP-13 | MRU dust filter: 1 × 100 %; 2 psid clean ΔP; manual bypass for online change-out. | DBM-Deepcut SEC-06 |
| R-EQP-14 | Recycle return: normal path returns saturated regen gas upstream of TEG inlet coalescer; provide a normally-closed alternate return upstream of mole-sieve coalescers. | DBM-Deepcut SEC-06 |
| R-EQP-15 | Dry-out header: provide low-pressure dry sales-gas recycle for cryogenic dry-out; ~250 psig initial operating pressure assumption; header MAWP and sales-compressor discharge pressure assumptions TBC. | DBM-Deepcut SEC-06 |
| R-CTRL-01 | Bring-online gas temperature shall not exceed 66 °C (downstream BAHX design temperature); exceedance shall trip the facility. | DBM-Deepcut SEC-06 |
| R-CTRL-02 | Blowdown shall be operator-initiated HMI only (no automatic blowdown with the rest of the facility); two blowdown valves provided (adsorption and regeneration loops); depressurization limited to 50 psi/min at maximum inlet pressure. | DBM-Deepcut SEC-06; §Process Controls |
| R-CTRL-03 | Regeneration compressor: automated blowdown on start; seals vented to flare with pressure monitoring; compressor bypass provided to prevent reverse rotation during blowdown. | DBM-Deepcut §Process Controls |
| R-IFC-01..12 | Implement and document all twelve interface types defined in `INTERFACE_REGISTER.csv` for PKG-069 (Process Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports). | `INTERFACE_REGISTER.csv` |
| R-CYC-01 | Cycle times (adsorption 54 h; heating ramps 0.2/0.4 h; preheat/hold 1 h; heating 3 h; cooling 3 h; standby ≥12 h, preliminary 38.8 h; total regen 7.6 h) carried as preliminary; vendor to confirm. Standby minimum 12 h per tower at 4 lb H2O loading is a hard floor. | DBM-Deepcut SEC-06 |
| R-LIFE-01 | Adsorbent life basis: typical 3 years (TBC by vendor); extension to 5 years to align with turnaround under review. | DBM-Deepcut SEC-06 |

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| ASME BPVC Section VIII | Adsorber vessels, MRU vessels, scrubber, exchangers (pressure containment) | ASSUMPTION — applicable per industry convention; clause-level requirements not in accessible sources; location TBD |
| ANSI B16.5 / B16.47 flange ratings (900# required by SEC-04) | Mole-sieve system flange rating | DBM-Deepcut SEC-04 line 628 |
| API 610 | Centrifugal pumps (if applicable to package scope) | ASSUMPTION — used elsewhere in DBM (NGL pumps); package-specific requirement TBD |
| API 661 (Air-cooled heat exchangers) | Regeneration gas aerial cooler | ASSUMPTION — industry standard for aerial coolers; location TBD |
| TEMA | Regeneration gas heater (BEU shell-and-tube) | ASSUMPTION — TEMA BEU class designation confirmed; clause-level TEMA reference TBD |
| Provincial/CRN (BC) | Pressure vessel registration | ASSUMPTION — DBM-Deepcut SEC-06 cites BC CRN for BAHX; vessel-level CRN requirement for mole-sieve TBD |
| Owner Engineering Standards | Owner-specific painting, insulation, EHT, labelling, F&G | TBD — list to be confirmed by EPC Integrator |

## Verification

| Verification Item | Approach | Source |
|---|---|---|
| Outlet water content performance | Vendor performance guarantee test; on-line moisture analyzer at unit outlet | DBM-Deepcut SEC-06 (outlet basis); SEC-08 (analyzers) |
| Bed pressure drop | Field ΔP measurement at SOL and EOL milestones; vendor design report | DBM-Deepcut SEC-06 |
| Adsorbent life | Vendor warranty + lab analysis of spent media at turnaround | DBM-Deepcut SEC-06 |
| Cycle time confirmation | Vendor regeneration simulation + commissioning HMI cycle log | DBM-Deepcut SEC-06 |
| Regeneration heater duty/temperature | Test-run heater outlet temperature against the resolved 450 °F vs 460 °F basis (see Guidance Conflict Table) | DBM-Deepcut SEC-06 |
| Cryogenic dewpoint protection | Continuous monitoring of bring-online gas temperature ≤66 °C; facility trip logic test | DBM-Deepcut SEC-06 |
| Blowdown rate | Witnessed depressurization ≤50 psi/min at max inlet pressure | DBM-Deepcut §Process Controls |
| MRU mercury performance | Inlet and outlet mercury sampling at startup and per turnaround | DBM-Deepcut SEC-06 |
| Interface completeness | Cross-check 12 interface types in `INTERFACE_REGISTER.csv` against vendor package boundary drawings | `INTERFACE_REGISTER.csv` |

## Documentation

| Artifact | Producer | Source |
|---|---|---|
| Package technical datasheet (this deliverable) | EPC Integrator | `_CONTEXT.md` Anticipated Artifacts |
| Vendor engineering handoff basis | EPC Integrator | `_CONTEXT.md` |
| Package interface requirements matrix (per 12 IFC rows) | EPC Integrator | `_CONTEXT.md`; `INTERFACE_REGISTER.csv` |
| Source-supported equipment and design criteria | EPC Integrator | `_CONTEXT.md` |
| Vendor-engineered equipment package | Package Vendor | `OBJECTIVE_DELIVERABLE_MAP.csv` (DEL-069-04) |
| Vendor document turnover package | Package Vendor | `OBJECTIVE_DELIVERABLE_MAP.csv` (DEL-069-05) |
| EPC vendor package review and acceptance | EPC Integrator | `OBJECTIVE_DELIVERABLE_MAP.csv` (DEL-069-06) |
