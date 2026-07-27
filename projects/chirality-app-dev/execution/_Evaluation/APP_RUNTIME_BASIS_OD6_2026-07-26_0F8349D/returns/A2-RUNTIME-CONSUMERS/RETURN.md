# A2-RUNTIME-CONSUMERS terminal return

- **Basis:** `0f8349d90f58c1e6b3339263f5aafaf36e783a7e`
- **Mode:** read-only ephemeral Agent 2
- **Repository writes:** none
- **Runtime/network execution:** none

## Runtime topology established from current source

The App is both the packaged provider of the one per-user daemon and a client
of it, but those roles are separate process postures. Normal Electron startup
constructs an operator `RuntimeClient`, resolves a project-scoped binding,
supervises reconnection, and exposes lifecycle/UI controls. The
`--runtime-daemon` posture instead starts the Root runtime host, which creates
the daemon-owned credential store, project registry, session store, auth,
engines, residency, and coordinator.

The App HTTP workflow API is a compatibility client, not a second runtime.
Exactly ten production routes call `getDaemonHarnessPort()`. The port has no
in-process runtime fallback and returns 503/`ENGINE_UNAVAILABLE` when unbound.
It performs App-side mappings while all engine/session/permission singleton
state remains in the daemon.

Electron main validates the App project registration and resolves a private
project token before binding. The renderer-facing process receives only the
project-scoped binding. Credentials are stored by the daemon-host process
through Electron `safeStorage`; environment credentials are read-only
compatibility sources.

The packaged CLI is a second operator client to the same daemon. It is bundled
separately and launched through the packaged Electron executable.

PEC is the only other production-code consumer found. Its server imports Root
runtime client/contracts, requires a private project token, rejects operator
tokens, revalidates PEC registration/drift/adapters, and streams project runs.
Only two scratch/demo agent routes currently use the seam; missing
configuration fails those routes closed while the deterministic server may
continue. The code forbids fallback to the retired sidecar.

Chirality Piping is not a Root-runtime client at this basis. Its desktop
capability explicitly reports `daemon_required: false`. No other production
RuntimeClient/socket consumer was found.

## Governed consumption evidence

Historical shared-runtime pilot evidence carried at this basis includes Root,
App, and PEC test suites plus live App-project oMLX and governed delegated
runs. It was not rerun at this basis. PEC's evidence is test/build evidence,
not a governed live PEC daemon consumption proof.

The later packaged-daemon drill proves daemon-mode `safeStorage`, App project
binding, and an App HTTP route through the daemon client, UDS, session store,
stub engine, and SSE without worktree writes. It also records a residual:
Finder/LaunchServices activation can resolve to the daemon under the shared
bundle identity. Current recovery retires/restarts and reconnects; a separate
helper identity remains undecided.

No governed live PEC `/agent/messages` or `runAgent1` execution was found.
Operational PEC consumption therefore remains UNKNOWN.

## Degraded mode

- App GUI startup tolerates daemon absence and retries binding, while
  agent/session routes fail closed. There is no in-process execution fallback.
- PEC deterministic APIs may continue while its scratch/demo agent routes fail
  closed; this is code/test supported, not live-production supported.
- Piping is independent, not a degraded shared-runtime mode.

No complete product-level degraded-mode capability matrix was found. Claims
beyond the narrow fail-closed behavior remain UNKNOWN.

## Version compatibility

The wire API is compile-time `v1`. App host and client source are bundled from
the same checkout, providing strong same-build coherence. PEC is independently
deployed and may encounter a separately installed App daemon.

A source search found zero client-side `RUNTIME_API_VERSION` or `apiVersion`
checks in Root client/CLI, App runtime-client/Electron, or PEC server code.
The daemon reports the value but clients neither negotiate nor reject an
incompatible version. Project-manifest hashes validate registration, not
runtime-contract compatibility. Cross-release compatibility is UNKNOWN.

## Machine-readable census

```csv
ConsumerID,Surface,Class,Interface,ObservedAtBasis,GovernedLiveEvidence,Limit
APP-HOST,"App electron/main.ts; electron/runtime-host.ts","packaged daemon provider","--runtime-daemon -> RuntimeDaemon /v1 UDS",YES,"historical pilot and packaged drills","not rerun at basis; bundle identity residual"
APP-GUI,"App electron/main.ts; desktop-project-client.ts","operator plus project binder","RuntimeClient UDS and Electron IPC",YES,PARTIAL,"not every renderer workflow or mid-turn restart"
APP-WORKFLOW-API,"App src/app/api/harness routes; runtime-client","project compatibility client","10 routes -> DaemonHarnessPort -> RuntimeClient",YES,YES,"V9 used stub engine; not every route"
APP-RENDERER-CONTROL,"preload.ts; runtime-settings.tsx","human UI control client","renderer IPC -> operator client/lifecycle",YES,PARTIAL,"no complete degraded-mode UX contract"
APP-CLI,"electron/cli-launcher.ts; Root CLI","operator client","bundled CLI -> RuntimeClient /v1",YES,YES,"no cross-version negotiation"
PEC-SERVER,"PEC shared-runtime-client.ts; agent-proxy.ts; api.ts","project external client","RuntimeClient /v1 Agent1 SSE",YES,NO,"scratch/demo only; no governed live PEC run"
PIPING-LOCAL,"Piping Tauri lib.rs","non-consumer","none; daemon_required=false",YES,NOT_APPLICABLE,"does not test shared runtime"
OTHER-PROJECTS,"projects excluding App and PEC","no production consumer found","none",YES,NO,"basis-scoped absence"
TEST-FAKES,"Root/App/PEC tests","validation only","fakes and test clients",YES,NO,"definitions are not runtime consumption"
```

## Reproduced counts

```text
App production routes using getDaemonHarnessPort=10
project manifests=2 (App and PEC)
other-project production runtime-client/socket hits=0
consumer-side RUNTIME_API_VERSION/apiVersion checks=0
PEC focused runtime test definitions=12
App focused runtime boundary/control test definitions=29
Root runtime test files=59
```

## Owner alternatives

1. Retain one-daemon posture, require one governed live PEC client run before
   operational reliance, and add an explicit daemon/client compatibility
   assertion with fail-closed actionable errors.
2. Alternatively accept coordinated mono-checkout releases without a wire
   handshake, record that as a release constraint, and require an
   App-daemon/PEC-client matrix for every runtime change.
3. Adopt a small per-client degraded-mode capability matrix, or avoid general
   degraded-mode claims and retain only the narrow tested fail-closed facts.
4. Decide separate helper-bundle identity independently; current behavior is
   self-healing but does not fully separate GUI and daemon identity.

## Rerun triggers

Rerun after Root protocol/client/daemon/auth/session changes; App packaging,
daemon lifecycle, CLI, or safeStorage changes; project manifest/token binding
changes; PEC operational-use claims; new project manifests or production
runtime-client imports; API/package version changes; new degraded-mode or
cross-version claims; or helper-bundle separation.
