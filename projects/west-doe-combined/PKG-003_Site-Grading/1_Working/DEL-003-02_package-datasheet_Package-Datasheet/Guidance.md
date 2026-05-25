# Guidance: DEL-003-02_package-datasheet — Package Datasheet

## Purpose

This guidance supports conservative preparation and use of the `PKG-003` Site Grading Package Datasheet. The datasheet is an EPC Integrator handoff artifact: it should make the accepted package identity, source-supported civil grading basis, interface facts, and unresolved design inputs visible for third-party vendor or discipline package engineering and design.

## Principles

| Principle | Guidance |
|---|---|
| Preserve source authority | Treat workbook row 4, accepted Gate 7 registers, and DBM SEC-11 civil/grading content as the evidence basis. Do not convert general civil practice into package-specific requirements unless the source slice supports it. |
| Keep interface facts visible | Drain / Containment and Grading / Site Drainage / Spill Containment are the package-specific workbook interface facts carried by this datasheet. They should remain visible in the interface matrix and verification checks. |
| Separate package data from final design | The datasheet can carry current grading and drainage design principles, but final geotechnical values, survey model details, hydrology values, retention pond sizing, and final pond location remain open until their source dependencies are accepted. |
| Maintain TBD discipline | Where the DBM explicitly leaves values open, keep them as `TBD`. Do not backfill them from convention or from another package. |
| Use objectives as context | `OBJ-001`, `OBJ-007`, `OBJ-008`, and `OBJ-009` explain why the package matters, but they are not substitutes for source-supported design values. |

## Considerations

- The accepted Gate 5 basis makes the Package Datasheet mandatory for every approved package and states that package datasheets carry the technical handoff basis for third-party vendor or discipline package engineering and design.
- The DBM states that civil and structural basis must be applied consistently across project buildings, equipment supports, foundations, roads, and drainage works, while incorporating more specific requirements from the geotechnical report, topographical survey, plot plan, or detailed engineering analyses when those become available.
- The site grading package has drainage and containment interfaces but no separate package-specific exclusions stated in the accessible source set.
- The DBM requires operations plans and procedures for release monitoring, analysis, and confirmation of non-contaminated surface water before removal or pump-out activities. This datasheet should flag the interface, but operating procedure ownership is `TBD` unless assigned by a later accepted source.
- Supporting 03-25 civil context confirms the same general civil themes for grading, drainage, roads, surface-water management, retention pond, foundations, fencing, and security, but the package is WBS 01 and should be governed primarily by the 04-25 Deepcut basis.

## Trade-offs

| Topic | Trade-off / handling |
|---|---|
| Current grading values vs. final geotechnical report | Use current DBM values for handoff, but preserve the geotechnical report as the closure authority where the DBM says parameters are pending. |
| Pad slope | Carry 1.5% from pipe racks as the default facility pad slope, with the source-supported allowance to reduce to 1.0% where required to maintain reasonable top-of-pile-cap elevations. |
| Maximum grade slope | Carry 3H:1V as the current maximum unless specifically engineered or mandated otherwise by the geotechnical report. |
| Retention pond | Carry the requirement to direct and contain on-site overflow into a retention pond, but keep location and capacity `TBD` pending plot-plan coordination and detailed drainage engineering. |
| Interface breadth | Keep the package interface matrix to source-supported interface facts. Do not add structural/foundation/support or other workbook columns unless later evidence adds them for row 4. |

## Examples

TBD. No package-specific completed datasheet example was available in the local truth set or accessible source slices.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| None identified | No direct source conflict identified during P1/P2 drafting. Open items are source-declared TBDs rather than conflicts. | N/A | N/A | N/A | N/A | N/A |
