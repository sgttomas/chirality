# RECON-C2F-R1 Launch Brief — v1

Role: `RECONCILIATION` (Agent 1 read-only remediation fan-in)

## Objective and basis

Rerun the C2 consumer reconciliation after HELPS-C2R-R1/R2 and
WORKING-C2A-R1. Preserve the original BLOCKED C2F package as immutable
upstream evidence. Read D-GOV-16, accepted Stage-2 plan, P0/P1 snapshots,
original C2R/C2A returns, original RECON/EVAL/REVIEW C2F packages,
C2F-REMEDIATION-001, all remediation returns/evidence, root C2A pointer, and
the current live candidate diff on `main@e150c972889d05a8fc270239451a35c7512dc9a9`.

Verify 64/64 root and 9/9 App caller classification, exact contained/disjoint
source sets, final hashes, zero governed project-state writes, SOW/legacy
success, exact ruled raw authority success, and fail-closed synthetic,
alternate, padded, malformed, missing, mismatched, non-isolated, wrong-path,
invalid, partial, ambiguous, and requested-format cases. Verify ISSUED
preparation now requires and embeds accepted basis plus source/status
bindings, remains lifecycle-neutral, and does not satisfy H1. Validate all
current root/App/check/export evidence and separate schema, content/authority,
preservation, and substrate. No child delegation.

## Writes

Only:

- `execution/_Reconciliation/DeliverableConcordance/SOW-STAGE2-EXEC-20260712-01-C2F-R1/**`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/RECON-C2F-R1/RETURN.md`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/RECON-C2F-R1/STATUS.json`

No subject, snapshot, Git, deliverable/control/status/lifecycle/receipt,
release, H1/H2, or legacy-retirement write.

Return `PASS | PARTIAL | BLOCKED | DECISION_REQUIRED` with exact evidence,
blocker closure, remaining blockers, reruns, and next owner. Any unresolved
authority, accepted-basis, caller, containment, or required-check issue blocks
C2G.
