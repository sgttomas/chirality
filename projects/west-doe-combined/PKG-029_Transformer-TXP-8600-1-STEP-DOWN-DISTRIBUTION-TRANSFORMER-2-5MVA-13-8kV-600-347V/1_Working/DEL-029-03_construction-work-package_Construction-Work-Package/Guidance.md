# Guidance: DEL-029-03_construction-work-package

## Purpose

The Construction Work Package exists to convert the accepted Gate 7 package basis for `PKG-029` into a construction-facing deliverable that describes how the step-down distribution transformer package (TXP-8600-1, 2.5 MVA, 13.8 kV / 600/347 V) is physically installed, built, inspected, turned over, and tied into the larger facility systems. It should make EPC construction and turnover scope explicit while keeping vendor-owned package design with the Package Vendor.

## Principles

- Preserve source spelling and identity. The package name is carried as "Transformer TXP-8600-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V" because that is the workbook and Gate 7 register spelling.
- Treat the Construction Work Package as construction-facing only. Do not redefine package design values; accept the Package Datasheet (`DEL-029-02`) as the technical handoff basis.
- Treat workbook interface `X` facts as construction-facing tie-in scope items.
- Keep vendor-owned design work (oil-filled vs dry-type selection, winding/connection configuration, protection scheme, accessories) with the Package Vendor and facility-level construction integration with the EPC Integrator.
- Use `TBD` for installation location, modularization, lifting/rigging plan, ITPs, hold points, package-specific feeder/conductor/conduit detail, foundation/pad detail, secondary-containment detail, oil-handling plan, and detailed turnover-checklist content until a source-supported basis is available.
- Use the DBM-Deepcut construction and electrical basis only at the level it supports: in-scope construction activities, transformer foundations on precast concrete bearing foundations or structural steel bases, CEC transformer spacing and grounding rules, MV/LV cable type and routing constraints, area classification basis, geotechnical confirmation requirement, and pre-issue alignment to plot plan, equipment list, and construction work package register.

## Considerations

The DBM-Deepcut construction scope summary explicitly includes construction management, grading, piling, foundations, electrical buildings, offloading and setting of modules, mechanical hookups, home-run cabling, terminations, and field interconnections. These activities are directionally relevant to `PKG-029` installation, but the source does not assign quantities, sequences, or package-specific construction steps to this transformer.

The DBM-Deepcut electrical design basis supports a 13.8 kV MV distribution backbone and 600 V LV service for motors up to 250 hp, lighting/utility distribution transformers, building heaters, and UPS systems larger than 10 kVA. The 600 V secondary of TXP-8600-1 aligns with this service basis; the 347 V phase-to-neutral aspect is not explicitly addressed in the available DBM slice and remains a vendor/detailed-design item.

Transformer-specific installation guidance from the DBM includes: large oil-filled transformers shall be spaced per CEC; transformers will generally be installed on structural steel transformer bases; secondary containment shall be reviewed and minimized where practical; ground wells at power transformers shall be provided for maintenance and operational testing. Whether TXP-8600-1 is oil-filled or dry-type is a vendor decision and is therefore `TBD` for the construction work package, with the construction plan supporting either path until vendor confirmation.

Grounding and bonding are applicable interface topics. The DBM contains facility grounding basis including two-point ground-grid connection for major electrical equipment, ground wells at transformers, separate copper ground conductors per CEC for distribution transformers, and a 5 A continuous high-resistance grounding resistor for 600 V transformers. The construction work package should require these to be respected as installation rules while avoiding unsupported package-specific conductor sizing.

Maintenance access is both an explicit workbook interface fact and a DBM routing constraint. The construction work package should require transformer spacing, equipment placement, and electrical routing to preserve maintenance access; detailed clearances remain `TBD` unless issued by detailed design or vendor data.

Structural/foundation/support requirements depend on the final geotechnical report. The construction work package should treat geotechnical values as a hard prerequisite before issue for construction.

Construction interface and turnover evidence will be consumed by the downstream EPC Vendor Package Review and Acceptance deliverable (`DEL-029-06`) and complemented by the Vendor Document Turnover Package (`DEL-029-05`). The construction work package should be authored so that its turnover checklist is directly usable by those reviews.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Oil-filled vs dry-type construction | Treat construction class as `TBD`; structure the construction work package so it supports either path (oil-handling/containment provisions optional but explicitly captured as conditional). | The accessible source set does not designate TXP-8600-1 as oil-filled or dry-type. |
| 600/347 V secondary | Carry the workbook spelling as identity; treat detailed winding/connection (wye/delta), neutral grounding method, and tap arrangement as vendor-design `TBD`. | DBM addresses 600 V service generally but does not detail this transformer's secondary configuration or the 347 V phase-to-neutral reference. |
| Installation location | Identify electrical buildings and outdoor transformer pads as possible context only; do not assign `PKG-029` to a specific building, pad, or location in the construction work package. | DBM lists possible housings but does not locate TXP-8600-1. |
| Modularization / shipping splits / lifting | Mark `TBD` pending vendor package data and EPC construction planning. | No package-specific modularization or lifting basis is recorded in accessible source material. |
| Detailed ITPs, hold points, and turnover-checklist content | Provide a structural placeholder and mark line-item content `TBD` pending the inspection plan, vendor documentation, and EPC review basis. Include common transformer field tests (insulation resistance, turns ratio, oil dielectric if oil-filled) as candidate tests. | No package-specific inspection or turnover content is recorded in accessible source material. |
| Standards | List CEC, area classification, project electrical specifications, and the final geotechnical report as governing bases with locations TBD. | DBM references these bases but specific clauses, specification documents, and the final geotechnical report are not available in the deliverable folder. |
| Foundations / supports | Treat foundation, pile, settlement, frost protection, structural support, and secondary-containment detail as `TBD` until the final geotechnical report is accepted, recognizing precast concrete and structural steel transformer bases as DBM defaults. | DBM explicitly treats geotechnical values as placeholders until the geotechnical report is accepted. |

## Examples

- Acceptable construction work package entry: "Two-point ground-grid connection shall be provided at the transformer; ground well at the transformer shall be provided for maintenance and operational testing. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs."
- Acceptable source-gap entry: "Lifting and rigging plan for TXP-8600-1: TBD. No package-specific source slice available."
- Not acceptable without new source: "TXP-8600-1 shall be installed in electrical building 810-1 on a 4.5 m by 3.5 m precast pad with 1.2 m clearance on the front and 1.0 m on each side." The accessible source set does not establish this location, pad size, or clearance.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-029-03-001 | Workbook identity gives the package as a 2.5 MVA, 13.8 kV / 600/347 V step-down distribution transformer, but the DBM-Deepcut transformer paragraphs describe only the 50 MVA utility transformer, the 13.8 kV/4.16 kV 12 MVA transformer, the 13.8 kV/600 V 3 MVA transformer, the LACT 480 V dry-type transformer, and 208/120 V distribution transformers; the 2.5 MVA / 600/347 V transformer is not individually described and its construction class (oil-filled vs dry-type), winding configuration, and installation context are therefore not source-confirmed. | Workbook Packages row 31; `PACKAGE_REGISTER.csv` row `PKG-029` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, incoming-power/transformers and grounding paragraphs | Datasheet Attributes/Construction; Specification Requirements; Procedure Steps | Carry workbook identity as authoritative for identity; treat construction class, winding/connection, and detailed installation requirements as `TBD` until vendor data or detailed electrical source is accepted. | TBD |
| HRR-029-03-002 | Installation location for `PKG-029` (electrical-building assignment, indoor/outdoor, transformer-pad vs structural-steel base, secondary-containment requirement) is not confirmed in accessible source material, but is required to author a complete construction work package and workface plan. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers and electrical-buildings paragraphs | Workbook Packages row 31; `PACKAGE_REGISTER.csv` row `PKG-029` | Datasheet Attributes/Construction; Specification Requirements; Procedure Steps | Hold installation location, foundation class, and clearance/containment basis as `TBD` until detailed design and plot-plan alignment confirm the location and vendor confirms construction class. | TBD |
| HRR-029-03-003 | Final geotechnical report, project plot plan, equipment list, and construction work package register are required pre-issue inputs per DBM, but their availability and currency for issue of the `PKG-029` construction work package is not confirmed in accessible source material. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, geotechnical and miscellaneous facilities/issue-for-construction paragraphs | `_REFERENCES.md`; Gate 7 registers | Specification Requirements (REQ-029-03-007, REQ-029-03-009); Procedure Steps | Treat geotechnical-report acceptance and plot-plan/equipment-list/construction-work-package-register alignment as gating prerequisites for issue for construction; record their absence as `TBD` until confirmed by the project. | TBD |
