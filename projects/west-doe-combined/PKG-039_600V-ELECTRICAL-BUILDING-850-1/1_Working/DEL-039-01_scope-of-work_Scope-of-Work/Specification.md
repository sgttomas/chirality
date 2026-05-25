# Specification: DEL-039-01 Scope of Work

## Scope

This deliverable defines the EPC Integrator scope of work for PKG-039, the workbook-defined Electrical package named `600V ELECTRICAL BUILDING (850-1)`, WBS 01, tracking number `26020-01-30-030`. The package is identified in the DBM facility electrical-building list as the 850-1 Inlet / Sales Compressor electrical building.

The Scope of Work shall cover:

- package identity, source basis, and workbook row traceability;
- package function and whole-facility integration narrative for a prefabricated modular 600 V electrical building located in a general purpose area;
- tagged equipment where source-supported (building tag 850-1; interior equipment lineup TBD);
- responsibility split between Package Vendor and EPC Integrator;
- the twelve applicable package interfaces flagged in workbook row 41: Utility Piping, Drain / Containment, Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Building HVAC / Services, Fire & Gas / Safety Systems, Maintenance Access, Grading / Site Drainage / Spill Containment, and Structural / Foundations / Supports;
- scope boundaries, assumptions, TBDs, and open items required for downstream package datasheet, construction work package, vendor package production, vendor document turnover, and EPC acceptance.

The Scope of Work shall not assign package engineering, package design, vendor documentation production, or physical equipment package supply to the EPC Integrator. Gate 7 assigns those responsibilities to the Package Vendor and assigns facility-level integration and interface responsibilities to the EPC Integrator.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| SOW-039-01 | The Scope of Work shall identify PKG-039, workbook ID 39, workbook row 41, WBS 01, tracking number `26020-01-30-030`, package name `600V ELECTRICAL BUILDING (850-1)`, and discipline Electrical. | Compare against workbook Packages row 41 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-039. |
| SOW-039-02 | The Scope of Work shall state that the package is vendor-owned for package engineering, package design, vendor documentation, and physical equipment package supply. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-039. |
| SOW-039-03 | The Scope of Work shall state that the EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-039. |
| SOW-039-04 | The Scope of Work shall include the twelve source-supported interface categories listed in `_CONTEXT.md` Conditions and Gate 7 `INTERFACE_REGISTER.csv` for PKG-039. | Compare against workbook Packages row 41 and Gate 7 `INTERFACE_REGISTER.csv` PKG-039 rows. |
| SOW-039-05 | The Scope of Work shall describe the building as a prefabricated modular electrical building located in a general purpose area, with bottom-entry cabling, n+1 HVAC, and 600 V grounding basis as facility context, without converting facility-level descriptions into package-specific design values. | Compare against DBM Electrical Buildings (lines 2971-2981), MCCs and 600 V services (lines 2937, 2959), Grounding and Bonding (lines 2985-2991). |
| SOW-039-06 | The Scope of Work shall mark unsupported package-specific values as `TBD`, including interior equipment lineup, ratings, quantities, dimensions, weights, foundation loads, HVAC unit size and count, generator/transfer-switch coordination, and any vendor-specific construction details. | Review against accessible sources and confirm no unsupported values are introduced. |
| SOW-039-07 | The Scope of Work shall preserve the four anticipated artifacts: package scope of work, tagged equipment and package identity list, package function and integration narrative, and responsibility assignment record. | Compare against `_CONTEXT.md` Anticipated Artifacts and Gate 7 `ARTIFACT_REGISTER.csv` rows for DEL-039-01_scope-of-work. |
| SOW-039-08 | The Scope of Work shall record supported objectives OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, and OBJ-010 as the package-grouped objective mapping (ASSUMPTION: package-heuristic mapping). | Compare against Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv` rows for DEL-039-01_scope-of-work. |
| SOW-039-09 | The Scope of Work shall identify no declared critical upstream or downstream dependencies unless `_DEPENDENCIES.md` is later updated. | Compare against `_DEPENDENCIES.md` declared lists. |
| SOW-039-10 | The Scope of Work shall surface the building-name discrepancy between the package name `600V ELECTRICAL BUILDING (850-1)` and the DBM equivalents (`850-1 600V Inlet / Sales Compressor Electrical Building` and `600 V Sales/Overheads Compressor Electrical Building`) as a human-ruling item rather than silently normalizing either name. | Compare against DBM lines 2815 and 2924; record in the Guidance Conflict Table. |

## Standards

| Standard / basis | Status |
|---|---|
| Gate 7 PROJECT_DECOMP snapshot | Authoritative accepted decomposition basis for package, deliverable, objective, artifact, scope, and interface registers. |
| Workbook Packages row 41 | Authoritative source row for package identity and interface flags. |
| DBM Deepcut electrical design basis (Section 12 / lines 2860-3090) | Accessible facility-level source for low-voltage service, electrical-building basis, MCC basis, grounding, standby power, and building heaters. |
| Canadian Electrical Code (CEC) | Referenced by DBM for grounding sizing, conduit, and area-classification compliance; specific clause applicability is TBD until detailed design. |
| NEMA VE2 | Referenced by DBM for cable-tray support where a support detail is not included; package-specific applicability TBD. |
| Package-specific electrical-building vendor specifications | TBD; not present in accessible source slices for this deliverable. |

## Verification

- Verify identity fields against workbook Packages row 41 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-039.
- Verify deliverable role against Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis and the Notes column of `DELIVERABLE_REGISTER.csv` row DEL-039-01_scope-of-work.
- Verify responsibility split against Gate 7 `PACKAGE_REGISTER.csv` row PKG-039.
- Verify the twelve interfaces against workbook row 41 and Gate 7 `INTERFACE_REGISTER.csv` PKG-039 rows.
- Verify electrical-building, MCC, grounding, standby power, and building-heater statements against DBM Deepcut Section 12 source slices cited in the Datasheet.
- Confirm each package-specific technical value is either source-supported or marked `TBD`.
- Confirm preserved spellings: package name `600V ELECTRICAL BUILDING (850-1)` (accepted source form) and the DBM building name variants (line 2815 vs line 2924) are both surfaced rather than reconciled.
- Confirm undeclared cross-package relationships are not treated as blockers.

## Documentation

The Scope of Work package shall produce or preserve:

- package scope of work (ART-700A2309BC);
- tagged equipment and package identity list, with interior equipment tags marked `TBD` where unavailable (ART-F6773941ED);
- package function and whole-facility integration narrative (ART-63C9C36771);
- package responsibility assignment record (ART-6F58720A97);
- interface basis for all twelve interface categories flagged for PKG-039;
- list of source limitations, TBDs, assumptions, and human-ruling items, including the building-name discrepancy and the DBM-identified TBDs that affect this building (standby generator integration, RDC design, secondary cable-tray routing).
