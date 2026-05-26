# Datasheet — DEL-062-04 Vendor Engineered Equipment Package (NGL Loading Pumps Building)

> Descriptive datasheet for the Package Vendor's engineered NGL Loading Pumps Building equipment package supplied under PKG-062. Values cite the GATE-07 PROJECT_DECOMP snapshot, which extracts the workbook Packages row 76 and `26020-Package_Requirements.docx` package heading 16. Where vendor-engineered values are required and the source does not state them, fields are marked `TBD`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-062-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable Name | Vendor Engineered Equipment Package | `_CONTEXT.md` |
| Parent Package | `PKG-062` — NGL Loading Pumps Building | `_CONTEXT.md` |
| Parent Workbook ID | 62 | `_CONTEXT.md` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Deliverable Type | Vendor Package Production Unit | `_CONTEXT.md` |
| Responsible Party | Package Vendor (engineering / design / equipment) with EPC Integrator integration review | `_CONTEXT.md`; OBJ-004 |
| Covers Scope Items | SOW-0153, SOW-0154, SOW-0155, SOW-0156 | `_CONTEXT.md`; SCOPE_LEDGER.csv |
| Supports Objectives | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md` (PACKAGE_HEURISTIC, ASSUMPTION) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Process function | Move LPG product from storage to LPG Truck Loading | SOW-0154 |
| Pump count | 4 identical pumps in parallel | SOW-0154; SOW-0155 |
| Pump tag numbers | P9510-1, P9520-1, P9530-1, P9540-1 | SOW-0155 |
| Pump manufacturer | Blackmer | SOW-0154; SOW-0155 |
| Pump model | LGL4B | SOW-0154; SOW-0155 |
| Pump type | Rotary vane | SOW-0154; SOW-0155 |
| Configuration | Parallel | SOW-0154 |
| Building | Self-framing building, erected at site | SOW-0155 |

## Conditions (Capacity / Design)

| Parameter | Value | Source |
|---|---|---|
| Capacity (per pump, flow) | 68 m³/hr (300 USGPM) | SOW-0155; SOW-0156 |
| Capacity (per pump, differential) | 345 kPad (50 psid) — TBC TDH | SOW-0155; SOW-0156 |
| Total package flow | TBD (4 pumps in parallel; configuration-dependent) | derivation; vendor to confirm |
| Driver | Electric motor, 575 V / 3-phase / 60 Hz | SOW-0156 |
| Motor sizing basis | Inlet stabilizer composition density at −40 °C start-up condition | SOW-0156 |
| Local control | Hand-Off-Auto (H-O-A) or On-Off switch (local) | SOW-0156 |
| Motor power supply | Fed from 600 V MCC (by others) | SOW-0156 |
| Operating conditions | TBC — see capacity/site conditions | SOW-0156 |
| Design conditions | TBC — see capacity/site conditions | SOW-0156 |
| Service fluid | LPG product (from storage to truck loading) | SOW-0154 |
| Site / ambient design temperature | TBD (start-up condition cited as −40 °C; full ambient envelope not stated in available source slice) | SOW-0156 |

## Construction

| Item | Value | Source |
|---|---|---|
| Building type | Self-framing building erected at site | SOW-0155 |
| Building dimensions / layout | TBD (vendor-engineered) | — |
| Pump skid / baseplate | TBD (vendor-engineered) | — |
| Materials of construction | TBD (vendor to specify per LPG service and sour-service applicability) | OBJ-009 (sour-service constraint to be confirmed for this package) |
| Winterization / heat tracing | TBD (vendor-engineered; informed by −40 °C start-up requirement) | SOW-0156; OBJ-010 |
| HVAC / ventilation | TBD (vendor-engineered) | OBJ-007 |
| Electrical area classification | TBD (vendor to confirm for LPG service) | — |
| Lighting | TBD (vendor-engineered) | OBJ-005 |

## Package Boundary — Excluded ("By Others")

| Item | Source |
|---|---|
| DCS integration | SOW-0156 |
| Foundations | SOW-0156 |
| Electrical supply to MCC | SOW-0156 |

## References

- `_CONTEXT.md` (deliverable identity)
- GATE-07 PROJECT_DECOMP snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `DELIVERABLE_REGISTER.csv` row `DEL-062-04_vendor-engineered-equipment-package`
  - `SCOPE_LEDGER.csv` rows `SOW-0153`, `SOW-0154`, `SOW-0155`, `SOW-0156`
  - `OBJECTIVE_REGISTER.csv` rows `OBJ-001`, `OBJ-003`..`OBJ-010`
- Upstream workbook source (cited, not directly readable as text in PREPARATION set): Workbook Packages row 76; `26020-Package_Requirements.docx` package heading 16 — location TBD for direct read.
