# Review 02 of PR #1021, transcribed

- **Reviewer:** the same read-only `pec-reviewer` as review 01 (TASK, `claude-opus-5-5`, high), resumed by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed from the host subagent transcript (verbatim apart from any disclosed whitespace normalization).
- **Reviewed head:** `54489b03d6181641b1ae0b1a5e94c9e86293c378`. The repairs listed under Disposition and this file follow that head.
- **SHA-256 of the report text below (UTF-8; the report text between the blank line after "## Report (verbatim)" and the blank line before the final "## Disposition", with no trailing newline):** `5149b825e6de185eec98083305ec0135bfab8a8139df44821a5d307233db5702`.

## Report (verbatim)

**Review 02 of PR #1021 at head `54489b03d6181641b1ae0b1a5e94c9e86293c378`. Verdict: PASS WITH NOTES.** I found no blocking findings, 3 non-blocking findings and 3 notes.

`git ls-remote` confirms that head for `claude/pec-tm1-intake-dispositions`, and confirms `main` = `d39daf548`. The head's parents are `98fcc42bc` (the repair, whose parent is `baf3c1308`) and `d39daf548`. I made no edits, no fetch and no checkout. I read the bytes through `git archive` into `rev1021.IDC9Gi`, ran the validators in scratch-only git repos that borrowed the object store read-only, and then deleted the directory.

## BLOCKING
None.

## NON-BLOCKING

**R1. The TM-PIP-030 contrast in TM-PEC-027's Notes is factually wrong.**
- Locator: `projects/pec/execution/_Coordination/_TaskManagement/REGISTER.csv:12`, Notes. It says: "The only other elevation to Root in the federated registers, Piping's TM-PIP-030, stays OPEN with ElevatedTo Root because its owner ruled OPEN."
- Piping's TM-PIP-031 is also `OPEN` with `ElevatedTo=Root`. Its Notes read "OWNER_RULING_2026-08-03 … PROMOTE OPEN, ElevatedTo=Root".
- Review 01, as transcribed at `returns/REVIEW_PR1021_01.md:22`, already said "TM-PIP-031 has the same form". The repair therefore contradicts the review it answers.
- Fix: "Piping's TM-PIP-030 and TM-PIP-031, the only other elevations to Root, stay OPEN with ElevatedTo Root because their owner ruled OPEN." The rest of the N1 repair is accurate:
  - The return line 30 now correctly says TM-PIP-030 is `OPEN` with ElevatedTo Root, and carries a dated correction note.
  - The Notes now cite PRD candidate §6.2 as the source of the elevation form.

**R2. Editing the merged D-PEC-107 record leaves every existing pin to it stale.**
- Its SHA-256 moves from `403a0497…f346` to `87c2d73a…08a3`. Inside this PR the old hash is still pinned, with no commit qualifier, in:
  - the `SourceSha` of the three new rows (`REGISTER.csv:11`, `:12`, `:13`). Their D-PEC-107 `SourceRef` is not marked "at commit acc7d3cc7", although the intake's is;
  - `TM_PEC_CLOSEOUT_POST_SCA005_2026-09-27/INTAKE.md:162` ("from `D-PEC-107` (SHA-256 `403a0497…`)").
- So when the PR merges, the rows' staleness basis already differs from the live record, and a later staleness review will flag all three rows.
- The same happens across PRs. The RV1 branch `claude/pec-rv1-d1-review` (`0a0408e9c`) pins D-PEC-107 at `403a0497…` as its authority in:
  - both `_REVIEW.md` files (DEL-00-01 L19; DEL-00-03 L30);
  - `RV1_D1_REVIEW_2026-09-27/MANIFEST.md:24`;
  - `briefs/COMMON_REVIEW_TASK.md:16`;
  - two evidence hash files;
  - `REV_DEL-00-01_2026-09-27_1554/Brief.md:7`.
- `projects/pec/AGENTS.md` ("Selection and decisions") tells agents to recompute pinned hashes and stop on mismatch. The sections RV1 cites (§RV1 authorization and §Freeze point) are byte-unchanged, but a mechanical recheck will fail.
- **Is the append sound and faithful?** In substance, yes:
  - It is append-only and dated.
  - It quotes the owner verbatim ("grant the MEMORY rows for DEL-00-01 and DEL-00-03", matching the words the graph recorded).
  - It names the two exact paths, both of which exist.
  - It labels "one row each" and the row content as HELP_HUMAN's interpretation.
  - It puts the grant in the governing D-PEC record, which is what `projects/pec/AGENTS.md` L292–295 asks.
  - The register-row clause is accurate.
- It does, however, depart from recent practice. I found no D-PEC record edited after its merge. The closest precedent, the later owner direction on D-PEC-96, got its own file (`D-PEC-96_AMEND_DIRECTION_2026-09-26.md`).
- Repair, either of:
  - (a) move the grant into a separate linked record, for example `D-PEC-107_MEMORY_GRANT_2026-09-27.md`, cited from the register row. This leaves the pinned bytes intact.
  - (b) keep the append, but qualify every `403a0497` pin as "at `acc7d3cc7`" or re-pin it, and tell the RV1 manager to do the same.

**R3. The TM1 return's "Final hashes" no longer match the head.**
- Locator: `returns/TM1_INTAKE_DISPOSITIONS.md:45` and `:47` give `REGISTER.csv` `5141b554…` and `INTAKE.md` `0c455b97…`.
- The repair changed both files (TM-PEC-027 Notes; the intake's disclosures at L171 and L186).
- The repair also edited the return itself (L30) but left those lines unmarked. Mark them "at `3a96ffa1e`, before review-01 repairs", or update them.

## NOTES

**P1. D-PEC-107 now contradicts itself.** Line 85 still says "This record grants no `MEMORY.md` path". The new §MEMORY grant (L87–97) explains this at L89, but a reader who stops at L85 is misled. A short "(superseded by §MEMORY grant below)" would remove the ambiguity.

**P2. The record and the graph disagree on who writes the MEMORY rows.** The new section (L93) says "WORKING_ITEMS appends". The graph's C1/M1/F1 row lists HELP_HUMAN as owner of the affected records. This is minor; align one of them.

**P3. The PR now edits decision records.** Beyond TM1's original containment, the repair edits `_DECISIONS/D-PEC-107…` and `_DECISIONS/_REGISTER.md`. Both are HELP_HUMAN's records under the default-writable `execution/_Coordination/**`, so this is acceptable, but the PR description should say so.

## Checks

**Repairs.**
- **N2:** repaired. `WORK_GRAPH.md:25` now reads ACTIVE and names `claude/pec-rv1-d1-review`. This is consistent with lines 34–36.
- **O1:** repaired. `INTAKE.md:171` and the K3 bullet at `:186` now disclose both status readings.
- **N3:** repaired in substance; see R2 for the side effects.
- **Graph:** L43 labels the reading as HELP_HUMAN's and points to D-PEC-107 §MEMORY grant. The D-PEC-88 trace line (L46) is accurate: no STATUS or README change.

**Transcription.**
- **Verbatim:** lines 9–50 of `REVIEW_PR1021_01.md` (verdict, findings and notes O1–O3) are byte-identical to my review 01 report. I checked the rest, lines 51–139, by eye, and it matches.
- **Hash:** the stated hash `4c6c8778…abb7a` is correct under its own extraction rule. The extracted text has no trailing whitespace.
- **Disposition:** truthful, with one exception. The N1 bullet says the Notes "name the TM-PIP-030 contrast"; they do, but inaccurately (R1). The O3 answer is fair: the in-run reviews were the manager's verifier child, and this file is the independent review.

**Validation on head, compared with `origin/main` `d39daf548`.**
- `taskmgmt validate`: PASS, 12 rows on REGISTER.csv and 16 on REGISTER_CLOSED.csv (main has 9 and 16).
- Federation: COMPLETE on 4 registers with 28 findings. No finding involves a PEC row.
- Strict registers: exit 1 (0 errors, 26 warnings), identical to main.
- `harness.py self-check`: exit 0, identical once paths are normalized.
- `validate_pec_loop_receipts.py`: exit 0, identical.
- `REGISTER_CLOSED.csv`: byte-identical to main.

**Merge.** It is clean and brings in nothing conflicting:
- `git diff d39daf548 54489b03d` touches only the PR's 10 files.
- Relative to the repair commit, the merge changes nothing under `projects/pec` or `execution/_Coordination`.
- Main's new content since review 01 (`bc1ea504d..d39daf548`, PR #1022) is six `projects/chirality-app-v4` files: an App v4 comparison against PEC upstream. It reads D-PEC-107 consistently with this PR (K3 publication entry, the consumer-contract consideration kept separate, CAND-03 routed to Root) and writes nothing in PEC.

**Containment, whitespace and CI.**
- Containment: the 10 files are TM1's 7, plus `REVIEW_PR1021_01.md`, `D-PEC-107…md` and `_DECISIONS/_REGISTER.md` (see P3).
- `git diff --check`: clean, both for the whole PR against `d39daf548` and for the repair commit alone.
- CI at `54489b03d`: pec, harness, Harness pre-merge, Desktop E2E and Select App / PEC / source coverage all pass; the product jobs were skipped by path selection. The PR is OPEN, MERGEABLE and CLEAN.

## Files
(The files as they are at PR head `54489b03d`; read them with `git show 54489b03d:<path>`.)
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_TaskManagement/REGISTER.csv
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_TaskManagement/TM_PEC_CLOSEOUT_POST_SCA005_2026-09-27/INTAKE.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-107_OWNER_DIRECTION_2026-09-27.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260927-RV1-INTAKE/returns/REVIEW_PR1021_01.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260927-RV1-INTAKE/returns/TM1_INTAKE_DISPOSITIONS.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260927-RV1-INTAKE/WORK_GRAPH.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/chirality-piping/execution/_Coordination/_TaskManagement/REGISTER.csv (TM-PIP-030 and TM-PIP-031)

## Disposition (HELP_HUMAN)

Verdict PASS WITH NOTES; nothing blocking. Dispositions:

- **R1 (TM-PIP-030 contrast wrong): repaired.** The TM-PEC-027 Notes now name TM-PIP-030 and TM-PIP-031 as the only other elevations to Root, both `OPEN` with `ElevatedTo` Root because their owner ruled `OPEN`.
- **R2 (the edit to merged D-PEC-107 left pins stale): repaired by option (a).**
  - `D-PEC-107_OWNER_DIRECTION_2026-09-27.md` is restored byte-for-byte to its merged state (`403a0497…f346`), so every existing pin holds, including the three new rows, the intake and the RV1 branch's records.
  - The grant is now recorded in a separate supplement, `_DECISIONS/D-PEC-107_MEMORY_GRANT_2026-09-27.md`. It follows the `D-PEC-96_AMEND_DIRECTION` precedent, quotes the owner verbatim, and names the two exact paths.
  - The `D-PEC-107` register row cites the supplement.
  - The review-01 disposition's mention of "`D-PEC-107` §MEMORY grant" is superseded by this.
- **R3 (the return's final hashes are stale): repaired.** A dated note in the return marks those hashes as at `3a96ffa1e`, before the review repairs.
- **P1:** resolved by R2's restoration. `D-PEC-107` is unedited, and the supplement explains the grant.
- **P2: repaired.** The graph's C1/M1/F1 row now names WORKING_ITEMS for the two granted MEMORY rows, matching the supplement.
- **P3: repaired.** The PR description now says the PR also adds the supplement decision record and a register-row clause (HELP_HUMAN's records under `execution/_Coordination/**`).

`taskmgmt validate` passes on `REGISTER.csv`. The repair head needs a fresh review before merge.
