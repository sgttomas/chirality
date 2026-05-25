# Procedure: DEL-024-01 Scope of Work

## Purpose

Define the working procedure for producing and checking the EPC Integrator Scope of Work for PKG-024, `MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD`, using accepted Gate 7 truth and accessible source slices.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- Workbook Packages row 26 is referenced via Gate 7 registers; the source workbook is `_Sources/26020-Packages_Interfaces_4_export.xlsx` (no local slice copied during PREPARATION).
- Facility-level DBM electrical basis is available in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Motor Control and Motor Specifications, Electrical Buildings).
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md`.
- Package-specific MV VFD vendor data: TBD; not present in accessible source slices.

## Steps

1. Confirm deliverable identity from `_CONTEXT.md`: `DEL-024-01_scope-of-work`, Scope of Work, PKG-024, Electrical, EPC Integrator.
2. Confirm package identity from Gate 7 `PACKAGE_REGISTER.csv` row PKG-024 and workbook Packages row 26: ID 24, WBS 01, tracking number `26020-01-30-015`, package name `MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD`, discipline Electrical.
3. Confirm Gate 7 package basis from `PACKAGE_REGISTER.csv` row PKG-024, including Package Vendor responsibility for package engineering/design/equipment/vendor documentation and EPC Integrator responsibility for facility integration/interfaces.
4. Confirm Scope of Work deliverable role from Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis and DEC-001.
5. Confirm the six source-supported interface categories from workbook row 26 and Gate 7 `INTERFACE_REGISTER.csv`: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports.
6. Use the DBM-Deepcut electrical basis only to state facility-level context: medium-voltage VFDs are listed equipment for prefabricated electrical buildings (line 2973); the 4.16 kV MCC connects to the plant PLC over Ethernet (line 2957); 4.16 kV VFD/soft-starter requirements are explicitly TBD at the facility-basis level (lines 2957, 3088); motors 100 hp and larger may be fed from soft starters or VFDs (line 2963).
7. Draft the SOW content so that EPC Integrator scope is limited to integration, interfaces, tie-ins, constructability, procurement/construction coordination, and acceptance support.
8. Mark missing package-specific information as `TBD`, including driven motor tag and service, manufacturer, VFD topology, harmonic mitigation, cooling, enclosure rating, weights, dimensions, support loads, control architecture, communication protocols, and protection settings.
9. Record objective associations OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 as accepted directional context per Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`; do not derive new requirements from objective IDs alone.
10. Add human ruling items when source name redundancy, missing driven-motor identity, or objective-binding interpretation could affect downstream package documents.
11. Cross-check the SOW against the package datasheet, construction work package assumptions, vendor turnover expectations, and EPC acceptance needs before closure.

## Verification

- Identity fields match `_CONTEXT.md`, Gate 7 `PACKAGE_REGISTER.csv` row PKG-024, and workbook Packages row 26 (via Gate 7).
- Responsibility statements match Gate 7 package register and do not transfer vendor design work to EPC.
- Interface list matches workbook row 26 and Gate 7 `INTERFACE_REGISTER.csv` rows for PKG-024 (six categories).
- DBM-Deepcut MV/VFD context is not overstated as package-specific design data; the explicit "4.16 kV VFD requirements TBD" statement is preserved.
- All unsupported technical values remain `TBD`.
- Human ruling items are visible for source-name redundancy, missing driven-motor identity, and objective-binding interpretation.
- Objective associations match Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv` DEL-024-01 rows.
- No undeclared dependencies are treated as blockers.

## Records

- Completed package Scope of Work.
- Tagged equipment and package identity list, with driven motor and other unavailable tag fields marked `TBD`.
- Package function and integration narrative anchored to the facility 4.16 kV / MV VFD basis.
- Responsibility assignment record.
- Interface checklist for Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
- Objective association record (OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010) as accepted context.
- TBD / Human Ruling Required list for unresolved source gaps.
