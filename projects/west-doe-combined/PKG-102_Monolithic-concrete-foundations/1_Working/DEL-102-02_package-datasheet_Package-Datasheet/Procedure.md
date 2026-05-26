# Procedure — DEL-102-02 Package Datasheet (PKG-102 Monolithic concrete foundations)

## Purpose

Produce the EPC Package Datasheet artifact for PKG-102 "Monolithic concrete foundations" so that a third-party vendor or discipline-package engineering team can begin detailed engineering and design with full traceability to source materials. The procedure also keeps the four production documents (`Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`) source-grounded and consistent with the Gate-7 decomposition snapshot.

## Prerequisites

- `_CONTEXT.md` present and current.
- `_REFERENCES.md` present with at least one locally accessible source. (At drafting time, the locally accessible source is `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`. The workbook binaries `_Sources/26020-Package_Requirements.docx` and `_Sources/26020-Packages_Interfaces_4_export.xlsx` are referenced but not text-accessible.)
- Gate-7 Final Published snapshot available at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` containing `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- `_DEPENDENCIES.md` declared-upstream/downstream review: both empty at PREPARATION; no declared blockers.
- `_STATUS.md` in a state listed in `ALLOW_OVERWRITE_STATES` (here `OPEN` or `INITIALIZED`).

## Steps

### Step 1 — Establish identity and scope
1. Read `_CONTEXT.md`; transcribe Identity-table values into `Datasheet.md` §Identification.
2. Read `PACKAGE_REGISTER.csv` row PKG-102 and confirm workbook row, WBS, discipline, and source-dependent responsibility caveat.
3. Read `DELIVERABLE_REGISTER.csv` row `DEL-102-02_package-datasheet` and confirm anticipated artifacts.

### Step 2 — Establish governing codes and standards
1. Open `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §"Governing Civil and Structural Basis."
2. Record the governing codes and standards into `Datasheet.md` §Attributes and `Specification.md` §Standards.
3. Mark each standard as "location TBD" because the standards themselves are not part of the local source set; use the DBM "latest edition" directive and flag the edition-pinning decision as Conflict C-02.

### Step 3 — Carry geotechnical and site inputs
1. Open DBM §"Geotechnical and Topographical Assumptions" and §"External Dependencies."
2. Record all geotechnical parameters (bearing capacity, LPILE curves, dynamic criteria, pavement and geotextile inputs) as TBD on `Datasheet.md` §Conditions.
3. Record the corresponding external inputs (geotechnical report, topographical survey, plot plan, compressor dynamic analysis) on `Datasheet.md` §"External Dependencies" and `Specification.md` R6.

### Step 4 — Establish foundation type basis
1. Open DBM §"Piles and Foundations."
2. Transcribe the equipment-vs-foundation table (transformers → precast concrete bearing; compressors → precast concrete block on driven steel piles, oil containment; default → driven steel piles).
3. Record the package-label reconciliation as Conflict C-01 in `Guidance.md` §"Conflict Table."

### Step 5 — Carry interface evidence
1. Open `INTERFACE_REGISTER.csv` and filter for `ParentPackageID = PKG-102`.
2. Record both active interfaces (`IFC-1EDEDC0453` Grading / Site Drainage / Spill Containment; `IFC-8283744B5B` Structural / Foundations / Supports) in `Datasheet.md` §Interfaces.
3. Build the interface requirements matrix per `ARTIFACT_REGISTER.csv` row ART-BA3D34EA23; mark per-interface attribute detail as TBD (Conflict C-04).

### Step 6 — Mark concrete/reinforcement/anchorage TBDs
1. Confirm no DBM source slice provides `f'c`, exposure class, rebar grade, or anchor schedules for PKG-102.
2. Record these as TBD on `Datasheet.md` §Attributes/§Construction and `Specification.md` R4.5; cross-reference Conflict C-03.

### Step 7 — Cross-document consistency sweep (Pass 2)
1. Walk every requirement in `Specification.md` and confirm a corresponding entry exists in `Datasheet.md` and a verification approach is listed in `Specification.md` §Verification.
2. Walk `Guidance.md` Principles/Considerations and confirm each is grounded in a DBM section or a Gate-7 register row.
3. Check terminology (e.g., "precast concrete bearing foundations," "precast concrete block," "driven steel piles," "top-of-pile-cap") for consistent usage across all four documents.
4. Check that every numeric value (1.5%, 1.0%, 0.2%, 0.5%, 3H:1V) is used consistently and only where the DBM applies it.
5. Where inconsistencies cannot be resolved from drafts alone, re-open the relevant DBM section; if still unresolved, add or update an entry in the `Guidance.md` Conflict Table.

### Step 8 — Status update
1. Read `_STATUS.md`.
2. If `Current State` is `OPEN`, run `tools/scaffolding/write_status.sh <DELIVERABLE_PATH> INITIALIZED TASK+four-documents`.
3. If `Current State` is `INITIALIZED` or later, do not modify `_STATUS.md`; record the skip in the run record.

### Step 9 — Run record
1. Write a run record at `_run_records/TASK_RUN_2026-05-25_<HHMM>.md` noting passes executed (P1, P2), sources read, conflicts opened, and status update outcome.

## Verification

| Check | Method |
|---|---|
| All four documents present | Directory listing of `DELIVERABLE_PATH`. |
| Default schema sections present in each document | Heading inspection. |
| All non-trivial values cite a source or are marked TBD | Inspect each Attribute/Condition/Construction row in `Datasheet.md` and each requirement in `Specification.md`. |
| Conflict Table present in `Guidance.md` | Heading inspection. |
| Cross-document terminology and numeric consistency | Manual sweep (Step 7). |
| `_STATUS.md` updated only when previously `OPEN` | Diff against starting state. |
| Run record written | File present under `_run_records/`. |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` — production documents in this folder.
- `_STATUS.md` — updated `OPEN → INITIALIZED` via `tools/scaffolding/write_status.sh` when applicable.
- `_run_records/TASK_RUN_2026-05-25_<HHMM>.md` — run record for this invocation.
- Conflict Table entries C-01 through C-05 in `Guidance.md` — open items routed for human ruling.
