# Guidance — Vendor Engineered Equipment Package (DEL-073-04)

> Directional guidance for the Package Vendor and for the EPC Integrator's integration review. Rationale is drawn from DBM-Deepcut SEC-06 ("Amine Treating Basis"), SEC-01 (Project Objectives), and SEC-02 (Site/Layout). Items not supported by accessible source are marked `TBD` or routed to the Conflict Table.

## Purpose

This deliverable exists because the PKG-073 Amine Treating Unit is one of the major process packages of the 04-25 Deep Cut Gas Plant and is procured as a vendor-engineered package rather than EPC-engineered piecewise. The vendor brings packaged amine-unit IP (column hydraulics, solvent management, surge/flash equipment, filtration) that the EPC Integrator integrates into the wider facility. DEL-073-04 is the vendor's production unit; DEL-073-01 (SOW) and DEL-073-02 (Package Datasheet) are the upstream EPC inputs, and DEL-073-06 is the EPC review/acceptance deliverable (`_CONTEXT.md`; DELIVERABLE_REGISTER rows 258–263).

## Principles

1. **Solvent selectivity over deep CO2 removal.** MDEA is selected to remove H2S to ≤4 ppmv while permitting controlled CO2 slip, with sales-gas CO2 ≤2 mol% as the binding downstream constraint (DBM SEC-06 L1156, L1158). The vendor should not propose a non-selective solvent or a configuration that drives CO2 to specification levels lower than required.
2. **H2S priority.** Where H2S removal and CO2 slip trade against each other, H2S removal governs (DBM SEC-06 L1158).
3. **No mercaptan credit.** Mercaptan recovery is 0% in the design basis; the vendor should not size or guarantee the package on incidental mercaptan adsorption (DBM SEC-06 L1157).
4. **Two-train absorption, full-flow filtration.** 2 × 50% absorbers and 2 × 100% inlet coalescers preserve operability and limit downtime during single-train upset, while full-flow particle and slipstream carbon filtration protect the solvent inventory (DBM SEC-06 L1165, L1166, L1170).
5. **Conservative reboiler skin temperature.** 350 °F heat-medium supply with skin ≤350 °F protects MDEA against thermal degradation (DBM SEC-06 L1177); vendors should not propose hotter supply to reduce reboiler area.
6. **Cold-climate package design.** −40 °C to +35 °C ambient envelope governs winterization, package buildings, heat tracing, and instrumentation (DBM SEC-02 L198). The amine area has no methanol injection; therefore hydrate margin must be maintained by upstream temperature control, not by chemical addition (DBM SEC-06 L1153).

## Considerations

- **Carbon filtration sizing.** The 25% lean slipstream through activated carbon balances solvent quality against carbon cost and changeout frequency; vendors with field data may propose alternative slipstream fractions but must justify against degradation kinetics for the inlet contaminant profile (DBM SEC-06 L1170 — vendor data TBD).
- **Reflux accumulator dilution gas.** Dilution-gas review for high-CO2 acid gas is open in the DBM (L1178). If acid gas is at the high-CO2 end of expected range, downstream acid-gas compressor surge and combustion characteristics need to be confirmed jointly.
- **Charge pump model.** API-610 multi-stage horizontal centrifugal axial-split is currently considered (L1175); final model is TBC. Vendor pump-selection rationale should address turndown, NPSHa, and lean-amine temperature.
- **Material selection at low H2S/CO2 ratios.** Open item in DBM L1183/L1388. Vendor should propose materials with explicit reference to lean and rich amine service experience.
- **Surge tank vent / VRU connection.** Surge tank vapors route to VRU header (L1373); the vendor's vent-handling design must close the SG, vent flow, and surge-tank design pressure items currently TBD/TBC (L1183/L1388).

## Trade-offs

| Trade-off | Direction | Source |
|---|---|---|
| MDEA vs. selective formulated solvent | MDEA selected for CO2 slip; alternative formulations may be proposed if performance and economics are demonstrated. | DBM SEC-06 L1158 (basis) |
| Plate-and-frame vs. shell-and-tube lean/rich exchangers | Plate-and-frame selected at 2 × 50% for turndown; vendor may propose alternative if maintenance access and gasket compatibility are addressed. | DBM SEC-06 L1171 |
| Sweet gas scrubber (currently excluded) | Not included as a separate downstream item; absorber top demister provides entrainment control. Vendor proposal to add one is acceptable if entrainment risk to downstream TEG inlet cooler is demonstrated. | DBM SEC-06 L1167 |
| 3 × 57.5% charge pumps vs. 2 × 100% | 3 × 57.5% selected for turndown and reliability; alternative configurations must demonstrate equivalent or better availability. | DBM SEC-06 L1175 |

## Examples

- **Acid-gas overheads handling.** Acid gas leaving the reflux accumulator is pressure-controlled to the acid-gas compressor first-stage suction scrubber. This is the only sink for amine acid gas in the design (DBM SEC-06 L1143; L1371). Vendor pressure control design must coordinate with the acid-gas compressor package basis (DBM SEC-05 L885).
- **Amine slop tank handoff.** Spent or waste amine is drained to the amine slop tank and trucked out for off-site disposal/reclamation (DBM SEC-03 L532). Vendor scope includes the amine slop tank within Module 530 (DBM SEC-06 L1132).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| C-001 | Authoritative package-requirements text is `26020-Package_Requirements.docx` h.27, but the .docx is not locally parseable. Drafts are anchored on DBM SEC-06. | `_CONTEXT.md` (Source Reference) | DBM-Deepcut SEC-06 | All four documents | Treat DBM SEC-06 as proximate authority pending source extraction of `26020-Package_Requirements.docx` h.27; mark divergences as `location TBD`. | TBD |
| C-002 | Module 520 contains both amine and TEG dehydration equipment in DBM (L1131). Package-boundary split between PKG-073 (Amine) and the TEG-dehydration package is not explicit in accessible sources. | DBM SEC-06 L1131 | `_CONTEXT.md` (PKG-073 = Amine Treating Unit) | Specification §Scope; Datasheet §Construction | Vendor scope is limited to amine inlet coalescers, amine absorbers (Module 520 amine portion), and the full Module 530 regeneration train; TEG dehydration is excluded. | TBD |
| C-003 | DBM L1155 lists "low operating pressure TBD." | DBM SEC-06 L1155 | (no second source) | Specification R-1.6 | Vendor to request EPC clarification before final hydraulics. | TBD |
| C-004 | Amine reboiler reference to "steam generated in the amine reboiler" (DBM L1143) conflicts with hot-oil heat-medium basis at 350 °F (DBM L1177, L1375). | DBM SEC-06 L1143 | DBM SEC-06 L1177, L1375 | Datasheet (Reboiler); Specification R-2.11 | Treat "steam" wording in L1143 as generic terminology; the heat medium is hot oil per L1177/L1375. | TBD |
