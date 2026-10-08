# I110 round 2 run records

Placeholders: `WT`, `NUM`, `P`, `PP`, `RE`. B is main `7eae707bb7` (`WT/t3-pret-base`); the candidate is `4c0d5d7c00` (`WT/t3-pret`, branch `codex/piping-t3-pressure-retire-20261008`). Every cargo ran through `WT/tools/t3_cargo.sh`, and every other heavy job ran through `WT/tools/t3_slot.sh`. Targets went to `WT/targets/i110-*`. Paths in the copied files are rewritten to placeholders.

| File | What |
|---|---|
| `heads.txt` | B and candidate commits |
| `manifests_base.txt`, `manifests_cand.txt` | `WT/scratch/calib/run_suites_nff.sh` summary per manifest (40 manifests) |
| `outcome_and_byte_diff.json` | from `scripts/compare_evidence.py`: per-test outcome changes, B to candidate (40 manifests, src-tauri, pytest, vitest), and the byte-equality counts per set and pass, with any differences (none) |
| `tauri_*.txt`, `pytest_*.txt`, `vitest_*.json` | per-test outcomes |
| `bytes_hb_*.jsonl`, `bytes_hc_*.jsonl` | the harness rows (`hb` = B, `hc` = candidate): `release` = sets E, F and B1, ordinary entry and runner, both modes; `w1` = B1 through the retained direct entry, debug build (the registered profile) |
| `bytes_*_release_progress.txt` | the harness's per-document progress |
| `scripts/` | `i110_bytes_harness.rs` (probe-only, placed untracked in `WT/t3-pret-hb` and `WT/t3-pret-hc`), `make_inputs.py`, `bytes_passes.sh`, `app_py_chain.sh`, `compare_evidence.py`, `rm_fns.py` (used to delete the oracle functions), `pp_tests.sh`, `runner_tests.sh`, `parse_outcomes.py` |
