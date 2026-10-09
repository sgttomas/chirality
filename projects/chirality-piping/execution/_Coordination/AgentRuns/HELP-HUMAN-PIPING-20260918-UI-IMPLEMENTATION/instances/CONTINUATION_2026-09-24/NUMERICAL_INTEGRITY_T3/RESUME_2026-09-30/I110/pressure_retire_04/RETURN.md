# I110 round 4: G11 extended, A1-S-1, A1-S-2, A1-N-4 and the text-truth item

I110 is a TASK for WORKING_ITEMS (T3). The round-4 instructions came as WORKING_ITEMS messages carrying ROOT's rulings:
- RR "U3 Stage 2 rulings: the 800 B profile re-pin, …";
- RV127 addendum 01 (A1-S-2, A1-N-4);
- the A1-S-1 ruling;
- RV128 N-5.

Branch `codex/piping-t3-pressure-retire-20261008` in `WT/t3-pret`. Head: **`5bc6f269da`**, 5 commits on `6b6543dc1e`. Product files only; not pushed.

## Stop

**STOP, item 4 only: two published-text corrections are not made.** Each reaches pins that ROOT reserved. Nothing was re-pinned. The blast radius is below, and ROOT decides.

- **T4: `PP/src/preview_physics.rs:75`, `LIMITATIONS[1]`** (RV128 N-5). It reads "Nonzero pressure is refused on this route, …", but a zero legacy primitive is refused too. It is in every preview-physics-1 and retained W1 output, and it reaches:
  - W-C2's successors;
  - B1's corpus;
  - the readers' corpus 07n;
  - a published schema `const`.
- **T2: `PP/src/lib.rs:1944`, the `product_preview_mechanics_v1` limitation.** It reads "Pressure thrust and pressure stress retain the existing preview formulation …", which is untrue. It is published only in envelopes where retained-source (source-block) recovery is selected.
  - It reaches none of W-C2, B1's corpus, or 07m/07n.
  - It does reach a retained-source publication pin and the source-block fixtures. I stopped on it conservatively.

Everything else asked in round 4 is done. Byte results: exact 96/96 and B1 and W1 64/64 equal. Pressure-free (F): 362 equal, 2 differ only in the declared text.

## Commits (`6b6543dc1e..5bc6f269da`)

| Commit | What |
|---|---|
| `16ce82f573` | G11 extended: an unresolved pipe or node is refused with the new blocking code `JOINT_ELEMENT_MAPPING_UNRESOLVED` |
| `d9782e16c9` | A1-N-4: the G11 tests fail before the fix in every case (details below) |
| `7a0873eb5c` | A1-S-2: stale references (details below) |
| `4aad4f42fa` | Text truth, the curved-bend and joint review rows (T1, T3) |
| `5bc6f269da` | A1-S-1: the legacy straight-pipe pressure thrust |

`16ce82f573` refuses these cases, before the M07 check:
- no pipe;
- an unknown pipe;
- an unknown joint node;
- a node that is not an end of the pipe.

It is a new code because `EXPANSION_JOINT_MAPPING_INPUT_INVALID` is a non-blocking validation warning on the same subject, and `JOINT_ELEMENT_STIFFNESS_INCOMPLETE` concerns stiffness values. A pipe without `y_reference`, or with an unknown end node, needed no new code; see G11.

`d9782e16c9` (A1-N-4) sets the lateral value to zero in every case except the missing-lateral one, so M07 cannot mask the defect. It also corrects `16ce82f573`'s claim that the node cases were already refused.

`7a0873eb5c` (A1-S-2):
- (a) the `STRESS-RANGE-MECHANICS-ORIGINAL` generator entry, the regenerated page and the hand calculation no longer cite the deleted test or the pressure ranges;
- (b) the `stress_recovery` README no longer describes the pressure membrane;
- (c) the DEL-10-05 multi-case witness loses MILLTOL's two membrane values. It now equals the current runner's payload for that input.

## G11: failing, then passing

The test logs are in `_run_records/g11_tests_before_fix.txt` and `g11_tests_at_head.txt`. "Before" means `preview_physics.rs` from `9930cfe6db`, with the head's tests.

**`flexibility_joint_missing_a_user_stiffness_is_refused_not_dropped`** fails before the fix: all four cases solve.

| Missing value | Status before the fix | Review rows saying "consumed" |
|---|---|---|
| lateral | `MECHANICS_SOLVED` | 3 |
| axial | `MECHANICS_SOLVED` | 2 |
| angular | `MECHANICS_SOLVED` | 2 |
| torsional | `MECHANICS_SOLVED` | 2 |

At the head, all four are refused by `JOINT_ELEMENT_STIFFNESS_INCOMPLETE`.

**`flexibility_joint_with_an_unresolved_mapping_is_refused_not_dropped`** fails before the fix: all four cases solve.

| Case | Status before the fix | Review rows saying "consumed" |
|---|---|---|
| no pipe | `MECHANICS_SOLVED` | 0 |
| unknown pipe | `MECHANICS_SOLVED` | 3 |
| unknown node | `MECHANICS_SOLVED` | 3 |
| node not on the pipe | `MECHANICS_SOLVED` | 3 |

At the head, all four are refused by `JOINT_ELEMENT_MAPPING_UNRESOLVED`, with the refs checked. Before A1-N-4, the node cases used a nonzero lateral value, and M07 refused them for a lateral coupling the model never realizes (`g11_extension_before_fix_lateral_nonzero.txt`).

**`flexibility_joint_pipe_without_orientation_or_a_known_end_is_refused_by_the_pipe`** passes both before and after the fix. There is no defect: the pipe itself is refused by `PIPE_ORIENTATION_INPUT_MISSING` or `PIPE_ENDPOINT_UNKNOWN`, both blocking. The test pins this.

No committed document has a flexibility joint in any of these states. The joint element's code is unchanged (T4).

## A1-S-1

**Removed:**
- the `Pressure` arm of `primitive_loads` `prepare_straight_pipe_axial_effects`, and `ElementAxialEffectProperties.internal_area`, which only that arm read. A pressure load is now refused (`UnsupportedTargetForCategory`) and blocks every output.
- MECH-TP-PHYS-008/009's pressure halves.
  - The axial totals, equivalent loads and axial resultants are now 3.0 N (was 12.0 N).
  - Transverse results and displacements are unchanged.
  - Hand calculations, README lines and the two regenerated manual pages are updated.
  - The fixture ids are kept; `-008`'s id still says PRESSURE.

**No exact-path caller.** `_run_records/a1s1_callgraph.txt` shows only two callers: `primitive_loads`' own tests and the mechanics benchmark. The 48 exact documents (96 rows) are byte-equal at the head.

**Suite counts:**

| | Main B | Round 3 head | Round 4 head |
|---|---|---|---|
| Mechanics suite | 25 cases, 206 values | 24, 194 | **24, 192** (TP-PHYS-008: 8→7 values; -009: 18→17) |
| Stress suite | 15 cases (12 matched, 3 blocked) | 14 (11, 3) | 14 (11, 3), unchanged |
| Manual pages | 64 | 63 | 63 |

The runner's frozen-projection test still checks the 11 original cases. It now compares the two changed cases by status and value names only.

## Text truth: changes and blast radius

The declared pairs are in `_run_records/scripts/text_pairs.json`. The carriers are in `static_carriers.md` (committed files), `text_census.txt` (corpus rows) and `experiment_failures.txt` (tests).

The mechanical check works as follows:
- For every output, the harness also records the SHA-256 of the output with each new string replaced by its old one.
- An output differs from B only in declared text when that normalized SHA equals B's SHA.
- `declared_text_check.txt` records the result.

**Made (`4aad4f42fa`):**
- **T1, the curved-bend row:** `pressure_thrust_treatment=none_pressure_refused_outside_the_exact_straight_contract`.
- **T3, the joint rows:**
  - basis: `pressure_thrust_generation=none_pressure_refused_outside_the_exact_straight_contract;user_pressure_thrust_reference=…`;
  - sign convention: "…; no joint pressure thrust is generated and no compliance claim is made".
- **Blast radius:**
  - **Corpus:** one document changes: `result_export_v0_2.json`'s producer case 1, in both modes (ordinary envelope and runner mechanics envelope). It changes in the declared string only (normalized SHA equals B). No joint row is published by any committed document.
  - **Tests:** no Rust, pytest or vitest outcome changed.
  - **Static files left as they are:**
    - `result_export_v0_2.json` (T1, T3);
    - I114's three demo fixtures (T3);
    - 8 historical evidence files and 2 stale witness outputs (T3).

**Not made (STOP):**

| | T2 (`lib.rs:1944`) | T4 (`preview_physics.rs:75`) |
|---|---|---|
| Corpus rows carrying it | F: 26 (13 source-block documents × 2 modes) | F: 316 of 364 ordinary rows; B1: 64/64; W1: 64/64 (34 successors) |
| New Rust failures with the text applied | 1: `f1b_w2_exact_block_selection_of_a_range_triggered_case_publishes_mains_bytes` | 28, listed below |
| Committed files carrying it | 14 source-block fixtures; 2 precision UI fixtures; I114's precision-1 pair | 8 retained successor fixtures; 07n; the schema; 7 other result fixtures; I114's preview-physics-1 pair |

T4's 28 new Rust failures include:
- every W-C2, milestone, l0 and U3 successor pin;
- `limitations_match_the_frozen_table`;
- `registered_g_c_declines_only_unattempted_solves`;
- 4 runner tests.

T4's committed carriers are:
- 8 retained successor fixtures: W-C2 (2), milestone (2), l0 (2) and derivative (2);
- the readers' corpus 07n, `retained_precision_cases.json`: all 26 cases carry it, and with them all 534 mutations and 78 must-pass entries;
- the published schema `schemas/results.v0.3.schema.yaml`: `const` limitations for preview-physics-1 and the retained W1a v2 profile;
- 7 other result fixtures;
- I114's preview-physics-1 pair.

**Proposed texts:**
- **T2:** "Pressure is not solved on this profile: legacy pressure inputs are refused, and pressure is solved only on the exact straight-pressure profile, under that profile's own qualifications."
- **T4:** "Legacy pressure primitives are refused on this route, zero values included, and so is legacy imposed_displacement."

**Other published texts found by the same test, unchanged** (for ROOT):
- `PP/src/validation.rs:1159`: "pressure thrust remains load-side input evidence";
- `PP/src/validation.rs:1350`: "before load-side pressure-thrust evidence can be generated";
- the MECH-TP-PHYS-008 fixture id.

## Evidence

B is main `7eae707bb7`; its B-side records are reused from round 2. The candidate is `5bc6f269da`.

**Per-test outcomes.** The changes equal, name for name, the source `#[test]` changes from B (`test_name_diff.txt`).

| Suite | B | Candidate | Changes |
|---|---|---|---|
| 40 manifests | 2776 pass / 3 fail / 80 ignored | 2755 / 3 / 80 | 57, as planned |
| src-tauri | 116 | 117 | |
| pytest | 4426 passed, 32 skipped | unchanged | |
| vitest | 4245 | 4248 | |

- Round 4's own manifest changes: +2 G11 tests, 1 `primitive_loads` rename, and 1 runner suite-test rename.
- The 3 failures are the known Mac ones at both B and candidate.

**Bytes:**

| Set | Result |
|---|---|
| E (exact) | 96/96 equal |
| F (pressure-free) | 362 equal; 2 differ only in the declared T1 string |
| B1 | 64/64 equal |
| W1 | 64/64 equal |

H-1 is unchanged from round 3.

## Notes

- **Merge with I114.** I114's demo fixtures are untouched and still carry the old T3 and T4 texts.
- **DEL-10-05 procedure.** The documented regeneration procedure now stops with `LOCAL_PRIVATE_INTENT_REQUIRED` (exit 1) unless `--explicit-local-private-intent` is given. This predates round 4; the procedure text is unchanged.
- **Worktrees.** `WT/t3-pret-hc` and `WT/t3-pret-hb` are detached at `5bc6f269da`, clean apart from the untracked harness.

Records: `RETURN.md`, `_run_records/`, `SHA256SUMS`. Placeholder paths only.
