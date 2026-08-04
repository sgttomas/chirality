# V2 author fan-in validation

- Verdict: `ACCEPTED_FOR_NEW_FRESH_REFUTATION`
- V1 status: immutable and rejected by first refutation
- V2 author return: `3566e9b2ea28fc0543007363ca3cbf0ab1b11a24792c8663fc312d724212e854`

## Frozen V2 review subject

| File | SHA-256 |
|---|---|
| `candidate_v2/AFFECTED_CLIENT_CENSUS_CANDIDATE_V2.md` | `2bff966d3806078472370cfd0e7f1546064660f325d4a0e2534a71a1a67c7d13` |
| `candidate_v2/DEGRADED_MODE_CONTRACT_COMPOSITE_CANDIDATE_V2.md` | `7f64cfd2ef567bbceab2d89046137b9d6fbf7ccd49920fa34a76f373547f9153` |
| `candidate_v2/EVIDENCE_AND_CUTOVER_PLAN_CANDIDATE_V2.md` | `d7c1838cf244595cb287173e44b073dfe73db2bdecd9b9946e851978ed89d95a` |
| `candidate_v2/OWNER_DECISION_RECORD_CANDIDATE_V2.md` | `2ce3aeae17212c87fa60f02c96ae5cbb0e6d3b9bf2f734417039178230af2e6c` |
| `candidate_v2/ROOT_COMPATIBILITY_CONTRACT_CANDIDATE_V2.md` | `cbe36a275bfe882c575673c8c70d8598b7f0c724b96fdf9ccae962a036677bc1` |
| `candidate_v2/ROOT_RECOVERY_SEMANTIC_CANDIDATE_V2.md` | `9b023b347dca4bd255e6c7f2fb499e5654d3ab455f90004be29dd1b545eaf5f8` |
| `application_trace_v2/SELECTION_APPLICATION_TRACE.md` | `bcea5d119dc84b56edf5c3ebeb4c3b1c0d6b4be9c0f54a4ffc044ff9b7877a5c` |

Manager checks reproduce exact 27-row order, six-file membership, allowed
tuple, no minted epoch, explicit pre-scan `RECOVERY_REQUIRED ->
RECOVERY_BLOCKED` transition, and exact all-six-member plus sorted V2 package
manifest binding. All original authority/no-effect boundaries remain present.
