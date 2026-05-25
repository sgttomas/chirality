# Specification: DEL-024-01 Scope of Work

## Scope

This deliverable defines the EPC Integrator scope of work for PKG-024, the workbook-defined Electrical package named `MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD`, WBS 01, tracking number `26020-01-30-015`.

The Scope of Work shall cover:

- package identity, source basis, and workbook row traceability;
- package function and whole-facility integration narrative as a medium-voltage variable frequency drive package;
- tagged equipment where source-supported (driven motor tag and process service are presently TBD);
- responsibility split between Package Vendor (engineering/design/equipment/vendor documentation) and EPC Integrator (facility integration and interfaces);
- applicable package interfaces: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports;
- scope boundaries, assumptions, TBDs, and open items required for downstream package datasheet, construction work package, vendor package production, vendor document turnover, and EPC acceptance.

The Scope of Work shall not assign package engineering, package design, vendor documentation production, or physical equipment package supply to the EPC Integrator. Gate 7 assigns those responsibilities to the Package Vendor and assigns facility-level integration/interface responsibilities to the EPC Integrator.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| SOW-024-01 | The Scope of Work shall identify PKG-024, workbook ID 24, workbook row 26, WBS 01, tracking number `26020-01-30-015`, package name `MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD`, and discipline Electrical. | Compare against workbook Packages row 26 (via Gate 7 registers) and Gate 7 `PACKAGE_REGISTER.csv` row PKG-024. |
| SOW-024-02 | The Scope of Work shall state that the package is vendor-owned for package engineering, package design, vendor documentation, and physical equipment package supply. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-024. |
| SOW-024-03 | The Scope of Work shall state that the EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-024. |
| SOW-024-04 | The Scope of Work shall include the six source-supported interface categories: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | Compare against workbook Packages row 26 and Gate 7 `INTERFACE_REGISTER.csv` PKG-024 rows. |
| SOW-024-05 | The Scope of Work shall describe the package function in source-supported terms: a medium-voltage variable frequency drive package nominally rated 2,000 hp, 4,160 V, 3-phase, 60 Hz with 4,160 V output, intended for facility integration consistent with the DBM 4.16 kV MCC and medium-voltage VFD context. Detailed topology (input rectifier configuration, output filter, bypass, harmonic mitigation, cooling, enclosure) shall be left TBD. | Compare against workbook Packages row 26, Gate 7 `PACKAGE_REGISTER.csv` row PKG-024, and `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2957, 2961, 2973. |
| SOW-024-06 | The Scope of Work shall mark unsupported package-specific design values as `TBD`, including driven motor tag and service, manufacturer, topology, harmonic mitigation, cooling, enclosure, environmental rating, weights, dimensions, support loads, control architecture, communication protocols, and protection settings. | Review against accessible sources and confirm no unsupported values are introduced. |
| SOW-024-07 | The Scope of Work shall preserve anticipated artifacts: package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. | Compare against `_CONTEXT.md` Anticipated Artifacts and Gate 7 `ARTIFACT_REGISTER.csv` DEL-024-01 rows. |
| SOW-024-08 | The Scope of Work shall identify no declared critical upstream or downstream dependencies unless `_DEPENDENCIES.md` is later updated. | Compare against `_DEPENDENCIES.md` declared lists. |
| SOW-024-09 | The Scope of Work shall record the objective associations OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 as accepted context per the Gate 7 objective-to-deliverable mapping. | Compare against Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv` rows for DEL-024-01_scope-of-work. |

## Standards

| Standard / basis | Status |
|---|---|
| Gate 7 PROJECT_DECOMP snapshot | Authoritative accepted decomposition basis for package, deliverable, objective, artifact, scope, and interface registers. |
| Workbook Packages row 26 | Authoritative source row for package identity and interface flags (carried via Gate 7 registers; no local source slice copied during PREPARATION). |
| DBM-Deepcut facility electrical basis | Accessible facility-level source for medium-voltage MCC/VFD context. |
| Package-specific MV VFD vendor standards (e.g., NEMA ICS 7, IEEE 519, IEC 61800, manufacturer specifications) | TBD; not present in accessible source slices for this deliverable. Listed here as `location TBD` for downstream sourcing, not as a derived requirement. |

## Verification

- Verify identity fields against Gate 7 `PACKAGE_REGISTER.csv` row PKG-024 and workbook Packages row 26.
- Verify deliverable role against Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis and DEC-001.
- Verify responsibility split against Gate 7 `PACKAGE_REGISTER.csv` row PKG-024.
- Verify interface list against workbook row 26 and Gate 7 `INTERFACE_REGISTER.csv` rows for PKG-024.
- Verify facility-level MV VFD context against DBM-Deepcut Motor Control and Motor Specifications and Electrical Buildings sections; do not overstate as package-specific design data.
- Confirm each package-specific technical value is source-supported or marked `TBD`.
- Confirm objective associations match Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv` DEL-024-01 rows.
- Confirm cross-document terminology uses the source-spelled package name `MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD`.

## Documentation

The Scope of Work package shall produce or preserve:

- package scope of work;
- tagged equipment and package identity list, with driven motor tag and other unavailable tag fields marked `TBD`;
- package function and integration narrative anchored to the facility 4.16 kV/MV VFD basis;
- responsibility assignment record;
- interface basis for Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports;
- list of source limitations, TBDs, assumptions, and human ruling items.
