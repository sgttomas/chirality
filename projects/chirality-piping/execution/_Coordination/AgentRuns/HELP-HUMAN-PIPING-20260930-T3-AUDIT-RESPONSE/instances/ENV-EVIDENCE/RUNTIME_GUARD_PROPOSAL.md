# E0 runtime and guard proposal — inert, not admitted

Status: read-only proposal, 2026-09-30. No guard was created or activated, no
signal was sent, and no build, installation, download or workload was run.
`observations.json` contains ENV-EVIDENCE's actual read-only commands and
results. ROOT's separately supplied host observations are explicitly attributed
in `CONTEXT.json`; they are not executions by ENV-EVIDENCE.

## Runtime replacement

Use a new response-specific runtime root `<RESPONSE_RUNTIME>` whose absolute
location ROOT selects and records locally. Keep portable records under `Run`.
Never bind `<RESPONSE_RUNTIME>` or `<RESPONSE_VENV>` to the absent M5 aliases
`<M5_T3>` / `<M5_VENV>` by implication.

Proposed layout, not materialized:

```text
<RESPONSE_RUNTIME>/
  sources/<slice>/<full-candidate-sha>/    ROOT-owned checkout/archive
  targets/<slice>/<candidate-sha>/        one target per slice/candidate
  venv/                                  isolated, version-recorded environment
  guard/registry/                        response job identities, ROOT admission
  logs/<slice>/<job-id>/                  complete raw outputs and host samples
  scratch/<slice>/                        exclusive disposable inputs/outputs
```

ROOT controls all Git and source snapshots. Use a clean Git working tree for
GEN-8, whose tracked-set contract is not met by an archive. Reviewers get their
own source snapshot/target. No copying of unrelated caches or existing targets
is proposed. A same-source base and candidate use the same approved M3 runtime.
Full-scale evidence that cannot fit here gets a pinned run packet for a suitable
host; it does not inherit the M5 observations.

The local default Rust is 1.92.0. The historical and CI-pinned 1.97.1 is absent.
Do not substitute the default. ROOT must seal the exact-1.97.1 provisioning
action below before compilation. Offline
registry/dependency completeness remains unknown: no cargo build/fetch or cache
walk was performed. Native and wasm target availability for 1.97.1 remains
unestablished because the toolchain itself is missing.

System Python 3.13.7 is available; no project venv was found in the exact paths
checked. Relevant installed metadata includes pytest 9.0.2, xdist 3.8.0,
jsonschema 4.26.0 and PyYAML 6.0.3. Coverage is 7.15.0, whereas the project's
requirements-dev.txt pins 7.15.3. Package metadata does not establish that the
project's entire Python environment works. Seal an isolated venv and complete
package/version inventory later. K4's generator declares standard-library-only
inputs; it was inspected and hashed, not imported or run.

Node 24.5.0, npm 11.5.2, Apple Clang 21.0.0 and a command-line SDK are visible.
Project and desktop node_modules are absent in this checkout. The lockfile is
present, but npm installation, native build dependencies and wasm tools remain
unverified. No installation is part of this checkpoint.

### Concrete provisioning proposal (not executed)

ROOT reported an approved HEAD request for the official 1.97.1 channel manifest
returned HTTP 200 (last-modified 2026-07-16); ENV-EVIDENCE did not make that
request or download the manifest. This supports planning exact 1.97.1 setup,
not claiming an installation exists.

Under a later sealed setup grant, allocate response-owned
`RUSTUP_HOME=<RESPONSE_RUNTIME>/rustup` and
`CARGO_HOME=<RESPONSE_RUNTIME>/cargo`. Use the already available rustup launcher
with those variables; keep the owner's default Rust home/configuration intact.
Retain `RUSTUP_AUTO_INSTALL=0`, so an accidental version probe never provisions.
The explicit authorized provisioning steps would be:

```text
rustup toolchain install 1.97.1 --profile minimal
rustup target add --toolchain 1.97.1 wasm32-unknown-unknown
```

The first command must install the `aarch64-apple-darwin` host toolchain, and
the second supplies the wasm target required by the maintained desktop build.
Record the downloaded official channel manifest, distribution checksum
verification and exact `rustc --version --verbose`, `cargo --version`,
`rustup toolchain list` and installed-target outputs. Add rustfmt/clippy only
if a sealed gate requires them; do not install extra toolchains by default.
These commands are inert documentation here; no setup is currently authorized
for this TASK.

For each exact candidate, enumerate the Cargo manifests required by its named
gates and hash their Cargo.lock files. In the separately approved setup phase,
fetch those locked dependencies into the response CARGO_HOME, then verify
`cargo metadata --offline --locked --format-version 1 --manifest-path <manifest>`
for every required manifest and target configuration. Metadata proves resolution,
not compilation. Do not use `--no-deps` as a completeness check, and do not edit
Cargo.lock to make resolution succeed. Preserve fetched dependency identities,
metadata, exit codes and Cargo-home identity in the setup evidence. Native
build prerequisites remain explicit until the first guarded compilation passes.

Create `<RESPONSE_RUNTIME>/venv` using the selected Python 3.13.7 without system
site packages, install the project's exact requirements-dev pins under the
setup grant, and retain the complete resulting package lock/freeze plus
`pip check`. Review additional tool/test dependencies from the named gates
before sealing that lock. Installed system packages are an inventory only.
For Node, preserve the existing package-lock identity and review required
installation scripts before running an authorized locked installation; any
native build script uses the guarded heavy slot. Do not let a missing `npx`
command provision tools implicitly. No setup/build/test command in this
paragraph was run by ENV-EVIDENCE.

Required launch environment for a later authorized workload:

```text
RUSTUP_TOOLCHAIN=1.97.1
RUSTUP_HOME=<RESPONSE_RUNTIME>/rustup
CARGO_HOME=<RESPONSE_RUNTIME>/cargo
RUSTUP_AUTO_INSTALL=0
CARGO_INCREMENTAL=0
CARGO_BUILD_JOBS=1
RUST_TEST_THREADS=1
CARGO_TARGET_DIR=<RESPONSE_RUNTIME>/targets/<slice>/<candidate-sha>
PYTHONDONTWRITEBYTECODE=1
```

Cargo commands retain `--offline --locked -j 1`. Use one pytest worker (no
`-n auto`; serial default or explicit one worker), and one supported JavaScript
worker. ROOT grants one global heavy workload group at a time. Compiler child
processes belong to that one group; this limit is not a claim that cargo itself
has no subprocesses. The archived DEC-025 driver exports jobs=8 and test
threads=4 internally, so prepending conservative variables is insufficient:
a separately reviewed response driver must remove/override those internal
settings while preserving the surfaces, inventories and failure reporting.
Never edit the archived driver to do this.

## What is visible now

ENV-EVIDENCE's snapshot at 16:27:48Z (see exact timestamps in observations.json):

- macOS 26.6.2, Darwin 25.6.0, arm64; M3 Air supplied by the owner.
- memory_pressure reports 17,179,869,184 bytes total (16 GiB), 68% system-wide
  memory free. This metric is a snapshot, not a byte-exact free-memory amount,
  a sustained reserve, or an allocation admission.
- vm_stat is permitted and provides page/compressor and cumulative swapin/out
  counters. A single cumulative count supplies neither current swap usage nor
  the rate attributable to this response.
- df reports 109,122,740 KiB available, about 104.07 GiB, on the shared data
  volume used by this checkout and temporary storage. This is a snapshot, not
  reserved space. Original M5 scratch was reported around 130 GB; do not try
  to mirror it wholesale or prune unrelated data to make room.
- Default sandbox denies sysctl memory-size, CPU-count, swap and pressure-level
  queries. It also denies ps for the collector's own PID and relevant-user
  process metadata. Relevant jobs, process identities, current per-process
  RSS/footprint and guard presence are therefore unknown from this execution.

ROOT subsequently supplied an approved read-only query outside the default
sandbox: 16 GiB, 8 logical CPUs, dynamic swap total 4096.00M / used 3118.19M /
free 977.81M, own-shell PID/PPID/PGID/RSS visible, and `/usr/bin/time -l` able to
report max RSS and peak footprint. These prove that default-sandbox denial is
not host absence. They do not establish a permitted continuous sampler for this
TASK. `time -l` is post-run peak evidence, not a live footprint monitor.
Existing swapped pages do not prove current resource trouble or causation by
this response. The nonzero baseline makes free percentage alone insufficient.

## Guard ownership contract

This is a proposal for later implementation and controlled validation. No
executable guard is supplied in this packet.

1. ROOT issues a single-use admission token naming response/run, slice, exact
   candidate/input hashes, allowed executable, target and log root, limits and
   expiry. A launcher consumes it under a lock that represents the single
   heavy slot. No token means no workload launch.
2. Each workload starts in a new OS session with a dedicated, persistent
   supervisor as session and process-group leader. Workload and all its children
   remain in that group; no daemonization, detached children or independent
   sessions are allowed. The guard is outside the target group.
3. The launcher creates an explicit registry entry containing run/job nonce,
   UID, supervisor PID, OS process start identity, PGID/session identity,
   candidate/input hashes, monotonic launch time, target/log paths, granted caps
   and the supervisor control endpoint. The supervisor remains alive until the
   group is empty, preventing reuse of its live PID/PGID during normal stopping.
   Its TERM handler must keep it alive during the stop grace while children
   retain normal signal behavior; do not accidentally propagate an ignored
   TERM disposition into workers. Validate this detail before qualification.
4. Before any signal, verify the live supervisor's UID, PID/start identity,
   group/session, registry nonce and control handshake. Only the registered
   response group can be stopped. Neither command substrings, directory names,
   owner-wide process lists, old PIDs nor historical guard names are ownership
   proof. Never use `pkill`, a broad `pgrep` match or a filesystem substring to
   choose signal recipients.
5. If identity fails or the leader disappears, fail closed to new admission.
   Use the previously authenticated supervisor/control path when still valid;
   do not signal a recycled numeric group. Escaped descendants or inability to
   contain the group are a failed guard qualification, not a reason to signal
   unrelated processes. Preserve the log and return to ROOT.

## Metrics, proposed initial limits and refusal rules

Keep three independently named quantities:

- **Allocator requested live bytes / peak:** the observation binary's counted
  heap; its in-place and move-model peaks differ. H's allocator cap applies to
  the in-place requested-live model. This excludes parts of process/OS memory.
- **Resident set size (RSS):** per-process resident pages. An aggregate over
  related processes can double count shared pages; it is a conservative
  operational signal, not interchangeable with heap or physical footprint.
- **Physical footprint:** OS-accounted process footprint, which must come from
  a validated live provider. Group summation and shared-memory semantics must
  be documented. It is not inferred from heap or post-run RSS.

Preserve the current independent binary heap backstop and refusal marker
(`H/src/bin/k6_observe/alloc.rs`; main requires `--heap-cap-bytes`). It protects
against a missed sampled peak within its accounting model. Never use the
estimate-bypass option to force a scale run. Keep VR's independent checks too;
this packet has not verified VR's runtime implementation.

Proposed initial observation group ceiling: **at most 2 GiB** physical footprint
and conservative aggregate RSS, with a separately stated binary heap cap **at
most 2 GiB** and lower when calibrated overhead requires it. Begin tiny cases
with a smaller cap chosen by the admitted plan; 2 GiB is a ceiling, not a target.
A heap cap equal to 2 GiB cannot be described as a 2-GiB process cap. Compiler,
linker and Python jobs have no demonstrated heap backstop here and require
separate budget validation before their first heavy grant.

Preserve a **35% available-memory reserve** as the operating policy. Proposed
warning/stop threshold is **40%** on the validated availability metric to leave
5 percentage points for sampling/stop delay. Proposed admission uses multiple
quiet preflight samples, requires normal pressure and stable swap, and requires
projected availability after the group's measured worst-case increment and
safety allowance to remain at least 40%. Derive the increment and allowance
from same-host tiny runs and observed stop latency before increasing size.
An uncalibrated free-percentage projection is not an admission calculation.
No userspace sampler reserves RAM or guarantees immunity to a sudden unrelated
allocation; a reserve breach is a failed resource condition.

The following intentionally conservative defaults are proposals, not validated
limits or engineering criteria:

| Signal | Action by a later qualified guard |
|---|---|
| Valid live group footprint or conservative RSS reaches its granted ceiling | Stop only the registered group; retain peak/stop evidence |
| Availability reaches 40%, or projected next-step reserve is insufficient | Refuse launch/next step; stop active owned workload while 35% reserve remains the policy floor |
| OS pressure changes to warning/critical | Stop owned workload, release no further grant until ROOT re-evaluates |
| New swapouts occur during the job or used swap grows by at least 64 MiB from the quiet baseline | Stop as a conservative host-resource event, without attributing causation to this job |
| Required sample missing, malformed, stale or denied | Refuse admission; for an active workload request its verified supervisor to stop immediately; log monitoring failure |
| Registry identity or containment verification fails | No blind group signal; authenticated-control recovery only; block further grants and return to ROOT |
| Guard heartbeat is lost | Supervisor's independent watchdog stops its own registered group; this control path needs validation |
| Disk headroom falls below the sealed per-job write budget plus reserve | Refuse next step / controlled stop, preserve records; no deletion outside owned scratch |

Start with a one-second sampler target and a two-second maximum sample age,
subject to measured latency. Do not run a build merely because periodic
sampling works. Stop initially requests cooperative termination, then SIGTERM
through the verified group owner; after a short bounded grace (proposed two
seconds), a still-verified owned group may receive SIGKILL. Critical pressure
may require immediate termination under ROOT's approved design. Before every
escalation recheck identity; after final group KILL, never retry against the
old numeric PGID without a still-live verified leader; log reason, signals, timestamps, samples and exits.
No such signal sequence was tested in E0. Resource refusal/stopping is not a
passing numerical outcome and triggers diagnosis, not automatic retries.

## Qualification required before a heavy slot

ROOT must explicitly authorize a separate light guard-implementation/validation
slice and its host boundary; ordinary workspace tools do not currently expose
all needed monitoring. In that slice:

1. Freeze the implementation, registry schema, providers, thresholds and
   response-owned paths for independent review. Verify live PID/start identity,
   session containment, RSS, footprint, pressure, swap, sample timestamps and
   failure semantics using an approved read-only host boundary first.
2. Validate logic with recorded/synthetic samples in a pure decision harness.
   Cover high baseline but stable swap, increasing swap, low reserve, pressure,
   malformed/stale samples, PID reuse, changed UID, escaped child and dead guard.
   Pure simulation must never call signal APIs.
3. Only under that later explicit validation grant, exercise termination on
   known response-owned low-memory sleepers and a bounded allocation child,
   including a child which ignores TERM. Prove an unrelated sentinel survives,
   verify descendant containment and capture stop latency/overshoot. Keep all
   validation allocations far below the proposed 2-GiB ceiling. No such test
   is authorized or performed by the present brief.
4. Verify the binary heap refusal independently with a tiny cap on an admitted
   observation binary and preserve the original marker/classification. Record
   `time -l` peaks in addition to live guard samples. Review failures before
   a ROOT-issued heavy slot.
5. Establish same-M3 base/candidate suites and calibration after runtime setup.
   Tiny/10/100-member cases precede 1,000; each increase needs a recalculated
   admission. Ten-thousand-member W1 runs remain conditional; dense matrices
   at 10,000 or more members remain prohibited. Preserve required gate coverage
   as outstanding if the host cannot admit it.

E0's inventory/proposal checkpoint is complete. The full graph E0 acceptance
condition (executable runtime, verified guard/admission) remains open.
