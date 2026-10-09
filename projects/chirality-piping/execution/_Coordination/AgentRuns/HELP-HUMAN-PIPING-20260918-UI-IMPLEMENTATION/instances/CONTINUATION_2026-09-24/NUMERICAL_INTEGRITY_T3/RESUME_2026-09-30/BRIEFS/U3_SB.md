# I107, round 3: Pass B on the U3 PR's code commit

TASK (Type 2), continued by WORKING_ITEMS for T3 (Agent 1), your return path. `R/BRIEFS/B1_COMMON.md` and your earlier briefs (`B1_SB.md`, `PR_N_SB.md`) bind you, with WORKING_ITEMS in ROOT's place. Keep the record short.

## The candidate

- **The code commit `8a12de28db`** on `codex/piping-t3-pressure-retire-pr-20261009` (`WT/u3-pr`; PR #1168). It is one commit on main `ba500defa4`, which carries PR-B1 and PR-N, with the 133 maintained files that NUM changes.
- **What it is:** the legacy pressure retirement. It removes code on the D1 call graph: the legacy pressure computation, and the always-empty pressure plumbing in `source_recovery.rs`, `source_receipt.rs` and `retained_product.rs`. It adds refusals, joint refusals and text corrections.
- **Records:** `R/I110/pressure_retire_01..06/` and `R/REVIEW_RV127/u3_stage1_01/`. RV127 checked the in-build profile change.
- **The basis to compare against** is main as merged (B1 plus PR-N): your PR-N Pass B and RV124's confirmation.

## Pass B must show

On an archive of `8a12de28db` against `ba500defa4`:
1. **The entry and registration.** They are unchanged; the reviewed inputs and PP's lock are untouched. If anything changed, show exactly what.
2. **TEXT, forms and the GENERATED PROFILE blocks.** Attribute every change to a removal or an added refusal, and give its effect on G5/G6 and M.
   - Expected: the in-build profile is exactly 800 B lower per phase, because two atoms shrink: `StressRecoveryResult` by 32 B ×9 and `DerivedSection` by 8 B ×64. ROOT accepted this on condition of Pass B.
   - **Stop** if M must change or the bound worsens.
3. **The delta rows.** Classify every one, with a reviewed entry for each production hunk.
4. **Loops and allocations** in any new code: the joint refusals and the panel logic on the Rust side.
5. **Outcomes, witnesses and the challenge.** Show the non-candidates, the controls, and that PP and runner outcomes change only by the listed tests. The witnesses and the challenge must equal B1's, apart from the profile's −800 B.

**Stops:** a production-class row not attributable to the retirement; any change to M or the registered identity; a witness or challenge regression.

## Host and records

- Targets go under `WT/targets/i107-u3*` and scratch in `WT/scratch/i107_u3/`. No DEC-025, no measurements, no installs.
- If you rerun the line map or the delta tool mechanically, refresh I65's fingerprints first (RV124 C-N1).
- Records go in `R/I107/u3_passb_01/` (RETURN.md, `_run_records/`, SHA256SUMS), placeholder paths only. If the host refuses a file, put its content in your final message.

End your turn with:
- the verdict and the gate codes;
- the delta rows;
- the profile change;
- RETURN's sha256;
- any stop.
