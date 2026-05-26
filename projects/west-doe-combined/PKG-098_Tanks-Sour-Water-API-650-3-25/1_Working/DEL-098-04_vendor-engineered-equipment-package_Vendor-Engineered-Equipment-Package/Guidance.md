# Guidance — DEL-098-04 Vendor Engineered Equipment Package

> Directional rationale, considerations, trade-offs, and human-ruling Conflict Table for the Vendor Engineered Equipment Package.

## Purpose

This deliverable carries the **vendor-side** production for PKG-098 "Tanks, Sour Water (API 650) 3-25": the Package Vendor engineers, designs, fabricates, and supplies the physical tank package from the EPC-side anchor deliverables (Scope of Work DEL-098-01, Package Datasheet DEL-098-02, Construction Work Package DEL-098-03). Without this deliverable, PKG-098 has no physical product to install, and downstream EPC review and acceptance (DEL-098-06) has nothing to assess.

## Principles

1. **EPC anchors, vendor builds.** SOW and Package Datasheet define what must be produced; the vendor decides how within those constraints. The vendor must not silently re-scope.
2. **Source fidelity over convention.** Where the source document (`26020-Package_Requirements.docx` package heading 50) states a value (e.g., "32 oz test pressure", "Modified API 650"), the vendor SHALL honor that wording even where convention might suggest different defaults.
3. **TBD honesty.** Source-declared TBDs (operating temperature for Item 2; driver; Appendix A throughput) are visible TBDs and SHALL be resolved through formal EPC clarification — not silently chosen by the vendor.
4. **Sour service caution.** "Sour" naming triggers metallurgy, NDE, PWHT, and coating discipline. Treat sour-service requirements as a binding constraint pending EPC confirmation, not an optional enhancement.
5. **Cold-climate envelope.** The -40 °C ambient basis (3-25 DBM) governs winterization across insulation, heat tracing, instrumentation, and material toughness, even where vendor-default standard climate would be milder.

## Considerations

- **Coating system.** Devchem 253 is named explicitly for floor, walls, and roof; substitution requires EPC approval. Surface-prep, application environment, and DFT control matter for sour produced-water service.
- **External electric heating.** Power source, redundancy of circuits, controllability, and integration with site electrical (by Others) require interface coordination with EPC Integrator.
- **Skim system.** Kennilworth HCL float skim system is a named vendor item; integration with tank internals, manways, and access affects mechanical design.
- **SG discrepancy.** Pump basis SG 1.18 vs tank design SG 1.25 (TBC) per 3-25 DBM is a known open item that must be closed during detailed design (see Conflict C-2).
- **Item 3 service classification.** SOW-0223 names Item 3 plainly "Produced Water Storage Tanks" while the package is titled "Sour Water"; downstream DBM allocation suggests these may be sweet (DBM: "5 sour, 2 sweet"). This is a conflict (see Conflict C-1).
- **Tag-set count vs Basic-scope.** SOW-0222 ("Basic scope") names only Item 1 (3 sour produced-water tanks). SOW-0223 ("Major included equipment") names all seven tanks across Items 1–3. The major-equipment list governs vendor supply per the source's own structure, but the "Basic scope" wording is narrower (see Conflict C-3).

## Trade-offs

- **Vendor-standard vs project-specific design.** Tank vendors typically have standard product lines for API 650 (Modified) atmospheric tanks; conforming to project-specific items (Devchem 253 coating, Kennilworth HCL skim, -40 °C envelope) may force non-standard configurations. Vendor proposal should make non-standard elements explicit.
- **Insulation/heating extent.** Source says "externally insulated and heated"; the trade-off between insulation thickness and heating duty is a vendor optimization that affects energy load on facility electrical (by Others).
- **Sour-service NDE rigor (ASSUMPTION).** Higher NDE coverage and PWHT increase cost and schedule but reduce in-service inspection burden and cracking risk. The EPC Package Datasheet (DEL-098-02) should specify the applicable rigor; absent that, the vendor SHALL propose a level appropriate to NACE MR0175 / ISO 15156 sour-service criteria.

## Examples

Source: 3-25 DBM "Produced-Water Storage, Treatment, and Transfer" reads:
> "The produced-water system includes seven 3,800 bbl tanks: five sour produced-water tanks and two sweet produced-water tanks. Tanks are API-650 Modified atmospheric tanks, externally insulated and heated, with Devchem 253 internal coating."

This DBM language is consistent with SOW-0223 on tank count, capacity, code, coating, insulation, and heating, but introduces a sour/sweet allocation (5/2) that the source `.docx` slices captured in SCOPE_LEDGER do not state in the same terms (see Conflict C-1).

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short) | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-1 | Item 3 service classification: SOW-0223 names Item 3 simply "Produced Water Storage Tanks (TK-9010-1, TK-9020-1)"; 3-25 DBM allocates "5 sour, 2 sweet" produced-water tanks, implying Items 1 + 2 are sour (5 tanks) and Item 3 is sweet (2 tanks). | SCOPE_LEDGER row SOW-0223 (`26020-Package_Requirements.docx` package heading 50; Major included equipment) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "Produced-Water Storage, Treatment, and Transfer" | Datasheet (service column for Item 3); Specification R-10 (sour-service scope) | PROPOSAL: Treat Item 3 (TK-9010-1, TK-9020-1) as **sweet** produced-water service consistent with the DBM 5/2 allocation; treat Items 1 and 2 as sour. Carry "Sour Water" package title as historical, not as evidence that all seven tanks are sour. | TBD |
| C-2 | Produced-water SG discrepancy: pump basis SG 1.18 vs tank design SG 1.25 (TBC). | 3-25 DBM "Liquids Hub Design Basis" table | 3-25 DBM "Produced-Water Storage, Treatment, and Transfer" | Datasheet (Conditions); Specification R-9; Procedure step on design-input freeze | PROPOSAL: Adopt **tank design SG 1.25** as the conservative tank-design value pending closure during detailed design; retain pump basis SG 1.18 for hydraulic equipment scope outside this deliverable. | TBD |
| C-3 | Tank-count scope tension: SOW-0222 "Basic scope" names only Item 1 (three sour tanks); SOW-0223 "Major included equipment" names all seven tanks. | SCOPE_LEDGER row SOW-0222 | SCOPE_LEDGER row SOW-0223 | Specification scope; R-7; R-8; Datasheet equipment list | PROPOSAL: Treat SOW-0223 "Major included equipment" list as the binding vendor supply scope (seven tanks across three items); treat SOW-0222 "Basic scope" wording as a non-exhaustive headline. | TBD |
| C-4 | Standards locality: API 650 (Modified) and NACE MR0175 / ISO 15156 (sour service ASSUMPTION) are cited but not locally accessible — full clause text cannot be confirmed from `_Sources/`. | SOW-0223 (states "Modified API 650") | Absent in `_Sources/` | Specification Standards table; R-10 | PROPOSAL: Accept "Modified API 650" as governing per source; require EPC to issue the specific Modified-API-650 deviations list and the applicable sour-service standard set in the Package Datasheet (DEL-098-02). | TBD |
| C-5 | Open source-declared items: Item 2 operating temperature, driver selection, and Appendix A capacity/throughput are all source-declared TBD or "see attached". | SCOPE_LEDGER row SOW-0224 | — | Datasheet; Specification R-5, R-7, R-11; Procedure inputs | PROPOSAL: Carry as TBD; freeze via formal EPC clarification before vendor IFC release. | TBD |
