# Datasheet — Package Datasheet (DEL-097-02)

Deliverable: `DEL-097-02_package-datasheet`
Package: `PKG-097` — Tanks, Condensate (API 650) 3-25
Tag basis: `26020-03-PT-19-006 - Tanks, Condensate`
Source basis: `26020-Package_Requirements.docx` (Heading 1 #49), `26020-Packages_Interfaces_4_export.xlsx` (Workbook Packages row 88), `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.

Spelling note: Project register uses "Condendate"; authoritative source spelling is "Condensate". Treated as cosmetic; functional identity matches via tag `26020-03-PT-19-006`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-097-02_package-datasheet | `_CONTEXT.md` |
| Name | Package Datasheet | `_CONTEXT.md` |
| ParentPackageID | PKG-097 | `_CONTEXT.md` |
| ParentWorkbookID | 97 | `_CONTEXT.md` |
| PackageName (register) | Tanks, Condendate (API 650) 3-25 | DELIVERABLE_REGISTER.csv |
| Package tag (source) | 26020-03-PT-19-006 — Tanks, Condensate | 26020-Package_Requirements.docx H1 #49 |
| Facility / Location | 03-25 West Doe Liquids Hub tank farm (LSD 03-25-80-15W6, near Dawson Creek, BC) | 26020-Package_Requirements.docx §49 (Location table); 3-25_Comp_and_Liquids_DBM.md §1 |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Source Basis (RFQ) | Bid Docs/Budgetary/26020-03-PT-RFQ-19-006 - Conde Tanks.docx (referenced; not locally read for this run) | 26020-Package_Requirements.docx §49 (Location/Status table) |

## Attributes (Equipment)

| Attribute | Value | Source |
|---|---|---|
| Process function | C5+ Condensate (product) storage | 26020-Package_Requirements.docx §49 / Basic Scope |
| Quantity | Four (4) tanks | 26020-Package_Requirements.docx §49 / Basic Scope |
| Capacity (per tank, nominal) | 3,800 bbl | 26020-Package_Requirements.docx §49 / Basic Scope |
| Tank design code | Modified API 650 | 26020-Package_Requirements.docx §49 / Major Included Equipment |
| Insulation | Non-insulated (atmospheric); winter recycle may be required to maintain temperature | 26020-Package_Requirements.docx §49 / Major Included Equipment |
| Blanket gas | Per API 2000 | 26020-Package_Requirements.docx §49 / Major Included Equipment |
| Internal coating (floor, walls, roof) | Devchem 253 | 26020-Package_Requirements.docx §49 / Major Included Equipment |
| Pressure / vacuum relief | PVRV (vacuum or modulating pressure relief), each tank | 26020-Package_Requirements.docx §49 / Major Included Equipment |
| Emergency pressure relief | EPRV (single worst-case relief), each tank | 26020-Package_Requirements.docx §49 / Major Included Equipment |
| Vapour management | VRU header connection, each tank | 26020-Package_Requirements.docx §49 / Major Included Equipment |
| Blanket-gas connection | Each tank | 26020-Package_Requirements.docx §49 / Major Included Equipment |
| Fill limit | Maximum fill 90% (shutdown) | 26020-Package_Requirements.docx §49 / Major Included Equipment |
| Fill rate | Tank nozzles sized so that plant design capacity can fill a single tank | 26020-Package_Requirements.docx §49 / Major Included Equipment |

## Conditions

| Parameter | Value | Source |
|---|---|---|
| Operating pressure | Atmospheric (ambient) | 26020-Package_Requirements.docx §49 / Scope Notes table |
| Operating temperature | 0 °C min / 40 °C max | 26020-Package_Requirements.docx §49 / Scope Notes table |
| Design pressure | 32 oz test pressure (≈2 psig) | 26020-Package_Requirements.docx §49 / Scope Notes table |
| Design temperature | −40 °C min / 60 °C max | 26020-Package_Requirements.docx §49 / Scope Notes table |
| Capacity / design throughput basis (package) | 94,940 kg/h; 3,187 Am³/d (Preliminary Design conditions) | 26020-Package_Requirements.docx §49 / Scope Notes table |
| Site ambient minimum (winterization basis) | −40 °C | 3-25_Comp_and_Liquids_DBM.md §"Site" |
| Hub-level C5+ condensate throughput context | 3,180 m³/d ≈ 20,000 bbl/d (Liquids Hub total) | 3-25_Comp_and_Liquids_DBM.md §"Condensate and Produced-Water Receipts" |
| Service classification | Stabilized C5+ condensate product (post-mercaptan-treating product storage) — ASSUMPTION based on DBM Liquids Hub narrative; specific service per tank routing TBD | 3-25_Comp_and_Liquids_DBM.md §"Liquids Hub" |

## Construction

| Attribute | Value | Source |
|---|---|---|
| Code of construction | Modified API 650 | 26020-Package_Requirements.docx §49 / Major Included Equipment |
| Venting / pressure-vacuum relief sizing standard | API 2000 (blanket-gas system) | 26020-Package_Requirements.docx §49 / Major Included Equipment |
| Geometry / orientation | Atmospheric vertical storage tank (ASSUMPTION based on API 650 modified + 3,800 bbl service); detailed geometry TBD | source location TBD |
| Materials of construction (shell/roof/floor) | TBD | source location TBD |
| Roof type | TBD | source location TBD |
| Foundation, mounting, platforms, staircases | By Others (excluded from package) | 26020-Package_Requirements.docx §49 / Scope Notes table |
| Electrical / instrumentation installation at site | By Others | 26020-Package_Requirements.docx §49 / Scope Notes table |
| Internal coating system | Devchem 253 on floor, walls, roof | 26020-Package_Requirements.docx §49 / Major Included Equipment |
| External coating / paint system | TBD | source location TBD |
| Cathodic protection | Required interface (Yes) — design by CP design package interface | 26020-Package_Requirements.docx §49 / Physical Interface Summary |
| Heat tracing / EHT | Not required at package boundary (EHT interface = No) | 26020-Package_Requirements.docx §49 / Physical Interface Summary |

## Package Boundary (By Others — exclusions)

- Foundations, mounting tanks at site.
- Electrical and instrumentation site installation.
- Platforms, staircases, ladders site installation.
Source: 26020-Package_Requirements.docx §49 / Scope Notes table.

## Physical Interface Summary

Interface source: `26020-Packages_Interfaces_4_export.xlsx` row 88 (per 26020-Package_Requirements.docx §49 Physical Interface Summary).

| Interface Type | Applicability | Notes |
|---|---|---|
| Process Piping | Yes | Vendor / EPC tie-in scope; tie-ins per Tie-In List |
| Utility Piping | No | — |
| Relief / Flare / Vent | Yes | PVRV, EPRV, VRU header connection per tank |
| Drain / Containment | Yes | Bund / secondary containment by EPC civil interface |
| Electrical Power | No | — |
| Area / Exterior Lighting | Yes | Workbook Packages row 88, column M |
| EHT | No | — |
| Grounding / Bonding | Yes | EPC ground grid interface |
| Cathodic Protection | Yes | CP design package interface |
| I&C / Control Cabling | Yes | Instrument hookup, loop, wiring termination |
| Communications / Network | No | — |
| Building HVAC / Services | No | — |
| Fire & Gas / Safety Systems | No | — |
| Maintenance Access | No | — |
| Grading / Site Drainage / Spill Containment | Yes | Civil grading + retention pond / containment basin |
| Structural / Foundations / Supports | Yes | Foundations and embedment by EPC structural |
| Product Loading | No | Truck loading is a separate package (PKG covering 26020-…-23-001) |
| Pipeline / Pigging | No | — |

Source for entire table: 26020-Package_Requirements.docx §49 / Physical Interface Summary.

## References

- 26020-Package_Requirements.docx (Heading 1 #49 — Tanks, Condensate)
- 26020-Packages_Interfaces_4_export.xlsx (Workbook Packages row 88)
- DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (3-25 facility design basis memo)
- Bid Docs/Budgetary/26020-03-PT-RFQ-19-006 - Conde Tanks.docx (Source Basis cited by §49; not read locally — location TBD)
- GATE-07 PROJECT_DECOMP snapshot (`/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`)
