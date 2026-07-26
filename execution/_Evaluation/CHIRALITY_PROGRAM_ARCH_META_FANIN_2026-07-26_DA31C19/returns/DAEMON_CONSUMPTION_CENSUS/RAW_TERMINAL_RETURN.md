# Shared-runtime daemon consumption census

## Decision-ready conclusion

At frozen basis `da31c19b5656dd74615e308c4215688971d33dc9`, the shared runtime is not merely proposed code:

- The Electron application, packaged CLI, and durable App `AgentRuns` records prove actual daemon use.
- PEC has a concrete shared-runtime client, fail-closed proxy, and tests, but I found no durable record proving a live governed PEC UI-to-daemon run.
- Chirality Piping is not an observed shared-runtime consumer at this basis.
- Root ownership is ruled, but the accepted Root decomposition provides only generic runtime/authority-boundary conformance. Specific continuing duties—contract stewardship, security, compatibility, migration, regression, and release—remain decomposed primarily into App deliverables.

No source, product, governance, evaluation, or Git state was changed.

## Basis and method

- Checkout: `/Users/ryan/dev/chirality-meta-fanin-worktree`
- HEAD: `da31c19b5656dd74615e308c4215688971d33dc9`
- Branch: `codex/chirality-program-architecture-meta-fanin...origin/main`
- Methods: `git rev-parse`, `git status`, bounded `rg`, `find`, `nl`, and `jq` queries over runtime source, App and PEC clients, PRDs, decompositions, decisions, tests, CI, run records, and SOWs.
- Status vocabulary:
  - `OBSERVED`: implemented or durably exercised at the frozen basis.
  - `DECLARED`: stated as architecture/intent, without direct execution evidence found.
  - `UNKNOWN`: the repository does not establish the claim within the reviewed boundary.
- Census agent identity: engine `Codex`; provider `OpenAI`; exact model identity was not exposed to this agent and is `UNKNOWN`.

## 1. Actual and declared consumers

| Consumer | Status | Consumption mode | Evidence |
|---|---|---|---|
| Electron headless daemon host | OBSERVED | `--runtime-daemon` launches the root daemon inside the packaged Electron identity with `safeStorage` credentials | `projects/chirality-app-dev/frontend/electron/main.ts:75,672-691,754-762`; `frontend/electron/runtime-host.ts:419-515`; packaged proof `execution/PKG-09.../DEL-09-04.../_run_records/R6_DAEMON_SERVICE_2026-07-25.md:40-72` |
| Electron GUI / Desktop main process | OBSERVED | Operator-token `RuntimeClient`; project registration; status probing; socket watching and rebinding | `frontend/electron/main.ts:575-644`; `frontend/electron/desktop-project-client.ts:51-118`; `frontend/electron/runtime-connectivity.ts:1-18,183-223` |
| App workflow API and renderer-facing facade | OBSERVED | Next API routes adapt the older Desktop harness contract to shared-runtime session, turn, interrupt, permission, scaffold, and agent routes | `frontend/src/lib/runtime-client/runtime-daemon-harness-port.ts:139-145,428-460`; `frontend/src/app/api/harness/{session,turn,interrupt,permission,scaffold,agents}/`; R2 live proof below |
| Root runtime CLI | OBSERVED | Unix-socket runtime client for status, projects, models, sessions, and Agent 1 runs | `runtime/packages/cli/src/cli.ts:279-428,464`; packaged CLI proof `R6_DAEMON_SERVICE_2026-07-25.md:62-65`; validation `RETURN_G5_VALIDATION.md:13-19` |
| Durable governed App Agent 1→Agent 2 runs | OBSERVED | Daemon-owned Agent 1 run coordination, local-model residency, bounded child tool, interruption, persisted review | Eleven records under `projects/chirality-app-dev/execution/_Coordination/AgentRuns/runtime/*/run.json`; example `0107f526.../run.json:1-48`; `RETURN_G5_VALIDATION.md:3-19` |
| PEC server compatibility client | OBSERVED implementation and tests; live governed use UNKNOWN | Project-token `RuntimeClient`, project binding, daemon status/model status, Agent 1 SSE run; no sidecar fallback | `projects/pec/server/src/shared-runtime-client.ts:1-170`; `server/src/index.ts:15-35`; `server/src/agent-proxy.ts:1-8,99-245`; `server/test/agent-proxy.test.ts:323-344` |
| Chirality Piping | No observed consumer | No direct `@chirality/runtime-*`, `RuntimeClient`, `CHIRALITY_RUNTIME_*`, or `--runtime-daemon` hit found | Targeted scan of `projects/chirality-piping`; D-GOV-20 pilot exclusions at `docs/governance_harness/_DECISIONS/D-GOV-20_shared_runtime_local_agent_pilot.md:47-49` |
| Other future project/domain clients | DECLARED | Registered project clients through runtime contracts and adapters | `runtime/README.md:7-11,27-42`; no concrete additional consumer execution found |

## 2. Current implementation carriers

- Daemon and API:
  - API version and routes: `runtime/packages/contracts/src/protocol.ts:13-40,104`
  - Private socket, operator scopes, token permissions: `runtime/packages/daemon/src/runtime-daemon.ts:49-87`
  - Credential/model/project/session/turn/interrupt/permission routes: `runtime-daemon.ts:146-235,243-331`
  - Health reports API version: `runtime-daemon.ts:334-340`
  - Bearer authentication and scoped authorization: `runtime-daemon.ts:343-352`

- Client transport:
  - Unix-socket client and token handling: `runtime/packages/client/src/client.ts:42-77,101-208`
  - Typed daemon operations: `runtime/packages/client/src/client.ts:211-297`
  - Test proves socket use, token use, and no TCP fallback: `runtime/packages/client/test/client.test.ts:81-145`

- Credentials and project authorization:
  - Runtime service composition: `runtime/packages/core/src/runtime-service.ts:31-75`
  - Project-specific scopes and client token issuance: `runtime-service.ts:78-113`
  - Token/scopes/project restrictions: `runtime/packages/core/src/auth-registry.ts:7-15,43-74,100-133`
  - Concrete encrypted credential carrier remains App composition: `frontend/electron/runtime-host.ts:419-450`

- Sessions:
  - Central daemon session records: `runtime/packages/core/src/session-store.ts:22-59`
  - Legacy visibility and normalization: `session-store.ts:62-79,272-320`
  - Non-destructive central migration with copied event log: `session-store.ts:223-269`

- Delegation and tools:
  - Durable Agent 1 run record and manager hooks: `runtime/packages/core/src/agent1-run-coordinator.ts:18-121`
  - Agent 1 validation and run persistence: `agent1-run-coordinator.ts:123-199`
  - Exactly one authorized local Agent 2, explicit residency and bounded `read_file` tool: `agent1-run-coordinator.ts:208-310`

- Turn locks and interruption:
  - Per-session single-active-turn enforcement and authorization: `runtime/packages/core/src/turn-coordinator.ts:70-116`
  - Turn and interrupt HTTP/SSE routes: `runtime-daemon.ts:288-331`
  - Client stream cancellation: `runtime/packages/client/test/client.test.ts:190-216`

- Model residency:
  - Exact-model admission and fail-closed transition handling: `runtime/packages/core/src/residency-coordinator.ts:24-95`
  - Explicit drain/unload/load activation sequence: `residency-coordinator.ts:98+`

## 3. Governed evidence of actual daemon use

The strongest evidence is not tests or source code:

1. `RETURN_G5_VALIDATION.md:3-19` records:

   - Runtime validation at 43/43.
   - Packaged CLI querying the daemon.
   - Live oMLX activation for two local models.
   - Successful bounded reads, interruption, missing-tool fail-closed behavior.
   - A final governed Agent 1→Agent 2 run.

2. `R6_DAEMON_SERVICE_2026-07-25.md:40-72` records:

   - Isolated packaged headless daemon startup.
   - `safeStorage` encryption/decryption and corrupt-ciphertext negative control.
   - LaunchAgent lifecycle.
   - Packaged CLI project-status query.
   - Packaged GUI end-to-end stub turn with zero exit.

3. `R2_DAEMON_SERVICE_2026-07-25.md:21-52` records:

   - GUI rebinding to the daemon.
   - A stub-adapter turn through the service boundary.
   - Real daemon sessions and events.
   - Daemon-side session state, with only governed evidence retained after the temporary environment was removed.

4. Eleven durable run records exist under `AgentRuns/runtime/`:

   - 6 `completed`
   - 3 `failed`
   - 2 `interrupted`
   - All 11 identify `WORKING_ITEMS` as manager.
   - Manager selection is `stub/stub/haiku`.
   - Child selections use `pi/omlx` with either `Qwen3.6-35B-A3B-8bit` or `Qwen3.5-122B-A10B-4bit`.
   - All six completed runs record a human/manager review decision of `rejected`.

That last fact does not erase execution proof: it shows the daemon carried governed runs and preserved their non-acceptance rather than manufacturing success.

## 4. Degraded mode and version incompatibility

### Observed behavior

- App missing/disconnected runtime:
  - API boundary returns typed `503 ENGINE_UNAVAILABLE`: `frontend/src/__tests__/api/harness/daemon-proxy-boundary.test.ts:42-63`.
  - Desktop supervisor retries probes and rebinds after availability transitions: `frontend/electron/runtime-connectivity.ts:13-16,183-223`.
  - Socket watcher never makes startup fatal and degrades to polling: `frontend/electron/runtime-socket-watch.ts:1-35,77-84`.
  - There is no alternate in-process agent execution loop on this path.

- PEC missing runtime:
  - Agent routes fail closed when runtime client configuration is absent: `projects/pec/server/src/index.ts:15-35`.
  - Proxy explicitly has no sidecar fallback: `projects/pec/server/src/agent-proxy.ts:1-8`.
  - Daemon failure returns `503` without PEC state mutation: `server/test/agent-proxy.test.ts:323-344`.
  - This matches D-T0-23’s fail-closed boundary: `_DomainEngines/_DECISIONS/D-T0-23_shared_runtime_cross_loop_effects.md:22-30`.

- Known packaged residuals:
  - SIGKILL can leave a stale socket, although recovery was demonstrated.
  - Login auto-start remained untested.
  - Release-quality premerge and deployment evidence remained outstanding.
  - See `R6_DAEMON_SERVICE_2026-07-25.md:94-147`.

### Unknown / missing behavior

- Runtime API version is fixed at `v1`: `runtime/packages/contracts/src/protocol.ts:13`; the daemon exposes it at `runtime-daemon.ts:334-340`.
- I found no client-side comparison that refuses or negotiates an incompatible daemon API version.
- I found no explicit upgrade/downgrade compatibility matrix or version-mismatch test across runtime, App, or PEC.
- `CompatibilitySessionPolicy` is engine/credential selection logic, not protocol-version negotiation: `runtime/packages/core/src/compatibility-session-policy.ts:14-56`.
- Actual degraded behavior for an old App against a newer daemon, or vice versa, is therefore `UNKNOWN`.
- Actual live PEC UI-to-daemon consumption and degraded recovery are also `UNKNOWN`; source and tests alone do not establish a governed live PEC run.

## 5. Ownership and duty loci

### Ruled ownership

Root ownership is clear in:

- `docs/governance_harness/_DECISIONS/D-GOV-20_shared_runtime_local_agent_pilot.md:18-53`
- `_DomainEngines/_DECISIONS/D-T0-23_shared_runtime_cross_loop_effects.md:12-30`
- `AGENTS.md:264-277`
- App PRD amendment `projects/chirality-app-dev/docs/PRD.md:1692-1720`

These establish the generic Root runtime, one daemon, App/PEC as clients, preserved project authority, operational-only daemon state, and separately bounded security/regression work.

### Decomposed loci at the frozen basis

| Duty | Current decomposed locus | Root-specific standing locus |
|---|---|---|
| Runtime contract and conformance | App `DEL-03-01` | Root `DEL-02-02` covers only generic three-layer authority-boundary conformance |
| API/SSE compatibility and fallback | App `DEL-03-03`, `DEL-04-01` | None specific found |
| Credential/security/network boundaries | App `DEL-04-05`, `DEL-06-*` | None specific found |
| Session/event migration and replay | App `DEL-05-*` | None specific found |
| Turn locks, interruption, tool controls | App `DEL-03-02`, `DEL-03-04`, `DEL-06-*` | Root delegation/write-scope controls are generic, not daemon stewardship |
| Regression and pilot validation | App `DEL-09-*` | None specific found |
| Packaging, deployment, release proof | App `DEL-09-*` | Root public-export boundary exists, but not shared-runtime release stewardship |
| Runtime authority separation | Root `SOW-027 → DEL-02-02` | Yes, expressly generic; “no implementation change implied” |

Exact Root anchors:

- Scope: `execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv:27-30`
- Deliverables: `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv:10-13`
- `DEL-02-02` says “no implementation change implied.”

Exact App duty inventory:

- `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md:297-367`
- SCA duty map: `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-003.../Execution_Deliverable_Impact.csv:1-21`

The accepted App decomposition also says App deliverables “retain semantic ownership” at `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md:603-614`, especially line 611. That differs from the ruled Root-owner/App-client posture. This census records the location mismatch; it does not independently assign severity or amend either instrument.

## 6. Coverage and limitations

Covered:

- Root runtime contracts, daemon, client, CLI, core coordinators.
- Electron daemon composition and GUI client.
- App API facade, connectivity supervisor, tests, CI, and governed run records.
- PEC shared-runtime client/proxy/tests and its governing decisions.
- Root/App PRDs, decompositions, SOWs, D-GOV-20, D-T0-23, and App runtime decisions.
- Targeted Piping search for direct shared-runtime use.

Not established:

- Live external-user daemon telemetry.
- Actual PEC governed live-use receipt.
- Any shared-runtime use by Piping.
- Protocol-version mismatch behavior.
- Login auto-start and deployment behavior beyond recorded residuals.
- Whether any untracked or non-file operational state survived.
- Product acceptance: the census observes use and duty locations; it does not accept them.

## 7. CSV-ready census

```csv
Consumer,ComponentPath,ConsumptionMode,Status,ActualUseEvidence,PrimaryAnchors,KeyUnknown
Electron headless daemon,projects/chirality-app-dev/frontend/electron/main.ts,Packaged --runtime-daemon host with safeStorage identity,OBSERVED,Packaged startup and credential/lifecycle proof,R6_DAEMON_SERVICE_2026-07-25.md:40-72;frontend/electron/runtime-host.ts:419-515,Login auto-start and deployment remain unproven
Electron GUI,projects/chirality-app-dev/frontend/electron/main.ts,Operator RuntimeClient plus project binding and reconnect,OBSERVED,Packaged GUI stub turn and daemon rebind proof,main.ts:575-644;runtime-connectivity.ts:183-223;R2_DAEMON_SERVICE_2026-07-25.md:21-52,Old-client/new-daemon compatibility unknown
App workflow API,projects/chirality-app-dev/frontend/src/app/api/harness,Shared-runtime compatibility facade for sessions turns interruption permission scaffold agents,OBSERVED,Daemon-backed API and GUI evidence,runtime-daemon-harness-port.ts:139-145,428-460;R2_DAEMON_SERVICE_2026-07-25.md:21-52,No explicit protocol-version refusal
Runtime CLI,runtime/packages/cli/src/cli.ts,Unix-socket client for daemon project model session and Agent1 commands,OBSERVED,Packaged CLI queried daemon,cli.ts:279-428,464;RETURN_G5_VALIDATION.md:13-19,None material for observed query
Governed AgentRuns,projects/chirality-app-dev/execution/_Coordination/AgentRuns/runtime,Daemon Agent1 to local Agent2 with tool and residency evidence,OBSERVED,11 durable runs: 6 completed 3 failed 2 interrupted,AgentRuns/runtime/*/run.json;RETURN_G5_VALIDATION.md:3-19,All completed runs were rejected rather than accepted
PEC server,projects/pec/server/src/shared-runtime-client.ts,Project-token daemon client and one-cycle SSE proxy,OBSERVED,Implementation and fail-closed tests only,shared-runtime-client.ts:1-170;agent-proxy.ts:1-245;agent-proxy.test.ts:323-344,Live governed PEC UI-to-daemon use not found
Chirality Piping,projects/chirality-piping,None found,UNKNOWN,No direct shared-runtime references found,D-GOV-20:47-49;targeted repository scan,Not an observed consumer at freeze
Future project/domain adapters,runtime/packages/core/src/project-registry.ts,Registered project clients through shared contracts,DECLARED,No additional concrete consumer run found,runtime/README.md:7-11,27-42,Actual consumers and compatibility behavior unknown
```

