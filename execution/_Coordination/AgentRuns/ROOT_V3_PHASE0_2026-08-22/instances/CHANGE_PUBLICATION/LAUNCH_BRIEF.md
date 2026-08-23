# CHANGE Brief — Initial Publication and PR Creation

Run ID: `ROOT_V3_PHASE0_2026-08-22`

Caller: `HELP_HUMAN`.

Role: `CHANGE` Agent 1. Read and obey `AGENTS.md` and
`agents/AGENT_CHANGE.md`.

## Owner authorization of record

Ryan Tufts, 2026-08-22:

> I authorize you to fetch and merge the latest `origin/main` into this branch,
> then complete Receipt 114, validation, push, and PR creation without merging
> the PR.

## Authorized objective

Publish the already validated committed branch
`codex/root-v3-phase0-2026-08-22` through merge commit
`0bd042e5299c81301cc726bc54eea265285b4159`, then create exactly one
ready-for-review PR to `main`. This initial publication deliberately precedes
the append-only Receipt 114 so HELP_HUMAN can record the actual PR identity in
the receipt without later editing it. HELP_HUMAN will append the receipt and
handoff in a final commit, rerun every closeout validator, and push that commit
to the same PR.

Do not stage or commit the untracked run-control folders. Do not merge the PR,
approve it, enable auto-merge, force-push, rebase, delete the branch, create a
second PR, or change any GitHub issue/project state.

## Required preflight

- Confirm branch, HEAD, clean index, and the three node ancestors plus merge
  parents.
- Confirm current `origin/main` is the merge's second parent. If it advanced
  again, stop and return the exact new SHA; do not fetch/sync again under this
  brief.
- Confirm these integrated checks already passed at current HEAD:
  candidate whitespace, agent instructions, instruction entrypoints, live
  manifest corpus, direct N2 draft manifest, Task Management register,
  `git diff --check`, and inactive patch `git apply --check`.

## Push and PR

Push the branch normally to `origin` with upstream tracking. Create one
non-draft PR against `main` with title:

`Root v3 Phase 0: D-GOV-35 proposal, DEL-02-03 prep, and SCA-004`

The body must summarize N1/N2/N3, state the clean authorized main merge,
enumerate the passing checks, and make the gates conspicuous:

- D-GOV-35 remains awaiting owner ruling.
- DEL-02-03 M2 application remains blocked on that ruling and separate
  application authority.
- SCA-004 remains awaiting owner acceptance and `_LATEST.md` is untouched.
- all ten DEL-02-06 bindings remain `HELD_UNAVAILABLE`.
- no protected instruction, status, pointer, pin, runtime, or project source
  was changed by this Root tranche.
- no merge is authorized/performed.

## Control write set

Only this instance folder's `STATUS.json` and `RETURN.md` in addition to the
authorized remote branch/PR state. Leave these files uncommitted for Receipt
114's closeout commit.

## Return contract

Return branch remote identity, push result, PR number/URL/title/base/head,
preflight evidence, and explicit confirmation that no PR merge or other
forbidden act occurred. Stop on any remote drift or existing-PR ambiguity.
