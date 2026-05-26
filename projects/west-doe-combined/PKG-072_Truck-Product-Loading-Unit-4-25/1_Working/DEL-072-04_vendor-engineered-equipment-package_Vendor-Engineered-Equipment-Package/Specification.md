# Specification — DEL-072-04 Vendor Engineered Equipment Package

## Scope

### In Scope (Package Vendor responsibility)

- Package engineering, package design, fabrication/supply, and the physical equipment package for PKG-072 Truck Product Loading Unit 4-25 (PACKAGE_REGISTER.csv row 99; `_CONTEXT.md`).
- Skid-mounted Low Pressure Fuel Gas Package comprising one (1) low-pressure fuel gas heater and one (1) low-pressure fuel gas scrubber, mounted on one (1) skid (SCOPE_LEDGER.csv SOW-0246, SOW-0247).
- Vendor package design basis and datasheet set substantiating the vendor-engineered equipment (ARTIFACT_REGISTER.csv ART-071DC1CCEF).
- Package-side terminations for each applicable interface type listed in PACKAGE_REGISTER.csv row 99.

### Out of Scope (By Others)

Per SCOPE_LEDGER.csv SOW-0248: shipping packages to site; installation; tie-in piping; electrical tie-in; and similar facility-integration activities. These are EPC Integrator scope (PACKAGE_REGISTER.csv row 99 Notes) and are covered by sibling deliverables DEL-072-01 (Scope of Work), DEL-072-02 (Package Datasheet), DEL-072-03 (Construction Work Package), and DEL-072-06 (EPC Vendor Package Review and Acceptance).

## Requirements

### REQ-072-04-01 — Package Composition

The vendor SHALL deliver one (1) skid-mounted Low Pressure Fuel Gas Package comprising one (1) low-pressure fuel gas heater and one (1) low-pressure fuel gas scrubber.
Source: SCOPE_LEDGER.csv SOW-0246.

### REQ-072-04-02 — Heater Capacity

Fuel gas heater capacity: TBD (vendor to size against the design flow and outlet temperature; final capacity value not stated in source).
Source: SCOPE_LEDGER.csv SOW-0247 ("A fuel gas heater capacity TBD").

### REQ-072-04-03 — Heater Control

The heater SHALL be controlled by SCR (600 V) and SHALL include skin-temperature thermocouple override control on the heater.
Source: SCOPE_LEDGER.csv SOW-0247.

### REQ-072-04-04 — Scrubber Sizing

The fuel gas scrubber SHALL be sized using a k factor of 0.35 (imperial) maximum plus a de-ration factor for operating pressure. Vendor to design.
Source: SCOPE_LEDGER.csv SOW-0247.

### REQ-072-04-05 — Process Function and Service

The skid SHALL serve the low-pressure fuel gas system for the West Doe Deep Cut Facility.
Source: SCOPE_LEDGER.csv SOW-0246; PACKAGE_REGISTER.csv row 99.

### REQ-072-04-06 — Design Flow

Design Flow Required: > 8.4 MMSCFD (237.5 e3m3/day). Final Flow TBD.
Source: SCOPE_LEDGER.csv SOW-0248.

### REQ-072-04-07 — Outlet Temperature

Gas heated to 95 F (35 C).
Source: SCOPE_LEDGER.csv SOW-0248.

### REQ-072-04-08 — Operating Pressure

Operating Pressure: 150 psig.
Source: SCOPE_LEDGER.csv SOW-0248.

### REQ-072-04-09 — Ambient Conditions

Ambient Temperature Range: -19 C to 22.2 C.
Source: SCOPE_LEDGER.csv SOW-0248.

### REQ-072-04-10 — Design Conditions

Design Pressure: 150 psig. Design Temperature Range: -40 C to 35 C. MAWP: TBD.
Source: SCOPE_LEDGER.csv SOW-0248.

### REQ-072-04-11 — Heater Driver / Control Panel Location

SCR heater control panels are 600 V and are located in the electrical building.
Source: SCOPE_LEDGER.csv SOW-0248.

### REQ-072-04-12 — Vendor Package Design Basis and Datasheets

The vendor SHALL produce a package design basis and a datasheet set covering the engineered equipment, sufficient to substantiate the vendor-engineered package against the source basis and the EPC Package Datasheet (DEL-072-02).
Source: ARTIFACT_REGISTER.csv ART-071DC1CCEF; DELIVERABLE_REGISTER.csv (DEL-072-04 anticipated artifacts).

### REQ-072-04-13 — Interface Terminations (Package-Side)

The vendor SHALL provide package-side terminations for each applicable interface type listed in PACKAGE_REGISTER.csv row 99 (see Interface List below). Facility-side tie-ins are EPC Integrator scope.
Source: PACKAGE_REGISTER.csv row 99; INTERFACE_REGISTER.csv rows for PKG-072.

#### Interface List (package-side terminations expected)

Process Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports; Product Loading.

## Standards

- Standards governing low-pressure fuel gas package design (e.g., ASME pressure equipment codes; electrical area classification standards; SCR heater control standards): **location TBD** — not enumerated in the locally accessible decomposition registers; vendor to identify and apply per the source basis package requirements document (heading 26) and the project Design Basis Memoranda (`DBM-Deepcut/4-25_Deepcut_DBM.md`).
- ASSUMPTION: Specific code references are likely applicable but are not derivable from accessible source slices at this pass; concrete clauses remain TBD.

## Verification

| Requirement | Verification Approach |
|---|---|
| REQ-072-04-01 | Vendor design documentation review (count of skid/heater/scrubber); EPC Integrator review against DEL-072-02 Package Datasheet |
| REQ-072-04-02 | Vendor sizing calculation submittal; review against process duty; capacity value carried forward when established |
| REQ-072-04-03 | Vendor control schematic and panel datasheet review; verify SCR (600 V) control and skin-temperature override |
| REQ-072-04-04 | Vendor scrubber sizing calculation review (k = 0.35 imperial max with operating-pressure de-ration) |
| REQ-072-04-05 | Cross-check against PKG-072 process function statement; integration review by EPC Integrator |
| REQ-072-04-06 to -10 | Vendor datasheet review against SOW-0248 process and design conditions; flag TBD values for resolution |
| REQ-072-04-11 | Vendor electrical interface specification review; location confirmed against facility electrical building drawings |
| REQ-072-04-12 | Submittal completeness check against ARTIFACT_REGISTER ART-071DC1CCEF; sufficiency review against DEL-072-02 |
| REQ-072-04-13 | Interface-by-interface termination check against INTERFACE_REGISTER.csv rows for PKG-072 |

Final acceptance evidence is consolidated by sibling deliverable DEL-072-06 (EPC Vendor Package Review and Acceptance).

## Documentation

Expected vendor-produced documentation (anticipated artifacts per ARTIFACT_REGISTER.csv):

- Vendor engineered physical equipment package evidence (ART-0BA5F8C575).
- Vendor package design basis and datasheet set (ART-071DC1CCEF).
- Major included equipment evidence (ART-9A43B6880A) — skid, fuel gas heater, fuel gas scrubber, as defined by SOW-0247.

Document submittal, register, and turnover packaging are handled separately by sibling deliverable DEL-072-05 (Vendor Document Turnover Package).
