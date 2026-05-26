# Datasheet — DEL-062-01 Scope of Work (PKG-062 NGL Loading Pumps Building)

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-062-01_scope-of-work` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 420 |
| Deliverable Name | Scope of Work | `_CONTEXT.md` |
| Parent Package ID | `PKG-062` | `_CONTEXT.md` |
| Parent Package Name | NGL Loading Pumps Building | `_CONTEXT.md` |
| Workbook Row | 76 | `_CONTEXT.md`; `SCOPE_LEDGER.csv` SOW-0153 |
| Discipline | Mechanical | `_CONTEXT.md` |
| Deliverable Type | EPC Scope of Work | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Decomposition Basis | GATE-07_Final_Published_2026-05-24 | `_REFERENCES.md` |
| Source Document | `26020-Package_Requirements.docx` package heading 16 | `_CONTEXT.md`; `SCOPE_LEDGER.csv` |
| Cross-cutting DBM | 4-25 (Deepcut) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2549, 2610 |

## Attributes — Package Identity

| Field | Value | Source |
|---|---|---|
| Package Function | Pumps to move LPG product from storage to LPG Truck Loading | SCOPE_LEDGER SOW-0154 |
| Building | Self-framing building to be erected at site | SCOPE_LEDGER SOW-0155 |
| Equipment Count | 4 identical pumps configured in parallel | SCOPE_LEDGER SOW-0154, SOW-0155 |
| Equipment Tags | P-9510-1, P-9520-1, P-9530-1, P-9540-1 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2610; SCOPE_LEDGER SOW-0155 ("P9510/20/30/40-1") |
| Equipment Type | Rotary vane pumps (Blackmer Model LGL4B) | SCOPE_LEDGER SOW-0154, SOW-0155 |

## Conditions — Process / Operating

| Field | Value | Source |
|---|---|---|
| Service | LPG transfer from storage to truck-loading | SCOPE_LEDGER SOW-0154 |
| Capacity per pump | 68 m3/hr @ 345 kPad (300 USGPM @ 50 psid) TBC TDH | SCOPE_LEDGER SOW-0155, SOW-0156 |
| Operating Conditions | TBC — refer to capacity/site conditions | SCOPE_LEDGER SOW-0156 |
| Design Conditions | TBC — refer to capacity/site conditions | SCOPE_LEDGER SOW-0156 |
| Driver | Electric motor, 575 V / 3 Ph / 60 Hz | SCOPE_LEDGER SOW-0156 |
| Motor Sizing Basis | Inlet stabilizer composition density at -40 C start-up | SCOPE_LEDGER SOW-0156 |
| Local Control | H-O-A or On-Off switch (local) | SCOPE_LEDGER SOW-0156 |
| Electrical Feed | Motors fed from 600 V MCC | SCOPE_LEDGER SOW-0156 |

## Construction — Package Boundary

| Field | Value | Source |
|---|---|---|
| In-package construction | Pump skids; self-framing building erected at site | SCOPE_LEDGER SOW-0155 |
| By Others (excluded) | DCS integration, foundations, electrical supply to MCC | SCOPE_LEDGER SOW-0156 |
| Vendor responsibility | Engineering, design, and equipment supply (Package Vendor) | SCOPE_LEDGER SOW-0153 |
| EPC responsibility | Facility integration of the vendor package | SCOPE_LEDGER SOW-0153 |

## Coverage — Scope Items and Objectives

| Field | Value | Source |
|---|---|---|
| Covered SOW items | SOW-0153, SOW-0154, SOW-0155, SOW-0156 | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supported objectives (ASSUMPTION, package-grouping heuristic) | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md`; `OBJECTIVE_SCOPE_MAP.csv` rows 91-94, 318-321 |

ASSUMPTION: objective list is associated by package-grouping heuristic (`OBJECTIVE_ASSOCIATION_MODE = PACKAGE_HEURISTIC`); not yet confirmed by human ruling.

## References

- `_CONTEXT.md`, `_REFERENCES.md` (deliverable-local)
- `26020-Package_Requirements.docx` package heading 16 — source heading, slice not yet locally extracted; location TBD beyond the SCOPE_LEDGER excerpt
- `SCOPE_LEDGER.csv` rows SOW-0153 through SOW-0156 (GATE-07 snapshot)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 73, 2549, 2610
- `DELIVERABLE_REGISTER.csv` row 420 (GATE-07 snapshot)
