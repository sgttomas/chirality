# Datasheet — DEL-098-01 Scope of Work

> Descriptive datasheet for the EPC Integrator Scope of Work covering PKG-098 Tanks, Sour Water (API 650) 3-25.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-098-01_scope-of-work` | `_CONTEXT.md` Identity |
| Deliverable Name | Scope of Work | `_CONTEXT.md` Identity |
| Parent Package | `PKG-098` — Tanks, Sour Water (API 650) 3-25 | `_CONTEXT.md` Identity |
| Workbook Package Row | 93 | `_CONTEXT.md` Source Reference |
| Discipline | Mechanical | `_CONTEXT.md` Identity |
| Type | EPC Scope of Work | `_CONTEXT.md` Identity |
| Responsible Party | EPC Integrator | `_CONTEXT.md` Identity |
| Authoritative Package Source | `26020-Package_Requirements.docx`, Heading 1 `26020-03-PT-19-007 - Tanks, Sour Water` | `_REFERENCES.md`; located in `_Sources/26020-Package_Requirements.docx` |
| Companion DBM Source | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` | `_REFERENCES.md` Shared Source Root |
| Source Basis (per Package Req) | `Bid Docs/Budgetary/26020-03-PT-RFQ-19-007 - Sour Water Tanks.docx` | Package Requirements §`26020-03-PT-19-007` (Location/Status table) |
| Location / Status | "3-25 liquids area and related compressor station scope; vetted package scope basis." | Package Requirements §`26020-03-PT-19-007` (Location/Status table) |

## Attributes — Package Identity and Tagged Equipment

The Scope of Work covers the following tagged equipment groupings as enumerated in the authoritative package source `26020-03-PT-19-007 - Tanks, Sour Water`, "Major Included Equipment":

| Item | Quantity / Size | Tags | Process Function | Source |
|---|---|---|---|---|
| Item 1 — Sour Produced Water Storage Tanks | 3 × 3,800 bbl | TK-9030-2, TK-9040-2, TK-9050-2 | Sour Water Tanks | Package Requirements §`26020-03-PT-19-007` Major Included Equipment |
| Item 2 — Sour Inlet Produced Water Storage Tanks | 2 × 3,800 bbl | TK-9010-2, TK-9020-2 | Sour inlet produced-water storage | Package Requirements §`26020-03-PT-19-007` Major Included Equipment |
| Item 3 — Produced Water Storage Tanks | 2 × 3,800 bbl | TK-9010-1, TK-9020-1 | Produced-water storage | Package Requirements §`26020-03-PT-19-007` Major Included Equipment |

ASSUMPTION: Items 2 and 3 share the common technical basis stated for Item 1 ("Below is the common information for Item No. 1 to 3"). Tank service designations for Items 2 and 3 are recorded as in the source; functional classification within the produced-water tank farm is governed by the final tank register (see Conflict Table in `Guidance.md`).

## Conditions

| Parameter | Value | Source |
|---|---|---|
| Operating Pressure | Atmospheric | Package Requirements §`26020-03-PT-19-007` Scope Notes / Open Items |
| Operating Temperature (Items 1, 3) | 10 °C | Package Requirements §`26020-03-PT-19-007` Scope Notes / Open Items |
| Operating Temperature (Item 2) | TBD (per source) | Package Requirements §`26020-03-PT-19-007` Scope Notes / Open Items |
| Design Pressure | 32 oz test pressure | Package Requirements §`26020-03-PT-19-007` Scope Notes / Open Items |
| Design Temperature (min) | -40 °C | Package Requirements §`26020-03-PT-19-007` Scope Notes / Open Items |
| Design Temperature (max) | 60 °C | Package Requirements §`26020-03-PT-19-007` Scope Notes / Open Items |
| Driver | TBD (per source) | Package Requirements §`26020-03-PT-19-007` Scope Notes / Open Items |
| Capacity / Design Throughput | "See attached in Appendix A" of source RFQ | Package Requirements §`26020-03-PT-19-007` Scope Notes / Open Items; location TBD (Appendix A not locally accessible) |
| Produced-water design SG (facility basis) | 1.25 TBC; pump fluid SG basis 1.18 (discrepancy to close in detailed design) | DBM `3-25_Comp_and_Liquids_DBM.md` §"produced-water system" |

## Construction

| Attribute | Value | Source |
|---|---|---|
| Design & Fabrication Code | Modified API 650 | Package Requirements §`26020-03-PT-19-007` Major Included Equipment; corroborated by DBM "Tanks are API-650 Modified atmospheric tanks" |
| Internal Coating | Devchem 253 applied to floor, walls, and roof | Package Requirements §`26020-03-PT-19-007` Major Included Equipment; DBM corroboration |
| External Treatment | External insulation with electric heating | Package Requirements §`26020-03-PT-19-007` Major Included Equipment; DBM corroboration |
| Skim System | Kennilworth type HCL float skim system, one per tank | Package Requirements §`26020-03-PT-19-007` Major Included Equipment |
| Material of Construction | TBD (not stated in accessible package source slice; DBM does not specify shell material) | location TBD |
| Foundation, mounting, E&I, platforms, staircases | By others (excluded from package scope) | Package Requirements §`26020-03-PT-19-007` Scope Notes / Open Items |

## Whole-Facility Integration (Descriptive)

PKG-098 sits in the 03-25 Liquids Hub produced-water subsystem. The Liquids Hub "receives stabilized condensate from 04-25, 06-29 Canlin, and future third-party sources… manages produced water and H2O2 treatment, provides VRU service for tank vapours, and supports truck loading" (DBM §"facility receives Doe field sour wellstream fluids…" and following). The hub-level produced-water tank set is described in the DBM as "seven 3,800 bbl tanks: five sour produced-water tanks and two sweet produced-water tanks" (DBM §"produced-water system"). PKG-098 contributes seven of these tanks per the authoritative package source.

ASSUMPTION: The DBM "five sour + two sweet" allocation versus the package source's Item 1 (3 sour) + Item 2 (2 sour inlet) + Item 3 (2 produced water) enumeration is treated as the same seven-tank set under different functional labels. Reconciliation is captured in the Conflict Table in `Guidance.md`.

## Anticipated Artifacts (as decomposed)

- Package scope of work
- Tagged equipment and package identity list
- Package function and integration narrative
- Responsibility assignment record

Source: `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-098-01_scope-of-work`.

## References

- `_Sources/26020-Package_Requirements.docx`, Heading 1 §`26020-03-PT-19-007 - Tanks, Sour Water` (Basic Scope, Major Included Equipment, Scope Notes / Open Items, Physical Interface Summary, Vendor Engineering Deliverables, Interface Coordination Notes)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (facility narrative; produced-water system basis; layout/electrical/area provisions)
- `_REFERENCES.md` (PROJECT_DECOMP GATE-07 snapshot; deliverable register; objective-scope map)
- Source-cited but not locally accessible:
  - `26020-Packages_Interfaces.3.xlsx` (Physical Interface Summary source) — location TBD
  - `Bid Docs/Budgetary/26020-03-PT-RFQ-19-007 - Sour Water Tanks.docx` (Source Basis) — location TBD
  - Appendix A to the RFQ (capacity/design throughput attachment) — location TBD
