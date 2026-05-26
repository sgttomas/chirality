# Guidance — DEL-081-02 Package Datasheet (Flare KO Drum (High Pressure) 3-25)

## Purpose

The Package Datasheet exists to carry, in one EPC-Integrator-owned artifact, the technical handoff information a Package Vendor needs to perform package engineering, design, vendor documentation, and physical equipment supply for the two HP flare KO drums (`V-4100-2`, `V-4150-2`) and their dedicated transfer pumps (`P-4100-2`, `P-4150-2`) in the 3-25 facility. It is the upstream technical anchor for `DEL-081-04` (Vendor Engineered Equipment Package) and the technical basis against which `DEL-081-06` (EPC Vendor Package Review and Acceptance) is checked. [Source: `_CONTEXT.md`; PACKAGE_REGISTER.csv row 54; DELIVERABLE_REGISTER.csv rows 289-293]

Per the deliverable note, interface facts for this package are intentionally carried here as evidence rather than as standalone interface deliverables. [Source: `_CONTEXT.md` §Notes]

## Principles

1. **Source-anchored, not invented.** Every numeric value, tag, and material requirement should be traceable to a locally accessible source slice or marked `TBD` / `ASSUMPTION` with the reason. The accessible DBM (`3-25_Comp_and_Liquids_DBM.md`) provides tag identity, header size, redundancy configuration, and design-margin basis; numeric design pressure/temperature/sizing values are not in the accessible slice.
2. **Carry interface facts as evidence.** This package datasheet is the canonical landing place for the ten interface types listed in PACKAGE_REGISTER.csv row 54 for `PKG-081`; the datasheet should populate the interface matrix rather than defer to a separate document.
3. **Respect the responsibility split.** Document what the Package Vendor needs to design and what the EPC Integrator retains (tie-ins, facility integration, constructability). [PACKAGE_REGISTER.csv row 54]
4. **Stagger with system-level basis.** HP relief is part of a staggered blowdown scheme on a shared HP/Cryo+LP dual flare stack with 04-25; per-drum sizing is meaningful only against the system-level relief and blowdown studies governed by `W242510-PRC-REP-000003-001`. [DBM §"Flare and Blowdown"]
5. **Prefer redundancy as declared.** Use the project basis "one transfer pump per drum, 1 x 100 percent". Do not invent alternative redundancy (2 x 100, 2 x 50) without a HAZOP/operations ruling. [DBM §"Pump Counts"]

## Considerations

- **Sour service confirmation.** Facility isolation philosophy contemplates sour hydrocarbon service. Material selection, NACE applicability, and vent/drain routing class for KO drum internals depend on the confirmed service envelope. [DBM §isolation philosophy (line 607)]
- **HP header size convention.** The project carries the HP relief header at 508 mm / 20 inch. KO drum inlet connections and isolation should be consistent with this. [DBM §"Flare and Blowdown" (line 499)]
- **Liquid management.** Pump discharge is "truck-out or transfer to slop"; the datasheet should make clear which mode applies at each KO drum location (compressor area vs tank farm) since site logistics differ. [DBM §"Flare and Blowdown"]
- **Foundation/structural inputs.** Vessel and pump foundation design requires the final geotechnical report and project wind/snow/seismic criteria; do not commit values not declared by project civil. [DBM §"Foundations" (line 700)]
- **Inaccessible sources.** `Bid Docs/Budgetary/24292-02-PT-ENR-17-201_HP FKOD_R2.pdf` is cited in PACKAGE_REGISTER as a budgetary go-by but is not in the workspace `_Sources/` tree. It is the most likely carrier of indicative size/pressure values and should be retrieved before the datasheet is finalized.

## Trade-offs

- **Datasheet completeness now vs deferral.** Completing the datasheet now with TBDs preserves vendor solicitation timing but increases the risk of late vendor rework when blowdown studies finalize. The alternative — waiting for `W242510-PRC-REP-000003-001` and final flare studies — delays Gate 5 EPC anchor work. The project's intent (mandatory Gate 5 EPC anchor) implies issuing with TBDs and updating, not waiting. [Source: `_CONTEXT.md` §Notes]
- **Single budgetary go-by vs full datasheet rebuild.** The budgetary PDF (`24292-02-PT-ENR-17-201_HP FKOD_R2.pdf`) is labeled "budgetary pricing/delivery go-by only" in PACKAGE_REGISTER.csv row 54; values from it should be treated as indicative until reconfirmed against final process basis.

## Examples

- DBM-line example: "HP headers route to HP KO drums V-4100-2 in the compressor area and V-4150-2 in the tank farm; both manifold to the HP flare." [`3-25_Comp_and_Liquids_DBM.md` line 497] — this is the canonical sentence that should drive the package's process-flow narrative in the datasheet.
- Redundancy example: "HP flare KO drum transfer pumps — One per KO drum, 1 x 100 percent." [DBM line 583] — sets the pump configuration field.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-01 | Whether sour-service (NACE MR0175 / ISO 15156) applies to HP flare KO drum internals. DBM isolation language implies "sour hydrocarbon service" is a credible case but does not assert it for HP flare KO drum specifically. | `3-25_Comp_and_Liquids_DBM.md` §isolation (line 607) | (no positive opposing source) | Datasheet §Conditions; Specification §R3 | HAZOP / process specialist ruling | TBD |
| C-02 | Indicative design pressure/temperature values. Budgetary go-by `24292-02-PT-ENR-17-201_HP FKOD_R2.pdf` is cited but not in `_Sources/`. | PACKAGE_REGISTER.csv row 54 (cites budgetary PDF as go-by) | No accessible source carries numeric values | Datasheet §Conditions | Retrieve budgetary PDF; confirm against final flare studies | TBD |
| C-03 | Final blowdown sequencing and HP relief load. `W242510-PRC-REP-000003-001` is required but not accessible. The same document number appears in a prime-mover/emissions context elsewhere in the DBM, which the DBM itself flags as a cross-reference conflict. | DBM §"Flare and Blowdown" (line 501) | DBM §"Prime Mover Basis" (cross-reference conflict note) | Datasheet §Conditions; Specification §R2 | Retrieve `W242510-PRC-REP-000003-001` and confirm scope | TBD |
