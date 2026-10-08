# I112: PR-N's product gates — T9 and the both-entry gate

TASK (Type 2), dispatched by WORKING_ITEMS for T3 (Agent 1), your return path. You do not delegate. **You are a fresh instance.** Read `R/BRIEFS/B1_COMMON.md` for the host, records and placeholder rules, with WORKING_ITEMS in ROOT's place.

**The grant.** You may run solver-at-scale jobs for these two gates only, as I61 did for U9 (RR "U9 G5 (T9) and G6 (both-entry) pass; …", under the I20/KF2 precedent). The gate set requires them because PR-N changes published bytes on the D1 call graph (RR "T3's gate set and Git rules, …", item 7).

## The revisions

- **Base B:** main `7eae707bb7`.
- **Candidate C:** PR-N's code commit `8dd64c1835` (`codex/piping-t3-correct-norm-20261008`). It replaces libm `hypot` with a correctly rounded norm on published paths. See `R/I109/platform_norm_01/` and `R/I109/pr_n_01/`.

Use `git archive` trees of `projects/chirality-piping`, with `execution/` excluded, and check every extracted blob.

## The method: exactly I61's (`R/I61/u9_g5g6_01/`)

Its scripts are preserved there as `.txt` files (`gate/*.sh.txt`, `gate/*.py`, `t9/…`). Rebuild them from those records and from S11-K's `fixdiff_main.rs`, and record each script's sha256 against the preserved copy. Note every difference you have to make. The host's scratch was wiped on 2026-10-08, so nothing under `WT/scratch/u9_*` remains.

1. **T9:** release builds of both trees over `core`, `fixtures` and `validation` and F1b's extra corpus. Build `--offline` without `--locked` as U9 decision 10 allows, then check the lock diff: PP's lock must be unchanged.
2. **The both-entry gate, part 1:** every run except the 4 known dense timeouts, on both entries and in both modes. `gate_check` must pass on B and C with 0 trusted breach triples. Compare B and C run by run.
3. **Part 2:** the 4 timeout cases on a quiet host. Run them **only under `WT/tools/t3_exclusive.sh`**, one execution at a time, with the overlap watcher as I61 fixed it.

## The acceptance rule for differences

Identity is required except where the norm moves a published magnitude. List every differing output or run. For each, show that:
- it differs only in magnitude fields, by at most one ulp, plus the hashes over them;
- the candidate's value equals the correctly rounded Euclidean norm of the same output's own components (an exact check: integers or `fractions`).

Any other difference is a **stop**. I109's envelope regeneration expects moves in `load_reference/connected` (sparse 2 values, dense 1), `rf_skew…` dense (1) and `load_reference_fallback_uz` sparse (1). The committed raw fixtures beside those requests should now be reproduced exactly.

## Host and records

- Targets under `WT/targets/i112-*`; scratch in `WT/scratch/i112_gates/`. Run one heavy job of yours at a time, through `WT/tools/t3_cargo.sh` or `WT/tools/t3_slot.sh`. Never signal another job. No DEC-025 and no installs.
- Records go in `R/I112/pr_n_gates_01/` (RETURN.md, `t9/`, `gate/`, SHA256SUMS), placeholder paths only. If the host refuses a record file, put its full content in your final message with the intended path; do not work around the refusal.
- Budget: 3–4 h, mostly build and run time.

End your turn with:
- T9's and each part's verdict;
- the list of differing outputs and runs, each with its norm check;
- RETURN's sha256;
- any stop.
