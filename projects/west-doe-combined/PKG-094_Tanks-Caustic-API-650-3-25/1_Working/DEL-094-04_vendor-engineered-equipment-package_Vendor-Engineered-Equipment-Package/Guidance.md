# Guidance: DEL-094-04 — Vendor Engineered Equipment Package

## Purpose

This deliverable exists to bound the Package Vendor's engineered work product — the physical caustic-service tank package and its design basis/datasheet set — within PKG-094 "Tanks, Caustic (API 650) 3-25." It is the production unit that converts the EPC's Scope of Work (DEL-094-01) and Package Datasheet (DEL-094-02) into a fabricated, code-compliant equipment package that downstream construction (DEL-094-03), turnover (DEL-094-05), and EPC acceptance (DEL-094-06) work against.

## Principles

- **EPC defines, vendor engineers.** The EPC's SOW and Package Datasheet are authoritative inputs; the vendor's engineering decisions must trace back to them. The vendor does not redefine the package scope.
- **Code family selection follows the package title.** API 650 is the governing tank code family per the package title. Edition, appendices, and project amendments are EPC-defined; the vendor implements them.
- **Source over convention for caustic service.** 50 wt% NaOH service drives material, coating, gasket, and gauging selections. Default tank-construction assumptions from generic API 650 examples are not sufficient.
- **Site basis is non-trivial.** The 03-25 site governs winterization, heat tracing, insulation, foundations, and metallurgy. -40 deg C ambient is a hard design driver.
- **Aluminum is excluded** from the caustic building per DBM. Material substitutions that reintroduce aluminum are not permitted without EPC ruling.
- **TBC values are TBC, not silently resolved.** Several DBM values (SG 1.75, caustic drain temperature, internal coating) are marked TBC in the source; the vendor must close them in design, not assume them.

## Considerations

- **Code edition and appendices.** API 650 appendices that may be relevant (Appendix S — austenitic stainless steel; Appendix M — elevated temperature; Appendix R — low-pressure storage tanks) depend on detailed service and are TBD until the EPC Package Datasheet is issued.
- **Internal coating.** DBM specifies Devchem 253 for produced-water tanks but is TBC for caustic tanks. Coating selection for 50 wt% NaOH at the design temperature is a meaningful engineering decision.
- **Heat tracing and insulation.** Caustic must be kept above freezing/precipitation thresholds; heating concept and redundancy are EPC/vendor decisions.
- **Vent/blanket/flare integration.** Spent caustic vent to incinerator header (with flame arrestor) and fresh caustic isolation from VRU are non-default integration choices documented in DBM.
- **Tank register supersession.** DBM equipment counts and sizes are subject to a final tank register; vendor scope must accommodate revisions before fabrication release.
- **SCA-002 effect.** Under SCA-002, VRU discharge is rerouted to the 04-25 SOC suction; the caustic tank package interfaces with this configuration via the LP fuel-gas blanket system, not via a 03-25 local SOC.

## Trade-offs

- **Material selection cost vs. service life.** Higher-grade caustic-compatible materials (e.g., nickel-bearing alloys for hot caustic regions) cost more but reduce risk of caustic stress corrosion cracking; carbon steel with coating reduces capex but increases inspection/coating-life dependency.
- **Shop-built vs. field-erected.** 400 bbl tanks are typically shop-built — this should accelerate delivery and improve QA versus field erection, but requires road access and lift planning.
- **Heat tracing redundancy.** Redundant circuits (per DBM "under consideration") increase reliability but add electrical load and complexity.

## Examples

DBM-supplied configuration examples directly applicable to this deliverable:
- Liquids hub equipment basis: "400 bbl caustic process-water, fresh-caustic, spent-caustic, and H2O2 tanks" (source: DBM 3-25).
- Caustic tank construction: "atmospheric 32 oz tanks with LP fuel-gas blanket, heating, and insulation" (source: DBM 3-25).
- Vent path: "spent caustic tank vents through a flame arrestor to the incinerator header and supports truck-out" (source: DBM 3-25).

Examples for clause-level API 650 design choices are not drawn from locally accessible code text and remain `TBD`.

## Conflict Table (for human ruling)

High Risk Result (HRR) items where source ambiguity or absence requires human ruling:

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-01 | Package title states "API 650"; DBM applies the qualifier "API-650 Modified" to produced-water tanks; caustic tank code application is not stated at clause level. | `_CONTEXT.md` PackageName ("Tanks, Caustic (API 650) 3-25") | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` ("Tanks are API-650 Modified atmospheric tanks…" — for produced water) | Datasheet (Construction.Code family); Specification R2, R5 | PROPOSAL: Treat API 650 as governing for caustic tanks; "API-650 Modified" appears tied to produced-water service in DBM and may not apply to caustic family. EPC Package Datasheet (DEL-094-02) to confirm edition/appendices/modifications. | TBD |
| C-02 | Caustic solution SG basis marked TBC in DBM (SG 1.75). Hydrostatic and structural design depend on this value. | DBM 3-25 (caustic basis) | None — value is TBC in source | Datasheet (Attributes); Specification R4 | PROPOSAL: Use SG 1.75 as design hydrostatic basis pending EPC confirmation; flag in vendor design basis as TBC-resolved. | TBD |
| C-03 | Internal coating for caustic tanks is not specified (DBM is TBC); DBM specifies Devchem 253 for produced-water tanks (different service). | DBM 3-25 (produced-water coating) | DBM 3-25 (caustic tanks: material/coating TBC) | Datasheet (Construction.Internal coating); Specification R6 | PROPOSAL: Vendor proposes a caustic-rated lining (or unlined with appropriate material) qualified for 50 wt% NaOH; EPC to confirm via Package Datasheet. | TBD |
| C-04 | Caustic drain max temperature is 121 deg C / 250 deg F TBC; affects nozzle rating selection above the 300# minimum. | DBM 3-25 (drain systems) | None — TBC in source | Datasheet (Attributes); Specification R7 | PROPOSAL: Design drain nozzles to 300# ANSI minimum at 121 deg C until EPC confirms; revisit if higher temp issued. | TBD |
| C-05 | "Aluminum shall not be used in the caustic building" — scope of "building" (process building only, or any structural element on the package skid)? | DBM 3-25 | None | Specification R6; Procedure (material acceptance) | PROPOSAL: Apply prohibition broadly to caustic-service vessel scope and any package-mounted equipment located in the caustic building; EPC to rule on edge cases (e.g., instrument tags, fasteners). | TBD |
| C-06 | Workbook Packages row 86 and 26020-Package_Requirements.docx heading 46 are referenced by `_CONTEXT.md`/`_REFERENCES.md` but no locally accessible source slice exists. | `_REFERENCES.md` (decomposition references) | None locally accessible | All four documents (requirements/values traceability) | PROPOSAL: Convert/extract source slices into the deliverable scope before final vendor release; until then, requirements derived from these sources remain `location TBD`. | TBD |
| C-07 | SOW item mapping (SOW-0193..0196) to specific vendor scope rows is not derivable without DEL-094-01 SOW content. | `_CONTEXT.md` Covers Scope Items | DEL-094-01 SOW (not yet drafted in this deliverable's view) | Specification R10 | PROPOSAL: Resolve in DEL-094-04 ↔ DEL-094-01 cross-walk after DEL-094-01 is drafted. | TBD |
