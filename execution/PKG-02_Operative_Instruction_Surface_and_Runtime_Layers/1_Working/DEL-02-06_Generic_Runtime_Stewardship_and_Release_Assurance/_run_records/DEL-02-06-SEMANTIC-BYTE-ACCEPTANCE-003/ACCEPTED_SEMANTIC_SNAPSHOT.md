# Accepted semantic snapshot — DEL-02-06 OWNER_SELECTION_V2

- Snapshot status: `HUMAN_ACCEPTED_SEMANTIC_BYTES`
- Effective acceptance date: `2026-08-03`
- Accountable human: `Ryan Tufts`
- Authority transcript SHA-256:
  `6396dd26c3fb8b6ed922c1cb7da584f67a08188d5b27525d650bf3ca1560c566`
- Accepted package manifest SHA-256:
  `6005a00695a96eb46e59896f01653d3504ef85b35a7d28509bba8d33171425e2`
- Accepted member-verification manifest:
  `ACCEPTED_SEMANTIC_MEMBERS.sha256`
- Source candidate run: `DEL-02-06-SEMANTIC-CANDIDATE-002`
- Source version: `OWNER_SELECTION_V2`
- Carried finding: `REFUTER-V2-F01 — NON_SEMANTIC, REPAIRED OUTSIDE THE SIX-MEMBER MANIFEST`

## Accepted exact bytes

| Member | SHA-256 |
|---|---|
| `AFFECTED_CLIENT_CENSUS_CANDIDATE_V2.md` | `2bff966d3806078472370cfd0e7f1546064660f325d4a0e2534a71a1a67c7d13` |
| `DEGRADED_MODE_CONTRACT_COMPOSITE_CANDIDATE_V2.md` | `7f64cfd2ef567bbceab2d89046137b9d6fbf7ccd49920fa34a76f373547f9153` |
| `EVIDENCE_AND_CUTOVER_PLAN_CANDIDATE_V2.md` | `d7c1838cf244595cb287173e44b073dfe73db2bdecd9b9946e851978ed89d95a` |
| `OWNER_DECISION_RECORD_CANDIDATE_V2.md` | `2ce3aeae17212c87fa60f02c96ae5cbb0e6d3b9bf2f734417039178230af2e6c` |
| `ROOT_COMPATIBILITY_CONTRACT_CANDIDATE_V2.md` | `cbe36a275bfe882c575673c8c70d8598b7f0c724b96fdf9ccae962a036677bc1` |
| `ROOT_RECOVERY_SEMANTIC_CANDIDATE_V2.md` | `9b023b347dca4bd255e6c7f2fb499e5654d3ab455f90004be29dd1b545eaf5f8` |

These exact six bytes are now the human-accepted DEL-02-06 semantic basis for
the selected recovery, compatibility, degraded-mode, affected-client,
evidence/cutover, and owner-decision surfaces. The accepted package remains
checkout-contained at its immutable source paths; this snapshot binds rather
than duplicates those bytes.

## Trace repair disposition

Commit `2b6d53027ea10374dd515a4a5a203f8ed4cf2f04` repaired only the two DEL-02-06
application-trace prose links from `candidate/` to `candidate_v2/`. The current
trace SHA-256 is
`0f49b9f9f6fa89e5a1a1d8e40d08d2fa0f6b7efe5bba237839cf9d74ba9bd564`.
The trace is outside the six-member accepted manifest, and the signed owner
return expressly requires no package regeneration. The carried finding is
therefore recorded as `REPAIRED_NON_SEMANTIC_NO_REGENERATION`.

## Preserved unresolved and authority boundaries

- TBD-001 supplies grammar only; the exact Root compatibility epoch remains a
  future owner-supplied value and no identity is minted by this acceptance.
- The complete future compatibility binding manifest remains unproduced and
  unaccepted.
- PEC remains `UNRESOLVED` with no work, dependency, veto, classification, or
  prescribed outcome.
- App retains its implementation, presentation, retained-function,
  conformance, and evidence ownership.
- Piping remains `NOT_AFFECTED` on current evidence.
- Tier-0 remains preparation/routing only; no relationship record is adopted.
- N3 remains `DESIGN_COMPLETE_NOT_EXECUTED`; semantic acceptance is not test
  execution or evidence acceptance.

## No implied downstream act

This semantic acceptance does not authorize implementation, source/test or
contract edits, software checks, affected-client work, compatibility repin,
cutover, lifecycle, release, publication, reliance, Git, PR, merge, notice,
register/receipt, dependency, or foreign-loop action. Each remains behind its
separate gate.
