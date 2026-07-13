# HELPS-C2R-R2 Launch Brief — v1

Role: `HELPS_HUMANS` (Agent 1 exact-authority edge repair)

## Objective

Close the whitespace-normalization defect relayed from C2A-R1 review. Root
format resolution and conversion must compare the supplied migration
authority byte-for-byte to
`D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176`. Leading or trailing
whitespace must fail closed even when `ScopeOfWork.md` binds the exact ruled
marker. Do not normalize the authority before authorization.

## Basis and exact write scope

Read D-GOV-16 items 4/8, C2F-REMEDIATION-001 clarifications 001-A/001-B,
C2R-R1 return, and the relayed C2A-R1 reviewer finding.

Only:

- `tools/scope_of_work/common.py`
- `tools/scope_of_work/convert_four_documents_to_scope_of_work.py`
- `tools/scope_of_work/test_scope_of_work_tools.py`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/P2_ROOT/**`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/HELPS-C2R-R2/**`

No child delegation. Preserve every other dirty path.

## Acceptance

Add a regression whose candidate marker is the exact ruled value while the
supplied authority has leading/trailing whitespace; converter and resolver
must refuse it and emit no output. Exact unpadded authority must continue to
pass. ISSUED accepted-basis behavior and all C2R-R1 gates remain green. Run
focused Scope-of-Work tests, full root tools, compile, diff hygiene, exact
containment, and refresh C2R evidence/hashes.

No project/deliverable/control/status/lifecycle/Git/release/H1/H2/retirement
action. Write terminal `PASS | PARTIAL | BLOCKED | DECISION_REQUIRED` return
and status with blockers and rerun requirements.
