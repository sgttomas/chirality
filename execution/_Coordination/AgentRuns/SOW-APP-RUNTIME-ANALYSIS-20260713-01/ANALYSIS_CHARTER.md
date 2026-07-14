# App Runtime Analysis Charter

Status: `ACTIVE — HUMAN-REQUESTED READ-ONLY EMPIRICAL ANALYSIS`

Objective: measure the runtime and failure properties of the completed App
ordinary-conversion waves in
`SOW-STAGE2-EXEC-20260712-01`, using reproducible extraction rather than
anecdotal summaries.

The source population is exactly App waves A1, A2, and A3: ten package-manager
instances and 47 ordinary deliverables. Piping, pilots, canon/consumer work,
the later PKG-01 batching experiment, and the unfinished H1 lane are excluded.

This run may add a deterministic analysis tool, its tests and registry entry,
and this derivative analysis package. It may not modify the accepted Stage-2
plan/current execution graph, source run evidence, project files, candidates,
lifecycle state, H1/H2, or integration state.

## Measurement model

- Inventory and result counts come from package, child, RECON, and CHANGE
  records.
- Command counts, exits, and durations come from normalized
  `PROJECT_CHECKS*.json` records.
- Wave wall-clock envelopes run from the accepted activation/basis commit to
  the merge commit; preparation ends at the evidence-binding commit. These are
  elapsed envelopes, not CPU or summed-agent time.
- An abnormal episode is one independently described failure/recovery chain.
  The curated catalog binds every classification to an exact evidence path,
  exact text needle, file hash, and line. It does not count generic rerun
  instructions or prose saying that no failures remain.
- `affected_units` preserves the source episode's natural unit: child attempt,
  package check, evidence surface, or grouped terminalization cluster. It is
  not a common statistical denominator and is never summed into a defect rate.
- Wilson intervals are descriptive uncertainty bounds only. Packages,
  deliverables, and attempts are neither random nor independent samples.

Native token use, context occupancy, complete per-agent timing, and CPU use
were not recorded and therefore remain unknown.
