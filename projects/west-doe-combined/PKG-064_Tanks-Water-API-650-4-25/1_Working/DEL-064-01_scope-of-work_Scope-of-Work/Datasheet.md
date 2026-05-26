# Datasheet — DEL-064-01 Scope of Work (Tanks, Water (API 650) 4-25)

> Descriptive datasheet for the EPC Integrator Scope of Work covering PKG-064 Tanks, Water (API 650) 4-25 (Process Water Storage).
> Pass 1/Pass 2 draft; values are source-grounded where the locally accessible DBM supports them. Unsupported values are `TBD`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-064-01_scope-of-work` | `_CONTEXT.md` |
| Deliverable Name | Scope of Work | `_CONTEXT.md` |
| Parent Package | `PKG-064` Tanks, Water (API 650) 4-25 | `_CONTEXT.md` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Scope of Work | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Facility | West Doe Deepcut Expansion (04-25 Deep Cut Gas Plant) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §SEC-01 |
| Decomposition Basis | GATE-07_Final_Published_2026-05-24 PROJECT_DECOMP snapshot | `_REFERENCES.md` |
| Covers Scope Items | SOW-0233, SOW-0234, SOW-0235, SOW-0236 | `_CONTEXT.md` |
| Supports Objectives | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (ASSUMPTION: package-grouping heuristic) | `_CONTEXT.md`; SKILL.md Step 1 §3 |

## Attributes (Package Identity)

| Attribute | Value | Source |
|---|---|---|
| Package function | Process water storage at the 04-25 Deep Cut Gas Plant tank farm; serves as the source of make-up water to the caustic NGL contactor water-wash system during upset operation and supports amine module 530 process-water storage and transfer service | DBM-Deepcut §SEC-07 (NGL caustic treating water wash, line "Make-up water, if required during upset operation, is supplied from the process water storage tank"); §SEC-05 amine regeneration module/building line ("process-water storage and transfer") |
| Configuration | Two (2) atmospheric API 650 water storage tanks, designated PROCESS WATER STORAGE TANK (x2, 4-25) | DBM-Deepcut §SEC-16 Workbook Packages row 102 ("Tanks, Water (API 650) 2 / PROCESS WATER STORAGE TANK (x2, 4-25) / 4-25 (Deepcut) / 2") |
| Tagged Equipment List | TK-5317-1, TK-5318-1 | DBM-Deepcut §SEC-16 deliverable row 102 ("TK-5317-1, TK-5318-1") |
| Associated transfer pumps | PROCESS WATER TRANSFER PUMPS (x2), tags P-5317-1, P-5318-1, located in Tank Farm Pump Building 2 | DBM-Deepcut §SEC-16 deliverable rows 83 and Workbook Packages row "Tank Farm Pump Building 2" (NOTE: transfer pumps are formally part of PKG (Tank Farm Pump Building 2), not PKG-064; recorded here as interface context) |
| Code basis | API 650 (atmospheric welded steel storage tanks) per package title and Workbook Packages classification | DBM-Deepcut §SEC-16 Workbook Packages row 102 ("Tanks, Water (API 650) 2"); package name |
| Service / fluid | Process water (utility-quality water used as caustic-treating make-up water and amine-module process water) | DBM-Deepcut §SEC-07 line 1556; §SEC-05 Module 530 description |
| Tank location | 04-25 tank farm storage area (alongside other API 650 product/utility tanks: condensate, produced water, fresh caustic, spent caustic, DSO) | DBM-Deepcut §SEC-16 Workbook Packages rows 87, 88, 90, 91, 99, 102 |
| Module / building scope | Tanks are atmospheric outdoor tank-farm storage; no building enclosure indicated for the tanks themselves (transfer pumps are inside Tank Farm Pump Building 2) | DBM-Deepcut §SEC-16 deliverable row 83 (pump building scope); tank scope not stated explicitly → ASSUMPTION based on standard API 650 outdoor tank-farm practice |

## Conditions (Design Basis)

| Parameter | Value | Source |
|---|---|---|
| Tank count | 2 | DBM-Deepcut §SEC-16 row 102 |
| Tank capacity | TBD — not stated for process water tanks in the accessible source slice | `location TBD` (analogous produced-water tank capacities of 2 × 2,000 bbl are cited in §SEC-03 storage table; process-water capacity is not given) |
| Operating temperature | TBD; tanks shall be insulated to prevent winter freezing | DBM-Deepcut §SEC-10 ("water tanks shall be insulated to prevent winter freezing") |
| Operating pressure | Atmospheric (API 650 basis) | DBM-Deepcut §SEC-16 package class ("Tanks, Water (API 650) 2"); API 650 standard scope |
| Design specific gravity | TBD — not stated for process water tanks in accessible source slice (produced water tanks use 1.25 TBC; process water service typically uses 1.00 — ASSUMPTION not entered as a value) | `location TBD` |
| Insulation | External insulation required for winter freeze prevention | DBM-Deepcut §SEC-10 |
| Heat tracing / heating | TBD — not specified for process water tanks; produced water tanks are externally insulated and heated per §SEC-03 | `location TBD` |
| Internal coating | TBD — not specified for process water tanks in accessible source slice | `location TBD` |
| PVRV / EPRV | TBD — not specified for process water tanks (produced water tanks specify at least one PVRV per tank per §SEC-03) | `location TBD` |
| Spacing to adjacent atmospheric tanks | 2.35 m (7.72 ft) minimum per NFPA 30 Table 22.4.2.1 | DBM-Deepcut §SEC-02 Atmospheric Tank and General Plant Spacing table |
| Spacing to public road | 80 m (262.5 ft) minimum per OGAOM Sec. 9.6.15, DPR 48 | DBM-Deepcut §SEC-02 Atmospheric Tank and General Plant Spacing table |
| Spacing to flare (atmospheric water tanks) | Not separately listed for process water tanks; the 25 m (82 ft) figure is given for atmospheric produced-water tanks per OGAOM Sec. 9.6.15 — applicability to process water tanks is ASSUMPTION pending discipline review | DBM-Deepcut §SEC-02 spacing table; ASSUMPTION |

## Construction (Package Constituents)

| Item | Description | Source |
|---|---|---|
| Tank 1 | TK-5317-1 — Process Water Storage Tank | DBM-Deepcut §SEC-16 row 102 |
| Tank 2 | TK-5318-1 — Process Water Storage Tank | DBM-Deepcut §SEC-16 row 102 |
| Tank standard | API 650 (atmospheric welded steel storage tank) | package class per DBM-Deepcut §SEC-16 row 102 |
| Insulation system | External insulation for winter freeze prevention | DBM-Deepcut §SEC-10 |
| Vent / overpressure protection | TBD (PVRV/EPRV not specified for process water tanks in accessible source slice) | `location TBD` |
| Internal coating | TBD | `location TBD` |
| Foundations and ringwall | TBD — civil scope referenced through §SEC-11 (Civil, Buildings, and Miscellaneous Facilities) but specific process-water-tank foundation details are not in the accessible slice | `location TBD` |
| Containment / berms | Containment scope is governed by PKG-006 Containment Berms (per project package register) — interface only | GATE-07 PACKAGE_REGISTER (PKG-006 entry); not in DBM-Deepcut source slice as a specific PKG-064 attribute |
| Tag plates / nameplates | TBD | `location TBD` |
| Instrumentation (level, temperature) | TBD — not enumerated for process water tanks in accessible source slice | `location TBD` |
| Inlet / outlet nozzles | TBD — sizes, ratings, locations not in accessible source slice | `location TBD` |
| Associated transfer pumps (interface) | PROCESS WATER TRANSFER PUMPS (P-5317-1, P-5318-1) — physically in Tank Farm Pump Building 2; not part of PKG-064 scope but is the immediate downstream interface | DBM-Deepcut §SEC-16 deliverable row 83; Workbook Packages "Tank Farm Pump Building 2" |

## Integration Narrative (Whole-Facility)

The two process water storage tanks (TK-5317-1, TK-5318-1) are part of the 04-25 Deep Cut Gas Plant tank-farm storage area and provide utility-quality water inventory to the plant. The DBM identifies the process water storage tank as the make-up water source to the caustic NGL contactor water-wash system during upset operation, with final routing to be confirmed during detailed engineering (DBM-Deepcut §SEC-07 NGL mercaptan treating). The DBM also lists "process-water storage and transfer" as part of the Module 530 amine regeneration module/building scope (DBM-Deepcut §SEC-05 Module 530 description). Downstream from the tanks, the PROCESS WATER TRANSFER PUMPS (P-5317-1, P-5318-1) located in Tank Farm Pump Building 2 are the dedicated transfer service to consumers; those pumps are not part of PKG-064 scope. The tanks are sited within the tank-farm storage area subject to the atmospheric-tank and tank-to-fired-equipment spacing rules in DBM-Deepcut §SEC-02. Winter freeze protection is required (DBM-Deepcut §SEC-10). Containment provisions are governed under the project's containment-berms package and are an interface to PKG-064 rather than internal scope. Source: DBM-Deepcut §SEC-02, §SEC-05 (Module 530), §SEC-07 (NGL caustic treating water wash), §SEC-10, §SEC-16 (package and deliverable register rows 83, 102).

## Responsibility Assignment (Summary)

| Function | Party | Source |
|---|---|---|
| EPC Scope of Work authorship and integration | EPC Integrator | `_CONTEXT.md` ResponsibleParty |
| Vendor package engineering, design, fabrication/supply of physical equipment (the API 650 tanks) | Package Vendor (with EPC Integrator integration review) | GATE-07 DELIVERABLE_REGISTER row DEL-064-04 |
| Vendor documentation register, submittals, turnover records | Package Vendor (with EPC Integrator review) | GATE-07 DELIVERABLE_REGISTER row DEL-064-05 |
| Vendor package review and acceptance, integration handoff | EPC Integrator (lead) | GATE-07 DELIVERABLE_REGISTER row DEL-064-06 |
| Construction, installation, tie-in, and turnover plan | EPC Integrator | GATE-07 DELIVERABLE_REGISTER row DEL-064-03 |
| Package Datasheet (technical handoff basis) | EPC Integrator | GATE-07 DELIVERABLE_REGISTER row DEL-064-02 |

## References

- `_REFERENCES.md`
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §SEC-01, §SEC-02, §SEC-05, §SEC-07, §SEC-10, §SEC-16 (Workbook Packages row 102; deliverable rows 83, 102)
- GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv (rows DEL-064-01..06)
- GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv (PKG-064; PKG-006 for containment interface)
- Workbook Packages row 96; `26020-Package_Requirements.docx` package heading 19 — NOT locally accessible as extracted markdown (`location TBD`)
