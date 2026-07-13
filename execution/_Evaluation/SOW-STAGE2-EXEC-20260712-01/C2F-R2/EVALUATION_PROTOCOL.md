# C2F-R2 Final Independent Consumer Evaluation Protocol

Status: `EXECUTED`
Verdict vocabulary: `PASS | PARTIAL | BLOCKED | DECISION_REQUIRED`
Scoring: none
Delegation: none

## Accepted basis

This protocol executes the sealed `EVAL-C2F-R2/LAUNCH_BRIEF.md` against:

- D-GOV-16 ruling publication
  `7584718aa32b112e415331736d1a8e68c12ac176` and synchronized
  `main@e150c972889d05a8fc270239451a35c7512dc9a9`;
- the accepted Stage-2 plan, P0 caller manifest, and P1_CANON handoff;
- both immutable prior C2F evaluation packages and every finding they retain;
- active `C2F-REMEDIATION-001`, including clarifications 001-A, 001-B, and
  001-C;
- terminal C2R-R1/R2/R3 and C2A-R1 source, manifests, returns, handoffs, and
  current-hash evidence; and
- current root/App/export/build/self-check/practitioner/premerge records and
  the root C2A/C2A-R1 terminal pointers.

All evaluated source and producer evidence is read-only subject state. Writes
are quarantined under this `C2F-R2/` directory and the sealed EVAL-C2F-R2
instance return/status only.

## Questions and criteria

1. Re-evaluate `EVAL-C2F-001` through `-004` and `EVAL-C2F-R1-001` without
   deleting or rewriting their history.
2. Require exact raw authority at the resolver, converter, checklist, and App
   seams; exact unpadded authority must work and padded authority must fail
   closed without a requested checklist output.
3. Reconcile 64 exact root callers, nine App callers, current hashes, exact
   changed-path containment/disjointness, and terminal return pointers.
4. Confirm ISSUED accepted-basis/source/status bindings and preservation.
5. Accept expensive-suite evidence only when its recorded source identities
   remain current; do not rerun those suites.

Any open mandatory blocker, material unknown, invalid mandatory return, or
hash/containment mismatch yields `BLOCKED` and keeps C2G parked. The low direct
DocumentView test-coverage risk remains separately classified.

## Minimal method

- direct source/test/manifest/return/handoff inspection;
- read-only Git, set, hash, containment, and pointer diagnostics excluding
  `.claude-worktrees/`;
- one targeted current pytest invocation covering deterministic exact/SOW-only
  checklist behavior and the padded-authority no-output regression, with all
  test output confined to this quarantine; and
- no delegation, scoring, source repair, expensive-suite rerun, Git mutation,
  snapshot/lifecycle/release/H1/H2/retirement act, or project-state write.
