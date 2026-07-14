# WORKING-I0-PKG01 Work Graph v1

Status: `FROZEN`

Selection authority: sealed parent brief. Posture:
`SEQUENTIAL_AUTHOR_VERIFY_FAN_IN`.

## Nodes and edges

1. `I0-AUTHOR` — fresh Agent 2; owns the isolated derivative candidate family
   and complete author evidence for exact `DEL-01-01`.
2. `I0-VERIFY` — fresh evidence-only Agent 2; depends on manager acceptance of
   `I0-AUTHOR`; independently reviews 100%; writes verifier evidence only and
   never repairs author output.
3. `MANAGER-FAN-IN` — WORKING_ITEMS; depends on accepted author and verifier
   terminal returns; independently reproduces bindings, manifests,
   apply/target/rollback simulation, required checks, containment, telemetry,
   terminal return, and H1-prohibited handoff.

Concurrency: none. Author/candidate writes and later verifier reads are
serialized. Children do not delegate. Coordination flows only through this
manager.

## Ownership, returns, and gates

`I0-AUTHOR` may write only
`candidates/I0/PIP-PKG01/DEL-01-01/**` and its own child folder. It returns the
evidence-rich candidate, distinct clean production candidate, external
finalization report, maps, parity, checklist, rendering, exact source/status
bindings, replacement and inverse rows, simulations, negatives, tests,
telemetry, findings, rerun triggers, status, and manifest.

`I0-VERIFY` reads frozen live inputs and accepted candidate family, and writes
only its child folder. It must independently reproduce every material result,
including deterministic evidence/production/report identity, 100% mappings
and source lines, source/status/lifecycle preservation, semantic-addition
review, simulations, negatives, tests, containment, and manifest bindings.

`MANAGER-FAN-IN` accepts only complete schema-valid terminal returns with no
semantic delta, drift, discrepancy, unexplained result, project/candidate
contamination, missing telemetry disclosure, or scope breach. Safe mechanical
evidence defects are repaired within scope with attempts retained and every
affected binding rebuilt. Semantic, authority, lifecycle, or scope conflicts
return `CONFLICT`, `BLOCKED`, or `DECISION_REQUIRED`.

Human decision point: H1 remains outside this graph. A PASS handoff prepares
evidence for independent RECONCILIATION and later human review; it never
approves H1 or releases integration.
