# RECON-A2-F Sealed Launch Brief — v1

Role: `RECONCILIATION` Agent 1. Run: `SOW-STAGE2-EXEC-20260712-01`.
Wave: `W-A2`. Accepted predecessors: `W-A2-PKG04_PASS`,
`W-A2-PKG05_PASS`, and `W-A2-PKG06_PASS` in `WORK_GRAPH.json` v17.

Independently reconcile the exact 16 accepted A2 derivative candidates across
APP-PKG-04, APP-PKG-05, and APP-PKG-06 against the accepted A2 preflight
snapshot and live read-only project state at
`main@0af23f4709e1c95f6b2e0f19db80779bd4c968fa`. Reproduce package and child
manifests, candidate/source/status/control hashes, coverage and authority,
exact combined replacement and inverse rollback, registered App checks,
portability inventories/normalization proofs, disjoint ownership, lifecycle,
and zero project writes. Perform isolated apply and rollback simulations for
all 16 members without changing live project paths.

Expected aggregate basis: 16 members, 491 mappings, 5,584 source lines, 80
replacement rows, 80 rollback rows, and 208 package-manifest bindings. Reject
partial, dual-live, ambiguous, stale, nonportable, nonterminal, or
non-reproducible returns. Record findings without repairing package evidence.

Write only
`execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/W_A2/preintegration/**`
and exact terminal surfaces under
`execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/RECON-A2-F/**`.
Live project paths, package candidates/evidence, coordination predecessors,
Git, H1/H2, and `.claude-worktrees/` are read-only or excluded. Return
`PASS`, `BLOCKED_REMEDIATION_REQUIRED`, or `DECISION_REQUIRED` with an immutable
acceptance snapshot and explicit handoff state only if every fan-in gate passes.
