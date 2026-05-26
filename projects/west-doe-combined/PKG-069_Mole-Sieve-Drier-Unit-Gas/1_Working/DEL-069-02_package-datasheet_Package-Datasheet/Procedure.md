# Procedure — DEL-069-02 Package Datasheet (Mole Sieve Drier Unit, Gas)

## Purpose

This procedure describes how the EPC Integrator **produces** the PKG-069 Package Datasheet from authoritative source materials and registers, and how the resulting datasheet is **used** to support vendor handoff and downstream EPC deliverables (DEL-069-03 through DEL-069-06).

## Prerequisites

- Deliverable-local context files present: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`.
- Accepted upstream decomposition snapshot available: GATE-07 Final Published (2026-05-24).
- Locally accessible authoritative source:
  - `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (SEC-06 governs the gas mole-sieve unit).
- Registers in the GATE-07 snapshot folder: `PACKAGE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`.
- Declared dependencies (per `_DEPENDENCIES.md`): none declared at PREPARATION; treat extracted summaries as context only.

## Steps (Produce the Datasheet)

1. **Read deliverable-local context.** Open `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`. Confirm `Current State` is in `ALLOW_OVERWRITE_STATES` before drafting.
2. **Read the source slice.** Open DBM-Deepcut `4-25_Deepcut_DBM.md` and read SEC-06 "Molecular-Sieve Dehydration and Mercury Removal Basis" in full, including subsections: Process Description, Molecular-Sieve Design Values, Bed and Regeneration Basis, Equipment/Controls/Protection, and Open Items and Assumptions. Also read §Process Controls and Protective Functions (molecular-sieve row), §Interfaces (relevant rows), and §Assumptions/TBDs.
3. **Read registers.** Extract the PKG-069 row from `PACKAGE_REGISTER.csv`; all PKG-069 rows from `INTERFACE_REGISTER.csv` (12 expected); all PKG-069 rows from `OBJECTIVE_DELIVERABLE_MAP.csv`.
4. **Draft the Datasheet** with five default sections (Identification, Attributes, Conditions, Construction, References). Populate each value with its source citation. Use `TBD` where the source explicitly defers; use `ASSUMPTION` where inference was unavoidable.
5. **Draft the Specification** with five default sections (Scope, Requirements, Standards, Verification, Documentation). Map each requirement to source. Where standards are conventional but clause-level text is not accessible, mark `ASSUMPTION` with `location TBD`.
6. **Draft the Guidance** with five default sections (Purpose, Principles, Considerations, Trade-offs, Examples). Build the Conflict Table for unresolved discrepancies (regeneration heater temperature, regeneration compressor differential, Gate-6 packaging note, outlet-water "required" value).
7. **Draft the Procedure** (this document) with five default sections (Purpose, Prerequisites, Steps, Verification, Records).
8. **Cross-document consistency sweep.** Verify the same numeric values, equipment names, and TBD/ASSUMPTION labels appear consistently across all four documents.
9. **Update `_STATUS.md`** via the safe transition `OPEN → INITIALIZED` only when the four documents are present and Pass 1/2 completed.
10. **Write the run record** `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` per AGENT_TASK contract.

## Steps (Use the Datasheet)

1. **Vendor RFQ packaging.** Issue the Datasheet, Specification, and Guidance (with Conflict Table) as the technical body of the RFQ to candidate Package Vendors.
2. **Interface matrix handoff.** Provide the 12 interface-type rows from `INTERFACE_REGISTER.csv` as the interface-requirements matrix; collect vendor responses on each.
3. **Conflict resolution.** Drive each Conflict Table row to human ruling before vendor design freeze; record ruling in `MEMORY.md` and update the Conflict Table.
4. **Downstream deliverable hand-offs.**
   - DEL-069-03 Construction Work Package: consumes Construction and Interfaces sections.
   - DEL-069-04 Vendor Engineered Equipment Package: consumes Requirements (R-EQP-01..15) and Verification.
   - DEL-069-05 Vendor Document Turnover: consumes Documentation table.
   - DEL-069-06 EPC Vendor Package Review and Acceptance: consumes all four documents plus the resolved Conflict Table.

## Verification

| Check | How verified |
|---|---|
| Four documents exist | File listing of deliverable folder |
| Default sections present in each | Heading scan of each document |
| Every non-trivial value cites a source (file + section/line) | Reviewer scan against Datasheet and Specification |
| 12 interface types from `INTERFACE_REGISTER.csv` are all present | Cross-check against register |
| Open items in DBM SEC-06 §Assumptions/TBDs are reflected as TBD/ASSUMPTION in Datasheet | Side-by-side compare |
| Conflict Table includes at least: regen heater temperature, regen compressor differential, Gate-6 packaging note, outlet-water "required" value | Guidance review |
| `_STATUS.md` transitioned `OPEN → INITIALIZED` only (no regression) | Status file diff |
| Run record present in `_run_records/` | File listing |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` — the four-document kit.
- `_STATUS.md` — updated to `INITIALIZED` via `tools/scaffolding/write_status.sh` operationally (or by safe in-file edit when the helper is unavailable).
- `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` — auditable run record per AGENT_TASK.
- Conflict Table entries (in `Guidance.md`) requiring human ruling.
