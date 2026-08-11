STUB — UNFILLED
Required content: owner fill-in form for Step 0, exact PID/direct-child proof,
timestamps, literal commands, exit codes, raw LLDB transcript, first-signal and
bounded observation, detach/quit, deviations, output hashes, cleanup state,
credential exclusion/redaction, and limitations.
# D-APP-93 Owner Evidence Capture Form

Status: BLANK OWNER FORM — PREPARATION ONLY

Complete every field. Use `NOT PERFORMED`, `NOT OBSERVED`, or `NOT APPLICABLE` rather than leaving blanks. Preserve raw evidence; absence is not a pass.

## A. Packet and approval binding

- Exact run root:
- Base `912e3a8c9c07e9b8359093f63feace1c7c9f4776`; Receipt `158`:
- Manager-presented adjacent manifest SHA-256:
- Owner-approved manifest SHA-256:
- Exact approval token, actor, and timestamp:
- Expected preflight script SHA-256:
- Expected LLDB script SHA-256:
- Confirmation packet bytes remained unchanged after Step 0:

## B. Target and direct-child proof

- Exact numeric `TARGET_PID` personally selected by owner:
- Selection actor and timestamp:
- Intended sealed helper identity:
- Exact parent PID and identity:
- Direct-child proof source/location/SHA-256:
- Owner conclusion:
- Confirmation no PID search, substitution, fallback, or relaunch:

## C. Step 0 neutral preflight

- Exact entered form, verbatim:
- Exact RUN_ROOT and TARGET_PID arguments:
- Both expected packet-script hashes:
- Start/end timestamps with timezone:
- Exit status:
- Stdout location and SHA-256:
- Stderr location and SHA-256:
- Combined transcript location and SHA-256:
- `PREFLIGHT_BEGIN` record:
- Final `PREFLIGHT_STATUS` record:

| Item | Expected | Actual | Match? | Evidence |
|---|---|---|---|---|
| preflight script SHA-256 | manager-presented | | | |
| LLDB script SHA-256 | manager-presented | | | |
| `/bin/zsh` SHA-256 | `528da649cc69510bd3c0bc565298cb602076b74a8ac3f18e793211b2a3c725e8` | | | |
| `/usr/bin/xcrun` SHA-256 | `4bc0cc7099775fbe35c653ceb09e0e393d2e5ada024db872e0eb8c43500b4dc6` | | | |
| LLDB binary SHA-256 | `0035650adb4c8278122f70771e2e052a2b6e6d644a76745ffecf8c3a0bd686ca` | | | |
| `/bin/ps` SHA-256 | `a1d8c4a0a96fb6159f09d8f520f54df829db5f2eae9b9f3448e18f0bee61115c` | | | |
| `/usr/bin/shasum` SHA-256 | `0812595f981a26f813d98dc380af14d4af427626c9339eda29eb849ae13de1e3` | | | |
| `/usr/bin/perl` SHA-256 | `626702a74f85d2664872f6a7aa9b639306a2035211d442a24ea32ef0d48c8afd` | | | |
| xcrun LLDB path | `/Applications/Xcode.app/Contents/Developer/usr/bin/lldb` | | | |
| LLDB versions | `lldb-2100.0.17.203`; `Swift version 6.3.3` | | | |
| zsh syntax | exit 0; empty output | | | |
| exact-PID ps | one exact-target record | | | |

- Every actual printed by Step 0:
- Any mismatch/deviation and stop disposition:
- Confirmation Step 0 performed no attach, signal, launch, build, keychain/credential access, memory/environment inspection, cleanup, or mutation:

## D. LLDB attach and raw trace

- Gate confirmation before attach:
- Exact attach form and exact numeric PID:
- Confirmation PID equals approval and Step 0 PID:
- Actor and attach-start timestamp:
- Attach result:
- Raw unedited PTY transcript location/bytes/SHA-256:
- Script-begin timestamp, SIGTERM policy output, and breakpoint-list output:

| Breakpoint | First-hit timestamp | Hit count | Backtraces ≤16? | Transcript locator |
|---|---|---:|---|---|
| `__sigtramp` | | | | |
| `uv__signal_handler` | | | | |
| `SignalWrap.*OnSignal` | | | | |
| `electron::Browser::Quit\|Browser::Quit` | | | | |
| `-[NSApplication terminate:]` | | | | |

## E. Separately approved first-signal act

- Separate frozen authority citation:
- Exact approved act, actor, target, and timestamp:
- Observed result and first breakpoint/timestamp:
- Confirmation no alternative or repetition was improvised:

## F. 150-second timing and same-PTY cleanup

- Attach start:
- `0x03` send timestamp and response:
- `process detach` + `0x0a` send and confirmation timestamps/response:
- `quit` + `0x0a` send and completion timestamps/response:
- Same-PTY evidence locator:
- Attach-to-confirmed-detach elapsed seconds and ≤150 result:
- Confirmation exact sequence was used; cleanup impediment if any:

## G. Deviations, retained evidence, redaction, limits

- Deviations/unexpected effects and stop disposition:
- Retained evidence inventory, locations, byte counts, and SHA-256 values:
- Original custody/location and unchanged confirmation:
- Derivative redacted-copy location/SHA-256:
- Exact redactions and reasons:
- Evidence limits, unobserved paths, ambiguities, and unsupported claims:

## H. Credential and effect exclusions

- Keychain accessed?:
- Credentials requested/read/printed/copied/used/changed?:
- Process memory or environment read?:
- Build, launch, cleanup, overlay, ingestion, or other mutation performed?:
- Effects beyond the separately approved signal/debugger sequence?:
- Supporting transcript locators:

## I. Owner assessment

- Owner assessment:
- Further approval/rerun required:

Completion is not acceptance, closure, runtime authority, credential authority, or a PASS verdict.
