# Guidance: DEL-087-02 — PKG-087 Incinerator Package Datasheet

## Purpose

This deliverable is the mandatory EPC Integrator technical handoff document for **PKG-087 Incinerator**. It exists so a third-party package vendor (and EPC discipline engineers integrating around the package) can engineer, design, and procure the single-train incinerator package (stack `FL-6920-1`, KO drum `V-6900-1`, transfer pump `P-6900-1`, blower `B-6920-1`) on a single, source-grounded basis. It is the Gate 5 EPC anchor deliverable for this package and intentionally carries interface evidence rather than deferring it to standalone interface deliverables (`_CONTEXT.md` Notes).

## Principles

1. **Source authority over convention.** Every non-trivial datasheet value traces to `26020-Package_Requirements.docx` heading 40 (primary) or `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (cross-facility allocation and caustic interfaces). Generic incinerator-design conventions (e.g., NFPA 86, API 537 / 521, typical destruction efficiency targets) are not substitutes for cited basis.
2. **Two scopes, one document.** Package Vendor scope and EPC Integrator scope are both visible in the datasheet but never merged. The vendor owns package engineering, design, vendor documentation, and the physical equipment package. EPC owns DCS integration, foundations, electrical supply to MCC, and facility-level integration (heading 40 Scope Notes "By others"; PACKAGE_REGISTER.csv row PKG-087).
3. **Mark unknowns; do not invent.** Items that depend on the inaccessible RFQ `Bid Docs/Budgetary/26020-01-PT-RFQ-25-003_Incinerator.docx`, on the source "Appendix A" fluid table, on the referenced PFD, or on unread xlsx interface rows are marked `TBD` or `location TBD`. Sour-service metallurgy is not asserted because the source slice does not state composition for this package.
4. **Shared-interface honesty.** DBM is explicit that the incinerator is a shared-interface system under 03-25 / 04-25 allocation and that the exact service split is an open item. The datasheet surfaces this; it does not close the allocation.
5. **Interface evidence is first-class.** Interface types in PACKAGE_REGISTER.csv row PKG-087 and the heading 40 Physical Interface Summary are carried verbatim. Discrepancies between the two are surfaced in the Conflict Table, not silently reconciled.

## Considerations

- **Process function.** The incinerator destroys vapours from the spent caustic storage tank (vented through a flame arrestor, per DBM) and the caustic regeneration column overheads (heading 40 Basic Scope). The KO drum sits upstream to remove entrained liquids; the transfer pump removes liquid bottoms.
- **Stack relief capacity.** The stack is sized to handle the maximum relief rate from the tank farm and the VRU "with less" (source phrase is incomplete in the accessible slice). Verification of the stack's relief load coverage requires the relief and flare deliverables (PRO-014/-015/-017/-018) listed in heading 40 and is not a datasheet-resolvable item.
- **Motor starting.** B-6920-1 is exactly at the 100 hp threshold for the VFD-or-soft-start requirement (heading 40). The datasheet states the requirement; the choice between VFD and soft start is detailed-design.
- **EPC-by-others items.** DCS integration, foundations, and MCC electrical supply are explicitly EPC scope. Construction work package (DEL-087-03) and EPC review/acceptance (DEL-087-06) carry the execution detail; this datasheet only records the boundary.
- **Cross-package coupling.** Caustic treating package (PKG-098 / `26020-02-PT-27-001 — Caustic Treating (Condensate Mercaptan Removal)`) is the principal upstream vapour source. The 03-25 caustic mercaptan treating package carries "incinerator overhead / dilution / enrichment-gas interfaces" (DBM caustic treating section).
- **Self-framing building.** The package includes a self-framing building erected at site (heading 40 Major Included Equipment). Foundations under that building remain EPC scope.

## Trade-offs

- **Single-train vs. installed spare.** Source identifies single quantities for all major equipment. No installed spare is shown; the operational consequence (outage equals loss of incinerator service) is implicit, not stated as a design intent. The datasheet records this as ASSUMPTION pending the RFQ slice.
- **Preliminary vs. final flow basis.** The 0.6 MMSCFD (17 E3M3D) figure is labelled "preliminary design flow" in the source. Final allocation depends on flare/relief and emissions studies the source defers (heading 40 Vendor Engineering Deliverables: PRO-014, PRO-015, PRO-017, PRO-018; DBM Emissions section explicitly not permit-final).
- **VFD vs. soft start for B-6920-1.** Source requires "VFD or soft start" for >= 100 hp motors. VFD adds harmonic and reactive-power considerations on the upstream MCC; soft start is simpler but provides less starting-current and process-control flexibility. Datasheet does not adjudicate.

## Examples

The accessible source slice does not contain worked examples (calculation walk-throughs, P&ID excerpts, or data-sheet templates) that can be transcribed verbatim. The decomposition row for PKG-080 (Inlet Compressors Package Datasheet) is a structural precedent for this deliverable's shape but is not normative content.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-01 | Building HVAC / Services applicability disagrees between registers | `PACKAGE_REGISTER.csv` row PKG-087, Applicable Interface Types (lists Building HVAC / Services as Yes) | `26020-Package_Requirements.docx` heading 40, Physical Interface Summary (records Building HVAC / Services as No) | Datasheet "Applicable Interface Types"; Specification R8 | PROPOSAL: prefer source (heading 40) for package interior; PACKAGE_REGISTER.csv Yes interpreted as facility-wide HVAC integration around the self-framing building | TBD |
| C-02 | Stack relief capacity wording is incomplete in source ("with less") | `26020-Package_Requirements.docx` heading 40, Major Included Equipment (FL-6920-1) | (no Source B) | Datasheet Conditions row "Capacity of stack vs. tank-farm/VRU max relief rate" | PROPOSAL: carry the source phrase verbatim and resolve via heading 40 deliverables PRO-014/-015/-017/-018 | TBD |
| C-03 | Spare philosophy is inferred, not stated | `26020-Package_Requirements.docx` heading 40 (single quantities) | (no Source B) | Datasheet Attributes row "Spare philosophy" | PROPOSAL: keep "Single-train; no installed spare" as ASSUMPTION until RFQ slice is accessible | TBD |
| C-04 | Incinerator service split is an open allocation item | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Exclusions / Emissions / Inter-facility Interfaces) | `26020-Package_Requirements.docx` heading 40 (process function statement) | Datasheet "Facility allocation context" | PROPOSAL: surface as open interface item; do not close in this datasheet | TBD |
