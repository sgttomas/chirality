# Datasheet — DEL-090-02 Package Datasheet (Vapour Recovery Unit 3-25)

> Document type: EPC Package Datasheet (descriptive).
> Authority: EPC Integrator. Source-grounded in the 3-25 Compressor Station and Liquids Hub Design Basis Memo (DBM). Decomposition routes; sources determine content. Non-trivial values cite the source slice; unknowns are marked `TBD`.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-090-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable Name | Package Datasheet | `_CONTEXT.md` |
| Parent Package | `PKG-090` Vapour Recovery Unit 3-25 | `_CONTEXT.md` |
| Workbook Package Row | 100 | `_CONTEXT.md` Source Reference |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Facility | 03-25 West Doe Compressor Station and Liquids Hub, LSD 03-25-80-15 W6M, north of Dawson Creek, BC | `3-25_Comp_and_Liquids_DBM.md` SEC-01, SEC-02 |
| Package Function | Tank-vapour recovery for the 03-25 Liquids Hub (condensate and produced-water tank systems and selected process vents) with discharge routed under SCA-002 to the 04-25 SOC suction | `3-25_Comp_and_Liquids_DBM.md` SEC-01, SEC-06 "Vapour Recovery" |

## Attributes — Package Equipment

| Attribute | Value | Source |
|---|---|---|
| Compressor count | 2 packages | `3-25_Comp_and_Liquids_DBM.md` SEC-01, SEC-06 "Vapour Recovery" |
| Configuration | 2 x 100 percent | `3-25_Comp_and_Liquids_DBM.md` SEC-06 "Vapour Recovery" |
| Driver | Electric drive | `3-25_Comp_and_Liquids_DBM.md` SEC-01, SEC-06 |
| Driver rating (each) | 200 hp | `3-25_Comp_and_Liquids_DBM.md` SEC-01, SEC-06 |
| Installed spare | None additional beyond 2 x 100 percent arrangement | ASSUMPTION (DBM states two-package 2 x 100 percent arrangement; no separate spare called out) |
| Suction sources | Condensate tank vapours, produced-water tank vapours, selected process vents per active process basis | `3-25_Comp_and_Liquids_DBM.md` SEC-06 "Vapour Recovery" |
| Normal discharge destination | 04-25 SOC suction (under SCA-002) | `3-25_Comp_and_Liquids_DBM.md` SEC-01, SEC-06 |
| Recycle | Second-stage discharge to first-stage suction, sized for 100 percent flow at minimum driver speed and lowest discharge pressure | `3-25_Comp_and_Liquids_DBM.md` SEC-06 "Vapour Recovery" |
| Make-up / blanket gas | LP fuel-gas regulator maintains minimum suction pressure at maximum turndown | `3-25_Comp_and_Liquids_DBM.md` SEC-06 "Vapour Recovery" |
| LP flare bypass | V-ball valve on VRU suction header, operated by VRU suction pressure | `3-25_Comp_and_Liquids_DBM.md` SEC-06 "Vapour Recovery" |
| Suction-header drainage | Free-drain or slope toward flare KO interface, per detailed design | `3-25_Comp_and_Liquids_DBM.md` SEC-06 "Vapour Recovery" |

## Attributes — Process Conditions

| Attribute | Value | Source |
|---|---|---|
| Service | Sour hydrocarbon vapours from tank systems and selected vents | `3-25_Comp_and_Liquids_DBM.md` SEC-01, SEC-06 |
| Tag prefix | TBD (no tag list extracted from local source slice) | source location TBD |
| Design suction pressure | TBD (not stated in accessible DBM slice) | source location TBD |
| Design suction temperature | TBD | source location TBD |
| Design discharge pressure | TBD (must align with 04-25 SOC suction interface) | source location TBD |
| Capacity (each package) | TBD | source location TBD |
| Inlet composition | TBD (governed by tank vapour and vent composition envelope) | source location TBD |
| Acid-gas content (H2S, mercaptans) | Sour service; methyl mercaptan toxicity context applies to vent and analyzer planning | `3-25_Comp_and_Liquids_DBM.md` SEC-07 "Fuel-Gas Sulphur and Purge Hazard Basis" |
| Liquid carryover handling | Suction header free-drain / slope to flare KO; KO interface defined by detailed design | `3-25_Comp_and_Liquids_DBM.md` SEC-06 |
| Recycle valve fail action | TBC (compressor recycle valves expected fail-open; VRU-specific final fail action not isolated in source slice) | `3-25_Comp_and_Liquids_DBM.md` SEC-05 (inlet compression context); VRU-specific value TBD |

## Construction and Interfaces

| Item | Value | Source |
|---|---|---|
| Modularization | TBD (DBM modularizes inlet compression into shop-assembled packages; VRU-specific modularization not stated in accessible slice) | source location TBD |
| Suction header / KO interface | VRU suction header connects to LP flare KO interface for liquid drainage | `3-25_Comp_and_Liquids_DBM.md` SEC-06 |
| LP flare relief | LP flare receives TEG regen, VRU, and compressor seal-pot services; LP KO drum V-3900-2 and pump P-3900-2 to slop | `3-25_Comp_and_Liquids_DBM.md` SEC-07 "Flare and Blowdown" |
| Electrical supply | Facility electrical power (shared cross-facility utility) | `3-25_Comp_and_Liquids_DBM.md` SEC-07 "Utility Integration Basis" |
| Instrument air supply | From 04-25 (no local 03-25 instrument-air compressors under SCA-006) | `3-25_Comp_and_Liquids_DBM.md` SEC-07 "Instrument Air" |
| Fuel-gas (blanket / make-up) | LP fuel-gas system | `3-25_Comp_and_Liquids_DBM.md` SEC-06 "Vapour Recovery", SEC-07 "Fuel Gas" |
| Discharge tie-in | 04-25 SOC suction (under SCA-002) | `3-25_Comp_and_Liquids_DBM.md` SEC-01 |
| Local 03-25 SOC | Removed; superseded by SCA-002 | `3-25_Comp_and_Liquids_DBM.md` SEC-01 "Removed scope items" |

## Scope Items and Objectives Covered

| Code | Source |
|---|---|
| SOW-0249, SOW-0250, SOW-0251, SOW-0252 | `_CONTEXT.md`; ARTIFACT/SOW register row 100 |
| OBJ-002 through OBJ-010 | `_CONTEXT.md` (ASSUMPTION — package-heuristic association per `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`) |

## Anticipated Datasheet Artifacts (this deliverable)

- Package technical datasheet
- Vendor engineering handoff basis
- Package interface requirements matrix
- Source-supported equipment and design criteria

## References

- `3-25_Comp_and_Liquids_DBM.md` (Comp_and_Liquids DBM; sections SEC-01 Executive Summary, SEC-02 Site Basis, SEC-06 Liquids Hub Process / Vapour Recovery, SEC-07 Utilities)
- `_CONTEXT.md` (this deliverable)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (decomposition row for DEL-090-02)
- 26020-Package_Requirements.docx package heading 43 (referenced by decomposition; source slice not locally accessible as text — `location TBD`)
- 26020-Packages_Interfaces_4_export.xlsx (referenced by decomposition; not locally accessible as text — `location TBD`)
