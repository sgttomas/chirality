# G1-DAPP50-REPAIR-COMMIT — CHANGE Brief

- **Role:** CHANGE
- **Branch/required HEAD:** `codex/app-dev-dapp50-headless-live-20260720` /
  `f67d44706f4b2b5495833f809cb0bc714d2bbc18`
- **Objective:** make W3 F-001 repair bytes reachable in one second content
  commit while preserving all uncommitted closeout/control/evaluation state.

Read full `AGENTS.md`, `agents/AGENT_CHANGE.md`, `updates/v6.md`, W3 terminal
records, and this brief. Reproduce zero staged paths, exact branch/HEAD, exact
repair hashes, `frontend/dist` absence, and separability from every other dirty
path. Return `BLOCK` on mismatch without cleanup or repair.

Stage and commit exactly:

1. `projects/chirality-app-dev/frontend/src/lib/harness/mcp/domain-headless-preview-runner.ts`
   at `d50d5c0c0b453547c8615f8239998b2860233bca6ab71b02e4cd9a135ba86109`;
2. `projects/chirality-app-dev/frontend/src/__tests__/lib/domain-headless-preview-runner.test.ts`
   at `133c8272ccce14f15a566363b9e46450e0b6d5b697242e752c815589dd69eb41`.

Run worktree and cached diff checks. Commit message:
`fix(app-dev): validate headless runner output contract`.

Do not stage any W2 closeout, status, receipt, pull contract, control,
evaluation, ignored/build, or other path. Do not push, open PR, merge, rebase,
amend, reset, stash, clean, delete, repin, edit content, or append a receipt.

After commit, verify the single parent is the required HEAD and the delta is
exactly two paths. Write terminal `RETURN.md`, `HANDOFF.md`, and `STATUS.json`
in this G1 instance unstaged. Return `ACCEPT | BLOCK` with commit SHA, parent,
paths/hashes, remaining dirty-state containment, and W4 as the only next gate.
