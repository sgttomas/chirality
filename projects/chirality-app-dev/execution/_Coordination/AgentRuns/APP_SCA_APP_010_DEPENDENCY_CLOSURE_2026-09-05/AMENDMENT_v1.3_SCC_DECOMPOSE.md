# Plan amendment v1.3 — owner ruling D-APP-110, decompose the SCCs (issued by HELP_HUMAN before any v1.3 dispatch)

**RunID:** `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05` · **Version:** 1.3 · **Authority:** owner direction 2026-09-05 "Decompose the SCC, record it as part of PR #714.", transcribed in `execution/_Coordination/_DECISIONS/D-APP-110_RULING_SCA_APP_010_SCC_DECOMPOSE_2026-09-05.md` (register row D-APP-110). Extends PR #714 with a third commit; Receipt 239 is re-authored again on the candidate before merge.

## Move basis

`docs/CYCLE_DRIVEN_RESOLUTION.md` §2.3 `decompose`, in the `SCC-SAFE-MOVES-001` form (2026-06-16): re-target a coarse deliverable edge that records contract consumption to the contract as a `DOCUMENT` node; keep the row `ACTIVE`; never retire, cut, merge, or invert. Eligibility: `INTERFACE`, `HANDOVER`, `CONSTRAINT`, `ENABLES` rows only; every `PREREQUISITE` row stays strict. The minimum eligible set that makes the strict graph acyclic was computed exhaustively over the 33 eligible cycle-participating edges (`Evidence/scc_decompose/decompose_choice.json`, `search_log.txt`): five edges, seven rows (six of the nineteen D-APP-109 rows plus the pre-existing `DEP-04-05-010`); full enumeration finds two minimum sets, the alternative opening the two-node SCC from the `DEP-08-01-018` side, and the `DEP-06-03-014` side was chosen because its contract has a documented Scope of Work anchor. Contract targets are named per row in `SCC_DECOMPOSE_RULINGS.csv`.

## New nodes

| Node | Objective | Instances | Write scope | Fan-in gate |
|---|---|---|---|---|
| N13 | Ruling record and register row; the rulings workbook; this amendment | HELP_HUMAN | `_DECISIONS/D-APP-110_*.md`, one `_REGISTER.md` row, `SCC_DECOMPOSE_RULINGS.csv`, `Evidence/scc_decompose/*` | workbook rows equal the computed set; simulated strict graph acyclic |
| N14 | **Apply the move.** `TASK + dependency-extract` per affected carrier: re-target the workbook rows to their `DOCUMENT` contract nodes (`TargetType`, `TargetPackageID` cleared, `TargetDeliverableID` cleared, `TargetRefID`, `TargetName`, `TargetLocation` at the owning carrier's Scope of Work anchor, `LastSeen`, `Notes` appended with the decompose clause); update the `Notes` of the other D-APP-109 rows the carrier holds from "non-gating until resolved" to "resolved by decompose under D-APP-110"; `_DEPENDENCIES.md` counts, Run Notes, Run History, handoff notes; Function 5; carrier run record | `N14-TASK-DEL-{02-01,02-02,02-04,02-05,03-02,04-05,05-02,06-03,08-01,08-04}` | `<carrier>/Dependencies.csv`, `<carrier>/_DEPENDENCIES.md`, `<carrier>/_run_records/TASK_RUN_2026-09-05_*.md`; `instances/<ID>/{RETURN.md,STATUS.json}` | every workbook row re-targeted exactly; every other row byte-identical or Notes-only; schema and enums valid |
| N15 | **Independent review** of N14 against the workbook and the ruling | `N15-REVIEWER` (read-only) | `REVIEW_v1.3.md` | zero BLOCKER or MAJOR |
| N16 | **AUDIT_DEP_CLOSURE** fresh run recording the acyclic strict graph and the move basis (`Dependency_Closure_Report.md` "Move Basis" section in the `SCC-SAFE-MOVES-001` form) | `N16-AUDIT-DEP-CLOSURE` | new snapshot under `_Reconciliation/DepClosure/`; `instances/<ID>/*`; no `_LATEST.md` move | `scc_count = 0` in the strict active deliverable execution graph; every re-targeted row ACTIVE |
| N17 | Fan-in; `HANDOFF_STATE.md`, `VALIDATION_EVIDENCE.md` (v1.3 section), `MANIFEST.sha256`; Receipt 239 re-authored; commit, G4, push | HELP_HUMAN | this packet; `loop/LOOP_RECEIPTS.md` | owner byte review and merge of PR #714 |

## Constraints carried

Everything in `ORCHESTRATION_PLAN.md` "Constraints carried" and amendment v1.2, narrowed to the workbook rows and the Notes updates named above. No row retired; no `PREREQUISITE` row changed; no `_STATUS.md`, `MEMORY.md`, `_CONTEXT.md`, `ScopeOfWork.md`, `_REFERENCES.md`, decomposition, pointer, or Root write; no `_LATEST.md` moved.
