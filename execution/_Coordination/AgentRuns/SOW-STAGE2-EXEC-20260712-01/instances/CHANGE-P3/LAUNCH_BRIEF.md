# CHANGE-P3 Sealed Launch Brief

Parent: `HELP_HUMAN`
Role: `CHANGE` (Agent 1)
Run: `SOW-STAGE2-EXEC-20260712-01`
Brief version: `1`
Basis: synchronized `main@4d153302c3c4cd42578936db160c2bac1270225a`

## Objective

Integrate the accepted 15-member W-P3 clean-production representation
replacement, run every required check, push a `codex/` branch, open a ready
PR, merge under active blanket approval only after required checks pass,
synchronize through an isolated exact-main worktree, run postmerge checks, and
bind the immutable W-P3 integration handoff.

## Accepted inputs and topology

- RECON snapshot: `snapshots/W_P3/preintegration/`;
- snapshot manifest SHA-256:
  `9bd3fbc04be6ed07a5123cc26da0119dbb4a3c835b38b73a949c09bdf72963c7`;
- HELP_HUMAN acceptance at
  `snapshots/W_P3/preintegration-acceptance/HELP_HUMAN_ACCEPTANCE.md`;
- exact 75-row replacement and inverse rollback manifests;
- clean production candidates under `candidates/W_P3/PIP-PKG10..12/`;
- active human merge approval for PRs created in this goal after required
  checks pass.

Read root `AGENTS.md`, `agents/AGENT_CHANGE.md`, standing workplan, D-GOV-16,
active amendments including both PKG-11/12 BRIEF_V2 recoveries, all three
WORKING returns, RECON return/handoff, and applicable Piping checks. Execute
directly as one fresh wave-scoped manager; do not create a redundant child.

## Exact mutation and Git scope

Use isolated branch/worktree `codex/sow-p3` from the exact basis. For each
accepted W-P3 member in package and ascending numeric DeliverableID order,
make one atomic project commit with exactly:

```text
A ScopeOfWork.md
D Datasheet.md
D Specification.md
D Guidance.md
D Procedure.md
```

Copy only clean production candidates bound by the accepted manifest. Preserve
all `_STATUS.md`, lifecycle, context, control, dependency, reference, and other
project paths byte-for-byte. After 15 ordered commits, commit complete scoped
W-P3 coordination/evidence and acceptance as a separate binding commit.
Exclude unrelated equation-audit and `.claude-worktrees` state.

CHANGE may write the exact 15 live five-path replacements,
`instances/CHANGE-P3/**`, new immutable W-P3 integration/postmerge snapshots,
root plan/graph/receipt/handoff bindings, and Git/PR state. It may not edit
candidates, other project members, PKG-00, accepted predecessors, lifecycle or
dependency truth, canon/tools/agents/skills, release/reliance, H2, rollback
execution, or retirement.

## Checks and closeout

Before mutation reproduce refs, accepted snapshot, all 75 before hashes, 15
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
required check is successful. Use a fresh isolated exact-origin/main worktree
for postmerge verification if the canonical checkout is dirty. Run postmerge
format/hash/status/control and project checks, write immutable integration
evidence, append the root receipt, and perform scoped evidence-binding closeout
through the same required-check/approved-merge path if needed. Return terminal
evidence and stop only for genuine semantic/authority/scope conflict,
unresolved hash drift, failed required check, remote conflict, or
authentication/protection failure.
