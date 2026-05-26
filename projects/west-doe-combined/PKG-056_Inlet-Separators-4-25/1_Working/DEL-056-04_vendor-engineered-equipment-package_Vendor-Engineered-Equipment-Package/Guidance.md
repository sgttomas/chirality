# Guidance — DEL-056-04 Vendor Engineered Equipment Package

**Pass:** P1/P2 | **DECOMP_VARIANT:** PROJECT | **Skill:** four-documents

## Purpose

This guidance directs the vendor and EPC Integrator reviewers in interpreting the requirements for the Inlet Separators 4-25 vendor engineered equipment package. The package realizes the EPC Scope of Work (DEL-056-01) and Package Datasheet (DEL-056-02) into physical hardware, and is the principal scope through which OBJ-001, OBJ-003 through OBJ-010 are physically expressed for PKG-056 (ASSUMPTION: package-grouping heuristic).

## Principles

- **EPC datasheet is the technical contract.** The vendor's design freedom is bounded by the EPC Package Datasheet (DEL-056-02) and Scope of Work (DEL-056-01). Where this Specification's clauses differ from the EPC Package Datasheet, the EPC Package Datasheet governs and a clarification shall be raised through the EPC Integrator (DEL-056-06).
- **Source-grounded basis.** Process and mechanical bases trace to the project DBM (Deepcut and Comp_and_Liquids). Where the DBM marks TBD/TBC, the vendor shall not invent values; the vendor shall flag and request EPC ruling.
- **Two-separator current authority; legacy four-package CONFLICT preserved.** Vendor shall design on the two-package, 50%-each, current authority basis. The legacy four-package count is preserved as unresolved and is not a design basis unless overridden by EPC ruling.
- **Sour service throughout.** All wetted equipment shall be sour-service rated per SEC-04 basis; coating (Devchem 253 on separator vessel) is mandatory.
- **Maintainability by isolation.** Each parallel package shall be capable of full unit isolation and removal from service while remaining units operate.
- **TBD discipline.** Numerical and methodological gaps (slug capacity range, heater duty/medium, ESDV setpoints, HIPPS) are flagged TBD/TBC and require explicit closure during detailed engineering, not silent vendor selection.

## Considerations

- **Plot space provision.** Provision for a future third separator is part of the current authority — vendor mechanical/structural layout shall accommodate the spare position without committing equipment.
- **Internals choice.** Mist eliminator type and weir adjustment range are subject to operations review; vendor should expose adjustment range, removal access, and inspection ports clearly.
- **PCV trim.** Two-phase hydrocarbon throttling at >=1300 psig with dP <= 5 psid drives valve selection toward balanced-globe, hardened trim, and multiple parallel paths. Anti-cavitation/anti-erosion needs are implicit; vendor shall make explicit.
- **Heater integration.** The liquid outlet heater target temperature and medium are unresolved; vendor shall expose the design envelope so EPC process simulation can close TBD items without forcing a redesign.
- **Methanol injection layout.** Injection points (upstream of PCV; upstream of HCL/water dump valves) shall be physically accessible and metered; capacities remain TBC.
- **Drive gas metering.** Drive gas enters upstream of plant inlet gas meters; separate metering per package is required for plant gas accounting.
- **Building configuration.** A self-framing package building enclosing instrumentation and one end of the vessel is the configuration narrative (sibling MPFF package configured "similarly to the inlet separator"); vendor shall confirm climate, hazardous area classification, and access.

## Trade-offs

| Trade-off | Discussion |
|---|---|
| Two installed vs. plot-reserved third | Current authority installs two and reserves plot space; this caps initial cost but constrains turndown/redundancy. Vendor shall not anticipate the third unit as installed. |
| Conflicting separator quantity (2 vs. 4) | Designing to four would oversize plot, utilities, and capex and would conflict with current authority. Designing to two is governed by current basis; legacy four-package references remain a known CONFLICT and shall be carried as such until ruled. |
| PCV count and trim | Two parallel PCVs minimum balances reliability and rangeability against capex; hardened trim is a fixed requirement, not a trade. |
| Heating medium (warm glycol vs. cross-exchange) | Warm glycol favors operational independence and start-up flexibility; cross-exchange improves heat integration but couples to upstream process states. Medium remains TBD pending EPC process simulation. |
| HIPPS vs. design-margin | If upstream pipeline MAOP exceeds facility design pressure, HIPPS is the conventional protection; designing the vessel and downstream rating to the higher MAOP is feasible but costly. Decision deferred to detailed engineering. |

## Examples

Source-supported configuration examples (not vendor commitments, only directional context):
- Per the Deepcut DBM, Inlet Separators 2 unit is tagged as V-1600-1 and V-1700-1 at the 4-25 facility location. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- Per the Comp_and_Liquids DBM, the inlet separation system uses tags V-1600-2 and V-1700-2. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- The two tag families reflect different design-case lineages; vendor shall align tag set to the EPC Package Datasheet (DEL-056-02) ruling.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-01 | Installed inlet separator quantity: two (current authority) vs. four (legacy) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — inlet separator design parameters, current basis | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — legacy "4 x 50%" table; "4 vessels" MPFF source table | Datasheet (Attributes), Spec R1, Procedure prerequisites | Adopt current authority: two installed with plot for third | TBD |
| CONF-02 | Separator tag family: V-1600-2 / V-1700-2 vs. V-1600-1 / V-1700-1 | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` | Datasheet (Attributes) | Defer to EPC Package Datasheet (DEL-056-02) | TBD |
| CONF-03 | Inlet separator ESDV shutdown pressure: 1360 psig vs. 635 psig | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` ("inlet separator shut ESDV pressure shutdown basis is 1360 psig") | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` ("635 psig at the inlet separator ESDV") | Spec R8.2, Procedure verification | Likely separate concepts (plant inlet ESDV shut vs. inlet separator ESDV operating low setpoint); confirm with EPC | TBD |
| CONF-04 | Per-separator slug capacity range: 31.8 m3 vs. 33.9 m3 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (alternate value within same source) | Spec R4.5 | Carry as TBD until EPC ruling | TBD |
| CONF-05 | Liquid outlet heater outlet temperature, duty, and medium | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (TBD pending process simulation) | n/a | Spec R7, Datasheet (Construction) | Defer to EPC process simulation | TBD |
| CONF-06 | HIPPS requirement | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (TBC during detailed engineering) | n/a | Spec R8.3 | Defer to detailed engineering | TBD |
| CONF-07 | Methanol injection design capacities | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (all design capacities TBC) | n/a | Spec R9 | Defer to EPC ruling | TBD |
| CONF-08 | Older "2 x 100%" table vs. current "two identical, each 50%" | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (notes older 2 x 100% table language requires reconciliation) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (current basis) | Datasheet (Attributes), Spec R1 | Current 2 x 50% basis | TBD |
