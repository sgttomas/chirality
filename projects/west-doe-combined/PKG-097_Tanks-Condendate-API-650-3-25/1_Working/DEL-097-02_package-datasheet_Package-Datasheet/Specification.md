# Specification — Package Datasheet (DEL-097-02)

Deliverable: `DEL-097-02_package-datasheet`
Package: `PKG-097` — Tanks, Condensate (API 650) 3-25 (`26020-03-PT-19-006`)

## Scope

This specification defines the normative content of the EPC Integrator Package Datasheet for the 3-25 Liquids Hub Condensate Storage Tanks package. The Package Datasheet provides the technical handoff basis for third-party (vendor) package engineering and design of four (4) 3,800 bbl C5+ condensate product storage tanks, including design conditions, code basis, fittings, coating, and the package interface matrix.

In scope:
- Equipment identification, attributes, operating/design conditions, materials and coatings, fittings (PVRV/EPRV/VRU/blanket gas).
- Package boundary statement (vendor scope vs. By-Others).
- Physical interface matrix (process piping, relief/flare/vent, drain/containment, lighting, grounding, cathodic protection, I&C, civil, structural).
- References to upstream source materials.

Excluded (per source):
- Foundations, on-site mounting of tanks. (26020-Package_Requirements.docx §49 Scope Notes — By Others)
- Electrical / instrumentation field installation. (same source)
- Platforms, staircases, ladders site installation. (same source)
- Truck loading (separate package); Pipeline/pigging; HVAC; F&G; Maintenance access. (26020-Package_Requirements.docx §49 Physical Interface Summary, "No")

## Requirements

| ReqID | Requirement | Source | Verification (see Procedure) |
|---|---|---|---|
| R-01 | Supply four (4) 3,800 bbl condensate product storage tanks for C5+ condensate service. | 26020-Package_Requirements.docx §49 Basic Scope | V-01 |
| R-02 | Design and fabricate tanks to modified API 650. | 26020-Package_Requirements.docx §49 Major Included Equipment | V-02 |
| R-03 | Tanks are non-insulated atmospheric storage; a recycle may be required to maintain a winter operating temperature. | 26020-Package_Requirements.docx §49 Major Included Equipment | V-03 |
| R-04 | Provide a blanket-gas system in accordance with API 2000. | 26020-Package_Requirements.docx §49 Major Included Equipment | V-04 |
| R-05 | Provide internal coating (Devchem 253) on floors, walls, and roof of each tank. | 26020-Package_Requirements.docx §49 Major Included Equipment | V-05 |
| R-06 | Each tank shall include a PVRV (vacuum or modulating pressure relief). | 26020-Package_Requirements.docx §49 Major Included Equipment | V-06 |
| R-07 | Each tank shall include an EPRV designed for the single worst-case relief event. | 26020-Package_Requirements.docx §49 Major Included Equipment | V-06 |
| R-08 | Each tank shall include a VRU header connection. | 26020-Package_Requirements.docx §49 Major Included Equipment | V-06 |
| R-09 | Each tank shall include a blanket-gas connection. | 26020-Package_Requirements.docx §49 Major Included Equipment | V-06 |
| R-10 | Maximum fill (shutdown trip) shall be 90%. | 26020-Package_Requirements.docx §49 Major Included Equipment | V-07 |
| R-11 | Tank nozzles shall be sized so plant design capacity can fill a single tank. | 26020-Package_Requirements.docx §49 Major Included Equipment | V-08 |
| R-12 | Operating conditions: atmospheric pressure; 0 °C min / 40 °C max temperature. | 26020-Package_Requirements.docx §49 Scope Notes | V-09 |
| R-13 | Design conditions: 32 oz test pressure; −40 °C min / 60 °C max design temperature. | 26020-Package_Requirements.docx §49 Scope Notes | V-09 |
| R-14 | Package throughput basis: 94,940 kg/h and 3,187 Am³/d (Preliminary Design conditions). | 26020-Package_Requirements.docx §49 Scope Notes | V-10 |
| R-15 | Excluded from package: foundations, site mounting, field electrical/instrumentation installation, platforms, staircases. | 26020-Package_Requirements.docx §49 Scope Notes | V-11 |
| R-16 | Provide physical interfaces as specified in the Interface Summary (Process Piping, Relief/Flare/Vent, Drain/Containment, Lighting, Grounding, Cathodic Protection, I&C, Grading/Spill Containment, Structural/Foundations interface). | 26020-Package_Requirements.docx §49 Physical Interface Summary | V-12 |
| R-17 | ASSUMPTION — Materials of construction for shell, roof, and floor shall comply with API 650 (modified) for −40 °C minimum design metal temperature; exact MOC values are TBD pending vendor selection / RFQ source. | location TBD (Bid Docs/Budgetary/26020-03-PT-RFQ-19-006) | V-13 |
| R-18 | ASSUMPTION — Tanks store stabilized C5+ condensate consistent with the 3-25 Liquids Hub product service; per-tank routing (e.g., product vs. recycle) is TBD. | 3-25_Comp_and_Liquids_DBM.md §"Liquids Hub" (directional); per-tank routing — location TBD | V-14 |

## Standards

| Standard | Use | Source / Location |
|---|---|---|
| API 650 (modified) | Tank design and fabrication code | 26020-Package_Requirements.docx §49 Major Included Equipment; specific modification clauses — location TBD |
| API 2000 | Blanket-gas / pressure-vacuum venting basis | 26020-Package_Requirements.docx §49 Major Included Equipment; clause refs — location TBD |
| Devchem 253 datasheet (manufacturer) | Internal coating system on floor/walls/roof | 26020-Package_Requirements.docx §49 Major Included Equipment; manufacturer datasheet — location TBD |
| CSA / provincial regulatory codes (BC) | Likely applicable to onsite construction interfaces; not directly cited in source | ASSUMPTION; location TBD |

## Verification

| VID | Verification approach | Maps to |
|---|---|---|
| V-01 | Confirm package register / equipment list shows quantity = 4 and capacity = 3,800 bbl each. | R-01 |
| V-02 | Confirm vendor design package cites API 650 (modified) and lists the applicable modifications. | R-02 |
| V-03 | Confirm datasheet identifies "non-insulated, atmospheric" and notes winter recycle provision. | R-03 |
| V-04 | Confirm blanket-gas system design / calculation references API 2000. | R-04 |
| V-05 | Confirm coating specification cites Devchem 253 for floor, walls, and roof. | R-05 |
| V-06 | Inspect tank fittings list/general arrangement for PVRV, EPRV, VRU header connection, and blanket-gas connection on each tank. | R-06, R-07, R-08, R-09 |
| V-07 | Confirm instrumentation/control narrative includes 90% high-fill shutdown. | R-10 |
| V-08 | Confirm nozzle sizing calculation demonstrates single-tank fill at plant design capacity. | R-11 |
| V-09 | Confirm datasheet captures operating and design pressure/temperature exactly as the source. | R-12, R-13 |
| V-10 | Confirm capacity / throughput basis 94,940 kg/h and 3,187 Am³/d are recorded. | R-14 |
| V-11 | Confirm package boundary section states By-Others items explicitly. | R-15 |
| V-12 | Confirm physical interface matrix matches source row 88 / §49 table. | R-16 |
| V-13 | Confirm MOC selection meets −40 °C MDMT (API 650 Annex requirements as applicable). | R-17 |
| V-14 | Confirm service description and per-tank routing are resolved from RFQ / DBM before issue. | R-18 |

## Documentation (anticipated artifacts)

Per `_CONTEXT.md` Anticipated Artifacts and 26020-Package_Requirements.docx §49 Vendor Engineering Deliverables:

- Package technical datasheet (this deliverable's output artifact).
- Vendor engineering handoff basis (RFQ-ready datasheet + interface matrix).
- Package interface requirements matrix.
- Source-supported equipment and design criteria.
- Cross-references to vendor deliverables enumerated in §49 (MEC-001, MEC-002, MEC-003, MEC-005, MEC-006, MEC-011, MEC-014, MEC-016, MEC-017, MEC-018, MEC-021, MEC-022, MEC-023, MEC-024, MEC-025; PRO-014, PRO-015, PRO-016, PRO-017, PRO-018, PRO-008, PRO-023; PIP-003, PIP-004, PIP-006, PIP-007, PIP-008, PIP-009, PIP-017, PIP-018, PIP-024, PIP-025, PIP-028; ELE-017, ELE-012, ELE-019; PLN-015, PLN-016; INS-002, INS-003, INS-005, INS-006, INS-008, INS-009, INS-010, INS-011, INS-016, INS-017, INS-018, INS-025, INS-029; CTL-003, CTL-005, CTL-006, CTL-026; STR-001, STR-002, STR-004, STR-005, STR-006, STR-011, STR-012, STR-013, STR-014, STR-020; CIV-003, CIV-004, CIV-014, CIV-015, CIV-019; QLT-003, QLT-006, QLT-013, QLT-020, QLT-021; PRQ-009, PRQ-013, PRQ-015, PRQ-016; DOC-008).
