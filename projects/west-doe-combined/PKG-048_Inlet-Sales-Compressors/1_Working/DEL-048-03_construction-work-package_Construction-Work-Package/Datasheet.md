# Datasheet: DEL-048-03 — Construction Work Package

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-048-03_construction-work-package |
| Name | Construction Work Package |
| ParentPackageID | PKG-048 |
| Package Name | Inlet / Sales Compressors |
| Discipline | Mechanical (multi-discipline construction execution) |
| Deliverable Type | EPC Construction Work Package |
| Responsible Party | EPC Integrator |
| Facility | 03-25 West Doe Compressor Station and Liquids Hub |
| Location | LSD 03-25-80-15 W6M, north of Dawson Creek, British Columbia (Source: 3-25_Comp_and_Liquids_DBM.md SEC-02) |
| Site Elevation | 673 m AMSL (Source: 3-25_Comp_and_Liquids_DBM.md SEC-02) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Subject scope items | SOW-0115, SOW-0116, SOW-0117, SOW-0118 | _CONTEXT.md; DELIVERABLE_REGISTER.csv row 356 |
| Supports objectives (ASSUMPTION — package-heuristic) | OBJ-001, OBJ-003..OBJ-010 | _CONTEXT.md; OBJECTIVE_DELIVERABLE_MAP.csv |
| Subject equipment scope (compression) | Two electric-drive, two-stage reciprocating inlet compressor packages, 5,200 hp each, 40 MMSCFD each, no installed spare | 3-25_Comp_and_Liquids_DBM.md SEC-05 |
| Subject equipment scope (dehydration) | One TEG dehydration package downstream of inlet compression | 3-25_Comp_and_Liquids_DBM.md SEC-05 |
| Modularization basis | Packages modularized for shop assembly; disassembled into three pieces for transportation and field installation in self-framing buildings | 3-25_Comp_and_Liquids_DBM.md SEC-05 |
| Compressor electric driver | 4,000 V, 3-phase, 60 Hz, 3,878 kW / 5,200 hp; starting VFD per SCA-001 VE #34 | 3-25_Comp_and_Liquids_DBM.md SEC-05 |
| Construction scope summary | Construction management, grading, piling, foundations, roads, field buildings, offloading and setting of modules, mechanical hookups, installation of shipped-loose instruments and valves, pipe supports, ISBL/OSBL interconnecting piping, home-run cabling, terminations, area lighting, fencing, security, control room and maintenance systems, potable and septic utilities, non-process building heating and fuel storage, demolition/removal where required for tie-ins | 3-25_Comp_and_Liquids_DBM.md SEC-03 Construction Scope Summary |
| Geotechnical basis | Final geotechnical report governs foundation, pile, settlement, frost, site prep, and structural support criteria; DBM values are design placeholders until report acceptance | 3-25_Comp_and_Liquids_DBM.md SEC-03 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service classification | Sour-gas service (raw-gas design H2S 0.3 mol%; license 2.0 mol%) | 3-25_Comp_and_Liquids_DBM.md SEC-03 |
| Compressor discharge pressure | 800 psig fixed (SCA-002 supersession) | 3-25_Comp_and_Liquids_DBM.md SEC-05 |
| First-stage suction / discharge MAWP | 653 psig MAWP | 3-25_Comp_and_Liquids_DBM.md SEC-05 |
| Second-stage discharge MAWP | 1,350 psig MAWP | 3-25_Comp_and_Liquids_DBM.md SEC-05 |
| Sour-gas export destination | 04-25 Deep Cut Gas Plant inlet gathering system | 3-25_Comp_and_Liquids_DBM.md SEC-04 |
| Electrical interconnect basis | Home-run cabling and terminations; VFD-started motors | 3-25_Comp_and_Liquids_DBM.md SEC-03, SEC-05 |
| Climate / wind / snow / seismic | TBD (location TBD in available source slices) | location TBD |

## Construction (Anticipated Artifacts)

| Artifact | Description | Source |
|---|---|---|
| Construction Work Package (CWP) | Master document bundling drawings, specs, procedures, ITPs, materials, schedule, and safety for the PKG-048 scope | _CONTEXT.md anticipated artifacts |
| Installation and Tie-in Workface Plan | Workface-level sequencing of module setting, mechanical hookups, ISBL/OSBL tie-ins, electrical home runs, and instrument hookups | _CONTEXT.md anticipated artifacts |
| Construction Interface and Turnover Checklist | Interface register and turnover/system completion checklist for handover to commissioning | _CONTEXT.md anticipated artifacts |

## References

- _CONTEXT.md
- _REFERENCES.md
- DELIVERABLE_REGISTER.csv (GATE-07 snapshot) row 356
- _Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (SEC-03 Construction Scope Summary; SEC-04 Inlet, Separation, Export; SEC-05 Inlet Compression and Sour-Gas Dehydration)
- 26020-Package_Requirements.docx package heading 3 (binary; location TBD — not parsed in this pass)
