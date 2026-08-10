# Proposed command-register amendment v1.14 — Attempt-6 preparation only

Status: `PROPOSED — OWNER COMMAND APPROVAL REQUIRED — NOT EXECUTED`

Attempt 5 consumed its sole C216 package invocation and terminalized with
verified package/identity/cleanup evidence. No package retry, helper/GUI launch,
PID work, LLDB invocation, signal, or replay authority carries forward from
that package-only grant.

The next real runtime graph needs two concurrent execution sessions: a
controller must keep the direct-child helper alive and expose one exact numeric
PID while C196 owns an interactive LLDB PTY; a fail-closed sentinel must release
the controller only after the attach session is objectively ready. Two bounded
preparers could not safely freeze that orchestration without live tool-shape
evidence. This amendment therefore proposes only a non-product preparation
probe. It launches LLDB with no target, then proves a two-session direct-child
PID/sentinel handshake using only `/bin/sleep`. It attaches to no process and
executes no package or runtime command.

The exact controller and second-session scripts are frozen at:

- `proposed/attempt6/mock-two-session-controller.mjs` — SHA-256
  `a6ebf793e38184f6cdb1b12fdda9a68360987b9e98bc84b09e966d168141538b`;
- `proposed/attempt6/mock-second-session.mjs` — SHA-256
  `02d651afbc13e7145de744977673aa54f4e9d7dd2411c06e2665537550ade11b`.

| ID | Class | Proposed state | Exact tool/command or control | Purpose / stop condition |
|---|---|---|---|---|
| C217 | debugger preparation / no target | OWNER APPROVAL REQUIRED | Start PTY command `/usr/bin/xcrun lldb --no-lldbinit` | Prove the exact LLDB executable can be held as an interactive PTY without attaching to any process. Stop on privilege, entitlement, target, or prompt anomaly. |
| C218 | debugger preparation / no target | OWNER APPROVAL REQUIRED | On only the C217 PTY, send exact bytes `help process attach\n` | Exercise command-channel write only; no attach command or target. Retain public help/prompt output only. |
| C219 | debugger preparation / no target | OWNER APPROVAL REQUIRED | On only the C217 PTY, send exact bytes `quit\n` | Prove clean PTY termination with no target or debugger residue. |
| C220 | read-only/unprivileged | OWNER APPROVAL REQUIRED | `/bin/test ! -e /private/tmp/chirality-dapp92-attempt6-protocol` | Fixed mock root must be absent. |
| C221 | temporary mock preparation | OWNER APPROVAL REQUIRED | `/bin/mkdir -p /private/tmp/chirality-dapp92-attempt6-protocol` | Create only the fixed mock root. |
| C222 | temporary mock preparation | OWNER APPROVAL REQUIRED | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt6/mock-two-session-controller.mjs` | Start in PTY/session A. Spawn only direct-child `/bin/sleep 10`, freeze its numeric PID, and wait at most 5 seconds for the exact sentinel. No signal is sent; the mock child exits naturally. |
| C223 | read-only/unprivileged | OWNER APPROVAL REQUIRED | `/usr/bin/shasum -a 256 /private/tmp/chirality-dapp92-attempt6-protocol/controller.json` | From session B after the C222 attach-ready record exists, bind the mock PID record before acknowledgment. |
| C224 | temporary mock preparation | OWNER APPROVAL REQUIRED | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt6/mock-second-session.mjs` | Session B validates the exact direct-child PID record and writes one matching sentinel. No process inspection, attach, or signal. |
| C225 | temporary mock preparation | OWNER APPROVAL REQUIRED | Poll only existing C222 session A without sending bytes until it exits, maximum 15 seconds | Prove the controller consumed the matching sentinel and the mock child exited naturally; stop on timeout. |
| C226 | temporary evidence | OWNER APPROVAL REQUIRED | `/bin/mkdir -p /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt6-preparation` | Create only the run-local preparation-evidence directory. |
| C227 | temporary evidence | OWNER APPROVAL REQUIRED | `/bin/cp -p /private/tmp/chirality-dapp92-attempt6-protocol/protocol-result.json /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt6-preparation/protocol-result.json` | Preserve only the mock PID/sentinel/natural-exit result; no environment or process data. |
| C228 | read-only/unprivileged | OWNER APPROVAL REQUIRED | `/usr/bin/shasum -a 256 /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt6-preparation/protocol-result.json` | Bind the mock result. |
| C229 | temporary mock cleanup | OWNER APPROVAL REQUIRED | `/bin/rm -rf /private/tmp/chirality-dapp92-attempt6-protocol` | Remove only the exact fixed mock root after evidence freeze; mandatory on every terminal path. |
| C230 | read-only/unprivileged | OWNER APPROVAL REQUIRED | `/bin/test ! -e /private/tmp/chirality-dapp92-attempt6-protocol` | Prove mock cleanup. |

C229-C230 are mandatory on every terminal path after C221. Any target attach,
privilege prompt, PID mismatch, sentinel mismatch, timeout, command deviation,
or cleanup failure stops the probe. No result authorizes the later real graph;
it supplies only tool-shape evidence for a fresh immutable runtime packet.

No package, cache seed, network, helper, GUI, process attach, signal, replay,
credential, memory, environment dump, product remedy, release, Git, Task
Management, foreign-loop, or other authority is proposed. C196/C197 remains
separately approved but unused.
