# I105, J0a: `b2` absorbs main (PR-B1, PR-N)

TASK (Type 2), I105, for WORKING_ITEMS for T3 (Agent 1), the return path by the owner's decision of 2026-10-08. I made no delegation. 2026-10-09 UTC.

**Basis:**
- `R/BRIEFS/B2_J0A.md` (sha256 `94319df1…`, verified);
- WORKING_ITEMS' J0a message: merge main at `ec5d397359`; `b2` at `7cc786285c`.

**Placeholders:** WT, P, R; PP = `P/core/product_physics`; RE = `P/core/reporting/result_export`.

## Heads on `codex/piping-t3-b2-20261008` (WT/b2; not pushed)

| Commit | What |
|---|---|
| `6094636871` | merge of main `ec5d397359` into `b2` (`7cc786285c`) |
| `9f5cfbcd75` | re-pins: the six B2-P pins that held a libm-`hypot` magnitude (RV123 N-1) |
| **`e582b61f9e`** (head) | B1 SQ's rule-8 site table lists B2-P's `combination_call` (found by the suite run; see "Suites") |

**Host screen** (`WT/tools/t3_host_screen.py`):
- `6094636871..e582b61f9e`: 0 hits (2 files).
- `ec5d397359..e582b61f9e` (everything on `b2` that main lacks): 0 hits (79 files).
- `7cc786285c..e582b61f9e` gives 2,503 hits. All of them are in `projects/chirality-app-v4`: main's bytes, which arrive unchanged through the merge. None is mine.

## 1. The merge

**Why git conflicted.** git merged against `601ba408e4`. `b2` forked from b1 at `8d46b045e2`, and PR-B1 was a recut, so git reported 16 conflicted files. I re-merged each file with the fork base (`git merge-file`).

**`merge/merge_check.json`** classifies every path that differs between `7cc786285c` and `ec5d397359` (1,705 paths):
- **Outside P (1,594 paths):** `b2` changes nothing outside P since `601ba408e4`, and every one of these paths equals main.
- **Inside P (111 paths):**

  | Result | Paths |
  |---|---|
  | `b2`'s bytes | 67 |
  | main's bytes | 33 |
  | the clean fork-base 3-way merge: `lib.rs`, `retained_facade_tests.rs`, `retained_memory.rs`, `retained_wire_tests.rs`, frame_kernel `final_case.rs` and `product_final_case_tests.rs`, `test_retained_precision_contract.py` | 7 |
  | hand-resolved | 4 |

  Every other P path equals the clean fork-base 3-way merge, or the bytes of the only side that has it.

**The four hand-resolved files** (`merge/merge_cc_hand.diff.gz` is `git show --cc` of the merge):
- **`retained_product.rs`:** I kept `b2`'s `support_observables` extraction. PR-N's `norm3` support guard now sits inside it (64ε relative of the correctly rounded norm), and its doc says so.
- **`retained_memory_law_tests.rs`:**
  - B1's final `M = 11_274_289_152` and `MARGIN = 9 * M / 10`, with B2-A's `NO_COMBINATIONS`.
  - B1 SQ's two-way runner tie is carried over to B2-A's re-based literals (`const C_EQ_PLUS_ONE`, `const COMBINATIONS`) inside B2-A's `b2_a_runner_oracle_literal_is_case_equivalents_plus_one`.
  - Both sides' appended tests are kept: the B3a-drop and B3b-A tests, and B1 SQ's two.
- **`retainedPrecision.test.ts` and RE `tests/retained_precision_contract.rs`:** both sides' appended tests are kept (the B3 readers' and 07n's).

**After the merge.** I made one more change, at `e582b61f9e`. The merge brought B1 SQ's rule 8 (`s11f_site_test`) over `retained_product.rs`, and `b2`'s `combination_call` (lane P) holds one accumulation, `*next_attempt += 1`, which is an integer attempt ordinal. I added it to the table as `integer: the next attempt ordinal`, like B1 SQ's `selected_attempts` row. This is a test-table row only.

No conflict needed a design choice, and no B2/B3 behaviour changed.

## 2. The moved pins (RV123 N-1)

Six B2-P pins move. Each successor moves in exactly one row, by 1 ulp, to the correctly rounded norm of that row's own components. The check is exact: RN64 of the exact square root of the exact sum of squares (`harness/moved_rows.py`; `pins/moved_rows.log`).

| Witness, mode | Receipt (old → new) | Bytes (old → new) | Row: old → new = CR norm |
|---|---|---|---|
| w_cb2, dense | `0538a919` → `94e468af` | `7d512202` → `cf9d4c6b` | combination support `force_magnitude` at rigid:N0: `0x1.c9a1856ab3947p-40` → `…948p-40` |
| w_cb4a, dense | `c002d0a6` → `00e21ac3` | `ac6076f1` → `f0210262` | the same row and values |
| w_cb4b, dense | `830ecd1c` → `2c5b46ca` | `16bd73ce` → `c558ccfe` | the same row and values |
| c1_range_mechanics, dense | `046bfc3f` → `5b281260` | `e579371e` → `bc641fe3` | the same row and values |
| rv123_c1_two_mechanics, sparse | `577b1fcb` → `6d9f6fc9` | `167eb711` → `98bddd82` | the −3·case ordinary combination `displacement_magnitude` at N1: `0x1.2196d7d8f228ep-2` → `…f228fp-2` |
| rv123_c1_two_mechanics, dense | `b2a8db32` → `88324f91` | `e5ad415d` → `d608a0b0` | the same row: `0x1.2196d7c7415c8p-2` → `…415c7p-2` |

**What did not move:**
- Every other B2-P pin, the W-CB1 and W-CB1z pins, both W-CB3 fixtures, the B3b pins and RV123's S-1 and S-2 pins.
- No retained support magnitude and no retained combination displacement magnitude.

**Why the two displacement rows move.** They are ordinary combination rows. PR-N changed `append_combined_vector_magnitude` (ordinary combination support force and displacement magnitudes) from nested `hypot` to `norm3`.

**The other ordinary rows.** In all 18 compared successors, every ordinary magnitude row equals the correctly rounded norm, with two exceptions:
- w_cb4b sparse `combination-range-ab:disp:N1`;
- c1_range_mechanics sparse `combination-range:disp:N1`.

These are range-envelope rows. They copy an operand case's ordinary `displacement_magnitude`, which PR-N keeps deterministic IEEE rather than correctly rounded. Both rows are unchanged.

**Development runs:**
- At the merge, the full PP lib ran 631 passed, with 2 failures (the two pin tests). `t13` passes.
- After the re-pin, both pin tests pass (`logs/dev_j3_pins_after_repin.log`).

## 3. Suites and census

All runs used archive copies at `9f5cfbcd75` (h), `7cc786285c` (b) and `ec5d397359` (m), one heavy job at a time. PP was rerun at `e582b61f9e` (h2). The table is test by test (`suites/SUITES_CMP.json`, `suites/PROVENANCE.json`, `suites/PP_H2_VS_H.json`):

| Suite | b `7cc786285c` | m `ec5d397359` | h `9f5cfbcd75` | h2 `e582b61f9e` |
|---|---|---|---|---|
| PP, all targets | 791 ok, 1 failed (t13), 11 ignored | 743 ok, 79 ignored | 795 ok, 1 failed (rule 8), 79 ignored | **796 ok, 0 failed, 79 ignored** |
| runner | 85 ok, 2 failed (`load_reference`) | 87 ok | **87 ok** | — |
| RE | 210 ok | 199 ok | **213 ok** | — |
| desktop vitest | 3,680 passed | 4,245 passed | **4,288 passed** | — |
| `tsc --noEmit` | rc 0 | rc 0 | **rc 0** | — |
| PY reader set (16 files; 15 at m) | 2,130 passed, 30 skipped | 2,310 passed, 30 skipped | **2,730 passed, 30 skipped** | — |

**Every difference, accounted for:**
- **Additions:**
  - Every test that h adds over b exists at m: main's, including B1's qualification and PR-N's.
  - Every test that h adds over m exists at b: `b2`'s.
  - No test is new on both comparisons.
- **Outcome changes:**
  - PP `t13` goes from failed to ok, and the runner's two `load_reference` tests go from failed to ok. Both are from PR-N.
  - PP rule 8 failed at h and is fixed at h2. That is the only test that differs between h and h2.
- **Removed against b (B1's qualification arriving):** the nine `witness_tests::witness_*` tests and `retained_direct_peak_is_within_the_profiles_ordinary_span`. Main's B1 final has them as per-mode and per-profile tests (`::dense`, `::sparse`; `retained_memory_challenge.rs::<profile>::<mode>::{direct,ordinary}`). h equals m here.
- **Removed against m:**
  - PP `b1_sa_runner_oracle_literal_is_load_cases_plus_one`. It is B2-A's re-base, which h keeps as `b2_a_runner_oracle_literal_is_case_equivalents_plus_one` with B1 SQ's tie.
  - vitest D31, renamed by the B3 readers (B3D-10).
- **Re-pins:** the six pins above. The pin tests pass at b with the old values and at h with the new ones.

h2 changes only `PP/tests/s11f_site_test.rs`. The runner, RE, vitest, tsc, PY and census results at h therefore hold for h2.

**Census** (RV113's RS and TS harnesses and I100's PY harness, all unchanged and hash-checked; `census/CENSUS_CMP.json`):
- **Corpora:**
  - 07m (`c21112fd…`, 339 entries);
  - B1's 07n (`ea113e7b…`, 638 entries);
  - main's 07n with PR-N's two re-pinned cases, "07n-N" (`0703ec17…`, 638 entries). This is the corpus at h and at m.
- **Comparison:** whole records, entry by entry, at h against b and against m, for RS, TS and PY.
- **Result: 0 changes in all 27 comparisons.** h also matches I101's repair-03 census for 07m and 07n in all three readers (0 changes).

## 4. Dispatch request

Please push `codex/piping-t3-b2-20261008` at **`e582b61f9e`** and dispatch Linux CI on that head.

## Stops and open points

- **Stops:** none.
- **Follow-up, not done:** `combination_observables`' displacement guard in `retained_product.rs` still compares against a nested `hypot` within 64ε. This is unchanged B2 behaviour, and it is robust at that tolerance. Moving it to `norm3` like the support guard is a later choice.

## Host

- **Jobs:**
  - Every cargo run went through `WT/tools/t3_cargo.sh --locked --offline` with toolchain 1.97.1, using targets `WT/targets/i105-j0a-*`.
  - Every other heavy job went through `t3_slot.sh`.
  - One heavy job ran at a time, with one waiter per chain. I signalled no other job.
  - No DEC-025, no installs, and no RSS or timing measurements.
- **Copies:** vitest ran in archive copies, with `node_modules` linked after a `cmp` of `package-lock.json`, and the eight wasm assets copied, never built.
- **PY helpers:** the PY helper binaries were built once from h. `canonical_json` and `units` are byte-identical at all three heads.
- **Junit:** host attributes were removed.
- **Records:** placeholders only. The records screen (host-screen patterns, `.gz` decompressed) found 0 hits. `SHA256SUMS` covers every file.
