# Procedure: DEL-022-01 Scope of Work

## Purpose

Define the working procedure for producing and checking the EPC Integrator Scope of Work for PKG-022, `5kV SWITCHGEAR EQUIPMENT`, using accepted Gate 7 truth and accessible source slices.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- Workbook Packages row 24 is available in `_Sources/26020-Packages_Interfaces_4_export.xlsx`.
- Facility-level DBM electrical basis is available in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (electrical and MV services sections).
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md`.
- Package-specific vendor data: TBD; not present in accessible source slices.
- Project-level MV switchgear standards/specifications: TBD; not directly accessible.

## Steps

1. Confirm deliverable identity from `_CONTEXT.md`: `DEL-022-01_scope-of-work`, Scope of Work, PKG-022, Electrical, EPC Integrator.
2. Confirm package identity from workbook Packages row 24: ID 22, WBS 01, tracking number `26020-01-30-013`, package name `5kV SWITCHGEAR EQUIPMENT`, discipline Electrical.
3. Confirm Gate 7 package basis from `PACKAGE_REGISTER.csv` row PKG-022, including Package Vendor responsibility for package engineering/design/equipment/vendor documentation and EPC Integrator responsibility for facility integration/interfaces.
4. Confirm Scope of Work deliverable role from Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis and Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-022-01_scope-of-work.
5. Confirm source-supported interface categories from workbook row 24 and Gate 7 `PACKAGE_REGISTER.csv`: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports.
6. Use the DBM Deepcut electrical sections only to state facility-level MV context: 13.8 kV main distribution bus from the 25 kV / 13.8 kV / 50 MVA utility transformer; facility MV services at 6.9 kV (motors 5,500 hp and above) and 4.160 kV (motors 250 hp up to 5,500 hp); 4.160 kV cables specified as TECK rated 5 kV with 100 percent insulation; low-resistance grounded MV system. Do not assert a discrete 5 kV facility bus.
7. Draft the SOW content so that EPC Integrator scope is limited to integration, interfaces, tie-ins, constructability, procurement/construction coordination, and acceptance support.
8. Mark missing package-specific information as `TBD`, including tagged equipment, fed-load list, bus voltage assignment, short-circuit rating, breaker type, lineup configuration, BIL, neutral grounding implementation, protection scheme, enclosure, cooling, environmental rating, weights, dimensions, footprint, and support loads.
9. Carry the "5 kV" naming-vs-facility-bus ambiguity as Conflict HR-022-01-01 and do not silently reconcile.
10. Carry the tagged equipment / served-load / PKG-022-to-PKG-037 building-association question as Conflict HR-022-01-02.
11. Carry the standards/specifications accessibility gap as Conflict HR-022-01-03.
12. Cross-check the SOW against the package datasheet, construction work package assumptions, vendor turnover expectations, and EPC acceptance needs before closure.

## Verification

- Identity fields match `_CONTEXT.md`, workbook row 24, and Gate 7 package register.
- Responsibility statements match Gate 7 package register and do not transfer vendor design work to EPC.
- Interface list matches workbook row 24 and Gate 7 PKG-022 interface columns.
- DBM MV electrical context is not overstated as package-specific switchgear design data.
- All unsupported technical values remain `TBD`.
- Human ruling items HR-022-01-01, HR-022-01-02, and HR-022-01-03 are visible.
- No undeclared dependencies are treated as blockers.

## Records

- Completed package Scope of Work.
- Tagged equipment and package identity list, with unavailable tag fields marked `TBD`.
- Package function and integration narrative.
- Responsibility assignment record.
- Interface checklist for Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
- TBD / Human Ruling Required list for unresolved source gaps.
