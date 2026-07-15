# VERIFY-B1 Focused Checks

Verdict: `PASS_WITH_ACCEPTED_BASELINE_FINDINGS`

| Check | Result | Evidence |
|---|---|---|
| SOW tool regression module | PASS | 19 passed in 2.63 s |
| Dependency schema, DEL-11-01 | PASS | 29 required columns, 20 data rows |
| Dependency schema, DEL-11-02 | PASS | 29 required columns, 15 data rows |
| Dependency schema, DEL-11-03 | PASS | 29 required columns, 12 data rows |
| Dependency schema, DEL-11-04 | PASS | 29 required columns, 17 data rows |
| Dependency schema, DEL-11-05 | PASS | 29 required columns, 11 data rows |
| Practitioner harness self-check | PASS_WITH_BASELINE_FINDINGS | INFO=15, NOT_APPLICABLE=2, REVIEW=27, WARN=6; same repository-level classes as accepted preflight, with no candidate-specific finding |
| Practitioner harness pytest | PASS | 264 passed in 30.23 s |

The self-check findings are pre-existing repository-level governance/path/reference observations outside this verifier's write and acceptance scope. They were not repaired, waived, or reclassified. Exact candidate/live post-hashes and complete five-member evidence show no new package-local discrepancy.
