# Guidance — DEL-093-01 Scope of Work (PKG-093 Tanks, Water (API 650) 3-25)

## Purpose

This Guidance document explains why DEL-093-01 exists, the principles that govern its content, the trade-offs that emerged from source material, and the open items (held requirements and conflicts) that downstream parties must close. It is the directional companion to the normative `Specification.md` and the descriptive `Datasheet.md`.

The Scope of Work is the EPC-Integrator anchor for PKG-093. It binds the Package Vendor to a defined engineering and equipment scope and provides the EPC Integrator with the integration narrative needed to align the package to the 03-25 Liquids Hub. (Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv DEL-093-01.)

## Principles

1. **Workbook row authority.** Workbook Packages row 95 and 26020-Package_Requirements.docx heading 45 are the authoritative scope envelope for PKG-093. (Source: PACKAGE_REGISTER.csv; SCOPE_LEDGER.csv.)
2. **Vendor / EPC split.** Package Vendor owns engineering, design, and equipment supply. EPC Integrator owns facility integration. Foundations, mounting, electrical/instrumentation, platforms, and staircases are EPC-side. (Source: SOW-0229; SOW-0232.)
3. **Sweet service only.** PKG-093 covers sweet produced water and process water service. Sour produced water tanks at 03-25 are a separate scope (per DBM, the full produced-water system has 5 sour + 2 sweet tanks; only the 2 sweet are in PKG-093). (Source: SOW-0230; DBM §Produced-Water Storage.)
4. **API 650 modified, not full API 650.** The tanks are atmospheric storage tanks built to a modified API 650 basis suited to the produced-water service. (Source: SOW-0231; DBM.)
5. **Source-grounded TBDs.** Where source language is incomplete (Item No. 2, dimensional volume, SG discrepancy), the held items are surfaced rather than invented.

## Considerations

- The package is one of six deliverables under PKG-093 (DEL-093-01 through DEL-093-06). The Scope of Work bounds the contractual envelope; the Package Datasheet (DEL-093-02) carries the interface and design-criteria facts.
- Whole-facility integration: tanks tie into the produced-water transfer pump system (2 x 100%), VRU collection, H2O2 treatment package, drain/containment, and truck-out / pipeline disposition per DBM §Produced-Water Storage. EPC-side interface design draws from the DBM.
- The H2O2 treatment package and the H2O2 storage tank are NOT in PKG-093 (DBM identifies them as separate equipment items in the produced-water system).
- Blanket gas comes from LP fuel gas (utility) per SOW-0231 and DBM. The fuel-gas system origin is 04-25 (per DBM utilities section); this is an EPC-Integrator interface concern.

## Trade-offs

- **Modified API 650 vs full API 650.** Modified API 650 accommodates freezing prevention, blanket-gas provisions, and coating requirements particular to produced-water service. Full code compliance is not claimed. (Source: SOW-0231.)
- **Tank fluid SG basis.** A tank design SG of 1.25 is conservative for produced-water solids loading; pump sizing on SG 1.18 reflects an earlier design basis. Reconciling the two is a detailed-design action item (CT-01).
- **Devchem 253 internal coating.** Chosen to resist produced-water chemistry; coating QA at the vendor shop is a critical hold point for handover.

## Examples / Patterns

- The condensate tank package elsewhere in the facility (11 x 3,800 bbl per DBM) follows a similar 3,800 bbl footprint, but with different service, coating, and skim-system requirements. PKG-093 is structurally similar but explicitly for sweet produced water with the Kennilworth float skim arrangement. (Source: DBM §Condensate Storage; §Produced-Water Storage.)

## Conflict Table (for human ruling)

The following conflicts and held requirements (HRR — Held Requirement / Ruling Required) require disposition by the responsible authority. They are not resolved by this skill.

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-01 | Produced-water tank design SG is 1.25 TBC, while produced-water transfer pump sizing basis is SG 1.18. The DBM itself flags the discrepancy for detailed-design closure. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md §Produced-Water Storage, Treatment, and Transfer (tank SG 1.25 TBC) | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md §Produced-Water Storage (pump SG 1.18) | Datasheet (Conditions); Specification REQ-093-01-09, REQ-093-01-10 | PROPOSAL: Adopt SG 1.25 as the tank design basis; re-rate pump basis to SG 1.25 (or document why 1.18 is acceptable) during detailed design. | TBD |
| CT-02 | SOW-0232 references "Item No. 2" with `TBD` design flow and operating temperature, but provides no tag or capacity. Whether Item No. 2 is a third sweet tank, a separate process-water tank, or a duplicate-numbered item is unresolved. | SCOPE_LEDGER.csv SOW-0232 (Scope notes and open items) | SCOPE_LEDGER.csv SOW-0230 (Basic scope identifies only two tanks: TK-9060-2 and TK-9070-2) | Datasheet (Tagged Equipment List); Specification REQ-093-01-02, REQ-093-01-03 | PROPOSAL: Open 26020-Package_Requirements.docx heading 45 in detailed-design phase to retrieve Item No. 2 definition; if no further definition exists, formally remove Item No. 2 from scope. | TBD |
| CT-03 | SOW-0229 / PACKAGE_REGISTER.csv describe PKG-093 as "Tanks, Water (API 650) 3-25" and SOW-0230 confines the basic scope to sweet produced water. DBM §Produced-Water Storage describes a combined 7-tank system (5 sour + 2 sweet) built to the same modified API 650 basis. Whether the sour produced-water tanks fall under a separate package or are out of project scope at PKG-093 is not stated in the accessible package row. | SCOPE_LEDGER.csv SOW-0230 (PKG-093 sweet-only) | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md §Produced-Water Storage (5 sour + 2 sweet) | Guidance §Principles 3; integration narrative | PROPOSAL: PKG-093 is sweet-only; sour produced-water tanks belong to a different (un-accessed) package row and are not part of this Scope of Work. Confirm with EPC project controls. | TBD |
| CT-04 | SOW-0231 specifies "32 oz test pressure" as the design pressure. The DBM does not separately confirm test vs design pressure for the tanks. | SCOPE_LEDGER.csv SOW-0232 (Design conditions: Pressure: 32 oz test pressure) | DBM §Produced-Water Storage (no explicit design pressure given) | Specification REQ-093-01-09 | PROPOSAL: Use 32 oz as the design pressure basis for the vendor datasheet; confirm with API 2000 venting calc during vendor design. | TBD |
| CT-05 | Item No. 2 design temperature is `TBD` in SOW-0232. Whether it follows Item No. 1 (5 °C operating) or a different service condition is unresolved. | SCOPE_LEDGER.csv SOW-0232 (Operating: Temperature: TBD for Item No. 2) | None (no overriding source) | Datasheet (Conditions); Specification REQ-093-01-09 | PROPOSAL: Hold until Item No. 2 itself is clarified (see CT-02). | TBD |
