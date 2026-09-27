# Review 03 of PR #1021, transcribed

- **Reviewer:** the same read-only `pec-reviewer` as reviews 01 and 02 (TASK, `claude-opus-5-5`, high), resumed by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed from the host subagent transcript (verbatim apart from any disclosed whitespace normalization).
- **Reviewed head:** `350fb976dc5ea01920e1773d2e42230641359568`. This file is the only addition after that head.
- **SHA-256 of the report text below (UTF-8; the report text between the blank line after "## Report (verbatim)" and the blank line before the final "## Disposition", with no trailing newline):** `f5aeecb38009eee56debbc7f2d20ac1a290dc0daa103086ff0546a1121833e5e`.

## Report (verbatim)

**Review 03 of PR #1021 at head `350fb976dc5ea01920e1773d2e42230641359568`. Verdict: PASS WITH NOTES.** I found no blocking or non-blocking findings, and 2 notes.

`git ls-remote` confirms that head for `claude/pec-tm1-intake-dispositions`, and confirms `main` = `d39daf548`, which is an ancestor of the head. The head is one commit on `54489b03d`. I made no edits, no fetch and no checkout. I read the bytes through `git archive` into `rev1021.TM8jKg`, ran the validators in scratch-only git repos that borrowed the object store read-only, and then deleted the directory.

## BLOCKING
None.

## NON-BLOCKING
None.

## NOTES

**Q1. The supplement describes the D-PEC-96 precedent slightly wrongly.**
- Locator: `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-107_MEMORY_GRANT_2026-09-27.md:5`. It calls `D-PEC-96_AMEND_DIRECTION_2026-09-26.md` a case "where a later owner direction on a ruling gets its own record rather than an edit of the merged one."
- That file says of itself (L5–6) that it is "an **amend** direction on the D-PEC-96 proposal, which is not yet ruled". So it was a direction on an unruled proposal, not on a ruling.
- The separate-record point still stands. This is wording only, partly inherited from my review 02's loose phrase. A possible fix: "where a later owner direction gets its own record".

**Q2. The PR description contradicts itself.**
- Its Summary still says "Nothing is written under `_DECISIONS/**`, and no graph or STATUS file is touched."
- Its last paragraph correctly says HELP_HUMAN's later commits add the graph records, the transcriptions, the supplement `_DECISIONS/D-PEC-107_MEMORY_GRANT_2026-09-27.md` and a register-row clause.
- Scope the first sentence to "TM1's own commits" so the description reads consistently. P3's substance (the disclosure) is met.

## Checks

**D-PEC-107 pins.**
- `D-PEC-107_OWNER_DIRECTION_2026-09-27.md` at the head is byte-identical to `acc7d3cc7` (`git diff --quiet` succeeds; SHA-256 `403a0497ae65c413f844b656daf6b3f5a58f99ffd65012dfd42b078430def346`). It no longer appears in the PR diff.
- Every `403a0497` pin now holds:
  - REGISTER.csv rows 11–13 `SourceSha`;
  - `INTAKE.md:162`;
  - the return's source table;
  - the supplement L5;
  - the RV1 branch's records (`0a0408e9c`), which pin the same bytes.
- No dangling "§MEMORY grant" reference remains outside the historical review-01 transcription, and review 02's disposition explicitly supersedes that one.

**Supplement record.** It is faithful and consistent:
- It is a separate, dated record from HELP_HUMAN under K-AUTH-1.
- It quotes the owner verbatim: "grant the MEMORY rows for DEL-00-01 and DEL-00-03". This matches graph L43.
- It names the two exact existing paths.
- It labels "one row each", the row content and the WORKING_ITEMS writer as HELP_HUMAN's interpretation.
- It states that prior bytes are preserved and no other `MEMORY.md` is opened.
- It is cited from the `D-PEC-107` register row, whose citation column adds the file and whose notes clause says it is "recorded separately in `D-PEC-107_MEMORY_GRANT_2026-09-27.md`".
- It is cited from graph L43.
- Its Background accurately says the "grants no `MEMORY.md` path" bullet sits in D-PEC-107 §Freeze point (L85).

**Repairs.**
- **R1:** repaired. The TM-PEC-027 Notes (REGISTER.csv L12) now read "Piping's TM-PIP-030 and TM-PIP-031, the only other elevations to Root in the federated registers, stay OPEN with ElevatedTo Root because their owner ruled OPEN." This is true: those are the only other non-empty `ElevatedTo` values in all four registers.
- **R3:** repaired. A dated HELP_HUMAN note in `returns/TM1_INTAKE_DISPOSITIONS.md` marks `5141b554…` and `0c455b97…` as at `3a96ffa1e`, before the review repairs.
- **P2:** repaired. The graph's C1/M1/F1 row names WORKING_ITEMS for the two granted MEMORY rows, matching supplement L17.
- **P1:** resolved by restoring D-PEC-107.
- **P3:** disclosed, subject to Q2.
- The D-PEC-88 trace line (graph L46) is accurate: no STATUS or README change.

**Transcription (`returns/REVIEW_PR1021_02.md`).**
- **Hash:** the stated hash `5149b825…5702` is correct under its own extraction rule, and the extracted text has no trailing whitespace.
- **Verbatim:** the opening through R1 is byte-identical to my review 02 report (checked mechanically). I read R2 through the Files header by eye, and it matches my report.
- **Disposition:** truthful for R1, R2 (option a), R3, P1 and P2. P3 holds subject to Q2.

**Validation on head, compared with `origin/main` `d39daf548`.**
- `taskmgmt validate`: PASS, 12 rows on REGISTER.csv and 16 on REGISTER_CLOSED.csv (main has 9 and 16).
- Federation: COMPLETE on 4 registers with 28 findings. No finding involves a PEC row.
- Strict registers: exit 1 (0 errors, 26 warnings), identical to main.
- `harness.py self-check`: exit 0, identical once paths are normalized.
- `validate_pec_loop_receipts.py`: exit 0, identical.
- `REGISTER_CLOSED.csv`: byte-identical to main.

**Containment, whitespace and CI.**
- The PR against `d39daf548` touches 11 files:
  - the notice;
  - the brief;
  - the return;
  - `REVIEW_PR1021_01.md` and `REVIEW_PR1021_02.md`;
  - the graph;
  - the supplement (new);
  - `_DECISIONS/_REGISTER.md`;
  - REGISTER.csv;
  - DISPOSITION_FEDERATION;
  - INTAKE.md.
- All of these are under `execution/_Coordination/**` or are the Root notice. D-PEC-107 itself is untouched.
- `git diff --check`: clean, both for the whole PR against `d39daf548` and for the repair commit alone.
- CI at `350fb976d`: pec, harness, Harness pre-merge, Desktop E2E and Select App / PEC / source coverage all pass; the product jobs were skipped by path selection. The PR is OPEN, MERGEABLE and CLEAN.

## Files
(The files as they are at PR head `350fb976d`; read them with `git show 350fb976d:<path>`.)
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-107_MEMORY_GRANT_2026-09-27.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-107_OWNER_DIRECTION_2026-09-27.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_TaskManagement/REGISTER.csv
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260927-RV1-INTAKE/returns/REVIEW_PR1021_02.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260927-RV1-INTAKE/returns/TM1_INTAKE_DISPOSITIONS.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260927-RV1-INTAKE/WORK_GRAPH.md

## Disposition (HELP_HUMAN)

Verdict PASS WITH NOTES; nothing blocking or non-blocking.

- **Q1 (the supplement describes the D-PEC-96 precedent wrongly): carried to the undertaking's closeout PR.** There the wording becomes "where a later owner direction gets its own record". The direction concerned an unruled proposal, not a ruling.
- **Q2 (the PR description contradicts itself): repaired on the PR surface.** The Summary sentence is now scoped to TM1's own commits.

This transcription is a record-only addition after the reviewed head; PR #1021 merges on green CI.
