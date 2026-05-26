# Guidance — DEL-069-02 Package Datasheet (Mole Sieve Drier Unit, Gas)

## Purpose

The Package Datasheet is the EPC Integrator's mandatory technical handoff to a Package Vendor (or to discipline engineering) for the PKG-069 Mole Sieve Drier Unit (Gas). It carries the source-supported design conditions, equipment basis, interfaces, and open items needed for downstream vendor engineering, while preserving the integrator's authority on facility-level integration. It also functions as a Gate 5 anchor that aggregates interface facts that would otherwise be scattered across separate deliverables.

## Principles

- **Source-anchored.** All design conditions and equipment-basis claims trace to the DBM-Deepcut (`4-25_Deepcut_DBM.md`) or to authoritative registers in the GATE-07 snapshot. Values without source support are carried as `TBD` or labelled `ASSUMPTION`, never invented.
- **Integration boundary preserved.** EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration; Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. (Source: `PACKAGE_REGISTER.csv` PKG-069.)
- **Interface coverage is exhaustive.** All twelve interface types in `INTERFACE_REGISTER.csv` for PKG-069 are carried forward; none is silently dropped.
- **Conflicts surfaced, not reconciled.** Where the DBM presents two values (e.g., regeneration heater temperature 450 °F vs 460 °F), the datasheet preserves both and flags a Conflict Table entry for human ruling.

## Considerations

- **Gate-6 disposition.** The PACKAGE_REGISTER notes record: "Gas Mole Sieve scope is included with the Cryogenic Unit package scope; NGL Mole Sieve remains a distinct package." This is a commercial/contract-packaging observation, not a process-scope merger. The Mole Sieve Drier Unit (Gas) remains a distinguishable functional unit with its own design basis and interfaces, regardless of how vendor packaging is awarded. The EPC Integrator should treat this datasheet as the technical basis for the gas mole-sieve scope element even if it is procured under a combined Cryogenic Unit contract.
- **Process placement.** The unit sits between TEG dehydration (upstream) and MRU/cryogenic recovery (downstream). It is *final* dehydration; downstream cryogenic dewpoint protection (<-75 °C) drives the outlet-water requirement.
- **Three-tower 2+1 configuration with no installed spare on adsorption side** is conservative given that single-bed adsorption is permitted only as a turndown case. The standby slot also covers regeneration and cooling, so true redundancy depends on cycle scheduling — vendor must demonstrate the cycle time table closes without violating the 12 h minimum standby per tower.
- **3A adsorbent is mandatory.** This is non-negotiable because 4A/5A adsorb H2S and produce sulphur spikes in the regeneration loop that would contaminate the recycle return path back into upstream gas. Vendors proposing alternative adsorbents must demonstrate equivalent sulphur exclusion.
- **Regeneration gas heating is OFF the unified heat-medium loop.** A separate direct-fired heater is required (SEC-09 change-of-basis). This is a recent design-basis change that vendors familiar with prior project versions must be alerted to.
- **Blowdown is manual.** The unit deliberately does not auto-blow down with the rest of the facility; this protects the adsorbent and the regeneration compressor. Vendor SIS/F&G logic must respect this constraint.

## Trade-offs

- **Adsorbent life vs turnaround alignment.** Typical 3-year media life is the cited base; extension to 5 years (turnaround alignment) is under review. Selecting 5-year basis adds adsorbent volume / bed sizing margin and may require an installed spare bed.
- **Single-bed adsorption (extreme turndown) vs channeling risk.** Turndown ratio of 2:1 is supported on the adsorption side; further turndown by single-bed adsorption is allowed but may cause channeling and premature breakthrough. Operations should treat single-bed mode as a transient operating point, not a sustained mode.
- **Regeneration gas recycle return path.** Normal return is upstream of the TEG inlet coalescer (re-uses TEG to handle desorbed water vapor remaining in saturated regen gas). The alternate return upstream of mole-sieve coalescers exists for contingency; sustained use would load the mole-sieve coalescers and bypass TEG conditioning.
- **MRU sparing.** Single 1 × 100 % MRU vessel is the current basis, with reserved space for a future second vessel. Single-vessel operation means MRU media change-out is a planned outage event aligned with turnaround.

## Examples

- **Cycle scheduling worked example (preliminary, per DBM):** With 54 h adsorption per bed and a 7.6 h total regeneration cycle, two beds in adsorption deliver continuous flow while the third sequences through preheat (1 h) → heating ramp (0.2 h) → heating (3 h) → cooling (3 h) → standby (≥12 h, preliminary 38.8 h). Vendor must close the cycle so the next-due regeneration starts before breakthrough.
- **Bring-online example:** When a freshly regenerated bed is placed in service, gas temperature into the downstream BAHX must not exceed 66 °C; the control system must hold the new bed in cooling/standby until thermal sweep confirms compliance. The facility trip on exceedance is the protective barrier.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-069-02-01 | Regeneration heater temperature basis: 450 °F vs 460 °F | DBM-Deepcut `4-25_Deepcut_DBM.md` SEC-06 system overview text (e.g., line 1617 vicinity for NGL mole sieve regen at 460 °F; gas mole-sieve uses 450 °F in narrative vs 460 °F in equipment detail row) | DBM-Deepcut `4-25_Deepcut_DBM.md` SEC-06 §Molecular-Sieve Equipment, Controls, and Protection (regen gas heater row) | Datasheet (Construction → Regen gas heater), Specification R-EQP-07, Procedure (operate) | PROPOSAL: adopt the equipment-detail row (vendor-package interface value) pending vendor heater duty calculation; treat 450 °F as upper-system narrative and the equipment-row value as the contractual heater outlet target. | TBD |
| C-069-02-02 | Regeneration gas compressor design differential: 100 psid (assumed) vs 79.5 psid (equipment loop table total) | DBM-Deepcut SEC-06 §Molecular-Sieve Equipment, Controls, and Protection (regen gas compressor row) | DBM-Deepcut SEC-06 same row (loop-table sub-claim) | Datasheet (Construction → Regen gas compressor), Specification R-EQP-06 | PROPOSAL: vendor to size for assumed 100 psid with documented margin until detailed loop hydraulics are closed; loop-table value used as a minimum-of-record. | TBD |
| C-069-02-03 | Gate-6 packaging note vs decomposition row identity: PKG-069 Gas Mole Sieve "included with Cryogenic Unit package scope" while still listed as a discrete PKG-069 with its own DEL-069-01..06 set. | `PACKAGE_REGISTER.csv` PKG-069 Notes column | `OBJECTIVE_DELIVERABLE_MAP.csv` PKG-069 deliverable rows | All PKG-069 deliverables, integrator commercial strategy | PROPOSAL: keep PKG-069 as the canonical technical scope register; defer commercial bundling to procurement-strategy deliverable. Document this in EPC Vendor Package Acceptance (DEL-069-06). | TBD |
| C-069-02-04 | Outlet water content "required" value | DBM-Deepcut SEC-06 (expected <0.1 ppmv, dewpoint <-90 °C) | DBM-Deepcut SEC-06 (maximum <1 ppmv, dewpoint -75 °C; "required outlet value TBD") | Specification R-PROC-05, Verification | PROPOSAL: contract the unit to the maximum (worst-acceptable) value as a guarantee floor; carry the expected value as the design target. | TBD |
