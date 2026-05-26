# Procedure: DEL-079-02 — Package Datasheet (Instrument Air Building, PKG-079)

## Purpose

This procedure covers both:
1. **Producing** the Package Datasheet artifact (the four-document kit in this deliverable folder), and
2. **Using** the Package Datasheet as the EPC-Integrator-to-vendor handoff basis during procurement, vendor engineering, FAT, and site integration.

It is operational and intentionally aligned to the Specification's requirements and verification mapping.

## Prerequisites

- Read the four documents in this deliverable: `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`.
- Locally accessible source material:
  - `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx` — section `26020-01-PT-39-001`.
  - `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx` — sheet `Packages` row 69.
- Decomposition snapshot: PROJECT_DECOMP Gate 7 final published at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Declared upstream dependencies: **none** declared during PREPARATION (`_DEPENDENCIES.md`). Confirm before relying on this assumption.
- Original RFQ basis (`26020-01-PT-RFQ-39-001_Instr_Air_Bldg_R1.docx`): **not locally accessible** — see Guidance CT-04.

## Steps

### Part A — Produce / maintain the datasheet

1. **Initialize from PREPARATION minimum-viable fileset** (already done: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md` present).
2. **Read source slices** for package `26020-01-PT-39-001` from the Requirements doc and row 69 of the Interfaces xlsx.
3. **Populate `Datasheet.md`** Identification, Attributes, Conditions, Construction, and Interface Summary fields from the source slices. Mark vendor-deferred and missing values as `TBD`; never invent.
4. **Populate `Specification.md`** Scope, Requirements (R1-R9), Standards, Verification, and Documentation from source slices. Trace each requirement to a source paragraph or table.
5. **Populate `Guidance.md`** with rationale, considerations, trade-offs, and the Conflict Table for any source contradictions (CT-01..CT-04 initial set).
6. **Populate `Procedure.md`** (this file) with production and operational steps.
7. **Cross-document consistency sweep** (Pass 2):
   - Equipment/values consistent between Datasheet and Specification.
   - Each Specification requirement has a Verification row.
   - Terminology consistent (`compressor`, `dryer`, `PSV`, `dew point`, etc.).
8. **Update `_STATUS.md`** via `tools/scaffolding/write_status.sh` only when state is `OPEN` (safe `OPEN -> INITIALIZED`).
9. **Write run record** at `_run_records/TASK_RUN_<timestamp>.md`.

### Part B — Use the datasheet for vendor handoff

10. **Issue RFQ package** to vendor including this datasheet, the Specification, and the Vendor Engineering Deliverables manifest (`Datasheet.md § Vendor Engineering Deliverables`).
11. **Vendor proposal review:**
    - Confirm compressor count/rating (2 × 1113 SCFM @ 861 kPag).
    - Confirm motor selection against R3 (HP per CT-02 ruling, 600 V / 3 PH / 60 Hz, TEFC, non-classified, soft starter or VFD-ready, anti-condensation heater).
    - Confirm desiccant dryer 100% with leave; confirm receiver configuration (1 dry receiver or 2 × 50%).
    - Confirm PSV set pressure per CT-03 ruling.
12. **Interface coordination:** for each applicable interface in R7.1, confirm the counterpart discipline/package has accepted the interface (Utility Piping, Drains, Electrical Power, Grounding, Lighting, I&C, Building HVAC, Fire & Gas, Maintenance Access, Structural).
13. **Engineering deliverable tracking:** maintain a deliverable register that mirrors `Datasheet.md § Vendor Engineering Deliverables`; track each item to issued/approved.
14. **FAT execution:**
    - Witness capacity test at 1113 SCFM @ 861 kPag (R2.1).
    - Witness dew point test at -73.3 °C @ 1000 kPag (R6.1).
    - Witness PSV set verification (R4.5 — subject to CT-03 ruling).
    - Capture results in `MEC-021` / `MEC-022`.
15. **Site integration (battery-limit walkdown):**
    - Confirm by-others scope (R9): shipping, piles, tie-in piping, electrical termination, mounting platform, stairs.
    - Verify interface terminations against `ELE-028` and `INS-008`.
16. **Energization and SAT:** execute `ELE-029` and record per `ELE-030`.

## Verification

- **Production-side verification (Part A):**
  - Datasheet, Specification, Guidance, Procedure all exist in the deliverable folder.
  - Every non-trivial value in Datasheet/Specification cites a source (file + section) or is marked `TBD`.
  - Conflict Table contains an entry for every unresolved source inconsistency.
  - `_STATUS.md` updated only per safe-update rules.
  - Run record persisted under `_run_records/`.
- **Use-side verification (Part B):**
  - Vendor proposal closes all `TBD` items via vendor data sheets.
  - Interface register row 69 marked closed for each applicable counterpart.
  - FAT witness records on file (MEC-021/022, ELE-029/030).
  - Battery-limit walkdown sign-off recorded.

## Records

- This deliverable folder (`DEL-079-02_package-datasheet_Package-Datasheet/`) and its `_run_records/`.
- Vendor Document Index (`PRQ-009`) and final Vendor Data Book (`PRQ-016` / `MEC-023`).
- FAT records: `MEC-021`, `MEC-022`, `ELE-029`, `ELE-030`.
- Interface coordination evidence: revised entries in `26020-Packages_Interfaces_*.xlsx` row 69 and the consumer-side interface acceptances.
- Pressure equipment registration (`REG-022`) and fire/building code compliance (`REG-021`) records.
