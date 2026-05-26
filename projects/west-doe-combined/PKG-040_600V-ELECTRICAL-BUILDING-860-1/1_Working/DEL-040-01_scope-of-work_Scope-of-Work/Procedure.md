# Procedure: DEL-040-01 Scope of Work

## Purpose

Define the working procedure for producing and checking the EPC Integrator Scope of Work for PKG-040, `600V ELECTRICAL BUILDING (860-1)`, using accepted Gate 7 truth and accessible DBM Deepcut Section 12 source slices.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- Workbook Packages row 42 is referenced in `_Sources/26020-Packages_Interfaces_4_export.xlsx` (binary workbook; clause-level workbook content cited only where mirrored by Gate 7 registers).
- DBM Deepcut electrical design basis (Section 12, lines 2860-3090) is available in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md`.
- Package-specific vendor data: TBD; not present in accessible source slices.

## Steps

1. Confirm deliverable identity from `_CONTEXT.md`: `DEL-040-01_scope-of-work`, Scope of Work, PKG-040, Electrical, EPC Integrator.
2. Confirm package identity from workbook Packages row 42 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-040: ID 40, WBS 01, tracking number `26020-01-30-031`, package name `600V ELECTRICAL BUILDING (860-1)`, discipline Electrical.
3. Confirm Gate 7 package basis from `PACKAGE_REGISTER.csv` row PKG-040, including Package Vendor responsibility for package engineering/design/equipment/vendor documentation and EPC Integrator responsibility for facility integration/interfaces.
4. Confirm Scope of Work deliverable role from Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-040-01_scope-of-work (mandatory Gate 5 EPC anchor deliverable) and `PROJECT_DECOMP.md`.
5. Confirm the twelve source-supported interface categories from workbook row 42 and Gate 7 `INTERFACE_REGISTER.csv` PKG-040 rows: Utility Piping, Drain / Containment, Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Building HVAC / Services, Fire & Gas / Safety Systems, Maintenance Access, Grading / Site Drainage / Spill Containment, Structural / Foundations / Supports.
6. Confirm the supported objectives from Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv` rows for DEL-040-01_scope-of-work (OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010) and record as ASSUMPTION (package-heuristic mapping).
7. Use the DBM Deepcut electrical-building source slices only to state facility-level context: 860-1 named as the General Area / Tank Farm electrical building (line 2816); prefabricated modular building in a general purpose area (lines 2911, 2971); possible interior contents at facility basis (line 2973); n+1 HVAC (line 2975); bottom-entry cabling and pile elevation (line 2977); TECK/ACIC wiring, EMT, outdoor GFI (line 2979); 600 V service basis (line 2937); MCC basis (line 2959); grounding basis including 5 A continuous high-resistance grounding (lines 2985-2991); standby power basis (line 2943); building heaters (line 3071).
8. Draft the SOW content so that EPC Integrator scope is limited to integration, interfaces, tie-ins, constructability, procurement/construction coordination, and acceptance support across the twelve interface categories.
9. Mark missing package-specific information as `TBD`, including interior equipment lineup, ratings, quantities, dimensions, weights, foundation loads, HVAC unit count and rating, generator/transfer-switch coordination, area classification at the 860-1 location, specific tank-farm loads served, RDC design, and secondary cable-tray routing.
10. Add human-ruling items for the building-name discrepancy (workbook/Gate 7 vs DBM line 2816), the package-specific interior lineup gap, the facility-wide standby generator integration TBD, and the tank-farm-load / area-classification TBD.
11. Cross-check the SOW against the package datasheet (DEL-040-02), construction work package (DEL-040-03), vendor package production (DEL-040-04), vendor document turnover (DEL-040-05), and EPC acceptance (DEL-040-06) anticipated content so the SOW does not pre-allocate downstream scope.

## Verification

- Identity fields match `_CONTEXT.md`, workbook row 42, and Gate 7 `PACKAGE_REGISTER.csv` row PKG-040.
- Responsibility statements match Gate 7 package register and do not transfer vendor design work to EPC.
- Interface list contains all twelve interface categories from workbook row 42 and Gate 7 `INTERFACE_REGISTER.csv` rows for PKG-040 and adds no others.
- DBM electrical-building, 600 V service, MCC, grounding, standby power, and building-heater statements are scoped as facility context, not as package-specific design values.
- All unsupported package-specific technical values remain `TBD`.
- Human-ruling items are visible for the building-name discrepancy, the interior-lineup source gap, the standby-generator integration TBD, and the tank-farm-load / area-classification gap.
- No undeclared dependencies are treated as blockers.

## Records

- Completed package Scope of Work (artifact ART-95D8796E51).
- Tagged equipment and package identity list, with unavailable interior equipment tags marked `TBD` (artifact ART-22111E8269).
- Package function and whole-facility integration narrative (artifact ART-EBFDF9B165).
- Package responsibility assignment record (artifact ART-1C1CC3907A).
- Interface checklist covering all twelve PKG-040 interface categories.
- TBD / Human Ruling Required list for unresolved source gaps (HR-040-01, HR-040-02, HR-040-03, HR-040-04).
