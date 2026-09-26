# VERIFIER_VERDICT_01 — D-PEC-99 option-A Remaining retirement act (PR #957)

- **Verifier role:** TASK (Type 2). Fresh, independent and read-only. I authored nothing in this package, and I edited, staged, committed and pushed nothing in any repository checkout. Scratch work ran only in `mktemp -d` directories (`/private/tmp/claude-501/d99v.6vKDgU/`), with `PYTHONDONTWRITEBYTECODE=1`. That includes `git archive` exports and three `git clone --shared` scratch clones used for the validators and for a trial merge.
- **Model (as reported by runtime):** Claude Opus 5.5, `claude-opus-5-5`. The host set the reasoning level; the steer asked for high.
- **Candidate head reviewed:** `10feef34cc1c0aff7ecd3098ce2a3a19494455bd`, branch `claude/pec-d99-remaining-retirement-act`. The review worktree's `git rev-parse HEAD` equals this, and `gh pr view 957` reports the same `headRefOid`, OPEN and MERGEABLE.
- **Basis:** `origin/main` `189f205ff02df4111b33c20be441ce06e65ada7a` (PR #954 merge). Current `origin/main` is `6b48b6f26ed3e9ef60fde1c7d2289843bd1aea25` (PR #955).
- **Date/time:** 2026-09-26, 12:21 MDT. My local date is 2026-09-26, so I ran the generator without `--reproduction`.
- **Instruction and authority sources relied on (SHA-256; identical at 189f205ff and 10feef34c unless noted):**
  - Root `AGENTS.md`: `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd`
  - `agents/AGENT_TASK.md`: `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7`
  - `projects/pec/AGENTS.md`: pre-act at 189f205ff is `4400c4e97d5c9dfeda7a9a764b204ed14784c687e55e81bb04875323b6c7139c`, as required. Postimage at 10feef34c is `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8`.
  - `_DECISIONS/D-PEC-99_remaining_retirement_proposal_2026-09-26.md`: `29e2ff5704d45f0da31f41fd80bf822003743fbf9effdda4ebbc2806306d5c79`, as required.
  - `_DECISIONS/D-PEC-99_RULING_2026-09-26.md`: `3e34403a59b2ba4893a785586b672786651992cba80c58d02dae7fe32c61c989`
  - `_DECISIONS/_REGISTER.md` at 189f205ff: `4306bd1094204552e3f5af448f1afb5928d57d58dc52775bdfee250972b70cf4`. The row `D-PEC-99` is at L116, status `RULED A / EFFECTIVE ON MERGE`.
  - `REMAINING_CENSUS.csv`: `b0e25361b4955b1a2689fa729b9727a2caa0efe8d3770cb0fd006af4ab445eb4`. `SEMANTIC_DECISION_ACCOUNT.csv`: `b240b38d940448a66b37752a1f2509ea4c6783f388c0a8d6cb0d3d21a465f7e2`. Both are unchanged between basis and head.
  - `ACTIVE_RELIANCE_HOLDS.csv`: `f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc` (header only). `pec_reliance_hold.py`: `b1712e4b6e9f1476c577afd9170a4dd078beaa95878fa5f3b6c46a17b548cd0e`.
  - Brief copy `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/RR3_D99_RETIREMENT_ACT.md`: `9f5702bd78384b9233751a50ec88aaa01e2372ad4d681eab400f5a1f593ce547`. I read it only for the write boundary.

## Overall verdict: **PASS WITH NOTES**

The act that PR #957 carries does exactly what the D-PEC-99 ruling and the proposal it incorporates grant, and nothing more:

- All 62 generator postimages reproduce byte for byte on a fresh export. They equal the candidate head and every hash tabled in the proposal.
- The closure check passes in both modes.
- The finite verification table holds on independent reruns.
- Every History line, exhibit block, gate and Part B carry-forward is true to the account and census.
- No lifecycle state, protected file or out-of-grant path changed.

Nothing here blocks the act. Note 1 records a merge precondition that the ruling places on HELP_HUMAN, not on the act.

## Findings

**1. NON-BLOCKING (merge precondition, outside the act's author scope): the ruling's graph consequence is not yet in the candidate.**
The ruling's Grant says: "In the act's PR, HELP_HUMAN adds the 'Absorbs … Part B items' sentences to graph rows S1, S2 and S4 of `HELP-HUMAN-PEC-20260925-POST-SCA005`." At 10feef34c, `projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md` contains 0 occurrences of "Absorbs as exact carry-forwards". `HANDOFF_STATE.md` discloses this truthfully ("NOT DONE here — HELP_HUMAN's, in the same PR"), and the RR3 brief forbids the act's author from writing either graph.
- Before merge, PR #957 needs HELP_HUMAN's sentences with exactly these keys:
  - S1: DEL-03-02-REM-016, DEL-03-03-REM-004, DEL-03-06-REM-004 (named for this correction only), DEL-04-05-REM-003
  - S2: DEL-02-07-REM-001..004
  - S4: DEL-04-01-REM-001, -002; DEL-04-02-REM-002; DEL-04-03-REM-002
- HELP_HUMAN's RS1 record is also still to come.
- Those additions create a new candidate revision. Under Root's merge rule, review must cover the actual final candidate. This verdict covers 10feef34c only.

**2. NON-BLOCKING: `FINAL_ROW_ACCOUNT.csv` keeps `HumanDecision=PENDING`. I judge that acceptable.**
The administrative grant says only that WORKING_ITEMS "sets `AppliedResult` in a copy of the account". The copy is byte-identical to the account apart from the 92 `AppliedResult` cells. I checked this by substituting `NONE` back into each cell of the raw file, which gives the account bytes exactly.
- Rewriting `HumanDecision` would have gone beyond the grant, and leaving it is the conservative reading. The owner decision is traceable: the ruling file and register row are on `origin/main`, and DEL-03-06-REM-004's `AppliedResult` quotes "Q1 a" and DEL-01-05's quotes "confirm F".
- One limit: the disclosure lives only in `HANDOFF_STATE.md` residual 2, not in the CSV. A reader of the CSV alone sees `PENDING` beside `APPLIED …`. This is informational; any fix would need its own authority.

**3. NON-BLOCKING (informational): the bound `verify_d99.py` silently keeps only the last `--allow-extra` flag.**
`--allow-extra` is declared `nargs='*'` with the default store action. The proposal's instruction "name each with `--allow-extra`" can therefore produce a spurious FAIL if the flag is repeated.
- Reproduced: act-mode verify on an export of generator commit 5066f895c, with three separate `--allow-extra` flags, gave `RESULT FAIL`. The same run with one `--allow-extra a b c` gave `RESULT PASS`.
- The failure mode is fail-closed (never a false PASS), and the act's recorded run used no `--allow-extra`. The script's bytes are bound by the ruling and cannot change under it.

**4. NON-BLOCKING: the SOW-count disclosure is accurate.**
`find projects/pec/execution -name ScopeOfWork.md` returns 34 at both 189f205ff and 10feef34c. That is 32 deliverable SOWs under `PKG-*/1_Working/` plus two D-PEC-98 candidate copies under `_Coordination/PEC_FIRST_SOWS_D98_PREP_2026-09-26/candidates/…/DEL-02-08_…` and `…/DEL-02-09_…`.
- `47bf0c1c7` added those two copies after the proposal's preparation basis `6281273fa`, which has exactly 32.
- All 34 give `PASS format=SOW_V1` before and after, with byte-identical output. The disclosure in `checks/COMMANDS.txt` and `HANDOFF_STATE.md` residual 1 is exact.

**5. NON-BLOCKING: `origin/main` advanced (PR #955, `6b48b6f26`). No granted path or pin is touched.**
- `git diff --name-only 189f205ff 6b48b6f26` lists 24 paths, and none intersects the candidate's 104 changed paths.
- The generator's pins are unchanged on current main: the 57 `_STATUS.md` preimages, `projects/pec/AGENTS.md`, the census and the account.
- `git merge-tree --write-tree 10feef34c origin/main` is clean (tree `57c4c43ed300…`).
- On a trial merge in a scratch clone:
  - G4 passes in CI mode and in diff mode (`--base 6b48b6f26`), with 130 manifests.
  - Entrypoints PASS.
  - Harness self-check exits 0.
  - Strict registers exit 1 with output byte-identical to the candidate's (0 errors, 28 warnings).
- Two things for downstream packets, neither affecting this act:
  - #955 changes `workflows/scope-of-work/WORKFLOW.md` from `d616865a…` (the proposal cites it as consulted) to `84dadde4c573…`, and it changes `docs/SPEC.md` §3.3/§3.4/§13. The S1, S2 and S4 packets that absorb the Part B texts should work from the current method.
  - #955 also routes a record-only notice to PEC (`projects/pec/execution/_Coordination/NOTICE_2026-09-26_PROJECT_SETUP_INCREMENTAL.md`).
- `task-management` `WORKFLOW.md` is unchanged at `d5e8eff5…`.

**6. NON-BLOCKING (informational): `checks/containment.out` was recorded at `c9ccfb645`, not at the head.**
It records 39 run-root files. The head adds `containment.out` itself, making 40. My recomputation at the head:
- 104 paths in total: the 62 grant paths, 40 run-root files, `FINAL_ROW_ACCOUNT.csv` and the brief copy.
- 0 HELP_HUMAN-owned paths and nothing outside the grant.

**7. NON-BLOCKING (informational): the manifest's `rollback` wording is loose.**
It says "Revert the retirement act's commit" (singular), but the act spans commits 5066f895c, c9ccfb645 and 10feef34c. The manifest's bytes are the proposal-tabled postimage `f077b995…`, and the proposal's §Rollback (a revert PR) governs. No action is proposed.

## Checks run (commands, exit codes, key output)

### 1. Basis
- `git merge-base --is-ancestor db9328789 189f205ff` exits 0: PR #943 is an ancestor. `189f205ff` is an ancestor of the head and of `origin/main`.
- Register row D-PEC-99 is present at 189f205ff L116.
- The ruling and the published proposal are present at 189f205ff, with the hashes listed above.
- Bound scripts at 3b0231ecc and at 10feef34c:
  - `gen_d99.py` hashes to `1fad023951f8fca887974452a6b65cfd312b74c1312997ac99a5260b64ee7237` in both the run root and `_TaskManagement/TM_PEC_REMAINING_RETIREMENT_2026-09-26/`.
  - `verify_d99.py` hashes to `c1d50dfd267894f8602b6b4497136e41a6fa2cf5f9ffe614efdb4314ea791865` in both.
  - The TM copies have the same hashes at 189f205ff.

### 2. Reproduction on a fresh export
- I exported `3b0231eccf65148930d37de91ba545d35f036ff6` with `git archive | tar -x` into the scratch directory. It is the parent of 5066f895c, and its parent is 189f205ff.
- CPython 3.13.7. Command: `python3 <export>/…/REMAINING_RETIREMENT_D-PEC-99_2026-09-26/gen_d99.py --repo <export> --act-date 2026-09-26 --ruling-date 2026-09-26 --decision D-PEC-99 --q1 s1`
  - `--check-only` exits 0 with `CHECK write_set 62`, `CHECK status_sections_removed 57`, `CHECK account_keys 92 {CLOSED_ON_RECORD 9, EXHIBIT_A_D83E 71, EXHIBIT_B_CARRY_S1 4, S2 4, S4 4}`.
  - The act exits 0 with `WROTE 62 files`.
  - A second run exits 1 with `FAIL preimage …DEL-00-02…`, so it fails closed.
- Byte comparison of all 62 written paths: reproduced tree, export of 5066f895c, `git show 10feef34c:<path>` and the generator's own POST line all agree, with 0 mismatches.
- `diff -rq reproduced gen-export` differs only by the three run-root outputs committed in 5066f895c (`closure_post.out`, `gen_act.out`, `posts_vs_proposal.out`).
- Against the proposal tables:
  - All 57 `_STATUS.md` preimages (at 189f205ff) and postimages (at 10feef34c) equal the tabled values.
  - `AGENTS.md` = `df9196d1…25eb8`.
  - Exhibit = `69b646f8…f45e`, byte-identical to `DRAFT_D-PEC-99_EXHIBIT_MOVED_ITEMS.rendered.md`.
  - Manifest = `f077b995…aeef`.
  - Root notice = `e1b3929f…8add`.
  - Runtime notice = `20aecce9…6aa6`.
  - Result: 62/62.
- The recorded `gen_act.out` POST, CHECK and WROTE lines are identical to my run.

### 3. Closure check
- `verify_d99.py --repo <pre export> --account-only` exits 0 with `RESULT PASS` (`held=73`). Its CHECK lines equal the recorded `checks/closure_pre.out`.
- Act mode on my reproduced tree: `--repo <reproduced> --pre <fresh export of 3b0231ecc> --decision D-PEC-99 --q1 s1` exits 0 with `RESULT PASS`. It reports changed 58, new equal to the 4 grant paths, 66 `_STATUS.md` with 0 surviving headings, 57 exact edits and protected paths unchanged. Its CHECK lines equal the recorded `checks/closure_post.out`.
- Act mode on the export of 5066f895c: exit 1 without `--allow-extra`, because the three committed run-root outputs count as new. With `--allow-extra` naming those three in one list it exits 0 with `RESULT PASS` (see Finding 3).

### 4. Finite verification table
I ran each check in scratch clones at 189f205ff and 10feef34c.

| Check | Result |
|---|---|
| Strict registers (`validate_decomposition_registers.py --strict projects/pec/execution`) | exit 1 before and after; 0 errors, 28 warnings; outputs byte-identical (`cmp`) |
| SOW validation, each file from `find` | 34/34 PASS before and after; outputs identical (Finding 4) |
| G4 manifest, CI mode | exit 0, `G4 PASS (CI mode)`, 129 manifests |
| G4 manifest, diff mode (`--base 189f205ff --head HEAD --added-manifests-only`) | exit 0, `G4 PASS (diff mode)`; 104 changed paths, 1 on the instruction surface. INFO only: over-declaration notices for `projects/pec/AGENTS.md` and the two notices |
| Instruction entrypoints (`validate_instruction_entrypoints.py .`) | exit 0 `PASS` before and after; identical |
| Pytest (`python3 -m pytest -q -p no:cacheprovider tools/validation/test_validate_instruction_entrypoints.py tools/validation/test_validate_pec_loop_receipts.py`) | `33 passed` |
| Harness self-check (`harness.py self-check`) | exit 0 before and after; outputs byte-identical, so no new finding cites a target path |
| Receipts validator (`validate_pec_loop_receipts.py --repo-root .`) | exit 0 `VALID … frozen through Receipt-166` before and after; only the clone path differs |
| `taskmgmt.py validate` on `REGISTER.csv` / `REGISTER_CLOSED.csv` | PASS (9 rows) / PASS (16 rows) before and after; identical |
| Containment (`git diff --name-status 189f205ff...10feef34c`) | 104 paths: 46 A, 58 M; details in section 8 |
| `git diff --check 189f205ff...10feef34c` | exit 0, no output |
| Reliance holds, my own run (`pec_reliance_hold.py --operation candidate-validation`, from `projects/pec`, all 63 `checks/hold_targets.txt` targets) | 63/63 ALLOW |
| Reliance holds, recorded | `hold_dispatch-for-production.tsv` and `hold_rely-for-production.tsv` each 63/63 ALLOW |

- The recorded `checks/pre_*.out` and `post_*.out` pairs are each byte-identical, and the recorded `post_strict.out` matches my output apart from its trailing `exit=1` annotation.
- `FINAL_ROW_ACCOUNT.csv` hashes to `c2f20bed…81c9`, equal to the value recorded in `checks/final_account.out`.
- The run root's `checks/COMMANDS.txt` and `HANDOFF_STATE.md` support every claim in the proposal's table.

### 5. Semantics
I wrote an independent parser for this, not the bound verifier.
- **Census against the removed blocks.** For all 57 files, the pre-act Remaining section holds exactly the census keys, in census order, with matching item counts. Each `- [ ]/[x] KEY — text` / `Depends:` / `(gated: …)` triple equals the census `ItemText`, `Depends`, `GateMarkers` and `Checkbox`. 0 mismatches.
- **Postimage shape.** Each postimage is the preimage minus the section, with only `**Last Updated:** 2026-09-26` changed and exactly one line appended as the last History entry. No `^## Remaining` heading remains in any of the 66 deliverable `_STATUS.md`.
- **History lines.** All 57 match the generator's fixed form. They name exactly each file's keys, in order, and every one of the 89 live keys maps to the destination its account `DestinationClass` implies (with `OWNER_DECISION` resolved to S1 under Q1 (a)). 0 errors. The exhibit pointer appears if and only if a key moved.
  - Part A keys read "the `D-PEC-83` E evidence-inquiry set in the D-PEC-99 exhibit (still unselected)".
  - Part B keys read "the D-PEC-99 exhibit, for exact carry-forward into this deliverable's `ScopeOfWork.md` by work-graph node Sn", with the correct node.
  - Closed keys read "closed on the record cited in the account".
- **Exhibit.** 83 blocks, equal to the 83 moved keys.
  - Part A holds 71 items: 70 live plus DEL-01-05-REM-003.
  - Part B holds S1 4 (DEL-03-02-REM-016, DEL-03-03-REM-004, DEL-03-06-REM-004, DEL-04-05-REM-003), S2 4 (DEL-02-07-REM-001..004) and S4 4 (DEL-04-01-REM-001, -002, DEL-04-02-REM-002, DEL-04-03-REM-002). This equals the proposal's absorption table with Q1 (a).
  - Every block's text, `Depends:` and `Gate:` equal the census exactly, and every gate begins `(gated:`, so no Part A or Part B item lost its gate.
  - Each Part B "Carry-forward input for Sn" text equals the account's `DestinationExactText` exactly (12/12).
  - The heading lifecycle equals the census `Lifecycle` for every block.
- **DEL-01-05.** The census text, Depends and gate for REM-001..003 equal the frozen carrier `PROPOSED_ITEMS.csv` (`91be3621…9b75` at 189f205ff). The exhibit's provenance line quotes that carrier's `PacketApplicationGate` and `PreparationState`. DEL-01-05-REM-003 is in Part A, and no DEL-01-05 path appears in the diff.
- **Closed set.** The 9 closed keys are DEL-01-03-REM-001..003, DEL-06-04-REM-001, DEL-07-02-REM-001, DEL-07-04-REM-001, DEL-07-05-REM-001, DEL-01-05-REM-001 and -002. This is exactly the proposal's (c) set.
- **AGENTS.md.** I rebuilt the postimage from the preimage by replacing L261–272 with the proposal's `text` block (`{N}`=D-PEC-99) and the `amended:` line with the tabled line (`{D}`=2026-09-26, `{N}`=D-PEC-99). The rebuilt file equals the head bytes exactly, so nothing else changed.

### 6. Protected files
- `**Current State:**` is identical at 189f205ff and 10feef34c for all 66 deliverable `_STATUS.md`, and it equals the proposal's State column for the 57.
- `grep` of the changed-path list for DEL-00-01, DEL-00-03, DEL-08-02, DEL-10-01, DEL-01-05, `ScopeOfWork.md`, `Dependencies.csv`, `_CONTEXT.md`, `_REFERENCES.md`, `MEMORY.md`, `_DEPENDENCIES.md`, `_Decomposition/`, `_REGISTER.md`, `checkpoint_snapshots/`, `_Evaluation/`, `projects/pec/loop/`, `projects/pec/init/`, `projects/pec/v2/`, `docs/PRD.md`, `software-workflow.json`, `_run_records/` and `WorkGraphs/` returns no match (exit 1).
- The only paths outside `projects/pec/` are the manifest and the two notices.

### 7. FINAL_ROW_ACCOUNT.csv
- 92 rows, with the same header as the account.
- Only `AppliedResult` differs, and the raw bytes are otherwise identical. Line endings and quoting are preserved.
- Each value is true to the act:
  - MOVED_EXHIBIT_A for 70 live keys, plus 1 frozen key described as "never applied … no DEL-01-05 file was written".
  - MOVED_EXHIBIT_B_S1/S2/S4 at 3+1, 4 and 4, where the +1 is DEL-03-06-REM-004 citing "Q1 a".
  - CLOSED_ON_RECORD for 7 live keys and 2 frozen keys.
  - The cited exhibit hash prefix `69b646f8481f` and commit `5066f895c` are correct.
- `HumanDecision=PENDING` on all 92 rows is judged in Finding 2.

### 8. Write boundary and origin/main
- The candidate diff (104 paths) is 57 `_STATUS.md` M, `projects/pec/AGENTS.md` M, exhibit A, manifest A, two notices A, 40 run-root files A, `FINAL_ROW_ACCOUNT.csv` A and the brief copy A. Nothing else.
- This fits the ruling's grant, the proposal's run root and account-closure clauses, and the brief's write boundary.
- For `origin/main` `6b48b6f26`, see Finding 5: no overlap, clean merge, and checks pass on the trial merge.

Relevant paths:
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-99_remaining_retirement_proposal_2026-09-26.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-99_RULING_2026-09-26.md`
- `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/wt-rr3/projects/pec/execution/_Coordination/REMAINING_RETIREMENT_D-PEC-99_2026-09-26/`
- `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/wt-rr3/projects/pec/execution/_Coordination/_TaskManagement/TM_PEC_REMAINING_RETIREMENT_2026-09-26/FINAL_ROW_ACCOUNT.csv`
- `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/wt-rr3/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-99_REMAINING_RETIREMENT_2026-09-26/EXHIBIT_MOVED_ITEMS.md`
- Scratch evidence (outputs of my runs): `/private/tmp/claude-501/d99v.6vKDgU/`

No human ruling is recorded or implied by this verdict.
