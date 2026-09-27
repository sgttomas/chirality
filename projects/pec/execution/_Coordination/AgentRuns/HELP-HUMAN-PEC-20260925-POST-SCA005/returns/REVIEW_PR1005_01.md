# Review 01 of PR #1005, transcribed

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high) dispatched by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed from the host subagent transcript (verbatim apart from any disclosed whitespace normalization).
- **Reviewed head:** `c21e75a238dafc7ee3f76d36febaf2a7facf8e36`. The repairs listed under Disposition and this file follow that head.
- **SHA-256 of the report text below (UTF-8; the report text between the blank line after "## Report (verbatim)" and the blank line before the final "## Disposition", with no trailing newline):** `f14655eb0326f378435a2fc936d3cb7c01a6f98058bd32d29e6f71a764dd1b47`.

## Report (verbatim)

## Review of PR #1005, head c21e75a238dafc7ee3f76d36febaf2a7facf8e36 (branch `claude/pec-d104-ruling`): **PASS WITH NOTES**

Nothing is BLOCKING. There are two NON-BLOCKING findings. I would fix both before merge, because a register row is hard to correct later. Everything else was verified true.

I stayed read-only: no edits, no git writes, no checkout. Exports went only into my own `mktemp -d …/scratchpad/rev1005.AIj7I5`, with TMPDIR exported. I deleted that directory at the end, and the worktree is clean.

All paths below are under `projects/pec/execution/_Coordination/`:
- `_DECISIONS/D-PEC-104_RULING_2026-09-27.md` is "RULING".
- `WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md` is "GRAPH".
- `_DECISIONS/_REGISTER.md` is "REGISTER".

### NON-BLOCKING

**NB-1. The register row's verdict summary is ambiguous and misleading per verdict (REGISTER:121).**
- The row says "in-run verdicts 01–15 (rounds 1–7 and verdict 14 FAIL, repaired; 12, 13 and 15 PASS WITH NOTES)".
- The verdict files actually say:
  - **FAIL:** 02, 03, 06, 07, 08, 09, 10, 11 and 14.
  - **PASS WITH NOTES:** 01, 04, 05, 12, 13 and 15.
- Rounds 1–7 cover verdicts 01–11, so the row implies that 01, 04 and 05 failed. It also mixes rounds with verdict numbers (verdict 14 is round 10).
- The reading is defensible per round, since every round from 1 to 7 ended FAIL overall. It is not accurate per verdict, and it leaves out three passing verdicts.
- The D-PEC-102 and D-PEC-103 rows count per verdict.
- **Suggested wording:** "in-run verdicts 02, 03, 06–11 and 14 FAIL (repaired); 01, 04, 05, 12, 13 and 15 PASS WITH NOTES".

**NB-2. D1 and X1 are marked READY while they wait for an owner ruling (GRAPH:66, GRAPH:67; also GRAPH:88 and GRAPH:159).**
- The graph's own line 104 says the adopted `construct-local-work-graph` "says a node awaiting a human decision is BLOCKED, naming the decision. This graph has applied that since the wave-2A update."
- The template agrees (`workflows/construct-local-work-graph/resources/work-graph-template.md:36-37`).
- Both rows now read "READY — packet merged … awaits the owner's ruling".
- One earlier graph state set a precedent: K2 stayed READY at `4b930819c`. That does not cure the contradiction.
- **Suggested state:** "BLOCKED — owner ruling on `D-PEC-105` (provisional)", and the same with `D-PEC-106` for X1.

### NOTE

1. **Usage-limit gloss (RULING:11).**
   - Treating "And usage limits have been reset." as not a ruling term is fair.
   - The added facts, "weekly" and "which had stopped one review", appear in no record. The only recorded stops are "API error" (`returns/REVIEW_PR986_02.md:3`, `REVIEW_PR979_02.md:3`).
   - Either drop the gloss or tie it to that record.
2. **Q1 cell wording (RULING:49).**
   - "two things change" is followed by an acceptance that "stays as history, because its bytes are replaced". The cell also leaves out the proposal's point that there is no lapse clause, which RULING:20 does keep.
   - The "stays as history" content comes from Q4 ("confirm 4"), but the cell cites "A" as its basis.
   - None of this enlarges the ruling. It matches the proposal at L119, L278 and L281, and Q4 was confirmed.
3. **Bare review filenames (RULING:16-17).** `REVIEW_PR986_01.md` and `_02.md` are given without the `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/` path. The D-PEC-102 ruling (L13) gives it.
4. **Truncated owner quote (REGISTER:121).** The row's "verbatim" owner quote leaves out the trailing sentence. This is consistent with the not-a-ruling-term reading, and RULING:9 carries the full string. The D-PEC-102 row quoted the whole string.
5. **STATUS header and placement (`projects/pec/docs/STATUS.md:223`, `:271-275`).**
   - The header still reads "Current owner gates (2026-09-26; …)" but now includes a 2026-09-27 ruling. This date was already not being updated before this PR.
   - The D1 and X1 sentences sit inside the "SOW currency (S1, S2, S4)" bullet, while separate "DEL-00-01/00-03 derivative review" and "P1 fixtures" bullets follow.
6. **Minor wording carried over (GRAPH:159).** "S1 and S4 absorb the `D-PEC-99` Part B items …" is now partly past: S4 has already absorbed them.

### Verified true

**Faithfulness (K-AUTH-1)**
- Each resolution matches both the owner's token and the proposal's question text (proposal L278–L283):
  - A with its S4 ordering;
  - the four Part B items, including the DEL-03-06 L229 paragraph and the DEL-04-05 bracket resolved to revision 1.6, each gate discharged only for the text it applies;
  - DEL-03-06 correction-only, including the two sibling quotations it makes non-verbatim;
  - Q4's three acceptances as history, with no REVIEW acceptance and no `_REVIEW.md` or `Review_Findings.csv` write;
  - M as 11 files created plus 1 section appended (matches proposal L125–L126 and L157–L162);
  - models at their defaults.
- **Acceptance packet `e3d6f2ae…b596`:** `e3d6f2ae9e52b149abb75f5bba8815a7eb65a549ebf3be258eae8581ff43b596` is at DEL-01-05 `_REVIEW.md` L12 and L130.
- **D-PEC-77 acceptance:** its 2026-08-03 wording is at `D-PEC-77_del_01_05_enforcement.md` L143–L146.
- **DEL-03-01 acceptance:** the 2026-08-09 `ACCEPT_EXACT_BYTES` is at its `_REVIEW.md` L11–L38.
- **Grant and limits:** these are a faithful subset under "apply unchanged", with no enlargement.

**Hashes and counts**
- The published proposal is `35301840d56f9972b0d7ca3c85dae0ee80ffdf5509c44586f219a47ff6545f51`, byte-identical to the prep draft at `origin/main`.
- `apply_s1p.py` is `26b677a7…625f` and parses to 12 TARGETS and 35 PINNED.
- On a head export, all 12 preimages and all 35 pins match, and a copy run with `--check-only` from outside the repository exits 0 with "CHECK preflight passed". The in-tree run refuses, by design, because the prep folder is not a run root.
- `SHA256SUMS -c` passes: 158 entries, 0 failures.
- DEL-01-03 `MEMORY.md` is `44b360c5…dae6`, the other 11 are absent, and the template is `5a9564f4…6a5a`.

**Reviews and merge commits**
- `REVIEW_PR986_01` is FAIL (BLOCKING-1 was the undisclosed DEL-01-05 acceptance, repaired). `REVIEW_PR986_02` is PASS WITH NOTES.
- Merge commits: #986 is `20a5c3232`, #996 is `b0a9a52b6`, #997 is `cfe753dc7` and #998 is `f0a6159c9`.
- The review files for #996 and #997 (01–03) and for #998 (01–02) exist. The S4 act verifier returned PASS WITH NOTES.

**Base drift paragraph (RULING:64)**
- Current `origin/main` is `20a5c3232`.
- The first-parent merges since `b0a9a52b6` are #1000–#1004 and then #986.
- `b0a9a52b6..9963645a7` changes 383 files, all under `projects/chirality-piping/`.
- The #986 merge adds only the S1 prep folder, its brief and return, and `REVIEW_PR986_01` and `_02`.
- No PEC path outside those changed, and no target or pin moved.

**Graph and STATUS**
- M1's D-PEC-104 list matches the proposal.
- The S4 row is correctly COMPLETE.
- The S1 row is correctly ACTIVE.
- The returns of the S1P, D1P and X1P managers exist, which supports "handed back".
- The D-PEC-88 trace line was added (GRAPH:239), and the verbatim owner line was added (GRAPH:205).
- I found no stale "awaiting review", "in preparation" or "provisionally D-PEC-104" text.

**Containment and CI**
- Exactly the five named paths change. `git diff --check origin/main...c21e75a238` is clean.
- The PR is MERGEABLE, with merge state CLEAN.
- CI at c21e75a23: pec, harness, Harness pre-merge, Desktop E2E, Select PEC, Select App and Select source coverage all pass; the others were skipped.
- I could not rerun the harness self-check or the receipts validator locally, because they need a git index and a plain export has none. I relied on the passing pec and harness CI jobs. The PR touches nothing those checks read.

## Disposition (HELP_HUMAN)

Verdict PASS WITH NOTES; nothing blocking. Dispositions:

- **NB-1 (register verdict summary): repaired.** It now counts per verdict: 02, 03, 06–11 and 14 FAIL (repaired); 01, 04, 05, 12, 13 and 15 PASS WITH NOTES.
- **NB-2 (D1/X1 READY while awaiting a ruling): repaired.** Both rows now read "BLOCKED — owner ruling on `D-PEC-105`/`D-PEC-106` (provisional)", as the adopted method requires.
- **Note 1: repaired.** The usage-limit gloss now cites the recorded API-error stop (`REVIEW_PR986_02.md`) and drops the unrecorded "weekly".
- **Note 2: repaired.** The Q1 cell now says two owner-accepted contracts are superseded. It keeps the no-lapse-clause point and cites "A" together with "confirm 4" for the history reading.
- **Note 3: repaired.** Both review filenames now carry their full `AgentRuns/…/returns/` path.
- **Note 4: repaired.** The register quotes the full owner string, marking the last sentence as not a ruling term.
- **Note 5: carried.** The STATUS owner-gates header date and bullet placement will be refreshed at the next STATUS touch.
- **Note 6: repaired.** The graph line now says S4 has absorbed its Part B items and S1 absorbs its own.

The repair head needs a fresh review before merge.
