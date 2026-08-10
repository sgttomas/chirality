# A2 Attempt-8 packet fresh adversarial verifier return R2

Status: `COMPLETE`

Verdict: `BLOCK_PACKET_REPAIR_REQUIRED`

The proposed packet is not decision-ready. Its frozen bytes are internally
well formed, but the runtime and cleanup graph contains unrelated-process,
escaped-child, timing, and evidence-retention hazards that violate the sealed
brief's fail-closed acceptance criteria. No proposed runtime command was run.

## Byte and structure checks

- `COMMAND_REGISTER_AMENDMENT_V1_16_PROPOSED.md`:
  `6ddf4b0fca2556b27f05fffd0a20cfe29aeb713520909da93c631b3148ebc073`
- `ATTEMPT_8_REAL_RUNTIME_COMMAND_APPROVAL_REQUEST.md`:
  `1c0b6cafa028460f47928f555606d05ae7167c02aa4b073a54bbb23b09dc9515`
- `real-runtime-controller.mjs`:
  `11a97d620e7f742e04d91418a1bbbeec2d1ef20b43e48596b75900c8cba4bd2f`
- `real-second-session-sentinel.mjs`:
  `a75b91299cb20f7daa2154a2ba9b36e4f71235ed634bfe81f80d16d7874d4242`
- `real-runtime-fallback-cleanup.mjs`:
  `ed577526d8d1122c24b96db1f62e4e796341bce27878145498288f94a1c19fec`
- packet-preparer return:
  `b337532eff788b3e256d5bdd3b21ff7d2989d480163522c84e037863d699237a`
- LLDB command file:
  `720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8`

All stated hashes reproduce. `node --check` passes for all three proposed
scripts. The amendment contains every ID C245 through C335 exactly once, plus
C196 and C197 exactly once: 93 rows and 93 unique IDs. C196 and C197 match the
approved v1.9 executable/control bytes. Their stated one-PID, enumerated-trace,
150-second, detach-only scope is not textually widened. Cited packet, ruling,
R3 verifier, manifest, overlay script, source dependency projection, and
Electron archive paths exist. The frontend is Git-clean.

## Blocking findings

### 1. Critical — C196 can attach to a reused, unrelated PID

The controller writes a numeric child PID at `ATTACH_READY`, but neither C300,
C335, nor the sentinel script proves that the live process at that PID is
still the same child immediately before C196. C300 only hashes the static JSON
record. The sentinel validates that same static record. Meanwhile the
controller does not race its `helperExit` promise against the wait for
`trace-ready.json`. If the helper exits after readiness and its PID is reused,
C196's `lldb -p <PID>` can attach to an unrelated process. This directly fails
the one-sealed-direct-child and no-unrelated-process criteria.

### 2. Critical — mandatory fallback cleanup can signal reused unrelated PIDs

`real-runtime-fallback-cleanup.mjs` reads numeric PIDs from durable JSON and
uses only `kill -0` before TERM/KILL. It performs no executable/start-identity
check. C318 is mandatory after both sessions terminate, including after the
controller has already reaped and cleaned its children. A released PID can be
reused between controller cleanup and C318, causing the fallback to signal an
unrelated process. The controller's own `waitExitPoll`/`exactKill` sequence has
the same check-then-signal PID-reuse race. Static controller provenance is not
live process identity.

### 3. Critical — the stale helper can escape on a pre-controller-record stop

The stale helper is block-scoped inside `try` and is never passed to
`cleanupOwned`. If `waitReady(stale.pid)`, its owner parse, the stale KILL, or
the stale exit assertion fails, `helper` is still undefined. The `finally`
branch therefore cleans neither process and can leave the stale direct child
running. In the readiness-failure cases there is also no `controller.json`, so
neither the detached sentinel nor C318 can identify or clean it. Thus not every
C299 terminal path is quiescent or recoverable.

### 4. High — the 150-second LLDB bound is not guaranteed by the packet timing

The sealed worst case can consume 28 seconds to GUI launch, 8 seconds for the
80 contact polls, 102 seconds to SIGTERM, and up to 8 seconds for the 80 exit
polls: about 146 seconds before post-signal snapshot and replay-terminal work.
C308 then permits waiting until 12 seconds after the signal target. That can
reach roughly 150 seconds from attach even before C197 and terminal polling.
The packet therefore cannot guarantee C197 detach before the inherited
150-second absolute C196 maximum on all allowed success-path timings.

### 5. High — network-attempt detection is not executable before runtime

C292 redirects all package output to a file. No later pre-runtime row reads or
searches that file, yet the row requires stopping on any network-attempt text.
An exit-zero package run that attempted network and recovered would proceed
through C299 without the required check. The output is only copied after the
runtime sequence. The stated no-network stop is therefore not mechanically
implemented.

### 6. High — fallback-cleanup evidence is created after the sole durable copy

C316 copies the temporary evidence directory to durable storage, then C318
creates `fallback-cleanup.json`, and C319 merely hashes the temporary cleanup
files. No command copies the newly created fallback receipt afterward; C333
removes the temporary root. Consequently the mandatory fallback action's raw
receipt is lost even on the nominal path, contrary to bounded evidence freeze
and cleanup-proof requirements.

### 7. High — early C247-or-later rollback is not executable as stated

The amendment says C320-C334 run after every C247-or-later terminal path, but
C320-C326 unconditionally copy all seven baseline files. If C247 succeeds and
any of C248-C254 fails before the full snapshot exists, the first missing
baseline copy makes this ordered rollback nonzero; the packet supplies no
separate pre-mutation cleanup branch. Thus the claimed every-terminal-path
rollback graph is incomplete, even though product bytes have not yet changed
on those earliest stops.

## Non-blocking confirmations and calibration

- The 28,000 ms target, 102,000 ms target, and 80-by-100 ms readiness/contact/
  exit loops are present and use monotonic scheduling where stated.
- Registration stdout is parsed in memory and the retained registration JSON
  excludes `tokenFile` and raw stdout. The retained GUI contact line contains
  the public `runtime.connectivity.bound` event and attempt count, not a token
  value. No memory/environment-dump command is present.
- Exact repo/frontend paths and declared cwd exceptions are coherent. Internal
  helper, GUI, registration, snapshot, signal, and cleanup tools are visible in
  the frozen scripts/proposal.
- Missing symbols or breakpoints remain nonzero/unknown evidence; the packet
  does not itself claim a remedy, D-APP-88 acceptance, release, or TM firing.

## Required repair before re-verification

Freeze a revised packet that (1) binds live child identity, not only PID,
immediately before attach and every signal; (2) makes stale/final-helper/GUI
cleanup exhaustive without ever signaling a reused PID; (3) fits detach and
terminal proof inside the 150-second bound under worst-case allowed timings;
(4) mechanically inspects package output for network attempts before C299;
(5) durably freezes post-fallback cleanup evidence; and (6) supplies a valid
cleanup branch for every C247-or-later stop. Fresh adversarial verification is
required on the revised bytes.

No runtime, package, helper, GUI, LLDB, attach, signal, replay, credential,
release, Git, Task Management, or foreign-loop action was performed.
