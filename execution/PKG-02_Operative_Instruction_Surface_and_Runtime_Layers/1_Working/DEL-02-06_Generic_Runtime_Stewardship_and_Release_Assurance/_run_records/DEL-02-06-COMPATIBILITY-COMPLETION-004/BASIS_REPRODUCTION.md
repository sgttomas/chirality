# Basis reproduction — compatibility completion 004

- Verdict: `PASS`
- Repository basis: `1b375af4f1219ecfc00fc2755854aa7fd4220901`
- Accepted Scope of Work: `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146`
- Pre-activation `_STATUS.md`: `3fedf815696ffd753a1dd83f2fbe23dcc57101acc34c0a700f32e074cc5d9b67`
- `_DEPENDENCIES.md`: `21261de261dfdbc077cb14df103fd7074b7b8785da58b56318e7d4e06ef0506f`
- Accepted semantic snapshot: `3fc56807c4cd83fd2b5f967848b770adfd226541880629493ddfe8ad3df989aa`
- Accepted six-member package manifest:
  `6005a00695a96eb46e59896f01653d3504ef85b35a7d28509bba8d33171425e2`
- Accepted member-verification manifest:
  `e1f841d808e73642e28a6dec0b19adfdcf0e0c4800b6541701a9d8e7ee6a2874`

## Six accepted members reproduced

| Member | SHA-256 | Result |
|---|---|---|
| `AFFECTED_CLIENT_CENSUS_CANDIDATE_V2.md` | `2bff966d3806078472370cfd0e7f1546064660f325d4a0e2534a71a1a67c7d13` | `PASS` |
| `DEGRADED_MODE_CONTRACT_COMPOSITE_CANDIDATE_V2.md` | `7f64cfd2ef567bbceab2d89046137b9d6fbf7ccd49920fa34a76f373547f9153` | `PASS` |
| `EVIDENCE_AND_CUTOVER_PLAN_CANDIDATE_V2.md` | `d7c1838cf244595cb287173e44b073dfe73db2bdecd9b9946e851978ed89d95a` | `PASS` |
| `OWNER_DECISION_RECORD_CANDIDATE_V2.md` | `2ce3aeae17212c87fa60f02c96ae5cbb0e6d3b9bf2f734417039178230af2e6c` | `PASS` |
| `ROOT_COMPATIBILITY_CONTRACT_CANDIDATE_V2.md` | `cbe36a275bfe882c575673c8c70d8598b7f0c724b96fdf9ccae962a036677bc1` | `PASS` |
| `ROOT_RECOVERY_SEMANTIC_CANDIDATE_V2.md` | `9b023b347dca4bd255e6c7f2fb499e5654d3ab455f90004be29dd1b545eaf5f8` | `PASS` |

Both the source package manifest and the accepted member-verification
manifest verified all six members. The accepted historical member directory
has no diff from the repository basis. It remains read-only.

## Activation preconditions

- Lifecycle state is `INITIALIZED`; no lifecycle transition is authorized.
- No DEL-02-06 dependency edge is declared.
- No Root-local `software-workflow.json` exists. The three tracked profiles
  are beneath separately governed App, PEC, and Piping project roots and are
  not borrowed.
- The owner supplied canonical positive-decimal epoch `1`, yielding candidate
  identity `root-runtime-1`, and authorized preparation only.
- Write containment is the new run root, the narrow REM-001 status
  disposition, and the supervising instance return/status files.

N0 fan-in gate passes. N1 authorship is released.
