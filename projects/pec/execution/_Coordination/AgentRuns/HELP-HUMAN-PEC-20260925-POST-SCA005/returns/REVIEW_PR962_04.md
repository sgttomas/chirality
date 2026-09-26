# Review 04 of PR #962 (D-PEC-101 preparation), transcribed

- **Reviewer:** the same read-only `pec-reviewer` as review 03 (`REVIEW_VERDICT_03.md` in the prep folder), resumed by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed verbatim from the host subagent transcript.
- **Reviewed head:** `4c3d73532636a9280657f6484130de634b83b326`. Repair: `2ad18c03c`; this file is added after that.
- **SHA-256 of the report text below (UTF-8; the report text between the blank line after "## Report (verbatim)" and the blank line before the final "## Disposition", with no trailing newline):** `eaff514bcfa49689982c7ef11f7134660ef7619cf4b216722ab7bfd1f825db4f`.

## Report (verbatim)

## Review 04 of PR #962 at head 4c3d73532636a9280657f6484130de634b83b326: PASS WITH NOTES

B1 is now true. The other repairs are accurate, the transcriptions are verbatim and their hashes are correct, containment is right, and `git diff --check` is clean. One NON-BLOCKING finding: `fill_draft.py` no longer reproduces the committed draft, because the draft was rendered before the two new verdict files were added.

Paths are relative to `projects/pec/execution/_Coordination/PEC_REV16_CURRENCY_SETUP_PREP_2026-09-26/`. `DRAFT` means `DRAFT_D-PEC-101_rev16_currency_setup_proposal.md`. Its recomputed SHA-256 is `70894e9caaff5eeef653a018548b8c7a041430311d789fd85f67a64f9c14a33b`, which matches.

### BLOCKING
None.

### NON-BLOCKING

**N1. `fill_draft.py` does not reproduce `DRAFT`, so the draft's artifact table is short two rows.**
- I ran `fill_draft.py` on a copy of the prep folder at HEAD. It produces `7ad17606…5a25`, not `70894e9c…a33b`.
- The only difference is two extra rows in the "Preparation artifacts" table (just after `DRAFT` line 567):
  - `REVIEW_VERDICT_02.md` `5d2fb71e…6cc8`
  - `REVIEW_VERDICT_03.md` `0d27872c…0b26`
- Cause: `fill_draft.py` lists every `.md`, `.py` and `.sh` file in the folder, and the committed draft was rendered before the two verdict files were added.
- No outside reference is affected:
  - neither verdict file cites the draft hash, so re-rendering is not circular;
  - `SHA256SUMS` would need regenerating;
  - the return (line 13) says only that the draft is rendered by `fill_draft.py`.
- Effect today:
  - every row the table does list is correct;
  - `REVIEW_VERDICT_02.md` (line 121) and `REVIEW_VERDICT_03.md` (line 81) say the draft re-renders byte for byte. That was true of the heads they reviewed, but it is no longer true at this head.
- Fix, before filing: re-run `fill_draft.py`, regenerate `SHA256SUMS`, and use the new draft hash. Or record that the verdict files are deliberately left out of the table.

### NOTE
1. **`REVIEW_VERDICT_02.md` is only checked for internal consistency.** I have no access to the in-run reviewer's transcript, so I could not compare it with its source. Its stated hash `c3c5a003…4d83` matches its report section.
2. **Hash convention in both verdict files.** The stated hashes match when the blank line after the "## Report (verbatim)" heading is also stripped, not only the trailing newline. With only the trailing newline stripped, the hashes are `927107ee…` and `2f8d52da…`. The header's wording ("trailing newline stripped") could say so.
3. **The D-PEC-100 note is supported only on an unmerged branch.** `D-PEC-100` appears on `origin/claude/pec-s2-sow-rebuild-proposal` (the briefs `S2P_SOW_REBUILD_PROPOSAL.md` and `S2P_DRAFTER_BRIEF.md`), not on main. The draft says "provisionally", which fits.
4. **`k4/SHA256SUMS` is not listed in the top-level `SHA256SUMS`.** That was already so before this head. All other 134 files in the folder are listed and verify.

### Verified

**B1 repair (`DRAFT` line 361, `.src.md` counterpart)**
- The row now prescribes the original export as the before-state on a combined tree, and states that a K1-applied before-state fails by design.
- On combined trees built from a fresh export of main (`projects/pec` and `tools` are identical from `dfb089b8a` to `f89eb0f65`), running `verify_d101_k4.py base <combined> --covers --allow-k1`:
  - for K4→K1: exit 1 with exactly one FAIL, on containment (changed 149, expected 129), and 10 PASS;
  - for K1→K4: the same result.
- With the K1-applied tree as the before-state: exit 1, with FAILs on exactly the census check (68/68) and the one-provenance-block check (66 contexts, 3 distinct), as the row states.
- `verify_d101_k1.py base <combined> --allow-k4`: PASS.
- Earlier I confirmed the combined tree is the union of K4+C and K1, so the 20 extra paths are K1's modified files.

**Other repairs**
- `DRAFT` line 3: the embedding list now includes the `_REFERENCES.md` closing line, the Declared Upstream text and the DEL-10-13 Run Notes; it says "K4's output bytes carry no packet number (only the K4 generator's docstring names it)"; and it adds the D-PEC-100 note.
- Line 96 (B3): "except the `Notes` prefix and `LastSeen`".
- Line 367: the whitespace check is scoped to product paths, with a run-root `.gitattributes`.
- The draft and `.src.md` each change by exactly those 4 lines.
- The return's review lines are accurate. The review-01 line is qualified, the review-02 line is filled, and review 03 is summarised.

**Transcriptions and dispositions**
- `REVIEW_VERDICT_03.md` lines 9–136 are my review-02 report verbatim. I diffed the first section mechanically and read the rest line by line. Stated hash `9785a5e7…05b1cb` reproduces.
- The shared disposition table accurately describes the changes made.

**Unchanged bytes**
- No generator or `k1/` or `k4/` evidence byte changed; the only new file there is `k1/.gitattributes`, which exempts `evidence/**` and `evidence_aca930622/**` with `-whitespace`.
- Generators remain `075036f0…0e73` and `4892c6a3…cecb`.
- Both `SHA256SUMS` files verify: 134 entries at the top level, and `k4/` all OK.

**Git**
- `git diff --check origin/main...HEAD` is clean.
- Against `origin/main` `f89eb0f65` the PR is 138 additions, all in the prep folder plus the brief and the return.
- The merge `4c3d73532` changes exactly the paths `dfb089b8a..f89eb0f65` changes, with identical content. Outside `projects/chirality-piping/**` that is nothing.

**Every-PR checks at HEAD**
- Harness self-check exits 0.
- The receipts validator is VALID.
- The reliance preflight gives `candidate-validation` ALLOW.

### Disclosure
I modified nothing in the repository. I used one scratch detached worktree at HEAD, which I have removed. Scratch files are under `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/r962.0hxY/`. A malformed `head` command briefly hung waiting on stdin; I stopped it, and it wrote nothing.

## Disposition (HELP_HUMAN)

| Finding | Disposition |
|---|---|
| N1 (`fill_draft.py` does not reproduce the draft) | Repaired in `2ad18c03c`: the draft is re-rendered (`7ad176063b10b4cb3093bc9c1d5c6efbab83fcdb5e6a059e6122c466fd095a25`) with both verdict rows; `SHA256SUMS` regenerated. PR-level review transcriptions from review 04 on are filed under `AgentRuns/…/returns/REVIEW_PR962_NN.md`, so they do not enter the draft's artifact table |
| NOTE 1 (`REVIEW_VERDICT_02.md` source) | Recorded: HELP_HUMAN extracted it verbatim from the host transcript of the in-run reviewer |
| NOTE 2 (hash convention wording) | Recorded: the stated hashes are of the report text without the surrounding blank lines; HELP_HUMAN's transcription header states this from this file on |
| NOTE 3 (D-PEC-100 on an unmerged branch) | No change: "provisionally" is accurate; HELP_HUMAN fixes numbers on publication |
| NOTE 4 (`k4/SHA256SUMS` not listed) | Repaired: listed in the top-level `SHA256SUMS` (135 entries) |
