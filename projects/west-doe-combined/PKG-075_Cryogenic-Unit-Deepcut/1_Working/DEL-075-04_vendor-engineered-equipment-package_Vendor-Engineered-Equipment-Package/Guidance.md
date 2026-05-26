# Guidance — DEL-075-04 Vendor Engineered Equipment Package (Cryogenic Unit "Deepcut")

## Purpose

This deliverable represents the **vendor-engineered physical equipment** at the heart of the West Doe Deepcut expansion: the UltraTEF cryogenic NGL recovery unit. It exists so a qualified package vendor can produce the engineering, design, fabrication, and the equipment package itself from the EPC Scope of Work (DEL-075-01) and EPC Package Datasheet (DEL-075-02), under EPC Integrator integration review (`_CONTEXT.md`; DBM-Deepcut SEC-01).

## Principles

1. **EPC anchors are authoritative.** The Scope of Work and Package Datasheet from PKG-075 govern what the vendor produces. The DBM provides the upstream design-basis values; vendor decisions must reconcile to both (DBM-Deepcut SEC-10 Applicability and Limits — process-unit and unit-specific sections govern where more specific).
2. **Source fidelity over decomposition prose.** Process basis values (recoveries, design conditions, equipment counts) come from DBM-Deepcut, not from decomposition summaries.
3. **Conservative inference.** Items not present in accessible sources are TBD or labeled ASSUMPTION, never invented (DEL-075-04 scope discipline; CONTRACT K-PROV-1).
4. **Winter governs much of the mechanical sizing.** Deethanizer reboiler service, pump differentials, and BAHX hydraulics are checked against winter operating loads (DBM-Deepcut SEC-06).
5. **Expander mode is design; J-T mode is real and must work safely.** Sales-gas total-sulphur compliance in upset/start-up requires J-T mode to deliver >=27% C3 recovery (DBM-Deepcut SEC-03 + SEC-06).
6. **Cryogenic safety drives mechanical features.** Water dewpoint <-75 degC, methanol injection at multiple points, J-T mechanical stroke limit for flare protection, MDMT protection via BAHX E-pass bypass, expander lube-oil accumulator ESD rundown (DBM-Deepcut SEC-06).

## Considerations

### Mercury tolerance (BAHX)
The DBM requires the upstream MRU to protect BAHX from elemental mercury, but also requires "mercury-tolerant features" for the BAHX itself (TBD detail). Vendor should propose mercury-tolerant practice and state assumptions explicitly (DBM-Deepcut SEC-06).

### J-T mode performance envelope
Several J-T-mode numbers (C4+ recoveries, sales flow, sales pressure) are TBC. Vendor should present J-T-mode performance as a function of inlet conditions and identify when sales-gas total-sulphur compliance limits throughput (DBM-Deepcut SEC-06 Open Items).

### Methanol injection topology
The DBM lists candidate methanol injection points but flags required points and capacities as TBC. Vendor should propose a coherent system with single-point-at-a-time injection logic and clear capacity sizing (DBM-Deepcut SEC-06).

### Future NGL interface
Deethanizer bottoms routing currently includes "future deethanizer bottoms exchanger" and "future deethanizer bottoms cooler" provisions for downstream NGL mercaptan treating. Vendor design should accommodate the tie-in without committing to the future equipment (DBM-Deepcut SEC-06).

### Mercaptan concentration
Cryogenic liquids can concentrate mercaptans; design summer expander-mode C3+ deethanizer bottoms can contain methyl mercaptan ~1373 ppmv and ethyl mercaptan ~2640 ppmv (DBM-Deepcut SEC-06 UltraTEF Design Values). This influences materials selection, gasketing, and downstream interface design.

### Site / layout dependence
Final equipment placement and spacing compliance depend on the plot plan CIV-235633-5002, which is currently unavailable in the source set (DBM-Deepcut SEC-02). Vendor general arrangement should preserve the spacing criteria from SEC-02 (process-equipment, fired-equipment, flare, MCC distances).

### Construction handoff
Off-loading, setting, and mechanical hookup are Tourmaline field-construction scope (DBM-Deepcut SEC-01). Vendor design should produce modules and skid limits compatible with field-construction handling.

## Trade-offs

| Trade-off | Considerations |
|---|---|
| Modularization vs. site assembly | Modular favors quality and schedule; site assembly favors transport/lift constraints. Tourmaline-led construction at 04-25 implies module-friendly packaging. |
| BAHX excess area vs. weight/cost | Specified minimum 10% excess area; vendor may propose more for mercury tolerance and fouling margin (DBM SEC-06). |
| Expander aftercooler winter operation | DBM flags below-95 degF winter operation as needing study; warm-air recirculation/bypass may be required. |
| J-T-mode capacity vs. simplicity | A wider J-T capacity envelope simplifies start-up but increases valve and absorber sizing implications. |
| Methanol redundancy | More injection points improve operability; concentration at vulnerable hydrate points improves protection. Single-point-at-a-time logic constrains the choice. |

## Examples

- DBM-Deepcut SEC-06 UltraTEF Equipment table provides authoritative equipment-by-equipment design statements. Vendor datasheets should cite these as the design basis where the value originates from DBM and label vendor-derived values explicitly.
- DBM-Deepcut SEC-10 Package Line-Item Requirements row 9 provides the binding equipment tag list (15 items) for cross-checking vendor bill-of-materials.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-01 | Deethanizer bottoms C2/C3 operating target stated as "<=654 mol%" in DBM-Deepcut SEC-06 UltraTEF Design Values; mol% cannot exceed 100. Likely intended 6.54 mol% (vs. design <=1.5 mol%). | DBM-Deepcut SEC-06 (table row "Deethanizer bottoms product") | (internal arithmetic consistency) | Datasheet Attributes; Specification R-1; verification approach | Interpret as 6.54 mol% operating target | TBD |
| C-02 | Cryogenic-Unit-Deepcut package sparing basis not stated. Package Roster (SEC-10) shows a single entry, but no explicit single-train ruling. | DBM-Deepcut SEC-10 Package Roster | DBM-Deepcut SEC-06 (no parallel-unit language) | Specification R-6.1; vendor scope sizing | Treat as single train; vendor to confirm | TBD |
| C-03 | `26020-Package_Requirements.docx` package heading 29 is listed in `_REFERENCES.md` but available only as binary. Any vendor-package requirements unique to that document have not been incorporated. | `_REFERENCES.md` (DEL-075-04) | DBM-Deepcut (DBM does not substitute) | All four documents | Convert docx to text or open vendor-requirements source slice before next pass | TBD |
| C-04 | Plot plan CIV-235633-5002 is not in the source set; package GA and spacing compliance cannot be confirmed at layout level. | DBM-Deepcut SEC-02 Plot Plan Status | DBM-Deepcut SEC-02 Spacing tables | Specification R-7.x; Procedure (siting confirmation) | Vendor GA produced provisionally; reissue after plot plan publishes | TBD |
