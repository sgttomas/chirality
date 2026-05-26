# Datasheet — Construction Work Package (DEL-095-03)

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-095-03_construction-work-package |
| Name | Construction Work Package |
| ParentPackageID | PKG-095 |
| PackageName | Tanks, Slop (API 650) |
| Workbook Row | 91 |
| Discipline | Mechanical |
| Type | EPC Construction Work Package |
| ResponsibleParty | EPC Integrator |
| Decomposition Basis | PROJECT_DECOMP GATE-07_Final_Published_2026-05-24 |
| Primary Source Slices (accessible) | DELIVERABLE_REGISTER.csv row DEL-095-03; PACKAGE_REGISTER.csv row PKG-095; SCOPE_LEDGER.csv rows SOW-0213, SOW-0214, SOW-0215, SOW-0216; INTERFACE_REGISTER.csv rows for PKG-095 |
| Primary Source Slices (deferred) | 26020-Package_Requirements.docx package heading 47 (binary; text slice not accessible to this run — location TBD) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Major Equipment Tag (Slop Storage Tank) | TK-9130-2 (likely) | SCOPE_LEDGER.csv SOW-0215 ("likely TK-9130-2") |
| Service Description | Slop storage for off-spec condensate or contaminated hydrocarbon liquids requiring segregation from on-spec condensate product | SCOPE_LEDGER.csv SOW-0214; PACKAGE_REGISTER.csv PKG-095 narrative |
| Tank Standard | API 650 (modified atmospheric) | SCOPE_LEDGER.csv SOW-0215; package name |
| Tank Count | One (1) | SCOPE_LEDGER.csv SOW-0214/SOW-0215 |
| Major Equipment Set | API 650 atmospheric slop storage tank; tank appurtenances; connections to drain/recycle/truck-out; standard tank instrumentation | SCOPE_LEDGER.csv SOW-0215 |
| WBS | 03 | PACKAGE_REGISTER.csv PKG-095 |
| Package-Equipment Tag (companion register) | 26020-03-PT-19-004 — Tanks, Slop | PACKAGE_REGISTER.csv PKG-095 |
| Module / Assembly Mode | TBD — vendor package design basis not yet established (API 650 tanks are typically field-erected, not modular) | ASSUMPTION (field erection is standard for API 650 atmospheric tanks; not explicitly stated in accessible source slices) |
| Vendor / EPC Split | Package Vendor owns engineering, design, vendor documentation, and physical equipment; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration | PACKAGE_REGISTER.csv PKG-095 Responsibility narrative |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service Class | Off-spec / contaminated hydrocarbon liquid (slop) | SCOPE_LEDGER.csv SOW-0214, SOW-0216 |
| Expected Slop Sources | Off-spec condensate; tank drains; KO drum pump-out; VRU/scrubber liquids; treating-unit drains; other contaminated hydrocarbon liquids | SCOPE_LEDGER.csv SOW-0216 |
| Storage Pressure | Atmospheric (API 650 modified) | SCOPE_LEDGER.csv SOW-0215 |
| Tank Design Basis (volume, dimensions, materials, lining, blanketing) | TBD — final source list, disposition path, and tank design basis require process confirmation | SCOPE_LEDGER.csv SOW-0216 |
| Spill Containment / Drainage | Within scope of interface coordination (Drain / Containment; Grading / Site Drainage / Spill Containment) | INTERFACE_REGISTER.csv PKG-095 |
| Electrical Area Classification | TBD — not stated in accessible source slices | TBD |

## Construction

| Construction Item | Value | Source |
|---|---|---|
| Assembly Mode | Field-erected API 650 tank (vendor-built foundation-down or shop-prefabricated shell rings, site-erected) | ASSUMPTION (standard API 650 construction practice; not explicit in accessible source slices) |
| Pre-Set Civil/Foundation Scope | Foundation (ringwall and/or pad) provided by a civil/earthworks package; tank-specific anchorage and underpad provisions per vendor design | ASSUMPTION (standard EPC split; specific civil package linkage location TBD) |
| Tie-In Points (process) | Inlet line(s) from slop sources (off-spec condensate, tank drains, KO drum pump-out, VRU/scrubber liquids, treating-unit drains); outlet/recycle line; truck-out connection | SCOPE_LEDGER.csv SOW-0215, SOW-0216 (slop source list); INTERFACE_REGISTER.csv (Process Piping) |
| Tie-In Points (relief / vent) | Atmospheric vent and/or pressure-vacuum relief to flare/vent system per interface | INTERFACE_REGISTER.csv (Relief / Flare / Vent) |
| Tie-In Points (drain / containment) | Tank drain to slop/contained drain system; secondary containment drain routing | INTERFACE_REGISTER.csv (Drain / Containment) |
| Tie-In Points (utility / electrical) | Grounding/bonding; area/exterior lighting; cathodic protection; I&C / control cabling for tank instrumentation | INTERFACE_REGISTER.csv PKG-095 |
| Standard Tank Instrumentation | Level, temperature, pressure (as applicable for atmospheric tank), high-level / overfill protection (set per process design — TBD) | SCOPE_LEDGER.csv SOW-0215 (standard tank instrumentation) |
| Inspection Hold Points | TBD — to be set by EPC inspection plan (bottom weld vacuum-box test, shell weld NDE, hydrotest, settlement survey, internal lining cure if applicable, instrument loop checks) | ASSUMPTION (standard API 650 inspection set; itemized list TBD) |
| Turnover Documents | Vendor data book (API 650 tank); foundation acceptance record; weld and NDE records; hydrotest record; settlement survey; cathodic protection commissioning; instrument calibration; punch list; as-builts | ASSUMPTION (standard EPC turnover set; itemized list TBD) |

## References

- _CONTEXT.md (this deliverable)
- _REFERENCES.md (this deliverable)
- _DEPENDENCIES.md (this deliverable)
- PROJECT_DECOMP GATE-07_Final_Published_2026-05-24 DELIVERABLE_REGISTER.csv (row DEL-095-03)
- PROJECT_DECOMP GATE-07_Final_Published_2026-05-24 PACKAGE_REGISTER.csv (row PKG-095)
- PROJECT_DECOMP GATE-07_Final_Published_2026-05-24 SCOPE_LEDGER.csv (rows SOW-0213, SOW-0214, SOW-0215, SOW-0216)
- PROJECT_DECOMP GATE-07_Final_Published_2026-05-24 INTERFACE_REGISTER.csv (PKG-095 rows: Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports)
- 26020-Package_Requirements.docx package heading 47 — location TBD (binary source; text slice not accessible to this run)
- Workbook Packages row 91 — location TBD (binary spreadsheet; not parsed in this run)
