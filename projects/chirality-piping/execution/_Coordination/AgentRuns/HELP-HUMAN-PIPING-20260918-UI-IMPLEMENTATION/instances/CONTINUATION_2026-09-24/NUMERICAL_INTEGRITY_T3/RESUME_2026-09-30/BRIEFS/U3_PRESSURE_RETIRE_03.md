# I110, round 3: Stage 1's repairs and Stage 2 (the legacy computation and the historical scope removed)

TASK (Type 2), continued by WORKING_ITEMS for T3 (Agent 1), your return path. `R/BRIEFS/B1_COMMON.md`'s rules apply, with WORKING_ITEMS in ROOT's place. Production code: working, tested code on the branch, with a short record.

## The basis

- **RV127's review of Stage 1:** `R/REVIEW_RV127/u3_stage1_01/REVIEW.md` (`335df8b2…`). Its verdict is FAIL on B-1 only.
- **The owner's M07 decision:** RR "Owner decision: M07's flawed joint element, option A; U3 Stage 2 released". Stage 2 is released.
- **Your plan:** `R/I110/pressure_retire_01/RETURN.md` §5 Stage 2.
- **The branch:** `codex/piping-t3-pressure-retire-20261008` (`WT/t3-pret`), at `4c0d5d7c00`. Stage 1 and Stage 2 go as one PR.
- **A parallel lane:** I114 owns the demo fixtures on its own branch from `4c0d5d7c00`. That covers G10/D-3 (`invented_mechanics_result.json`, the precision-1 pair and the preview-physics-1 pair, with their consumers) and RV127's S-1, the nonzero legacy primitive's refusal text at `PP/src/pressure_runtime.rs:226-228`.
  - Do not edit those fixtures, those consumers, or those lines.
  - Leave `invented_preview_model.json` (the refused demo model) and the PP test fixtures as they are, except for deleting O1–O4.

## The task

1. **Stage 1's repairs (RV127):**
   - **B-1:** restore the thermal half of `endpoint_section_cut_fixed_and_free_pressure_thermal_match_uniform_stations_historical_pressure_premise` as a pressure-free test. RV127's probe passes on the head with no re-pin: fixed −24 MPa, free about 0. Correct the "each pressure-only" claim in your record.
   - **N-5:** the panel decides "retired" from the label alone, so a model that still carries legacy primitives is mislabelled. Make it say so.
   - **N-6:** pin the zero-primitive refusal on the retained and CLI routes.
   - **N-7:** the two pre-existing texts at `pressure_runtime.rs:117-120` and `:131-137` name the exact contract.
2. **Stage 2, as the owner released it:**
   - **Delete:**
     - `historical_pressure_reference.rs` and its `mod`;
     - the joint bypass (`PP/src/preview_physics.rs:111-115`);
     - O1, and O3's second half (O3's first half, a valid refusal test, stays);
     - O2 and O4;
     - the scope's pressure bypass, `historical_pressure_preview`, and the scope part of `private_historical_pressure_scope_restores_public_refusal_and_rejects_exact`.
   - **Then delete the legacy pressure computation as you planned:**
     - PP's thrust types, builders and assembly, the bend radial thrust, the joint thrust review rows and `EXPANSION_JOINT_PRESSURE_THRUST_APPLIED`, `pressure_for_pipe`, the hoop and longitudinal rows, `include_pressure_longitudinal`, the W2 `pressure_thrust_load` family, and `recover_section_stress`'s `pressure` parameter;
     - the always-empty plumbing in `source_recovery.rs`, `source_receipt.rs` and `retained_product.rs`;
     - the `stress_recovery` membrane and `PressureBasis`;
     - `curved_bend`'s radial-pressure API;
     - `STRESS-PRESSURE-MEMBRANE-ORIGINAL`: its benchmark, runner binding, hand calculation and manual page (RV127 N-1).
   - **Keep** what your plan keeps (§5 Stage 2 item 3).
   - **H-1 (signed zero):** prove with the byte evidence that no −0.0 is published where +0.0 was. Keep an explicit `+ 0.0` where it is needed.
   - **N-4:** the source-block namespace gate (`PP/src/source_recovery.rs:604-608`) is now unreachable. Remove it, or pin it.
   - **Not now:** the joint element's code (FK `user_stiffness_local_matrix` and its plumbing). T4 deletes it. Keep no historical copy of the old element anywhere.
3. **G11** (I111): a joint with no lateral value passes the refusal and is skipped silently, while its review rows say "consumed" (`PP/src/lib.rs:12368-12460`).
   - **First confirm the defect with a failing test.**
   - Then refuse such a joint, with the existing joint refusal or a precise one, and a test.
4. **The evidence, against main `7eae707bb7`, as in round 2:**
   - per-test outcomes over the 40 manifests, src-tauri, pytest and vitest. List every change; an unplanned change is a stop;
   - byte-equal envelopes and RE exports for the 48 exact documents and the 182 implicit pressure-free documents, plus B1's 32 documents with W1 (H-1 included).

**Stop and return** if a deletion changes an exact or pressure-free byte, or needs anything held by T4.

## Records and return

Commit in reviewable steps, product files only. WORKING_ITEMS pushes and merges I114's lane. Records go in `R/I110/pressure_retire_03/` (RETURN.md, `_run_records/`, SHA256SUMS), placeholder paths only. If the host refuses a file, put its content in your final message.

End your turn with:
- the head and commits;
- the outcome diff;
- the byte evidence, including H-1;
- G11's confirming test;
- any stop.
