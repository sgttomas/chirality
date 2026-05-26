# Guidance — DEL-073-03 Construction Work Package (PKG-073 Amine Treating Unit)

## Purpose

The Construction Work Package (CWP) translates the EPC Scope of Work (DEL-073-01) and Package Datasheet (DEL-073-02) into an executable construction plan for installing the vendor-supplied Amine Treating Unit (ATU) at the 04-25 Deepcut Gas Plant, integrating it into facility systems, and turning it over to commissioning. It is the EPC Integrator's anchor deliverable for how PKG-073 becomes a physically installed, inspected, and turnover-ready production unit. (Source: `_CONTEXT.md` Scope; PROJECT_DECOMP PACKAGE_REGISTER row PKG-073.)

## Principles

- **Source authority.** The CWP follows the vendor package design (DEL-073-04) and the EPC Package Datasheet (DEL-073-02) for what is being installed; the Datasheet and DBM-Deepcut process basis govern what equipment is involved and what conditions it operates under. The CWP does not create new process design intent.
- **Integration ownership.** PKG-073 is divided between Package Vendor (engineering/design/equipment) and EPC Integrator (facility-level integration). The CWP is the EPC Integrator's authoritative artifact for tie-ins, constructability, and turnover; vendor design constraints must be respected unmodified. (Source: PROJECT_DECOMP PKG-073.)
- **Tie-in completeness.** All interface types identified for PKG-073 must be planned, not just process piping. Utility, relief, drain, electrical, EHT, grounding, lighting, I&C, HVAC, F&G, structural, and maintenance access are all in scope. (Source: PROJECT_DECOMP PKG-073 "Applicable interface types".)
- **Cold-climate constructability.** The 04-25 site design ambient envelope (-40 °C to +35 °C; extreme -49.2 °C to +38.9 °C) drives sequencing decisions: cold-weather welding, hydrotest freeze management, EHT energization timing, and outdoor work limits. (Source: DBM-Deepcut Sec. 2 site basis.)
- **Turnover discipline.** Mechanical completion and turnover evidence is the bridge to commissioning; the CWP must produce a defensible, witnessed dossier rather than a narrative.
- **Respect of vendor scope boundaries.** Field rework of vendor-supplied scope is constrained by warranty, design responsibility, and acceptance under DEL-073-06; field changes must be routed through the EPC change process.

## Considerations

- **Modularization vs. stick-build trade.** Layout maturity drives this decision; DBM-Deepcut Sec. 2.3 indicates that modular construction requirements are to be coordinated with the plot plan as layout matures. The CWP should be re-baselined when the modular split is fixed. (TBD pending plot plan freeze.)
- **Reboiler hot-oil interface.** Amine reboiler hot-oil tie-ins must accommodate the 350 °F supply basis with mixing-valve control to hold amine-side skin ≤350 °F; commissioning of this interface depends on hot-oil system availability (heat medium package outside PKG-073). (Source: DBM-Deepcut Amine Equipment.)
- **Flare/relief tie-ins.** Amine regenerator overhead, reflux accumulator, and flash drum pressure-control paths route to LP flare and to acid-gas compression; CWP planning must coordinate with flare and acid-gas package readiness. (Source: DBM-Deepcut Sec. "Amine treating" advanced-control row in C&I table.)
- **Hydrocarbon skim and drain routing.** Surge tank, amine flash drum, and reflux accumulator each have hydrocarbon skim provisions; routing to amine slop tank / produced-water storage must be cleanly documented in the workface plan. (Source: DBM-Deepcut Amine Equipment.)
- **Sour-service material handling.** Construction interventions on amine and acid-gas service piping must respect material selection and post-weld procedures; the material selection review at low H2S/CO2 ratios is open per DBM. (Source: DBM-Deepcut "Amine Open Items and Assumptions".)
- **Loop-check and instrument readiness.** Amine pressure, level, and flow control loops (level-controlled rich-amine path; pressure-controlled flash-gas to SOC; LP flare pressure control; surge-tank and regenerator fuel-gas blanket) require coordinated loop checks before turnover. (Source: DBM-Deepcut C&I "Amine treating" row.)

## Trade-offs

| Trade-off | Direction | Notes |
|---|---|---|
| Early tie-in vs. late mechanical completion | Early tie-ins reduce schedule risk but increase exposure during adjacent work; late tie-ins simplify QA but compress commissioning. | Workface plan should sequence by interface type and adjacent-package readiness. |
| Stick-build vs. modular sub-assembly | Modular pre-assembly improves quality and shortens field schedule but is constrained by transport limits and layout maturity. | Decision is downstream of plot plan freeze (TBD). |
| Single-pass hydrotest vs. spool-level testing | Single-pass minimizes joints to retest but is logistically heavier; spool-level eases scheduling but increases joint count. | Choose per EPC pressure-test plan (TBD). |
| Hot-oil commissioning sequence | Commissioning reboiler hot-oil loops with cold amine vs. introducing amine first | Coordination with heat-medium package availability governs. |

## Examples

ASSUMPTION: example construction sequences are inferred from the equipment and interface list; they are not transcribed from a worked construction precedent in the accessible sources.

- **Example A — Absorber set and tie-in.** Lay down absorber sections; set absorbers and inlet coalescer trains on foundations; mate vendor-internal piping and demister assemblies; cap nozzles pending tie-in; install absorber tie-ins to inlet compression discharge and TEG inlet cooling per the workface plan; complete pressure testing of new welds; close out punch list; sign turnover witness.
- **Example B — Regenerator and reboiler installation.** Set regenerator column and reboiler kettle; align hot-oil supply and return tie-ins; pressure-test new spools; loop-check temperature/level instruments; perform dry function check of mixing valves with hot-oil package availability; complete punch list before solvent fill.
- **Example C — Surge tank installation.** Set surge tank within secondary containment; install LP fuel-gas blanket tie-in, hydrocarbon skim outlet, truck-out connection, insulation and heater; commission with nitrogen and gas blanket prior to amine introduction.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| (none identified at Pass 2) | — | — | — | — | — | TBD |

No Pass 2 cross-document inconsistencies were identified that required source reconciliation beyond the open items already noted in DBM-Deepcut ("Amine Open Items and Assumptions"). The 26020-Package_Requirements.docx and 26020-Packages_Interfaces_4_export.xlsx sources are binary and not text-accessible in this run; clause-level conflicts cannot be ruled in/out without text extraction.
