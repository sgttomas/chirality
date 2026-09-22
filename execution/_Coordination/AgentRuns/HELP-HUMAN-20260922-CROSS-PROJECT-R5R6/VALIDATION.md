# Shared validation and limits

These local checks cover the working candidate derived from `379df923927d157be3ebb51d8a1dcf783d970112`. Independent source manifests bind the final production/control bytes. The PR's required CI must separately cover its actual committed head. Raw local results are preserved in `validation/` with `LOG_BINDINGS.json`; they are not rewritten into an uninterrupted all-green history.

| Check | Observed result |
|---|---|
| `python3 -m pytest -q tools/practitioner_harness tools/validation` | Initial fan-in run: 897 passed, 48 subtests passed. Final run after the App receipt was appended: 896 passed, 48 subtests passed, one live self-check test failed on the new receipt's measurement-like wording. |
| Affected receipt test backcheck | After correcting the receipt, `test_live_baseline.py::test_live_self_check_reports_root_ratified_governance_and_exits_clean` passed. No test or validator was weakened. The correction was confined to the new receipt's wording; the other suite results remain applicable. |
| Practitioner-harness `self-check` after repair | Exit 0; no BLOCK. The report retains 14 INFO, 1 NOT_APPLICABLE, 4 REVIEW and 113 WARN findings. These are not represented as universal corpus cleanliness. |
| App and Piping loop-receipt validators | Both pass on the current append-only ledgers. |
| Claims-language validator | Pass; 356 governed surfaces scanned. |
| App `app_hold.py scan --require-register-match` | Pass; 54 contracts clear, no active holds, register matches. Register SHA `d289b248a900122b012ae540b9b197feae3adbe264bf181f3d46556c500f320c`; scan fingerprint `7bd56dd823f28427dd4bfb8ca65017b4fe9c0b8165fb32a702f896e49f8ba6ec`. |
| App final R6 backcheck | Pass after residual-field correction; all 3,568 rows accounted, 138 exact changed source keys, 54-file inverse reconstruction, 54-deliverable census and missing/duplicate negative controls. Root also matched all 195 independently reviewed production/control hashes and the 196-file final map including the receipt. |
| Piping final R6 backcheck | Pass; 1,721 changed references in 287 files, complete 102-deliverable census, missing/duplicate key and census negative controls reject. |
| Piping accounting and dependency mirror checks | Pass; all 9,889 claims, 2,234 H4 rows and 598 capabilities accounted; exactly 30 Status cells in 15 local mirrors, topology unchanged. |
| Root G0–G3 live guards | Pass; no new production or governance acceptance inferred. |
| App maintained secret-evidence scanner | Pass; 14,562 files scanned, zero blocked findings and 30 allowed fixture findings. An initial attempted invocation used a nonexistent filename and ran no scan; the recorded pass is from `frontend/scripts/scan-secret-evidence.mjs` with output under `/tmp`. |

Both projects' SoW structure, exact replay/re-extraction, source-key multiset and historical preservation checks are in their frozen R5/R6 evidence. Independent source and integration review are recorded separately under `reviews/`. Coverage accounting is not semantic acceptance. No local product, native UI, signing, notarization or engineering qualification result is asserted. The product-code-only Piping evidence-sweep trigger does not apply to this record-only change.

Conflict-marker and instruction-tranche range checks are run against the committed PR candidate and recorded in the PR before merge. Required CI and the final Git state belong to that candidate's PR record, avoiding a circular claim that an uncreated commit was already tested.
