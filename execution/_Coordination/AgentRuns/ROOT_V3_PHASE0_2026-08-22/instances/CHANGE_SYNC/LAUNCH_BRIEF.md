# CHANGE Brief — Authorized Main Sync

Run ID: `ROOT_V3_PHASE0_2026-08-22`

Caller: `HELP_HUMAN`.

Role: `CHANGE` Agent 1. Read and obey `AGENTS.md` and
`agents/AGENT_CHANGE.md` before mutation.

## Owner authorization of record

Ryan Tufts, 2026-08-22:

> I authorize you to fetch and merge the latest `origin/main` into this branch,
> then complete Receipt 114, validation, push, and PR creation without merging
> the PR.

## Authorized objective

Fetch `origin`, then merge the fetched latest `origin/main` into
`codex/root-v3-phase0-2026-08-22` using a merge commit. Preserve the existing
node commit identities and ordering:

1. `45eead4edf524b9b31293b4f8b8f59ec58b283d4` — N1
2. `d329529cf07e255415edef0f2d3f3ceee357d5c1` — N2
3. `7590c002b1dc9399e95029d51551895bb700b302` — N3

This brief authorizes fetch and local merge only. Do not push, open a PR, or
merge a PR in this step. HELP_HUMAN must complete Receipt 114 and integrated
validation first.

## Preflight and containment

- Confirm current branch and the three-node HEAD chain.
- Preserve the uncommitted `instances/CHANGE_NODE_COMMITS/` control folder and
  this `instances/CHANGE_SYNC/` folder; do not stage them in the merge.
- Fetch `origin` and record the fetched `origin/main` SHA.
- Before merge, inspect the incoming path set. If it overlaps any Root-owned
  tranche path, `AGENTS.md`, the Root receipt/handoff, `_LATEST.md`, DEL-02-03,
  or the D-GOV-35/SCA-004 outputs, stop and return the overlap for semantic
  supervision. App-only changes may proceed under the explicit authorization.
- Merge with a non-rebase merge commit and a descriptive message. If any
  conflict occurs, stop without resolving it or widening authority.

## Post-merge evidence

- Record merge SHA and both parents.
- Prove all three node commits remain ancestors of HEAD.
- Record `git status --short`, changed incoming paths, and any overlap result.
- Reproduce SHA-256 for `AGENTS.md`, `execution/_ScopeChange/_LATEST.md`,
  DEL-02-03 `ScopeOfWork.md`, and both steer source files.
- Confirm no push, PR creation, or PR merge occurred.

## Control write set

Only this instance folder's `STATUS.json` and `RETURN.md` in addition to the
authorized Git fetch/merge metadata. Leave both control files uncommitted for
the later Receipt-114 closeout commit.

## Return contract

Return `COMPLETE` with fetched SHA, merge SHA, parents, overlap evidence,
protected identities, and clean/confined state; or `BLOCKED` with exact
conflict/overlap evidence. Never rebase or rewrite the node commits.
