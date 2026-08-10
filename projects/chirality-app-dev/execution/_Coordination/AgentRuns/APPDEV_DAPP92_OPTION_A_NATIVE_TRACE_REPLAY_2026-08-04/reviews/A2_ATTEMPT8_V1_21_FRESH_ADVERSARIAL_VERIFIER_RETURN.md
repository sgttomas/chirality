# A2 Attempt-8 v1.21 fresh adversarial verifier return

Status: `COMPLETE`

Verdict: `BLOCK_PACKET_REPAIR_REQUIRED`

The frozen v1.21/R6 packet is byte-stable, the immutable v1.20/R5 identities
do not drift, and the permitted static checks pass. The packet is nevertheless
unsafe for owner presentation. Four material authorization/safety defects
remain in the exact C847 byte-binding, deadline/callback, C1015 stdin-completion,
and C1066 action-enumeration contracts. No token may issue and no repair follows
from this return. No proposed operation was executed.

## Mandatory first stability pass

| Frozen object | SHA-256 |
|---|---|
| verifier brief | `ba31666c2a022e16fe8578bf990620370540aed3bb6026739fc0fe8654ac0cd9` |
| manager freeze | `2040199d4d8a3431c021086d9689da018fef45a47943716c5163667badd23789` |
| packet-author brief | `207ae6da7693b323f2fbc6e3eafb198caf435ae3493ade9d4a5be15f2afd4571` |
| amendment | `d1141dbfbe5469870f4114f42da2e39a9235f5a5e22eda6dd5d548b0e3872a63` |
| approval request | `2ebf1a98b699a11e00dd0318f26a8993938c79bc50d448a96daefa3741c7ec5f` |
| PACKET-08 return | `409fae3fb849b0efd18f6fc053576f938b5addea77275a4aa9217f04d3f9db4b` |
| accepted v1.20 verifier | `47b57dae327e247c97a8957ad2cdf602b10ff64b94546babc3c5c1b8f5dbe655` |
| R6 README | `fcd0fa4e6ab8f4d79b9fcca5db369e49017078593b8b88c76f332ad1ecddfd3b` |
| `real-runtime-controller-r6.mjs` | `49cdc334388896fefd066e7e3d0405b870923a1e3ad81e3f41e8d2542c225722` |
| `real-second-session-sentinel-r6.mjs` | `bb6be369be35d8d73ac20fb244c0df844c0041ac87bfd33158ec8d19099fbce8` |
| `lldb-session-supervisor-r6.mjs` | `2137a72e0c53639319b3120cc65a27e58a66e900a5577b7747ff9bb4c55495a4` |
| `session-terminal-receipt-r6.mjs` | `d6292506552630b3d8db0f21de7f93e6e37102663632db59a6e36d6d5b3a51ce` |
| `session-terminal-proof-r6.mjs` | `20c0e9477489e9b00b5cc4ccf3db85f79b59c1cb2d0807ceeafb66a253a5178d` |
| `transcript-capture-r6.mjs` | `8c3a4edcb32224091c9490034ef46f2e48c7dc0c291cdb486cb82aa4232d5edc` |
| `real-runtime-cleanup-verifier-r6.mjs` | `17d068b207dd277e257e1cc55f486b9a0ae29e06bd5a24e4e7a31fef15f5eacb` |
| `network-attempt-scan-r6.mjs` | `f03479d834868f7befd264eba03dbefdb61fdbe93fd942b1c34d69bda87e5453` |
| `evidence-manifest-r6.mjs` | `c752f0b1bd33073e7aafa951e1fd51fb374ee18b393d1c025ef30416a6db0be5` |
| `rollback-verifier-r6.mjs` | `c06f58cabf2130518be19cc58d3a21901b674a0ca63ceeb1289b3a9a0621f4a3` |

C787's literal path order independently reproduced the accepted v1.20
verifier identity followed by the ten R6 script identities in exactly the
order shown above.

## Immutable v1.20/R5 identities

These identities reproduced in both the first and final stability passes.

| Immutable object | SHA-256 |
|---|---|
| manager freeze v1.20 | `e3e4dc3035038ebbc8c980e3a5fe587ae22b8274a8e3e31bd37c008af83da0f6` |
| amendment v1.20 | `e281e17e13a080cc0e045cf4fb3f435c8f6a0bf47976302cd194ef4ce037c771` |
| approval request R5 | `9a928ea97472ac6cd77b5b89885439d0ef536f629fc6b7157b3a41a3f68eca9d` |
| PACKET-07 return | `90ab9c698e5c8f3fe42939fd0f0692b27eb72920bdb74a381fe6e875266fef28` |
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

No R5 drift was observed.

## Static and boundary results

- C787-C1066 contains exactly 280 rows. Every integer occurs once, in
  contiguous order; external C787-C902 and internal C903-C1066 are correctly
  partitioned numerically.
- All ten R6 scripts pass the sole permitted script invocation, static
  `node --check`.
- No manager-hash placeholder or trailing whitespace was found in the frozen
  candidate; `git diff --check` passes.
- Frontend-scoped Git status is exactly empty.
- The fixed temporary root and R6 durable evidence target are absent.
- The five candidate additions and all six named build/dependency derivative
  roots are absent.
- The eight current frontend hashes exactly reproduce C797/C1053, in order:
  `850f7b00bd50af669d2cb6c1963c9b5f9b47f5a30badeda754752f3b896d335b`,
  `16ad6688abaebd0bb1bfe04921a7eb1d20601bf2f2af983153da3c734f44ad1f`,
  `5006bef6922295eb24c54f4a034f2d42929c71b80704b4fe03f8e7e5af36026a`,
  `1f14df17d407b18949d5a7195a786574fa8f03eda731dbe7b77f3e91685fba53`,
  `5c8fce2a3c0e2e7b55730ac673ccb07424dcae1e4bbbb408260b1090040c1a56`,
  `a6759be00c3bf2aaf9bd172657d723cf724bae33aa9a1941724cc173eaee5558`,
  `1918ae7dc10c12608a0d591db565f538a9ed91289e2b78eb728483d9c7cf91e9`,
  and `f8b6d8c2d5c2d8f947e585dd5d99a85a9b207a7277de8ddcb2214cab92136be6`.
- Candidate write paths are App-only. Pre-existing manager/control-plane state
  outside this verifier return was inspected read-only and left untouched.

These mechanical passes do not cure the semantic defects below.

## Material blocking findings

### 1. Critical — C1015 does not inspect the stdin completion error

The C1014 call supplies a zero-argument completion callback and
unconditionally sets `inputWriteCompleted = true`
(`proposed/attempt8-r6/lldb-session-supervisor-r6.mjs`, line 137). A Node
`Writable.end` completion callback can receive an error argument; this callback
does not bind or test it. Its `try/catch` can catch only an exception thrown by
the assignment, not the delivered completion error. The normal classifier then
trusts `inputWriteCompleted` (line 177), and the proof trusts it again
(`session-terminal-proof-r6.mjs`, line 30).

Thus C1015 does not trap its specified completion-callback error and can mark a
failed completion successful. The separate stream `error` listener at line 145
does not make the completion callback itself exact or guarantee that its error
argument was observed. This directly falsifies the fourth required v1.20 repair.

### 2. Critical — C847 does not byte-bind the accepted controller and attach-intent objects

The amendment claims a “byte-bound attach-intent/controller” guard at C847
(`COMMAND_REGISTER_AMENDMENT_V1_21_PROPOSED.md`, line 91). The supervisor reads
and immediately parses both files (lines 12-13), compares selected semantic
fields (lines 49-56), and writes a guard receipt containing only selected state
and the live process proof (lines 81-85). It records neither source-object hash
nor exact source bytes. C844 merely prints a controller hash; no accepted value
is asserted or passed into C847, and attach-intent bytes are never hashed.

Additionally, both reads/parses occur before the C847 `try` at line 82. An
unreadable or malformed source object therefore exits before the required typed
`FAILED_CLOSED_NO_LLDB_SPAWN` receipt can be written. LLDB is not spawned on
that path, but the mandatory truthful typed fail-closed proof and exact branch
disposition are absent. The immediate live PID/PPID/start/executable probes are
present; the exact accepted-byte binding and complete guard-failure proof are not.

### 3. Critical — LLDB output callbacks are unbounded against the hard deadline

The supervisor arms +149,000 ms and +149,900 ms timers (lines 97-106), but both
LLDB data callbacks synchronously append every chunk to a file and retain every
chunk again in unbounded in-memory arrays (lines 111-112). There is no byte,
chunk, duration, or backpressure cap. These callbacks run on the same event loop
as both timers and can delay the watchdog and absolute-deadline callbacks.

The sealed brief specifically requires proof that no unbounded callback can
contradict the requested cap. The fixed trace script does not establish a
program-enforced output bound. Consequently the packet cannot prove that C1018
runs at its intended watchdog point or that the supervisor selects its deadline
branch by +149,900 ms under every reachable output state.

### 4. High — C1066 does not enumerate the accepted-watchdog/no-close exit

C1066 authorizes exit 0 for exact detach, exit 4 for the identity-unsafe
diagnostic, and exit 1 for every other observed-terminal branch
(`COMMAND_REGISTER_AMENDMENT_V1_21_PROPOSED.md`, line 318). The script instead
executes `process.exit(4)` for *every* no-close state (line 192), including
`WATCHDOG_SIGNAL_ACCEPTED_NO_CLOSE_AT_DEADLINE`; the proof explicitly requires
tool exit 4 for that branch (`session-terminal-proof-r6.mjs`, lines 35-36).

The new branch is semantically distinct from identity-unsafe and is not an
observed-terminal branch. Its actual exit action is therefore outside C1066's
literal condition. This violates individual operation enumeration and makes
the action graph narrower than the executable graph.

## Required review dispositions

1. **Enumeration and authority — BLOCK.** Numeric uniqueness/contiguity and
   wholly-new C787-C1066 language pass; historical C196/C197 supply no
   authority. C1066 nevertheless fails to enumerate one actual exit condition.
2. **Immediate target identity — BLOCK.** Immediate PID/PPID/start/executable
   probes precede spawn, but accepted controller/attach-intent bytes are not
   exactly bound and pre-guard read/parse failures lack the required typed proof.
3. **Deadline and timing — BLOCK.** The 28.0 s, 102.0 s, +149,000 ms, and
   +149,900 ms constants are preserved, with no explicit timer reset. Unbounded
   LLDB data callbacks prevent the required cap proof.
4. **Terminal/error semantics — PASS for the v1.20 child-error defect.** LLDB
   and controller-owned-child `error` events are recorded separately and do
   not resolve terminal promises; drained `close` is required for terminal-safe
   proofs and controller cleanup. This does not cure the C1015 callback defect.
5. **Accepted-watchdog/no-close branch — BLOCK on exact enumeration.** The
   branch is otherwise unique, retains the root, withholds cleanup/durable
   copy/rollback/deletion, and claims no LLDB terminality, orphan absence, or
   150-second maximum. Its actual exit-4 operation is not described by C1066.
6. **C1009/C1014 stdin chain — BLOCK.** Accepted C1009, its successful receipt
   write, whole-buffer equality, EOF, and one-time forwarding gates are present;
   stream errors are recorded. C1015 ignores the completion error argument and
   can falsely mark completion.
7. **Branch exhaustiveness and settlement — BLOCK.** Controller-owned-child
   error/close/deadline settlement is independently represented, but the C847
   pre-read failure path lacks its typed branch proof and the new no-close exit
   is not truthfully enumerated.
8. **Evidence and rollback — PASS statically, not reachable as accepted
   execution authority.** Terminal-safe branches place durable evidence and a
   deterministic manifest before rollback; both diagnostic branches withhold
   those actions. Eight hashes, empty frontend status, derivative absence,
   deletion permission, and durable-manifest postcondition are present.
9. **Static and boundary checks — PASS** as recorded above.

## Branch-by-branch disposition

| Branch | Disposition |
|---|---|
| `PRE_CONTROLLER_NO_SESSION_B` | Structurally mapped; controller child settlement remains close-gated. |
| `CONTROLLER_NO_LLDB_SPAWN` | BLOCK: ordinary in-guard mismatch is fail-closed, but source bytes are not bound and pre-try read/parse failure cannot produce the required typed proof. |
| `LLDB_TERMINAL_BEFORE_ATTACH` | Drained-close gated; no child `error` can fabricate terminality. |
| `NORMAL_EXACT_DETACH` | BLOCK: C1015 can falsely mark a failed stdin completion successful. |
| `FORCED_WATCHDOG_TERMINAL` | Drained-close and accepted-C1018 gated; hard timing remains unproved because output callbacks are unbounded. |
| `WATCHDOG_SIGNAL_ACCEPTED_RACE_TERMINAL` | Drained-close gated; same deadline/callback defect remains. |
| `WATCHDOG_SIGNAL_ACCEPTED_NO_CLOSE_AT_DEADLINE` | Retained-root/no-claim proof is structurally distinct and cleanup-safe, but its actual exit 4 is omitted from C1066's literal condition. |
| `POST_START_ABNORMAL_LLDB_TERMINAL` | Drained-close gated and callback failures are evidenced; no false cleanup from child `error` alone. |
| `UNSAFE_TO_SIGNAL_AT_ABSOLUTE_DEADLINE` | Identity-unsafe/no-signal retained-root proof is structurally coherent. |

## Mandatory final stability pass

| Frozen object | SHA-256 |
|---|---|
| verifier brief | `ba31666c2a022e16fe8578bf990620370540aed3bb6026739fc0fe8654ac0cd9` |
| manager freeze | `2040199d4d8a3431c021086d9689da018fef45a47943716c5163667badd23789` |
| packet-author brief | `207ae6da7693b323f2fbc6e3eafb198caf435ae3493ade9d4a5be15f2afd4571` |
| amendment | `d1141dbfbe5469870f4114f42da2e39a9235f5a5e22eda6dd5d548b0e3872a63` |
| approval request | `2ebf1a98b699a11e00dd0318f26a8993938c79bc50d448a96daefa3741c7ec5f` |
| PACKET-08 return | `409fae3fb849b0efd18f6fc053576f938b5addea77275a4aa9217f04d3f9db4b` |
| accepted v1.20 verifier | `47b57dae327e247c97a8957ad2cdf602b10ff64b94546babc3c5c1b8f5dbe655` |
| R6 README | `fcd0fa4e6ab8f4d79b9fcca5db369e49017078593b8b88c76f332ad1ecddfd3b` |
| `real-runtime-controller-r6.mjs` | `49cdc334388896fefd066e7e3d0405b870923a1e3ad81e3f41e8d2542c225722` |
| `real-second-session-sentinel-r6.mjs` | `bb6be369be35d8d73ac20fb244c0df844c0041ac87bfd33158ec8d19099fbce8` |
| `lldb-session-supervisor-r6.mjs` | `2137a72e0c53639319b3120cc65a27e58a66e900a5577b7747ff9bb4c55495a4` |
| `session-terminal-receipt-r6.mjs` | `d6292506552630b3d8db0f21de7f93e6e37102663632db59a6e36d6d5b3a51ce` |
| `session-terminal-proof-r6.mjs` | `20c0e9477489e9b00b5cc4ccf3db85f79b59c1cb2d0807ceeafb66a253a5178d` |
| `transcript-capture-r6.mjs` | `8c3a4edcb32224091c9490034ef46f2e48c7dc0c291cdb486cb82aa4232d5edc` |
| `real-runtime-cleanup-verifier-r6.mjs` | `17d068b207dd277e257e1cc55f486b9a0ae29e06bd5a24e4e7a31fef15f5eacb` |
| `network-attempt-scan-r6.mjs` | `f03479d834868f7befd264eba03dbefdb61fdbe93fd942b1c34d69bda87e5453` |
| `evidence-manifest-r6.mjs` | `c752f0b1bd33073e7aafa951e1fd51fb374ee18b393d1c025ef30416a6db0be5` |
| `rollback-verifier-r6.mjs` | `c06f58cabf2130518be19cc58d3a21901b674a0ca63ceeb1289b3a9a0621f4a3` |

The first and final complete tables are identical. C787's ordered list and all
immutable v1.20/R5 identities also reproduced on the final pass.

## Non-execution and authority statement

No R6 command or generated script was executed except static `node --check` on
the ten R6 scripts. No package, runtime, cache, network, helper, GUI, LLDB,
attach, signal, replay, credential, cleanup, rollback, deletion, product,
release, Git mutation, Task Management, or foreign-loop operation occurred.

The prospective owner token remains unpresented, unadopted, and
non-authorizing. The packet requires repair and a new freeze/fresh-verifier
cycle before any owner presentation.
