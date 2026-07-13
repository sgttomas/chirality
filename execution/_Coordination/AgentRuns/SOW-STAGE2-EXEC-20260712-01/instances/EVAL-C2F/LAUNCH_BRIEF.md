# EVAL-C2F Launch Brief — v1

Role: `EVALUATION` (Agent 1, independent read-only consumer evaluation)

## Objective

Evaluate whether the completed C2R and C2A candidates satisfy the accepted
C2 consumer-activation gate, independently of the producing managers and the
RECONCILIATION synthesis.

## Frozen basis and questions

Basis is D-GOV-16, the accepted Stage-2 plan/graph, P0 caller manifest,
post-merge P1 canon handoff, C2R candidate/return, C2A package run/return, and
the current candidate diff on synchronized main
`e150c972889d05a8fc270239451a35c7512dc9a9`.

Evaluate:

1. Are all 64 root active callers and all nine frozen App callers classified,
   with zero unknown active consumer?
2. Are root and App changed paths exactly contained, mutually disjoint, and
   free of governed deliverable/control/status/lifecycle/receipt/release
   writes?
3. Do evidence and tests prove SOW-only and retained legacy success plus
   fail-closed missing, partial, ambiguous, unauthorized-dual, and invalid
   behavior?
4. Are root tools, agents, skills, exports, App focused/full tests, typecheck,
   build, self-check, practitioner tests, and owned-server premerge evidence
   current and green?
5. Are observed issues correctly classified as schema, content, preservation,
   or substrate, without averaging away a blocker?

Minimal toolbelt: direct evidence inspection, Git diff/hash diagnostics, and
only bounded deterministic checks needed to validate a disputed or missing
claim. No scoring. No child delegation.

## Writes

Only:

- `execution/_Evaluation/SOW-STAGE2-EXEC-20260712-01/C2F/**`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/EVAL-C2F/RETURN.md`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/EVAL-C2F/STATUS.json`

These are quarantined derivative evaluation evidence. Do not write the
parent-owned `snapshots/P2_CONSUMERS/` snapshot.

## Denied and acceptance

No subject edits, repairs, Git state changes, deliverable/control/lifecycle
writes, release, H1/H2, or legacy retirement. Return `PASS | PARTIAL |
BLOCKED | DECISION_REQUIRED` with evidence-linked findings (including an empty
findings register when appropriate), coverage, unknowns, blockers, reruns,
and next owner. Any material unknown or failed mandatory criterion blocks C2G.
