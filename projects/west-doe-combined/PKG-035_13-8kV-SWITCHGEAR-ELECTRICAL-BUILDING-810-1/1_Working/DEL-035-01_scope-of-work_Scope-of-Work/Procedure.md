# Procedure: DEL-035-01 Scope of Work

## Purpose

Define the working procedure for producing and checking the EPC Integrator Scope of Work for PKG-035, `13.8kV SWITCHGEAR ELECTRICAL BUILDING (810-1)`, using accepted Gate 7 truth and accessible source slices.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- Workbook Packages row 37 is available in `_Sources/26020-Packages_Interfaces_4_export.xlsx`.
- Facility-level DBM-Deepcut electrical basis is available in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Electrical Buildings table, 13.8 kV switchgear narrative, System Voltages table).
- Facility-level DBM-Comp_and_Liquids electrical-buildings narrative is available in `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md`.
- Package-specific vendor data (switchgear ratings, building dimensions, structural loads, HVAC heat load, fire & gas device list): TBD; not present in accessible source slices.

## Steps

1. Confirm deliverable identity from `_CONTEXT.md`: `DEL-035-01_scope-of-work`, Scope of Work, PKG-035, Electrical, EPC Integrator.
2. Confirm package identity from workbook Packages row 37: ID 35, WBS 01, tracking number `26020-01-30-026`, package name `13.8kV SWITCHGEAR ELECTRICAL BUILDING (810-1)`, discipline Electrical.
3. Confirm Gate 7 package basis from `PACKAGE_REGISTER.csv` row PKG-035, including Package Vendor responsibility for package engineering/design/equipment/vendor documentation and EPC Integrator responsibility for facility integration/interfaces.
4. Confirm Scope of Work deliverable role from Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis.
5. Confirm source-supported interface categories from workbook row 37 and Gate 7 `INTERFACE_REGISTER.csv` (twelve categories: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports).
6. Use the DBM-Deepcut 13.8 kV switchgear narrative to state the package function (plant main 13.8 kV power distribution center), the utility supply basis (BC Hydro 25 kV (TBC) feed, 25 kV/13.8 kV, 50 MVA utility-supplied transformer, 13.8 kV bus sized for full facility scope), the downstream radial distribution targets (6.9 kV, 4.16 kV, 600 V, and 4.16 kV/600 V electrical buildings), and the shared 03-25 / 04-25 distribution posture.
7. Use the DBM-Deepcut System Voltages table to state medium-voltage system basis: 13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded.
8. Use the DBM-Deepcut Electrical Buildings table and the DBM-Comp_and_Liquids electrical-buildings narrative to identify 810-1 as a Shop-delivered pre-engineered electrical building housing MCCs, switchgear, distribution equipment, and associated HVAC/ventilation systems, with area classification, HVAC, and remote distribution centres coordinated with hazardous area classification and controls architecture.
9. Draft the SOW content so that EPC Integrator scope is limited to integration, interfaces, tie-ins, constructability, procurement/construction coordination, and acceptance support.
10. Mark missing package-specific information as `TBD`, including switchgear ratings, bus continuous current, short-circuit rating, breaker count, lineup configuration, building dimensions, structural loads, HVAC heat load, and fire & gas device list.
11. Add human ruling items for the "25 kV (TBC)" utility voltage, missing package-specific design values, and the 03-25 / 04-25 shared distribution / metering / protection / emergency scope items.
12. Cross-check the SOW against the package datasheet, construction work package assumptions, vendor turnover expectations, and EPC acceptance needs before closure.

## Verification

- Identity fields match `_CONTEXT.md`, workbook row 37, and Gate 7 package register.
- Responsibility statements match Gate 7 package register and do not transfer vendor design work to EPC.
- Interface list matches the twelve categories in workbook row 37 and Gate 7 interface register (no silent omission, no expansion).
- Package function narrative matches the DBM-Deepcut 13.8 kV switchgear narrative (utility feed, transformer, bus sizing, radial distribution targets, shared 03-25 / 04-25 posture).
- Medium-voltage system parameters match the DBM-Deepcut System Voltages table.
- Building identity and housed-equipment scope match DBM-Deepcut Electrical Buildings table and DBM-Comp_and_Liquids electrical buildings narrative.
- All unsupported technical values remain `TBD`.
- Human ruling items are visible for the TBC utility voltage, missing package-specific design values, and shared 03-25 / 04-25 open items.
- No undeclared dependencies are treated as blockers.

## Records

- Completed package Scope of Work.
- Tagged equipment and package identity list (building tag `810-1`; equipment tag fields marked `TBD` where unavailable).
- Package function and integration narrative covering utility supply, 13.8 kV bus, radial distribution to downstream electrical buildings, and shared 03-25 / 04-25 posture.
- Responsibility assignment record.
- Interface checklist for the twelve source-supported interface categories.
- TBD / Human Ruling Required list for unresolved source gaps (TBC utility voltage, package-specific design values, shared 03-25 / 04-25 items).
