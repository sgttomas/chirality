# RV122 (RV-Q2), round 1: lane A, J1's statics package and the B3a, B2 and B3b admission

TASK (Type 2), RV122, holding RV-Q2 for B2/B3, for ROOT (HELP_HUMAN, Agent 0), the return path. I am a fresh instance, I wrote none of this change, and I delegated nothing. 2026-10-08 UTC.

**Brief:** `R/BRIEFS/RV122_RVQ2_ROUND1.md` (`bda53be4…2a47ea5`, verified before reading). I read NUM's `AGENTS.md` and `agents/AGENT_TASK.md` first. The basis is what the brief names: lane A's brief; I93 PLAN §1.2–§1.4 and REVISION_01 §1.3–§1.4; B2-C (CONTRACT, REVISION_01, REVISION_02, with every sum OK); B3-D (DESIGN and REVISION_01, with every sum OK); and the RR rulings the brief lists. I read I103's `RETURN.md` after forming my own view of J1 and the expressions.

**Candidate:** `WT/b2-a`, branch `codex/piping-t3-b2-a-20261008`, head `e96355ef8f`, which is also origin's head. It sits over I4′ `8d46b045e2`. The four commits are J1 `cd7bc9b363`, B3a-A `3cc71f2e60`, B2-A `a76bbd4477` and B3b-A `e96355ef8f`.

**Method:**
- **Copies:** `git archive` copies of P (without `execution/`) at all five revisions, in `WT/scratch/rv122_rvq2/`. Probes and mutants ran only in further copies.
- **Hosts and jobs:** every cargo went through `WT/tools/t3_cargo.sh --locked --offline`, and pytest and vitest through `t3_slot.sh`, one heavy job at a time. vitest ran in an archive, with `node_modules` linked after a `cmp` of the lock and the eight wasm assets copied.
- **Restrictions kept:** no Git write, no DEC-025, no install. Paths below are placeholders (WT, NUM, R, T, P, PP).
- **A slip of mine, disclosed and repaired.** My first head and `a76bbd4477` PP and runner runs reused base's target directory. `git archive` gives source files the commit time as their mtime, so cargo treated base's `build.rs` output as fresh. Those runs therefore compiled base's reviewed-input digests and were Stale, and I discarded them. I re-ran them in fresh per-tree targets. All results below come from Registered builds: `the_registered_profile_is_the_only_permit_source` and `reviewed_inputs_bind…` pass, and probe C prints `build_status() = Ok(0)`. The mutant copy (made by `cp -R`, so fresh mtimes) built Registered, as its unmutated-equivalent baseline shows (585 passed, only `t13` failing).

## Verdict

**PASS: 0 BLOCKING, 2 SHOULD-FIX, 3 NOTE.** J1 is complete and mechanical. I found no bound that admits more than B2-C's or B3-D's text. Nothing priced changes. Every pin is unchanged, and every suite matches I4′ test by test.

| ID | Sev. | Finding | Required change |
|---|---|---|---|
| **SF-1** | SHOULD-FIX (confirmed) | **m3l's interim outcome is not pinned.** `b3a_direct_entry_oracles` accepts `Some(Ok(_))`, which would let a published successor pass, and on G8 compares only `results`. Probe A shows the actual Direct publication in both modes is exactly `Precommit{G8, RETAINED_PRECISION_INVOCATION_MISMATCH}` with bytes `== with_notice(plain, "case", None)` (one notice: 68,614 / 69,730 B against plain 68,295 / 69,411 B). B1 pins precommit fallbacks this way, in `u3g2_direct_entry_w1_fallbacks_append_one_notice`. | I103: pin that cause and `with_notice`'s bytes (through `into_publication`), and drop the `Ok` arm. RR has ruled it a test repair. |
| **SF-2** | SHOULD-FIX (confirmed; ruled) | **Branch E admits an unread typed owner.** `pressure_regions: Some(vec)` with length 0 passes D1.5-exact whatever its capacity, and no D1.9 row reads it. RESIDUALS T03's rule is to read actual capacities, not trust construction. Probe B: E with `Vec::with_capacity(65,536)` gives `domain = None`; the control (empty `sections` with capacity 1) refuses with `SectionsCapacity`. It is unreachable from today's Value entries, which parse it with capacity 0. I103 disclosed it. | ROOT ruled it: the exact D1.5 clause also requires `capacity() == 0`, as a B3b-A repair. Probe B is the witness for its test. |
| N-1 | NOTE | The doc comment on `COMPILED_REVIEWED_INPUTS` (`retained_memory.rs`) still says "the precommit reader's 13 `include_str!` inputs". There are now 17 inputs, 13 of them the reader's. | Optional wording fix. |
| N-2 | NOTE | `reviewed_inputs_bind_the_lock_and_the_reader_statics` checks `[1..14]`. That scope is correct now, but it must return to `[1..]` when RS packages DEF-C, DEF-E and XTABLE. | Readers' lanes (B2/B3b RS work). |
| N-3 | NOTE | Lane P's facade comments still read "a combination: outside D1.4": `retained_w1`'s domain-re-check test and the `w1_case_ids` test. They now test only W1's re-check, which B2-P changes. | Lane P (I105) at B2-P, as ruled. |

## Evidence, by brief item

1. **J1 is complete and mechanical.** Evidence: `statics_equal.out.txt`, `repin_check.*`, `def_h.*`, `hash_cascade.out.txt`, `generated_block.out.txt`.
   - **Statics:** all five are byte-equal, at J1 and at the head, to their selected files: SCHEMA `abf3225c` (B2-C statics), PTABLE r2 `b2b4a54d`, DEF-C r2 `3cebce55`, DEF-E r1 `71f63d39`, XTABLE r1 `c4987e87`.
   - **Hashes:** my own canonical-JSON hash gives DEF-O `a7ed7ca0` (the control), DEF-C `d3fde142` and DEF-E `5a3bac43`, equal to PTABLE's and XTABLE's lists.
   - **Schema:** `definition_id` is ProductAttempt [ordinary, exact], CombinationAttempt DEF-C and OperandPreparation DEF-O, as C-3 and N-12 require.
   - **Reviewed inputs:** `REVIEWED_INPUTS` is 17, appended DEF-C, DEF-E, XTABLE (B3D-18), and `build.rs`'s and `encode_reviewed_inputs`' arrays are 17. My re-derivation of `REGISTERED_PROFILES[0].reviewed_inputs` from the files equals the pin at base (14), J1 and head (17).
   - **Nothing else re-pinned:** identity, `reader_layouts`, `threshold_bytes` 4,026,531,840 and the cap constants are unchanged; the caps only gain the four new ones.
   - **Cascade:** PTABLE's old hash is in exactly 12 files at base and in none at head. The new hash is in the same 12 files, and SCHEMA's old hash is gone. The edits are constants only, apart from B2-C §11's three list edits.
   - **The return's diff:** `statics_j1.diff` reproduces (`3934606c`).
   - **I103's three stated differences: accepted.**
     - B2-C §11, as trimmed by N-8, is what RV118 ruled necessary.
     - The `[1..14]` scope is required until RS packages the new statics (N-2).
     - The carrier enums are lane T's under B3-D REVISION_01 §6, and REVISION_01 §1.4's J1 list does not name them.
2. **The expressions match the texts.**
   - **D1.3:** L is `0.1.0|0.2.0` with no contract. L3 is `0.3.0` with exactly `{1.0.0, legacy_pressure_v1}`. E is `0.3.0` with exactly `{2.0.0, exact_straight_pressure_v2}`. Otherwise a known schema refuses with `PressureContract` and any other with `SchemaVersion`; `PressureContractInput` denies unknown fields. The shared namespace conditions are kept.
   - **D1.4 (B2-C §9):**
     - C-9 is a new `FamilyFact`.
     - The exact clause refuses any combination first, under B3-S ruling 4.
     - Six rows sit before `ControlBytes` (47 → 53): z ≤ 2, C_eq = c + z ≤ 3, terms ≤ 3 and range operands ≤ 3 with their capacities, maxima over every basis. That is stricter than "mechanics" and "range" only, and B2-C §9 gives the reason.
     - `CombinationsCapacity` is 2.
     - The census reads all 9 combination strings and both contract strings.
   - **D1.5:** L and L3 keep `None`; E requires `Some([])`, and see SF-2.
   - **G-C:** `ceq·P_final` (with its capacity and text) and `ceq·(3m+1)·ERR`. Contract evidence stays per case; G-B (`late`) and T-3 (e) are unchanged.
   - **Intermediate commits:** at B3a-A and B2-A the exact contract still refuses with `PressureContract`, and each commit stands alone.
3. **Nothing priced changes.**
   - The generated profile block is `a3c62721…` at all five revisions.
   - With output, `profile_in_build_record` prints 246 atom and phase lines, identical at base and head (no skip line). `s(ThreadPacketOutput)` is 1,704 B in-build in both, and probe C shows report = 928 B and `READER_LAYOUTS` unchanged.
   - `CombinationFacts` is computed in `admit` and passed through `DomainFacts`, never stored in the report.
4. **Byte identity holds.**
   - Every c = 1 and B1 multi-case pin passes in the Registered head build, among them `u1_milestone_successor_both_modes`, `b1_sp_w_c2_direct_entry_publishes_the_pinned_successor` and `b1_sp_multi_case_coexistence_pin`.
   - Admitted combinations, m3x, n05 and n06 publish exact ordinary bytes (their tests pass). m3l's notice is SF-1.
5. **The oracles at C_eq + 1:**
   - The runner literal is 3 cases plus 1 combination, refused at `CaseEquivalents`.
   - Its tie test asserts `CASE_EQUIVALENTS + 1 = 4` and `LOAD_CASES = 3`.
   - The facade oracle is c = 1, z = 3, refused under clause Caps (the z row first).
   - The law tests cover h = 4 and 4 operands.
6. **Mutants (`rv122_mutants.json`): 39 of 40 killed.** Each is one exact edit, run against the full PP `--lib` suite in a Registered build.
   - Every killed run fails only named lane-A tests, besides `t13`.
   - The survivor, RQ-22 (`ceq` read as `LOAD_CASES`), is equivalent while both caps are 3.
   - **I103's B2A-13 equivalence claim is confirmed:** same const value, and the G-C test asserts the caps equal.
7. **Suites against I4′, test by test** (`compare_*_vs_base.json`, `py_ts_summaries.txt`):

   | Suite | I4′ | head `e96355ef8f` | B2-A `a76bbd4477` |
   |---|---|---|---|
   | PP lib and all 22 integration tests | 738 ok, 1 failed, 11 ignored | 0 changed; +11 new ok; tie test renamed | 0 changed; +9 new ok; tie test renamed |
   | Runner (all) | 85 ok, 2 failed | identical | identical |
   | RE (all) | 196 ok | identical | (no RE change after J1) |
   | PY (17 files) | 2,168 passed, 17 skipped | identical | (no PY change) |
   | TS (results, stress-neutral, result-export; two service tests) | 1,846 passed | identical | (no TS change) |

   The three failures are I4′'s own, in both runs: PP `s11g_tests::t13_committed_fallback_uz_is_byte_identical`, and the runner's two load-reference tests.

## For ROOT

- SF-1 is confirmed; repair as ruled. SF-2 is confirmed, and probe B is its witness; repair in B3b-A as ruled.
- I confirm both repairs from my scratch, which I keep at `WT/scratch/rv122_rvq2/`.
- Lane P's later change to `b3b_direct_entry_keeps_the_exact_ordinary_bytes` on `b2` is outside this candidate. I reviewed lane A at `e96355ef8f`.
- Nothing needs the owner.

## Evidence files

`evidence/`:
- scripts, all with placeholder paths: `run_suites.sh` (now per-tree targets; base ran first in the shared ones), `run_probes.sh`, `run_mutants.sh`, `chain.sh` (the first chain, whose head and B2-A PP/runner logs were the discarded Stale ones), `mutants_def.py`, `mutant_apply.py`, `compare.py`, `repin_check.py`, `def_h.py`;
- outputs: the `meta_*` files and `chain.txt`, the comparisons, `rv122_mutants.json`, `probes.out.txt`, and the two appended probe sources.

Raw logs stay in scratch.
