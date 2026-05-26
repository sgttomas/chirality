# Datasheet — DEL-065-01 Scope of Work — Tanks, Caustic (API 650) 4-25 (PKG-065)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-065-01_scope-of-work` | `_CONTEXT.md` |
| Deliverable Name | Scope of Work | `_CONTEXT.md` |
| ParentPackageID | `PKG-065` | `_CONTEXT.md` |
| Package Name | Tanks, Caustic (API 650) 4-25 | PACKAGE_REGISTER.csv row PKG-065 |
| Workbook Row | 87 | PACKAGE_REGISTER.csv row PKG-065 |
| Discipline | Mechanical | PACKAGE_REGISTER.csv row PKG-065 |
| WBS | 01 | PACKAGE_REGISTER.csv row PKG-065 |
| Vendor Tracking No. | 26020-01-PT-19-003 | PACKAGE_REGISTER.csv row PKG-065 (VendorTrackingNumberName) |
| Responsible Party | EPC Integrator (facility integration); Package Vendor (engineering, design, equipment, documentation) | PACKAGE_REGISTER.csv row PKG-065 (Responsibility) |
| Document Type | EPC Scope of Work | `_CONTEXT.md` |

## Attributes — Tagged Equipment in Package

| Tag | Description | Quantity | Source |
|---|---|---|---|
| `TK-6780-1` | Spent Caustic Storage Tank | 1 | SCOPE_LEDGER SOW-0199 |
| (TBD tag) | Fresh Caustic Storage Tank | 1 | SCOPE_LEDGER SOW-0198 (tag not asserted in available source slices — `TBD`) |

Additional caustic-system equipment named in the design basis (DBM-Deepcut/4-25_Deepcut_DBM.md) and identified as adjacent but NOT explicitly enumerated as part of this Tanks package in the workbook row: `V-6940-1` Pressurized Caustic Drain Drum (DBM-Deepcut). Inclusion of `V-6940-1` in the Tanks package is `TBD` (drum is described in DBM as a separate vessel feeding the spent caustic tank).

## Conditions — Design and Operating

| Item | Spent Caustic Tank (TK-6780-1) | Fresh Caustic Tank | Source |
|---|---|---|---|
| Service | Receives spent caustic from pressurized caustic drain drum via level control | Stores and supplies fresh caustic solution to the caustic treatment unit | SOW-0198; SOW-0199 |
| Nominal Capacity | 400 bbl | 400 bbl | SOW-0199; SOW-0200 |
| Design Pressure | 32 oz (atmospheric); 1.0 oz vacuum | Atmospheric | SOW-0199; SOW-0200 |
| Design Temperature (min) | Minimum ambient | Minimum ambient | SOW-0200 |
| Flow Rate | TBD (workbook scope notes) | TBD (workbook scope notes) | SOW-0200 |
| Heater | Minimum 32.2 degC (90 degF); vendor to design heater | Heated and insulated (per DBM) | SOW-0199 (TK-6780-1); DBM-Deepcut (fresh tank heated/insulated) — `ASSUMPTION` applied to fresh tank from DBM, not workbook |
| Atmospheric Vent / Blanket | Connected to incinerator header; flame-arrestor-protected; LP fuel-gas blanket (per DBM) | LP fuel-gas blanket; NOT connected to VRU header (per DBM, to avoid VRU vapour contamination) | DBM-Deepcut/4-25_Deepcut_DBM.md (caustic tanks subsection) |
| Truck Connection | Truck-out for off-site disposal | Truck-in for fresh caustic supply | DBM-Deepcut/4-25_Deepcut_DBM.md |
| Fresh caustic concentration | n/a | 50 wt% NaOH | DBM-Deepcut/4-25_Deepcut_DBM.md |
| Fresh caustic tank design SG | n/a | 1.75 TBC | DBM-Deepcut/4-25_Deepcut_DBM.md |

## Construction

| Item | Value | Source |
|---|---|---|
| Code of Construction | Modified API 650 | SOW-0199 |
| Materials of Construction | Polymer or other caustic-compatible material (per DBM); detailed selection TBD | DBM-Deepcut/4-25_Deepcut_DBM.md |
| Indoor / Outdoor Installation | Indoors (per DBM, caustic freezing/crystallization risk) | DBM-Deepcut/4-25_Deepcut_DBM.md |
| Insulation Cladding | Stainless steel in caustic exposure areas (per DBM) | DBM-Deepcut/4-25_Deepcut_DBM.md |
| Prohibited Materials | No aluminum in caustic building (per DBM) | DBM-Deepcut/4-25_Deepcut_DBM.md |
| Foundations, mounting, electrical/instrumentation, platforms, staircase | By others (NOT in package vendor scope) | SOW-0200 |

## Scope Items Covered

| SOW Item | Summary |
|---|---|
| `SOW-0197` | Carry the workbook-defined vendor-responsible Mechanical package as a distinct flat project package for WBS 01; Package Vendor owns engineering/design/equipment; EPC Integrator owns facility integration. |
| `SOW-0198` | Supply (1) spent caustic tank and (1) fresh caustic tank; process functions stated. |
| `SOW-0199` | Major included equipment — spent caustic storage tank TK-6780-1 detail. |
| `SOW-0200` | Scope notes and open items — by-others list and design condition placeholders. |

## Objectives Supported

`OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION: package-grouping heuristic via `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`; mapping copied from `_CONTEXT.md` and PACKAGE_REGISTER row).

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- Gate 7 PROJECT_DECOMP snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `DELIVERABLE_REGISTER.csv` row DEL-065-01_scope-of-work
  - `PACKAGE_REGISTER.csv` row PKG-065
  - `SCOPE_LEDGER.csv` rows SOW-0197, SOW-0198, SOW-0199, SOW-0200
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (sections: NGL mercaptan treating unit; spent caustic storage; fresh caustic storage; caustic building materials and safety)
- Workbook Packages row 87 (binary source `_Sources/26020-Packages_Interfaces_4_export.xlsx` — not directly read; values relayed via SCOPE_LEDGER / PACKAGE_REGISTER extraction)
- 26020-Package_Requirements.docx package heading 20 (binary `.docx` — not directly read; values relayed via SCOPE_LEDGER extraction)
