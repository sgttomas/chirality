# I111: M07's user-stiffness joint premise, the five questions

The host refused this file's write, first by I111 and then by WORKING_ITEMS ("Subagents should return findings as text, not write report files"). ROOT wrote it from the text WORKING_ITEMS returned. The evidence is `evidence.json` (31 entries; the ids below), `_run_records/` and SHA256SUMS. The basis is NUM `9cd61ba201`, read only. WORKING_ITEMS spot-checked three citations:
- FK `user_stiffness_local_matrix` at `frame_kernel/src/lib.rs:1739-1758`;
- the `#[cfg(test)]` scope at `PP lib.rs:105-106`;
- the bypass at `preview_physics.rs:111-115`.

## 1. The flaw

- **The element.** FK `user_stiffness_local_matrix` is six uncoupled endpoint-difference springs, made by six `add_relative_dof_stiffness` calls (UX, UY, UZ, RX, RY, RZ). It has no lateral-to-rotation coupling and no length term (F1).
- **The parallel pipe.** PP also keeps the joint's own pipe as a full frame element in parallel (F4). JR `CONTRACT.md:7` names both defects.
- **A rigid rotation.** On C-150 (L = 2.2 m), a 1e-3 rad rigid rotation gives ∓1980 N instead of 0. With the lateral stiffness at 0 the result is exactly 0 (F5, from an exact transcription in `local_check.py`). The FK probe binary did not run, because it was queued behind DEC-025.
- **A relative lateral δ.** It gives the couple kδL = 658.4368 N·m at L-100's δ. The independent 2026-09-08 record gives 658.4367607905 (F6, F7).
- **The cited figures.** The cited 658.44 is right. The written factorization 900000 × 3.3254e-4 × 2.2 gives 658.43 (F8).

## 2. Reachability

- **Compiled but not assembled.** The element is compiled into every PP build, and FK and NI expose it publicly, but no product path assembles it.
- **The solve gate.** Every public solve entry, ordinary and retained (including `prepare_observed`), calls `refuse_unqualified_joint_elements` before the build. The builder's success conditions imply the refusal fires (G1–G4). It is the only gate on the solve path (G7).
- **The exact contract.** It refuses every component earlier (G5), so the joint refusal matters only for 0.1.0, 0.2.0 and 0.3.0-legacy documents.
- **The bypass** exists only in `cfg(test)` (G6).
- **Other consumers:**
  - desktop native and the runner use PP's public entries (G8);
  - neither WASM engine builds the element, but the authoring UI and the WASM op engine can author a joint whose solve is refused (G9);
  - the readers read rows only.
- **G10.** The browser app's reference-only view shows bundled precision-1 demo results computed with this joint (`previewService.ts:639-646`). The same fixtures are in I110's inventory.
- **G11 (by reading, not run).** A joint with no lateral value passes the refusal and is silently skipped by the builder. Its review rows still say "consumed by the assembled user-stiffness macro-element" (PP `lib.rs:12368-12460`).

## 3. The oracles

Four tests run C-150 in the scope, and no other scope call carries a joint (O5).
- **M07 only:**
  - O1, `current_composite_derived_normal_friction_and_reversal` (`lib.rs:14915-15125`);
  - O3's second half (`lib.rs:18514-18593`). Its first half is a valid refusal test and is kept.
- **Pressure and M07:** O2 (`…nonlinear_support_loop_evidence_historical_pressure_premise`) and O4 (`…pressure_thrust…historical_pressure_premise`). The pressure retirement removes both under every option.
- **What O1 and O2 pin:** numbers of the flawed model, calibrated from product observations (O6). C-150 moves the friction normal from 52.37 N to 40.91 N in the independent record.
- **What still holds:** their law checks (Coulomb μN, the slip sign, stop release, DEC-067's counts) hold whatever the joint does, and joint-free tests cover the friction law (O7). Only O1 covers the three-way reversal with stop release.

## 4. What T4 needs

- **T4's inputs:** the JR package and `ANALYTICAL_ORACLES_V1.json`'s connector oracles. These are records, and no option touches them (T1, T2).
- **The corrected element** has a different form: B, Ke = BᵀKB, offsets, Q, a 21-entry H, and a replaced span. Nothing in F1 carries over, and legacy finite-span joints must be re-authored.
- **Removing the oracles** loses nothing T4 needs.
- **Removing the element** loses three things:
  - the T4 tripwire `k5_t4_tripwire_user_tie_space_is_the_represented_null_space`;
  - the reviewed slot plumbing: dense and sparse assembly, the K2b census, the K-D5 re-formation, the W4 tie, the W2 admission, and the NI adapter;
  - JR J-A's plan to keep the old element "for historical witnesses only", which the owner's 2026-10-08 principle may supersede.

## 5. The options

- **(a)** Delete `historical_pressure_reference.rs`. In PP `lib.rs`, remove the mod (105–106), O1, O3's second half and the comments, and remove the bypass (`preview_physics.rs:111-115`).
  - The scope tests at 15127 and 15152, O2 and O4 are already in I110's removal.
  - Inside the pressure PR this is under an hour of extra work and removes 2 M07-only tests.
  - Optionally, re-author O1's reversal on the joint-free demo against a new independent reference.
- **(b)** Also remove the element.
  - That is about 26 files and 247 lines (FK 8, NI 7, sparse_direct, performance_harness, the nonlinear benchmark, PP 8), plus about 27 test call sites in about 12 files, including NI's 4 friction tests and the T4 tripwire.
  - It needs a new refusal for every realized flexibility joint, which JR assigns to T4/J-B (`LEGACY_FINITE_CONNECTOR_REAUTHOR_REQUIRED`).
  - It changes solver crates, so it needs the full gate set as its own PR: 1–2 days.
- **(c)** Leave it until T4.
  - The pressure PR keeps an M07-only scope: trim `run()`'s pressure asserts and keep the bypass.
  - O1 and O3 survive only if Q1 keeps 0.1.0 documents accepted, and T4 deletes them later anyway.

**I111 recommends (a), inside the pressure PR.** The oracles pin numbers from a model out of moment balance by 658 N·m and protect nothing T4 needs. Option (b) would pre-empt T4/J-B's refusal design for code that no product path reaches.
