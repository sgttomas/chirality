# Procedure — DEL-080-01 Scope of Work (PKG-080 Inlet Compressors)

> Operational procedure for **producing** the Scope of Work deliverable for
> PKG-080 Inlet Compressors. (This deliverable is a documentation product; the
> "operate" interpretation does not apply at this level — operational
> procedures for the physical equipment package belong to the Package Vendor
> Engineered Equipment Package `DEL-080-04` and to the Construction Work
> Package `DEL-080-03`.)

## Purpose

Produce the Scope of Work narrative and supporting four-document kit that, once
human-reviewed and Gate 5 accepted, governs the EPC Integrator scope for the
Inlet Compressors package and anchors the remaining PKG-080 deliverables.

Source: `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` `DEL-080-01_scope-of-work`.

## Prerequisites

1. **Accepted decomposition snapshot** present at
   `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
   Specifically:
   - `PACKAGE_REGISTER.csv` row `PKG-080`
   - `DELIVERABLE_REGISTER.csv` row `DEL-080-01_scope-of-work` and the five
     companion rows `DEL-080-02` through `DEL-080-06`
   - `SCOPE_LEDGER.csv` rows `SOW-0119`–`SOW-0122`
   - `OBJECTIVE_DELIVERABLE_MAP.csv` (used in PACKAGE_HEURISTIC mode)
2. **Deliverable folder minimum viable fileset** seeded by PREPARATION:
   `_CONTEXT.md`, `_STATUS.md` (state `OPEN` or `INITIALIZED`),
   `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md` placeholder.
3. **At least one locally accessible authoritative source slice.** Currently
   satisfied by `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
   SEC-04 and SEC-05. Other cited sources (`26020-Package_Requirements.docx`
   package heading 33; `Bid Docs/Budgetary/brief.md`; budgetary PDF) remain
   `location TBD` until staged — see Guidance Conflict Table C-03, C-04.
4. **No declared upstream blockers.** `_DEPENDENCIES.md` declares none.
5. **`_STATUS.md` state in `ALLOW_OVERWRITE_STATES`** (`OPEN` or
   `INITIALIZED`); otherwise the four-documents skill returns
   `SKIPPED_PROTECT_HUMAN_WORK`.

## Steps

1. **Read deliverable-local truth set.** Read `_CONTEXT.md`, `_STATUS.md`,
   `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`. Confirm
   `Current State` is `OPEN` or `INITIALIZED`.
2. **Read decomposition entries.** Pull the `DEL-080-01_scope-of-work` row from
   `DELIVERABLE_REGISTER.csv`, the `PKG-080` row from `PACKAGE_REGISTER.csv`,
   and the `SOW-0119` through `SOW-0122` rows from `SCOPE_LEDGER.csv`.
   Capture: package function, responsibility split, applicable interface types,
   covered scope items, anticipated artifacts.
3. **Resolve objective associations.** Under
   `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`, record
   OBJ-002 … OBJ-010 as directionally relevant context (label as
   `ASSUMPTION (best-effort mapping)`).
4. **Read locally accessible source slices.** Read DBM SEC-04 (inlet,
   separation, sour-gas export) and SEC-05 (inlet compression and TEG
   dehydration) end-to-end. Extract: capacity basis, configuration, driver,
   modularization, pressures/temperatures, NACE materials, tie-in routings,
   SCA supersessions in effect.
5. **Draft Datasheet.md** with Identification, Attributes, Conditions,
   Construction, References sections. Cite source for every non-trivial value.
   Use `TBD` for missing values; do not invent.
6. **Draft Specification.md** with Scope (in/out), Requirements (REQ-080-01-*),
   Standards, Verification, Documentation sections. Label inferred requirements
   `ASSUMPTION`. Mark unresolved standard locations `location TBD`.
7. **Draft Guidance.md** with Purpose, Principles, Considerations, Trade-offs,
   Examples sections. Append a Conflict Table for human ruling on items where
   sources and decomposition disagree or where authoritative source slices are
   unavailable.
8. **Draft Procedure.md** (this document) with Purpose, Prerequisites, Steps,
   Verification, Records sections.
9. **Pass 2 cross-reference consistency check.**
   - Datasheet ↔ Specification: confirm KM-2150/2250 identity, 2 x 50%
     configuration, 40/80 MMSCFD, 800 psig discharge, NACE materials, and the
     thirteen interface types appear consistently in both.
   - Specification ↔ Guidance: confirm every REQ-080-01-* has rationale or
     consideration coverage in Guidance Principles/Considerations.
   - Specification ↔ Procedure: confirm Verification approaches in
     Specification are reachable via review/inspection steps that the
     downstream PKG-080 deliverables can execute.
   - Terminology: "Package Vendor" vs "Vendor" — use "Package Vendor"
     consistently. "EPC Integrator" — never "EPC" alone for scope assignments.
   - Values: psig values are governing per Conflict C-02 resolution proposal;
     kPag values are summary-only.
   - Where inconsistencies cannot be resolved from drafted documents alone,
     re-read the relevant DBM source slice; if still unresolved, add to
     Conflict Table.
10. **(Pass 3 — deferred.)** Apply `_SEMANTIC_LENSING.md` enrichment when
    that register is produced by ORCHESTRATOR Phase 2.4 (`lens-register` skill).
    Pass 3 is **not run** in this invocation (`RUN_PASSES=P1_P2`).
11. **Update `_STATUS.md`** from `OPEN` to `INITIALIZED` (only when current
    state is `OPEN`; no state regression). Record this run in History.
12. **Persist the run record** at
    `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` with input echo, resolved
    state, applied changes, MISSING items, and NEEDS_HUMAN_RULING items.

## Verification

| Check | Method | Pass criterion |
|---|---|---|
| All four documents present | Folder listing | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` all exist |
| Default schema sections present | Section grep | Each document carries its default sections (see skill SKILL.md Step 2 schema table) |
| At least one locally accessible source read | Reference review | DBM SEC-04 and SEC-05 cited as source in Datasheet and Specification |
| Non-trivial values cite source | Spot-check | Each capacity, pressure, temperature, motor-rating, NACE statement carries a source pointer or `location TBD` |
| Responsibility split mirrors PACKAGE_REGISTER row | Side-by-side compare | Verbatim alignment of who-owns-what for engineering/design/equipment vs facility integration |
| Thirteen interface types enumerated | Count | All 13 interface types from `PACKAGE_REGISTER.csv` PKG-080 appear in Datasheet Construction and Specification REQ-080-01-09 |
| SCA supersessions reflected | Text search | SCA-001, SCA-002 referenced; no 650 psig discharge language carried |
| Conflict Table contains unresolved items | Inspection | C-01 (KBC/KBZ), C-02 (psig/kPag), C-03 (docx not accessible), C-04 (bid-docs not staged) present and marked TBD |
| `_STATUS.md` updated only on `OPEN` | State diff | `OPEN -> INITIALIZED` recorded with History entry; no regression on `INITIALIZED` or later |
| Run record persisted | File existence | `_run_records/TASK_RUN_<ts>.md` with `run-status: SUCCESS` |

## Records

Evidence produced by this procedure (within deliverable-local scope):

- `Datasheet.md`
- `Specification.md`
- `Guidance.md` (includes Conflict Table C-01 … C-04)
- `Procedure.md`
- `_STATUS.md` (updated `OPEN → INITIALIZED`; History appended)
- `_run_records/TASK_RUN_2026-05-24_2338.md` (this run)

Downstream consumers of these records (per `DELIVERABLE_REGISTER.csv`):

- `DEL-080-02_package-datasheet` — consumes the EPC scope statement as input
  for the vendor-handoff datasheet.
- `DEL-080-03_construction-work-package` — consumes EPC interface scope and
  modularization basis for installation/turnover planning.
- `DEL-080-04_vendor-engineered-equipment-package` — Package Vendor production
  unit anchored by this Scope of Work and `DEL-080-02`.
- `DEL-080-05_vendor-document-turnover-package` — Vendor documentation
  register anchored by the SoW responsibility split.
- `DEL-080-06_epc-vendor-package-review-and-acceptance` — EPC reviews vendor
  outputs against the scope, interfaces, and responsibilities defined here.
