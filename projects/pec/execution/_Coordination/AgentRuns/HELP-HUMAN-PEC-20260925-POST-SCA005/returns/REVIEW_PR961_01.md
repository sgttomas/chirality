# Review 01 of PR #961 (work graphs after the D-PEC-98 and D-PEC-99 acts), transcribed

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high), dispatched by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed verbatim from the host subagent transcript.
- **Reviewed head:** `4537ccb6bd210f829bf0d53760f3e8521beb8ddd` (base `origin/main` `aca930622`). Repairs: `ba5091550`; this file is added after that.
- **SHA-256 of the report text below (UTF-8, trailing newline stripped):** `92f5c55226e820eb3516454d6e67e263c41a0882d100d08d62af8aa7486b7cc4`.

## Report (verbatim)

**Review of PR #961 at head `4537ccb6bd210f829bf0d53760f3e8521beb8ddd` (base `origin/main` `aca930622`): CHANGES REQUESTED.** I only read and checked; no files were modified.

Two statements this PR changes are false at head, and the graph it edits still has several stale current-state statements. Every repair is a wording fix to the records. Nothing is wrong in substance: no unmerged record is cited as merged fact, no node wrongly awaits the owner, and nothing prompts about CHECKING.

Paths below are short forms:
- `POST` = `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`
- `RET` = `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260926-REMAINING-RETIREMENT/WORK_GRAPH.md`

## Findings, most serious first

**1. Wrong merge commit for two of the three notices (changed line) — `POST:116`.**
The line says "Three Root notices merged by `6128f8b85` (PRs #955, #956, #959)". Only the dependency notice came in with that commit. The first-parent history of `origin/main` shows:
- `NOTICE_2026-09-26_PROJECT_SETUP_INCREMENTAL.md` came in with `6b48b6f26` (PR #955).
- `NOTICE_2026-09-26_SOFTWARE_PRD_REGISTRATION.md` came in with `cb85f85d1` (PR #956).
- `NOTICE_2026-09-26_DEPENDENCY_FOLLOWUPS.md` came in with `6128f8b85` (PR #959).

Elsewhere the graph uses "merged by `<sha>`" to name the introducing merge, so this reads as a false citation. Name all three merges.

**2. Retirement graph says nothing is unmerged while this PR is open (changed line) — `RET:38`.**
It reads "Local or unmerged work: none." PR #961 is OPEN and carries this very edit. `POST:142` handles the same case as "this graph update". Use the same wording, or phrase it as "none after this PR merges".

**3. Notice-triage heading count is stale, and this PR made it worse — `POST:94`.**
It says "five Root wave-2A workflow notices and seven later Root notices". The section now lists 11 later notices (3 + 4 + 1 + 3), and `_Coordination/` holds 16 notices dated 2026-09-26 (5 wave-2A + 11). The count was already off at base (8 listed against "seven").

**4. Stale "Unresolved consequence" cells in the completed-work table (unchanged lines, but current-state claims):**
- `POST:158` (`D-PEC-98` publication): "Owner ruling given 2026-09-26; act pending". The act merged as PR #958 (`aca930622`). This contradicts the new S3 COMPLETE row at `POST:63`.
- `POST:160` (ruling PR, branch `claude/pec-rulings-20260926b`): "Review and merge". It merged as PR #954 (`189f205ff`).
- `POST:154` (`D-PEC-96` revision 4): "Owner ruling". The ruling was given (PR #946), and the act merged as PR #950.
- `POST:151` ("R2 checkpoint-2 preparation") and `POST:155` ("R3 checkpoint-3 preparation"): both are done; R2 and R3 are COMPLETE.
- The table has no rows for the `D-PEC-99` act (#957) or the `D-PEC-98` act (#958). This is optional, but it would close the S3 recovery trail.

**5. "This undertaking makes no lifecycle act" is now false — `POST:110`.**
Add-on S of `D-PEC-98`, carried out in this undertaking, set DEL-02-08 and DEL-02-09 `OPEN → INITIALIZED`. Both `_STATUS.md` files show "2026-09-26 — State set to INITIALIZED". Narrow the sentence, for example to "makes no CHECKING, ISSUED or review lifecycle act".

**6. The new triage bullet sits awkwardly with the owner's deferral — `POST:117`, low.**
The notice says: "no adoption, `SETUP_LOG.md` baseline or incremental setup run is expected in this loop now". Having every K1 and S packet name adoption "as an owner option" puts a deferred question back to the owner in each packet. It does not assume adoption, but a closer reading of the deferral would be: follow current practice, and raise adoption only if the owner does. (The PR body says the same thing, so align both if you change it.)

**7. Low: other stale tense or basis wording (unchanged lines):**
- `POST:9` and `POST:24`: the intended result and route still name revision 1.5 and PRD v2.3. The basis is now 1.6 / v2.4, and S3 was re-pinned to 1.6.
- `POST:97`: "applies that from this update (G1, R3)".
- `POST:103`: "R3's audit will use".
- `POST:105`: "applies when … the R3 audit run … at R3". R3 is COMPLETE.
- M1 names HELP_HUMAN as owner (`POST:76`), while the `D-PEC-98` proposal (`_DECISIONS/D-PEC-98_first_sows_del_02_08_02_09_proposal_2026-09-26.md:207`) says "WORKING_ITEMS creates the two `MEMORY.md` paths". Reconcile this before M1.

**8. Outside this diff, for the record: the review-02 transcription hash does not reproduce.**
`AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/REVIEW_PR958_02.md:5` states `78218053…443e`. I used a method that does reproduce review 01's stated hash (`3256c2ba…322`): the text between "## Report (verbatim)" and "## Disposition", with surrounding newlines stripped. On review 02 it gives `cfd849b6…984b`, and no other plausible cut matches. The file is already merged (PR #958), so this is not a defect of this PR. HELP_HUMAN could record it in the graph or re-transcribe it.

## Verified true at head
- **PR states:**
  - #954 merged as `189f205ff`, #957 as `22502e059`, #958 as `aca930622`.
  - #955 merged as `6b48b6f26`, #956 as `cb85f85d1`, #959 as `6128f8b85`.
  - #961 is open, and its CI is green (harness, pec, Harness pre-merge all pass).
  - The checked basis `aca930622` at `POST:138` and `RET:37` is correct.
- **S3 row (`POST:63`):**
  - The contract hashes recompute with `shasum -a 256`: DEL-02-08 is `2319661b…fdd26`, DEL-02-09 is `eab18e17…b6f5e`.
  - Both `_STATUS.md` files say `INITIALIZED`.
  - No `MEMORY.md` exists yet, which matches the `D-PEC-98` ruling's "at the undertaking's closeout (graph node M1)" (ruling L54).
  - The S3A and RR3 briefs and returns are on `origin/main`.
- **Line locators (`POST:125–126`):**
  - The "did not exist at `c9e5cd87d`" text is at DEL-02-08 L29–31 and DEL-02-09 L30–32.
  - The `_CONTEXT.md` / `_REFERENCES.md` sentence ends on DEL-02-08 L44 and DEL-02-09 L43.
  - CLM-013 (DEL-02-08:111) still calls `c9e5cd87d` "the decomposition pin".
- **Review-02 dispositions:** NOTE 1's locator correction is applied at `POST:125`. NOTE 2 is applied: the S3 row now cites review 01 alone. NOTE 3 is met: PR #958 CI passed, including harness.
- **The three notices:** each says the owner defers action for PEC (INCREMENTAL L18, DEPENDENCY L32, SOFTWARE_PRD L14). Each adds only its own notice file under `projects/pec`, so "none changes a PEC file" is true if the notice file itself is not counted. The summaries are accurate, and so is the `D-PEC-62` materializer point.
- **Other claims:**
  - `REVIEW_PR954_03.md` exists, and the human-owned `_COORDINATION.md` Notes line (L225) still names revision 1.5.
  - `POST:112`'s "26 `XRG-013`" is still true.
  - The census of 28 `OPEN` / 28 `INITIALIZED` matches the 66 `_STATUS.md` files.
- **Node states:** no node awaits an owner decision; the READY nodes are waiting on packet preparation, so none needs BLOCKED. `POST:110` and `POST:145` expressly do not prompt about CHECKING.
- **Checks:**
  - Containment is exactly the two graphs, in one commit, with the Co-Authored-By trailer present.
  - `git diff --check origin/main...HEAD` exits 0.
  - `harness.py self-check` exits 0.
  - `validate_pec_loop_receipts.py` reports VALID (exit 0).
  - The strict register validator exits 1 with 0 errors and 28 warnings (26 XRG-013, 2 DRB-008). That exit is the known baseline.
  - The working tree is still clean after the checks.

**Verdict: CHANGES REQUESTED.** Repair findings 1–3 (false or stale statements that this PR changed or made worse) and the stale cells in 4–5. Findings 6–8 are notes.

## Disposition (HELP_HUMAN)

| Finding | Disposition |
|---|---|
| 1 (notice merge commits) | Repaired in `ba5091550`: each notice names its introducing merge (`6b48b6f26`, `cb85f85d1`, `6128f8b85`); "none changes a PEC file other than adding its own notice" |
| 2 (retirement graph unmerged-work line) | Repaired: "this graph update (PR #961); none after it merges" |
| 3 (notice count) | Repaired: eleven later Root notices |
| 4 (stale completed-work cells; missing act rows) | Repaired: R1, D-PEC-96 revision 4, R2, D-PEC-98 publication and ruling-PR cells are current; rows added for the D-PEC-99 act (#957) and the D-PEC-98 act (#958) |
| 5 (lifecycle sentence) | Repaired: the undertaking makes no CHECKING, ISSUED or review lifecycle act; its only lifecycle act is D-PEC-98 add-on S |
| 6 (owner option vs deferral) | Repaired: the triage says the K1 and S packets follow current practice and disclose the new modes in one line without putting adoption to the owner; both preparing managers received the same brief amendment |
| 7 (tense and basis wording; M1 actor) | Repaired: intended result and route name both bases; wave-2A lines in past tense; M1 names the actor per packet (D-PEC-98 add-on M: WORKING_ITEMS) |
| 8 (REVIEW_PR958_02 hash) | Checked: the stated hash `78218053…443e` is correct. The review-02 report quotes the literal heading "## Disposition", so a cut at its first occurrence stops early; cutting at the final heading reproduces it. Recorded in the graph's D-PEC-98 act row |
