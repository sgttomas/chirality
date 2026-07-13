# C2F-R1 Independent Consumer Remediation Evaluation Protocol

Status: `EXECUTED`
Verdict vocabulary: `PASS | PARTIAL | BLOCKED | DECISION_REQUIRED`
Scoring: none
Delegation: none

## Accepted basis

This protocol executes the sealed `EVAL-C2F-R1/LAUNCH_BRIEF.md` against the
same frozen basis as C2F plus `C2F-REMEDIATION-001`:

- D-GOV-16 ruling publication
  `7584718aa32b112e415331736d1a8e68c12ac176`;
- accepted Stage-2 plan, graph, P0 caller manifest, and P1_CANON post-merge
  handoff at `main@e150c972889d05a8fc270239451a35c7512dc9a9`;
- the original C2F protocol, report, diagnostics, findings, and handoff;
- C2R-R1/R2 briefs, terminal returns/status, repaired root source, refreshed
  P2_ROOT evidence, and current hashes;
- C2A-R1 root/project-local terminal returns/status, review return, repaired
  App source, check evidence, handoff, and current hashes; and
- the current root C2A and C2A-R1 return pointers.

All evaluated source and producer evidence is read-only subject state. This
evaluation writes only quarantined derivative evidence under `C2F-R1/` and its
sealed instance return/status.

## Questions and decision criteria

1. Reconcile all 64 exact P0 caller rows and the nine frozen App callers with
   no unknown active consumer.
2. Confirm exact root/App changed-path containment, disjointness, current
   identities, and absence of deliverable, control, status, lifecycle,
   receipt, release, H1, H2, or retirement writes.
3. Require raw equality to
   `D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176` at every applicable
   consumer seam. Unruled, alternate, padded, malformed, missing, mismatched,
   non-isolated, wrong-path, invalid, partial, ambiguous, and misleading
   requested states must fail closed.
4. Confirm mandatory ISSUED accepted-basis, source-commit, four source-hash,
   and status-hash bindings and byte-identical `_STATUS.md` evidence.
5. Validate the root C2A terminal pointer and current root/App/export/build/
   self-check/practitioner/premerge evidence without rerunning expensive suites
   whose current source identities and terminal records reconcile.
6. Preserve the original findings and close each blocker only with direct
   current evidence.

Any failed mandatory fail-closed criterion, material unknown, or invalid
mandatory return yields `BLOCKED` and keeps C2G parked.

## Minimal toolbelt and method

- direct inspection of accepted authority, plan, manifests, returns, handoffs,
  implementation, tests, and normalized check evidence;
- read-only hash, manifest-set, diff-path, and containment diagnostics that
  exclude `.claude-worktrees/`;
- one targeted end-to-end reproduction of the disputed padded-authority
  checklist caller, written wholly inside this evaluation quarantine; and
- no child delegation, source repair, scoring, expensive-suite rerun, Git
  mutation, snapshot write, lifecycle act, release, H1/H2, or retirement act.
