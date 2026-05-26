# Guidance — DEL-079-04 Vendor Engineered Equipment Package

## Purpose

This deliverable exists because PKG-079 carries a Package Vendor production unit: the consolidated instrument air package at 04-25 that serves the 04-25 gas plant, the 03-25 liquids hub, and the 03-25 compressor station as a shared utility. The vendor is responsible for engineering, design, fabrication/supply, and the physical equipment package developed from the EPC Scope of Work (DEL-079-01) and the EPC Package Datasheet (DEL-079-02). (Decomposition row 381; `_CONTEXT.md`.)

## Principles

- **Shared-utility basis.** The consolidated 04-25 instrument air package is the single shared package basis for both 04-25 and 03-25 demand. Local 03-25 instrument-air compressors are explicitly superseded under SCA-006 (SourcePath: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`; SectionRef: L68, L473).
- **EPC anchor, vendor execute.** The EPC Scope of Work and Package Datasheet anchor what must be built; the vendor's engineered package implements them. The vendor proposes; the EPC Integrator integrates and reviews (DEL-079-06 handles formal acceptance).
- **TBC numbers are not vendor-final.** Demand numbers (720 / 393 / 1,113 SCFM) are TBC in the source basis. Vendor sizing must reconcile against EPC-confirmed instrument counts at detailed engineering, not against the TBC table alone (SourcePath: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; SectionRef: L1925).
- **Reserve volume is a safety-significant design margin.** The 15-minute usable reserve after IA shutdown is the basis for safe-state hold-up of facility shutdown valves; vendor sizing of the dry and wet receivers and the header volume must explicitly demonstrate this margin from 120 psig down to 80 psig (SectionRef: L1941-L1942).

## Considerations

- **03-25 booster compressor question is open.** Whether a 03-25 booster compressor is required is unresolved in the source basis and must be confirmed in detailed engineering. The vendor package scope as written assumes consolidated compression at 04-25 (SectionRef: L1925; cross-ref `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L820).
- **Caustic-unit oxidation air (214 SCFM) is the single largest 03-25 demand line item.** Its TBC status materially affects compressor sizing; vendor should flag any change to this number as a sizing trigger (SectionRef: L1919).
- **Area classification is assumed Non-Classified.** The vendor must validate this against the building configuration and combustible-gas inventory; do not silently accept the assumption (SectionRef: L1943).
- **Spectacle-blind exception at skid edge is unusual.** Other services require spectacle blinds at skid edge; instrument air explicitly does not. This is a deliberate design choice — vendor should not "add it back" for consistency (SectionRef: L2452).
- **Sparing matters for the third-compressor provision.** Skid spacing and piping provision (not just floor space) must be designed in; retrofitting piping later defeats the intent (SectionRef: L1940).

## Trade-offs

- **Consolidation at 04-25 versus distributed compression.** Consolidation simplifies vendor scope and maintenance but creates a cross-facility single point of failure and adds distribution losses to 03-25. The consolidated basis is set; the trade is captured here for the human record.
- **20 percent contingency applied at the per-facility level versus combined level.** The source applies 20 percent contingency per facility and then sums (720 + 393 = 1,113). A combined-level contingency would yield a different number. The current basis is per-facility; vendor must not silently re-roll the contingency.
- **PSV setting "1034 kPag or less."** The source permits any setting at or below 1034 kPag. Vendor should select the highest setting consistent with discharge piping rating to maximize reseat margin; do not set arbitrarily low.

## Examples

- **Lead-lag changeover narrative.** Lead compressor runs; lag compressor in hot standby; lag starts on header pressure droop below a defined setpoint (setpoint TBD; not in source). Source supports the 2 x 100 percent lead-lag arrangement (SectionRef: L1939) but not the specific changeover setpoint — that is vendor scope.
- **Skid-edge tie-in pattern.** Block valve at skid edge, located outside the building, in the interconnect run between the pipe rack and the package; NO spectacle blind (instrument air exception). Pipe-rack-side 1 in. vent valve per the generic skid-edge isolation pattern (SectionRef: L2455).

## Conflict Table (for human ruling)

No conflicts identified between sources during this Pass 1/Pass 2 run. The 03-25 and 04-25 DBMs agree on the consolidated-at-04-25 basis and on the 720 / 393 / 1,113 SCFM split. The TBC labels on demand numbers are flagged consistently in both sources.

If a vendor proposal or EPC clarification raises a numeric or scope conflict during execution, populate this table with: Conflict ID; Conflict (short statement); Source A (file + section); Source B (file + section); Impacted sections; Proposed authority (PROPOSAL); Human ruling (TBD).
