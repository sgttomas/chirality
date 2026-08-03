# WORKING_ITEMS manager return — D-APP-88 Option B

## Verdict

`BLOCKED / PARTIAL — EVIDENCE ACCEPTED; PRODUCT CANDIDATE ROLLED BACK`

D-APP-88 Option B is not complete. The copied-Electron-main helper technique produced a relocatable package candidate and proved several required conjuncts, but it failed the ruling's graceful/recover-on-start preservation boundary after GUI coexistence. No weakened interpretation of the ruling is inferred.

## Accepted findings

- Preserving relative framework symlinks fixed the nested-child ICU/resource failure; the final candidate had 15 helper-local relative symlinks and zero absolute links.
- The helper candidate had a distinct bundle path, `CFBundleIdentifier`, and `LSUIElement` posture; LaunchAgent/CLI routing, fresh startup, packaged CLI same-PID status, GUI coexistence without helper replacement, no TCP listener, clean-start SIGTERM, and SIGKILL recover-on-start were demonstrated to the bounded evidence level recorded in the sanitized run package.
- After GUI coexistence, first `SIGTERM` and a helper-only `SIGUSR2` diagnostic did not enter graceful teardown. A second signal terminated without teardown and left a stale socket. This is the blocking preservation failure.
- Renaming the copied Electron main could not satisfy Electron 43.2's pre-JavaScript child-helper lookup in the tested arms.
- A separately built full Electron helper target was not evaluated. It remains an untried lawful alternative; this run does not establish impossibility.

## Integration disposition

- Every D-APP-88 product/config/test addition and hunk is absent from integration state.
- Five touched existing source/test files equal `HEAD`; the three D-APP-88 additions are absent.
- `frontend/package.json` retains only D-APP-89's removal of `@chirality/harness-contract`; D-APP-89, planning, and ruling bytes are preserved.
- DEL-09-04 remains `IN_PROGRESS`; its Checking Approval SHA and lifecycle boundary are unchanged.
- Root runtime tracked state is clean, all six D-APP-81 UNKNOWN relations are untouched, and no receipt, register, Git, release, signing, notarization, publication, or distribution effect occurred.

## Evidence and validation

- Implementation return: `A2_IMPLEMENTATION_RETURN.md`, SHA-256 `39c6f2f389b9fa69caea986a59ee3ae15319f60c2019f4f20802f98633986028`.
- Agent 2 return: `instances/A2-DAPP88-IMPLEMENT-01/RETURN.md`, SHA-256 `17f0eae218859840664254b9dbc458e501e191899d890a9bb579330226990b28`.
- Drill report: `instances/A2-DAPP88-IMPLEMENT-01/evidence/DRILL_REPORT.md`, SHA-256 `c837c2be3caf2bc1507e978624cc40fb8131caa9d1c75e72efd8fb01d3cfd403`.
- Raw evidence index: `instances/A2-DAPP88-IMPLEMENT-01/evidence/raw-salvage/RAW_EVIDENCE_INDEX.md`, SHA-256 `0c894ce2c48112bda80f95894d63e4582cef8f89b1cad18a7478a717d1d960a3`.
- Candidate manifest: `instances/A2-DAPP88-IMPLEMENT-01/evidence/CANDIDATE_SOURCE_MANIFEST.md`, SHA-256 `c06dca26e1e2f69cf94b0a30f89f8f618f04e6caa38de99b1fc9b122f4d8e168`.
- Rollback manifest: `instances/A2-DAPP88-IMPLEMENT-01/evidence/ROLLBACK_MANIFEST.md`, SHA-256 `811cc020a29902ae78bf7bef641d5f73207c81fccb883355fbe4b7ab44322bd5`.
- Cleanup addendum: `instances/A2-DAPP88-IMPLEMENT-01/evidence/CLEANUP_ADDENDUM.md`, SHA-256 `ac375c420c384cb57dd4f4831622df9f41fdd2780b25a932a36e9666a1279101`.
- Telemetry: `RUNTIME_EVENTS.jsonl` SHA-256 `56467874f8f7d0394823cd318731305600d7e11753c51e0bab7bf6010c9dab46`; `RUNTIME_SUMMARY.json` SHA-256 `ecafd46cdc53d4a968933c164e8324501521f96ffbb63c86bf45190ce7097256`, status `PASS`.
- TASK record: deliverable `_run_records/TASK_RUN_2026-08-02_2356.md`, terminal `FAILED`, SHA-256 `4f7050082eb78da8a481c6736362694d58b8dd73d553df5818c2d0818a8363c8`.
- Second fresh verifier: `PASS` for this blocked/partial fan-in, with stable start/end hashes.

Cleanup is complete: 19 exact D-APP-88 temporary trees were removed after zero-holder checks, totaling 566 files and 578,359,296 allocated bytes; zero matching trees, test processes, launchd jobs, credential/token artifacts, or dependency-projection backups remain.

## Return to App HELP_HUMAN

Keep D-APP-88 Option B open as an accepted ruling with implementation blocked on the copied-main technique. The next lawful implementation path is a separately built full Electron helper target (or another explicitly scoped design), followed by a clean source-aligned package build and the complete D-APP-88 package/live proof. Selection or expansion beyond the existing App packaging authority remains with App `HELP_HUMAN` and the owner where judgment is required.

Ignored `frontend/dist/` may still contain derivative generated package output from the failed candidate. It is outside tracked integration state and must not be committed; it may be cleared during ordinary build-output housekeeping.
