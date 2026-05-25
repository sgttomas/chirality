# Procedure: DEL-014-01 Scope of Work

## Purpose

Define the working procedure for producing and checking the EPC Integrator Scope of Work for PKG-014, `CONTACTOR PANELS - LIGHTING / EXHAUST FAN CONTACTOR PANELS - LOW VOLTAGE`, using accepted Gate 7 truth and accessible source slices.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- Workbook Packages row 16 identity and interface flags are reflected in Gate 7 `PACKAGE_REGISTER.csv` (PKG-014) and `INTERFACE_REGISTER.csv` (PKG-014 rows).
- Facility-level DBM electrical basis is available in `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` and `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md`.
- Package-specific vendor data: TBD; not present in accessible source slices.

## Steps

1. Confirm deliverable identity from `_CONTEXT.md`: `DEL-014-01_scope-of-work`, Scope of Work, PKG-014, Electrical, EPC Integrator.
2. Confirm package identity from Gate 7 `PACKAGE_REGISTER.csv` row PKG-014: ID 14, workbook row 16, WBS 02, tracking number `26020-02-30-005`, package name `CONTACTOR PANELS - LIGHTING / EXHAUST FAN CONTACTOR PANELS - LOW VOLTAGE`, discipline Electrical.
3. Confirm Gate 7 responsibility split: Package Vendor owns package engineering/design/equipment/vendor documentation; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination.
4. Confirm Scope of Work deliverable role from Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis and `_CONTEXT.md` Notes.
5. Confirm source-supported interface categories from Gate 7 `INTERFACE_REGISTER.csv` PKG-014 rows and workbook row 16: Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports.
6. Use the DBM Comp and Liquids Electrical Power Distribution table only to state facility-level LV service context (600 V, 3 phase, 3 wire, 60 Hz HRG with 5A continuous resistor) and 120/208 V lighting/utility service context.
7. Use the DBM Deepcut Electrical Buildings section to state the contactor-panel housing context (208/120 V contactor panels in the electrical building lineup; EMT conduit between control panels and contactor panels) and the 208/120 V AC building exhaust fan / heater blower load context.
8. Use the DBM Remote I/O note as permissive context only for possible exhaust-fan/heater control through Remote I/O nodes; do not assign a control topology to PKG-014.
9. Draft the SOW content so that EPC Integrator scope is limited to integration, interfaces, tie-ins, constructability, procurement/construction coordination, and acceptance support.
10. Mark missing package-specific information as `TBD`, including tagged equipment, panel counts, panel ratings, enclosure type, environmental class, lineup arrangement, load schedules, lighting branch circuit details, and exhaust-fan control wiring counts.
11. Add human ruling items when source gaps could affect downstream package documents (see Guidance Conflict Table).
12. Cross-check the SOW against the package datasheet (DEL-014-02), construction work package (DEL-014-03), vendor production unit (DEL-014-04), vendor turnover (DEL-014-05), and EPC acceptance (DEL-014-06) expectations before closure.

## Verification

- Identity fields match `_CONTEXT.md`, Gate 7 `PACKAGE_REGISTER.csv` row PKG-014, and Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-014-01_scope-of-work.
- Responsibility statements match Gate 7 package register and do not transfer vendor design work to EPC.
- Interface list matches Gate 7 `INTERFACE_REGISTER.csv` PKG-014 rows (seven YES) and workbook row 16.
- DBM LV, lighting/utility, contactor-panel housing, and Remote I/O statements are not overstated as PKG-014-specific design data.
- All unsupported technical values remain `TBD`.
- Human ruling items are visible for missing package-specific design data and for the permissive Remote I/O control note.
- No undeclared dependencies are treated as blockers.

## Records

- Completed package Scope of Work.
- Tagged equipment and package identity list, with unavailable tag fields marked `TBD`.
- Package function and integration narrative for low-voltage lighting and exhaust-fan contactor panels.
- Responsibility assignment record.
- Interface checklist for the seven Gate 7 flagged categories.
- TBD / Human Ruling Required list for unresolved source gaps.
