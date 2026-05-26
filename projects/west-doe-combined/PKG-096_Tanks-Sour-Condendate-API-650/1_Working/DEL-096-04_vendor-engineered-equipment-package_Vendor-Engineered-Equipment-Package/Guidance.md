# Guidance — DEL-096-04 Vendor Engineered Equipment Package (Tanks, Sour Condensate, API 650)

> Directional deliverable. Captures rationale, considerations, trade-offs, and unresolved conflicts requiring human ruling. The Vendor Engineered Equipment Package is the Package Vendor production unit; this guidance frames how the vendor produces and the EPC Integrator reviews the package.

## Purpose

The Vendor Engineered Equipment Package exists to convert the EPC anchoring inputs (DEL-096-01 Scope of Work and DEL-096-02 Package Datasheet) into a **physically engineered, fabricated/supplied tank package** plus its **vendor design basis and datasheet set**. Per `_CONTEXT.md`, this is the Package Vendor production unit, with EPC Integrator integration review. Without this deliverable, the EPC Integrator has no vendor-engineered hardware to install (DEL-096-03), accept (DEL-096-06), or document the turnover of (DEL-096-05).

## Principles

1. **EPC anchors govern vendor scope.** DEL-096-01 (SOW) and DEL-096-02 (Package Datasheet) bind the vendor; deviations are documented, not silent.
2. **Source-anchored facts only.** Tank counts, capacities, service classifications, site conditions, and ambient envelope come from the accepted DBM. Statements not grounded in accessible sources are marked `TBD` or `ASSUMPTION`.
3. **Conservative metallurgy under sour service.** Where source ambiguity exists, default to the more conservative interpretation pending human ruling.
4. **No reintroduction of withdrawn scope.** Local 03-25 stabilization, local 03-25 SOC, and condensate dehydration are explicitly out of scope per accepted SCAs (DBM lines 64–65, 366, 442) and shall not appear in vendor scope.
5. **Vendor document scope is bounded.** This deliverable produces the **vendor design basis and datasheet set** plus hardware; vendor document register and turnover records are DEL-096-05.
6. **Final tank register governs.** Quantities and functional allocations remain subject to supersession per DBM line 406; vendor engineering change must accommodate.
7. **Integration review is the EPC backstop.** The vendor is responsible for engineering correctness; the EPC Integrator is responsible for integration correctness against facility-wide systems (VRU, foundations, layout, electrical, controls).

## Considerations

- **EPC anchor maturity.** DEL-096-01 and DEL-096-02 are sibling deliverables in PKG-096. Vendor engagement before those anchors are ISSUED introduces rework risk. ASSUMPTION: vendor will be engaged after anchor ISSUE; if not, treat the vendor package as preliminary.
- **Sour service stewardship.** Stabilized condensate still contains the mercaptan family (DBM line 210). Tank internals, gaskets, seals, and roof joints must tolerate these species over service life. Mercaptan compatibility evidence is a vendor responsibility under R-7.
- **Vapour balance with VRU.** Tank breathing must coordinate with VRU header capacity (2 × 100% 200 hp electric units, line 436) routed to 04-25 SOC under SCA-002. Vendor PVRV sizing and the EPC VRU header sizing must be reconciled at the tank tie-in.
- **Winterization.** Site basis is −40 °C minimum ambient (line 145). Heat tracing, insulation, valve/instrument freeze protection, and roof drainage all need cold-weather provisions. Vendor design package must show winterization details and load implications for the EPC civil scope.
- **Source allocation routing flexibility.** Future third-party stabilized condensate may route to sour tanks **with optional product-tank routing** (line 382). Vendor design should not preclude this; e.g., nozzle layout, transfer pump piping interface, and instrumentation provisions.
- **0.6-day upset storage** (line 411) is short. Vendor design should support smooth turnaround/changeover operations (sample valves, drains, accessible manways) so operations is not penalized by a tight storage envelope.
- **Geotechnical preliminary.** SEC-02 lists soil as "clay over clay till," Site Class D, with foundation parameters TBD. Vendor foundation load deliverable must allow EPC civil to size against the final geotechnical report — i.e., loads + settlement criteria as ranges/inputs, not assumed foundation.
- **Source binary gap.** `26020-Package_Requirements.docx` heading 48 and `26020-Packages_Interfaces_4_export.xlsx` are referenced but **binary and not locally accessible**. Specific project-form requirements they encode may not be reflected in this deliverable until extracted — see CT-05.

## Trade-offs

| Topic | Trade-off | Recommendation |
|---|---|---|
| Tank standard literal interpretation | "API 650" vs. "API-650 Modified" | Default to API 650 baseline; treat modifications (external insulation/heating, internal coating, sour-service nozzles) as documented deviations rather than a separate standard. Resolve via CT-01. |
| Internal coating | Devchem 253 (per produced-water tank basis, line 421) vs. coating optimized for sour condensate | Evaluate Devchem 253 mercaptan compatibility before adopting; require vendor compatibility statement. Resolve via CT-02. |
| Vendor scope split between shop fabrication and field erection | Shop-built (smaller diameter) vs. field-erected (larger diameter, more shipping flexibility) | Vendor selects; EPC reviews shipping envelope, lay-down area, and field erection schedule fit. |
| Materials selection conservativeness | Carbon steel + coating vs. clad/stainless components in selected service | Default conservative for sour wetted areas; carbon steel + qualified coating elsewhere; vendor justifies per NACE basis. Resolve sour metallurgy via CT-04. |
| Vapour space pressure setting | Conventional API 650 vapour space (≤ 2.5 psig) vs. low-pressure VRU header coupling | Confirm VRU header design pressure at tank tie-in; pick the more restrictive value. |
| Tank service flexibility | Dedicate tanks to sour service vs. allow product re-routing | DBM permits future third-party routing flex (line 382). Retain flexible nozzle layout in vendor design. |
| Vendor design basis vs. EPC Package Datasheet duplication | Replicate every field vs. cite-by-reference | Vendor design basis should cite-by-reference and add only vendor-internal engineering content (load takeoffs, weld map, NDE plan), to keep DEL-096-02 the single source of truth for facility-side data. |

## Examples

- **Produced-water tank precedent (DBM line 421):** "API-650 Modified atmospheric tanks, externally insulated and heated, with Devchem 253 internal coating." Closest accessible precedent for the sour condensate tank construction style; not transferable as fact — see CT-01, CT-02.
- **Caustic tank precedent (DBM line 402):** Atmospheric, LP fuel-gas blanket, heating, and insulation. Demonstrates that LP fuel-gas blanket is the local convention for atmospheric tanks; applicability to sour condensate service is `TBD`.
- **Sibling deliverable DEL-096-02 Datasheet** provides the EPC-side data the vendor consumes; vendor design basis should cite back to it rather than restating.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-01 | Package title says "API 650"; the accessible DBM uses "API-650 Modified" only for produced-water tanks and does not state the literal code basis for sour condensate tanks. | `_CONTEXT.md` / PackageName (literal "API 650") | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 421 (produced-water tanks: "API-650 Modified") | Datasheet § Attributes/Construction; Specification R-4, R-15; Standards table | PROPOSAL: Adopt **API 650** as design code with explicit documented modifications (external insulation/heating, internal coating, sour-service appurtenances). Treat "API-650 Modified" as identical baseline + listed modifications, not a different standard. | TBD — requires EPC Integrator ruling. **HRR (Human Ruling Required).** |
| CT-02 | Internal coating Devchem 253 is stated in the DBM for produced-water tanks only; it is not stated for sour condensate tanks but is the only locally-cited coating precedent. | DBM line 421 (produced-water tanks: Devchem 253) | No source — silence in DBM SEC-06 for condensate tanks | Datasheet § Construction (Internal Coating); Specification R-9 | PROPOSAL: Carry Devchem 253 as candidate pending vendor sour-condensate mercaptan compatibility confirmation; do not adopt as default without test data. | TBD — requires coating engineering ruling. **HRR.** |
| CT-03 | DBM line 406 says "unless superseded by final tank register" — the tank count and functional allocation may change before vendor fabrication release. | DBM line 406 | Final tank register (not yet produced) | Datasheet § Identification/Attributes; Specification R-2, R-13 | PROPOSAL: Lock current basis (2 sour inlet + 4 sour condensate) for vendor engineering; track any superseding tank register as a controlled vendor engineering change with cost/schedule impact. | TBD — confirm at gate. **HRR.** |
| CT-04 | Sour-service NACE standard is not explicitly named in the accessible DBM slice; vendor metallurgy selection has no locally-cited binding standard reference. | DBM (no NACE citation in accessible slices) | Common industry default: NACE MR0175 / ISO 15156 | Specification R-8; Standards table | PROPOSAL: Vendor shall comply with NACE MR0175 / ISO 15156 for sour-service materials selection unless EPC Integrator names an alternative. | TBD — requires EPC Integrator ruling. **HRR.** |
| CT-05 | Project source `26020-Package_Requirements.docx` heading 48 and `26020-Packages_Interfaces_4_export.xlsx` are referenced in `_CONTEXT.md` / `_REFERENCES.md` but are **binary and not locally accessible**. Requirements unique to those files are presently missing from this deliverable. | `_CONTEXT.md` / `_REFERENCES.md` references | No accessible plain-text equivalent | All four documents | PROPOSAL: Convert these source files to a locally accessible source slice (pdf2md / docx2md / xlsx2csv) and re-run the four-documents skill. | TBD — requires source ingestion step. **HRR.** |
| CT-06 | Vendor split between shop fabrication and field erection is not stated in any accessible source. | None accessible | Industry convention (tank diameter > ~12 m typically field-erected) | Datasheet § Construction (Shipping/Site Erection); Specification (implicit) | PROPOSAL: Vendor proposes shop vs. field split with shipping/erection schedule; EPC reviews for site logistics fit. | TBD — vendor proposal at engineering. **HRR.** |

**HRR items above** = CT-01, CT-02, CT-03, CT-04, CT-05, CT-06. Each is marked `TBD` pending human ruling; downstream design may proceed using the PROPOSAL value at the EPC Integrator's risk.
