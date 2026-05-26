# Guidance — DEL-063-04 Vendor Engineered Equipment Package (Tanks, DSO API 650)

## Purpose

DEL-063-04 is the vendor-owned production unit that converts the EPC Scope of Work (DEL-063-01) and the Package Datasheet (DEL-063-02) into a fabricated, supplied, and ready-to-install DSO storage tank package (TK-6770-1). It anchors the physical equipment for PKG-063 and is the upstream of vendor turnover (DEL-063-05) and EPC review/acceptance (DEL-063-06). (`_CONTEXT.md`; package siblings in `1_Working/`.)

## Principles

- **Single-tank vendor scope, mercaptan-treating service.** The package is a single 400 bbl atmospheric DSO storage tank serving the 4-25 NGL Mercaptan Treating Unit (DBM-Deepcut L1530, L1564, L2626). Treat it as one integrated mechanical package with vapour-handling, heating, and truck-out attachments, not as a stand-alone tank-only item.
- **API 650 governs the tank.** The package classification is API 650 (PROJECT_DECOMP PKG-063 title). Vendor engineering decisions defer to API 650 unless the Package Datasheet specifies a modification. The DBM applies "Modified API 650" to condensate tanks (DBM-Deepcut L1646); whether a similar modification applies to the DSO tank is TBD and is a Package Datasheet question.
- **Vapour management is a safety-critical interface.** The blanket gas, incinerator-header connection, and flame arrestor are not optional accessories; they are the integrity boundary between the tank vapour space and the shared incinerator system (DBM-Deepcut L1564, L1570). Treat the flame-arrestor specification and the blanket-gas tie-in as primary design drivers.
- **Heated/insulated service.** DSO is stored heated and insulated (DBM-Deepcut L1564). Heat-loss calculations and trace/heating system reliability under winter conditions should be early vendor work, not late detail.
- **Source fidelity over convention.** Where the DBM is explicit (e.g., "TBC" on design SG, blanket gas, incinerator routing), reflect the source. Do not collapse TBCs into hard requirements without an EPC ruling.

## Considerations

- **Specific gravity 1.75 TBC.** Vendor shell, anchorage, and foundation design loads scale with SG. Carrying SG 1.75 is conservative if actual DSO SG is lower; EPC should close the TBC early so the vendor does not over-design or have to rework (DBM-Deepcut L1564).
- **Alternate C5+ disposal path.** Pumping DSO into C5+ product is a possible disposal path under detailed-engineering review (DBM-Deepcut L528, L1564). If retained, the vendor scope should include the necessary tank nozzle, isolation, and pump interface; if dropped, the nozzle should be omitted to reduce leak paths.
- **Indoor vs outdoor location.** Caustic-containing equipment is indoors (DBM-Deepcut L1552). The DSO tank's location is not explicitly stated in available sources. Whether the DSO tank is co-located with the caustic equipment indoors materially affects insulation, freeze protection, and HAC. TBD.
- **Material selection.** No explicit DSO-tank material constraint was located in available sources; the aluminum prohibition is scoped to the caustic building (DBM-Deepcut L1566). Material selection should consider DSO chemistry, mercaptan/sulphur content, and elevated-temperature service.
- **Gas-detection coverage.** LEL/H2S/methyl mercaptan/fire detection placement is governed at the facility level by a hazards study, not by the tank vendor (DBM-Comp_and_Liquids L838). Vendor should coordinate detector mounting provisions but should not specify quantity/voting logic.
- **Shared incinerator dependency.** The incinerator is physically at 3-25 and serves the 4-25 mercaptan treating system (DBM-Deepcut L1570). Vendor scope ends at the tank's vapour-header tie-in flange; the shared-facility operability responsibility is open (DBM-Deepcut L1572) and is not a vendor decision.

## Trade-offs

- **Roof type (fixed cone vs internal floating, vs IFR).** API 650 permits multiple roof configurations. Fixed cone + blanket is consistent with the DBM (atmospheric, blanketed). An internal floating roof would reduce vapour generation but conflicts with the blanket + incinerator-header strategy. PROPOSAL: fixed cone roof with N2/fuel-gas blanket — confirm in Package Datasheet.
- **Heating method (steam coil vs electric trace vs jacketed bottom).** Steam may not be available; electric heating simplifies utilities but increases area-classification scrutiny; jacketed bottoms add fabrication complexity. TBD pending utility availability statement.
- **Single 400 bbl vs alternative sizing.** The DBM specifies 1 x 400 bbl (L1530). Splitting into two smaller tanks would improve availability but doubles flanged connections to the incinerator header. Recommend retaining 1 x 400 bbl unless EPC overrides.
- **Truck-out frequency vs storage residence.** 400 bbl at expected DSO generation rate sets truck-out frequency; rate data — TBD.

## Examples

Reference equipment patterns from the same DBM:
- **Spent caustic tank (sibling pattern).** Atmospheric, heated, insulated, truck-out capable, incinerator-header connected with backflash protection, fuel-gas blanket (DBM-Deepcut L1562). The DSO tank shares this attribute set (L1564). The vendor may reuse the spent-caustic configuration as a starting point, adjusting for DSO chemistry and SG.
- **Fresh caustic tank (counter-example).** Atmospheric, heated, insulated, truck-in (not truck-out), fuel-gas blanket, **not** tied to VRU header to avoid contamination (DBM-Deepcut L1562). Demonstrates that the vapour-route choice is service-specific.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-01 | Whether the DSO tank is "Modified API 650" or unmodified API 650. DBM applies "Modified API 650" to condensate tanks (L1646); DBM does not state this for DSO tank (L2558/L1564). Decomposition package title is "Tanks, DSO (API 650)". | DBM-Deepcut L1646 (Modified API 650 — condensate) | PROJECT_DECOMP PKG-063 title "API 650"; DBM-Deepcut L2558 / L1564 | Datasheet "Construction"; Specification R-1 | Default to API 650; defer "Modified" qualifier to Package Datasheet DEL-063-02 | TBD |
| CONF-02 | DSO tank location (indoor with caustic equipment vs outdoor). | DBM-Deepcut L1552 (caustic equipment indoors) | No explicit statement for DSO tank | Datasheet "Conditions"; Guidance "Considerations" | EPC ruling required | TBD |
| CONF-03 | Alternate C5+ disposal path inclusion in vendor scope. | DBM-Deepcut L528 (alternate disposal under review) | DBM-Deepcut L1564 (subject to detailed engineering) | Specification R-9; Datasheet Construction | Include nozzle + isolation provision; flag for EPC ruling | TBD |
