# D-PEC-72 — DEL-10-01 candidate validation

**Result:** METHOD/LATENCY CANDIDATE PASS; TOKEN BASELINE BLOCKED; deliverable
unaccepted and C-05 open.

## Bound artifacts

| Artifact | SHA-256 |
|---|---|
| `artifacts/STEP0_COST_BASELINE_METHOD.md` | `b02d010c2d8c7bf10a009cc88a22f3c6923e53069913af5688470f982acb6fa2` |
| `artifacts/STEP0_COST_BASELINE.md` | `d826e4eaa68849fb2950715066e129f8657f254593ee90bd0d57f209849116f9` |
| `ScopeOfWork.md` | `40d47fb636ca72e52213929b2337dbbc3a02f0f7c073758c996f5d651e1a5a7e` |

Accepted bases: PRD v2.2
`6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba`;
decomposition revision 1.3
`3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787`.

## Gate and checks

- Reliance-hold entry preflight, `dispatch-for-production`: `ALLOW`.
- Reliance-hold fan-in preflight, `candidate-validation`: `ALLOW`.
- `validate_scope_of_work.py`: `PASS`, format `SOW_V1`.
- Derived REVIEW checklist: eight `AC-*` items, all mapped.
- Latency arithmetic independently reproduced: mean `2.854 s` from the five
  recorded observations; median `2.78 s`, range `2.64..3.34 s`.
- Method and report distinguish tokens from command latency and prohibit
  estimates, substitution, or fabricated zeroes.
- Output path matches D-PEC-72 and this production commit is prepared as a
  PKG-10-only change set.

## Acceptance mapping

| Acceptance criterion | Candidate disposition | Evidence |
|---|---|---|
| AC-001 | PASS | Method defines the PEC-loop-only unit, `n = 1` baseline design, semantic interval, exact token boundary, and required capture fields. |
| AC-002 | PASS | Repeatability, unchanged post-P1 protocol, and limitations are explicit. |
| AC-003 | **BLOCKED** | The eligible orientation has `NOT_OBSERVED` token fields because the task/runtime exposed no exact per-call usage ledger or interval timestamps. No count was estimated. |
| AC-004 | PASS | Five-run `self-check` latency re-test cites the 2026-07-02 record, reports all values, and neither directs the harness nor opens its cache. |
| AC-005 | PASS | Classification inheritance is explicit; every statement is method, measured value, or declared limit, with no behavior requirement for another package. |
| AC-006 | PASS | Both packet-recorded artifacts exist and the prepared production change set is confined to PKG-10. |
| AC-007 | PASS | Both criteria are applied and reported separately; neither unit substitutes for the other. |
| AC-008 | BLOCKED/PENDING OWNER | No exact token baseline exists for the owner to accept as the PRD §11 “before” leg. |

## Failure isolation and rerun

The method and latency evidence remain valid candidate work. The token-capture
failure holds DEL-10-01 and the C-05 fan-in only; it does not invalidate the
PKG-00 candidates. Rerun when a runtime supplies exact per-call input,
cached-input, and output usage plus an interval locator for a fresh PEC-loop
orientation. `_STATUS.md` remains `INITIALIZED`; no P1 node may start.
