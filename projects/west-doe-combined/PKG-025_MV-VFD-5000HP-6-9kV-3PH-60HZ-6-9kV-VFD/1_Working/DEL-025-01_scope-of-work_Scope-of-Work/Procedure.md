# Procedure: DEL-025-01 Scope of Work

## Purpose

Define the working procedure for producing and checking the EPC Integrator Scope of Work for PKG-025, `MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD`, using accepted Gate 7 truth and accessible source slices.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- Workbook Packages row 27 is available in `_Sources/26020-Packages_Interfaces_4_export.xlsx`.
- Facility-level DBM electrical basis is available in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md`.
- Package-specific vendor data: TBD; not present in accessible source slices.

## Steps

1. Confirm deliverable identity from `_CONTEXT.md`: `DEL-025-01_scope-of-work`, Scope of Work, PKG-025, Electrical, EPC Integrator.
2. Confirm package identity from workbook Packages row 27: ID 25, WBS 01, tracking number `26020-01-30-016`, package name `MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD`, discipline Electrical.
3. Confirm Gate 7 package basis from `PACKAGE_REGISTER.csv` row PKG-025, including Package Vendor responsibility for package engineering/design/equipment/vendor documentation and EPC Integrator responsibility for facility integration/interfaces.
4. Confirm Scope of Work deliverable role from Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis.
5. Confirm source-supported interface categories from workbook row 27 and Gate 7 `INTERFACE_REGISTER.csv`: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports.
6. Use the DBM electrical table only to state facility-level 6.9 kV MV service context: 6.9 kV, 3-phase, 3-wire, 60 Hz, low-resistance grounded; 100 A, 10 s NGR per 6.9 kV transformer; 6.9 kV MV cable basis (three-conductor copper TECK rated 8 kV, 100% insulation); MV starter / VFD basis at 6.9 kV MCC; electrical building basis.
7. Note in the SOW that the DBM names Starting VFDs for the inlet/sales compressor motors KM-2150/2250 on the 6.9 kV system, but do not bind PKG-025 to that application; the rating in the package title (5,000 hp) does not match the inlet/sales compressor driver rating (6,700 hp).
8. Draft the SOW content so that EPC Integrator scope is limited to integration, interfaces, tie-ins, constructability, procurement/construction coordination, and acceptance support.
9. Mark missing package-specific information as `TBD`, including driven-equipment tag, VFD topology, output filtering / harmonic mitigation, input/isolation transformer arrangement, bypass arrangement, enclosure, cooling, environmental rating, weights, dimensions, and support loads.
10. Add human ruling items when source gaps, rating-band mismatches, or driven-equipment binding could affect downstream package documents.
11. Cross-check the SOW against the package datasheet, construction work package assumptions, vendor turnover expectations, and EPC acceptance needs before closure.

## Verification

- Identity fields match `_CONTEXT.md`, workbook row 27, and Gate 7 package register.
- Responsibility statements match Gate 7 package register and do not transfer vendor design work to EPC.
- Interface list matches workbook row 27 and Gate 7 interface register (six interfaces).
- DBM MV electrical context is not overstated as package-specific design data.
- The 5,000 hp / 6,700 hp rating discrepancy and the 5,000 hp / 5,500 hp DBM rating-band point are both surfaced rather than reconciled silently.
- All unsupported technical values remain `TBD`.
- Human ruling items are visible for driven-equipment identity, rating-band mismatch, and missing package-specific MV VFD design data.
- No undeclared dependencies are treated as blockers.

## Records

- Completed package Scope of Work.
- Tagged equipment and package identity list, with unavailable tag fields marked `TBD`.
- Package function and integration narrative.
- Responsibility assignment record.
- Interface checklist for Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
- TBD / Human Ruling Required list for unresolved source gaps.
