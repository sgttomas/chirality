# Guidance: DEL-052-01 — Scope of Work, PKG-052 Inlet / TEG Dehy Cross Exchanger

## Purpose

This Guidance explains the rationale for the PKG-052 Inlet / TEG Dehy Cross Exchanger Scope of Work, the design intent behind the boundaries, and the unresolved items the human owner must rule on before the Scope of Work is signed for vendor RFQ issue.

The Scope of Work exists to bound EPC Integrator responsibility for the one (1) shell-and-tube heat integration exchanger (E-5718-1) within the West Doe 04-25 Deep Cut expansion. The exchanger is a *heat integration* item rather than a primary process unit operation: it reduces gas temperature entering the cryogenic plant and helps balance compression load between inlet and sales compressor services. Source: DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger".

## Principles

1. **Vendor-supplied package, EPC-integrated.** Package Vendor owns the equipment, package engineering, package design, and vendor documentation. EPC Integrator owns the facility-level integration: piping, utilities, drains, EHT, grounding, lighting, controls, structures, and maintenance access. Source: PACKAGE_REGISTER.csv row 62 (Responsibility).
2. **Source-anchored Scope of Work.** Every normative requirement traces to either the project workbook row 62, the 26020-Package_Requirements.docx package heading 7, or the DBM-Deepcut design-basis section. Inference beyond these sources is labeled ASSUMPTION or TBD.
3. **Conflicts surfaced, not resolved silently.** Where accessible sources disagree (notably the warm-side stream identity), the Scope of Work records both candidates and defers the ruling to the owner.

## Considerations

- **Heat integration sensitivity.** The exchanger sits between sour inlet gas and a warm process gas stream. Changes to warm-side source identity will change H2S exposure on the warm side (and therefore materials and metallurgy) and will change downstream temperature into the molecular-sieve filter/coalescers. The warm-side ruling has downstream effects on DEL-052-02 (Package Datasheet) and on heat-integration design.
- **Tube-bundle pull and skid layout.** TEMA 'R' BEM bundles require pull length on one end. Maintenance access (an EPC Integrator interface) must be coordinated with the package skid orientation before construction work-package design (DEL-052-03). ASSUMPTION: tube-pull is conventional BEM practice; confirm in vendor package.
- **Materials for sour service.** Cold side is sour gas from the inlet separator overheads. Sour-service material requirements (NACE MR0175/ISO 15156) are likely applicable. ASSUMPTION: not explicitly stated in accessible sources; confirm in DEL-052-02.
- **EHT and winterization.** The package interface list includes EHT. Cold-side dewpoint and ambient conditions (West Doe site) warrant winterization of skid piping and instrumentation. Source: PACKAGE_REGISTER.csv row 62 (Applicable interface types).

## Trade-offs

- **Warm-side source selection (TEG contactor vs amine absorber overheads).** Selecting dehydrated TEG-contactor overhead gas avoids carrying water to the warm side and may improve materials selection, but routes flow ahead of molecular-sieve filtration in a manner that must be checked against the contactor outlet temperature. Selecting amine-absorber sweet gas matches the workbook scope wording but routes saturated sweet gas through the exchanger, with higher dewpoint and water-handling implications. Both candidates impact heat-integration economics. Owner ruling required; see Conflict Table CT-01.
- **Skid scope vs facility scope at flanges.** Pulling minor instrumentation, lighting, or grounding into the vendor skid scope improves single-point responsibility but may complicate facility-standard maintenance. Default position: vendor stops at skid-edge flanges with all facility-side interfaces in EPC Integrator scope (PACKAGE_REGISTER.csv row 62).

## Examples

- The DBM-Deepcut "Interfaces" section frames a comparable interface unresolution pattern for the inlet/TEG dehy cross exchanger, noting that warm-side identity "must be closed before final P&ID and heat-integration design." This Scope of Work follows that pattern: define what is known, record what is unresolved, and bind the resolution to a named gate (DEL-052-02 Package Datasheet issue) before vendor RFQ release.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-01 | Warm-side stream identity for E-5718-1 is unresolved | PACKAGE_REGISTER.csv row 62 (Scope: "exchanges heat with sweet gas leaving the amine sweetening unit") | DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger" and "Interfaces" (states identity unresolved between dehydrated TEG-contactor overhead gas and warm sweet gas from amine sweetening) | Datasheet.md Process Conditions (warm-side service); Specification.md R2.2, R5.2, R5.3; Guidance.md Trade-offs | PROPOSAL: defer to DBM-Deepcut framing (unresolved); owner to confirm warm-side source before DEL-052-02 issue | TBD |
| CT-02 | Materials standard for sour service not stated in accessible package sources | PACKAGE_REGISTER.csv row 62 (no materials clause) | DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger" (no materials clause) | Datasheet.md Construction Scope (materials); Specification.md Standards | PROPOSAL: ASSUMPTION NACE MR0175/ISO 15156 applies; confirm in DEL-052-02 | TBD |
| CT-03 | Pressure vessel code (ASME BPVC Section VIII) not stated in accessible package sources | PACKAGE_REGISTER.csv row 62 (no code clause) | DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger" (no code clause) | Specification.md Standards | PROPOSAL: ASSUMPTION ASME BPVC Section VIII applies; confirm in DEL-052-02 | TBD |
