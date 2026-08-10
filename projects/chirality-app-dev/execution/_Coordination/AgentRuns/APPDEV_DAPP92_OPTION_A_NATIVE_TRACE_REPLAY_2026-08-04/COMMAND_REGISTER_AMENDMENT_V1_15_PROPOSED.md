# Proposed command-register amendment v1.15 — Attempt-7 timing-only mock retry

Status: `PROPOSED — OWNER COMMAND APPROVAL REQUIRED — NOT EXECUTED`

The accepted Attempt-6 verifier at SHA-256
`fed5aa422277720f2d74d8cfefe042f82ba76b7a8b05ac9d05889c143c91a5b5`
permits only a fresh immutable, owner-gated timing/order repair packet. Attempt
6 proved the no-target LLDB PTY shape and therefore LLDB is not rerun here. It
also produced a schema-valid, matching-PID second-session sentinel, but the
five-second controller window expired before the sentinel was consumed.

Attempt 7 changes only the mock controller. The v2 controller:

- spawns only its own direct child `/bin/sleep 35`;
- registers the child-exit promise immediately after spawn;
- durably writes `controller.json` and then immediately emits its exact compact
  `ATTACH_READY` JSON record as one newline-terminated PTY line;
- waits at most 30 seconds for the existing exact v1 second-session sentinel;
- rejects malformed, mismatched, late, or post-child-exit sentinels;
- sends no signal and performs no process inspection;
- writes `protocol-result.json` only after exact schema/PID/state matching and
  natural child exit with code `0` and no signal; and
- remains bounded by the 35-second mock-child lifetime plus local command-tool
  scheduling overhead; the session-A poll is capped at 45 seconds.

The exact scripts are frozen at:

- `proposed/attempt7/mock-two-session-controller-v2.mjs` — SHA-256
  `9a756a7eb272bcc270e3a482f2664b8290cffac5f236230ccf7a4dfe38ebb9c4`;
- unchanged `proposed/attempt6/mock-second-session.mjs` — SHA-256
  `02d651afbc13e7145de744977673aa54f4e9d7dd2411c06e2665537550ade11b`.

| ID | Class | Proposed state | Exact tool/command or control | Purpose / stop condition |
|---|---|---|---|---|
| C231 | read-only/unprivileged | OWNER APPROVAL REQUIRED | `/usr/bin/shasum -a 256 /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt7/mock-two-session-controller-v2.mjs` | Recompute and compare the v2-controller identity to `9a756a7eb272bcc270e3a482f2664b8290cffac5f236230ccf7a4dfe38ebb9c4`; stop on mismatch. |
| C232 | read-only/unprivileged | OWNER APPROVAL REQUIRED | `/usr/bin/shasum -a 256 /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt6/mock-second-session.mjs` | Recompute and compare the unchanged session-B script identity to `02d651afbc13e7145de744977673aa54f4e9d7dd2411c06e2665537550ade11b`; stop on mismatch. |
| C233 | read-only/unprivileged | OWNER APPROVAL REQUIRED | `/bin/test ! -e /private/tmp/chirality-dapp92-attempt6-protocol` | Fixed mock root must be absent before execution. |
| C234 | temporary mock preparation | OWNER APPROVAL REQUIRED | `/bin/mkdir -p /private/tmp/chirality-dapp92-attempt6-protocol` | Create only the fixed mock root. |
| C235 | temporary mock preparation | OWNER APPROVAL REQUIRED | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt7/mock-two-session-controller-v2.mjs` | Start only in PTY/session A. Retain the live session and yield as soon as its first newline-terminated output parses as the exact controller record with schema `chirality-dapp92-two-session-controller/v1`, positive numeric `directChildPid`, child `/bin/sleep 35`, and state `ATTACH_READY`. Stop if no such line appears within 5 seconds or any other output/error appears first. No bytes are sent to session A. |
| C236 | read-only/unprivileged | OWNER APPROVAL REQUIRED | `/usr/bin/shasum -a 256 /private/tmp/chirality-dapp92-attempt6-protocol/controller.json` | From session B after C235 readiness, bind the durably written controller record before acknowledgment. |
| C237 | temporary mock preparation | OWNER APPROVAL REQUIRED | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt6/mock-second-session.mjs` | Session B executes the byte-identical frozen script, validates the exact controller schema/direct-child PID/state, and writes one matching sentinel. No inspection, attach, or signal. |
| C238 | temporary mock preparation | OWNER APPROVAL REQUIRED | On the success path only, poll the existing C235 session A without sending bytes until it exits, maximum 45 seconds after C235 started | Require one exact result line and exit code `0`; stop the success path on timeout, schema/PID mismatch, non-natural child exit, other output, or nonzero controller exit. This does not replace mandatory C242 session quiescence. |
| C239 | temporary evidence | OWNER APPROVAL REQUIRED | `/bin/mkdir -p /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt7-preparation` | Create only the run-local Attempt-7 preparation-evidence directory after C238 passes. |
| C240 | temporary evidence | OWNER APPROVAL REQUIRED | `/bin/cp -p /private/tmp/chirality-dapp92-attempt6-protocol/protocol-result.json /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt7-preparation/protocol-result.json` | Preserve only the successful protocol result; do not copy controller, sentinel, environment, or process data. |
| C241 | read-only/unprivileged | OWNER APPROVAL REQUIRED | `/usr/bin/shasum -a 256 /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt7-preparation/protocol-result.json` | Bind the sole copied protocol-result evidence. |
| C242 | mandatory session quiescence | OWNER APPROVAL REQUIRED | After any C235 invocation, poll only the existing C235 session A without sending bytes until it is confirmed terminal, with a hard deadline 45 seconds after C235 started. If C238 already recorded it terminal, confirm that terminal state; if C235 returned without a session identifier, require its command result to be terminal. | Run on every terminal path after C235, including readiness failure/timeout and any C236-C241 stop. No interrupt, EOF, signal, or process inspection is permitted. Do not proceed to root removal while session A could be live. On a 45-second timeout, stop with cleanup blocked and preserve the root for a new owner ruling. |
| C243 | temporary mock cleanup | OWNER APPROVAL REQUIRED | `/bin/rm -rf /private/tmp/chirality-dapp92-attempt6-protocol` | Only after C242 proves session A terminal, remove only the exact fixed mock root; mandatory on every terminal path after C234. |
| C244 | read-only/unprivileged | OWNER APPROVAL REQUIRED | `/bin/test ! -e /private/tmp/chirality-dapp92-attempt6-protocol` | Prove exact mock-root cleanup. |

C242 is mandatory after every C235 invocation and always precedes C243. It
waits only for the controller's own bounded child-await path; it sends no bytes
or signal and performs no process inspection. C243-C244 are mandatory on every
terminal path after C234, including a C235 readiness failure or timeout, but
C243 must not run unless C242 has proved session A terminal. C239-C241 execute
only after C238 passes. Any hash mismatch, pre-existing root, unexpected
output, schema/PID/state mismatch, early or non-natural child exit, timeout,
command deviation, or cleanup failure stops the probe. No proposed command may
be retried or altered under this packet.

A pass permits preparation of a fresh, separately governed real-runtime
packet only. It does not authorize that packet, any real process, or any
runtime action. No LLDB rerun, target or attach, package/reconstruction, cache
seed, network, helper, GUI, signal, replay, credential, memory or environment
dump, process inspection, product remedy, release, Git, Task Management,
foreign-loop, or other authority is proposed. C196/C197 remains separately
approved but unused.
