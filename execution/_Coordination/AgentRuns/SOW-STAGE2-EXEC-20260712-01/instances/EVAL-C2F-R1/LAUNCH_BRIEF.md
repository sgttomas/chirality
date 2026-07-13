# EVAL-C2F-R1 Launch Brief — v1

Role: `EVALUATION` (Agent 1 independent read-only remediation evaluation)

## Objective

Independently determine whether C2R-R1/R2 and C2A-R1 close every original C2F
blocker and satisfy the accepted C2 consumer gate. Use the same frozen basis
and questions as EVAL-C2F plus C2F-REMEDIATION-001 and all remediation
returns/evidence/current hashes. Preserve original findings; mark them closed
only with direct current evidence.

Evaluate exact caller coverage and containment; raw equality to
`D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176`; refusal of unruled,
alternate, padded, malformed, missing, mismatched, non-isolated, wrong-path,
invalid, partial, ambiguous, and misleading requested states; mandatory
ISSUED accepted-basis/source/status bindings; root C2A terminal pointer; and
all current root/App/exports/build/self-check/practitioner/premerge evidence.
No scoring or child delegation. Direct targeted diagnostics only; do not rerun
expensive suites unless current evidence is missing or disputed.

## Writes and denial

Only:

- `execution/_Evaluation/SOW-STAGE2-EXEC-20260712-01/C2F-R1/**`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/EVAL-C2F-R1/RETURN.md`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/EVAL-C2F-R1/STATUS.json`

No subject/snapshot/Git/project-state/lifecycle/release/H1/H2/retirement write.
Return terminal `PASS | PARTIAL | BLOCKED | DECISION_REQUIRED` with findings,
coverage, unknowns, blocker closure, reruns, and next owner.
