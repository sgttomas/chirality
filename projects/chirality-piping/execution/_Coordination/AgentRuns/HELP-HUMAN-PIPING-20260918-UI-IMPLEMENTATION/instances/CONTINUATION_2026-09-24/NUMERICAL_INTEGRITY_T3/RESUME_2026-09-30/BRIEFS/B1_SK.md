# I108: SK, PR-B1's evidence package (records only)

Read `R/BRIEFS/B1_COMMON.md`. It binds you. You wrote none of B1. **The owner directs production first: the package is short and factual, and it cites records rather than restating them.**

## The candidate

- **PR-B1's code commit:** `8248921552` on `codex/piping-t3-pr-b1-20261008` (`WT/pr-b1`). It is cut from main `6c821d9ccf` and carries the 33 maintained files that NUM `a41eea7b5f` changes outside the execution records.
- **Check it with `T/IMPLEMENTATION/F2A_D1/source_equality.py`:**
  - `--repo WT/pr-b1 --pr 8248921552 --int a41eea7b5f --main 6c821d9ccf --work WT/scratch/i108_b1_sk/seq`;
  - checks 1–3 and 5 pass today;
  - check 4 needs your package (`--package`).
- **The form:** T6S's package (`T/IMPLEMENTATION/T6S/`) and U8's (`T/IMPLEMENTATION/U8/`). The tools are in `T/IMPLEMENTATION/F2A_D1/`.
- **The basis:**
  - PLAN_v2 §6 and its "B1's evidence in the package" list (`R/I84/b1_plan_01/PLAN_v2.md`);
  - every B1 ruling in RR from "B1's PLAN_v2 accepted; …" through "R6b: …";
  - the slice returns and reviews (SP, SA, SR-*, SC, SQ, SG and their RV-P, RV-R and RV-Q records).

## Deliverable: `T/IMPLEMENTATION/B1/`

1. **CHANGE_RECORD.md:**
   - **What the PR contains:** each of the 33 files, with its +/− lines, a one-line change, and its sha256 at `8248921552`.
   - **What it does:** C = 3 at S3 through the retained route. The Direct entry is in the registered dev/test build only, with M = 11,274,289,152 B (10.5 GiB). The three readers' eligibility; 07n.
   - **What it does not do:** no product caller; no public activation (B8); no supported-machine statement (owner-held); B2, B3, S-I2, F2b and F3.
   - **Review:** one line per review, with its counts and repairs.
   - **Gates:** rows that need the PR head (Pass B, CI and the dispatch, GEN-8, DEC-025, the src-tauri suite, T9, both-entry) read "see the merge record". SG's Direct-entry gates cite I106.
   - **B1's evidence,** by citation:
     - QUAL_B1 with M's ruling and the text-error budget, including QUAL's §7 (the identifier audit) and §9 (controls), per Q-N3;
     - the generator and the profile tree;
     - `registration.diff`;
     - the witness logs and the challenge;
     - RSS_TIME with R9's reading;
     - 07n's parity;
     - the W-C2 pins;
     - RV95 N-5's direct test;
     - RV97 R2-N-2.

     Copy only the small files a reviewer of the PR needs (QUAL_B1.md, RSS_TIME.md and `registration.diff`) into `copies/`, as F2A_D1 does.
   - **Routed notes:** the open notes that go to B2, B3 or SQ2, one line each.
2. **PR_BODY.md:** short and plain, in the form of T6S's. State that the reviews are agent reviews, not personal review by the owner.
3. **citations.json** for `check_citations.py`, pinned at NUM's head. Run it with `--base 6c821d9ccf --head 8248921552`, and record the output in `_draft_run_records/`, which ROOT removes at the cut.
4. **SHA256SUMS** over the package.

Then run `source_equality.py` with `--package` on a scratch copy that holds your package (for example a `git worktree add --detach` of `8248921552` under `WT/scratch/i108_b1_sk/`, with the package copied in and committed there). Report checks 1–5. Remove that worktree afterwards.

## Rules

- **Records only.** No source edits, no Git writes on a shared branch, no cargo, vitest or native jobs, and no installs. Use Python from `WT/venv`.
- Placeholder paths only. Scratch goes in `WT/scratch/i108_b1_sk/`.
- Every claim is checked against Git or the records. Where the records disagree, say so.
- If the host's write guard refuses a write into NUM, write to `WT/scratch/i108_b1_sk/records/` and say so.

## Return

- **Budget:** 2–3 h.
- **End your turn with:**
  - the package's files with sha256;
  - the citation result;
  - source equality checks 1–5;
  - anything ROOT must rule on.
