# I115 return: T4 plan 01's annex A, the claims that protect T3

TASK (Type 2) for T3's WORKING_ITEMS (Agent 1). Brief: `R/BRIEFS/T4_ANNEX_A_CHECK.md` (sha256 `bd2be7c6…`, verified). Read-only: no product change, no commit, no ref.

**Basis.**
- **Annex A:** `R4/PLAN_01/T3_AGREEMENT.md`, sha256 `159356ac…`, identical at `7a1863a37c` and at `WT/t4`'s head `ac40986957`. That later commit adds only HELP_HUMAN's H-1 to H-3 rulings to `T4_RULINGS.md`. Its context is `PLAN.md` §3.3 and §4.2, and its source `R4/T4-I5/RETURN.md`.
- **main + U3:** main `ec5d397359` with U3 `1e9724fb94`. Their composition C (tree `c64687a327`) has one conflict, U3's import line against PR-N's `correct_norm` import. U3's PR code `8a12de28db` (#1168, on main `ba500defa4`) equals C in product code except U3's later T2 string and its test, so these conclusions hold there too.
- **`b2`:** `e582b61f9e`. **RR:** `T/ROOT_RULINGS_V1.md` at NUM `ad421fbb13`.

**Citation rule.** Files U3 touched are cited `@1e9724fb94`; FK and NI, which U3 did not touch, are cited `@ec5d397359`. In C, `PP/src/lib.rs` lines after 46 are 2 higher than `@1e9724fb94`, and `@ec5d397359`'s numbering differs again.

**Method.** `git show`, `grep` and `diff`, plus one read-only `git merge-tree` simulation (§3; `_run_records/SIM_STEPS.md`). No cargo. **Inference** is marked as such.

## Verdicts

| # | Annex A's claim (for T4-U1 and T4-U3) | Verdict |
|---|---|---|
| 1 | Every retained-route and source-route output is unchanged | **Holds, with a scope condition** (§1) |
| 2 | `REVIEWED_INPUTS` is unchanged | **Holds, with conditions:** `preview_physics::LIMITATIONS` unchanged, the PP lock unchanged, and H-4 (§2) |
| 3 | `REGISTERED_PROFILES`, the priced atoms, `PINNED_RECORD` and M are unchanged, provided H-4 holds | **Holds, with conditions:** H-4, claim 2's conditions, and no layout change to a priced type in the files T4 edits (§2) |
| 4 | No textual overlap with `b2` | **Holds (indicative)** at `e582b61f9e`: both simulated merges are clean. **The shared-file list needs one addition,** `PP/tests/s11f_site_test.rs` (§3) |

## 1. Retained and source outputs

**W1 refuses components before anything specific to curves or joints runs. Confirmed.**
- The dispatch runs census and admission on the parsed request before either route (`PP/src/lib.rs:2253-2266@1e9724fb94`).
- D1.4 and D1.8 refuse any component (`PP/src/retained_memory.rs:755-756`, `:801-802@1e9724fb94`), inside `domain_clauses` (`:893-901`), which `admit` calls (`:2957-3018`). `b2` keeps both refusals (`retained_memory.rs:872-873`, `:930-931@e582b61f9e`).
- Curved and user elements are built only from `model.components`:
  - the joint builder: `lib.rs:7492-7496`;
  - the curved builder: `:7648-7651`;
  - the realized-pipe set: `:7613-7617@1e9724fb94`.

  So for an admitted model, both lists are empty.

**On the retained route, the joint and curve code calls only `assess_rigid_body`. Confirmed.**
- FK's whole retained tree imports from `rigid_body` only `assess_rigid_body`, `ObjectiveFamily` and `RigidBodyStatus` (`FK/src/structural/retained/factor.rs:50`, `:201@ec5d397359`; the same at `b2`).
- It names no curved, user, formation-check or constrained-body item.
- T4-U3 deletes `TieRefusal` and `user_element_tie` (`FK/src/rigid_body.rs:329-361@ec5d397359`). It does not touch `assess_rigid_body` (`:33-193`).
- In SA, a straight-only body calls `assess_rigid_body` only. W4's `assess_constrained_bodies` runs only for unqualified (mixed) bodies (`NI/src/structural_adapter.rs:1287-1320`, `:1493@ec5d397359`).

**Does any retained-route or source-route path reach the curved formation or the user-stiffness element? No path forms either one.** Several paths do run code that T4 edits, with empty lists:
- **Retained.** The W1 permitted run executes the observed ordinary pass (`lib.rs:2971@1e9724fb94`). That pass:
  - hands `users` and `curved` to the SA solve (`:1455-1457`);
  - forms the basis stiffness with both lists (`assemble_basis_stiffness`, `:3519`);
  - counts the summary key (`:2777-2779`).

  W1's capture then fails closed if either list is non-empty: "unsupported producer present" (`retained_product.rs:1557-1559,1570@1e9724fb94`).
- **Source.** `prepare_sources` refuses before forming anything:
  - A curved model fails first at `source_recovery.rs:526-537@1e9724fb94` ("actual model/source dimensions"), because curved spans are left out of `frame_elements` (`lib.rs:7324-7330`).
  - Any other component model fails at `:579-585`.

  The receipt replay (`source_receipt.rs:306-318`) runs only after a recovery succeeded (`lib.rs:5595-5603`), so it always assembles with empty lists. T4-U3 still edits that call site.

**The scope condition.** The claim holds for the retained successor and for the source route's own result. Three related things do change:
- **The ordinary envelope.** A retained-entry call that admission refuses publishes the ordinary envelope (`lib.rs:2263-2266`). That envelope changes as declared: U1 moves arc values at the rounding level, and U3 changes the legacy joint code.
- **The source attempt's reach.** As I5 §4 says, U1 changes whether the source attempt is reached for curved cases that K-D5 demotes today. Their `SOURCE_BLOCK_RECOVERY_UNAVAILABLE` info disappears. Annex A's summary drops this qualification; it should restate it.
- **Pass B.** It applies because the edits sit on the D1 call graph (`retained_product.rs:1558`; `lib.rs:1455`, `:2777`, `:3519`; SA; FC). Both units must preserve behaviour for empty lists. I5 inferred this; it is now confirmed.

## 2. `REVIEWED_INPUTS`, the profile and M

**T4's planned edit set.** It is 51 files with H-4 holding and 55 without, built from PLAN §3.3 and §6, I5 §1 and I3 §1.2 (`_run_records/t4simA.txt`, `t4simB.txt`):
- **Production:** CB `lib.rs`; FK `lib.rs`, `rigid_body.rs`, `structural.rs`, `structural/formation_check.rs`, `structural/sparse.rs`; NI `lib.rs` and `structural_adapter.rs`; PP:
  - `lib.rs`, `preview_physics.rs`, `validation.rs`;
  - `retained_product.rs`, `source_recovery.rs`, `source_receipt.rs`, `source_receipt/source.rs`;
  - `formation_guard.rs`.
- **Elsewhere:** the headless runner's `lib.rs` and `result_envelope_binding.rs`; the benchmarks (mechanics and nonlinear) and the performance harness's `k6/staged.rs`; the TS `previewService.ts`, `ReportPanel.tsx` and `componentIntent.ts`.
- **Tests:** CB, FK, NI, SD, PP, the runner and RE, as I5 §1 and I3 §1.2 list them, with `kd5_models.rs` regenerated.
- **Docs:** two READMEs.
- **Only if H-4 is reversed:** `retained_product_tests.rs`, RE `retained_precision.rs`, `retainedPrecision.ts` and `analysis_runs/retained_precision.py`.

**None of these files is a reviewed input.**
- `REVIEWED_INPUTS` has 14 entries on main and at U3 (`PP/src/build_identity.rs:148-163`) and 17 at `b2` (`:149-170`).
- The entries are the PP lock, schemas and `fixtures/results` JSON. T4's set contains none of those.

**The claim's conditions.**
- **`LIMITATIONS` must stay unchanged.** Its seven strings appear verbatim in two reviewed inputs, `semantic_contract_v0_3_preview_physics_1.json` and `semantic_contract_v0_3_preview_physics_retained_1.json` (`supported_profile_limitations`, lines 1243–1249).
  - A change to `LIMITATIONS` therefore changes the reviewed-input text. The build becomes Stale and must be re-registered, not only re-pinned.
  - **This applies equally to the deferred `preview_physics.rs:75` wording and to T4-U4's frame unification for arcs.**
  - Annex A item 4 and H-4 describe that radius only as corpus pins (20 files at U3, 22 at `b2`; 24 after J0b, `_run_records/COUNTS.md`).
- **The PP `Cargo.lock` must not change.** It records the path crates and their dependency edges, for example CB and NI. Adding or removing a crate dependency, or bumping a crate version, anywhere in PP's graph changes it.
- **H-4 must hold.** The joint row kind is in all 10 of `b2`'s reviewed semantic contracts: the 9 on main plus `physics_retained_1`.

**What H-4 protects.**
- `MechanicsEnvelope` holds `Summary` by value (`lib.rs:832@1e9724fb94`). `Summary` is ten fields, all 8-byte aligned, including `component_user_stiffness_macro_element_count: usize` (`:1954-1965`).
- `s(MechanicsEnvelope)` is a priced atom (`retained_memory.rs:1746`).
- **Removing the field** would shrink the atom by 8 B and move every phase that prices an envelope. That re-pins `PINNED_RECORD` (`retained_memory_law_tests.rs:1203-1206` in C, `:1194-1197@1e9724fb94`; asserted at `:1191-1194` in C) and the challenge literals `W1_PHASE_BYTES` and `MAX_PHASE_BYTES` (`tests/retained_memory_challenge.rs`, checked at `:1216-1225` in C).
  - The code's rule (`:1182-1186` in C) is to regenerate the record together with the profile.
  - U3's precedent, a 800 B re-pin, was accepted conditional on Pass B, T9 and the both-entry gate (RR:16494-16496).
- **A rename that keeps the field** leaves the atom unchanged. It still re-pins 93 files' bytes after J0b.
- **Removing the row kind** changes the reviewed-input text: Stale, then re-registration.
- **M does not move** on a decrease (`threshold_bytes` 11,274,289,152, `retained_memory.rs:972-992`).
- **`REGISTERED_PROFILES` holds no atom values:** only the identity, the reviewed-input text, four reader layouts and M.

**The priced-layout condition (claim 3).**
- I5's statement holds: no priced atom holds a curved element, a user element or `BuiltModel` by value. But T4 edits files that define priced types:
  - `preview_physics::MemberRecord` (`preview_physics.rs:221`; T4-U3 edits `:106-211`);
  - `formation_guard::RecoveryRecord` (`formation_guard.rs:334`; T4-U3 edits `:83`, and T4-U1b reworks the arc bound there).
- The input types `PreviewPipe`, `PreviewNode`, `PreviewSupport`, `PreviewLoadCase` and `PreviewPrimitiveLoad` are priced; the component input types are not.
- So T4-U3's connector fields (`ObjectiveConnectorV1`, `replaces_span`) and any per-member E/ν for bends must sit on component types, or on types outside the atom list. Otherwise `PINNED_RECORD` moves even with H-4. I3 §1.3 item 8 already flags `PreviewLoadCase` for T4-U5.

## 3. `b2`: the simulated merge (indicative only; T4 has no code)

**The setup** (`_run_records/SIM_STEPS.md`):
- T4's planned edit set is applied to C as edits of every cited site and every curve or joint line: 5,298 lines in 51 files.
- It is merged against B2U = `b2` `e582b61f9e` + U3 (the J0b state), with C as the merge base.
- It is also merged directly against `e582b61f9e` (with history).

**Results:**
- **Variant A (H-4 holds):** exit 0, no conflict. The six shared files are:

  | File | Nearest gap |
  |---|---|
  | `previewService.ts` | 208 lines |
  | PP `lib.rs` (T4 253 hunks, `b2` 13) | 66 lines |
  | `retained_product.rs` | **5.5 lines** (`b2`'s insertion after C:1552; T4 at C:1558-1559) |
  | `PP/tests/s11f_site_test.rs` | **5.5 lines** (`b2`'s row after C:543; T4's re-listed `PP/lib.rs` block at C:506-538) |
  | the RE contract test | 222 lines |
  | FK `structural.rs` | 18 lines |

  The result differs from B2U only by T4's 5,298 marker lines. The direct merge with `e582b61f9e` gives the identical tree.
- **Variant B (H-4 reversed):** exit 0. It adds `retained_product_tests.rs`, RE `retained_precision.rs`, `retainedPrecision.ts` and `retained_precision.py`, all clean.

**Change from I5's basis.** `s11f_site_test.rs` is new: `e582b61f9e` (J0a's last commit) adds a `combination_call` row there. Annex A's list should name it. The two 5-line margins are the places where T4's real hunks could touch `b2`'s.

## 4. Facts for annex A's items 1, 2 and 7

### Item 1: M31b and M31b0

**RR's rulings.**
- "K-D5 mutation M31b: equivalence withdrawn" (RR:689-706) supersedes the earlier acceptance (RR:526-560).
- **The mutant.** K-D5's intended element takes H from the product's formula chord R(cos φ − 1, R sin φ, 0) (binary64 R, atan2, cos, sin) instead of the actual node chord xⱼ − xᵢ. M31b0 is the same formula evaluated at p.
- **What the kill protects.** K-D5 must see the first-order translation error θ·δc that a chord inconsistency produces on the stiff rows.
  - With M31b, admissible models (radius mismatch ≤ 1e-9, well conditioned) publish **Passed with actual error 1.10–6.48 of the criterion**: CANT60_PLANAR, CANT30_SKEW, CANT10_SKEW and PP_UTM at X 5e6.
  - That is condition (a), a silently wrong Passed (RR:693-701).
- **The required tests** (RR:702-705). They are test-only; the implementation already uses the actual chord.
  - SA `kd5_tests.rs:447`: CPLANAR_60 and CSKEW_30_N122, both modes. Each patch fails a behavioural assertion.
  - PP `tests/formation_check_runtime.rs:379`: X 5e6, φ 5°, R 0.3; SENSITIVE, which M31b turns into CHECKS_PASSED.
  - Its control at `:358`: PP_UTM, X 5e5, not demoted, error below half the criterion.
- **SA `:419` is a different requirement.** It is the superseded ruling's condition 1 (RR:542-547): the actual-chord test and M31a's kill (M31a is the whole-matrix form). Annex A lists it among "M31b's kills". Its premise (the centre moved 6.5e-10·R) also disappears with U1.
- **Inference.** Once the product forms H from d with no absolute centre, M31b's chord error falls to rounding on objective inputs. M31b is then probably equivalent by construction, or a false demotion as I2 §1.7 says. Either disposition needs a written derivation and an independent check (RR:1217, the M31b lesson).

### Item 2: `CSKEW_8_5`

**What depends on it.**
- The definition: `NI/…/kd5_models.rs:85`, a generated model with a binary64 centre.
- **SA `kd5_tests.rs:400-416`:** K-D5's only curved true positive whose premise survives U1. It asserts Passed, actual > 1.0, demotion in both modes, and EF/actual within 1e-3.
- **NI `k1_tests.rs:336-360`:** dense/sparse parity of the demotion. F122, a straight model, is the other demoting case.
- **NI `k1_tests.rs:1313`:** RV8-3, the sparse check reading the ledger terms (kills RV8-FC-TERMS), together with F122.
- **NI `k2b_tests.rs:1313`:** carries it with no demotion assertion.
- **Corpora:** `k1_tests.rs:191`, `k2b_tests.rs:47` and `k5_tests.rs:299`.
- **Evidence:** R5_4's table (`DESIGN_NUMERICS/R5_4_CURVED.md:100-115`): k_X = 8.5, cond 6.4e7, actual 1.481 dense and 1.096 sparse.

**If it stops demoting after U1:**
- `:400` and the curved halves of `:336` and `:1313` fail their premise. Every other required curved demotion (`:419`, `:447`, PP `:379`) is already lost to U1.
- Nothing would then assert that K-D5 ever demotes a curved model.
- Whether F122 alone still kills RV8-FC-TERMS is not established by reading.

### Item 7: where H-4's renames go

**The radius after J0b** (`COUNTS.md`):
- **The key:** 93 files, including 10 successor pins and 07n (26 occurrences).
- **The row kind:** 10 reviewed semantic contracts, plus the reader classification sites (RE `retained_precision.rs:2654`, TS `retainedPrecision.ts:125`, PY `retained_precision.py:1188@e582b61f9e`) and a few product-preview and export fixtures. It appears in no successor pin and not in 07n.
- **The `:75` wording:** 24 files, including the same two reviewed inputs.

**At PR-B2.**
- B2/B3's own plan makes it a stop to change any c = 1 or B1 multi-case successor byte, and any 07n outcome (I93 `PLAN.md:601-602`; `REVISION_01.md:116`).
- `b2` re-pins no existing corpus. Against main it adds 10 fixtures and modifies one, the reviewed `semantic_contract_v0_3_preview_physics_retained_1.json`.
- So **the key rename and `:75` are not cheap at PR-B2.** They need ROOT to make a declared exception to PR-B2's own stop rules.
- They also need the extended mechanical check (RR, "U3, T2's re-pin check, option (a)"). The successor and source carriers bind their bytes by digest, so a string-only edit cannot hold. That check runs across 93 and 24 files, on PR-B2's critical path (206–329 agent-hours, WG:585).
- **The row-kind removal is cheap there only if it lands before the statics freeze.** SQ2's single `registration.diff` re-derives `reviewed_inputs` from the frozen statics at J7 (`REVISION_01.md:130-133`). After the freeze it costs a second registration.

**At B7.** "The release identity, registered once, with the milestone's bytes and verdicts re-established on it" (RR:11882; WG:586).
- All three ride a generation and a registration that happen anyway. The marginal cost is the edits plus the extended check.
- **The deferral cost:** the misleading key and the `:75` text stay published until B7, and any T4 fixture created in between carries the key into B7's radius.
- **Inference:** B7 is the cheaper single wave. Splitting the row-kind removal into PR-B2 before J7 is cheap but makes two waves.

## 5. Concerns

1. **`LIMITATIONS` and the `:75` wording are reviewed inputs.** Annex A item 4, H-4 and RR:16518 count their radius as pins only. A change re-registers.
2. **K-D5's curved true positives after U1.**
   - U1 removes the premises of SA `:419` and `:447` and of PP `:379`, and `CSKEW_8_5` is undetermined.
   - T3's disposition of M31b and M31b0 should therefore also secure M31a's kill. It should require at least one constructible curved demotion, or an equivalent kernel-level kill, before U1 merges. Otherwise a mutant that never demotes curved models survives.
3. **Shared files.** `s11f_site_test.rs` joins them. Two shared files have a 5-line margin, so T4's real diffs should be re-merged against `b2` before T4-U1 and T4-U3 land.
4. **Priced types in T4's files** (§2), and connector or bend fields kept off the priced input types.
5. **The source-route qualification** (§1) should be restated in annex A.
6. **H-4's "removed, not just renamed".** The retained readers never meet the joint row: admission refuses components, and it is absent from every successor and from 07n. Removing it from the reader tables is therefore safe for successors. For other historical readers it is a design point for T3 and T4.

## 6. Evidence and host notes

- **`_run_records/`:**
  - `SIM_STEPS.md`, `t4sim.py`, `t4simA.txt` and `t4simB.txt`;
  - `merge_A_messages.txt` and `merge_B_messages.txt`;
  - `shared_files.txt` and `margins_A.txt`;
  - `trees.txt` and `sim_commits.txt`;
  - `COUNTS.md`.
- **Git writes:** loose objects only. These are the merge-tree trees, the blobs and trees from `hash-object` and `write-tree` through a scratch index, and two dangling commits from `commit-tree` (`df429ead71`, `100a71a1fe`) for the direct merge. No refs and no worktree index were written.
- **Deviations:**
  - Scratch was in the session's scratch directory, not `WT/scratch/I115_t4_annex_check/`.
  - One file was briefly written to the system temp directory and deleted at once.
  - No cargo or heavy job ran.
