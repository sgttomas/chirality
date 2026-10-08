# I107 round 2: Pass B on PR-N's code commit (pr_n_passb_01)

TASK (Type 2), I107, for WORKING_ITEMS for T3 (Agent 1), the return path by the owner's decision of 2026-10-08 (RR "Owner decisions: …; T3 gains a WORKING_ITEMS manager"). 2026-10-08 UTC. No delegation.

**The brief:** `R/BRIEFS/PR_N_SB.md` (`e157c13f…`), under B1_COMMON and round 1's B1_SB. **Read:** RR "I109: a correctly rounded norm replaces libm `hypot` …"; `WORKING_ITEMS_LOG.md`; I109's `platform_norm_01` and `pr_n_01` (SHA256SUMS OK); round 1's record.

## The candidate

**`8dd64c1835698da87e5f0fd303c1b886daee956f`** is one commit on main `7eae707bb7` (B1 as merged, #1154). Its 21 files are all under P; nothing outside P changes. P without `execution/` equals NUM `ef8ab78473` (`prep/identity_pn.txt`).

I took an archive of it and compared it with **B1 as merged** for the entry, the delta and the suites. TEXT, the forms, the non-candidates, the controls, the witnesses and the challenge I compared with **SQ's records**, which round 1 matched on PR-B1's code.

## Verdict: `DELTAS TO READ`, exit 6. Three gates to read, every one a listed or environmental difference. No stop.

`VERDICT DELTAS TO READ exit=6 basis=8dd64c1835698da87e5f0fd303c1b886daee956f tag=pn passA=SQ(57c92a7b33..69002bc862+registration) delta_old=B1-as-merged(7eae707bb7) gates=tree:0 entry:0 entry_code:0 m:0 law:0 law_sq:0 statics:0 premise57:0 linemap:0 premise:0 text_run:0 delta:0 text:0 text_n5:0 forms:0 forms_g5:0 noncand_run:0 noncand:0 controls_run:0 controls:0 controls_sq:0 pp_outcomes:6 runner_outcomes:6 witnesses:0 challenge:6`

| Brief item | Result |
|---|---|
| 1. Entry and registration | **Unchanged.**<br>- `REGISTERED_PROFILES` is byte-equal to main's, with `threshold_bytes` 11,274,289,152.<br>- None of the 14 reviewed inputs, and no `Cargo.lock` or `Cargo.toml`, is among the 21 files.<br>- law: 55 passed, 0 failed. The compiled identity, reviewed inputs and layouts equal the entry.<br>- **The 276 `I65_G5_*` in-build record lines equal SQ's registered record, in order.** |
| 2. TEXT, forms, the blocks, M | **Unchanged:**<br>- D 41,769, D_env 22,911, TAV 6,234,394,666, complete. text_budget rows equal SQ's in all four variants.<br>- The profile tree, producer caps, composite text, g4 caps, ordinary caps, T25 and the text closure are byte-equal.<br>- **Both GENERATED PROFILE blocks regenerate exactly:** the N-5 tree gives the head's block, the G5 tree `b075c5c59f`'s.<br>- **The norm adds no text, so G5's and G6's bound and M's margin do not move** (the in-build record above). No stop. |
| 3. Delta | 0. Every row classified; 25 of 25 entries matched (below). |
| 4. `correct_norm`'s loops | No heap, no recursion; every loop bounded except the correction loop, which ran at most 2 passes in every call measured (below). |
| 5. Non-candidates, controls, suites | non-candidates 0: 412 rows, 408 matched, 4 new, 2 gone; the rows equal SQ's once line numbers are dropped (PP `lib.rs` moves by 2). controls 0: 12 of 12, each equal to SQ's. **PP and runner differ only by the listed tests** (gates 6, below) |
| 6. Witnesses, challenge | witnesses 0: all 40 of SQ's entry points pass with SQ's lines. Challenge: **all 27 product entries equal SQ's to the byte**, and the default passes. Gate 6 is only the floor control (below) |

**The three gates to read:**
- **pp_outcomes 6:** against main, one change: `s11g_tests::t13_committed_fallback_uz_is_byte_identical` FAILED → ok. PP is 743 passed, 0 failed, 79 ignored (main: 742 / 1 / 79).
- **runner_outcomes 6:** against main, `load_reference_route_tests::load_reference_one_actual_solve_…` and `cli_load_reference_one_both_modes_…` FAILED → ok. The runner is 87 / 0 (main: 85 / 2).
- **These are I109's listed outcomes** (pr_n_01 §1): the Mac now produces the committed bytes. No test was added or removed in either suite.
- **challenge 6:** `process_floor` printed 4,161 live bytes against SQ's 4,162. As round 1 measured, that count is 4,060 + len(argv[0]), and this run's binary path is 101 bytes. It is environmental.
- **The norm's one-ulp moves:** none shows in the witness or challenge lines. Those lines print outcomes, successor sizes and peaks. W-C2 dense's value moves by one ulp at the same decimal length (I109 §3), so its size (455,479 B) and peak are unchanged. The moved bytes are held by PP's re-pinned fixture tests, which pass.

## The delta rows (`runs/pn/delta_inventory.json.gz`; main `7eae707bb7` → `8dd64c1835`)

**21 files and 39 rows, all classified:** 14 live, 6 item, 5 qualification-test, 4 unreachable, 2 no-code, 2 test and 6 not-d1. All **25** that need an entry have one. The table is `delta_reviewed_pn.json` (`bcf0ce2b…9258b`), built by `mk_delta_reviewed_pn.py`, with 0 refused. Each entry is attributed by me to I109's norm, for RV126 (RV-N) and RV124 to confirm.

**Every production-class row is the norm, by these checks:**
- **M, the module (1):** `FK/src/correct_norm.rs:1–295`, which is new. Its production part has no allocating construct, and on this pass's call graph none of its 10 functions reaches itself.
- **C, call sites (14):**
  - the rows: `lib.rs:4928`, `:5124`, `:11876`, `:11882`, `:13511`; `preview_physics.rs:465`, `:634`, `:966–967`; `retained_product.rs:2446`; `resolve.rs:899`; `rigid_body.rs:52–53`, `:109`; `final_case.rs` after `:1846` and `:1849–1851`;
  - **the check:** every removed line calls `hypot`, and every added line calls `norm2` or `norm3` with the same operands. In each file, the number of `hypot` calls equals the norms' arguments less one per norm, so each chain becomes one norm. The one temporary dropped is `final_case.rs`'s `xy`.
- **D, declarations (5):** `FK/src/lib.rs:6` `pub mod correct_norm;`; stress_recovery `lib.rs:9–12` (`#[path]`); the `use` lines in PP `lib.rs:38–39`, `resolve.rs:18` and `pressure_runtime.rs:13`.
- **Q, qualification tests (5):** `retained_memory_law_tests.rs:134`–`154`, I109 round 2's ring check (RV125 A1-N1). The absolute escape is kept for the 3 counted near-zero residues only, so it is a tightening.
- **The rest:**
  - **unreachable (4):** `elastic_section.rs:106` (no caller, as I109 corrected); `pressure_runtime.rs:1082` and `:1100` (`traverse_region`, reached only through an `edge_zero` rule); and the W-C2 dense fixture, which only `#[test]` code embeds;
  - **no-code (2):** comments;
  - **test (2) and not-d1 (6):** the facade and wire tests, `preview_physics_runtime.rs`, the oracle test and vectors, `k5_constrained_bodies.rs`, the reader corpus and the PY test.

**No production-class row is outside the norm.**

## Item 4: `correct_norm`'s loops and allocation (`FK/src/correct_norm.rs` at the head)

- **No heap.** The production part (lines 1–201) uses only scalars and the stack arrays `[f64; 6]` and `[f64; 10]`. It contains no `Vec`, `String`, `Box`, `format!` or `collect`. **No recursion:** the call graph is `norm2 → norm3 → {midpoint_sign → {square, exact_sign → two_sum}, exponent, ulp_exponent, pow2, scale → pow2, square, two_sum}`.
- **The loops:**
  - `scale`'s `while k > 1000` and `while k < -1000` (`:148`, `:152`) run at most once each, because every caller passes |k| ≤ 1,074;
  - `exact_sign`'s `for &term in terms` (10) and `for i in 0..length` (≤ 10) are bounded by the array (`:178`, `:181`);
  - **the correction `loop` (`:85`) has no static bound in the code.**
- **The correction loop, measured** (`item4/`). I counted passes on a scratch copy with one counter added; the diff to the module is that line alone.
  - The copy reproduces all 1,200 oracle vectors (0 mismatched).
  - **The maximum is 2 passes,** on the vectors (121 of 2,400 calls take 2) and on 20,000,000 random triples, each run through `norm3` and `norm2` (2 of 40,000,000 calls take 2).
  - This agrees with I109's argument: the candidate is RN or a neighbour of it, so the loop makes at most one move and one confirming pass.
- **My loop scan does not need a static bound.** The function has no text site and calls none, so TEXT has no row for its loops (the loop log has no `correct_norm` entry), and TEXT is complete.
- **If a static bound is wanted** (a code change, which I have not made): replace `loop {` at `correct_norm.rs:85` with a counted loop over the same body, for example `for _ in 0..3 { … }`, and add a terminal `r` after it as an unreachable fallback. A test should then assert that the third pass is never reached.

## For WORKING_ITEMS and the reviewers

1. **The line map.** PR-N changes three crates' `lib.rs`. SQ's short `lib.rs:N` rule keys therefore became ambiguous, and SQ's tool refused them (run `prep`, exit 4).
   - `tools/g7_linemap_crates_rows.py` resolves such a key to the one chain-crate file, changed or not, that has a TEXT row at line N in SQ's basis run. Failing that, it takes the one file long enough to hold line N; otherwise the key stays unmapped.
   - It resolved 18 rule keys, all to PP's `lib.rs`. An earlier form of the rule, which considered only the changed files, carried the rules to identical bytes.
2. **TEXT's graph changes**, attributed by `tools/text_pn.py`:
   - +10 nodes (the norm's functions), +29 edges and +29 site-loop entries. The call-site loop headers differ only by the `hypot`/`norm` spelling. The deepest call chain is still 40.
   - Three of the edges are name fan-outs that carry no text: `norm3` → `wide.rs` `sqrt` (two of them) and `exponent` → `wide.rs` `leading_zeros`.
3. **The controls** are SQ's, re-keyed by +2 in PP `lib.rs` (`audit_controls_pn.py`), and compared with line numbers dropped.
   - **Run 1 stopped:** SQ's own copy failed on its 57c92a7b33 keys. That first run (`logs/pass_pn_run1_stopped.log`) was stopped by me; one START it left in `cargo_jobs.log` has no END.
   - **Run 2 reused run 1's targets** (`WT/targets/i107-pn-pn`, `-runner`, `-main`, `-runner-main`, built fresh in run 1).
4. **I109's "16 of 17 in D1" and this delta agree.** `traverse_region` is reachable, but only through an `edge_zero` edge, so the delta tool calls its rows unreachable.

## Execution

- **Jobs:**
  - cargo: through `t3_cargo.sh` (`--locked --offline`);
  - the TEXT points, the sweep, the controls, every test binary, and the loop count's `rustc -O` build and run: through `t3_slot.sh`.
  - One chain of mine ran at a time. Waiting was slowed by other lanes' jobs.
- **Waiters:** twice I left a second waiter running on the same chain; I stopped both.
- **Not done:** no DEC-025, no RSS or timing measurement, no install, no Git write. `WT/pr-n` was not touched.
- **Scratch:** `WT/scratch/i107_pn/`, kept for RV124.
- **Records:** placeholder paths only. The host screen and `SHA256SUMS` cover this folder.
