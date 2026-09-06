# Chirality Shared Runtime

This workspace contains Chirality's provider-neutral runtime contracts,
orchestration core, headless daemon, authenticated Unix-socket client, CLI, and
safe engine adapters.

The daemon is the sole owner of engines, credentials, sessions, delegation,
turn locks, interruption, tools, and local-model residency. Desktop, CLI, and
project integrations are clients. Runtime state is operational and
non-authoritative; project manifests and governed execution records remain in
their registered repositories.

## Development

Requires Node.js 22.19 or newer.

```sh
npm ci
npm run typecheck
npm test
npm run build
```

The integration tests use temporary Unix-domain sockets. Sandboxed runners
must permit local socket creation; no TCP control listener is used.

## Packages

- `@chirality/runtime-contracts`: public events, sessions, projects, residency,
  and protocol types.
- `@chirality/runtime-core`: project/session registries, turn coordination,
  governed delegation, and residency control.
- `@chirality/runtime-daemon`: authenticated HTTP/1.1 and SSE over a Unix
  socket.
- `@chirality/runtime-client`: typed Node client for that Unix socket.
- `@chirality/runtime-cli`: the `chirality` command surface.
- `@chirality/engine-claude` and `@chirality/engine-pi-omlx`: host-injected
  engine adapters. Pi/oMLX is loopback-only and accepts no ambient Pi
  configuration.

The Electron composition root supplies encrypted provider credentials and the
concrete embedded engines when it starts with `--runtime-daemon`.

## Opt-in delegated runtime

The v2 broker composes a registered canonical project identity, private consent
and retirement stores, and a second, purpose-limited supervisor Unix socket.
Only the daemon holds supervisor credentials. Existing v1 routes remain usable
and cannot enter this service; their compatibility adoption remains separate.
Every consequential v2 request obtains a one-use project/operation preflight and
checks the exact compatibility identity and contract-basis SHA on both sides.
`RUNTIME_COMPATIBILITY_MISMATCH` details survive client and CLI handling.

`RuntimeClient` exposes delegated capabilities, consent, turns, interruption,
pending approvals, approval decisions, and operator sign-in. The CLI exposes
`delegated capabilities|consent|turn|interrupt|approvals|decide-approval` and
`hosted-login start|status|cancel`. The generic `approvals list|decide` surface also
serves supervisor-backed manager workers in local-engine-only composition, with
explicit attributed decisions and the same compatibility preflight. Use
`chirality --help` for arguments. Role
entry offers untyped, Agent 0, Agent 1, Agent 2, and TASK, labelled **role not
mechanically enforced** with instruction-asserted evidence. Executed role policy
is recorded separately from the actual model and fences thread reuse.

Consent stores all three command-network postures: off, ask per destination, and
on. All three have explicit native policy settings. The ask configuration and
attributed approval forwarding are implemented, but actual supplier ask remains
unavailable pending the supplier correction and validation described below.
Approval requests and decisions are durable, generation-bound records.
`applied:true` means the decision was written to the active supplier transport;
it does not claim the requested command or network operation succeeded. Stored
consent and a vendor configuration value do not establish network enforcement.
The closed v2 event contract validates approval attribution and the four terminal
events: completed, failed, interrupted, and cancelled. Optional vendor diagnostics
are bounded and cannot confer authority; unknown vendor requests fail closed.

Retirement commits one immutable terminal record per turn. Recovery does not
replay work: an unresolved journal requires reconciliation. A persistent vendor
thread may resume only when canonical root, cwd, account, epoch, root policy and
selected role policy match. Native start, resume and turn requests explicitly bind
the user reviewer and posture-derived approval policy; start/resume responses must
confirm both, so persisted thread overrides cannot silently replace them. This guarantees one durable terminal record, not
exactly-once external effects.

## Standalone composition

After `npm run build`, two separate processes can be started with the package bin:

```sh
chirality-runtime-service supervisor --config /absolute/private/runtime/config.json
chirality-runtime-service daemon --config /absolute/private/runtime/config.json
```

`startStandaloneJob` and `readStandaloneConfig` expose the same composition to a
host. The strict `StandaloneConfig` type in `packages/daemon/src/standalone.ts`
is the configuration contract. Configuration is an owner-only 0600 file inside
its 0700 runtime directory. The project must already be registered through an
authorized runtime operation. Supervisor credentials rotate with the process
generation and bind the complete configuration; restart both jobs after a change.
`renderRuntimeJobs` renders these two jobs for launchd but does not install them.
No secret belongs in a plist, client request, or command argument.

The tagged `controlled-worker` mode runs a trusted operator-provided executable
with bounded process lifetime and process-group cleanup. It is a test/embedding
seam, not a filesystem or network sandbox, and cannot satisfy hosted verification.

The `hosted-validation` mode connects the accepted App Server 0.149.0 payload to
the real broker through a trusted provider process and a verified native named
policy for model actions. It requires an
explicit model, attributed provider-network consent, and an auth-file digest.
The exact binary and private `CODEX_HOME` reside in a dedicated worker-private
subtree, disjoint from broker credentials, journals, registries and configuration;
the project itself is also disjoint from broker storage. The environment omits
ambient credentials. Payload size and SHA are checked before execution and again
before use. Vendor signature status remains a separate finding.

Production hosted Codex worker acquisition also requires a complete, current conformance record
and separately referenced owner acceptance. The record binds the actual supply,
canonical root, account and epoch, consent, policy, configuration, activation and
deployed artifacts. All 18 primary/descendant and owner-live limbs are required;
selected canaries or controlled factories cannot mint admission. Missing or stale
evidence prevents both ordinary and manager worker acquisition. Login remains a
separate operation. This gate does not apply to the separate local Pi or legacy v1
paths and does not establish their release acceptance. Deployment drift invalidates the process generation and
requires restart. The inventory includes first-party deployed files, manifests,
lock and the resolved declared production dependency packages, including installed
optional/peer dependencies and workspace links. This is a bounded disk and
resolution inventory, not proof of every already-loaded module or arbitrary
dynamic import or validation that every declared peer requirement is satisfied.
The measured inventory contains 35,598 external files (210 MB): startup plus first
check took 8.50 seconds and an unchanged check 3.82 seconds in the latest
single-run measurement on the test host. This
is a material admission cost, separate from expensive execution canaries. Changed
content or resolution requires new conformance evidence. Full standalone process
retirement cancels and joins pending inventory work, permanently invalidating that
process generation; it cannot reset or reuse the generation for later admission.

Operator-only sign-in returns an allowlisted HTTPS authorization URL and safe
status. Credentials remain in the fresh private home; status can report the
resulting auth-file digest without returning tokens. A new installation may use
an unfulfilled digest in its private configuration while signing in; turns stay
unavailable until an operator binds the actual digest and restarts both jobs.
Credential-file drift fails closed and requires revalidation. Sign-in requires
explicit provider-network authorization; no ambient account is imported.

## Local Pi/oMLX composition

The `local-engine-only` configuration starts an actual Pi 0.82.0 adapter against
an explicit loopback oMLX endpoint and resident model. It does not load or unload
models or choose a fallback. Credentials come from an owner-private referenced
file or a host-injected credential port. Pi resources and session state are
isolated from ambient configuration. Governed children use the coordinator's
bound, canonical, size-limited read callback; they cannot substitute a model's
claim that a read occurred. Automatic context compaction and bounded in-memory
continuity are implemented; durable Pi resume and manual compaction are not exposed.

An optional `codex-supervisor` manager binding connects the local daemon to the
separate authenticated hosted supervisor. The real Agent 1 coordinator creates
parent and child sessions, approves the sealed read task, dispatches the Pi child,
and requires manager review. Local Pi is not offered as Agent 1. Controlled tests
inject the manager port while retaining the real coordinator, Pi SDK and tool
bindings. That injection does not establish hosted manager conformance.

## Validation limits

Controlled tests exercise real daemon/client sockets, worker processes, manager
callbacks, Pi SDK loops, bounded reads, compaction, interruption, journal races
and descendant reconciliation. Process-group cleanup and bounded observed-process
reconciliation do not prove detection of every unobserved detached process.

The accepted App Server 0.149.0 payload has completed actual text turns and a
second-process thread resume against a local deterministic Responses fixture,
without an account or external provider. Its native child workflow also ran;
tool canaries failed because the command shell aborts during dyld startup. A
paired Seatbelt diagnostic isolates a missing literal root-directory data read.
The inspected native configuration lowers read paths and supported read globs to
recursive grants, so no safe equivalent is currently verified. Production does
not grant recursive root access or enable implicit platform defaults to bypass
this failure. A separately built supplier candidate adds only that literal directory-read rule.
The paired local source baseline reproduces the startup failure; the patched
candidate passes selected primary/native-child shell, project-write, foreign-read
and file-change canaries, including a second-process resume. The candidate is
unaccepted and has distinct hashes, build provenance and ad-hoc signing; it does
not replace the accepted vendor pin. Build recipe and evidence are retained under
this run's `IMPLEMENTATION/CONTAINMENT/NATIVE_POLICY/LITERAL_ROOT_ANALYSIS/CLOSURE/BUILD_FEASIBILITY/CANDIDATE/`.
Separate baseline and patched binaries remain in owned scratch for owner review,
not in this repository. Full conformance and supply acceptance remain outstanding.

Live local Pi validation has completed actual client-to-daemon-to-Pi-to-oMLX
inference, a bounded read and the expected final marker. Both the historical pre-admitted child limb and the subsequent genuine
coordinator-created child limb passed. The latter also verified durable parentage
and required review using an explicitly controlled manager port. A further composed
limb passed with the actual accepted Codex manager binary, authenticated private
supervisor, coordinator and live Pi child. That limb used a trusted no-account
test launch and deterministic manager model; it does not validate hosted login. Successful hosted login, hosted-account manager execution and full native
primary/descendant filesystem, network and process conformance remain unproven.
Approval forwarding passed controlled end-to-end transport tests. The patched
candidate also passed a bounded public HTTP positive control.
The matched public off check also passed. Ask currently fails before producing a
request because exact supplier initialization only connects the approval callback
when managed network requirements exist; a distinct constraint-preserving supplier
candidate source patch is prepared, but its build was interrupted and no second
candidate binary exists. Native-child approval and complete conformance remain
pending; earlier loopback failures do not establish network denial because
private destinations are independently forbidden by supplier policy. Stored consent and configuration readback
must not be presented as kernel enforcement evidence.

`software-workflow.json` registers `npm run typecheck` and `npm test`. Passing
local tests, verifying supply, rendering jobs, or implementing these routes does
not release compatibility holds, resolve Pi source-identity acceptance, adopt App
clients, or establish shared release acceptance.

Current session continuation and exact failed/unexecuted canaries are recorded in
[the Agent 0 handoff](execution/_Coordination/AgentRuns/RUNTIME_EXECUTION_2026-09-06/AGENT0_HANDOFF.md).
This PR preserves an incomplete implementation checkpoint, not a production release.
