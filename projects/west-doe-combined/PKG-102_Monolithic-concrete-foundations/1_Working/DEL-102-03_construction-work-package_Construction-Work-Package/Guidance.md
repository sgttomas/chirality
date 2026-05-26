# Guidance: DEL-102-03 — Construction Work Package (PKG-102)

## Purpose

This deliverable exists so the EPC Integrator can plan, execute, inspect, and turn over the physical construction of monolithic concrete foundations (PKG-102) and demonstrate clean physical integration with adjacent packages — particularly site grading/drainage/spill-containment and other structural/foundation/support packages. It is the Gate 5 EPC anchor deliverable for this package.

Source: `_CONTEXT.md` Scope; DELIVERABLE_REGISTER.csv row `DEL-102-03`; PACKAGE_REGISTER.csv row `PKG-102`.

## Principles

- **Workface plan precedes pour.** No concrete pour is authorized without an Issued-for-Construction workface plan (ART-E8798F2006). Source: `_CONTEXT.md` Anticipated Artifacts; Specification R-7.
- **Design authority is the structural package, not the CWP.** The CWP executes against IFC drawings produced under CAN/CSA A23.3; it does not originate design values. Source: DBM-Deepcut/4-25_Deepcut_DBM.md §"Governing Civil and Structural Basis" (line ~2674).
- **Geotechnical TBDs are gating.** Bearing capacity, LPILE curves, and dynamic criteria are TBD pending the geotechnical report; foundations depending on those values cannot be poured until resolved. Source: DBM-Deepcut/4-25_Deepcut_DBM.md §"Geotechnical and Topographical Assumptions" (lines ~2685-2696).
- **Interfaces are the package's external face.** Both declared interface types — Grading/Site Drainage/Spill Containment and Structural/Foundations/Supports — require evidenced walkdowns and turnover records. Source: INTERFACE_REGISTER.csv rows `IFC-1EDEDC0453`, `IFC-8283744B5B`.
- **Code-of-record discipline.** All concrete materials, placement, and testing records must trace to CSA A23.1/A23.2; structural design references to CAN/CSA A23.3; loading to NBCC. Source: DBM-Deepcut/4-25_Deepcut_DBM.md §"Governing Civil and Structural Basis".

## Considerations

- **Default plant foundation basis is driven steel piles** (DBM line 2740). PKG-102's existence as a distinct "Monolithic concrete foundations" package implies a project-defined subset of foundations that depart from the pile default — the CWP should make that subset explicit and trace each monolithic foundation to its design basis.
- **Concrete-bearing equipment classes documented in the DBM** include transformers (precast concrete bearing) and compressors (precast concrete block on driven piles, subject to dynamic analysis) (DBM lines 2745-2747). Whether any of these equipment foundations are within PKG-102 scope or in a separate precast package is not explicit in accessible sources — see Conflict Table C-1.
- **Pad grading interacts with foundation top elevations.** Pad slope may be reduced from 1.5% to 1.0% to maintain reasonable top-of-pile-cap elevations (DBM line 2710). The CWP should coordinate top-of-foundation elevations with the grading package early.
- **Spill containment proximity.** For NGL storage and similar areas, surface-control features (berms, declines) interact with foundation footprints (DBM line 2722). The Grading/Drainage/Spill interface walkdown should consider these.
- **Cold-weather concreting** is governed by CSA A23.1 but specific project provisions (heating, hoarding, accelerators) are TBD — location TBD in accessible sources. Plan a project-specific cold-weather concreting addendum if construction season extends into Canadian winter conditions.

## Trade-offs

- **Monolithic cast-in-place vs. precast.** DBM uses precast for transformers and compressor blocks. Monolithic (cast-in-place) is typically chosen for larger mat/spread foundations, equipment with complex anchor patterns, or where transportation of precast units is impractical. Trade-off: cast-in-place increases schedule sensitivity to weather and cure time; precast shifts effort to off-site fabrication and lift planning. Source: DBM §"Piles and Foundations" (lines 2740-2749); the explicit monolithic/precast trade-off itself is an ASSUMPTION (industry convention) — location TBD in accessible sources.
- **Pour sequencing vs. interface readiness.** Pouring a foundation before adjacent grading is complete simplifies access but risks edge damage and rework; pouring after grading risks finished-grade damage from concrete activities. The workface plan should sequence per the interface walkdown outcome.
- **Pad-slope flexibility (1.5% vs. 1.0%).** Choosing 1.0% to keep top-of-pile-cap elevations reasonable trades drainage performance for construction practicality (DBM line 2710); this must be a deliberate, documented choice.

## Examples

- **Compressor concrete block (illustrative, not necessarily in PKG-102 scope).** DBM specifies precast concrete block on driven steel piles, subject to dynamic analysis (line 2746). If detailed engineering substitutes a monolithic block for this equipment class, the change basis required by Specification R-4 applies.
- **Transformer bearing foundation (illustrative).** DBM specifies precast concrete bearing foundations for transformers (line 2745). A monolithic cast-in-place alternative would similarly require a documented change basis.

(No additional examples available from accessible sources — TBD.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| C-1 | "Monolithic concrete foundations" is the PKG-102 PackageName, but the accessible DBM (§"Piles and Foundations", lines 2740-2749) defaults to driven steel piles and uses precast (not monolithic cast-in-place) for transformers and compressor blocks. Which specific foundations belong to PKG-102 is not explicit. | PACKAGE_REGISTER.csv row `PKG-102` (PackageName = "Monolithic concrete foundations") | DBM-Deepcut/4-25_Deepcut_DBM.md §"Piles and Foundations" (lines 2740-2749) | Datasheet Construction; Specification R-2, R-4; Guidance Principles, Considerations | Treat PKG-102 as the package container for any monolithic cast-in-place foundations identified by detailed structural engineering; populate the specific list during structural design. PROPOSAL. | TBD |
| C-2 | OBJ-001, OBJ-008, OBJ-010 associations come from PACKAGE_HEURISTIC (decomposition uses package-grouped objective mapping). Individual deliverable-to-objective evidence not present in accessible sources. | `_CONTEXT.md` "Supports Objectives" | OBJECTIVE_DELIVERABLE_MAP.csv (package-grouped mapping) | Datasheet Identification | Accept as ASSUMPTION per RuntimeOverrides `OBJECTIVE_ASSOCIATION_MODE: PACKAGE_HEURISTIC`. | TBD |
| C-3 | Source materials in `_Sources/` include `26020-Package_Requirements.docx` and `26020-Packages_Interfaces_4_export.xlsx` that were not accessed in this pass (binary formats; not converted to a locally accessible text form). They may contain package-specific construction or interface requirements that should refine Specification R-5, R-9, and Guidance Considerations. | `_REFERENCES.md` Shared Source Root | `_Sources/26020-Package_Requirements.docx`; `_Sources/26020-Packages_Interfaces_4_export.xlsx` | Datasheet References; Specification R-5, R-9, R-10 | Convert these to locally accessible markdown/CSV in a follow-up pass; re-open this deliverable to incorporate. | TBD |
