# I115: the simulated merge, step by step

All commands ran in `WT/t3-pret` (the shared object store) with `GIT_OPTIONAL_LOCKS=0`. Writes were loose objects only (`merge-tree --write-tree`, `hash-object -w`, `write-tree`, `commit-tree`) through a scratch index file (`GIT_INDEX_FILE` outside the repository). No ref, branch, index of any worktree, or working file was written.

## 1. The two bases

| Name | How | Tree |
|---|---|---|
| C = main `ec5d397359` + U3 `1e9724fb94` | `git merge-tree --write-tree ec5d397359 1e9724fb94` (tree `ffb50c98e6`), one conflict in `PP/src/lib.rs`'s import block (lines 38–46), resolved as main's two `correct_norm` lines plus U3's `use …::exact_sum::ExactAccumulator;` | `c64687a327` |
| B2U = `b2` `e582b61f9e` + U3 `1e9724fb94` (what J0b would produce) | `git merge-tree --write-tree e582b61f9e 1e9724fb94` (tree `8628533290`), the same single import conflict, resolved the same way | `9ac081c25a` |

**Check of the resolution.** U3's PR code `8a12de28db` (on main `ba500defa4`) differs from C in product code only by U3's later T2 string (`PP/src/lib.rs`, one line) and its test (`PP/tests/f1b_w2_runtime.rs`); the import block is identical (`git diff c64687a327 8a12de28db -- P ':!P/execution'`).

## 2. T4's planned edit set on C

`t4sim.py` (this folder) builds T4's simulated tree: every line T4-U1 and T4-U3 plan to touch gets a marker appended. For 3-way conflict detection, editing every line of a range is equivalent to replacing or deleting it. The lines are:
- every line matching the curve/joint identifiers (`curved`, `user_stiffness`, `user_element`, `UserTie`, `TieRefusal`, `expansion_joint`, `JOINT_ELEMENT`, `center`, `bend_plane_orientation`, `users`, `user_matrix`, `add_relative_dof_stiffness`) in each planned file; and
- explicit windows (±3 lines unless stated) around every site I3 §1.2 and I5 §1 cite, mapped to C (PP `lib.rs`: I3's U3 line + 2).

Variant **A** (H-4 holds) leaves the summary key and the joint row kind untouched. Variant **B** (H-4 reversed) also edits every key occurrence in the planned files, `retained_product_tests.rs:2435`, and the three reader row-kind sites (`RE/src/retained_precision.rs:2500-2503`, `retainedPrecision.ts:110`, `analysis_runs/retained_precision.py:1150`).

Results: `t4simA.txt` (51 files, 5,298 marked lines; tree `d4498a6600`) and `t4simB.txt` (55 files, 5,309 marked lines; tree `56d3520661`). Both are deterministic (rerun gave the same trees).

## 3. The merges

- `git merge-tree --write-tree --messages --merge-base=C T4A B2U` → exit 0, tree `6d38b99e47`, no conflict (`merge_A_messages.txt`).
- `git merge-tree --write-tree --messages --merge-base=C T4B B2U` → exit 0, tree `ae3bc07813`, no conflict (`merge_B_messages.txt`).
- Direct form against `b2` itself, with history: dangling commits `CC` = `df429ead71` (C, parents `ec5d397359` and `1e9724fb94`) and `TC` = `100a71a1fe` (T4A on CC). `git merge-tree --write-tree CC e582b61f9e` → clean, tree `9ac081c25a` (= B2U); `git merge-tree --write-tree TC e582b61f9e` → clean, tree `6d38b99e47` (= the variant-A result).
- **Sanity:** the variant-A result differs from B2U only by the 5,298 marker lines, and from T4A only by `b2`'s 61,681 added lines.

`shared_files.txt` lists the files both sides change (variant B; variant A is the same list minus the four H-4-reversal files). `margins_A.txt` gives each shared file's nearest T4/`b2` hunk gap in C's numbering.
