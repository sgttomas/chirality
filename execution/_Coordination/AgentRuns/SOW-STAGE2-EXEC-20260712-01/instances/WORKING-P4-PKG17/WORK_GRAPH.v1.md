# WORKING-P4-PKG17 Work Graph v1

Status: `FROZEN`

Selection authority: sealed `LAUNCH_BRIEF.md`. Posture:
`SEQUENTIAL_BATCHES_WITH_INDEPENDENT_FAN_IN`.

1. `AUTHOR-B1` — one fresh Agent 2; owns exactly `DEL-17-01..05` candidate
   families and its own evidence.
2. `VERIFY-B1` — one fresh evidence-only Agent 2; depends on terminal parent
   acceptance of `AUTHOR-B1`; reviews 100% and writes only verifier evidence.
3. `AUTHOR-B2` — one fresh Agent 2; depends on accepted B1 verifier
   `PASS_UNCHANGED`; owns exactly `DEL-17-06..09` candidate families and its
   own evidence.
4. `VERIFY-B2` — one fresh evidence-only Agent 2; depends on terminal parent
   acceptance of `AUTHOR-B2`; reviews 100% and writes only verifier evidence.
5. `MANAGER-FAN-IN` — WORKING_ITEMS; depends on both accepted verifier
   `PASS_UNCHANGED` returns; reproduces package bindings, exact 45 replacement
   and 45 inverse rows, nine simulations, checks, containment, telemetry,
   return, and derivative handoff for direct RECONCILIATION.

Concurrency: none. Bash-bearing and overlapping work is serialized. Each
author PASS requires complete member evidence, deterministic clean production,
mapping and exact physical source-line coverage, exact hashes, negative probes,
telemetry, containment, and no blocker/waiver/unknown. Each verifier acceptance
requires `PASS_UNCHANGED` for every member with no repair, discrepancy,
candidate or project write, drift, omission, or abbreviation.

Escalate any project, source, candidate-semantic, lifecycle, authority, scope,
or acceptance drift. Safe mechanical evidence defects may be repaired only in
owned evidence scope with failed attempts and before/after hashes retained,
all direct and transitive bindings rebuilt, and affected checks rerun.
