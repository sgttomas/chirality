# Datasheet: DEL-076-01 — Scope of Work (Lube Oil Supply)

Pass: P1 (initial draft); Pass 2 consistency sweep applied.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-076-01_scope-of-work` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 384 |
| Deliverable Name | Scope of Work | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 384 |
| Deliverable Type | EPC Scope of Work | `DELIVERABLE_REGISTER.csv` row 384 |
| Parent Package | `PKG-076` — Lube Oil Supply | `PACKAGE_REGISTER.csv` row 70 |
| Workbook Row | 70 | `PACKAGE_REGISTER.csv` row 70 |
| WBS | 01 | `PACKAGE_REGISTER.csv` row 70 |
| Discipline | Mechanical | `PACKAGE_REGISTER.csv` row 70 |
| CoA Tracking Number | 26020-01-29-001 | `PACKAGE_REGISTER.csv` row 70 |
| Source CoA Tracking Number | 26020-01-29-001 | `PACKAGE_REGISTER.csv` row 70 |
| Responsible Party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 384 |
| Vendor Package Title | 26020-01-PT-29-001 — Lube Oil Supply | `PACKAGE_REGISTER.csv` row 70 |
| Vendor RFQ Source | Bid Docs/Budgetary/26020-01-PT-RFQ-29-001-Lube oil supply.docx | `PACKAGE_REGISTER.csv` row 70 (location TBD — not locally accessible) |

## Attributes (Package Identity Carried Into the SoW)

| Attribute | Value | Source |
|---|---|---|
| Package Function | Lube oil supply to all compressor packages on site | `SCOPE_LEDGER.csv` SOW-0136; `PACKAGE_REGISTER.csv` row 70 |
| Facility | West Doe Deepcut facility, Storage Tank Area | `SCOPE_LEDGER.csv` SOW-0136 |
| Service | Sweet and sour service | `SCOPE_LEDGER.csv` SOW-0137 |
| Number of Transfer Pumps | 2 | `SCOPE_LEDGER.csv` SOW-0136, SOW-0137 |
| Driver Type | Electric motor driven | `SCOPE_LEDGER.csv` SOW-0137 |
| Driver Constraint | No Toshiba motors | `SCOPE_LEDGER.csv` SOW-0138 |

## Tagged Equipment List

| Tag | Service | Function | Source |
|---|---|---|---|
| P-9240-1 | Cylinder Lube Oil Transfer Pump | Fills frame day tanks of compressor packages with cylinder lubricating oil from 400 bbl heated tank | `SCOPE_LEDGER.csv` SOW-0137; `4-25_Deepcut_DBM.md` Lube Oil Storage and Pump Basis |
| P-9250-1 | Crankcase Lube Oil Transfer Pump | Fills frame day tanks of compressor packages with crankcase lube oil from 200 bbl heated tank | `SCOPE_LEDGER.csv` SOW-0137; `4-25_Deepcut_DBM.md` Lube Oil Storage and Pump Basis |
| (Storage Tank) | Horizontal storage tank, split in middle for both lube oils (crankcase and compressor packing/cylinder) | Bulk storage | `SCOPE_LEDGER.csv` SOW-0137 |

Additional storage-system basis from `4-25_Deepcut_DBM.md` (Lube Oil Storage and Pump Basis):

| Item | Value |
|---|---|
| Compressor cylinder lube oil tank design specific gravity | 1.00 (TBC) |
| Compressor crank-case lube oil tank design specific gravity | 1.00 (TBC) |
| Cylinder lube oil storage volume | 400 bbl heated tank, storage tank area |
| Crank-case lube oil storage volume | 200 bbl heated tank, storage tank area |
| Cylinder oil type per compressor service | TBC (manufacturer-recommended; multiple oils may be required due to sulphur, rich gas, H2S) |
| Additional storage requirements | TBD |

## Conditions (Operating and Design)

| Parameter | Value | Source |
|---|---|---|
| Operating pressure | Low / atmospheric (lube oil transfer pump service) | `SCOPE_LEDGER.csv` SOW-0138 |
| Operating temperature range | Ambient to heated tank temperature | `SCOPE_LEDGER.csv` SOW-0138 |
| Design pressure | Low / atmospheric (lube oil transfer pump service) | `SCOPE_LEDGER.csv` SOW-0138 |
| Design temperature range | Ambient to heated tank temperature | `SCOPE_LEDGER.csv` SOW-0138 |
| Heated-tank set point | TBD | not stated in accessible sources |
| Fluids | Compressor cylinder oil; compressor crank-case oil | `SCOPE_LEDGER.csv` SOW-0137; DBM Lube Oil Storage basis |
| Service classification | Sweet and sour service | `SCOPE_LEDGER.csv` SOW-0137 |

## Construction / Battery-Limit Items

| Item | Treatment | Source |
|---|---|---|
| Shipping to site | By others (outside package vendor scope) | `SCOPE_LEDGER.csv` SOW-0138 |
| Installation on piles | By others | `SCOPE_LEDGER.csv` SOW-0138 |
| Tie-in piping | By others | `SCOPE_LEDGER.csv` SOW-0138 |
| Electrical connections (to package) | By others | `SCOPE_LEDGER.csv` SOW-0138 |
| Mounting platform and stairs | By others | `SCOPE_LEDGER.csv` SOW-0138 |
| Pump skid | Vendor scope | `SCOPE_LEDGER.csv` SOW-0137 |
| Storage tank (horizontal, split) | Vendor scope | `SCOPE_LEDGER.csv` SOW-0137 |

## Declared Interface Set (Workbook-Asserted)

| Interface Type | Asserted | Interface ID |
|---|---|---|
| Utility Piping | YES | `IFC-B592C2D9F7` |
| Drain / Containment | YES | `IFC-09EA6BEDB8` |
| Electrical Power | YES | `IFC-4D53A7E70E` |
| Grounding / Bonding | YES | `IFC-7117284B73` |
| Area / Exterior Lighting | YES | `IFC-986D504634` |
| I&C / Control Cabling | YES | `IFC-8C17CDE23B` |
| Maintenance Access | YES | `IFC-6D43DAF029` |
| Structural / Foundations / Supports | YES | `IFC-ACA2756AA0` |

Source: `INTERFACE_REGISTER.csv` rows 557-564 (Workbook Packages row 70).

## Scope Items Covered

| Scope Item | Disposition | Subject |
|---|---|---|
| `SOW-0135` | IN | Carry workbook-defined vendor-responsible Mechanical package as a distinct flat project package; vendor/EPC responsibility split |
| `SOW-0136` | IN | Basic scope: supply of two (2) lube oil transfer pumps for the Storage Tank Area serving all compressor packages on site |
| `SOW-0137` | IN | Major included equipment: P-9240-1, P-9250-1, horizontal split storage tank, electric drivers, sweet/sour service |
| `SOW-0138` | IN | Scope notes / open items: by-others list, no Toshiba motors, operating and design conditions |

Source: `SCOPE_LEDGER.csv` rows 136-139.

## Supported Objectives

`OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` — per `_CONTEXT.md`, `DELIVERABLE_REGISTER.csv` row 384, and `PACKAGE_REGISTER.csv` row 70 (package-grouped association — ASSUMPTION at package-heuristic resolution; objective texts retrieved from `OBJECTIVE_REGISTER.csv`).

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` row 70
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` rows 384-389
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/SCOPE_LEDGER.csv` rows 136-139 (SOW-0135 through SOW-0138)
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv` rows 557-564
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/ARTIFACT_REGISTER.csv` rows 4033-4037
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/OBJECTIVE_REGISTER.csv` rows for OBJ-001/004/005/006/007/008/009/010
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — Lube Oil Storage and Pump Basis (lines ~2059-2072)
- `_Sources/26020-Package_Requirements.docx` — package heading 30 (binary; location TBD for direct text extraction)
- `_Sources/Bid Docs/Budgetary/26020-01-PT-RFQ-29-001-Lube oil supply.docx` (location TBD — not present in accessible workspace)
