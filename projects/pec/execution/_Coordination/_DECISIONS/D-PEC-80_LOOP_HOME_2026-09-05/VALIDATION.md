# D-PEC-80 verification index

All results are agent-produced execution evidence, not acceptance. Basis:
7458e9c1eb9399ed259da464207d9a507acdea2e. Migration checkpoint:
ca49b846dabc563192caa0effd389265535a8598. Corrective migration checkpoint:
aa17255b56f6b8e405cc633e9e88731f797bff31. B/C follows both checkpoints on
the same branch, with only Receipt 167 appended for this entire run.

| Stage/check | Evidence / outcome |
|---|---|
| Original standing-plan discovery | BASELINE_CHECKS.json, BASELINE_POINTERS.json, baseline outputs; original plan has prose and paths, not an executable Step 0 block; command omissions repaired |
| Migration before first commit | MIGRATION_CHECKS/CHECKS.json; all ten checks exit 0 |
| Exact first migration commit | MIGRATION_COMMIT_CHECKS/CHECKS.json; all ten exit 0 |
| Corrected migration alone, before restoring B/C | MIGRATION_CORRECTED_CHECKS/CHECKS.json; all ten exit 0 |
| Migration candidate whitespace | Initially failed due CRLF in new CSV evidence; fixed before first published commit. Later failed on trailing whitespace in the newly captured awk error log; diagnostic-preserving trim applied. Subsequent candidate check PASS |
| Final candidate functional suite | FINAL_CHECKS/CHECKS.json; all ten exit 0: entrypoints, receipt contract, live/archive Task Management, 89 focused tests, harness self-check, 6 API tests, 12 registry tests, core posture, git diff --check |
| Full practitioner harness tests | SUPPLEMENTAL_CHECKS.json / harness-pytest.stdout; 351 passed, exit 0 |
| Candidate complete Step 0 | SUPPLEMENTAL_CHECKS.json / step0-final.stdout; exit 0 with approved fetch |
| Fresh-reader complete Step 0 | DRY_RUN_2.md; initial sandbox denial recovered, full rerun exit 0 |
| State-column grep | REGISTER_GREP_CHECKS.json; baseline live, historical open D-PEC-75, final candidate live, all exit 0 |
| Profile validation | PROFILE_VALIDATION.json; VALID, zero findings; no ungranted validator-output write |
| Move/history integrity | INTEGRITY_CHECKS.json; all 337 hashes identical at corrected A; 335 final historical files unchanged; only new init and prospective ledger continuation differ |
| External write/fence audit | SCOPE_CHECKS.json; exact grant only, no agents changes, project fence verbatim |
| Literal and constructed old locators | REFERENCE_INVENTORY.csv, CONSTRUCTED_PATHS.md, FINAL_REFERENCE_INVENTORY.csv / SUMMARY.json; preserved immutable lines and new provenance records only |
| Fresh-reader friction tables | DRY_RUN_1.md and DRY_RUN_2.md with literal input fixtures; missing rules and wrong command fixed before PR |
| Post-commit whitespace and mergeability | POST_COMMIT_CHECKS.json and associated logs (recorded against the committed candidate) |

Reproduction: from repository root, run the candidate's full Step 0 block;
run `python3` on this directory's `run_check_suite.py` with an output-directory
label (writes evidence here), selecting the recorded compatible Python path
or an equivalent Python 3.10+ with pytest. Run `verify_migration.py` from the
root to reproduce the move hashes and whole-source-tree old-reference scan.
The inventory includes hidden tracked/unignored files and all repository
areas; excluded build artifacts, Git internals, binary files and symlinks are
not textual reference sources. Historical strings inside this new sealed
packet/logs are provenance and are enumerated too.

The first parent Step 0 attempt exposed BSD awk delimiter behavior (exit 2);
the portable field-based loader fixed it, and step0-repaired outputs preserve
the successful rerun. The first fresh reader independently caught an
accepted decomposition pin mismatch not detected by the structural suite;
A's repair restores the exact accepted bytes. This is why independent
acceptance checks and deterministic validators are both recorded.

Self-check exit 0 includes 55 WARN and four REVIEW findings; no clean-corpus
claim is made. Source/product kill and parity capabilities are not changed by
this locator/instruction tranche, so their production gates are not asserted
satisfied. Compatible Python 3.13 was used for the existing v2 registry tests;
default Xcode Python 3.9 cannot execute its existing slotted dataclasses.

Fresh origin/main advanced only through sister app-dev governance work during
this run. It does not overlap the exact changed paths. No remote work is
reset, rebased away, or treated as PEC authority. Owner disposition remains
the only pending acceptance gate; no merge is performed by this run.
