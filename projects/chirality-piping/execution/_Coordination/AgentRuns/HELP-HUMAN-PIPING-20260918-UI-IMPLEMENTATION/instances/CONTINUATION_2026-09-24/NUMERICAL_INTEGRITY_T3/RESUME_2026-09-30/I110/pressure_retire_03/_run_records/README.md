# I110 round 3 run records

Placeholders: `WT`, `NUM`, `P`, `PP`, `RE`, `R`. B is main `7eae707bb7`; the candidate is `6b6543dc1e` (`WT/t3-pret`, branch `codex/piping-t3-pressure-retire-20261008`). Every cargo ran through `WT/tools/t3_cargo.sh`, and every other heavy job through `WT/tools/t3_slot.sh`. Targets went to `WT/targets/i110-*`. Paths in the copied files are rewritten to placeholders.

**B-side records are reused from round 2** (`R/I110/pressure_retire_02/_run_records/`: `manifests_base.txt`, `tauri_base.txt`, `pytest_base.txt`, `vitest_base.json`, `bytes_hb_release.jsonl`, `bytes_hb_w1.jsonl`). They are the same commit, measured on the same host and toolchain (rustc 1.97.1), by the same scripts. Only the candidate side was run in round 3.

| File | What |
|---|---|
| `heads.txt` | the candidate commit, and the B commit whose round-2 records are reused |
| `manifests_cand.txt` | `WT/scratch/calib/run_suites_nff.sh` summary per manifest (40 manifests), at the candidate |
| `outcome_and_byte_diff.json` | from `scripts/compare_evidence.py` (unchanged from round 2): per-test outcome changes from B to the candidate (40 manifests, src-tauri, pytest, vitest), and byte equality per set and pass, with any differences (none) |
| `test_name_diff.txt` | `#[test]` names removed and added from B to the candidate, by source scan (`scripts/test_names.py`); the observed outcome changes equal this list exactly (54 = 53 in the manifests + 1 in src-tauri) |
| `tauri_cand.txt`, `pytest_cand.txt`, `vitest_cand.txt` | per-test outcomes at the candidate |
| `bytes_hc_release.jsonl`, `bytes_hc_w1.jsonl` | the harness rows at the candidate (`release` = sets E, F and B1, ordinary entry and runner, both modes; `w1` = B1 through the retained direct entry, debug build, the registered profile). Each row also carries `h1`, the count of `-0.0` tokens in the ordinary envelope and the export document (reported, not compared) |
| `g11_confirm_before_fix.txt` | the G11 test failing on the tree before the fix |
| `scripts/` | `i110_bytes_harness.rs` (probe-only, untracked in `WT/t3-pret-hc`; round 2's plus the `h1` count), `bytes_passes.sh` and `app_py_chain.sh` (round 2's, writing to a round-3 folder), `compare_evidence.py`, `test_names.py`, `rm_fns.py` (used for the deletions), `g11_fix.py` (applied the committed fix) |
