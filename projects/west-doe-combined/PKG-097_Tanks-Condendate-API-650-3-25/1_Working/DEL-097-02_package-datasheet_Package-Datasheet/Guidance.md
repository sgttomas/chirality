# Guidance — Package Datasheet (DEL-097-02)

Deliverable: `DEL-097-02_package-datasheet`
Package: `PKG-097` — Tanks, Condensate (API 650) 3-25 (`26020-03-PT-19-006`)

## Purpose

The Package Datasheet is the EPC Integrator's authoritative technical handoff to the third-party tank package vendor. It consolidates source-grounded equipment identification, design conditions, code basis, fittings/coatings, package boundary, and the physical interface matrix into a single artifact suitable for RFQ issue and subsequent vendor engineering. It supports OBJ-002 through OBJ-010 by establishing the data needed for vendor selection, fabrication, integration, and turnover within the 3-25 Liquids Hub tank farm.

## Principles

- **Source fidelity.** Every non-trivial datasheet value traces to a named source slice (Word §49, Workbook row 88, DBM section). Inferences are labeled ASSUMPTION; missing values are labeled TBD. (Authority: SKILL — Source-grounded drafting.)
- **EPC vs. Package Vendor scope.** EPC Integrator owns facility-level integration; the Package Vendor owns package engineering, design, vendor documentation, and the physical equipment package. The datasheet is the boundary artifact. (PACKAGE_REGISTER row PKG-097.)
- **Interface facts are evidence.** Per `_CONTEXT.md` Notes, interface facts are carried within this datasheet rather than spun out as standalone deliverables.
- **Stable interfaces over speculative completeness.** Where the source is silent, prefer TBD and route to vendor RFQ/clarification rather than invent a value.

## Considerations

- **Service description.** §49 names "C5+ Condensate Storage Tanks" but does not enumerate per-tank routing (sour vs. product vs. recycle). The 3-25 DBM frames the hub-level inventory of eleven 3,800 bbl condensate tanks total; PKG-097 covers four of them, and the per-tank service mapping is an open item.
- **Winter operation.** §49 states "a recycle may be required to maintain a certain temperature during winter." Site minimum ambient is −40 °C (DBM). Recycle source, pump basis, and temperature setpoint are not specified in §49 and should be clarified during vendor engineering.
- **Relief design.** Each tank carries both a PVRV (vacuum / modulating pressure relief) and an EPRV (single worst-case relief). Coordination with the VRU header (which receives the modulating vapour flow) and with the blanket-gas API 2000 sizing is required so the three devices act in the correct sequence.
- **Coating.** Devchem 253 is specified for floor, walls, and roof — same coating system also used in the 3-25 inlet separator internals (DBM line 256), implying consistency with the upstream sour-service experience.
- **By-Others scope.** Foundations, on-site mounting, electrical/instrumentation field installation, and platforms/staircases are excluded from the vendor package. These belong to EPC civil / electrical / structural disciplines and create interface points captured in the Physical Interface Matrix.
- **Capacity reconciliation.** §49 Scope Notes give a package capacity of 94,940 kg/h and 3,187 Am³/d at preliminary design conditions; the DBM gives a Liquids Hub C5+ condensate total of 3,180 m³/d ≈ 20,000 bbl/d. The §49 figure is at the package boundary in preliminary design; the DBM figure is hub-level. They are not in conflict but operate at different system boundaries.

## Trade-offs

- **Recycle vs. heating.** §49 leaves "recycle may be required" open. A continuous winter recycle uses pump energy and complicates inventory accounting; tank/jacket heating would add capex and EHT interface scope (currently "No" in the interface matrix). The datasheet preserves the recycle direction; the trade study itself is vendor / process-engineering work.
- **Modulating (PVRV) vs. emergency (EPRV) split.** Splitting relief into a modulating device routed to VRU and an emergency device sized for worst-case avoids over-flaring during routine breathing but adds two devices per tank. §49 prescribes this split; the datasheet should not collapse it.
- **Coating standardization.** Devchem 253 across walls/floor/roof simplifies procurement and inspection at the cost of optimizing per-surface. Source mandates the single coating; document accordingly.

## Examples

- Operating / design conditions block per §49 Scope Notes, exactly as cited in the Datasheet.
- Physical interface matrix rendered verbatim from §49 Physical Interface Summary table.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-01 | Package name spelling — "Condendate" vs "Condensate". | DELIVERABLE_REGISTER.csv (PKG-097 row); PROJECT_DECOMP folder name | 26020-Package_Requirements.docx §49 (H1) — "Condensate"; DBM `3-25_Comp_and_Liquids_DBM.md` — "Condensate" | Datasheet Identification, Specification Scope, Guidance Purpose | Authoritative source: "Condensate". Project register spelling is cosmetic and traceable via tag `26020-03-PT-19-006`. | TBD |
| C-02 | Per-tank service routing (sour / product / recycle / slop). | 26020-Package_Requirements.docx §49 — only states "C5+ Condensate Storage" generally | 3-25_Comp_and_Liquids_DBM.md §"Liquids Hub" / §"Condensate Mercaptan Treating" — describes sour vs. product vs. slop categories at hub level (across 11 tanks) | Datasheet Attributes, Specification R-18 | Resolve via RFQ / DBM mapping table. Pending: identify which of the four PKG-097 tanks are product, sour, slop, or recycle service. | TBD |
| C-03 | Materials of construction (shell/roof/floor) and roof type. | 26020-Package_Requirements.docx §49 — silent | Bid Docs/Budgetary/26020-03-PT-RFQ-19-006 — Conde Tanks.docx — cited as Source Basis but not locally accessible | Datasheet Construction, Specification R-17 | Read RFQ source slice and update; until then mark TBD; ensure MOC complies with API 650 modified for −40 °C MDMT. | TBD |
| C-04 | Capacity basis frame. §49 package throughput (94,940 kg/h; 3,187 Am³/d preliminary) vs. DBM hub throughput (3,180 m³/d ≈ 20,000 bbl/d total). | 26020-Package_Requirements.docx §49 Scope Notes | 3-25_Comp_and_Liquids_DBM.md §"Liquids Hub" / §"Condensate and Produced-Water Receipts" | Datasheet Conditions, Guidance Considerations | Not a true conflict: §49 = preliminary package boundary; DBM = hub-level. Carry both with explicit framing. | TBD |
| C-05 | Winter recycle requirement is permissive ("may be required") with no source-stated setpoint, recycle source, or pump basis. | 26020-Package_Requirements.docx §49 Major Included Equipment | (no other source identifies setpoint or basis) | Datasheet Attributes (insulation row), Specification R-03, Procedure prerequisites | Confirm winter operating philosophy during vendor engineering kickoff; capture decision in Datasheet revision before RFQ award. | TBD |
