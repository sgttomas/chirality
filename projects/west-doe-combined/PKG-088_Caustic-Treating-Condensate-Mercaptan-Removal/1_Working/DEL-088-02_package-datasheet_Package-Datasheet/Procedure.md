# Procedure — DEL-088-02 Package Datasheet (PKG-088 Caustic Treating)

`epistemic-status: DRAFT (Pass 1+2)`

This Procedure describes how the EPC Integrator produces, issues, and maintains the PKG-088 Package Datasheet artifact. Vendor and operations procedures for the physical package belong with the vendor deliverable (`DEL-088-04_vendor-engineered-equipment-package`, if produced).

## Purpose

Produce a source-grounded EPC Package Datasheet that the package vendor can use as the authoritative technical handoff for engineering, design, and supply of the non-regenerative caustic treating package serving the 03-25 Liquids Hub.

## Prerequisites

- Gate 7 PROJECT_DECOMP snapshot accepted: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`. [Source: `_REFERENCES.md`]
- Deliverable-local minimum viable fileset present (`_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md` placeholder). [Source: `_REFERENCES.md`]
- Source set available under `_Sources/`:
  - `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (locally readable; primary source for treating duty)
  - `26020-Package_Requirements.docx` package heading 41 (binary; ASSUMPTION not locally readable in markdown form for this run)
  - `26020-Packages_Interfaces_4_export.xlsx` (binary; ASSUMPTION not locally readable in plain text for this run)
- No upstream declared dependencies blocking; `_DEPENDENCIES.md` declares none upstream/downstream as of PREPARATION.

## Steps

1. **Read context.** Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and the PKG-088 / DEL-088-02 rows of the Gate 7 registers.
2. **Read source slices.** Read the "Condensate Mercaptan Treating", "Products and Downstream Routing", "Instrument Air", and "Fuel Gas" sections of `3-25_Comp_and_Liquids_DBM.md`. Resolve any further package-specific text from `26020-Package_Requirements.docx` heading 41 when it becomes locally readable.
3. **Populate Datasheet identification.** From `_CONTEXT.md` and PACKAGE_REGISTER.csv (tag `26020-02-PT-27-001`, vendor reference go-by, discipline, WBS).
4. **Populate Datasheet attributes/conditions/construction.** Use only values explicitly present in source slices. Mark `TBC`/`TBD` where source defers.
5. **Derive Specification requirements.** Convert each anchored source value into a requirement clause with explicit `[Source: …]` citation. Use SHALL only where the source is normative.
6. **List interfaces.** Cross-check the PKG-088 "Applicable interface types" list against vendor and EPC interface registers. Carry interface evidence here per Gate 5 anchor convention (DELIVERABLE_REGISTER.csv DEL-088-02 notes).
7. **Draft Guidance.** Record purpose, principles, considerations, and trade-offs grounded in the DBM and PACKAGE_REGISTER.
8. **Draft Procedure (this file).** Capture the issuance procedure and the verification / records hooks.
9. **Cross-document consistency sweep (Pass 2).** Compare entity names, numeric values (20,000 bbl/d; 30/50 ppmw S; 50 wt% NaOH; 214 SCFM TBC), and equipment list across all four documents. Open the source slice again if any value cannot be confirmed from drafts alone.
10. **Open `TBD`s and Conflict Table.** Where source is absent or contradictory, record `TBD` (or open a Conflict Table row in `Guidance.md`). Do not invent values.
11. **Update `_STATUS.md`.** From `OPEN` → `INITIALIZED` once Pass 1/2 is complete. (Safe transition only; no regression.)
12. **Write run record.** Persist `_run_records/TASK_RUN_<timestamp>.md`.

## Verification

- All four documents exist and contain default schema sections.
- Every non-trivial value in `Datasheet.md` and `Specification.md` cites a source (or carries `TBD` / `location TBD` with reason).
- Terminology and numeric values are consistent across the four documents.
- `_STATUS.md` reflects only the safe `OPEN → INITIALIZED` transition.
- No edits outside `{DELIVERABLE_PATH}`.

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` — production artifacts.
- `_STATUS.md` — state transition recorded.
- `_run_records/TASK_RUN_2026-05-25_0511.md` — run report for this Pass 1/2 invocation.
