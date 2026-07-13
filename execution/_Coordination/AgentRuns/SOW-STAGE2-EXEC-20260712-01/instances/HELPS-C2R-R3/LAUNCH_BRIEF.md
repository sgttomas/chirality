# HELPS-C2R-R3 Launch Brief — v1

Role: `HELPS_HUMANS` (Agent 1 checklist authority-input repair)

## Objective

Close the exact padded-authority bypass reproduced by EVAL-C2F-R1 in the
registered checklist caller. `derive_review_checklist.py` must pass the raw
supplied `--migration-authority` to the resolver and must not emit an output
artifact for leading/trailing whitespace, even when the candidate binds the
exact ruled marker. Exact unpadded authority and SOW-only behavior must remain
deterministic and unchanged.

## Basis and exact write scope

Read D-GOV-16 items 3/4/8, C2F-REMEDIATION-001 clarification 001-C,
EVAL-C2F-R1 reproduced evidence, C2R-R2 return, and REVIEW-C2F-R1 return.

Only:

- `tools/scope_of_work/derive_review_checklist.py`
- `tools/scope_of_work/test_scope_of_work_tools.py`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/P2_ROOT/**`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/HELPS-C2R-R3/**`

No child delegation. Preserve every other dirty path.

## Acceptance

Add an end-to-end regression with exact marker plus padded supplied authority;
the checklist command must fail and the requested output file must not exist.
Exact unpadded dual and SOW-only checklist derivation must still pass with
byte-stable item ordering/text/linkage. Run focused Scope-of-Work tests, full
root tools, compile, diff hygiene, exact containment, and refresh root evidence
and hashes.

No App/project/deliverable/control/status/lifecycle/Git/release/H1/H2/
retirement action. Write terminal `PASS | PARTIAL | BLOCKED |
DECISION_REQUIRED` RETURN and STATUS with blockers and rerun requirements.
