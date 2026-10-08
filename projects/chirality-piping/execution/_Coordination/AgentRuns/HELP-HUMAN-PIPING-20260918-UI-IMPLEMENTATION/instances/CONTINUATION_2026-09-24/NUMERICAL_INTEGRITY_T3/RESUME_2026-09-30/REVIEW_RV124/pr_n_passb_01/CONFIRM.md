# RV124 (RV-Q) confirms I107's Pass B on PR-N and its carry-over to the head

TASK (Type 2), RV124, for WORKING_ITEMS for T3 (Agent 1), which is the return path by the owner's decision of 2026-10-08 (RR "Owner decisions: …; T3 gains a WORKING_ITEMS manager"). No delegation. 2026-10-08 UTC.

**The request:** WORKING_ITEMS' two messages to RV124:
- confirm I107's Pass B on PR-N: the 25 entries, the two tool adaptations, and whether the correction loop needs a static bound;
- then read repair round 01's production delta and say whether Pass B carries over to the PR head.

**The candidate:** PR-N #1163 (`codex/piping-t3-correct-norm-20261008`), a correctly rounded norm in place of libm `hypot`.
- **Code commit:** `8dd64c1835`, from main `7eae707bb7` (B1 as merged).
- **Head:** `0c7490e1be`. It is `8dd64c1835` plus the package `dab19291a8`, repair round 01 `8ca80508b6` (I109, for RV126) and the repair's package `0c7490e1be`.

**The record:** `R/I107/pr_n_passb_01/RETURN.md`.
- RETURN.md sha256 `7cd20ba77ef6983b665d022b4d94b27226678f4b1dbd3c358bc032c23dada071`. SHA256SUMS: 79 of 79 OK.
- `delta_reviewed_pn.json` sha256 `bcf0ce2b6f535bdb1dee4d3ca56d041226ccb9a4aab457f74267b936daf9258b`.
- VERDICT: `DELTAS TO READ exit=6`. Every gate is 0 except `pp_outcomes:6`, `runner_outcomes:6` and `challenge:6` (`E/record_check.txt`).

**Placeholders:** `WT` (the T3 worktree root); `NUM` = `WT/numerics`; `R` = the T3 records folder `RESUME_2026-09-30`; `S` = `WT/scratch/rv124_rvq`; `E` = this folder's `evidence/`.

**Limits:**
- Git reads only, and no Git write.
- No cargo and no measurement. The only programs run were Python: I65's delta tool, and I107's Pass B driver with cargo skipped, retargeted to `S` (`E/tools/pn_pass_rv.diff`).
- I107's scratch was read only.

## Verdict: **CONFIRMED**, with 0 BLOCKING, 0 SHOULD-FIX and 3 NOTE. **Pass B carries over to `0c7490e1be`.**

### 1. The 25 entries (`E/entries_pn.out.txt`, `E/tools/entries_pn.py`, `E/delta_rerun.txt` A)

- **The inventory reproduces.** I re-ran I65's `delta_inventory2.py` with I107's inputs on main → `8dd64c1835`, and its output equals I107's `runs/pn/delta_inventory.json.gz` as a whole:
  - 21 files and 39 rows;
  - live 14, item 6, qualification-test 5, unreachable 4, no-code 2, test 2, not-d1 6;
  - 0 unreviewed.
- **Each entry is one real hunk.** Each of the 25 matches exactly one hunk of `git diff -U0` by I65's fingerprint, with that row's file and class. Its stored lines are that hunk's code lines.
- **C, call sites (14 entries at 13 sites).**
  - Each removed line calls `hypot` and each added line calls `norm2` or `norm3`.
  - The number of `hypot` calls equals Σ(arity − 1) over the norms.
  - With the `hypot`/`norm` names dropped, the identifier, literal and operator tokens are equal on both sides, so the operands are the same.
  - `final_case.rs`'s two entries were checked together. The only tokens left over are `let xy =` and the uses of `xy`, which is the dropped temporary.
- **D, declarations (5):** every added code line declares the module or imports `norm2`/`norm3`.
- **M, the module (1):** the hunk is the whole new file (295 lines). Its production part (lines 1–201) has no allocating token.
- **Q, qualification tests (5):** the ring check in `retained_memory_law_tests.rs`.
  - Before, every coordinate passed with `ulps ≤ 1 || |Δ| ≤ 1e-14`.
  - Now `|Δ| ≤ 1e-14` applies only to a nonzero |pinned| < 1e-14. Those are counted and must be exactly 3 (N8's x, N16's y, N24's x). Every other coordinate must be within 1 ulp.
  - This is a tightening, as I107 says.

**Every production-class row is the norm.** The 4 unreachable rows are `elastic_section.rs:106`, `traverse_region`'s two rows and the W-C2 fixture. They need no entry by the tool's design, and RV126 reviews them with the module and the call sites.

### 2. The tool adaptations

**(a) `g7_linemap_crates_rows.py`** (`E/linemap_resolutions.txt`)
- It differs from SQ's `g7_linemap_crates.py` in one rule. A short key `lib.rs:N` that several changed files make ambiguous resolves to the one chain-crate file with a row at line N in SQ's G5 TEXT run. If no file has such a row, it resolves to the one file with at least N lines. Anything else stays unmapped, which fails closed as before.
- The rule is sound because the rows are keyed at `57c92a7b33`, the old side of the map, so a resolution cannot be steered by the new code.
- **Result:** 18 resolutions, all to PP `lib.rs`. 12 are rule keys resolved by TEXT rows, and 6 are citation values (`lib.rs:13636`, `:13643`) resolved by length. 504 remapped and 0 unmapped.

**(b) `audit_controls_pn.py`** (`E/controls_rekey_check.txt`)
- Its body differs from SQ's `audit_controls_b1.py` in 4 lines, and each is a pure +2 re-key of a PP `lib.rs` site:
  - c3 and c7: 5773 → 5775;
  - c4: 1708 → 1710;
  - c8: 8976 → 8978.
- PR-N's PP `lib.rs` hunks are one 2-line insertion at :38 and five 1-for-1 replacements. So each site moves by +2, and each re-keyed line's text equals main's.
- **Controls: 12 of 12,** equal to SQ's with line numbers dropped.

### 3. The suites, the witnesses and the challenge (`E/outcomes_check.txt`, `E/record_check.txt`)

- **PP:** 822 = 822 lines, with one change: `s11g_tests::t13_committed_fallback_uz_is_byte_identical` goes from FAILED on main to ok.
- **Runner:** 87 = 87 lines, with two changes: the `load_reference` library-route and CLI tests go from FAILED to ok.
- No test goes from ok to FAILED.
- **Witnesses:** 40 of 40 equal SQ's lines.
- **Challenge:** one difference, `process_floor` at 4,161 against SQ's 4,162. That count is 4,060 + len(argv[0]), and I107's binary path is 101 bytes. **It is environmental,** as in round 1, where my own point printed 4,160 at a 100-byte path.

### 4. The correction loop at `correct_norm.rs:85`: **I agree that no static bound is needed for Pass B**

- **Pass B checks heap and TEXT.** The loop uses only scalars and the stack arrays `[f64; 6]` and `[f64; 10]`. Its frame is fixed, and it allocates and formats nothing.
- **TEXT is unchanged.** At the norm's call sites, TEXT's rows, TAV and D equal SQ's (`text:0`, `text_n5:0`), and the 29 added site loops are attributed to the norm.
- **So the iteration count changes time only,** not any bound that Pass B prices.
- **Termination is a correctness property, so it is RV126's to rule.** My reading of the loop:
  - Each pass moves `r` one ulp, always in the same direction.
  - After a move up, the new "below" midpoint is the old "above" midpoint, including at a power of two, where `down` is `up * 0.5`. Its tie rule is the complement of the old one: `sticky`, and the parity flips. So it cannot move back down. The same holds for a move down.
  - The double-double candidate is within about 1 ulp of the result, which agrees with I107's measured maximum of 2 passes.
- **A static cap would be hardening** for I109 or RV126 to weigh, not a Pass B condition (C-N3).

### 5. Carry-over to the head `0c7490e1be` (`E/head_carry.txt`, `E/delta_rerun.txt`, `E/dryrun_head_0c.txt`)

**The production delta from `8dd64c1835` to `0c7490e1be` is comment-only and line-neutral.**
- The two package commits change only records under `execution/`.
- The repair changes 7 lines, each a `//` comment on both sides. With I65's `code_of`, the code-differing lines are []:
  - PP `lib.rs:38`;
  - FK `correct_norm.rs:6–10`;
  - FK `rigid_body.rs:465–466` and `:542–543`.
- Line counts are unchanged: 24,516, 295 and 1,409 (`wc -l`; `head_carry.txt` counts split fields, one more each).

**The test changes:**
- PP `tests/preview_physics_runtime.rs`: a `//!` header only; 0 code lines, and the same 26 tests.
- FK `tests/retained_k4/product_final_case_tests.rs`: exact expected constants in one test. That is FK's suite, outside Pass B's PP and runner outcome gates.

**No source-text guard sees the new comments.**
- PP's `retained_facade_tests.rs` and `tests/retained_precision_admission.rs` slice fn bodies or count named tokens. None of those tokens is in the new `lib.rs:38` comment, and line 38 comes before every sliced fn.
- `s11f_site_test.rs` and FK's `k5_constrained_bodies.rs` lex comments out.

**Dry run at the head.** I ran I107's `pn_pass.sh` with `I107_SKIP_CARGO=1` on `0c7490e1be` and compared it with I107's run on `8dd64c1835`.
- These gates are 0: tree, entry, entry_code, m, statics, premise57, linemap, premise, text_run, delta (with C-N1's two refreshed fingerprints), text_n5, forms, forms_g5, noncand and controls 12/12 (= SQ's).
- **Every output is byte-equal except three:**
  - `linemap.out.json`: only the revision, and rigid_body's hunk count 3 → 5. Remapped, unmapped and the resolutions are equal.
  - `g5/edges.json` and `n5/edges.json`: the edges and site loops are equal. Only character spans move, and one is resized (C-N2).
- All 42 other files of each TEXT point are equal, including TEXT's rows, TAV, D, the profile and FORMS.

**The cargo gates were not re-run.** These are the law gate, the PP and runner outcomes, the witnesses and the challenge. They carry over because:
- the production code is token-identical, since doc comments do not change codegen;
- the only PP test change is a doc header;
- the floor depends only on argv[0].

## Findings

| ID | Class | Finding | Disposition |
|---|---|---|---|
| C-N1 | NOTE | On the head, I107's table stops the delta gate (exit 5) with 2 unreviewed hunks: PP `lib.rs:38–39` (D) and `correct_norm.rs:1–295` (M). I65's fingerprint hashes comment lines, and the repair edited comments inside both reviewed hunks. Their code is unchanged. With those two fingerprints refreshed (`E/delta_reviewed_carry_0c.json.gz`, scratch only: `e569f6b5…` → `c95c80bb…` and `7f7bdf7e…` → `8f93c7e7…`), the delta passes: 22 files, 42 rows, 0 unreviewed. The 3 new rows are 2 no-code (rigid_body's comments) and 1 not-d1 (the FK K4 test). | No change is needed for this carry-over. If Pass B is re-run mechanically at the head, refresh these two fingerprints in the table first. |
| C-N2 | NOTE | At the head, the G5 text gate reports one resized span, `rigid_body.rs:480:assess_constrained_bodies` (`text:6`). Its span grows by the 29 characters that the `:542–543` comment gained. `text_pn.py` measures spans in source characters and allows a resize only where a norm call site is enclosed. The edges, site loops, TEXT rows, TAV and D are equal. | I read it: it is a comment, not a TEXT change. |
| C-N3 | NOTE | The correction loop (`correct_norm.rs:85`) has no static bound in the code. I agree that Pass B needs none: the loop has no heap, no text and a fixed frame, and TEXT is unchanged. On my reading it moves monotonically, and I107 measured at most 2 passes. | Termination is for RV126; a cap would be optional hardening. |

## Evidence (`E/`)

- **I107's record:** `record_check.txt`.
- **Entries and inventory:** `entries_pn.out.txt` and `delta_rerun.txt`.
- **Tool adaptations:** `linemap_resolutions.txt` and `controls_rekey_check.txt`.
- **Suites:** `outcomes_check.txt`.
- **Carry-over:** `head_carry.txt`, `dryrun_head_0c.txt`, `gate_text_head_0c.json`, `pass_head_0c.log.gz` and `delta_reviewed_carry_0c.json.gz`.
- **Tools:**
  - `tools/entries_pn.py` (the entry checks);
  - `tools/delta_rep.sh` (the delta re-runs);
  - `tools/pn_pass_rv.diff` (I107's driver retargeted to `S`: outputs, TMPDIR, the table as an argument, and no deletion).
