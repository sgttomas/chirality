# Specification: DEL-013-01 Scope of Work

## Scope

This deliverable defines the EPC Integrator scope of work for PKG-013, the workbook-defined Electrical package named `100A DC UNINTERUPTIBLE POWER SUPPLY`, WBS 02, tracking number `26020-02-30-004`.

The Scope of Work shall cover:

- package identity, source basis, and workbook row traceability;
- package function and whole-facility integration narrative;
- tagged equipment where source-supported;
- responsibility split between Package Vendor and EPC Integrator;
- applicable package interfaces: Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports;
- scope boundaries, assumptions, TBDs, and open items required for downstream package datasheet, construction work package, vendor package production, vendor document turnover, and EPC acceptance.

The Scope of Work shall not assign package engineering, package design, vendor documentation production, or physical equipment package supply to the EPC Integrator. Gate 7 assigns those responsibilities to the Package Vendor and assigns facility-level integration/interface responsibilities to the EPC Integrator.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| SOW-013-01 | The Scope of Work shall identify PKG-013, workbook ID 13, workbook row 15, WBS 02, tracking number `26020-02-30-004`, package name `100A DC UNINTERUPTIBLE POWER SUPPLY`, and discipline Electrical. | Compare against workbook Packages row 15 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-013. |
| SOW-013-02 | The Scope of Work shall state that the package is vendor-owned for package engineering, package design, vendor documentation, and physical equipment package supply. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-013. |
| SOW-013-03 | The Scope of Work shall state that the EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-013. |
| SOW-013-04 | The Scope of Work shall include the four source-supported interface categories: Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports. | Compare against workbook Packages row 15 and Gate 7 `INTERFACE_REGISTER.csv` PKG-013 rows. |
| SOW-013-05 | The Scope of Work shall identify UPS service context as 120 VAC / 125 VDC where facility-level electrical basis is discussed, without converting that context into package-specific design values. | Compare against DBM Comp and Liquids electrical power distribution table, lines 734-736. |
| SOW-013-06 | The Scope of Work shall mark unsupported package-specific design values as `TBD`, including UPS capacity confirmation, battery autonomy, battery type, charger configuration, DC distribution, enclosure, environmental rating, weights, dimensions, and support loads. | Review against accessible sources and confirm no unsupported values are introduced. |
| SOW-013-07 | The Scope of Work shall preserve anticipated artifacts: package scope of work, tagged equipment and package identity list, package function and integration narrative, and responsibility assignment record. | Compare against `_CONTEXT.md` Anticipated Artifacts. |
| SOW-013-08 | The Scope of Work shall identify no declared critical upstream or downstream dependencies unless `_DEPENDENCIES.md` is later updated. | Compare against `_DEPENDENCIES.md` declared lists. |

## Standards

| Standard / basis | Status |
|---|---|
| Gate 7 PROJECT_DECOMP snapshot | Authoritative accepted decomposition basis for package, deliverable, objective, artifact, scope, and interface registers. |
| Workbook Packages row 15 | Authoritative source row for package identity and interface flags. |
| DBM Comp and Liquids electrical basis | Accessible facility-level source for UPS service context. |
| Package-specific electrical/UPS standards and vendor specifications | TBD; not present in accessible source slices for this deliverable. |

## Verification

- Verify identity fields against workbook Packages row 15 and Gate 7 `PACKAGE_REGISTER.csv`.
- Verify deliverable role against Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis and DEC-013.
- Verify responsibility split against Gate 7 `PACKAGE_REGISTER.csv` row PKG-013.
- Verify interface list against workbook row 15 and Gate 7 `INTERFACE_REGISTER.csv` rows for PKG-013.
- Verify UPS service context against DBM Comp and Liquids electrical power distribution table.
- Confirm each package-specific technical value is source-supported or marked `TBD`.
- Confirm cross-document terminology uses `100A DC UNINTERUPTIBLE POWER SUPPLY` as the source spelling while noting that the spelling appears source-derived.

## Documentation

The Scope of Work package shall produce or preserve:

- package scope of work;
- tagged equipment and package identity list, with tag values marked `TBD` when unavailable;
- package function and integration narrative;
- responsibility assignment record;
- interface basis for Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports;
- list of source limitations, TBDs, assumptions, and human ruling items.
