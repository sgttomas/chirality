# CHANGE-B1G Postmerge Handoff

Verdict: `PASS`
Recorded: `2026-07-13`
Derivative status: accepted B1/P3 evidence-only freeze integrated; it remains a
derivative package and is not decomposition or lifecycle truth.

## Accepted upstream and integration identity

- Sealed main basis: `9349594530dc19e55baf9c2ef0b7eb4716f48a17`.
- Accepted upstream: ORCHESTRATOR-B1 `PASS`, RECON-B1 `PASS`, and
  `snapshots/P3_MANIFEST/ACCEPTANCE.md` at `IMMUTABLE DERIVATIVE — B1/G3
  PASS`.
- Source branch: `codex/sow-stage2-b1`.
- Evidence commit: `103b33dfa3af08ef1e0b41ec8bee8f37e46aca63`.
- PR: `#222`, `https://github.com/sgttomas/chirality/pull/222`.
- Required check: `governance-harness / harness` `SUCCESS`.
- Merge commit: `30dba0628cd5aa9856ac96dfdb5851d5b80b1340`, merged at
  `2026-07-13T09:22:58Z` under `HUMAN-STEER-001`.

## Exact integrated inventory

The PR contained exactly 28 authorized evidence/control paths:

- root `WORK_GRAPH.json`;
- amendment `B1-EVIDENCE-FORMAT-001.md`;
- six ORCHESTRATOR-B1 and RECON-B1 launch/return/status files;
- five CHANGE-B1G premerge launch/readiness/check/return/status files;
- nine files in `snapshots/P3_MANIFEST/`;
- six files in the B1 reconciliation package.

The only postmerge writes are this handoff plus terminal replacements of
CHANGE-B1G `RETURN.md` and `STATUS.json`. No project, source, caller, tool,
canon, deliverable, lifecycle, conversion, receipt, release, H1/H2, ISSUED,
or retirement path changed. `.claude-worktrees/` remained untouched.

## Closure and rerun state

Accepted hashes pass `17/17`; internal P3 hashes pass `6/6`; the 154-row,
twelve-field execution manifest remains byte-equal to the accepted census; all
154 row comparisons remain `MATCH` with zero delta. Both manager contracts are
terminal PASS, structured files parse, portability passes, containment passes,
and diff hygiene passes. Blockers, waivers, and material unknowns are none.

Local main, `origin/main`, and remote main were synchronized at the merge
commit with divergence `+0/-0` before these terminal files were written. Their
ordinary evidence-only containing commit becomes the final synchronized-main
tip reported by CHANGE at runtime.

Rerun CHANGE-B1G if any accepted/internal hash, manager contract, row
comparison, required check, PR/merge identity, exact integrated inventory, or
this handoff changes. Rollback requires a new approved ordinary revert commit;
history rewrite and force-push are prohibited.

Next lawful owner: `HELP_HUMAN` for pilot release. Closure of this Git node does
not accept or mutate lifecycle truth and does not authorize conversion, H1,
H2, release, ISSUED integration, or legacy retirement.
