# Landing Manifest — D-APP-64 (frozen scope and gate)

## Frozen candidate

- Path: `WORKPLAN_CANDIDATE_2026-07-18b_app_dev_loop.md` (this run directory)
- File bytes: 14,932 (span 14,931 + one trailing LF)
- Git blob: `5f01938c92b719426e9c0716a5d5a3980cf78566`
- Span SHA-256: `a8e1a1d05e1f5c2a44db30cac2cbfb28bf5a9ff5c4dd3984d9ef94a4e0a22573`
- Governed twin: packet §12 Appendix W span (byte-identical; V1-verified)

## Exact landing scope (the single atomic commit; no other path is in scope)

1. `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-64_PACKET_REASONED_SELECTION_OVERLAY_2026-07-18.md`
2. `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md` (one appended row)
3. `projects/chirality-app-dev/loop/WORKPLAN_2026-07-18b_app_dev_loop.md` (materialized from the frozen candidate bytes)
4. `projects/chirality-app-dev/loop/LOOP_INIT.md` (§2 committed-HEAD loader)
5. `projects/chirality-app-dev/loop/LOOP_RECEIPTS.md` (Receipt-70 append)
6. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/D-APP-64_REASONED_SELECTION_OVERLAY_2026-07-18/**` (complete run directory: orchestration plan, sealed briefs, candidate, rationale, matrix, this manifest, choreography, all verifier returns)

**Amendment v2 (post-N5, pre-receipt; reason recorded in
`RATIONALE_D-APP-64.md` item 8):** the closeout battery surfaced GEN8
ABS_PATH_IN_PROJECT_SURFACE findings on the three records carrying the owner
direction's verbatim span (which cites the piping precedent worktree by
machine-absolute path). Detect-never-rewrite forbids relativizing them, so
the landing scope gains exactly one item:

7. `tools/practitioner_harness/test_live_baseline.py` (conscious pin update:
   severity anchor and GEN8 baseline set, with dated in-file notes)

V2 verified the pre-amendment scope; V3 verifies against this amended
manifest.

Explicitly out of scope: Shared-Block v1 bytes, every D-APP-59..63 record,
prior workplans, receipts through Receipt-69, `projects/chirality-piping/**`,
`_DomainEngines/**`, `projects/pec/**`, frontend/runtime source.

## Gate

Materialize the active path from the frozen candidate bytes only; require
`cmp -s` equality and equal `git hash-object` against the candidate; stage
only the declared scope; verify pre-commit `HEAD` discovery still selects
`WORKPLAN_2026-07-18_app_dev_loop.md`; commit the complete scope atomically;
post-commit require a unique mode-100644 active blob equal to
`5f01938c92b719426e9c0716a5d5a3980cf78566` and `HEAD` discovery selecting
`WORKPLAN_2026-07-18b_app_dev_loop.md`. Nothing lands on `BLOCK`.
