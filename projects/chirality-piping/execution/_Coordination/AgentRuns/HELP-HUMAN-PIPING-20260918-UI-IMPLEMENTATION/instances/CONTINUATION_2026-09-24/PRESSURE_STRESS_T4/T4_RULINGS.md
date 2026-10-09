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
