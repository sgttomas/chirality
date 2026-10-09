# RV123 (RV-P2, round 2), addendum 02: J0a (main into `b2`), the re-pins and PP resolutions

TASK (Type 2), RV123. Return path: WORKING_ITEMS for T3 (Agent 1). 2026-10-09 UTC. This extends `REVIEW.md` and `ADDENDUM_01.md` and changes neither. Its checksums are in `SHA256SUMS.addendum_02`.

**Scope.** `b2` head `e582b61f9e`:
- `6094636871` merges main `ec5d397359` into `7cc786285c` (b);
- `9f5cfbcd75` re-pins;
- `e582b61f9e` adds the rule-8 row.

I read I105's `R/I105/b2_j0a_01/RETURN.md` (`1e001ebf…`; its SHA256SUMS verifies 132 of 132).

I did not review the B3 reader merges already on b (`cf607a02cd..7cc786285c`), nor main's own content. I checked only what J0a did.

**How:**
- Copies are `git archive` from NUM's objects: `WT/rv123/{j0a, j0achk, bchk, mainchk}`. I never used `WT/b2`.
- Cargo went through `WT/tools/t3_cargo.sh` (`--locked --offline`), targets `WT/targets/rv123-r2-{j0a,j0achk,bchk,mainchk}`, one heavy job at a time. I signalled nothing. No Git writes.

**Placeholders:** as in `REVIEW.md`. E is `evidence/addendum_02/`.

## Verdict

**Confirmed, with 0 BLOCKING, 0 SHOULD-FIX and 2 NOTE.**
- Each re-pin is exactly the norm move.
- No other B2-P pin or byte moved.
- The four hand resolutions keep both B1's final code and B2-P's behaviour.
- The rule-8 row is right.

## 1. The six re-pins: exactly the norm move (`E/results/j0a_repin_check.txt`)

**Method.** I re-dumped all 22 B2-P successors at `e582b61f9e` with my unchanged round-2 harness: the 20 pinned witness/mode pairs, W-CB1 and W-CB1z, and my unpinned B + 0.5·A probe. I compared each with my dump at `72b3e5d9ea`, by row id and by every other field.

**What moved.** Exactly 6 successors changed: the 6 I105 lists. Their new successor-bytes sha256 values equal the new pins. In each:
- exactly one row moves, by 1 ulp;
- the new value is RN64 of the exact 3-norm of that row's own three components, decided exactly;
- the old value was not;
- the components are unchanged;
- the row is ordinary (no `recovery_method`).

| Moved row | Witness and mode | Change |
|---|---|---|
| `rigid:N0` force magnitude | w_cb2, w_cb4a, w_cb4b, c1_range_mechanics (all dense) | `0x1.c9a1856ab3947p-40` → `…948p-40` |
| `combination-m3case:disp:N1` | rv123_c1_two_mechanics, sparse | `…f228ep-2` → `…f228fp-2` |
| `combination-m3case:disp:N1` | rv123_c1_two_mechanics, dense | `…415c8p-2` → `…415c7p-2` |

The receipt is identical apart from `publication_sha256` and `receipt_sha256`.

**What did not move.** The other 16 successors are byte-identical, including W-CB1, W-CB1z, both W-CB3 modes, B + A and B + 0.5·A. The two W-CB3 fixtures and DEF-C's file are unchanged in Git. No retained row moved in any successor.

**Independent checks.** `b2p_checks.py` against J0a's P passes all 22: 0 failures, including the publication and receipt hashes.

## 2. No other B2-P byte moved

I ran my unchanged byte harness (37 inputs × 2 modes) at main, b and J0a.

**J0a against main** (`E/results/bytes_compare_j0a_vs_main.txt`):
- Plain bytes are identical for all 74.
- Direct bytes are identical for every input except b2's own features:
  - the 4 R-7 combination inputs, which publish main's plain bytes plus T-12's notices exactly;
  - the 4 exact-route `m3x*` inputs, which publish b2's successors.

**J0a against b, Direct output** (`E/results/j0a_merge_bytes_vs_b.txt`):
- 64 of 74 are identical. These include every exact-route successor and the milestone successor.
- The other 10 differ only in ordinary rows, 58 in all. Each change matches main's plain change for the same input exactly: same row, same old value, same new value.
- No retained row changed, and no other field changed.

## 3. The merge (`E/results/j0a_merge_recheck*.{json,txt}`)

I re-derived I105's classification independently from the objects, using `git merge-file` on the fork base `8d46b045e2`, and it matches exactly:
- 1,594 paths outside P equal main.
- Inside P:
  - 67 paths take b's bytes;
  - 33 take main's bytes;
  - 7 are clean 3-way merges;
  - 4 conflict (1, 1, 1 and 3 hunks).
- For each of the 100 paths taken from one side, the other side is unchanged since `8d46b045e2`.

**The base is right.** `8d46b045e2` is b's fork point from b1, and it is not an ancestor of main, because PR-B1 was a recut. git's own merge base, `601ba408e4`, is an older main merge; I105 reports it gave 16 conflicted files.

**The four hand resolutions:**
- **`retained_product.rs`:** main's only change to this file since the fork is `hypot(hypot)` → `norm3` in the support guard. The merge applies exactly that inside b's extracted `support_observables`, plus a doc update; nothing else differs from b. So B1's final guard holds for case freezes, and through `support_observables` for combination freezes too. Within the guard's 64ε tolerance this changes no outcome: no witness moved.
- **`retained_memory_law_tests.rs`:**
  - Hunk 1: main's `M = 11_274_289_152` and `MARGIN`, plus b's `NO_COMBINATIONS`.
  - Hunk 2: b's C_eq + 1 assertions, with main's two-way runner tie moved onto b's runner lines (`const C_EQ_PLUS_ONE: usize = 4;`, `const COMBINATIONS: usize = 1;`). The runner file is b's, since main left it unchanged.
  - Hunk 3: b's appended tests, then main's, each verbatim, joined by one closing `}`.
- **`retainedPrecision.test.ts` and RE's `tests/retained_precision_contract.rs`:** each is b's appended block plus main's, verbatim, joined by one closing brace.

**PP at `e582b61f9e`** (`E/logs/j0a_pp_reg.txt`), my own run: 796 passed, 0 failed, 79 ignored. Both `rule_8_every_accumulation_in_the_listed_files_is_in_the_table` and t13 pass. This matches I105. I did not re-run the runner, RE or the census; those figures are I105's.

## 4. The rule-8 row

`combination_call` holds exactly one rule-8 shape, `*next_attempt += 1`, so the count of 1 is right. It is an integer attempt ordinal, at most C_eq ≤ 3, so the disposition "integer: the next attempt ordinal" is right. The row is in the same form as `selected_attempts`. No other B2-P function in `retained_product.rs` is missing from the table; the test passes.

## 5. Findings

**J-N1 (NOTE): the displacement guard in `combination_observables`.** It compares against nested `hypot` within 64ε (`retained_product.rs` 5724). My view: correct and robust as it stands.
- It is a guard, not a published value, so no byte depends on libm.
- Nested `hypot` is off by a few ulp at most. 64ε relative is about 2⁻⁴⁶, so the margin is more than an order of magnitude.
- Moving it to `norm3`, like the support guard and FK's projection, is a uniformity change. Make it at the next edit of that function, with its doc at 5680. It need not block J0a or wait for Linux CI.

**J-N2 (NOTE): round 2's N-1 is resolved in substance.** At J0a, no B2-P published magnitude is formed by libm:
- FK's `support_hypot` and PP's `append_combined_vector_magnitude` use `norm3`;
- PP's remaining `hypot` calls are only this guard and one test.

The Linux CI run remains the confirmation.

## For the return path

Nothing needs a ruling.
