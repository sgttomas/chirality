# Runtime Hardening Checks

Status: `PASS`

## Deterministic tools

- `python3 -m py_compile` for the managed-service runner and runtime telemetry:
  PASS.
- Focused Python suites for software workflow, telemetry, and agent-instruction
  validation: 19 passed.
- Agent instruction validator over WORKING_ITEMS and RECONCILIATION: 0 errors,
  0 warnings.
- Live path-anchor validator: PASS across 449 surfaces.
- Instruction-entrypoint validator: PASS.
- Modified JSON documents: parse PASS.
- `git diff --check`: PASS.

## Real self-contained project check

The registered App `frontend-premerge` check ran without a pre-existing
server. The runner allocated loopback port 50307, started the registered
stub-provider Next service, reached readiness in 2.712 seconds, ran the check,
and confirmed shutdown with service exit 0.

- Overall check: PASS in 14.882 seconds.
- Section 8: PASS, 8 tests.
- Section 9: PASS, 16 report-only tests.
- Captured home-directory or temporary-directory paths in evidence: 0; paths
  are normalized to `{WORKSPACE_ROOT}` and `{TMPDIR}`.
- Residual `next dev` / `next-server` process after check: 0.

Evidence: `SELF_CONTAINED_PREMERGE.json`.

## Telemetry dogfood

The new recorder captured one START, one CHECK, and one FINISH event for this
validation session. `RUNTIME_SUMMARY.json` reports PASS, one matched session,
zero retries/remediations, and the explicit limitation that native context
occupancy was unavailable.
