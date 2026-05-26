# Guidance — Construction Work Package (DEL-074-03)

> Directional guidance for the EPC Integrator team producing and consuming the Construction Work Package (CWP) for PKG-074 (Caustic Treating — NGL Mercaptan Removal). This document supports the normative `Specification.md` with rationale, principles, and trade-offs; it is not itself binding.

## Purpose

This CWP exists because the West Doe 04-25 NGL mercaptan treating unit is a current-scope EPC anchor whose physical installation, indoor caustic-containment requirements, cross-facility incinerator tie-in, and chemical hazards demand explicit construction planning beyond what the package datasheet or vendor engineered package alone can carry. The decomposition designates DEL-074-03 as a mandatory Gate 5 EPC anchor deliverable (per `DELIVERABLE_REGISTER.csv` row 272).

## Principles

1. **Source authority before convention.** Construction provisions that constrain materials, layout, or interfaces (no-aluminum rule, indoor caustic equipment, blanket-gas isolation of fresh caustic from VRU, incinerator co-location at 03-25) come from the DBM. The CWP must implement these provisions rather than substitute generic construction conventions.
2. **The package is a chemical-handling unit, not a routine mechanical install.** Construction sequencing must respect that the equipment will contact 50 wt% NaOH fresh caustic and disulphide oil. Material control, contamination control, and freeze protection are leading risks.
3. **Tie-ins are the contract surface.** The CWP's primary integration value is in cataloguing tie-ins (process, utility, vapour, electrical, controls) and assigning unambiguous completion and acceptance owners.
4. **Cross-facility coupling is real.** The incinerator that services 04-25 MTU vapours is physically at 03-25 near the flare stacks. Construction completion and operational handoff cross facility boundaries; the CWP must surface this rather than hide it inside generic utility lists.
5. **Open items are first-class.** The source basis is explicit that several items remain `TBD` (process licensor, caustic concentration confirmation, MTU floor material, caustic tank material, safety-shower count and location, detector tag lists, supplemental fuel gas rate). The CWP must carry these as open items into the turnover checklist rather than close them with assumptions.
6. **Workface logic mirrors hazard logic.** Sequence and prerequisite logic should follow hazard exposure: building enclosure before caustic-bearing equipment; hydrotest before chemical introduction; ESD/F&G commissioning before truck-in.

## Considerations

### Material and chemical
- 50 wt% NaOH fresh caustic and DSO impose material restrictions (no aluminum; SS cladding/straps in caustic exposure areas; polymer or caustic-compatible tank material). MTU building floor material remains `TBD`. Construction QA must validate material conformance at receipt and at installation.
- Spent caustic, DSO, and fresh caustic tanks are blanketed with LP fuel gas; fresh caustic tank is explicitly not connected to the VRU header to avoid VRU-vapour contamination. The CWP must coordinate piping, blanket-gas regulation, and isolation distinct from the VRU header.

### Building, layout, and access
- Caustic-containing equipment is installed indoors because of freeze and crystallization risk. The MTU building is an enabling construction prerequisite for major caustic equipment installation.
- Water safety showers are required inside the MTU, with discrete control-room alert on activation. Shower count and location are `TBD` and should be set in coordination with operability and emergency response.
- Truck-in (fresh caustic), truck-out (spent caustic, DSO), and emergency-response access must be respected by the construction logistics plan and by laydown/erection sequencing.

### Cross-facility coordination (03-25 incinerator)
- The incinerator is physically at the 03-25 facility near the flare stacks and services the 04-25 MTU. Construction completion of 04-25 vapour tie-ins is gated by 03-25 readiness. Supplemental fuel gas rate, incinerator flow basis, and shared-facility operational responsibility are open items per the DBM and should be carried forward.

### Detection, ESD, and HAZOP closeout
- Methyl mercaptan toxicity and odour are explicit hazards. LEL, H2S, methyl-mercaptan, and fire detection coverage; ESD and shutdown interfaces; voting logic and set points — all remain `TBD` until HAZOP/SIL outputs close. The CWP should expose these as turnover gates rather than push them into "operations".

### Climate and execution window
- The -40 °C winter design basis governs winterization of partially installed equipment, heat tracing energization, hydrotest fluid selection, and module-delivery / heavy-lift windows.

## Trade-offs

- **Vendor-led detailed engineering vs EPC construction sequencing.** A third-party proprietary process provider supplies the detailed engineering package. The CWP should be drafted to accommodate vendor variation in skid configuration (number of contactor stages, filter housing, drain drum integration) without re-issuing the whole construction work package. ASSUMPTION: vendor selection occurs upstream of construction issue.
- **Modular vs stick-built MTU equipment.** The decomposition does not specify a basis (`TBD`). Modular delivery reduces winter exposure and reduces field caustic-area work; stick-built reduces heavy-lift planning. The decision affects the workface plan structure.
- **DSO disposal route.** DSO is trucked out by default; pumping DSO into C5+ product is identified as a possible disposal path subject to detailed-engineering review. The CWP should accommodate the truck-out base case and flag the optional product-mix tie as a future-scope provision rather than a hidden assumption.
- **Spare bed / spare filter discipline.** Caustic outlet filters are 2 × 100 %. Mole-sieve sparing (adjacent package) is open. The CWP should not assume sparing decisions outside its own scope but should declare prerequisites.

## Examples

(Illustrative only; not normative.)

- *Example tie-in entry in the construction interface and turnover checklist:* "TI-074-MTU-V01 — Spent caustic tank vapour to 03-25 incinerator header. Mechanical completion sign-off: EPC Integrator construction superintendent. Pre-commissioning sign-off: EPC Integrator commissioning lead with 03-25 incinerator operations witness. Outstanding items at issue: supplemental fuel-gas rate `TBD`; incinerator-system operational-responsibility split `TBD`."
- *Example workface package sequencing:* "WFP-074-03 (MTU building enclosure) precedes WFP-074-05 (caustic NGL contactor setting); WFP-074-05 precedes WFP-074-08 (caustic piping hydrotest); WFP-074-08 precedes WFP-074-12 (fresh caustic introduction)."

## Conflict Table (for human ruling)

No conflicts identified at Pass 1/Pass 2 between accessible source slices, `_CONTEXT.md`, and the decomposition register row for `DEL-074-03`. The package title "NGL Mercaptan Removal" aligns with the 04-25 NGL caustic basis; no conflict with the 03-25 condensate caustic treating system (which is decomposed elsewhere). If the 03-25 condensate caustic treating unit is reassigned to this package by a future ruling, this CWP would need substantial expansion — surfaced here as a watch item rather than an active conflict.

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| (none) | — | — | — | — | — | — |
