# RECON-C2F Launch Brief — v1

Role: `RECONCILIATION` (Agent 1, read-only consumer fan-in)

## Objective

Independently reconcile the completed C2R root lane and C2A App runtime lane
against the accepted D-GOV-16 Stage-2 consumer-activation contract. Determine
whether every active caller is dispositioned, changed paths are contained and
disjoint, legacy compatibility is retained, and no governed deliverable,
control, status, lifecycle, receipt, or release surface was modified.

## Accepted basis

- D-GOV-16 ruling and accepted Stage-2 work plan/graph.
- `snapshots/P0_BASIS/` and `snapshots/P1_CANON/POSTMERGE_HANDOFF.md`.
- `basis/CALLER_MANIFEST.tsv` (64 root active caller rows).
- `candidates/P2_ROOT/` and `instances/HELPS-C2R/RETURN.md`.
- App package run
  `projects/chirality-app-dev/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01-C2A/`
  and root pointer `instances/WORKING-C2A/`.
- Live dirty candidate diff on synchronized main `e150c972889d05a8fc270239451a35c7512dc9a9`.

## Scope and method

Read all returned manifests, changed-path lists, behavior/check matrices,
review correction evidence, and current diffs. Reproduce counts and hashes
where useful. Classify outcomes separately as schema, content, preservation,
and substrate. Verify 64/64 root and 9/9 App caller classification, zero
unclassified caller, exact write containment, disjoint root/App ownership, and
fail-closed behavior for missing, partial, ambiguous, unauthorized dual, and
invalid states. Verify SOW-only and retained legacy paths remain supported.

No child delegation. This is a bounded R3-style synthesis under the adopted
Stage-2 activation; it is not a new full concordance run and does not enter R4
or R5.

## Writes

Only:

- `execution/_Reconciliation/DeliverableConcordance/SOW-STAGE2-EXEC-20260712-01-C2F/**`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/RECON-C2F/RETURN.md`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/RECON-C2F/STATUS.json`

These are derivative run evidence. Do not write the parent-owned
`snapshots/P2_CONSUMERS/` fan-in snapshot.

## Denied

All subject-source edits; deliverable/control/status/lifecycle/receipt writes;
Git/branch/commit/PR/merge operations; release actions; H1/H2 actions;
provider/network changes; repair tranches; legacy retirement.

## Required return

`PASS | PARTIAL | BLOCKED | DECISION_REQUIRED`, evidence-linked counts,
containment/disjointness verdict, compatibility/fail-closed verdict,
classification of any substrate conditions, blockers, rerun requirements,
and next owner. A new/unclassified caller, ownership overlap, source write,
unexplained failed check, or semantic authority conflict blocks C2G.
