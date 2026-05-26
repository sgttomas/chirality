# Package Datasheet Specification — Flare KO Drum (High Pressure) 4-25 (PKG-054)

> Normative requirements that the Package Datasheet (`DEL-054-02`) shall satisfy. Requirements are drawn from the GATE-07 PROJECT_DECOMP snapshot and the DBM-Deepcut source slices listed in `_REFERENCES.md`.

## Scope

This specification governs the EPC Integrator-authored Package Datasheet for the High-Pressure Flare KO Drum package (`PKG-054`) at the 04-25 (Deepcut) facility, including the tagged equipment V-4100-1 (H.P. FLARE K.O. DRUM) and P-4100-1 (HP FLARE K.O. DRUM TRANSFER PUMP).

### In scope

- Package identity, tags, and module-assembly classification.
- Process service envelope, header-interface conditions, and backpressure basis at the HP flare KO drum.
- Spacing, freeze protection, and other regulatory/DBM-derived constraints applicable to the HP KO drum package.
- The interface boundary between the EPC scope and the third-party vendor or discipline package engineering scope.

### Out of scope

- Detailed mechanical design calculations (vessel sizing, PSV sizing, pump hydraulics). These remain with the package vendor or detailed-design discipline.
- Construction Work Package content (covered by `DEL-054-03`).
- Vendor document turnover content (covered by `DEL-054-05`).
- LP flare KO drum (V-3900-1) and cryogenic flare KO drum (V-4110-1) primary scope; referenced only where they share routing or shop module with V-4100-1.

## Requirements

| ID | Requirement | Source / Note |
|---|---|---|
| REQ-DS-01 | The datasheet shall identify the package using the canonical decomposition IDs `PKG-054` and `DEL-054-02_package-datasheet`. | `_CONTEXT.md`; GATE-07 register |
| REQ-DS-02 | The datasheet shall list tagged equipment V-4100-1 and P-4100-1 with descriptions exactly as carried in the Deepcut DBM tag table. | DBM-Deepcut lines 2579-2580 |
| REQ-DS-03 | The datasheet shall declare the package as shop-fabricated module 410-1 (HP / Cryo Flare KO Drum Module). | DBM-Deepcut line 2784 |
| REQ-DS-04 | The datasheet shall declare the HP flare relief header size at the vessel as 508 mm (20 in) and the downstream HP flare main header as 762 mm SA-333. | DBM-Deepcut lines 2028, 2039 |
| REQ-DS-05 | The datasheet shall record peak built-up backpressure design basis of 695 kPag (100 psig) during peak blowdown coinciding with the highest fire-zone load, and a typical PSV maximum total backpressure limit of less than 1172 kPag (170 psig) under the 150# flange rating. | DBM-Deepcut line 2044 |
| REQ-DS-06 | The datasheet shall record the connected service definition: balance-of-plant outside the cryogenic unit and low-pressure equipment routed to the HP flare; combined with cryogenic flare downstream of both KO drums before the common HP/cryo stack. | DBM-Deepcut lines 2027-2028 |
| REQ-DS-07 | The datasheet shall record the regulatory and DBM spacing constraint of 10 m (32 ft) minimum from flare KO drums to vegetation and other fire hazards, citing OGAOM Sec. 9.6.15. | DBM-Deepcut line 287 |
| REQ-DS-08 | The datasheet shall record freeze protection requirements: HP flare headers outside heated buildings shall be electrically heat traced and insulated, except PSV outlets that free-drain into the flare header. | DBM-Deepcut line 2033 |
| REQ-DS-09 | The datasheet shall require that any blended gas mixture directed to flare meet LHV >= 20 MJ/Sm3. | DBM-Deepcut line 2033 |
| REQ-DS-10 | Liquid disposition from V-4100-1 shall be by transfer pump P-4100-1 with truck-out provision. | DBM-Deepcut line 2028 |
| REQ-DS-11 | The datasheet shall mark all values not present in accessible source material as `TBD` (e.g., vessel dimensions, design P/T, MOC, MAWP, pump hydraulic curve, relief load set). | Skill rule: no invented values |
| REQ-DS-12 | The datasheet shall cite source for each non-trivial value (SourcePath + SectionRef or location TBD). | Skill source-grounding rule |
| REQ-DS-13 | The datasheet shall align with the package scope items covered by `DEL-054-02` (`SOW-0075`, `SOW-0076`, `SOW-0077`, `SOW-0078`). | `_CONTEXT.md` |
| REQ-DS-14 | The datasheet shall record that the package supports objectives `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION via PACKAGE_HEURISTIC objective association). | `_CONTEXT.md`; skill default mode |
| REQ-DS-15 | The datasheet shall preserve interface facts (e.g., shared HP/cryo stack at 03-25, shared with 04-25) as evidence within this deliverable rather than as a separate deliverable. | `_CONTEXT.md` Notes; GATE-07 register row |

## Standards

| Standard / Reference | Applicability | Location |
|---|---|---|
| OGAOM Sec. 9.6.15 (BC Oil and Gas Activity Operations Manual — Flare and Incinerator Spacing) | Spacing of flare KO drums to vegetation and fire hazards (10 m / 32 ft) | DBM-Deepcut line 287; full standard location TBD |
| BCER Oil and Gas Processing Facility Regulation, Appendix 1, Schedule 1, Sec. 2 / Sec. 7(4) | Thermal radiation flux limits at flare boundaries; informs siting of KO drum module | DBM-Deepcut lines 285-286, 2050-2057; regulation text location TBD |
| API 2510 | Spacing between flare and pressurized bullets (referenced in DBM spacing basis) | DBM-Deepcut line 284; full standard location TBD |
| ASME BPVC Sec. VIII Div. 1 | Pressure vessel design code for V-4100-1 | ASSUMPTION (industry-standard for HP flare KO drums); not explicit in source; location TBD |
| ASME B31.3 | Process piping code for relief headers connecting to V-4100-1 | ASSUMPTION; not explicit in source; location TBD |
| 26020-Package_Requirements.docx, package heading 9 | EPC package requirements applicable to PKG-054 | DELIVERABLE_REGISTER source basis; native .docx not parsed; location TBD |

## Verification

| Requirement | Verification Approach |
|---|---|
| REQ-DS-01 / REQ-DS-02 / REQ-DS-13 / REQ-DS-14 | Cross-check IDs and tag names against GATE-07 registers and `_CONTEXT.md` during datasheet review. |
| REQ-DS-03 | Confirm module 410-1 entry in DBM-Deepcut module table is reflected on the datasheet's Construction section. |
| REQ-DS-04 / REQ-DS-05 / REQ-DS-06 | Cross-reference values to DBM-Deepcut Flare Equipment and Routing and Flare Header and Backpressure Basis tables. |
| REQ-DS-07 / REQ-DS-08 / REQ-DS-09 | Confirm regulatory/DBM constraints appear with the cited source clauses. |
| REQ-DS-10 | Confirm pump disposition statement matches DBM-Deepcut Flare Equipment and Routing table. |
| REQ-DS-11 / REQ-DS-12 | Datasheet review confirms every value either has a citation, is labeled ASSUMPTION, or is labeled TBD. |
| REQ-DS-15 | Confirm interface facts are surfaced within this deliverable folder rather than as a sibling deliverable. |

## Documentation

The Package Datasheet deliverable shall include the following artifacts (per `_CONTEXT.md` Anticipated Artifacts):

- Package technical datasheet (`Datasheet.md`).
- Vendor engineering handoff basis (captured in `Datasheet.md` Conditions/Construction and in `Guidance.md`).
- Package interface requirements matrix (TBD — to be developed from `26020-Packages_Interfaces_4_export.xlsx` once parsed; placeholder remains in `Datasheet.md` Open Items).
- Source-supported equipment and design criteria (captured in `Datasheet.md` Attributes/Conditions with citations).
- This Specification (`Specification.md`), Guidance (`Guidance.md`), and Procedure (`Procedure.md`).
