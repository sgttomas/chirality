# Guidance: DEL-055-03 — Construction Work Package (LP Flare KO Drum, 4-25)

## Purpose

The Construction Work Package (CWP) for PKG-055 exists because the LP flare KO drum and its transfer pump are a vendor-engineered package that must be physically integrated into the 4-25 facility. The Package Vendor owns equipment engineering, design, and documentation; the EPC Integrator owns *how the package becomes part of the operating plant*. This deliverable is the EPC Integrator's primary anchor for that integration during the construction phase and is one of the mandatory Gate 5 EPC anchor deliverables defined by user instruction. — Sources: PACKAGE_REGISTER.csv row PKG-055; `_CONTEXT.md` Notes.

It supports objectives OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (per OBJECTIVE_DELIVERABLE_MAP.csv; treated as PACKAGE_HEURISTIC association — `ASSUMPTION`).

## Principles

1. **Vendor scope is not EPC scope.** The CWP must respect the package boundary: vendor-supplied internals, instrumentation supplied with the skid, and vendor-tagged piping spools are not modified by the EPC Integrator unless specifically authorized. — PACKAGE_REGISTER.csv row PKG-055.
2. **Tie-ins are the critical path.** The LP flare KO drum sits at the convergence point of many low-pressure relief and vent sources (amine regen, TEG regen, VRU, recip compressor seal pot, primary seal vent, mole-sieve regen blowdown, VRU bypass). Workface planning must sequence tie-ins so that downstream services can be commissioned without re-opening the LP header. — DBM-Deepcut lines 1702, 1781, 1787, 1801, 2029.
3. **Freeze protection is not optional.** LP flare header sections outside heated buildings shall be electrically heat traced and insulated; PSV outlets that free-drain into the header are the only exception. Skipping or deferring EHT installation breaks DBM compliance. — DBM-Deepcut line 2033.
4. **No traps or pockets in LP flare piping.** The VRU suction header to LP flare bypass piping must free-drain without traps and slope toward the LP flare KO drum; this constrains pipe rack routing and support spacing. — DBM-Deepcut line 1787.
5. **Spacing is regulatory.** Maintain ≥10 m from vegetation or other fire hazards (OGAOM Sec. 9.6.15 via DBM). Location decisions made during construction (laydown, temporary structures, scaffolding) must not violate operating clearances. — DBM-Deepcut line 287.

## Considerations

- **LP element shares a stack with HP/cryo flares.** The LP flare is a piggy-back element on the common HP/cryo flare stack; construction sequencing must consider stack work that affects HP/cryo systems as well. — DBM line 2029.
- **Relief volumes and LP stack element OD remain TBD.** Final detailed-design values may change LP-header sizing locally near the drum or the LP nozzle on the stack; the CWP should flag header/structural changes as field-revision risks. — DBM lines 1834, 2031.
- **Truck-out routing.** LP KO drum pump (P-3900-1) has a truck-out provision and a low-pressure-header return to the condensate slop tank. Both routes must be installed and labeled to avoid construction-phase ambiguity. — DBM lines 1665, 2029.
- **Cross-facility shared-utility allocation (03-25/04-25) is TBD.** If LP flare allocations change between facilities during detailed design, the CWP may need to revise tie-in scope. — DBM line 1834.

## Trade-offs

- **Pre-fabrication vs. field assembly.** LP flare piping is large (508 mm / 20 in) but must slope to drain; field-fit at the KO drum nozzle may be preferable to fully pre-fab spools where elevation is sensitive.
- **EHT density vs. cost.** Tracing only sections "outside heated buildings" is the minimum DBM requirement; over-tracing wastes capex while under-tracing risks freeze events on cold-region winter shutdowns. — DBM line 2033.
- **Turnover granularity.** Turning over the LP KO drum as a single unit is operationally simpler, but partial turnover (drum mechanical-complete before pump electrical-complete) can unblock downstream commissioning of upstream LP-relief consumers. The workface plan should explicitly choose a strategy.

## Examples

The DBM Equipment List (lines 2577-2581) confirms the tag map used throughout this kit:

- V-3900-1: L.P. Flare K.O. Drum
- P-3900-1: L.P. Flare K.O. Drum Transfer Pump

This mirrors the HP flare package convention (V-4100-1 / P-4100-1) and the cryo flare convention (V-4110-1 with immersion heater H-4112-1), per DBM lines 2027-2029, 2577-2580.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted Sections | Proposed Authority (PROPOSAL) | Human Ruling (TBD) |
|---|---|---|---|---|---|---|
| CWP-CFL-01 | The deliverable register references "26020-Package_Requirements.docx package heading 10" as a primary source, but this Word document is not locally accessible as markdown; therefore detailed package requirements beyond DBM coverage cannot be cited at clause level in this run. | DELIVERABLE_REGISTER.csv row DEL-055-03 (Source Reference) | `_Sources/` directory (no markdown derivative of the .docx) | All four documents — clauses depending on package-specific requirements remain `TBD` | PROPOSAL: convert `26020-Package_Requirements.docx` to markdown and re-run the four-documents skill, then close `TBD` items. | TBD |
| CWP-CFL-02 | DBM line 287 cites the 10 m KO-drum/vegetation spacing under OGAOM Sec. 9.6.15, but the actual OGAOM section text is not in the locally accessible source set. | DBM-Deepcut line 287 | OGAOM Sec. 9.6.15 (not locally accessible) | Specification R-CWP-05; Guidance Principles #5 | PROPOSAL: retain DBM-stated 10 m value as design basis; verify against OGAOM during detailed design as DBM itself instructs (line 289). | TBD |
| CWP-CFL-03 | Objective-to-deliverable mapping (OBJECTIVE_DELIVERABLE_MAP.csv) lists eight objectives (OBJ-001, 004-010) against DEL-055-03, but underlying objective texts were not read in this run. Association is recorded under PACKAGE_HEURISTIC mode as ASSUMPTION. | OBJECTIVE_DELIVERABLE_MAP.csv | (objective definitions not read) | Datasheet "Supports Objectives" implication; Guidance "Purpose" | PROPOSAL: confirm objective alignment when the project objective register is opened in a later pass. | TBD |
