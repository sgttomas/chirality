# Plan amendment v1.2 — owner ruling D-APP-109 (issued by HELP_HUMAN before any v1.2 dispatch)

**RunID:** `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05` · **Version:** 1.2 · **Authority:** owner direction 2026-09-05, transcribed verbatim in `execution/_Coordination/_DECISIONS/D-APP-109_RULING_SCA_APP_010_HELD_EDGES_AND_CONTEXT_ALIGNMENT_2026-09-05.md` (register row D-APP-109). Extends the open candidate (PR #714, first commit `f38f1448675b8e9f40f33932a11b7ffa4126fe69`) with a second commit; the receipt for the iteration is re-authored on the candidate branch before merge.

## New nodes

| Node | Objective | Instances | Write scope | Fan-in gate |
|---|---|---|---|---|
| N8 | Ruling record and register row; this amendment; deterministic context alignment through `build_context_fix.py` (freeze, apply, check) acting as WORKING_ITEMS' applicator under D-APP-109 | HELP_HUMAN | `_DECISIONS/D-APP-109_*.md`, one `_REGISTER.md` row; the thirteen carriers' `_CONTEXT.md`, `_STATUS.md` (one history line), `MEMORY.md` (one line); `Evidence/context_fix/*` | pre-image and post-image parity; SOW validator unchanged (no `ScopeOfWork.md` write) |
| N9 | **Emit the held rows.** `TASK + dependency-extract` apply per carrier that holds proposals: author the reserved rows in full (29 columns, the carrier's quoting convention) from the preview's held-proposal section and `HELD_EDGE_PROPOSALS.csv`, with the D-APP-109 non-gating `Notes` clause; replace the `HELD` Run Notes bullets; reconcile counts; add a Run History row; Function 5; carrier run record | `N9-TASK-DEL-{02-01,02-02,02-04,02-05,03-02,05-02,06-03,08-01,08-04}` | `<carrier>/Dependencies.csv`, `<carrier>/_DEPENDENCIES.md`, `<carrier>/_run_records/TASK_RUN_2026-09-05_*.md`; `instances/<ID>/{RETURN.md,STATUS.json}` | every reserved ID present exactly once; schema and enums valid; nineteen rows equal the held proposals' edges, directions, and types |
| N10 | **Independent review** of the N9 rows and the N8 context edits | `N10-REVIEWER` (read-only) | `REVIEW_v1.2.md` | zero BLOCKER or MAJOR |
| N11 | **AUDIT_DEP_CLOSURE** fresh run (same label, new snapshot) recording the post-emission SCC picture; **AUDIT_DECOMP** fresh run recording context fidelity | `N11-AUDIT-DEP-CLOSURE`, `N11-AUDIT-DECOMP` | new snapshots under `_Reconciliation/DepClosure/` and `_Evaluation/DecompCoverage/`; `instances/<ID>/*`; no `_LATEST.md` move | verdicts recorded; SCC change reported, not linearized |
| N12 | Fan-in; `HANDOFF_STATE.md`, `VALIDATION_EVIDENCE.md` (v1.2 section), `MANIFEST.sha256`; Receipt 239 re-authored on the candidate; commit, G4, push | HELP_HUMAN | this packet; `loop/LOOP_RECEIPTS.md` | owner byte review and merge of PR #714 |

## Constraints carried

Everything in `ORCHESTRATION_PLAN.md` "Constraints carried" except the two widenings D-APP-109 grants: the reserved rows may now be written, and the thirteen `_CONTEXT.md`, `_STATUS.md` (history line only), and `MEMORY.md` (one line) files may be written for the alignment named in the ruling. No `ScopeOfWork.md`, `_REFERENCES.md`, lifecycle, Checking Approval SHA, `docs/**`, decomposition, pointer, or Root write. Emitted cycle-participating rows are non-gating until the SCC is resolved by a recorded move.
