# Stage 2 — governing requirements matrix

Status: `COMPLETE — AUTHORING CONTRACT FIXED`

| Requirement | Packet implementation | Acceptance / stop rule |
|---|---|---|
| Preparation only | Every operative command is documentary; this author runs only harmless scratch probes. | Any runtime, helper, debugger, Security, signal, GUI, product, or cleanup act during authorship blocks. |
| Exact approval gate | Packet execution requires owner approval of the final frozen packet SHA-256. | No approval by description, branch, PR, filename, or earlier packet is accepted. |
| Fresh authorship | Text derives only from current live sources, ruled citations, and the cleared 80-row ledger. | No prior authored packet bytes or historical command identities occur. |
| Ledger completeness | `STAGE_3_COMMAND_ALIGNMENT.csv` has exactly 80 unique contiguous semantic rows. | Missing, duplicate, noncontiguous, or uncovered semantics reject author return. |
| Diagnostic minimum | Only fifteen justified catalog entries survive; build, overlay, dependency, installation, and replay surfaces are removed. | Convenience is not a necessity justification. |
| Subject readiness | A separately prepared helper executable exists at the frozen path and matches the stated SHA-256 before approval/execution. | Missing or mismatched subject returns to the gate; packet performs no preparation. |
| Two-tier ledger | Every authored command/check form appears in one ledger as `AGENT_PROVEN` or `OWNER_PREFLIGHT`. | Missing coverage, syntax failure, missing binary, or invalid tier rejects authorship. |
| Agent tier | Sandbox-permitted neutral forms run in the exact restricted environment with full chain pins and exits. | Nonzero result outside an explicitly documented command-specific expected exit rejects. |
| Owner tier | Only readable, hash-pinned, trace-necessary binaries denied by sandbox execution qualify. | Missing tool or malformed invocation never qualifies. |
| Owner Step 0 | Each owner-tier entry is re-run before any operative act with exact command, pin, expected exit/output, and recording fields. | Any mismatch stops unexecuted and returns to the approval gate. |
| Restricted environment | Commands use `/usr/bin/env -i`, `PATH=/nonexistent`, frozen `HOME`, `TMPDIR`, `LANG=C`, `LC_ALL=C`, absolute external paths, ninth-packet cwd. | Ambient resolution, rc files, aliases, functions, or unpinned executables are deviations. |
| Transitive closure | `shasum` includes `/usr/bin/perl`; `xcrun` includes the exact Xcode LLDB binary; all remaining survivors are real binaries. | Any unresolved wrapper, symlink, or interpreter rejects. |
| Isolated credential posture | Only a disposable sealed-HOME login keychain is created; no explicit unlock, credential value, owner-keychain write, environment dump, or memory inspection. | Prompt, credential request/value, owner drift, or uncertainty stops and retains evidence. |
| Exact target | Owner shell records its PID and launches one hash-bound helper subject as its direct child; `/bin/ps` verifies PID and PPID immediately before attach and signal. | Stale, absent, replaced, non-child, alternate, or searched PID stops. |
| First signal | Owner uses Activity Monitor Quit exactly once on the displayed numeric helper PID; never Force Quit. | No shell signal, repeat, alternate target, or causal claim after deviation. |
| Debugger fence | Exact pinned LLDB and fresh script; enumerated breakpoints/backtraces only; same PTY interrupt, detach, quit. | Prompt, entitlement request, target mismatch, unresolved required breakpoint, or other debugger input stops. |
| Absolute duration | UTC attach-start and attach-end epochs prove a nonnegative elapsed value no greater than 150 seconds. | At the bound, owner sends only the permitted same-PTY interrupt/detach/quit sequence. |
| Evidence durability | Raw LLDB transcript, exact script/tool/subject hashes, PID relation, timestamps, step outcomes, first-signal attestation, terminal state, cleanup, deviations, and limitations are retained. | Missing raw bytes remain missing and are never reconstructed. |
| Credential safety | No token, API key, keychain value, secret, environment dump, or memory dump enters returned evidence. | Suspected credential-bearing bytes are withheld and routed separately; never silently edited. |
| Fail closed | Every unexpected result records STOP and performs no alternate target, retry, recovery, force signal, or improvisation. | Only explicitly safe evidence retention and cleanup whose preconditions are proven may continue. |
| Cleanup | Delete only the disposable isolated keychain and fixed diagnostic root after child terminality, transcript retention, and owner-state safety are established. | Unknown live state or owner drift retains state and returns a blocker. |
| Claim boundary | Return distinguishes operator attestation, raw evidence, derived checks, unknowns, and deviations. | Execution never implies cause, remedy, acceptance, release, reliance, or closure. |

The packet is intentionally a trace-only execution object. Package preparation
and post-return ingestion, causal-matrix work, and fresh post-execution review
remain separately authorized phases.
