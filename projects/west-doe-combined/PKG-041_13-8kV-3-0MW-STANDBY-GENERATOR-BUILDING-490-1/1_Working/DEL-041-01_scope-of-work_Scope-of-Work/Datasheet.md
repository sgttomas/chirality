# Datasheet — DEL-041-01 Scope of Work (PKG-041, 490-1 Standby Generator Building)

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-041-01_scope-of-work |
| Name | Scope of Work |
| ParentPackageID | PKG-041 |
| ParentWorkbookID | 41 |
| PackageName (as titled in workbook) | 13.8kV, 3.0MW STANDBY GENERATOR BUILDING (490-1) |
| Discipline | Electrical |
| Type | EPC Scope of Work |
| ResponsibleParty | EPC Integrator |
| WBS | 01 |
| Source basis | Workbook Packages row 43; DBM-Deepcut/4-25_Deepcut_DBM.md |
| Vendor package label (source) | 490-1 Emergency Generator Module (Shop, part of vendor package) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package title (workbook) | 13.8kV, 3.0MW STANDBY GENERATOR BUILDING (490-1) | PACKAGE_REGISTER.csv row 43 |
| Current standby-power basis | TOU-typical low-voltage standby generator set on LV MCC with transfer switch (480 V or 600 V class); centralized 13.8 kV emergency-generator concept eliminated for this facility scope | DBM Sec. "Emergency Power Generation Basis"; "Standby Power" section |
| Rated generator output voltage | Low voltage, 480 V or 600 V class (rating TBD; superseded prior 13.8 kV) | DBM "Emergency Power Generation Basis" table |
| Rated generator capacity | 3.0 MW (workbook title) — CONFLICT: not supported by current DBM basis; LV standby generator sizing is TBD (see Conflict Table CT-001) | PACKAGE_REGISTER.csv vs DBM "Standby Power" |
| Loads served | 04-25 and 03-25 critical loads via transfer switch at 600 V MCC level; heat medium, UPS, control systems, servers, freeze-protection electric heat tracing | DBM "Emergency Power Generation Basis"; "Standby Power" |
| Enclosure | Vendor-supplied weather-protective enclosure suitable for outdoor installation | DBM "Emergency Power Generation Basis" |
| Area classification | General Purpose | DBM "Emergency Power Generation Basis" table |
| Start system | Electric start, 24 Vdc battery system | DBM "Emergency Power Generation Basis" table |
| Fuel source | Natural gas (HP buyback) or diesel — selection TBD by MLE | DBM "Emergency Power Generation Basis" table |
| Natural gas pressure constraint | If natural gas selected, fuel gas regulated to less than 66 psig before generator enclosure | DBM "Emergency Power Generation Basis" table |
| Pneumatic start | Superseded; not required | DBM "Emergency Power Generation Basis" table |
| Overhead lift / access | 1 m access walkway maintained; overhead lift provisions to be confirmed by MLE | DBM "Emergency Power Generation Basis" |
| Tagged equipment (490-1 / Standby Generator row) | AC-4910-1, EGD-4950-1, EG-4950-1, ACM-4910-1 | DBM Tagged Equipment table, row 69 |
| Applicable interfaces | Utility Piping; Drain/Containment; Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Communications/Network; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports | PACKAGE_REGISTER.csv row 43 |
| Diesel storage | Required only if diesel selected; storage and day-tank sizing TBD | DBM "Emergency Power Generation Basis" table |
| Battery / charger sizing | TBD for selected package | DBM "Emergency Power Generation Basis" table |
| Operating speed | TBD; typically 1800 RPM for 60 Hz units (ASSUMPTION per DBM note) | DBM "Emergency Power Generation Basis" table |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Installation environment | Outdoor, weather-protective vendor enclosure | DBM "Emergency Power Generation Basis" |
| Module assembly mode | Shop-assembled vendor package (490-1 Emergency Generator Module) | DBM Module Assembly table |
| Service classification | Standby; supports outage and turnaround load | DBM "Standby Power" |
| Paralleling / load-shedding | TBD pending electrical studies and TOU standard confirmation | DBM "Standby Power"; Item table |
| Transfer mode (automatic vs manual) | TBD | DBM Item table "Standby generator integration" |
| Connection points and count | TBD | DBM Item table "Standby generator integration" |
| Transfer switch ratings | TBD | DBM Item table "Standby generator integration" |
| 13.8 kV tie-in | Eliminated (superseded for this facility scope) | DBM "Emergency Power Generation Basis" table |

## Construction

| Item | Value | Source |
|---|---|---|
| Module identity | 490-1 Emergency Generator Module | DBM Module Assembly table |
| Assembly location | Shop; part of vendor package | DBM Module Assembly table |
| Ownership split | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, and procurement/construction coordination. | PACKAGE_REGISTER.csv row 43 |
| Foundation / structural supports | EPC Integrator interface scope; details TBD | PACKAGE_REGISTER.csv (interface list) |
| Grounding/bonding, lighting, HVAC, F&G, communications, control cabling, drain/containment, site grading | EPC Integrator interface scope; details TBD | PACKAGE_REGISTER.csv (interface list) |

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` (row 43)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (row 228)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — sections "Emergency Power Generation Basis", "Standby Power", Module Assembly table, Tagged Equipment table row 69
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`
