# Procedure: DEL-028-01 Scope of Work

## Purpose

Define the working procedure for producing and checking the EPC Integrator Scope of Work for PKG-028, `Transformer TXP-8801-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 7.5MVA 13.8kV/4160/2400V`, using accepted Gate 7 truth and accessible source slices.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- Workbook Packages row 30 is available in `_Sources/26020-Packages_Interfaces_4_export.xlsx`.
- Facility-level DBM Deepcut electrical basis is available in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md`.
- Package-specific vendor data: TBD; not present in accessible source slices.

## Steps

1. Confirm deliverable identity from `_CONTEXT.md`: `DEL-028-01_scope-of-work`, Scope of Work, PKG-028, Electrical, EPC Integrator.
2. Confirm package identity from workbook Packages row 30 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-028: ID 28, WBS 01, tracking number `26020-01-30-019`, package name `Transformer TXP-8801-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 7.5MVA 13.8kV/4160/2400V`, equipment tag `TXP-8801-1`, discipline Electrical.
3. Confirm Gate 7 package basis from `PACKAGE_REGISTER.csv` row PKG-028, including Package Vendor responsibility for package engineering/design/equipment/vendor documentation and EPC Integrator responsibility for facility integration/interfaces.
4. Confirm Scope of Work deliverable role as a mandatory EPC anchor deliverable from Gate 7 `PROJECT_DECOMP.md` and the DELIVERABLE_REGISTER row for DEL-028-01.
5. Confirm source-supported interface categories from workbook row 30 and Gate 7 `INTERFACE_REGISTER.csv` (rows IFC-5A6FBABCBA, IFC-22E75E0E48, IFC-487236B7E5, IFC-FD9BCC3585, IFC-2C9EC16D97, IFC-5C19FEBFC8, IFC-B1AD88E9C0): Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports.
6. Use the DBM Deepcut electrical section (lines 2917-2991) only to state facility-level context: 25 kV utility feed, 50 MVA utility transformer, 13.8 kV switchgear feeding step-down transformers radially, transformer foundation/spacing per CEC, and transformer grounding basis.
7. Draft the SOW content so that EPC Integrator scope is limited to facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and acceptance support.
8. Mark missing package-specific information as `TBD`, including vendor nameplate confirmation, impedance, vector group, taps, cooling class, insulation/BIL, fluid, accessories, weights, dimensions, support loads, secondary winding configuration, and load assignment.
9. Add human ruling items when source gaps or authority questions could affect downstream package documents (see Guidance Conflict Table, items HR-028-01..HR-028-03).
10. Cross-check the SOW against the package datasheet, construction work package assumptions, vendor turnover expectations, and EPC acceptance needs before closure.

## Verification

- Identity fields match `_CONTEXT.md`, workbook row 30, and Gate 7 package register.
- Equipment tag `TXP-8801-1` and the full source-derived package name string are preserved exactly.
- Responsibility statements match Gate 7 package register and do not transfer vendor design work to EPC.
- Interface list matches workbook row 30 and Gate 7 interface register (seven interface types).
- DBM Deepcut electrical context is not overstated as package-specific design data.
- All unsupported technical values remain `TBD`.
- Human ruling items are visible for secondary configuration, missing package-specific transformer design data, and load assignment.
- Objective associations match Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv` (OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010).
- No undeclared dependencies are treated as blockers.

## Records

- Completed package Scope of Work.
- Tagged equipment and package identity list, including `TXP-8801-1` and additional tags marked `TBD` where unavailable.
- Package function and integration narrative.
- Responsibility assignment record.
- Interface checklist for Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
- TBD / Human Ruling Required list for unresolved source gaps.
