# I105, J0a: `b2` absorbs main with PR-B1 and PR-N

TASK (Type 2), continued by WORKING_ITEMS for T3 (Agent 1), your return path. `R/BRIEFS/B1_COMMON.md`'s rules apply, with WORKING_ITEMS in ROOT's place. Production code: a working merge with tests, and a short record.

## Why now

Main now carries PR-B1 (#1154, `7eae707bb7`) and PR-N (#1163, `ec5d397359`, the correctly rounded norm). J0 was planned for after U3 too. WORKING_ITEMS splits it:
- **J0a now**, so B1's qualification and the norm reach `b2` while U3 is in progress;
- **J0b later:** a smaller absorb once U3 merges.

## The task, on `codex/piping-t3-b2-20261008` (`WT/b2`, head `0ef9a8ace9`)

1. **Merge main** (`ec5d397359` or later; use the main commit WORKING_ITEMS names in the dispatch message) into `b2`.
   - Resolve the conflicts in `retained_memory_law_tests.rs`, and anywhere else, **against B1's final M** (R6b, `threshold_bytes` 11,274,289,152) and B1's merged code.
   - `b2`'s own B2/B3 work (lanes A, K and P, the readers, and the B3a drop) is kept.
   - **Do not change B2/B3 behaviour** to resolve a conflict. If a conflict needs a design choice, stop and return.
2. **Re-take the Mac pins (RV123 N-1).** B2-P's pins that held libm-`hypot` magnitudes now hold the correctly rounded norm. Re-pin them to the new bytes, which are now platform-independent. Check each moved value exactly: it must equal the correctly rounded norm of its own components.
   - Retained support magnitudes and the combination displacement magnitudes were already robust and should not move.
   - List every pin that moves.
3. **Run PP's suite, the runner, `result_export`, the PY and TS reader suites, and the readers' 07m and 07n census.** Compare against `b2`'s start head and against main.
   - The census must show 0 changes.
   - Every outcome change must be explained: B1's qualification arriving, a re-pin, or `t13` and the `load_reference` tests now passing.
4. **Ask for the Linux CI dispatch of the merged head** in your return. WORKING_ITEMS pushes and dispatches.

I101 is meanwhile repairing the readers on `b2-r`, `b2-t` and `b2-p` (N2b). Those lanes merge into `b2` after your merge; stay out of them.

## Host and records

- Targets go under `WT/targets/i105-j0a*`, scratch in `WT/scratch/i105_j0a/`. Cargo goes through `WT/tools/t3_cargo.sh`; other heavy jobs through `WT/tools/t3_slot.sh`. No DEC-025.
- Commit on `b2` with truthful messages.
- Records go in `R/I105/b2_j0a_01/` (RETURN.md, `_run_records/`, SHA256SUMS), placeholder paths only. If the host refuses a file, put its content in your final message.

End your turn with:
- the merge commit and the conflicts resolved;
- the moved pins with their exact checks;
- the suite and census comparison;
- the dispatch request;
- any stop.
