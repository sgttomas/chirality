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
