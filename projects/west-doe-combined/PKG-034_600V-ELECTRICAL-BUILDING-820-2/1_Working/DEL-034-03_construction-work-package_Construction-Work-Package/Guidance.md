# Guidance: DEL-034-03_construction-work-package

## Purpose

The Construction Work Package exists to convert the accepted Gate 7 package basis for `PKG-034` into a construction-facing deliverable that describes how the 600V ELECTRICAL BUILDING (820-2) package is physically installed, built, inspected, turned over, and tied into the larger facility systems. It should make EPC construction and turnover scope explicit while keeping vendor-owned package design with the Package Vendor.

## Principles

- Preserve source spelling and identity. The package name is carried as "600V ELECTRICAL BUILDING (820-2)" because that is the workbook and Gate 7 register spelling.
- Treat the Construction Work Package as construction-facing only. Do not redefine package design values; accept the Package Datasheet (`DEL-034-02`) as the technical handoff basis.
- Treat workbook interface `X` facts as construction-facing tie-in scope items, covering all twelve PKG-034 interfaces.
- Keep vendor-owned design work with the Package Vendor and facility-level construction integration with the EPC Integrator.
- Use `TBD` for installation plot-plan location, modularization/shipping split, lifting plan, ITPs, hold points, package-specific feeder/conductor/conduit detail, foundation/support detail, building HVAC/F&G/communications tie-in detail, and detailed turnover-checklist content until a source-supported basis is available.
- Use the DBM construction and electrical basis only at the level it supports: in-scope construction activities, electrical buildings as housings for distribution/MCC/UPS equipment, grounding/bonding basis, cable tray/conduit routing constraints, area classification basis, geotechnical confirmation requirement, and pre-issue alignment to plot plan, equipment list, and construction work package register.

## Considerations

The DBM construction scope summary explicitly includes construction management, grading, piling, foundations, electrical buildings, offloading and setting of modules, mechanical hookups, home-run cabling, terminations, and field interconnections. These activities are directionally relevant to `PKG-034` installation, but the source does not assign quantities, sequences, or package-specific construction steps to this 600V electrical building package.

The DBM electrical design basis identifies the project voltage hierarchy and notes that electrical buildings may house MV/LV distribution, MCCs, UPS systems with battery banks, and protection/control equipment. The construction work package should respect this basis while preserving the Package Datasheet position that detailed building equipment population, distribution layout, and capacity values remain `TBD` until vendor data or detailed electrical source is accepted.

Grounding and bonding are applicable interface topics. The DBM source contains facility grounding basis including two-point ground-grid connection for major electrical equipment and separate copper ground conductors per CEC sizing for certain equipment. The construction work package should require these to be respected as installation rules while avoiding unsupported package-specific conductor sizing or connection details.

Maintenance access is both an explicit workbook interface fact and a DBM routing constraint for cable tray and conduit. The construction work package should require equipment placement, building penetrations, and electrical routing to preserve maintenance access; detailed clearances remain `TBD` unless issued by detailed design or vendor data.

Structural/foundation/support requirements depend on the final geotechnical report. Because the 600V electrical building is likely modular/skid-mounted (ASSUMPTION pending vendor confirmation), the construction work package should treat geotechnical values as a hard prerequisite before issue for construction rather than as a downstream check.

The twelve interfaces for `PKG-034` include several building-services topics (Building HVAC / Services, Fire & Gas / Safety Systems, Communications / Network, Area / Exterior Lighting, Utility Piping, Drain / Containment, Grading / Site Drainage / Spill Containment) that are not present on simpler electrical packages. The construction work package should require explicit coordination of these tie-ins between the building package and the corresponding facility scope, without inventing detail that is not in source material.

Construction interface and turnover evidence will be consumed by the downstream EPC Vendor Package Review and Acceptance deliverable (`DEL-034-06`) and complemented by the Vendor Document Turnover Package (`DEL-034-05`). The construction work package should be authored so that its turnover checklist is directly usable by those reviews.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| 600V building equipment population | Treat "600V ELECTRICAL BUILDING (820-2)" as package title/identity; do not derive installation-specific equipment list, feeder counts, or distribution layout from the title. | The accessible source set does not enumerate the equipment housed inside this specific building. |
| Installation location | Identify the 820-2 WBS area as context only; do not assign `PKG-034` to a specific plot-plan coordinate, orientation, or adjacency in the construction work package. | DBM mentions electrical buildings generally; it does not locate `PKG-034`. |
| Modularization / shipping splits / lifting | Mark `TBD` pending vendor package data and EPC construction planning; note ASSUMPTION that electrical buildings are commonly pre-fabricated/modular. | No package-specific modularization or lifting basis is recorded in accessible source material. |
| Building HVAC / F&G / Comms tie-in detail | Provide a coordination requirement and mark line-item content `TBD` pending the vendor building design and facility-services interface schedules. | No package-specific HVAC/F&G/Comms content is recorded in accessible source material. |
| Detailed ITPs, hold points, and turnover-checklist content | Provide a structural placeholder and mark line-item content `TBD` pending the inspection plan, vendor documentation, and EPC review basis. | No package-specific inspection or turnover content is recorded in accessible source material. |
| Standards | List CEC, area classification, project electrical specifications, and the final geotechnical report as governing bases with locations TBD. | DBM references these bases but specific clauses, specification documents, and the final geotechnical report are not available in the deliverable folder. |
| Foundations / supports | Treat foundation, pile, settlement, frost protection, and structural support detail as `TBD` until the final geotechnical report is accepted. | DBM explicitly treats geotechnical values as placeholders until the geotechnical report is accepted. |

## Examples

- Acceptable construction work package entry: "Installation shall preserve maintenance access; cable tray, conduit routing, and building penetrations shall not interfere with maintenance access. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, cable tray/conduit paragraphs."
- Acceptable source-gap entry: "Lifting plan and set-on-foundation sequence for the 600V electrical building: TBD. No package-specific source slice available."
- Not acceptable without new source: "The 600V electrical building shall be set on a 12 m x 6 m piled foundation at coordinate N+120, E+85, with HVAC condensers on the south wall and fire alarm panel on the east entry." The accessible source set does not establish this location, dimension, or building services layout.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-034-03-001 | Package title says "600V ELECTRICAL BUILDING (820-2)", but accessible sources do not enumerate the equipment housed (MV/LV distribution, MCC, UPS, transformers, protection), capacity, distribution layout, or building dimensions; this propagates into construction installation assumptions (lifting weight, foundation size, feeder counts, building services sizing). | Workbook Packages row 36; `PACKAGE_REGISTER.csv` row `PKG-034` | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical buildings and voltage/service source slices | Datasheet Attributes/Construction; Specification Requirements; Procedure Steps | Treat "600V ELECTRICAL BUILDING (820-2)" as title/identity only and keep installation-specific feeder, support, lift, and building-services detail `TBD` until vendor data or detailed electrical source is accepted. | TBD |
| HRR-034-03-002 | Installation plot-plan location for `PKG-034` (specific coordinate, orientation, adjacency to other 820-series equipment) is not confirmed in accessible source material, but is required to author a complete construction work package and workface plan. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical buildings paragraph | Workbook Packages row 36; `PACKAGE_REGISTER.csv` row `PKG-034` | Datasheet Attributes/Construction; Specification Requirements; Procedure Steps | Hold installation plot-plan location, orientation, and clearance basis as `TBD` until detailed design and plot-plan alignment confirm the location. | TBD |
| HRR-034-03-003 | Final geotechnical report, project plot plan, equipment list, and construction work package register are required pre-issue inputs per DBM, but their availability and currency for issue of the `PKG-034` construction work package is not confirmed in accessible source material. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, geotechnical and miscellaneous facilities/issue-for-construction paragraphs | `_REFERENCES.md`; Gate 7 registers | Specification Requirements (REQ-034-03-007, REQ-034-03-009); Procedure Steps | Treat geotechnical-report acceptance and plot-plan/equipment-list/construction-work-package-register alignment as gating prerequisites for issue for construction; record their absence as `TBD` until confirmed by the project. | TBD |
| HRR-034-03-004 | Building HVAC / Services, Fire & Gas / Safety Systems, Communications / Network, Area / Exterior Lighting, Utility Piping, Drain / Containment, and Grading / Site Drainage / Spill Containment are declared applicable interfaces for `PKG-034`, but accessible source material does not provide package-specific tie-in points, sizes, routes, or schedules. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` rows for `PKG-034` | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (no package-specific tie-in detail) | Datasheet Conditions; Specification Requirements (REQ-034-03-013); Procedure Steps | Carry these as coordination requirements with detail held `TBD` pending vendor building design and the facility interface schedules. | TBD |
