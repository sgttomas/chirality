# T4 plan 01, annex A: what T4 changes on T3's side

**For:** T3's WORKING_ITEMS, through HELP_HUMAN, for agreement before the owner sees the plan.

**Who:** HELPS_HUMANS (T4), 2026-10-09 UTC.

**Plan:** `R4/PLAN_01/PLAN.md` §3.3. Unit names are T4's: T4-U1 is the curved element's objective formation, T4-U1b the formation certificate for arc load vectors, and T4-U3 T4's corrected-joint PR. "T3's U3" is T3's pressure retirement.

**Source:** `R4/T4-I5/RETURN.md`, which cites `path:line@commit` for each item.

This section is from T4-I5. Its basis is main plus T3's U3, and `b2` at `9f5cfbcd75`.

**What does not change.** Neither T4-U1 nor T4-U3 changes:
- any output of the retained route or the source route;
- `REVIEWED_INPUTS` (14 entries at T3's U3, 17 at `b2`; no file either unit edits is among them);
- `REGISTERED_PROFILES`, any priced atom, `PINNED_RECORD` or M, provided H-4 holds. Without H-4, removing the summary key would shrink `s(MechanicsEnvelope)` and re-pin `PINNED_RECORD`.

W1 refuses any model with components before anything specific to curves or joints runs, and calls only `assess_rigid_body` (I5 §3–4). Pass B still applies to both units, because they edit files on the D1 call graph.

**`b2` and its lanes.** No textual overlap: the simulated merges are clean. The shared files are PP `lib.rs`, `retained_product.rs` and `retained_product_tests.rs`, the RE contract test, `previewService.ts` and FK `structural.rs`; their hunks are disjoint (I5 §5).

**T4-U1: T3 decides.**
1. **The M31b/M31b0 mutant.**
   - Two of its required kills become impossible to construct: SA `kd5_tests.rs:419` and `:447`.
   - A third, PP `tests/formation_check_runtime.rs:379`, fails by design. Its precondition `actual > 1.0` no longer holds, and it becomes a UTM control for C2.
   - T3 rules the mutant's disposition: a new kill, or equivalence by construction.
2. **`CSKEW_8_5`.** Whether it still demotes cannot be settled by reading. SA `kd5_tests.rs:400` and NI `k1_tests.rs:336` and `:1313` depend on it. T4-U1's reference work runs it, and T3 agrees the outcome.
3. **Regenerated or mechanical changes:**
   - `kd5_models.rs` (7 bend models) and its generator are regenerated, with `u_int` re-derived;
   - the k1, k2b and k5 model sets lose 3 models;
   - FK `formation_check_tests.rs:69` and `:276` are re-derived;
   - the S11 site tables are re-listed where accumulations change;
   - 21 constructor call sites in 9 files change.
4. **No committed corpus pin changes,** provided T4-U1 leaves `preview_physics::LIMITATIONS` unchanged. A change there reaches T3's whole corpus radius: 20 files at T3's U3 and 22 at `b2`. For the same reason, T4-U4's frame unification for arcs on preview-physics-1 waits for T3's corpus generation (H-4).

**T4-U1b: T3 decides.** T3 agrees the certificate design before any code. S11-G's T15 (`s11g_tests.rs:1747`) then changes meaning: a certified arc load stops being `CannotBound`.

**T4-U3: T3 decides.**
1. **The W4 tie reduction. Recommended: keep it, and delete only its producer:** `user_element_tie`, `TieRefusal` and SA's `UserTie`.
   - The reduction is correct, general machinery. T7's rigid links and any later ideal ties are natural future producers.
   - Deleting it would re-derive most of FK's K5 suite. Ties appear in 961 of 1,000 `b1_sample` records, 23 of 29 `cases` and 222 of 301 `subnormal`, plus `k5_scale.rs`'s chain of 10,000 ties.
   - Keeping it changes only:
     - K5-C (`k5_constrained_bodies.rs:943`);
     - the T4 tripwire (`:992`), which fires by design;
     - B10's name list;
     - NI's joint cases.
2. **Tests deleted or rewritten:**
   - NI `k5_tests.rs:937` and `kd5_tests.rs:631` are deleted;
   - the joint cases in NI k5 (`:506`, `:1106`, `:1225`) are dropped;
   - in FK: the user half of `formation_check_tests.rs:69`; `k2b_force_scaling`; the sparse tests; `k1_k2a_interaction`; one `s11_site_table` row;
   - PP `f1b_tests.rs:2227` (the family name) and `s11g_tests.rs:2605` (the assembler API) are rewritten;
   - the four joint-refusal tests that T3's U3 added (`lib.rs:17391`, `:17407`, `:17469`, `:17541`) are re-pinned to the legacy code.
3. **Pins.** With H-4, none of T3's corpora change. The refusal-code re-pins lie outside them: the headless runner's envelope-binding and admission tests, the result-export contract test, and two cases of `result_export_v0_2.json`.
4. **Texts.** NI's assumption and limitation strings and SA's M03 mixed-family text are corrected under the published-text rule. No fixture pins them at `b2`.

## What T4 asks T3 to agree

1. **T4-U1.** The disposition of the M31b/M31b0 mutant: a new kill, or equivalence by construction.
2. **T4-U1.** Running `CSKEW_8_5` in T4-U1's reference work, and the outcome for SA `kd5_tests.rs:400` and NI `k1_tests.rs:336` and `:1313`.
3. **T4-U1.** The regenerated and re-derived tests of item 3, and the condition that `preview_physics::LIMITATIONS` stays unchanged.
4. **T4-U1b.** The certificate design for arc load vectors, before code, and the change of meaning of S11-G's T15.
5. **T4-U3.** Keep the W4 tie reduction and delete only its producer (recommended), or delete the reduction and regenerate the K5 suite.
6. **T4-U3.** The deleted and rewritten tests of item 2.
7. **H-4.** The summary-key rename and the row-kind disposition, together with the `preview_physics.rs:75` wording and any other `LIMITATIONS` change, go in PR-B2's re-pin wave if T3 judges it cheap there, otherwise in B7.
