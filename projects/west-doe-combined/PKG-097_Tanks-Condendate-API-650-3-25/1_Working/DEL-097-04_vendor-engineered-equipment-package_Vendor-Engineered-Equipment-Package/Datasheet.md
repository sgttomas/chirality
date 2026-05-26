# Datasheet — Vendor Engineered Equipment Package (PKG-097 Tanks, Condensate, API 650)

DeliverableID: `DEL-097-04_vendor-engineered-equipment-package`
ParentPackageID: `PKG-097`
PackageName: Tanks, Condensate (API 650) 3-25
Discipline: Mechanical
Type: Vendor Package Production Unit

## Identification

| Field | Value | Source |
|---|---|---|
| Package title | Tanks, Condensate (API 650) 3-25 | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv (GATE-07) |
| Vendor deliverable name | Vendor Engineered Equipment Package | `_CONTEXT.md` |
| Responsible party | Package Vendor (engineering / design / equipment supply) with EPC Integrator integration review | `_CONTEXT.md` |
| EPC anchor inputs | EPC Scope of Work (DEL-097-01); EPC Package Datasheet (DEL-097-02) | DELIVERABLE_REGISTER.csv (GATE-07) |
| Governing scope items | SOW-0201, SOW-0202, SOW-0203, SOW-0204 | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv |
| Supported objectives (PACKAGE_HEURISTIC) | OBJ-002, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 — **ASSUMPTION (best-effort package mapping)** | DELIVERABLE_REGISTER.csv |
| Source basis row | Workbook Packages row 88; 26020-Package_Requirements.docx heading 49 | `_REFERENCES.md` |

## Attributes (Physical Equipment Package — Condensate Storage Tanks)

The vendor's engineered scope corresponds to the condensate storage tankage and associated package-internal items defined by the 03-25 Liquids Hub DBM (3-25 Comp & Liquids).

| Attribute | Value | Source |
|---|---|---|
| Storage service | Condensate (sour inlet, sour, product, slop) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §"Condensate Storage and Product Handling" (line 404 ff.) |
| Number of tanks | 11 | DBM §"Condensate Storage and Product Handling" (line 406, 410) |
| Nominal capacity each | 3,800 bbl | DBM §"Condensate Storage and Product Handling" (line 406, 410) |
| Functional allocation | 2 sour inlet condensate; 4 sour condensate; 4 product condensate; 1 slop (unless superseded by final tank register) | DBM §"Condensate Storage and Product Handling" (line 406) |
| Tank construction code | API 650 (package title); API-650 Modified used for related produced-water tanks at site (analogy only — confirm for condensate) — **ASSUMPTION** | `_CONTEXT.md` package title; DBM §"Produced-Water Storage…" (analogy) |
| Sour-inlet upset storage basis | ~0.6 day across 2 x 3,800 bbl | DBM (line 411) |
| Vapour management | Tank vapours routed to VRU (2 x 200 hp electric, 2 x 100%); under SCA-002 VRU discharge rerouted to 04-25 SOC suction | DBM §"Vapour Recovery" (line 423 ff.) |
| Internal coating (analogous PW tanks; condensate TBC) | Devchem 253 internal coating on produced-water tanks — **ASSUMPTION** for condensate; location TBD | DBM §"Produced-Water Storage…" |
| External insulation / heating | External insulation and heating provided on related PW tanks; condensate tanks heating/insulation — TBD | location TBD; confirm in 26020-Package_Requirements.docx heading 49 |
| Design specific gravity | TBD (PW tank design SG 1.25 TBC; condensate value not given in available DBM slice) | location TBD |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service classification | Atmospheric storage of stabilized condensate (sour and product) | DBM §SEC-06 narrative (line 22, 40, 404 ff.) |
| Sour service applicability | Applies to sour-inlet and sour condensate tanks | DBM (line 406) |
| Blanket gas | LP fuel gas blanket noted for caustic tanks; condensate blanket basis — TBD | location TBD |
| Design temperature / pressure | TBD — not in available DBM slice; expected in 26020-Package_Requirements.docx heading 49 | location TBD |
| Seismic / wind / snow loads | TBD — site-specific loads to be confirmed in EPC Package Datasheet (DEL-097-02) | location TBD |

## Construction (Vendor Engineering Scope)

| Item | Value | Source |
|---|---|---|
| Engineering scope | Vendor engineering and design of the condensate tank package (mechanical, structural, instrumentation interfaces) | `_CONTEXT.md` Scope |
| Fabrication / supply scope | Vendor fabrication and supply of the physical equipment package | `_CONTEXT.md` Scope |
| Design basis input | EPC Scope of Work (DEL-097-01) and EPC Package Datasheet (DEL-097-02) | DELIVERABLE_REGISTER.csv (DEL-097-04 row) |
| Vendor outputs (artifacts) | Vendor engineered physical equipment package; vendor package design basis and datasheet set | `_CONTEXT.md` Anticipated Artifacts |
| Integration review | EPC Integrator integration review of vendor engineering, design, and equipment | `_CONTEXT.md` ResponsibleParty |
| Code of construction | API 650 (per package title) — confirm specific clause set in 26020-Package_Requirements.docx heading 49 | location TBD |
| Coating / lining specification | TBD (PW analogous: Devchem 253) | location TBD |
| Painting / external finish | TBD | location TBD |
| Nameplate / certification documentation | TBD — typically a vendor turnover artifact (cross-ref DEL-097-05) | location TBD |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (SEC-06 Liquids Hub, Condensate Storage and Product Handling; Produced-Water Storage; Vapour Recovery)
- `_Sources/26020-Package_Requirements.docx` package heading 49 — **inaccessible as text in current toolchain; relevant slices location TBD**
- DELIVERABLE_REGISTER.csv (GATE-07_Final_Published_2026-05-24)
