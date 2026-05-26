# Guidance — DEL-070-03 Construction Work Package (Mole Sieve Drier Unit, NGL)

## Purpose

This deliverable exists to make the EPC Integrator's physical execution of PKG-070 (Mole Sieve Drier Unit, NGL) auditable and turnoverable: how the vendor-supplied package is installed, built, inspected, tied into the larger facility, and handed over. Per the GATE-07 decomposition snapshot, it is one of the mandatory EPC anchor deliverables for the package (alongside DEL-070-01 Scope of Work and DEL-070-02 Package Datasheet) and is the construction-side counterpart to the vendor production unit (DEL-070-04) and EPC acceptance evidence (DEL-070-06).

## Principles

- **Vendor design governs equipment install method.** Construction sequencing for the dryer vessels, cooler, scrubber, and enclosure is anchored to vendor MEC-017 setting drawings and MEC-018 lifting study, not to EPC-side conventions invented at construction time.
- **Battery-limit discipline.** The CWP only commits EPC construction effort to interface categories the source Physical Interface Summary marks Applicability=Yes. By-others scope from the source Scope Notes (upstream mercaptan treating, downstream NGL storage/loading/LACT/export, sales-gas and stabilizer-overheads compression, produced-water tank and facility drain header beyond nozzles, flare header) is explicitly out of CWP scope.
- **Hydrotest and cleanliness control before molecular sieve loading.** Once 3A molecular sieve and silica-gel layer are loaded, water-bearing test fluids near the beds are no longer acceptable; hydrotest (PIP-024) and flushing/cleaning/drying (PIP-025) must complete and drying must be witnessed before bed loading.
- **Winterization features are construction-significant.** The aerial cooler is split-header with automated warm-air recirculation louvers, intake louvers, and a plenum heating bundle; these are installation and commissioning items, not paper features.
- **Three-tower availability protects facility throughput.** One tower in adsorption, one in regeneration, one on standby (per source Basic Scope) means construction punch-list closure should not credit "one tower complete" as mechanical completion of the package function.

## Considerations

- **Pre-commissioning interfaces.** Regen-gas heating, regen-gas cooling, and three-phase regen scrubber must be commissioned as a system; tie-ins to relief/flare/vent and drain/containment headers are required before regen can be run.
- **Heated enclosure.** Source notes that a heated building/enclosure houses the inlet gas coalescer, inline mixers, settling vessel, and regen scrubber "as required by final heater/scrubber location and area classification." This conditional drives whether building HVAC/services becomes in scope despite the current Applicability=No on that row; the CWP should re-test this assumption against final vendor general arrangement.
- **Moisture analyzer integration.** A single moisture analyzer with vaporizing regulator for C3+ sampling is in the package; sample-system tubing, vent routing, and calibration are construction interface items even though the analyzer itself is vendor-supplied.
- **Outlet water spec (< 7 ppmw)** is a process performance target; mechanical completion cannot demonstrate it, so the turnover checklist should defer that demonstration to commissioning rather than treating it as a CWP acceptance criterion.

## Trade-offs

- **Pre-loaded sieve vs. site-loaded sieve.** Source does not specify; site loading defers a hazardous, time-sensitive activity into the construction window and may extend critical path, while pre-loaded vessels constrain shipping/handling and require strict desiccation control. TBD pending vendor decision.
- **Modularization vs. stick-build of the heated enclosure.** Source does not specify; modular delivery reduces site labor but constrains transport envelopes; stick-build increases site time but accommodates final area classification adjustments. TBD pending vendor general arrangement.
- **Tie-in scheduling against live facility.** Process piping, relief/flare/vent, electrical power, and I&C tie-ins must be sequenced against the rest of the West Doe facility shutdown/turnover plan; CWP should not optimize this package's schedule in isolation.

## Examples

No worked examples are present in the available source slice. Worked examples (representative tie-in sequence, sample turnover checklist) are deferred until vendor general arrangement (MEC-016) and tie-in list (PIP-004) revisions are available.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CT-01 | Building HVAC/Services is marked Applicability=No in the source Physical Interface Summary, but the source Major Included Equipment description requires a "heated building/enclosure ... as required by final heater/scrubber location and area classification," which implies HVAC-adjacent provisioning may become necessary. | `_Sources/26020-Package_Requirements.docx` heading 22-003 Physical Interface Summary (Building HVAC/Services = No) | same heading Major Included Equipment (heated enclosure as required) | Specification R-CWP-02/R-CWP-03; Guidance Considerations | PROPOSAL: treat HVAC as conditional in-scope pending vendor general arrangement; default remains No until vendor confirms | TBD |
| CT-02 | Standards table lists API-661 (modified) as a likely basis for the aerial cooler by reference to other packages in the same source workbook, but heading 22-003 does not explicitly cite API-661 for this package. | Other heading(s) in `_Sources/26020-Package_Requirements.docx` citing API-661 (modified) for air coolers | heading 22-003 (no explicit standards list) | Specification Standards | PROPOSAL: keep API-661 as ASSUMPTION until vendor MEC-009/MEC-010 confirms | TBD |
