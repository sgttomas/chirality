# Datasheet — DEL-088-03 Construction Work Package

> Descriptive datasheet for the EPC Construction Work Package covering Package PKG-088, Caustic Treating (Condensate Mercaptan Removal). Substantive engineering attributes derive from the parent package datasheet (DEL-088-02) and the project DBM; this datasheet carries the construction-execution view.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-088-03_construction-work-package` | `_CONTEXT.md` |
| Deliverable Name | Construction Work Package | `_CONTEXT.md` |
| Parent Package | `PKG-088` — Caustic Treating (Condensate Mercaptan Removal) | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-088 |
| Workbook Row | 50 | `PACKAGE_REGISTER.csv` row PKG-088 |
| Discipline | Mechanical | `_CONTEXT.md` |
| Deliverable Type | EPC Construction Work Package | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Tag (Equipment Basis) | 26020-02-PT-27-001 — Caustic Treating (Condensate Mercaptan Removal) | `PACKAGE_REGISTER.csv` row PKG-088 |
| Source Basis | Workbook Packages row 50; 26020-Package_Requirements.docx package heading 41 | `_CONTEXT.md`; `_REFERENCES.md` |

## Attributes

| Attribute | Value | Source / Status |
|---|---|---|
| Package function | Non-regenerable caustic treating package for C5+ condensate mercaptan removal | `3-25_Comp_and_Liquids_DBM.md` "Condensate Mercaptan Treating" |
| Treating capacity (process basis) | 20,000 bbl/d C5+ | `3-25_Comp_and_Liquids_DBM.md` |
| Regeneration | Not included | `3-25_Comp_and_Liquids_DBM.md` |
| Construction execution role | EPC Integrator-led integration into the whole process facility | `PACKAGE_REGISTER.csv` row PKG-088 (Boundaries) |
| Vendor scope boundary | Package Vendor owns package engineering, design, vendor docs, and physical equipment package | `PACKAGE_REGISTER.csv` row PKG-088 |
| Applicable interface types | Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports | `PACKAGE_REGISTER.csv` row PKG-088 (Interface Types) |
| Aluminum prohibition in caustic building | Aluminum shall not be used in the caustic building | `3-25_Comp_and_Liquids_DBM.md` |
| Caustic drain header rating (minimum) | 300# ANSI | `3-25_Comp_and_Liquids_DBM.md` "Drains" |

## Conditions

| Condition | Value | Source / Status |
|---|---|---|
| Site climate basis | -40 deg C facility design basis | `3-25_Comp_and_Liquids_DBM.md` "Roads"; DBM general basis |
| Caustic solution basis | 50 wt% NaOH/H2O, SG 1.75 (TBC) | `3-25_Comp_and_Liquids_DBM.md` |
| Caustic drain maximum temperature | 121 deg C / 250 deg F (TBC) | `3-25_Comp_and_Liquids_DBM.md` |
| Caustic drain minimum tank temperature | 80 deg F | `3-25_Comp_and_Liquids_DBM.md` |
| Fresh/spent caustic tank type | Atmospheric 32 oz tanks with LP fuel-gas blanket, heating, insulation | `3-25_Comp_and_Liquids_DBM.md` |
| Instrument air supply | From 04-25; caustic oxidation demand 214 SCFM (TBC) | `3-25_Comp_and_Liquids_DBM.md` "Instrument Air" |
| Hazard context | Methyl mercaptan toxicity and odour hazards relevant to purge, analyzer, and operations practices | `3-25_Comp_and_Liquids_DBM.md` "Fuel-Gas Sulphur and Purge Hazard Basis" |
| Geotechnical basis | Treat DBM geotechnical values as design placeholders until final geotechnical report is accepted | `3-25_Comp_and_Liquids_DBM.md` |

## Construction (Execution View)

| Topic | Value | Source / Status |
|---|---|---|
| Civil scope (package-relevant subset) | Site grading, foundations, roads, buildings, electrical buildings, pipe racks, field interconnections, lighting, fencing, security | `3-25_Comp_and_Liquids_DBM.md` "Scope Inclusions" |
| Construction scope (facility level) | Construction management, grading, piling, foundations, roads, field buildings, offloading and setting of modules, mechanical hookups, installation of shipped-loose instruments and valves, pipe supports, ISBL/OSBL interconnecting piping, home-run cabling, terminations, area lighting, fencing, security systems, control room and maintenance systems, potable and septic utilities, non-process building heating and fuel storage, demolition/removal where required for project tie-ins | `3-25_Comp_and_Liquids_DBM.md` "Construction Scope Summary" |
| Modularization | Compressor packages are modularized for shop assembly and disassembled into three pieces for transportation and field installation; package-level modularization for PKG-088 is TBD until vendor package is selected | ASSUMPTION (analogy from `3-25_Comp_and_Liquids_DBM.md` line 294) |
| Local control wiring practice | Local control stations are hard-wired back to the motor starter circuit in the MCC by the field construction contractor | `3-25_Comp_and_Liquids_DBM.md` |
| Shipped-loose handling | Installation of shipped-loose instruments and valves included in construction scope | `3-25_Comp_and_Liquids_DBM.md` |
| Module offloading and setting | Included in construction scope | `3-25_Comp_and_Liquids_DBM.md` |
| Mechanical hookups | Included in construction scope | `3-25_Comp_and_Liquids_DBM.md` |
| Interconnecting piping | ISBL/OSBL interconnecting piping included in construction scope | `3-25_Comp_and_Liquids_DBM.md` |
| Tie-in coordination | Package buildings, self-framing enclosures, MCC interfaces, RIO interfaces, heat tracing, HVAC, fire/gas detection, and drain/vent tie-ins coordinated with civil, electrical, controls, and instrumentation sections of the DBM | `3-25_Comp_and_Liquids_DBM.md` line 619 |
| Turnover alignment | Final miscellaneous facilities list shall be aligned to plot plan, equipment list, and construction work package register before issue for construction | `3-25_Comp_and_Liquids_DBM.md` line 661 |
| Material handling notes — caustic | Caustic drain material selection requires detailed review due to embrittlement concerns | `3-25_Comp_and_Liquids_DBM.md` "Drains" |

## Covered Scope Items / Supported Objectives

- Covers Scope Items: `SOW-0055`, `SOW-0056`, `SOW-0057`, `SOW-0058` (from `_CONTEXT.md`).
- Supports Objectives (PACKAGE_HEURISTIC, ASSUMPTION): `OBJ-002`..`OBJ-010` (from `_CONTEXT.md`).

## Anticipated Artifacts

- Construction work package document set
- Installation and tie-in workface plan
- Construction interface and turnover checklist

(Source: `_CONTEXT.md` "Anticipated Artifacts".)

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local).
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row `DEL-088-03_construction-work-package`.
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` row `PKG-088`.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Scope Inclusions, Construction Scope Summary, Condensate Mercaptan Treating, Instrument Air, Drains, Mechanical Packages).
- `_Sources/26020-Package_Requirements.docx` package heading 41 — referenced; `location TBD` (binary not parsed in this run).
