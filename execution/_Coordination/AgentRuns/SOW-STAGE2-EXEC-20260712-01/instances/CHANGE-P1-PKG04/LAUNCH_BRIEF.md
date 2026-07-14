# CHANGE-P1-PKG04 Sealed Launch Brief

Parent: `HELP_HUMAN`
Role: `CHANGE` (Agent 1)
Run: `SOW-STAGE2-EXEC-20260712-01`
Brief version: `1`
Basis: synchronized `main@2a5e3825d8d2fc4943742a53ccad3b89c4c81902`

## Objective

Integrate the accepted six-member Piping PKG-04 clean-production
representation replacement, run every required check, push a `codex/` branch,
open a ready PR, merge under active blanket approval only after required checks
pass, synchronize main, run postmerge checks, and bind the immutable P1
integration handoff.

## Accepted inputs and topology

- RECON snapshot: `snapshots/W_P1/PKG04-preintegration-r1/`;
- snapshot manifest SHA-256:
  `c30cacfbf26ceb9daa691cedf7688aba5e390d979c76c16142d67961084b94c4`;
- HELP_HUMAN acceptance sibling;
- exact 30-row replacement and inverse rollback manifests;
- clean production candidates under
  `candidates/W_P1/PIP-PKG04/DEL-04-01..06/production/ScopeOfWork.md`;
- active human merge approval for PRs created in this goal after required
  checks pass.

Read root `AGENTS.md`, `agents/AGENT_CHANGE.md`, standing workplan, D-GOV-16,
active amendments/directions, full WORKING_ITEMS and RECON handoffs, and
applicable Piping checks. Execute directly as one fresh package-scoped manager;
do not create a redundant child.

## Exact mutation and Git scope

Create isolated branch/worktree `codex/sow-p1-pkg04` from the exact basis to
protect unrelated dirty shared-checkout state. For each `DEL-04-01..06` in
numeric order, make one atomic project commit with exactly:

```text
A ScopeOfWork.md
D Datasheet.md
D Specification.md
D Guidance.md
D Procedure.md
```

Copy only clean production candidates bound by the accepted manifest. Preserve
all `_STATUS.md`, lifecycle, context, control, dependency, reference, and other
project paths byte-for-byte. After six ordered commits, commit complete scoped
PKG-04 coordination/evidence and acceptance as a separate binding commit.
Exclude unrelated equation-audit and `.claude-worktrees` state.

CHANGE may write the exact six live five-path replacements,
`instances/CHANGE-P1-PKG04/**`, new immutable PKG-04 integration/postmerge
snapshots, root plan/graph/receipt/handoff bindings, and Git/PR state. It may
not edit candidates, other project members, PKG-00, `DEL-01-01`, lifecycle or
dependency truth, canon/tools/agents/skills, H1/H2, release, or retirement.

## Checks and closeout

Before mutation reproduce refs, accepted snapshot, all 30 before hashes, six
production hashes, all status/control hashes, and project containment. After
each commit require clean `SOW_V1`, exact candidate hash, four legacy files
absent, preserved control hashes, and no unexpected path.

Before push run replacement/inverse/simulation, validation/map/parity/
checklist/finalization, practitioner self-check and full harness, applicable
root validators/tests/exports, and whole diff hygiene. Normalize safe evidence
whitespace before manifest freeze, regenerate every affected binding, retain
pre-fix attempts, and continue; do not escalate mechanical issues resolvable
within scope.

Push, open ready PR, verify final remote head/path/commit sequence, and monitor
all required checks. Merge under blanket approval only after every required
check is successful. Synchronize main, run postmerge format/hash/status/control
and project checks, write immutable integration evidence, append the root
receipt, and perform scoped evidence-binding closeout. Return `PASS`,
`BLOCKED`, or `DECISION_REQUIRED` with complete Git/check/rollback/handoff
evidence. Stop only for genuine semantic/authority/scope conflict, unresolved
hash drift, failed required check, remote conflict, or auth/protection failure.
