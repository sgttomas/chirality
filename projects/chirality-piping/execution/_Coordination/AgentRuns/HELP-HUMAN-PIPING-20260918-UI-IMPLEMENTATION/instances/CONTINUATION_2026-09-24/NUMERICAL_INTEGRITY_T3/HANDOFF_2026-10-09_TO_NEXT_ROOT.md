# Handoff to the next ROOT session, T3 and T4 (ephemeral, 2026-10-09)

This note is for the owner's next session only. It is not a standing record and is not maintained after use. Durable facts live in the records it points to.

## The arrangement

- **ROOT (HELP_HUMAN, Agent 0)** runs T3 under the owner's standing delegation and coordinates T4. It rules, keeps alignment with the owner, and forwards returns. It does not implement.
- **T3's WORKING_ITEMS (Agent 1)** owns T3's implementation and integration. Its brief is `R/BRIEFS/WORKING_ITEMS_T3.md`; the U1 to U4 state in it is historical.
- **T4's WORKING_ITEMS (Agent 1)** implements T4 plan 01. Its brief is `R4/BRIEFS/WORKING_ITEMS_T4.md`.
- **T4's HELPS_HUMANS** is the design partner, re-engaged only when the design changes.
- **None of this session's agents can be resumed.** Every agent id in the briefs and logs is dead.
  - Commission a fresh T3 WORKING_ITEMS and a fresh T4 WORKING_ITEMS from their briefs. Each resumes from its log's "resume here" block.
  - Returns from agents a WORKING_ITEMS starts arrive at ROOT. ROOT forwards each one to the right manager and does no work on it.

**Placeholders.** T is this folder. R is `T/RESUME_2026-09-30`, and RR is `T/ROOT_RULINGS_V1.md`. R4 is `…/CONTINUATION_2026-09-24/PRESSURE_STRESS_T4`.

## Where the state is

- **The work graph** is `execution/_Coordination/WorkGraphs/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/WORK_GRAPH.md`. It has:
  - the T4 row, now ACTIVE with plan 01 approved;
  - "T3 current route", kept by T3's WORKING_ITEMS;
  - "Owner decisions in force", which includes the 2026-10-09 T4 decisions.
- **The T3 log:** `T/WORKING_ITEMS_LOG.md`.
- **T3's rulings:** RR, append-only. The newest sections are 2026-10-09's:
  - T4 starts;
  - U3's T2 outcome;
  - annex A's agreement, with the `:75` wording moved to B7;
  - #1168's A2-B-1;
  - U5's Q1–Q3.
- **T4:**
  - the plan: `R4/PLAN_01/PLAN.md` (revision 2) and annex A;
  - the rulings: `R4/T4_RULINGS.md`. These hold the owner's D-1 to D-4, H-1 to H-4 with H-4 = B7, T3's conditions, the SP-1 exception for D-4, R-1 and R-2, small bends, annotation joints, and the note for D-6;
  - the log: `R4/WORKING_ITEMS_LOG.md`.
- **Branches.** NUM is `codex/piping-numerical-integrity-20260926`, and T4's branch is `codex/piping-t4-pressure-stress-20261009`. Both are pushed.

## In flight at handoff

**The heads.** NUM is at `89a58fe597`, and the T4 branch at `b9dc7c784f`, both pushed. Every T4 agent has returned, and its records are committed: T4-RV2, T4-RV5 and T4-I10's revision 01 were committed by ROOT after T4's WORKING_ITEMS stopped, with log lines placed before its resume block. Where the WORKING_ITEMS addenda list them as running, the log lines are right. Each manager's log ends with a "resume here" block giving the head, branch, worktree, running jobs, output locations and next step for each item. The next IDs are I117 and RV132 for T3, and T4-I13 and T4-RV6 for T4.

**T3:**
- **#1168, the legacy pressure retirement. Not merged; the head is `37724dea27`.**
  - Passed: CI; the full-SHA dispatch 37878270521 (target_base `ba500defa4`); source equality, citations and GEN-8; RV127 (after the A2-B-1 repair), RV128 and I112's T9 and both-entry gate.
  - **Pass B is not done.** I107 never returned, and its partial tools are in `R/I107/u3_passb_01/`. A fresh Pass B by `BRIEFS/U3_SB.md` is next, then RV124's confirmation.
  - **DEC-025** (the chain `U3_37724dea27`) was still running at handoff: the sweep exited 0 at 03:46Z and the suites finished at 04:00Z. Check that `WT/scratch/u9_dec025/U3_37724dea27/meta.txt` ends with ALL-DONE and that src-tauri ran on the head and on main (`WT/scratch/prb1_merge/dec_chain_U3_37724dea27.txt`). Then run cmp_cargo.
  - Main moved to `2759c0f1a1` (App v4). Before the merge, confirm that nothing since `ba500defa4` touches `projects/chirality-piping/`.
  - Then the merge record, `gh pr merge 1168 --merge --match-head-commit 37724dea27a782ad4b889a5e06f8c0e91e2a67ce`, NUM absorbing main, and telling T4.
- **J0b.** It is in `WT/b2-j0b` on `codex/piping-t3-b2-j0b-20261009` at `b446fb0cd6`, unpushed: #1168's head merged into `b2`, plus one arity-test fix. I105's checks are unfinished. A fresh TASK finishes `BRIEFS/B2_J0B.md` items 2–4 and merges main after #1168. Then come Linux CI and an independent confirmation, and `b2` fast-forwards.
- **B2's readers.** `BRIEFS/B2_READERS.md` is ready to dispatch after J0b: three fresh lanes plus RV-R2. Then 07o, the J7 freeze, SQ2 (its brief is not yet written), SG2/SB2/SK2, RV-X2 and PR-B2.
- **U5, the governance documents.** It is in `WT/u5-docs` on `codex/piping-t3-u5-governance-docs-20261009` at `f995add7c6`, unpushed, with Q1–Q3 ruled. After #1168: merge main, rerun GEN-8 and the light harness, push and open the PR. Then an independent reviewer on the actual head, CI and the merge.
- **After U3:** O1's friction-reversal re-author (A1-N-3), and a records PR carrying RR.

**T4** (plan 01; all code waits for #1168):
- **T4-U0 and T4-U1.**
  - The references are in `T4-I6/`. T4-RV2 passed them with findings: 0 blocking and S-1 to S-4, which go to I6 as repair round 01. S-1 asks for a demotion from conditioning (the CSKEW_8_5/9/10 cantilevers), because K2 rests on small-angle rounding.
  - T3's RV131 also says K2 does not meet the conditioning condition (its B-1), and K1 meets the requirement only if it is accurate at φ = 1e-8.
  - RV131 also confirms O4: long, nearly straight bends (φ ≤ 2e-9) falsely demote in K-D5. T3's remedy is the stable form 1 − cos φ = 2s² in K-D5. M31b0's equivalence needs K-D5's inputs to become (R, y) (N-2), and the derivation needs its numerical paragraph corrected (N-1).
  - The small-angle stable form is settled, with its stop rule. T4-U1's brief carries D-B, D-I, the stable form, K1 and K2, and O4–O6.
- **T4-U1b.** The design is in `T4-I9/`. T3's RV129 returned after the handoff; its final record is committed in NUM (`REVIEW_RV129/t4_i9_01/`). The verdict is PASS WITH AMENDMENTS, and T15c needs a different natural candidate (k between 6e35 and 1e39, not 1e40). R-1's (a)–(c) hold. The blocking finding is that `Formation::Certified` changes a priced layout, so the no-type-change alternative (O-2) is used. The successor sends RV129's amendments and T3's answers on O-1 to O-13 to T4-I9 for revision.
- **T4-U2.** Both reference sets are accepted: the bends (T4-I7, confirmed by RV3) and the rebuilt straight cases (T4-I8, confirmed by RV4). The authoring design is settled (`T4-I11/`). RV3's condition: the bend term's free-expansion field is treated like the thermal one.
- **T4-U3.**
  - The slot table's revision 01 (`T4-I10/REVISION_01.md`) folds in RV130's nine amendments. It goes back to T3 for RV130 to confirm.
  - The references are frozen through round 01 (`T4-I12/`, indices 0–22).
  - T4-RV5 refuted round 0: every value passes, and it is BLOCKING on B-1. The system document's spring hanger lacks its load and travel metadata, so validation refuses it before the connector runs; the fix restores the demo's values, and no frozen value changes.
  - Next: T4-I12's repair round 02 (B-1, S-1 to S-3), which RV5 confirms with round 01 in an addendum.
  - The log notes how S20's "presence" is to be read against I12's cases.

## Decisions waiting for ROOT

- **M31b0's equivalence by construction.** This is a narrowing, and it is ready to rule on. RV131 found that it holds, with conditions N-1 and N-2. T4's WORKING_ITEMS brings T4-I6's corrected derivation, RV131's record and T3's view together. M31b0's kill stays until the ruling.
- **The conditioning demotion for T3's K-D5 condition.** Neither RV2's S-1 nor RV131's B-1 accepts K2. If no CSKEW-type candidate demotes after T4-U1, "K2 alone" comes to ROOT as a narrowing.
- **R-1** for T4-U1b's certificate: ruled in `T4_RULINGS.md` ("R-1 after RV129"). It stays in force on T4-I9's revision 01 with A-1 to A-6 and RV129's confirmation. Two items may still come here: O-7 (T15c at guard level, R-2's narrowing) and O-10 (a re-registration, which T3 does not expect).
- **O-10.** A re-registration forced by T4-U1b's loops comes to ROOT before code, or rides B7.

## Open items for the owner

- **Later T4 decisions:**
  - D-5, section bases, needed before T4-U6;
  - D-6, the shear default, needed before T4-U8. Present it with the SP-1 note in `T4_RULINGS.md`.
- **G10,** the native witness, needs the owner's Mac.
- **Carried from 2026-10-08:** decision 22's machine-adaptive memory budget (a design study after PR-B1, not yet started).
- **Home-directory paths in App v4 on main** (about 4,000, in 728 files). A suggestion chip was offered; it is not T3's.
- **Records.** NUM's records are not yet on main. A records-only PR is due after #1168 merges; the owner's production-first direction allows it to wait.

## The host (machine-local; check it)

| | |
|---|---|
| **WT** | The sibling folder `chirality-t3` beside the main checkout. Since 2026-10-08 it is T3's permanent home. NUM's worktree is `WT/numerics`, and the T4 branch is in `WT/t4` |
| **Other worktrees** | `WT/u3-pr` (#1168), `WT/u5-docs` (U5), `WT/b2` and `WT/b2-j0b` (B2), `WT/b2-*` (the lanes), `WT/t3-norm` (merged; waiting for cleanup) |
| **The memory guard** | `WT/guard/memguard.sh`, PID 78827 at handoff. Check it with `pgrep -f memguard.sh` |
| **Locks** | Four slots. Cargo goes through `WT/tools/t3_cargo.sh`, other heavy jobs through `t3_slot.sh`, and exclusive jobs through `t3_exclusive.sh`. T4 shares them |
| **DEC-025** | `WT/scratch/prb1_merge/dec_chain.sh <label> <head> <main>` runs DEC-025 under the exclusive lock, then src-tauri. Compare with `WT/scratch/root_b1_suite/tools/cmp_cargo.py` |
| **The screens** | `WT/tools/t3_host_screen.py <repo> --staged`, or `<repo> <base> <head>`; and `tools/validation/validate_private_terms.py --from-host --terms-file WT/tools/t3_host_names.private.txt`. **Never commit, copy or quote that list** |
| **Disk** | About 601 GiB free at handoff |
| **Main** | `2759c0f1a1` (#1171, App v4) at handoff |
