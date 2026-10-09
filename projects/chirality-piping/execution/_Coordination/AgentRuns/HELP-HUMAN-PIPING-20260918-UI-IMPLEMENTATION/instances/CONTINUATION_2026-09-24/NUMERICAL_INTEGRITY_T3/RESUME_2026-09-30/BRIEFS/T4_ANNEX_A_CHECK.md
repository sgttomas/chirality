# I115: verify T4 plan 01's annex A claims that protect T3

TASK (Type 2), dispatched by WORKING_ITEMS for T3 (Agent 1), your return path. You do not delegate. **You are a fresh instance.** Read-only: no product change and no commits. `R/BRIEFS/B1_COMMON.md`'s host and records rules apply, with WORKING_ITEMS in ROOT's place.

## The claims

T4's design manager asks T3 to agree what T4's plan changes on T3's side. The claims are in annex A, `R4/PLAN_01/T3_AGREEMENT.md` (sha256 `159356ac…`), on T4's branch `codex/piping-t4-pressure-stress-20261009` at `7a1863a37c` (`WT/t4`). Here `R4` = `…/CONTINUATION_2026-09-24/PRESSURE_STRESS_T4`. The context is `PLAN.md` §3.3 and §4.2 H-4. The source is `R4/T4-I5/RETURN.md`, which cites `path:line@commit` for every item. Its basis is main plus T3's U3 (`70e7f49ced`) and `b2` at `9f5cfbcd75`.

Annex A claims that T4-U1 (the curved element's objective formation) and T4-U3 (the corrected joint, with the old element deleted) leave the following unchanged:
- every retained-route and source-route output;
- `REVIEWED_INPUTS`;
- `REGISTERED_PROFILES`, the priced atoms, `PINNED_RECORD` and M, provided H-4 holds;
- `b2`, with which there is no textual overlap.

## The task (proportionate: read and spot-check; about 1.5 h)

1. **Retained and source outputs unchanged.** Check I5's argument at its cited lines:
   - W1 refuses any model with components before anything specific to curves or joints runs;
   - the retained route calls only `assess_rigid_body` from the joint and curve code paths.

   Check this at main `ec5d397359` plus U3's head (`WT/t3-pret`, now `1e9724fb94`), not only at I5's basis. Say whether any retained-route or source-route path reaches the curved formation or the user-stiffness element.
2. **`REVIEWED_INPUTS` and M untouched.** List the files T4-U1 and T4-U3 plan to edit (PLAN §3.3, I5), and confirm that none is in `REVIEWED_INPUTS`: 14 entries on main, 17 on `b2` at `e582b61f9e`. Say what H-4 protects, which is the `s(MechanicsEnvelope)` summary key, and what would re-pin `PINNED_RECORD` without it.
3. **No overlap with `b2`.** Reproduce one simulated merge, read-only with `git merge-tree`: T4's planned edit set against `b2` at `e582b61f9e` (J0a, which is newer than I5's basis). Treat a clean result as indicative only, since T4 has no code yet; report the shared files.
4. **Facts for items 1, 2 and 7 of annex A's last section:**
   - For M31b/M31b0, find RR's K-D5 rulings (RR "K-D5 mutation M31b: equivalence withdrawn") and say what the required kill protects.
   - For `CSKEW_8_5`, say what depends on it.
   - For H-4, compare the cost of the summary-key rename and row-kind removal in PR-B2's re-pin wave with doing it at B7.

## Records and return

Records go in `R/I115/t4_annex_check_01/` (RETURN.md, `_run_records/`, SHA256SUMS), placeholder paths only. If the host refuses a file, put its content in your final message.

End your turn with:
- a verdict on each of the four claims (holds, holds with a condition, or does not hold), with path:line evidence;
- the facts for items 1, 2 and 7;
- any concern.
