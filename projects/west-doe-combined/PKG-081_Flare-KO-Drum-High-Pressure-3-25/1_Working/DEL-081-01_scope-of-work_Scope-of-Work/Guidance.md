# Guidance: DEL-081-01 — Scope of Work (PKG-081 Flare KO Drum (High Pressure) 3-25)

> Directional guidance for EPC Integrator authors producing the Scope of Work for PKG-081. This is not a normative specification (see `Specification.md`) and not an operational procedure (see `Procedure.md`).

## Purpose

The Scope of Work for PKG-081 exists to give the EPC project the authoritative, source-grounded description of what the Flare KO Drum (High Pressure) 3-25 package is, what it does inside the facility, where its boundaries lie, who is responsible for which part, and which open items must be ruled on before procurement and construction commit. It is the Gate-5 EPC anchor deliverable that the Package Datasheet (`DEL-081-02`), Construction Work Package (`DEL-081-03`), and downstream vendor production unit (`DEL-081-04`) all draw from.

Source: `_CONTEXT.md` Scope and Notes; `DELIVERABLE_REGISTER.csv` row.

## Principles

1. **Source primacy.** Substantive scope statements must be drawn from accessible source materials (Gate-7 registers and `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`). Where the registers point to inaccessible artifacts (`26020-Package_Requirements.docx` clause text, `W242510-PRC-REP-000003-001`), record `location TBD` rather than reconstructing values from prose.
2. **EPC-level abstraction.** The Scope of Work is an integration-and-responsibility document, not a vendor datasheet. Resist pulling per-vessel mechanical design values (pressures, dimensions, materials, sparing curves) into this artifact; route those to `DEL-081-02_package-datasheet`.
3. **Responsibility-first framing.** PKG-081 is a vendor-owned package with EPC integration; the Scope of Work must make that split visible and unambiguous, including which interfaces remain EPC-side at the skid edge.
4. **Interface completeness.** The 10 active facility-level interfaces in `INTERFACE_REGISTER.csv` for PKG-081 are an EPC integration checklist. Each interface should be acknowledged even when its detailed routing is `TBD`.
5. **Shared-system honesty.** The HP/Cryo and LP dual flare stack and the slop / drain destinations are shared between 03-25 and 04-25. The Scope of Work must flag the shared-interface allocation as an open coordination item, not a closed boundary.
6. **Open items are first-class.** SOW-0074 records an explicit scope conflict (flare system technically described vs. excluded in DBM scope table). The Scope of Work must surface it; it must not silently resolve it.

## Considerations

- **Decomposition uses package-grouped objective mapping.** Objectives `OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010` are associated to all PKG-081 deliverables via the package-heuristic, not by deliverable-specific evidence. Label the association `ASSUMPTION (PACKAGE_HEURISTIC)`.
- **Sour-service classification.** DBM SEC-07 and SEC-09 treat HP flare relief as sour hydrocarbon service. Isolation, drain, vent, and inspection provisions in the Scope of Work should reflect sour-service constraints even though per-vessel mechanical design lives in the Package Datasheet.
- **Header sizing context.** The DBM cites a current HP relief header size of 508 mm / 20 inch. This is a facility-side basis, not a package-internal nozzle requirement; the Scope of Work can cite it for interface framing only.
- **Truck-out provision.** P-4100-2 / P-4150-2 transfer to slop with a truck-out provision (DBM SEC-07). The Scope of Work should retain truck-out as a package feature because it carries facility-side logistics implications (access, road, containment) that fall on the EPC scope.
- **Avoid scope creep into LP flare KO drum.** V-3900-2 / P-3900-2 are LP flare KO equipment per DBM SEC-07; they are not part of PKG-081 and must not be drawn into this Scope of Work.

## Trade-offs

| Trade-off | Discussion |
|---|---|
| Detail vs. abstraction | More tagged-equipment and interface detail aids EPC integration planning, but per-vessel design values belong in `DEL-081-02_package-datasheet`. Draw the line at "what the EPC needs to integrate" vs. "what the vendor needs to design". |
| Source completeness vs. publication readiness | Several anchors (`26020-Package_Requirements.docx` heading 34, `W242510-PRC-REP-000003-001`) are not locally extracted. Issuing the Scope of Work with explicit `location TBD` is preferable to deferring publication or to inventing clause text. |
| Carrying interface enumeration vs. interface design | The Scope of Work should enumerate interface types (a checklist) but should not author interface design content; the EPC interface fact artifacts and the Package Datasheet carry that load. |
| Surface conflict vs. resolve conflict | SOW-0074 conflict (flare equipment in/out boundary) is a human-ruling item. The Scope of Work should record it, not preempt it. |

## Examples

- Cross-document reuse: the four tagged equipment items (V-4100-2, V-4150-2, P-4100-2, P-4150-2) appear identically in `Datasheet.md` and `Specification.md` REQ-SOW-02 to keep terminology consistent.
- Interface checklist style: the Scope of Work narrative should restate the 10 interface types from `INTERFACE_REGISTER.csv` PKG-081 rows verbatim so that downstream interface tracking can be done by exact-string search.
- Responsibility wording: reuse the `PACKAGE_REGISTER.csv` description text ("Package Vendor owns ... EPC Integrator owns integration into the functional process facility ...") so audit traces back to a single authoritative phrasing.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-081-01-A | SOW-0074 records that flare-system equipment is technically described but listed as excluded in the DBM scope table. Final in/out boundary requires owner/engineering ruling. | `SCOPE_LEDGER.csv` SOW-0074 | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-01 Exclusions table (no flare KO drum exclusion line found in accessible text) and SEC-07 HP flare basis (technical description present) | Specification REQ-SOW-04, REQ-SOW-07; Datasheet "Tagged Major Equipment"; Guidance Principles | Treat flare-system technical description as IN scope for PKG-081 pending owner ruling; carry exclusion language only as a flag, not as a removal. | TBD |
| CONF-081-01-B | Shared HP/Cryo and LP dual flare stack and incinerator service split between 03-25 and 04-25 is unresolved. | DBM SEC-01 Shared Interface Notes | DBM SEC-07 HP flare basis | Specification REQ-SOW-08; Datasheet Construction row "EPC scope (this deliverable)" | EPC Scope of Work should describe the package as terminating at the HP flare header tie-in, leaving stack-side allocation to the shared-flare interface owner. | TBD |
| CONF-081-01-C | Clause-level requirements from `26020-Package_Requirements.docx` package heading 34 are referenced by every PKG-081 register row but the docx is not converted to markdown in the workspace. | `_REFERENCES.md`; `_Sources/26020-Package_Requirements.docx` (binary) | DBM SEC-07 (partial overlap only) | Specification REQ-SOW-09; Datasheet References | Mark clause-level requirements `location TBD` until the docx is extracted; do not reconstruct from register summaries. | TBD |
| CONF-081-01-D | External `W242510-PRC-REP-000003-001` Plant Shutdown and Blowdown Philosophy governs final blowdown sequencing but is not in the workspace. | DBM SEC-07 closing paragraph | (no second accessible source) | Specification REQ-SOW-09 | Cite the document by number and mark sequencing `location TBD`; do not invent staggered-blowdown rules. | TBD |
