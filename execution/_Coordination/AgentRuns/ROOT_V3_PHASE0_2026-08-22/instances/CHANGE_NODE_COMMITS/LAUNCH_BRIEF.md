# CHANGE Brief — Root v3 Phase-0 Node Commits

Run ID: `ROOT_V3_PHASE0_2026-08-22`

Caller: `HELP_HUMAN`.

Role: `CHANGE` Agent 1. Read and obey `AGENTS.md` and
`agents/AGENT_CHANGE.md` before any Git mutation.

## Authorized objective

Create exactly three local commits on
`codex/root-v3-phase0-2026-08-22`, in dependency order N1 → N2 → N3, from
the already accepted and fresh-reviewed node artifacts. This is local commit
packaging only. Do not fetch, sync, merge, rebase, push, open a PR, or merge.

The authorized branch basis remains
`6b0c5219b6a2653e2fc491b1d998abcf78fcf776`. `origin/main` advanced during
execution to `166efa82748133e90674be62304b81f8a0a8c1b4`; quarantine that drift and
do not integrate it without a later owner authorization.

## Required preflight

- Verify current branch and HEAD.
- Verify `AGENTS.md` SHA-256 remains
  `268becd0bac9da8421b30089e4e4167a5e5f79bf3892d0f72ad41a63180a3aeb`.
- Verify `execution/_ScopeChange/_LATEST.md` SHA-256 remains
  `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1`.
- Verify the three accepted review verdicts/hashes recorded in the run handoff.
- Verify no path outside the exact commit groups below is staged for each
  commit. Preserve every unrelated/user change if any appears.

## Commit 1 — N1

Stage only:

- `docs/governance_harness/_PROPOSALS/D-GOV-35_2026-08-22_delegated_harness_native_class/`
- `execution/_Coordination/AgentRuns/ROOT_V3_PHASE0_2026-08-22/ORCHESTRATION_PLAN.md`
- `execution/_Coordination/AgentRuns/ROOT_V3_PHASE0_2026-08-22/WORK_GRAPH.json`
- `execution/_Coordination/AgentRuns/ROOT_V3_PHASE0_2026-08-22/amendments/N1/`
- `execution/_Coordination/AgentRuns/ROOT_V3_PHASE0_2026-08-22/instances/N1/`

Commit message:
`governance: prepare D-GOV-35 delegation class proposal`

## Commit 2 — N2

Stage only:

- `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-03_Delegation_Hierarchy_and_Entry_Rules/_run_records/DEL-02-03-M2-PREP-001/`
- `execution/_Coordination/AgentRuns/ROOT_V3_PHASE0_2026-08-22/instances/N2/`

Commit message:
`governance: prepare DEL-02-03 M2 instruction tranche`

## Commit 3 — N3

Stage only:

- `execution/_ScopeChange/SCA-004_2026-08-22_1749/`
- `execution/_Coordination/NOTICE_2026-08-22_ROOT_SCA-004_V3_RELEASE_PATHWAY_DAG.md`
- `execution/_Coordination/AgentRuns/ROOT_V3_PHASE0_2026-08-22/amendments/N3/`
- `execution/_Coordination/AgentRuns/ROOT_V3_PHASE0_2026-08-22/instances/N3/`
- `execution/_Coordination/AgentRuns/ROOT_V3_PHASE0_2026-08-22/HANDOFF_STATE.md`

Commit message:
`governance: assess SCA-004 release pathway graph`

## Commit checks

Before each commit, record `git diff --cached --name-status` and confirm exact
containment. After each commit, record the commit SHA and `git show --stat`.
After all three, confirm the order with `git log --oneline`, confirm no
forbidden protected path was changed, and leave every uncommitted path that is
outside the three groups untouched.

## Control write set

Only:

- this instance folder's `STATUS.json`
- this instance folder's `RETURN.md`

Those two closeout-control files are intentionally not part of the three node
commits; HELP_HUMAN will include them in the later Receipt-114 closeout commit
after the owner decides the required sync gate.

## Return contract

Return the three commit SHAs in order, exact staged path evidence, branch/base
evidence, post-commit status, remaining uncommitted paths, and explicit
confirmation that no sync, push, PR, or merge occurred. Stop and return a
blocker instead of widening any stage set.
