# Runtime Engine Contract

Current application: D-GOV-43 topology A2, D-APP-127, D-APP-131 and D-APP-118 (2026-09-22 record reconciliation). The App owns its Runtime service child, which owns the stock, lockfile-pinned Codex App Server. The App is a client of the retained Runtime socket API through its loopback HTTP/SSE renderer channel.

The dated D-APP-56 R4-P24 description of App-local IAgentSdkManager and adapter-side terminal persistence is compatibility history. The live Codex adapter still implements the Runtime-owned AgentEnginePort; the coordinator owns lifecycle/persistence. The browser carrier still uses UIEvent/SSE, including the harness:event bridge; its content preserves the full upstream protocol rather than being limited to the old named-event set. Original method names, identifiers and payloads remain inspectable, subject to structural secret redaction.

The Scope, TurnEngine, Tool Catalog and First Adapter sections below retain first-adapter compatibility detail. Their former “current” assertions apply to that historical subject only, not live Codex qualification or a mandate to restore retired provider/default/policy machinery. The six current sections repaired here retain substantive controls and explicitly separate missing live evidence. No support for the retired @chirality/harness-contract facade remains.

## Scope

This contract defines Chirality's product-owned turn boundary for harness runtime adapters.
It applies to the deterministic stub adapter, the existing direct Anthropic Messages adapter,
and the Claude Agent SDK / Anthropic first-adapter path.

SCA-APP-001 establishes a provider-adapter-general runtime strategy. The Claude Agent SDK
/ Anthropic path remains the first concrete adapter and, per D-APP-18 Option A, the
key-aware default provider: the real `agentSdk` path is selected when an Anthropic API key
is configured and no explicit provider override is set; otherwise the runtime falls back to
`stub`. Concrete non-Anthropic providers require bounded future implementation scope.

The browser-facing event stream remains the stable public contract. Provider and SDK message
names, transcript paths, session IDs, tool names, and permission modes are adapter metadata
unless explicitly mapped into Chirality-owned records.

## AgentEnginePort

The canonical boundary is `projects/chirality-runtime/packages/contracts/src/harness/agent-engine-port.ts`. Its descriptor/preflight, turn execution and interrupt methods remain live interface obligations; the public method yields `UIEvent`. Runtime `codex.notification` and `codex.request` evidence carries upstream parameters through that representation; such source data is not falsely described as provider-neutral.

Known items may have normalized views. Unfamiliar notifications remain inspectable and every server request receives a response, with an explicit unsupported-request outcome where no handler exists. Structural redaction before every persistence/log/artifact/renderer sink remains required and is not established merely by complete forwarding.

Explicit Stop interrupts the Runtime-owned turn. Closing a renderer subscription only unsubscribes; replay/reattachment recovers state and missed activity without sending the original prompt again. Codex thread linkage is retained in the Runtime session record, not an invented App thread index. Native resume is the continuation path; historical v2 records remain readable without a release prerequisite to import or resume them.

Verification hooks: Runtime `tests/codex-supervisor.test.ts`, `tests/app-owned-composition.test.ts`, `tests/turn-registry.test.ts` and App `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. Missing live conformance/redaction checks stay with DEL-03-01/03/04.

## TurnEngine

`frontend/src/lib/harness/turn-engine.ts` owns the product turn lifecycle above the
adapter port. API routes are transport adapters: they parse HTTP, await engine
preflight, format `UIEvent`s as SSE, and delegate cancellation.

Current lifecycle ownership includes:

- same-session active-turn locking;
- session resume and provider API-key preflight;
- runtime option resolution;
- attachment warning and executable attachment shaping;
- persona prompt existence validation;
- subagent governance evaluation and delegated-subagent shaping;
- adapter stream execution through `IAgentSdkManager`;
- engine session metadata persistence on `session:init`;
- mid-stream adapter error mapping to stable `turn:error` and `process:exit` events.

Pre-stream failures remain JSON API errors. Adapter failures after SSE streaming begins
remain browser-visible SSE terminal evidence.

## HarnessEvent Evidence

The Runtime contract source is `projects/chirality-runtime/packages/contracts/src/harness/event-schema.ts`; the canonical session store and turn coordinator are under `projects/chirality-runtime/packages/core/src/`. Runtime owns accepted-input ordering, durable terminal outcomes, append-only records and replay. Browser UIEvent and stored HarnessEvent remain separate carriers without suppressing upstream identity.

Live Codex tool evidence is produced from upstream item notifications and output deltas, with normalized tool views where known. Upstream payloads remain inspectable. Earlier SDK canUseTool/hook wrappers, safe-path-only inputs and the blanket “no raw tool output in HarnessEvent.data” description are compatibility-path observations, not proof of the live path. Actual event redaction is a known implementation/verification residual under D-APP-131 P-12: structural secret protection must happen before every durable, log, artifact and renderer sink. Do not mark that guarantee fulfilled from legacy wrapper tests.

Surviving guarantees include accepted input before execution, truthful durable terminal outcome, unique event identity, malformed-tail recovery, original source/parentage and actual decisions, and no conversion of runtime records into project acceptance. Live native Codex tools follow user-selected Codex policy; application-tool catalog/call validation and domain-stage controls remain separate. A policy label, Full access selection, caller HUMAN string or recorded approval SHA alone proves neither normative authority nor every enforcement boundary.

Verification hooks: Runtime `tests/turn-hardening.test.ts`, `tests/codex-supervisor.test.ts`, `tests/codex-application-tools.test.ts` and current sink-specific secret/replay checks. These hooks do not supply missing results. Retain distinct unknown outcomes and actual adapter/source attribution.

## Agent/Subagent Runtime Contract

The live path uses Codex-native delegation and records the actual native mechanism, parentage, supplied basis, scope, observed decisions and return. Current direct-entry roles are HELP_HUMAN, HELPS_HUMANS and WORKING_ITEMS; TASK is a bounded delegated role and does not delegate. Role instructions and actual host enforcement are different facts; do not describe an unimplemented native depth limit as an enforced guarantee.

D-GOV-43 preserves user Codex configuration and supported native capabilities. Legacy App agent-runtime-contract.ts, SDK tools:[]/maxTurns:1 wrappers and D-APP-09/10 bridge records retain their actual subject; they do not qualify native delegation. Retained Pi compatibility code and earlier experiments do not establish another qualified MVP engine, and the earlier “no Pi dependency or adapter exists” statement is not a current source fact. Codex remains the sole MVP qualification target.

Bounded delegation authorization, scope and capability accountability survive. DEL-03-02/DEL-08-04 still require current per-chat delegation-policy binding/default and interface ownership; parent/child presentation must use recorded relationships, not inference. D-APP-132 leaves the optional D-APP-117 per-attempt replay product unadopted while retaining existing record/replay duties; it creates no universal duplicate store or complete-history promise.

Verification hooks: Runtime `tests/codex-supervisor.test.ts`, current native-parentage/role integration checks and App recorded-descendant presentation checks owned by DEL-08-04/05 and DEL-02-02. Missing live evidence remains explicit.

## Harness Tool Descriptor Contract

Runtime owns the canonical descriptor registry. Current Codex-native tools follow the user's Codex policy and must not be described by a legacy SDK whitelist. Runtime `packages/daemon/src/application-tools.ts` validates Chirality application catalog registration/calls separately; `codex-supervisor.ts` passes policy and registered dynamic tools. The D-APP-132 P-01 release authorizes this distinction, not additional application-tool exposure or waiver of deterministic ordering, domain-stage, secret, human-gate or instruction-root controls.

The following exact descriptor/domain constraints describe retained application-tool/first-adapter surfaces. They do not add a native Codex exposure restriction or qualify an unavailable application operation. Unknown application calls must fail validation; ordering and current live verification remain explicit residuals.


`projects/chirality-runtime/packages/contracts/src/harness/tool-descriptor.ts` defines the Chirality-owned
`HarnessToolDescriptor` registry for SDK built-ins and reserved future tool surfaces.
Descriptors record provider-neutral names, aliases, permissions, path scope, idempotence,
concurrency, interrupt behavior, result-budget policy, provenance events, human-gate
metadata, and adapter tool names.

The retained first-adapter compatibility path exposes requested read-class first-adapter SDK built-ins (`Read`,
`Glob`, `Grep`, and `LS`), requested Chirality MCP read tools, requested
SDK `Write` / `Edit` built-ins, requested SDK `Bash` only in `workspaceWrite` mode,
and requested mutating Chirality MCP tools only in `workspaceWrite` mode after descriptor,
permission-overlay, and handler-wrapper resolution. The retained Chirality application read tools
are `mcp__chirality__status_read`,
`mcp__chirality__deps_read`, `mcp__chirality__scope_scan`, and
`mcp__chirality__scaffold_preview`. D-APP-50 tranche-1 also exposes the
read-side domain transport wrappers `mcp__chirality__domain_completeness_check`
and `mcp__chirality__domain_rule_check_run`; those handlers return DEC-041
in-process read-transport evidence envelopes only and do not produce domain
verdicts, live-binding claims, professional conclusions, shell execution, network
access, or piping writes. The retained mutating Chirality application tools are
`mcp__chirality__status_transition` and `mcp__chirality__deps_write`.
D-APP-50 exposes `mcp__chirality__domain_headless_preview_run` only for the
registered `open_pipe_stress` profile through the final DEC-065 configured-local
`openpipestress-runner solve` process. The handler requires an absolute local
runner path in `CHIRALITY_OPEN_PIPE_STRESS_RUNNER_PATH` and exact lowercase
SHA-256 in `CHIRALITY_OPEN_PIPE_STRESS_RUNNER_SHA256`, verifies the resolved regular executable
immediately before direct foreground spawn, sends the exact complete
project-root-contained `runnerInputRef` bytes to stdin, caps stdout and stderr
independently, and parses one stdout JSON result. The child gets a deliberately
minimal environment; no PATH lookup, shell, network, daemon, telemetry, output
path, SQL/SQLite, proposal, acceptance, or apply path is introduced. The old
`modelInputPath` concept is retired because it represented the provisional
TP-RUNNER-014 model-only fixture rather than the complete DEC-065 request envelope.
`operation_applier.apply` remains unregistered and unexposed.

The SDK options builder passes requested and allowed names through both `tools` and
`allowedTools`, keeps denied and unrequested tool names in `disallowedTools`, attaches
the in-process `chirality` MCP server only when a Chirality MCP descriptor is
allowed, and keeps `canUseTool` attached for explicit hard-deny enforcement. Unknown
`opts.tools` fail structurally before adapter streaming begins.

`MultiEdit`, notebook edits, network, unrestricted subagent capability, and
`mcp__chirality__scaffold_exec` remain
unavailable to the model. Their descriptors remain metadata only until their bounded
implementation, hook, result-storage, and validation tranches land.


Verification hooks: Runtime `tests/codex-application-tools.test.ts`, current descriptor/collision tests and the DEL-06-02 P-01 current obligation. No live check is claimed executed by this record repair.

## Tool Catalog, Naming, Collision Prevention, and Adding Tools

The local/in-process tool boundary is documented by two R6 artifacts:

- `frontend/docs/harness/tool_catalog.md` is generated from
  `HARNESS_TOOL_DESCRIPTORS` and lists descriptor name, adapter name, surface,
  permissions, path scope, modes, idempotence, concurrency, human-gate, hook
  requirements, and model-exposure status.
- `frontend/docs/harness/adding_a_tool.md` records the governed contributor path for
  adding SDK built-ins or in-process Chirality MCP tools without bypassing permission,
  hook, path, redaction, event, or human-gate policy.

Catalog drift is gated by `tool-catalog.test.ts`; descriptor collisions and
descriptor-to-MCP-registration drift are gated by `tool-descriptor.test.ts`.
`createDescriptorLookup` fails closed when two descriptors claim the same normalized name,
alias, or adapter tool name. Same-descriptor canonical/adapter equivalence is permitted
only when it resolves to the same descriptor.

Chirality-owned in-process MCP tools use `mcp__chirality__*` adapter names.
The D-APP-50 read-side wrappers include the two in-process evidence envelopes
and the separately constrained DEC-065 local headless process above. None applies
domain operations, writes piping paths, or advances the tier-0 integration level.
Remote MCP, plugins, broad tool
search, remote execution, provider/network expansion, concrete non-Anthropic
providers, further default/provider semantics changes, and release/professional-boundary
changes remain out of scope until a future human ruling authorizes them.

The R6-04 module split was deferred at closeout because it was optional organization work
and the acceptance criteria were satisfied by the collision invariant, generated catalog,
contributor guide, and this contract refresh without changing MCP exposure or behavior.

## First Adapter Current Posture

`CHIRALITY_HARNESS_PROVIDER=agentSdk` explicitly selects the Claude Agent SDK adapter.
With no explicit provider selection, D-APP-18 Option A applies the key-aware default:
`agentSdk` is selected when an Anthropic API key is configured through the environment or
UI Settings store; otherwise the runtime selects `stub`. Explicit `stub`, `anthropic`, and
`agentSdk` overrides still win over the key-aware default.

Probe posture:

- `@anthropic-ai/claude-agent-sdk` is pinned to `0.3.150`.
- `@anthropic-ai/sdk` is pinned to `0.93.0` to satisfy the SDK peer dependency.
- SDK filesystem settings default to `settingSources: []`.
- `CHIRALITY_SDK_SETTING_SOURCES=project` is the only accepted development override.
- `user` and `local` settings are never passed by the CODEV-001 options builder.
- Requested read built-ins, requested Chirality MCP read tools, requested
  `Write` / `Edit` built-ins, requested `Bash` in `workspaceWrite` mode, and requested
  mutating Chirality MCP tools in `workspaceWrite` mode are exposed
  for the `agentSdk` path after descriptor, permission, handler-wrapper, and hook-policy
  resolution. Denied or unrequested built-ins and MCP tools remain in descriptor-derived
  `disallowedTools`.

Pi is a pattern corpus/reference only. This contract does not authorize a Pi adapter, fork,
package import, Node 22 sidecar, runtime-floor migration, or spike.

## Conformance Gates

The qualification subject is the App client and live Codex adapter against Runtime-owned contracts. D-APP-131 P-08 requires mapping surviving correctness obligations to current contract checks and S-1–S-8: accepted-input ordering, terminal durability, session/request/capability correctness, selected policy, applicable tools, interruption, native continuation, route/stream continuity, full upstream event preservation and structural secret protection.

Use source-valid existing results and execute each missing distinct check. No blanket legacy-suite admission gate or unproved suite equivalence follows; deterministic stub and first-adapter fixtures prove only their named subject. A missing redaction or current adapter result remains a delivery/evidence gap, not a new vote to adopt the already-ruled Codex path.

The evaluator is `projects/chirality-runtime/packages/contracts/src/harness/engine-conformance.ts`. Current verification also includes Runtime `tests/codex-supervisor.test.ts`, `tests/app-owned-composition.test.ts`, `tests/turn-hardening.test.ts`, App turn-registry route tests and the production S-1–S-8 checklist under `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/`. Exact source, actual subject and recorded results are required; file existence is not a pass.

Repeat affected checks when source, configuration or packaging invalidates prior evidence. Signing/notarization integrity and exact-candidate release authorization retain their own controls; record coherence does not release a product or advance lifecycle. DEL-03-01 owns the remaining coverage matrix and current App-client evidence.

## Fallback criteria and reliance-register handoff

Under UPD-113 / D-APP-56 R5 P45, inability to satisfy or verify a
product-critical SDK boundary triggers the K-ENGINE-5 exit path and explicit
residual-risk review; it is not silently accepted. The row-level enforcement,
fallback, and validation crosswalk is maintained in
`docs/harness/reliance_boundary_register.md` (DEL-01-02).
