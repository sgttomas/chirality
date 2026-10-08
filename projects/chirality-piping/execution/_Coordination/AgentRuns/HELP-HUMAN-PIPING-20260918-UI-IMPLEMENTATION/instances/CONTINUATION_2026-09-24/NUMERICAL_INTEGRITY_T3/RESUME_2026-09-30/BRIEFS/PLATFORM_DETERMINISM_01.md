# I109: platform-independent published values: a correctly rounded `hypot`, and the libm inventory

TASK (Type 2), dispatched by ROOT (HELP_HUMAN, Agent 0). ROOT is your return path, and you do not delegate. **You are a fresh instance.** Read `R/BRIEFS/B1_COMMON.md` for the host, Git and records rules. This is production code: the deliverable is working, tested code on a branch, with a short record.

## Why

PR-B1's hosted CI (glibc) failed where the Mac passes (RR "I107's Pass B (no stop); PR-B1's hosted CI fails on Linux: …"). The ordinary route publishes support and member force magnitudes formed with `f64::hypot`. That function is not correctly rounded, and macOS's libm and glibc's differ in the last bit:
- on W-C2's case C, `rigid:N0`'s support force magnitude is `1.6258317075882521e-12` on macOS and `…523e-12` on glibc;
- PP's `s11g_tests::t13_committed_fallback_uz_is_byte_identical` has failed on every Mac run because its pin was taken on Linux.

Published bytes therefore depend on the machine. B1 works around this with exact per-platform pins. The product should not need them.

## The task

1. **The inventory.** Find every call into a not-correctly-rounded libm function whose result can reach published bytes, a receipt, a pinned test value or an admission decision:
   - the functions: `hypot`, `sin`, `cos`, `tan`, `atan2`, `asin`, `acos`, `atan`, `exp`, `exp_m1`, `ln`, `ln_1p`, `log10`, `log2`, `powf`, `powi`, `cbrt`, `to_radians` and `to_degrees` where they feed those, and any others you find;
   - the scope: `P/core/product_physics` (ordinary and retained routes), the solver crates (`P/core/solver/*`), `P/core/loads/*`, `P/core/reporting/result_export` (the RS reader), and the PY and TS readers. In JavaScript, `Math.hypot` and the trigonometric functions are not correctly rounded; `Math.sqrt` is.
   - For each site: path:line, what it computes, whether it reaches published bytes, and whether the readers recompute it.

   `sqrt`, `+`, `−`, `×`, `÷` and `mul_add` are correctly rounded by IEEE 754 and are not in scope.
2. **A correctly rounded Euclidean norm** for 2 and 3 components (`norm2`, `norm3`), and `hypot`'s chain semantics where the code uses `a.hypot(b).hypot(c)`. Decide whether the published value should be the correctly rounded 3-norm or a correctly rounded chain, and say why.
   - Use only IEEE basic operations, `sqrt` and `f64::mul_add`: error-free products and sums into a double-double, a square root, then a correction step. Handle zeros, signed zeros, infinities, NaN, subnormals and overflow scaling exactly as `hypot`'s contract does.
   - **The oracle:** exact rational arithmetic (Python `fractions`, or a big-integer square-root comparison) on a large random set (at least 10⁷ cases across magnitudes, including the subnormal and overflow ranges) plus adversarial near-halfway cases. **Zero misrounded results is the acceptance bar.**
   - Put it in one small module that PP and the readers can share, or mirror exactly in PY and TS if the readers need it. Say which.
3. **The measurement, on a branch from NUM** (`codex/piping-t3-platform-norm-20261008`, worktree `WT/t3-norm`). Replace the published-path `hypot` calls with the new norm. Run PP's suites, the runner, `result_export` and the 40 manifests on the Mac, and list every test whose bytes change:
   - which committed fixtures, goldens, pins and corpus entries move, by how many values, and by how many ulps;
   - whether `t13` now passes on the Mac.

   Do not re-pin anything yet. The list is the decision input.
4. **Linux.** ROOT runs a hosted-CI diagnostic dispatch of your branch on request. Ask in your return, giving the head, so the glibc side of the measurement can be read. Then say whether the B1 platform pins become unnecessary.
5. **The other functions** (`sin`, `cos`, `atan2`, `exp`, …) on published paths: for each, give a recommendation (a correctly rounded implementation, an exact reformulation, or proof that it cannot reach published bytes) and a size estimate. Implement only `hypot`'s replacement in this round.

## Rules

- **Host:**
  - every cargo through `WT/tools/t3_cargo.sh` (`--locked --offline`), with targets under `WT/targets/i109-*`, and other heavy jobs through `WT/tools/t3_slot.sh`;
  - one heavy job at a time, with no RSS or timing measurements, no DEC-025 and no installs. Python `fractions` and `decimal` are in the standard library.
- **Git:** commit on your branch only; ROOT pushes. Do not touch `WT/numerics`, `WT/pr-b1` or other lanes' worktrees.
- **Records:** `R/I109/platform_norm_01/` (RETURN.md, `_run_records/`, SHA256SUMS), placeholder paths only. Scratch goes in `WT/scratch/i109_norm/`.
- **Budget:** 8–12 h. If your context runs low, commit a compiling state, write what remains, and return.

## Return

End your turn with:
- the branch head;
- the oracle result;
- the inventory's counts;
- the list of moved bytes;
- whether `t13` passes;
- the CI dispatch request;
- any stop.
