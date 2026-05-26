# Guidance — Vendor Engineered Equipment Package (PKG-097 Tanks, Condensate, API 650)

## Purpose

This deliverable is the Package Vendor's production unit for PKG-097. Its purpose is to convert the EPC anchor deliverables (Scope of Work and Package Datasheet) into a vendor-engineered, vendor-designed, vendor-supplied physical equipment package: the API-650 condensate tankage and its package-internal items for the 03-25 Liquids Hub.

Source: `_CONTEXT.md` Scope; DELIVERABLE_REGISTER.csv DEL-097-04 row.

## Principles

1. **EPC anchors govern.** The vendor production-unit shall not invent scope outside the EPC Scope of Work (DEL-097-01) and EPC Package Datasheet (DEL-097-02). Deviations are surfaced for human ruling, not silently absorbed.
2. **API 650 is the construction code.** Detail clauses, edition, addenda, and any "Modified" provisions are governed by the EPC Package Datasheet and the site source slice in `26020-Package_Requirements.docx` heading 49 (location TBD).
3. **Sour-service realism.** The 03-25 Liquids Hub stores sour and product condensate (DBM §"Condensate Storage and Product Handling"). Sour-class tanks are engineered for sour duty even when local upset storage is small (~0.6 day on 2 x 3,800 bbl sour inlet).
4. **Vapour interface integrity.** Tank vapour interfaces must remain compatible with the LP VRU header and with the SCA-002 routing of VRU discharge to 04-25 SOC suction (DBM §"Vapour Recovery").
5. **Tank register subject to supersession.** The 2/4/4/1 functional allocation is the current DBM basis "unless superseded by final tank register" (DBM line 406). Vendor engineering tracks the final tank register issued by the EPC Package Datasheet.
6. **Production unit, not approval authority.** Vendor outputs are inputs to EPC acceptance (DEL-097-06). Vendor does not self-certify integration acceptability.

## Considerations

- **Coating and metallurgy.** Site produced-water tanks use Devchem 253 internal coating (DBM §"Produced-Water Storage…"). This is an ASSUMPTION-only signal for condensate-side selection; final coating and metallurgy are TBD against the EPC Package Datasheet.
- **External insulation and heating.** Cold-climate operability is established for the PW tanks. Condensate-tank insulation/heating provision is TBD.
- **Design SG conflict precedent.** PW tank design SG (1.25 TBC) and pump fluid SG (1.18) discrepancy is flagged for closure during detailed design (DBM §"Produced-Water Storage…"). Vendor shall avoid re-introducing a similar SG inconsistency between condensate tank design SG and condensate pump basis.
- **Slop tank coordination.** Slop tank TK-9130-2 receives liquids from the LP fuel-gas scrubber (DBM §"Fuel Gas"). The vendor slop tank within this package must reconcile that interface with the EPC Package Datasheet.
- **Truck loading and LACT.** Loading pumps and LACT scope are downstream of these tanks; LACT is excluded from 03-25 facility scope (DBM §"Condensate Storage and Product Handling"). The vendor package tie-ins serve the booster pumps and slop routing, not LACT directly.

## Trade-offs

- **Vendor-standard tank vs. site-specialized design.** Vendor-standard configurations reduce cost/schedule risk; site-specialized features (heating, coating, blanket integration) increase fitness for the 03-25 sour-condensate service. Where the EPC Package Datasheet specifies site features, those override vendor standards.
- **Conservative SG / pressure margins vs. cost.** Until design SG and design pressure/temperature are confirmed (currently TBD), conservative margins are advisable but shall be explicitly documented in the vendor design basis.
- **Coating selection.** Adopting a proven site analogue (Devchem 253) eases inspection commonality but may not be optimal for sour condensate; selection is the EPC Package Datasheet's call.

## Examples

- **Functional allocation example:** Current DBM basis — 2 sour inlet + 4 sour + 4 product + 1 slop = 11 x 3,800 bbl. Vendor engineering shall mirror this allocation in tank-by-tank datasheets unless the final tank register issued via DEL-097-02 supersedes it.
- **Vapour interface example:** Each tank vapour nozzle connects to the LP VRU header; under SCA-002, header discharge goes to 04-25 SOC suction, not a local 03-25 SOC (DBM §"Vapour Recovery").

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-01 | Construction code: package title says "API 650"; site PW tanks are described as "API-650 Modified". Whether the condensate tanks here are plain API 650 or "API 650 Modified" is unresolved. | `_CONTEXT.md` PackageName "Tanks, Condensate (API 650) 3-25" | DBM §"Produced-Water Storage…" ("API-650 Modified atmospheric tanks") | Datasheet Construction; Specification R-03, Standards | EPC Package Datasheet (DEL-097-02) governs; vendor follows whichever code/modification it specifies. | TBD |
| C-02 | Tank functional allocation: DBM basis is 2 sour inlet / 4 sour / 4 product / 1 slop, "unless superseded by final tank register". The final tank register has not been confirmed within this deliverable's accessible sources. | DBM §"Condensate Storage and Product Handling" line 406 | Final tank register (not locally accessible) — location TBD | Datasheet Attributes; Specification R-02 | DEL-097-02 EPC Package Datasheet (final tank register) governs. | TBD |
| C-03 | Internal coating: PW tanks use Devchem 253; condensate-tank coating is unspecified in the accessible DBM slice. | DBM §"Produced-Water Storage…" | 26020-Package_Requirements.docx heading 49 — location TBD | Datasheet Attributes; Specification R-07 | EPC Package Datasheet governs; vendor proposes coating only after datasheet specifies service class. | TBD |
| C-04 | Design SG precedent: PW tank design SG (1.25 TBC) vs pump fluid SG (1.18) is open in the DBM; condensate-side SG basis is not given in the accessible slice. | DBM §"Produced-Water Storage…" | (No condensate-side authoritative value located) | Datasheet Conditions; Specification R-09 | EPC Package Datasheet shall declare condensate design SG explicitly; vendor shall not assume PW values. | TBD |
| C-05 | Authority of `26020-Package_Requirements.docx` heading 49: this document is the named source-row anchor in `_REFERENCES.md` but is not text-accessible to the current run. Any clause-level requirement supposedly drawn from it is not yet verifiable. | `_REFERENCES.md`; DELIVERABLE_REGISTER.csv | (file inaccessible as text) | Datasheet; Specification R-03, R-06–R-10; Procedure prerequisites | Re-run with text-extracted slice from heading 49; do not derive clause-level requirements until verified. | TBD |
