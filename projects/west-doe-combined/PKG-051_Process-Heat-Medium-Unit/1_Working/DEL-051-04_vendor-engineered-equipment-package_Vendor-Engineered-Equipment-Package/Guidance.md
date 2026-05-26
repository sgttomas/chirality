# Guidance — DEL-051-04 Vendor Engineered Equipment Package (PKG-051 Process Heat Medium Unit)

## Purpose

This deliverable is the Package Vendor's production unit that, when executed, yields the physical Process Heat Medium Unit equipment package and its supporting vendor engineering/design documentation. It is dispatched by the EPC Scope of Work (DEL-051-01) and Package Datasheet (DEL-051-02) and is consumed downstream by the Vendor Document Turnover Package (DEL-051-05) and the EPC Vendor Package Review and Acceptance (DEL-051-06). (`SourcePath`: SCOPE_LEDGER.csv; `SectionRef`: SOW-0165 dispatched deliverables list.)

## Principles

- **Source-of-record split.** The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility-level integration: interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration (`SourcePath`: PACKAGE_REGISTER.csv; `SectionRef`: row PKG-051).
- **Battery-limit clarity.** The by-others exclusions (interconnecting piping, DCS integration, foundations, mounting buildings at site, electrical supply from MCC, platforms/stairs) are explicit in the workbook source and shall be preserved at vendor skid edges (`SourcePath`: 26020-Package_Requirements.docx; `SectionRef`: heading 6 / Scope notes and open items, via SOW-0168).
- **Closed-loop service.** The hot oil / heat medium system supplies heat to process users in a closed loop; the package is one element of a facility-level loop (`SourcePath`: 26020-Package_Requirements.docx; `SectionRef`: heading 6 / Basic scope, via SOW-0166).
- **Vendor-led sizing.** Expansion tank size & capacity are explicitly "to be advised by vendor" — guidance is to size against the 85% fill-at-274 deg C and pump NPSHR criteria stated in the source.

## Considerations

- **Loop topology in flux.** Two project-internal source streams describe the loop differently. The 26020 workbook package source (vendor scope baseline) calls for hot loop / cold loop with 3 x 66% pumps and 260 deg C maximum bulk temperature. The DBM-Deepcut single unified loop basis (220 deg C, single pump module, sparing under review) consolidates this scope. Until a human ruling resolves the conflict (see Conflict Table), the vendor is expected to bid against the workbook source basis and to flag any divergence requested by the EPC Integrator.
- **Fluid selection.** Petro Canada Peterotherm (workbook source) vs Brenntag Petrotherm (DBM-Deepcut). These are different product designations; in addition to the loop-temperature conflict, the heat-transfer fluid identity itself is in conflict and merits a documented selection ruling.
- **Heater duty unknown at vendor-scope level.** PKG-051 source heading 6 does not state a heater duty. The DBM-Deepcut total post-VE single-loop heat medium duty (approx. 21,913 kW ≈ 74.8 MM BTU/h) and the API-560 heater type are candidate basis values pending Conflict Table resolution; do not flow these into vendor bid documents until the loop topology is settled.
- **Interface envelope.** PKG-051 applicable interface types span Utility Piping, Drain/Containment, Electrical Power, Grounding/Bonding, Area/Exterior Lighting, I&C/Control Cabling, Building HVAC/Services, Fire & Gas/Safety Systems, Maintenance Access, and Structural/Foundations/Supports. The vendor package shall present clean, listable tie-in points for each applicable type rather than embedding facility-level integration logic.
- **Pressure containment basis.** The pump design pressure of 2413 kPag (350 psig) in the workbook source aligns with the DBM-Deepcut "all heat medium fluid-containing components designed for at least 350 psig" statement; this is one area where both sources agree.

## Trade-offs

- **Loop consolidation vs vendor scope re-baselining.** Adopting DBM-Deepcut's unified-loop basis would simplify field piping and reduce equipment count but would require re-baselining the vendor scope (one pump module instead of separate hot/cold pumps, revised expansion-tank sizing, possibly different fluid and bulk temperature). The trade-off is constructability/lifecycle simplification vs schedule/commercial impact on the vendor package.
- **Sparing philosophy.** The workbook source explicitly sets 3 x 66% pumps. DBM-Deepcut leaves the consolidated sparing philosophy "to be confirmed during detailed engineering." Locking the workbook 3 x 66% basis early gives the vendor a stable basis to bid; deferring risks rework if the consolidated philosophy lands differently.
- **Vendor-defined vs EPC-defined heater duty.** Allowing the vendor to size the heater off a stated process-user demand (preferred) requires the EPC Integrator to deliver a consolidated user-duty table; in the absence of one, the vendor can only quote against a notional duty band.

## Examples

No fully worked vendor-package examples are present in the accessible source slices; examples section is intentionally minimal pending vendor reference packages.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted Sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-051-04-01 | Loop topology: hot/cold split with mix vs single unified loop | 26020-Package_Requirements.docx heading 6 / Basic scope (via SOW-0166) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 1945-1947 (Heat Medium Basis) | Datasheet §Attributes, §Construction; Specification R-1, R-5; Procedure Prerequisites/Steps | PROPOSAL: workbook source governs vendor scope basis until EPC issues a single-loop scope change to PKG-051. | TBD |
| CONF-051-04-02 | Maximum bulk temperature: 260 deg C (workbook) vs 220 deg C normal / 315 deg C max bulk (DBM) | 26020-Package_Requirements.docx heading 6 / Major included equipment (via SOW-0167) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 1951-1959 | Datasheet §Conditions; Specification R-4; Procedure Verification | PROPOSAL: workbook source 260 deg C governs vendor scope basis until reconciled. | TBD |
| CONF-051-04-03 | Heat medium fluid: Petro Canada Peterotherm vs Brenntag Petrotherm | 26020-Package_Requirements.docx heading 6 / Major included equipment (via SOW-0167) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 1951 | Datasheet §Conditions; Specification R-4 | PROPOSAL: confirm fluid identity with EPC fluid-selection ruling before vendor bid issue. | TBD |
| CONF-051-04-04 | Pump sparing: 3 x 66% (workbook) vs sparing-philosophy TBC (DBM) | 26020-Package_Requirements.docx heading 6 / Major included equipment (via SOW-0167) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 1996 | Datasheet §Conditions; Specification R-2 | PROPOSAL: hold workbook 3 x 66% basis for vendor scope until EPC issues alternative. | TBD |
| CONF-051-04-05 | Heater duty and configuration: not stated at PKG-051 source level vs API-560 natural-draft cabin-style direct-fired, 1.25 x winter steady-state, 1 x 125% sparing under review (DBM) | 26020-Package_Requirements.docx heading 6 (silent on heater duty) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 1998-2000 | Specification R-6, Standards table; Procedure Verification | PROPOSAL: route DBM heater-basis values into vendor bid only after CONF-051-04-01 is ruled. | TBD |
| CONF-051-04-06 | Expansion tank operating pressure transcription: "125 to 240 Kapg (18 to 23 Psig)" — kPag/psig conversion inconsistent | 26020-Package_Requirements.docx heading 6 / Major included equipment (via SOW-0167) | (none — internal source consistency issue) | Datasheet §Conditions; Specification R-3 | PROPOSAL: confirm correct expansion-tank operating-pressure band with original DOCX section; treat as `TBD` numerically until confirmed. | TBD |
