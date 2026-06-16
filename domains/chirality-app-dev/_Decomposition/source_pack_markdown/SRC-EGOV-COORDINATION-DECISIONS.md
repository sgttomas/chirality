# Source Pack: SRC-EGOV-COORDINATION-DECISIONS

Grouping: `GROUPED_FOLDER`  RepoGlob: `execution/_Coordination/_DECISIONS/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/_Coordination/_DECISIONS/D-APP-01_RULING_2026-06-13.md

### D-APP-01 Ruling

**Status:** RULED
**Date:** 2026-06-13
**Decision:** Pi posture for Chirality App Dev
**Ruling authority:** Human project authority in chat, propagated by `SCA-APP-001`
**Scope-change snapshot:** `execution/_ScopeChange/SCA-APP-001_2026-06-13_1819_Provider-General_Runtime_Pi_Pattern-Corpus_v2/`

#### Ruling

Pi is a strong pattern corpus and reference for stable agentic work patterns.

This ruling does **not** approve:

- a Pi adapter;
- a Pi fork;
- direct Pi package imports;
- a Node 22 sidecar for Pi;
- a runtime-floor change for Pi;
- an immediate Pi spike.

#### Intent

Pi demonstrates useful agent patterns, tool-use patterns, lifecycle patterns, and harness patterns. Chirality should study and adapt those patterns into Chirality-owned contracts and implementation surfaces.

Governance should be interpreted as human intention alignment, evidence capture, and human judgment at gates and after work. It should not suppress effective agent tool use merely because a capability exists.

#### Implementation Boundary

Any future use of Pi as more than a reference requires a new human-ruling path and bounded implementation tranche. This ruling keeps Pi out of runtime dependency, adapter, fork, and spike scope.

## Component: execution/_Coordination/_DECISIONS/D-APP-02_RULING_2026-06-13.md

### D-APP-02 Ruling

**Status:** RULED
**Date:** 2026-06-13
**Decision:** Pi package import and runtime strategy
**Ruling authority:** Human project authority in chat, propagated by `SCA-APP-001`
**Scope-change snapshot:** `execution/_ScopeChange/SCA-APP-001_2026-06-13_1819_Provider-General_Runtime_Pi_Pattern-Corpus_v2/`

#### Ruling

Do not import Pi packages into Chirality App Dev.

Because Pi package import is not approved, no Node `>=22.19.0` runtime-floor migration, Node 22 sidecar, package dependency, lockfile update, packaging change, or wrapper/runtime migration is approved for Pi.

#### Intent

Chirality may study Pi packages and adapt patterns into Chirality-owned code and governance. Pattern adaptation must preserve separate intellectual-property identity and must not create a runtime package dependency on Pi.

#### Implementation Boundary

Any future direct Pi package dependency or Pi sidecar strategy requires a new explicit human ruling and bounded implementation tranche.

## Component: execution/_Coordination/_DECISIONS/D-APP-03_RULING_2026-06-13.md

### D-APP-03 Ruling

**Status:** RULED
**Date:** 2026-06-13
**Decision:** Provider-adapter runtime strategy
**Ruling authority:** Human project authority in chat, propagated by `SCA-APP-001`
**Scope-change snapshot:** `execution/_ScopeChange/SCA-APP-001_2026-06-13_1819_Provider-General_Runtime_Pi_Pattern-Corpus_v2/`

#### Ruling

Strategic provider-adapter generality is approved.

Chirality should build and govern a Chirality-owned harness with provider adapters that translate provider-specific API needs, sessions, tool behavior, event streams, permission modes, and agentic abilities into Chirality-owned runtime contracts.

Claude Agent SDK / Anthropic remains the first concrete adapter and the current shipped path.

#### Boundaries

This ruling does **not** approve implementation of any concrete non-Anthropic provider.

Every concrete new provider requires a bounded future implementation tranche with provider-network policy, adapter conformance, error classification, security/redaction checks, and release validation.

#### Governance Interpretation

The prior Anthropic-centered policy is now a current-shipped-path constraint, not the permanent strategic ceiling. Broader provider strategy is approved at the architecture level; shipped provider expansion remains gated.

## Component: execution/_Coordination/_DECISIONS/D-APP-04_PACKET_2026-06-15.md

### D-APP-04 Decision Packet - Post-Write Runtime Capability Sequence

**Status:** PROPOSAL
**Date:** 2026-06-15
**Prepared by:** WORKING_ITEMS
**Active plan item:** `plans/PLAN_2026-06-13_runtime_completion.md` dependency spine row 6

This packet asks for a human ruling before the next runtime capability implementation
after `WRITE-HOOKS-001`.

#### Decision Question

Which, if any, next capability lane is approved for a bounded implementation tranche?

The ruling may approve exactly one lane, approve a narrower prerequisite-only lane, or
hold all three lanes pending additional evidence.

#### Blocks

Until this packet is ruled, do not implement or expose:

- model-visible `Bash` / shell execution or bash-capable modes beyond the current deny posture;
- SDK `Agent` tool / governed subagent runtime execution beyond the existing validation gate and event-type skeleton;
- concrete non-Anthropic provider adapters, provider routing, provider network policy expansion, or provider package/runtime changes.

This packet does not reopen Pi scope. D-APP-01 and D-APP-02 continue to rule out any Pi
adapter, fork, package import, Node 22 sidecar, runtime-floor migration, or spike.

#### Authority Basis

- `docs/PRD.md#3.2 Non-Goals` says Chirality must not add `bash` as a user-enabled capability before permission, hooks, result storage, timeout, audit logging, and packaging checks exist.
- `docs/PRD.md#6.1 In Scope` requires governed SDK subagents to have Chirality identity, parent-child linkage, restricted capabilities, and stored output artifacts.
- `docs/CONTRACT.md#1.6 Permission, Tool Exposure, Hooks, and MCP` defines hard-deny precedence, hook fail-closed behavior, and `K-BASH-1`.
- `docs/CONTRACT.md#1.8 Agent and Subagent Governance` defines Type 2 sealing, subagent fail-closed gates, restricted child capability, and parent-child records.
- `docs/CONTRACT.md#1.9 Security, Network, Release, and Packaging` keeps outbound network limited to loopback plus the current Anthropic API path unless governed future scope expands it.
- `docs/PLAN.md#R4 - Bash, Tool Result Budgeting, and Context Mirror` places Bash after read and write hooks, and requires timeout, stdout/stderr capture, output storage, interrupt behavior, and audit events.
- `docs/PLAN.md#R5 - Governed Subagent Runtime` places executable SDK subagents after the local runtime spine and governance bridge are stable.
- `execution/_Coordination/_DECISIONS/D-APP-03_RULING_2026-06-13.md` approves provider-adapter generality only at the architecture level and explicitly does not approve concrete non-Anthropic providers.
- `frontend/docs/harness/runtime_engine_contract.md#Harness Tool Descriptor Contract` records that `MultiEdit`, notebook edits, shell, network, subagent, and mutating Chirality MCP tools remain unavailable until bounded implementation, hook, result-storage, and validation tranches land.

#### Current Baseline

Landed runtime spine through `WRITE-HOOKS-001`:

- SDK read built-ins and read-only Chirality MCP tools are exposed behind descriptor and permission policy.
- SDK `Write` and `Edit` are exposed only in `workspaceWrite` after path containment, instruction-root blocking, symlink rejection, and write-hook audit evidence.
- `Bash`, network-capable tools, SDK subagent execution, concrete non-Anthropic providers, mutating Chirality MCP tools, notebook edits, `MultiEdit`, artifact spill files, and full diff storage remain out of scope.

Known evidence debt:

- Normal instruction-root integrity still fails under the pre-existing split source-root/package-resource posture.
- Prior runtime tranches used temporary merged instruction roots for harness premerge validation.
- Artifact spill files and full tool-result storage contracts are not yet implemented.

#### Options

| Option | Ruling | What it permits | What remains denied |
|---|---|---|---|
| A | Approve R4 Bash prerequisites and controlled Bash implementation | A bounded tranche may implement Bash descriptor exposure, timeout, stdout/stderr capture, interrupt handling, output budgeting/storage, hook enforcement, and audit events. Model-visible Bash remains allowed only after tranche validation passes. | Bash in `readOnly` / `dontAsk`, unbounded commands, instruction-root writes, project-root escapes, provider/network expansion, subagent execution, Pi work. |
| B | Approve R5 governed subagent runtime first | A bounded tranche may wire SDK `Agent` tool behavior through `evaluateSubagentGovernance`, restricted child cwd/tools, sealed Type 2 briefs, parent-child event records, and output artifact references. | Bash, provider/network expansion, non-Type-2 agents, child capability inheritance/expansion, unsealed context, Pi work. |
| C | Prepare a concrete provider-expansion implementation packet only | A future packet may identify one candidate non-Anthropic provider, network policy, adapter conformance, key handling, redaction, and validation requirements. No provider code is implemented under this option. | Concrete provider adapter code, provider routing, provider package/runtime changes, broader network access, Pi work. |
| D | Hold all capability expansion | No capability implementation proceeds. The next work must repair prerequisite evidence or return to an already-approved unblocked item if one exists. | Bash, subagent execution, concrete provider expansion, Pi work. |

#### Recommendation

Approve Option A only as a bounded R4 tranche, with explicit constraints:

- Bash remains denied by default and in `readOnly` / `dontAsk`.
- Bash is exposed only in an explicitly governed mode after descriptor, permission, hook, timeout, interrupt, result-budget, result-storage, audit-event, and redaction tests pass.
- The tranche must not broaden provider/network policy. Network-capable shell behavior needs explicit deny or containment policy before model-visible exposure.
- Governed subagents remain deferred to a later R5 ruling or tranche.
- Concrete non-Anthropic providers remain deferred to a separate provider-specific packet and ruling.

Rationale: R4 is the next roadmap phase after write hooks, and Bash depends on the same path,
hook, tool-result, interruption, and audit surfaces just stabilized by `WRITE-HOOKS-001`.
Subagents are higher-order orchestration and should not land before the shell/tool-result
boundary is validated. Provider expansion is strategically approved but remains intentionally
provider-specific and network-sensitive.

#### Validation Implications If Option A Is Ruled

Minimum expected validation for a Bash tranche:

- focused tests for descriptor exposure, permission overlay decisions, unknown tool denial, denied Bash no-spawn behavior, and mode mapping;
- hook tests for project-root containment, instruction-root blocking, symlink rejection, timeout/failure evidence, and fail-closed audit persistence;
- tool-result tests for stdout/stderr metadata, byte budgets, artifact spill behavior, redaction, and no raw secret/API-key event payloads;
- runtime mapper/event tests for `tool.permission`, `tool.started`, `tool.progress`, `tool.completed`, `tool.failed`, `context.compacted`, interruption, and terminal turn outcomes;
- `npm run test`;
- `npm run typecheck`;
- `npm run harness:validate:premerge` against a reachable local app, using the documented temporary merged instruction-root workaround until split-root repair lands;
- `npm run proof:network-policy` if the implementation changes any network, provider, or command-network enforcement path;
- `npm run instruction-root:integrity`, with the existing split-root failure recorded if still unresolved.

#### Affected Future Files

Likely Option A implementation files include, but are not limited to:

- `frontend/src/lib/harness/tool-descriptor.ts`
- `frontend/src/lib/harness/permission-overlay.ts`
- `frontend/src/lib/harness/sdk-options-builder.ts`
- `frontend/src/lib/harness/chirality-hooks.ts`
- `frontend/src/lib/harness/tool-evidence.ts`
- `frontend/src/lib/harness/event-schema.ts`
- `frontend/src/lib/harness/sdk-message-mapper.ts`
- focused tests under `frontend/src/__tests__/lib/`
- runtime contract documentation and plan closeout records

#### Ruling Template

When the human rules, add a ruling record under `execution/_Coordination/_DECISIONS/`
and update `_REGISTER.md` to `RULED`.

Recommended ruling fields:

- selected option: A, B, C, D, or narrower custom ruling;
- permitted implementation tranche id, if any;
- explicit denied surfaces;
- validation requirements and any waivers;
- whether the ruling changes provider/network policy;
- whether further human approval is required before model-visible exposure.

## Component: execution/_Coordination/_DECISIONS/D-APP-04_RULING_2026-06-15.md

### D-APP-04 Ruling

**Status:** RULED
**Date:** 2026-06-15
**Decision:** Post-write runtime capability sequence
**Ruling authority:** Human project authority in chat
**Packet:** `execution/_Coordination/_DECISIONS/D-APP-04_PACKET_2026-06-15.md`

#### Ruling

Option A is approved.

A bounded R4 Bash tranche may proceed after `WRITE-HOOKS-001`. The approved lane is
Bash prerequisites and controlled Bash implementation.

#### Permitted Implementation Scope

The bounded R4 Bash tranche may implement:

- Bash descriptor exposure;
- permission-overlay and mode mapping for Bash;
- default denial of Bash in `readOnly` and `dontAsk`;
- governed-mode Bash exposure after policy and hook checks pass;
- timeout behavior;
- stdout/stderr capture and separation;
- interrupt handling;
- result budgeting and result-storage or artifact-spill behavior;
- safe audit events for permission, start, progress, completion, failure, interruption,
  and terminal turn outcomes;
- redaction checks for secrets and API keys;
- tests and runtime-contract documentation updates required to validate the lane.

Model-visible Bash exposure is allowed only after the tranche's validation requirements
pass and closeout records the evidence.

#### Explicit Denials And Deferrals

This ruling does not approve:

- Bash in `readOnly` mode;
- unapproved Bash in `dontAsk` mode;
- unbounded shell execution;
- instruction-root writes;
- project-root escapes;
- provider/network policy expansion;
- SDK `Agent` tool or governed subagent runtime execution;
- concrete non-Anthropic provider implementation or provider routing;
- remote MCP, plugins, or network-capable tools beyond the current policy;
- Pi adapter, fork, package import, Node 22 sidecar, runtime-floor migration, or spike;
- release readiness, lifecycle issuance, professional approval, certification, sealing,
  authentication, or code-compliance acceptance.

Governed SDK subagents and concrete provider expansion remain deferred unless a future
bounded tranche and human ruling explicitly approve them.

#### Validation Requirements

The R4 Bash tranche must include evidence for:

- descriptor exposure and deterministic option construction;
- permission overlay allow, deny, ask, and unknown-tool behavior;
- denied Bash no-spawn behavior;
- project-root containment;
- instruction-root blocking;
- symlink rejection where filesystem writes or redirects are implicated;
- timeout and interrupt behavior;
- stdout/stderr metadata and result budgeting;
- artifact-spill or result-storage behavior for large outputs;
- redaction of secrets/API keys from runtime events, logs, and artifacts;
- `tool.permission`, `tool.started`, `tool.progress`, `tool.completed`,
  `tool.failed`, context/compaction where applicable, interruption, and terminal turn
  outcome events;
- no provider/network broadening without a separate ruling.

Minimum command routing:

- focused tests for touched descriptor, permission, options, hook, event, mapper, and
  result-storage modules;
- `npm run test`;
- `npm run typecheck`;
- `npm run harness:validate:premerge` against a reachable local app, using the documented
  temporary merged instruction-root workaround until split-root repair lands;
- `npm run proof:network-policy` if the implementation changes any network, provider, or
  command-network enforcement path;
- `npm run instruction-root:integrity`, with the existing split-root failure recorded if
  still unresolved.

#### Implementation Boundary

No further human ruling is required to start the bounded R4 Bash implementation described
above. Any expansion beyond this ruling, including subagent execution, concrete provider
implementation, provider/network expansion, Pi work, or release-publication posture,
requires a separate human ruling.

## Component: execution/_Coordination/_DECISIONS/D-APP-05_PACKET_2026-06-15.md

### D-APP-05 Decision Packet - R5 Governed SDK Subagent Runtime

**Status:** PROPOSAL
**Date:** 2026-06-15
**Prepared by:** WORKING_ITEMS
**Active plan item:** Post-`BASH-R4-001` runtime capability gate

This packet asks for a human ruling before implementing the next roadmap capability:
governed SDK subagent execution through the first-adapter `Agent` tool and SDK `agents`
configuration.

#### Decision Question

Is a bounded R5 governed SDK subagent runtime tranche approved after the landed R4 Bash
work?

The ruling may approve the full bounded R5 tranche, approve a narrower prerequisite-only
tranche, require dependency/SCC reconciliation before implementation, or hold subagent
execution pending additional evidence.

#### Blocks

Until this packet is ruled, do not implement or expose:

- model-visible SDK `Agent` tool execution;
- SDK `agents` definitions that can execute child turns;
- governed subagent runtime execution beyond the existing validation gate and event-type
  skeleton;
- child runtime records that imply executable subagent support has landed;
- parent-to-child capability inheritance or expansion.

This packet does not reopen Pi scope, provider expansion, remote MCP, plugins, or broader
network scope. D-APP-01 and D-APP-02 continue to rule out any Pi adapter, fork, package
import, Node 22 sidecar, runtime-floor migration, or spike. D-APP-03 approves
provider-adapter generality only; concrete non-Anthropic providers still need a separate
bounded future tranche.

#### Authority Basis

- `docs/PRD.md#R5 - Governed Subagent Runtime` requires SDK subagents to be generated from
  Type 2 agent instructions, restricted by tool/model/turn limits, gated by
  `evaluateSubagentGovernance`, mirrored into parent Chirality events, and linked to child
  output artifacts.
- `docs/CONTRACT.md#1.8 Agent and Subagent Governance` defines sealed Type 2 context,
  fail-closed delegation, restricted child capabilities, and parent-child records as
  invariants.
- `docs/CONTRACT.md#1.6 Permission, Tool Exposure, Hooks, and MCP` says prompt text and
  `allowedTools` are not safety boundaries; subagent actions require runtime enforcement
  through permission policy and hooks.
- `docs/SPEC.md#15 Permission Modes and Hooks` requires the `Agent` tool to be gated
  through `evaluateSubagentGovernance`, and hook failures fail closed for subagent actions.
- `docs/PLAN.md#R5 - Governed Subagent Runtime` places executable subagents after the local
  runtime spine, permission policy, hooks, and prior tool phases are stable.
- `frontend/docs/harness/runtime_engine_contract.md#Harness Tool Descriptor Contract`
  records that subagent capability remains unavailable until bounded implementation, hook,
  result-storage, and validation tranches land.
- `execution/_Coordination/_DECISIONS/D-APP-04_RULING_2026-06-15.md` approved only R4 Bash
  and explicitly deferred SDK `Agent` tool / governed subagent runtime execution.
- `execution/_Reconciliation/DepClosure/CLOSURE_SCC001_RESIDUAL_CLOSEOUT_2026-05-24_2320/Dependency_Closure_Report.md`
  still reports a residual six-node strict SCC. R5 implementation must not claim
  project-wide dependency closure; if a later R5 implementation depends on SCC closure,
  that requires the recommended RECONCILIATION ruling package.

#### Current Baseline

Landed runtime posture:

- Runtime contract, TurnEngine, session events, SDK options, message mapping, permission
  overlay, read tools, read-only Chirality MCP tools, write/edit hooks, controlled Bash,
  and split-root instruction-root package integrity repair have landed.
- `frontend/src/lib/harness/subagent-governance.ts` already evaluates persona allowlists,
  sealed context, pipeline approval metadata, approval references, and Type 2 eligibility.
- `TurnEngine` evaluates subagent governance and passes `delegatedSubagents` metadata to
  the adapter path, but it does not execute SDK subagents.
- The tool descriptor registry has an `agent` descriptor, and the permission overlay
  hard-denies subagent execution as future policy.
- `sdk-message-mapper` and `event-schema` can represent subagent lifecycle event categories,
  but executable SDK subagent runtime support is not landed.

Existing deferrals remain in force:

- no SDK `Agent` tool exposure;
- no concrete non-Anthropic provider implementation or routing;
- no remote MCP, plugins, provider/network broadening, Pi work, notebook edits, `MultiEdit`,
  mutating Chirality MCP tools, release-readiness claims, lifecycle issuance, professional
  approval, certification, sealing, authentication, or code-compliance acceptance.

#### Options

| Option | Ruling | What it permits | What remains denied |
|---|---|---|---|
| A | Approve bounded R5 governed SDK subagent runtime implementation | A future tranche may generate SDK `agents` definitions from eligible Type 2 instructions, expose `Agent` only when governance metadata passes, restrict child cwd/tools/model/turns, fail closed through a `PreToolUse` governance hook, persist parent-child lifecycle events, and store child output artifact references. Model-visible exposure is allowed only after tranche validation passes. | Non-Type-2 agents, unsealed context, missing approval metadata, child capability inheritance/expansion, provider/network broadening, remote MCP/plugins, Pi work, release-readiness/professional claims. |
| B | Approve prerequisite-only R5 bridge | A future tranche may add the registry, option-construction, hook, and event tests needed for R5 while keeping the SDK `Agent` descriptor hard-denied and non-model-visible. | Any executable SDK subagent run, model-visible `Agent`, child output artifacts that imply execution, provider/network broadening, Pi work. |
| C | Require dependency/SCC ruling package before R5 implementation | No subagent code lands. The next control-plane work should be a RECONCILIATION longer-cycle ruling package for the residual six-node SCC if it is judged to block R5 closure claims. | R5 implementation, model-visible `Agent`, provider/network broadening, Pi work. |
| D | Hold subagent capability expansion | No subagent implementation proceeds. Future work must select another unblocked plan item or prepare a different human-gated packet. | SDK subagent execution, provider expansion, remote MCP/plugins, Pi work. |

#### Recommendation

Approve Option A only as a bounded R5 tranche, with explicit constraints:

- SDK `Agent` remains unavailable until the R5 implementation passes validation.
- `evaluateSubagentGovernance` remains the required fail-closed decision source.
- Only Type 2 task agents with sealed context, pipeline approval metadata, approval
  reference, restricted child tools, restricted cwd, and parent-child audit records may be
  executable.
- Developer-only bypass must not grant ungated subagent autonomy.
- The tranche must not broaden provider/network policy, expose remote MCP/plugins, implement
  concrete non-Anthropic providers, reopen Pi scope, or make release/professional-boundary
  claims.

Rationale: R5 is the next roadmap capability after the read, write, and Bash tool phases.
The required governance evaluator and subagent event categories already exist, but the
runtime must not connect them to SDK execution without an explicit human ruling and a
bounded validation plan.

#### Validation Implications If Option A Is Ruled

Minimum expected validation for a full R5 tranche:

- focused tests for SDK `agents` definition generation from Type 2 instruction files;
- tests proving non-Type-2, non-allowlisted, unsealed, missing-approval, and unknown
  subagent requests are denied before execution;
- SDK options tests proving `Agent` is model-visible only after descriptor, mode,
  permission, and governance checks pass;
- hook tests proving `Agent` tool preflight fails closed on evaluator errors, missing
  metadata, inherited capability expansion, and child cwd/tool violations;
- event tests for `subagent.started`, `subagent.progress`, `subagent.completed`, and
  `subagent.failed` with parent-child linkage and no raw secrets;
- output artifact tests proving child outputs are referenced through bounded artifact
  records rather than treated as project truth;
- regression tests proving `readOnly`, `dontAsk`, and developer-only `bypass` do not grant
  ungated subagent autonomy;
- `npm run test`;
- `npm run typecheck`;
- `npm run harness:validate:premerge` against a reachable local app when browser-facing
  session or turn behavior changes;
- `npm run instruction-root:integrity`;
- `npm run proof:network-policy` only if the implementation touches provider, network, or
  outbound behavior, which Option A does not authorize by default.

#### Affected Future Files

Likely Option A implementation files include, but are not limited to:

- `frontend/src/lib/harness/subagent-governance.ts`
- `frontend/src/lib/harness/sdk-options-builder.ts`
- `frontend/src/lib/harness/chirality-hooks.ts`
- `frontend/src/lib/harness/tool-descriptor.ts`
- `frontend/src/lib/harness/permission-overlay.ts`
- `frontend/src/lib/harness/turn-engine.ts`
- `frontend/src/lib/harness/sdk-message-mapper.ts`
- `frontend/src/lib/harness/event-schema.ts`
- `frontend/src/lib/harness/session-events.ts`
- focused tests under `frontend/src/__tests__/lib/` and relevant route/harness tests
- runtime contract documentation and plan closeout records

#### Ruling Template

When the human rules, add a ruling record under `execution/_Coordination/_DECISIONS/`
and update `_REGISTER.md` to `RULED`.

Recommended ruling fields:

- selected option: A, B, C, D, or narrower custom ruling;
- permitted implementation tranche id, if any;
- explicit denied surfaces;
- required validation commands and any waivers;
- whether dependency/SCC reconciliation is prerequisite to implementation or only to
  project-wide closure claims;
- whether the ruling changes provider/network policy;
- whether further human approval is required before model-visible `Agent` exposure.

## Component: execution/_Coordination/_DECISIONS/D-APP-05_RULING_2026-06-15.md

### D-APP-05 Ruling

**Status:** RULED
**Date:** 2026-06-15
**Decision:** R5 governed SDK subagent runtime prerequisite
**Ruling authority:** Human project authority in chat
**Packet:** `execution/_Coordination/_DECISIONS/D-APP-05_PACKET_2026-06-15.md`

#### Ruling

Custom Option B/A-prerequisite is approved.

Before executable SDK subagents are exposed, Chirality must implement or specify a
Chirality-owned provider-adapter-neutral agent/subagent runtime contract informed by both
the Claude Agent SDK and Pi agent SDK patterns.

Claude Agent SDK `Agent` may remain the first adapter-specific substrate, and Pi may be
used as an architectural pattern corpus, but neither Claude nor Pi may define Chirality's
public or core runtime contract.

#### Permitted Implementation Scope

A bounded prerequisite tranche may:

- define or implement Chirality-owned provider-adapter-neutral agent/subagent runtime
  interfaces and contracts;
- define provider-neutral child-run, delegation, parent-child linkage, capability, event,
  artifact, and replay semantics;
- map Claude Agent SDK `Agent` as the first adapter-specific implementation substrate
  without exposing it as Chirality's public/core contract;
- use Pi agent SDK patterns as an architectural corpus for durable sessions, event trees,
  tool lifecycle hooks, ordered tool results, restore boundaries, and host-rehydrated
  tools/models/hooks;
- update runtime-contract documentation, conformance expectations, descriptor metadata,
  and tests needed to preserve provider-adapter neutrality before executable subagents
  are exposed.

#### Explicit Denials And Deferrals

This ruling does not approve:

- executable SDK subagent exposure before the prerequisite contract work lands and validates;
- model-visible SDK `Agent` tool execution;
- executable SDK `agents` definitions that can run child turns;
- Pi package import;
- Pi adapter, fork, sidecar, or spike;
- Node 22 sidecar or runtime-floor migration for Pi;
- concrete non-Anthropic provider implementation or provider routing;
- provider or network policy expansion;
- remote MCP, plugins, or network-capable tool expansion;
- child capability inheritance or expansion beyond Chirality-owned policy;
- release readiness, lifecycle issuance, professional approval, certification, sealing,
  authentication, or code-compliance acceptance.

#### Validation Requirements

The prerequisite tranche must include evidence that:

- Chirality-owned interfaces and event names remain provider-neutral;
- Claude Agent SDK and Pi concepts appear only as adapter metadata, implementation
  substrates, or pattern-corpus rationale;
- no Pi runtime dependency, package import, sidecar, fork, adapter, or spike is introduced;
- no concrete non-Anthropic provider implementation, routing, package/runtime change, or
  network broadening is introduced;
- executable subagents remain blocked until a later bounded implementation tranche
  explicitly enables them after contract validation.

Minimum command routing for docs/control-plane-only prerequisite work is the governance
gate from `docs/RELEASE_QUALITY_GATES.md`. Runtime-contract source or test changes must
also route through the runtime contract gate in `docs/VALIDATION_STRATEGY.md`.

#### Implementation Boundary

No further human ruling is required to start the bounded provider-adapter-neutral
agent/subagent contract prerequisite described above.

Any expansion beyond this ruling, including executable subagent exposure, Pi implementation
paths, concrete provider implementation, provider routing, provider/network expansion,
remote MCP/plugins, or release-publication posture, requires a separate human ruling or
bounded future implementation tranche where already required by project policy.

## Component: execution/_Coordination/_DECISIONS/D-APP-06_PACKET_2026-06-15.md

### D-APP-06 Decision Packet - Post-Contract R5 Executable Subagent Runtime

**Status:** PROPOSAL
**Date:** 2026-06-15
**Prepared by:** WORKING_ITEMS
**Active plan item:** `plans/PLAN_2026-06-13_runtime_completion.md` dependency spine row 9

This packet asks for a human ruling after the provider-adapter-neutral
agent/subagent runtime contract prerequisite landed in `AGENT-SUBAGENT-CONTRACT-001`.
It does not implement or expose executable subagents.

#### Decision Question

Is a bounded executable R5 governed subagent runtime tranche approved now that the
provider-neutral prerequisite contract has landed and validated?

The ruling may approve a narrowly bounded executable implementation, approve another
non-executable bridge tranche, require dependency/SCC reconciliation first, or hold R5
capability expansion.

#### Blocks

Until this packet is ruled, do not implement or expose:

- model-visible SDK `Agent` tool execution;
- executable SDK `agents` definitions that can run child turns;
- generated child definitions that imply executable support has landed;
- child capability inheritance or expansion beyond Chirality-owned policy;
- parent-child output artifact records that imply an executable child run occurred.

This packet does not reopen Pi scope, concrete non-Anthropic providers, provider routing,
provider/network broadening, remote MCP, plugins, package/runtime migration, or release
publication posture.

#### Authority Basis

- `execution/_Coordination/_DECISIONS/D-APP-05_RULING_2026-06-15.md` approved only the
  provider-adapter-neutral prerequisite before executable SDK subagents are exposed.
- `plans/PLAN_COMPLETION_LOG.md#2026-06-15 - Provider-adapter-neutral agent/subagent contract prerequisite landed` records that the prerequisite landed, while executable subagent runtime remains future/human-gated.
- `frontend/docs/harness/runtime_engine_contract.md#Agent/Subagent Runtime Contract` records the current contract-only posture and states that executable exposure requires a later bounded implementation.
- `docs/PRD.md#R5 - Governed Subagent Runtime` requires SDK `agents` and `Agent` tool execution to be generated from Type 2 instructions, restricted by tool/model/turn limits, fail-closed through `evaluateSubagentGovernance`, mirrored into parent runtime events, and linked to child output artifacts.
- `docs/PLAN.md#R5 - Governed Subagent Runtime` places executable subagents after the local runtime spine and governance bridge are stable.
- `docs/CONTRACT.md#1.8 Agent and Subagent Governance` defines sealed Type 2 context, fail-closed delegation, restricted child capabilities, and parent-child records as governance invariants.
- `docs/SPEC.md#15 Permission Modes and Hooks` requires subagent actions to fail closed through runtime permission and hook enforcement.
- `execution/_Reconciliation/DepClosure/CLOSURE_SCC001_RESIDUAL_CLOSEOUT_2026-05-24_2320/Dependency_Closure_Report.md` still reports a residual six-node strict SCC. Any R5 work must not claim project-wide dependency closure from current evidence.

#### Current Baseline

Landed runtime posture:

- read tools, read-only Chirality MCP tools, write/edit hooks, controlled Bash, package
  instruction-root integrity repair, and the provider-neutral agent/subagent contract are
  landed;
- child-run records are provider-neutral and keep adapter metadata isolated;
- executable delegation remains blocked by contract;
- child capability inheritance is disabled by contract;
- Pi is pattern corpus/reference only, with no runtime dependency, adapter, fork, sidecar,
  package import, or spike;
- concrete non-Anthropic provider routing remains blocked.

Remaining implementation gap:

- no model-visible SDK `Agent` tool;
- no executable SDK `agents` definitions;
- no child turn execution;
- no child output artifact persistence from executable runs;
- no validation proving executable subagents are constrained by the landed contract.

#### Options

| Option | Ruling | What it permits | What remains denied |
|---|---|---|---|
| A | Approve bounded executable R5 implementation | A future tranche may expose SDK `Agent` only after descriptor, permission, and governance checks pass; generate SDK `agents` from eligible Type 2 instructions; restrict child cwd/tools/model/turns; fail closed through `evaluateSubagentGovernance`; persist parent-child events and output artifact references. | Non-Type-2 agents, unsealed context, missing approval metadata, child capability inheritance/expansion, Pi implementation, provider/network broadening, remote MCP/plugins, release/professional claims. |
| B | Approve non-executable R5 bridge only | A future tranche may add registry, option-construction, hook, artifact-schema, and event tests while keeping SDK `Agent` hard-denied and non-model-visible. | Executable child turns, model-visible `Agent`, SDK `agents` that can run, provider/network broadening, Pi work. |
| C | Require dependency/SCC ruling package first | No R5 implementation lands until RECONCILIATION prepares the residual six-node SCC ruling package or the human rules it non-blocking for R5. | R5 implementation, model-visible `Agent`, provider/network broadening, Pi work. |
| D | Hold R5 capability expansion | No subagent capability implementation proceeds. Future work must select another unblocked plan item or prepare a different human-gated packet. | SDK subagent execution, provider expansion, remote MCP/plugins, Pi work. |

#### Recommendation

Approve Option A only as a bounded future implementation tranche, with these constraints:

- executable exposure remains unavailable until implementation validation passes;
- `evaluateSubagentGovernance` is the fail-closed source of truth for child execution;
- only Type 2 task agents with sealed context, pipeline approval metadata, approval
  reference, restricted child tools, restricted cwd, and parent-child audit records may be
  executable;
- child runs do not inherit parent capabilities;
- developer-only bypass must not grant ungated subagent autonomy;
- the tranche must not broaden provider/network policy, expose remote MCP/plugins,
  implement concrete non-Anthropic providers, reopen Pi scope, or make release,
  lifecycle, professional, certification, sealing, authentication, or code-compliance
  claims.

#### Validation Implications If Option A Is Ruled

Minimum expected validation for a full executable R5 tranche:

- focused tests for SDK `agents` definition generation from Type 2 instruction files;
- tests proving non-Type-2, non-allowlisted, unsealed, missing-approval, unknown, and
  malformed subagent requests are denied before execution;
- SDK options tests proving `Agent` is model-visible only after descriptor, mode,
  permission, and governance checks pass;
- hook tests proving `Agent` preflight fails closed on evaluator errors, missing metadata,
  inherited capability expansion, child cwd violations, and child tool violations;
- event tests for `subagent.started`, `subagent.progress`, `subagent.completed`, and
  `subagent.failed` with parent-child linkage and adapter metadata isolation;
- output artifact tests proving child outputs are referenced through bounded artifacts and
  are not treated as project truth;
- regression tests proving `readOnly`, `dontAsk`, and developer-only `bypass` do not grant
  ungated subagent autonomy;
- `npm run test`;
- `npm run typecheck`;
- `npm run harness:validate:premerge` against a reachable local app when browser-facing
  session, SSE, or turn behavior changes;
- `npm run instruction-root:integrity`;
- `npm run proof:network-policy` only if the implementation touches provider, network, or
  outbound behavior, which Option A does not authorize by default.

#### Affected Future Files

Likely Option A implementation files include, but are not limited to:

- `frontend/src/lib/harness/agent-runtime-contract.ts`
- `frontend/src/lib/harness/subagent-governance.ts`
- `frontend/src/lib/harness/sdk-options-builder.ts`
- `frontend/src/lib/harness/chirality-hooks.ts`
- `frontend/src/lib/harness/tool-descriptor.ts`
- `frontend/src/lib/harness/permission-overlay.ts`
- `frontend/src/lib/harness/turn-engine.ts`
- `frontend/src/lib/harness/sdk-message-mapper.ts`
- `frontend/src/lib/harness/event-schema.ts`
- `frontend/src/lib/harness/session-events.ts`
- focused tests under `frontend/src/__tests__/lib/`
- runtime contract documentation and plan closeout records

#### Ruling Template

When the human rules, add a ruling record under `execution/_Coordination/_DECISIONS/`
and update `_REGISTER.md` to `RULED`.

Recommended ruling fields:

- selected option: A, B, C, D, or narrower custom ruling;
- permitted implementation tranche id, if any;
- explicit denied surfaces;
- required validation commands and any waivers;
- whether dependency/SCC reconciliation is prerequisite to implementation or only to
  project-wide closure claims;
- whether the ruling changes provider/network policy;
- whether further human approval is required before model-visible `Agent` exposure.

## Component: execution/_Coordination/_DECISIONS/_REGISTER.md

### Human Decision Register - Chirality App Dev

**Created:** 2026-06-13
**Status:** Non-governing tracking surface.

This register tracks human-gated decisions for the active app-integration loop. Agents may prepare decision packets labeled `PROPOSAL`; only the human project authority rules. Authority remains with `docs/PRD.md`, `docs/PLAN.md`, source code, tests, and git history.

**Row states:** `NOT_PREPARED` -> `AWAITING_RULING` -> `RULED`.

| ID | Decision | Blocks | State | Packet | Ruling record |
|---|---|---|---|---|---|
| D-APP-01 | Whether Pi should be treated as adapter/fork/import/spike scope or as a pattern corpus only | Any Pi adapter, fork, package import, sidecar, or spike work | RULED | - | `execution/_Coordination/_DECISIONS/D-APP-01_RULING_2026-06-13.md` |
| D-APP-02 | If Pi packages are imported, choose runtime strategy: raise Chirality runtime floor to Node `>=22.19.0` or isolate Pi behind a Node 22 sidecar | Any direct Pi package dependency or Node 22 sidecar/runtime-floor change for Pi | RULED | - | `execution/_Coordination/_DECISIONS/D-APP-02_RULING_2026-06-13.md` |
| D-APP-03 | Whether to broaden runtime strategy beyond the current shipped Anthropic path toward provider-adapter generality | Any concrete non-Anthropic shipped backend adapter or provider routing | RULED | - | `execution/_Coordination/_DECISIONS/D-APP-03_RULING_2026-06-13.md` |
| D-APP-04 | Which post-write runtime capability lane, if any, is approved next: Bash, governed SDK subagents, or concrete provider expansion preparation | Bash exposure, governed SDK subagent execution, and concrete non-Anthropic provider implementation/routing after `WRITE-HOOKS-001` | RULED | `execution/_Coordination/_DECISIONS/D-APP-04_PACKET_2026-06-15.md` | `execution/_Coordination/_DECISIONS/D-APP-04_RULING_2026-06-15.md` |
| D-APP-05 | Whether to approve bounded R5 governed SDK subagent runtime after landed R4 Bash | SDK `Agent` tool exposure, executable SDK `agents` definitions, and governed subagent runtime execution | RULED | `execution/_Coordination/_DECISIONS/D-APP-05_PACKET_2026-06-15.md` | `execution/_Coordination/_DECISIONS/D-APP-05_RULING_2026-06-15.md` |
| D-APP-06 | Whether to approve bounded executable R5 governed subagent runtime after landed provider-neutral contract prerequisite | Model-visible SDK `Agent` tool execution, executable SDK `agents` definitions, child turn execution, and executable child output artifacts | AWAITING_RULING | `execution/_Coordination/_DECISIONS/D-APP-06_PACKET_2026-06-15.md` | - |

#### Decision Preparation Rules

- Prepare a packet only when the selected tranche is blocked by the decision.
- Keep packets under `execution/_Coordination/_DECISIONS/`.
- Label packets `PROPOSAL`.
- Include options, recommendation, risks, validation implications, and affected files.
- Treat approval as recorded only when a ruling record is added.
- `RULED` decisions remain subject to their ruling record. Do not infer broader implementation approval than the ruling text grants.
