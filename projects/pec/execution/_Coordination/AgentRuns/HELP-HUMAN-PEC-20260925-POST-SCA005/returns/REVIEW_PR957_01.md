# Review 01 of PR #957 (D-PEC-99 Remaining retirement act), transcribed

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high), dispatched by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed verbatim from the host subagent transcript.
- **Reviewed head:** `f826c56c2577e03fe0d4b07b531a6e3c81426395` (base `origin/main` `cb85f85d1`). Repairs: `ecb745294`; this file is added after that.
- **SHA-256 of the report text below (UTF-8, trailing newline stripped):** `76cc1152fdef68bd879141ff2c5b26be3d0dc5dd9ba1fefe78a6a127d1516e56`.

## Report (verbatim)

## Verdict: PASS WITH NOTES

PR #957 at head `f826c56c2577e03fe0d4b07b531a6e3c81426395` (base `origin/main` `cb85f85d1`). I found nothing blocking. The act does what D-PEC-99 A grants, and nothing more. The findings below are record-currency issues in HELP_HUMAN's graph edits. I modified no files; every run used `git archive` exports in the scratchpad.

## What I checked, with evidence

**Basis hashes (recomputed with `shasum -a 256`)**
- Ruling: `3e34403a…c989`.
- Proposal: `29e2ff57…6c79`.
- `gen_d99.py`: `1fad0239…7237`, identical in `3b0231ecc` and at head.
- `verify_d99.py`: `c1d50dfd…1865`, identical in `3b0231ecc` and at head.

**1. Reproduction: 62/62 byte-identical**
- I exported `3b0231ecc` and ran the bound generator with CPython 3.13.7: `--act-date 2026-09-26 --ruling-date 2026-09-26 --decision D-PEC-99 --q1 s1 --reproduction --render-to <tmp>`.
- It exited 0 with `CHECK write_set 62`, `status_sections_removed 57` and `account_keys 92` (closed 9, A 71, B S1 4 / S2 4 / S4 4).
- All 62 rendered files `cmp` equal to the PR head export.
- All 62 hashes appear in the proposal's tables.

**1b. Closure check in act mode: `RESULT PASS`, exit 0**
- `--repo` was the head export. `--pre` was the `3b0231ecc` export plus main's delta `189f205ff..cb85f85d1`, applied with `git apply`.
  - The delta is needed because the checker's roots include `docs/`, `execution/` and the sibling `_Coordination` folders, which #955/#956 touched.
- Every extra path went after a single `--allow-extra`: the run root, `FINAL_ROW_ACCOUNT.csv`, the RR3 brief and return, both graphs, and `projects/pec/docs/STATUS.md`.
- Results:
  - 66 `_STATUS.md` scanned, 0 sections left.
  - 57 exact edits.
  - Changed paths: 58, matching the grant.
  - New paths: 4, matching the grant.
  - No protected path changed.

**2. Containment: PASS**
- The `origin/main...HEAD` diff has 110 paths:
  - the 62 granted paths;
  - 42 run-root files;
  - `FINAL_ROW_ACCOUNT.csv`;
  - the RR3 brief and return;
  - the two graphs;
  - `projects/pec/docs/STATUS.md`.
- Nothing else is in the diff.
- The merge brought only main's changes: `git diff a65defea5 f826c56c2` is byte-identical to `git diff 189f205ff cb85f85d1`, and `git diff 189f205ff a65defea5` is byte-identical to `git diff cb85f85d1 f826c56c2`.

**3. HELP_HUMAN's records: PASS, with notes below**
- Rows S1 (L61), S2 (L62) and S4 (L64) of `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md` carry the sentence in the "Needs / why" cell.
- The keys exactly match exhibit Part B (`EXHIBIT_MOVED_ITEMS.md` L725–863):
  - S1: DEL-03-02-REM-016, DEL-03-03-REM-004, DEL-03-06-REM-004 "(for DEL-03-06, this correction only)", DEL-04-05-REM-003. The parenthetical satisfies ruling Q1 a.
  - S2: DEL-02-07-REM-001..004.
  - S4: DEL-04-01-REM-001, DEL-04-01-REM-002, DEL-04-02-REM-002, DEL-04-03-REM-002.
- RS1 (L74) cites the ruling and says the act "is in PR #957".
- `docs/STATUS.md` L137–145 and L277–286 no longer say the sections remain, and make no claim of a merge.

**4. Instruction change: PASS**
- `projects/pec/AGENTS.md` hashes to `df9196d1…25eb8`; the base was `4400c4e9…139c`.
- The diff is only the `amended:` line (L6) and the Remaining paragraph (L261–276). Both match the proposal's text (L162–177 and L180) with `{N}`/`{D}` substituted.
- The account folder cited at L265 exists.
- Tranche manifest: `G4 PASS (CI mode)` exit 0, and `G4 PASS (diff mode)` with `--base origin/main --head HEAD --added-manifests-only` exit 0.
- Instruction entrypoints PASS; pytest 33 passed.

**5. Every-PR checks: PASS**
- Strict registers: exit 1 at both base and head, byte-identical output (0 errors, 28 warnings).
- `validate_pec_loop_receipts.py`: VALID.
- Harness self-check: exit 0, and its output is identical to the recorded `checks/pre_harness.out`, so there are no new findings.
- `git diff --check origin/main...HEAD`: clean.
- PR CI: all required jobs SUCCESS or SKIPPED; the PR is MERGEABLE.

**6. Limits: PASS**
- The `_STATUS.md` edits touch only the section, `Last Updated` and one History line, so no lifecycle state changed.
- No write to any SOW, `MEMORY.md`, `Dependencies.csv`, `_CONTEXT.md`, `_REFERENCES.md`, `v2/`, PRD, decomposition, `loop/`, `init/`, `checkpoint_snapshots/` or `_Evaluation/` file.
- Every mention of CHECKING is a limit statement or original item text. Nothing prompts the owner about CHECKING.
- `FINAL_ROW_ACCOUNT.csv` differs from the account (`b240b38d…`) only in `AppliedResult`: 71 A, 9 closed, 12 B.

## Findings

**NON-BLOCKING**

1. **The POST-SCA005 graph's current-state lines are stale at head.** HELP_HUMAN edited this graph in the PR but left these lines behind the ruling PR's merge (#954, `189f205ff`):
   - L78: "Ready after the ruling PR merges: the S3 act".
   - L128: checked basis is still `0583e36ff`.
   - L130–131: "Merge the ruling PR … Then dispatch … the retirement act (RR3)".
   - L133: "Local or unmerged work: the ruling PR".
   - L134: the handed-back managers omit the RR3 manager, whose brief and return sit in this run folder.

   This contradicts RS1 at L74 and the retirement graph at L37–38. It does not affect the grant, but it misleads recovery.

2. **RR3 is marked COMPLETE before its own completion check is met.** L32 of `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260926-REMAINING-RETIREMENT/WORK_GRAPH.md` says "COMPLETE with PR #957", but that row's completion check includes "review", which is this PR review, and the PR is unmerged.
   - It does not claim a merge, and L38 correctly lists PR #957 as unmerged work.
   - The state would be false if the PR closed unmerged. Other COMPLETE rows use "merged as …".

**NOTE**

3. **Missing sentence separator.** Each "Absorbs …" sentence runs on from the previous text with no period: POST-SCA005 graph L61 "packet per batch Absorbs", L62 "next scope change Absorbs", L64 "exact rows Absorbs".
4. **Retirement graph route line is stale (pre-existing).** L24 says items are carried by "S2, S4, D1". The ruled outcome is S1, S2 and S4, and D1 carries none. The same wording is in the bound manifest's `scope_limits` (L55). The manifest's bytes are pinned, so leave them.
5. **`docs/STATUS.md` L404 is stale (pre-existing).** It records `AGENTS.md` amendments only through D-PEC-94 and omits the SCA-006 and D-PEC-99 amendments.
6. **`HumanDecision=PENDING` in all 92 rows of `FINAL_ROW_ACCOUNT.csv`.** This is disclosed at retirement graph L40 and in the RR3 return, but could be misread as open owner decisions.
7. **Extra helper scripts in the run root.** It holds `check_posts_vs_proposal.py`, `containment.py`, `make_final_account.py`, `run_checks.sh` and `run_holds.sh`, beyond the proposal's list. They are under default-writable `_Coordination/**` and inside the Containment row's "run root".
8. **Reproducing the closure check after the main merge needs an adjusted pre tree.** Any rerun must build `--pre` as the `3b0231ecc` export plus main's delta (or run before merging main), or the check fails on #955/#956 paths. The in-run records correctly describe the pre-merge run.

## Files
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-99_RULING_2026-09-26.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-99_remaining_retirement_proposal_2026-09-26.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-99_REMAINING_RETIREMENT_2026-09-26/EXHIBIT_MOVED_ITEMS.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260926-REMAINING-RETIREMENT/WORK_GRAPH.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/docs/STATUS.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/AGENTS.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/docs/governance_harness/tranche_manifests/PEC-REMAINING-RETIREMENT-20260926.yaml
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_TaskManagement/TM_PEC_REMAINING_RETIREMENT_2026-09-26/FINAL_ROW_ACCOUNT.csv

## Disposition (HELP_HUMAN)

| Finding | Disposition |
|---|---|
| NON-BLOCKING 1 (POST-SCA005 graph current-state lines) | Repaired in `ecb745294`: Order line names the S3 act as in review (PR #958); checked basis `cb85f85d1`; next work, unmerged work and handed-back managers (adds RR3 and S3A) are current |
| NON-BLOCKING 2 (RR3 marked COMPLETE before review) | Repaired: RR3 is `ACTIVE — in PR #957, awaiting review and merge`; the next graph update after merge marks it COMPLETE |
| NOTE 3 (missing sentence separators) | Repaired: a period precedes each "Absorbs …" sentence |
| NOTE 4 (retirement graph route line) | Repaired: the route line names S1, S2 and S4 as ruled, D1 none, and notes the manifest keeps its bound wording |
| NOTE 5 (`docs/STATUS.md` `AGENTS.md` amendment line) | Repaired: names the SCA-006 tranche and the `D-PEC-99` paragraph replacement |
| NOTE 6 (`HumanDecision=PENDING`) | No change: bound by the grant (only `AppliedResult`), disclosed in the retirement graph and the RR3 return |
| NOTE 7 (helper scripts in run root) | No change: inside the run root under default-writable `_Coordination/**` |
| NOTE 8 (closure-check rerun after the main merge) | Recorded: a rerun builds `--pre` from `3b0231ecc` plus main's delta, as this review did |
