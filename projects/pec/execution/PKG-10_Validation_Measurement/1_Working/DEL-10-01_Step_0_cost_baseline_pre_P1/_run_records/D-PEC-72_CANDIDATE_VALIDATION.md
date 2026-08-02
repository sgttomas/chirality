# D-PEC-72 — DEL-10-01 candidate validation

**Result:** COMPLETE CANDIDATE PASS; REVIEW AND OWNER FITNESS PENDING;
deliverable unaccepted and C-05 open.

## Bound artifacts

| Artifact | SHA-256 |
|---|---|
| `artifacts/STEP0_COST_BASELINE_METHOD.md` | `b02d010c2d8c7bf10a009cc88a22f3c6923e53069913af5688470f982acb6fa2` |
| `artifacts/STEP0_COST_BASELINE.md` | `1955bd6197b93be167cc5449683c860cae8a98a58967fb64f1354a98b65a82d9` |
| `_run_records/D-PEC-72_TOKEN_TELEMETRY_RERUN_2026-08-02.md` | `baa80859d40845cc1c2448342befcacc83fd3519dd34e9e9b00dceb6764f7f89` |
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
- Exact token arithmetic independently reproduced from five contributing
  session deltas: input `5,691,203`, cached-input subset `5,440,768`, output
  `22,436`, logical total `5,713,639`; uncached input is `250,435` and
  reasoning-output subset is `8,395`.
- Output path matches D-PEC-72 and this production commit is prepared as a
  PKG-10-only change set.

## Acceptance mapping

| Acceptance criterion | Candidate disposition | Evidence |
|---|---|---|
| AC-001 | PASS | Method defines the PEC-loop-only unit, `n = 1` baseline design, semantic interval, exact token boundary, and required capture fields. |
| AC-002 | PASS | Repeatability, unchanged post-P1 protocol, and limitations are explicit. |
| AC-003 | PASS | The rerun records one exact pre-P1 orientation with token count, UTC interval, corpus SHA, loop/scope, provider/runtime, model mix, and per-session evidence locators. No count was estimated. |
| AC-004 | PASS | Five-run `self-check` latency re-test cites the 2026-07-02 record, reports all values, and neither directs the harness nor opens its cache. |
| AC-005 | PASS | Classification inheritance is explicit; every statement is method, measured value, or declared limit, with no behavior requirement for another package. |
| AC-006 | PASS | Both packet-recorded artifacts exist and the prepared production change set is confined to PKG-10. |
| AC-007 | PASS | Both criteria are applied and reported separately; neither unit substitutes for the other. |
| AC-008 | PENDING OWNER | Exact candidate evidence now exists; only the accountable owner can confirm it is fit as the PRD §11 “before” leg and satisfies the pre-P1 obligation. |

## Failure isolation and next route

The exact-telemetry rerun resolved the producer-side AC-003 blocker without
changing the method or criteria. Route the complete candidate to formal REVIEW
and then to the owner for the separate AC-008 artifact-fitness ruling.
`_STATUS.md` remains `INITIALIZED`; C-05 remains open and no P1 node may start.
