# Guidance — DEL-095-02 Package Datasheet

Authority: directional. Captures rationale, considerations, and trade-offs used when populating the package datasheet, and surfaces conflicts requiring human ruling (HRR).

## Purpose

The Package Datasheet for `PKG-095` exists so that a third-party Package Vendor (or another discipline performing the package engineering) can engineer and design the slop storage tank package against a stable, source-supported EPC handoff. It carries:

- the EPC Integrator's facility-side basis,
- the interface envelope the vendor must respect,
- and the documentation expectations for turnover.

It is the Gate 5 EPC anchor for this package: per `_CONTEXT.md`, interface facts are deliberately carried here as evidence rather than as standalone deliverables.

## Principles

1. **Source authority over convention.** Tank attributes are recorded only when the source (DBM 3-25 or package requirements) supports them. Where the source is silent for the slop tank specifically, the datasheet marks `TBD` rather than copying from the produced-water or sour-condensate tank rows.
2. **Single artifact, multi-purpose handoff.** The datasheet doubles as (a) tank technical datasheet, (b) vendor handoff basis, and (c) interface requirements matrix. Avoid splitting into separate deliverables; this is intentional per `_CONTEXT.md` Notes.
3. **API 650 family alignment.** The slop tank shares the API 650 Modified atmospheric family used elsewhere on the facility. Where the slop-specific basis is silent, family analogs become ASSUMPTIONs surfaced for confirmation in detailed design, never silent adoptions.
4. **Battery-limit clarity.** The EPC Integrator owns facility-level integration; the Package Vendor owns package engineering, design, vendor documentation, and the physical equipment package (PACKAGE_REGISTER row `PKG-095`). The datasheet should make this split unambiguous on every interface row.

## Considerations

- **Capacity confirmation:** DBM 3-25 line 406 implies the slop tank is one of the eleven 3,800 bbl tanks but states the allocation can be "superseded by final tank register." Treat 3,800 bbl as a directional planning capacity (ASSUMPTION) and require confirmation.
- **Truck-out and segregation:** The slop tank is a sink for KO drum pumps and scrubber liquid drains. The datasheet should reflect truck-out access, segregation from on-spec product tanks, and any required drainage / containment provisions per the Drain / Containment and Grading interfaces (`IFC-0589336378`, `IFC-A01689FD3F`).
- **Vapor handling:** No explicit vapor-recovery / blanket-gas requirement is stated for the slop tank in the accessible source slices. Apply VRU vs. flare disposition during detailed design; do not infer from the caustic or produced-water tank basis without ruling.
- **Major equipment tag:** ARTIFACT_REGISTER `ART-340A371C42` marks the tank tag as "likely TK-9130-2." Use this tag as a placeholder; confirm against the final tag register.

## Trade-offs

- **Combining interface evidence into the datasheet** (current choice) vs. issuing a separate interface deliverable: combining keeps the vendor handoff coherent and traceable but creates a denser datasheet. The decomposition selected combining; honor it.
- **API 650 vs. API 650 Modified:** API 650 Modified atmospheric is the family basis for adjacent tanks (DBM line 421). Selecting "Modified" early aligns construction with companion tanks; selecting plain API 650 may simplify vendor procurement. The accessible source basis does not adjudicate; surface as Conflict C-001 below.
- **Internal coating selection:** Devchem 253 is named for the produced-water family (DBM line 421). Adopting it on slop simplifies inventory and coating qualification; selecting a hydrocarbon-service-appropriate coating may be more correct for slop service. Insufficient source support — leave TBD.

## Examples

(Examples beyond what is in the Datasheet would require source slices not currently accessible. Mark TBD.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-001 | API 650 vs. API 650 Modified atmospheric basis | Package name "Tanks, Slop (API 650)" (PACKAGE_REGISTER `PKG-095`) | DBM 3-25 line 421 — adjacent tank family is "API-650 Modified atmospheric" | Datasheet Attributes/Construction; Specification R3.1 / R3.2 | PROPOSAL: API 650 Modified atmospheric to align with the rest of the facility tank family | TBD |
| C-002 | Slop tank capacity not separately specified | DBM 3-25 line 406 ("one slop tank" in the eleven 3,800 bbl set; "unless superseded by final tank register") | No source confirms 3,800 bbl for slop specifically | Datasheet Attributes (Nominal Capacity); Specification R3.4 | PROPOSAL: carry 3,800 bbl as planning basis (ASSUMPTION), confirm against final tank register | TBD |
| C-003 | Internal coating / insulation / heating for slop tank | DBM 3-25 line 421 specifies Devchem 253 internal coating + external insulation/heating for produced-water tanks | No source statement for slop tank | Datasheet Attributes/Construction; Specification R3.5 | PROPOSAL: defer to detailed design / package vendor proposal; do not adopt the produced-water family selection by default | TBD |
| C-004 | Major equipment tag (`TK-9130-2`) is "likely" not confirmed | ARTIFACT_REGISTER `ART-340A371C42` records "likely TK-9130-2"; DBM 3-25 line 463 references slop `TK-9130-2` in drain routing | No final tag register accessible | Datasheet Identification; Specification R1.2 | PROPOSAL: use `TK-9130-2` as placeholder with ASSUMPTION label; replace with final tag register value | TBD |
| C-005 | Vapor disposition (LP fuel-gas blanket vs. VRU vs. flare) for slop tank | DBM 3-25 line 402 specifies LP fuel-gas blanket for caustic tanks; nothing explicit for slop | Vapor disposition for slop is not in the accessible slices | Datasheet Attributes (Vapor Service); Specification (would extend R3) | PROPOSAL: leave TBD; require explicit ruling during detailed design before vendor handoff | TBD |
