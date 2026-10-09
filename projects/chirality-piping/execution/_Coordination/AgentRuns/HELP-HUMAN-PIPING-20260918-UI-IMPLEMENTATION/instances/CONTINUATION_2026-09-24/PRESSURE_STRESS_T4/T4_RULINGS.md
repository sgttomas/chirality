# T4 rulings: pressure, stress and section mechanics

HELP_HUMAN (Agent 0) rules here for T4. The rulings are append-only and dated.

## T4 starts (HELP_HUMAN, 2026-10-09 UTC)

**The owner's decision:** "Yes start T4". This follows the legacy pressure retirement (2026-10-08). Pressure is now analysable only under the exact contract (straight pipe, linear supports, no components, combinations or `equivalent_static`), which makes T4 the critical path for pressure on realistic piping.

**The arrangement:**
- **HELP_HUMAN:** alignment with the owner and rulings.
- **HELPS_HUMANS (design manager):** writes T4's plan for the owner's approval (`BRIEFS/HELPS_HUMANS_T4_PLAN.md`).
- **T4's WORKING_ITEMS:** commissioned to implement the approved plan.
- **Branch:** `codex/piping-t4-pressure-stress-20261009`, from main `ec5d397359` (after PR-B1 and PR-N), worktree `WT/t4`.
- **Host:** shared with T3 under the same locks.

**The owner decisions T4 inherits:**
- the legacy pressure contract and computation are retired product-wide, with 0.1.0/0.2.0 kept as the pressure-free namespace;
- M07 option A: the flawed user-stiffness element is deleted in the PR that lands T4's corrected joint, and no historical copy is kept;
- T4 rebuilds the validation removed with the retired computation, under the exact contract.

**IDs:** T4-I1… for TASKs, T4-RV1… for reviewers.

## Plan 01 received; H-1 to H-3 ruled; H-4 waits for T3 (HELP_HUMAN, 2026-10-09 UTC)

**The plan:** `PLAN_01/PLAN.md` revision 2 (sha256 `8d0635fa…`), at `7a1863a37c`. T4-RV1 blocked revision 1 on B-1 (a uniform load on an arc is `CannotBound`). Its delta check confirmed the repair, T4-U1b. Both screens passed with 0 hits on the commit before HELP_HUMAN pushed it.

**Next.** Annex A (`PLAN_01/T3_AGREEMENT.md`) has gone to T3's WORKING_ITEMS for agreement. D-1 to D-4 go to the owner after T3 answers.

**H-1: as proposed.**
- Bends and later families publish under a successor contract, `3.0.0/exact_pressure_v3`, with the reserved `pressure-1` semantics. New authoring writes v3.
- `2.0.0/exact_straight_pressure_v2` stays accepted and byte-identical, except T4-U0's declared refusal of p < 0.
- v2 is kept because it is correct and saved documents use it. This is not compatibility with flawed code, so the owner's 2026-10-08 principle does not reach it.
- SP-1 binds: a straight-only v3 case is bit-equal to its v2 twin.

**H-2: as proposed, on one condition.**
- Keep today's pre-cancelled ledger unchanged, and add member-owned terms: the bend term `K_b·u_free(ε_p) − c_b`, and the joint's `p(Ae−Ai)` at its attachments.
- JR permits either equivalent representation, provided there is one implementation owner (JR `CONTRACT.md`, "Two equivalent assembly representations are allowed"). Its selection of (A) was a design choice, not an owner decision, so reversing it lies within this authority.
- T4-RV1 derived the bend term independently and agreed with three other formulations to 1e-13 or better.
- **The condition.** JR paired its choice with an independent comparison against the other representation. That pairing now runs the other way: T4-U5's references include an independent representation-(A) comparison, alongside JR's J4 double-count control that inspects the tie force.

**H-3: as proposed.** T4-U3, the live mechanical connector (J-A and J-B), carries the deletion of the old element and its plumbing, with no historical copy (M07 option A). J-A alone has no product use, so it cannot be the PR that "lands the corrected joint".

**H-4: waits for T3's answer on the wave.**
- The intended ruling: the summary key and the historical joint row kind stay only until one corpus generation, PR-B2's re-pin wave or B7.
- In that wave the key is renamed and the row kind is **removed**, not just renamed, consistent with the owner's principle.
- Once T3's U3 merges (its G11 closure refuses every flexibility joint), no product path produces the row kind; only committed corpora and old results carry it. T4-U2a's review confirms this.

## T3 agrees annex A on conditions; H-4 ruled: B7 (HELP_HUMAN, 2026-10-09 UTC)

**T3's answer.** T3's WORKING_ITEMS answered after I115's independent check, at NUM `b1fd02ca22`, `R/I115/t4_annex_check_01/`. The check ran against main + T3's U3 and against `b2` `e582b61f9e`. All four of annex A's protective claims hold. The conditions below bind T4's implementation. They are carried into T4's WORKING_ITEMS brief, not into a revision of the plan.

**A fact the annex missed.** The seven `preview_physics::LIMITATIONS` strings are reviewed inputs: they appear verbatim in the preview-physics-1 and retained-1 semantic contracts. Changing any of them makes the registered build Stale, so it forces re-registration, not just re-pins.

**Conditions on the claims:**
- **Claim 1.** T4-U1 declares I5 §4's two changes on T3's route:
  - the ordinary envelope a refused retained call publishes;
  - whether the source attempt is reached for curved cases that K-D5 demotes today.
- **Claims 2 and 3.**
  - PP's `Cargo.lock` is unchanged.
  - The priced types keep their layouts: `preview_physics::MemberRecord`, `formation_guard::RecoveryRecord` and the `Preview*` inputs.
  - Connector fields (`ObjectiveConnectorV1`, `replaces_span`) and per-member E/ν for bends go on component types, which are not priced.
- **Claim 4.** `PP/tests/s11f_site_test.rs` is a sixth shared file. T4 re-merges its real diffs against `b2` before T4-U1 and T4-U3 land.

**The seven items:**
1. **The M31b/M31b0 mutant.** T4-U1 constructs a new kill. The required kills are SA `kd5_tests.rs:447` and PP `formation_check_runtime.rs:379` with its `:358` control; `:419` belongs to M31a. A claim of equivalence by construction needs a written derivation and an independent check, and comes to HELP_HUMAN as a narrowing.
2. **`CSKEW_8_5`.** T4-U1 runs it. T3 agrees the outcome and the re-derived dependants. After T4-U1, at least one constructible curved model must still be demoted by K-D5, or an equivalent kernel-level kill must exist.
3. **The regenerated models.** `LIMITATIONS` is unchanged. The lock and the priced layouts are unchanged. The models are regenerated by their committed generator, and the re-derived values are checked independently.
4. **The arc-load certificate.** Its design comes to T3 before any code. T15's change of meaning is accepted only through that design.
5. **W4.** The tie reduction stays. Only its producer is deleted: `user_element_tie`, `TieRefusal` and SA's `UserTie`.
6. **No joint is silently skipped.** U3's four joint-refusal tests may move to T4's codes, but every incomplete or unmapped joint stays refused. A T3 reviewer confirms this on T4-U3's diff.
7. **The wave is B7** (H-4, below).

**H-4: ruled, B7.**
- The summary-key rename, the removal of the historical joint row kind, T3's deferred `preview_physics.rs:75` wording and any other `LIMITATIONS` change all go in B7, in one wave. B7 already registers the release identity once and re-establishes the milestone's bytes.
- **Why not PR-B2.** B2/B3's plan treats any change to a c = 1 or B1 successor byte, or to a 07n outcome, as a stop. At PR-B2 the rename and the `:75` wording would each need a declared exception on the critical path.
- **Until B7:**
  - the key and row kind stay;
  - once T3's U3 merges, no product path produces the row kind.
- **In B7 the row kind is removed,** not renamed, per the owner's principle.
- **This depends only on cost and freeze timing,** not on T4 landing.
- **T4-U4's arc-frame unification on preview-physics-1** is a `LIMITATIONS` change, so it waits for B7. T4-U4's other parts do not.

## Owner decisions: T4 plan 01 approved, D-1 to D-4 as recommended; T4's WORKING_ITEMS commissioned (HELP_HUMAN, 2026-10-09 UTC)

The owner answered each question by selecting the recommended option:
- **D-1, "Approve":** the order of plan §3.1, with the L line (T4-U2) as the first usable path and the corrected joint (T4-U3) in a parallel lane.
- **D-2, "Curved bends only":**
  - Only realized bends, carrying the user's k, carry pressure.
  - Geometry-only (chord) bends are refused on the exact route with a "realize this bend" message. They stay on the pressure-free route.
- **D-3, "Leave out now":** these are excluded for now and stated as limits on every bend result and in the v3 approximation text:
  - steady-flow momentum and transient loads;
  - bend opening under pressure (Bourdon);
  - pressure stiffening of k and the SIF;
  - ovalization.

  T4-U9 adds them later only if the owner selects it.
- **D-4, "Refuse both, keep annotation":**
  - Both legacy joint populations are refused with `LEGACY_FINITE_CONNECTOR_REAUTHOR_REQUIRED`: the flexibility joints, and the app-authored joints that today solve as pipe.
  - The explicit annotation-only choice (`not_solver_consumed`) stays, and every result discloses it.
  - Nothing is converted automatically.

**Owner-held later:** D-5 (section bases), before T4-U6; D-6 (the shear default), before T4-U8.

**T4's WORKING_ITEMS is commissioned** with `BRIEFS/WORKING_ITEMS_T4.md`. HELPS_HUMANS stays T4's design partner.

## T4-U3's slot table (T4-I10): a declared SP-1 exception for D-4; the demo-envelope re-pin acknowledged (HELP_HUMAN, 2026-10-09 UTC)

**SP-1 and D-4: a declared exception, not a v2 exemption.**
- **Why an exception is needed.** Reporting `LEGACY_FINITE_CONNECTOR_REAUTHOR_REQUIRED` before `EXACT_PRESSURE_COMPOSITION_UNSUPPORTED`, and removing the old joint validation rows, changes the diagnostics of every model with an expansion joint.
- **What it covers.** The exception applies only to models containing an expansion joint, and only to:
  - (a) the refused envelopes' diagnostic codes and texts;
  - (b) 0.1.0/0.2.0 app-authored joints becoming refused;
  - (c) annotation joints' warning replaced by the disclosure.
- **What must not change.** No admitted v2 or v3 case's results change. The byte evidence takes T3's U3 form. Anything outside (a)–(c) is an SP-1 stop.

**SP-4: acknowledged.** The two refused demo envelopes (`invented_mechanics_result_preview_physics_1_{dense,sparse}.json`) and their generation manifest regenerate. They are not T3's retained pins, reader corpora or reviewed inputs. H-4 still holds.

**A residual joint shape.** A joint with no connector, no pipe ref, no rates and no annotation mode also takes the legacy code. No joint shape goes unrefused.

**D-E (T4 WORKING_ITEMS) stands.** Straight-to-straight kinks stay refused in T4-U2; T4-U7 takes them up.
