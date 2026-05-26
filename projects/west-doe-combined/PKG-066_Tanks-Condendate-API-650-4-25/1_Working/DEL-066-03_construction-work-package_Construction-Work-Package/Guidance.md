# Guidance — DEL-066-03 Construction Work Package (PKG-066 Tanks, Condensate (API 650) 4-25)

> Directional document. Captures purpose, principles, considerations, and trade-offs for assembling and executing the Construction Work Package (CWP) for the 04-25 condensate tank package.

## Purpose

The CWP exists to make the 04-25 condensate tank package physically installable, inspectable, tie-in-ready, and turnover-ready under the West Doe EPC model in which Tourmaline holds field-construction responsibility and the EPC Integrator owns package integration. Per the GATE-07 decomposition, the CWP is one of three mandatory EPC Integrator anchor deliverables (alongside Scope of Work and Package Datasheet) for every approved package. (Source: `_Decomposition/.../PROJECT_DECOMP.md` discussion of mandatory EPC anchors; reflected in `_CONTEXT.md`.)

The CWP translates package engineering (vendor and EPC) into a construction-execution dossier that the field organization can act on, while preserving the boundaries set by the Scope of Work and the technical envelope set by the Package Datasheet.

## Principles

1. **Anchor in source.** Construction direction is grounded in the 04-25 Deepcut DBM (tank specification, blanket-gas, VRU connection, transfer-pump arrangement) rather than in convention. Where the DBM is silent or open, the CWP carries the open item explicitly as `TBD` and routes it to detailed engineering or human ruling.
2. **Respect the construction responsibility split.** Tourmaline holds field-construction responsibility for the activities listed in DBM-Deepcut lines 107-125; the EPC Integrator's CWP authorship serves Tourmaline's execution and does not assume EPC self-perform.
3. **Plan tie-ins jointly.** Tie-ins (VRU suction header, blanket-gas header, drain headers, condensate transfer to 03-25 Liquids Hub) are joint-planning artifacts, not unilateral scope. (DBM-Deepcut line 127.)
4. **Sequence with the tank-farm pump module.** Tanks without the recycle / skim / transfer pump services cannot be brought into useful operation; CWP scheduling shall keep these dependent. (DBM-Deepcut lines 1669-1675.)
5. **Hold construction-release behind the geotechnical report.** Foundation design and construction shall not proceed against placeholder geotechnical values. (DBM-Comp_and_Liquids lines 141, 688, 700.)
6. **Keep the CWP register reconciled.** Before issue-for-construction, the CWP register shall be reconciled with the plot plan, equipment list, and overall construction work-package register. (DBM-Comp_and_Liquids line 661.)

## Considerations

- **Cold weather (-40 deg C basis).** Winterization is a first-order driver — slop tank insulation, product-tank recycle (in lieu of insulation), heat-traced lines, and blanket-gas to prevent winter vacuum are not optional construction items. (DBM-Comp_and_Liquids line 145; DBM-Deepcut lines 1644-1645, 1663, 1679.)
- **Sour-service / vapour management.** Tank isolation philosophy in the presence of potentially sour vapours is flagged for detailed engineering review; CWP construction shall preserve all isolation/instrumentation provisions even where final settings are TBD. (DBM-Deepcut line 1663.)
- **Plot-plan gap.** Drawing CIV-235633-5002 is not in the source package. CWP coordinate content depends on the released plot plan; until issued, all coordinate-bound CWP items are `TBD`. (DBM-Deepcut line 323.)
- **Standards locally inaccessible.** API 650, API 2000, API 2510, NFPA 30, and OGAOM are cited as governing, but their text is not locally accessible. Clause-level requirements (e.g., specific weld inspection requirements, specific hydrotest hold-times) are `TBD` against the actual standards.
- **Condensate tank quantity conflict.** DBM-Deepcut line 1640 names "4 x 3,800 bbl tanks"; line 2625 names 5 tags (TK-9110-1 through TK-9150-1). The 5-tag basis is used pending human ruling. See Conflict Table below.
- **Inlet-separator quantity conflict (adjacent context).** The DBM also notes an inlet-separator quantity conflict (two installed plus future plot vs. four-package legacy text). Not in CWP scope, but flagged because it touches construction sequencing of adjacent areas. (DBM-Deepcut line 589.)

## Trade-offs

- **Insulation vs. recycle.** Product tanks are non-insulated with winter recycle as the temperature-maintenance mechanism. This trades capital cost for operating exposure: a recycle-pump outage during winter requires either alternative heat input or operational drawdown.
- **Common truck-out manifold vs. dedicated lines.** Common truck-out simplifies civil/piping work and the unloading pad arrangement but complicates isolation during off-spec or contaminated batches. CWP shall ensure isolation/lockout provisions are physically constructible.
- **Joint tie-in planning vs. construction tempo.** Joint planning protects facility integrity at the cost of construction-front independence. The CWP turnover checklist is the place to make that trade-off visible.
- **EPC Integrator as planner vs. field executor.** The EPC Integrator authors the CWP but does not perform the field work; CWP content must be executable by an owner-managed construction organization without requiring re-authorship.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CFL-01 | Number of 04-25 condensate storage tanks: 4 vs 5 | DBM-Deepcut line 1640 ("4 x 3,800 bbl tanks") | DBM-Deepcut line 2625 (equipment register lists 5 tags TK-9110-1 through TK-9150-1) | Datasheet "Attributes", Spec REQ-CWP-03 / REQ-CWP-04, Procedure step list | Equipment register (line 2625) — 5 tanks — as it is the explicit tag-level basis | TBD |
| CFL-02 | Inlet-tank vs. slop-tank vs. product-tank allocation across the 5 tags | DBM-Deepcut line 1661 (pattern: inlet/outlet cascade + slop) | No explicit per-tag service assignment | Spec REQ-CWP-04, Procedure prerequisites | Defer to DEL-066-02 Package Datasheet for per-tag service assignment | TBD |
| CFL-03 | ISBL/OSBL tie-in piping responsibility | DBM-Deepcut line 117 ("External interface responsibility marker; responsibility is to be confirmed for each tie-in") | (no contrary source) | Spec REQ-CWP-08, REQ-CWP-09; Procedure tie-in steps | Per-tie-in responsibility matrix produced jointly with Tourmaline before IFC | TBD |
| CFL-04 | Standard clause-level construction/inspection criteria | API 650 / API 2000 / NFPA 30 / OGAOM citations in DBM | Standards text not locally accessible | Spec "Standards", all verification rows | Cite standards by reference; carry `location TBD` for clause-level criteria | TBD |

## Examples

Source-supported examples are limited because the only locally accessible authority is the 04-25 DBM (basis-of-design level, not work-package level). Worked construction examples (e.g., a fully-sequenced tank-erection workface plan) would require the vendor engineered equipment package (DEL-066-04) and the released plot plan. Until then, illustrative examples are intentionally omitted to avoid implying source support that does not exist.
