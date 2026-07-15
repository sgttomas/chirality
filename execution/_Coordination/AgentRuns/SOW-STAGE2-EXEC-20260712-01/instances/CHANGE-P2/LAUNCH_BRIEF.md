# CHANGE-P2 Sealed Launch Brief

Parent: `HELP_HUMAN`
Role: `CHANGE` (Agent 1)
Run: `SOW-STAGE2-EXEC-20260712-01`
Brief version: `1`
Basis: synchronized `main@eaad463c0d481f6f1654e6adb5ee718f566176e9`

## Objective

Integrate the accepted 29-member W-P2 clean-production representation
replacement, run every required check, push a `codex/` branch, open a ready
PR, merge under active blanket approval only after required checks pass,
synchronize main, run postmerge checks, and bind the immutable W-P2
integration handoff.

## Accepted inputs and topology

- RECON snapshot: `snapshots/W_P2/preintegration/`;
- snapshot manifest SHA-256:
  `a42918b012864c245082837dc8abf5d0d403b3453edb56bd2484b9b139e5fe9b`;
- HELP_HUMAN acceptance at
  `snapshots/W_P2/preintegration-acceptance/HELP_HUMAN_ACCEPTANCE.md`;
- exact 145-row replacement and inverse rollback manifests;
- clean production candidates under `candidates/W_P2/PIP-PKG05..09/`;
- active human merge approval for PRs created in this goal after required
  checks pass.

Read root `AGENTS.md`, `agents/AGENT_CHANGE.md`, the standing workplan,
D-GOV-16, active amendments/directions, all five WORKING_ITEMS returns, the
RECON return/handoff, and applicable Piping checks. Execute directly as one
fresh wave-scoped manager; do not create a redundant child.

## Exact mutation and Git scope

Create an isolated branch/worktree `codex/sow-p2` from the exact basis to
protect unrelated dirty shared-checkout state. For each accepted W-P2 member
in package and ascending numeric DeliverableID order, make one atomic project
commit with exactly:

```text
A ScopeOfWork.md
D Datasheet.md
D Specification.md
D Guidance.md
D Procedure.md
```

Copy only clean production candidates bound by the accepted manifest. Preserve
all `_STATUS.md`, lifecycle, context, control, dependency, reference, and other
project paths byte-for-byte. After 29 ordered commits, commit complete scoped
W-P2 coordination/evidence and acceptance as a separate binding commit.
Exclude unrelated equation-audit and `.claude-worktrees` state.

CHANGE may write the exact 29 live five-path replacements,
`instances/CHANGE-P2/**`, new immutable W-P2 integration/postmerge snapshots,
root plan/graph/receipt/handoff bindings, and Git/PR state. It may not edit
candidates, other project members, PKG-00, accepted predecessors, lifecycle or
dependency truth, canon/tools/agents/skills, release/reliance, H2, rollback
execution, or retirement.

## Checks and closeout

Before mutation reproduce refs, accepted snapshot, all 145 before hashes, 29
production hashes, all status/control hashes, and project containment. After
each commit require clean `SOW_V1`, exact candidate hash, four legacy files
absent, preserved control hashes, and no unexpected path.

Before push run replacement/inverse/simulation, validation/map/parity/
checklist/finalization, practitioner self-check and full harness, applicable
root validators/tests/exports, and whole-diff hygiene. Normalize safe evidence
whitespace before manifest freeze, regenerate every affected binding, retain
pre-fix attempts, and continue; do not escalate mechanical issues resolvable
within scope.

Push, open a ready PR, verify final remote head/path/commit sequence, and
monitor all required checks. Merge under blanket approval only after every
required check is successful. Synchronize main, run postmerge format/hash/
status/control and project checks, write immutable integration evidence,
append the root receipt, and perform scoped evidence-binding closeout. Return
`PASS`, `BLOCKED`, or `DECISION_REQUIRED` with complete Git/check/rollback/
handoff evidence. Stop only for genuine semantic/authority/scope conflict,
unresolved hash drift, failed required check, remote conflict, or
authentication/protection failure.
