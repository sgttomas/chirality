# I112 RETURN: PR-N's product gates — T9 and the both-entry gate (parts 1 and 2)

**Verdict: T9 PASS. Part 1 STOP (two classes of difference outside the brief's rule; nothing else). Part 2 PASS.**

Every difference between B and C, in every gate, is a published norm value that moves from this host's libm `hypot` result to the exactly correctly rounded norm. The candidate's value is checked exactly, with Fractions, against the components it is the norm of. Nothing else differs: no outcome, exit code, error text, standing, gate_check row, stderr or timing limit.

The brief's rule does not cover two classes in part 1, so they are stops for WORKING_ITEMS to rule on:
- **S1:** 10 magnitude moves of **2 ulps**, in 6 runs. The rule allows at most one ulp.
- **S2:** moved numbers in **diagnostic text**, in 10 runs. These are not magnitude result fields.

Each is still the exact correctly rounded norm of its own components (§3).

**Who and when:** I112 (TASK, Type 2), dispatched by WORKING_ITEMS for T3 (Agent 1). The brief is `R/BRIEFS/PR_N_GATES.md` (sha256 `fa74a42a…`, verified). I worked on 2026-10-08 from 18:09Z to about 20:20Z, and ran solver-at-scale only for these two gates, under the grant the brief states.

**Revisions:**
- **Base B** = `7eae707bb77722a69b61678c149aa816976bc162` (main, the merge of #1154).
- **Candidate C** = `8dd64c1835698da87e5f0fd303c1b886daee956f`, PR-N's code commit on `codex/piping-t3-correct-norm-20261008`. Its parent is B.

**The branch moved during this run** (an observation; the carry-over is WORKING_ITEMS' ruling). The PR worktree is now at `0c7490e1be`: `dab19291a8`, `8ca80508b6` and `0c7490e1be` follow C. Outside `execution/` they change 5 files:
- **three production files**, with comment-only, line-neutral edits: `lib.rs` (1 line), `correct_norm.rs` (5) and `rigid_body.rs` (4). A check that every changed line is a `//` comment finds 0 others;
- **two test files:** `preview_physics_runtime.rs` and `product_final_case_tests.rs`.

These gates ran on C as briefed.

**Host:**
- The memory guard ran throughout (PID 78827; `memguard.log` has no KILLED line).
- rustc 1.97.1, the default toolchain; python 3.13.14 (`WT/venv/bin/python`).
- **Every cargo** went through `WT/tools/t3_cargo.sh`.
- **The other heavy jobs** each went through `WT/tools/t3_slot.sh`: gen and each side's part-1 driver.
- **Part 2** ran only under `WT/tools/t3_exclusive.sh`, one execution, 20:04:20Z–20:13:49Z.
- I ran one heavy job at a time and signalled no other job. My lock-log lines are in `gate/host_jobs_i112.txt`.
- No Git writes: reads used `GIT_OPTIONAL_LOCKS=0`, and `hash-object` ran without `-w`. No DEC-025 and no installs.
- Targets are under `WT/targets/i112-t9/` and `i112-gate/`; scratch is `WT/scratch/i112_gates/`.
- **Disclosure:** two early runs of my own comparison script, outside a slot, reached about 10 GB and 16 GB RSS on the 400 MB envelopes before I stopped them. The final version streams, and peaked at 4.8 GB.

**Trees** (`trees_check.txt`): `git archive` of `projects/chirality-piping` with `execution/` excluded.
- B has 2,970 files and C has 2,973 (C adds `correct_norm.rs`, its oracle test and its vectors).
- Every extracted file's `git hash-object` equals its blob: 0 mismatches.
- The trees were re-checked after all builds and still match.

## 1. T9 (`t9/`): PASS

**Method:** I61's (KF2 B's).
- S11-K's `fixdiff_main.rs` (`ec089c1d…`), unchanged.
- Built `--release --offline` without `--locked`. Cargo added only the harness package to the copied PP lock (`lock_diff_*.txt`, 9 lines each).
- **PP's lock is unchanged** in both trees: blob `833cbda4…`, the same in B and C.
- Run over `core`, `fixtures` and `validation`, plus F1b's 8-request extra corpus. Its inputs equal KF2's list.

**Results** (`t9_compare.txt`, `t9_compare.json`, `t9_libm_check.txt`):
- **Outputs:** 114 per side (core 10, fixtures 74, validation 30), every rc 0, and no output added or removed.
- **Main corpus:** 105/114 byte-identical. **Extra corpus:** 14/16.
- **11 outputs differ, in 12 values.** Each moves by exactly 1 ulp, and nothing else in the output differs: the accounting is byte-exact, by lexeme. Each candidate value is the exact correctly rounded norm of the same output's own component rows. Each base value is this host's libm chain `hypot(hypot(x, y), z)`.

| Output (mode) | Row | Base → candidate |
|---|---|---|
| `fixtures/product_preview/load_reference/connected.request.json` (sparse) | force magnitude, case cold, support root | `298575.2677594065` → `298575.26775940653` |
| the same (sparse) | force magnitude, case hot, support root | `1172235.122530021` → `1172235.1225300212` |
| the same (dense) | force magnitude, case hot, support root | the same move |
| `fixtures/product_preview/rf_skew_t_cant_off_122_r1e-04.request.json` (dense) | force magnitude, case 8, `rigid:N0` | `1.6258317075882521e-12` → `1.6258317075882523e-12` |
| extra `b7_gap_rf_skew_t_cant_off_122_r1e_04.json` and `kd5_rf_skew_t_cant_off_122_r1e_04.json` (dense) | the same row | the same move |
| `core/reporting/result_export/tests/fixtures/load_reference_fallback_uz.request.json` (sparse) | moment magnitude, case join, anchor | `2.000000000000002e-6` → `2.0000000000000025e-6` |
| `core/product_physics/tests/fixtures/exact_pressure_connected_request.json` (sparse) | force magnitude, case six-component-load, fixture-root | `3741.6573867739435` → `3741.657386773944` |
| `fixtures/model_operations/exact_pressure_authoring_model.json` and `physics_thermal_ui_model.json` (sparse) | the same row | the same move |
| `fixtures/model_operations/precision_connected_ui_model.json` (dense) | moment magnitude, case six-component-load, fixture-root | `3629.04946232481` → `3629.0494623248105` |
| `core/product_physics/tests/fixtures/preview_physics_unicode_ids_model.json` (dense) | combination Σ, displacement magnitude, node γ (mm) | `1.9846472695235164` → `1.9846472695235162` |

**Against I109's expectation:**
- Every expected move is present: `connected` sparse 2 and dense 1, `rf_skew…` dense 1, `fallback_uz` sparse 1.
- The other 6 differing outputs are inputs outside I109's regeneration set: the PP test fixtures, the `model_operations` fixtures and the extra corpus's two rf_skew copies.

**Committed raw fixtures beside requests:** 30.
- **The candidate reproduces all 30.**
- The base reproduces 27. It misses `fallback_uz` sparse and `connected` sparse and dense.
- The committed file is the pretty envelope plus one final newline.

## 2. Both-entry gate, part 1 (`gate/part1/`): STOP

**Method:** I61's (KF2 B's).
- The full-envelope `t3_p1_probe` (`cd1052f7…`, 6 GiB heap cap). Its lock gains only the path package `t3_p1_probe`.
- gen.py 223/223 equal to the calibration's hashes.
- G1's driver, `run.py` and `compare.py`, K-D5's `gate_check.py` with the empty exception lists, and KF2's `compare_gate_kf2.py`, all unchanged.
- 884 runs per side: base 18:53:21Z–18:56:37Z, candidate 18:58:18Z–19:01:46Z.

| Check | Result |
|---|---|
| gate_check, B and C | **PASS**, 764 evaluated, 332 trusted, **0 trusted breach triples**. The 764 rows are identical between sides. |
| Outcomes, both sides | solved 676, refused_blocked 142, refused_capture 64, refused_error 2. Heap-cap aborts 0, timeouts 0, every exit 0. |
| `compare_gate_kf2.py` (identity) | FAIL, as PR-N implies: 126 differences, all envelope hashes. 106 runs differ in the full envelope only; 10 in the full and the summary. No outcome, ok, exit or error-text difference. |
| stderr | 884/884 identical |
| runs.jsonl and stdout | No residue beyond the timing fields, `run.envelope_sha256` (each equal to its side's full-envelope sha256) and the summary span |
| **Full envelopes under the rule** | 702 identical, 66 runs without one, **100 norm-only**, 6 with a 2-ulp move (S1), 10 with diagnostic-text moves (S2) |
| **Runs within the rule** | **868 of 884**; 16 outside |
| Moved magnitudes | **5,254** in 108 runs: force 5,214, moment 40; 5,244 by 1 ulp, 10 by 2 ulps |
| Norm check | **The candidate equals the exact correctly rounded norm in 5,254 of 5,254.** The base equals the libm hypot chain in 5,254 of 5,254. The components are identical on both sides. |

B's 818 full and summary envelopes equal I61's and KF2's (list sha256 `a8fb70b9…`, `32005949…`).

The 116 differing runs are listed in `part1_differing_runs.tsv`, with their counts, the maximum ulp and the check flags. They are grouped by case (51 cases) in `part1_differing_by_case.txt`, and every moved value is in `part1_norm_compare.json.gz`.

## 3. The stops (part 1)

**S1. Ten 2-ulp magnitude moves**, each a support force magnitude whose candidate is the exact correctly rounded norm and whose base is the libm chain, 2 ulps away. A chain of two `hypot` calls can be 2 ulps off.
- `RF-LARGE-CONT-n01000-ROT`:
  - dense, both entries: `rigid:S118`, `210.57088871340565` → `210.5708887134057`;
  - sparse, both entries: `rigid:S435`, `210.570888713408` → `210.57088871340807`.
- `RF-LARGE-CONT-n10000-ROT` sparse, both entries:
  - `rigid:S435`: the same move;
  - `rigid:S2700`: `210.57088871340807` → `210.57088871340812`;
  - `rigid:S3375`: `210.570888713408` → `210.57088871340807`.

**S2. Numbers in diagnostic text** (`diag_norm_check.txt`, `.json`). Every one is explained exactly.
- **`NUMERICAL_INTEGRITY_PHYSICAL_MECHANISM`** (blocking), in `RF-MECH-DISC-CHAIN100` and `RF-MECH-DISC-CHAIN100-SPRING`, both modes and both entries (8 runs).
  - Four entries of the printed mechanism direction move `5.196152422706631` → `5.196152422706632`. They are the D0–D3 UX entries, or the UY entries for SPRING.
  - Each is FK `assess_rigid_body`'s characteristic length times the rigid translation 1. The characteristic length is the maximum of `norm3(p − p_D0)` over the free body. Its maximum is D3 − D0 = (3, 3, 3) from the run's request, so the candidate value is RN(√27) exactly, and the base is the libm chain.
  - These components are request coordinates; the envelope does not echo them.
  - The block's code and outcome are unchanged.
- **`NUMERICAL_INTEGRITY_SENSITIVE`** (warning), in `RF-WEAK-W-3D-rho1e-08` dense, both entries (2 runs).
  - The printed `A01.j: q=` value moves `7.21050920018446e-7` → `7.210509200184459e-7`. That is the formation guard's end bending magnitude, `norm2(My, Mz)`.
  - The candidate's value is the exact correctly rounded norm of the same envelope's published A01 end-j `element_local_bending_moment_y` and `_z`. The base is libm `hypot` of them.

These are within I109's intended scope. RR "I109: a correctly rounded norm replaces libm `hypot` on published paths; …" records `c8369cfda2` as "every product `hypot` reaching published bytes, a receipt or diagnostic text uses the norm", and `d538f469af` as the rank screen. The brief's rule, however, names only magnitude fields and one ulp.

**For WORKING_ITEMS to rule:** whether the rule extends to:
- a move of any size that lands on the exact correctly rounded norm, where the base is the libm chain;
- norm values printed in diagnostic text.

With those two extensions, every part-1 difference satisfies the rule.

**Part 2 was run anyway.** The stop concerns how part 1's differences are judged. Part 2 is independent of that, is within the grant, and lets the ruling close the gate without another dispatch. If the ruling changes the candidate instead, every gate reruns.

## 4. Both-entry gate, part 2 (`gate/part2_run1/`): PASS

**The runs:** the four dense 1,000-member runs on B and C. They are `RF-LARGE-CHAIN-n01000-ROT` and `RF-LARGE-TREE-n01000-AX`, `dense_scrutiny`, captured and typed.
- I13's `gate_part2.py` (`e43c662b…`), unchanged, with `TIMEOUT_LARGE` 1,800 s and its load wait.
- I61's fixed quiet wait and watcher. The quiet wait ran 8 polls; one load wait of 90 s preceded base CHAIN typed.
- **One execution, under `t3_exclusive.sh`.** **0 of 89 watcher samples saw a foreign job**, so no rerun was needed.

**Results** (`part2_combined.tsv`):
- **Every run ended in 44.1–46.3 s**, with exit 0 and no timeout.
- **Outcomes:** every run is `refused_blocked`, `NUMERICAL_INTEGRITY_UNRESOLVED`.
- **Full envelopes:** base and candidate are byte-identical per run: `68cf1929…`, `cb611210…`, `7a3d32b4…`, `9384c225…`. **These equal I61's and KF2's part-2 envelopes.**
- envelopes and stderr are identical; stdout differs only in `run.solve_seconds`.
- **RESULT PASS.**

## 5. Method differences from I61

The full list, with each script's sha256 against its preserved copy, is in `gate/script_provenance.txt`. Every preserved script and input was used byte-unchanged: the probe, the harness, gen, the driver, `run.py`, `compare.py`, `gate_check.py`, `compare_gate_kf2.py`, `gate_part2.py`, `overlap.py`, `part2_combined.py` and the five inputs. Their 12 hashes equal I61's list.

The scripts rebuilt from I61's `.sh.txt` differ only as follows:
1. paths;
2. cargo through `t3_cargo.sh`, the drivers through `t3_slot.sh`, and part 2 under `t3_exclusive.sh`;
3. the interpreter is `WT/venv/bin/python`, the same python 3.13.14; the REPO_ROOT `.venv` that I61 named is absent;
4. T9's run loop is split into `run_t9_runs.sh`;
5. **`foreign_jobs.sh`** filters my own targets, and no longer counts shell and lock wrappers (bash, sh, zsh, lockf, sleep).
   - Since 2026-10-07, T3 jobs queue in wrappers whose command lines carry their job's words.
   - While I hold the exclusive lock they can only be waiting, so counting them would block the quiet wait indefinitely.
   - A running job is still seen through its worker process.

**New scripts:** the identity comparison cannot apply the brief's rule, so I added:
- `setup_trees.sh` and `verify_trees.sh`;
- `normdiff.py` (exact correctly rounded square root, tested against an integer-square-root oracle on 32,000 cases with 0 mismatches);
- `normdiff2.py` (a streaming structure walk for envelopes up to 400 MB; it agrees with `normdiff.py` on all 11 T9 outputs);
- `t9_compare.py`, `t9_libm_check.py`, `part1_norm_compare.py`, `diag_norm_check.py`, `gate_rows_compare.py` and `screen_files.py`.

## 6. Records

All paths are relative to this folder. Bulk outputs are uncommitted, with their hashes and sizes in `gate/uncommitted_sha256.txt`: `WT/scratch/i112_gates/` (trees, T9 outputs, `gen_out`, `part1_{base,cand}/` at about 606 MB of runs.jsonl each, and `part2_run1/`). Nothing was pruned.
- **`t9/`:** the scripts, manifests, lock diffs, build and run logs, sha lists, binary hashes and the comparisons.
- **`gate/`:** the scripts and provenance, probe manifests, lock diffs, build logs and binary hashes, the gen log and hashes, and the host job lines.
  - **`part1/`:** SUMMARY, the driver and gate_check logs and results, schedules, host samples, indexes, the identity comparison, the rule comparison (`.txt`, `.tsv`, `.json.gz`), the S2 check and the gate_check-row comparison.
  - **`part2_run1/`** and `part2_combined.tsv`.
- **Top level:** `trees_check.txt`, `normdiff.py`, `normdiff2.py`, `screen_files.py` and SHA256SUMS.
- **The host screen:** the patterns of `WT/tools/t3_host_screen.py`, run over every record file by `screen_files.py`, give 0 hits. No machine paths appear.
