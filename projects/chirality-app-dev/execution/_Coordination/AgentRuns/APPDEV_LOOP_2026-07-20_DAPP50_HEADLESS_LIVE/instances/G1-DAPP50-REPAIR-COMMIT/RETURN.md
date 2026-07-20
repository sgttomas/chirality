# G1 D-APP-50 Repair Commit Return

## Terminal result

`ACCEPT`

CHANGE created one local commit containing exactly the two W3-repaired paths.
No push, pull request, merge, rebase, amend, reset, stash, clean, deletion,
repin, receipt update, lifecycle update, or implementation edit was performed
by G1.

## Commit evidence

- Branch: `codex/app-dev-dapp50-headless-live-20260720`
- Commit: `fcf152bdae1e1764b11dfabf3f87d50c5680213d`
- Single parent: `f67d44706f4b2b5495833f809cb0bc714d2bbc18`
- Subject: `fix(app-dev): validate headless runner output contract`
- Commit delta: exactly two paths:
  1. `projects/chirality-app-dev/frontend/src/lib/harness/mcp/domain-headless-preview-runner.ts`
     — SHA-256 `d50d5c0c0b453547c8615f8239998b2860233bca6ab71b02e4cd9a135ba86109`
  2. `projects/chirality-app-dev/frontend/src/__tests__/lib/domain-headless-preview-runner.test.ts`
     — SHA-256 `133c8272ccce14f15a566363b9e46450e0b6d5b697242e752c815589dd69eb41`

The pre-commit branch, HEAD, empty-index, W3 terminal-evidence hashes,
repair-file hashes, `frontend/dist` absence, and worktree-diff checks all
passed. The staged diff named only the two approved paths, passed
`git diff --cached --check`, and reproduced both required hashes. The
post-commit parent, path population, and committed blob hashes were then
reproduced directly from the commit.

## Dirty-state containment

The index is empty after the commit. The two repair paths are clean. Existing
tracked closeout changes (`_STATUS.md`, D-APP-48 pull contract, and
`LOOP_RECEIPTS.md`) and existing untracked run-control, evaluation, and
closeout/run-record evidence remain outside the commit. This return, sibling
handoff, and terminal status are also untracked control evidence. No unrelated
dirty path was staged or modified by G1.

## Next gate

W4 is the only next released gate. It owns the separately gated D-APP-48
repin/correction and related closeout preparation. A fresh independent V2
EVALUATION and final publication remain downstream and unreleased here.
