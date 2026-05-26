# Guidance — DEL-100-02 Package Datasheet (PKG-100 Hydrogen Peroxide Sweetening Unit)

> Directional rationale, considerations, trade-offs, and the Conflict Table for human ruling.
> Source key: see `Datasheet.md` References.

## Purpose

The Package Datasheet is the **EPC Integrator's technical handoff** to the Package Vendor and to the EPC disciplines that must integrate the H2O2 sweetening unit into the 03-25 facility. It exists so that:

1. The Package Vendor can engineer, design, document, and supply the physical equipment package (per `PKG-REG` responsibility split) without re-interpreting source materials.
2. The EPC Integrator can present the 13 PKG-100 interfaces (`IFC-REG`) as bounded handoffs with clear sides and handoff conditions, anchoring constructability and procurement.
3. The deliverable functions as the Gate 5 anchor that downstream production units (`DEL-100-03` Construction Work Package, `DEL-100-04` Vendor Engineered Equipment Package, `DEL-100-05` Vendor Document Turnover, `DEL-100-06` EPC Vendor Package Review and Acceptance) consume as accepted truth (per `DEL-REG` notes).

## Principles

- **Source-grounded.** Every non-trivial value cites a source slice (`SourcePath` + `SectionRef`) or is marked `TBD`. Decomposition prose does not substitute for source.
- **Interface-evidence intent.** Per the `DEL-REG` note, interface facts are carried in this datasheet as evidence rather than as standalone deliverables. The 13 PKG-100 interface rows (`IFC-REG`) must therefore be expanded with boundary and handoff data inside this deliverable.
- **Responsibility-respecting.** The split between Package Vendor scope (engineering, design, vendor docs, equipment) and EPC Integrator scope (facility integration, interfaces, tie-ins, constructability, procurement coordination) is governance (`PKG-REG`) and is not to be re-shaped here.
- **Surface, do not silently resolve.** Where the source carries `TBC` (e.g., 3,840 m3/d), the datasheet carries `TBC` forward; where the source is binary and not locally text-accessible (PKG-REQ.docx, the RFQ, the Interfaces XLSX), the datasheet flags `location TBD` rather than inventing values.
- **Units consistent with DBM.** m3/d, bbl, °C, m AMSL.

## Considerations

- **H2O2 chemistry hazards.** Hydrogen peroxide service introduces material compatibility, decomposition (oxygen evolution / pressure rise), thermal stability, contamination sensitivity, and emergency dilution considerations. Specific MOC, hazard ratings, and emergency-response provisions are `TBD` until the RFQ / PKG-REQ source slices are accessible.
- **Sour-water service.** Inlet stream is sour produced water (`DBM` line 214); H2S handling and venting routing (Relief / Flare / Vent interface) requires alignment with facility flare/vent basis.
- **Cold-weather operation.** -40 °C design basis (`DBM` SEC-11) makes EHT, building HVAC/services, freeze-protection, and chemical-tank heating non-optional. EHT (`IFC-5CD88768D1`) and Building HVAC / Services (`IFC-56086E492D`) interface rows must be developed with this in mind.
- **Throughput closure.** 3,840 m3/d is carried `TBC` in DBM; the datasheet must not promote this to a hard FACT without source confirmation.
- **Storage tank scope.** `DBM` records one 400 bbl H2O2 tank as part of the 03-25 facility chemical-systems scope. `PKG-REG`'s package scope does not list a tank. Whether the tank is inside the PKG-100 vendor boundary or facility-side is unresolved — see CT-01.

## Trade-offs

- **Datasheet completeness vs. source fidelity.** Filling more fields earlier accelerates vendor RFQ response but risks unsourced values. This deliverable preserves source fidelity (more `TBD`s) over apparent completeness.
- **Vendor freedom vs. EPC constraint.** Tight specification of interface boundaries (battery limits, handoff flanges, electrical/EHT/HVAC supply points) reduces vendor design freedom but improves integration certainty in a 13-interface package.
- **Carrying interface facts here vs. as separate deliverables.** The `DEL-REG` note records the project decision to carry interface facts here as evidence. Trade-off: keeps Gate-5 anchor cohesive but makes this document larger and more change-sensitive.

## Examples

Not derivable from accessible sources — `TBD`. Reference vendor packages for sour-water H2O2 treatment are likely identified in the binary PKG-REQ / RFQ source materials; clause-level examples cannot be quoted here without source access.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted Sections | Proposed Authority (PROPOSAL) | Human Ruling |
|---|---|---|---|---|---|---|
| CT-01 | Whether the 1 × 400 bbl H2O2 storage tank is inside the PKG-100 vendor package boundary or outside (facility chemical-systems scope). | `PKG-REG` row `PKG-100` package scope: lists "Hydrogen Peroxide Pumps; Hydrogen Peroxide Reactors; Static Mixer" only (no tank). | `DBM` `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 216, 428: "one H2O2 treatment package and one 400 bbl H2O2 storage tank"; line 655 lists H2O2 under facility chemical systems. | Datasheet §Equipment Constituents; Datasheet §Conditions (reagent); Specification R-03, R-12; interface rows for Process Piping and Utility Piping. | PROPOSAL: Treat the 400 bbl H2O2 storage tank as **facility-side** (outside the vendor package boundary), supplied to the PKG-100 H2O2 pumps via a Utility Piping interface. Rationale: `PKG-REG` package scope is the governance row; `DBM` describes it as facility chemical-systems. | TBD |
| CT-02 | Throughput value 3,840 m3/d. | `DBM` line 427: "3,840 m3/d TBC". | No other accessible source confirms or refutes. | Datasheet §Attributes; Specification R-05. | PROPOSAL: Carry as `3,840 m3/d (TBC)` until vendor RFQ response or RFQ source text confirms. | TBD |
| CT-03 | Standards basis (ASME B31.3, BPVC, area-classification standards, H2O2-specific codes). | Decomposition prose / convention. | Accessible sources do not enumerate standards for this package. | Specification §Standards; Datasheet §Construction. | PROPOSAL: List as ASSUMPTION pending RFQ / PKG-REQ access; do not derive clause-level requirements. | TBD |
| CT-04 | Per-equipment design pressure, design temperature, materials of construction, driver ratings, electrical area classification per piece of equipment. | None — not in accessible sources. | RFQ / PKG-REQ are binary and not text-accessible to this drafting pass. | Datasheet §Conditions; §Construction; Specification R-04. | PROPOSAL: Mark `TBD` with `location TBD` citation to PKG-REQ heading 52 and RFQ; resolve when source slices are text-extracted. | TBD |
| CT-05 | Whether the Hydrogen Peroxide Sweetening Unit and the Hydrogen Peroxide Treatment Package are the same package (terminology variance). | `PKG-REG`/this deliverable uses "Hydrogen Peroxide Sweetening Unit". | `DBM` lines 40, 216, 427 use "H2O2 treatment package". | Datasheet §Identification; Datasheet §Attributes; Specification §Scope. | PROPOSAL: Treat as the same package; standardize on "Hydrogen Peroxide Sweetening Unit" per governance row `PKG-REG`; record "H2O2 treatment package" as DBM-side synonym. | TBD |
