# Review 01 of PR #1010, transcribed

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high) dispatched by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed from the host subagent transcript (verbatim apart from any disclosed whitespace normalization).
- **Reviewed head:** `266534e239016a6d5b93085f5e074b80faeabb39`. The repairs listed under Disposition, this file and a merge of `origin/main` follow that head.
- **SHA-256 of the report text below (UTF-8; the report text between the blank line after "## Report (verbatim)" and the blank line before the final "## Disposition", with no trailing newline):** `02e974a919465c3de951a6d89aa7383a5173594bad094fd88792c36e833a2737`.

## Report (verbatim)

## Review of PR #1010 (D-PEC-104 act) at head 266534e239016a6d5b93085f5e074b80faeabb39

**Verdict: PASS WITH NOTES.** Nothing is blocking. Every check the brief asked for reproduces at the head. I found one NON-BLOCKING record finding (a wrong hash abbreviation, repeated in four records) and one NON-BLOCKING stale graph line. The rest are NOTEs.

This review records no ruling. It makes no lifecycle, CHECKING, acceptance or reliance claim, and it prompts nothing about CHECKING.

### What I verified

**1. Product writes.**
- All twelve `ScopeOfWork.md` files at the head hash to the proposal's postimages (proposal L136–149), 12/12.
- The same files on `origin/main` hash to the tabled preimages, 12/12.
- The run-root candidates also equal the postimages.
- The proposal hashes `35301840…5f51` and the brief copy hashes `b60d21db…296a`. The brief copy is byte-identical to HELP_HUMAN's scratchpad original `acts2/S1A.md`.
- `apply_s1p.py` and all nine aids hash exactly as the proposal binds them.
- No `_STATUS.md`, `_REVIEW.md`, `Review_Findings.csv` or `MEMORY.md` changed.
- No S4 target was written: all 35 pins match at both the head and `origin/main` (70/70), including DEL-04-01 `98a3a3ec…` and DEL-04-03 `10819cb2…`.
- The add-on M preimages still hold: DEL-01-03 `MEMORY.md` is `44b360c5`, the other eleven are absent, and the template is `5a9564f4`.

**2. Finite verification, rerun on a `git archive` of the head.** Python 3.13.7, with `TMPDIR` pointed at my scratch folder and `PYTHONDONTWRITEBYTECODE=1`.
- **Validator:** `PASS format=SOW_V1` ×12.
- **Checklists:** exit 0; each rerun is byte-identical; all 12 equal the run-root copies and the prepared hashes in the prep `SHA256SUMS`. The prep `SHA256SUMS` checks 158/158.
- **Boundary owners:** exit 0 ×12, with no `UNRESOLVED_OWNER` or `UNDEFINED_CLAIM`. The JSON equals the run-root copies. The `NOT_CHECKABLE` counts (1/0/0/4/1/2/0/1/0/2/0/0) match the proposal's QA 21 table.
- **Quotes / state claims / qualified IDs:** 884/884, 905/905, 44/44.
- **Dependency-quote currency:** 127/127 at both the head and `origin/main`, outputs identical.
- **Strict registers:** identical to `origin/main` (exit 1, 0 errors, 26 warnings).
- **Harness self-check and loop receipts:** identical, exit 0 each. The exports needed a Git identity through alternates, the method `run_s1p_checks.sh` uses.
- **`run_s1p_checks.sh`:** OVERALL PASS at `0adfbc747`, and its `SUMMARY.out` is byte-identical to the recorded `evidence/rerun_0adfbc747/SUMMARY.out`. It also passes at the new `origin/main` `8bbd022b9`, with a summary identical apart from the basis line.
- **`--check-only`:** refuses on the head export as designed (12 "does not hold its preimage" lines, exit 1, nothing else) and passes on the `origin/main` export.
- **DEL-01-03 / DEL-01-05:** the REQ/AC/VER lines (10+10+9 and 12+11+9) are byte-identical to the preimage. The only changed line that mentions any of them is the DEL-01-03 `OUT-003` matrix row, which gains `AX-007`, as disclosed.
- **DEL-03-06:** hunks only at `@@ -220`, `-222,4`, `-229`, `-476`.

**3. Reliance-hold evidence.** Each preflight file carries `date -u` lines, and each shows ALLOW ×12.
- Dispatch: 17:18:24Z, at `16010b4ca`.
- `--check-only`: 17:19:09Z. The act: 17:19:45Z.
- Rely: 17:19:59Z, contained in act commit `1e33df616` (17:19:59Z).
- Rely again before the verdict fan-in: 18:01:23Z, before verdict commit `0b5bcc050` (18:01:33Z).

So dispatch precedes the act. My own preflight on `origin/main` (register `f877d931…`) returns ALLOW ×12 for both `candidate-validation` and `rely-for-production`.

**4. The verifier.** `VERIFIER_VERDICT_01.md` is a fresh read-only TASK `MODE=VERIFY` run on `1cc8ce997`. Its hash `5dab70b3…` matches the return.
- I spot-checked N1 (eleven "provisional `D-PEC-104`" entries; DEL-03-06 has none), N2 (DEL-04-05 L301), and N4 (L334 gains `, AX-012`). All are true.
- No product byte changed after `1cc8ce997`: the diff to the head leaves the twelve contracts untouched, and every run-root change is an `A`.

**5. Run root.**
- `SHA256SUMS` checks 334/334 OK.
- Coverage is exact: the 335 files are the 334 listed plus the sums file itself.
- No `__pycache__` is listed, none is tracked at the head, and no commit in the PR history ever added one. The first `SHA256SUMS` listed one; `1f0a8fefc` removed that entry.
- The act worktree (`.claude/worktrees/pec-d104-act`) is clean, with no `__pycache__`.
- The record hashes the return gives for MANIFEST, VALIDATION, HANDOFF_STATE, the verdict and `SHA256SUMS` all reproduce. The return file itself hashes `5506db40…`.

**6. Merge from main.** `8e09da59f` has parents `0b5bcc050` and `0adfbc747`. It brings nine `projects/pec` paths: STATUS, the graph, the PR #1006 reviews, the `D-PEC-105`/`106` rulings and proposals, and `_REGISTER.md`. None is an S1 target, pin or quoted file, and the `D-PEC-104` register row is unchanged.

`origin/main` has since moved to `8bbd022b9` (PR #1011, 10 `projects/chirality-app-v4` files only), so no PEC path changed. The PR reports MERGEABLE / CLEAN.

**7. HELP_HUMAN records (`266534e23`).**
- The graph S1 row is ACTIVE-in-PR with the PR URL. Order L88 is correct. The Recovery section (next work, unmerged work, active operations) is correct. The carried S1 items are present, and the `D-PEC-88` trace is at L246.
- The STATUS "Done" text for S1 matches the facts.
- The owner-gates header date changed from 2026-09-26 to 2026-09-27; that is correct, since PR #1006 already added 2026-09-27 rulings.
- The two sentences at STATUS L262 and L346 now read "S4 and S1 (both done, below)" and "S1 the other four (`D-PEC-104`, PR #1010)".
- README.md is not made stale by this act. Neither STATUS nor README cites the old DEL-01-05 or DEL-03-01 contract hashes or calls those contracts currently accepted.

**8. Containment, whitespace and CI.** `git diff origin/main...head` touches exactly:
- the 12 contracts;
- the run root (335 files);
- the brief and the return;
- `WORK_GRAPH.md`;
- `projects/pec/docs/STATUS.md`.

`git diff --check` is clean. **CI on the head is green:** Desktop E2E, Harness pre-merge, pec, Select App/PEC/source coverage and harness all pass; the remaining jobs are path-gated skips.

### Findings

**BLOCKING:** none.

**NON-BLOCKING**
1. **Wrong proposal-hash abbreviation in four records.** The proposal hash ends `…6545f51`, so its abbreviation is `35301840…5f51`. Four places write `35301840…6f51`:
   - `execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/S1A_D104_SOW_ACT.md:22`
   - `execution/_Coordination/SOW_CURRENCY_S1_2026-09-27/VALIDATION.md:18`
   - the PR #1010 body, line 3
   - `VERIFIER_VERDICT_01.md:43`, which says "The row cites the proposal SHA `35301840…6f51`". The register row actually cites the full hash ending `5f51`.

   The full hash is correct in MANIFEST L32, `evidence/preconditions.out` L13 and verdict L27, so nothing relied on the wrong tail. Suggested repair: correct the return, VALIDATION (then regenerate `SHA256SUMS`) and the PR body. The verdict's bytes are bound, so leave it and note the slip.
2. **The graph's checked basis is stale.** `WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md:159` still says `origin/main` `16010b4ca`. The records commit sits on `0adfbc747`, which adds PR #1006 (the D1/X1 rulings the graph cites elsewhere) and PR #1009. Live main is now `8bbd022b9`. Suggest updating the line and adding PR #1006.

**NOTES**
- **Third acceptance omitted.** Ruling question 4 keeps three acceptances as history. `STATUS.md:276–277` and graph L61 ("DEL-03-01's acceptance lapses and DEL-01-05's `D-PEC-77` acceptance becomes history") name only two. They leave out the separate 2026-08-03 exact-artifact acceptance bound to `e3d6f2ae…b596`. HANDOFF_STATE L20–23 names all three.
- **Status of the SOW currency bullet.** `STATUS.md:255–256` still lists "SOW currency (S1, S2, S4)" under "Open:". All three acts are now recorded as done, and only add-on M at M1 remains. Other bullets in that list carry a "done:" prefix; this one could say what is still open (MEMORY at closeout).
- **"Done" before merge.** STATUS says "Done" for the act while the graph says ACTIVE-in-PR. This is the same split PR #998 review 01 noted, and it becomes true on merge. Graph L91 and L162 ("S1 and S4 packets absorb", "S1 absorbs") should be updated at merge, under the same convention.
- **Trace wording.** The `D-PEC-88` trace (graph L246) says the STATUS change "records the S1 act done and the owner-gates header date". It does not name the L262 and L346 sentence edits, which the S4 precedent trace did name. Both edits sit in the open list, so this is a wording point only.
- **Partial carry-forward list.** Graph L167 carries a subset of HANDOFF_STATE's later-currency items. It omits the second part of N3 (the DEL-03-01 REQ-007 "CLM-019" row), the DEL-10-02 `C-08` / `_DEPENDENCIES.md` L22 wording, and the register/record wording items. It cites HANDOFF_STATE as the source, so nothing is lost.
- **Stale PR body containment line.** PR body L18 ("Containment: the twelve contracts, the run root and the brief copy (plus the return)") predates HELP_HUMAN's records commit, which adds the graph and STATUS. L21 ("No … `docs/**` write") reads correctly only as the manager's write set.

### My footprint
- **Scratch:** `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/rev1010.XScvoW`. It holds the `git archive` exports of the head and `origin/main` (each given an empty `git init` with alternates), my outputs, and the `run_s1p_checks.sh` output folders `rerun_main/` and `rerun_main2/`. I left it in place. Nothing was written to /tmp or /var/folders.
- **Git: one deviation from "no git writes".** I ran `git fetch origin` twice (read-only in intent), and that updated the shared remote-tracking ref `origin/main` from `0adfbc747` to `8bbd022b9`. Nothing else changed: no local branch, index, worktree, checkout or config. Every other Git command was a read: show, diff, log, archive, ls-tree, ls-remote, rev-parse, and gh pr view/checks.
- **Worktrees and CHECKING:** no file edits, and no worktree was modified. Nothing here asks about CHECKING.

### Relevant paths
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d104-act/projects/pec/execution/_Coordination/SOW_CURRENCY_S1_2026-09-27/ (MANIFEST.md, VALIDATION.md, HANDOFF_STATE.md, VERIFIER_VERDICT_01.md, SHA256SUMS, evidence/)
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d104-act/projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/S1A_D104_SOW_ACT.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d104-act/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d104-act/projects/pec/docs/STATUS.md

## Disposition (HELP_HUMAN)

Verdict PASS WITH NOTES; nothing blocking. Dispositions:

- **NB-1 (wrong proposal-hash abbreviation): repaired.** The S1A return and `VALIDATION.md` now read `35301840…5f51`, and the run-root `SHA256SUMS` entry for `VALIDATION.md` is updated (all entries pass). The PR body is corrected too. `VERIFIER_VERDICT_01.md` keeps its bound bytes, and its slip is noted here.
- **NB-2 (stale checked basis): repaired.** The graph now names `origin/main` `8bbd022b9` and PR #1006.
- **Notes:**
  - **Third acceptance:** repaired. The graph S1 row and STATUS now name the separate 2026-08-03 exact-artifact acceptance (`e3d6f2ae…b596`) as history.
  - **SOW-currency bullet:** repaired. It now says all three acts are done and only their `MEMORY.md` records remain open.
  - **Trace wording:** repaired. The D-PEC-88 trace names the two sentence edits.
  - **"Done" before merge, and the graph's "S1 and S4 absorb" lines:** they follow the act-PR convention, and HELP_HUMAN updates them after merge.
  - **Partial carry-forward list:** it cites `HANDOFF_STATE.md` as the source, so no change.
  - **PR body containment line:** corrected.
- **Reviewer footprint:** the reviewer left its scratch directory in place, and HELP_HUMAN removed it. Its `git fetch` updated only the remote-tracking ref.

The repair head needs a fresh review before merge.
