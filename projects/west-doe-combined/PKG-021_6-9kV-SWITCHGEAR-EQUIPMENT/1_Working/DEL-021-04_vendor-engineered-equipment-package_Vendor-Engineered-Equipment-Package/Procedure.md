# Procedure — DEL-021-04 Vendor Engineered Equipment Package (6.9 kV Switchgear Equipment)

> Operational procedure for producing and accepting the engineered 6.9 kV switchgear equipment package. The procedure describes steps to **produce** the deliverable artifact (vendor engineering + physical package) and to **prepare it for facility integration**. Detailed production steps internal to the Package Vendor's manufacturing process are out of scope.

## Purpose

Produce a Package-Vendor-engineered 6.9 kV switchgear equipment package that satisfies the EPC Scope of Work (`DEL-021-01`) and Package Datasheet (`DEL-021-02`), passes FAT, and is ready for EPC Integrator integration review (`DEL-021-06`) and turnover (`DEL-021-05`).

## Prerequisites

### Inputs that must exist before vendor engineering begins

- `DEL-021-01 Scope of Work` (EPC-issued) — package scope and boundaries.
- `DEL-021-02 Package Datasheet` (EPC-issued) — voltage, grounding, interface, sizing inputs.
- Accepted electrical studies (load flow, short-circuit, relay coordination, arc-flash) sufficient to confirm or refine vendor design assumptions. (DBM identifies these studies as required; current state TBD.)
- Project package requirements (`_Sources/26020-Package_Requirements.docx` — location TBD; treat as authoritative once extracted).

### Inputs already available

- Gate 7 `PROJECT_DECOMP` snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- DBM electrical chapter: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Power System, System Voltages, Motor Control, Grounding, Electrical Buildings sections).

### Declared dependencies (per `_DEPENDENCIES.md`)

- Coordination Mode: DECLARED.
- Declared Upstream: none.
- Declared Downstream: none.
- Advisory only: `DEL-021-01` and `DEL-021-02` are logically upstream and should be added to `Dependencies.csv` when `dependency-extract` is run (HRR).

## Steps

### Step 1 — Establish vendor package design basis

1. Consume `DEL-021-01` Scope and `DEL-021-02` Datasheet.
2. Translate accessible DBM constraints (REQ-021-04-001 through REQ-021-04-009) into the vendor design basis.
3. Mark TBD inputs (bus current, short-circuit, BIL, enclosure type) explicitly with placeholder assumptions and the upstream study dependency.

### Step 2 — Vendor engineering and design

1. Produce one-line and three-line diagrams.
2. Produce protection and control schematics covering: motor protection relay coordination with `MCC-8200`; bus-level protection (TBD); ground-fault protection consistent with the 100 A/10 s tripping system basis.
3. Produce termination, grounding, and interface drawings (bottom cable entry; 8 kV TECK cable terminations; ground bus interface to facility ground grid).
4. Produce the Ethernet/PLC interface description.
5. Confirm absence of PFCC on the `MCC-8200` synchronous-transfer bus in design documentation.

### Step 3 — Fabrication / supply

1. Fabricate or procure the switchgear lineup(s) and accessory equipment per the issued vendor design.
2. Maintain manufacturing records sufficient for turnover (`DEL-021-05`).

### Step 4 — Factory Acceptance Test (FAT)

1. Execute FAT against the vendor-issued FAT plan covering REQ-021-04-001, -002, -004, -005, -006, -008.
2. Witness arrangements per EPC Integrator (typically supports `DEL-021-06`).
3. Capture FAT records for turnover.

### Step 5 — Handoff for installation

1. Package equipment for shipment to the Building 820-1 6.9 kV Inlet/Sales Compressor Electrical Building site.
2. Provide installation, operation, and maintenance documentation in support of the EPC Integrator's installation activities (Construction Work Package `DEL-021-03`).

### Step 6 — Integration support

1. Support EPC Integrator field activities required to verify bottom-entry cabling, ground tie-in, and PLC interface energization.
2. Support EPC integration review (`DEL-021-06`).

## Verification

| Check | Confirms |
|---|---|
| Vendor design basis review | REQ-021-04-001/002/003 (voltage, grounding, sizing basis) |
| One-line / three-line review | REQ-021-04-004/005 (feeder positions, PFCC absence) |
| Termination compartment review | REQ-021-04-008 (8 kV TECK termination compatibility) |
| Protection/PLC FAT | REQ-021-04-006 (protection, metering, Ethernet interface) |
| Environmental/dimensional check vs. Building 820-1 | REQ-021-04-007 (indoor MV-building installation envelope) |
| Code-compliance declaration and certifications | REQ-021-04-009 (governing codes) |
| Interface verification vs. `DEL-021-02` interface matrix | REQ-021-04-010 |
| Quantity confirmation via `DEL-021-02` | REQ-021-04-011 / HRR-021-04-001 |

## Records

- Vendor package design basis (issued, revision-controlled).
- Engineered drawing set (one-line, three-line, schematics, terminations, grounding, interfaces).
- Datasheet set for switchgear lineup and integrated devices.
- FAT plan and signed FAT records.
- Code-compliance declarations and certifications.
- Installation/operation/maintenance manuals.

These records are aggregated and submitted via `DEL-021-05 Vendor Document Turnover Package` and reviewed via `DEL-021-06 EPC Vendor Package Review and Acceptance`.
