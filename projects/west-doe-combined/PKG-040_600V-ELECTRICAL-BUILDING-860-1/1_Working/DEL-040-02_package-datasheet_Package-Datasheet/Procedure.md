# Procedure — DEL-040-02 Package Datasheet (PKG-040 600V Electrical Building 860-1)

> Operational procedure to **produce** the Package Datasheet artifact for PKG-040.
> The artifact itself (`Datasheet.md`) is the primary deliverable; this procedure is how the EPC Integrator authors and issues it.

## Purpose

Produce a source-grounded, vendor-issuable Package Datasheet for the 600V Electrical Building (860-1), with all requirements per `Specification.md` satisfied or explicitly marked `TBD` with a named owner.

## Prerequisites

### Inputs (must be available)

- `_CONTEXT.md` (this deliverable folder) — identity, scope, anticipated artifacts.
- `_REFERENCES.md` — pointers to authoritative materials.
- `_DEPENDENCIES.md` — declared upstream/downstream (currently none declared).
- Gate 7 PROJECT_DECOMP snapshot at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`, specifically:
  - `DELIVERABLE_REGISTER.csv` (DEL-040-02 row).
  - `PACKAGE_REGISTER.csv` (row 42).
  - `INTERFACE_REGISTER.csv` (rows 262–273 for PKG-040).
  - `OBJECTIVE_DELIVERABLE_MAP.csv`.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- `Specification.md` (this folder) — the normative requirements list this procedure must satisfy.
- `Guidance.md` (this folder) — Conflict Table; carry rulings into the datasheet as they are made.

### Tools / environment

- Plain-text Markdown editor.
- Access to the read-only Gate 7 snapshot path.
- No deterministic tooling is required for this skill's primary work.

### Skills / roles

- EPC Integrator electrical engineer or delegate (author).
- EPC Integrator package manager (reviewer).
- Project standards owner (CSA/CEC/OGAOM compliance reviewer).

## Steps

### Step 1 — Initialize the datasheet shell

1. Open `Datasheet.md` (already present from the four-documents Pass 1 run).
2. Confirm the Identification table fields all carry a source cite or `TBD`.
3. Confirm the Anticipated Artifacts list matches `_CONTEXT.md`.

### Step 2 — Populate Design Conditions from the DBMs

For each requirement R3 through R8, R13, R14, R15 in `Specification.md`:
1. Open the cited source slice in the relevant DBM.
2. Quote the operative clause verbatim into the datasheet condition row.
3. Cite source file path and section.
4. If the slice does not exist locally, mark the value `TBD — location TBD in source <X>`.

### Step 3 — Populate Power System Context

1. From `4-25_Deepcut_DBM.md` Power System and System Voltages, populate voltage classes the building must support (R9).
2. From `4-25_Deepcut_DBM.md` Standby Power and `3-25_Comp_and_Liquids_DBM.md` 600V MCC and Standby Power, populate the standby-power tie-in description; mark generator count, ratings, and load-shedding as `TBD` (R11).
3. From `4-25_Deepcut_DBM.md` Grounding and Bonding, populate grounding requirements (R10).

### Step 4 — Populate Interface Matrix

1. Read `INTERFACE_REGISTER.csv` rows 262–273.
2. Create one datasheet row per interface ID (12 rows total) (R12).
3. For each row, fill the technical envelope where source material is available; otherwise mark `TBD` with the downstream task expected to resolve it (typically detailed engineering or vendor proposal).
4. Do not merge rows.

### Step 5 — Populate Standards section

1. From `4-25_Deepcut_DBM.md` Governing Codes, carry the standards and authorities list into the datasheet Standards section (R3 standards / R10 grounding / general compliance).
2. For each standard where a specific clause is referenced in the DBM, carry the clause reference (e.g., OGAOM Sec. 9.6.15 for fired-heater spacing).
3. For standards where no clause is referenced, mark clause-level `location TBD`.

### Step 6 — Populate TBD register

1. Sweep the populated datasheet for every `TBD`.
2. For each, assign a named owner (Package Vendor, EPC Integrator electrical, EPC Integrator civil, Tourmaline Oil Corp., etc.) and the expected resolution task (vendor proposal, detailed engineering, owner ruling, study).
3. Confirm no value has been invented (R16).

### Step 7 — Cross-document consistency check

1. Compare terminology (e.g., "600V" vs "600 V", "MCC" vs "motor control center") with `Specification.md` and `Guidance.md`; normalize.
2. Confirm every requirement in `Specification.md` is reflected in either a populated datasheet row or a `TBD` with owner.
3. Update `Guidance.md` Conflict Table if new conflicts emerge during population.

### Step 8 — Internal review

1. EPC Integrator package manager reviews the datasheet against `Specification.md` requirements R1–R16.
2. Project standards owner reviews the Standards section.
3. Any disagreement that cannot be resolved from sources is added to the `Guidance.md` Conflict Table and surfaced for human ruling — not silently resolved.

### Step 9 — Issue for vendor handoff

1. Move the deliverable through `_STATUS.md` per project state machine (this skill only auto-progresses OPEN → INITIALIZED; subsequent states are human-authored).
2. Package the datasheet plus its cited source slices into the vendor handoff bundle.
3. Record issue in the package vendor's document register (consumed by DEL-040-05).

## Verification

| Check | Pass criterion |
|---|---|
| All Identification fields populated or TBD with cite | 100% rows. |
| Every `Specification.md` requirement R1–R16 reflected in datasheet | 16/16 traceable. |
| 12 interface-matrix rows present | One row per `INTERFACE_REGISTER.csv` PKG-040 row. |
| No invented values | Audit shows every non-TBD value has a source cite. |
| Conflict Table updated | All discrepancies surfaced; none silently reconciled. |
| Standards section cites CSA C22.1-21 CEC | Required by `4-25_Deepcut_DBM.md` Governing Codes. |
| Building heater clause carried as 600 V, 3 phase | Required by `4-25_Deepcut_DBM.md`. |
| HVAC n+1 clause carried | Required by `4-25_Deepcut_DBM.md` Electrical Buildings. |
| Bottom-cable-entry and pile-elevation clauses carried | Required by `4-25_Deepcut_DBM.md` Electrical Buildings. |
| Building color (Cloverdale #2593) carried | Required by `4-25_Deepcut_DBM.md` Buildings color schedule. |

## Records

The procedure shall produce / update:

- `Datasheet.md` — the artifact itself, populated to vendor-issue level.
- Updated `Guidance.md` Conflict Table (when new conflicts surface).
- Run record under `_run_records/TASK_RUN_<timestamp>.md` for each authoring or revision pass (this run record covers the initial four-documents Pass 1/2 generation).
- `_STATUS.md` history entry when state advances (safe update only).
- Vendor handoff bundle index (location set by project document control; not part of this folder).
