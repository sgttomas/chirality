# Procedure — DEL-064-01 Scope of Work (Tanks, Water (API 650) 4-25)

> Operational procedure for producing the EPC Integrator Scope of Work artifact for PKG-064.
> Pass 1/Pass 2 draft. Steps requiring judgment that the locally accessible DBM source slice does not warrant are marked `TBD`.

## Purpose

Produce the EPC Integrator Scope of Work artifact for PKG-064 Tanks, Water (API 650) 4-25, satisfying the requirements in `Specification.md` and remaining consistent with `Datasheet.md` and `Guidance.md`. The procedure describes how to author, integrate, review, and freeze this deliverable rather than how to operate the physical tanks (which is governed by the Vendor package, DEL-064-04, and downstream operating procedures outside the four-document kit).

## Prerequisites

- Accepted upstream decomposition snapshot: GATE-07_Final_Published_2026-05-24 PROJECT_DECOMP (per `_REFERENCES.md`).
- Locally accessible authoritative source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (especially §SEC-02 spacing, §SEC-05 Module 530 amine regeneration, §SEC-07 NGL caustic treating water wash, §SEC-10 mechanical/freeze-protection requirements, §SEC-16 Workbook Packages row 102 and deliverable row 102).
- Deliverable-local metadata: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` present and current.
- Sibling PKG-064 deliverable identifiers known: DEL-064-02 Package Datasheet, DEL-064-03 Construction Work Package, DEL-064-04 Vendor Engineered Equipment Package, DEL-064-05 Vendor Document Turnover Package, DEL-064-06 EPC Vendor Package Review and Acceptance.
- No declared upstream dependencies blocking initialization (per `_DEPENDENCIES.md`).
- Interfacing packages identified: Tank Farm Pump Building 2 (Process Water Transfer Pumps, P-5317-1, P-5318-1 — outside PKG-064 boundary) and PKG-006 Containment Berms (secondary-containment interface — outside PKG-064 boundary).
- Optional but recommended: extracted source slices for Workbook Packages row 96 and `26020-Package_Requirements.docx` package heading 19 (currently NOT locally accessible; carry as `location TBD`).

## Steps

1. **Read the deliverable-local truth set.** Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`, and `_SEMANTIC.md`. Confirm `_STATUS.md` is in an overwrite-permitted state.
2. **Identify the authoritative source slices.** From `_REFERENCES.md` and `_CONTEXT.md`, identify all locally accessible source files. For PKG-064 the primary slices are DBM-Deepcut §SEC-05 (Module 530 amine regeneration line that includes "process-water storage and transfer"), §SEC-07 (caustic NGL treating make-up-water statement), §SEC-10 (water-tank freeze-protection mandate), and §SEC-16 (Workbook Packages row 102 and deliverable row 102, which give the tag list TK-5317-1, TK-5318-1). The supporting context slice is §SEC-02 (atmospheric tank spacing). Verify that referenced material not locally accessible (Workbook Packages row 96, `26020-Package_Requirements.docx` heading 19) is flagged `location TBD` rather than synthesized.
3. **Confirm package identity.** From `_CONTEXT.md` and GATE-07 DELIVERABLE_REGISTER, record DeliverableID, package, discipline, type, responsible party, covered scope items (SOW-0233..0236), and supported objectives (OBJ-001, OBJ-003..010 under PACKAGE_HEURISTIC association — ASSUMPTION). Verification: identity fields in `Datasheet.md` Identification section match `_CONTEXT.md` and the deliverable register row.
4. **Draft the Datasheet.** Populate Identification, Attributes (package identity), Conditions (design basis), Construction (package constituents), Integration Narrative, Responsibility Assignment, and References. Use only values explicitly stated in the source slice; mark every other value `TBD`. Verification: every non-identification table row carries a Source column entry that points to a real file and section, or `source not local` / `location TBD`.
5. **Draft the Specification.** Convert the source-supported design basis into normative requirements with IDs `R-064-01-NN`. Group Scope, Requirements, Standards, Verification, Documentation. Each requirement shall trace to a DBM-Deepcut section (or be labeled ASSUMPTION when based on generic industry practice such as API 2000 venting).
6. **Draft the Guidance.** Capture Purpose, Principles, Considerations, Trade-offs, Examples, and a Conflict Table seed. Each principle/consideration/trade-off references the source slice that motivates it; the Conflict Table is present even when empty.
7. **Draft the Procedure (this document).** Capture Prerequisites, Steps, Verification, Records. Steps cover authoring through freeze; Records list the artifacts produced.
8. **Run cross-document consistency checks (Pass 2).** Apply the SKILL.md Step 5 matrix: Datasheet ↔ Specification (entities/attributes — tank count, tag list, code basis, freeze protection), Specification ↔ Guidance (rationale — winter freeze, multi-consumer inventory, package-boundary discipline), Specification ↔ Procedure (verification hooks — vendor U-1A review, insulation review, tag reconciliation), terminology (consistent "process water storage tank" naming, consistent tag forms TK-5317-1 / TK-5318-1), numeric values/units (none currently numeric beyond spacing). Resolve resolvable inconsistencies; for unresolved, prefer `TBD` over guessing and add an entry to the Guidance Conflict Table.
9. **Update `_STATUS.md` safely.** Only when current state is `OPEN` and Pass 1 or Pass 2 ran, transition to `INITIALIZED` with note `TASK+four-documents`. Do not regress state.
10. **Write the TASK run record.** Persist `_run_records/TASK_RUN_<timestamp>.md` with the four-documents skill outcome, tool usage, missing items, and dependency notes.
11. **Surface unresolved items for downstream passes.** List values currently carried as `TBD` (tank capacity; PVRV/EPRV sizing; internal coating; heat tracing; drain routing; foundation/ringwall split; ancillary tags; provincial-registration applicability) so that Pass 3 (after `_SEMANTIC_LENSING.md` exists) or human review can resolve them with additional source slices.

## Verification

| Step | Verification |
|---|---|
| 1 | All deliverable-local metadata files present read and reported in the run record. |
| 2 | At least one locally accessible source from `_REFERENCES.md` was read (DBM-Deepcut §SEC-05, §SEC-07, §SEC-10, §SEC-16). |
| 3 | Identity fields in this deliverable match `_CONTEXT.md` and GATE-07 DELIVERABLE_REGISTER row for DEL-064-01. |
| 4 | `Datasheet.md` contains Identification, Attributes, Conditions, Construction, References; every numeric or specification value cites a source or is marked `TBD`. |
| 5 | `Specification.md` contains Scope, Requirements, Standards, Verification, Documentation; each requirement cites a DBM section or is labeled ASSUMPTION. |
| 6 | `Guidance.md` contains Purpose, Principles, Considerations, Trade-offs, Examples and a Conflict Table block. |
| 7 | `Procedure.md` (this document) contains Purpose, Prerequisites, Steps, Verification, Records. |
| 8 | Cross-document terminology (PROCESS WATER STORAGE TANK; TK-5317-1; TK-5318-1) and code basis (API 650) are consistent; any conflict appears in the Guidance Conflict Table. |
| 9 | `_STATUS.md` shows transition OPEN → INITIALIZED with timestamped history entry (or "skipped, state not OPEN" reported). |
| 10 | A `_run_records/TASK_RUN_<timestamp>.md` exists with `run-status: SUCCESS` (or `FAILED_INPUTS`/`FAILED` with explanation). |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` (this file) — the four-document kit.
- `_STATUS.md` — updated to `INITIALIZED` after a successful P1/P2 run from `OPEN`.
- `_run_records/TASK_RUN_<timestamp>.md` — durable run record.
- Surfaced `TBD` items and the empty seed of the Guidance Conflict Table — inputs for subsequent passes.
