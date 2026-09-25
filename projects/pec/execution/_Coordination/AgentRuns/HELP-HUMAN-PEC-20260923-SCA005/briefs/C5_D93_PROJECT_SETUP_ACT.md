# Brief C5 — D-PEC-93 option A PROJECT_SETUP act (WORKING_ITEMS with PROJECT_SETUP)

Parent: HELP_HUMAN run `HELP-HUMAN-PEC-20260923-SCA005`, node C5. Role: WORKING_ITEMS (Type 1) coordinating the PROJECT_SETUP act. Model steer: `claude-opus-5-5`, high reasoning, for you and your children.

## Authority and specification

- **Ruling:** `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-93_RULING_2026-09-25.md`, the owner's "D-PEC-93: A.". Its clarifications N1, N2, N5 and N6 bind this act.
- **Proposal:** `D-PEC-93_project_setup_sca005_a4_b3_proposal_2026-09-25.md`, SHA-256 `46470575625522398fa47d0a39aa09d2b4d252dd89c083ba317f9e577f489422`. This is your specification: generation method, exact product grant, finite verification, re-audit and audit-pointer rule, administrative grant, rollback and limits. Do not enlarge it.
- **Generator:** `projects/pec/execution/_Coordination/PROJECT_SETUP_SCA005_A4_B3_PREP_2026-09-25/gen_d93.py`, SHA-256 `cfae005258659c55915d0e9e2a8566399c3c84a95ede8e567205fecaea08d6c2`.

## Preconditions (stop and return if any fails)

- Fetched `origin/main` contains the merged ruling and its register row (`RULED A`).
- The local date is the act date, and the act date is recorded. The proposal's table hashes are at 2026-09-25. On another date, the verifier's independent comparison is: take the tabled 2026-09-25 postimages (as in the preparation folder's `protoA_vs_base.diff`), substitute the act date at the proposal's slot loci, hash, and compare with the written files; not the act's own recorded hashes. No clock or time-zone manipulation.
- The reliance-hold preflight returns ALLOW for every target: `projects/pec/execution/_Scripts/pec_reliance_hold.py`, operation `dispatch-for-production`.
- You are in an isolated worktree on branch `claude/pec-d93-project-setup-act`, cut from fresh `origin/main`. If the host refuses a new local branch, push your worktree branch to that remote name and record it. On any generator or check failure, discard the worktree and return (N1). Do not repair.

## Act

1. Copy the generator byte for byte into the run root `projects/pec/execution/_Coordination/PROJECT_SETUP_SCA005_A4_B3_<act-date>/` and check its hash. Run the binding command once from the repository root, exactly as the proposal states, with no `--mirror-set` and no `--optional-edge`. Save its stdout under the run root.
2. Verify:
   - every written path is on the proposal's 31-path list;
   - every postimage hash matches the table, with the slot rule applied if the date differs;
   - the strict registers validator reports 0 errors and 0 warnings;
   - `analyze_dep_closure.py` reports 111 edges, 0 SCCs, 0 bidirectional pairs, and isolated nodes DEL-00-03, DEL-01-05, DEL-06-04, DEL-07-02, DEL-07-04 and DEL-07-05;
   - the schema validator passes on the 8 registers written;
   - `check_min_viable_fileset` passes on both new folders.

   Save outputs under the run root's `checks/`.
3. Re-audit. Dispatch a TASK child (`pec-task`, opus) to run `audit-decomp`: full SOFTWARE scope, revision 1.5, into a new `projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA005_POSTSETUP_<act-date>_<HHMM>/`, compared with `COV_SCA005_POSTCHANGE_2026-09-25_1344`. The proposal states the expected result: COV-001/002/070/071 and the others it names clear, and the verdict is WARN. The child writes only its folder.
4. If and only if the re-audit reports 0 BLOCKERs, update `_Evaluation/DecompCoverage/_LATEST.md` to name the new audit, as the proposal states. Preimage: `0084d218…7432`. If it reports any BLOCKER, leave the pointer and report.
5. Run one fresh read-only verifier (`pec-reviewer`, opus). It checks that the act equals the proposal byte for byte, using the N2 method; that the checks and the audit reading are honest; and containment. It saves its verdicts. Defects come back to you. Repair only within the proposal; otherwise stop and report.

## Write boundary

You may write only:
- the 31 proposal paths;
- the run root;
- the new `COV_SCA005_POSTSETUP_*` folder;
- `_Evaluation/DecompCoverage/_LATEST.md`, conditionally;
- `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/returns/C5_D93_PROJECT_SETUP_ACT.md` (your return) and `returns/C5_VERIFIER_VERDICT_NN.md`.

You may not write:
- `_Decomposition/**`, `_ScopeChange/**`, or any SOW, `_CONTEXT.md` or `_REFERENCES.md` outside the two new folders;
- any `_STATUS.md` other than the two new ones;
- `v2/**`, `docs/**`, `loop/**`, `README.md`, `_DECISIONS/**`, or the HELP_HUMAN `RUN.md`;
- any foreign path.

Commit your return to your PR branch before you hand back, so it survives a host-forced handback.

## Publication

Commit. End each commit message with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Push and open a PR against `main`. End the PR body with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`. Do not merge.

## Return

- PR URL and head SHA
- act date
- the generator report
- written paths with hashes
- check results
- the re-audit path and verdict
- whether the pointer moved
- verifier verdicts
- containment
- anything unresolved
- the delegation record

## Limits

- No SOW, `v2/**`, PRD, decomposition-register or lifecycle change beyond the two new `OPEN` statuses.
- No O or B1 add-on.
- No evidence-quote refresh.
- No CHECKING, ISSUED or acceptance. Do not ask the owner about CHECKING.
