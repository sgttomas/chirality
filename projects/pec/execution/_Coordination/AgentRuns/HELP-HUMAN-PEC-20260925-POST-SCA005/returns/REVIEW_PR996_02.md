# Review 02 of PR #996, transcribed

- **Reviewer:** the same read-only `pec-reviewer` as review 01 (TASK, `claude-opus-5-5`, high), resumed by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed from the host subagent transcript (verbatim apart from any disclosed whitespace normalization).
- **Reviewed head:** `5598fd4bb70a5b1d0f7b096862fa037b9f0aaeff`. The repairs listed under Disposition and this file follow that head.
- **SHA-256 of the report text below (UTF-8; the report text between the blank line after "## Report (verbatim)" and the blank line before the final "## Disposition", with no trailing newline):** `7061fd9cf6765053e752b28682f12a9e58d758c7eca93787f7de17b090544796`.

## Report (verbatim)

**Review 02 of PR #996. Verdict: PASS WITH NOTES.** Nothing blocks. All four findings and five notes from review 01 are repaired accurately. The rerun rules have one new gap (finding 1); it is small and should be fixed at or before publication.

I reviewed head `5598fd4bb70a5b1d0f7b096862fa037b9f0aaeff`: its parent is `9fa634f1e`, and it is four X1P commits plus the transcription beyond `4f2e4f44a`. I read everything with `git show`, `git diff` and `git archive` into a scratchpad `mktemp -d` directory built from an explicit template. `TMPDIR` pointed at that directory. I made no edits and no git writes, and afterwards I deleted the directory.

## Checks
- **Full check run.** `run_x1p_checks.sh` against current `origin/main` (still `f0a6159c9`) gives **OVERALL PASS**:
  - act 0 / 0 / 1; containment 34 files plus 1 modify; all six checks exit 0; 10 tests ok;
  - bindings 442/442; pins 19/19; draft claims 67/67;
  - strict, harness and receipts identical before and after; hygiene PASS; fault injection 11/11; negative controls 20/20.
  - The new `SUMMARY.out` has no trailing blanks.
- **`shasum -a 256 -c SHA256SUMS`.** All 111 files OK, and the coverage equals the prep file list.
- **Hashes.**
  - Draft `ca3b6a72…b515`, `SHA256SUMS` `4cecf632…5aca` and `apply_x1p.py` `452ff66a…2428` confirmed.
  - No candidate or act byte changed since `4f2e4f44a`: the diff of `candidates/`, `apply_x1p.py`, the template and the builder is empty.
  - The COMMON copy hashes to `51b70e46…b311`, matching the cited hash.
- **Containment.** Outside the prep folder, the diff against `origin/main` touches only four files: the brief (unchanged since `4f2e4f44a`), `briefs/COMMON_PREP_RULES_2026-09-26.md`, `returns/REVIEW_PR996_01.md` and the X1P return.
- **`git diff --check origin/main...HEAD`.** Clean.
- **CI at `5598fd4bb`.** OPEN, MERGEABLE, CLEAN. Passing: `pec-tests`, `governance-harness`, Harness Pre-merge Validation, Piping Desktop E2E. The rest were skipped by path selection.

## Review 01 repairs, item by item
- **NB-1, paths.** Repaired accurately (draft L65–68, Q3 L409). I checked each citation against the contract text at `origin/main`:
  - DEL-02-09 REQ-003 and DEL-02-08 REQ-007 require normalized repository-relative paths.
  - DEL-02-03 REQ-007 lists repository-relative paths among permitted facts.
  - DEL-02-09 REQ-007, DEL-02-08 REQ-009 and DEL-02-03 REQ-004 prohibit silently omitting a field.

  Checking paths by shape and not by existence is therefore correct. The example claims are true at `d61981ee2`:
  - blob `7c683795…` cites `…DEL-12-01_Local-first storage and private data paths/Specification.md` and `Guidance.md` at lines 33–34, and both are absent;
  - blob `15dcfee1…` cites `execution/_Coordination/DEV-001_DISPATCH_DEL-08-01.md` at line 103, which is absent.

  The loophole of prose placed in a path-typed field is disclosed.
- **NB-2, threshold framing.** Repaired accurately (L62, L66, Limits L397, Q3). The body, Limits and Q3 now say which threshold each TBD assigns. DEL-02-08 TBD-006 is identified as not assigning it, and the 8-word copy threshold is called an operational test of the absolute no-copy rules.
- **NB-3, whitespace.** Repaired: the aid now joins lines with `paste -sd ' '`, and `git diff --check` is clean.
- **NB-4, pin currency.** Repaired. The draft (L152) and return (L94) now say the `FX-PEC-0.graph` path holds `8e32fc0fd` at `f0a6159c9`; this is informational because the pin is by blob. The pin table header is corrected too.
- **Note 5, COMMON.** The rules are now committed, hash-identical. Draft L3 and return L3 are updated.
- **Note 6, "remaining" scan.** Removed from `run_x1p_checks.sh` (hygiene step and message) and from the draft's FX-PEC-0 bullet and Limits. No aid, candidate or evidence summary scans for the word. The one remaining occurrence is a quotation of R-05 in `claims/quotes.json`, which the quotation check verifies. That is not a scan of sections.
- **Note 7, single run.** Addressed at L204, L322, Rollback and row 1a. It is consistent with the act script on the substantive paths:
  - a rolled-back exit 1 restores the preimages and removes `v2/tests/parsers` and its temporary files;
  - the script leaves no marker, so a rerun can pass preflight;
  - a rerun reusing the run root is safe, because the script's own directory is excluded from the write-set inventory.

  Finding 1 covers the gap.
- **Note 8, TMPDIR fallback.** The aids fall back to `.scratch/` beside the script instead of `/tmp`. `test_apply_x1p.py` and the negative controls now honour it, and the runner passes its scratch directory through. See note A.
- **Note 9.** Carried to the first parser packet, as stated.

**Draft edits after verdict 08** (`4db36e6de..9fa634f1e`): the DEL-02-03 REQ-007/REQ-004 citations, the preflight exit-1 rule inside the grant, the rerun run root and `{D}`, and the verdict-08 row. All accurate.

**Transcription `returns/REVIEW_PR996_01.md`.**
- It is **verbatim**: its lines 9–72 are byte-identical to my review-01 report.
- The stated SHA-256 `f62d2644…cbc` is correct. I recomputed it on the text between the delimiters, without a trailing newline.
- The disposition is truthful: verdicts 07 (FAIL, then repaired) and 08 (PASS WITH NOTES) exist, and each repair it lists is present.

## Findings
**NON-BLOCKING**
1. **The exit-code rule mistakes a usage error for an incomplete rollback.** The grant (draft L204: "A run that exits 2 (incomplete rollback) consumes it too") and the failure semantics (L320) treat any exit 2 as an incomplete rollback. But `apply_x1p.py` parses its arguments with `argparse`, which exits 2 on a usage error, before any preflight or write. I confirmed that argparse exits 2 on a missing required argument. So a mistyped flag would, read literally, consume the single run and force owner routing even though nothing was written. The script writes the string `ROLLBACK INCOMPLETE` only on its real exit-2 path (L287). Fix: key the rule to exit 2 together with that `FAIL …; ROLLBACK INCOMPLETE` line, and treat any other exit that writes nothing like a preflight refusal.

**NOTE**
- **A.** The `.scratch/` fallback lives inside the repository tree, in the prep folder or run root, and is not git-ignored (`git check-ignore` finds no rule). With `TMPDIR` unset, the aids would temporarily put full `git archive` exports and copies of `projects/pec` under `projects/pec/execution/_Coordination/…`. A crashed run could leave them untracked, where a broad `git add` of the run root would pick them up. The directory itself persists, but empty, so git ignores it. On macOS `TMPDIR` is normally set, to `/var/folders/…`, so the fallback rarely applies. Consider stating in finite verification that `TMPDIR` must point at a scratchpad directory.
- **B.** The grant's preflight classes (L204) name the missing candidate and the drift cases. They leave three failures to "transient local problem": a candidate hash mismatch (fix by recopying the bound bytes), a leftover temporary sibling (in practice only after an exit 2) and running from outside a run root. This is readable as intended, but one clause naming them would remove the ambiguity.
- **C.** The draft edits after verdict 08 have had no fresh reviewer apart from this review. I found no defect in them beyond finding 1.

Files (at the PR head; this worktree is on a different branch):
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/PEC_X1_FIXTURES_PREP_2026-09-26/DRAFT_D-PEC-106_x1_parser_fixture_suites_proposal.md (L204, L320, L322)
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/PEC_X1_FIXTURES_PREP_2026-09-26/apply_x1p.py (L203–206 argparse; L287 exit 2)
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/PEC_X1_FIXTURES_PREP_2026-09-26/run_x1p_checks.sh (L9–11)
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/REVIEW_PR996_01.md

## Disposition (HELP_HUMAN)

Verdict PASS WITH NOTES; nothing blocking. HELP_HUMAN made these repairs:

- **NB-1 (exit 2 conflated with a usage error): repaired.** The grant now ties the consuming exit-2 case to the script's `FAIL …; ROLLBACK INCOMPLETE` line. Any other exit that writes nothing, including an `argparse` usage error, is treated as a preflight refusal: it is recorded and does not consume the grant. The failure-semantics bullet says the same.
- **Note A (TMPDIR fallback inside the tree): repaired.** Finite verification now requires `TMPDIR` to be set to a scratch directory outside the repository before any aid runs, and says why.
- **Note B (preflight classes): repaired.** The grant now names the candidate hash mismatch, running from outside a run root, and a leftover temporary sibling as fix-and-rerun classes.
- **Note C:** this review covered the edits made after verdict 08.

The draft is now `677b59f6b1ae19b911e6e07aecfa4df0f39a380fb3ab806903da87c8fa18d279` (was `ca3b6a72…b515`), and `SHA256SUMS` is updated. No candidate or act byte changed. The repair head needs a fresh review before merge.
