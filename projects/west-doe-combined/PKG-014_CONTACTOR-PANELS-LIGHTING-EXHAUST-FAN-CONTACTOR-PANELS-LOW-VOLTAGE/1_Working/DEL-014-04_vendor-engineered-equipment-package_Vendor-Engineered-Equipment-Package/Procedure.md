# Procedure: DEL-014-04_vendor-engineered-equipment-package

## Purpose

Steps to produce the vendor engineered equipment package for `PKG-014` and to support its integration into the facility. Steps cover vendor engineering, design, fabrication/supply, and the EPC integration handoff.

## Prerequisites

- EPC Scope of Work (`DEL-014-01`) issued for vendor handoff.
- EPC Package Datasheet (`DEL-014-02`) issued for vendor handoff (load lists, control philosophy, interface requirements matrix).
- Accepted upstream decomposition snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`.
- DBM electrical design basis available: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- Declared upstream dependencies: none recorded in `_DEPENDENCIES.md`. (ASSUMPTION: practical upstream dependencies on `DEL-014-01` and `DEL-014-02` are inherent to the vendor production model; declare formally before acceptance.)
- EPC interface registry rows for `PKG-014` (`INTERFACE_REGISTER.csv`) reviewed.

## Steps

1. **Receive and acknowledge EPC handoff.** Vendor receives `DEL-014-01` (Scope of Work) and `DEL-014-02` (Package Datasheet); raises clarifications to EPC Integrator before engineering starts.
2. **Establish vendor design basis.** Vendor restates package function (low-voltage contactor panels for lighting and exhaust fan control), confirms applicable service voltages against DBM (600 V HRG, 120/208 V solid grounded), and records standards basis (`TBD` pending EPC confirmation).
3. **Develop electrical engineering deliverables.** Vendor produces single-line diagram(s), panel schedules, schematic diagrams, control logic descriptions, and bill of materials for each contactor panel covered by the package.
4. **Engineer interfaces.** Vendor addresses each PKG-014 interface (Electrical Power, Grounding/Bonding, Area/Exterior Lighting, I&C/Control Cabling, Communications/Network, Maintenance Access, Structural/Foundations/Supports) per `INTERFACE_REGISTER.csv`. Local control station coordination per DBM 600V MCC basis is included where exhaust fan circuits are MCC-fed.
5. **Coordinate enclosure and installation basis.** Vendor selects enclosure ratings to match area classification assigned by EPC documents; coordinates mounting basis (wall, floor stand, or skid) with the Structural/Foundations/Supports interface owner.
6. **Issue vendor package datasheet set.** Vendor issues the package design basis and datasheet set for EPC integration review.
7. **EPC integration review.** EPC Integrator reviews vendor package against `DEL-014-01`, `DEL-014-02`, and PKG-014 interfaces. Findings drive vendor rework where required. (This step provides input evidence to `DEL-014-06`.)
8. **Fabricate / procure / supply.** Vendor fabricates or procures contactor panels per the accepted engineering; performs factory acceptance testing.
9. **Ship and turn over.** Vendor delivers physical equipment package and supplies associated documentation to the vendor turnover deliverable (`DEL-014-05`).
10. **Support site integration and SAT.** Vendor supports EPC Integrator during installation, tie-in, site acceptance testing, and turnover (closeout evidence captured by `DEL-014-06`).

## Verification

- Vendor design basis traces to EPC Scope of Work and Package Datasheet.
- Single-line, schematics, and panel schedules reconcile to the EPC Package Datasheet load lists.
- Interface compliance demonstrated for each `PKG-014` interface row in `INTERFACE_REGISTER.csv`.
- Local control station provisions reconcile to DBM 600V MCC basis where applicable.
- Enclosure ratings reconcile to EPC-assigned area classification.
- Factory acceptance test report records pass/fail for each tested function.
- EPC integration review report (input to `DEL-014-06`) records acceptance status.

## Records

- Vendor engineering deliverable package (single-line, schematics, panel schedules, bill of materials, control logic narrative).
- Vendor package design basis and datasheet set.
- Interface compliance review record against `INTERFACE_REGISTER.csv` rows for `PKG-014`.
- Factory acceptance test report.
- EPC integration review record (input to `DEL-014-06`).
- Shipping and turnover records (consolidated under `DEL-014-05`).
- Site acceptance test record and turnover evidence (consolidated under `DEL-014-06`).
