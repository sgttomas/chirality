# Review 02 of PR #990, transcribed

- **Reviewer:** the same read-only `pec-reviewer` as review 01 (TASK, `claude-opus-5-5`, high), resumed by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed from the host subagent transcript (verbatim apart from any disclosed whitespace normalization).
- **Reviewed head:** `a473d32b610b684682213e6ea881ca52812606c9`. The repairs listed under Disposition, this file and the `SHA256SUMS` update follow that head.
- **SHA-256 of the report text below (UTF-8; the report text between the blank line after "## Report (verbatim)" and the blank line before the final "## Disposition", with no trailing newline):** `dd3cf917538a366fc02be57ad1c0cd97bf265fdf1bcecfd9c89e6135dc83d480`.

## Report (verbatim)

## PR #990 review 02 (repair head a473d32b6)

**Verdict: PASS WITH NOTES.** Nothing blocks. There is one NON-BLOCKING finding. It is a factual slip in the note-3 disclosure, and it comes from my own review 01. CI is fully green and the "Update the PR base" failure is gone.

I ran only read-only commands: `git fetch`, `git show/diff/archive`, `gh`. I made no git writes and checked nothing out. `TMPDIR` was set before my `mktemp -d` (`rev2.ZDzXYR`), and I have deleted that directory. The worktree is clean. The `rev2.pQpX` directory in the scratchpad was already there and is not mine.

### What changed after 243078f01
- **fd03c3fe5.** It touches three files: the draft, `SHA256SUMS` (the draft line only) and the new `returns/REVIEW_PR990_01.md`. No candidate, script, claim, quote or evidence file changed.
- **a473d32b6.** It merges `origin/main` `7004eaeda`, with parents `fd03c3fe5` and `7004eaeda`.

### Checks
- **Repairs.**
  - **NB-1: correct and complete.** Draft L235 now names DEL-04-05 `REQ-013`. The quotation matches main (DEL-04-05 L216). The ordering bullet (L241) names it too.
  - **NB-2: correct.** The new bullet at L242 matches DEL-03-04 candidate L257 ("every manifest-named feed") and S1 draft L103 (PR #986, still OPEN). "Under either ruling order…" is right, and so is the commit-anchor statement. The work-graph suggestion mirrors the one for DEL-10-11.
  - **Note 4: correct.** Option A (L263) now discloses that the untouched `_REVIEW.md` will still read "EXACT-BYTE ARTIFACT ACCEPTANCE COMPLETE" for the prior bytes.
  - **Note 5: correct.** L258 names the D-PEC-103 act as PR #992. That PR is `claude/pec-d103-first-sows-act`, OPEN and not merged, so "not merged at this draft's last recheck" is true.
  - **No new inconsistency found**, apart from NB-1 below.
- **New source-state bullet (L54): true.**
  - `git diff d385b6a19 7004eaeda` touches only `projects/chirality-piping`.
  - Its first-parent merges are exactly #983 (`3e861f53c`) and #991 (`7004eaeda`).
  - My review 01 did rerun `run_s4p_checks.sh` at `3e861f53c` and got OVERALL PASS.
  - The status line's reservation fact still holds: the register is unchanged since `d385b6a19`.
- **`shasum -a 256 -c SHA256SUMS`** on an archive of a473d32b6: 107/107 OK.
  - The draft is `3e6943139a7d96ed8158674ec0c138f1b2615516d811324d83e1a92a24d88b81`, as stated.
  - `apply_s4p.py` is unchanged at `2b6792fe…4869`.
- **Transcription.**
  - I recomputed the report-text SHA-256 using the file's own stated method and got `38fced88…f69a`, which matches.
  - Its first 25 lines of body text, through the end of section 1, are byte-identical to my hand-back text. I read the rest line by line and it matches my report, with no edits.
  - The dispositions describe the repairs truthfully, with one exception: note 3's reads "seven postimages … (DEL-04-02 says 'provisional')". That repeats my own error; see NB-1.
- **Merge and pins.**
  - `projects/pec` is unchanged from `d385b6a19` to `7004eaeda`.
  - `git diff 7004eaeda a473d32b6` covers exactly 111 files: the 110 PR files plus `REVIEW_PR990_01.md`. Nothing is outside the prep folder, the brief copy, the return and the transcription.
  - I recomputed all 8 preimages and all 19 pins in `apply_s4p.py` at `7004eaeda` and at `a473d32b6`: 0 mismatches.
  - Nothing pinned could have moved, so I did not rerun `run_s4p_checks.sh`.
- **`git diff --check 7004eaeda a473d32b6`:** clean.
- **CI at a473d32b6, all finished.**
  - pass: `pec`, `harness`, `Harness pre-merge`, `Select source coverage`, `Select PEC coverage`, `Select App coverage` and `Desktop E2E (source mode)`;
  - the rest are skipped;
  - mergeStateStatus is CLEAN.

### Finding

**NON-BLOCKING 1: all eight postimages say "not yet ruled", not seven.**
- **Where:** draft L243. The same error is in the transcription's disposition, `REVIEW_PR990_01.md` L141.
- **The error.** The bullet says "Seven of the eight postimages … describe this packet as not yet ruled; DEL-04-02 says only 'provisional'". In fact all eight contain the phrase:
  - DEL-03-04 L391, DEL-04-01 L469, DEL-04-02 L385, DEL-04-03 L23 and L386;
  - DEL-08-01 L214, DEL-08-03 L421, DEL-08-04 L391, DEL-10-03 L446.
  - DEL-04-02's L20 says only "provisional", but its L385 reads "(provisional `D-PEC-102`, not yet ruled)".
- **Where it came from.** My review 01 NOTE 3 (transcription L98–99) listed DEL-04-02 L385 among the locations but wrote "seven of the eight" in its heading. The repair copied that heading.
- **Repair, text only:** change L243 to "All eight postimages … (DEL-04-02 at L385; its L20 says only 'provisional')", and correct the disposition to match. The transcription body stays verbatim. No candidate change is needed.

### Note
- **"Its REQ-013" wording (L241).** In "…its DEL-04-05 quotations of … and its `REQ-013`", "its" refers to the S1 packet. REQ-013 is DEL-04-05's own requirement, not a quotation. The meaning is clear enough; tighten it if the draft is touched again.

### Paths
- Draft (at a473d32b6): `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/PEC_SOW_CURRENCY_S4_PREP_2026-09-26/DRAFT_D-PEC-102_s4_sow_currency_proposal.md` (L54, L235, L241–243, L258, L263)
- Transcription: `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/REVIEW_PR990_01.md` (L141)

## Disposition (HELP_HUMAN)

Verdict PASS WITH NOTES; nothing blocking. Dispositions:

- **NB-1 ("seven", not all eight): repaired.** The draft bullet now says all eight postimages describe the packet as not yet ruled, and gives each line: DEL-03-04 L391, DEL-04-01 L469, DEL-04-02 L385, DEL-04-03 L23 and L386, DEL-08-01 L214, DEL-08-03 L421, DEL-08-04 L391 and DEL-10-03 L446. HELP_HUMAN rechecked these with `grep -n` on the candidates. DEL-04-02's L20 says only "provisional". The note-3 disposition in `REVIEW_PR990_01.md` is corrected to match, with a dated correction line; that file's report text, and so its hash, is unchanged.
- **Note ("its REQ-013"): repaired.** The ordering bullet now reads "and DEL-04-05's own `REQ-013`".

The draft is now `baf178125e37ea8d82735f0bd4c0913531188ca9daffd95309339eb82fffcfdd` (was `3e694313…8b81`), and `SHA256SUMS` is updated to match; all 107 entries pass. The repair head needs a fresh review before merge.
