# Procedure: DEL-051-01_scope-of-work — Scope of Work

> Operational procedure to **produce** the EPC Scope of Work for PKG-051 Process Heat Medium Unit. The deliverable is a planning/scope artifact; this procedure describes how to assemble it, not how to operate the heat medium system.

## Purpose

Produce a source-grounded, conflict-aware Scope of Work for PKG-051 that satisfies the requirements stated in `Specification.md` and the guidance in `Guidance.md`, and is fit for issuance to the Package Vendor and for use by DEL-051-02 through DEL-051-06.

## Prerequisites

### Inputs (must be available before starting)

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` for this deliverable.
- Decomposition snapshot at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — specifically `PACKAGE_REGISTER.csv` (row PKG-051), `DELIVERABLE_REGISTER.csv` (rows DEL-051-01..06), `SCOPE_LEDGER.csv` (rows SOW-0165..0168), `OBJECTIVE_REGISTER.csv`.
- Local source slices: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (`## Heat Medium Basis` lines 1945-2002, `## Utilities and Support Systems Basis` heat medium row line 1832, energy-balance rows lines 1884, 2242-2243, 2264, 2293, 2357-2359, 2435).
- Workbook source `26020-Package_Requirements.docx` package heading 6 — currently not locally readable in markdown form; relevant content is captured via `SCOPE_LEDGER.csv` SOW-0165..0168. Direct clause-level rereads are `location TBD`.
- The four-document deliverable templates as expressed in this folder: `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`.

### Roles

- **Drafter:** Type 2 TASK shell running the `four-documents` skill (this run).
- **Reviewer:** EPC Integrator engineer (human) to resolve Conflict Table items C-01..C-05.
- **Approver:** Authorized EPC Integrator role (human; agents may not approve per K-AUTH-1).

### Required references

- See `_REFERENCES.md`. The Gate 7 final published snapshot is the authoritative decomposition basis. The DBM-Deepcut markdown is the authoritative facility-side source slice.

## Steps

1. **Read context.** Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` and confirm deliverable identity, scope items, and objective associations.
2. **Locate authoritative source slices.** Open `PACKAGE_REGISTER.csv` row PKG-051; `SCOPE_LEDGER.csv` rows SOW-0165..0168; `OBJECTIVE_REGISTER.csv` rows for the listed objectives; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` `## Heat Medium Basis` slice.
3. **Extract package identity and function.** Populate `Datasheet.md` Identification and Attributes from the workbook row and DBM slice. Cite source for every row.
4. **Build tagged equipment list.** From SOW-0166/0167 (vendor scope) and DBM duty table (downstream users). Add the heater tag `H-5170-1` and the user-side exchanger tags from the DBM table.
5. **Record design and operating envelope.** Populate Datasheet Conditions with DBM-sourced values. For each conflicting parameter (max bulk temp; expansion tank pressure), record both sources and mark `TBD pending human ruling`.
6. **State responsibility split.** Use the `PACKAGE_REGISTER.csv` responsibility model text verbatim or summarized; do not invent additional vendor or EPC obligations.
7. **Author Specification requirements.** Convert datasheet entries into normative `REQ-*` statements with verification approaches. Each requirement cites its source slice.
8. **Author Guidance principles, considerations, trade-offs, examples.** Surface the architecture conflict, fluid temperature conflict, expansion-tank pressure conflict, vendor identity conflict, and pop-tank scope boundary as Conflict Table rows C-01..C-05.
9. **Cross-check consistency (Pass 2).** Verify Datasheet ↔ Specification ↔ Guidance ↔ Procedure terminology, equipment tags, numeric values, and unit usage. Fix what can be fixed from drafts; mark `TBD` and route to Conflict Table what cannot.
10. **Carry open items forward.** Confirm REQ-17 lists every open `TBD`/`TBC` that downstream deliverables (DEL-051-02..06) must consume.
11. **Update `_STATUS.md`.** If current state is `OPEN`, run the safe status update to `INITIALIZED` (or modify `_STATUS.md` in place when the helper script is not invoked). Do not regress state.
12. **Write run record.** Persist the run record at `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` capturing inputs, resolved state, tools used, outputs, missing items, and needs-human-ruling.

## Verification

| Step | Verification |
|---|---|
| 2 | Each cited row/slice resolves to an existing file under the snapshot or `_Sources` tree. |
| 3, 4, 5 | Each Datasheet row has a Source column populated with file + section (or `location TBD`). |
| 6 | Responsibility statements match `PACKAGE_REGISTER.csv` PKG-051 wording; no expansion or substitution. |
| 7 | Every `REQ-*` has a verification approach and a cited source. |
| 8 | Conflict Table contains rows for every unresolved cross-source disagreement; no parameter is silently chosen. |
| 9 | Same equipment tag (e.g., `H-5170-1`) is written identically across all four documents; numeric values use the same units. |
| 10 | REQ-17 open-item list matches the union of `TBC`/`TBD` entries in DBM `## Heat Medium Basis` and any new conflicts from this run. |
| 11 | `_STATUS.md` reflects `INITIALIZED` only when prior state was `OPEN`; otherwise unchanged. |
| 12 | Run record exists, `run-status` is set to its final value, and YAML frontmatter is complete. |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` (this file) in `{DELIVERABLE_PATH}`.
- `_STATUS.md` state transition entry (when applicable).
- `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` — durable run record.
- Conflict Table in `Guidance.md` — durable record of items requiring human ruling (C-01..C-05).
- Open-item carry-forward list in `Specification.md` REQ-17 — feeds DEL-051-02 datasheet population, DEL-051-03 work-package planning, and DEL-051-06 EPC review checklist.
