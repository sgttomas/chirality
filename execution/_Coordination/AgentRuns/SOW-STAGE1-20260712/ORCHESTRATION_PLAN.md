# Scope-of-Work Stage 1 Orchestration Plan — v1

Status: `EXECUTING`
Selection authority: `HUMAN` (`D-GOV-15` plus the current owner objective)
Posture: `MIXED`
Frozen source basis: `main@2770fda4c63c98ee9f18cffbafd14c9aa59f497f`
Published ruling: `58aa81d62f4a32e3c2d687e4356a1e4be8141674`
Candidate basis: `c4c5dd2df0d7b5424d48672c38d1eef37262e2f6`

## Work graph

1. `APP-CAL` and `PIP-CAL` execute concurrently in disjoint isolated
   worktrees. Each owns one calibration deliverable and its project-local run
   records. Neither may edit `_STATUS.md`, legacy sources, canon, historical
   evidence, or any other deliverable.
2. `ROOT-FREEZE` validates both calibration returns and freezes the candidate
   schema/tool revision. Any substantive schema or content conflict returns to
   the owner; no exact TYPES/SPEC amendment is permitted.
3. `APP-FROZEN` and `PIP-FROZEN` reconvert the calibration targets from the
   frozen source basis and convert the remaining eight targets. They remain
   disjoint and may proceed concurrently after `ROOT-FREEZE`.
4. `RECON-FANIN` independently audits all ten derivative packages for complete
   claim disposition, parity, source binding, lifecycle neutrality, consumer
   behavior, deterministic rendering, and preservation fences.
5. `CHANGE-CLOSE` performs Git/evidence closeout without merging either pilot
   branch. Root then publishes a PASS/FAIL handoff and D-GOV-16 proposal.

## Ownership and fan-in

- App Dev writes only branch `codex/sow-app-pilot`, exact PKG-07 pilot
  deliverables, and project-local records under its worktree.
- Piping writes only branch `codex/sow-piping-pilot`, exact PKG-13 pilot
  deliverables, and project-local records under its worktree.
- Root integration writes only branch `codex/sow-stage1-execution` and root
  governance/evidence records. Candidate deliverables are never integrated
  into this branch or `main`.
- Every manager return must name commits, files, checks, blockers, reruns,
  derivative status, and Stage-2 recommendation. Missing or contradictory
  returns fail closed.

## Human gates

Stop for scope expansion, a substantive content or authority conflict,
lifecycle acceptance, shared-write conflict, exact canon amendment, corpus
conversion, pilot merge, or Stage-2 authorization. D-GOV-16 remains an owner
ruling and is not implemented by this run.

## Native substrate determination

The platform supplies hierarchical parent/child identity, bounded prompts,
concurrent execution, follow-up amendments, terminal structured returns, and
parent-mediated communication. This run freezes equivalent briefs and scopes
below and persists all launch/return evidence. The D-GOV-15 sequential
fallback remains available only if these properties fail during execution;
such a failure is recorded separately from schema and project-content results.
