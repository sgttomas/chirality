STUB — UNFILLED
Required content: Step 0 owner-run preflight for every OWNER_PREFLIGHT entry;
exact pinned identities and recording form; operative owner-controlled LLDB
trace procedure; exact direct-child PID fence; 150-second attach-to-detach
bound; stop/deviation rules; evidence capture; cleanup limited to approved
interrupt, process detach, and quit; explicit no-authority-until-hash approval.
# D-APP-93 Owner-Operated Interactive Trace Runbook

Status: PREPARATION ONLY — NOT EXECUTABLE WITHOUT HASH-SPECIFIC OWNER APPROVAL

## Authority boundary

This packet prepares D-APP-93 Option A only. It grants no execution authority. The owner personally selects and enters one exact numeric direct-child helper PID, performs the future LLDB attach, performs the separately approved and frozen first-signal act, and performs the same-PTY interrupt, detach, and quit. No operative step may begin until the owner approves the adjacent `freeze/FROZEN_PACKET.sha256` by the exact manager-presented SHA-256.

D-APP-94 Option A is a planning baseline only. It grants no keychain, runtime, credential, attach, or signal authority.

C196/C197 historical semantics constrain the proposal to one sealed direct-child helper PID, enumerated breakpoint/backtrace capture, an absolute 150-second attach-to-detach limit, and same-PTY cleanup by interrupt byte `0x03`, `process detach` plus line feed, then `quit` plus line feed. Changed bytes, path, PID, manifest, or procedure require new exact approval.

## Fixed inputs

Exact run root:

`/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_ELEVENTH_PACKET_AUTHORING_2026-08-10`

The owner enters and records literally:

- `TARGET_PID`: one exact numeric PID personally selected by the owner; no search, discovery, substitution, fallback, or relaunch.
- `EXPECTED_OWNER_PREFLIGHT_SHA256`: manager-presented final SHA-256 of `packet/scripts/OWNER_PREFLIGHT.zsh`.
- `EXPECTED_LLDB_SIGNAL_TRACE_SHA256`: manager-presented final SHA-256 of `packet/scripts/lldb-signal-trace.txt`.
- `FROZEN_PACKET_MANIFEST_SHA256`: manager-presented SHA-256 of adjacent `freeze/FROZEN_PACKET.sha256`.

The owner records direct-child proof for the exact PID and confirms it identifies the intended sealed helper. The preflight prints metadata for that PID only; it never searches for or replaces it.

## Host pins and invocation chains

| Path | Expected SHA-256 | Chain |
|---|---|---|
| `/bin/zsh` | `528da649cc69510bd3c0bc565298cb602076b74a8ac3f18e793211b2a3c725e8` | script → `/bin/zsh` |
| `/usr/bin/xcrun` | `4bc0cc7099775fbe35c653ceb09e0e393d2e5ada024db872e0eb8c43500b4dc6` | LLDB form → `/usr/bin/xcrun` |
| `/Applications/Xcode.app/Contents/Developer/usr/bin/lldb` | `0035650adb4c8278122f70771e2e052a2b6e6d644a76745ffecf8c3a0bd686ca` | `/usr/bin/xcrun lldb` → pinned binary |
| `/bin/ps` | `a1d8c4a0a96fb6159f09d8f520f54df829db5f2eae9b9f3448e18f0bee61115c` | direct exact-PID metadata check |
| `/usr/bin/shasum` | `0812595f981a26f813d98dc380af14d4af427626c9339eda29eb849ae13de1e3` | direct hashing |
| `/usr/bin/perl` | `626702a74f85d2664872f6a7aa9b639306a2035211d442a24ea32ef0d48c8afd` | `/usr/bin/shasum` → `/usr/bin/perl` |

`/usr/bin/xcrun --find lldb` must return the pinned LLDB path. LLDB version output must contain `lldb-2100.0.17.203` and `Swift version 6.3.3`.

Probe calibration:

- AGENT_PROVEN: neutral zsh syntax, hash, xcrun path/version, and Perl-mediated shasum probes.
- OWNER_PREFLIGHT: `/bin/ps` exists, is readable, and is pinned, but its neutral invocation was denied in the agent sandbox with `PermissionError` errno 1.
- REVIEWED_NOT_EXECUTED: attach, first signal, interrupt, detach, and quit pending approval.

## Step 0 — mandatory neutral preflight

In the owner-controlled PTY, replace the three angle-bracket values with exact literals and run:

```text
EXPECTED_OWNER_PREFLIGHT_SHA256=<EXPECTED_OWNER_PREFLIGHT_SHA256> EXPECTED_LLDB_SIGNAL_TRACE_SHA256=<EXPECTED_LLDB_SIGNAL_TRACE_SHA256> /bin/zsh /Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_ELEVENTH_PACKET_AUTHORING_2026-08-10/packet/scripts/OWNER_PREFLIGHT.zsh /Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_ELEVENTH_PACKET_AUTHORING_2026-08-10 <TARGET_PID>
```

Record the exact form, parameters, start/end timestamps, exit, complete stdout/stderr, stream hashes, and every printed `actual=` in `packet/EVIDENCE_CAPTURE.md`.

Success shape is exit `0`, one `PREFLIGHT_BEGIN`, PASS pin records for both packet scripts and all six host identities, PASS syntax/path/version records, one `TARGET|status=OBSERVED` record for the exact PID, and final `PREFLIGHT_STATUS|PASS`. Failure shape is a nonzero exit and final stderr record `PREFLIGHT_STATUS|FAIL|reason=...`.

Stop on any mismatch, missing expected hash, shape deviation, inability to prove direct-child status, or nonzero exit. Do not repair, substitute, retry with another PID, or continue to LLDB under the request.

Step 0 is neutral. It must not attach, signal, launch, build, access keychains or credentials, inspect process memory or environment, clean up, or mutate product/runtime/system state.

## Approval and freeze gate

Step 0 success is evidence, not authority. Do not proceed unless the owner issues the exact token proposed in `packet/APPROVAL_REQUEST.md`, binding the manager-presented adjacent manifest SHA-256 and exact PID, and the first-signal act is separately frozen and approved. A change to either script invalidates preflight and requires a new freeze, hashes, preflight, and approval.

## Owner-controlled LLDB trace

Only after the gate is satisfied, use this exact form in one owner-controlled PTY:

```text
/usr/bin/xcrun lldb -p <EXACT_HELPER_PID> -s /Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_ELEVENTH_PACKET_AUTHORING_2026-08-10/packet/scripts/lldb-signal-trace.txt
```

The numeric PID must equal both the approved and Step 0 PID. Start the absolute 150-second deadline when attach begins. Capture the raw, unedited PTY transcript from before invocation through final quit. The LLDB script configures SIGTERM, installs only enumerated breakpoints, limits backtraces to 16 frames, continues after each stop, and finishes setup with `process continue`. It reads no memory, environment, keychain, or credentials.

This packet does not define or authorize the first-signal act. Perform only the exact act already separately frozen and approved; record act, actor, target, timestamp, and first breakpoint. Do not improvise a replacement.

## Same-PTY cleanup and evidence

Before 150 seconds elapse, in the same attach PTY, send exactly:

1. one interrupt byte `0x03`;
2. ASCII `process detach` followed by `0x0a`;
3. ASCII `quit` followed by `0x0a`.

Record timestamp and response for each. Attach-to-confirmed-detach must be at most 150 seconds. If cleanup is impeded, preserve the raw transcript and record the deviation; do not invent additional effects.

Complete every evidence field. Retain raw transcripts and cite hashes. Redact only in a derivative copy, document all redactions, and retain the original under the approved evidence boundary. This packet makes no runtime-success, authority, acceptance, PASS, or closure claim.
