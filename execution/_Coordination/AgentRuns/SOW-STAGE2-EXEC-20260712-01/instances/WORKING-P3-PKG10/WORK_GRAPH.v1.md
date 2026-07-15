# WORKING-P3-PKG10 Work Graph v1

Status: `FROZEN`

Selection authority: sealed `LAUNCH_BRIEF.md`. Posture:
`SEQUENTIAL_BATCH_WITH_INDEPENDENT_FAN_IN`.

1. `AUTHOR-B1` — one fresh Agent 2; owns exactly `DEL-10-01..05` candidate
   families and its own evidence.
2. `VERIFY-B1` — one fresh evidence-only Agent 2; depends on accepted
   `AUTHOR-B1`; reviews 100% and writes only verifier evidence.
3. `MANAGER-FAN-IN` — WORKING_ITEMS; depends on the accepted verifier return;
   reproduces package manifests, exact replacement/inverse rows,
   apply/target/rollback simulations, checks, containment, telemetry, return,
   and derivative handoff for direct RECONCILIATION.

Concurrency: none. Bash-bearing and overlapping work is serialized. Author
PASS requires complete member evidence, deterministic clean production,
mapping and exact 1,594/1,594 physical source-line coverage, exact hashes,
negative probes, telemetry, containment, and no blocker/waiver/unknown.
Verifier acceptance requires `PASS_UNCHANGED` for every member with no repair,
discrepancy, candidate or project write, drift, omission, or abbreviation.

