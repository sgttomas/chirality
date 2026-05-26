# Specification: DEL-102-03 — Construction Work Package (PKG-102)

## Scope

This specification governs the EPC Integrator Construction Work Package (CWP) for PKG-102 Monolithic Concrete Foundations. The CWP defines how the package's monolithic concrete foundation scope is physically installed, built, inspected, turned over to commissioning, and tied into adjacent facility systems.

**Includes:**
- Workface planning for cast-in-place monolithic concrete foundation installation within PKG-102.
- Construction interface management at the two declared package interface types (Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports). Source: INTERFACE_REGISTER.csv rows `IFC-1EDEDC0453`, `IFC-8283744B5B`.
- Construction inspection, hold points, and turnover documentation for PKG-102.

**Excludes:**
- Detailed structural design of foundations (governed by the structural design deliverables under the Structural discipline; not produced by this CWP).
- Procurement of bulk materials beyond what the CWP coordinates at the workface.
- Items outside PKG-102 scope; cross-package interfaces are coordinated but not designed here.
- Package-specific exclusions: TBD — none stated in source materials (PACKAGE_REGISTER.csv row `PKG-102`).

## Requirements

| ReqID | Requirement | Basis (Source) | Type |
|---|---|---|---|
| R-1 | The CWP shall implement foundation construction in accordance with CSA A23.1/A23.2 (concrete materials, construction, and testing). | DBM-Deepcut/4-25_Deepcut_DBM.md §"Governing Civil and Structural Basis" (line ~2677) | NORMATIVE |
| R-2 | Structural design values used at the workface (rebar, embeds, anchor bolts, dimensions) shall be obtained from approved CAN/CSA A23.3 design output documents (issued-for-construction structural drawings). | DBM-Deepcut/4-25_Deepcut_DBM.md §"Governing Civil and Structural Basis" (line ~2674) | NORMATIVE |
| R-3 | Foundation engineering inputs (bearing capacity, lateral resistance, frost depth, settlement criteria) shall be those of the project geotechnical report; the CWP shall not proceed with foundation pours that depend on geotechnical values still marked TBD. | DBM-Deepcut/4-25_Deepcut_DBM.md §"Geotechnical and Topographical Assumptions" (lines ~2685-2696); Canadian Foundation Engineering Manual (line ~2675) | NORMATIVE |
| R-4 | Where a structure historically supported on driven steel piles is converted, in detailed engineering, to a monolithic concrete bearing foundation, the CWP shall include the change basis (which equipment, why, and the supporting analysis) before construction. | DBM-Deepcut/4-25_Deepcut_DBM.md §"Piles and Foundations" (lines 2740-2749) | ASSUMPTION (interpretive: DBM default is driven steel piles; monolithic concrete usage requires explicit basis) |
| R-5 | Construction-tie-in evidence shall be produced for each declared package interface type and shall demonstrate physical, geometric, and dimensional compatibility with the adjacent package scope. | INTERFACE_REGISTER.csv rows `IFC-1EDEDC0453`, `IFC-8283744B5B`; `_CONTEXT.md` Anticipated Artifacts | NORMATIVE |
| R-6 | A construction interface and turnover checklist (ART-66649A8AE4) shall be completed and accepted before the package is turned over to commissioning. | ARTIFACT_REGISTER.csv `ART-66649A8AE4`; `_CONTEXT.md` Anticipated Artifacts | NORMATIVE |
| R-7 | An installation and tie-in workface plan (ART-E8798F2006) shall exist and be issued for construction before any foundation pour begins. | ARTIFACT_REGISTER.csv `ART-E8798F2006`; `_CONTEXT.md` Anticipated Artifacts | NORMATIVE |
| R-8 | Building/equipment loading assumptions used to verify the as-built foundations shall conform to the National Building Code of Canada for snow, rain, wind, and seismic loads, with project-site values taken from the structural design package. | DBM-Deepcut/4-25_Deepcut_DBM.md §"Governing Civil and Structural Basis" (line 2672); §"Buildings and Miscellaneous Facilities" (line ~2753) | NORMATIVE |
| R-9 | Construction shall respect site grading and surface water management requirements at and adjacent to foundations, including pad slopes (1.5% nominal, 1.0% allowed where required to maintain reasonable top-of-pile-cap elevations) and tank-farm dike interfaces. | DBM-Deepcut/4-25_Deepcut_DBM.md §"Site Grading and Surface Water Management" (lines ~2706-2722) | NORMATIVE |
| R-10 | Concrete mix design, cold-/hot-weather concreting controls, curing, and tolerances shall be documented per CSA A23.1; specific project values are TBD pending issued-for-construction concrete specifications. | DBM-Deepcut/4-25_Deepcut_DBM.md §"Governing Civil and Structural Basis" (line ~2677); location TBD | NORMATIVE (with TBD inputs) |

## Standards

| Standard | Application | Source |
|---|---|---|
| National Building Code of Canada | Building/loading code | DBM-Deepcut/4-25_Deepcut_DBM.md line 2672 |
| CAN/CSA A23.3 | Concrete structural design | DBM-Deepcut/4-25_Deepcut_DBM.md line 2674 |
| CSA A23.1 / A23.2 | Concrete materials, construction, testing | DBM-Deepcut/4-25_Deepcut_DBM.md line 2677 |
| Canadian Foundation Engineering Manual | Foundation engineering | DBM-Deepcut/4-25_Deepcut_DBM.md line 2675 |
| CAN/CSA-S16 | Steel design (for steel embeds, baseplates) | DBM-Deepcut/4-25_Deepcut_DBM.md line 2673 |
| CSA G40.20/G40.21 (350W / 300W) | Embed/baseplate material grades — location TBD for application to anchor bolts and embeds | DBM-Deepcut/4-25_Deepcut_DBM.md line 2676 |

## Verification

| ReqID | Verification Approach |
|---|---|
| R-1 | Concrete materials and placement records audited against CSA A23.1/A23.2; cylinder break results retained. |
| R-2 | Field verification against IFC structural drawings; deviation log managed under Management of Change. |
| R-3 | Documented hold point — no concrete pour authorized until geotechnical TBDs affecting that foundation are resolved. |
| R-4 | Change-basis package on file in the CWP record set when monolithic concrete substitutes for the driven-pile default. |
| R-5 | Interface walkdowns at both declared interface types (Grading/Drainage/Spill; Structural/Foundations/Supports) with sign-off by the adjacent package representatives. |
| R-6 | Turnover checklist (ART-66649A8AE4) signed and filed before commissioning handover. |
| R-7 | Workface plan (ART-E8798F2006) status: Issued-for-Construction at pour authorization gate. |
| R-8 | Cross-check of structural design loads against NBCC site values; included in construction record. |
| R-9 | As-built survey of foundation tops and adjacent pad grades against design slopes. |
| R-10 | Concrete pre-pour checklist (mix ticket, ambient conditions, curing plan) signed at each pour; cylinder testing per CSA A23.2. |

## Documentation

Required documentation produced or assembled by this deliverable:

- ART-009507D767 — Construction work package document set
- ART-E8798F2006 — Installation and tie-in workface plan
- ART-66649A8AE4 — Construction interface and turnover checklist
- Concrete pour records, cylinder test reports, non-conformance reports, and interface walkdown sign-offs (TBD format — location TBD in accessible sources)
