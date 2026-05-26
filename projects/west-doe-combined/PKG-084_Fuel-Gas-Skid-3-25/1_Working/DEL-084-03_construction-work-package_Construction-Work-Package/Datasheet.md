# Datasheet — Construction Work Package (DEL-084-03)

Pass: P1_P2 (initial draft + cross-reference sweep)

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-084-03_construction-work-package |
| Name | Construction Work Package |
| ParentPackageID | PKG-084 |
| PackageName | Fuel Gas Skid 3-25 |
| Discipline | Mechanical |
| Type | EPC Construction Work Package |
| ResponsibleParty | EPC Integrator |
| Decomposition Basis | GATE-07_Final_Published_2026-05-24 (PROJECT_DECOMP) |
| Covers Scope Items | SOW-0095, SOW-0096, SOW-0097, SOW-0098 |
| Supports Objectives | OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (ASSUMPTION: PACKAGE_HEURISTIC association) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Subject package | Fuel Gas Skid serving 03-25 facility | DELIVERABLE_REGISTER row 326 (PACKAGE row 60) |
| Fuel gas role | Provides LP fuel gas for stripping, blanketing, purge, dilution/enrichment, building heaters, and related utility users | 3-25_Comp_and_Liquids_DBM.md SEC "Fuel Gas" (line 456) |
| Primary fuel-gas source | Enbridge sales-gas pipeline via the 04-25 plant sales-gas splitter; Alliance as secondary source | 3-25_Comp_and_Liquids_DBM.md line 456 |
| Physical location of fuel-gas building | At or associated with 04-25; serves 03-25 compressor station, 03-25 liquids hub, and 04-25 gas plant | 3-25_Comp_and_Liquids_DBM.md line 452 |
| Listed users | TEG stripping, caustic treating overhead dilution, maintenance purge, drive gas, blanket gas, building heat | 3-25_Comp_and_Liquids_DBM.md lines 463, 546 |
| Skid configuration / package boundary | TBD (skid-edge isolation required per package philosophy) | 3-25_Comp_and_Liquids_DBM.md line 605 (general principle); skid-specific layout location TBD |

## Conditions

| Condition | Value | Source |
|---|---|---|
| LP fuel-gas normal total flow | 1.382 MMSCFD (39.13 e3m3/d) — current basis, TBC | 3-25_Comp_and_Liquids_DBM.md line 463 |
| LP fuel-gas design flow | > 1.5 MMSCFD (42.5 e3m3/d) — current basis, TBC | 3-25_Comp_and_Liquids_DBM.md line 463 |
| LP fuel-gas scrubber tag | V-3210-2 (downstream of heater, K=0.35, liquids to slop TK-9130-2) | 3-25_Comp_and_Liquids_DBM.md line 463 |
| Fuel-gas source pressures / MAWP | Table present in source but not transcribed at clause level; location TBD | 3-25_Comp_and_Liquids_DBM.md line 458 |
| Ambient design basis | -40 deg C winter operation referenced for site infrastructure | 3-25_Comp_and_Liquids_DBM.md line 696 |
| Emergency buyback fuel gas | Unresolved (W242510 says not required; Process_DBM_fixed includes it) — NEEDS_HUMAN_RULING | 3-25_Comp_and_Liquids_DBM.md line 465 |
| Sweet-gas purge / mercaptan hazard | Methyl mercaptan present; formal hazard review required before finalizing purge/analyzer maintenance | 3-25_Comp_and_Liquids_DBM.md line 469 |

## Construction

| Item | Value | Source |
|---|---|---|
| Construction scope (facility-level context) | Construction management, grading, piling, foundations, roads, field buildings, module offload and setting, mechanical hookups, shipped-loose instruments/valves, pipe supports, ISBL/OSBL interconnecting piping, home-run cabling, terminations, area lighting, fencing, security, control room and maintenance systems, potable/septic utilities, non-process building heating and fuel storage, tie-in demo as required | 3-25_Comp_and_Liquids_DBM.md line 75 |
| Modularization basis (facility precedent) | Process packages are modularized for shop assembly and disassembled for transport and field reassembly | 3-25_Comp_and_Liquids_DBM.md line 294 |
| Package boundary isolation | Isolation at skid edge required where needed for maintenance | 3-25_Comp_and_Liquids_DBM.md line 605 |
| Package deliverable expectations | Datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing, materials/coating basis, maintenance access, shipped-loose item lists, vendor document register | 3-25_Comp_and_Liquids_DBM.md line 617 |
| Foundation/geotechnical basis | Final geotechnical report governs; values treated as placeholders until accepted | 3-25_Comp_and_Liquids_DBM.md line 141 |
| Fuel-gas skid civil/structural details | TBD (location TBD) |
| Tie-in list (mechanical, electrical, controls, fire/gas, drains, HVAC, heat tracing) | TBD — 04-25 utility building interfaces noted at facility level | 3-25_Comp_and_Liquids_DBM.md line 619 |
| Turnover package definition / checklist content | TBD |
| Workface plan structure | TBD |
| Inspection and test plan (ITP) hooks | TBD |

## Anticipated Artifacts

- Construction work package (binder/scope basis)
- Installation and tie-in workface plan
- Construction interface and turnover checklist

## References

- 3-25_Comp_and_Liquids_DBM.md (accessible) — `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
- Trace_Appendix.md — `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/Trace_Appendix.md`
- 26020-Package_Requirements.docx, package heading 37 — NOT LOCALLY ACCESSIBLE AS TEXT (binary .docx); skid-specific requirements remain TBD until source slice is extracted
- DELIVERABLE_REGISTER.csv row 326 (GATE-07 snapshot)
