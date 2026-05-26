# Procedure — DEL-040-04 Vendor Engineered Equipment Package (600V Electrical Building 860-1)

> Operational procedure for producing and accepting the engineered 600 V electrical building equipment package for `PKG-040` (Building 860-1, 600V General Area / Tank Farm Electrical Building). The procedure describes steps to **produce** the deliverable artifact (vendor engineering + physical package) and to **prepare it for facility integration**. Detailed production steps internal to the Package Vendor's manufacturing process are out of scope.

## Purpose

Produce a Package-Vendor-engineered 600 V electrical building equipment package that satisfies the EPC Scope of Work (`DEL-040-01`) and Package Datasheet (`DEL-040-02`), passes FAT, and is ready for EPC Integrator integration review (`DEL-040-06`) and turnover (`DEL-040-05`).

## Prerequisites

### Inputs that must exist before vendor engineering begins

- `DEL-040-01 Scope of Work` (EPC-issued) — package scope and boundaries.
- `DEL-040-02 Package Datasheet` (EPC-issued) — voltage, grounding, MCC/UPS/transformer/PLC composition, transfer-switch interface, served-area definition (resolves HRR-040-04-001/-002/-016).
- Accepted electrical studies (load flow, short-circuit, relay coordination, arc-flash) sufficient to confirm or refine vendor design assumptions. (DBM identifies these as required project studies, lines 2895-2903; current state TBD.)
- Project package requirements (`_Sources/26020-Package_Requirements.docx` — location TBD; treat as authoritative once extracted).

### Inputs already available

- Gate 7 `PROJECT_DECOMP` snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- DBM electrical chapter: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Power System, System Voltages, Motor Control, Electrical Buildings, Grounding, 208/120 V, Cables/Raceways, Standby Power, Area Classification, Buildings table, Equipment List).
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`.

### Declared dependencies (per `_DEPENDENCIES.md`)

- Coordination Mode: DECLARED.
- Declared Upstream: none.
- Declared Downstream: none.
- Advisory only: `DEL-040-01` and `DEL-040-02` are logically upstream and should be added to `Dependencies.csv` when `dependency-extract` is run (HRR-040-04-004).

## Steps

### Step 1 — Establish vendor package design basis

1. Confirm `_STATUS.md` is in an overwrite-allowed state before drafting/redrafting the four documents.
2. Consume `DEL-040-01` Scope and `DEL-040-02` Datasheet when issued; in their absence, anchor the design basis to the accessible DBM electrical chapter and the Gate 7 PKG-040 row.
3. Translate accessible DBM constraints (REQ-040-04-001 through REQ-040-04-013) into the vendor design basis.
4. Mark TBD inputs (transformer kVA, bus current, short-circuit, MCC/UPS/transformer quantities, served-area definition for 860-1, 4.16 kV scope question) explicitly with placeholder assumptions and upstream study/datasheet dependency.

### Step 2 — Vendor engineering and design

1. Produce building general arrangement showing MCC, VFD sections, UPS rooms, transformer/panelboard locations, PLC/network rack, HVAC equipment, doors, and exterior lighting/GFI receptacle.
2. Produce HVAC sizing/redundancy documentation demonstrating n+1 capability.
3. Produce 600 V one-line and three-line diagrams including transfer-switch interface to LV standby generator.
4. Produce 600 V MCC schedules with VFD assignments, feeder breakers, SCR-panel feeders, and motor circuit details — sized for the General Area / Tank Farm load list when issued.
5. Produce 208/120 V distribution-transformer and panelboard schedules with solidly grounded neutral arrangement.
6. Produce UPS configuration: 120 V AC and 125 V DC UPS sizing, battery autonomy, distribution panel schedules.
7. Produce protection/metering schematics including ground/resistor-fault detection and alarm-only ground-fault on 600 V.
8. Produce grounding interface drawings (two ground-grid connection points, ground wells, conductor type/conduit, compression connections).
9. Produce cable termination drawings consistent with bottom-entry, ACWU/TECK cable types per cable schedule.
10. Produce plant PLC interface description and network rack arrangement.
11. Produce Fire & Gas interface provisions consistent with the PKG-040 interface row (Fire & Gas / Safety Systems applicability is YES).

### Step 3 — Fabrication / supply

1. Fabricate the prefabricated modular building shell with bottom-entry provisions, n+1 HVAC, lighting, GFI receptacle, and door/transom sizing for largest-equipment removal.
2. Procure/fabricate MCC lineups, VFDs, UPS systems, distribution transformers, panelboards, SCR panels, PLC panels, and network racks per the issued vendor design.
3. Maintain manufacturing records sufficient for turnover (`DEL-040-05`).

### Step 4 — Factory Acceptance Test (FAT)

1. Execute FAT against the vendor-issued FAT plan covering REQ-040-04-001, -003, -004, -005, -006, -007, -008, -012.
2. Witness arrangements per EPC Integrator (typically supports `DEL-040-06`).
3. Capture FAT records for turnover.

### Step 5 — Handoff for installation

1. Package the building and loose equipment for shipment to the site location designated for Building 860-1.
2. Provide installation, operation, and maintenance documentation in support of EPC Integrator installation activities (Construction Work Package `DEL-040-03`).

### Step 6 — Integration support

1. Support EPC Integrator field activities required to verify bottom-entry cabling, ground tie-in at two points, transfer-switch energization, PLC/network connectivity, HVAC commissioning, and Fire & Gas interface validation.
2. Support EPC integration review (`DEL-040-06`).

### Step 7 — Status update

After successful P1/P2 completion of this deliverable's four-document set, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Confirms |
|---|---|
| Vendor design basis review | REQ-040-04-001 / -002 (voltage, grounding, upstream feed) |
| Building general arrangement / HVAC review | REQ-040-04-009 (modular shell, n+1 HVAC, doors, GFI) |
| One-line / three-line review | REQ-040-04-003 / -008 (MCC architecture, transfer-switch interface) |
| 208/120 V distribution review | REQ-040-04-005 (transformer secondary grounding, panel split) |
| UPS sizing / battery autonomy review | REQ-040-04-007 |
| SCR heater-control panel review | REQ-040-04-006 |
| Protection / metering FAT | REQ-040-04-004 (metering, ground/resistor fault, alarm-only) |
| Cable termination compartment review | REQ-040-04-010 (ACWU/TECK accommodation, bottom-entry) |
| Grounding interface review | REQ-040-04-011 (two-point ground-grid connection, ground wells) |
| PLC / network interface review | REQ-040-04-012 |
| Code-compliance declaration and certifications | REQ-040-04-013 |
| Interface verification vs. `DEL-040-02` matrix and `INTERFACE_REGISTER.csv` | REQ-040-04-014 |
| Quantity confirmation via `DEL-040-02` | REQ-040-04-015 / HRR-040-04-002 |
| 860-1 served-area and feed confirmation via `DEL-040-02` | REQ-040-04-016 / HRR-040-04-001 |

## Records

- Vendor package design basis (issued, revision-controlled).
- Engineered drawing set (general arrangement, one-line, three-line, schematics, terminations, grounding, interfaces, HVAC, lighting).
- Datasheet set for building, MCC, VFDs, UPS, transformers, panels, SCR panels, PLC/network panels.
- FAT plan and signed FAT records.
- Code-compliance declarations and certifications.
- Installation/operation/maintenance manuals.
- `_STATUS.md` state history.
- `_run_records/TASK_RUN_*.md`.

These records are aggregated and submitted via `DEL-040-05 Vendor Document Turnover Package` and reviewed via `DEL-040-06 EPC Vendor Package Review and Acceptance`.
