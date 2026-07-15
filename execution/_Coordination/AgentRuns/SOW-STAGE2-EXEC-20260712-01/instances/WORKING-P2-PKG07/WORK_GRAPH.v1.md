# WORKING-P2-PKG07 Work Graph v1

Status: `FROZEN`

Selection authority: sealed `LAUNCH_BRIEF.md`. Posture:
`SEQUENTIAL_BATCH_WITH_INDEPENDENT_FAN_IN`.

1. `AUTHOR-B1` — fresh Agent 2; owns exactly `DEL-07-01..05` candidate
   families and its own evidence.
2. `VERIFY-B1` — fresh evidence-only Agent 2; depends on accepted
   `AUTHOR-B1`; reviews 100% and writes only verifier evidence.
3. `AUTHOR-B2` — fresh Agent 2; depends on accepted `VERIFY-B1`; owns exactly
   `DEL-07-06..08` candidate families and its own evidence.
4. `VERIFY-B2` — fresh evidence-only Agent 2; depends on accepted
   `AUTHOR-B2`; reviews 100% and writes only verifier evidence.
5. `MANAGER-FAN-IN` — WORKING_ITEMS; depends on both accepted verifier
   returns; reproduces package manifests, exact replacement/inverse rows,
   apply/target/rollback simulations, checks, containment, telemetry, return,
   and derivative handoff for direct RECONCILIATION.

Concurrency: none. Bash-bearing and overlapping work is serialized. Each
author PASS requires complete member evidence, clean deterministic production,
mapping and exact physical source-line coverage, exact hashes, negative probes,
telemetry, containment, and no blocker/waiver/unknown. Each verifier acceptance
requires `PASS_UNCHANGED` for every member with no repair, discrepancy,
candidate or project write, drift, omission, or abbreviation.
