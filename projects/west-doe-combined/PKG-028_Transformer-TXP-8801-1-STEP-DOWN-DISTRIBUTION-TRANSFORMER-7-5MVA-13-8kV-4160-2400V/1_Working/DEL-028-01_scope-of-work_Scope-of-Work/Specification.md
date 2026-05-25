# Specification: DEL-028-01 Scope of Work

## Scope

This deliverable defines the EPC Integrator Scope of Work for PKG-028, the workbook-defined Electrical package named `Transformer TXP-8801-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 7.5MVA 13.8kV/4160/2400V`, WBS 01, tracking number `26020-01-30-019`.

The Scope of Work shall cover:

- package identity, source basis, and workbook row traceability;
- package function and whole-facility integration narrative consistent with the facility 13.8 kV distribution basis;
- tagged equipment where source-supported (equipment tag `TXP-8801-1` is exposed in the package name);
- responsibility split between Package Vendor and EPC Integrator;
- applicable package interfaces: Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports;
- scope boundaries, assumptions, TBDs, and open items required for the downstream package datasheet, construction work package, vendor package production, vendor document turnover, and EPC acceptance.

The Scope of Work shall not assign package engineering, package design, vendor documentation production, or physical equipment package supply to the EPC Integrator. Gate 7 assigns those responsibilities to the Package Vendor and assigns facility-level integration/interface responsibilities to the EPC Integrator.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| SOW-028-01 | The Scope of Work shall identify PKG-028, workbook ID 28, workbook row 30, WBS 01, tracking number `26020-01-30-019`, package name `Transformer TXP-8801-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 7.5MVA 13.8kV/4160/2400V`, and discipline Electrical. | Compare against workbook Packages row 30 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-028. |
| SOW-028-02 | The Scope of Work shall state that the package is vendor-owned for package engineering, package design, vendor documentation, and physical equipment package supply. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-028. |
| SOW-028-03 | The Scope of Work shall state that the EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-028. |
| SOW-028-04 | The Scope of Work shall include the seven source-supported interface categories: Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. | Compare against workbook Packages row 30 and Gate 7 `INTERFACE_REGISTER.csv` rows for PKG-028. |
| SOW-028-05 | The Scope of Work shall describe the facility electrical context (25 kV utility, 50 MVA utility transformer, 13.8 kV switchgear, radial step-down distribution) only as facility integration context, without converting that context into package-specific design values. | Compare against `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2917-2937. |
| SOW-028-06 | The Scope of Work shall mark unsupported package-specific design values as `TBD`, including vendor nameplate confirmation, impedance, vector group, taps, cooling class, insulation class, BIL, fluid type, accessories, weights, dimensions, support loads, and whether 4160 V / 2400 V is a dual-secondary, tertiary-winding, or sectionalized arrangement. | Review against accessible sources and confirm no unsupported values are introduced. |
| SOW-028-07 | The Scope of Work shall preserve anticipated artifacts: package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. | Compare against `_CONTEXT.md` Anticipated Artifacts. |
| SOW-028-08 | The Scope of Work shall preserve equipment tag `TXP-8801-1` exactly as carried in accepted source materials. | Compare against workbook Packages row 30 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-028. |
| SOW-028-09 | The Scope of Work shall identify no declared critical upstream or downstream dependencies unless `_DEPENDENCIES.md` is later updated. | Compare against `_DEPENDENCIES.md` declared lists. |
| SOW-028-10 | The Scope of Work shall name the seven supported objectives (OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010) as the objective context for the package deliverables. | Compare against Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv` rows for DEL-028-01. |

## Standards

| Standard / basis | Status |
|---|---|
| Gate 7 PROJECT_DECOMP snapshot | Authoritative accepted decomposition basis for package, deliverable, objective, artifact, scope, and interface registers. |
| Workbook Packages row 30 | Authoritative source row for package identity and interface flags. |
| DBM Deepcut Electrical sections (lines 2917-2991) | Accessible facility-level source for 13.8 kV distribution architecture, transformer foundation/spacing basis, and grounding basis. |
| CSA C22.1 (Canadian Electrical Code) | Referenced via DBM (transformer spacing, grounding sizing); location TBD for clause-level requirements; do not derive clause-level requirements without source access. |
| Package-specific transformer standards (e.g., CSA C88, IEEE C57, vendor specifications) | TBD; not present in accessible source slices for this deliverable. |

## Verification

- Verify identity fields against workbook Packages row 30 and Gate 7 `PACKAGE_REGISTER.csv`.
- Verify deliverable role against Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis.
- Verify responsibility split against Gate 7 `PACKAGE_REGISTER.csv` row PKG-028.
- Verify interface list against workbook row 30 and Gate 7 `INTERFACE_REGISTER.csv` rows for PKG-028.
- Verify facility electrical context against the DBM Deepcut Electrical section.
- Confirm each package-specific technical value is source-supported or marked `TBD`.
- Confirm equipment tag `TXP-8801-1` and full package name string are preserved exactly.
- Confirm objective associations match the Gate 7 objective-deliverable map.

## Documentation

The Scope of Work package shall produce or preserve:

- package scope of work;
- tagged equipment and package identity list, with tag values marked `TBD` when unavailable;
- package function and integration narrative;
- responsibility assignment record;
- interface basis for Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports;
- list of source limitations, TBDs, assumptions, and human ruling items.
