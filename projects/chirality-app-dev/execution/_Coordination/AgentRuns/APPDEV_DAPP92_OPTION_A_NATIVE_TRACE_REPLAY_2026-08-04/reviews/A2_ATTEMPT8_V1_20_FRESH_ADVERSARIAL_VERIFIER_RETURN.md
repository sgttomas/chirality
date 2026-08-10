# A2 Attempt-8 v1.20 fresh adversarial verifier return

Status: `COMPLETE`

Verdict: `BLOCK_PACKET_REPAIR_REQUIRED`

The frozen v1.20 bytes are stable, the numeric command/action range and static
checks pass, and the packet correctly requests C847, C852, C1003, C1007, and
C1010 only as wholly new authority. The packet is nevertheless not safe for
owner presentation. Four material mismatches remain in the exact attach,
terminal-observation, deadline-branch, and stdin-guard contracts. No proposed
operation was executed.

## Frozen-byte evidence

The mandatory first substantive check and final post-review check independently
reproduced the same frozen identities:

| Frozen object | SHA-256 |
|---|---|
| verifier brief | `c5d8b65edbb261d2626800e695d4bf3d9aff758c496e892a0a31acf559d252f4` |
| manager freeze | `e3e4dc3035038ebbc8c980e3a5fe587ae22b8274a8e3e31bd37c008af83da0f6` |
| amendment | `e281e17e13a080cc0e045cf4fb3f435c8f6a0bf47976302cd194ef4ce037c771` |
| approval request | `9a928ea97472ac6cd77b5b89885439d0ef536f629fc6b7157b3a41a3f68eca9d` |
| PACKET-07 return | `90ab9c698e5c8f3fe42939fd0f0692b27eb72920bdb74a381fe6e875266fef28` |
| rejected v1.19 verifier | `2c8f8a1db7e207783a556c4a2e5d5f6f676cb32f63ade9cc4b384f2dc7302e8b` |
| R5 README | `d7a2387e8da45ec671298e89db99020c354dd6f95e9b27c9efb5ee9238e939af` |
| `real-runtime-controller-r5.mjs` | `7ddac5f585e00b12a9806db73351654234776e5324d1d2bdbbaecbe5a82da945` |
| `real-second-session-sentinel-r5.mjs` | `e42616c3a3015e9c25b4b717ab90b669a38ed055f0809207bc61997e7c44868e` |
| `lldb-session-supervisor-r5.mjs` | `49ee82b38e3a29b64c81d24b795c6b5fd462db2de936fa15f82e865705e32b90` |
| `session-terminal-receipt-r5.mjs` | `73ed3a89b6304107462d9e6f04ea8f6252def2b387829dec3ce5d20fa922ca1b` |
| `session-terminal-proof-r5.mjs` | `711c90244444508cfb08db6e05d76371c8ed424fc1f8ed0bc5652722d12e75c9` |
| `transcript-capture-r5.mjs` | `7d36bdf05ef607bf3feca49e3242529dcd7b9d6b0d58a8ac27878619c7c6eaa1` |
| `real-runtime-cleanup-verifier-r5.mjs` | `e42d04822c5c94e220482928d6496e890ea7a91dbc9a7e6217c77b3845b39714` |
| `network-attempt-scan-r5.mjs` | `1c24cfc932a8410ce7938d5274585e26174e265bea0f29650905abaa370571e4` |
| `evidence-manifest-r5.mjs` | `7f9939d4eeaac0796900ac4f6ccd4d234820949c47e7c7c131c39ea795984dae` |
| `rollback-verifier-r5.mjs` | `5938e1afcf12ceddf5bddf73efe1bf4e44abe909d5178635e600f1062c97d53c` |

C787's literal path order independently reproduced, in order, the rejected
v1.19 verifier identity followed by the ten R5 script identities shown above.
No frozen-byte drift was observed.

## Row and static results

- C787-C1057 contains 271 rows. Every ID occurs exactly once; the first is
  C787, the last is C1057, and there is no numeric gap or duplicate.
- The ten R5 scripts pass the only permitted script invocation,
  `node --check`.
- Candidate-whitespace validation passes, reporting one safely skipped
  untracked binary/symlink path. `git diff --check` passes.
- Frontend-scoped Git status is exactly empty.
- The fixed temporary root and durable R5 evidence target are absent.
- The five candidate additions and six build/dependency derivative roots are
  absent.
- The eight current frontend hashes reproduce the C797/C1044 rollback
  constants in exact order:
  `850f7b00bd50af669d2cb6c1963c9b5f9b47f5a30badeda754752f3b896d335b`,
  `16ad6688abaebd0bb1bfe04921a7eb1d20601bf2f2af983153da3c734f44ad1f`,
  `5006bef6922295eb24c54f4a034f2d42929c71b80704b4fe03f8e7e5af36026a`,
  `1f14df17d407b18949d5a7195a786574fa8f03eda731dbe7b77f3e91685fba53`,
  `5c8fce2a3c0e2e7b55730ac673ccb07424dcae1e4bbbb408260b1090040c1a56`,
  `a6759be00c3bf2aaf9bd172657d723cf724bae33aa9a1941724cc173eaee5558`,
  `1918ae7dc10c12608a0d591db565f538a9ed91289e2b78eb728483d9c7cf91e9`,
  and `f8b6d8c2d5c2d8f947e585dd5d99a85a9b207a7277de8ddcb2214cab92136be6`.

These supporting checks do not cure the semantic defects below.

## Material blocking findings

### 1. Critical — C847 has no immediate direct-child target-identity guard

The sentinel proves the helper identity during C845 and only then writes
`attach-intent.json` (`real-second-session-sentinel-r5.mjs` lines 15-34).
The separately launched supervisor reads only `controller.json`, compares the
numeric target PID, and later spawns LLDB with that PID
(`lldb-session-supervisor-r5.mjs` lines 10-12 and 67-68). It neither reads the
attach-intent proof nor re-probes the target's current PID, PPID, start time,
and executable immediately before C847. A helper exit/PID-reuse race between
C845 and C847 can therefore attach LLDB to a process that is not the
controller's direct-child helper. Later C848 rejection cannot undo the attach.

This falsifies the exact-direct-child scope claimed by amendment lines 89-92
and request lines 26-28 and leaves hidden process/attach authority outside the
requested boundary.

### 2. Critical — `error` is treated as drained process terminality

The supervisor's purported stream-`close` promise resolves both on the child
`error` event and on `close` (`lldb-session-supervisor-r5.mjs` lines 69-72).
The fan-in then treats either resolution as `terminalObserved:true`
(lines 127-146). Thus an error callback can select
`LLDB_TERMINAL_BEFORE_ATTACH_OBSERVED` or
`POST_START_ABNORMAL_LLDB_TERMINAL` and obtain cleanup permission through
`session-terminal-proof-r5.mjs` lines 18-24 and 33-38 without an observed,
drained LLDB `close` event. This directly contradicts C991/C996 and the
branch-law stream-`close` requirement at amendment lines 243-249 and 320-325.

The controller repeats the same semantic defect: `owned.exit` resolves on
either child `error` or `exit` (`real-runtime-controller-r5.mjs` lines 67-71),
and `settleOwned` treats any resulting `exitResult` as terminal and cancels the
170-second guard (lines 93-95). The cleanup verifier later accepts only the
stored Boolean (`real-runtime-cleanup-verifier-r5.mjs` lines 5-10). The packet
therefore cannot prove that all controller-owned children are terminal on
every claimed terminal-safe branch.

### 3. Critical — accepted C1010 with delayed `close` has no valid branch

The watchdog may prove identity and accept C1010 at spawn+149,000 ms while the
independent absolute deadline resolves at spawn+149,900 ms
(`lldb-session-supervisor-r5.mjs` lines 73-82). If LLDB stream `close` is not
observed during that 900 ms interval, the supervisor records
`terminalObserved:false` and labels the result
`UNSAFE_TO_SIGNAL_AT_ABSOLUTE_DEADLINE` even though the watchdog record says
`C1010_IDENTITY_GUARDED_SIGKILL` and `signalAccepted:true` (lines 127-143), then
exits 4 (line 160).

The unsafe proof instead requires watchdog mode `UNSAFE_TO_SIGNAL` and
`signalAccepted:false` (`session-terminal-proof-r5.mjs` lines 35-36), while the
forced and concurrent-race branches require observed terminality (lines
29-32). Consequently this executable state satisfies none of the eight
end-to-end proof paths. It also may terminate the non-detached supervisor
before LLDB `close` is observed. The seven-safe/one-unsafe exhaustiveness claim
in amendment lines 311-355 and request lines 43-75 is false.

### 4. High — C1007 is not guarded by an accepted C1003 event, and stdin errors are untrapped

The SIGINT callback increments `interruptCount` before the current identity
proof and C1003 signal attempt (`lldb-session-supervisor-r5.mjs` lines 90-96).
The EOF callback checks only `interruptCount === 1` and byte equality, sets
`inputForwarded = true`, and invokes `child.stdin.end` (lines 107-112). It does
not require a successful C1003 return or the C1004 receipt. A failed C1001-
C1003 path can therefore reach the C1007 call site under a counter that means
"attempted", not "accepted".

In addition, the script installs handlers for child process error/close and
LLDB stdout/stderr data, but no `child.stdin` error handler (lines 69-72 and
87-116). An asynchronous writable-stream error from C1007 is therefore outside
the callback-error state and can terminate the supervisor without C1051-C1057.
This contradicts C991's every-callback-error claim and C1006/C1007's exact
accepted-interrupt precondition (amendment lines 243 and 252-259).

## Eight-branch disposition

| Branch | Disposition |
|---|---|
| `PRE_CONTROLLER_NO_SESSION_B` | Structurally mapped, but not terminal-safe because controller child `error` is accepted as terminal. |
| `CONTROLLER_NO_LLDB_SPAWN` | Structurally mapped, but has the same false controller-terminal proof. |
| `LLDB_TERMINAL_BEFORE_ATTACH` | Blocked: supervisor `error` can masquerade as drained LLDB `close`. |
| `NORMAL_EXACT_DETACH` | Whole-buffer/no-pre-EOF-forwarding structure is present, but C1007 lacks an accepted-C1003 guard and stdin errors are untrapped. |
| `FORCED_WATCHDOG_TERMINAL` | Valid only when `close` arrives before +149.9 s; it omits accepted-SIGKILL/no-close-at-deadline. |
| `WATCHDOG_SIGNAL_ACCEPTED_RACE_TERMINAL` | Structurally present for an observed non-SIGKILL concurrent terminal, but it does not cover accepted C1010 with no timely `close`. |
| `POST_START_ABNORMAL_LLDB_TERMINAL` | Blocked: child `error` can produce a false terminal-safe classification. |
| `UNSAFE_TO_SIGNAL_AT_ABSOLUTE_DEADLINE` | Its intended failed-identity proof is coherent, but the supervisor also routes accepted-C1010/no-close into the same label and that state fails the proof. |

The claimed result is therefore not exactly seven terminal-safe branches plus
one identity-unsafe diagnostic failure.

## Other acceptance dispositions

- C847, C852, C1003, C1007, and C1010 are described only as new authority;
  no C196/C197 inheritance claim remains. This part passes.
- The normal-path buffer logic stores bytes without forwarding before EOF and
  requires whole-buffer equality. Its accepted-interrupt guard fails as noted
  above, so acceptance item 7 does not pass overall.
- Credential minimization, the mechanical package-output network scan,
  deterministic evidence-manifest ordering, the eight-hash rollback table,
  frontend cleanliness, derivative absence, and deletion marker are present
  in the static bytes. They do not become executable evidence because the
  terminal/branch gates fail first.
- The request retains the correct no-approval/no-execution/no-product/no-
  release/no-reliance/no-Git/no-Task-Management/no-foreign-loop boundary, but
  its direct-child and seven-terminal-safe claims are broader than the scripts
  can prove.

No owner token may be presented from this return. No R5 command or script was
executed except static `node --check`; no runtime, package, cache, network,
helper, GUI, LLDB, attach, signal, replay, credential, cleanup, rollback,
deletion, release, Git mutation, Task Management, or foreign-loop effect
occurred.
