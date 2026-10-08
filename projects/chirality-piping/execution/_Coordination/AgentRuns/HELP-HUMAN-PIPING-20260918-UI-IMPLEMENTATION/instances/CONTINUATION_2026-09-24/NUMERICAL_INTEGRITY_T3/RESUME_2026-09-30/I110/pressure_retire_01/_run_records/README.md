# I110 run records

Placeholders: `WT`, `NUM`, `P`, `PP`, `RE`. The probe tree is `WT/t3-pret`, detached at NUM `9cd61ba201` (product code = PR-B1 head = main `7eae707bb7`). Targets went to `WT/targets/i110-pret` and `WT/targets/i110-pret-runner`; scratch went to `WT/scratch/i110_pret`. Every cargo run went through `WT/tools/t3_cargo.sh` with `--locked --offline`. The probe edits (`probe_p2_p3_runner.diff`) were applied only to the probe tree. They were never committed, and they were reverted afterwards (`git diff` there is empty). Paths in the copied logs and scripts are rewritten to placeholders, so the scripts are records, not runnable as-is.

| File | What |
|---|---|
| `scan_models.py`, `models_scan.json` | every JSON model document under `P` (execution records excluded), with paths relative to `P`: version, contract, pressure primitives, exact-refused features |
| `build_inventory.py`, `mech_purposes.txt` | builds `../inventory.json`: line numbers are resolved in NUM's tree, and the B3a sites come from `git grep` on the b2 refs |
| `pp_tests.sh`, `runner_tests.sh` | PP `--lib` plus 19 integration targets (the three memory targets excluded); the runner crate's tests |
| `prototype.py` (P1/P2), `prototype_p3.py`, `prototype_runner.py` | the probe-only edits (RETURN §6) |
| `pp_baseline.log`, `pp_p2.log`, `pp_p3.log`, `runner_baseline.log`, `runner_p3.log` | raw cargo output; the runner logs are filtered to run, test, result and panic lines |
| `outcomes.json`, `outcomes_diff.txt` | per-test outcomes and the diffs (baseline → P2, baseline → P3; runner baseline → P3) |
