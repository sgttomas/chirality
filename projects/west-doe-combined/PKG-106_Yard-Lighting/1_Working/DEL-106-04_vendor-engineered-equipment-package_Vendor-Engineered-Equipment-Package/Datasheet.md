# Datasheet — DEL-106-04 Vendor Engineered Equipment Package (Yard Lighting)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-106-04_vendor-engineered-equipment-package` | `_CONTEXT.md` Identity |
| Name | Vendor Engineered Equipment Package | `_CONTEXT.md` Identity |
| ParentPackageID | `PKG-106` | `_CONTEXT.md` Identity |
| PackageName | Yard Lighting | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-106 |
| Discipline | Electrical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-106 |
| Type | Vendor Package Production Unit | `_CONTEXT.md` Identity |
| ResponsibleParty | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-106-04 |
| Covers Scope Item | `SOW-0011` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-106-04 |
| Supports Objectives | OBJ-001; OBJ-004; OBJ-005; OBJ-009; OBJ-010 (ASSUMPTION — package-grouped) | `_CONTEXT.md`; PACKAGE_HEURISTIC |
| Decomposition Snapshot | Gate 7 Final Published 2026-05-24 | `_REFERENCES.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package Engineering and Design Owner | Package Vendor | `PACKAGE_REGISTER.csv` row PKG-106 (Ownership) |
| Vendor Documentation Owner | Package Vendor | `PACKAGE_REGISTER.csv` row PKG-106 (Ownership) |
| Physical Equipment Package Owner | Package Vendor | `PACKAGE_REGISTER.csv` row PKG-106 (Ownership) |
| Facility Integration Owner | EPC Integrator | `PACKAGE_REGISTER.csv` row PKG-106 (Ownership) |
| Lighting Technology | LED (all lighting; process area and outdoor lighting; exterior lighting per regulatory light-pollution basis) | DBM-Deepcut `4-25_Deepcut_DBM.md` `## Lighting and Receptacles` |
| General-purpose Lighting Service | 120/208 V, 3 phase, 4 wire, 60 Hz, solidly grounded (lighting and utility distribution) | DBM-Deepcut `4-25_Deepcut_DBM.md` Electrical Services table |
| Distribution Source | Nearest Power Distribution Centre (RDC) | DBM-Deepcut `4-25_Deepcut_DBM.md` `## Lighting and Receptacles` |
| Area Classification Suitability | Fixtures suitable for area classification in which installed | DBM-Deepcut `4-25_Deepcut_DBM.md` `## Lighting and Receptacles` |
| Light-Pollution Controls | Downcast floodlights; no horizontally aimed floodlights; photocell or switch control; selective minimization to working areas; mast pole locations away from pad edge | DBM-Deepcut `4-25_Deepcut_DBM.md` `## Lighting and Receptacles` (final paragraph) |
| Mast Poles | Required where applicable; locate away from pad edge | DBM-Deepcut `4-25_Deepcut_DBM.md` `## Lighting and Receptacles` (final paragraph) |
| Anticipated Artifacts | Vendor engineered physical equipment package; vendor package design basis and datasheet set | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row DEL-106-04 |
| Package Interface Types | Electrical Power; Grounding / Bonding; Area / Exterior Lighting | `INTERFACE_REGISTER.csv` rows IFC-6FCF1B30D6, IFC-DA0D60681B, IFC-ED86F51087 |
| Light Levels (lux) | TBD — not specified in accessible source slices | location TBD |
| Pole Height, Spacing, Mount Details | TBD | location TBD |
| Fixture Catalogue/Models | TBD | vendor selection |
| Foundation Design (poles) | TBD — depends on geotechnical and vendor base loads | location TBD |
| WBS | TBD | `PACKAGE_REGISTER.csv` row PKG-106 (WBS TBD) |
| Package-specific exclusions | TBD; no package-specific exclusions stated in source materials | `PACKAGE_REGISTER.csv` row PKG-106 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site | West Doe Deepcut expansion (4-25); facility 04-25 | DBM-Deepcut `4-25_Deepcut_DBM.md` `## Terminology Basis` |
| Outdoor Service | Yes (yard lighting) | `_CONTEXT.md` Scope; DBM Lighting section |
| Hazardous Area Applicability | Fixtures must match local area classification (process area and outdoor) | DBM-Deepcut `4-25_Deepcut_DBM.md` `## Lighting and Receptacles` |
| Cold-Weather Basis | Outdoor electrical equipment selection consistent with facility cold-weather basis (ASSUMPTION — consistent with DBM Section 12 envelope) | ASSUMPTION; DBM-Deepcut Section 12 context |
| Ambient Design Limits | TBD — to be drawn from accepted electrical/civil basis | location TBD |
| Lighting Categories Implied by Source | Area lighting (yard / outdoor / process area); MCC room lighting (flat-panel LED); interior lighting; exit/emergency lighting (with battery backup) — yard scope is the outdoor/area subset | DBM-Deepcut `4-25_Deepcut_DBM.md` `## Lighting and Receptacles` |

## Construction

| Item | Description | Source |
|---|---|---|
| Vendor Scope | Engineering, design, fabrication/supply of the physical equipment package per EPC Scope of Work (`DEL-106-01`) and EPC Package Datasheet (`DEL-106-02`) | `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` rows DEL-106-01, DEL-106-02 |
| Conduit/Raceway (where shop-installed) | Rigid conduit for shop-fabricated/erected building lighting prior to shipment; sealed where crossing area classification boundaries; minimum 21 mm (3/4 in); CEC compliant | DBM-Deepcut `4-25_Deepcut_DBM.md` paragraph preceding `## Lighting and Receptacles` |
| Conductor Sizing for Lighting Branch Circuits | Conductors selected not larger than #10 AWG where possible by locating RDCs closer to lighting loads | DBM-Deepcut `4-25_Deepcut_DBM.md` cable section paragraph |
| Receptacle/Lighting Circuit Mixing | Receptacle circuits shall not be mixed with lighting circuits | DBM-Deepcut `4-25_Deepcut_DBM.md` `## Lighting and Receptacles` (receptacles paragraph) |
| Vendor Documentation | Vendor package design basis and datasheet set produced by Package Vendor | `_CONTEXT.md` Anticipated Artifacts |
| Integration into Facility | EPC Integrator integrates the package into the facility (interfaces, tie-ins, constructability) | `PACKAGE_REGISTER.csv` row PKG-106 (Ownership) |
| Foundations and Mast Pole Layout | TBD — vendor design with EPC civil interface | location TBD |
| Photometric / Layout Design Basis | TBD — vendor design subject to EPC review | location TBD |
| Standards/Codes Compliance | Canadian Electrical Code (CEC); applicable area classification | DBM-Deepcut `4-25_Deepcut_DBM.md` `## Lighting and Receptacles`; preceding conduit paragraph |

## References

- `_CONTEXT.md` (deliverable identity and scope)
- `_REFERENCES.md` (authoritative decomposition basis; shared source root)
- `_DEPENDENCIES.md` (declared dependency state)
- Gate 7 PROJECT_DECOMP snapshot: `DELIVERABLE_REGISTER.csv` row DEL-106-04; `PACKAGE_REGISTER.csv` row PKG-106; `INTERFACE_REGISTER.csv` rows IFC-6FCF1B30D6 / IFC-DA0D60681B / IFC-ED86F51087
- DBM-Deepcut: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (sections: `## Lighting and Receptacles`; Electrical Services table; conduit/cable paragraphs preceding lighting section)
- DEL-106-01 Scope of Work (sibling deliverable; not yet drafted — used as decomposition pointer)
- DEL-106-02 Package Datasheet (sibling deliverable; not yet drafted — used as decomposition pointer)
- `26020-Package_Requirements.docx` — not extracted for `PKG-106` (no package-specific slice copied during PREPARATION)
- DBM-Comp_and_Liquids (`3-25_Comp_and_Liquids_DBM.md`) — connected 03-25 scope; not consulted for `PKG-106` deliverable text in this pass
