# I105 lane P (I-P for B2/B3): Part 1, B3b-P (the exact route), and a stop before Part 2

TASK (Type 2), I105, lane P's implementer, for ROOT (HELP_HUMAN, Agent 0); no delegation. 2026-10-08 UTC. Fresh instance.

**Brief:** `R/BRIEFS/B2_P_LANE.md` (`525e5cd8…`) with `R/BRIEFS/B1_COMMON.md` (`2d170307…`), both verified. Basis read (sums verified against each folder's SHA256SUMS): I93 PLAN (`e1147dbd…`) §1.2.4–§1.2.8, §1.4, §6 with REVISION_01 (`63abb73f…`); B3-D `R/I96/b3_d_01/` DESIGN (`ad7942f6…`) with REVISION_01 (`6f5b1a6d…`); I99's PROBE; I85's RETURN; I102's and I103's RETURNs; RR "RV116 (RV-D) accepts B3-D …", "RV116 confirms B3-D's revision 01; …", "RV115's addendum accepts B3-K …", "I99's B3-W verified; …", "Lane A returned; `b2` built …".

## Heads

| Part | Commits (`WT/b2`, `codex/piping-t3-b2-20261008`, over `e67c364680`; not pushed) |
|---|---|
| 1. B3b-P | `8d3419b542` (producer, pins, fixtures), `cc24cd955c` (tests), then **`22e9d00062`** (tests: two mutant kills) |
| 2. B2-P | **not started** (the stop below) |

## The stop (brief: "if you need a change outside your files")

B3b-P changes the behaviour that lane A's interim oracle pins. `PP/retained_memory_law_tests.rs` `b3b_direct_entry_keeps_the_exact_ordinary_bytes` asserts `W1Fallback::Domain` for m3x, n05 and n06 (its doc: "no producer change yet"). After B3b-P the exact route runs W1: n05 and n06 are `Coexistence` with the same exact bytes, and m3x reaches precommit, where today's RS refuses `physics-retained-1` at G0, so it publishes the ordinary bytes plus one notice. **In the registered build that one lane-A test now fails; nothing else changed.**

- **Proposed, not applied:** `_run_records/proposal/lane_a_b3b_direct_oracle.diff` (that test only: coexistence pins keep exact bytes; m3x accepts the successor, or today's G0 refusal with one notice).
- **Checked:** applied in a scratch archive of `cc24cd955c` (`22e9d00062` changes only my tests), lane A's law tests pass 55 of 55 in the registered build (`proposal/propcheck_law_tests.log`).
- **For ROOT:** route it to lane A, or authorize me to apply it; then Part 2 can start from `22e9d00062`.

## Part 1: what changed (PP only; B3-D's P-numbers)

- **P-1:** `lib.rs` `w1_route` decides the route once from lane A's `namespace_branch`: L and L3 preview, E exact; load states and 0.4.0 stay `Domain`. The observer is built on the route (`permitted_probe_on`); the private driver uses the same decision.
- **P-2:** `w1_budget`: the exact route's per-case exact-block limit is `PHYSICS_SOURCE_WORK_LIMIT` (8,000,000), as `ordinary_dispatch`'s.
- **P-3, P-5:** on the exact route the capture records each used material's ν and refuses typed unless the basis is `homogeneous_isotropic_E_nu_v1` and Ĝ is a positive normal equal to RN64(E/(2·RN64(1+ν))); members carry `ProductMaterial::BaseENu`; a selected basis is refused.
- **P-6:** the exact route's observables over physics-1's closed evidence (`{pressure: [], connector: [], exact_cases}`; the eight entry keys; profile, basis, complete coverage, no assembly group and +0 vectors; sections and materials bound to the captured OD, wall, E, ν, Ĝ), then the shared extrema, support and headline checks.
- **P-7, P-8:** maxima read `exact_cases[c]`; the owner case's `pipe_sections` take the prepared A, I, J, Z beside its extrema (same stage); unselected entries untouched.
- **P-9, S-1:** one route descriptor (`retained_wire::route_wire`): identity `physics-retained-1`, profile `exact_straight_retained_w1a_v2`, DEF-E's id on every attempt and DEF-E's H (`5a3bac43…`) in the preparation payload, `derived_e_nu` shear origin, `geometry.route: exact`. The preview route's bytes are unchanged.
- **P-10, P-11:** no PP change: precommit calls `retained_precision::validate` as before, and the legacy disposition is the existing machinery. The receipt carries no legacy disclosure on the selected case (asserted).
- **P-12:** two new hooks, `fault_next_exact_capture` and `break_next_section_overlay`.
- **P-13:** the pins below. Refused exact requests take the ordinary route: a combination, regions absent or non-empty, 0.4.0, and a point basis (`b3b_refused_exact_requests_take_the_ordinary_route`).
- **P-4** is a static test: no retained file or W1 function names a pressure-runtime builder.
- **One expected-text change** in a guard of mine: `u3_capture_permit_is_linear` now looks for `ProductCapture::permitted_probe_on(permit, route);` (the permit still moves into the observer; the test states why).

## Pins (both modes; `retained_facade_tests.rs`)

| Witness | Sparse | Dense |
|---|---|---|
| m3x exact successor: receipt; bytes; fixture document | `b1b4a668…896f`; `f18227f7…b20d`; `02465c6c…56d6` | `eabd2fc5…776d`; `e31f03a4…db2a`; `31f10f04…47cc` |
| m3x_mix_anchor (`case` selected, `case:b` not_required): receipt; bytes | `71703ab1…b29f`; `ca2cd750…a53b` | `b5cf5a4f…eec3`; `a50c530f…1337` |

- **New fixtures:** `P/fixtures/results/retained_precision_exact_successor_{sparse_interactive,dense_scrutiny}.json` are the live successor documents, byte for byte (tested).
- **The section evidence** (m3x, M1): SourceAnnulus's I/J/Z `…210b/…210b/…a7` become the prepared `…210a/…210a/…a6` (A unchanged), exactly B3-D §1.3's table; the receipt's section terms equal them (G5b's cross-check, asserted).
- **The receipt** shows Ĝ `4232a05f20000000` (8e10), ν `3fd0…`, `legacy_source_work[0].limit` 8,000,000, no legacy disclosure on the selected case, 98/99 rows all with the method token, `not_covered` empty.
- **Inputs:** m3x, m3x_mix_anchor and m3l built in the tests equal B3-W's Value sha256s (`c920a96d…`, `6ca777a6…`, `2f5ff465…`); n05, n06 and `fields` are the committed requests (`332319ee…`, `5551f164…`, `7f8ff9d5…`).
- **SCHEMA (G1 shape):** both new successors' `retained_precision` validate with 0 errors (jsonschema 2020-12; `scripts/schema_check.py`).

## What the readers do today (pinned and stated)

- **RS's precommit refuses every exact successor at G0 `SOURCE_PRODUCER_CONTRACT_UNSUPPORTED`** (no `physics-retained-1` branch until B3's readers land). So m3x and the mixed base fall back with the ordinary physics-1 bytes plus one N1 notice per case in A. The tests accept that or a validated successor and print which.
- **m3l (B3a): no producer change.** W1 runs to precommit; RS's G8 refuses (`INVOCATION_MISMATCH`, the contract); the successor differs from the milestone's pinned one in exactly `invocation.value`, `legacy_source_work[0].charged` and `receipt_sha256`; the ordinary bytes differ in exactly `diagnostics[3].message`.
- **N-11:** the noticed physics-1 fallback (Direct; and after serializer, section-overlay and precommit faults) is accepted by physics-1's base readers with the same contract and standing in **RS** (test), **PY** (`compatibility._source_contract`, standing; 8 of 8, each with a refused negative control) and **TS** (`sourceContract`, `validatePhysicsEvidence`, `numericalResultStanding`; vitest 9 of 9) (`_run_records/n11/`).

## Suites against `b2` at `e67c364680` (test by test; `_run_records/suites/`)

| Suite | `e67c364680` | `8d3419b542` | `22e9d00062` (head) |
|---|---|---|---|
| PP, all targets | 748 ok, 1 failed (t13), 11 ignored | 762 ok, 2 failed, 11 ignored: 15 added (all ok); **1 changed: lane A's oracle ok → FAILED** | 763 ok, 2 failed, 11 ignored: 16 added (all ok); the same 1 changed |
| Runner (all tests) | 85 ok, 2 failed (load-reference) | identical | identical |
| PP's dependents (`self_weight_wasm`, `operation_applier`; `--no-run --all-targets`) | compile | compile | compile |
| `src-tauri` (`cargo check --all-targets`, a PP dependent) | not run | not run | compiles |

The failures other than lane A's oracle are the base's own: PP `s11g_tests::t13_committed_fallback_uz_is_byte_identical` (RR's "known Mac `t13`"), and the runner's two load-reference tests. Every c = 1 and B1 multi-case pin is unchanged (no other test changed). FK is untouched.

## Mutants (`_run_records/mutants/`)

One per new check (59; `mutants/p1.json`), each an exact edit of a scratch archive, run with PP `--lib` filtered to the B3b, B3a, `u1_constants`, `u3_permitted_path` and W-C2 transaction tests (lane A's failing oracle skipped). Each is killed by a named failing assertion (`mutants/logs_*`).

- **On `cc24cd955c`'s tests: 56 killed, 3 survived.** I added assertions for two of the survivors in `22e9d00062`, then reran the three survivors on it: P1-42 (`ProductCaseView::number` reading the preview evidence) and P1-34 (the observables' section coverage) are now killed.
- **Result: 58 of 59 killed.**
- **The one survivor, P1-02, is equivalent:** `w1_route`'s load-state guard. 0.4.0 has no namespace branch, so `namespace_branch` already returns no route. I kept the guard as a defensive check.

## Notes for ROOT

1. **The stop** (above): one lane-A test; proposal and check attached.
2. **Readers:** until B3's readers land, no exact successor publishes; the new successors' bytes are pinned on the private driver and the Direct entry (the same bytes reach precommit).
3. **One defensive check kept, equivalent by construction:** `w1_route`'s load-state guard (P1-02).
4. **N-11** needed no physics-1 reader change: the readers accept the notice.

## Host and records

- Every cargo ran through `WT/tools/t3_cargo.sh --locked --offline` with targets `WT/targets/i105-b2-p-{pp,runner,self_weight_wasm,operation_applier,tauri,dev,mut}`; PY and vitest through `WT/tools/t3_slot.sh`; one heavy job of mine at a time; no RSS or timing measurement, no DEC-025, no install. Scratch and `TMPDIR`: `WT/scratch/i105_b2_p/`. The TS check ran in a scratch archive of `e67c364680` (TS is untouched) with `node_modules` linked from the App worktree and the wasm assets copied from `WT/sweep-skewpin` (sums in `n11/ts_wasm_assets.sha256`); vitest's cache stayed in the archive.
- **A slip, disclosed:** I started a second wait loop on the mutant job while my first wait was still running, then stopped it. Afterwards each job had one wait. I signalled no other job.
- Records: placeholder paths only (`scripts/sanitize.py`), no symlink, no folder named `build`. The host screen (`WT/tools/t3_host_screen.py`) over `e67c364680..22e9d00062`: 9 files, 0 hits; over these records (`scripts/screen_files.py`, its patterns read whole files): 0 hits.

---

# Part 2: B2-P, with RV123's items, lane A's repair merge and RV125's constraint

2026-10-08 UTC. After Part 1, ROOT sent:
- its ruling on the stop (apply lane A's oracle on `b2`);
- RV123's refinement of that oracle;
- RV123's S-1, S-2 and N-2;
- the lane A merge;
- RV125's forward constraint.

All are done. Part 2's records are in `_run_records/part2/`.

**Basis (sums verified):**
- B2-C: CONTRACT `165cd4b1…`, REVISION_01 `6f6a583f…`, REVISION_02 `79007dcd…`;
- I102's RETURN `0d538ca1…`;
- I98's PROBE `e224899a…`;
- PLAN `e1147dbd…` §1.2.4 and §1.2.6;
- RR on RV118, RV115, I98, RV122, RV123 and RV125.

## Heads (`WT/b2`, `codex/piping-t3-b2-20261008`; not pushed)

| Commit | What |
|---|---|
| `56e44fa081`, `a09e24b44c` | Lane A's B3b oracle, as ROOT ruled, then RV123's refinement. The oracle is renamed `b3b_direct_entry_coexistence_keeps_the_exact_bytes_and_m3x_falls_back_at_g0`. It pins m3x's G0 fallback byte for byte; n05 and n06 stay Coexistence. Lane A's law tests: 55 of 55. |
| `1032fc8357` | B2-P part 1: the producer |
| `794cb36e85` | RV123's S-1, S-2 and N-2 (test-only, plus the hook `fail_freeze_of_case`) |
| `384c9a1ed8` | B2-P part 2: the witnesses, pins, fixtures and tests |
| `583fc758ee` | **The merge of lane A's repair round 01 (`ea5625ad04`), as ROOT asked; no conflict** |
| **`638214d8d8`** | B2-P part 3: the mutant kills, RV125's refusal pin and the `with_case` guard |

## B2-P (PP only)

- **`lib.rs`:**
  - `w1_case_ids` is widened.
  - One D1.4 predicate, `w1_combinations_admitted`, serves T-4's re-check and the T-2′ capture hooks.
  - `W1Fallback::CombinationCustody` is added.
- **`retained_product.rs`:**
  - T-2′ captures the combinations.
  - T-9′ checks the gate entries for shape and consistency only.
  - T-6′ ends the case blocks at the first combination row, and each mechanics combination's rows form one run.
  - At c = 1 with z ≥ 1, the case is its own block.
  - T-8′ uses `for_invocation`, and T-11′ takes headlines from load-case rows.
  - T-10a assigns the dispositions.
  - T-10b sets the operand sources: Selected; Rebuilt at the batch source id with no import; or Prepared through C3a and `register_prepared_source`.
  - Each retained combination gets one Call, then its freeze on operand 0's slot, with REVISION_01 §1.2's observables stage, then the staging overlays.
  - A rebuild refusal abandons with `CombinationCustody`.
- **`retained_wire.rs`:**
  - `combinations[]` and `operand_preparations[]` (absent when empty);
  - `CaseSource.preparation`, `CombinationSource`, the mechanics Call and the group imports;
  - `CombinationAttempt` (DEF-C);
  - the ordinal mapping, the meter chain and the combination diagnostics.
  - At z = 0 the bytes are unchanged.
- **Hooks:** `fail_operand_preparation`, `fail_combination_call`, `fault_next_combination_freeze` and `break_next_meter_chain`.
- **RV122 N-3:** the two facade tests now use h = 4.

## Witnesses, pins and readers (both modes; `pins.txt`, `b2p_tests.txt`)

| Witness | Disposition | Precommit today |
|---|---|---|
| W-CB1: 1·A + 0.5·B on SW's cap-maximal cases | retained_selected | G0 |
| W-CB1z: A + B, the labelled cancellation pin | retained_selected | G0 |
| W-CB2 | retained_unavailable (`combination_unresolved`, kernel) | G0 |
| W-CB3 v1 | retained_selected, with one operand preparation | G0 |
| W-CB4a, W-CB4b, W-CB5 | ordinary | G3 |
| `b2_c1_range_mechanics` | ordinary, then retained_selected | G0 |

- **Inputs:** W-CB1 and W-CB1z are built in the tests from I86's generator. The four I98 inputs are JSON-equal to I98's files (`inputs_check.txt`).
- **Each pinned successor (receipt and bytes) meets B2-C's producer requirements:**
  - the combinations and their rows;
  - R-COMB-1's producer side: ordinary and unavailable rows are untouched, and selected rows carry the method token;
  - headlines from load cases;
  - the meter chain and the ordinal mapping;
  - the operands and their identities;
  - operand 0 as the representative;
  - the combined ledger.
- **Direct entry (registered build):** precommit receives the private driver's successor, byte for byte.
- **Readers today:**
  - **RS precommit** refuses at G0 `SOURCE_PRODUCER_CONTRACT_UNSUPPORTED` (a DEF-C attempt) or G3 `RETAINED_PRECISION_COVERAGE_MISMATCH` (ordinary only). It publishes the plain bytes plus one notice per case in A, byte for byte. The base readers read those bytes with the plain bytes' contract and standing.
  - **PY:** `validate_retained_precision` refuses both fixtures at G0 `SOURCE_PRODUCER_CONTRACT_UNSUPPORTED`, as RS does (`readers_py.log`; checked-JSON authority built through `t3_cargo.sh`).
  - **TS:** not run on these successors. RS's precommit gates publication, and the noticed fallback is B1's shape, which the base readers already accept.
- **Fixtures:** `retained_precision_combination_successor_{sparse_interactive,dense_scrutiny}.json` are W-CB3's live successor documents, tested byte for byte. W-CB1 and W-CB3 both select. I chose W-CB3 because it carries the operand preparation and its documents are 0.55 MB; W-CB1's are 10.4 MB each, and the largest existing fixture is 5.5 MB.
- **SCHEMA:** 0 errors on 16 witness successors and on 29 more from the failure set and the expressions (`schema_check*.log`).
- **Tests:** Part 2 adds 24: 20 `b2p_*` and RV123's 4. Three existing tests were updated within lane P's files: RV122 N-3's two facade tests, and the i51 seam's combination case (now h = 4).
- **NA4-5:**
  - The ordinary route forms a combination's displacement magnitude by nested binary64 `hypot`. The retained route (B2-K's projection) forms RN64 of the exact 3-norm. The two can differ by about 2 ulps; G7's 64ε guard holds on both.
  - On W-CB1, W-CB3 and `b2_c1_range_mechanics`, every retained magnitude equals RN64 of its components' exact 3-norm, and nested `hypot` gives the same bits there (`na45.log`).

## RV123, lane A's merge, RV125

- **RV123:** S-1 (two-member exact, both orders), S-2 (an `unavailable` exact case, on both serializer branches) and N-2 (an unused material) are pinned. Its mutants R-01, R-02, R-03, R-06 and R-11 are killed (`rv123/`).
- **Lane A's merge (`583fc758ee`; `lane_a_merge_check.txt`):**
  - Law tests: 55 ok, 1 failed. The passing tests include SF-2's new test, and SF-1's `b3a_direct_entry_oracles` passes.
  - `retained_precision_admission`: 5 of 5, as before.
  - The one failure is lane A's interim test (the STOP below), failing since `1032fc8357`.
  - No other outcome changed.
- **RV125 N-2:** no B2-P or B3b-P path admits a material selector at c ≥ 2, so the custody stays per invocation (`rv125.txt`):
  - G-A refuses a selector on any case (D1.5).
  - The exact capture refuses any selector (P-5).
  - On the private driver, a selector on case 0 fails the custody (`Preparation`), and a selector on case 1 alone fails every attempted case's freeze (`Candidate`).
  - `b2p_selectors_at_two_cases_are_refused` pins all of this for z = 0 and 1 and both modes.
- **RV125 N-3:** `with_case` documents the hazard. In debug builds, the per-case accessors assert they never read the lent case or the last-seen case inside it; `b2p_with_case_guards_cross_case_reads` shows the assert firing.

## STOP: lane A's interim test (outside my files)

`b2_a_admitted_combinations_keep_the_exact_ordinary_bytes_until_b2_p` asserts `W1Fallback::Domain` "until B2-P". In the registered build it now fails: c = 1, z = 2 gives `Precommit{G0, SOURCE_PRODUCER_CONTRACT_UNSUPPORTED}`, and c = 2 with a range gives G3.

- **Proposed, not applied:** `proposal/lane_a_b2_admitted_combinations.diff` (test-only, against `583fc758ee`). It renames the test `b2_a_admitted_combinations_run_w1_and_fall_back_at_precommit_today` and pins:
  - G0 with notice `case`;
  - G3 with notices `case-1` and `case-2`, byte for byte;
  - or a validated successor once B2's readers land.
- **Checked:** lane A's law tests pass 56 of 56 in a scratch archive of `583fc758ee` (`proposal/propcheck2_law_tests.log`).
- **For ROOT:** route it to lane A, or authorize me to apply it.

## Suites against `e67c364680` at `638214d8d8`, test by test (`suites/`)

| Suite | `e67c364680` | `638214d8d8` |
|---|---|---|
| PP, all targets (registered) | 748 ok, 1 failed (t13), 11 ignored | 788 ok, 2 failed, 11 ignored |
| Runner (all tests) | 85 ok, 2 failed (load-reference) | identical |
| PP's dependents (`self_weight_wasm`, `operation_applier`; `--no-run --all-targets`) | compile | compile |
| `src-tauri` (`cargo check --all-targets`) | not run | compiles |

- **PP, test by test:**
  - 42 tests added, all ok: Part 1's 16; ROOT's renamed lane-A oracle; Part 2's 24; lane A's SF-2 test.
  - 1 removed: the lane-A oracle's old name.
  - **1 changed: lane A's interim `b2_a_…_until_b2_p`, ok → FAILED (the STOP).**
- **The other failures are the base's own:** PP's `t13` and the runner's two load-reference tests.
- **Every c = 1 and B1 multi-case pin and the coexistence bytes are unchanged:** no other test changed. FK is untouched.

## Mutants (`mutants/`)

There is one mutant per new check, 47 in all (`mutants/p2.py`). Each is an exact edit of a scratch archive, run under PP `--lib` with the `b2p_`, `b3b_rv123`, `b1_sp_w_c2`, `b1_sp_domain` and `i51_c0` tests; W-CB1's two slow tests are skipped.

- **First run, at `583fc758ee`:** 39 killed, 7 survived.
- **Part 3 (`638214d8d8`) added kills for five of the survivors:**
  - P2-05: the predicate at its caps, z ≤ 2 at c = 0;
  - P2-07: the early hook's own refusal;
  - P2-09: an extra gate entry, and no gate entry;
  - P2-31: a second row of one translation;
  - P2-44: the meter chain, through `break_next_meter_chain`. Its edit now removes the check together with the hook's term.
- **Part 3 also added P2-47,** for the N-3 guard.
- **The rerun at `638214d8d8`:** these six are killed. P2-47 is killed by a `should_panic` test, whose name the driver's first pattern missed; I corrected the pattern and re-derived every verdict from the logs (`scripts/rederive.py`). Only P2-47 changed.
- **Result: 45 of 47 killed.**
- **Two equivalents are kept as defensive checks:**
  - **P2-22,** T-10a's "mechanics" conjunct: the capture records terms only for mechanics combinations, so no other combination has a selected term.
  - **P2-36,** the ordinal mapping's prepared-registration branch: no FK Call names a prepared registration as its owner, because registrations are not Calls, and an unknown owner fails closed.

## For SQ2 (as RV123's N-5 was for B3b-P)

At z ≥ 1, B2-P adds work on the preview route:
- **allocations:** the captured combinations, the combination row runs, the combination attempts, the operand preparations and the rebuilt sources, and FK's combination Runs, which `for_invocation` prices;
- **loops:** custody over the combination rows; the gate-entry checks; the combination observables stage, nodes × block rows per combination.

The combination freeze runs inside W1 on the reserved stack, and S1's stack witnesses do not cover its frames.

## Host and records

- **Host:** every cargo command ran through `WT/tools/t3_cargo.sh --locked --offline`, with targets `WT/targets/i105-b2-p-*`. PY ran through `t3_slot.sh`. One heavy job of mine ran at a time, with one wait each. No RSS or timing measurement, no DEC-025, no install.
- **Records:** placeholder paths only, with no symlink and no folder named `build`. The host screen over `22e9d00062..638214d8d8` (12 files) found 0 hits, and over these records (`scripts/screen_files.py`) it also found 0 hits.
- **Scope:** since `e67c364680`, `b2` changes only PP (`core/product_physics`) and adds four fixtures; no schema and no FK file changes. Outside lane P's files, the only changes are ROOT's one-off lane-A oracle edit and lane A's merged repair.

## Addendum: the stop applied; the NUM merge not made

- **ROOT ruled the stop: apply the proposal on `b2`.** It is applied at **`72b3e5d9ea`**: lane A's `retained_memory_law_tests.rs`, test-only, byte for byte the file checked in the scratch archive.
  - Law tests: 56 of 56.
  - `retained_precision_admission`: 5 of 5.
  - Records: `_run_records/part2/lane_a_applied_check.txt`.
  - Host screen of the commit: 0 hits.
- **NUM's `31eed8497f` is not merged: it conflicts.** `git merge-tree` reports a content conflict in `retained_memory_law_tests.rs`, in three hunks:
  - b2's M and `NO_COMBINATIONS` against B1 SQ's M = 10.5 GiB and `MARGIN`;
  - the runner-literal test;
  - B3a- and B3b-A's law tests against B1 SQ's two new tests.
- The conflict already exists at `794cb36e85`, before the lane A merge. b2's merge base with NUM is `8d46b045e2`, so the merge would also bring B1 SQ G5/G6, R6b (M), B6, SI1b/SI1c and the cases fixture, not only the three test files. Per ROOT, I did not start it.
