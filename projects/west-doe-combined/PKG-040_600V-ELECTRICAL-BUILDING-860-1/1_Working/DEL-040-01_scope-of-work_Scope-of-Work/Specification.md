# Specification: DEL-040-01 Scope of Work

## Scope

This deliverable defines the EPC Integrator scope of work for PKG-040, the workbook-defined Electrical package named `600V ELECTRICAL BUILDING (860-1)`, WBS 01, tracking number `26020-01-30-031`. The package is identified in the DBM facility electrical-building list as the 860-1 General Area / Tank Farm electrical building.

The Scope of Work shall cover:

- package identity, source basis, and workbook row traceability;
- package function and whole-facility integration narrative for a prefabricated modular 600 V electrical building located in a general purpose area, serving the general area / tank farm;
- tagged equipment where source-supported (building tag 860-1; interior equipment lineup TBD);
- responsibility split between Package Vendor and EPC Integrator;
- the twelve applicable package interfaces flagged in workbook row 42: Utility Piping, Drain / Containment, Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Building HVAC / Services, Fire & Gas / Safety Systems, Maintenance Access, Grading / Site Drainage / Spill Containment, and Structural / Foundations / Supports;
- scope boundaries, assumptions, TBDs, and open items required for downstream package datasheet, construction work package, vendor package production, vendor document turnover, and EPC acceptance.

The Scope of Work shall not assign package engineering, package design, vendor documentation production, or physical equipment package supply to the EPC Integrator. Gate 7 assigns those responsibilities to the Package Vendor and assigns facility-level integration and interface responsibilities to the EPC Integrator.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| SOW-040-01 | The Scope of Work shall identify PKG-040, workbook ID 40, workbook row 42, WBS 01, tracking number `26020-01-30-031`, package name `600V ELECTRICAL BUILDING (860-1)`, and discipline Electrical. | Compare against workbook Packages row 42 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-040. |
| SOW-040-02 | The Scope of Work shall state that the package is vendor-owned for package engineering, package design, vendor documentation, and physical equipment package supply. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-040. |
| SOW-040-03 | The Scope of Work shall state that the EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-040. |
| SOW-040-04 | The Scope of Work shall include the twelve source-supported interface categories listed in `_CONTEXT.md` Conditions and Gate 7 `INTERFACE_REGISTER.csv` for PKG-040. | Compare against workbook Packages row 42 and Gate 7 `INTERFACE_REGISTER.csv` PKG-040 rows. |
| SOW-040-05 | The Scope of Work shall describe the building as a prefabricated modular electrical building located in a general purpose area, with bottom-entry cabling, n+1 HVAC, and 600 V grounding basis as facility context, without converting facility-level descriptions into package-specific design values. | Compare against DBM Electrical Buildings (lines 2971-2981), MCCs and 600 V services (lines 2937, 2959), Grounding and Bonding (lines 2985-2991). |
| SOW-040-06 | The Scope of Work shall mark unsupported package-specific values as `TBD`, including interior equipment lineup, ratings, quantities, dimensions, weights, foundation loads, HVAC unit size and count, generator/transfer-switch coordination, and any vendor-specific construction details. | Review against accessible sources and confirm no unsupported values are introduced. |
| SOW-040-07 | The Scope of Work shall preserve the four anticipated artifacts: package scope of work, tagged equipment and package identity list, package function and integration narrative, and responsibility assignment record. | Compare against `_CONTEXT.md` Anticipated Artifacts and Gate 7 `ARTIFACT_REGISTER.csv` rows for DEL-040-01_scope-of-work. |
| SOW-040-08 | The Scope of Work shall record supported objectives OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, and OBJ-010 as the package-grouped objective mapping (ASSUMPTION: package-heuristic mapping). | Compare against Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv` rows for DEL-040-01_scope-of-work. |
| SOW-040-09 | The Scope of Work shall identify no declared critical upstream or downstream dependencies unless `_DEPENDENCIES.md` is later updated. | Compare against `_DEPENDENCIES.md` declared lists. |
| SOW-040-10 | The Scope of Work shall surface the building-name discrepancy between the package name `600V ELECTRICAL BUILDING (860-1)` and the DBM electrical-building list entry `860-1 600V General Area / Tank Farm Electrical Building` as a human-ruling item rather than silently normalizing either name. | Compare against DBM line 2816; record in the Guidance Conflict Table. |
| SOW-040-11 | The Scope of Work shall surface the general-area / tank-farm service-area characterization as descriptive context only, with specific tank-farm loads served by 860-1 marked `TBD` until detailed engineering or vendor data resolves them. | Compare against DBM line 2816 and Gate 7 PKG-040 row; record loads as `TBD`. |

## Standards

| Standard / basis | Status |
|---|---|
| Gate 7 PROJECT_DECOMP snapshot | Authoritative accepted decomposition basis for package, deliverable, objective, artifact, scope, and interface registers. |
| Workbook Packages row 42 | Authoritative source row for package identity and interface flags (binary workbook; text extraction not present locally — content cited only where mirrored by Gate 7 registers). |
| DBM Deepcut electrical design basis (Section 12 / lines 2860-3090) | Accessible facility-level source for low-voltage service, electrical-building basis, MCC basis, grounding, standby power, and building heaters. |
| Canadian Electrical Code (CEC) | Referenced by DBM for grounding sizing, conduit, and area-classification compliance; specific clause applicability is TBD until detailed design. |
| NEMA VE2 | Referenced by DBM for cable-tray support where a support detail is not included; package-specific applicability TBD. |
| Package-specific electrical-building vendor specifications | TBD; not present in accessible source slices for this deliverable. |

## Verification

- Verify identity fields against workbook Packages row 42 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-040.
- Verify deliverable role against Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis and the Notes column of `DELIVERABLE_REGISTER.csv` row DEL-040-01_scope-of-work.
- Verify responsibility split against Gate 7 `PACKAGE_REGISTER.csv` row PKG-040.
- Verify the twelve interfaces against workbook row 42 and Gate 7 `INTERFACE_REGISTER.csv` PKG-040 rows.
- Verify electrical-building, MCC, grounding, standby power, and building-heater statements against DBM Deepcut Section 12 source slices cited in the Datasheet.
- Confirm each package-specific technical value is either source-supported or marked `TBD`.
- Confirm preserved spellings: package name `600V ELECTRICAL BUILDING (860-1)` (accepted source form) and the DBM building name variant (line 2816) are both surfaced rather than reconciled.
- Confirm undeclared cross-package relationships are not treated as blockers.

## Documentation

The Scope of Work package shall produce or preserve:

- package scope of work (ART-95D8796E51);
- tagged equipment and package identity list, with interior equipment tags marked `TBD` where unavailable (ART-22111E8269);
- package function and whole-facility integration narrative (ART-EBFDF9B165);
- package responsibility assignment record (ART-1C1CC3907A);
- interface basis for all twelve interface categories flagged for PKG-040;
- list of source limitations, TBDs, assumptions, and human-ruling items, including the building-name discrepancy, the package-specific interior-lineup source gap, the tank-farm-load TBD, and the DBM-identified TBDs that affect this building (standby generator integration, RDC design, secondary cable-tray routing).
