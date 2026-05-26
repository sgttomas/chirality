# Guidance — DEL-059-01_scope-of-work — Scope of Work (PKG-059 Storage Bullets)

## Purpose

This guidance directs the EPC Integrator in authoring and maintaining the Storage Bullets Scope of Work as the Gate 5 anchor deliverable for PKG-059. The Scope of Work establishes the package identity, function, source basis, responsibility split, and integration narrative that downstream package deliverables (Datasheet, Construction Work Package, Vendor Engineered Equipment Package, Vendor Document Turnover, EPC Vendor Package Review and Acceptance) inherit.

Source: `_CONTEXT.md` Notes ("Mandatory Gate 5 EPC anchor deliverable defined by user instruction"); OBJECTIVE_DELIVERABLE_MAP.csv.

## Principles

1. **Vendor/EPC split is structural, not a negotiating position.** Per PACKAGE_REGISTER row 83 and OBJ-004, the Package Vendor owns engineering/design/documentation/equipment and the EPC Integrator owns integration. The Scope of Work must not assign vendor design work to the EPC Integrator or vice versa.
2. **Source-anchored content only.** Equipment counts, dimensions, design conditions, and service definitions come from `26020-Package_Requirements.docx` package heading 14 (carried via SCOPE_LEDGER SOW-0181..SOW-0184). Spacing rules come from `DBM-Deepcut/4-25_Deepcut_DBM.md` Pressurized Bullet Spacing (citing API 2510).
3. **Decomposition routes; sources determine.** The decomposition register identifies which interfaces apply (10 entries) but does not author the values. Use the registers as routing, not as engineering basis.
4. **Preserve the safety regime.** Sour-service, fire/gas, relief/flare/vent, and environmental constraints (OBJ-009) must remain explicit; do not allow them to disappear into a "by others" clause.

## Considerations

- **Two distinct services in one package.** Unstable condensate bullets and LPG bullets share package identity but have different process services. Vapour equalization, blanket-gas, relief routing, and metering may differ — keep the scope language unambiguous.
- **NGL-storage development item.** `DBM-Deepcut/4-25_Deepcut_DBM.md` section "NGL Storage Bullets" notes that "detailed NGL bullet design parameters are not fully developed in the available product-storage basis and remain a required design-development item." The Scope of Work should reflect this maturity honestly.
- **By-others items are tie-in surface.** Foundations, DCS integration, and electrical supply to MCC are explicitly excluded from the Package Vendor; these are EPC Integrator tie-ins and must appear in INTERFACE_REGISTER for PKG-059 (already preserved at GATE-07).
- **Heuristic-based objective mapping.** Objective associations OBJ-001 and OBJ-003..OBJ-010 are derived from the package-grouping heuristic. Treat as directional until a deliverable-ID-explicit mapping confirms.

## Trade-offs

- **Package as one vs. service-split into condensate vs. LPG.** Source materials treat both as one PKG-059. Splitting would multiply procurement/integration overhead; keeping as one preserves vendor accountability but requires careful service-by-service treatment in the Datasheet and Procedure.
- **Coverage of API 2510 in the SoW vs. Datasheet.** Spacing requirements may be authored at the SoW level (as boundary) or pushed to the Datasheet (as detailed engineering). Current draft keeps them as a requirement (REQ-059-01-14) ASSUMPTION-tagged so the Datasheet can detail them without re-derivation.
- **Listing all 10 interfaces in the SoW vs. by reference.** Listing all 10 makes the SoW self-contained; referencing INTERFACE_REGISTER avoids duplication risk. Current draft lists them explicitly in the Specification with source citation.

## Examples

Example responsibility statement aligned with PACKAGE_REGISTER row 83:

> "The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package for the eighteen pressure vessels comprising PKG-059. The EPC Integrator owns integration of the package into the 04-25 process facility, including interface management for Process Piping, Relief/Flare/Vent, Drain/Containment, EHT, Grounding/Bonding, Area/Exterior Lighting, I&C/Control Cabling, Maintenance Access, Grading/Site Drainage/Spill Containment, and Structural/Foundations/Supports."

(Source basis: PACKAGE_REGISTER row 83 Responsibility column; INTERFACE_REGISTER PKG-059 ten rows.)

## Conflict Table (for human ruling)

No active conflicts identified between Datasheet, Specification, Guidance, and Procedure as drafted in Pass 1/2. The objective association (OBJ-001, OBJ-003..OBJ-010) is recorded as ASSUMPTION rather than CONFLICT because the source registers are consistent and the heuristic resolves the routing.

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| (none) | — | — | — | — | — | — |
