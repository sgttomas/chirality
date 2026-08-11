# D-APP-93 sixth-lineage evidence return

Status: `BLANK OWNER TEMPLATE — NO EXECUTION OR INGESTION EFFECT`

Complete only during a separately approved execution of the exact frozen
packet. The full 80-row worksheet is the byte-pinned
`authoring/STAGE_5_EVIDENCE_RETURN_PACKET.md` attachment inventoried by
`PACKET_INDEX.md`; that worksheet and this return are both mandatory freeze
members.

Do not return tokens, secrets, keychain values, API keys, memory dumps, or
environment dumps. Withhold suspected credential-bearing material and route it
to a separately governed credential-safe process. Do not silently redact,
reconstruct, or normalize missing or unsafe bytes.

## 1. Packet and authority identity

| Field | Owner return |
|---|---|
| Complete freeze hash | `<fill>` |
| Packet-index SHA-256 | `<fill>` |
| Execution-packet SHA-256 | `<fill>` |
| LLDB-script SHA-256 | `<fill>` |
| Evidence-template SHA-256 | `<fill>` |
| Alignment attachment SHA-256 | `<fill>` |
| Literal-runbook attachment SHA-256 | `<fill>` |
| Full worksheet attachment SHA-256 | `<fill>` |
| Exact owner approval citation | `<fill>` |
| Execution start/end UTC | `<fill>` |
| Host OS and architecture capture hashes | `<fill>` |

## 2. Complete command outcomes

The full worksheet must contain exactly one disposition for every step
`P93-001` through `P93-080`, in order and without alias or duplicate. For each
step return: actor, start/end UTC, exact command/action performed, exit/state,
raw stdout and stderr path/hash, observed output, success-gate result,
deviation, and skipped reason. A skipped step is not a PASS.

Full worksheet path/hash: `<fill>`.

Rows present and unique: `<PASS / FAIL / UNKNOWN>`.

First failed or deviated step: `<fill or NONE>`.

Universal stop record path/hash: `<fill or NOT RUN>`.

## 3. Reconstruction, dependency, package, and identity

| Evidence | Exact path | SHA-256 | Result/limitation |
|---|---|---|---|
| Governed baseline manifest |  |  |  |
| Candidate manifest |  |  |  |
| Offline install capture |  |  |  |
| Unchanged lockfile proof |  |  |  |
| Dependency projection |  |  |  |
| Local archive identity |  |  |  |
| Overlay identity |  |  |  |
| Tests |  |  |  |
| Typecheck |  |  |  |
| Build |  |  |  |
| Package |  |  |  |
| Five package-object identities |  |  |  |
| Helper public plist |  |  |  |
| Helper symlink topology |  |  |  |

Network observation and limitation: `<fill>`.

## 4. Isolated HOME, keychain, and owner state

| Field | Owner return |
|---|---|
| Isolated HOME/user-data paths | `<fill>` |
| Disposable login-keychain path | `<fill>` |
| Explicit unlock performed | `NO` or `<DEVIATION — STOP>` |
| Create stdout/stderr hashes and status | `<fill>` |
| Isolated default readback/hash | `<fill>` |
| Isolated search-list readback/hash | `<fill>` |
| Prompt state | `<NONE / exact prompt and stop>` |
| Credential request/exposure | `<NONE / WITHHELD AND ESCALATED>` |
| Pre-owner default/search hashes | `<fill>` |
| Post-owner default/search hashes | `<fill>` |
| Default/search comparisons | `<MATCH / MISMATCH / UNKNOWN>` |
| Owner-keychain write performed | `NO` or `<DEVIATION — STOP>` |

## 5. Target, first signal, and LLDB trace

| Field | Owner return |
|---|---|
| Persistent owner-shell PID | `<fill>` |
| Traced-helper PID/PPID | `<fill>` |
| Direct-child equality and immediate recheck | `<fill>` |
| GUI PID | `<fill>` |
| Script-hash match | `<fill>` |
| LLDB exact attach target | `<fill>` |
| Raw LLDB transcript path/hash | `<fill>` |
| Breakpoint resolution list | `<fill>` |
| Unresolved breakpoints classified UNKNOWN | `<fill>` |
| Trace events and bounded backtraces | `<fill>` |
| LLDB errors/prompts | `<fill>` |
| Activity Monitor Quit exact PID/time | `<fill>` |
| Force Quit or repeated signal | `<NO / exact deviation and stop>` |
| Same-PTY interrupt evidence | `<fill>` |
| Same-PID detach evidence | `<fill>` |
| LLDB quit/terminal evidence | `<fill>` |
| Attach start/end epochs and hashes | `<fill>` |
| Elapsed seconds and 150-second result | `<fill>` |

Owner attestation: `I targeted only the recorded traced-helper numeric PID,
selected Activity Monitor Quit exactly once, confirmed Quit, never selected
Force Quit, never targeted a replacement PID, and recorded the action
contemporaneously.`

Owner signature/date: `<fill>`.

## 6. Process and socket terminality

| Field | Owner return |
|---|---|
| Traced-helper exit status / terminal state | `<fill>` |
| Traced socket absence | `<fill>` |
| Replay PID/PPID and direct-child proof | `<fill>` |
| Replay readiness within 15 seconds | `<fill>` |
| Exact replay TERM count/target | `<fill>` |
| Replay exit status / terminal state | `<fill>` |
| Replay socket absence | `<fill>` |
| Exact GUI TERM count/target | `<fill>` |
| GUI exit status / terminal state | `<fill>` |
| Remaining diagnostic process/socket | `<NONE / exact retained state>` |

## 7. Evidence manifests and credential exclusions

| Field | Owner return |
|---|---|
| Source evidence manifest path/hash | `<fill>` |
| Returned evidence manifest path/hash | `<fill>` |
| Digest/path equality | `<fill>` |
| Returned file count | `<fill>` |
| Withheld unsafe objects | `<none / opaque identifiers only>` |
| Separate redaction-process citation | `<none / fill>` |
| Missing raw bytes | `<none / exact limitation>` |
| Immutable external return root | `<fill>` |

## 8. Cleanup and rollback proof

| Gate | Evidence/status | Result |
|---|---|---|
| Disposable keychain deletion and absence | `<fill>` | `<PASS / FAIL / SKIPPED>` |
| Three Electron files restored | `<fill>` | `<PASS / FAIL / SKIPPED>` |
| Package manifests restored | `<fill>` | `<PASS / FAIL / SKIPPED>` |
| Build script restored | `<fill>` | `<PASS / FAIL / SKIPPED>` |
| Two tests restored | `<fill>` | `<PASS / FAIL / SKIPPED>` |
| Five candidate additions absent | `<fill>` | `<PASS / FAIL / UNKNOWN>` |
| Six derivative roots absent | `<fill>` | `<PASS / FAIL / UNKNOWN>` |
| Eight baseline hashes restored | `<fill>` | `<PASS / FAIL / UNKNOWN>` |
| Frontend Git-status capture zero bytes | `<fill>` | `<PASS / FAIL / UNKNOWN>` |
| Fixed diagnostic root absent | `<fill>` | `<PASS / FAIL / UNKNOWN>` |
| Return root retained | `<fill>` | `<PASS / FAIL / UNKNOWN>` |

When process, socket, owner-state, evidence-return, or rollback safety is
unknown, destructive cleanup must be `SKIPPED`; retain state and seek a new
ruling.

## 9. Deviations, limitations, and calibrated disposition

Exact deviations/skips: `<fill>`.

Unexpected prompt, privilege, entitlement, PID, target, debugger, signal,
socket, owner-state, cleanup, package, network, or credential condition:
`<fill or NONE>`.

Known limitations, unresolved symbols, timing uncertainty, missing output,
operator transcription uncertainty, and credential omissions: `<fill>`.

Choose exactly one terminal disposition:

- `EXECUTION_COMPLETE — EVIDENCE RETURNED — CLEANUP COMPLETE — NO CAUSAL OR ACCEPTANCE CLAIM`
- `STOPPED — EVIDENCE RETAINED — CLEANUP PARTIAL OR WITHHELD — NO CAUSAL OR ACCEPTANCE CLAIM`
- `STOPPED — LIVE OR OWNER STATE UNKNOWN — DESTRUCTIVE CLEANUP WITHHELD — NO CAUSAL OR ACCEPTANCE CLAIM`
- `STOPPED — CREDENTIAL-SAFE INGESTION REQUIRED — NO CAUSAL OR ACCEPTANCE CLAIM`

Selected disposition: `<fill>`.

This return does not establish cause, remedy, product acceptance, release,
reliance, lifecycle closure, receipt, or next-step authority. Ingestion,
validation, supported-versus-unknown causal matrix authorship, and fresh
post-execution adversarial verification remain separate governed acts.
