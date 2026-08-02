# Agent 2 Return — DEL-09-03 Shared-Daemon Proof R2

RunID: `WORKING_ITEMS_RUN_2026-08-02_DEL0903_DESKTOP_CLI_CONCURRENCY_R2`

ChildInstanceID: `A2-DEL0903-R2`

Status: `COMPLETED_WITH_RERUN_ADVISORIES`

## Output

Implemented the frozen test-only target:

- `projects/chirality-app-dev/frontend/src/__tests__/integration/runtime-desktop-cli-shared-daemon.integration.test.ts`

The target directly proves:

1. one `RuntimeDaemon` owns one socket;
2. project `chirality-app-dev` is registered once and two `RuntimeClient` instances use the same socket path and project token file;
3. Desktop's `RuntimeDaemonHarnessPort` and the CLI client observe equal daemon/project state and the same runtime session;
4. the real `PiAgentEngineAdapter` reaches the existing authenticated fake-oMLX loopback through the bounded `read_file` tool posture;
5. a competing same-session CLI turn is rejected with typed code `SESSION_TURN_IN_PROGRESS` while the Desktop turn is active;
6. a second `RuntimeDaemon` cannot own the live socket and is rejected with the implementation-defined typed code `RESIDENCY_TRANSITION_IN_PROGRESS`;
7. Desktop cancellation settles the canonical runtime session to `interrupted` with exactly one replayed durable terminal event across `turn.completed`, `turn.failed`, `turn.cancelled`, and `turn.interrupted`;
8. separate Desktop and CLI Agent 2 sessions reach two concurrent fake-oMLX streams without a same-session conflict.

No runtime, Electron, App implementation, dependency, decomposition, lifecycle,
Checking Approval, decision, Task Management, parity, D-APP-84, UNKNOWN-relation,
shared receipt, or completion-log source was modified. No C06 daemon-crash or
model-drain recovery claim is made.

## Milestones and test-development evidence

- The first focused command, before dependency linking, was
  `npm test -- src/__tests__/integration/runtime-desktop-cli-shared-daemon.integration.test.ts`;
  it exited 127 because frontend-local `vitest` was absent.
- The primary and worktree frontend lockfiles matched at SHA-256
  `674fe2dab74572f21d26455498461d62eaa4218560e45024ed2a31e00c635ab8`.
  The brief-permitted temporary `frontend/node_modules` symlink was then used.
- The first compiled execution exposed macOS `/var` versus `/private/var`
  canonical-root identity. Binding the Desktop port to `realpath(projectRoot)`
  was the smallest test-fixture correction; focused Milestone 1 then passed 1/1.
- The real Pi/fake-oMLX plus same-session typed-rejection milestone passed 2/2.
- The first second-owner expectation used `FORBIDDEN`; execution returned
  `RESIDENCY_TRANSITION_IN_PROGRESS`. The runtime owner-recovery code confirms
  that live socket plus live/ambiguous owner deliberately uses the latter, while
  `FORBIDDEN` covers different unsafe recovery cases. The corrected focused run
  passed.
- The first cancellation/coexistence run reached its assertions but cleanup
  raced final asynchronous runtime writes and reported `ENOTEMPTY` for the test
  temp root. Polling both sessions to stable `interrupted` state removed the
  cleanup race. The final focused run passed 2/2 in 757 ms (542 ms tests).

## Validation

Passed:

- focused Vitest: 1 file, 2 tests;
- full frontend Vitest: 141 files passed / 1 skipped, 1098 tests passed / 4 skipped;
- frontend TypeScript check;
- production Next, Electron, and runtime-CLI build (including a clean rebuild
  after the dev-server premerge attempt);
- App loop receipt validator: frozen through Receipt 52, contract valid;
- App authority corpus v18: eight `MATCH`, no drift;
- practitioner status: 53/53 deliverables `IN_PROGRESS`, no finding severities;
- repo-wide practitioner self-check: exit 0 with pre-existing cross-root
  `REVIEW=4`, `WARN=27`, `INFO=14`, `NOT_APPLICABLE=1` only;
- practitioner-harness pytest: 349 passed;
- final whitespace, containment, and preservation checks recorded below.

Rerun advisories retained without weakening the checks:

1. Applicable runtime suites:
   `NODE_PATH=/Users/ryan/dev/chirality/runtime/node_modules /Users/ryan/dev/chirality/runtime/node_modules/.bin/vitest run tests/daemon.test.ts tests/turn-hardening.test.ts`
   exited 1 before collection because the current worktree has no
   `runtime/node_modules` and Vite could not resolve `@chirality/runtime-core`.
   The sealed scope did not permit a runtime dependency symlink. PR CI must rerun
   `runtime/tests/daemon.test.ts` and `runtime/tests/turn-hardening.test.ts` in its
   lock-installed runtime workspace.
2. App premerge:
   the dev-server attempt was invalidated by `EMFILE` watcher exhaustion and 404
   route responses. A clean rebuild followed by watcher-free production
   `next start` reached the App, but all eight premerge cases received HTTP 503
   because this test worktree had no live registered shared-runtime
   `CHIRALITY_RUNTIME_SOCKET_PATH`, project token, project ID, and canonical
   project-root binding. PR CI must rerun the owned shared-runtime premerge gate
   with those four bindings provisioned.

## Deliverable closeout

Because every frozen behavioral conjunct is directly executable and passing,
only the fake-oMLX Desktop/CLI concurrency bullet was removed from DEL-09-03
`## Remaining` (and the now-empty heading was removed). `_STATUS.md` received a
dated history entry and `MEMORY.md` received this evidence summary. Current
State remains `IN_PROGRESS`; Checking Approval SHA remains
`8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`.

The temporary frontend `node_modules` symlink was removed before return.
