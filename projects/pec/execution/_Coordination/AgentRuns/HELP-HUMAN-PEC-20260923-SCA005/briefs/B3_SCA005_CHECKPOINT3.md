# Brief B3 — SCA-005 checkpoint-3 preparation (WORKING_ITEMS, scope-change workflow)

Parent: HELP_HUMAN run `HELP-HUMAN-PEC-20260923-SCA005`, node B3. Role: WORKING_ITEMS (Type 1). Model steer: `claude-opus-5-5`, high reasoning, for you and your children (D-PEC-86 I-8).

## Authority

The owner accepted checkpoint group 2 on 2026-09-25 with the words "CP2: accept; Q1 a; Q2 a; Q3 a; Q4 a with A4 deferred." The record is `projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-2_2026-09-25/`, which holds `DECISION.md`, `ACCEPTED_MANIFEST.csv` and `Handoff_State.md`. Register row `D-PEC-92` makes that snapshot the D-PEC packet that opens PEC's write fence for Lane A. A4 is not opened.

Stage: **checkpoint-3 preparation**. Execute the accepted writes, validate and audit them, complete the SCA snapshot, and produce the audited poststate package for the owner's checkpoint-3 acceptance. Then stop.

## Method

Use `Workflow: chirality-root:bundled:workflow:scope-change`. Load `WORKFLOW.md`, `resources/contract.md` and `resources/method.md`, and record their SHA-256. Follow the method's checkpoint-3 preparation section.

Your specification is the accepted `projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139/Propagation_Plan.md` (`50cd0b1d91ea25cc8ecba28ce649278b376fb952feec09e007a26ca5bbf91350`) together with `Amendment_Preview.md` (`ad48cc5621d796a662addc03640a32f7f4cdafbf627ad6fda3f60bdede65ebe4`). Apply both as bounded by the group-2 `DECISION.md`, which governs where they differ. Do not enlarge them.

## Preconditions (stop before any write if one fails; a mismatch returns to checkpoint 2 with drift evidence)

Everything in `Propagation_Plan.md` §"Checkpoint-3 preconditions", plus the following:
- Fetched `origin/main` contains the merged group-2 record and the `D-PEC-92` register row.
- Every artifact in the group-2 `ACCEPTED_MANIFEST.csv` has its listed hash. The exception is the two rows labelled "at package publication".
- The reliance-hold preflight returns `ALLOW` for every write target, using `projects/pec/execution/_Scripts/pec_reliance_hold.py` with operation `dispatch-for-production`.

## Execute (Lane A as bounded by D-PEC-92)

- **A1.** Apply the decomposition and the four register postimages, and adopt `docs/PRD.md` from `CP2_CANDIDATE/docs/PRD.md` byte for byte.
  - Write the decomposition with the two pre-acceptance front-matter lines.
  - Its date slots take the actual application date.
  - Record every slot value and apply the slot hash rule in `Amendment_Preview.md` §"Acceptance-bound tokens".
- **A2.** The 22 `_CONTEXT.md` mirrors, exactly as planned. Each preimage and postimage hash must match the plan.
- **A3.** The four `_STATUS.md` retirements by hand-authored exact edit, as Q-CP2-1 (a) requires.
  - Read each file's sibling `MEMORY.md` first.
  - Do not use `write_status.sh`.
- **A4.** NOT opened. Do not create the DEL-02-08 or DEL-02-09 folders or any `Dependencies.csv` rows.
- **A5.** Complete the SCA snapshot.
  - Generate `Supersession_Map.csv` with the accumulator command in the plan. Never write it by hand.
  - Copy the post-change audit's `coverage_summary.json` to `Post_Change_Coverage.json`.
  - Write `RUN_SUMMARY.md`.
  - Update `Decision_Log.md` (SCA005-CP3 row set to `PREPARED / AWAITING_OWNER`, with hashes) and `Handoff_State.md` additively.
  - Fix the `Handoff_State.md` heading and front matter to say the stage is checkpoint 3.
  - Keep every checkpoint-1 and checkpoint-2 artifact byte-unchanged.
- **A6.** Do NOT move either `_LATEST.md` pointer. That happens only after the owner's checkpoint-3 acceptance, in a later HELP_HUMAN act.

## Validate (Lane C, with the group-2 expectations)

- **C1.** Check the diff against an allowlist:
  - live decomposition and four registers, `docs/PRD.md`, the 22 `_CONTEXT.md` files, the four `_STATUS.md` files;
  - the SCA-005 snapshot folder, the new `COV_SCA005_POSTCHANGE_*` folder;
  - the run-record `returns/` files named below.

  Assert that every written hash matches its planned value, with the slot rule applied to `SOFTWARE_DECOMP.md`.
- **C2.** `validate_decomposition_registers.py projects/pec/execution --strict`. Expected: 0 errors and exactly two DRB-008 warnings, for DEL-02-08 and DEL-02-09.
  - `analyze_dep_closure.py`. The expected result is the pre-B3 topology: 119 edges, 0 SCCs, isolated nodes DEL-00-03 and DEL-01-05, and `DEP-09-05-005` present.
  - Per `DECISION.md`, neither of these is a defect.
- **C3.** Run the exact successor assertions in the plan (counts, the union rule, envelopes and so on).
- **C4.** Dispatch a TASK child (`pec-task`, opus) to run the `audit-decomp` workflow (`workflows/audit-decomp/`). Use `DECOMP_VARIANT=SOFTWARE`, full scope, expected revision 1.5, and SCA-005 as the candidate. Output goes to a new `projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA005_POSTCHANGE_<YYYY-MM-DD>_<HHMM>/`.
  - Compare it with `COV_SCA005_PRECHANGE_2026-09-23_2139`.
  - Report any finding that stems only from the absent DEL-02-08/09 folders or from the unopened B3 as a consequence, not a defect.
- **C5.** Check the snapshot for completeness.

If validation fails before a pointer move, keep the failed state as evidence and report it. Do not repair beyond the accepted plan.

## Independent verification

Dispatch one fresh read-only verifier (`pec-reviewer`, opus). It confirms that the live poststate equals the accepted candidates, that the edits contain nothing outside the plan, the C1–C5 results, and that the audit reading is honest. Defects go back to you, and you repair them within the plan. Repeat until nothing is blocking. Save each verdict.

## Write boundary

Work in your isolated worktree, on branch `claude/pec-sca005-cp3-execution` cut from fresh `origin/main`.

You may write only:
- the Lane A targets above, except A4 and A6;
- the SCA-005 snapshot folder;
- the new `COV_SCA005_POSTCHANGE_*` folder;
- `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/returns/B3_SCA005_CHECKPOINT3.md` (your return) and `returns/B3_VERIFIER_VERDICT_NN.md`.

Do NOT write:
- `_ScopeChange/_LATEST.md`, `_Decomposition/_LATEST.md`, `checkpoint_snapshots/**`, or the group-1 and group-2 pointers;
- any SOW, `_REFERENCES.md`, `_DEPENDENCIES.md` or `Dependencies.csv`;
- `v2/**`, `software-workflow.json` or `projects/pec/AGENTS.md`;
- `loop/**`, `docs/STATUS.md`, `README.md`, `_DECISIONS/**` or the HELP_HUMAN `RUN.md`;
- any Root, sister or foreign path.

HELP_HUMAN writes the three informational notices the group-2 `DECISION.md` names, so you do not write them:
- Root, about RETIRED;
- Root, about `LOOP_INIT`;
- one App/Piping notice about `adapter.yaml`, filed in both loops' `execution/_Coordination/` folders.

Include their drafted text in your return.

## Checkpoint-3 owner question

At the end of `RUN_SUMMARY.md`, put this question: accept the audited poststate. Cite the live decomposition, registers and PRD hashes, the audit snapshot and its verdict, the closure state fields and the known consequences of the A4/B3 deferral. On acceptance, HELP_HUMAN moves the pointers (A6) with the checkpoint-3 dates. List only the genuinely open choices, each with a recommendation.

## Publication

Commit. End each commit message with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Push and open a PR against `main`, ending the PR body with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`. Do not merge.

## Return

- PR URL and head SHA.
- Written files with preimage and postimage hashes.
- Slot values used.
- C1–C5 results.
- The audit snapshot path and verdict.
- The closure state fields.
- The checkpoint-3 question set.
- Verifier verdicts and cycles.
- Containment output.
- Draft notice texts.
- Anything unresolved.
- The delegation record.

## Limits

No A4, no Lane B rerun, and no pointer move. No lifecycle transition other than the four A3 retirements. No CHECKING, ISSUED or artifact acceptance, and do not ask the owner about CHECKING. No reliance-text amendment.
