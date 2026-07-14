# CHANGE-P1-PKG03 Sealed Launch Brief

Parent: `HELP_HUMAN`
Role: `CHANGE` (Agent 1)
Run: `SOW-STAGE2-EXEC-20260712-01`
Brief version: `1`
Basis: synchronized `main@5f124ad80fe84357f6dc33072dc4fbdbeb05d545`

## Objective

Integrate the HELP_HUMAN-accepted eight-member Piping PKG-03 clean-production
representation replacement, run every required check, push a `codex/` branch,
open a ready pull request, merge it under the active human blanket approval
only after all required checks pass, synchronize main, run postmerge checks,
and bind the immutable integration handoff.

## Accepted inputs

- RECON snapshot:
  `snapshots/W_P1/PKG03-preintegration-accepted/`;
- snapshot manifest SHA-256:
  `39e29ecf82dffe8ecbeaaa1f944a7557c348e655eb6d4fef09943903a237195c`;
- HELP_HUMAN acceptance in that snapshot;
- exact 40-row replacement and exact inverse rollback manifests;
- clean production candidates at
  `candidates/W_P1/PIP-PKG03/DEL-03-01..08/production/ScopeOfWork.md`;
- active human merge approval for PRs created within this goal, conditional on
  required checks passing.

Read root `AGENTS.md`, `agents/AGENT_CHANGE.md`, the standing workplan,
D-GOV-16, active Stage-2 amendments including the topology clarification, the
complete WORKING_ITEMS and RECON handoffs, and applicable Piping project
instructions/check profile.

## Exact mutation and Git scope

Create branch `codex/sow-p1-pkg03` from the exact basis. For each `DEL-03-01`
through `DEL-03-08` in numeric order, make one atomic project commit whose
deliverable delta is exactly:

```text
A ScopeOfWork.md
D Datasheet.md
D Specification.md
D Guidance.md
D Procedure.md
```

Copy only the clean production candidate whose SHA is bound by the accepted
replacement manifest. Preserve `_STATUS.md`, lifecycle, `_CONTEXT.md`,
dependency/control/reference files, and every other project path byte-for-byte.
After the eight ordered commits, commit the complete scoped Stage-2 PKG-03
coordination/evidence changes and preintegration acceptance as a separate
binding commit. Exclude all unrelated domain equation-audit paths and
`.claude-worktrees/` state.

CHANGE may write the exact eight live deliverable five-path replacements,
`instances/CHANGE-P1-PKG03/**`, a new immutable PKG-03 integration/postmerge
snapshot under `snapshots/W_P1/`, the root run plan/graph/receipt/handoff
surfaces necessary to bind the accepted integration, and Git branch/commit/
push/PR/merge state. It may not edit candidates, other project members,
PKG-00, `DEL-01-01`, lifecycle/control/dependency truth, canon/tools/agents/
skills, H1/H2, release, retirement, or unrelated user state.

## Checks, PR, and closeout

Before mutation, reproduce synchronized refs, the accepted snapshot manifest,
all 40 before hashes, all eight production hashes, all status/control hashes,
and exact project containment. After every deliverable commit require clean
`SOW_V1`, exact candidate hash, absent four legacy files, unchanged status and
control hashes, and no unexpected path.

Before push/PR run all accepted deterministic replacement/inverse/simulation,
Scope-of-Work validation/map/parity/checklist/finalization bindings, Piping
practitioner self-check, full registered practitioner harness, applicable root
agent/skill/path/entrypoint/export checks, and `git diff --check`. Keep schema,
content, preservation, and substrate outcomes separate.

Push the branch and open a ready PR. Confirm the final remote head equals the
locally validated head and the changed-path/commit sequence is exact. Monitor
all required checks; do not merge on pending, skipped-required, neutral,
cancelled, timed-out, or failed state. Under the human blanket approval, merge
only after every required check passes. Synchronize local main to remote main,
run postmerge format/hash/status/control/project checks, write immutable
integration/postmerge evidence, append the minimal root receipt, and perform
the scoped evidence-binding commit/push required by the established loop.

Return `PASS`, `BLOCKED`, or `DECISION_REQUIRED` with commit SHAs, PR and merge
identity, required-check evidence, changed-path containment, postmerge results,
rollback binding, remaining dirty files, derivative status, closure verdict,
rerun triggers, blockers, and next owner. Stop on any drift, unexpected path,
hash mismatch, failed required check, conflict, remote-head change, protection/
auth failure, or overlap with unrelated user work.
