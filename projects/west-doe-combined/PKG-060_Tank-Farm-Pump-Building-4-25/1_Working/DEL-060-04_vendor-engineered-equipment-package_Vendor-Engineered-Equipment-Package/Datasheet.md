# Datasheet — DEL-060-04 Vendor Engineered Equipment Package

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-060-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Name | Vendor Engineered Equipment Package | `_CONTEXT.md` |
| ParentPackageID | `PKG-060` | `_CONTEXT.md` |
| Package | Tank Farm Pump Building 4-25 | `_CONTEXT.md`; DBM SEC-10 line items rows 80-84 (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2618-2622) |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | Vendor Package Production Unit | `_CONTEXT.md` |
| Responsible Party | Package Vendor (engineering, design, equipment) with EPC Integrator integration review | `_CONTEXT.md` |
| Facility | West Doe Deepcut expansion (04-25); LSD 04-25-80-15W6 | DBM SEC-01 (lines 7, 16-17) |
| Anchoring deliverables | DEL-060-01 EPC Scope of Work; DEL-060-02 EPC Package Datasheet | `_CONTEXT.md`; deliverable register row 477 |

## Attributes — Package Composition (source: DBM SEC-10 line items)

ASSUMPTION: The DBM labels this package "Tank Farm Pump Building 2" (4-25 area). The decomposition deliverable name is "Tank Farm Pump Building 4-25". Treated as the same package pending human ruling. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2555, decomposition `DELIVERABLE_REGISTER.csv` row 477.

| Line Item | Service | Quantity | Equipment Tags | Pump Type (DBM Notes) |
|---|---|---:|---|---|
| Row 80 | Condensate Transfer Pumps | x2 | P-9210-1, P-9220-1 | Pumps (multi-stage horizontal) |
| Row 81 | Water Transfer Pump | x4 declared / x2 listed (CONFLICT) | P-9290-1, P-9293-1 | Pumps (radial centrifugal) 1 |
| Row 82 | Sour Water Treatment Pumps | x2 | P-9231-1, P-9232-1 | Pumps (radial centrifugal) 1 |
| Row 83 | Process Water Transfer Pumps | x2 | P-5317-1, P-5318-1 | Pumps (radial centrifugal) 2 |
| Row 84 | Fresh Caustic Transfer Pumps | x2 | P-6760-1, P-6765-1 | Pumps (radial centrifugal) 2 |
| Building | Tank Farm Pump Module (920-1) | 1 | n/a | Shop-fabricated module (SEC-10 module list line 2817) |

CONFLICT: Source line 2555 indicates "WATER TRANSFER PUMP (x4)" in the line-item summary, while the detailed table (line 2619) lists only two tags (P-9290-1, P-9293-1) at count 2. Recorded for human ruling in Conflict Table (Guidance.md).

## Conditions

| Parameter | Value | Source |
|---|---|---|
| Site / facility identifier | 04-25 | DBM line 16 |
| Primary site | LSD 04-25-80-15W6 | DBM line 17 |
| Module fabrication mode | Shop-built (920-1 Tank Farm Pump Module) | DBM line 2817 |
| Service envelope (condensate transfer) | 350 kPad / 50 psid differential to liquids hub; sized for >= 150% of combined condensate product design flow; both pumps capable of simultaneous operation | DBM lines 1673-1675 |
| Design NPSHR limit (condensate transfer) | <= 0.75 m at design flow | DBM line 1677 |
| Motor design temperature basis | Inlet stabilizer composition density at -40 deg C startup, including JT-mode startup | DBM line 1679 |
| Minimum-flow control | Continuous pumping minimum-flow control valve provided | DBM line 1679 |
| Product recycle pump | 1 x 100%, manual operator start; 20 m3/h at 80 m TDH, TBC | DBM line 1671 |
| Condensate skim pump | 1 x 100%, automatic skim on produced-water interface level; 20 m3/h at 80 m TDH, TBC | DBM line 1672 |
| Building color (flashing/doors/trim) | Cloverdale # 2593 "Safety Green" | DBM line 2824 |

## Construction

| Aspect | Value | Source |
|---|---|---|
| Fabrication | Shop-built pump module 920-1 | DBM SEC-10 module table (line 2817) |
| Building envelope | Pre-painted galvanized metal walls and roof; bright white QC8783 interior | DBM lines 2825-2826 |
| Tank-farm storage interface tags | TK-9110-1..TK-9150-1 (5 condensate); TK-9010-1, TK-9020-1 (produced water); TK-5317-1, TK-5318-1 (process water); TK-6760-1 (fresh caustic); TK-6770-1 (DSO); TK-6780-1 (spent caustic) | DBM lines 2623-2628 |
| Hazardous-area / pump pad arrangement | TBD pending vendor engineering | location TBD in source |

## Scope Coverage and Objectives

| Scope items covered | Objectives supported |
|---|---|
| SOW-0189, SOW-0190, SOW-0191, SOW-0192 | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 |

Objective associations are PACKAGE_HEURISTIC (ASSUMPTION) per `_CONTEXT.md`.

## References

- `_CONTEXT.md` (this deliverable folder)
- `_REFERENCES.md` (this deliverable folder)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — sections SEC-09 (Product Pumps; lines 1667-1679), SEC-10 (Package Line-Item Requirements; lines 2555, 2618-2622, 2817), SEC-11 (Civil/Buildings; line 2825)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row 477
- Original workbook row 85 (`26020-Packages_Interfaces_4_export.xlsx`) — location TBD (binary not opened)
- `26020-Package_Requirements.docx` heading 15 — location TBD (binary not opened)
