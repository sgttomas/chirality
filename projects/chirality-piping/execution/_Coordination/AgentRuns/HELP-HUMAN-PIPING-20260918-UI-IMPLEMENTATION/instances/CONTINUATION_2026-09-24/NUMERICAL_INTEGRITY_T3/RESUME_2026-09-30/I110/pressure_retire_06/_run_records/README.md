# I110 round 6 run records (placeholders: WT, NUM, P, PP, RE, T, R)

- `heads.txt`, `scratch_heads.txt`: the branch commits, the scratch heads (never pushed) and the worktrees.
- `t2_per_file_check.txt`: T2's per-file check under ROOT's exact steps, from Git objects (`scripts/t2_check.py`).
- `t2_probe/`: the probe's baseline and re-pin reports (`scripts/i110_t2_repin.rs`), and the 15 source-block-related harness rows at the head without T2 and at the final head.
- `demo_regeneration_check.txt`: both recipe modes against the committed records (`scripts/regen_compare.py`); `regen_*.stdout`: the recipe's stdout (first run, and the shim rerun in WT/t3-pret-hb).
- `a1n4_vitest.log`, `a1n4_pytest.log`: RV128 A1-N-4's four tests after the merge.
- `bytes_final_release.jsonl`, `bytes_final_w1.jsonl`: the harness rows at the final head (E, F, B1; and W1).
- `bytes_release_compare.json`, `bytes_w1_compare.json`, `declared_text_check.txt`: the extended byte classification against B (`scripts/compare_ext.py`).
- `outcome_and_byte_diff.json`: per-test outcome changes against B, all suites (`scripts/compare_evidence.py`); `test_name_diff.txt`: the source `#[test]` diff; `manifests_cand.txt`: the 40 manifests' summary.
- `e2e_final.log`: the four e2e specs (`scripts/e2e.sh`).
- `merge_main_check.txt`: the merge with main ec5d397359 (`scripts/resolve_lib.py`).
- `source_equality.out`, `source_equality.json`, `check_citations.out`, `citations_resolved.md`: the package checks.
- `scripts/`: every script used this round, including the round-6 harness and the cargo shim.
