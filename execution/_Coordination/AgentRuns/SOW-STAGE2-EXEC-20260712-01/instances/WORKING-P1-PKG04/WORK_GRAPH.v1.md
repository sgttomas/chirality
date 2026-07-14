# WORKING-P1-PKG04 Work Graph v1

Status: `FROZEN`

Selection authority: sealed `LAUNCH_BRIEF.md`. Posture:
`SEQUENTIAL_BATCH_WITH_INDEPENDENT_FAN_IN`.

Nodes and edges:

1. `BATCH-01-AUTHOR` — fresh Agent 2; integration owner for
   `DEL-04-01..05`; writes those candidate families and its own evidence.
2. `BATCH-01-VERIFY` — fresh evidence-only Agent 2; depends on accepted
   `BATCH-01-AUTHOR`; reviews 100%; writes only verifier evidence and never
   repairs author output.
3. `BATCH-02-AUTHOR` — fresh Agent 2; depends on accepted Batch-01 verifier;
   integration owner for `DEL-04-06`.
4. `BATCH-02-VERIFY` — fresh evidence-only Agent 2; depends on accepted
   `BATCH-02-AUTHOR`; reviews 100%; never repairs author output.
5. `MANAGER-FAN-IN` — WORKING_ITEMS; depends on both accepted verifier
   returns; reproduces aggregate manifests, exact replacement/inverse rows,
   apply/target/rollback simulations, required checks, containment,
   telemetry, terminal return, and handoff.

Concurrency: none. All overlapping or Bash-bearing work is serialized.

Every author gate requires complete per-member evidence-rich and clean
production candidates, external finalization reports, complete mapping and
source-line coverage, exact hashes, deterministic validation, parity,
checklist, negative probes, containment, telemetry, and zero blocker, waiver,
or unknown. Every verifier gate requires independent 100% reproduction and
`PASS_UNCHANGED`; discrepancies fail and return to the manager. Escalation
points are frozen-input drift, semantic conflict or expansion, source loss,
wrong-member binding, finalization defect, failed required check, scope breach,
project write, missing telemetry disclosure, or verifier discrepancy.
