# HELPS-C2G-P1 Sealed Launch Brief — v1

Role: `HELPS_HUMANS` Agent 1 manager

Objective: repair the C2G App evidence portability defect exactly as authorized
by `amendments/C2G-EVIDENCE-PORTABILITY-001.md`, without changing source,
semantics, verdicts, counts, authority, or lifecycle state.

Accepted basis: D-GOV-16; P2_CONSUMERS C2F-R2 PASS; PR #221 source head
`42c347ad8e75d95ea4605868463a0380f682d69f`; failed governance-harness run
`29235554306`; `HUMAN-STEER-001`; `C2G-EVIDENCE-PORTABILITY-001`.

Read scope: the amendment; the twelve named evidence files; P2_CONSUMERS
manifest and handoff; CHANGE-C2G records; applicable governance-harness tests
and path-normalization conventions; Git diff/status. Do not read or modify
`.claude-worktrees/`.

Write scope: only the twelve evidence files named in the amendment and
`instances/HELPS-C2G-P1/{RETURN.md,STATUS.json}`. The parent owns the amendment,
work graph, integration records, Git, PR, and postmerge handoff.

Tools: read, bounded shell diagnostics, deterministic validators, and
`apply_patch` or an exact deterministic bulk substitution for the single
literal prefix. No delegation is needed. No Git staging, commit, push, PR,
merge, source, canon, deliverable, lifecycle, H1/H2, release, or retirement
action is authorized.

Required method and acceptance checks:

1. Prove the literal prefix occurs only in the declared twelve-file write
   scope within the two App run roots before editing.
2. Replace only `/Users/ryan/ai-env/projects/chirality` with `~`.
3. Prove the literal prefix is absent from both App run roots and changed paths
   are exactly the declared twelve evidence files plus manager return/status.
4. Search accepted manifests and records for downstream hashes of the twelve
   pre-edit files; if a binding exists, stop and report it rather than silently
   changing its owner.
5. Run `python3 -m pytest tools/practitioner_harness -q` and the focused live
   self-check and GEN8 tests implicated by CI; require PASS with REVIEW restored
   to 27 and GEN8 restored to its accepted 24-file baseline.
6. Run `git diff --check` over the working-tree change.

Return contract: `PASS`, `BLOCKED`, or `DECISION_REQUIRED`; exact before/after
occurrence counts; exact changed paths; exact commands/results; hash-binding
assessment; confirmation that no evidence semantics changed; rerun triggers;
remaining blockers; next lawful owner. `STATUS.json` must be terminal and
machine-readable.
