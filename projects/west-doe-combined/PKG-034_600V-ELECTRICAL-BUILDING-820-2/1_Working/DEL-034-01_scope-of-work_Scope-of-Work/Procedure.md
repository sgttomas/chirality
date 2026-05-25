# Procedure: DEL-034-01 — Scope of Work (PKG-034 600V Electrical Building (820-2))

## Purpose

Produce the EPC Integrator's Scope of Work for PKG-034 "600V ELECTRICAL BUILDING (820-2)" such that it carries package identity, function, source basis, boundaries, responsibility split, and whole-facility integration narrative, grounded in Gate 7 registers and the 03-25 DBM.

## Prerequisites

- Read the deliverable-local truth set:
  - `_CONTEXT.md`
  - `_STATUS.md`
  - `_REFERENCES.md`
  - `_DEPENDENCIES.md`
- Confirm declared upstream dependencies (none declared at PREPARATION).
- Access the Gate 7 Final Published snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`:
  - `DELIVERABLE_REGISTER.csv` (row `DEL-034-01_scope-of-work`).
  - `PACKAGE_REGISTER.csv` (row `PKG-034`).
  - `ARTIFACT_REGISTER.csv` (artifacts mapped to DEL-034-01).
  - `INTERFACE_REGISTER.csv` (interface IDs scoped to PKG-034; carried operationally in DEL-034-02).
- Access source slices in `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`: SEC-12 "Electrical Buildings, Raceways, Lighting, and Heat Tracing"; SEC-12 "Incoming Power and Transformers"; SEC-12 "600V MCC and Standby Power"; SEC-11 buildings/foundations paragraphs.
- Access `_Sources/DBM-Comp_and_Liquids/Trace_Appendix.md` rows SUB-12-05-01 and SUB-12-05-02.

## Steps

1. **Identity capture.** From Gate 7 `PACKAGE_REGISTER.csv` row PKG-034, transcribe PackageID, package name (with "820-2" suffix), CoA tracking number, WBS, discipline, and source row into the SOW header. Confirm consistency with `_CONTEXT.md` Identity table.
2. **Scope items and objectives.** From Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-034-01, transcribe `Covers Scope Items` (`SOW-0035`) and the objective list (`OBJ-002`, `OBJ-004`–`OBJ-010`); label the objective list ASSUMPTION (package-grouping heuristic) per `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`.
3. **Function statement.** Compose a function paragraph grounded in DBM 3-25 SEC-12 (electrical buildings house MCCs, switchgear, distribution equipment, HVAC) and Trace_Appendix SUB-12-05-02 (pre-fabricated modular building). Constrain to 600V scope per package designation "820-2".
4. **Source basis.** Cite Workbook Packages row 36 and the 3-25 DBM; mark direct workbook citations as "location TBD" pending row-36 slice copy.
5. **Upstream electrical context.** Document the sub-feed from 04-25 13.8 kV Main Switchgear Electrical Building via 13.8 kV / 600V, 3 MVA transformer to the 600V MCC (DBM SEC-12 "Incoming Power and Transformers").
6. **Standby power note.** Record LV standby natural-gas generator at the 600V MCC level with transfer switch; mark transfer-switch type, bus configuration, generator count/rating as `TBD` (DBM SEC-12 "600V MCC and Standby Power").
7. **Boundaries and interfaces.** Transcribe the 12 workbook interface types verbatim from Gate 7 `PACKAGE_REGISTER.csv` and point detailed interface-fact content to DEL-034-02 (ART-28791428C9 and per-interface ART-* entries).
8. **Responsibility split.** Quote Gate 7 `PACKAGE_REGISTER.csv` responsibility wording (Package Vendor vs EPC Integrator) verbatim to avoid drift across PKG-034 deliverables.
9. **Exclusions.** State LACT units (third-party) and local 03-25 instrument-air compressors (per SCA-006) as exclusions.
10. **Cross-document consistency sweep (Pass 2).** Verify Datasheet identity, Specification requirements, Guidance principles, and Procedure prerequisites use the same package name, CoA, WBS, discipline, voltage class, and interface list. Reconcile from Gate 7 register text where ambiguity arises. Capture unresolved conflicts in the Guidance Conflict Table.
11. **Status update.** If `_STATUS.md` is `OPEN`, run `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`. Do not regress state.
12. **Run record.** Write `_run_records/TASK_RUN_2026-05-24_<HHmm>.md` per the AGENT_TASK run-record format.

## Verification

| Check | Method | Pass condition |
|---|---|---|
| Identity matches Gate 7 register | Field-by-field diff | All seven identity fields match `PACKAGE_REGISTER.csv` row PKG-034 |
| All twelve interface types present | List comparison | SOW lists the same 12 interface types as the register |
| Responsibility wording verbatim | Text diff | Responsibility paragraph matches `PACKAGE_REGISTER.csv` Responsibility column |
| Source citations present | Document review | Every non-trivial statement cites a register row or DBM section (or carries "location TBD") |
| `TBD` items justified | Document review | Each `TBD` traces to absent or inaccessible source content |
| Cross-document terminology | Lexical check | Package name uses "(820-2)" consistently; voltage class consistently rendered as "600V" |
| `_STATUS.md` transition safety | File read | If pre-run state ≠ `OPEN`, no state edit performed |

## Records

- Datasheet.md
- Specification.md
- Guidance.md (with Conflict Table)
- Procedure.md
- Updated `_STATUS.md` (only when safe transition `OPEN → INITIALIZED`)
- `_run_records/TASK_RUN_2026-05-24_<HHmm>.md`
