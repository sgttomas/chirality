# Guidance: DEL-007-03 Construction Work Package

## Purpose

The Construction Work Package translates the accepted PKG-007 Retention Pond basis into construction-facing instructions, checks, and turnover evidence. It exists to make the civil retention pond work buildable, inspectable, and handoff-ready while preserving known source limitations.

## Principles

- Treat the Gate 7 decomposition registers as the accepted package and deliverable basis.
- Treat accessible DBM source slices as the authority for civil, drainage, retention pond, and regulatory constraints.
- Preserve the distinction between source-supported requirements and construction details that remain TBD.
- Keep the two declared PKG-007 interfaces visible through workface planning and turnover: Drain / Containment and Grading / Site Drainage / Spill Containment.
- Do not convert objective mappings into clause-level construction requirements unless the source basis supports the requirement.
- Use the CWP to surface unresolved hydrology, geotechnical, layout, pond location, pond capacity, and regulatory items before construction closure.

## Considerations

The DBM basis confirms that the current rainfall basis uses NBCC 2020 Dawson Creek intensity-duration-frequency data as a proxy and that civil drainage, retention pond sizing, and surface-water management carry uncertainty until final hydrology inputs are confirmed. The CWP should therefore avoid presenting pond size, final capacity, final location, or detailed drainage dimensions as settled unless a later approved source supplies those values.

The civil basis requires surface-water management to prevent uncontrolled offsite discharge, protect process areas, and support construction and operations access. It also states that process-contaminated drainage must route to the appropriate drain or containment system rather than surface-water discharge. Construction planning should treat this as a segregation and verification problem, not only as earthworks execution.

The Gate 7 package row identifies Retention Pond as a Civil WBS 02 package with Drain / Containment and Grading / Site Drainage / Spill Containment interfaces. The construction package should make those interfaces explicit in workface planning, inspection hold points, and turnover checklists.

## Trade-offs

| Topic | Guidance |
|---|---|
| Source fidelity vs. completeness | Prefer `TBD` and open-item tracking over filling in pond dimensions, elevations, slopes, or discharge criteria not present in the accessible source basis. |
| Construction readiness vs. design closure | The CWP can define records, hold points, and interface checks before detailed design closure, but final construction release depends on approved hydrology, drainage, geotechnical, and layout inputs. |
| Surface-water management vs. contaminated drainage | Keep uncontaminated surface-water controls separate from process-contaminated drainage routing and containment. |
| Objective coverage vs. enforceable requirements | OBJ-002, OBJ-007, OBJ-008, OBJ-009, and OBJ-010 provide context for why the deliverable matters, but the CWP requirements should be tied to cited package, interface, artifact, and DBM source slices. |

## Examples

| Example item | Acceptable treatment |
|---|---|
| Pond capacity | `TBD pending final hydrology inputs and detailed drainage design`; do not invent a capacity. |
| Pond location | `TBD pending plot plan/civil layout coordination`; do not infer from package name alone. |
| Drain / containment tie-in | Identify as a declared interface and include owner/status/hold point fields; exact tie-in point remains TBD unless supplied by detailed design. |
| Regulatory review | Carry as an open item covering BC water, watercourse, diversion, discharge, produced-water handling, stormwater management, and related requirements until detailed regulatory review closes it. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-001 | `_REFERENCES.md` says no deliverable-specific source slices were copied, but accessible project sources contain relevant DBM and register evidence. | `_REFERENCES.md`, Missing / Deferred References | Gate 7 registers and `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` | All four documents | Use Gate 7 registers and accessible DBM slices as accepted upstream/local sources; keep missing detailed values as TBD. | TBD |
