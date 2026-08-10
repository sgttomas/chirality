# Sealed replay manifest — D-APP-92 Option A

Status: `SEALED v1 — NO TIMING OR SEQUENCE SUBSTITUTION`

## Fixed runtime identity

- Runtime root: `/private/tmp/chirality-dapp92-option-a-20260804`.
- Isolated HOME: `/private/tmp/chirality-dapp92-option-a-20260804/home`.
- Isolated userData/store: `/private/tmp/chirality-dapp92-option-a-20260804/user`.
- Helper and GUI executable paths are exactly C044 and C045.
- Public test project identifier: `chirality-app-dev`.
- Registration uses the existing authenticated public CLI path. The token is
  created/consumed internally; no command, log, snapshot, trace, or retained
  artifact may read, print, export, record, or expose its value.

## Fixed sequence

1. Prove the runtime root absent; create the three fixed isolated directories.
2. Create an absent-PID stale socket/owner state only through one run-owned
   helper launch followed by explicit SIGKILL; record PID, inode, mode, owner
   public schema/PID only. Never open the token file.
3. Launch the exact helper directly and start the monotonic replay clock.
4. Poll only for public readiness/socket/owner existence, bounded at 80 × 0.1 s.
5. Wait exactly 28.0 seconds after helper-ready before launching the GUI, matching
   the earlier R3 helper-to-GUI interval to the nearest retained whole-second
   evidence without claiming unavailable sub-second identity.
6. Register the public project and establish authenticated GUI contact through
   the existing CLI/GUI path; retain only exit status, public project ID, and
   redacted success/binding state.
7. Record contact time, then wait exactly 102.0 seconds before the first signal,
   matching the earlier R3 retained contact-to-signal interval. No GUI input or
   automation occurs during the wait.
8. Before signal: record helper/GUI PIDs, parent/group/state/elapsed time;
   helper Unix descriptors and TCP census; socket/owner inode/mode/uid/gid/size;
   package/source hashes; and one same-user bounded stack sample if C050 runs
   without special authority.
9. An adequate authorized native tracer must already be attached and recording
   before signal. Without it, do not send the replay signal; return an approval
   stop after cleanup.
10. Send exactly `/bin/kill -TERM <EXACT_HELPER_PID>` once. Record wall and
    monotonic time immediately before invocation.
11. Poll helper existence exactly 80 times at 0.1 seconds, stopping early only
    if the helper exits. Record every poll/time/result. Do not send another
    signal during the credited window.
12. Record post-window process/socket/owner/descriptors, exact exit status if
    available, raw trace, and GUI survival. Freeze evidence before cleanup.
13. Clean the GUI gracefully, then use exact run-owned-PID SIGKILL only if the
    bounded cleanup fails. Remove generated/runtime state and restore all
    product/config/test bytes.

## Trace targets and limits

Desired distinguishers are OS signal delivery, libuv/JS `SIGTERM` callback
entry, Electron `before-quit`, App `teardown()`, and Root-stop call/settlement.
The native tracer may record breakpoint/event names, exact PID/time, thread,
and bounded backtraces only. It may not dump process memory, environment,
arguments containing credentials, keychain state, tokens, or secrets. Any
unavailable seam remains `UNKNOWN`; absence of an observable is not converted
to a zero inference.

## Exact deviations

Any command, path, PID-selection method, source/package hash, delay, poll count,
snapshot order, tracer, or argument change is a stop. The retained R3 record is
not byte-complete for every original shell action, so this manifest truthfully
seals the closest evidence-supported replay rather than claiming bit-for-bit
historical command identity. That limitation must remain explicit in fan-in.
