# Guidance — DEL-096-02 Package Datasheet (Tanks, Sour Condensate, API 650)

> Directional deliverable. Captures rationale, considerations, trade-offs, and unresolved conflicts requiring human ruling.

## Purpose

This package datasheet exists to provide the **EPC Integrator technical handoff** for the sour condensate atmospheric storage tanks in the 03-25 Liquids Hub. Per `_CONTEXT.md`, it is a "Mandatory Gate 5 EPC anchor deliverable" and the "interface facts are intentionally carried here as evidence rather than standalone deliverables." It enables third-party vendor or discipline package engineering and design to proceed without further upstream interpretation.

## Principles

1. **Source-anchored facts only.** Tank counts, capacities, service classifications, and ambient conditions come from the accepted DBM. Statements not grounded in accessible sources are marked `TBD` or `ASSUMPTION`.
2. **Interface clarity over component completeness.** The package datasheet's primary value is unambiguous battery-limit definition; component-level vendor selection is downstream.
3. **Conservative metallurgy under sour service.** Where source ambiguity exists, default to the more conservative interpretation pending human ruling.
4. **No reintroduction of withdrawn scope.** Local 03-25 stabilization, local 03-25 SOC, and condensate dehydration are explicitly out of scope per accepted SCAs (DBM lines 64–65, 366, 442) and shall not be reintroduced as design progresses.
5. **Final tank register governs.** Quantities are subject to supersession per DBM line 406.

## Considerations

- **Sour service stewardship.** Stabilized condensate still contains the mercaptan family listed in the DBM (line 210). Tank internals, gaskets, seals, and roof joints must tolerate these species over service life.
- **Vapour balance with VRU.** Tank breathing must be coordinated with VRU header capacity. VRU is 2 × 100 % 200 hp electric units (line 436) routed to 04-25 SOC under SCA-002 — any sour condensate tank turnover that exceeds VRU header capacity will overpressure or flare.
- **Winterization.** Site basis is −40 °C minimum ambient (line 145). Heat tracing, insulation, valve/instrument freeze protection, and roof drainage all need cold-weather provisions.
- **Source allocation routing.** Future third-party stabilized condensate may route to **sour tanks with optional product-tank routing** (line 382). Tank service flexibility (sour ↔ product) may be a vendor requirement.
- **0.6-day upset storage** (line 411) is short. Operational discipline and 04-25 process reliability govern whether this retention is adequate.

## Trade-offs

| Topic | Trade-off | Recommendation |
|---|---|---|
| Tank standard literal interpretation | "API 650" vs. "API-650 Modified" | Default to API 650 baseline; treat modifications (e.g., external insulation/heating, internal coating, sour-service nozzles) as documented deviations rather than alternate standard. Resolve via CT-01. |
| Internal coating | Devchem 253 (per produced-water tank basis, line 421) vs. coating optimized for sour condensate | Evaluate Devchem 253 chemical compatibility with mercaptan family before adopting wholesale. Resolve via CT-02. |
| Sour/Product tank flexibility | Dedicate tanks to sour service vs. allow product re-routing | DBM permits future third-party routing to sour tanks with optional product routing (line 382). Retain flexible nozzle layout in vendor design. |
| Vapour space basis | Conventional API 650 vapour space (≤ 2.5 psig) vs. low-pressure VRU header coupling | Confirm VRU header design pressure at tank tie-in; pick the more restrictive value. |

## Examples

- **Produced-water tank precedent (DBM line 421):** "API-650 Modified atmospheric tanks, externally insulated and heated, with Devchem 253 internal coating." This is the closest accessible precedent for the sour condensate tank construction style but it is **not** transferable as fact — see Conflict Table.
- **Caustic tank precedent (DBM line 402):** Atmospheric, LP fuel-gas blanket, heating, and insulation. Demonstrates that LP fuel-gas blanket is the local convention for atmospheric tanks; applicability to sour condensate service is `TBD`.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-01 | Package title says "API 650"; the accessible DBM uses "API-650 Modified" only for produced-water tanks and does not state the literal code basis for sour condensate tanks. | `_CONTEXT.md` / PackageName (literal "API 650") | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 421 (produced-water tanks: "API-650 Modified") | Datasheet § Attributes/Construction; Specification R-3, R-11; Standards table | PROPOSAL: Adopt **API 650** as design code with explicit documented modifications (external insulation/heating, internal coating, sour-service appurtenances). Treat "API-650 Modified" as identical baseline + listed modifications, not a different standard. | TBD — requires EPC Integrator ruling. **HRR (Human Ruling Required).** |
| CT-02 | Internal coating Devchem 253 is stated in the DBM for produced-water tanks only; it is not stated for sour condensate tanks but is the only locally-cited coating precedent. | DBM line 421 (produced-water tanks: Devchem 253) | No source — silence in DBM section 06 for condensate tanks | Datasheet § Construction (Internal Coating); Specification R-9 | PROPOSAL: Carry Devchem 253 as candidate pending vendor sour-condensate compatibility confirmation; do not adopt as default without test data. | TBD — requires coating engineering ruling. **HRR.** |
| CT-03 | DBM line 406 says "unless superseded by final tank register" — the tank count and functional allocation may change. | DBM line 406 | Final tank register (not yet produced) | Datasheet § Identification/Attributes; Specification R-1, R-12 | PROPOSAL: Lock current basis (2 sour inlet + 4 sour condensate) for the package datasheet; track any superseding tank register as a controlled change. | TBD — confirm at gate. **HRR.** |
| CT-04 | DBM line 421 cites produced-water tank design SG 1.25 TBC vs. pump fluid SG 1.18 — discrepancy. The sour condensate tank design SG is **not stated**. | DBM line 421 (water service SGs) | No accessible value for sour condensate SG | Datasheet § Conditions (Stored Fluid SG) | PROPOSAL: Capture sour condensate density/SG from vendor or stream composition basis during detailed design; mark TBD here. | TBD — requires process engineering data. **HRR.** |
| CT-05 | Package title references the source `26020-Package_Requirements.docx` package heading 48 which is **not locally accessible** (binary .docx). Any requirements unique to that file are presently missing. | `_CONTEXT.md` / `_REFERENCES.md` references the .docx | No accessible plain-text equivalent | All four documents | PROPOSAL: Convert `26020-Package_Requirements.docx` heading 48 to a locally accessible source slice (pdf2md or equivalent extraction) and re-run drafting. | TBD — requires source ingestion step. **HRR.** |

**HRR items above** = CT-01, CT-02, CT-03, CT-04, CT-05. Each is marked `TBD` pending human ruling; downstream design may proceed using the PROPOSAL value at the EPC Integrator's risk.
