# I103 lane A (I-A for B2/B3): J1's package, B3a-A, B2-A and B3b-A

TASK (Type 2), I103, for ROOT (HELP_HUMAN, Agent 0); no delegation. 2026-10-08 UTC. Fresh instance.

**Brief:** `R/BRIEFS/B2_A_LANE.md` (`0af05623…`) with `R/BRIEFS/B1_COMMON.md` (`2d170307…`), both verified. Basis: I93 PLAN §1.2.2, §1.2.4, §1.2.7, §1.3, §1.4 with REVISION_01 §1.3–§1.4; B2-C (`R/I97/b2_c_01/`, CONTRACT with REVISION_01 and REVISION_02; all sums OK); B3-D (`R/I96/b3_d_01/`, DESIGN with REVISION_01; all sums OK); RR sections the brief names.

## Heads (`WT/b2-a`, `codex/piping-t3-b2-a-20261008`, from I4′ `8d46b045e2`; not pushed)

| Part | Commit | Files |
|---|---|---|
| 1. J1's package | `cd7bc9b363` | 20 (3 added statics) |
| 2. B3a-A | `3cc71f2e60` | PP `retained_memory.rs`, law tests |
| 2. B2-A | `a76bbd4477` | the same, plus the runner's admission test and one PP facade test (below) |
| 2. B3b-A (separate, provisional on B1's M) | `e96355ef8f` | PP `retained_memory.rs`, law tests |

The generated profile block is byte-identical at every head. FK, the base readers and the ordinary route are untouched. The host screen (`WT/tools/t3_host_screen.py`) over `8d46b045e2..e96355ef8f`: 22 files, 0 hits.

## Part 1: J1

- **Statics, each byte-equal to its selected file:** SCHEMA `abf3225c…` (B2-C's merged J1 text, which carries B3b's `SCHEMA_ENUM.diff`; `SCHEMA_J1.diff` applied to I4′'s SCHEMA reproduces it); PTABLE r2 `b2b4a54d…`; DEF-C r2 `3cebce55…`; XTABLE r1 `c4987e87…`; DEF-E r1 `71f63d39…`.
- **`REVIEWED_INPUTS` 14 → 17** (DEF-C, DEF-E, XTABLE appended, B3D-18), with `encode_reviewed_inputs`' and `build.rs`'s arrays. **The interim re-pin:** `REGISTERED_PROFILES[0].reviewed_inputs` re-derived from the 17 files in order (only SCHEMA, PTABLE and the three appended entries change). Identity, reader layouts, M, the profile, the caps, successor and corpus bytes: unchanged.
- **The two law tests at 17.** **PTABLE's cascade** `c74742ce…` → `b2b4a54d…`, constants only, in the 12 files.
- **Stated, mechanical differences from REVISION_01 §1.4's letter:**
  1. B2-C §11 as trimmed by its REVISION_01 N-8 (RV118: necessary): RS `g0`'s and TS `header`'s formation constant lists and PP `u1_constants_bound_to_in_tree_fixtures` gain `{DEF-C id, d3fde142…}` (literals).
  2. `reviewed_inputs_bind_the_lock_and_the_reader_statics` checks "each reviewed static is a reader `include_str!` input" over G4's 13 statics (`[1..14]`): RS does not package DEF-C, DEF-E or XTABLE until B2's and B3b's reader work (N-8). The three are bound by hash only until then.
  3. `CARRIER_PROFILE_ENUMS.diff` is not in J1: B3-D REVISION_01 §6 assigns both carrier files to lane T (B3b-T), and it is not a hash constant.
- **For RV-Q2:** `statics_j1.diff` (`git diff --binary 8d46b045e2 cd7bc9b363`, sha256 in SHA256SUMS).

**J1's acceptance (Registered build):** passed; no stop.
- The build is the registered one: `profile_in_build_record` asserts the pinned record (no skip line) and `the_registered_profile_is_the_only_permit_source` asserts `build_status() == Ok(0)` in that identity; the compiled reviewed-input text is the re-pin (`_run_records/j1_registered.log`).
- Every c = 1 and B1 multi-case pin test passes unchanged (for example `u1_milestone_successor_both_modes`, `u3g2_direct_entry_publishes_the_pinned_successor`, `u8_l0_isolated_node_publishes_pinned_successor`, `b1_sp_w_c2_direct_entry_publishes_the_pinned_successor`, `b1_sp_w_c2_fixtures_are_the_live_successors`, `b1_sp_multi_case_coexistence_pin`, `b1_sp_sf2_selected_not_first_and_two_selected_pins`), with the Direct-entry facade tests, both law tests, the three readers' suites and the carrier schema tests: every suite is test-by-test identical to I4′ (table below).

## Part 2: the admission (PP `retained_memory.rs` outside the generated block)

- **B3a-A:** D1.3 decided once by `namespace_branch`: L (0.1.0/0.2.0, no contract) or L3 (0.3.0, exactly `{1.0.0, legacy_pressure_v1}`). B3-D §4.1's refusal map (`PressureContract` for a contract outside its schema's branch, `SchemaVersion` otherwise). D1.5 and D1.7 unchanged on L3 (N-11's zero pressure load stays outside). The typed census reads the contract's two strings.
- **B2-A:** caps `COMBINATIONS` 2, `CASE_EQUIVALENTS` 3, `COMBINATION_TERMS` 3, `RANGE_OPERANDS` 3. D1.4 admits combinations on L and L3, with the new `FamilyFact::CombinationIds` (C-9). D1.9 gains six rows before `ControlBytes` (47 → 53): `Combinations`, `CaseEquivalents`, `CombinationTerms` (+ capacity), `RangeOperands` (+ capacity); `CombinationsCapacity` 0 → 2. Terms and operand ids are bounded over every combination of any basis (typed arrays before validation). The typed walk reads every combination string (id, label, basis, term cases, minuend, subtrahend, operands, mode, provenance; label added to N-10's list). The array facts are `CombinationFacts`, computed beside the report (`DomainFacts`), so the report's layout, a priced profile atom (`s(ThreadPacketOutput)`), is unchanged: the pinned-record test passes. G-C: `EnvelopeResults` (and capacity, text) ≤ C_eq·P_final and `RetainedErrorTextBytes` ≤ C_eq·(3m+1)·Text(err); G-B, T-3 (e), contract evidence and B-6 unchanged.
- **Out-of-domain oracles at C_eq + 1:** the runner's literal (C = 3 cases + 1 combination, refused at `CaseEquivalents`) and its PP tie test `b2_a_runner_oracle_literal_is_case_equivalents_plus_one` (replaces `b1_sa_runner_oracle_literal_is_load_cases_plus_one`). The C + 1 load-case oracles stay valid (z = 0).
- **B3b-A:** branch E (0.3.0, exactly `{2.0.0, exact_straight_pressure_v2}`; 0.4.0 out); D1.4's exact clause (no combination; ruling 4); D1.5's exact clause (`pressure_regions == Some([])` on every case). B3-D §4.2's law-test list, plus n05 and n06 on branch E.
- **Behaviour under the interim** (Direct entry, registered build; pinned by tests):
  - an admitted combination-bearing invocation publishes the exact ordinary bytes (`W1Fallback::Domain`: PP `w1_case_ids` still refuses combinations until B2-P);
  - m3x, n05 and n06 publish the exact ordinary bytes (`permitted_run` sends exact models to the ordinary route, `Domain`, until B3b-P);
  - **m3l is admitted and W1 runs to precommit, where RS refuses at G8 `RETAINED_PRECISION_INVOCATION_MISMATCH` (as I99 §5 found), so its publication is the ordinary rows plus one unavailable notice** until the readers' B3a (J5). The test accepts a successor or that G8 refusal.

## Suites against `b1` at I4′ (test by test; `_run_records/compare_*.json`)

| Suite | I4′ | J1 `cd7bc9b363` | B2-A head `a76bbd4477` | B3b-A head `e96355ef8f` |
|---|---|---|---|---|
| RE (all tests) | 196 ok | 196 ok, 0 changed | (no RE file changed after J1) | same |
| PY (17 files: readers, carriers, schemas, AnalysisRun, stress-neutral, consumers) | 2,168 passed, 17 skipped | identical | (no PY file changed) | same |
| TS (results, stress-neutral, result-export dirs; two service tests; archive) | 1,846 passed | identical | (no TS file changed) | same |
| PP `--lib` + `retained_precision_admission` + `s11f_site_test` | 591 ok, 1 failed, 11 ignored | identical | 0 changed; +9 new tests ok; tie test renamed | 0 changed; +11 new tests ok; tie test renamed |
| Runner (all tests) | 85 ok, 2 failed | identical | identical (re-based oracle passes) | identical |

The three failures are I4′'s own and unchanged: PP `s11g_tests::t13_committed_fallback_uz_is_byte_identical` (the known Mac failure), runner `load_reference_route_tests::load_reference_one_actual_solve_mints_bound_evidence_and_canonical_document_both_modes` and `cli_load_reference_one_both_modes_is_controlled_and_equals_the_library_route` (load-reference "actual producer changed" on this host). The B3a-A head alone: PP 0 changed, +2 tests ok.

## Mutants (`_run_records/mutants.json`; one exact edit each, PP `--lib` filtered to the killing tests)

**23 of 24 killed; the one survivor is equivalent by value.**

| Mutant | Check | Killed by |
|---|---|---|
| B2A-01 | combination ids disjoint (C-9) | `b2_a_combination_ids_are_disjoint_from_load_case_ids` |
| B2A-02 | z <= 2: the cap | `b2_a_d1_admits_case_equivalents_up_to_three` |
| B2A-03 | z <= 2: combination counting | `b2_a_d1_admits_case_equivalents_up_to_three` |
| B2A-04 | C_eq = c + z: combination counting (z dropped) | `b2_a_runner_oracle_literal_is_case_equivalents_plus_one`, `b2_a_d1_admits_case_equivalents_up_to_three` |
| B2A-05 | C_eq <= 3: the bound | `b2_a_runner_oracle_literal_is_case_equivalents_plus_one`, `b2_a_d1_admits_case_equivalents_up_to_three` |
| B2A-06 | h <= 3: the term bound | `b2_a_terms_and_range_operands_are_at_most_three` |
| B2A-07 | h: term counting over every combination | `b2_a_terms_and_range_operands_are_at_most_three` |
| B2A-08 | h: the typed terms capacity | `b2_a_terms_and_range_operands_are_at_most_three` |
| B2A-09 | range operands <= 3: the bound | `b2_a_terms_and_range_operands_are_at_most_three` |
| B2A-10 | range operands: the typed capacity | `b2_a_terms_and_range_operands_are_at_most_three` |
| B2A-11 | combinations typed capacity <= 2 | `typed_capacity_and_units_rows_read_the_actual_owners` |
| B2A-12 | the typed census reads combination strings | `b2_a_typed_census_reads_every_combination_string` |
| B2A-13 | G-C: EnvelopeResults <= C_eq * P_final (vs c * P_final; equivalent while C_eq's cap = C's) | **survives (equivalent)** |
| B3A-01 | L3: the contract version | `b3a_direct_entry_oracles`, `b3a_d1_3_admits_the_legacy_pressure_contract_on_0_3_0` |
| B3A-02 | L3: the contract mode | `b3a_d1_3_admits_the_legacy_pressure_contract_on_0_3_0` |
| B3A-03 | L3: the schema 0.3.0 | `b3a_d1_3_admits_the_legacy_pressure_contract_on_0_3_0` |
| B3A-04 | D1.3 refusal map: a contract outside its branch is PressureContract | `every_family_clause_refuses_with_its_fact`, `b3a_direct_entry_oracles`, `b3a_d1_3_admits_the_legacy_pressure_contract_on_0_3_0` |
| B3A-05 | the typed census reads the contract strings | `b3a_d1_3_admits_the_legacy_pressure_contract_on_0_3_0` |
| B3B-01 | exact D1.4: no combination (ruling 4) | `b3b_d1_admits_the_exact_route_with_empty_regions` |
| B3B-02 | exact D1.5: regions absent refuse | `b3b_d1_admits_the_exact_route_with_empty_regions` |
| B3B-03 | exact D1.5: non-empty regions refuse | `b3b_d1_admits_the_exact_route_with_empty_regions` |
| B3B-04 | D1.5 on L and L3: Some([]) refuses | `every_family_clause_refuses_with_its_fact`, `b3a_d1_3_admits_the_legacy_pressure_contract_on_0_3_0` |
| B3B-05 | E: the contract version | `b3b_d1_admits_the_exact_route_with_empty_regions` |
| B3B-06 | E: 0.4.0 stays out | `b3b_d1_admits_the_exact_route_with_empty_regions` |

- **B2A-13** replaces C_eq by C in G-C's `EnvelopeResults` bound. Both caps are 3, so no input can tell them apart; `b2_a_g_c_bounds_are_per_case_equivalent` states the identity (`CASE_EQUIVALENTS == LOAD_CASES`). It is not a new check: G-C's values are B1's.
- Every mutant compiled; each killed run failed only in the named tests.

## For ROOT

1. **A file outside lane A's list:** B2-A re-bases one oracle in PP `retained_facade_tests.rs` (lane P's): `u3g2_direct_entry_no_w1_refusals_keep_exact_bytes`'s "combination" input becomes C_eq + 1 (one case, three combinations; clause D1.9), because one combination is now inside D1. 7 lines, test-only; lane P should rebase onto it.
2. **The B3a interim notice** (Part 2 above): m3l on the Direct entry now publishes a notice instead of plain bytes until J5. Dev/test only, no product caller.
3. **B3b-A is provisional on B1's M** (separate commit); about 152 MB under-priced on S3's profile, inside 0.9 M (B3D-17).
4. **Not done here:** CARRIER_PROFILE_ENUMS (lane T); RS packaging DEF-C/DEF-E/XTABLE (readers' lanes). The `pressure_regions` capacity on branch E is not a cap row (B3-D's predicate is emptiness; parsed input has capacity 0).
5. **A disclosed repair:** B2-A was first committed as `78c7cbba9b`; its check (`next2.sh`, run tag `b2a`; logs in scratch) failed two of my new tests because their combinations lacked the provenance the ordinary validation requires (the inputs were blocked, not the admission). I added the provenance and amended to `a76bbd4477` before B3b-A; nothing was pushed.
6. **Records:** no symlink, no `build` folder, placeholder paths only. Raw logs stay in `WT/scratch/i103_b2_a/runs/`. Waits were sequential foreground loops or one monitor per job; no other job was signalled.
