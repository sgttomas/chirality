# Brief U1 — D-PEC-95 P + R currency act with T1 (WORKING_ITEMS)

Parent: HELP_HUMAN, undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node U1 (with N1–N3 and T1). Role: WORKING_ITEMS (Type 1). Model steer: `claude-opus-5-5`, high reasoning, for you and your children (owner: "defaults").

## Authority and specification

- **Ruling:** `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-95_RULING_2026-09-25.md`. The owner's words: "D-PEC-95: P+R (don't append); accept 10-05-004 as prepared; confirm TM-PEC-023; no re-audit; include; defaults". The ruling's question resolutions and its "P + R bytes" section bind this act.
- **Proposal:** `D-PEC-95_revision_1_5_currency_proposal_2026-09-25.md`, SHA-256 `9137d3872329cea5093f61fb6c4150121e4ffcc2abe900ca88e7339049064b22`. This is your specification: generation method, exact product grant, finite verification, independent verifier, administrative grant, rollback and limits. Do not enlarge it.
- **Generator:** `projects/pec/execution/_Coordination/PEC_CURRENCY_D95_PREP_2026-09-25/gen_d95.py`, SHA-256 `0e9ede5044b34cc4594836aab73a0a8df02cd4d1de8ae5e1e5625ebb232ebe78`. Also in that folder:
  - `verify_d95.py` (`fcf172b5aa2ec6179a5af541f1a01d68a0148590d3b3f6eafbf913e64bfb185f`);
  - `t1_tm_pec_023.py` (`0e0cd6f94448005ecf17f564f35ef72a42f2c2862e97bc33256a3c701b957bec`).

## Preconditions (stop and return if any fails)

- Fetched `origin/main` contains the ruling and the register row `RULED P + R`.
- Record the local date `{D}` of the run. No clock or time-zone manipulation.
- `projects/pec/execution/_Scripts/pec_reliance_hold.py` returns ALLOW for every target with operation `dispatch-for-production`, and with `rely-for-production` before fan-in.
- You are in an isolated worktree on branch `claude/pec-d95-currency-act`, cut from fresh `origin/main`. On any generator or check failure, discard the worktree and return. Do not repair.

## Act

1. Create the run root `projects/pec/execution/_Coordination/CURRENCY_REV15_D95_{D}/`. Copy `gen_d95.py` and `verify_d95.py` into it byte for byte and check their hashes. Take a `git archive` export of the pre-act `origin/main` to use as the `pre` tree for `verify_d95.py`, and keep it outside the repository.
2. Run the generator once from the repository root:

   ```text
   PYTHONDONTWRITEBYTECODE=1 python3 projects/pec/execution/_Coordination/CURRENCY_REV15_D95_{D}/gen_d95.py --repo . --act-date {D} --option P --retired-covers
   ```

   Save stdout in the run root. It must report `AGGREGATE option=P+R files=119` and `CHECK active_execution_quotes_verbatim 111 111`.
3. Run the proposal's whole "Finite verification" table and save the outputs under the run root:
   - `verify_d95.py <pre export> . --option P --retired-covers`.
   - Byte identity:
     - 115 files equal their P postimage in `PEC_CURRENCY_D95_PREP_2026-09-25/evidence/genP.tsv`;
     - the four retired `_REFERENCES.md` equal their A + R postimage in `genAR.tsv`;
     - both apply the proposal's slot rule if `{D}` is not 2026-09-25.
   - The SCA-005 `Handoff_State.md` and `RUN_SUMMARY.md` are byte-unchanged.
4. **T1.** Apply `t1_tm_pec_023.py` (copy it into the run root first) under `workflows/task-management/`. Then run `tools/taskmgmt/taskmgmt.py validate` on both registers, then `archive`, then `validate` again. Record the outputs. The owner's disposition is the ruling's "confirm TM-PEC-023".
5. Write `MANIFEST.md`, `VALIDATION.md` and `HANDOFF_STATE.md` in the run root, in the PROJECT_SETUP closeout format. Use the D-PEC-93 run root `PROJECT_SETUP_SCA005_A4_B3_2026-09-25/` as precedent.
6. Dispatch one fresh read-only verifier (`pec-reviewer`, opus). It applies the proposal's "Independent verifier" section, with option P + R. On item 4, it records DEP-10-05-004's weaker warrant and does not fail it, per the ruling. Save its verdicts as `VERIFIER_VERDICT_NN.md` in the run root. Defects come back to you. Repair only within the proposal and ruling; otherwise stop and report.

## Write boundary

You may write only:
- the 119 P + R paths;
- the run root;
- `projects/pec/execution/_Coordination/_TaskManagement/REGISTER.csv` and `REGISTER_CLOSED.csv` (T1 only);
- `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/U1_D95_CURRENCY_ACT.md` (your return).

You may not write:
- any other `_Decomposition/**`, `_ScopeChange/**` or `_Evaluation/**` path;
- `checkpoint_snapshots/**`;
- any SOW, `_STATUS.md`, `docs/**`, `README.md`, `v2/**`, `_DECISIONS/**`, the work graph, or `MEMORY.md`;
- any foreign path.

Commit your return to your PR branch before you hand back.

## Publication

Commit, ending each message with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Push and open a PR against `main`, ending the body with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`. Do not merge. If CI reports "Update the PR base", say so; do not repair it.

## Return

- PR URL and head SHA.
- `{D}`.
- The generator report aggregate.
- Written paths with hashes, or the path to the manifest.
- Check results, including T1.
- Verifier verdicts.
- Containment.
- Anything unresolved.

## Limits

- No SOW, `v2/**`, PRD, decomposition-text, register-content or lifecycle change.
- No SCA-005 snapshot write.
- No audit and no pointer move under `_Evaluation/**`.
- No CHECKING, ISSUED or acceptance. Do not ask the owner about CHECKING.
