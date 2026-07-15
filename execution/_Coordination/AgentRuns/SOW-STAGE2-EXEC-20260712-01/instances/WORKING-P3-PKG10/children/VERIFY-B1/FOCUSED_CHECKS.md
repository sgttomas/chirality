# VERIFY-B1 Focused Checks

Verdict: `PASS_WITH_ACCEPTED_BASELINE_FINDINGS`

| Check | Result | Evidence |
|---|---|---|
| SOW tool regression module | PASS | `python3 -m pytest -q tools/scope_of_work/test_scope_of_work_tools.py`: 19 passed in 2.73 s |
| Dependency schema, DEL-10-01 | PASS | 29 required columns, 14 data rows |
| Dependency schema, DEL-10-02 | PASS | 29 required columns, 18 data rows |
| Dependency schema, DEL-10-03 | PASS | 29 required columns, 20 data rows |
| Dependency schema, DEL-10-04 | PASS | 29 required columns, 20 data rows |
| Dependency schema, DEL-10-05 | PASS | 29 required columns, 29 data rows |
| Practitioner harness self-check | PASS_WITH_BASELINE_FINDINGS | Completed with the same repository-level baseline finding classes recorded by accepted W-P3 preflight; no candidate-specific finding or new blocker |
| Practitioner harness pytest | PASS | 264 passed in 31.88 s |

The self-check findings concern pre-existing cross-repository governance/path/reference surfaces outside this verifier's write and acceptance scope. They were not repaired, waived, or reclassified. The exact candidate/live post-hashes and five-member method evidence show no new package-local discrepancy.
