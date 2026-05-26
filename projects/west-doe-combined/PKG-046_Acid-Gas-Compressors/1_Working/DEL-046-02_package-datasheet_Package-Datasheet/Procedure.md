# Procedure — PKG-046 Acid Gas Compressors (Package Datasheet)

> Operational procedure to **produce** the PKG-046 Package Datasheet deliverable (EPC handoff). Source authority: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-05; `_CONTEXT.md`; `_REFERENCES.md`; decomposition snapshot at GATE-07.

## Purpose

Define a repeatable procedure for assembling, verifying, and issuing the PKG-046 Package Datasheet (this deliverable's four documents plus interface-matrix cross-references), so that a third-party vendor or discipline package engineering team can begin design work with traceable, source-grounded inputs.

## Prerequisites

### Declared upstream dependencies
- None declared during PREPARATION (per `_DEPENDENCIES.md`). The deliverable currently consumes the upstream decomposition snapshot directly. TBD: explicit upstream deliverable edges (e.g., amine regenerator scope, VRU scope, electrical scope, plant control system) should be declared in `_DEPENDENCIES.md` before vendor RFQ.

### Required references (must be locally accessible to proceed)
- `_CONTEXT.md` — identity, parent package, discipline, scope items, supports-objectives, source reference.
- `_REFERENCES.md` — authoritative references and shared source root.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — SEC-05 "Compression and Acid Gas Handling Basis" (primary source).
- Decomposition snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`: `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`.

### Required references (text extraction needed; currently TBD)
- `_Sources/26020-Package_Requirements.docx` — extract text for clause-level EPC requirements.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — extract PKG-046 interface rows.

## Steps

### Step 1 — Confirm scope and identity
1. Read `_CONTEXT.md`; confirm DeliverableID `DEL-046-02_package-datasheet`, ParentPackageID `PKG-046`, discipline Mechanical, type EPC Package Datasheet.
2. Confirm covers-scope items `SOW-0047`-`SOW-0050` and supports-objectives list. Flag any deviation in `MEMORY.md` (if produced by a later task).

### Step 2 — Resolve authoritative source slices
1. Open DBM-Deepcut SEC-05 sections: "Acid Gas Injection Compression Basis", "Acid Gas Composition Basis", "Acid Gas Compressor Design Conditions", "Acid Gas Disposal Well Interface", "Controls and Protection Basis", "Assumptions, TBDs, and Design Development Requirements".
2. For each acid-gas compressor parameter (configuration, flow, composition, MAWP, temperatures, driver, scrubbers, coolers, recycle, blowdown, sequencing, metering, dehydration), record the source slice (file + section).
3. Extract `_Sources/26020-Package_Requirements.docx` text (TBD; binary). Until extracted, record affected requirements as `location TBD` and treat 26020 clause references as ASSUMPTION.

### Step 3 — Populate the Datasheet
1. Fill `Datasheet.md` Identification from `_CONTEXT.md`.
2. Fill Attributes (flow, composition, pressure/temperature, driver, stage water content) from DBM-Deepcut SEC-05 tables, citing each table.
3. Fill Conditions (service, inlet/outlet origin, mercaptan handling, lubricant disposition, sweet-gas purge) from SEC-05.
4. Fill Construction (compressor frame, scrubbers, aftercoolers, blowdown, recycle, packing drains/vents, metering, composition monitoring, sequencing) from SEC-05.
5. Mark missing values explicitly as `TBD`. Do not invent values.

### Step 4 — Derive the Specification
1. Convert each Datasheet attribute that imposes a vendor obligation into a numbered R-46-* requirement.
2. List standards. Where standards are not enumerated in accessible source slices, list as ASSUMPTION with `location TBD`.
3. Map each requirement to a verification activity (vendor data review, calc review, FAT, SAT, hydrotest, hazardous-area review).
4. List required documentation (anticipated artifacts from `_CONTEXT.md` plus industry-standard vendor deliverables, the latter labelled ASSUMPTION).

### Step 5 — Capture rationale in Guidance
1. State purpose (per `_CONTEXT.md`).
2. State principles (source primacy, leakage-point minimization, sequencing automation, recycle-first capacity control, disposal interface fidelity).
3. State considerations (configuration choice, composition envelope, methane floor, mercaptan, dehydration option, aftercooler freeze protection, injection pipeline NPS assumption).
4. Tabulate trade-offs.
5. Populate the Conflict Table for every internal inconsistency, missing value, or TBD that requires human ruling (frame KBT/6 vs KBK/6, 5th-stage discharge 1,200 vs 1,500 psig, stages 1-2 MAWP inversion, configuration 2x100%+spare vs 3x50%, dehydration trigger, disposal-well pressures, 02-25 facility modifications, 26020 text extraction).

### Step 6 — Cross-document consistency sweep (Pass 2)
1. Datasheet ↔ Specification: every Specification requirement traces back to a Datasheet attribute or Construction item; every Datasheet attribute that materially affects vendor work appears as a numbered requirement.
2. Specification ↔ Guidance: every requirement that involves judgement, exclusion, or trade-off has a Guidance principle, consideration, or trade-off entry.
3. Specification ↔ Procedure: every requirement has a verification entry and a corresponding produce-the-deliverable step (this document).
4. Terminology and values: confirm consistent use of "acid gas compressor", "package", stage numbering, pressure/temperature units, and composition mol% values across all four files.
5. Where the sweep surfaces an irreconcilable issue, add a Conflict Table row in `Guidance.md`.

### Step 7 — Interface matrix cross-reference (when extracted)
1. Extract PKG-046 rows from `INTERFACE_REGISTER.csv` and `26020-Packages_Interfaces_4_export.xlsx` (TBD; binary xlsx).
2. Reconcile against the Interfaces table in `Datasheet.md`; update Datasheet citations from `location TBD` to specific interface IDs.

### Step 8 — Status update
1. Read `_STATUS.md`. If `Current State` is `OPEN`, set state to `INITIALIZED` using `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`.
2. If `Current State` is not `OPEN`, do not modify `_STATUS.md`; record skip in the run record.

### Step 9 — Issue the run record
1. Write `_run_records/TASK_RUN_<timestamp>.md` with run-status `SUCCESS` (or `FAILED` / `FAILED_INPUTS` per actual outcome), tool usage, outputs produced, missing items, needs human ruling, dependency notes.

## Verification

- All four documents (`Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`) exist in `{DELIVERABLE_PATH}` with default schema sections present.
- Every non-trivial value/requirement cites a source (`SourcePath` + `SectionRef`) or is marked `TBD` / `ASSUMPTION` with reason.
- Terminology and numeric values consistent across the four documents.
- Conflict Table in `Guidance.md` records every internal inconsistency and missing value requiring human ruling.
- `_STATUS.md` updated only when permitted by the safe-update rule; no state regression.
- `_run_records/TASK_RUN_<timestamp>.md` exists and lists tools used, outputs, missing items, and rulings needed.
- No files modified outside `{DELIVERABLE_PATH}`.

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` (this set) — issued package datasheet kit.
- `_STATUS.md` history entries — state transitions.
- `_run_records/TASK_RUN_<timestamp>.md` — auditable provenance for this run.
- Future: `Dependencies.csv` (from `dependency-extract`), `_SEMANTIC_LENSING.md` (from `lens-register`), Pass-3 enrichment run record.
