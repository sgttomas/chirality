# Runtime implementation audit — 2026-09-06

Author: OpenAI GPT-6; exact serving model id unavailable. Ephemeral Agent 2, instruction-asserted role, not mechanically enforced. Read-only product/contract audit; no delegation. Source inventory pins the inspected baseline. No implementation acceptance or hold disposition is claimed.

## Finding

The inherited runtime is a working v1 daemon/core/client library, not an implemented Codex v2 runtime. Its full existing regression suite passes 79 tests across nine files in an isolated copied workspace; typecheck and build pass. The accepted DEL-02-07 through 12 targets add substantial functionality absent from the inspected source. Passing the inherited suite does not establish those newer requirements.

## Source-cited gap matrix

Paths below are Runtime-relative unless stated otherwise. Requirement references refer to each accepted carrier ScopeOfWork.md under execution/PKG-02_Runtime_Product/1_Working/.

| Carrier | Existing implementation/evidence | Missing target / assessment |
|---|---|---|
| DEL-02-06 stewardship | Seven packages, real daemon lifecycle/auth/session/turn/model machinery; contracts preserve v1 consumers. | Accepted implementation/source/release fan-in is still distinct from diagnostics. Nine holds are not resolved by this audit. |
| DEL-02-07 REQ-001..008 | packages/daemon/src/runtime-daemon.ts has authenticated private Unix broker, daemon-generation fencing and bounded shutdown; tests/daemon.test.ts exercises ownership, restart, SSE cancellation and residual cleanup. | No DelegatedHarnessProcessSupervisorPort, second purpose-limited socket, worker token owner/generation binding, acquisition/reconnect inventory, or second launch job. Daemon-generation safety is not worker-generation safety. |
| DEL-02-08 CLM-002..004 | package-lock.json pins installed tooling; historical R15 accepts exact App Server 0.149.0 G2 asset identities; sdk-version.ts pins historical Claude SDK contract. | No Codex supply verifier/package or generated protocol surface in software. G2 accepted generated-schema/type gaps; not proof the protocol is absent. TM-ROOT-106 is separate Pi 0.80.10 authority versus 0.82.0 executable/family identity, not a missing Codex version choice. |
| DEL-02-09 REQ-001..006 | AuthRegistry implements runtime client bearer scopes; SessionStore records project root and engine selection. | No HostedEngineConsentPort, root-private Codex home/account epoch binding, K-ROLE-2 digest, three-posture consent state or drift invalidation. Client auth does not substitute for hosted account consent. |
| DEL-02-10 CLM-001..005 | AgentEnginePort provides preflight/startTurn/interrupt; PermissionDecisionRequest at contracts/src/protocol.ts:89 is requestId + allow/deny + optional reason; harness/event-schema.ts is schemaVersion1 and named terminal types. | No versioned v2 event discriminated payload validation, attributed decision record or networkApprovalContext/session-grant model. RuntimeService.createSession (~163) rejects all explicit Agent2 and listAgents(directChatOnly) excludes Type2; this must be changed deliberately for Codex-labelled fallback, without weakening existing managed-delegation paths. |
| DEL-02-11 CLM-001..003 | TurnCoordinator validates one terminal and persists canonical completion/failure; daemon handles drain/crash-adjacent cancellation. | No WorkerRetirementCoordinatorPort, durable prepared/committed/reconciliation-required journal, worker-crash reconciliation or four-field root/account/policy/cwd continuity resume decision. In-memory active turn map is not crash-persistent worker retirement. |
| DEL-02-12 CLM-001..005 | tests/ contains seven suites, packages/*/test two further suites; existing v1 conformance helpers and truthful accepted compatibility history exist. | No new Codex conformance matrix/source identity bound to accepted new implementation, exact-pin three-posture empirical proof or client G5/G7 fan-in. Diagnostics cannot provide accountable-human acts. |

Only engine-claude (injected ClaudeTurnRuntimePort) and engine-pi-omlx packages exist. There is no engine-codex package. The daemon package exports a library, while CLI daemon install accepts a caller-provided executable; the production composition/host currently belongs to the App integration. Standalone runtime ownership therefore needs an explicit composition entry to exercise its new worker path end to end.

## Concrete implementation tranche

Implement actual state machines and transports, not declaration-only placeholders:

1. Add additive v2 contracts under packages/contracts/src/v2/: exact supply manifest, supervisor acquire/inventory/reconnect/retire requests, attributed approvals and closed terminal events, continuity tuple, consent and role-evidence records. Keep current v1 public contracts working for existing clients until their separate integration.
2. Add packages/core/src hosted-consent store and retirement coordinator. Persist consent under canonical-root/account-epoch/policy digest; default command network off; reject stale grants; validate explicit user session acceptance. Retirement uses durable prepared/committed/reconciliation-required journal and idempotent terminalization. Resume only on all four continuity values; otherwise fresh thread, no replay.
3. Add actual private Unix supervisor server/client and worker process manager in a new supervisor package. Each request validates token plus socket owner and worker generation; stale recovery invalidates tokens; reconnect cannot adopt a foreign generation. The daemon is the only client of this purpose-limited endpoint; no renderer/CLI route to it.
4. Add isolated executable worker fixtures and real transport/process integration tests. Exercise start/acquire, inventory, reconnect, generation mismatch, process kill, restart/journal recovery, exactly-one terminal, consent drift and unknown payload rejection. Add a daemon composition smoke harness that runs this full path with controlled workers without account/login/network or changing launchctl state.
5. Add supply verifier and exact-pin adapter incrementally from accepted observed method evidence; reject mismatched executable bytes before launch. Do not implement guessed method payloads from current generic documentation. Pin-specific JSON-lines traffic tests and runtime API v2 fixtures can be produced offline; keep any actual provider/auth claim unavailable until measured.
6. Add two-job launch rendering tests and standalone configuration/composition documentation. Rendering is testable without installing jobs. Existing CLI/client v1 regression suite remains required.

Recommended project profile: isolated Node24.18.0 (satisfies package >=22.19), npm/workspace lock, TypeScript5.9.3 and Vitest3.2.7; temporary directories and Unix sockets only; scratch-owned binaries/fixtures; no ambient CODEX_HOME, account state, network, operational registry, launchctl installation or provider calls. Every subprocess test must prove teardown. Coverage is requirement-specific, not a proxy percentage. Parent must reconcile this candidate with the specification manager graph before dispatch.

## Exact supply/protocol distinction and remaining owner-dependent work

Historical repository paths:

- plans/steers/chirality_app_v3_root_ruling_record_r15_2026-08-25.md accepts G2 candidate at baa29d22fa034784cda221b2929061213e83ec91 with documented gaps and G5 signature finding.
- plans/steers/chirality_app_v3_r16_g05_and_spikes_steer_root_2026-08-27.md:91 pins rust-v0.149.0 macOS arm64. Payload SHA256 b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2. No new version selection is needed.
- execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-08_Exact_Supply_and_Protocol_Pinning/_run_records/APP-SERVER-0.149.0-G2-CANDIDATE-2026-08-24/03_EMPIRICAL_EVIDENCE/SCHEMA_TYPES_GAPS.md records actual generate-json-schema and generate-ts probes, both exit2 unexpected argument. All three allowed assets omit the codex wrapper needed for documented generators. This is an artifact-boundary evidence gap, not a conclusion that protocol methods do not exist or that probes were never attempted.
- The companion METHOD_CONFIG_FEATURE_MATRIX.md is observed bounded method evidence, and R16 records features.plugins=false with two isolated runs suppressing observed plugin startup attempts.

New owner intervention is not needed merely to diagnose or design isolated code under the current directive. Actual hosted account login/consent, empirical authenticated provider traffic, client adoption, cutover and release require their concrete named acts/evidence. Do not ask for a Codex version choice already ruled. An additional wrapper artifact, if required to produce exhaustive schema, needs its own scope decision rather than silent substitution. Invalid vendor signature and Pi G1 mismatch remain separately routed issues. No current binary was downloaded or executed by this audit.

## Measurement calibration

CHECKS.json and raw logs give actual commands. Initial scratch construction omitted top-level tests, so its29-test PASS was partial; final copy included them and all79 passed. Initial sandbox denied Unix socket listen with EPERM; isolated execution outside that sandbox passed with scratch TMPDIR. An accidental build invocation at repository root was not treated as evidence; corrected scratch build passed. No source/status/contract changes were made. No inference of conformance acceptance follows from test success.
