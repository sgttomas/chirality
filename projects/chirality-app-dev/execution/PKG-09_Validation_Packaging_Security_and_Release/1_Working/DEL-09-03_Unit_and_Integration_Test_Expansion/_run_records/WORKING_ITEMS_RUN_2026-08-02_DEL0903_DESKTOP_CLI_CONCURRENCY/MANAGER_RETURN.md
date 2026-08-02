# WORKING_ITEMS Return — DEL-09-03 Shared-Daemon Proof

RunID: `WORKING_ITEMS_RUN_2026-08-02_DEL0903_DESKTOP_CLI_CONCURRENCY`

PackageCoverage: `PKG-09 / DEL-09-03 only`

Verdict: `BLOCKED / NO IMPLEMENTATION RETURN ACCEPTED`

## Accepted outputs

Only the activation, frozen briefs, attempt disposition, and this manager
handoff are accepted as process evidence. Neither Agent 2 attempt produced a
test, focused test result, or blocker analysis that meets the fan-in gate.

## Deliverable effect

None. DEL-09-03 remains `IN_PROGRESS`; its lifecycle and Checking Approval SHA
are unchanged; its fake-oMLX Desktop/CLI concurrency Remaining item is retained
verbatim.

## Blocker

This is an execution-return blocker, not evidence that the public seam is
missing. Existing current bytes expose the ingredients that a future bounded
attempt should compose:

- App Desktop compatibility adapter:
  `frontend/src/lib/runtime-client/runtime-daemon-harness-port.ts`;
- generic authenticated client: `runtime/packages/client/src/client.ts`;
- generic daemon/service setup patterns: `runtime/tests/daemon.test.ts` and
  `runtime/tests/turn-hardening.test.ts`;
- real App Pi/oMLX adapter and fake provider pattern:
  `frontend/src/__tests__/integration/pi-omlx-wire.integration.test.ts` and
  `fake-openai-loopback.ts`.

Those ingredients were not assembled into executable proof during this run.
Therefore none of the five intended conjuncts is credited, and no minimal seam
change is proposed as necessary.

## Recommended next lawful approach

Use one fresh implementation-first Agent 2 with the same frozen test filename
and no preliminary survey stage. Its first patch should inline the small
project/runtime fixture from `runtime/tests/daemon.test.ts`, register an
`app-dev` project, register the real `PiAgentEngineAdapter` configured through
the existing `fake-openai-loopback.ts`, start one `RuntimeDaemon`, and construct
two clients over the same socket and project token:

1. a Desktop-side `RuntimeDaemonHarnessPort`; and
2. a generic CLI-side `RuntimeClient`.

The first focused compile/run should assert only shared `daemonStatus()`
identity. Later patches should add, in order, shared-session visibility,
same-session lock rejection, second-daemon owner rejection, Desktop cancel with
one replayed terminal, and distinct-session coexistence. This staged assertion
order keeps failures attributable without changing any implementation seam.

## Validation and preservation

Write containment is limited to this new DEL-09-03 run directory. `git diff`
contains no frontend, runtime, status, memory, dependency, decomposition,
lifecycle, decision, Task Management, receipt, completion-log, or other-package
change. Frontend/runtime suites were not run because no implementation or test
candidate reached fan-in; the relevant rerun requirement is a fresh bounded
implementation attempt followed by the full validation matrix in the sealed
brief.

Process-record validation passed: receipt ledger structure; App authority corpus
v18 `MATCH`; 53/53 deliverable status census (`IN_PROGRESS`); repo-wide
self-check exit 0 with only pre-existing cross-root REVIEW/WARN findings; and
the practitioner-harness suite (349 passed). Whitespace, final newline, target
absence, containment, and exact DEL-09-03 status/memory preservation checks also
passed.

DerivativeStatus: process evidence only; not authoritative decomposition truth
and not verification evidence.

CrossPackageNotice: none. C04 remains open; C06 remains Root owned.

RequestedAgent0Action: retain the current Remaining item and either retry later
with a fresh bounded test implementer or choose a different lawful App tranche.
