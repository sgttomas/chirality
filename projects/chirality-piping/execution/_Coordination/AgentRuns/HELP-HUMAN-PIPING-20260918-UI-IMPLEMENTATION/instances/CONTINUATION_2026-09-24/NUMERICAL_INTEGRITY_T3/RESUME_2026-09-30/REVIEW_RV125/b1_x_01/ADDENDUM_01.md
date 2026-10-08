# RV125 (RV-X, B1), ADDENDUM_01: PR-B1's platform test repair, confirmed

**The request:** ROOT's message to RV125, a same-reviewer repair confirmation. The basis is RR "I107's Pass B (no stop); PR-B1's hosted CI fails on Linux: …" and "RV124 confirms B1's Pass B; the platform test fix committed on NUM", read at NUM `31eed8497f`.

**The candidate:** #1154's new code commit `7f5f72912ec53b306abaaa0aec4dbcc4281af6d6`, cut from main `953d8c94466db5543426a2de7b26a591564e4dca` (#1155, App v4 only) and pushed. It replaces `d07006c2f0`. SK's refreshed package follows as commit 2, so this addendum covers the code commit only.

**Placeholders:** as in REVIEW.md. `E1` = `_run_records/addendum_01/`.

## Verdict: **CONFIRMED.** 0 BLOCKING, 0 SHOULD-FIX, 1 NOTE

The repair is exactly the test-only change described, in three PP test files. Each glibc value is exact, and I derived each one independently from the macOS bytes. The macOS path is unchanged, bit for bit, and no pin is weakened.

## 1. The delta

- **The diff.** `git diff d07006c2f0 7f5f72912e -- projects/chirality-piping` (+110/−9) has sha256 `744c1633a635453a…3c8b08`. That is the hash ROOT recorded, and the diff is byte-identical to NUM's `git diff 75cd6be76b 31eed8497f` outside `execution/`.
- **The three files are test-only:**
  - `PP/src/retained_facade_tests.rs` (`#[cfg(test)] mod` in `lib.rs`);
  - `PP/src/retained_memory_law_tests.rs` (`#[cfg(test)] #[path]` in `retained_memory.rs`);
  - `PP/tests/common/b1_sq_inputs.rs` (integration-test helper).

  No production line changes.
- **Source equality** (`--pr 7f5f72912e --int 31eed8497f --main 953d8c9446`) passes checks 1, 2, 3 and 5: |S| = 33, 33 equal, B = `6c821d9ccf`. Check 4 reports `execution_files: 0`, as expected before the package is added (`E1/source_equality_7f5f72912e.{log,json}`).
- **Main's delta and the message.** Main `3d73db745e` → `953d8c9446` touches no path under P. The commit message adds one true line on the platform-exact tests.

## 2. My checks on the Mac (`E1/zz_rv125_glibc.rs`, `E1/glibc.json`)

**The setup:** a `git archive` copy of `7f5f72912e`, built registered (debug, 1.97.1, no RUSTFLAGS), with one job through `WT/tools/t3_cargo.sh`.

**The run, 10 of 10 pass** (`E1/test_results.txt`):
- my check;
- the five affected tests:
  - `cap_maximal_ring_is_the_trigonometric_ring`;
  - `b1_sq_inputs_are_i86s_and_the_committed_helpers`;
  - `b1_t4_w2b_and_w6_phys_r4_inputs_are_no_triggered_case_pins`;
  - `b1_sp_w_c2_fixtures_are_the_live_successors`;
  - `b1_sp_sf2_selected_not_first_and_two_selected_pins`;
- the W-C2 Direct pin and three other W-C2 tests.

`tests/retained_memory_challenge.rs` compiles (compile only; no RSS run).

| Check | Result |
|---|---|
| **Ring tables** | `CAP_MAXIMAL_RING` in `law_tests` and in `tests/common/b1_sq_inputs.rs` are identical. **All 64 coordinates equal this Mac's `10·cos t` and `10·sin t` bit for bit.** So the macOS input, and every hash pinned on it, is unchanged; the platform's trigonometry is now out of the input on every platform |
| **W-C2 dense, glibc variant** | **The variant is exactly a one-ulp change.** In the committed macOS fixture `source`, `1.6258317075882521e-12` occurs once (`/results/377/value`); `1.6258317075882523e-12` is its `next_up`. Replacing it and recomputing both hashes with the wire's own `domain_hash` (C1 §3) gives publication `35fa7aca…` and receipt `ca6a62a6…`. Those are the repair's values, and the result equals the repair's three-replacement document exactly. Control: the macOS fixture rehashes to its own `57624d75…` and `612e23ca…`. The sparse fixture does not contain the value |
| **(C, B, A) dense, glibc pair** | My Direct entry run reproduces the macOS pin (`7aeecbac…`, `c719bd8d…`). The value occurs once there (`/results/35/value`). The same one-ulp replacement and recomputation give exactly `CBA_DENSE_GLIBC` (`255785d2…`, `a320a5d3…`). So the pair is that value and nothing else |
| **The macOS path** | `GLIBC` is false here. `w_c2_on_this_platform` returns the committed fixture and the original receipt pin, and the (C, B, A) branch keeps `CBA_PINNED`. W-C2's `W_C2_PINNED`, its fixtures' `file_sha` checks, `AA2_PINNED` and `REVERSED_PINNED` are untouched |
| **No pin weakened** | Each platform gets exact bytes: the glibc document must equal the fixture with three replacements, each asserted to occur exactly once, and the glibc hash pairs are exact. The `file_sha` check still reads the committed fixture. The input pins (`W2B_INPUT_SHA256` and the I86 hashes) are unchanged and are now met on every platform |

## 3. The (A, A2) dense pin on glibc (ROOT's judgement item)

**My expectation: glibc reproduces the macOS pin, so no glibc pair should be needed.** The evidence:
- My Direct entry run on the Mac reproduces `AA2_PINNED` dense (`30001ccf…`, `f4075cdc…`).
- **The value that differs on glibc does not occur in it.**
- **Both of its cases' 171 rows equal W-C2's case A rows bit for bit,** by kind, entity and value bits. A2 is A's copy, on the same model and stiffness.
- Linux's W-C2 dense document differs from the Mac's only in case C's one value. So every hypot-formed value of case A is identical on glibc, and so, therefore, is every value of (A, A2).

**If CI does fail there,** it contradicts this reading. It should be read before any pin is added. A glibc pair, if one is needed, should be derived as these two were: from the observed Linux bytes, with the differing values named and both hashes recomputed from the macOS successor, so the pair is shown to be only those values.

At the time of writing, #1154's head was `7f5f72912e` and its numerical cargo suite was still running. I did not wait on it.

## 4. Finding

| ID | Class | Where | Evidence | Remedy |
|---|---|---|---|---|
| A1-N1 | NOTE | `PP/src/retained_memory_law_tests.rs`, `cap_maximal_ring_is_the_trigonometric_ring` | The doc says each coordinate is "within one ulp" of the platform's trigonometry. The check is `ulps ≤ 1 \|\| \|Δ\| ≤ 1e-14`, and its comment scopes the absolute clause to the near-zero entries (i = 8, 16, 24). But the clause applies to every entry, where it admits up to 45 ulps for coordinates ≥ 1 (about 1.95 has an ulp of 2.2e-16). This is a sanity check on data that is now exact bits. It pins nothing, so no pin is weakened | Optional, after CI shows glibc within one ulp: apply the absolute clause only where \|pinned\| < 1e-14 |

## 5. Host

- **Jobs:** every cargo job went through `WT/tools/t3_cargo.sh` (`--locked --offline`), one at a time.
- **Not run:** DEC-025, RSS or timing jobs.
- **No Git writes.**
- **Cleanup:** the copy `WT/rv125/` and the target `WT/targets/rv125-reg3` are deleted after this record.
- **Records:** placeholder paths only, no symlink and no folder named `build`.
