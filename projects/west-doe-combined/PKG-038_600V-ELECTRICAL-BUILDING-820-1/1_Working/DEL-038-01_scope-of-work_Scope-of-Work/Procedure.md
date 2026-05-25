# Procedure: DEL-038-01 Scope of Work

## Purpose

Define the working procedure for producing and checking the EPC Integrator Scope of Work for PKG-038, `600V ELECTRICAL BUILDING (820-1)`, using accepted Gate 7 truth and accessible DBM Deepcut electrical source slices.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- Workbook Packages row 40 is available in `_Sources/26020-Packages_Interfaces_4_export.xlsx`.
- DBM Deepcut electrical design basis is available in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md`.
- Package-specific vendor data: TBD; not present in accessible source slices.

## Steps

1. Confirm deliverable identity from `_CONTEXT.md`: `DEL-038-01_scope-of-work`, Scope of Work, PKG-038, Electrical, EPC Integrator.
2. Confirm package identity from workbook Packages row 40 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-038: ID 38, WBS 01, tracking number `26020-01-30-029`, package name `600V ELECTRICAL BUILDING (820-1)`, discipline Electrical.
3. Confirm Gate 7 package basis from `PACKAGE_REGISTER.csv` row PKG-038, including Package Vendor responsibility for package engineering, package design, vendor documentation, and physical equipment package supply and EPC Integrator responsibility for facility integration and interfaces.
4. Confirm Scope of Work deliverable role from Gate 7 `DELIVERABLE_REGISTER.csv` row `DEL-038-01_scope-of-work` and the mandatory Gate 5 EPC anchor deliverable basis in `PROJECT_DECOMP.md`.
5. Confirm the four anticipated artifacts from Gate 7 `ARTIFACT_REGISTER.csv`: package scope of work; tagged equipment and package identity list; package function and whole-facility integration narrative; package responsibility assignment record.
6. Confirm the twelve source-supported interface categories from workbook row 40 and Gate 7 `INTERFACE_REGISTER.csv` PKG-038 rows: Utility Piping, Drain / Containment, Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Building HVAC / Services, Fire & Gas / Safety Systems, Maintenance Access, Grading / Site Drainage / Spill Containment, Structural / Foundations / Supports.
7. Confirm the supported objectives from Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv` rows for `DEL-038-01_scope-of-work` (OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010) and record the package-level association as context, not as additional technical requirements.
8. Use the DBM Deepcut electrical-building source slices only to state facility-level context: electrical buildings in general purpose areas; low-voltage services at 600 V, 3 phase, 3 wire, 60 Hz, high-resistance grounded with 5 A continuous resistor; 600 V MCC basis; prefabricated modular electrical-building housing scope; n+1 HVAC; bottom-entry cabling and pile elevation; TECK/ACIC wiring and EMT use; outdoor GFI receptacle; equipment removal provisions; grounding; and standby power at 600 V MCC level.
9. Preserve the workbook/Gate 7 package name `600V ELECTRICAL BUILDING (820-1)` and add a human-ruling item for the DBM conflict that names 820-1 as a 6.9 kV building while listing 600 V electrical buildings as 840-1, 850-1, and 860-1.
10. Draft the SOW content so that EPC Integrator scope is limited to integration, interfaces, tie-ins, constructability, procurement/construction coordination, and acceptance support across the twelve interface categories.
11. Mark missing package-specific information as `TBD`, including interior equipment lineup, ratings, quantities, dimensions, weights, foundation loads, HVAC unit count and rating, generator/transfer-switch coordination, and final building-number reconciliation.
12. Cross-check the SOW against the downstream package datasheet, construction work package, vendor package production, vendor document turnover, and EPC acceptance deliverables so the SOW does not pre-allocate downstream scope.

## Verification

- Identity fields match `_CONTEXT.md`, workbook row 40, and Gate 7 `PACKAGE_REGISTER.csv` row PKG-038.
- Responsibility statements match Gate 7 package register and do not transfer vendor design work to EPC.
- Interface list contains all twelve interface categories from workbook row 40 and Gate 7 `INTERFACE_REGISTER.csv` rows for PKG-038 and adds no others.
- DBM electrical-building, 600 V service, MCC, grounding, standby power, HVAC, cabling, and building-service statements are scoped as facility context, not as package-specific design values.
- All unsupported package-specific technical values remain `TBD`.
- Human-ruling items are visible for the workbook/Gate 7 `820-1` package name versus DBM building-list discrepancy, the interior-lineup source gap, and standby-generator allocation.
- No undeclared dependencies are treated as blockers.

## Records

- Completed package Scope of Work.
- Tagged equipment and package identity list, with unavailable interior equipment tags marked `TBD`.
- Package function and whole-facility integration narrative.
- Package responsibility assignment record.
- Interface checklist covering all twelve PKG-038 interface categories.
- TBD / Human Ruling Required list for unresolved source gaps: HR-038-01-01, HR-038-01-02, HR-038-01-03.
