# Guidance — DEL-088-02 Package Datasheet (PKG-088 Caustic Treating)

`epistemic-status: DRAFT (Pass 1+2)`

## Purpose

This Package Datasheet is the EPC Integrator's mandatory technical handoff to the third-party caustic-treating package vendor for the 03-25 Liquids Hub. It anchors Gate 5 EPC scope, carries interface evidence in lieu of standalone interface deliverables, and supports the project objectives mapped to PKG-088 (`OBJ-002`..`OBJ-010`, excluding `OBJ-001`). [Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv]

## Principles

1. **Source-grounded.** Every non-trivial value originates from a locally accessible source (the 03-25 DBM); inferences are labeled `ASSUMPTION` and unknowns labeled `TBD`. [Source: skill `four-documents` authority hierarchy]
2. **Boundary clarity.** Vendor owns the package; EPC owns facility-level integration. The datasheet is the artifact that makes the boundary auditable. [Source: PACKAGE_REGISTER.csv PKG-088]
3. **Non-regenerative selection is fixed.** Caustic regeneration is excluded from 03-25 scope. Vendors offering regenerative variants must demonstrate scope-equivalent non-regenerative performance. [Source: DBM §"Condensate Mercaptan Treating"]
4. **Safety-led caustic handling.** Aluminum is prohibited in the caustic building; spent caustic vents only through a flame arrestor to the incinerator header. Material specs default to TBC and require explicit human/vendor ruling, not silent inference. [Source: DBM §"Condensate Mercaptan Treating"]

## Considerations

- **Feed origin.** Feed is stabilized C5+ condensate returned from 04-25 to the 03-25 Liquids Hub. The package sees a stabilized feed, not raw sour condensate. [Source: DBM §Overview]
- **DSO disposition.** DSO is produced continuously; downstream routing for DSO is not stated in the accessible source slice and is `TBD`.
- **Spent caustic logistics.** Spent caustic is trucked out; trucking frequency, contractor, and receiving facility are operational concerns the EPC and operator must close out before commissioning. `TBD` here.
- **Fuel-gas integration.** Caustic treating consumes LP fuel gas for overhead dilution and enrichment-gas service. LP fuel-gas design flow is TBC at the facility level; package loading must be confirmed against facility loading. [Source: DBM §"Fuel Gas"]
- **Mercaptan toxicity / odour.** Methyl mercaptan and related species drive IDLH/odour considerations for purge, analyzer maintenance, and operations planning at the facility level. A formal hazard review is called out by the DBM. [Source: DBM §"Fuel-Gas Sulphur and Purge Hazard Basis"]
- **Vendor reference.** Millenia Proposal 7304 Rev. 0 is identified in PACKAGE_REGISTER.csv as a budgetary pricing/delivery go-by only — it is not a design basis. [Source: PACKAGE_REGISTER.csv PKG-088]

## Trade-offs

| Choice | In-source position | Trade-off |
|---|---|---|
| Non-regenerative vs. regenerative caustic | Fixed as non-regenerative for 03-25 | Lower CAPEX & complexity; ongoing fresh-caustic consumption and spent-caustic disposal logistics |
| Atmospheric 32 oz caustic tanks with LP fuel-gas blanket | DBM-prescribed | Simple atmospheric storage; depends on continuous reliable LP fuel-gas blanket and flame arrestor integrity |
| Truck-out spent caustic | DBM-prescribed | Avoids dedicated pipeline; introduces logistics, regulatory, and surge-storage considerations (sizing TBD) |
| Aluminum prohibition | DBM-prescribed | Constrains building material/coating selection; raises material costs but reduces caustic-corrosion risk |

## Examples

- **Equipment list as authoritative envelope.** The DBM lists "caustic C5+ contactor, pre-heater, caustic outlet filter, water wash, DSO/spent/fresh-caustic/fresh-water tanks, and incinerator overhead/dilution/enrichment-gas interfaces" — this is the minimum equipment-set anchor. [Source: DBM §"Condensate Mercaptan Treating"]
- **Interface envelope.** PKG-088 carries thirteen applicable interface types — using this list as a checklist when reviewing vendor tie-in drawings is the intended use. [Source: PACKAGE_REGISTER.csv PKG-088]

## Conflict Table (for human ruling)

No source/source or source/decomposition conflicts surfaced during Pass 1/2 drafting. Open `TBD` items are tracked in `Datasheet.md` and `Specification.md` rather than as conflicts.
