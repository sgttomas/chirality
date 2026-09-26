# Review 01 of PR #958 (D-PEC-98 first SOWs act), transcribed

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high), dispatched by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed verbatim from the host subagent transcript.
- **Reviewed head:** `b73fc42dc60133a0a83cb57439d74c5fc82e5280` (base `origin/main` `22502e059`). Repairs: `29ccf391e`; this file is added after that.
- **SHA-256 of the report text below (UTF-8, trailing newline stripped):** `3256c2baea8758c9f3fcda724f19601f6d93d7fd192c0fb457a39fe731b26322`.

## Report (verbatim)

**Verdict: PASS WITH NOTES.** I found nothing blocking. I reviewed PR #958 at head `b73fc42dc60133a0a83cb57439d74c5fc82e5280` against base `22502e059`. I recomputed every hash with `shasum -a 256` and ran the checks myself, in `git archive` exports and in detached scratch worktrees (both removed afterwards). I modified no file. Interpreter: CPython 3.13.7 with `PYTHONDONTWRITEBYTECODE=1`.

## Results by item

**1. Re-pin — PASS**
- **Starting bytes.** The prepared originals hash as bound: candidates `03cce13f…dc0a` and `aafb54fd…188b`, and `apply_d98.py` `19c2ecb6…419e`.
- **Contracts.** I diffed each prepared candidate against its written contract. Each shows exactly three hunks, the three places question 4 allows:
  - the frontmatter pin, line 5;
  - the Purpose paragraph "The accepted basis is …" (DEL-02-08 lines 19–27; DEL-02-09 lines 20–28);
  - the "Observation commit." clause (DEL-02-08 lines 32–43; DEL-02-09 lines 33–42).
- **`apply_d98.py`.** The only changes are the two `TARGETS` values (lines 29 and 31) and the four register/PRD `PINNED` values (lines 35–38). They equal `git show 189f205ff` of the four files and HEAD: `9374c21f…8eb1`, `94ee5d18…9805`, `1d24a4b8…916e`, `ae49b806…3fbe`. The four deliverable-file pins are unchanged.
- **`verify_d98_state_claims.py`.** The only change is an inserted `PIN2` block at lines 86–102. Every original check is kept.
- **Reruns at the PR head, after D-PEC-99:**
  - `verify_d98_quotes.py`: exit 0, `RESULT PASS 69/69`. This includes the two `projects/pec/AGENTS.md` quotes, against the post-D-PEC-99 AGENTS.md (`df9196d1…`).
  - `verify_d98_state_claims.py`: exit 0, `RESULT PASS 56/56`.

**2. Byte identity — PASS**
- The written contracts equal the run-root candidates: `2319661b…dd26` and `eab18e17…6f5e`.
- The `_STATUS.md` preimages at base and at `189f205ff` are `d80800a4…` and `3e14313c…`. The postimages are `4341d6b2…04fe` and `e67be587…1056`, matching add-on S's table. The diff is exactly the slot rule.
- The validator prints `PASS format=SOW_V1` for both.
- Checklists:
  - 21 and 17 items; reruns are byte-identical and equal the run-root JSON.
  - After normalising, they equal the prepared checklists `54c84487…` and `2f495a54…`. The only differences are the contract hash and line numbers shifted by +10 (DEL-02-08) and +8 (DEL-02-09).
- Boundary owners: exit 0 with 1 checked and 0 failing for each contract. The `NOT_CHECKABLE` items are REQ-009/010/011 (DEL-02-08) and REQ-007/008/009 (DEL-02-09). My JSON equals the run-root `boundary_*.json`.
- The 66 run-root hash rows in `MANIFEST.md` all check OK.
- Add-on S ran after the verifier verdict. The S TASK started at HEAD `1e4088623`, the verdict commit.

**3. Containment — PASS**
- The diff against base is exactly: the two `ScopeOfWork.md`, the two `_STATUS.md`, 67 run-root files, the brief and the return, both work graphs, `_REGISTER.md` and `docs/STATUS.md`.
- It contains no `MEMORY.md`, register CSV, dependency, context, decomposition, `v2/**`, PRD, AGENTS.md or foreign path.
- The main merge `467c38a93` brought only main's changes:
  - `git show --remerge-diff` is empty.
  - Its changed paths equal main's 136 paths since merge base `6b48b6f26`, and every blob equals main's copy.
  - Of those, 57 are `_STATUS.md`, none of them DEL-02-08 or DEL-02-09.

**4. HELP_HUMAN's records — PASS**
- **Lifecycle census.** Recount of the 66 `PKG-*/1_Working/DEL-*/_STATUS.md`: 28 OPEN / 28 INITIALIZED / 4 CHECKING (DEL-00-01, 00-03, 08-02, 10-01) / 2 IN_PROGRESS (DEL-01-03, 01-05) / 4 RETIRED (DEL-06-04, 07-02, 07-04, 07-05). None is ISSUED, and no `## Remaining` section remains. This matches `projects/pec/docs/STATUS.md:124-130`.
- **RR3.** The COMPLETE claim is true: `gh` shows PR #957 MERGED at `22502e059`.
- **Other records, all accurate:**
  - S3 row: POST-SCA005 `WORK_GRAPH.md:63`.
  - Order: `:81`.
  - Carried-disclosure section: `:118-120`.
  - Current state: `:132-137`.
  - D-PEC-88 trace line: `:184`.
  - Retirement graph: `:32` and `:37-39`.
  - Register row note: `_REGISTER.md:115`.
  - Open-list bullet: `docs/STATUS.md:249-254`.
- Nothing claims PR #958 has merged. I found no stale statement that Remaining sections still exist.

**5. Every-PR checks — PASS**
- Strict registers: exit 1, 0 errors, 28 warnings. Output is byte-identical at head and base.
- `validate_pec_loop_receipts.py`: exit 0, VALID at both. The output is identical once the worktree path is normalised.
- Harness self-check: exit 0 at both, byte-identical.
- `git diff --check origin/main...HEAD`: clean.
- CI on the head passes and GitHub reports the PR as CLEAN and mergeable.

**6. Limits — PASS**
- The only lifecycle change is add-on S's `OPEN → INITIALIZED`.
- CON-005 stays open (DEL-02-08 line 198; AX-010).
- No registry act, CHECKING, ISSUED or REVIEW gate occurs.
- CHECKING appears only in the census count and in negative limit statements. Nothing prompts the owner about it.

## NON-BLOCKING
None beyond the notes below.

## NOTES
1. **The post-D-PEC-99 rerun is not recorded in the PR.** Brief S3A says to rerun the quote and state-claims checks if D-PEC-99 merges first. `HANDOFF_STATE.md:62` and the return (item 4) still say D-PEC-99 was not merged at hand-back, and no later record shows the rerun. My rerun passes (69/69 and 56/56). Suggest the graph or central receipt records this review's result.
2. **The carried-disclosure section is incomplete (POST-SCA005 `WORK_GRAPH.md:118-120`).** It carries verifier notes 1 and 2 but leaves out two related items:
   - The companion point the verifier and `HANDOFF_STATE.md` raised: lines 29–31 of both contracts ("…did not exist at `c9e5cd87d`") no longer say that `c9e5cd87d` is the former pin.
   - The ruling's own disclosure: the sentence that "`_CONTEXT.md` and `_REFERENCES.md` name revision 1.5 and PRD v2.3" is true only of the two file types together (DEL-02-08 line 44, DEL-02-09 line 43). At `53145aaeb` the DEL-02-08 `_CONTEXT.md` names only revision 1.5.
   Both are durable elsewhere (the verdict, `HANDOFF_STATE` and the ruling), but the later revision would find them faster in the graph.
3. **Contract wording already disclosed, correctly left alone.** Question 4 allowed only the three moves, so the act did not change:
   - DEL-02-08 `ScopeOfWork.md:111`, which still calls `c9e5cd87d` "the decomposition pin".
   - The observation clause's list of re-verified loci, which leaves out `AnticipatedArtifacts` and DL-4. I confirmed "one per feed kind" is verbatim at `189f205ff`.
4. **Minor wording in the Order list.** POST-SCA005 `WORK_GRAPH.md:81` puts "The retirement act merged as PR #957" in the "In review" bullet rather than under Done. It is true, just oddly placed.
5. **README census is superseded.** `projects/pec/README.md:44-45` still carries the census "(2026-09-25): 30 OPEN / 26 INITIALIZED". It is dated, so it is not false, but it is now superseded. The D-PEC-88 trace line (`:184`) names only STATUS and does not say README was left unchanged.
6. **The added state-claim checks go slightly past the literal wording.** `verify_d98_state_claims.py:86-102` adds, beyond the register hashes: PRD v2.4, revision 1.6 `current_basis`, the `_LATEST.md` record, pin ancestry, and "differs at `53145aaeb`". These support the new observation clause, and every original check is kept.
7. **Stale comment.** `apply_d98.py:33` still says "(values at origin/main 53145aaeb)". `REPIN.md` discloses this.
8. **Base moved after the candidate.** Remote `main` is now `6128f8b85` (Root PR #959, five commits past `22502e059`). Under `projects/pec` it adds only `NOTICE_2026-09-26_DEPENDENCY_FOLLOWUPS.md`. It touches no pinned file, validator, harness, `scope-of-work` or scaffolding path, so none of my results change. The graphs' checked basis (`22502e059`) remains a truthful statement of what was checked.

## Relevant paths
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser/ScopeOfWork.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser/ScopeOfWork.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/SOW_INIT_D98_2026-09-26/ (REPIN.md, apply_d98.py, verify_d98_state_claims.py, HANDOFF_STATE.md, MANIFEST.md)
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260926-REMAINING-RETIREMENT/WORK_GRAPH.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/docs/STATUS.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/README.md

My rerun outputs are in /private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/ (quotes_head.out, state_head.out, strict2_*.out, rcpt2_*.out, harn2_*.out).

## Disposition (HELP_HUMAN)

| Finding | Disposition |
|---|---|
| NOTE 1 (post-D-PEC-99 rerun not recorded) | Repaired in `29ccf391e`: the S3 row records the rerun (69/69, 56/56) and cites this review |
| NOTE 2 (carried disclosures incomplete) | Repaired: the graph's carried section adds the lines 29–31 point and the ruling's context/reference sentence disclosure |
| NOTE 3 (contract wording left alone) | No change: question 4 allowed only three moves; carried for a later owner-authorized revision |
| NOTE 4 (Order placement) | Repaired: the retirement act is under its own "Done" bullet |
| NOTE 5 (README census) | Repaired: README's dated census reads 2026-09-26, 28 `OPEN` / 28 `INITIALIZED`; the D-PEC-88 trace names it |
| NOTE 6 (extra state-claim checks) | No change: they support the re-pinned observation clause and keep every original check |
| NOTE 7 (stale comment in `apply_d98.py`) | No change: the script's bytes are the re-bound act script; `REPIN.md` discloses it |
| NOTE 8 (base moved to `6128f8b85`) | Recorded; if CI asks for a base update, HELP_HUMAN merges main and confirms nothing pinned changed |
