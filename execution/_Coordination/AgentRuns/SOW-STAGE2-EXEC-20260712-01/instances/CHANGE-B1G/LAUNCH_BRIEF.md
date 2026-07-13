# CHANGE-B1G Sealed Launch Brief — v1

Role: `CHANGE` Agent 1

Objective: integrate the accepted B1/G3 evidence-only tranche, verify required
remote checks, merge under HUMAN-STEER-001, synchronize main, and record the
terminal evidence handoff. This is Git closeout only.

Accepted basis: D-GOV-16; Stage-2 B1 contract; main
`9349594530dc19e55baf9c2ef0b7eb4716f48a17`; ORCHESTRATOR-B1 PASS;
RECON-B1 PASS; `P3_MANIFEST/ACCEPTANCE.md`; blanket merge approval in
`HUMAN-STEER-001`.

Read scope: exact B1/P3, ORCHESTRATOR-B1, RECON-B1, work-graph, Git/ref/PR,
and applicable CI state. Do not read or modify `.claude-worktrees/`.

Write/Git scope: only the current B1 evidence outputs under
`instances/{ORCHESTRATOR-B1,RECON-B1,CHANGE-B1G}/`, `snapshots/P3_MANIFEST/`,
`execution/_Reconciliation/DeliverableConcordance/SOW-STAGE2-EXEC-20260712-01-B1/`,
and root `WORK_GRAPH.json`; a dedicated `codex/sow-stage2-b1` branch, ordinary
commits, PR, merge, synchronized main, and terminal CHANGE-B1G return/status.

No project, source, control, `_STATUS.md`, lifecycle, canon, caller, tool,
deliverable, conversion, receipt, release, H1/H2, ISSUED integration, or legacy
retirement write is authorized. Do not rewrite history or force push.

Required gates:

1. Begin from exact synchronized main basis with tracked state containing only
   the declared B1 outputs and untouched `.claude-worktrees/`.
2. Verify both P3 manifests, ORCHESTRATOR/RECON terminal contracts, 154-row
   byte equality, zero comparison deltas, JSON/CSV/TSV structure, accepted
   hashes, portability, exact changed-path containment, and diff hygiene.
3. Create `codex/sow-stage2-b1` from the exact basis; stage only authorized B1
   evidence and CHANGE records; create ordinary evidence commit(s), push, and
   open a PR to main.
4. Verify remote head/path inventory and mergeability. Wait for all required
   checks. Merge only when required checks PASS, using the recorded blanket
   approval.
5. Synchronize local main, origin/main, and remote main with divergence 0/0.
   Write terminal RETURN/STATUS and a CHANGE-B1G postmerge handoff under its
   instance directory, then bind those records with an ordinary evidence-only
   commit/push if needed. Final refs must again be equal and tracked-clean
   except `.claude-worktrees/`.

Return contract: `PASS` or exact blocker; branch/commit/PR/check/merge/final
main identities; exact path inventory; validation and containment results;
blockers/unknowns/waivers; rerun/rollback; next lawful owner HELP_HUMAN for
pilot release. No Git success itself accepts lifecycle or authorizes H1/H2.
