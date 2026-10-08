# I107, round 2: Pass B on PR-N's code commit

TASK (Type 2), continued by WORKING_ITEMS for T3 (Agent 1), your return path. `R/BRIEFS/B1_COMMON.md` and your round-1 brief `B1_SB.md` bind you, with WORKING_ITEMS in ROOT's place. Production first: keep the record short.

## The candidate

- **PR-N's code commit `8dd64c1835`** on `codex/piping-t3-correct-norm-20261008` (`WT/pr-n`): one commit on main `7eae707bb7` (PR-B1 merged). It carries the 21 maintained files that NUM `ef8ab78473` changes against main: I109's correctly rounded norm (`FK/src/correct_norm.rs`), its call sites, the rank screen, and the re-pins.
- **I109's records:** `R/I109/platform_norm_01/` (the norm, the inventory) and `R/I109/pr_n_01/` (the re-pins). By SQ's call graph, 16 of the norm's 17 production call sites are reachable from `run_linear_static_preview_value_with_retained_direct` (pr_n_01 RETURN "D1 call sites").
- **The basis to compare against** is B1 as merged: your round-1 Pass B (`R/I107/b1_passb_01/`, RV124's confirmation) on PR-B1's code, with the registration at `threshold_bytes` 11,274,289,152.

## Pass B must show, on an archive of `8dd64c1835` against `7eae707bb7`

1. the entry and the registration unchanged (the 14 reviewed inputs and PP's `Cargo.lock`), or exactly what changed;
2. TEXT and the forms (D, D_env), and the GENERATED PROFILE blocks: equal, or every change attributed to the norm with its effect on G5/G6's bound and M's margin. If M must change, **stop**;
3. every delta row classified, with a reviewed entry for each production hunk (the norm module and its call sites);
4. `correct_norm`'s loops and allocation: no heap, no recursion, and a bound for its correction loop. I109 says the loop runs at most twice by construction but has no static bound in the code. If your loop scan needs one, say exactly what change it needs, and do not make it yourself;
5. the non-candidates, the controls, and PP and runner outcomes changed only by the listed tests;
6. the witnesses and the challenge: equal to B1's, or moved only by the norm's one-ulp values, each listed.

**Stops:** a production-class row you cannot attribute to the norm; a change to M or the registered identity; a witness or challenge regression beyond a listed one-ulp move.

## Host and records

- Targets under `WT/targets/i107-pn*`; scratch in `WT/scratch/i107_pn/`. No DEC-025, RSS or timing measurements, or installs.
- Records go in `R/I107/pr_n_passb_01/` (RETURN.md, `_run_records/`, SHA256SUMS), placeholder paths only. If the host refuses a record file, put its full content in your final message with the intended path; do not work around the refusal.
- Budget: 2–3 h plus build time.

End your turn with:
- the verdict and the gate codes;
- the delta rows;
- the loop-bound finding;
- RETURN's sha256;
- any stop.
