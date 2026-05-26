# Procedure — DEL-049-01 Scope of Work (Sales Gas Booster Compressor)

> Operational procedure for producing the EPC Integrator Scope of Work artifact for PKG-049.
> Pass 1/Pass 2 draft. Steps requiring judgment that the locally accessible DBM source slice does not warrant are marked `TBD`.

## Purpose

Produce the EPC Integrator Scope of Work artifact for PKG-049 Sales Gas Booster Compressor, satisfying the requirements in `Specification.md` and remaining consistent with `Datasheet.md` and `Guidance.md`. The procedure describes how to author, integrate, review, and freeze this deliverable rather than how to operate the physical compressor (which is governed by the Vendor package, DEL-049-04).

## Prerequisites

- Accepted upstream decomposition snapshot: GATE-07_Final_Published_2026-05-24 PROJECT_DECOMP (per `_REFERENCES.md`).
- Locally accessible authoritative source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (especially §SEC-02 Plant Overview and §SEC-05 Compression and Acid Gas Handling Basis).
- Deliverable-local metadata: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` present and current.
- Sibling PKG-049 deliverable identifiers known: DEL-049-02 Package Datasheet, DEL-049-03 Construction Work Package, DEL-049-04 Vendor Engineered Equipment Package, DEL-049-05 Vendor Document Turnover Package, DEL-049-06 EPC Vendor Package Review and Acceptance.
- No declared upstream dependencies blocking initialization (per `_DEPENDENCIES.md`).
- Optional but recommended: extracted source slices for Workbook Packages row 80 and `26020-Package_Requirements.docx` package heading 4 (currently NOT locally accessible; carry as `location TBD`).

## Steps

1. **Read the deliverable-local truth set.** Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`, and `_SEMANTIC.md`. Confirm `_STATUS.md` is in an overwrite-permitted state.
2. **Identify the authoritative source slices.** From `_REFERENCES.md` and `_CONTEXT.md`, identify all locally accessible source files. For PKG-049 the primary slice is DBM-Deepcut §SEC-05 (Sales Gas Booster Compressor Basis and Design Conditions); the supporting context slice is §SEC-02 (Plant Overview). Verify that referenced material not locally accessible is flagged `location TBD` rather than synthesized.
3. **Confirm package identity.** From `_CONTEXT.md` and GATE-07 DELIVERABLE_REGISTER, record DeliverableID, package, discipline, type, responsible party, covered scope items (SOW-0169..0172), and supported objectives (OBJ-001, OBJ-003..010 under PACKAGE_HEURISTIC association — ASSUMPTION). Verification: identity fields in `Datasheet.md` Identification section match `_CONTEXT.md` and the deliverable register row.
4. **Draft the Datasheet.** Populate Identification, Attributes (package identity), Conditions (design basis), Construction (package constituents), Integration Narrative, Responsibility Assignment, and References. Use only values explicitly stated in the source slice; mark every other value `TBD`. Verification: every non-identification table row carries a Source column entry that points to a real file and section, or `source not local` / `location TBD`.
5. **Draft the Specification.** Convert the source-supported design basis into normative requirements with IDs `R-049-01-NN`. Group Scope, Requirements, Standards, Verification, Documentation. Verification: each requirement traces to a DBM-Deepcut §SEC-05 sub-section (or is labeled ASSUMPTION when based on generic industry practice).
6. **Draft the Guidance.** Capture Purpose, Principles, Considerations, Trade-offs, Examples, and a Conflict Table seed. Verification: each principle/consideration/trade-off references the source slice that motivates it; the Conflict Table is present even when empty.
7. **Draft the Procedure (this document).** Capture Prerequisites, Steps, Verification, Records. Verification: Steps cover authoring through freeze; Records list the artifacts produced.
8. **Run cross-document consistency checks (Pass 2).** Apply the SKILL.md Step 5 matrix: Datasheet ↔ Specification (entities/attributes), Specification ↔ Guidance (rationale), Specification ↔ Procedure (verification hooks), terminology, numeric values/units. Resolve resolvable inconsistencies; for unresolved, prefer `TBD` over guessing and add an entry to the Guidance Conflict Table.
9. **Update `_STATUS.md` safely.** Only when current state is `OPEN` and Pass 1 or Pass 2 ran, transition to `INITIALIZED` with note `TASK+four-documents`. Do not regress state. (See `_STATUS.md` History.)
10. **Write the TASK run record.** Persist `_run_records/TASK_RUN_<timestamp>.md` with the four-documents skill outcome, tool usage, missing items, and dependency notes.
11. **Surface unresolved items for downstream passes.** List values currently carried as `TBD` so that Pass 3 (after `_SEMANTIC_LENSING.md` exists) or human review can resolve them with additional source slices.

## Verification

| Step | Verification |
|---|---|
| 1 | All five deliverable-local metadata files read and reported in the run record. |
| 2 | At least one locally accessible source from `_REFERENCES.md` was read (DBM-Deepcut §SEC-05). |
| 3 | Identity fields in this deliverable match `_CONTEXT.md` and GATE-07 DELIVERABLE_REGISTER row for DEL-049-01. |
| 4 | `Datasheet.md` contains Identification, Attributes, Conditions, Construction, References; every numeric value cites a source or is marked `TBD`. |
| 5 | `Specification.md` contains Scope, Requirements, Standards, Verification, Documentation; each requirement cites a DBM section or is labeled ASSUMPTION. |
| 6 | `Guidance.md` contains Purpose, Principles, Considerations, Trade-offs, Examples and a Conflict Table block. |
| 7 | `Procedure.md` (this document) contains Purpose, Prerequisites, Steps, Verification, Records. |
| 8 | Cross-document terminology and numeric values are consistent; any conflict appears in the Guidance Conflict Table. |
| 9 | `_STATUS.md` shows transition OPEN → INITIALIZED with timestamped history entry (or "skipped, state not OPEN" reported). |
| 10 | A `_run_records/TASK_RUN_<timestamp>.md` exists with `run-status: SUCCESS` (or `FAILED_INPUTS`/`FAILED` with explanation). |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` (this file) — the four-document kit.
- `_STATUS.md` — updated to `INITIALIZED` after a successful P1/P2 run from `OPEN`.
- `_run_records/TASK_RUN_<timestamp>.md` — durable run record.
- Surfaced `TBD` items and the empty seed of the Guidance Conflict Table — inputs for subsequent passes.
