# Datasheet: DEL-071-01 — Scope of Work (PKG-071 Fuel Gas Skid 4-25)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-071-01_scope-of-work | `_CONTEXT.md` |
| Deliverable Name | Scope of Work | `_CONTEXT.md` |
| Parent Package ID | PKG-071 | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Workbook ID | 71 | PACKAGE_REGISTER.csv |
| CoA Tracking Number | 26020-01-23-001 | PACKAGE_REGISTER.csv (location TBD in source workbook) |
| Package Name | Fuel Gas Skid 4-25 | PACKAGE_REGISTER.csv; Workbook Packages row 61 |
| WBS | 01 | PACKAGE_REGISTER.csv |
| Discipline | Mechanical | PACKAGE_REGISTER.csv; `_CONTEXT.md` |
| Type | EPC Scope of Work | DELIVERABLE_REGISTER.csv |
| Responsible Party | EPC Integrator | DELIVERABLE_REGISTER.csv |
| Package Vendor Responsibility | Package engineering, package design, vendor documentation, physical equipment package | PACKAGE_REGISTER.csv; Workbook Packages row 61 |
| EPC Integrator Responsibility | Integration into the functional process facility — interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration | PACKAGE_REGISTER.csv; Workbook Packages row 61 |

## Attributes (Package Function and Identity)

| Attribute | Value | Source |
|---|---|---|
| Package Function | Serve the low-pressure fuel gas system for the West Doe Deep Cut Facility | SCOPE_LEDGER SOW-0100; 26020-Package_Requirements.docx package heading 25 — Basic scope |
| Basic Scope | 1 skid-mounted Low Pressure Fuel Gas Package comprising 1 low-pressure fuel gas heater and 1 low-pressure fuel gas scrubber | SCOPE_LEDGER SOW-0100; 26020-Package_Requirements.docx package heading 25 |
| Discipline | Mechanical | PACKAGE_REGISTER.csv |
| WBS Bucket | 01 (04-25 Deepcut facility) | PACKAGE_REGISTER.csv; OBJ-001 |

## Conditions (Operating and Design)

| Parameter | Value | Source |
|---|---|---|
| Design Flow Required | > 8.4 MMSCFD (237.5 e3m3/day) | SCOPE_LEDGER SOW-0102; 26020-Package_Requirements.docx package heading 25 — Scope notes and open items |
| Final Flow | TBD | SCOPE_LEDGER SOW-0102 (explicit TBD in source) |
| Gas Outlet Temperature | Heated to 95 F (35 C) | SCOPE_LEDGER SOW-0102 |
| Operating Pressure | 150 psig | SCOPE_LEDGER SOW-0102 |
| Ambient Temperature | -19 C to 22.2 C | SCOPE_LEDGER SOW-0102 |
| Design Pressure | 150 psig | SCOPE_LEDGER SOW-0102 |
| Design Temperature | -40 C to 35 C | SCOPE_LEDGER SOW-0102 |
| MAWP | TBD | SCOPE_LEDGER SOW-0102 (explicit TBD in source) |
| Heater Driver | SCR heater control panels, 600 V, located in electrical building | SCOPE_LEDGER SOW-0102; SOW-0101 |
| Heating Value | TBD for 4-25 package (1040 BTU/SCF cited only for the sister PKG-084 3-25 row; not asserted here) | SCOPE_LEDGER SOW-0098/SOW-0102 comparison; ASSUMPTION not propagated |

## Construction (Major Included Equipment)

| Item | Description | Source |
|---|---|---|
| Skid | A skid for the system to be mounted on | SCOPE_LEDGER SOW-0101; 26020-Package_Requirements.docx package heading 25 — Major included equipment |
| Fuel Gas Heater | Capacity TBD; heater controlled by SCR (600 V); shall include skin temperature thermocouple override control on heater | SCOPE_LEDGER SOW-0101 |
| Fuel Gas Scrubber | Sized using a k-factor of 0.35 (imperial) maximum plus de-ration factor for operating pressure; vendor to design | SCOPE_LEDGER SOW-0101 |

## Tagged Equipment and Package Identity List

- Package: Fuel Gas Skid 4-25 (Workbook ID 71; CoA tracking 26020-01-23-001; WBS 01).
- Equipment tags: not assigned in source for this package (TBD; to be issued during package datasheet and vendor documentation cycles).

## Boundaries (By Others)

The following are explicitly excluded from this package scope per source:

- Shipping packages to site (SCOPE_LEDGER SOW-0102 — By others).
- Installation (SOW-0102 — By others).
- Tie-in piping (SOW-0102 — By others).
- Electrical tie-in (SOW-0102 — By others).

## Applicable Interface Types

| Interface Type | Source |
|---|---|
| Process Piping | PACKAGE_REGISTER.csv (PKG-071 applicable interfaces) |
| Utility Piping | PACKAGE_REGISTER.csv |
| Relief / Flare / Vent | PACKAGE_REGISTER.csv |
| Drain / Containment | PACKAGE_REGISTER.csv |
| Electrical Power | PACKAGE_REGISTER.csv |
| Grounding / Bonding | PACKAGE_REGISTER.csv |
| Area / Exterior Lighting | PACKAGE_REGISTER.csv |
| I&C / Control Cabling | PACKAGE_REGISTER.csv |
| Building HVAC / Services | PACKAGE_REGISTER.csv |
| Fire & Gas / Safety Systems | PACKAGE_REGISTER.csv |
| Maintenance Access | PACKAGE_REGISTER.csv |
| Structural / Foundations / Supports | PACKAGE_REGISTER.csv |

## Responsibility Assignment Record

| Responsibility | Owner | Source |
|---|---|---|
| Package engineering | Package Vendor | PACKAGE_REGISTER.csv; ART-451A242BFC |
| Package design | Package Vendor | PACKAGE_REGISTER.csv |
| Vendor documentation | Package Vendor | PACKAGE_REGISTER.csv |
| Physical equipment package supply | Package Vendor | PACKAGE_REGISTER.csv |
| Facility integration (interfaces, tie-ins) | EPC Integrator | PACKAGE_REGISTER.csv |
| Constructability | EPC Integrator | PACKAGE_REGISTER.csv |
| Procurement/construction coordination | EPC Integrator | PACKAGE_REGISTER.csv |
| Facility-level integration | EPC Integrator | PACKAGE_REGISTER.csv |

## Covered Scope Items

- SOW-0099 — Carry PKG-071 as a distinct flat project package; vendor/EPC responsibility split.
- SOW-0100 — Basic scope and process function.
- SOW-0101 — Major included equipment.
- SOW-0102 — Scope notes, capacity/design throughput, operating/design conditions, by-others list.

## References

- `_REFERENCES.md`
- PACKAGE_REGISTER.csv (PKG-071 row)
- DELIVERABLE_REGISTER.csv (DEL-071-01 row)
- SCOPE_LEDGER.csv (SOW-0099, SOW-0100, SOW-0101, SOW-0102)
- ARTIFACT_REGISTER.csv (ART-AC01900208, ART-31BC19483F, ART-5369838D71, ART-451A242BFC, ART-CD58F7CD21)
- Workbook Packages row 61 (source workbook 26020-Packages_Interfaces_4_export.xlsx; binary — location TBD at clause level)
- 26020-Package_Requirements.docx, package heading 25 (binary — location TBD at clause level)
