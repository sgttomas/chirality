# Independent review — restart-admission repair (R16)

Reviewer: Type 2 independent reviewer, Claude Fable 5.1, medium reasoning, no
delegation. Read-only source review on the integration checkout at HEAD
`5045178d4`; subject commits `15a07bdef` (repair) and `5045178d4` (test-only
correction), reviewed as `git diff bad09b9d2..HEAD -- projects/chirality-runtime`
together with the complete final files named in REVIEW_BRIEF.md. All four
hashes in FINAL_SOURCE_HASHES.json matched the checkout before review. No
product or test file was edited; nothing was committed; no App, GUI, network,
supplier, keychain or trial userdata was touched or read.

Path prefix for all `file:line` references below: `projects/chirality-runtime/`.

## Verdict: PASS

No blocking finding. The repair preserves fail-closed admission: no superseded
admission, preparation or queued candidate can be used after a host
replacement; renewal cannot change account, epoch, project, policy, consent,
release or daemon generation; no launch path depends on the composition's
swallowed `live()` renewal; no authentication, code-signature, seal, payload or
supplier policy is relaxed. Three non-blocking findings (one Medium, two Low)
and a list of test gaps are recorded for the next consolidated candidate.

## Commands run (from `projects/chirality-runtime`)

| Command | Result |
|---|---|
| `npx tsc -b --pretty false` | exit 0, no diagnostics (clean) |
| `npx vitest run tests/runtime-conformance-v2-admission.test.ts tests/codex-admitted-launcher.test.ts tests/codex-supervisor.test.ts tests/hosted-private-composition.test.ts tests/hosted-bootstrap-integration.test.ts tests/custody-config-status.test.ts` | 6 files passed (6), 121 tests passed (121), 0 failed, 0 skipped, 3.03 s |

Per file: runtime-conformance-v2-admission 13, codex-admitted-launcher 7,
codex-supervisor 42, hosted-private-composition 10, hosted-bootstrap-integration
9, custody-config-status 40. The 81/81 figure in RUN_LOG plus the 40
custody-config-status tests equals the 121 observed.

## Q1 — Superseded state after host replacement; renewal subject drift

Superseded objects stay invalid by construction and the repair adds no path
that revives them:

- An admission's liveness is the closure stored at issue time in a private
  WeakMap, `packages/daemon/src/runtime-conformance-v2-admission.ts:183`
  (`source.matchesAdmissionLease(lease)` with the lease snapshot captured at
  issue). `matchesAdmissionLease` (`packages/daemon/src/host-account-authority.ts:153-160`)
  compares `liveLeaseDigest`, which is a digest of daemon generation, client id
  and connection id (`:148`); `completeCeremony` revokes the old host as
  `host-replaced` (`:331-332`) and installs a new clientId/connectionId
  (`:335-366`). Nothing in the diff writes to `hostAuthorities` or
  `instanceAdmissions`; the only way to obtain a live admission is a fresh
  `issueHostedAccountAuthorityV2FromP2` against the current lease.
- A preparation's liveness is `source.matchesAdmissionLease(preparation.lease)`
  (`runtime-conformance-v2-admission.ts:207,211`). The factory keeps the old
  preparation until the renewed one is validated and then replaces it
  atomically (`packages/daemon/src/codex-admitted-launcher.ts:176-181`); any
  launcher already composed holds the bindings it was created with (`:166`),
  which is why renewal refuses while `launchers.size > 0` (`:171,179`) and
  `create()` refuses during renewal (`:164`). The production transport
  revalidates the preparation at launch
  (`packages/daemon/src/codex-authenticated-transport.ts:220,324,328`).
- The queued candidate (`preadmitted`) was admitted under the superseded
  preparation; the supervisor retires authority, session and candidate before
  renewal and refuses renewal on any retirement failure
  (`packages/daemon/src/codex-supervisor.ts:303-311`). After that,
  `launchAdmittedCandidate` (`:366-367`) has nothing queued and launches
  through the renewed factory.
- Running workers block renewal (`:301`); a worker entry stays in `entries`
  until `retire()` deletes it (`:645`), and DelegatedRuntime retires each
  worker after its turn (`packages/core/src/delegated-runtime.ts:293-300` and
  the completion/failure paths that call `retire()`), so an idle supervisor
  has no entries.

Renewal cannot change the subject:

- Release: the factory re-prepares from `previous.source, previous.releaseBasis,
  previous.input` (`codex-admitted-launcher.ts:176`); `prepareRuntimeWorkerInstanceV2FromP2`
  requires the release admission to be bound to that exact basis object
  (`runtime-conformance-v2-admission.ts:194-195`) and re-runs
  `revalidateRuntimePurposeReleaseV2` (`:197` -> `:348-354`), which re-reads
  and re-hashes the record, acceptance and owner-act files and re-checks
  expiry (`:319-332`, `:287-288`). Expiry is tested (`PURPOSE_RELEASE_STALE`).
- Daemon generation: `codex-admitted-launcher.ts:177` refuses a changed
  `daemonGeneration` (`HOST_ADMISSION_DAEMON_CHANGED`).
- Account, epoch, digest, project, manifest, canonical root, consent, policy,
  digests: the account is taken from the supervisor's current admission
  (`codex-supervisor.ts:312`) and the supervisor compares the complete renewed
  `instanceInput` against the current one with only `hostAuthority` masked
  (`:314`); both inputs are built by the same constructor
  (`runtime-conformance-v2-admission.ts:222`) from the same frozen preparation
  input, so key order is identical and any value drift fails closed. The
  renewed admission is then revalidated (`:315`) and the supervisor confirms
  its own admission did not change across the await (`:316`) before
  publishing `{ ...current, ...next }` (`:317`), which keeps the original
  `releaseBasis`. The renewed account is not trusted blindly: the next launch
  still checks the bound continuity and account digest against the admission
  (`codex-supervisor.ts:232-238`, `:485-487`).

## Q2 — Races

1. `acquire` awaits renewal before registering in `acquiring`
   (`codex-supervisor.ts:461-463`). The await is covered for cancellation and
   close: `cancelled()` at `:462` re-reads `cancellation.cancelled` (settable
   through `cancelAdmission`, because the cancellation record is installed at
   `:455` before the await) and `this.closed`. What is not repeated after the
   await is the guard at `:425` (duplicate worker id, `maxWorkers` capacity).
   See Finding 1 (Medium). No stale-preparation launch results from this:
   every acquisition still runs the full candidate admission.
2. `close()` during renewal: `close()` sets `closed` (`:647`), awaits
   registered acquisitions (`:649`) and then the in-flight renewal (`:650`).
   An acquisition parked on the renewal is not yet in `pendingAcquisitions`,
   but when it resumes `cancelled()` throws on `this.closed` before it
   registers or launches. Inside the renewal, `:313` and `:316` reject after
   the factory call when the supervisor closed, so the supervisor never
   adopts a renewed admission after retirement. If the factory already
   committed its preparation (`codex-admitted-launcher.ts:181`) the factory is
   closed next by `close()` (`codex-supervisor.ts:654`). Safe.
3. Two acquires plus a status poll during renewal: all three join the same
   promise (`codex-supervisor.ts:289`); a rejection propagates to each joiner
   (`:289`, `:292`), so both acquires fail with the renewal reason while the
   status poll swallows and reports the durable-binding result
   (`packages/daemon/src/hosted-private-composition.ts:641`). On success the
   status poll syncs `context.runtimeV2` only if the admission context is
   still current (`:642`), and both acquires proceed through candidate
   admission against the renewed factory. The `refreshHostAdmission` return
   value is always the supervisor's current admission (`:292`), so the
   composition context is re-synced on every poll even when renewal happened
   through `acquire`.
4. Renewal while a worker entry is being retired: the entry remains in
   `entries` until the end of `retire()` (`codex-supervisor.ts:645`), so
   renewal is refused at `:301` throughout retirement; the candidate's
   transport close settles the launcher and removes it from the factory set
   (`codex-admitted-launcher.ts:135-139,166`) before the entry is deleted, so
   there is no interval in which the supervisor is idle while a launcher
   still holds the old bindings. In the acquisition failure path the entry is
   deleted synchronously (`codex-supervisor.ts:579`) before the launcher is
   cleaned up (`:590`), but `acquiring` still holds the worker id until the
   `finally` (`:594`) and the factory independently refuses while
   `launchers.size > 0` (`codex-admitted-launcher.ts:171,179`).

No path publishes a worker or launches a candidate on a stale preparation:
launch always goes through `acquireGuarded` (`startManager`,
`acquireWithRuntimeTools` and `acquire` all route to it), which renews first,
then `launchAdmittedCandidate` revalidates the admission (`:369`), the transport
revalidates the preparation at launch, `admitCandidate` revalidates twice
(`:210`, `:248`), and the post-authority checks (`:484-487`) and the result path
(`:536`) revalidate again.

## Q3 — Fail-closed posture

Renewal failures are swallowed only in `hosted-private-composition.ts:641`
(`live()`), which is a status signal, not a launch gate: its result is consumed
only by `hosted-bootstrap.ts` `status()` (`:277-291`) to decide whether to
fence a ready admission. Every launch-bearing consumer either propagates the
renewal failure (`codex-supervisor.ts:461`, joined callers at `:289`) or
revalidates the admission directly without renewal
(`launchAdmittedCandidate` `:369`; `materializeAdmission`
`hosted-private-composition.ts:678-683`; `productionLogout` `:301,313-315`).
In `refreshHostAdmissionIdle`, only `HOST_AUTHORITY_NOT_LIVE` enters the
renewal branch; any other revalidation error rethrows unchanged
(`codex-supervisor.ts:298-299`). Renewal refusals are distinct
(`:300-302`), a queued-candidate retirement failure rethrows (`:309-310`),
the factory refuses non-idle states (`codex-admitted-launcher.ts:171,179`)
and rethrows issuer errors while resetting `refreshing` in `finally` (`:183`).
The in-flight promise is always awaited by its creator (`:292`) or by
`close()` with a catch (`:650`), so no unhandled rejection is introduced.

The design decision that `live()` does not fence on a renewal failure is
consistent with the durable-binding semantics documented at
`hosted-bootstrap.ts:86` and does not create an optimistic launch: a turn
issued while the host is not yet reconnected fails at `:461` with the
renewal reason instead of the generic admission message.

## Q4 — No relaxation of authentication, signature, seal, payload or supplier policy

- The diff touches only five files; `runtime-conformance-v2-admission.ts`,
  `host-account-authority.ts`, `hosted-packaged-release-state.ts`,
  `codex-authenticated-transport.ts` and `host-account-release.ts` are
  unchanged (`git diff --stat bad09b9d2..HEAD -- projects/chirality-runtime`).
- Renewal reuses the existing issuers unchanged. `prepareRuntimeWorkerInstanceV2FromP2`
  re-runs the release chain including `revalidateIssuedPackagedReleaseBasisV2`
  (`runtime-conformance-v2-admission.ts:351`) — the signed-bundle integrity
  check introduced by `21ca2dc22` — without any payload rehash, satisfying the
  owner's no-payload-rehash requirement while still re-verifying the release
  record, acceptance and owner act bytes by hash (`:323-324`).
- The factory re-runs `validateBindings` on the renewed bindings
  (`codex-admitted-launcher.ts:181`), which re-asserts the issued supply
  verifier (`:95`), the v2 policy/effective-config binding (`:97-108`) and the
  compiler identity (`:96`). `create()` gains one more refusal (`:164`); no
  check was removed.
- The new `refreshHostAdmission` on the factory is reachable only in-process
  from the supervisor that owns the factory; the composition never exposes the
  factory or the supervisor outside `hosted-private-composition.ts`, and the
  account argument comes from the supervisor's own current admission.
- Composition `live()` retains the durable account/epoch check as its first
  gate (`:633`) and adds a stricter final check (`:644`); it never returns
  `true` on a path that previously returned `false`.
- Host P2 ceremony semantics, peer requirement, EUID, proof and journal
  handling are untouched.

## Q5 — Are the tests real; coverage; gaps

Real components: the release file verifier (`verifyRuntimePurposeReleaseV2`
over private temp files), the P2 issuers (`prepare...FromP2`,
`complete...FromP2`, `revalidate...`), the launcher factory
(`createControlledCodexCandidateLauncherFactoryForTests` wraps the same
`factory()` as production, with a controlled `launchCandidate` adapter that
revalidates the preparation and stops before any supplier execution), and the
supervisor's real `refreshHostAdmission`/`refreshHostAdmissionIdle` methods on
an `Object.create(CodexSupervisor.prototype)` instance with the private fields
the path reads. Synthetic: the host lease carrier (an `Object.create(HostAccountAuthority.prototype)`
with `generation`, `closing`, `active`; `snapshotAdmissionLease` and
`matchesAdmissionLease` are the real prototype methods), and the packaged seal
check `revalidateIssuedPackagedReleaseBasisV2` is mocked to a no-op
(`tests/runtime-conformance-v2-admission.test.ts:13-16`, pre-existing in this
file). The launcher-factory `kernelLease` is a plain `{ held: true }` object.

Stated negatives covered (`tests/runtime-conformance-v2-admission.test.ts`):
disconnected host refusal with unchanged admission (`:219-222`); fresh-host
success with old admission and old preparation rejected and the new launcher
bound to the current lease (`:225-241`); queued-candidate retirement order
(`:223,227-228`); refusal while entries/acquiring non-empty (`:251-254`),
with an outstanding launcher (`:256-257`), after retirement (`:260-261`);
concurrent join returning one identity with the in-flight slot cleared
(`:262-265`); account-epoch and consent-digest mismatch rejected with the
superseded admission left unrenewed (`:278-284`); disconnect during renewal
leaving the admission unrenewed, then renewal on the next host (`:296-312`);
expired release (`:321-324`). Daemon generation is asserted equal on the
positive path (`:233`).

Gaps (none blocking):

1. No negative for a changed daemon generation
   (`codex-admitted-launcher.ts:177`, `HOST_ADMISSION_DAEMON_CHANGED`).
2. No test drives the real `acquireGuarded` prologue: renewal before
   registration, `cancelled()` after the await, a `cancelAdmission` during
   renewal, or concurrent acquires at capacity (see Finding 1).
3. No test for `close()` awaiting an in-flight renewal
   (`codex-supervisor.ts:650`) or for the `:313`/`:316` "changed during
   renewal" rejections (for example an entry registered or `runtimeV2`
   replaced across the await).
4. No test that a queued-candidate retirement failure blocks renewal
   (`:308-310`) or for the ownership consequence in Finding 3.
5. `tests/hosted-private-composition.test.ts` and
   `tests/hosted-bootstrap-integration.test.ts` are unchanged; the
   composition `live()` renewal, its swallowed-failure behaviour and the
   `context.runtimeV2` re-sync (`hosted-private-composition.ts:639-644`) are
   untested through `status()`.
6. The seal check is mocked, so the renewal's re-verification of the packaged
   basis is not exercised (pre-existing test posture for this file).
7. The supervisor fixture bypasses the constructor, so invariants that depend
   on `cancellations`, `pendingAcquisitions` or `managers` are not
   observable in these tests.

## Findings

### Finding 1 — Medium (non-blocking): duplicate-worker and capacity guard precedes the renewal await

`packages/daemon/src/codex-supervisor.ts:425` performs the
`entries.has(workerId) || acquiring.has(workerId) || capacity` check, but the
acquisition now awaits `refreshHostAdmission()` at `:461` (which performs
release-file I/O in `revalidateRuntimeInstanceAdmissionV2` even when no
renewal is needed) before `acquiring.add(workerId)` at `:463`. Only
cancellation/close are rechecked at `:462`. HANDOFF item 2 asked for the
worker/closed/capacity checks to be repeated after the await; RUN_LOG records
that only cancellation/close were.

Scenario A (capacity): with `maxWorkers = N` and `N - 1` workers registered,
two acquisitions for distinct turn ids both pass `:425`, both await the same
renewal, both register and launch, so `N + 1` candidates run. Bounded
over-commit; every candidate still passes full admission.

Scenario B (duplicate id): two concurrent acquisitions for the same worker id
both pass `:425`; the second overwrites the first's `cancellations` record
(`:455`) and `pendingAcquisitions` entry (`:465`); at `:572` the second
`entries.set` replaces the first's entry, whose running worker becomes
untracked (its `result`/retirement still run, but `inventory()`, `retire()`
and approval liveness no longer see it). In production this scenario is
prevented upstream: DelegatedRuntime refuses a duplicate turn id with
`SESSION_TURN_IN_PROGRESS` (`packages/core/src/delegated-runtime.ts:424-425`)
and forbids replaying a turn with a durable record (`:428`). The supervisor's
own invariant is nonetheless weakened.

Recommended repair (not applied): repeat the `:425` guard immediately after
`:462`, before `:463`.

### Finding 2 — Low: cancellation record leaks when the pre-try prologue throws

`codex-supervisor.ts:455` installs `cancellations[workerId]` before the
renewal await at `:461`, but `:461-462` are outside the `try` that begins at
`:469`, so when the renewal rejects (for example "Host admission cannot renew
while work is active" or a `PURPOSE_RELEASE_STALE` renewal failure) or
`cancelled()` throws, the `finally` at `:594` does not run and the record is
never deleted. Scenario: repeated failed turns while the host is
disconnected each leave one entry in `cancellations` (turn ids are unique), and
`close()` later calls `cancelAdmission` on each stale record (`:648`), which is
harmless. Memory growth only; no admission effect.

### Finding 3 — Low: queued-candidate retirement failure drops ownership of the candidate

`codex-supervisor.ts:306` clears `this.preadmitted` before attempting the three
closes at `:308`. If any close fails the renewal is refused (`:309-310`), as
designed, but the partially retired candidate is no longer referenced, so
`close()` (`:654`) will not retry it and a second renewal attempt proceeds
without it. Scenario: `pending.candidate.cleanup()` throws a descendant
reconciliation diagnostic; the supplier process group may linger until daemon
stop while the next renewal succeeds. The stale candidate can never be
published (`launchAdmittedCandidate` only returns `this.preadmitted`,
`:366-367`), so this is a resource-retention concern, not an admission one.
Note that `close()` keeps `preadmitted` on failure (`:658`), so the two paths
have different ownership semantics.

### Informational

- `runtime-conformance-v2-admission.ts:174` issues the host authority from a
  fresh lease snapshot rather than `preparation.lease`; a host replacement in
  the gap between `:211` and `:221` would bind the admission to the new host
  while the factory's preparation stays on the old one, leaving the next
  launch to fail closed (`WORKER_PREPARATION_INVALID`) with no renewal
  trigger because the admission itself is live. The gap is microtask-
  contiguous under Node's event loop, the code is pre-existing and shared with
  the original `establishAdmission` path, and the outcome is fail-closed.
- When the supervisor rejects at `codex-supervisor.ts:313-316` after the
  factory already committed at `codex-admitted-launcher.ts:181`, the factory
  preparation is renewed while the supervisor admission stays superseded; the
  next acquisition re-enters renewal and the factory re-prepares from the
  renewed preparation, so the state self-heals and nothing launches meanwhile.
- Every `status()` poll now revalidates the v2 admission, which re-reads and
  hashes the three release files (`runtime-conformance-v2-admission.ts:323`).
  Cost only; the same read already occurs on every launch.
- The test-only commit `5045178d4` correctly adds `timeoutMs` to the expected
  request key set; the client forwards `timeoutMs` on every request
  (`packages/client/src/client.ts:156`), and the change is confined to the
  assertion (`tests/custody-config-status.test.ts:90`).

## Scope statement

Reviewed: the diff and the seven files named in the brief, plus the read-only
consumers needed to answer the questions (`hosted-bootstrap.ts` `status()`,
`codex-authenticated-transport.ts` preparation revalidation,
`packages/core/src/delegated-runtime.ts` acquire/retire, `packages/client/src/client.ts`).
Not performed: any build, sign, launch, GUI, network, supplier, keychain,
trial App or userdata access; no suite other than the six named files; no
edits to product or test files; no commit. Live-state item 5 of HANDOFF
(native quit/relaunch with retained daemon) remains open and is outside this
review.
