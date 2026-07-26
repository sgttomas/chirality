# Sealed Brief — S3: Export-boundary audit for the standing deferral (ROOT-OGC-20260725)

Issued by: `HELP_HUMAN` (Agent 0), 2026-07-25. Executor: ephemeral bounded
Agent 2 generalist, `opus-5`. One objective; no delegation; READ-ONLY
except the two named output files.

## Authorization

Owner ruling 2026-07-25 (verbatim in
`docs/governance_harness/_DECISIONS/D-GOV-26_owner_gated_closeout.md`,
authored this tranche): the four owner-gated issues close by following
Agent 0's recommendations. You execute R4 — the export-staging
regeneration item converts from carried-open-debt to a **standing
disposition**: regeneration stays deferred until the public export is next
actually needed; it is deterministic whenever run. Your audit supplies the
evidence that this disposition is SAFE — that deferral accumulates no
leak risk and no silent staleness hazard.

## Work (all read-only)

1. Read `exports/chirality-app/export_public.py` (the allowlist profile —
   K-EXPORT-1's boundary contract, PRD D-10) and any profile/config files
   it consumes. Report: the exact allowlist membership; the sanitization
   steps; the failure conditions (forbidden paths, leak detection).
2. Verify by inspection (not by running the export) that the repository
   state ADDED since the profile was last exercised cannot leak through a
   future regeneration run: root `execution/PKG-*` trees, root
   `execution/_harness/` guard state, `execution/_Decomposition/`,
   `execution/_Coordination/AgentRuns/`, decision records, tranche
   manifests. For each: IN or OUT of the allowlist, and by what rule.
   Per D-GOV-20 doctrine the public export may include generic
   runtime/CLI/contracts/safe adapters but excludes credentials, machine
   state, downloaded models, and private project adapters/evidence —
   flag anything ambiguous under that boundary rather than deciding it.
3. Check whether the existing staged export content (if any staging
   output is committed under `exports/`) makes claims now stale enough to
   mislead (e.g. a staged README describing pre-D-GOV-21 doctrine). Report
   what a regeneration would materially change — headline level, not a
   full diff.
4. Verdict: is the standing deferral SAFE / SAFE-WITH-CAVEATS / UNSAFE,
   with the caveats named. You decide nothing; you evidence the
   disposition the owner ruled.

## Constraints

- Write ONLY:
  `execution/_Coordination/AgentRuns/ROOT-OGC-20260725/evidence/EXPORT_BOUNDARY_AUDIT.md`
  (the audit) and
  `execution/_Coordination/AgentRuns/ROOT-OGC-20260725/returns/S3_RETURN_RAW.md`
  (your return; may summarize and point to the audit). Modify nothing
  else; run no export; no commits.
- Siblings are editing `docs/SPEC.md`, `docs/CONTRACT.md`,
  `tools/validation/` — do not touch them; reading is fine.
- Machine-absolute paths prohibited in your outputs.

## Terminal return (`S3_RETURN_RAW.md`, and return the same content)

Allowlist summary; the IN/OUT table for post-profile repository state;
staleness findings; the safety verdict with caveats; anything ambiguous
under the D-GOV-20 export boundary flagged for the owner.
