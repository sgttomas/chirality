# Guidance — DEL-052-04 Vendor Engineered Equipment Package (Inlet / TEG Dehy Cross Exchanger)

## Purpose

This deliverable exists to bound the Package Vendor's responsibility for the engineered physical equipment for the Inlet / TEG Dehy Cross Exchanger (E-5718-1) so that the EPC Integrator can hand off well-defined scope (DEL-052-01) and technical basis (DEL-052-02), receive a fabricated package, and integrate it into the 4-25 facility. [Source: `_CONTEXT.md` Scope; decomposition row for DEL-052-04.]

## Principles

- **EPC handoff basis is authoritative.** Vendor engineering proceeds from the EPC Scope of Work (DEL-052-01) and Package Datasheet (DEL-052-02). The DBM source provides framing context (size, design pressure/temperature, service) but is not a substitute for the EPC Package Datasheet. [Source: `_CONTEXT.md` Scope.]
- **Heat-integration intent.** The exchanger exists to reduce gas temperature entering the cryogenic plant and to help balance compression load between inlet and sales compressor services. Vendor design choices that degrade this intent must be flagged for EPC review. [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 606.]
- **Source-grounded conservatism.** Where the EPC Package Datasheet is silent and only DBM-level basis is available, vendor proposals are PROPOSAL rather than commitment.

## Considerations

- The warm-side stream identity is unresolved between dehydrated TEG-contactor overhead gas and warm sweet gas leaving the amine sweetening unit (see Conflict Table). This drives composition, water content, and material-selection choices. [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 606, 836.]
- Sour-gas service severity (H2S, CO2 partial pressures) is referenced in the broader DBM context (sour-gas dehydration upstream) but the specific service envelope at E-5718-1 is TBD pending EPC Package Datasheet issue. ASSUMPTION: NACE MR0175 / ISO 15156 sour-service qualification applies.
- The exchanger sits between TEG dehydration and process-gas molecular-sieve dehydration; carryover and upset conditions in the TEG unit could affect inlet conditions to the exchanger. [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 1193, 1278.]
- The DBM names the configuration as BEM "as described in the DBM source"; vendor should confirm shell/tube head selection against thermal design, maintenance access, and sour-service inspection needs. [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 602.]

## Trade-offs

- **Tighter approach temperature vs. surface area / cost.** A closer hot-end approach improves heat-integration benefit (R-6) but increases area and pressure drop; the optimum point belongs in the EPC Package Datasheet rather than vendor judgment.
- **Materials uplift vs. corrosion margin.** Conservative material selection (e.g., upgraded tube alloy) reduces sour-service risk but increases cost and lead time; finalize after the R-5 warm-side ruling.
- **Shop-assembled package vs. site assembly.** Higher shop content reduces field labour and improves QA but adds shipping/lifting constraints. TBD against site logistics defined in DEL-052-03.

## Examples

- DBM equipment list assigns one shell-and-tube cross exchanger E-5718-1 in the 4-25 (Deepcut) unit, in the "Heat Exchangers (Shell and Tube)" class alongside Inlet Condensate Heaters Units 1 and 2. [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2537, 2586.]

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-1 | Warm-side stream identity is unresolved (dehydrated TEG-contactor overhead gas vs. warm sweet gas leaving the amine sweetening unit) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 606 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 836 (same source flags the unresolved state) | Datasheet "Warm-side fluid"; Specification R-5, R-8; Guidance "Considerations"; Procedure "Prerequisites" | EPC Package Datasheet (DEL-052-02) issues the binding warm-side identity; vendor freezes design against that ruling | TBD |
| C-2 | Code of construction and sour-service standards not explicitly cited in the accessible source slice | ASSUMPTION (industry convention: ASME VIII Div 1, TEMA R, NACE MR0175 / ISO 15156) | 26020-Package_Requirements.docx heading 7 — text not extracted (location TBD) | Specification R-7, R-8, "Standards" table | EPC Package Datasheet to confirm code/standards stack | TBD |
