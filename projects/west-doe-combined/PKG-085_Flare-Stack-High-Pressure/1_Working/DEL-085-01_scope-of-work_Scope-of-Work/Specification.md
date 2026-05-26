# Specification — DEL-085-01 Scope of Work (PKG-085 Flare Stack (High Pressure))

## Scope

This Scope of Work normatively defines the EPC Integrator scope for PKG-085 Flare Stack (High Pressure), framed as a Reference/interface package for the common HP/Cryo flare stack (FL-4120-1) that serves HP and cryogenic flare relief and blowdown for the 03-25 and 04-25 facilities. The EPC Integrator scope covers facility-level integration, interface definition, tie-in design, constructability, procurement/construction coordination, and integration acceptance. Package engineering, package design, vendor documentation, and the physical equipment package are owned by the Package Vendor under DEL-085-04 and DEL-085-05.

In scope of this SoW (EPC Integrator):

- Package identity and tagged-equipment list anchoring (FL-4120-1 and downstream shared flare-stack interface content). [SCOPE_LEDGER SOW-0089]
- Package function and integration narrative including the shared 03-25/04-25 service basis. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines ~56, 497-501]
- Boundaries definition with the HP knockout-drum manifold (V-4100-2, V-4150-2), the 508 mm HP relief header, and downstream stack interfaces. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines ~497-499]
- Whole-facility integration narrative including utility piping, relief/flare/vent, drain/containment, electrical power, grounding/bonding, I&C/control cabling, fire & gas/safety systems, and structural/foundations/supports interfaces. [PACKAGE_REGISTER row 58 — Applicable Interface Types]
- Responsibility assignment record for Package Vendor vs. EPC Integrator roles. [PACKAGE_REGISTER row 58 — Responsibility Model; DELIVERABLE_REGISTER row 312]

Out of scope of this SoW:

- Package engineering, package design, vendor documentation, and physical equipment supply (assigned to DEL-085-04 and DEL-085-05). [DELIVERABLE_REGISTER rows 315-316]
- Construction execution detail (assigned to DEL-085-03 Construction Work Package). [DELIVERABLE_REGISTER row 314]
- Package datasheet content beyond identity/interface summary (assigned to DEL-085-02). [DELIVERABLE_REGISTER row 313]
- EPC vendor package review and acceptance evidence (assigned to DEL-085-06). [DELIVERABLE_REGISTER row 317]

## Requirements

| Req ID | Requirement | Source / Authority |
|---|---|---|
| R-085-01-01 | The SoW shall identify the package by Workbook tracking number 26020-02-25-001 and name "Flare Stack (High Pressure)". | PACKAGE_REGISTER row 58 |
| R-085-01-02 | The SoW shall list the tagged equipment as HP flare stack FL-4120-1 and downstream shared flare-stack interface content. | SCOPE_LEDGER SOW-0089 |
| R-085-01-03 | The SoW shall state the package function as a Reference/interface package for the common HP/Cryo flare stack serving HP and cryogenic flare systems. | PACKAGE_REGISTER row 58; SCOPE_LEDGER SOW-0088 |
| R-085-01-04 | The SoW shall record that the stack is a shared 03-25/04-25 asset and is treated as an interface/reference package unless the boundary ruling changes. | SCOPE_LEDGER SOW-0090; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line ~56 |
| R-085-01-05 | The SoW shall define the HP relief header inlet boundary as the 508 mm HP relief header manifolding V-4100-2 (compressor area) and V-4150-2 (tank farm) to the HP flare. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines ~497-499 |
| R-085-01-06 | The SoW shall reference HP-flare-served loads of record from the DBMs, including but not limited to pig-receiver vents, stabilizer flash/feed and tower relief and blowdown, SOC blowdown, MPFF, and TEG contactor automated blowdown. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line ~354; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines ~585, 704, 813, 838-842 |
| R-085-01-07 | The SoW shall require staggered blowdown to limit maximum relief and shall reference the Plant Shutdown and Blowdown Philosophy W242510-PRC-REP-000003-001 as the governing detailed source for final blowdown sequencing. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line ~501 |
| R-085-01-08 | The SoW shall enumerate the eight applicable interface types: Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; Grounding/Bonding; I&C/Control Cabling; Fire & Gas/Safety Systems; Structural/Foundations/Supports. | PACKAGE_REGISTER row 58 |
| R-085-01-09 | The SoW shall record the Responsibility Model: Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration). | PACKAGE_REGISTER row 58 |
| R-085-01-10 | The SoW shall identify the four anticipated artifacts: package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. | DELIVERABLE_REGISTER row 312 |
| R-085-01-11 (ASSUMPTION) | The SoW supports OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 per the package-grouping objective heuristic for PKG-085. Treat as directional context until a deliverable-ID-level objective map is confirmed. | DELIVERABLE_REGISTER row 312; OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC (ASSUMPTION) |
| R-085-01-12 | Stack mechanical attributes shall reflect accessible source values: sonic HP/Cryo stack 660 mm OD x 60,957 mm tall. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line ~499 |
| R-085-01-13 (TBD) | Governing codes and standards (e.g., API 521 relief sizing, API 537 flare equipment) shall be cited; specific clause-level requirements are TBD pending access to 26020-Package_Requirements.docx package heading 38 source slices. | `TBD` — source-binary, location TBD |
| R-085-01-14 (TBD) | Site location, design pressure/temperature of the stack, materials of construction, pilot/ignition/purge provisions, and emissions/radiation acceptance criteria are TBD pending access to vendor datasheet inputs and the Word package requirements section. | `TBD` |

## Standards

| Standard | Applicability | Locator |
|---|---|---|
| 26020-Package_Requirements.docx — package heading 38 | Governing EPC-side package-requirement clauses for the HP flare stack | location TBD (binary source; not locally rendered) |
| W242510-PRC-REP-000003-001 Plant Shutdown and Blowdown Philosophy | Detailed blowdown sequencing | external; not locally accessible (location TBD) |
| API 521 / API 537 / API 560-family (typical for flare relief and equipment) | Industry standards typically governing HP flare systems | TBD — not explicitly cited in accessible source slices (ASSUMPTION: likely applicable) |

## Verification

| Req ID | Verification Approach |
|---|---|
| R-085-01-01 to R-085-01-04 | Document review against PACKAGE_REGISTER row 58 and SCOPE_LEDGER rows 88-91 |
| R-085-01-05, R-085-01-06 | Cross-check of SoW interface narrative against DBM source slices (lines ~497-499, ~354; 4-25 DBM lines ~585, 704, 813, 838-842) |
| R-085-01-07 | Document review confirming staggered-blowdown statement and reference to W242510-PRC-REP-000003-001 |
| R-085-01-08, R-085-01-09 | Document review against PACKAGE_REGISTER row 58 (Applicable Interface Types; Responsibility Model) |
| R-085-01-10 | Anticipated-artifact checklist against DELIVERABLE_REGISTER row 312 |
| R-085-01-11 | Objective-map confirmation by human reviewer (PACKAGE_HEURISTIC association is ASSUMPTION) |
| R-085-01-12 | Datasheet cross-check (Datasheet.md attribute table) |
| R-085-01-13, R-085-01-14 | Pending source access — verification recorded as `TBD` |

## Documentation

The deliverable shall produce, at minimum, the four anticipated artifacts:

1. Package scope of work (this Specification, together with Guidance and Procedure).
2. Tagged equipment and package identity list (captured in Datasheet.md — Identification and Attributes).
3. Package function and integration narrative (Guidance.md and Specification §Scope).
4. Responsibility assignment record (Specification R-085-01-09 and Guidance §Considerations).

Source: DELIVERABLE_REGISTER row 312 (Anticipated Artifacts).
