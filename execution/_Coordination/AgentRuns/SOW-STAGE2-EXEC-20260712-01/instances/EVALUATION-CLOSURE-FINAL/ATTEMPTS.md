# Attempts

1. The structural evaluator first used the repair-manifest field names
   `report_path` and `report_sha256`. The live schema uses
   `finalization_report_path` and `finalization_report_sha256`. The resulting
   `KeyError` occurred before terminal output; the owned evaluator was corrected
   and the complete audit reran PASS.
2. The first App-suite substrate copied only `frontend/`. Four tests correctly
   failed because repository-level `agents/`, `docs/`, and `.github/` fixtures
   were absent. This was a substrate failure, not a subject failure. The output
   is retained in `final_evaluation/checks/app_tests.txt`; R1 reconstructed the
   full repository layout and passed 713 tests with four declared skips.

No project or retirement state was modified by either attempt.
