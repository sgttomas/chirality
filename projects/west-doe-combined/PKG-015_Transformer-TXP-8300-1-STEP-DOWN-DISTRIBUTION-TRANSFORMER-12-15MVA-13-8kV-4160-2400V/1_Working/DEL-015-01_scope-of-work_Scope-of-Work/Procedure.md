# Procedure — DEL-015-01 Scope of Work (PKG-015)

> Operational procedure for the EPC Integrator to **produce** the Scope of Work artifact for PKG-015 Transformer TXP-8300-1.
> This procedure is a drafting/handoff procedure, not a field execution procedure. Field execution belongs to DEL-015-03 (Construction Work Package).

## Purpose

Produce a Gate-5-ready EPC Scope of Work that satisfies all `REQ-015-01-*` items in `Specification.md`, anchored in the accessible source set (PACKAGE_REGISTER.csv, DELIVERABLE_REGISTER.csv, 3-25 DBM), with all unsupported items explicitly carried as `TBD` or `ASSUMPTION`.

## Prerequisites

| Prerequisite | Source |
|---|---|
| `_CONTEXT.md` present and accurate | deliverable-local truth set |
| `_REFERENCES.md` present with Gate 7 snapshot pointers | deliverable-local truth set |
| `_DEPENDENCIES.md` reviewed (declared upstream/downstream: none) | deliverable-local truth set |
| Gate 7 PACKAGE_REGISTER.csv accessible | `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` |
| Gate 7 DELIVERABLE_REGISTER.csv accessible | same |
| 3-25 Comp_and_Liquids DBM accessible | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| Workbook row 17 (package row) | referenced by PACKAGE_REGISTER.csv; raw workbook export not separately read |

## Steps

1. **Read deliverable-local truth set.** Read `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md` (placeholder). Confirm `Current State = OPEN` or `INITIALIZED`.
2. **Resolve decomposition rows.** Locate PKG-015 in `PACKAGE_REGISTER.csv` and DEL-015-01 in `DELIVERABLE_REGISTER.csv`. Confirm `Source Reference = Workbook Packages row 17`.
3. **Read source slices.** Read DBM sections:
   - System Voltages (L728–L736)
   - Incoming Power and Transformers (L738–L750)
   - Area Classification (L720–L726)
   - Standby Power notes (L505, L762)
   - General Transformer policy (L2947–L2949, 4-25 DBM context)
4. **Populate identity.** Fill the Identification table in the SoW from PACKAGE_REGISTER.csv columns verbatim; do not paraphrase the package title.
5. **Draft package function.** Write the package-function paragraph using DBM L740, L744, L754 as source anchors. Cite each non-trivial fact.
6. **Declare vendor/EPC boundary.** Copy the boundary statement verbatim from PACKAGE_REGISTER.csv `Vendor_EPC_Boundary`.
7. **Enumerate interfaces.** For each of the seven applicable interface types in PACKAGE_REGISTER.csv `Interface_Types`, write a one-line EPC integration responsibility statement. Mark detailed parameters `TBD`.
8. **Carry source gaps as TBD/ASSUMPTION.** For 2,400 V service, dual MVA rating (cooling class), impedance/BIL/taps/vector group, package-bundled auxiliary tag list, secondary containment requirements — emit `TBD` or `ASSUMPTION` per Specification REQ-015-01-11.
9. **Cross-reference sibling deliverables.** Reference (do not duplicate) DEL-015-02, DEL-015-03, DEL-015-05, DEL-015-06 by ID.
10. **Author Conflict Table entries.** Populate the Guidance Conflict Table with any newly discovered source conflicts (currently CFL-015-01-01..03).
11. **Cross-document consistency sweep.** Confirm identity values, voltage values, source citations, and terminology are identical across Datasheet, Specification, Guidance, Procedure.
12. **Run safe `_STATUS.md` update.** If `Current State = OPEN`, set state to `INITIALIZED` and append a History line. If state is already `INITIALIZED` or later, do not regress.
13. **Write run record.** Write `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHMM>.md` per AGENT_TASK contract.

## Verification

| Verification | Method |
|---|---|
| All `REQ-015-01-*` satisfied | Map each REQ to a section/paragraph in the SoW set. |
| All non-trivial claims cite a source | Reviewer pass; unsourced quantitative claim = defect. |
| Vendor/EPC boundary verbatim from register | Diff against PACKAGE_REGISTER.csv `Vendor_EPC_Boundary`. |
| Seven interface types each addressed | Checklist against PACKAGE_REGISTER.csv `Interface_Types`. |
| No design data invented | Reviewer audit; gaps appear as `TBD` or `ASSUMPTION`. |
| Cross-document consistency | Read all four documents end-to-end; reconcile any terminology drift. |
| Status update safe | If state was not `OPEN`, no edit was made. |

## Records

- The four documents (`Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`) in the deliverable folder.
- `_STATUS.md` updated (or not, per safe-update rule) with appended History line.
- `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHMM>.md`.
- Conflict Table entries in `Guidance.md` flagged for human ruling (CFL-015-01-01..03).
