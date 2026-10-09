# I107 round 3: Pass B on the U3 PR's code commit (u3_passb_01)

TASK (Type 2), I107, for WORKING_ITEMS for T3 (Agent 1). Dated 2026-10-09 UTC; no delegation.

**The brief:** `R/BRIEFS/U3_SB.md` (`3e7dcd23…0260`, verified), under B1_COMMON and my earlier briefs. **Read:** I110's `pressure_retire_06` RETURN; RV127's `u3_stage1_01` REVIEW and both addenda (the 800 B atoms); my round 2 record and RV124's confirmation of it (C-N1).

## The candidate

**`8a12de28db5ede85d3df09d5307e795ff39e4373`** (PR #1168) is one commit on main `ba500defa4` (B1 + PR-N as merged).
- **Files:** 133, all under P: 121 modified, 6 added, 6 deleted. No `Cargo.lock`, no `Cargo.toml` and not `retained_memory.rs`.
- **Against NUM's head** (`3743b79291`), P without `execution/` is equal except for three fixtures. NUM deleted them in `180bf9b26d`; the candidate keeps them (note 1).
- **Method:** I took an archive of the candidate.
  - **Compared with main:** the entry, the delta, PP and the runner.
  - **Compared with SQ's records** (B1's Pass A, which rounds 1 and 2 matched): TEXT, the forms, the non-candidates, the controls, the witnesses and the challenge.

## Verdict: `DELTAS TO READ`, exit 6. No stop.

`VERDICT DELTAS TO READ exit=6 basis=8a12de28db5ede85d3df09d5307e795ff39e4373 tag=u3 passA=SQ(57c92a7b33..69002bc862+registration) delta_old=main(ba500defa4) gates=tree:0 entry:0 entry_code:0 m:0 law:0 law_sq:6 statics:0 premise57:0 linemap:0 premise:0 text_run:0 delta:0 text:6 text_n5:0 forms:6 forms_g5:6 forms_u3:0 forms_g5_u3:0 noncand_run:0 noncand_sq:6 noncand_u3:0 controls_run:0 controls:0 controls_sq:6 controls_u3:0 pp_outcomes:6 runner_outcomes:6 witnesses:0 challenge:6`

The six equality gates that read 6 compare U3 with SQ's records or with main for equality. A reading attributes each one, and every reading is 0:
- **In the pass:** `forms_u3`, `noncand_u3` and `controls_u3`.
- **After the pass:** `law_u3`, `outcomes_u3` (PP and the runner) and `challenge_u3`. Tools: `tools/u3_checks.py` and `tools/post_u3.py`; outputs: `runs/u3/post_u3_*.json`.

**TEXT's 6 is one increase to read:** T2's limitation text, +116 B requested.

| Brief item | Result |
|---|---|
| 1. Entry and registration | **Unchanged.**<br>- `REGISTERED_PROFILES` is byte-equal to main's: `threshold_bytes` 11,274,289,152 and 1 profile. Its code equals the applied registration's.<br>- **All 14 reviewed inputs** hash to the entry's pins, and none is among the 133 files. PP's `Cargo.lock` is one of them (`prep/identity_u3.txt`).<br>- law: 55 passed, 0 failed. The compiled identity, the inputs and the layouts are equal. |
| 2. TEXT, forms, the blocks, M | **Every change is attributed** (below).<br>- **In-build:** every phase in both modes is **exactly 800 B lower**: 9 × 32 B (`(&str, StressRecoveryResult)` 192 → 160) plus 64 × 8 B (`(String, DerivedSection)` 88 → 80).<br>- **The committed GENERATED PROFILE blocks are unchanged.** Regenerated from U3's trees, they would differ only in four TEXT constants, each lower. So the committed blocks over-price U3's code.<br>- **M is unchanged; the bound does not worsen.** No stop. |
| 3. The delta | 0: all 327 rows are classified, and all 129 that need an entry have one, with 0 refused (below). |
| 4. Loops and allocations | The added code's loops are linear in the model and are run once per solve. **On an admitted model there is no allocation**; on refusal, one diagnostic per refused joint (below). |
| 5. Outcomes, non-candidates, controls | **PP and the runner change only by the tests the commit removes and adds:** PP −22 / +11, the runner −1 / +3. No outcome flips, and no failure on either side.<br>- **Non-candidates:** SQ's rows less the 2 on lines U3 deleted.<br>- **Controls:** 12 of 12, each equal to SQ's, with TAV offsets equal. |
| 6. Witnesses and the challenge | **Witnesses:** 40 of 40 pass with SQ's lines (gate 0).<br>- **Challenge:** all 27 product entries and the default pass, with the outcome, rows and bound name equal to SQ's.<br>- **bound_bytes:** exactly 800 lower everywhere.<br>- **Peaks:** none rose. Ordinary-route peaks are 512 or 32 B lower, and direct/successor peaks are equal.<br>- **The floor:** 4,161 = 4,060 + len(argv[0]) = 101, which is environmental, as in rounds 1 and 2. |

### The gates to read, each attributed

- **law_sq 6 → law_u3 0:** of the 276 `I65_G5_*` lines, 18 differ, all as stated in item 2:
  - 14 PHASE lines: requested and E_mov+R are exactly 800 lower, moving is unchanged;
  - 2 PROFILE lines: max_without_R and E_mov+R are 800 lower. Sparse is 9,800,676,166 → 9,800,675,366 and dense 9,859,807,510 → 9,859,806,710. fraction_of_M is still **0.8693 / 0.8745**;
  - 2 ATOM lines: the two atoms;
  - IDENTITY, REVIEWED_INPUTS, READER_LAYOUT, BUDGET and ESTIMATE_WEIGHT are equal.
- **text 6:** the one increase is PP `preview_formulation_basis` (`to_string`, mult 2): 155 → 184 B, requested 620 → 736, in each of the 4 variants. This is T2's text correction (delta W). Everything else is attributed to removals (below). text_n5 0.
- **forms / forms_g5 6 → forms_u3 / forms_g5_u3 0:** the regeneration differs from the committed block in exactly four constants, each lower. No form, expression or phase changes.
  - `TEXT_TAV_TEXT_MOVING` 6,236,994,628 → 5,789,308,259;
  - `TEXT_TAV_TEXT_REQUESTED` 6,234,394,666 → 5,786,708,902;
  - `TEXT_TEXT_DIAG_ENV` 175,409,684 → 174,361,824;
  - `TEXT_TEXT_DIAG_TOTAL` 271,493,888 → 270,446,028.
- **noncand_sq 6 → noncand_u3 0:**
  - SQ's 412 rows less 2 is 410, all equal with lines dropped. No row is new.
  - The 2 are `station` (int, mult 768) at SQ's `lib.rs:13183` and `:13198`: the pressure-hoop and pressure-longitudinal station rows. The line map pruned both lines as deleted with nothing in their place.
  - RV87's comparison is SQ's plus those 2 absent rows.
- **controls_sq 6 → controls_u3 0:**
  - Each control's outcome, completeness and finding equal SQ's. Each TAV offset from c0 equals SQ's (0, −370, −9,461,760 and −318,296,486).
  - The common shift is U3's TAV change, −447,685,764.
- **pp_outcomes 6 → 0:** 822 → 811 lines. The 22 only on main and the 11 only on the candidate are exactly the `#[test]` fns the commit removes and adds in PP, by source scan. PP has 732 passed, 0 failed, 79 ignored (main: 743 / 0 / 79).
- **runner_outcomes 6 → 0:** 87 → 89. Removed: `mechanics_whole_suite_is_25_cases_206_values…`. Added: its 24-case/192-value successor and the two CLI refusal tests. 89 / 0 (main: 87 / 0).
- **challenge 6 → challenge_u3 0:** as in item 6. The lower peaks are consistent with the 8 B `(String, DerivedSection)` entry times a power-of-two table (512 = 64 × 8, 32 = 4 × 8); I did not trace them further.

## The profile change, and its effect on G5, G6 and M

- **In-build** (the law test and `PINNED_RECORD`): −800 B per phase, in both modes. Both atoms sit in `O_base_dense` / `O_base_sparse` with coefficients 9 and 64, the 9 × 32 + 64 × 8 counts RV127 stated. `PINNED_RECORD` and the challenge's `W1_PHASE_BYTES` / `MAX_PHASE_BYTES` are each old − 800 (delta Q).
- **Static TEXT chain, regenerated (not committed):** E_mov+R, with assumed strides, falls by 308,249,794 B in every chain:
  - G5: sparse 9,588,398,067 → 9,280,148,273; dense 9,647,529,411 → 9,339,279,617;
  - G6 (N-5): sparse 9,588,404,355 → 9,280,154,561; dense 9,647,535,699 → 9,339,285,905.
  - D (41,769) and D_env (22,911) are unchanged; TEXT is complete.
- **TAV falls by 447,685,764 B.** It is the sum of four parts, found by row alignment against SQ's point:
  - **185,198,976: fewer calls.** The stress-recovery helpers (`checked_recovered`, `require_finite`, `require_positive`) and `append_{endpoint,station}_stress_result` lose the pressure components;
  - **2,699,904: rows in removed code** (`build_pressure_thrust_loads`, the pressure stress rows);
  - **−116: the T2 text.**
  - **259,787,000: −605 B per use of the static-literal measure, 2,173 → 1,568 B (note 2).**
- **M** is 11,274,289,152, unchanged. In the in-build record U3 sits 800 B lower than SQ's, so **the bound does not worsen**.

## The delta rows (`runs/u3/delta_inventory.json.gz`; main `ba500defa4` → `8a12de28db`)

**There are 133 files and 327 rows:** 109 not-d1, 91 item, 82 test, 34 live, 6 no-code, 4 qualification-test and 1 unreachable.
- **unreachable:** stress_recovery `lib.rs:293` `new`, which is not on the lexical D1 graph.
- **129 rows need an entry** (125 production, 4 qualification-test), and **all 129 have one.** The table is `delta_reviewed_u3.json` (`f08a881b…fd751`), built by `tools/mk_delta_reviewed_u3.py`, with 0 refused.
- **Fingerprints:** the delta tool computes them on this candidate, and no fingerprint is carried over, so RV124 C-N1 does not arise.

**Every production-class row is the retirement:**

| Kind | Rows | What it is, and the check |
|---|---|---|
| R | 83 | **A pure removal naming an identifier the commit retired.** It is retired from the file, from the enclosing fn, or as a local binding the fn lost (e.g. `pressure`). The rows are in stress_recovery 22, PP `lib.rs` 44, primitive_loads 4, curved_bend 5, retained_product 2, source_receipt 3 + 1, and source_recovery 2. |
| S | 21 | **A subtractive edit:** the token diff only deletes, and each deleted run names a retired identifier or is punctuation. The two literal arguments are `None` to `recover_section_stress` (its `pressure` parameter removed) and `false` to `open_formula_summary_mpa` (its `include_pressure_longitudinal` removed). |
| H | 2 | **H-1:** `axial + pressure_longitudinal` → `axial + 0.0`, at stress_recovery `lib.rs:906–908` and PP `lib.rs:11620–11622`. |
| A | 2 | **Removed arguments:** `false, false` for `append_{endpoint,station}_stress_results`'s removed `include_pressure` / `include_pressure_longitudinal` (rows.rs after `:489` and `:497`). |
| W | 10 | **Wording only:** string literals changed, with their placeholders unchanged. The rows are PP `lib.rs:1946` (T2), `:11990`, `:11997` and `:12030` (joint and bend basis texts, now "none_pressure_refused_outside_the_exact_straight_contract"); `pressure_runtime.rs:120`, `:137`, `:146` and `:222`; and `validation.rs:1159` and `:1350`. |
| F | 4 | **The refusals:**<br>[F1] `RETIRED_MODE` / `RETIRED_VERSION` (`pressure_runtime.rs:21–23`);<br>[F2] `PRESSURE_MODEL_REAUTHOR_REQUIRED` for exactly 1.0.0/legacy_pressure_v1 (`:140–144`);<br>[F3] the legacy-primitive refusal, widened from nonzero values to every value (`:220`);<br>[F4] G11's joint refusals (`preview_physics.rs:120–187`), which only push blocking diagnostics and `continue`. |
| T | 2 | **Test-only code:**<br>- the deleted `historical_pressure_reference.rs`, declared only as `#[cfg(test)] mod`;<br>- its `#[cfg(test)]` bypass statement in `refuse_unqualified_joint_elements` (`preview_physics.rs` after `:113`). |
| Z | 1 | **`component_pressure_thrust_load_count = 0`** (PP `lib.rs:4732–4733`). |
| Q | 4 | **The re-pin:** `retained_memory_law_tests.rs:1200–1205` (the doc comment and `PINNED_RECORD`) and the challenge's `:36` and `:39`. Every value is old − 800. |

**Premise P0, for S, H and Z:**
- **The refusal:** on every admitted model, no primitive load has category or dimension "pressure". [F3] refuses any value without the exact contract, and the existing `EXACT_PRESSURE_REQUIRES_REGION` refuses it with the contract.
- **Coverage:** `validate_profile` runs first on the one ordinary entry, and the source-receipt routes passed `&[]`.
- **Consequence:** `build_pressure_thrust_loads` returned nothing, `pressure_for_pipe` returned `None`, every removed summand was +0.0 and every removed branch was not taken.

## TEXT, attributed (`runs/u3/gate_text.json`, `gate_text_n5.json`; `tools/text_u3.py`)

- **Rows:** text_budget has 2,847 → 2,827 rows in each of the four variants. The rows are aligned per (file, kind, fn) in line order:
  - 2,662 equal, and 150 smaller (mult, bytes and req all ≤);
  - 5 positive-mult rows gone, all in removed code: `build_pressure_thrust_loads` (a deleted fn) and the four pressure rows of `append_{endpoint,station}_stress_results`. 28 zero-mult rows are gone;
  - 13 new rows, all in [F4]'s added code and all mult 0 / req 0;
  - 2 grown rows: T2's (above), and `append_expansion_joint_user_stiffness_results` 1,506 → 1,549 B at mult 0, which requests nothing.
- **Functions:** `function_multiplicity` drops 5 deleted fns; nothing else is lost or new.
- **The call graph** (SQ's, carried 57c92a7b33 → candidate by the line map). Against SQ it shows:
  - 19 nodes lost, every one a deleted fn: the 4 historical-scope fns, 8 pressure fns in PP `lib.rs`, the two stress_recovery `PressureBasis*::new` and `pressure_membrane`, and 4 curved_bend radial-pressure fns;
  - 1 re-keyed: stress_recovery `new`, whose header was edited (346 → 293);
  - +10 nodes, PR-N's norm (as in round 2);
  - 102 edges lost and 116 site loops lost, all in removed code or callers with removals;
  - 32 edges added: 29 are the norm's, and 3 are `refuse_unqualified_joint_elements` → name fan-outs to `is_empty`;
  - 46 site loops added: the norm's, [F4]'s, or 10 narrowed entries (fewer call sites, or a header window shifted by the edit);
  - 56 spans resized, all in fns that enclose a delta row of this pass, PR-N or round 1, except `rigid_body.rs` `assess_constrained_bodies`, which differs from SQ's basis only in comments (PR-N's head; RV124 C-N1);
  - the deepest call chain is still 40, and the cyclic components are equal as sets.
- **The loop log:** 3,348 → 3,322 entries. 43 are lost in removed code; 17 are added, all in `refuse_unqualified_joint_elements`.
- **Every other output is dominated, value by value:** producer caps are equal. The profile tree, g4 caps, ordinary caps, T25, composite text, text closure and summary are each ≤ SQ's, symbolic forms included, with no new atom.

## Item 4: loops and allocations in the new code (`item4/added_code_scan.json`)

The scan lists every added production line, outside test modules, with its loop and allocation constructs.

**G11's joint refusals** (`preview_physics.rs:120–187`, in `refuse_unqualified_joint_elements`):
- **When and how often:** the code runs once per solve, in validation and before the build, over the expansion joints that declare user flexibility (J).
- **Per joint:**
  - a 4-element array goes through `filter_map(…).collect::<Vec<&str>>()`. This allocates only when an axis is missing (the refusal path); an empty collect does not allocate;
  - `pipe_segments.iter().find` costs O(P), and `nodes.iter().any` costs O(N).
- **Total:** O(J·(P + N)) string comparisons. **There is no allocation for an admitted joint.**
- **On refusal:** one `refs` Vec (1–2 id clones) and two `format!` strings (the diagnostic id and the message, bounded by the joint, pipe and node ids and a fixed text), then `continue`. The solve then returns the blocked envelope. TEXT has these sites at mult 0.

**The pressure contract and primitives** ([F2], [F3]): one `problem()` call on refusal. [F3] keeps the existing loop over a case's primitives; there is no new loop.

**The Rust side of the panels:**
- **The operation applier** (`resolve_create_primitive_load`): a constant-time early refusal for `category == "pressure"`, which pushes one diagnostic (two strings and a one-element Vec) and returns. The other pressure branches are removed, and there is no loop.
- **src-tauri** `lib.rs`: the production change is the default fixture's name, one sample `model_ref` string and doc comments. `model_document_migration.rs` changes only a doc comment.
- **Other Rust in the commit:**
  - curved_bend's `Vec::with_capacity` is smaller;
  - the runner's production changes are removals;
  - the example `preview_result.rs` iterates a 2-entry constant table.
  - These are not D1. The TS panels are outside this item.

## For WORKING_ITEMS and the reviewers

1. **Three fixtures:**
   - `P/fixtures/product_preview/invented_mechanics_result.json` and `…_precision_1_{dense,sparse}.json` are deleted in NUM (`180bf9b26d`) and kept by the PR.
   - At the candidate, only docs and records name them (`SMOKE.md`, `DEMO_FIXTURES.md`, `PLAN_COMPLETION_LOG.md` and old sweep records). No code, test or fixture reads them.
   - So after merge, main carries 3 files that NUM does not. This is not a Pass B gate.
2. **The static-literal measure moves for a reason outside production code.**
   - **Where it sits:** TEXT's `composite_text.py` takes the longest `"…"` regex match in four source files, test modules included. The quote pairing misaligns in test code, so the measure is a spurious span: 2,173 B at main, 1,568 B at U3, both in PP `lib.rs`'s test module. U3's removal of test code is what moves it.
   - **Both values still bound the real literals.** A Rust-aware lexer (strings, raw strings, char literals and comments) finds the longest literal in those files to be 677 B at SQ's basis, at main and at U3.
   - **Its effect is half the TAV drop** (259,787,000 of 447,685,764). Without it, TAV and the chain still fall by the removal parts alone. The committed blocks keep SQ's values in any case.
   - The measure is I65's, carried over unchanged. This is a note on it, not a U3 defect.
3. **The line map.**
   - SQ's rows tool failed on the deleted `historical_pressure_reference.rs`. My copy (`tools/g7_linemap_crates_rows3.py`) reads a deleted file as empty and tags each unmapped key `deleted` or `replaced`.
   - `tools/prune_deleted.py` dropped the 5 rule keys that lay on lines U3 deleted with nothing in their place: PP `lib.rs:10833`, `:13079`, `:13094`, `:13183` and `:13198`, the id audit of the removed pressure rows. Nothing else was unmapped.
   - I65's delta tool also needed a one-line change for a deleted file (`tools/delta_inventory2_u3.py`; `tools/tools_diff_vs_round2.txt`).
4. **The W rows change published metadata** for bends and expansion joints with user stiffness: their basis text now says no joint or bend pressure thrust is generated.
   - These are the declared text corrections. I did not check which of I110's byte sets cover models with bends or user-stiffness joints.
   - None of them reaches the witnesses or the challenge, which equal SQ's apart from the −800 B and the lower peaks.

## Execution

- **Jobs:**
  - cargo: through `t3_cargo.sh` (`--locked --offline`), with targets under `WT/targets/i107-u3-u3*`;
  - the TEXT points, the sweep, the controls, every test binary and the challenge: through `t3_slot.sh`.
  - One chain of mine ran at a time, with one waiter (the chain itself). The rest was log watching.
- **Waiting:** the runs waited about two hours for another lane's exclusive job. I did not touch it.
- **The runs:**
  - `prep` and `prep2`, then `prep3`: Python-only dry runs. `prep` stopped at the delta, before the table existed;
  - `u3`: the full pass.
- **Not done:** no DEC-025, no RSS or timing measurement, no install and no Git write. `WT/u3-pr` was not touched.
- **Scratch:** `WT/scratch/i107_u3/`, kept for RV124.
- **Records:** placeholder paths only. The host screen (`_run_records/screen.txt`) and `SHA256SUMS` cover this folder.
