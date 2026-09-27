# Review 01 of PR #992, transcribed

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high) dispatched by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed from the host subagent transcript (verbatim apart from any disclosed whitespace normalization).
- **Reviewed head:** `44488316148a4dd6b5f5d8f95c4560e47d16d615`. The repairs listed under Disposition and this file follow that head.
- **SHA-256 of the report text below (UTF-8; the report text between the blank line after "## Report (verbatim)" and the blank line before the final "## Disposition", with no trailing newline):** `41ae533503c505655887f648c83fcd666e96686928019e54726cc108f9c64230`.

## Report (verbatim)

# Review of PR #992 (D-PEC-103 act) at head 44488316148a4dd6b5f5d8f95c4560e47d16d615

**Verdict: PASS WITH NOTES.** I found nothing blocking and nothing non-blocking. There are 6 notes. The product writes match the grant exactly, the checks reproduce at the head, the steps ran in the ruled order, and the run root is intact.

**How I checked.**
- I read these first: `agents/AGENT_TASK.md`, root `AGENTS.md`, `projects/pec/AGENTS.md`.
- I exported the head and `origin/main` with `git archive` into a `mktemp -d` under the session scratchpad, with `TMPDIR` set to it.
  - For the git-dependent tools I gave each export a scratch-local `.git` that borrows the repository's objects (alternates). No repository ref or index was touched.
  - I removed the export when I finished. I made no edits, no git writes and no checkout.
- The reliance-hold preflight (`candidate-validation`) returned ALLOW with exit 0 on all 5 written paths. The holds register has a header and no rows.
- Python was CPython 3.13.7 with `PYTHONDONTWRITEBYTECODE=1`.

**Pinned inputs recomputed.**
- Proposal: `cfc2e65d…5417`.
- Brief: `bb0d6e31…8d6b`. The copy at `AgentRuns/…/briefs/K2A_D103_SOW_ACT.md` is the one file and matches the pin.
- Ruling: `67ff8f1e…dfa2`.
- Register: `fe2cc825…45ea`. It has a D-PEC-103 row and the D-PEC-102 reservation row.
- Prep `SHA256SUMS` (`09f637d4…`): 66 entries, all OK.

## 1. Product writes: match the grant
- New contracts:
  - DEL-08-06 `ScopeOfWork.md` = `aecc513161c1…50826`
  - DEL-10-13 `ScopeOfWork.md` = `c7743ee2ab7d…56633`
- DEL-10-13 `_DEPENDENCIES.md`:
  - preimage on main `5087e581…eb63`, head `609aa807710f…65693`;
  - the diff is exactly one added line, the tabled C-08 bullet, at line 7 inside `## Dependency Tracking Mode`. No heading was added and no other byte changed.
- The two `_STATUS.md` files:
  - DEL-08-06 `73e21846…` → `75366b6b…a127`; DEL-10-13 `c7a5705d…` → `3771d526…e567`;
  - each diff is `Current State: OPEN→INITIALIZED` plus one history line, `- 2026-09-26 — State set to INITIALIZED (TASK+status-advance)`;
  - `Last Updated` was already 2026-09-26, so nothing else changed.
- There is no `MEMORY.md` in either folder.

## 2. Verification reproduced at the head
- **Validator:** `PASS format=SOW_V1 target=…` ×2, exit 0.
- **Checklists:** run twice each, all exit 0, 17 and 19 items. Hashes `2227dbeb…9641` and `8e07ff3e…ba30`: the reruns and the run-root JSONs are byte-identical.
- **Boundary owners:** exit 0, "boundary requirements checked: 1 … contracts failing: 0" each, 0 `NOT_CHECKABLE`. JSONs `b2e8ee78…679f` and `d0197ec9…7879` equal the run root.
- **Run-root verifiers:**
  - `verify_k2_quotes.py`: `RESULT PASS 137/137`, "DEP rows citing this contract: 0" ×2;
  - `verify_k2_state_claims.py`: `RESULT PASS 482/482`;
  - `check_cited_ids.py`: `RESULT PASS 0/0`;
  - `scan_old_s2_text.py`: `RESULT PASS stale=0 current=43`.
- **Strict registers:** exit 1, 0 errors, 26 warnings, all `XRG-013`. The output is byte-identical to `origin/main`.
- **Every-PR checks:**
  - harness self-check: exit 0, identical to main;
  - receipts validator: exit 0, identical except the export path;
  - closure: exit 0, 0 bidirectional pairs, no cycles; `closure_summary.json` and all CSVs identical to main apart from the embedded export path.
- **Pins of `apply_k2.py`:** 17/17 at main and 14/17 at head. The 3 that differ are exactly the S ×2 and C8 postimages, as `VALIDATION.md` says.
- **Run-root evidence:** `strict_`, `harness_` and `receipts_` outputs `{postA,postC8,final,final2}` are each byte-identical to `*_pre.out`.
- **Reliance-hold evidence:** `reliance_hold_dispatch.out` (ALLOW ×5) and `reliance_hold_fanin.out` (ALLOW ×5) are present, with the register and script hashes recorded (see Note 3).

## 3. Ordering: the ruled order A → C8 → verifier → S was followed
- **Commit order:** A `96537e934` (20:48) → C8 `ece62f792` (20:50) → pre-S records `4d2c19c1d` → verdict `83260ef0a` (21:12:56) → S brief `ca63944b1` → S `5fc8424e1` (21:18).
- **Scratch files corroborate the order:** the verifier's `k2verify.pMy3jX/rerun/SUMMARY.out` (21:02:46, `OVERALL PASS`, fault injection 19/19) and the S TASK's `s_task.s2l61k/cmd1.stdout` / `cmd2.stdout` (21:15:49 / 21:15:58). Each file holds one `write_status.sh` output line.
- **The verifier is independent.** `VERIFIER_VERDICT_01.md` comes from a separate agent (`a0414fd09eeccb8de`) under `VERIFIER_BRIEF_01.md` (`e49c1daa…`). It ran `MODE=VERIFY` against head `4d2c19c1d`, before S, when both `_STATUS.md` were still `OPEN`. It reran `run_k2_checks.sh` on a clean `d385b6a19` export and did its own quote and claim sampling.
- **The dispositions are true:**
  - Note 1 is recorded at `VALIDATION.md` "Pins at the final head";
  - Notes 2, 3 and 4 are at `HANDOFF_STATE.md` items 1 and 7;
  - Note 5 was actioned: the brief was committed with the verdict, and the fan-in preflight and records followed.
  - The verdict hash `649c5923…` was already the same when the S TASK read it, so the dispositions were in place at commit.
- **The S TASK's guard refusal wrote nothing.** Its preimage copies are timestamped 21:14, before its commands. Each command left one stdout file, and each `_STATUS.md` holds exactly one INITIALIZED history line.

## 4. Run-root integrity
- `shasum -a 256 -c SHA256SUMS`: 92 entries, all OK, and every file in the run root is covered.
- The hashes the return cites all match: `SHA256SUMS` `d1a493a9…`, `MANIFEST` `054c4fdd…`, `VALIDATION` `81fd6364…`, `HANDOFF_STATE` `48aa141f…`, `S_TASK_BRIEF` `75d7fb4d…`, `S_TASK_RETURN` `a98ebb56…`, `state_checks.sh` `41f4cfe7…`.
- The candidate and add-on copies equal the grant.
- The instruction and method hashes recorded in `MANIFEST.md` (root and PEC `AGENTS.md`, `AGENT_WORKING_ITEMS`/`AGENT_TASK`, `index.json`, `WORKFLOW.md`, `execution.json`, `brief`/`checks`/`tools`, the standard, the four SOW tools, `write_status.sh` `0bf835f5…`, the holds CSV and script) all recompute at the head.
- `MANIFEST.md`, `VALIDATION.md` and `HANDOFF_STATE.md` are truthful against the evidence files and the commit history.

## 5. Merges from main
- `c0d4098ca` (parent 2 `3e861f53c`) and `c4ae46f6e` (parent 2 `7004eaeda`) change only `projects/chirality-piping` (71 and 417 files).
- `git diff d385b6a19 7004eaeda -- projects/pec _DomainEngines tools workflows docs AGENTS.md agents` is empty.
- Live `origin/main` (checked with `ls-remote`) is still `7004eaeda`, which is the merge-base. Nothing pinned has moved.

## 6. HELP_HUMAN's records commit (`44488316`)
- **Census:** I recounted all 68 `PKG-*/1_Working/DEL-*/_STATUS.md` files.
  - Head: 28 OPEN / 30 INITIALIZED / 4 CHECKING (DEL-00-01, 00-03, 08-02, 10-01) / 2 IN_PROGRESS (01-03, 01-05) / 4 RETIRED (06-04, 07-02, 07-04, 07-05).
  - Main: 30 / 28 / 4 / 2 / 4.
  - STATUS lines 127–134 and README lines 47–48 match.
- **Contract count:** there are 36 `ScopeOfWork.md` at the head (34 on main). README lines 35–37 say 36 (32 + 2 + 2), which is correct.
- **DEL-01-06:**
  - its contract is `2053fb65abc2…177e`, and the D-PEC-100 proposal line 119 tables `5fdcfd96…` → `2053fb65…`;
  - no REVIEW has accepted it: the latest `_Evaluation/Reviews` entry is `REV_DEL-01-06_2026-08-04_1113`, the last commit touching `_REVIEW.md` or Reviews is `e92a82ca9` (2026-08-09), and `2053fb65` appears only in the STATUS/README records, the S2 returns and the D-PEC-100 proposal.
  - The corrected sentences at STATUS lines 45–50 and README lines 37–41 are accurate.
- **Acceptance-lapse carry:**
  - `ACCEPT_EXACT_BYTES` appears in exactly the `_REVIEW.md` files of DEL-00-03, DEL-02-07, DEL-03-01 and DEL-04-01;
  - DEL-01-06's contract was REVIEW-accepted at `REV_DEL-01-06_2026-08-04_1113`;
  - the D-PEC-100 proposal tables both replacements (lines 55, 60, 119, 124) and discloses no lapse;
  - the "S4 verdict 06" citation resolves: `PEC_SOW_CURRENCY_S4_PREP_2026-09-26/VERIFIER_VERDICT_06.md` lines 37 and 42 on PR #990's branch.
- **Graph:**
  - checked basis `7004eaeda` is correct;
  - PR #986 and PR #990 are open, as stated;
  - the completed-work row and the D-PEC-88 trace line 231 are accurate;
  - the Piping E2E flake claim matches the CI history (`c513e5dfd` Piping Desktop E2E passed on attempt 2).

## 7. Containment, whitespace and CI
- **Containment:** the diff against `origin/main` holds only the 5 grant product paths, 93 run-root files, the brief, the return, and HELP_HUMAN's `WORK_GRAPH.md`, `docs/STATUS.md` and `README.md`.
- **Whitespace:** `git diff --check origin/main <head>` exits 0.
- **CI at the head:** the PR is `MERGEABLE` / `CLEAN`. harness, pec, Harness pre-merge, Desktop E2E, and Select App/PEC/source coverage all pass; the rest are skipped by path selection; none fail.

## Findings

1. **NOTE: the graph and STATUS mark K2 done before the merge.** `WORK_GRAPH.md:70` says K2 `COMPLETE`, `:71` says K3 `READY` because "K2 is done (PR #992)", `:85` repeats "Ready now: … K3", and `docs/STATUS.md:302` says "Done". The S2 and S3 precedent used "ACTIVE — in PR #…, awaiting review and merge" inside the act PR and wrote COMPLETE only after the merge (graph at `aca930622` and `125cfacc1`). These records become true when this PR merges and die with it if it does not, so nothing is harmed. It is a departure from the house convention and from the `projects/pec/AGENTS.md` rule to rely only on what is observable on `origin/main`.

2. **NOTE: the lapse carry item overstates DEL-02-07's record.** `WORK_GRAPH.md:158` says of all four records that "the record calls for a REVIEW rerun". That is literally true for DEL-00-03 `_REVIEW.md:168`, DEL-03-01 `:203` and DEL-04-01 `:182` ("Any SOW … byte change invalidates this acceptance…"). DEL-02-07's `_REVIEW.md` has no invalidation clause; its lapse follows only from the exact-bytes terms (`d044499a…` accepted, `3d122087…` current). It could be worded "lapses on its exact-byte terms" for DEL-02-07.

3. **NOTE: the fan-in preflight was committed after the fan-in.** `evidence/reliance_hold_fanin.out` (`rely-for-production`, ALLOW ×5) was committed in `3cc19b058`, after the verdict (`83260ef0a`) and the S writes (`5fc8424e1`) were committed. The file carries no timestamp, so the evidence cannot show that the check ran "before fan-in", as proposal check 1 requires. The register is empty, so the outcome is unaffected. The D-PEC-98 precedent recorded only dispatch evidence, so this act is stronger than its precedent.

4. **NOTE: an adjacent STATUS sentence now reads ambiguously.** `docs/STATUS.md:51–55` ("The current SELF_CHECK snapshot … the accepted successor maps SOW-077 and SOW-094…") now follows the corrected sentence and describes the replaced revision-1.4 contract. Optional fix: "latest" in place of "current", and "the accepted revision-1.4 successor".

5. **NOTE: README staleness predates this act.** `README.md:29–34` still says "64 deliverables (66 after D-PEC-93)" and "all 66 contexts and 66 references name revision 1.5". It has been stale since D-PEC-101 (68 deliverables, re-pinned to 1.6), is identical on main, and was not caused by this act.

6. **NOTE: two minor gaps.**
   - The STATUS K2 "Done" bullet (`docs/STATUS.md:302–307`) omits the "MEMORY.md at closeout" clause that the DEL-02-08/09 bullet carries; the graph does carry it.
   - `S_TASK_RETURN.md` was not saved fully verbatim: git's blank context lines are shown as `[SP]`. The substitution is disclosed in its manager note.

Nothing else in STATUS or README was made stale by this act and left uncorrected.

Key paths (repository `/Users/ryan/ai-env/projects/chirality`, branch `claude/pec-d103-first-sows-act`):
- `projects/pec/execution/_Coordination/SOW_INIT_K2_2026-09-26/` (`MANIFEST.md`, `VALIDATION.md`, `HANDOFF_STATE.md`, `VERIFIER_VERDICT_01.md`, `S_TASK_RETURN.md`, `evidence/`)
- `projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`
- `projects/pec/docs/STATUS.md`, `projects/pec/README.md`
- `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/_REVIEW.md`

## Disposition (HELP_HUMAN)

Verdict PASS WITH NOTES; nothing blocking and no non-blocking findings. Dispositions:

- **Note 1 (K2 marked done before merge): repaired in the graph.** Following the S2 and S3 convention:
  - K2 reads "ACTIVE — act in PR #992, awaiting review and merge".
  - K3 stays PLANNED until that PR merges.
  - The Order and Next-work lines say the same.

  HELP_HUMAN flips both after the merge, in its next graph PR. The STATUS "Done" bullet follows the `D-PEC-98` act-PR precedent: STATUS is updated in the act PR and becomes true at merge.
- **Note 2 (DEL-02-07 record wording): repaired.** The carry item now says a replacement lapses each acceptance on its exact-byte terms, and that only the DEL-00-03, DEL-03-01 and DEL-04-01 records also carry the "any byte change invalidates" clause.
- **Note 3 (fan-in preflight timing): recorded, no change.** The holds register is empty, so the outcome is unaffected. The file carries no timestamp, so the evidence cannot show it ran before fan-in. This act still records more than the `D-PEC-98` precedent did.
- **Note 4 (adjacent STATUS sentence): repaired.** It now reads "latest SELF_CHECK snapshot" and "the accepted revision-1.4 successor".
- **Note 5 (README staleness from before this act): repaired under `D-PEC-88`.** README now says 68 deliverables (after `D-PEC-101` added DEL-08-06 and DEL-10-13), and records the `D-PEC-101` re-pin of the remaining 63 contexts and all 66 references to revision 1.6 / PRD v2.4.
- **Note 6:** the STATUS K2 bullet now names the `MEMORY.md` files at closeout. The `S_TASK_RETURN.md` substitution was disclosed by the manager, and no change is made.

The repair head needs a fresh review before merge.
