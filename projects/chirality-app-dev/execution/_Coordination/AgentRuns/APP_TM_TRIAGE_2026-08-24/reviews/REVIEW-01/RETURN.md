# REVIEW return — App v3 G0 Task Management triage preparation

- RunID: `APP_TM_TRIAGE_2026-08-24`
- Instance: `REVIEW-01`
- Review type: `INDEPENDENT_VERIFICATION`
- Basis: `8884b143f3d8dbca49756e981e4e20299d55875d`
- Verdict: `RETURN_FOR_REPAIR`
- Findings: `1 MAJOR`
- Subject modified by reviewer: `NO`
- Repair required: `YES`

RF-001 requires full exact path/SHA bindings for three material claims currently represented only by packet-unique abbreviations:

1. acceptance-005 snapshot `f497cbbd...` in `OWNER_TRIAGE_SHEET.md`;
2. SCA-APP-008 Carrier Map `72a1b55b...` in the owner triage and Electron candidate; and
3. Root graceful-stop notice `1029648d...` in the staleness/closure echo.

The independently verified full values and exact repair targets are enumerated in `REVIEW.md`. After repair, update changed packet/run/Receipt-201 hashes, rerun all required gates, and send the result to a fresh reviewer. Preserve the hypothetical CSV post-image as an exact 12-cell `LastReviewed`-only diff and do not alter any live register or other governed surface.

All other reviewed areas passed: required row population, no-disposition calibration, Electron D-APP-98 successor handling plus distinct G1 concordance, both notice-adoption option sets, all seven OPEN-row SourceSha/staleness conclusions, exact CSV mechanics, federation, receipt structure/current hashes, write containment, candidate whitespace, receipt validation, Task Management register validation, and `git diff --check`.
