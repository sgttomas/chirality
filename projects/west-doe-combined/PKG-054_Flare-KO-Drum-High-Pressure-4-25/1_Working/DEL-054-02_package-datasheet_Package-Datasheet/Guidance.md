# Guidance — Package Datasheet for Flare KO Drum (High Pressure) 4-25 (PKG-054)

> Directional guidance for the EPC Integrator authoring `DEL-054-02_package-datasheet`. This document explains *why* the requirements in `Specification.md` are framed as they are and the trade-offs the author should consider when interpreting source ambiguities.

## Purpose

The HP Flare KO Drum package is the technical handoff anchor between EPC and the third-party vendor or discipline designer who will engineer and supply the HP flare knock-out function for the 04-25 (Deepcut) facility. The datasheet exists so that the vendor receives a single, source-grounded statement of *what the package must do, where it connects, and what constraints govern it*, without having to mine the DBM directly.

## Principles

1. **Source over narrative.** The Deepcut DBM (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`) is the authoritative source for flare system architecture, header sizes, backpressure basis, and tags. Decomposition prose and `_CONTEXT.md` route and frame the deliverable; they do not generate design values.
2. **Carry interface facts as evidence.** The decomposition explicitly chose to fold package interfaces into this deliverable rather than create a standalone interface deliverable (`_CONTEXT.md` Notes). The datasheet should therefore include the interface requirements matrix — even if currently TBD — and not push it elsewhere.
3. **Mark, don't invent.** Where the source slice does not provide a value (vessel dimensions, design pressure, MOC, pump curve, relief load set), the datasheet records `TBD` rather than typical industry values.
4. **Preserve traceability to scope and objectives.** Every requirement should be traceable to the SOW items (`SOW-0075` through `SOW-0078`) and the package-heuristic objectives (`OBJ-001`, `OBJ-004`-`OBJ-010`).
5. **Respect the shared-stack reality.** The HP/cryo flare stack is physically at 03-25 and shared with 04-25 (DBM-Deepcut line 2030; DBM-Comp_and_Liquids line 497). The KO drum package itself sits at 04-25, but downstream routing leaves the facility. The datasheet should make this boundary explicit so the vendor's tie-in scope is unambiguous.

## Considerations

- **HP / Cryo flare module co-fabrication.** Module 410-1 packages both HP and cryogenic flare KO drums into a single shop-built skid (DBM-Deepcut line 2784). The vendor must coordinate vessel orientation, pump access, immersion-heater service (on V-4110-1) and HP truck-out access (on V-4100-1) within a single module envelope. The datasheet should not treat V-4100-1 in isolation.
- **Backpressure budget.** Estimated peak built-up backpressure on HP/cryogenic flare is 695 kPag (100 psig) at peak blowdown coinciding with the highest fire-zone load; PSV maximum total backpressure must remain under 1172 kPag (170 psig) for the 150# flange rating (DBM-Deepcut line 2044). Vendor KO drum hydraulic basis (vessel pressure drop, demister loss) must fit within this budget.
- **Freeze protection vs. PSV free-drain.** HP flare headers outside heated buildings require heat tracing and insulation *except* PSV outlets that free-drain into the header (DBM-Deepcut line 2033). Datasheet nozzle and inlet-piping basis should reflect both the heated-trace requirement on the main header and the free-drain exception at PSV outlets.
- **Spacing constraint.** OGAOM Sec. 9.6.15 requires 10 m (32 ft) minimum between flare KO drums and vegetation or other fire hazards (DBM-Deepcut line 287). This drives module placement on the plot plan and is a hard input to layout coordination.
- **Liquid disposition.** The current basis is truck-out via P-4100-1 (DBM-Deepcut line 2028). DBM-Comp_and_Liquids line 1665 also lists "flare knock-out drum pumps" as a low-pressure header source feeding the condensate slop tank, suggesting an alternative liquid route may exist at the project level. For the 04-25 HP KO drum, truck-out is the current basis; alternative routing to slop should be confirmed by the vendor/EPC interface review.
- **Sizing flows are open.** Relief volumes are explicitly TBD; preliminary Aspen Flare System Analyzer models support header sizing but not vessel sizing (DBM-Deepcut line 2021). The datasheet must record sizing flows as TBD and reference the Aspen model as the eventual source.
- **Native source files not parsed in this pass.** `26020-Package_Requirements.docx` (package heading 9) and `26020-Packages_Interfaces_4_export.xlsx` were not text-extracted in this drafting pass. Detailed design must either parse them or rely on Aspen/Deepcut DBM where overlap exists. Items derived solely from those native files are TBD.

## Trade-offs

- **Single datasheet vs. separate vessel + pump datasheets.** Carrying V-4100-1 and P-4100-1 in one package datasheet matches the modular delivery basis (Module 410-1) but creates a denser document; vendors often expect separate equipment datasheets. The EPC Integrator should produce vendor-facing equipment datasheets *derived from* this package datasheet, not in place of it.
- **Backpressure assumption vs. measured / modeled.** The 695 kPag value is a project-wide estimate at peak blowdown coincident with highest fire-zone load. Using it as the vessel design backpressure is conservative for early sizing but should be replaced with the case-specific Aspen output when available.
- **Truck-out vs. routed liquid disposal.** Truck-out simplifies the package interface scope (no live tie-in to slop / condensate systems) but creates an operational liability (truck access, recordkeeping). Routed disposal would shift work to the EPC scope and may be revisited during detailed design.
- **PACKAGE_HEURISTIC objective association.** Objectives `OBJ-001, OBJ-004..OBJ-010` are inherited from the package row in the GATE-07 register and labeled ASSUMPTION per skill default (`OBJECTIVE_ASSOCIATION_MODE = PACKAGE_HEURISTIC`). A future tightening to deliverable-ID-level mapping may narrow this set.

## Examples

- A reference passage to cite when stating header size at the vessel:
  > "508 mm (20 in) relief header and HP flare KO drum V-4100-1; HP KO drum pump P-4100-1 and truck-out provided; HP flare combines with cryogenic flare before common stack." — `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2028 (Sec. Flare Equipment and Routing).
- A reference passage to cite for spacing:
  > "Distance between flare tanks, including KO drums, and vegetation or other fire hazards | 10 m (32 ft) | OGAOM, Sec. 9.6.15" — same source, line 287 (Sec. Flare and Incinerator Spacing).

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-01 | HP KO drum liquid disposition: truck-out only vs. routing to condensate slop via "flare knock-out drum pumps". | DBM-Deepcut line 2028 (Flare Equipment and Routing) — truck-out provided | DBM-Deepcut line 1665 (Condensate slop tank) — "Low-pressure header sources include flare knock-out drum pumps..." | Datasheet — Attributes (Liquid disposition), Construction; Guidance — Considerations | PROPOSAL: Treat truck-out as the primary disposition for the 04-25 HP KO drum (V-4100-1); the slop-tank routing language in line 1665 likely refers to LP KO drum pumps. Confirm with EPC process lead. | TBD |
| CONF-02 | Package decomposition name "Flare KO Drum (High Pressure) 4-25" maps to DBM tag-table row "Flare KO Drum (High Pressure) 2". | `_CONTEXT.md` / GATE-07 register: PKG-054 — "Flare KO Drum (High Pressure) 4-25" | DBM-Deepcut lines 2534, 2579-2580 — "Flare KO Drum (High Pressure) 2" tagged 4-25 (Deepcut) with V-4100-1 / P-4100-1 | Datasheet — Identification | PROPOSAL: Treat them as the same package (tag-table "2" denotes the 04-25 instance per facility column); naming difference is a register/source convention. | TBD |
| CONF-03 | Pump sparing basis "1 x 100 percent" stated for 03-25 HP flare KO drum transfer pumps; not explicitly stated for 04-25 V-4100-1 / P-4100-1. | DBM-Comp_and_Liquids line 583 — "One per KO drum, 1 x 100 percent" | DBM-Deepcut line 2028 — silent on sparing count | Datasheet — Attributes (Pump sparing) | PROPOSAL: Apply the 1 x 100% project basis to P-4100-1 as ASSUMPTION pending detailed design / vendor confirmation. | TBD |
