# Runtime Stabilization Development Plan

**Date:** 2026-06-16
**Status:** DRAFT / NON-GOVERNING
**Product:** Chirality desktop harness and bundled agent operating system
**Working root:** `projects/chirality-app-dev/`
**Prepared by:** `WORKING_ITEMS`

This draft proposes the next app-dev development program after completion of the
runtime completion plan and six-node SCC resolution plan. It is an outline for
human review and later RESEARCH-informed revision. It does not select an active
implementation queue, change product requirements, approve release readiness,
advance lifecycle state, create professional approval, certify, seal,
authenticate, or accept code compliance.

Project truth remains in governed docs, decomposition and deliverable artifacts,
source, tests, evidence records, accepted snapshots, decision records, and git
history. Runtime logs, SDK transcripts, completion logs, validation artifacts,
and this draft are derivative evidence or planning material only.

## 1. Draft Purpose

The next program should prioritize runtime stabilization rather than broad
feature expansion. The landed runtime now has a provider-adapter spine, event
schema, permission overlay, hooks, read/write/Bash surfaces, and governed R5
subagent execution. The immediate planning need is to reconcile that landed
state with governance and validation, make runtime evidence repeatable, and
identify the minimum bounded work needed before any further tool, provider,
remote-MCP, plugin, or domain-engine expansion.

This draft is intentionally local-evidence-only. Concurrent RESEARCH work may
later add findings, but this draft does not wait for them and does not invent
their conclusions.

## 2. Local Baseline

Current local evidence indicates:

- `execution/_Coordination/_COORDINATION.md` records that the residual six-node
  strict dependency SCC is closed and no new broad runtime roadmap has been
  selected.
- `plans/PLAN_2026-06-13_runtime_completion.md` is retired as an active queue
  and records runtime work through `R5-EXEC-001` as landed.
- `plans/PLAN_2026-06-16_six_node_scc_resolution.md` is closed and
  non-governing after `SCC-CLOSEOUT-001`.
- `plans/PLAN_COMPLETION_LOG.md` records landed runtime and SCC tranches as
  historical narrative, not authority.
- `frontend/docs/harness/runtime_engine_contract.md` is the best current
  runtime contract baseline. It records the opt-in `agentSdk` path, current
  exposed tool classes, denied tool classes, event categories, and subagent
  posture.
- `frontend/src/lib/harness/` now contains the runtime implementation surfaces
  implied by prior plans: `turn-engine`, `event-schema`, `session-events`,
  `run-logger`, SDK options/message mapping, permission overlay, tool
  descriptors, read MCP tools, path/shell policy, hooks, result artifacts, and
  subagent bridge.
- `frontend/src/__tests__/` contains focused tests for the current runtime
  modules, including engine contract, session events, SDK mapping/options,
  permissions, hooks, descriptors, Bash policy, MCP read tools, and subagents.
- `frontend/scripts/validate-harness-section8.mjs` and
  `frontend/scripts/validate-harness-premerge.mjs` still expose the running-app
  harness validation surface as Section 8. Section 9 validation IDs are
  specified in governance but are not yet first-class premerge artifacts.

Known reconciliation issues:

- Some early PRD assessment text still describes the harness as lacking runtime
  primitives that now exist in source.
- The v3.2 software decomposition remains the topology authority, but many
  deliverable `_STATUS.md` files remain at `SEMANTIC_READY` from earlier
  decomposition work rather than reflecting later runtime implementation.
- The coordination record correctly states that no new broad runtime roadmap is
  selected; this draft should not be treated as active queue until accepted.
- The retired runtime completion plan contains useful residual handoffs, but it
  must not be revived as the active selection instrument.

## 3. Program Principles

- Stabilize before expanding: validation, replay, evidence, packaging, and
  governance reconciliation precede new capability.
- Keep provider-adapter generality strategic, but do not implement concrete
  non-Anthropic providers without a future bounded ruling and plan.
- Preserve current network policy: loopback plus the current Anthropic API path.
- Treat `CHIRALITY_HARNESS_PROVIDER=agentSdk` as opt-in unless a later tranche
  records the evidence and ruling needed for default-provider cutover.
- Keep `allowedTools` insufficient by itself; execution requires descriptor
  resolution, mode policy, `disallowedTools`, permission callback, hooks, and
  evidence capture.
- Keep raw secrets, raw full diffs, unbounded raw outputs, SDK transcripts, and
  runtime artifacts out of project truth.
- Keep domain-engine profiles and operation proposals as future-boundary scope
  unless explicitly activated by a governed amendment.

## 4. Draft Tranche Spine

| Tranche | Purpose | Primary scope | Minimum validation |
|---|---|---|---|
| `STAB-00` Baseline Reconciliation | Produce an accepted current-state map before new implementation. | Compare source/tests, runtime contract, PRD/PLAN/SPEC/TYPES, v3.2 decomposition, coordination files, decision register, completion log, and latest SCC evidence. Identify stale text and mismatched lifecycle/status surfaces. | Governance gate: markdown diff checks, path/reference checks, no-runtime-change check. Runtime commands only if source assumptions are tested. |
| `STAB-01` Section 9 Validation Surface | Make runtime validation IDs explicit and machine-readable. | Add Section 9 validation script or extend premerge summary so landed runtime behavior is represented by stable IDs for event log, replay, permission precedence, tool runtime, hooks, result artifacts, compaction/subagent evidence where implemented. | Focused script tests, relevant runtime tests, `npm run typecheck`, `npm run test`, running-app `npm run harness:validate:premerge`. |
| `STAB-02` SDK Runtime Readiness | Prove the opt-in SDK path and decide whether default cutover needs a human ruling. | Exercise `CHIRALITY_HARNESS_PROVIDER=agentSdk`, verify settings isolation, SDK session linkage, allowed/disallowed tools, key redaction, subprocess/package behavior, network policy, and packaged-app readiness. | Runtime premerge plus security/network gate. Packaging proof uses `npm run desktop:dist` when package behavior or release-candidate evidence is in scope. |
| `STAB-03` Session Replay and Artifact Evidence | Harden user/auditor reconstruction of runtime activity. | Improve replay coverage, artifact metadata, non-shell result storage policy, redacted overflow handling, diff/provenance summaries, and malformed-tail diagnostics without storing secrets or unbounded raw payloads. | Focused session-events/replay/artifact/redaction tests, `npm run typecheck`, `npm run test`; harness premerge if UI/API behavior changes. |
| `STAB-04` Deterministic Chirality MCP Maturity | Plan and implement only bounded mutating Chirality MCP tools after validation hardening. | Candidate tools: `_STATUS.md` transition and `Dependencies.csv` write/update through existing lifecycle, dependency, permission, hook, path, redaction, and event policies. No remote MCP or plugin system. | Permission/tool gate plus lifecycle/dependency tests, path and hook denial tests, `npm run typecheck`, `npm run test`; harness premerge if exposed to running app workflows. |
| `STAB-05` Governance Refresh and Active Queue | Convert accepted stabilization outcomes into current coordination surfaces. | Refresh stale PRD/PLAN/decomposition notes or write supersession guidance; update active coordination only after human acceptance; retire this draft or replace it with final plan. | Governance gate. Runtime commands skipped unless executable behavior changed. |

## 5. Tranche Detail

### STAB-00 - Baseline Reconciliation

Goal: create a defensible current-state map before any feature or validation
change.

Required outputs:

- Current-state matrix mapping landed runtime capabilities to source files,
  tests, governance requirements, and prior tranche evidence.
- Stale-governance list with proposed disposition: update, supersede, keep as
  historical, or defer.
- Deliverable-status reconciliation note explaining why `_STATUS.md` lifecycle
  state should not be used alone to infer runtime implementation completion.
- Explicit list of required human rulings, if any, before `STAB-01` or
  `STAB-02`.

Initial candidate findings to verify:

- Early PRD "not yet full runtime" language is stale relative to source and
  `frontend/docs/harness/runtime_engine_contract.md`.
- Section 9 validation exists as specified IDs but not yet as a stable running
  premerge artifact.
- The `agentSdk` provider is opt-in in source, while strategic docs describe the
  Claude Agent SDK / Anthropic path as first concrete and current shipped path.

### STAB-01 - Section 9 Validation Surface

Goal: make current runtime maturity visible to agents, reviewers, and CI-like
local checks.

Candidate Section 9 IDs:

- `section9.runtime_engine_contract`
- `section9.adapter_turn_engine_event_log`
- `section9.adapter_message_mapper`
- `section9.session_event_replay`
- `section9.settingsources_isolation`
- `section9.permission_overlay_hard_deny_precedence`
- `section9.tool_runtime_read_file`
- `section9.chirality_mcp_status_dependencies`
- `section9.path_containment_hook`
- `section9.instruction_root_protection_hook`
- `section9.tool_result_budget`
- `section9.subagent_governance_hook`

Scope control:

- Do not use Section 9 work to broaden runtime capability.
- Do not rename or destabilize existing Section 8 IDs.
- Section 9 may initially aggregate deterministic unit/contract checks and
  evidence summaries; it does not need live-provider execution unless a tranche
  explicitly selects that.

### STAB-02 - SDK Runtime Readiness

Goal: prove the real SDK path is packageable, governable, and safe enough for a
future default-provider decision.

Required decisions:

- Whether default-provider cutover from current default behavior to SDK-backed
  Anthropic requires a human ruling before implementation.
- Whether packaged SDK subprocess proof is a prerequisite for default-provider
  cutover or only for release-candidate evidence.

Evidence targets:

- `agentSdk` can run with `settingSources: []` by default.
- `CHIRALITY_SDK_SETTING_SOURCES=project` remains the only accepted local
  settings override.
- API keys are supplied only for active turn execution and redacted from logs,
  events, and artifacts.
- SDK visible tools match descriptor/mode policy.
- `Agent` is model-visible only when explicitly requested and delegated child
  eligibility exists.
- Network proof does not silently widen beyond approved policy.
- Packaged app can locate required SDK resources or records a concrete blocker.

### STAB-03 - Session Replay and Artifact Evidence

Goal: make runtime audit evidence useful without making it project truth.

Scope:

- Replay accepted turns, assistant deltas/completions, terminal outcomes, tool
  summaries, permission events, hook events, subagent lifecycle events, and
  artifact references.
- Generalize existing artifact metadata where safe, especially for medium/large
  tool results and redacted overflow.
- Preserve raw-output restraint: raw secrets, raw full diffs, and unbounded raw
  outputs must not enter `HarnessEvent.data`.

Out of scope:

- Importing SDK transcripts as authoritative project truth.
- Creating a hidden project database.
- Treating replay or artifacts as human acceptance evidence.

### STAB-04 - Deterministic Chirality MCP Maturity

Goal: introduce only bounded, deterministic, local Chirality MCP maturity after
validation and evidence surfaces are stable.

Candidate implementation sequence:

1. Status transition MCP planning and tests around `_STATUS.md` lifecycle rules,
   actor authority, forward-only transitions, and approval SHA gates.
2. Dependency writer MCP planning and tests around `Dependencies.csv` v3.1,
   row preservation, enum validation, evidence/source fields, and schema
   warnings.
3. Optional scaffold execution MCP only if preview evidence and write-scope
   policy are accepted.

Denied in this tranche:

- Remote MCP servers.
- Plugin marketplace or plugin installation flow.
- Network-capable MCP tools.
- Direct domain-engine protected path writes.
- Broad tool search exposing denied tools.

### STAB-05 - Governance Refresh and Active Queue

Goal: align current coordination and governance surfaces after stabilization is
accepted.

Scope:

- Update stale wording in governance docs or add supersession notes where direct
  rewrites would be too broad.
- Replace this draft with a final accepted plan or explicitly mark it
  superseded.
- Update `execution/_Coordination/_COORDINATION.md` and
  `execution/_Coordination/NEXT_INSTANCE_PROMPT.md` only after human acceptance
  of the active queue.
- Keep `plans/PLAN_COMPLETION_LOG.md` as landed-tranche history, not authority.

## 6. Validation Policy

Use `docs/VALIDATION_STRATEGY.md` and `docs/RELEASE_QUALITY_GATES.md` to choose
tranche-specific checks.

Default runtime/shared-behavior validation from `frontend/`:

```bash
npm run test
npm run typecheck
npm run harness:validate:premerge
npm run instruction-root:integrity
```

Add security/network validation when provider, API-key, redaction, or outbound
behavior changes:

```bash
npm run proof:network-policy
```

Add packaging evidence when package layout, SDK subprocess behavior, instruction
root resources, or release-candidate evidence is in scope:

```bash
npm run build
npm run desktop:pack
npm run desktop:dist
```

Governance-only tranches use static checks and must explicitly state why runtime
commands were skipped.

## 7. Research Intake Pending

Concurrent domain knowledge database and RESEARCH-agent work is expected to
inform the final development plan. This draft does not depend on those findings.

When RESEARCH outputs arrive, final-plan revision should:

- add cited findings under the affected tranche;
- distinguish local source facts from RESEARCH interpretation;
- resolve conflicts against authority order: governed docs, decomposition and
  deliverable artifacts, source, tests, accepted snapshots, decision records,
  and git history;
- update tranche order only when evidence changes readiness or risk;
- preserve out-of-scope and human-gated boundaries unless a ruling changes them.

## 8. Explicit Out Of Scope

This draft does not authorize:

- concrete non-Anthropic provider implementation or provider routing;
- provider-network expansion beyond current approved policy;
- Pi adapter, fork, package import, Node 22 sidecar, runtime-floor migration, or
  Pi spike;
- remote MCP servers, plugins, remote execution, or marketplace work;
- broad tool search or exposure of denied tools;
- child capability inheritance, unrestricted child tools, or nested subagent
  autonomy;
- direct protected-domain-path writes or domain operation execution;
- Windows/Linux packaging;
- release publication, release-readiness claims, signing, notarization,
  attestation, or external distribution approval;
- lifecycle issuance, professional approval, certification, sealing,
  authentication, or code-compliance acceptance.

## 9. Draft Acceptance Checks

Before this draft can be treated as ready for human review:

- the file exists at
  `projects/chirality-app-dev/plans/PLAN_2026-06-16_runtime_stabilization_draft.md`;
- markdown diff hygiene passes;
- referenced local paths exist or are explicitly future placeholders;
- no runtime source, package manifest, dependency, lockfile, desktop wrapper,
  provider, network, tool-exposure, release, or professional-boundary surface is
  changed by the draft itself;
- the draft remains labeled non-governing;
- skipped runtime checks are recorded as skipped because this artifact is
  governance-only.

## 10. Finalization Rule

This draft becomes an active development plan only after human acceptance or a
replacement plan is recorded. Until then, `execution/_Coordination/_COORDINATION.md`
remains correct: the SCC plan is complete, and no new broad runtime roadmap has
been selected.

