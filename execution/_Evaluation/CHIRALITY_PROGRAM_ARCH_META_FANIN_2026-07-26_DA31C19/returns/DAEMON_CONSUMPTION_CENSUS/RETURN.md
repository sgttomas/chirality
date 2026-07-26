# Shared-Runtime Daemon Consumption Census

RUN_STATUS: `PASS_WITH_UNKNOWNS`

This is the EVALUATION-manager filing of a read-only Agent 2 terminal return.
The evidence child changed no file or Git state.

## Basis and method

- Checkout: `/Users/ryan/dev/chirality-meta-fanin-worktree`
- HEAD: `da31c19b5656dd74615e308c4215688971d33dc9`
- Methods: bounded `git`, `rg`, `find`, `nl`, and `jq` queries over runtime
  source, clients, PRDs, decompositions, decisions, tests, CI, run records,
  and SOWs
- Runtime: Codex / OpenAI / exact model `UNKNOWN`

`OBSERVED` means implemented or durably exercised; `DECLARED` means stated
without direct execution evidence; `UNKNOWN` means the reviewed repository
boundary does not establish the claim.

## Decision-relevant observations

- The Electron application, packaged CLI, and durable App `AgentRuns` prove
  actual daemon use.
- PEC has a concrete client, fail-closed proxy, and tests, but no durable
  record was found proving a live governed PEC UI-to-daemon run.
- Piping is not an observed shared-runtime consumer at this basis.
- Root ownership is ruled, but the accepted Root decomposition supplies only
  generic runtime/authority-boundary conformance. Specific continuing duties
  remain decomposed primarily into App deliverables.

These are basis observations, not product judgments.

## Consumers and evidence

| Consumer | Status | Evidence |
|---|---|---|
| Electron headless daemon host | OBSERVED | `projects/chirality-app-dev/frontend/electron/main.ts:75,672-691,754-762`; `frontend/electron/runtime-host.ts:419-515`; `R6_DAEMON_SERVICE_2026-07-25.md:40-72` |
| Electron GUI / desktop process | OBSERVED | `frontend/electron/main.ts:575-644`; `frontend/electron/desktop-project-client.ts:51-118`; `frontend/electron/runtime-connectivity.ts:1-18,183-223` |
| App workflow API | OBSERVED | `frontend/src/lib/runtime-client/runtime-daemon-harness-port.ts:139-145,428-460`; `frontend/src/app/api/harness/{session,turn,interrupt,permission,scaffold,agents}/` |
| Root runtime CLI | OBSERVED | `runtime/packages/cli/src/cli.ts:279-428,464`; `R6_DAEMON_SERVICE_2026-07-25.md:62-65`; `RETURN_G5_VALIDATION.md:13-19` |
| App Agent 1→Agent 2 runs | OBSERVED | Eleven `projects/chirality-app-dev/execution/_Coordination/AgentRuns/runtime/*/run.json` records; `RETURN_G5_VALIDATION.md:3-19` |
| PEC server client | OBSERVED implementation/tests; live governed use UNKNOWN | `projects/pec/server/src/shared-runtime-client.ts:1-170`; `server/src/index.ts:15-35`; `server/src/agent-proxy.ts:1-8,99-245`; `server/test/agent-proxy.test.ts:323-344` |
| Piping | UNKNOWN / no observed consumer | Targeted `projects/chirality-piping` scan; D-GOV-20 pilot exclusions at lines 47-49 |
| Future project/domain clients | DECLARED | `runtime/README.md:7-11,27-42`; no further concrete run found |

## Implementation carriers

- Protocol and routes:
  `runtime/packages/contracts/src/protocol.ts:13-40,104`
- Socket, permissions, authorization, and daemon routes:
  `runtime/packages/daemon/src/runtime-daemon.ts:49-87,146-235,243-352`
- Unix-socket client and typed operations:
  `runtime/packages/client/src/client.ts:42-77,101-297`
- No-TCP-fallback test:
  `runtime/packages/client/test/client.test.ts:81-145`
- Runtime composition, project scopes, and client tokens:
  `runtime/packages/core/src/runtime-service.ts:31-113`
- Token, scope, and project restrictions:
  `runtime/packages/core/src/auth-registry.ts:7-15,43-74,100-133`
- Concrete encrypted credential carrier:
  `projects/chirality-app-dev/frontend/electron/runtime-host.ts:419-450`
- Sessions and non-destructive migration:
  `runtime/packages/core/src/session-store.ts:22-79,223-320`
- Agent 1 run coordination and one bounded Agent 2:
  `runtime/packages/core/src/agent1-run-coordinator.ts:18-310`
- Turn lock and authorization:
  `runtime/packages/core/src/turn-coordinator.ts:70-116`
- Interrupt/cancellation:
  `runtime/packages/daemon/src/runtime-daemon.ts:288-331`;
  `runtime/packages/client/test/client.test.ts:190-216`
- Model admission and fail-closed residency:
  `runtime/packages/core/src/residency-coordinator.ts:24-95`

## Durable evidence of use

1. `RETURN_G5_VALIDATION.md:3-19` records 43/43 runtime validation, packaged
   CLI use, live oMLX activation, bounded reads, interruption, missing-tool
   fail-closed behavior, and a governed Agent 1→Agent 2 run.
2. `R6_DAEMON_SERVICE_2026-07-25.md:40-72` records packaged daemon startup,
   `safeStorage` encryption/decryption, a corrupt-ciphertext negative control,
   LaunchAgent lifecycle, CLI status, and a GUI stub turn.
3. `R2_DAEMON_SERVICE_2026-07-25.md:21-52` records GUI rebinding, a
   service-boundary stub turn, real daemon sessions/events, and governed
   evidence retained after removal of the temporary environment.
4. Eleven runtime run records comprise six completed, three failed, and two
   interrupted runs. All identify `WORKING_ITEMS`; all six completed runs
   record the review decision as `rejected`, preserving non-acceptance rather
   than manufacturing success.

## Degraded and incompatible-version behavior

Observed:

- App absence/disconnection returns typed `503 ENGINE_UNAVAILABLE`:
  `frontend/src/__tests__/api/harness/daemon-proxy-boundary.test.ts:42-63`.
- The desktop supervisor retries and rebinds:
  `frontend/electron/runtime-connectivity.ts:13-16,183-223`.
- Socket watching degrades to polling without fatal startup:
  `frontend/electron/runtime-socket-watch.ts:1-35,77-84`.
- PEC fails closed without client configuration, has no sidecar fallback, and
  returns `503` without mutation:
  `projects/pec/server/src/index.ts:15-35`;
  `server/src/agent-proxy.ts:1-8`;
  `server/test/agent-proxy.test.ts:323-344`.
- Recorded residuals include stale socket after SIGKILL, untested login
  auto-start, and outstanding release/deployment evidence:
  `R6_DAEMON_SERVICE_2026-07-25.md:94-147`.

Unknown:

- API version is fixed at `v1`
  (`runtime/packages/contracts/src/protocol.ts:13`) and exposed in daemon
  health (`runtime-daemon.ts:334-340`), but no incompatibility refusal,
  negotiation, or upgrade/downgrade matrix was found.
- `CompatibilitySessionPolicy` selects engine/credential compatibility rather
  than protocol negotiation:
  `runtime/packages/core/src/compatibility-session-policy.ts:14-56`.
- Old-App/new-daemon behavior, new-App/old-daemon behavior, and live governed
  PEC degraded recovery remain `UNKNOWN`.

## Ownership and decomposed duty loci

Ruled Root ownership appears in:

- `docs/governance_harness/_DECISIONS/D-GOV-20_shared_runtime_local_agent_pilot.md:18-53`
- `_DomainEngines/_DECISIONS/D-T0-23_shared_runtime_cross_loop_effects.md:12-30`
- `AGENTS.md:264-277`
- `projects/chirality-app-dev/docs/PRD.md:1692-1720`

| Duty | Current locus | Root-specific standing locus |
|---|---|---|
| Contract and conformance | App `DEL-03-01` | Root `DEL-02-02` covers generic authority-boundary conformance |
| API/SSE compatibility and fallback | App `DEL-03-03`, `DEL-04-01` | None specific found |
| Credential/security/network boundaries | App `DEL-04-05`, `DEL-06-*` | None specific found |
| Session/event migration and replay | App `DEL-05-*` | None specific found |
| Locks, interruption, and tools | App `DEL-03-02`, `DEL-03-04`, `DEL-06-*` | Root controls are generic rather than daemon stewardship |
| Regression and pilot validation | App `DEL-09-*` | None specific found |
| Packaging and release proof | App `DEL-09-*` | Root export boundary exists, not runtime release stewardship |
| Runtime authority separation | Root `SOW-027 → DEL-02-02` | Yes; expressly generic and says no implementation change is implied |

Root anchors:

- `execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv:27-30`
- `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv:10-13`

App anchors:

- `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md:297-367`
- `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-003.../Execution_Deliverable_Impact.csv:1-21`

The accepted App decomposition says App deliverables retain semantic ownership
at lines 603-614, especially line 611. This differs from the ruled
Root-owner/App-client posture. The census records the mismatch without
assigning severity.

## Coverage and limitations

Covered Root runtime code; Electron/App clients; App API, tests, CI, and run
records; PEC client/proxy/tests; Root/App instruments; and a targeted Piping
scan.

Not established: external-user telemetry, a governed PEC live-use receipt,
Piping consumption, protocol-version mismatch behavior, full login/deployment
behavior, untracked operational state, or product acceptance.

