# I109, round 2: PR-N's re-pins on the norm branch

TASK (Type 2), continued by WORKING_ITEMS for T3 (Agent 1), which is now your return path. Your round 1 is ruled (RR "I109: a correctly rounded norm replaces libm `hypot` on published paths; …"): PR-N goes as its own PR from main after PR-B1 merges, and carries your four commits plus this round's re-pins. Host, Git and records rules are `R/BRIEFS/B1_COMMON.md`'s, with WORKING_ITEMS in ROOT's place.

## The task, on `codex/piping-t3-platform-norm-20261008` (`WT/t3-norm`, at `b9dea77a85`)

1. **glibc.** Read the diagnostic dispatch run 37808190331 (head `b9dea77a85`, which carries B1's platform fix through NUM) when it completes, against your §6 items 1–5. Say what it establishes and what it does not.
2. **The re-pins,** as product-file commits on the branch (no records in them, so they cherry-pick cleanly onto main):
   - re-pin the Mac fixtures and pins to the correctly rounded bytes (= glibc's): the W-C2 dense fixture and `W_C2_PINNED`, `CBA_PINNED` dense, and the two reader-corpus cases with their hashes and any dependent mutation;
   - retire B1's glibc variants (`W_C2_DENSE_GLIBC`, `CBA_DENSE_GLIBC`) and their `cfg` selection: one pin for every platform;
   - make u1's ordinary pin unconditional at the correctly rounded hash; the next Linux run confirms it;
   - switch m08's own expectation to `norm2`;
   - tighten the ring check (RV125 A1-N1): the absolute escape only for the near-zero entries, a one-ulp check elsewhere;
   - `t13` and the runner's two `load_reference` tests need no change; remove any known-failure listing of them that the product tree carries.
3. **The checks on the Mac:** the affected crates' suites, the PY and TS reader suites that read the corpus, then the 40 manifests (CI's numerical profile, fresh target, through `WT/tools/t3_cargo.sh`). **Expect 0 FAILED.** Compare outcomes with your round-1 base and list every changed outcome.
4. **The D1 call graph:** list which of the norm's call sites lie in the retained route's (D1) call graph, so WORKING_ITEMS can decide whether Pass B applies.
5. **Ask for a Linux dispatch** of the re-pinned head in your return.

Do not cut PR-N, rebase onto main, or push; WORKING_ITEMS does that after PR-B1 merges. ROOT's DEC-025 holds the exclusive lock now; your cargo jobs queue behind it.

## Records and return

`R/I109/pr_n_01/` (RETURN.md, `_run_records/`, SHA256SUMS), placeholder paths only. End your turn with: the branch head and the re-pin commits; glibc's reading; the 40-manifest result; the D1 call-site list; the dispatch request; any stop.
