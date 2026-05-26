# Procedure — DEL-079-01 Scope of Work: Instrument Air Building (PKG-079)

This procedure covers how to **produce** and maintain the EPC Scope of Work deliverable for PKG-079 (Instrument Air Building). Operating/using the physical instrument air package is owned by the Package Vendor (DEL-079-04) and EPC operations; it is not authored here. (Source: skill interpretation rule; DELIVERABLE_REGISTER.csv responsibility entries.)

## Purpose

Define the repeatable steps that the EPC Integrator follows to author, validate, and maintain this Scope of Work, so that the package identity, responsibility split, equipment basis, design conditions, interfaces, and "By Others" scope assignments are carried correctly into every downstream PKG-079 deliverable.

## Prerequisites

### Authoritative source materials (required)
- Workbook row 69 — accessible via PACKAGE_REGISTER.csv, SCOPE_LEDGER.csv (SOW-0131..0134), and INTERFACE_REGISTER.csv (PKG-079 rows). (Source: GATE-07_Final_Published_2026-05-24 snapshot.)
- 26020-Package_Requirements.docx — package heading 32 "Basic scope", "Major included equipment", "Scope notes and open items". Locally accessible at `_Sources/26020-Package_Requirements.docx`. (Verified via _Sources listing.)
- DELIVERABLE_REGISTER.csv rows DEL-079-01 .. DEL-079-06 for PKG-079.
- OBJECTIVE_REGISTER.csv rows OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010.

### Deliverable-local truth set (required)
- `_CONTEXT.md` (identity, scope, anticipated artifacts).
- `_REFERENCES.md` (decomposition basis and source pointers).
- `_DEPENDENCIES.md` (currently no declared upstream/downstream — DECLARED mode).
- `_STATUS.md` (must be `OPEN` or `INITIALIZED` to permit overwrite per ALLOW_OVERWRITE_STATES).

### Declared upstream dependencies
- None declared during PREPARATION. (Source: `_DEPENDENCIES.md`.)

## Steps

1. **Load the deliverable-local truth set.** Read `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`. Confirm `Current State` is in ALLOW_OVERWRITE_STATES (OPEN, INITIALIZED). If not, stop with `SKIPPED_PROTECT_HUMAN_WORK`.

2. **Load the decomposition slices for PKG-079.** From the Gate 7 snapshot, extract:
   - `PACKAGE_REGISTER.csv` row PKG-079 (identity, responsibility model, applicable interface types).
   - `SCOPE_LEDGER.csv` rows SOW-0131, SOW-0132, SOW-0133, SOW-0134 (basic scope; major equipment; scope notes / By Others / pressures / dewpoint / capacity / design temperatures).
   - `DELIVERABLE_REGISTER.csv` rows DEL-079-01 .. DEL-079-06 (sibling deliverable identities).
   - `INTERFACE_REGISTER.csv` rows for PKG-079 (10 interface IDs).
   - `OBJECTIVE_REGISTER.csv` rows OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (treated as directional context per package-grouping heuristic, ASSUMPTION-level).

3. **Re-read the source document slice when authoring or revising design conditions.** Open `_Sources/26020-Package_Requirements.docx` package heading 32 and reconcile each numeric value (pressures, dewpoint, SCFM, temperature, HP, voltage, equipment count) against SCOPE_LEDGER.csv SOW-0133/SOW-0134 before publishing changes to Datasheet or Specification. In this pass the document slice was not re-opened directly; values transcribed from SCOPE_LEDGER.csv only — record this in run-record and treat as a candidate Pass 3 reread.

4. **Author the Datasheet.** Populate Identification from `_CONTEXT.md` and PACKAGE_REGISTER.csv; Attributes (function, basic scope, equipment list) from SOW-0131/SOW-0132/SOW-0133; Conditions from SOW-0133/SOW-0134; Construction (responsibility split, By Others, interfaces, exclusions) from PACKAGE_REGISTER.csv, SOW-0134, INTERFACE_REGISTER.csv. Preserve `TBD` and ASSUMPTION labels where source defers.

5. **Author the Specification.** Convert SOW-0132/0133/0134 statements into numbered requirements R1..R10 with each R cell carrying the source citation. Map each requirement to a Verification entry V1..V10. List standards/codes only when stated in source; mark others as `Location TBD`.

6. **Author the Guidance.** Capture the principles (vendor/EPC split, source-of-truth rule, vendor-sizing-vs-invention, interfaces-as-obligations) and considerations (coupled pressures/dewpoint, dryer margin framing, motor area-classification check, broad objective coverage), then trade-offs and examples. Add a Conflict Table only when an unresolved cross-document conflict is found.

7. **Author the Procedure.** Document the steps above plus verification and records.

8. **Cross-document consistency sweep (Pass 2).** Verify:
   - Equipment counts identical across Datasheet (Attributes), Specification (R2/R3), Guidance (Trade-offs).
   - Numeric values identical (1113 SCFM @ 861 kPag; PSV 948 kPag; max system 1034 kPag; min 551 kPag; shutdown 482 kPag; max discharge/shutdown 1000 kPag; dewpoint -73.3 °C @ 1000 kPag; -40 °C to 38 °C; 250 HP / 200-250 HP / 600V/3PH/60Hz).
   - Interface list (10 types) identical between Datasheet Construction table and Specification R8.
   - Responsibility split wording consistent between Datasheet, Specification R1, and Guidance Principle 1.
   - Terminology stable: "Instrument Air Building", "Package Vendor", "EPC Integrator", "PKG-079".

9. **Update `_STATUS.md` safely.** If current state is `OPEN`, write `INITIALIZED` with provenance `TASK+four-documents`. If current state is already `INITIALIZED` or higher, skip and report.

10. **Persist run record.** Write `_run_records/TASK_RUN_<YYYY-MM-DD_HHmm>.md` with input echo, resolved state, outputs, missing items, and applied changes.

## Verification

| ID | Verifies | Method |
|---|---|---|
| PV1 | Step 1 | `_STATUS.md` read confirms eligible state. |
| PV2 | Step 2 | All listed decomposition slice files referenced exist under the Gate 7 snapshot folder. |
| PV3 | Step 3 | Each numeric value in Datasheet/Specification cites SOW-0133 or SOW-0134; deferred re-reads recorded in run record. |
| PV4 | Steps 4-7 | All four files exist with required default schema sections and source-grounded content; TBD/ASSUMPTION used where source defers. |
| PV5 | Step 8 | Cross-document numeric and terminology check passes; no Conflict Table needed, or Conflict Table populated with explicit ruling rows. |
| PV6 | Step 9 | `_STATUS.md` shows `INITIALIZED` with the four-documents provenance line (or skip is logged). |
| PV7 | Step 10 | `_run_records/TASK_RUN_*.md` exists with `run-status: SUCCESS` (or appropriate failure mode). |

## Records

- The four artifact files: `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`.
- Updated `_STATUS.md` carrying the state transition.
- Run record `_run_records/TASK_RUN_2026-05-24_2338.md` for this pass (P1_P2). Subsequent Pass 3 (semantic lensing enrichment) will produce its own run record after `_SEMANTIC_LENSING.md` is generated by the `lens-register` skill.
- Candidate Pass 3 worklist items already identifiable now (recorded here as TBD-flag for the next pass):
  - Re-open `_Sources/26020-Package_Requirements.docx` package heading 32 to reconcile every numeric value directly against the source text.
  - Re-open `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-08 (Utilities and Support Systems Basis), SEC-12 (Electrical Basis), SEC-13 (Controls), SEC-14 (Instrumented Protection / Fire & Gas), SEC-15 (Regulatory, Codes, Standards) to populate the Standards table.
  - Open `_Sources/26020-Packages_Interfaces_4_export.xlsx` to confirm interface count and any per-interface notes for PKG-079.
  - Locate `Bid Docs/Budgetary/26020-01-PT-RFQ-39-001_Instr_Air_Bldg_R1.docx` if accessible; reconcile RFQ-level statements.
