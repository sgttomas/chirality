# Guidance — DEL-065-02 Package Datasheet (PKG-065 Tanks, Caustic (API 650) 4-25)

## Purpose

The Package Datasheet exists so that a third-party vendor or a discipline package engineer can engineer, procure, and integrate the caustic tank package without having to re-derive the EPC's facility-level basis. It is the *single technical handoff surface* for the package. Per `_CONTEXT.md`, interface facts are intentionally carried in this deliverable as evidence rather than as separate deliverables.

## Principles

- **Source-faithful, not source-substituting.** Values, codes, and constraints in the datasheet must trace to project basis (DBM, package requirements document, interface export). Where the underlying text is not locally accessible (the binary `.docx` and `.xlsx`), entries are marked `location TBD` rather than invented.
- **Caustic service drives almost every non-trivial choice.** Heating, indoor location, material selection, prohibited materials (aluminum), insulation cladding (stainless), vapour-space management, and safety shower placement all stem from the corrosivity, freeze/crystallization, and personnel-exposure profile of NaOH service.
- **Vapour-space discipline is asymmetric.** Fresh and spent caustic tanks share fuel-gas blanketing, but the spent tank vents to the incinerator (with backflash protection) and the fresh tank is explicitly excluded from the VRU header. Treat these as hard rules, not preferences.
- **TBD over guess.** Where the DBM marks a value TBC, the datasheet preserves that status. Detailed engineering will close out remaining TBDs (tank MoC selection, building floor material, safety shower count, PVRV/EPRV sizing).

## Considerations

- **Code governance for caustic tanks.** The package title names API 650, but caustic service often pulls in additional standards (e.g., supplementary requirements for chemical service, lining/coating specifications, and supplier-specific polymer tank standards if a non-steel construction is selected). Material selection (polymer vs. coated steel) materially affects which code is operative. (Source: DBM line 1566 leaves MoC open; API 650 named in package title; cross-confirmation in `26020-Package_Requirements.docx` heading 20 is `location TBD`.)
- **Indoor installation drives plot, HVAC, and detection.** Because caustic-containing equipment is installed indoors (DBM line 1552), atmospheric separation tables (R8) interact with building placement, not bare tank-to-tank distance in open air. Vendor and EPC must agree on whether NFPA / OGAOM separations apply at building envelope or at vent/discharge points.
- **Safety shower coverage is a control-room-integrated function.** Activation must raise a discrete control-room alert (DBM line 1552). Treat this as an instrumented safety function for design purposes (count, location, alarm path) even if final SIL classification is deferred.
- **Truck handling is a real interface, not a footnote.** Both tanks have a trucking interface (truck-in fresh, truck-out spent). Address loading/unloading area, secondary containment, hose connections, station electrical classification, and operator procedures during package handoff.
- **Specific gravity drives nozzle elevations, structural support, and pump NPSH.** Fresh caustic at SG 1.75 (TBC) is a high-density service; nozzle, support, and downstream pump selection should be sized against the design SG rather than water-equivalent.

## Trade-offs

- **Polymer tanks vs. lined steel.** Polymer tanks tolerate concentrated caustic and avoid coating maintenance but constrain heating method, nozzle loads, fire exposure, and fitting choices. Lined steel preserves API 650 compliance familiarity but introduces coating selection (and the `Devchem 253` pattern noted for produced-water tanks in DBM line 524 is not directly transferable to caustic). Source: DBM line 1566 leaves the selection open.
- **VRU exclusion vs. fugitive control.** Excluding the fresh caustic tank from the VRU (to avoid VRU-vapour contamination of fresh caustic) means relying on fuel-gas blanketing alone for vapour control. The trade-off is accepted in the basis. (Source: DBM line 1562.)
- **Incinerator routing for spent caustic.** Routing spent caustic vapours to the incinerator header (vs. flare/VRU) requires flame arrestor backflash protection and tight blanket-gas control. The trade-off favours destruction of odorous/sulphur species at the cost of a more demanding tie-in. (Source: DBM line 1562.)
- **Indoor segregation vs. plot economy.** Indoor placement of caustic tanks consumes building footprint and HVAC capacity but eliminates freezing/crystallization risk and concentrates spill/exposure containment. The basis accepts this. (Source: DBM line 1552.)

## Examples

- **Example tank entry (illustrative form only).** A vendor datasheet row for the spent caustic tank would carry: Tag TBD; Service "Spent NaOH from NGL mercaptan treating"; Nominal capacity 400 bbl; Design SG TBD; Design code API 650 (per package title); MoC polymer or caustic-compatible material (TBD); Heated and insulated; Blanket low-pressure fuel gas; Vent incinerator header w/ flame arrestor; Truck-out interface present. Each field cites DBM source as in `Datasheet.md`.
- **Example spacing application.** A plot reviewer applies NFPA 30 Table 22.4.2.1 (2.35 m / 7.72 ft) between the fresh and spent caustic tanks if they are co-located outside the building envelope; otherwise the building separation tables in the OGAOM site standards govern. (Source: DBM lines 268-298.)

## Conflict Table (for human ruling)

| ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-01 | Governing code for caustic tank shell (API 650 per package title vs. polymer / caustic-compatible material direction in DBM that may take tank out of API 650 scope) | Package title "Tanks, Caustic (API 650) 4-25" | `4-25_Deepcut_DBM.md` line 1566 | Specification R2, R3 | Treat API 650 as governing for steel-tank case; require explicit ruling if vendor proposes polymer construction outside API 650 | TBD |
| CONF-02 | Source authority for package requirements is binary (`26020-Package_Requirements.docx` heading 20) and not locally readable; DBM is the only locally accessible text source for caustic tanks | `_REFERENCES.md` (names the .docx) | `4-25_Deepcut_DBM.md` (read in full) | All four documents — multiple R-items marked `location TBD` | Defer authoritative values to a future pass after the .docx is extracted to markdown; flag any DBM-vs-.docx disagreement when extract becomes available | TBD |
| CONF-03 | PVRV / EPRV provision basis cited by analogy with the produced-water tank pattern (DBM line 524) rather than from a caustic-tank-specific source | DBM line 524 (produced-water tank basis) | No direct caustic-tank relief statement in DBM | Datasheet "Construction" row, Specification R4 | Apply produced-water-style PVRV provision as a PROPOSAL pending DE confirmation | TBD |
| CONF-04 | Flare/condensate-tank spacing line (DBM line 282, OGAOM §9.6.15) is written for condensate tanks; applicability to caustic tanks is not asserted in the DBM | DBM line 282 | DBM §"Atmospheric Tank and General Plant Spacing" | Specification R8 | Apply the generic atmospheric-tank-to-flare separation conservatively; confirm OGAOM line item for caustic service | TBD |
