STUB — UNFILLED
Required content: exact execution-approval gate, adjacent frozen-manifest
binding, five-component scope, exact commands/interactive bytes requested,
non-authorized effects, stop conditions, and owner approval-return surface.
# D-APP-93 Hash-Specific Owner Approval Request

Status: APPROVAL REQUIRED — NOT EXECUTABLE

## Requested decision

Approve or decline one owner-operated D-APP-93 Option A trace bound only to:

- adjacent `freeze/FROZEN_PACKET.sha256` at manager-presented SHA-256 `<FROZEN_PACKET_MANIFEST_SHA256>`;
- exact numeric direct-child helper PID `<EXACT_HELPER_PID>`;
- the neutral Step 0 and LLDB forms below;
- a separately frozen and separately approved first-signal act, absent from this packet;
- the exact same-PTY cleanup bytes; and
- an absolute 150-second attach-to-confirmed-detach deadline.

Changed manifest, packet byte, path, PID, signal act, form, cleanup byte, or deadline requires a new exact request.

## Neutral Step 0

```text
EXPECTED_OWNER_PREFLIGHT_SHA256=<EXPECTED_OWNER_PREFLIGHT_SHA256> EXPECTED_LLDB_SIGNAL_TRACE_SHA256=<EXPECTED_LLDB_SIGNAL_TRACE_SHA256> /bin/zsh /Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_ELEVENTH_PACKET_AUTHORING_2026-08-10/packet/scripts/OWNER_PREFLIGHT.zsh /Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_ELEVENTH_PACKET_AUTHORING_2026-08-10 <EXACT_HELPER_PID>
```

Step 0 hashes both packet scripts and pinned host tools, checks preflight syntax, exact LLDB path/version, and metadata for only the exact PID. It must exit `0` with final `PREFLIGHT_STATUS|PASS`; any mismatch or shape deviation stops the request.

## Exact proposed attach form

```text
/usr/bin/xcrun lldb -p <EXACT_HELPER_PID> -s /Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_ELEVENTH_PACKET_AUTHORING_2026-08-10/packet/scripts/lldb-signal-trace.txt
```

No PID search, discovery, substitution, relaunch, or fallback is allowed. The script traces only `__sigtramp`, `uv__signal_handler`, `SignalWrap.*OnSignal`, `electron::Browser::Quit|Browser::Quit`, and `-[NSApplication terminate:]`, at most 16 frames each, continuing after each; it sets `process handle SIGTERM -s false -n true -p true` and ends setup with `process continue`.

## First-signal boundary

This packet neither defines nor authorizes the first-signal act. Before execution, its exact actor, target, form/bytes, timing, and authority must exist in separate frozen material and separate explicit approval. Nothing may be inferred from historical semantics.

## Exact same-PTY cleanup bytes

Before 150 seconds elapse, in the same PTY, send:

1. `0x03`;
2. `process detach` plus `0x0a`: `70 72 6f 63 65 73 73 20 64 65 74 61 63 68 0a`;
3. `quit` plus `0x0a`: `71 75 69 74 0a`.

Detach must be confirmed within 150 seconds. No alternate cleanup is authorized.

## Excluded effects

Excluded are PID search/substitution/relaunch; pre-approval debugger or signal effects; any non-separately-approved signal; memory/environment reads; keychain or credential request/read/print/copy/use/change; build, package, overlay, ingestion, fixture, node-toolchain, cleanup, or other product/runtime/system mutation; D-APP-94 runtime authority; and any claim that preflight, clearance, or capture equals acceptance or closure.

## Proposed exact token

Replace both placeholders with exact literals:

```text
APPROVE D-APP-93 OPTION A PACKET MANIFEST SHA256 <FROZEN_PACKET_MANIFEST_SHA256> FOR EXACT DIRECT-CHILD HELPER PID <EXACT_HELPER_PID>; OWNER-OPERATED LLDB ATTACH AND SAME-PTY 0x03/PROCESS-DETACH-0x0A/QUIT-0x0A CLEANUP ONLY; ABSOLUTE ATTACH-TO-DETACH LIMIT 150 SECONDS; FIRST-SIGNAL ACT REQUIRES SEPARATE FROZEN APPROVAL; ALL OTHER EFFECTS EXCLUDED
```

Until that exact token and separate first-signal approval exist, attach, first signal, interrupt, detach, and quit remain REVIEWED_NOT_EXECUTED.
