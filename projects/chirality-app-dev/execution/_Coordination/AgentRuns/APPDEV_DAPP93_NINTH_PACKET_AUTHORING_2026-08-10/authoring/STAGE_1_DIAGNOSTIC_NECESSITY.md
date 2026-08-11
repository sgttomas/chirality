# Stage 1 — diagnostic necessity and minimal tool surface

Status: `COMPLETE — FRESH NINTH-LINEAGE ANALYSIS`

Purpose: retain only what directly supports the owner-operated LLDB causal
trace of the sealed helper's response to its first graceful termination
signal. Construction, build, overlay, installation, dependency projection,
and replay are prerequisite or later work, not trace commands.

## Required pre-run subject

The packet consumes one separately prepared helper bundle as a diagnostic
subject. Its executable must be present at the packet's frozen path and must
hash to `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`
before the packet may be approved or run. The subject is not a packet tool and
the packet does not construct, copy, alter, sign, install, or register it.
Absence or identity mismatch is a hard stop returned to the approval gate.

## Candidate dispositions

| Candidate | Disposition | One-line trace necessity |
|---|---|---|
| `/bin/zsh` | RETAIN | Owns the single interactive terminal and expresses exact shell constructs without ambient aliases or startup files. |
| `/usr/bin/env` | RETAIN | Starts every shell/tool form under the frozen minimal environment rather than ambient executable selection. |
| `/usr/bin/printf` | RETAIN | Emits exact, non-secret step, timestamp, PID, stop, and deviation evidence records. |
| `/bin/test` | RETAIN | Enforces absence, identity-adjacent, target, socket, and cleanup gates before later acts. |
| `/bin/mkdir` | RETAIN | Creates only the isolated private evidence, HOME, keychain-parent, user-data, and return directories. |
| `/usr/bin/sw_vers` | RETAIN | Binds the macOS version on which signal, Keychain, Electron, and LLDB semantics are observed. |
| `/usr/bin/uname` | RETAIN | Binds the host architecture relevant to the helper and debugger binary identities. |
| `/usr/bin/shasum` -> `/usr/bin/perl` | RETAIN | Binds the packet, diagnostic subject, debugger script, tool binaries, transcript, and returned evidence by SHA-256. |
| `/usr/bin/security` | RETAIN | Creates, observes, and deletes only the sealed-HOME login keychain required by the ruled isolated baseline. |
| `/bin/ps` | RETAIN | Proves the numeric target is the exact direct child of the owner shell immediately before attach and first signal. |
| `/usr/bin/awk` | RETAIN | Parses the declared PID/PPID fields and enforces the 150-second elapsed bound without a broad process search. |
| `/bin/date` | RETAIN | Records UTC epochs around attach, first signal, detach, and terminal return. |
| `/usr/bin/xcrun` -> Xcode `lldb` | RETAIN | Attaches the frozen debugger script to the one bound helper PID and captures the causal seam. |
| `/usr/bin/tee` | RETAIN | Preserves the interactive LLDB byte stream while leaving the owner in the same PTY. |
| `/bin/kill` | REMOVE | The ruled first signal is the owner's Activity Monitor Quit action; a shell signal would weaken same-PTY owner causation and is unnecessary. |
| `/bin/sleep` | REMOVE | No automated timer, polling loop, supervisor, or replay is needed for the owner-observed trace. |
| `/bin/rm` | RETAIN | Removes only the isolated disposable keychain/root after evidence retention and terminal-safety gates pass. |

## Explicitly removed dependency surface

`npm`, `node`, dependency installation, builds, packaging, archive extraction,
overlays, copying product bytes, tests, typechecking, package inventory,
LaunchAgent manipulation, and replay are absent. They do not make the LLDB
trace more causally discriminating. Any required helper package is prepared
and approved separately before this packet reaches its execution gate.

## Result

Fifteen catalog entries survive with trace-tied justifications. Two are
removed. The surviving external execution chains are direct Mach-O binaries
except the pinned `shasum` Perl shebang chain and the pinned `xcrun` to Xcode
LLDB chain. The subject helper is separately hash-bound and never treated as
proof that a packet tool exists.
