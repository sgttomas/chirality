# I113: drop B3a from `b2` (the legacy pressure label's admission to the retained route)

TASK (Type 2), dispatched by WORKING_ITEMS for T3 (Agent 1), your return path. You do not delegate. **You are a fresh instance.** `R/BRIEFS/B1_COMMON.md`'s host, Git and records rules apply, with WORKING_ITEMS in ROOT's place. Production code: working, tested code on the branch, with a short record.

## Why

The owner retired `1.0.0/legacy_pressure_v1` product-wide (RR "Owner decisions: the legacy pressure contract is retired product-wide; …"; ROOT's U3 rulings "U3 rulings on I110's pressure inventory: D-1 A, D-2 A1, D-3 held with M07"). B3a admitted zero-pressure 0.3.0 documents carrying that label to the retained route: lane A's D1.3 admission in PP, and the three readers' G8 namespace predicate (B3-D `R/I96/b3_d_01/DESIGN.md` §6.3, with REVISION_01). B3a is dropped. **B3D-10's tightenings stay**:
- 0.3.0 without a contract is `INVOCATION_MISMATCH`;
- PY's `{}` is `INVOCATION_MISMATCH`.

The resulting G8 predicate, in all three readers, is: schema 0.1.0 or 0.2.0 with `pressure_contract` absent or null; anything else is `INVOCATION_MISMATCH`. D1.3 in PP refuses the label as it refuses any non-null contract on the retained route.

## The branch

`codex/piping-t3-b2-20261008` (`WT/b2`), at the head WORKING_ITEMS gives you in the dispatch message. That head carries the reader lanes `b2-p`, `b2-r` and `b2-t`, merged after RV120's confirmation. The sites, from I110's inventory (`R/I110/pressure_retire_01/inventory.json`, kind `b3a`, 34 entries):
- PP: `retained_memory.rs` (3), `retained_memory_law_tests.rs` (8), `retained_facade_tests.rs` (3);
- PY: `core/analysis_runs/retained_precision.py` (2), `tests/test_retained_precision_b3.py` (4), `tests/test_retained_precision_contract.py` (2);
- RS: `RE/src/retained_precision.rs` (2), `RE/tests/retained_precision_contract.rs` (4);
- TS: `apps/desktop/src/features/results/retainedPrecision.ts` (2) and its test (4).

## The task

1. **Remove the admission** in PP and in the three readers. Each B3a admission test becomes a refusal test: D1.3 for PP, G8 `INVOCATION_MISMATCH` for each reader, with one shared shape the three readers pin alike. m3l, B3a's witness (RR "I99's B3-W verified; …"), becomes a refusal witness, or goes if nothing else uses it; say which.
2. **Keep everything else byte-identical:** every exact-route and 0.1.0/0.2.0 outcome, lane P's pins, the readers' 07m and 07n census (0 changes), and B3b.
3. **Run:** PP's suite, the runner, `result_export`, the PY reader tests and the TS reader tests. Compare outcomes with the head you started from, and list every removed, edited or added test.

**Stop** if the drop changes anything outside B3a, or needs a design change beyond removing B3a.

## Host, Git and records

- Targets under `WT/targets/i113-*`; scratch in `WT/scratch/i113_b3a/`. Cargo through `WT/tools/t3_cargo.sh`; other heavy jobs through `WT/tools/t3_slot.sh`. No DEC-025.
- Commit on `b2` in `WT/b2` with truthful messages. WORKING_ITEMS pushes.
- Records go in `R/I113/b3a_drop_01/` (RETURN.md, `_run_records/`, SHA256SUMS), placeholder paths only. If the host refuses a record file, put its full content in your final message with the intended path; do not work around the refusal.
- Budget: 2–3 h.

End your turn with:
- the head and commits;
- the test diff;
- the census;
- any stop.
