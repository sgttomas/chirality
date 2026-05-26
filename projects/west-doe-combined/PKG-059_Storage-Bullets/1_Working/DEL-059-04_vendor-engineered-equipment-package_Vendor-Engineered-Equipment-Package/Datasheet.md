# Datasheet — DEL-059-04 Vendor Engineered Equipment Package

> Decomposition-routed, source-grounded draft. Non-trivial values cite a source slice; missing values are explicitly `TBD`. Inferences are labeled `ASSUMPTION`.

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-059-04_vendor-engineered-equipment-package` |
| Name | Vendor Engineered Equipment Package |
| ParentPackageID | `PKG-059` Storage Bullets |
| Discipline | Mechanical |
| Type | Vendor Package Production Unit |
| Responsible Party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review |
| Covers Scope Items | `SOW-0181`, `SOW-0182`, `SOW-0183`, `SOW-0184` |
| Supports Objectives (PACKAGE_HEURISTIC; ASSUMPTION) | `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package subject | NGL storage bullets (pressurized C3+ NGL product storage) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §"Product Storage and Pumps / NGL Storage Bullets" (lines 1627-1629); §"NGL C3+ Product" (line 448) |
| Storage configuration basis (count and size) | 16 x 120,000 USG storage bullets | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 448; §"Product Storage and Distribution Summary" line 492 |
| Production-rate basis | 15,400 bbl/d | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 448 |
| Storage duration basis | 2.5 days | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 448 |
| Stored product | C3+ NGL product (replaces retired C3/C4 storage concept) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 1627-1629 |
| Product disposition | Routed to NRM NEBC Connector via LACT | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 446, line 492 |
| Detailed bullet design parameters (pressure, temperature, materials, nozzles, internals) | TBD — "Detailed NGL bullet design parameters are not fully developed in the available product-storage basis and remain a required design-development item." | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 1629 |
| Required design-development item flag | Yes | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 1814 ("develop the detailed design basis for 16 x 120,000 USG NGL storage bullets") |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | Pressurized NGL (C3+) storage | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §2.5 "Pressurized Bullet Spacing" (lines 245-259); §"NGL Storage Bullets" |
| Truck/rail distribution | Not planned for NGL product from 04-25 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 446 |
| Governing spacing standard | API 2510 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §2.5 (lines 249-259) |
| Maximum bullets per cluster | <=6 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 249 (API 2510) |
| Minimum spacing between pressurized bullet clusters | 15.24 m (50 ft) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 250 (API 2510) |
| Minimum spacing bullet-to-property-line | 38.1 m (125 ft) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 259 (API 2510 Table 1) |
| Minimum spacing bullet-to-flare | 30.48 m (100 ft) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 284 (API 2510) |
| Minimum spacing bullet-to-fired-heater | 15.24 m (50 ft) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 299 (API 2510) |
| Minimum spacing bullet-to-suction-pump-skid | 3.05 m (10 ft) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 252 (API 2510) |
| Grading / containment intent | Sloped grading beneath bullets to redirect NGL away from pipe rack and process areas | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2722 |
| Design pressure | TBD (not stated in available source) |  |
| Design temperature range | TBD (not stated in available source) |  |
| Materials of construction | TBD (not stated in available source) |  |
| Insulation/heat-trace requirements | TBD (not stated in available source) |  |
| Relief/load data | TBD — to be developed per package-deliverables expectation (see Specification) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617 |

## Construction

| Item | Value | Source |
|---|---|---|
| Vendor scope | Engineering, design, fabrication/supply, and the physical equipment package | `_CONTEXT.md` Scope |
| Vendor deliverables (package-level expectation) | Datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, vendor document registers | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617 |
| Scope boundaries | Clear scope boundaries among process vendors, electrical/controls systems, field construction, and cross-facility utility interfaces (ASSUMPTION: applied to PKG-059 by analogy from project-wide mechanical-package basis) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617 |
| Fabrication standard | TBD (likely ASME Section VIII Div 1/2 for pressurized vessels — ASSUMPTION pending source confirmation) |  |
| Shop testing requirements | TBD |  |
| Surface preparation and coatings | TBD |  |
| Shipped-loose / field-mount items list | TBD |  |
| Vendor document register | TBD — required as a package deliverable | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617 |

## References

- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (NGL Storage Bullets section; Minimum Spacing Criteria; NGL C3+ Product; Product Storage and Distribution Summary; Spill containment grading)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Mechanical-package deliverables expectation, line 617)
- `_CONTEXT.md` (deliverable identity and scope)
- `_REFERENCES.md` (authoritative reference set; Gate-7 PROJECT_DECOMP snapshot)
- Workbook Packages row 83; `26020-Package_Requirements.docx` package heading 14 — `location TBD` (binary `.docx` source not locally rendered as markdown slice)
- API 2510 — referenced by DBM spacing tables; full standard text not locally accessible (`location TBD`)
- ASME Section VIII (pressure vessel code) — ASSUMPTION (likely applicable)
