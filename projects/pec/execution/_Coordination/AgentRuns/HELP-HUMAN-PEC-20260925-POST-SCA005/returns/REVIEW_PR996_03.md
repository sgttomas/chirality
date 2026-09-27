# Review 03 of PR #996, transcribed

- **Reviewer:** the same read-only `pec-reviewer` as reviews 01 and 02 (TASK, `claude-opus-5-5`, high), resumed by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed from the host subagent transcript (verbatim apart from any disclosed whitespace normalization).
- **Reviewed head:** `3d47a82256e7503c940b8d5449196df3200e7e09`. This file is the only addition after that head.
- **SHA-256 of the report text below (UTF-8; the report text between the blank line after "## Report (verbatim)" and the blank line before the final "## Disposition", with no trailing newline):** `22126aa171ecc7b7a7471b034b8950671db816ac83a2f573d962f498cbeececd`.

## Report (verbatim)

**Review 03 of PR #996. Verdict: PASS.** Nothing blocks, and nothing needs repair. The note below is optional wording.

I reviewed head `3d47a82256e7503c940b8d5449196df3200e7e09`, whose parent is `5598fd4bb`. As before, I read with `git show`, `git diff` and `git archive` into a scratchpad `mktemp -d` directory built from an explicit template, with `TMPDIR` pointed at it. I made no edits and no git writes, and afterwards I deleted the directory.

## Scope of the commit
The commit changes exactly three files:
- the draft;
- `SHA256SUMS`, where only the draft's line changed, to `677b59f6…d279`;
- the new `returns/REVIEW_PR996_02.md`.

No candidate, act-script, aid or evidence byte changed. `apply_x1p.py` is still `452ff66a…2428`.

## Repairs checked against `apply_x1p.py`'s real behaviour
- **NB-1 (draft L204 grant; L320 failure semantics).** Accurate. The single run is now consumed only by exit 2 together with the `FAIL …; ROLLBACK INCOMPLETE` line. The script prints that line only on its real exit-2 path, at L287. An `argparse` usage error exits 2 before preflight and writes nothing; it is now treated as a preflight refusal and recorded. That matches the code: `parse_args` runs before any file access, and argparse's error exit is 2.
- **Note B (L204).** Accurate. The three fix-and-rerun classes (candidate hash mismatch, running from outside a run root, leftover temporary sibling) match the script's preflight checks at L209–237. The route-to-owner classes match too: target off its preimage, pinned file changed, created target or `v2/tests/parsers` already present.
- **Note A (finite-verification preamble, L339).** Accurate. It requires `TMPDIR` to point at a scratch directory outside the repository before any aid runs, and says why.

## Checks
- **`SHA256SUMS`.** `shasum -a 256 -c` passes for all 111 files, and the coverage equals the prep file list. Draft `677b59f6…d279` confirmed.
- **Draft claims.** `verify_x1p_claims.py` on the new draft: **RESULT PASS 67/67**.
- **Full check run.** `run_x1p_checks.sh` against current `origin/main` (`f0a6159c9`) gives **OVERALL PASS**. Every step passes, including draft claims 67/67, bindings 442/442, pins 19/19, fault injection 11/11 and negative controls 20/20.

## Transcription `returns/REVIEW_PR996_02.md`
- It is **verbatim**: the report text between the delimiters is identical to my review-02 report.
- The stated SHA-256 `7061fd9c…4796` is correct. I recomputed it on the delimited text, without a trailing newline.
- The disposition is truthful. The three repairs it lists are present as described, note C is accurately described, the draft hashes before and after are correct, and no candidate or act byte changed.

## Containment and CI
- **Containment.** Outside the prep folder, the diff against `origin/main` touches only the brief, `briefs/COMMON_PREP_RULES_2026-09-26.md`, `returns/REVIEW_PR996_01.md`, `returns/REVIEW_PR996_02.md` and the X1P return.
- **`git diff --check origin/main...HEAD`.** Clean.
- **CI at `3d47a8225`.** Finished: OPEN, MERGEABLE, CLEAN. `pec-tests`, `governance-harness`, Harness Pre-merge Validation and Piping Desktop E2E all succeeded. The per-job checks passed or were skipped by path selection.

## NOTE (optional)
The parenthetical "leftover temporary sibling (in practice only after an exit 2, below)" at L204 sits a little awkwardly, because an exit 2 already consumes the grant and goes to the owner. In practice a leftover temporary file on a still-open grant can come only from a run that died without an exit code, such as a kill or power loss mid-write. A run like that is not otherwise classified. The wording can stand; tightening it is up to HELP_HUMAN.

Files (at the PR head; this worktree is on a different branch):
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/PEC_X1_FIXTURES_PREP_2026-09-26/DRAFT_D-PEC-106_x1_parser_fixture_suites_proposal.md (L204, L320, L339)
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/PEC_X1_FIXTURES_PREP_2026-09-26/apply_x1p.py (L203–237, L287)
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/REVIEW_PR996_02.md

## Disposition (HELP_HUMAN)

Verdict PASS. There is one optional wording note, with no change here: a leftover temporary sibling on an open grant can come only from a run killed mid-write. The act brief will say that such a run is recorded and treated as the fix-and-rerun class, after the targets are checked against their preimages. This transcription is a record-only addition after the reviewed head; PR #996 merges on green CI.
