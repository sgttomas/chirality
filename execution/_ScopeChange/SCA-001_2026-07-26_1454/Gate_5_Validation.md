# SCA-001 Gate 5 Validation

Date: 2026-07-26  
State: `CONFIRMED`

## Exact-byte application

The accepted revision 1.0 hashes matched
`Pre_Change_Register_Baseline.json` immediately before application.
`validate_gate3_candidate.py` then passed 50/50 checks. The seven authoritative
surfaces were replaced only by copying the approved Gate 3 candidate bytes.

`Applied_File_Hashes.json` proves for each surface that:

- the predecessor SHA-256 matches the Gate 1 baseline;
- the candidate SHA-256 matches `Gate_3_Validation.json`; and
- the applied SHA-256 equals the approved candidate SHA-256.

No semantic text was regenerated during application.

## Deterministic register result

`validate_gate5_applied.py` passes 45/45 checks:

- 104 scope items: 95 IN, 9 OUT, 0 TBD;
- 6 packages;
- 46 deliverables;
- 7 objectives;
- 85 forward-coverage rows;
- 52 reverse-trace rows;
- unique scope, deliverable, and objective IDs;
- all package, deliverable, scope, objective, forward, and reverse references
  resolve;
- all IN scope items have one resolving package and at least one resolving
  deliverable;
- `SOW-104 → PKG-02 → DEL-02-06 → OBJ-001/2/4/7`;
- O-11 is uniquely forward-covered;
- DEL-02-06 is reverse-traced;
- DEL-02-02 predecessor semantics are preserved through Gate 3 proof plus
  Gate 5 candidate/applied hash parity;
- category and context-envelope counts match the approved candidate; and
- the observed write set is limited to approved decomposition, SCA, and
  AUDIT_DECOMP evaluation surfaces.

## Post-change AUDIT_DECOMP

Valid immutable snapshot:

`execution/_Evaluation/DecompCoverage/COV_SCA001_POSTCHANGE_2026-07-26_2159/`

Coverage-summary SHA-256:

`bbc4eb8c45a66b0fafa54c7b6b3d31f5b8e86a911f3d60f696a6a6f021a0a26e`

| Measure | Result |
|---|---|
| Overall status | `BLOCKERS` |
| Closure readiness | `FAIL` |
| Findings | 1 BLOCKER / 0 WARNING / 132 INFO |
| Packages | 6/6 |
| Deliverables | 45/46 |
| Existing contexts | 45/45 match |
| Existing SOW contracts | 45/45 valid |
| Active SCA snapshot | PASS |
| Objective/register integrity | PASS |

The sole blocker is the protocol-required forward-coverage finding for the
absent DEL-02-06 scaffold. This is the expected downstream derivative gap
reserved to PROJECT_SETUP by the approved propagation plan. The audit finding
is retained as `AuditState=BLOCKED`; it is not reclassified or repaired inside
SCOPE_CHANGE.

The unpointed `COV_SCA001_POSTCHANGE_2026-07-26_2158/` attempt exposed a
context-parser defect and falsely emitted 45 warnings. It remains immutable
invalid-run residue, is excluded from reliance, and must not be staged.

## Root guard and path checks

Executed with the repository's configured `python` interpreter:

- G0 materialization fence: PASS;
- G1 harness adapter: PASS at the unchanged 45-status-file baseline;
- G2 surface ownership: PASS with the unchanged six package entries;
- G3 work graph: PASS with six nodes and no active node;
- path-anchor scan: 1,100 files checked, 0 findings; and
- targeted pytest suites: 122 passed.

These results do not imply downstream state is current for revision 1.1.
PROJECT_SETUP must later scaffold DEL-02-06 and refresh G1/G2/G3 under the
accepted Git basis.

## Formatting check

`git diff --check` reports three trailing-whitespace findings on the newly
changed CSV records for SOW-104, PKG-02 reverse trace, and DEL-02-06. They are
the CRLF record terminators in the exact owner-approved candidate bytes.
Normalizing them would change the approved SHA-256 identities, so Gate 5
preserved them and records this as an exact-byte formatting warning.

All other changed-path and deterministic checks pass.

## Gate 5 disposition

Ryan Tufts confirmed the post-change state in session on 2026-07-26 and
accepted decomposition revision 1.1 as the current basis. SCA-001 is closed
for scope change only. PROJECT_SETUP remains blocked until separate CHANGE Git
closeout; runtime work, SOW authoring, and client-scope work remain
unauthorized.
