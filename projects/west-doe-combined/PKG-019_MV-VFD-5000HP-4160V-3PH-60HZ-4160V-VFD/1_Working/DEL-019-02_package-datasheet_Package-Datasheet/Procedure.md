# Procedure: DEL-019-02_package-datasheet

## Purpose

Produce and maintain the EPC Integrator Package Datasheet for `PKG-019` such that it can be handed to a third-party vendor or discipline package engineering function as a source-grounded basis, with all gaps explicitly marked `TBD` and all source-grounded values traceable.

## Prerequisites

- `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` present in this deliverable folder (verified during Pass 1 read).
- Accepted Gate 7 PROJECT_DECOMP snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Read access to:
  - `PACKAGE_REGISTER.csv` (row 21 / `PKG-019`)
  - `DELIVERABLE_REGISTER.csv` (row 97 / `DEL-019-02_package-datasheet`)
  - `ARTIFACT_REGISTER.csv` (PKG-019 / DEL-019-02 rows)
  - `INTERFACE_REGISTER.csv` (PKG-019 rows)
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (motor / MV bus / SCA-001 VE slices)
- Declared upstream dependencies: none.
- Declared downstream dependencies: none.

## Steps

1. **Resolve identity.** Populate `Datasheet.md` Identification table from `_CONTEXT.md` and `PACKAGE_REGISTER.csv` row `PKG-019`. Carry the workbook name verbatim.
2. **Anchor driven-motor electrical basis.** From `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 324-326 and 533, record the NEMA MG1 motor basis (voltage, hp/kW, enclosure, insulation, speed, inverter duty, starting VFD per SCA-001 VE #34).
3. **Anchor MV source bus.** From DBM lines 744 and 752-754, record the 13.8 kV → 4.16 kV, 12 MVA transformer and 4160V MCC with EtherNet to plant PLC.
4. **Capture capacitor/harmonic constraint.** From DBM line 756, record SCA-001 VE #37 and mark detailed harmonic mitigation as a detailed-design item.
5. **Carry interface facts.** For each `INTERFACE_REGISTER.csv` row attributed to `PKG-019`, add a row to the Datasheet Conditions table citing the `IFC-*` ID.
6. **Mark gaps.** Any vendor-engineering value not supported by an accessible source slice (cooling, enclosure rating, filter topology, footprint, weights, package-requirements mapping) is recorded `TBD` with the source-gap note.
7. **Surface conflicts.** Record:
   - PKG-018 vs. PKG-019 duplication (CONF-019-02-A in `Guidance.md`).
   - Workbook nameplate vs. DBM motor basis (CONF-019-02-B).
   - Missing `26020-Package_Requirements.docx` slice (CONF-019-02-C).
8. **Generate Specification.** Map each captured fact to a `REQ-019-02-*` row in `Specification.md`, with verification approaches.
9. **Generate Guidance.** Record purpose, principles, considerations, trade-offs, examples, and the Conflict Table.
10. **Cross-reference consistency sweep (Pass 2).** Verify terminology and values are consistent across `Datasheet.md`, `Specification.md`, `Guidance.md`, and this `Procedure.md`; verify each `REQ-019-02-*` has both a Datasheet anchor and a Verification entry.
11. **Update status.** If `_STATUS.md` Current State is `OPEN`, transition to `INITIALIZED` and append a history line.

## Verification

| Check | Method | Pass criterion |
|---|---|---|
| Identity matches authoritative registers | Compare Datasheet Identification table to `PACKAGE_REGISTER.csv` row 21 and `DELIVERABLE_REGISTER.csv` row 97. | All fields match verbatim or are explicitly noted. |
| Driven-motor electrical basis grounded | Trace Attributes row to DBM lines 324-326, 533. | Source line range cited; no values exceed source. |
| MV source bus grounded | Trace Attributes row to DBM lines 744, 752-754. | Source line range cited. |
| SCA-001 VE #37 captured | Inspect Attributes / Conditions for the capacitor-bank constraint. | Constraint scope limited to MCC-8200 as stated in source. |
| All six PKG-019 interface rows present | Compare Conditions table to `INTERFACE_REGISTER.csv` PKG-019 rows. | Six rows, each with an `IFC-*` ID. |
| Conflicts surfaced | Inspect `Guidance.md` Conflict Table. | CONF-019-02-A, -B, -C present with proposed authority and TBD ruling. |
| `_STATUS.md` only modified per safe rule | Inspect `_STATUS.md` history. | OPEN → INITIALIZED transition or no change. |
| No writes outside deliverable folder | Inspect run record. | Zero out-of-scope writes. |

## Records

- `Datasheet.md` (this run)
- `Specification.md` (this run)
- `Guidance.md` (this run; includes Conflict Table)
- `Procedure.md` (this run)
- `_STATUS.md` (updated OPEN → INITIALIZED)
- `_run_records/TASK_RUN_2026-05-24_<HHMM>.md` (this run record)
