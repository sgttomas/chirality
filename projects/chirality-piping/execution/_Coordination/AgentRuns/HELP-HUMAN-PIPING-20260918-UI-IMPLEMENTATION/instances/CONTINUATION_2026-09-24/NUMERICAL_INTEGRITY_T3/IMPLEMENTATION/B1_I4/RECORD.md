# B1's I4: the three readers merged into `b1` (ROOT, 2026-10-08 UTC)

**I4 = `30f3d1b24a`** on `codex/piping-t3-b1-20261007`, pushed. Its parents are I3's `b1` head `03f55e7178` (SP complete) and the three readers' heads, each merged with `--no-ff`:
- `b6327a5155` merges `b1-r` at `6e3e4fe219` (SR-RS round 2);
- `abff6d1ee5` merges `b1-p` at `2843a59a16` (SR-PY repair 02 with item 4);
- `30f3d1b24a` merges `b1-t` at `6fa6a64658` (SR-TS repair 01).

The sides are file-disjoint, and there were no conflicts. I4 changes 8 files over I3 (+2,711/−86). The ruling is RR "I4 made at `30f3d1b24a`; …".

## ROOT's check on I4

Each job ran in a T3 lock slot, one at a time, in the fresh target `WT/targets/root-i4`, with toolchain 1.97.1 and `--locked --offline`. The logs are in `_run_records/`, with machine paths replaced by `WT`, `APPWT` (the App worktree whose `node_modules` was linked) and `HOME`.

| Job | Result |
|---|---|
| RE (`core/reporting/result_export`), all tests | 193 passed, 0 failed; `retained_precision_contract` 76 passed |
| PY readers: `test_retained_precision_contract.py`, `_carriers.py`, `_schema.py` | 528 passed, 0 failed |
| TS readers: `retainedPrecision.test.ts`, `previewPhysicsEvidence.test.ts` | 543 passed, 0 failed (2 files) |
| PP `--lib` | 575 passed, 1 failed, 11 ignored. The failure is the known Mac `s11g_tests::t13_committed_fallback_uz_is_byte_identical`, as at I2 |

**The TS run, as I92 ran it:** a `git archive` of `P` without `execution/`, with `node_modules` linked from a checkout whose `package-lock.json` is byte-identical, and the eight wasm assets copied, not built, from `WT/sweep-skewpin` (`ts_wasm_assets.sha256`, equal to I71's).
- **A first attempt in `WT/b1` itself failed at setup:** `WASM-ENGINE-ASSET-ABSENT`, with no test run (`ts_reader.log`). It is disclosed here and counts for nothing.
- The link was removed after each run, and the archive was deleted.
