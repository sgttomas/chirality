# I110 round 3: Stage 1 repairs and Stage 2 (implemented)

I110 is a TASK for WORKING_ITEMS (T3). The brief is `R/BRIEFS/U3_PRESSURE_RETIRE_03.md` (sha256 `7c5f055a6d64223853abfce09e14bf9cc69e982b5a962b49c003bf9b193df9b5`, verified). The review is `R/REVIEW_RV127/u3_stage1_01/REVIEW.md`. The plan is round 1's §5 Stage 2 (`R/I110/pressure_retire_01/RETURN.md`).

The branch is `codex/piping-t3-pressure-retire-20261008` in `WT/t3-pret`. Head: **`6b6543dc1e`**, 4 commits on `4c0d5d7c00`. Product files only; not pushed.

## Stop status

**Stop: none on the brief's conditions.**
- No exact or pressure-free byte changed: 588 of 588 rows are equal, H-1 included.
- Nothing held by T4 was needed or touched. The joint element's code (FK `user_stiffness_local_matrix` and its plumbing) is unchanged.
- I114's fixtures, their consumers, and `pressure_runtime.rs:226-228` are untouched.
- Every per-test outcome change is a planned removal, rename or addition.

**One deviation from the plan needs your acceptance before merge.**
- Round 1's plan said "B1's pins unchanged". One B1 pin moves: the in-build memory-profile record.
- **Cause.** Deleting the `StressComponents` pressure fields (two `Option<f64>`) and `DerivedSection.membrane_radius` shrinks two profile atoms:
  - `s((&str,StressRecoveryResult))`: −32 bytes, 9 per phase;
  - `s((String,DerivedSection))`: −8 bytes, 64 per phase.
  - Together that lowers every phase by exactly 800 bytes, in both modes.
- **What I did.** I regenerated `PINNED_RECORD` (`PP/src/retained_memory_law_tests.rs`) and the challenge literals `W1_PHASE_BYTES` and `MAX_PHASE_BYTES` (`PP/tests/retained_memory_challenge.rs`), following the code's rule "regenerate the record with the profile". This is in commit `9930cfe6db`.
- **What did not change.** No binding, form or phase changed. All B1 publication bytes are equal (W1: 64/64, with 34 successors). The pin tests pass.
- **Merge risk.** `QUAL_B1.md` cites the old figures. I101's B1 lane may edit the same constants, so a conflict is possible.
- **Alternative.** Keep the three dead fields so that B1's pins stay unchanged. That is a code change, not a revert of a commit.

## Commits (`4c0d5d7c00..6b6543dc1e`)

| Commit | What |
|---|---|
| `769c109d82` | Stage 1 repairs from RV127 |
| `cda85e06d5` | Stage 2: the test-only historical scope removed |
| `9930cfe6db` | Stage 2: the legacy computation and its validation cases removed; also N-4, H-1 and the B1 profile re-pin |
| `6b6543dc1e` | G11 |

**`769c109d82`, Stage 1 repairs from RV127:**
- **B-1:** `endpoint_section_cut_fixed_and_free_thermal_match_uniform_stations` restores the deleted test's thermal half as a pressure-free test, in both modes.
- **N-5:** the panel now marks "retired" only for exactly `1.0.0/legacy_pressure_v1`. Other contracts show "unsupported". A model without a contract that still carries legacy primitives says so and names their count.
- **N-6:** the zero-primitive refusal is pinned on the retained entry and in a CLI solve.
- **N-7:** both pre-existing texts name `2.0.0/exact_straight_pressure_v2`.

**`cda85e06d5`, the test-only historical scope removed:**
- `historical_pressure_reference.rs` and its `mod`;
- both bypasses: the joint bypass and the legacy-pressure bypass;
- O1, O2 and O4;
- O3's second half. Its first half stays as `realized_user_stiffness_joint_is_refused_on_the_ordinary_route`;
- `historical_pressure_preview(_with_mode)` and the two scope tests. The demo's ordinary refusal stays as `bundled_demo_with_legacy_nonzero_pressure_is_refused_on_the_ordinary_route`.

**`9930cfe6db`, the legacy computation removed.** It follows the plan's Stage 2 item 2.

In PP:
- the thrust types, builders and assembly;
- the bend radial thrust;
- the joint thrust rows and `EXPANSION_JOINT_PRESSURE_THRUST_APPLIED`;
- `pressure_for_pipe`;
- the hoop and longitudinal rows and `include_pressure_longitudinal`;
- the W2 `pressure_thrust_load` family;
- `recover_section_stress`'s `pressure` parameter;
- the always-empty plumbing in `source_recovery.rs`, `source_receipt.rs` and `retained_product.rs`;
- `membrane_radius`, which only the hoop rows read.

In the other crates:
- `stress_recovery`: `PressureBasis`, the membrane, and the pressure components and ranges;
- `curved_bend`: the radial-pressure API.

Validation cases:
- **`STRESS-PRESSURE-MEMBRANE-ORIGINAL`:** benchmark, runner binding, hand calculation, manual page and index rows removed.

Kept, as the plan says:
- `component_pressure_thrust_load_count`, always 0;
- the exact retain list;
- the preview-physics-1 kind lists and the result schemas;
- the primitive `pressure` category;
- `pressure_thrust_reference`.

**`6b6543dc1e`, G11.** See below.

## Consequential changes for review (not named in the brief)

- **`MECH-CURVED-BEND-PRESSURE-THRUST-ARC` is removed** (benchmark, hand calculation, README rows). It exercised the deleted radial API. The mechanics suite goes from 25 to 24 cases and from 206 to 194 values.
- **`STRESS-TP-PMM-P3-MILLTOL-EFFECTIVE-WALL-STRESS` loses its two membrane values.**
  - Its runner binding also ran the legacy thin-wall formula. RV127's N-1 covered only the membrane case.
  - The case keeps its four mechanics components. Its hand calculation says the membrane values were removed.
  - The stress suite goes from 15 to 14 cases (11 matched, 3 blocked).
  - The benchmark-local governed complete stress envelope goes from 6 to 4 quantities.
  - The manual inventory goes from 64 to 63 pages.
- **Published texts that name the old treatment are kept** (they are pressure-free bytes):
  - the formulation limitation at `PP/src/lib.rs:1944`;
  - the joint review-row basis and sign texts (`:11988-11995`), which mention `pressure_thrust_generation`;
  - the curved-bend review row's `pressure_thrust_treatment=…`.
  - Changing any of them is a separate text decision, for the owner or T4.
- **The "each pressure-only" claim is corrected.** Round 2's record called all 11 deleted `*_historical_pressure_premise` tests pressure-only scope oracles. In fact 10 were pressure-only or had a pressure-free twin. `endpoint_section_cut_fixed_and_free_pressure_thermal_match_uniform_stations_historical_pressure_premise` also had a thermal half (RV127 B-1), which `769c109d82` restores.

## N-4 and H-1

- **N-4.** The source-block namespace gate (`PP/src/source_recovery.rs`) stays as defence in depth. It is now pinned at unit level by `non_exact_source_blocks_gate_refuses_a_later_version_a_contract_or_regions`, which covers:
  - 0.3.0 without a contract;
  - each of the two contracts on 0.1.0;
  - regions present.
- **H-1, the code.** The retired term entered three sums as `+ unwrap_or(0.0)`. Each now keeps an explicit `+ 0.0`:
  - `open_formula_summary_mpa`;
  - `straight_summary_extrema`;
  - `stress_recovery`'s `summarize_components`.
- Every other removed term was absent for pressure-free models: an empty slice, or a loop with no entries. So the remaining sums are unchanged.
- **H-1, the bytes.** All 588 rows are byte-equal to B. The candidate's envelopes contain many `-0.0` tokens, so the corpus does exercise signed zeros:

| Set | Rows with `-0.0` in the ordinary envelope | Tokens in ordinary envelopes | Tokens in export documents |
|---|---|---|---|
| E | 92 of 96 | 11374 | 28915 |
| F | 109 of 364 | 269617 | 68191 |
| B1 | 44 of 64 | 3610 | 1260 |

## G11

**The confirming test** is `PP/src/lib.rs` `tests::flexibility_joint_missing_a_user_stiffness_is_refused_not_dropped`. It loops over the four user stiffness values, lateral first.

**Before the fix it failed** (`_run_records/g11_confirm_before_fix.txt`):

```
lateral: the joint without this value must be refused, not dropped
  left: ("MECHANICS_SOLVED", 3)
 right: ("MODEL_INCOMPLETE", 0)
```

So the demo model with C-150's lateral value removed solved without the joint, and published three review rows saying its stiffness was "consumed by the assembled user-stiffness macro-element".

**The fix** is in `PP/src/preview_physics.rs` `refuse_unqualified_joint_elements`. A `mechanics_geometry_and_user_flexibility` joint that lacks any of the four user stiffness values is refused before the solve:
- code `JOINT_ELEMENT_STIFFNESS_INCOMPLETE`, blocking;
- the message names the missing values;
- refs: the joint and its pipe.

The builder skips such a joint, so a missing axial, angular or torsional value has the same defect.

The test passes on the head. No committed document has such a joint (scanned).

Residual, for T4: the builder's other silent skips (an unmapped pipe or node, a missing `y_reference`) are not covered.

## Evidence (B = main `7eae707bb7`; candidate = `6b6543dc1e`; this host)

The B side reuses round 2's records: same commit, host, toolchain and scripts.

**Per-test outcomes.** Every change is in the plan. The changes equal, name for name, the `#[test]` names removed and added in source between B and the candidate (`_run_records/test_name_diff.txt`).

| Suite | B | Candidate | Changes |
|---|---|---|---|
| 40 manifests | 2776 pass / 3 fail / 80 ignored | 2753 / 3 / 80 | 53: 38 removed, 15 added (round 3's share is 22 removed and 10 added; listed below) |
| src-tauri | 116 | 117 | +1 (round 2) |
| `P/tests` pytest | 4426 passed, 32 skipped | 4426 passed, 32 skipped | 0 |
| vitest (reporter totals) | 4245 | 4248 | `App.test` renamed (round 2); 3 panel tests added (2 in round 2, 1 in round 3) |

- The three failures are the same tests at B and at the candidate. All are known Mac platform failures: PP `t13_committed_fallback_uz_is_byte_identical` and the runner's two load-reference frozen goldens.

Round 3's 22 removals:
- the stress-recovery pressure tests (3; one is renamed);
- O1, O2, O3's old name and O4;
- the two scope tests;
- the macro-span arc thrust test;
- 6 `curved_bend` radial-pressure tests;
- 2 `MECH-CURVED-BEND-PRESSURE-THRUST-ARC` tests;
- 2 `STRESS-PRESSURE-MEMBRANE-ORIGINAL` tests;
- 2 suite-count tests, renamed with their new counts.

Round 3's 10 additions:
- B-1;
- the demo refusal and O3's new name;
- G11;
- N-4;
- N-6, twice;
- the 3 renames.

**Byte equality.** The probe-only harness hashes three things: PP's ordinary envelope, the runner's mechanics envelope, and the RE export document. Both modes:

| Set | Rows | Result |
|---|---|---|
| E (48 exact documents) | 96 | all equal |
| F (182 pressure-free implicit documents outside B1) | 364 | all equal |
| B1 (32 documents) | 64 | all equal |
| B1 through the retained direct entry (W1, debug build) | 64 | all equal: 34 successors and 30 ordinary publications |

## For WORKING_ITEMS

- **Merge with I114.** `cda85e06d5` deletes the five bypass lines directly above I114's S-1 lines at `PP/src/pressure_runtime.rs:226-228`. A small adjacent conflict is likely. Neither side changes the other's lines.
- **Linux CI.** Please dispatch CI on the pushed head. It is needed for the frozen goldens this Mac cannot check, and for `r2-smoke` (RV127 N-8). The e2e spec was not run here.
- **Worktrees.** `WT/t3-pret-hc` is now detached at `6b6543dc1e`, with the untracked harness. `WT/t3-pret-hb` and `WT/t3-pret-base` are unchanged.

## Records

- `RETURN.md`
- `_run_records/` (see its `README.md`)
- `SHA256SUMS`

Paths use placeholders only.
