# Procedure — DEL-078-02 Package Datasheet (Pig Receivers (Inlet) 4-25)

Operational procedure for producing and maintaining the PKG-078 Package Datasheet. The procedure covers both producing the datasheet artifact (EPC Integrator) and using it as the basis for vendor engineering handoff.

## Purpose

Provide a repeatable, source-grounded procedure for assembling the Package Datasheet for PKG-078 Pig Receivers (Inlet) 4-25 such that the resulting artifact satisfies the requirements in `Specification.md` and aligns with the basis in `Datasheet.md` and `Guidance.md`.

## Prerequisites

- Deliverable-local files present: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`.
- Access to Gate 7 final published PROJECT_DECOMP snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` including:
  - `PACKAGE_REGISTER.csv` (row 78)
  - `DELIVERABLE_REGISTER.csv` (rows 432-437)
  - `SCOPE_LEDGER.csv` (rows 162-165: `SOW-0161` through `SOW-0164`)
  - `INTERFACE_REGISTER.csv` (rows 647-656 for PKG-078)
  - `OBJECTIVE_DELIVERABLE_MAP.csv`
- Access to `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (facility basis SEC-04).
- Declared dependencies: none declared at PREPARATION (`_DEPENDENCIES.md`); upstream constraints come solely from the decomposition snapshot.
- Underlying Word source `26020-Package_Requirements.docx` package heading 31 is not directly read in this run; SCOPE_LEDGER extraction is treated as the locally accessible source slice.

## Steps

1. **Confirm scope.** Read `_CONTEXT.md`. Confirm DeliverableID `DEL-078-02_package-datasheet`, ParentPackageID `PKG-078`, package name "Pig Receivers (Inlet) 4-25". Confirm discipline (Mechanical) and ResponsibleParty (EPC Integrator).
2. **Pull package row.** Open `PACKAGE_REGISTER.csv` row 78. Record PackageTag (`26020-01-PT-35-001 - Pig Receivers (Inlet)`), process function, declared interface types, and authoritative companion register row note.
3. **Pull scope ledger rows.** Open `SCOPE_LEDGER.csv` rows for `SOW-0161` (carry decision), `SOW-0162` (basic scope), `SOW-0163` (major included equipment), `SOW-0164` (scope notes, capacity, operating/design conditions). Extract attributes, conditions, and `By Others` allocations verbatim where they are values; rephrase only narrative wrappers.
4. **Pull interface rows.** Open `INTERFACE_REGISTER.csv`, filter by PKG-078. Capture all ten rows (`IFC-49A2026DAA` through `IFC-65EDB92369`). For each, record InterfaceID, interface type, and a counterparty-boundary description grounded in `SOW-016*` text where possible.
5. **Pull facility basis context.** Read `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-04 (Inlet, Separation, Stabilization basis) and SEC-03 (Inlet Composition and Contaminants). Capture: plant inlet design H2S (1.0 mol%), CO2 (0.7 mol%), inlet water (4 lbH2O/MMSCF design), lease-boundary basis (1100 psig, 5-35 deg C, TBC), hydrate management policy.
6. **Draft `Datasheet.md`.** Populate Identification, Attributes, Conditions, Construction, Interfaces, Scope Coverage, Supported Objectives, References sections. Each non-trivial value carries a Source column; unknowns are `TBD`; inferences are `ASSUMPTION`.
7. **Draft `Specification.md`.** Populate Scope (in/out), Requirements (REQ-DS-001 to REQ-DS-017), Standards (with ASSUMPTION labels where clause-level text is not accessible), Verification (mapping each REQ to evidence), Documentation (anticipated artifacts and downstream consumers).
8. **Draft `Guidance.md`.** Populate Purpose, Principles, Considerations, Trade-offs, Examples. Add a Conflict Table; record "none detected" when Pass 2 finds no conflicts.
9. **Draft `Procedure.md`** (this document).
10. **Run Pass 2 cross-reference consistency check.** Walk the matrix in `Specification.md`'s Verification section, confirm every requirement points to a populated section in `Datasheet.md`. Confirm terminology consistency: "pig receiver", "HIPPS", "ESDV", "HP flare", "sour service", "MAOP", "MAWP" used identically across documents. Confirm numeric values (225 MMSCFD, 653-725 psig, MAOP 1300, MAWP 1440, -40/+35 deg C, 1.0 mol% H2S) match across documents.
11. **Resolve or record conflicts.** When Pass 2 finds a conflict, prefer `TBD` over guess and record in the `Guidance.md` Conflict Table.
12. **Update `_STATUS.md` (safe update).** If current state is `OPEN`, invoke `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`. Do not regress state.
13. **Write the run record.** Persist `_run_records/TASK_RUN_{YYYY-MM-DD}_{HHmm}.md` with the prescribed YAML frontmatter and markdown body; finalize `run-status` at completion.

## Verification

| Check | Method |
|---|---|
| All four documents present in `{DELIVERABLE_PATH}` | Directory listing. |
| Default schema sections present in each document | Section-heading walk. |
| Every non-trivial value in `Datasheet.md` carries a Source column entry or `TBD`/`ASSUMPTION` | Manual walk of Datasheet tables. |
| All ten PKG-078 interfaces present in Interfaces matrix | Count = 10; IDs match `INTERFACE_REGISTER.csv` rows 647-656. |
| All four `SOW-016*` items referenced in `Datasheet.md` Scope Coverage | Text search. |
| Cross-document numeric and terminology consistency | Pass 2 walk per Step 10. |
| `_STATUS.md` updated only when safe (state was `OPEN`) | Inspect `_STATUS.md` and run record. |
| No edits outside `{DELIVERABLE_PATH}` | Git diff / shell observation in run record. |

## Records

Each invocation produces:

- Updated `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`.
- Updated `_STATUS.md` (only when state advancement is safe: `OPEN` to `INITIALIZED`).
- New run record at `_run_records/TASK_RUN_{YYYY-MM-DD}_{HHmm}.md` with input echo, resolved state, tools used, outputs produced, missing items, dependency notes, and applied changes.

Records to preserve over the deliverable lifecycle:

- All run records (immutable after completion).
- Successive versions of the four documents (managed via Git history at the repo level).
- Any human ruling that resolves an item from the `Guidance.md` Conflict Table (when populated).
