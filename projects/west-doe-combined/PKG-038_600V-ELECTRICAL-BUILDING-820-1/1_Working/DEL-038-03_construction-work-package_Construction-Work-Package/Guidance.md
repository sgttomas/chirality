# Guidance: DEL-038-03_construction-work-package

## Purpose

The Construction Work Package exists to convert the accepted Gate 7 package basis for `PKG-038` into a construction-facing deliverable that describes how the 600V Electrical Building (workbook tag 820-1) is physically installed, built, inspected, turned over, and tied into the larger facility systems. It should make EPC construction and turnover scope explicit while keeping vendor-owned package design (the modular building and its internal electrical equipment) with the Package Vendor.

## Principles

- Preserve source spelling and identity. The package name is carried as "600V ELECTRICAL BUILDING (820-1)" because that is the workbook and Gate 7 register spelling, even though the DBM electrical-buildings list assigns a different descriptor to tag 820-1 (see Conflict Table HRR-038-03-001).
- Treat the Construction Work Package as construction-facing only. Do not redefine package design values; accept the Package Datasheet (`DEL-038-02`) as the technical handoff basis.
- Treat workbook interface `YES` facts as construction-facing tie-in scope items. All twelve interfaces marked applicable for `PKG-038` are construction-relevant.
- Keep vendor-owned design work (modular building, internal MCCs, UPS, transformers, panels, PLCs, network racks) with the Package Vendor and facility-level construction integration with the EPC Integrator.
- Use `TBD` for exact plot location, modularization/shipping splits, lift plan, ITPs, hold points, package-specific feeder/conductor/conduit detail, foundation/pile/settlement detail, building-internal equipment quantities, HVAC equipment selection, and detailed turnover-checklist content until a source-supported basis is available.
- Use the DBM-Deepcut electrical basis at the level it supports: prefabricated/modular construction, elevation on piles with bottom cable entry, general-purpose siting, n + 1 HVAC, two-point ground-grid connection, ground wells, DBM-specified cable types and ratings, and EMT-between-adjacent-equipment conduit basis.

## Considerations

The DBM-Deepcut Electrical Buildings section is the primary installation basis. It mandates prefabricated, modular construction in general-purpose areas; n + 1 HVAC; pile elevation with bottom cable entry for both incoming and outgoing power cables; TECK and ACIC cable wiring with EMT conduit between adjacent equipment; an outdoor GFI maintenance receptacle; and equipment-removal-sized doors or transoms. The construction work package should treat each of these as installation rules the EPC scope must honor.

The DBM Grounding and Bonding section provides facility grounding rules that directly govern building grounding installation: two-point ground-grid connections for major equipment, ground wells at electrical buildings with bolted ground-test connections, above-grade green insulated conductors in PVC conduit where mechanical protection is required, compression-type connections, and separate copper ground conductors for distribution transformers, panelboards, and large motors sized per CEC. The 600 V transformer feeding the building is high-resistance grounded (5 A continuous) per DBM, which affects testing and protection turnover.

The DBM Cable, Wire, and Raceways section sets the tray cable basis (TECK 90, ACWU, ACIC; HL rated; aluminum interlocking armor; -40 deg C; copper to #1/0 AWG and ACWU above), the conduit basis (EMT between adjacent equipment), and the field-routing basis (shop-installed pipe rack trays, field-run trays for tank-farm and interconnects between racks, skids, and electrical buildings). Construction installation methods should respect this basis even where specific cable lists and quantities are TBD.

Area classification is governed by detailed area-classification drawings. DBM places electrical buildings in general-purpose areas, so installation methods and material selection should default to non-hazardous unless the area-classification drawings indicate otherwise for a specific portion of the package footprint.

Maintenance access is both an explicit workbook interface fact and a DBM requirement for equipment removal and routing. The construction work package should require equipment placement and electrical routing to preserve maintenance access; detailed clearances remain `TBD` unless issued by detailed design or vendor data.

Structural/foundation/support requirements depend on the final geotechnical report. The DBM requirement that electrical buildings be elevated and installed on piles is a hard construction constraint, but pile size/depth, settlement, and frost protection values for the specific building location are TBD until the geotechnical report is accepted.

Construction interface and turnover evidence will be consumed by the downstream EPC Vendor Package Review and Acceptance deliverable (`DEL-038-06`) and complemented by the Vendor Document Turnover Package (`DEL-038-05`). The construction work package should be authored so that its turnover checklist is directly usable by those reviews.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Package identity / "820-1" descriptor | Preserve workbook spelling "600V ELECTRICAL BUILDING (820-1)" as authoritative for this deliverable identity; record the DBM list discrepancy as a conflict for human ruling. Do not silently restate the DBM descriptor. | Workbook row 40 is the authoritative deliverable-identity source for Gate 7 package decomposition; DBM list is a parallel source slice whose 820-1 row uses a different descriptor. Human ruling is required. |
| Exact plot location | Hold plot location as `TBD`; identify general-purpose-area siting and OGAOM 25 m spacing from fired heaters as constraints when the location is set. | DBM does not provide plot coordinates for tag 820-1; plot plan is not in the deliverable folder. |
| Modularization / shipping splits / lift plan | Confirm modular, shop-fabricated, pile-elevated construction; hold shipping splits, lift weights, and crane/rigging detail as `TBD` pending vendor data. | Modular basis is established by DBM; package-specific module count, weights, and rigging plans are vendor data. |
| Detailed ITPs, hold points, and turnover-checklist content | Provide a structural placeholder and mark line-item content `TBD` pending the inspection plan, vendor documentation, and EPC review basis. | No package-specific inspection or turnover content is recorded in accessible source material. |
| Standards | List CEC, area classification, project electrical specifications, OGAOM 9.6.15, and the final geotechnical report as governing bases with locations TBD. | DBM references these bases but specific clauses, specification documents, and the final geotechnical report are not available in the deliverable folder. |
| Foundations / supports | Treat foundation, pile, settlement, frost protection, and structural support detail as `TBD` until the final geotechnical report is accepted; preserve "elevated on piles, bottom cable entry" as a hard DBM constraint. | DBM Electrical Buildings section requires pile elevation and bottom entry but defers values to geotechnical and detailed design. |
| Internal equipment quantities | Treat 13.8 kV switchgear, MV MCCs, 600 V MCCs, UPS systems, transformers, panelboards, contactor panels, PLC panels, and network racks as possible building contents per DBM but do not assign quantities, ratings, or counts to `PKG-038`. | DBM lists candidate contents "as required by detailed design"; package-specific equipment list is vendor scope. |
| HVAC equipment selection | Require n + 1 HVAC and electric building heaters as default; hold equipment make/model and duct routing `TBD`. | DBM mandates n + 1 redundancy and default electric heaters; specifics are detailed design and vendor data. |

## Examples

- Acceptable construction work package entry: "Electrical building shall be installed elevated on piles with bottom cable entry for incoming and outgoing power cables. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section."
- Acceptable source-gap entry: "Lift plan and shipping-split detail for the 600 V Electrical Building (820-1) modular building: TBD. No package-specific source slice available."
- Acceptable conflict-handling entry: "Workbook designates `PKG-038` as `600V ELECTRICAL BUILDING (820-1)`; DBM electrical-buildings list identifies tag 820-1 as `6.9 kV Inlet / Sales Compressor Electrical Building`. Identity conflict held for human ruling (HRR-038-03-001)."
- Not acceptable without new source: "The 600 V Electrical Building (820-1) shall be installed at plot coordinates X, Y north of the 13.8 kV switchgear with a 6 m clear maintenance envelope on the south face." The accessible source set does not establish this location or clearance.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-038-03-001 | Tag 820-1 is described differently across accepted sources: the workbook (and Gate 7 PACKAGE_REGISTER row `PKG-038`) names the package "600V ELECTRICAL BUILDING (820-1)", while the DBM-Deepcut electrical-buildings list identifies tag "820-1" as the "6.9 kV Inlet / Sales Compressor Electrical Building." This affects voltage-class assumptions about the building's primary distribution role, internal equipment basis, and feeder/grounding scope. | Workbook Packages row 40; `PACKAGE_REGISTER.csv` row `PKG-038` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings list (tag 820-1) | Datasheet Identification/Attributes/Construction; Specification Scope/Requirements; Procedure Steps | Treat workbook identity as authoritative for deliverable identity (per Gate 7 decomposition truth) and hold the building's primary voltage class/role as `TBD` until human resolution of the workbook-vs-DBM descriptor mismatch for tag 820-1. | TBD |
| HRR-038-03-002 | Exact plot location, modularization (number of modules, shipping splits), lift weights, and crane/rigging plan for `PKG-038` are not confirmed in accessible source material but are needed to author a complete construction work package and workface plan. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings and Area Classification sections | Workbook Packages row 40; `PACKAGE_REGISTER.csv` row `PKG-038` | Datasheet Attributes/Construction; Specification Requirements; Procedure Steps | Hold plot location, modularization/shipping splits, lift plan, and crane/rigging detail as `TBD` until vendor data and plot-plan alignment confirm the values. | TBD |
| HRR-038-03-003 | Final geotechnical report, project plot plan, equipment list, and construction work package register are required pre-issue inputs but their availability and currency for issue of the `PKG-038` construction work package are not confirmed in accessible source material. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section (pile-elevated requirement); `_REFERENCES.md` | Gate 7 registers | Specification Requirements (REQ-038-03-009, REQ-038-03-013); Procedure Steps | Treat geotechnical-report acceptance and plot-plan/equipment-list/construction-work-package-register alignment as gating prerequisites for issue for construction; record their absence as `TBD` until confirmed by the project. | TBD |
