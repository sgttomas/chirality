# Guidance — DEL-093-04 Vendor Engineered Equipment Package (Tanks, Water (API 650) 3-25)

## Purpose

This document records directional rationale, considerations, and trade-offs for the Package Vendor producing the engineered design and physical equipment for `PKG-093`. It supports the Vendor in interpreting the EPC Scope of Work (`DEL-093-01`) and Package Datasheet (`DEL-093-02`) without overstating source authority.

## Principles

1. **Source fidelity over convention.** Where the SOW rows and the 03-25 DBM state a specific provision (API 650 Modified, Devchem 253, blanket gas per API 2000, Kennilworth-type skim), the vendor design carries that provision exactly. Generic API 650 conventions are not a substitute for the "Modified" clauses defined in `26020-Package_Requirements.docx` heading 45.
2. **Non-sour service.** Item No. 1 tanks are explicitly Sweet Produced Water service (SOW-0231). NACE sour-service provisions do not apply unless EPC Integrator confirms otherwise for Item No. 2.
3. **Cold-climate envelope governs metallurgy.** A -40 °C minimum design metal temperature drives plate selection, impact testing, nozzle materials, and gasket choices.
4. **Atmospheric service with positive blanket gas.** Tank vent and vacuum protection are governed by API 2000 with LP fuel gas blanketing; nothing in the vendor design may compromise vacuum protection during winter cold-soak.
5. **Vendor scope is engineering + supply only.** Foundations, site mounting, electrical/instrumentation, platforms, and staircases are explicitly by others (SOW-0232). Vendor interface drawings shall isolate these boundaries clearly.

## Considerations

- **Coating qualification (Devchem 253).** Internal coating on floors, walls, and roof is a vendor responsibility. Surface preparation, cure conditions, and thickness shall be controlled and documented; coating qualification is a closure precondition for `DEL-093-06`.
- **Insulation and heating.** External insulation plus heating is required (SOW-0231). The vendor should locate penetrations, manway access, and instrumentation ports so EPC-supplied insulation/heating systems terminate cleanly.
- **Skim system.** The Kennilworth-type HCL float skim (one per tank, float SG ≤ 0.67) determines internal nozzle layout, weir/baffle interaction, and operability access. ASSUMPTION: skim is normally-operating; vendor design should treat it as continuous service.
- **Vapour interface to VRU.** Vapour management is via the facility VRU system (DBM §SEC-06 line 436); vendor tank design shall provide a properly sized vapour outlet, vent, and isolation interface.
- **Design SG reconciliation (open item).** DBM §SEC-06 line 421 carries tank design SG 1.25 TBC while pump-fluid SG basis is 1.18 (DBM §SEC-03 line 176); vendor design should adopt the more conservative 1.25 SG for tank shell/nozzle structural sizing pending EPC closure, while flagging this for resolution.
- **Item No. 2 incompleteness.** SOW-0232 carries TBD for design flow and operating temperature for Item No. 2. Vendor should not infer values; engagement with the EPC Integrator is required to close this scope before commencing detailed design on Item No. 2.

## Trade-offs

- **Plate thickness vs SG.** Adopting SG 1.25 for structural design increases shell course thickness vs the 1.18 SG pump basis. Trade-off favors conservatism given the open SG reconciliation; downstream weight, foundation loads (EPC scope), and freight impacts should be flagged.
- **Coating system maintenance.** Devchem 253 coating extends life in produced-water service but requires controlled application; trade-off is up-front qualification effort vs in-service repair cost.
- **Heating method selection.** Coil heating vs external trace vs jacketed bottom: source materials do not select a heating method explicitly. Trade-off resolution rests with detailed design coordinated with EPC heat-tracing scope (by others).

## Examples

No example values are provided in source beyond the Datasheet attributes. Worked examples shall be developed during detailed design and recorded in the vendor design basis (per `DEL-093-05`).

## Conflict Table (for human ruling)

This table captures conflicts and open items in the source set that materially affect the vendor engineered package. HRR = Human Ruling Required.

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-093-04-01 | Tank design SG vs pump fluid SG mismatch. Tank design SG = 1.25 TBC; pump fluid SG basis = 1.18. | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 421) | `3-25_Comp_and_Liquids_DBM.md` §SEC-03 (line 176) | Specification REQ-093-04-013; Datasheet Process/Service; vendor structural calculations | Adopt SG 1.25 for tank structural design (conservative); reconcile pump-fluid basis in detailed design. HRR. | TBD |
| CONF-093-04-02 | SOW-0231 cites "modified API 650, volume: TBD" while SOW-0230 fixes Item No. 1 nominal capacity at 3,800 bbl. | SOW-0231 | SOW-0230 | Datasheet capacity attribute; REQ-093-04-001 | Treat SOW-0230 (3,800 bbl) as authoritative nominal capacity for Item No. 1; interpret SOW-0231 "volume TBD" as net working volume or Item No. 2 capacity. HRR. | TBD |
| CONF-093-04-03 | SOW-0232 design pressure is stated as "32 oz test pressure" without separation of design vs hydrotest. | SOW-0232 | API 650 Modified | Specification REQ-093-04-004; vent/vacuum protection design | Interpret 32 oz as design pressure (gauge); apply API 650 Modified hydrotest provisions; confirm with EPC Integrator. HRR. | TBD |
| CONF-093-04-04 | Item No. 2 scope is incompletely specified: design flow TBD, operating temperature TBD. | SOW-0232 | (no second source) | Specification REQ-093-04-002, 011, 012; Datasheet | Hold detailed design of Item No. 2 until EPC Integrator closes flow and operating temperature. HRR. | TBD |
| CONF-093-04-05 | API 2000 edition not stated. | SOW-0231 | (no edition cited) | Vent sizing calculation; REQ-093-04-007 | Adopt latest published edition of API 2000 in effect at vendor design start unless EPC specifies otherwise. HRR. | TBD |
| CONF-093-04-06 | "Modified" API 650 clauses are not enumerated in available source slices; reference is to `26020-Package_Requirements.docx` heading 45 (Major included equipment), which has not been locally extracted to markdown. | SOW-0231 | `26020-Package_Requirements.docx` heading 45 (location TBD) | Specification REQ-093-04-003; vendor design | EPC Integrator to confirm the enumerated set of API 650 modifications applicable to Item No. 1 and Item No. 2 in the Package Datasheet (`DEL-093-02`). HRR. | TBD |

ASSUMPTION items elsewhere in this Guidance are not enumerated as conflicts because they are vendor-side interpretive defaults that can be reversed without changing the source. Conflicts above represent source-set inconsistencies that materially affect engineering decisions.
