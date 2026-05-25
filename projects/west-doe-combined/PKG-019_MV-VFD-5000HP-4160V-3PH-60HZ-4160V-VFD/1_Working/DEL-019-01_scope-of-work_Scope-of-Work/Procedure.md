# Procedure: DEL-019-01 Scope of Work

## Purpose

Define the working procedure for producing and checking the EPC Integrator Scope of Work for PKG-019, `MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD`, using accepted Gate 7 truth and accessible source slices.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- Workbook Packages row 21 is available in `_Sources/26020-Packages_Interfaces_4_export.xlsx`.
- Facility-level DBM electrical basis is available in `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (electrical and 4160V MCC sections).
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md`.
- Package-specific vendor data: TBD; not present in accessible source slices.
- SCA-001 document text: TBD; referenced by the DBM but not directly accessible.

## Steps

1. Confirm deliverable identity from `_CONTEXT.md`: `DEL-019-01_scope-of-work`, Scope of Work, PKG-019, Electrical, EPC Integrator.
2. Confirm package identity from workbook Packages row 21: ID 19, WBS 02, tracking number `26020-02-30-009`, package name `MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD`, discipline Electrical.
3. Confirm Gate 7 package basis from `PACKAGE_REGISTER.csv` row PKG-019, including Package Vendor responsibility for package engineering/design/equipment/vendor documentation and EPC Integrator responsibility for facility integration/interfaces.
4. Confirm Scope of Work deliverable role from Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis and Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-019-01_scope-of-work.
5. Confirm source-supported interface categories from workbook row 21 and Gate 7 `PACKAGE_REGISTER.csv`: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports.
6. Use the DBM electrical sections only to state facility-level MV context: 13.8 kV to 4.16 kV / 12 MVA transformer feeding the 4160V MCC; 4160V MCC serving large 4000V motors including inlet compressors `KM-2150` and `KM-2250`; starting VFDs required per SCA-001 VE #34; capacitor banks removed from the synchronous bus on MCC-8200 where VFDs are present per SCA-001 VE #37; harmonic / reactive-power mitigation to be determined by detailed electrical studies.
7. Draft the SOW content so that EPC Integrator scope is limited to integration, interfaces, tie-ins, constructability, procurement/construction coordination, and acceptance support.
8. Mark missing package-specific information as `TBD`, including tagged equipment, drive count and duty, VFD topology, transformer/reactor configuration, harmonic filtering, enclosure, cooling, environmental rating, weights, dimensions, footprint, and support loads.
9. Carry the voltage/horsepower mismatch between the package title and the DBM motor basis as Conflict HR-019-01-01 and do not silently reconcile.
10. Carry the tagged-equipment allocation question as Conflict HR-019-01-02 and the SCA-001 access gap as Conflict HR-019-01-03.
11. Cross-check the SOW against the package datasheet, construction work package assumptions, vendor turnover expectations, and EPC acceptance needs before closure.

## Verification

- Identity fields match `_CONTEXT.md`, workbook row 21, and Gate 7 package register.
- Responsibility statements match Gate 7 package register and do not transfer vendor design work to EPC.
- Interface list matches workbook row 21 and Gate 7 PKG-019 interface columns.
- DBM MV electrical context is not overstated as package-specific VFD design data.
- All unsupported technical values remain `TBD`.
- Human ruling items HR-019-01-01, HR-019-01-02, and HR-019-01-03 are visible.
- No undeclared dependencies are treated as blockers.

## Records

- Completed package Scope of Work.
- Tagged equipment and package identity list, with unavailable tag fields marked `TBD`.
- Package function and integration narrative.
- Responsibility assignment record.
- Interface checklist for Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
- TBD / Human Ruling Required list for unresolved source gaps.
