# Procedure: DEL-013-01 Scope of Work

## Purpose

Define the working procedure for producing and checking the EPC Integrator Scope of Work for PKG-013, `100A DC UNINTERUPTIBLE POWER SUPPLY`, using accepted Gate 7 truth and accessible source slices.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- Workbook Packages row 15 is available in `_Sources/26020-Packages_Interfaces_4_export.xlsx`.
- Facility-level DBM electrical basis is available in `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md`.
- Package-specific vendor data: TBD; not present in accessible source slices.

## Steps

1. Confirm deliverable identity from `_CONTEXT.md`: `DEL-013-01_scope-of-work`, Scope of Work, PKG-013, Electrical, EPC Integrator.
2. Confirm package identity from workbook Packages row 15: ID 13, WBS 02, tracking number `26020-02-30-004`, package name `100A DC UNINTERUPTIBLE POWER SUPPLY`, discipline Electrical.
3. Confirm Gate 7 package basis from `PACKAGE_REGISTER.csv` row PKG-013, including Package Vendor responsibility for package engineering/design/equipment/vendor documentation and EPC Integrator responsibility for facility integration/interfaces.
4. Confirm Scope of Work deliverable role from Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis and DEC-013.
5. Confirm source-supported interface categories from workbook row 15 and Gate 7 `INTERFACE_REGISTER.csv`: Electrical Power, Grounding / Bonding, Maintenance Access, Structural / Foundations / Supports.
6. Use the DBM electrical table only to state facility-level UPS service context: UPS services are listed as 120 VAC / 125 VDC for control system, selected emergency/critical lighting, MV breaker control, and MV protective relay.
7. Draft the SOW content so that EPC Integrator scope is limited to integration, interfaces, tie-ins, constructability, procurement/construction coordination, and acceptance support.
8. Mark missing package-specific information as `TBD`, including tagged equipment, UPS capacity confirmation, battery autonomy, battery type, charger configuration, DC distribution, enclosure, weights, dimensions, and support loads.
9. Add human ruling items when source spelling, source gaps, or authority questions could affect downstream package documents.
10. Cross-check the SOW against the package datasheet, construction work package assumptions, vendor turnover expectations, and EPC acceptance needs before closure.

## Verification

- Identity fields match `_CONTEXT.md`, workbook row 15, and Gate 7 package register.
- Responsibility statements match Gate 7 package register and do not transfer vendor design work to EPC.
- Interface list matches workbook row 15 and Gate 7 interface register.
- DBM UPS service context is not overstated as package-specific design data.
- All unsupported technical values remain `TBD`.
- Human ruling items are visible for source spelling and missing package-specific UPS design data.
- No undeclared dependencies are treated as blockers.

## Records

- Completed package Scope of Work.
- Tagged equipment and package identity list, with unavailable tag fields marked `TBD`.
- Package function and integration narrative.
- Responsibility assignment record.
- Interface checklist for Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports.
- TBD / Human Ruling Required list for unresolved source gaps.
