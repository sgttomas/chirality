# RETURN — GUARD-IMPLEMENTATION source-only checkpoint

**Implemented and pure-tested; inactive and not live-qualified.** Return from
TASK `/root/delivery_manager/guard_implementation` to DELIVERY
`/root/delivery_manager`, under ROOT `/root`. Independent review of this sealed
packet must precede any controlled signal test or active workload grant.

Launch basis: `b2acd4023557eeff2416d99aaed1f03abf7a2404`; sealed brief SHA-256
`09079fc3441de766ef4abbe463d6731741b8c0df8cbadb4ee3c13d147e66ee68` verified.
Product basis remains main `3bddc2b05f6106e969c7cf43373b230845c7cc66`.
`CONTEXT.json` records actual native parentage, supplied/read instruction and
record hashes, SDK origins/hashes, supplementary steering, and host limits.
All tracked read-basis bytes still matched the launch commit at seal; the ROOT
native-toolchain setup record is a later separately hashed supplement.
No model-diversity claim is made and no descendant was delegated.

## Source and tests

`Run/tools/host_guard.py` is a standard-library local command launcher/monitor.
It uses an explicit job JSON and one shared runtime flock, a separate session
supervisor, private inherited nonce/sequence control, and the supervisor's own
TERM/KILL path. The monitor never signals a remembered workload PGID. The
supervisor's live ownership remains pinned through escalation, workers reset
signal dispositions, monitor/heartbeat failure stops via the owned supervisor,
and an unresolved ACTIVE latch blocks further admission. Normal contained
workload failures preserve original return codes separately from guard health.

Providers distinguish group RSS, physical footprint, system available estimate,
pressure, swap baseline/growth/swapout counters and disk headroom. Conservative
40% stop/projection threshold precedes the 35% reserve policy, with at most
2 GiB group caps and explicit per-job allowance/disk/duration limits. Raw job,
provider, identity, sample, output and stop evidence stays in bounded private
runtime logs. No approval-token interface or general process service was added.

The pure suite passes **41 tests**, including threshold equalities, high stable
swap versus new growth, invalid/NaN/negative/stale readings, denial/monitoring
loss, heartbeat loss and TERM/KILL grace, missing/reused/changed identities,
UID/session/escape checks, unrelated sentinel exclusion, fake native adapter
return sizes and identity races, control nonce/sequence replay, signal-default
reset, log bounds and required executable hash presence/content. Import and every test block live process creation,
signals, session mutation, os._exit, native loading, real socketpair/flock and
live identity reads; tested providers/control sinks are in-memory fakes.
The real fork, native calls, signals, lock and workload branches were not run.

| Artifact | SHA-256 |
|---|---|
| `Run/tools/host_guard.py` | `feb0e1508fde6c764eefb85e2b72bc7a597edf86d48307fb646a80a80eac03db` |
| `test_host_guard.py` | `5e72b5d9589b345d1ef45171227b7b6a56281b7b2984e97625291112fb62b5b1` |
| `pure-tests.log` | `976d0b3ee9ed9856bb78236e553a7b8963d7762020f78528a81d38874da557c8` |

`VALIDATION.json` records those hashes and the normalized SDK-manifest hash.
`SHA256SUMS` seals this complete packet plus source, using repository-relative
paths. It excludes only itself.

## Review and later qualification

- `PROVIDERS.md`: exact installed-SDK ctypes derivation, primary-source API
  return semantics, metric distinctions and fail-closed behavior. Layout is
  source-derived and pure-calculated, not a compiled or live ABI witness.
- `LIMITS.md`: ownership, latching, resource/log limits and unproved conditions.
  A userspace poll cannot guarantee detection of an unobserved double-fork /
  reparent escape. External supervisor SIGKILL also defeats this single-owner
  containment; the monitor retains the latch and never targets an old group.
  Conservative process-table races may stop short-lived cargo children and
  must be evaluated in later direct-command qualification.
- `LIVE_QUALIFICATION.md`: precise later read-only provider witness, bounded
  fixture/job schema/commands, retained sentinel/monitor child handles, clean
  completion, 16 MiB allocation, sleepers, TERM-ignore escalation, 64 MiB cap
  crossing, monitor loss, visible escape, lock/latch refusal and latency targets.
  All commands are proposals, not executions or new grants. Record measured
  overhead, cadence and overshoot before enlarging any job.
- `DEC025_SERIAL_PROPOSAL.md`: separate minimal new driver adaptation. It
  removes internal 8/4 concurrency settings, preserves maintained discovery,
  all-manifest/no-fail-fast and other surface inventories, keeps original
  failures explicit, and stops on resource/containment refusal. It is neither
  implemented nor covered by initial command qualification.

K6's existing launcher creates a new session, and VR uses it. Those runners
remain unsupported. LIMITS proposes a later explicit registered-supervisor
adapter that retains their watchdog decisions and independent binary heap
backstop. No existing runner, watchdog, cap, tolerance or protected gate changed.

ROOT's separate setup evidence reports native minimal Rust 1.97.1 in its isolated
runtime, leaving the owner's default toolchain untouched. This TASK neither
probed nor activated it, and preserved the older RUNTIME_BINDING record. The
later owner direction permits safe new M3 evidence while M5 originals are
unavailable for now; it does not expand this source-only checkpoint.

## Execution and write boundary

Only `Run/tools/host_guard.py` and `Run/instances/GUARD-IMPLEMENTATION/**` were
written. Initial sealed packets, product source, instructions and other agent
outputs were preserved. No live provider/guard/workload, process signal,
compiler/model run, package download/install, setting change, Git/index
mutation or delegation was performed. Read-only SDK and primary source
inspection supported the bindings; it supplied no runtime capability claim.
Full E0 guard/admission qualification and any heavy slot remain outstanding.
