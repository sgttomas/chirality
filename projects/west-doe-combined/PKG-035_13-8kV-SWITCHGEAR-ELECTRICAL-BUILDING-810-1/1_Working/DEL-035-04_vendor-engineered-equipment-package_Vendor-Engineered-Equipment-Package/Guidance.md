# Guidance: DEL-035-04 — Vendor Engineered Equipment Package

## Purpose

This deliverable exists so the Package Vendor can deliver an engineered, fabricated, shop-built modular electrical building that houses the West Doe Deepcut plant's main 13.8 kV switchgear. The vendor's engineered package converts the EPC Scope of Work (`DEL-035-01`) and EPC Package Datasheet (`DEL-035-02`) into a complete physical equipment package and the vendor engineering/design records that support it. The EPC Integrator retains facility integration and acceptance.

## Principles

- **Vendor owns the package; EPC Integrator owns the facility integration.** Treat PKG-035 ownership splits in the package register as authoritative when allocating responsibility (`PACKAGE_REGISTER.csv` PKG-035).
- **DBM governs the role.** 810-1 is the plant main power distribution center; its bus must be sized for the full facility scope (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`).
- **Shop-build the building.** The Deepcut electrical building basis is prefabricated, modular, elevated on piles, with bottom cable entry, n+1 HVAC, and standard grounding and wiring practices. Vendor design should not diverge from these without EPC ruling.
- **Interfaces precede internals.** Lock the PKG-035 interface types early (Electrical Power, Grounding, I&C, Communications, HVAC, F&G, Lighting, Maintenance Access, Structural, Drainage, Utility Piping) so EPC integration can advance in parallel.

## Considerations

- The exact 13.8 kV switchgear ratings (short-circuit, BIL, continuous current, arc-flash class) come from the EPC Package Datasheet (`DEL-035-02`), not from this deliverable. Until the datasheet is accepted, those values stay `TBD`.
- The "Medium Voltage Switchgear" quantity 1 and "Low Voltage Switchgear" quantity 2 in the DBM QAS list are facility-level entries; allocation to PKG-035 specifically is not asserted in the source. Vendor should confirm allocation with EPC before procurement.
- Source `26020-Package_Requirements.docx` is referenced for project-wide package requirements but is a binary docx not parsed in P1/P2. Vendor and reviewer should reconcile its content in a later pass.
- OGAOM Sec. 9.6.15 is cited by the DBM for the 25 m fired-heater separation. The OGAOM text itself is not in the local source set; treat the DBM citation as authoritative reference and confirm OGAOM revision in detailed design.

## Trade-offs

- **Shop-built modular vs. site-built.** DBM directs shop build; deviating would shift schedule risk to construction and complicate integration. Recommend staying with shop build unless ruled otherwise.
- **Single vs. multiple 13.8 kV lineups.** DBM frames a single plant main switchgear sized for the full facility. Splitting would change the facility one-line and is out of scope for vendor design without EPC ruling.

## Examples

- DBM-defined radial distribution: 810-1 main → step-down transformers → 820-1, 830-1, 840-1, 850-1, 860-1 buildings. The vendor's feeder schedule must align with this list (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`).
- DBM-defined building utilities (HVAC n+1, bottom cable entry, ground-grid two-point connection) are concrete examples of constraints the vendor design must satisfy.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-035-04-001 | Detailed 13.8 kV switchgear ratings (short-circuit, BIL, Ic, arc-flash) are not stated in DBM and the EPC Package Datasheet (`DEL-035-02`) is not yet accepted. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Medium-voltage services — voltage/grounding only) | `DELIVERABLE_REGISTER.csv` row DEL-035-02 (handoff basis, content pending) | Datasheet "Conditions"; Specification R-035-04-012 | Hold detailed ratings as `TBD` until DEL-035-02 acceptance; then propagate as the binding rating set. | TBD |
| HRR-035-04-002 | DBM QAS lists "Medium Voltage Switchgear" qty 1 and "Low Voltage Switchgear" qty 2 at facility level but does not allocate quantities to PKG-035 specifically. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (QAS list) | `PACKAGE_REGISTER.csv` PKG-035 (no quantity field) | Datasheet "Attributes" | Do not assume PKG-035 receives any specific count; vendor and EPC confirm allocation before procurement. | TBD |
| HRR-035-04-003 | `_Sources/26020-Package_Requirements.docx` may impose vendor obligations (formats, FAT, documentation) not visible to this pass because the docx is unparsed. | `_Sources/26020-Package_Requirements.docx` (binary, unread) | This Specification (R-035-04-010, R-035-04-011) | Specification "Standards" and "Documentation" | Parse the docx in a follow-up TASK and reconcile vendor obligations before vendor PO release. | TBD |
| HRR-035-04-004 | OGAOM Sec. 9.6.15 is cited via DBM but the OGAOM revision/text is not in the local source set. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (citation only) | OGAOM (not in local sources) | Specification R-035-04-009 | Confirm OGAOM revision in detailed design; current 25 m value is taken from DBM citation. | TBD |
