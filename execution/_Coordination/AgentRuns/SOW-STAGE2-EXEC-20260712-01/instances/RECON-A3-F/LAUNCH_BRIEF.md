# RECON-A3-F Sealed Launch Brief — v1

Role: `RECONCILIATION` Agent 1. Run: `SOW-STAGE2-EXEC-20260712-01`.
Wave: `W-A3`. Accepted predecessors: `W-A3-PKG08_PASS`,
`W-A3-PKG09_PASS`, and `W-A3-PKG10_PASS` in `WORK_GRAPH.json` v27.

Independently reconcile the exact 16 accepted A3 derivative candidates across
APP-PKG-08, APP-PKG-09, and APP-PKG-10 against the accepted A3 preflight
snapshot and live read-only project state at
`main@193663b1d93299c18d64f59b543b36a0dd5f0ee1`. Reproduce package and child
manifests, candidate/source/status/control hashes, coverage and authority,
exact combined replacement and inverse rollback, registered App checks,
portability inventories and normalization proofs, disjoint ownership,
lifecycle, and zero project writes. Perform isolated apply and rollback
simulations for all 16 members without changing live project paths.

Expected aggregate basis: 16 members, 481 mappings, 4,985 source lines, 80
replacement rows, 80 rollback rows, 220 package-manifest bindings, 1,470
accepted child-manifest bindings, and 144 frozen live bindings. Reject partial,
dual-live, ambiguous, stale, nonportable, nonterminal, or non-reproducible
returns. Preserve and classify the package recovery histories, including the
DEL-10-02 malformed negative-fixture attempt and corrected proof, without
repairing package evidence.

Write only
`execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/W_A3/preintegration/**`
and exact terminal surfaces under
`execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/RECON-A3-F/**`.
Live project paths, package candidates/evidence, coordination predecessors,
Git, H1/H2, and `.claude-worktrees/` are read-only or excluded. Return `PASS`,
`BLOCKED_REMEDIATION_REQUIRED`, or `DECISION_REQUIRED` with an immutable
acceptance snapshot and explicit handoff state only if every fan-in gate passes.
