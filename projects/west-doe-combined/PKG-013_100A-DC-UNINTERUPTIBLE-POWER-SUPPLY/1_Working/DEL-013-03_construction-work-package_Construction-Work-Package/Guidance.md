# Guidance: DEL-013-03_construction-work-package

## Purpose

The Construction Work Package exists to convert the accepted Gate 7 package basis for `PKG-013` into a construction-facing deliverable that describes how the 100A DC UNINTERUPTIBLE POWER SUPPLY package is physically installed, built, inspected, turned over, and tied into the larger facility systems. It should make EPC construction and turnover scope explicit while keeping vendor-owned package design with the Package Vendor.

## Principles

- Preserve source spelling and identity. The package name is carried as "100A DC UNINTERUPTIBLE POWER SUPPLY" because that is the workbook and Gate 7 register spelling.
- Treat the Construction Work Package as construction-facing only. Do not redefine package design values; accept the Package Datasheet (`DEL-013-02`) as the technical handoff basis.
- Treat workbook interface `X` facts as construction-facing tie-in scope items.
- Keep vendor-owned design work with the Package Vendor and facility-level construction integration with the EPC Integrator.
- Use `TBD` for installation location, modularization, lifting plan, ITPs, hold points, package-specific feeder/conductor/conduit detail, foundation/support detail, and detailed turnover-checklist content until a source-supported basis is available.
- Use the DBM construction and electrical basis only at the level it supports: in-scope construction activities, electrical buildings as possible UPS housing context, grounding/bonding basis, cable tray/conduit routing constraints, area classification basis, geotechnical confirmation requirement, and pre-issue alignment to plot plan, equipment list, and construction work package register.

## Considerations

The DBM construction scope summary explicitly includes construction management, grading, piling, foundations, electrical buildings, offloading and setting of modules, mechanical hookups, home-run cabling, terminations, and field interconnections. These activities are directionally relevant to `PKG-013` installation, but the source does not assign quantities, sequences, or package-specific construction steps to this UPS package.

The DBM electrical design basis supports a general UPS service basis of 120 VAC / 125 VDC for control system, selected emergency or critical lighting, MV breaker control, and MV protective relay loads, and notes that electrical buildings may house UPS systems with battery banks and distribution panels. The construction work package should respect this basis while preserving the Package Datasheet position that detailed UPS parameters remain `TBD` until vendor data or detailed electrical source is accepted.

Grounding and bonding are applicable interface topics. The DBM source contains facility grounding basis including two-point ground-grid connection for major electrical equipment and separate copper ground conductors per CEC sizing for certain equipment. The construction work package should require these to be respected as installation rules while avoiding unsupported package-specific conductor sizing or connection details.

Maintenance access is both an explicit workbook interface fact and a DBM routing constraint for cable tray and conduit. The construction work package should require equipment placement and electrical routing to preserve maintenance access; detailed clearances remain `TBD` unless issued by detailed design or vendor data.

Structural/foundation/support requirements depend on the final geotechnical report. The construction work package should treat geotechnical values as a hard prerequisite before issue for construction rather than as a downstream check.

Construction interface and turnover evidence will be consumed by the downstream EPC Vendor Package Review and Acceptance deliverable (`DEL-013-06`) and complemented by the Vendor Document Turnover Package (`DEL-013-05`). The construction work package should be authored so that its turnover checklist is directly usable by those reviews.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| 100A DC interpretation | Treat "100A DC" as package title only; do not derive installation-specific load, rating, or feeder values from the title. | The accessible source set does not define whether "100A DC" describes charger output, DC distribution capacity, load, or another rating. |
| Installation location | Identify electrical buildings as possible context only; do not assign `PKG-013` to a specific building, room, or location in the construction work package. | DBM says electrical buildings may house UPS systems but does not locate `PKG-013`. |
| Modularization / shipping splits / lifting | Mark `TBD` pending vendor package data and EPC construction planning. | No package-specific modularization or lifting basis is recorded in accessible source material. |
| Detailed ITPs, hold points, and turnover-checklist content | Provide a structural placeholder and mark line-item content `TBD` pending the inspection plan, vendor documentation, and EPC review basis. | No package-specific inspection or turnover content is recorded in accessible source material. |
| Standards | List CEC, area classification, project electrical specifications, and the final geotechnical report as governing bases with locations TBD. | DBM references these bases but specific clauses, specification documents, and the final geotechnical report are not available in the deliverable folder. |
| Foundations / supports | Treat foundation, pile, settlement, frost protection, and structural support detail as `TBD` until the final geotechnical report is accepted. | DBM explicitly treats geotechnical values as placeholders until the geotechnical report is accepted. |

## Examples

- Acceptable construction work package entry: "Installation shall preserve maintenance access; cable tray and conduit routing shall not interfere with maintenance access. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, cable tray/conduit paragraphs."
- Acceptable source-gap entry: "Lifting plan for the UPS package skid: TBD. No package-specific source slice available."
- Not acceptable without new source: "The UPS package shall be installed in electrical building B at the north end of the control room with a 6 m clear maintenance envelope on the front face." The accessible source set does not establish this location, building, or clearance.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-013-03-001 | Package title says "100A DC", but accessible sources do not define the technical meaning, rating basis, voltage, battery autonomy, or charger/distribution configuration; this propagates into construction installation assumptions (feeder sizing, ground sizing, weight, lift). | Workbook Packages row 15; `PACKAGE_REGISTER.csv` row `PKG-013` | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, UPS services and electrical-building source slices | Datasheet Attributes/Construction; Specification Requirements; Procedure Steps | Treat "100A DC" as title/identity only and keep installation-specific feeder, support, and ground-conductor details `TBD` until vendor data or detailed electrical source is accepted. | TBD |
| HRR-013-03-002 | Installation location for `PKG-013` (electrical building assignment, indoor/outdoor, skid vs panel) is not confirmed in accessible source material, but is required to author a complete construction work package and workface plan. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical buildings paragraph | Workbook Packages row 15; `PACKAGE_REGISTER.csv` row `PKG-013` | Datasheet Attributes/Construction; Specification Requirements; Procedure Steps | Hold installation location, building assignment, and clearance basis as `TBD` until detailed design and plot-plan alignment confirm the location. | TBD |
| HRR-013-03-003 | Final geotechnical report, project plot plan, equipment list, and construction work package register are required pre-issue inputs per DBM, but their availability and currency for issue of the `PKG-013` construction work package is not confirmed in accessible source material. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, geotechnical and miscellaneous facilities/issue-for-construction paragraphs | `_REFERENCES.md`; Gate 7 registers | Specification Requirements (REQ-013-03-007, REQ-013-03-009); Procedure Steps | Treat geotechnical-report acceptance and plot-plan/equipment-list/construction-work-package-register alignment as gating prerequisites for issue for construction; record their absence as `TBD` until confirmed by the project. | TBD |
