# C2F Independent Consumer Evaluation Protocol

Status: `EXECUTED`
Verdict vocabulary: `PASS | PARTIAL | BLOCKED | DECISION_REQUIRED`
Scoring: none

## Accepted basis

This protocol executes the human-accepted C2F node and sealed
`EVAL-C2F/LAUNCH_BRIEF.md`. The frozen basis is:

- D-GOV-16 ruling publication
  `7584718aa32b112e415331736d1a8e68c12ac176`;
- accepted Stage-2 plan and execution graph;
- P0 caller manifest;
- P1_CANON post-merge handoff and synchronized
  `main@e150c972889d05a8fc270239451a35c7512dc9a9`;
- the C2R candidate, manifest, return, status, tests, and handoff; and
- the C2A project-local package, implementation/review returns, manifest,
  tests, rerun evidence, status, and handoff.

All candidate source changes are read-only subject state. Evaluation writes
are quarantined under this directory and the EVAL-C2F instance return/status.

## Questions and decision criteria

1. Reconcile all 64 P0 exact caller rows and the nine frozen App callers with
   no unknown active consumer.
2. Prove exact changed-path containment, root/App disjointness, current
   identities, and absence of deliverable/control/status/lifecycle/receipt or
   release writes.
3. Confirm successful SOW-only and legacy-only behavior and fail-closed
   missing, partial, invalid, ambiguous, misleading, and unauthorized-dual
   behavior.
4. Validate current green root, export, agent, skill, App focused/full,
   typecheck, build, self-check, practitioner, and owned-server premerge
   evidence.
5. Keep schema/mechanical, content/authority, preservation/containment, and
   execution-substrate outcomes separate. Do not average away a blocker.

Any material unknown, invalid mandatory return, or failed mandatory criterion
returns `BLOCKED` and does not release C2G.

## Minimal toolbelt and method

- direct inspection of the ruled canon, accepted plan, manifests, returns,
  handoffs, code, tests, and normalized check evidence;
- read-only Git status/diff/hash diagnostics and deterministic TSV/set/hash
  comparisons;
- targeted current reruns only: 30 root resolver/reporting/semantic tests,
  agent and skill validators, export profile, diff hygiene, the seven-file App
  seam (70 tests), and App typecheck;
- no child delegation, scoring, source repair, Git operation, full-suite
  rerun, release, lifecycle act, H1/H2 act, or snapshot write.

The existing expensive full-root, full-App, build, self-check, practitioner,
and owned-server premerge evidence is accepted only after its source hashes
and current candidate identities are independently reconciled.
