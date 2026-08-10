# A2 Attempt-8 v1.18 fresh adversarial verifier return

Status: `COMPLETE`

Verdict: `BLOCK_PACKET_REPAIR_REQUIRED`

V1.18 is not decision-ready. Its amendment, request, and packet-author return
reproduce, but the supposedly frozen proposal scripts did not remain immutable
during this verification and do not match the hashes asserted by those three
artifacts. The currently observed bytes also retain blocking early-stop,
watchdog, terminal-proof, enumeration, evidence-freeze, and rollback defects.
No proposed operation was executed.

## Frozen-byte and static checks

- Verifier brief: `482b2d8a309ba9e93c02554ae02d2c322a9d56e5573c48fc99d0d09b1a7f1801`.
- Attempt-7 verifier: `1546dc33b24bbbd86d43d6b547b404113267e594b4eb6f0247c59455ad13ce6f`.
- V1.17 blocker: `93d5e64db0017f14b61c327cae86a009a103a10be593514ea39314bedb312b4e`.
- V1.18 amendment: `f2aa50cb4dfc55a8f4d5c3c58e2d7a679081d66fd3978de696cee8ca5ff5fb39`.
- V1.18 request: `49630578673d138e0cb08ac27ec8e9ec7dab227f632dedb24d599088202ed49c`.
- Packet-author return: `a19de2274632c1ec4c1d563ffd6094ba6a4ebd51cc215070fc2c9478b9ef49dc`.
- D-APP-92 packet/ruling: respectively
  `644c80ecff11577c9ab0f4f4fae4fa9b1f609cdaa2d801f118ffe052bfad77c6`
  and `391b96507bfc877050ca4d1e4cb0ce421c60171becfabd13a13ab65d98fe1c78`.
- LLDB command file:
  `720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8`.
- Current post-drift scripts: controller
  `55b6b5f8cd1f3deb276a5decc35ae683a674c380360b813ea60e2b0a5a8141b8`;
  sentinel `bcf96adaf8c251a21b7786d1912059dfe26232ab69d3f8603717c5999626ebc1`;
  supervisor `cd653f898f5c6436186cfb123159eaf493eede93421f1eb2cf71ca0da671f6fa`;
  observer `9221e9cdcd94b9d5ca7340c32bec8d7bc2d655634f88b3bad4d774417b094744`;
  cleanup verifier `b9c6c53e166df3270d2f9c22ceab1ac5013bf97d9dea2be0a579fd18b42905d3`;
  network scan `4456f35254a34e3c1e8e0680f0d9f4321f2a578d9cc6b13b3e3f768cd34d1285`.

All six current scripts pass `node --check`; no script was invoked. C375-C530
are contiguous, with 156 rows and 156 unique IDs, each occurring once. C196
and C197 each occur once and preserve the v1.9 executable/input semantics.
Candidate trailing-whitespace and `git diff --check` checks returned clean.
The frontend is Git-clean; the fixed temporary root, durable R3 target, and
listed derivative paths are absent.

## Blocking findings

### 1. Critical — the verified object was not frozen and its asserted hashes are false

The first hash pass observed controller `112845500d6be97549bb4c23c0f7454ef1d93e8045281792e1cd43c20f7d2550`,
sentinel `36e7a99697d69d039c76893522e3a1e1ab8fb170ad42a843729f42d45678c43e`,
supervisor `da7034e4bc079c4e0c581f785bdb94fc2b27da0137350c69024166ef934062be`,
observer `91421c0ce439eaffaa3b3c2973f70eacf747d13403e61269deb077426035b241`,
cleanup verifier `68e29a77a68e818d37ddb344416ef1770ae46d7b25d0b77e410bc1ce97f09d06`,
and network scan `4456f352...`. A later pass observed the current hashes listed
above; five files had changed, all at filesystem mtime
`2026-08-05T08:06:48-0600`. One-second repeated hashes after the author was
interrupted were stable. Amendment lines 11-18, request lines 11-19, and the
packet return lines 12-22 still assert the obsolete controller/sentinel/
supervisor/observer/cleanup hashes. C375 would therefore stop immediately.

### 2. Critical — early-stop branch law is contradictory and can orphan children

Amendment lines 200-203 require every C431-or-later stop to execute C439-C457
and forbid cleanup until C441 creates `detached.json`. If C431 fails before a
controller record, the controller exits before C434, or C433 exists but C434
fails before `lldb-spawn-attempt.json`, C439-C442 require a supervisor return
and LLDB artifacts from a session that never existed. The sentinel implements
a `no-debugger-start` phase (sentinel lines 8-24), but no separately gated row
invokes it.

Additionally, controller `spawnOwned` spawns at lines 59-70 but does not return
the owned handle to the outer `stale`, `helper`, `gui`, or `registration`
variable until after the initial wait and identity probes at lines 71-73. An
identity/probe/exit-observer failure in that interval enters `finally` with the
outer variable undefined, so lines 233-237 cannot settle the already spawned
direct child. This defeats the claimed exhaustive independent cleanup.

An LLDB attach failure is also non-closable: an LLDB child that exits before
C197 yields neither normal detach nor `watchdog.fired`; observer lines 25-27
reject it even though LLDB is actually terminal. There is consequently no
executable route to evidence freeze, exact rollback, and fixed-root removal for
all mandatory early-stop branches.

### 3. Critical — C196 can escape the watchdog, and C197 permits unapproved debugger bytes

Supervisor line 14 spawns detached LLDB. Line 16 performs a synchronous
exclusive write before exit/error listeners and before the watchdog is created
at lines 53-63. If that write or intervening setup throws, the supervisor exits
with a detached LLDB child and no watchdog. At watchdog time, a C521/C522
identity-probe failure rejects the watchdog without signaling LLDB (lines
57-61). The 149-second timer also starts only after post-spawn synchronous work,
not at the LLDB spawn/attach point, and its callback can be delayed by the Node
event loop; terminality by LLDB-child +149.9 seconds is therefore not mechanical
on every path.

More seriously, supervisor lines 46-51 forward every stdin chunk up to 64
bytes to LLDB before checking at lines 79-80 whether the accumulated bytes are
exactly `process detach\nquit\n`. Arbitrary debugger commands can therefore be
executed and merely rejected after the fact. That exceeds the inherited C197
authority and the prospective token's exclusion of other debugger authority.

### 4. High — terminal/detach proof is not bound to the same session and can unlock too early

C440 is discretionary runtime byte generation, not an exact mechanically
sourced template. Its JSON contains no supervisor PID/session identity. The
observer does not require or compare `lldb-start.json`; it accepts only file
hashes plus a self-authored role/exit field (observer lines 6-24). Normal detach
uses `/Process \d+ detached/` (supervisor line 81) without requiring the exact
target PID. Forced terminality can be accepted with no `lldbIdentity`/
`lldb-start.json` because observer lines 25-27 inspect only watchdog flag,
action ID, and exit signal. C441 can thus create `detached.json` and unlock
controller cleanup before C442 discovers a missing or inconsistent start file.
An arbitrary LLDB child exit code is also accepted on the normal-detach branch.

### 5. High — individual enumeration and durable evidence remain incomplete

C471 combines five distinct registration races; C480/C481 aggregate multiple
bounded waits and four different child settlements; supervisor 100 ms/900 ms
waits and numerous controller readiness/sentinel/timing waits have no unique
owner-gated rows. C440, C445, and C446 instruct an operator to synthesize
runtime-dependent base64/JSON/transcript bytes without an exact template and
mechanical source. These violate the brief's ban on aggregates and free-form
runtime byte generation.

C457 prints per-file hashes in unspecified `find` order but does not write a
hash manifest into the durable package. The claimed final hashes therefore are
not durably frozen. On the no-session branches, C445/C446 also demand PTY
transcripts and terminal metadata for sessions that never existed.

### 6. High — rollback is not mechanically asserted before deleting its basis

C458-C466 name the restore/removal operations, but C525 only prints current
hashes without comparing them to C385 and C526 returns success even when Git
status is nonempty. No row asserts byte equality or empty status. The branch
law does not make rollback operations independent after one fails. C529 can
therefore delete the baseline/temp root after a partial or dirty restore. The
current clean/absent state does not repair this prospective path defect.

## Prior-blocker disposition

The numeric row range, exact C196/C197 transcription, tracked registration
handle on the post-return path, separate settlement calls, and broad evidence
copy inventory improve on v1.17. They do not close v1.17's governing defects:
unique internal-operation enumeration is still incomplete; pre-return child
handles and no-debugger/attach-failure branches remain unsafe; the LLDB cap has
orphan/late-watchdog paths; terminal proof is not same-session fail-closed; and
runtime-generated evidence/final hashes are not mechanically frozen.

This verification does not authorize runtime execution, acceptance, remedy,
release, reliance, Git, Task Management, or foreign-loop action. No package,
helper, GUI, LLDB, attach, signal, replay, credential, network, product,
release, Git, Task Management, or foreign-loop operation was performed.
