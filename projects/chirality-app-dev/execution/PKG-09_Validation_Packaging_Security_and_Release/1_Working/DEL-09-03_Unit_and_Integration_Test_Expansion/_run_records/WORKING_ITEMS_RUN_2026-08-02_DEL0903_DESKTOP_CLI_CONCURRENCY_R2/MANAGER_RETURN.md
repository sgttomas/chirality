# WORKING_ITEMS Return — DEL-09-03 Shared-Daemon Proof R2

RunID: `WORKING_ITEMS_RUN_2026-08-02_DEL0903_DESKTOP_CLI_CONCURRENCY_R2`

PackageCoverage: `PKG-09 / DEL-09-03 only`

Verdict: `ACCEPTED / COMPLETE WITH NON-BLOCKING PR-CI RERUN ADVISORIES`

## Accepted Agent 2 return

WORKING_ITEMS accepts `AGENT2_RETURN.md`. The single serialized Agent 2 reached
the mandatory smallest-test milestone before refinement, then directly proved
every frozen conjunct at the existing public seams without modifying runtime or
App implementation source:

1. Desktop and CLI use one daemon socket, project credential, and session;
2. the real `PiAgentEngineAdapter` reaches authenticated fake oMLX;
3. same-session CLI competition is rejected with
   `SESSION_TURN_IN_PROGRESS` while the Desktop turn is active;
4. a second daemon owner is rejected on the live socket;
5. Desktop cancellation produces exactly one replayed durable terminal; and
6. distinct Desktop and CLI Agent 2 sessions coexist.

The accepted test is
`frontend/src/__tests__/integration/runtime-desktop-cli-shared-daemon.integration.test.ts`
at SHA-256
`1da25070630446f3c539c856e9f7b9f18ff903a23ea52c09a01de9594acc45be`.

## Deliverable effect

The sole fake-oMLX Desktop/CLI concurrency bullet and its now-empty
`## Remaining` heading were removed from DEL-09-03 `_STATUS.md`. A dated
history entry and package-local `MEMORY.md` evidence entry were added. Current
State remains `IN_PROGRESS`; Checking Approval SHA remains
`8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`.

Accepted closeout hashes:

- `_STATUS.md`:
  `81e0d5059c687229056685799c6b48f22dcd234d8d347466069fe90de0ee1590`;
- `MEMORY.md`:
  `ce4d05506b0c89d61808a247a80fe4bd099aad1c0d3eac3e33c6b15437c4ea61`;
- `AGENT2_RETURN.md`:
  `2a31ae0bf1fbacf756f536eade782f4efa58d78efff706a4016b771fc01ed352`.

## Validation fan-in

Accepted passing evidence:

- focused Vitest: 1 file, 2 tests;
- full frontend Vitest: 141 files passed / 1 skipped, 1098 tests passed /
  4 skipped;
- frontend TypeScript check;
- production Next, Electron, and runtime-CLI build;
- receipt validator through Receipt 52;
- authority corpus v18: eight `MATCH`;
- status census: 53/53 `IN_PROGRESS` with no practitioner finding severities;
- repo-wide practitioner self-check: exit 0 with only pre-existing cross-root
  review/warn/info/not-applicable findings;
- practitioner-harness pytest: 349 passed;
- final `git diff --check`, trailing-whitespace, containment, lifecycle,
  Checking Approval, and temporary-symlink-removal checks.

Two environment-dependent checks remain explicit non-blocking rerun
advisories, without weakened acceptance:

1. rerun `runtime/tests/daemon.test.ts` and
   `runtime/tests/turn-hardening.test.ts` in PR CI with the runtime workspace
   lock-installed; this worktree had no `runtime/node_modules`, so Vite could
   not resolve `@chirality/runtime-core` before collection;
2. rerun the App premerge gate in PR CI with the live registered shared-runtime
   socket, token file, project ID, and canonical project-root bindings; the
   local production-server run reached the App but correctly returned HTTP 503
   without those bindings.

No further long test rerun was authorized at package closeout.

## Preservation and handoff

No `runtime/**`, Electron/App implementation, dependency, decomposition,
lifecycle, Checking Approval, decision, Task Management, parity, D-APP-84,
historical UNKNOWN-relation, other-package, shared receipt, or completion-log
surface changed. The lock-matched temporary frontend `node_modules` symlink was
removed before fan-in.

DerivativeStatus: the R2 run records are package-local process and verification
evidence; they do not amend authoritative decomposition truth.

CrossPackageNotice: the direct proof is available to HELP_HUMAN for C04/C16
evidence reconciliation. C06 daemon-crash/model-drain recovery remains Root
owned, excluded, and unclaimed.

RequestedAgent0Action: accept this package-local proof and route the bounded
change to CHANGE, retaining both PR-CI rerun advisories.
