# Guidance — DEL-097-03 Construction Work Package (Tanks, Condensate, API 650, 3-25)

## Purpose

The Construction Work Package (CWP) is the EPC Integrator's mandatory deliverable describing **how** the PKG-097 condensate tank package will be physically installed, inspected, tied in, and turned over to commissioning at the 3-25 area. It is the bridge between the vendor-engineered tank package (`DEL-097-04`) and operational readiness, and it captures the construction interfaces that connect this package to the rest of the facility. (Source: `_CONTEXT.md` Scope; Gate 7 PROJECT_DECOMP DELIVERABLE_REGISTER row for `DEL-097-03`.)

## Principles

- **Modified API 650 governs the tank.** The PKG-097 source slice states the tanks are designed and fabricated to modified API 650; the CWP must not invent or relax tank-erection acceptance criteria.
- **API 2000 governs the blanket-gas system.** Blanket-gas tie-ins, vent sizing, and PVRV/EPRV interaction with the blanket-gas / VRU header must remain consistent with API 2000 framing in the source slice.
- **The 90% fill limit is an installed protection, not a procedural one.** The CWP must ensure overfill protection is physically installed, loop-checked, and function-tested before turnover.
- **Coating integrity is non-substitutable.** Devchem 253 internal coating protects the tank from condensate; coating QC must be evidenced before mechanical completion.
- **Interfaces are first-class.** PKG-097 has an explicit interface source (`26020-Packages_Interfaces.3.xlsx`); the CWP is the place where each interface becomes a workface task with a punch-list line.

## Considerations

- **Vendor scope vs. EPC scope.** Tank fabrication / shop testing is vendor scope (`DEL-097-04`); field erection, tie-ins, coating touch-up, and commissioning handoff are EPC scope. The CWP must keep this boundary explicit so vendor-document items are not duplicated as EPC inspections.
- **Civil interfaces.** Foundations, containment berms, grading typically precede tank erection. The PKG-097 source slice does not state the upstream civil package; downstream resolution against `Dependencies.csv` is needed (currently not generated; see `_DEPENDENCIES.md`).
- **Winter operability.** The source slice notes a recycle may be required to maintain a temperature during winter. The CWP should ensure that any associated piping / instrumentation tie-ins are installed and function-tested even though detailed sizing is not in the PKG-097 source slice.
- **Relief device population.** Each tank carries both a PVRV (modulating / vacuum) and an EPRV (single worst-case); the CWP must verify both are installed, set, and witnessed — not one in lieu of the other.

## Trade-offs

- **Pre-coated vs. field-coated interior surfaces.** Shop coating reduces field weather risk but limits field weld repair; the PKG-097 source slice does not direct one path. The CWP should record the chosen approach and the corresponding inspection regime. (ASSUMPTION; not in source.)
- **Hydrotest medium and timing.** Hydrotest before or after coating affects coating risk and water-handling logistics. Choice is project-specific and **TBD** in the PKG-097 source slice.
- **Sequencing of tank erection across the four tanks.** Parallel vs. serial erection trades schedule for crew/crane utilization and tie-in window. **TBD** at this stage; should be resolved in the workface plan.

## Examples

- A typical CWP table of contents for a modified API 650 atmospheric storage tank package includes: scope, references, organization & responsibilities, sequencing, installation procedures per discipline, NDE & hydrotest plan, coating QC, relief device installation & testing, blanket-gas commissioning, interface / tie-in matrix, punch-list & turnover, and records index. (ASSUMPTION: typical EPC structure; not stated in PKG-097 source slice.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-01 | "modified API 650" — the specific deltas vs. base API 650 are not enumerated in the locally accessible source slice. | `26020-Package_Requirements.docx` §`26020-03-PT-19-006` (states "modified API 650") | Base API 650 standard text — not in `_Sources` (location TBD) | Specification R-2.1, R-5.1; Procedure §Steps (NDE/hydrotest) | PROPOSAL: treat modified API 650 as the governing standard at the PKG-097 level; defer enumeration of deltas to a vendor-package document review under `DEL-097-04`. | TBD |
| C-02 | Objective association (OBJ-002…OBJ-010) is package-grouped; explicit deliverable-level objective mapping is not enumerated in `OBJECTIVE_DELIVERABLE_MAP.csv` in a way that names DEL-097-03 individually for every listed objective. | `_CONTEXT.md` Supports Objectives | `OBJECTIVE_DELIVERABLE_MAP.csv` (package-grouped) | Specification R-7; Procedure prerequisites | PROPOSAL: keep the listed objectives as directional context (ASSUMPTION via PACKAGE_HEURISTIC); do not bind requirements to specific objectives without confirmation. | TBD |
| C-03 | Civil / foundation upstream is implied but not declared. | `_CONTEXT.md` (silent on upstream civil) | `_DEPENDENCIES.md` (no declared upstream) | Specification R-7.2; Procedure Prerequisites | PROPOSAL: add upstream civil package(s) to declared dependencies after `Dependencies.csv` is generated. | TBD |
| C-04 | Site / ambient / seismic / wind design data needed for construction sequencing is absent from the PKG-097 source slice. | `26020-Package_Requirements.docx` §`26020-03-PT-19-006` (silent) | Project basis-of-design — not opened in this pass (location TBD) | Datasheet §Conditions; Specification R-5; Procedure §Prerequisites | PROPOSAL: open `_Sources/DBM-*` design-basis documents in a later pass and update. | TBD |
