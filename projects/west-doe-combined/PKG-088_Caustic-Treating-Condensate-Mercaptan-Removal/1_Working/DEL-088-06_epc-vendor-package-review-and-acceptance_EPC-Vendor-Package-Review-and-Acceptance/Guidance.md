# Guidance — DEL-088-06 EPC Vendor Package Review and Acceptance

## Purpose

This deliverable exists so that the EPC Integrator records an auditable review and integration acceptance of the PKG-088 Caustic Treating (Condensate Mercaptan Removal) vendor package against the upstream EPC anchor deliverables (SOW, Package Datasheet, Construction Work Package). It provides the evidence basis required to permit handoff into construction completion, commissioning, and operations readiness. [Source: _CONTEXT.md; DELIVERABLE_REGISTER.csv row DEL-088-06]

## Principles

1. **Acceptance is integration-centric.** The EPC Integrator does not re-perform vendor engineering — it confirms that the vendor package, as engineered and documented, integrates with the broader 03-25 facility basis. The DBM is authoritative on the facility-side basis. [Source: 3-25_Comp_and_Liquids_DBM.md]
2. **Source fidelity over convenience.** Acceptance findings are anchored to the EPC Scope of Work, Package Datasheet, Construction Work Package, and the 03-25 DBM. Vendor wording does not redefine the facility basis.
3. **Traceability is mandatory.** Each requirement in DEL-088-06 Specification maps to a vendor document or vendor witness evidence record. Gaps are tracked, not glossed.
4. **TBC and TBD items are surfaced, not silently resolved.** Where the source basis carries TBC (e.g., DSO design value, caustic SG, drain temperature), the acceptance record either confirms the vendor value, records the TBC carry-over, or routes the item to human ruling.
5. **Safety-critical attributes get explicit attention.** Caustic embrittlement potential, methyl mercaptan toxicity, aluminum exclusion in the caustic building, fuel-gas blanketing of atmospheric tanks, and incinerator/flame-arrestor interfaces are each individually evidenced before acceptance.

## Considerations

- **Boundary with DEL-088-05.** The vendor document turnover package is a separate deliverable owned by the Package Vendor. DEL-088-06 reviews it; it does not duplicate the register.
- **Boundary with DEL-088-04.** Vendor engineering content is owned by DEL-088-04. DEL-088-06 records the EPC Integrator's review and acceptance disposition of that engineering content.
- **Boundary with DEL-088-03.** Construction tie-in, installation, and field acceptance scope is governed by DEL-088-03. DEL-088-06 confirms vendor package conformance with those requirements; it does not author them.
- **Interfaces.** The caustic treating package interfaces with: incinerator (overhead/dilution/enrichment gas), LP fuel-gas system (tank blanketing, treating overhead dilution), instrument air (caustic oxidation demand 214 SCFM TBC), produced-water/drain systems, condensate booster/feed pumps, and truck-loading facilities. [Source: 3-25_Comp_and_Liquids_DBM.md §Condensate Mercaptan Treating, §Fuel Gas, §Instrument Air, §Drains]
- **Hazard linkage.** Methyl mercaptan IDLH/LC50 implications govern purge and analyzer practices. Acceptance should confirm vendor MSDS, vent design, and operator-exposure provisions are reviewed. [Source: 3-25_Comp_and_Liquids_DBM.md §Fuel-Gas Sulphur and Purge Hazard Basis]
- **HAZOP linkage.** Caustic drain pressure segregation requires HAZOP review. Acceptance should confirm vendor drain interface is consistent with the HAZOP outcome, or surface the dependency. [Source: 3-25_Comp_and_Liquids_DBM.md §Drains]

## Trade-offs

- **Conditional acceptance vs. hard reject.** Where TBC items (e.g., DSO design value, caustic SG, tank material/coating) remain open at acceptance time, conditional acceptance with documented closure conditions is preferred over either (a) silent acceptance or (b) hard reject that stalls turnover. The condition list must have an owner and a closure deadline. [ASSUMPTION: standard EPC acceptance practice]
- **Punch-list vs. defect.** Cosmetic or non-functional findings belong on a punch list; functional non-conformances against R1-R10 are defects and block unconditional acceptance.
- **Re-FAT vs. integration witness.** Where vendor FAT evidence is incomplete or non-conforming, integration witness at site can sometimes substitute; in other cases re-FAT is required. The choice depends on whether the gap is observable at site under representative conditions.

## Examples

- *Example A: DSO design value.* Source basis 50 ppmw S TBC. Vendor reports guaranteed 50 ppmw S supported by FAT. **Acceptance:** confirm and close the TBC.
- *Example B: Caustic tank coating.* Source basis tank material/coating TBC. Vendor proposes a coating system. **Acceptance:** verify the vendor selection against material compatibility evidence and HAZOP outcome; condition acceptance on confirmation if evidence is incomplete.
- *Example C: Aluminum exclusion.* Vendor BOM lists aluminum guarding inside caustic building. **Acceptance:** reject the item; require substitution. [Source: 3-25_Comp_and_Liquids_DBM.md §Condensate Mercaptan Treating — "Aluminum shall not be used in the caustic building"]

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|

No cross-document conflicts identified at Pass 1/Pass 2.
