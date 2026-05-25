# Procedure: DEL-033-01 Scope of Work

## Purpose

Define the working procedure for producing and checking the EPC Integrator Scope of Work for PKG-033, `4160V SWITCHGEAR ELECTRICAL BUILDING (830-2)`, using accepted Gate 7 truth and accessible source slices.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- Workbook Packages row 35 is referenced via Gate 7 registers (`_Sources/26020-Packages_Interfaces_4_export.xlsx`).
- Facility-level DBM electrical basis is available in `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Area Classification; System Voltages; Incoming Power and Transformers; 4160V MCC; Electrical Buildings, Raceways, Lighting, and Heat Tracing).
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md`.
- Package-specific vendor data and switchgear lineup: TBD; not present in accessible source slices.

## Steps

1. Confirm deliverable identity from `_CONTEXT.md`: `DEL-033-01_scope-of-work`, Scope of Work, PKG-033, Electrical, EPC Integrator.
2. Confirm package identity from Gate 7 `PACKAGE_REGISTER.csv` row PKG-033 / workbook Packages row 35: ID 33, WBS 02, tracking number `26020-02-30-024`, package name `4160V SWITCHGEAR ELECTRICAL BUILDING (830-2)`, discipline Electrical.
3. Confirm Gate 7 package basis, including Package Vendor responsibility for package engineering/design/equipment/vendor documentation and EPC Integrator responsibility for facility integration/interfaces.
4. Confirm Scope of Work deliverable role from Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis.
5. Confirm the twelve source-supported interface categories from Gate 7 `INTERFACE_REGISTER.csv` PKG-033 rows: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports.
6. Use the DBM electrical sections only to state facility-level context: 13.8 kV incoming from 04-25; 4,160 V medium-voltage service (3 phase, 3 wire, 60 Hz LRG; motors 250 hp to 5,500 hp); 13.8 kV / 4.16 kV / 12 MVA transformer feeding the 4160V MCC; electrical buildings housing MCCs, switchgear, distribution equipment, and HVAC/ventilation; separation of MV/LV power circuits from control/instrument circuits.
7. Draft the SOW content so that EPC Integrator scope is limited to integration, interfaces, tie-ins, constructability, procurement/construction coordination, and acceptance support across the twelve flagged interfaces.
8. Mark missing package-specific information as `TBD`, including tagged equipment, switchgear bus rating, short-circuit/withstand rating, breaker count and ratings, protective relaying scheme, enclosure rating, building dimensions, HVAC capacity, ventilation rate, fire/gas scheme, foundation loads, weights, and dimensions.
9. Add human ruling items for the `830-2` tag definition, missing package-specific design values, and the MCC vs. switchgear scope distinction.
10. Cross-check the SOW against the downstream PKG-033 deliverables (DEL-033-02 package datasheet, DEL-033-03 construction work package, DEL-033-04 vendor engineered equipment package, DEL-033-05 vendor document turnover, DEL-033-06 EPC review and acceptance) before closure.

## Verification

- Identity fields match `_CONTEXT.md`, Gate 7 `PACKAGE_REGISTER.csv` row PKG-033, and workbook row 35.
- Responsibility statements match Gate 7 package register and do not transfer vendor design work to EPC.
- Interface list matches Gate 7 `INTERFACE_REGISTER.csv` PKG-033 rows (all twelve YES interfaces).
- DBM facility electrical context is not overstated as package-specific switchgear or building design data.
- All unsupported technical values remain `TBD`.
- Human ruling items are visible for the `830-2` tag, missing design values, and the MCC vs. switchgear scope distinction.
- No undeclared dependencies are treated as blockers.

## Records

- Completed package Scope of Work.
- Tagged equipment and package identity list, with unavailable tag fields marked `TBD`.
- Package function and integration narrative for the 4,160 V switchgear electrical building (830-2).
- Responsibility assignment record.
- Interface checklist for all twelve Gate 7 YES interfaces.
- TBD / Human Ruling Required list for unresolved source gaps.
