# Runtime Stabilization Development Plan

**Date:** 2026-06-16
**Status:** ACCEPTED / ACTIVE / GOVERNING (active development queue)
**Acceptance ruling:** `execution/_Coordination/_DECISIONS/D-APP-11_RULING_2026-06-16.md` (human project authority in chat)
**Supersedes as active queue:** `plans/PLAN_2026-06-16_six_node_scc_resolution.md` (closed)
**Product:** Chirality desktop harness and bundled agent operating system
**Working root:** `projects/chirality-app-dev/`
**Prepared by:** `WORKING_ITEMS`
**Evidence basis:** `domains/chirality-app-dev/_Research/RCH_20260616T1830Z_runtime_stabilization/` (derivative research packet)

> **Provenance note.** This plan began as `PLAN_2026-06-16_runtime_stabilization_draft.md`
> and was renamed to `PLAN_2026-06-16_runtime_stabilization.md` on acceptance as the active
> governing queue (D-APP-11). Epistemic status is carried by this status block and by the
> coordination pointers.

This plan is the app-dev development program selected after completion of the runtime
completion plan and the six-node SCC resolution plan. It was accepted by the human
project authority and is now the active development queue. It does **not** by itself
change product requirements, decomposition truth, runtime API, source code,
package/runtime requirements, provider scope, network policy, release-readiness posture,
lifecycle issuance, professional approval, certification, sealing, authentication, or
code-compliance posture. Project truth remains in governed docs, decomposition and
deliverable artifacts, source, tests, evidence records, accepted snapshots, decision
records, and git history. Humans decide all gates.

Runtime logs, SDK transcripts, completion logs, validation artifacts, and the research
packet that informs this plan are derivative evidence or planning material only.

## 1. Purpose

The next program prioritizes **runtime stabilization rather than broad feature
expansion**. The landed runtime now has a provider-adapter spine, an append-only event
schema, a permission overlay with explicit hard-deny precedence, hooks, read/write/Bash
tool surfaces, opt-in Claude Agent SDK execution, and a governed R5 executable subagent
bridge. The program reconciles that landed state with governance and validation, makes
runtime evidence repeatable and machine-readable, proves the opt-in SDK path well enough
to support a future default-provider decision, and matures only bounded, deterministic,
local capability before any further tool, provider, remote-MCP, plugin, or domain-engine
expansion.

The program was scoped from a local-evidence-first research pass over the live repository
and a retrieval mirror (see §13). Where the research corrected an earlier assumption, the
correction is recorded inline.

## 2. Local Baseline

The following baseline is verified against the live tree and tests (2026-06-16):

- `execution/_Coordination/_COORDINATION.md` previously recorded the residual six-node
  strict dependency SCC as closed with no new broad runtime roadmap selected. This plan
  is that newly selected roadmap; the coordination surfaces are updated to point here.
- `plans/PLAN_2026-06-13_runtime_completion.md` is retired as an active queue; it records
  runtime work through `R5-EXEC-001` as landed and remains historical evidence only.
- `plans/PLAN_2026-06-16_six_node_scc_resolution.md` is closed (`scc_count = 0`) and
  non-governing after `SCC-CLOSEOUT-001`.
- `plans/PLAN_COMPLETION_LOG.md` records landed runtime and SCC tranches as historical
  narrative, not authority.
- `frontend/docs/harness/runtime_engine_contract.md` is the best current runtime contract
  baseline (opt-in `agentSdk` path, exposed/denied tool classes, event categories,
  subagent posture, `Packaging BLOCKED_TBD`).
- `frontend/src/lib/harness/` contains the landed runtime surfaces; `frontend/src/lib/`
  also contains the landed `lifecycle/` (status transition engine) and `dependencies/`
  (Dependencies.csv v3.1 reader/writer/linter) engines and `workspace/deliverable-contracts.ts`.
- `frontend/src/__tests__/` contains focused unit/contract tests for the runtime modules.
- `frontend/scripts/validate-harness-section8.mjs`, `validate-harness-section9.mjs`, and
  `validate-harness-premerge.mjs` expose the harness validation surface. Section 9 now
  aggregates 13 canonical deterministic runtime IDs into a stable report-only premerge
  artifact while Section 8 remains the hard premerge gate.

Reconciliation issues confirmed by research (drives STAB-00 and STAB-05):

- Several governance passages describe the harness as lacking runtime primitives that now
  exist in source (PRD §2 assessment, KG-004/005/006/010; PLAN/PRD R2–R5 forward
  roadmap). A minority are genuinely stale; a few are still accurate gaps (persona stub).
- All **53** deliverable `_STATUS.md` files read `Current State: SEMANTIC_READY`
  (uniform 2026-05-20 decomposition value). The v3.2 decomposition remains the topology
  authority, but `_STATUS.md` lifecycle state does **not** reflect runtime implementation
  and must not be read as runtime completion.
- The `agentSdk` provider is opt-in in source (`CHIRALITY_HARNESS_PROVIDER=agentSdk`;
  default is the stub manager), while several strategic docs call the Claude Agent SDK /
  Anthropic path the "current shipped path." This framing should be reconciled and a
  default-provider cutover should not be inferred from it.

## 3. Acceptance and Governing Status

Per the original draft's §10 finalization rule, this plan becomes active only on human
acceptance. That acceptance was given by the human project authority and is recorded in
`execution/_Coordination/_DECISIONS/D-APP-11_RULING_2026-06-16.md`. As a result:

- this plan is the **active development queue**;
- `execution/_Coordination/_COORDINATION.md`, `NEXT_INSTANCE_PROMPT.md`, and `_LATEST.md`
  point to it as the active tranche-selection surface;
- the six-node SCC plan and the runtime completion plan remain closed/retired history.

Acceptance of the *program* does not pre-approve the human-gated rulings inside it
(default-provider cutover, mutating Chirality MCP exposure). Those remain pending in
`_DECISIONS/_REGISTER.md` (§9) and must be ruled before their tranches implement.

## 4. Program Principles

- **Stabilize before expanding:** validation, replay, evidence, packaging, persona, and
  governance reconciliation precede new capability.
- **Unit-proven is not runtime-proven.** Nearly every `agentSdk` "landed" claim today
  rests on a mocked `query()` and scripted-stub conformance fixtures; no real or
  scripted-real SDK turn has executed end-to-end (dev or packaged). The plan treats
  "has a passing unit/contract test" and "completes a real turn" as distinct evidence
  tiers and never lets the former masquerade as the latter.
- **Provider-adapter generality stays strategic**; do not implement concrete
  non-Anthropic providers without a future bounded ruling and plan.
- **Preserve current network policy:** loopback plus the current Anthropic API path.
- **`CHIRALITY_HARNESS_PROVIDER=agentSdk` stays opt-in** unless a later tranche records
  the evidence and ruling needed for a default-provider cutover (D-APP-12).
- **`allowedTools` is insufficient by itself**; execution requires descriptor
  resolution, mode policy, `disallowedTools`, the `canUseTool` permission callback,
  hooks, and evidence capture.
- **Keep raw secrets, raw full diffs, unbounded raw outputs, SDK transcripts, and runtime
  artifacts out of project truth** and out of `HarnessEvent.data`.
- **Canonical IDs/strings come from a single source.** Section 9 IDs come from
  `docs/SPEC.md` §19.3; provider-mode env values come from `runtime.ts`. Any tranche that
  hard-codes a string pulls from the canonical source, not from archived/legacy spellings.
- **Domain-engine profiles and operation proposals remain future-boundary scope** (PKG-10)
  unless explicitly activated by a governed amendment.

## 5. Current-State Matrix (STAB-00 backbone)

Status legend: **LANDED** (implemented + unit/contract-tested), **PARTIAL** (core landed,
a named sub-behavior missing), **GAP** (specified, not implemented), **METADATA-ONLY**
(descriptor/contract reserved, not exposed). Source paths are under
`frontend/src/lib/harness/` unless noted; tests under `frontend/src/__tests__/`.

| # | Capability | Primary source | Tests | Deliverable | Status |
|---:|---|---|---|---|---|
| 1 | AgentEnginePort + engine conformance evaluator | `agent-engine-port.ts`, `engine-conformance.ts` | `lib/engine-conformance.test.ts`, `lib/agent-engine-port.test.ts` | DEL-03-01 | LANDED |
| 2 | Thin TurnEngine + same-session active-turn locking | `turn-engine.ts` | `lib/turn-engine.test.ts` | DEL-03-02 | LANDED |
| 3 | Harness API + SSE compatibility adapter | `app/api/harness/turn/route.ts`, `.../interrupt`, `.../session/*` | `api/harness/*` | DEL-03-03 | LANDED |
| 4 | Interrupt / cancel / terminal outcomes (exit 130) | `claude-agent-sdk-manager.ts`, `turn-engine.ts` | `lib/claude-agent-sdk-manager.test.ts`, `lib/engine-conformance.test.ts` | DEL-03-04 | LANDED |
| 5 | HarnessEvent schema + append-only JSONL | `event-schema.ts`, `session-events.ts` | `lib/session-events.test.ts` | DEL-05-02 | LANDED |
| 6 | Redacted RunLogger / secret hygiene | `run-logger.ts` | via `lib/sdk-message-mapper.test.ts` | DEL-05-03 | LANDED |
| 7 | SdkMessageMapper provider-neutral translation | `sdk-message-mapper.ts` | `lib/sdk-message-mapper.test.ts` | DEL-04-03 | LANDED |
| 8 | SdkOptionsBuilder + `settingSources: []` isolation | `sdk-options-builder.ts` | `lib/sdk-options-builder.test.ts`, `lib/harness-options.test.ts` | DEL-04-02 | LANDED |
| 9 | Permission overlay + explicit hard-deny precedence | `permission-overlay.ts` | `lib/permission-overlay.test.ts` | DEL-06-01 | LANDED |
| 10 | SDK read tool surface + unknown-tool rejection | `tool-descriptor.ts`, `turn-engine.ts` | `lib/tool-descriptor.test.ts` | DEL-06-02 | LANDED |
| 11 | Chirality MCP **read** tools (status/deps/scope/scaffold) | `mcp/read-tools.ts`, `mcp/tool-names.ts` | `lib/chirality-read-mcp.test.ts` | DEL-06-03 | LANDED |
| 12 | Write/Edit + path hooks (containment, instruction-root, symlink) | `chirality-hooks.ts`, `tool-path-policy.ts`, `instruction-root.ts` | `lib/chirality-hooks.test.ts`, `lib/harness-instruction-root.test.ts` | DEL-06-04, DEL-07-01 | LANDED |
| 13 | Bash governance + timeout / no-network policy | `tool-shell-policy.ts` | `lib/chirality-hooks.test.ts`, `lib/permission-overlay.test.ts` | DEL-06-05 | LANDED |
| 14 | Hook lifecycle + **compaction mirror** | `chirality-hooks.ts`, `sdk-message-mapper.ts:818-840` | `lib/chirality-hooks.test.ts`, `lib/sdk-message-mapper.test.ts`, `lib/session-events.test.ts` | DEL-06-06 | LANDED (corrected) |
| 15 | Tool result budgets + overflow artifact spill | `tool-evidence.ts`, `tool-result-artifacts.ts`, `sdk-message-mapper.ts`, `chirality-hooks.ts`, `mcp/read-tools.ts` | `lib/tool-evidence.test.ts`, `lib/tool-result-artifacts.test.ts`, `lib/sdk-message-mapper.test.ts`, `lib/chirality-hooks.test.ts` | DEL-05-05 | LANDED |
| 16 | Runtime replay (append/replay round-trip + summary) | `session-events.ts` (`replayHarnessEvents`) | `lib/session-events.test.ts` | DEL-05-04 | LANDED |
| 17 | Type 2 subagent governance bridge (R5 Option C) | `subagent-bridge.ts`, `subagent-governance.ts`, `agent-runtime-contract.ts` | `lib/subagent-bridge.test.ts`, `lib/harness-subagent-governance.test.ts`, `lib/agent-runtime-contract.test.ts` | DEL-08-04 | LANDED |
| 18 | Subagent child-run **records** (adapter mapping) | `agent-runtime-contract.ts`, `sdk-message-mapper.ts` | `lib/agent-runtime-contract.test.ts`, `lib/sdk-message-mapper.test.ts` | DEL-08-05 | LANDED |
| 19 | Status transition **engine** (forward-only, approval-SHA) | `lib/lifecycle/transition.ts`, `lib/lifecycle/status-parser.ts` | `lib/lifecycle-status.test.ts` | DEL-07-04 | LANDED (engine + route); MCP tool is GAP (row 28) |
| 20 | Dependencies.csv v3.1 reader/writer/linter **engine** | `lib/dependencies/register-writer.ts`, `lib/dependencies/schema.ts`, `lib/workspace/deliverable-contracts.ts` | `lib/dependencies-register-contract.test.ts` | DEL-07-05 | LANDED (engine); MCP writer is GAP (row 28) |
| 21 | Provider selection (default stub; `anthropic`; `agentSdk` opt-in) | `runtime.ts`, `agent-sdk-manager.ts`, `anthropic-agent-sdk-manager.ts`, `claude-agent-sdk-manager.ts` | `lib/harness-runtime.test.ts` | DEL-04-01 | LANDED (opt-in preserved) |
| 22 | **API key supply to SDK for the active turn** | — (not wired) | — | DEL-04-05 | **GAP** (no `ANTHROPIC_API_KEY` injection before `query()`; UI-only key passes presence gate but never reaches the SDK) |
| 23 | **PersonaComposer from instruction root** | `persona-manager.ts` (`StubPersonaManager`) | — | DEL-04-04 | **GAP** (still one-line stub; `runtime.ts:62` instantiates the stub) |
| 24 | Section 8 running-app validation + stable premerge artifact | `scripts/validate-harness-section8.mjs`, `scripts/validate-harness-premerge.mjs` | `scripts/*` | DEL-09-01 | LANDED |
| 25 | **Section 9 runtime validation IDs (aggregator)** | `scripts/validate-harness-section9.mjs` | targeted deterministic Vitest groups | DEL-09-02 | LANDED (report-only premerge integration) |
| 26 | macOS DMG packaging + SDK subprocess probe | `package.json` build, `scripts/verify-instruction-root-integrity.mjs` | `scripts/dmg-packaging-policy.test.ts`, `scripts/verify-instruction-root-integrity.test.ts` | DEL-09-04 | PARTIAL (DMG path exists; **no `asarUnpack` for the SDK**; subprocess proof `BLOCKED_TBD`) |
| 27 | Network policy proof | `scripts/run-network-policy-proof.mjs` | `scripts/build-network-policy.test.ts` | DEL-09-06 | LANDED for default/`anthropic`; `agentSdk`-mode outbound **unproven** |
| 28 | **Mutating Chirality MCP tools** (`status_transition`, `deps_write`) | descriptor metadata only (`tool-descriptor.ts`) | — | DEL-07-04 / DEL-07-05 (MCP half) | **METADATA-ONLY** (STAB-04) |

**Deliverable-status reconciliation note (STAB-00 output).** Every deliverable
`_STATUS.md` reads `SEMANTIC_READY`, which is a *decomposition-process* state set on
2026-05-20, not a runtime-implementation state. The matrix above is the authoritative
runtime-implementation view; the decomposition remains the **topology** authority only.
`_STATUS.md` files are **not** mass-edited by this plan: forward-only transitions are
actor-authorized and SHA-gated, and rewriting them is itself a human-gated lifecycle
action. The reconciliation is recorded as this derived note plus the matrix, not as bulk
status edits.

## 6. Tranche Spine

Tranche numbers are identities, not a strict linear order; see §10 for the dependency DAG.

| Tranche | Purpose | Primary scope | Minimum validation |
|---|---|---|---|
| `STAB-00` Baseline Reconciliation & ID Canonicalization | **LANDED 2026-06-16** on `codex/chirality-app-work`. | Artifacts: `plans/artifacts/runtime_capability_matrix.md` and `plans/artifacts/stab00_reconciliation_disposition.md`. Residual handoff: STAB-01 uses canonical Section 9 IDs; STAB-06 consumes the disposition list. | Governance gate; see `plans/PLAN_COMPLETION_LOG.md`. |
| `STAB-01` Section 9 Validation Surface | **LANDED 2026-06-16** on `codex/chirality-app-work`. | Added `validate-harness-section9.mjs` for 13 canonical deterministic IDs, npm script, stable ignored artifact path, docs, and additive report-only premerge integration. Residual handoff: STAB-03 item B and STAB-04 can consume the Section 9 validation namespace; Section 9 should flip from report-only to hard-fail after one stable cycle. | Runtime premerge gate; see `plans/PLAN_COMPLETION_LOG.md`. |
| `STAB-02` SDK Runtime Readiness & Cutover Decision | Prove the opt-in SDK path well enough for a future default decision. | (a) wire API-key injection for the active turn + redaction test; (b) one dev-build real/scripted `agentSdk` turn; (c) `agentSdk`-mode network proof; (d) packaged subprocess probe (`asarUnpack` + HOME + DMG). Prepare D-APP-12 default-cutover packet. | Runtime premerge + security/network gate; packaging gate (`build`, `desktop:pack`, `desktop:dist`) for (d). |
| `STAB-03` Session Replay, Artifact Evidence & Subagent Records | **LANDED 2026-06-16** on `codex/chirality-app-work`. | Generalized descriptor-driven artifact overflow across hook, MCP, and async SDK mapper paths; added replay summaries and full synthetic event-class replay coverage; added bounded write/edit diff summaries; wired adapter-observed child-run records into SDK task events; added direct tool-evidence/artifact tests and Section 9 coverage. Residual handoff: STAB-02 real/scripted turns can later exercise the same replay/artifact surfaces against live SDK evidence. | Runtime premerge gate; see `plans/PLAN_COMPLETION_LOG.md`. |
| `STAB-04` Deterministic Chirality MCP Maturity | Expose only bounded mutating Chirality MCP tools after validation hardening. | SDK-behavior probe (does `canUseTool`/hooks fire for in-process MCP tools?); then `status_transition` → `deps_write` (→ optional `scaffold_exec`) over the **already-landed** lifecycle/deps engines, with an in-handler diff-evidence wrapper. Requires D-APP-13. | Permission/tool gate + lifecycle/deps tests + denial tests; `typecheck`; `test`; one running-app round-trip check; premerge. |
| `STAB-05` Persona Composer from Instruction Root | Replace the persona stub so a real turn is meaningful. | Implement `PersonaComposer` from instruction-root governance, active persona, working-root policy, mode, and tool-surface composition; content-hash + boot fingerprint; replace `StubPersonaManager` wiring in `runtime.ts`. | Persona composition tests, content-hash tests, `typecheck`, `test`; premerge (boot/turn behavior changes). |
| `STAB-06` Governance Refresh & Active Queue | Convert accepted outcomes into governance/coordination surfaces. | Apply the STAB-00 disposition list (factual corrections + dated supersession notes only); reflect D-APP-12 ruling; refresh coordination; record program completion. | Governance gate. Runtime commands skipped unless executable behavior changed. |

## 7. Tranche Detail

### STAB-00 — Baseline Reconciliation & ID Canonicalization

Status: **LANDED 2026-06-16**.

Outputs:

- `plans/artifacts/runtime_capability_matrix.md`
- `plans/artifacts/stab00_reconciliation_disposition.md`

Residual handoff:

- STAB-01 must use canonical Section 9 IDs from `docs/SPEC.md` Section 19.3 and
  `docs/PRD.md` Section 12.4.
- STAB-06 consumes the disposition list for factual corrections and dated supersession
  notes only; policy changes remain gated by D-APP-12/D-APP-13.
- STAB-00 corrected the earlier guidance assumption that legacy `sdk_*` aliases live only
  under `.archive`; they also occur in live deliverable-local kits, so new validation work
  must bind to the canonical `adapter_*` IDs without mass-editing lifecycle artifacts.

### STAB-01 — Section 9 Validation Surface

Status: **LANDED 2026-06-16**.

Outputs:

- `frontend/scripts/validate-harness-section9.mjs`
- `frontend/artifacts/harness/section9/latest/summary.json` (ignored stable artifact)
- `harness:validate:section9` npm script
- additive `HARNESS_PREMERGE_SECTION9_*` report-only premerge machine lines
- validation documentation updates in `docs/` and `frontend/docs/harness/`

Residual handoff:

- STAB-03 item B may feed malformed-tail replay diagnostics into the Section 9 namespace.
- STAB-04 may consume the Section 9 namespace after its SDK-behavior probe and D-APP-13
  ruling.
- Section 9 remains report-only in premerge for the initial stable cycle; later work should
  flip it to hard-fail once accepted.

### STAB-02 — SDK Runtime Readiness & Default-Provider Cutover Decision

Goal: prove the real SDK path is functional, governable, and safe enough for a future
default-provider decision. **Internal ordering matters** — steps (a)–(c) are unblocked
today; step (d) is the `BLOCKED_TBD` packaging gate.

- **(a) API-key injection for the active turn (load-bearing GAP).** The `agentSdk` path
  never sets `process.env.ANTHROPIC_API_KEY` to the resolved key before `query()`;
  `turn-engine.ts` only *presence-checks* the key. A UI-safeStorage-only key passes the
  503 gate but never reaches the SDK, so the path cannot complete a real turn. Implement
  set-before-`query()` / restore-after in `ClaudeAgentSdkManager` (or `TurnEngine` before
  delegating), per the followups doc §12. Add a test asserting (i) `query()` sees the key
  via env, (ii) the prior env is restored, (iii) the key value never appears in any
  appended `HarnessEvent`. Note redaction is value-based: if the key is never wired,
  redaction has nothing to match — so (a) and the redaction test must land together.
- **(b) Dev-build real/scripted agentSdk turn.** Execute at least one non-packaged
  `agentSdk` turn (real or scripted-real, offline-safe) so key-injection and
  no-network-widening are observed without packaging risk. This is a new evidence target;
  current tests inject a mock `query()` only.
- **(c) agentSdk-mode network proof.** Extend `proof:network-policy` to run a turn with
  `CHIRALITY_HARNESS_PROVIDER=agentSdk`, asserting only loopback + `api.anthropic.com`;
  record the CONF-002 OCSP/CRL carve-out status.
- **(d) Packaged subprocess probe (resolves `BLOCKED_TBD`).** Add electron-builder
  `asarUnpack` for `node_modules/@anthropic-ai/claude-agent-sdk/**`; `build` →
  `desktop:pack` (`--dir`) probe, launch, run one read-tool `agentSdk` turn, confirm the
  SDK subprocess resolves from `app.asar.unpacked` and the transcript lands under a
  resolvable HOME; extend `instruction-root:integrity` to assert SDK presence in the
  bundle; then `desktop:dist` and repeat. If still failing, record the exact resolution
  error as the documented blocker — do **not** claim landed.

Default-provider cutover decision (D-APP-12, §9): keep `agentSdk` opt-in until (a)–(d)
plus Section 8 and Section 9 are green. **Packaged subprocess proof is a hard prerequisite
for default cutover** (recommended), not merely release-candidate evidence, because the
SDK runs as a CLI subprocess with asar/HOME/signing risk. Versions remain pinned
(`claude-agent-sdk 0.3.150`, `@anthropic-ai/sdk 0.93.0`).

### STAB-03 — Session Replay, Artifact Evidence & Subagent Records

Status: **LANDED 2026-06-16**.

Outputs:

- descriptor-driven artifact overflow in hook, Chirality read MCP, and async SDK mapper
  paths;
- replay summaries with event count, malformed-line count, event-type histogram, and
  first/last timestamps;
- bounded Write/Edit diff summaries with byte deltas and added/removed line counts, with
  no full diff text stored in `HarnessEvent.data`;
- adapter-observed child-run records embedded in SDK task lifecycle events;
- direct `tool-evidence` and `tool-result-artifacts` tests included in Section 9
  `tool_result_budget` validation.

Residual handoff:

- STAB-02 real/scripted SDK turns can later exercise these replay/artifact surfaces against
  live SDK evidence.
- Runtime logs, artifacts, replay summaries, and child-run records remain derivative
  evidence only; they are not project truth or human acceptance evidence.

### STAB-04 — Deterministic Chirality MCP Maturity

Goal: introduce only bounded, deterministic, local mutating Chirality MCP tools after
validation/evidence surfaces are stable. **The write engines already exist and are
unit-tested** (`lib/lifecycle/transition.ts`, `lib/dependencies/register-writer.ts`,
`lib/workspace/deliverable-contracts.ts`); this tranche is bounded **MCP exposure +
in-handler evidence**, not new write logic.

Prerequisite probe (sequencing dependency, not a detail): empirically confirm whether the
pinned SDK invokes `canUseTool` and `PreToolUse`/`PostToolUse` hooks for in-process
`mcp__chirality__*` tools, or only for built-ins. If hooks/`canUseTool` do **not** fire
for in-process MCP tools, hard-deny enforcement and before/after diff evidence must live
entirely in a new in-handler wrapper (`runMutatingMcpToolWithEvidence`) that snapshots
target-file SHA + byte length, emits `tool.started`/`permission`/`completed` with
`recordsDiff` metadata, and stores **only** metadata (mirroring the read-MCP redaction
tests).

Implementation sequence (each gated on STAB-01 validation namespace + the probe; mutating
tools never default-on):

1. **`status_transition`** (`mcp__chirality__status_transition`): new descriptor
   (`surface: 'chirality-mcp'`, `permissions: ['workspace-write']`,
   `pathScope: 'project-root-write'`, `idempotence: 'mutating'`, `recordsDiff: true`,
   `humanGate.required: true`); calls `transitionDeliverableStatus`; reuses
   `transition.ts` gates verbatim. Tests: happy path + denials (`UNAUTHORIZED_ACTOR`,
   `BACKWARD_TRANSITION`, `TRANSITION_NOT_ALLOWED`, `APPROVAL_SHA_REQUIRED`/
   `INVALID_APPROVAL_SHA`), path/instruction-root/symlink denial, permission deny in
   `readOnly`/`ask`, evidence redaction, and a conformance assertion that the tool is
   denied unless requested in `workspaceWrite` mode.
2. **`deps_write`** (`mcp__chirality__deps_write`): calls `writeDeliverableDependencies`
   (passes `previousRows` for row/satisfaction preservation); reuses register-writer v3.1
   validation + warnings. Tests: schema/enum/classification/provenance/target failures,
   duplicate-ID rejection, invalid satisfaction transition, row preservation,
   schema-warning surfacing, host-deliverable-ID enforcement, containment/redaction/
   permission parity.
3. **Optional `scaffold_exec`**: only if scaffold-preview evidence + write-scope policy
   are accepted; otherwise default-denied.

Requires **D-APP-13** (§9) to flip these from metadata-only to exposed, and rulings on
whether the MCP tool may perform human-gated (`CHECKING`/`ISSUED`) transitions given an
`approvalSha` and on actor identity.

Denied in this tranche (asserted in tests): remote MCP servers; plugin marketplace/install;
network-capable MCP tools; domain-engine protected-path writes; broad tool search exposing
denied/reserved tools.

### STAB-05 — Persona Composer from Instruction Root

Goal: replace `StubPersonaManager` so a default or opt-in turn produces a governed,
instruction-root-driven system prompt. This is a confirmed live gap (DEL-04-04, SOW-017,
PRD KG-002) that no other tranche owned; real persona quality also makes the STAB-02
default-cutover decision meaningful.

Scope: implement `PersonaComposer` composing instruction-root governance, active persona,
working-root policy, runtime mode, and tool-surface posture into the system prompt;
content-hash the composed persona and surface it in boot/turn evidence (boot fingerprint);
replace the `StubPersonaManager` wiring in `runtime.ts`. Preserve the rule that the
composed prompt carries no professional-approval or release-readiness claims.

Tests: persona content-hash stability, instruction-root resolution + typed missing-resource
failure, mode/tool-surface composition, and a boot-fingerprint assertion. This is an
implementation slice within already-approved scope; it needs no new human ruling beyond
program acceptance, but should land before the D-APP-12 default-cutover ruling.

### STAB-06 — Governance Refresh & Active Queue

Goal: align governance and coordination after stabilization outcomes are accepted.

Scope:

- Apply the STAB-00 disposition list: **factual corrections in place** (env-value wiring
  errors in PRD FR-027/FR-070, PLAN R1, SPEC §19.4) and **dated supersession notes** for
  assessment text (PRD §2, KG-004/005/006/010, "current shipped path" framing,
  PLAN/PRD R2–R5 roadmap). Preserve the persona-stub clause until STAB-05 lands.
- **Do not make policy changes in place.** Any change that declares the SDK the default
  provider, broadens network/provider scope, or alters professional-boundary posture
  requires its governing ruling (D-APP-12) first. If a redline would change policy rather
  than correct a fact, it is deferred behind a supersession note, not written.
- Reflect the D-APP-12 cutover ruling once recorded.
- Refresh `execution/_Coordination/_COORDINATION.md`, `NEXT_INSTANCE_PROMPT.md`, and
  `_LATEST.md` to the post-program active queue; keep `plans/PLAN_COMPLETION_LOG.md` as
  landed-tranche history; mark this plan complete or hand off to the next selected program.

## 8. Tranche Maintenance

This plan is a selection instrument, not a history. When an item lands, compress its row
to one line with: `LANDED <date>`; tranche id or commit; residual handoffs; validation
pointer; and a link to `plans/PLAN_COMPLETION_LOG.md`. Move narrative detail to the
completion log. Partially landed rows keep remaining scope here and move landed detail to
the log. Decision rows carry only state, packet pointer, and ruling pointer.

## 9. Required Human Rulings (Decision Register Additions)

Recorded in `execution/_Coordination/_DECISIONS/_REGISTER.md`:

| ID | Decision | Blocks | State |
|---|---|---|---|
| `D-APP-11` | Accept the Runtime Stabilization program as the active development queue. | Selection of this plan as the active queue; coordination re-pointing. | **RULED** 2026-06-16 (this plan's acceptance). |
| `D-APP-12` | Default-provider cutover from the current default to the SDK-backed Anthropic path. | Any change making `agentSdk` the default; any doc stating the SDK is the active default. | **AWAITING_RULING** — packet prepared in STAB-02 once (a)–(d) + Section 8/9 are green; packaged-subprocess proof recommended as a hard prerequisite. |
| `D-APP-13` | Exposure of bounded mutating Chirality MCP tools (`status_transition`, `deps_write`) from metadata-only to `workspaceWrite`-gated, incl. whether the tool may perform human-gated (`CHECKING`/`ISSUED`) transitions and the required actor identity. | STAB-04 implementation. | **NOT_PREPARED** — packet prepared when STAB-04 is selected. |

Tranches **not** requiring a new ruling beyond D-APP-11: STAB-00, STAB-01, STAB-03,
STAB-05, and the STAB-02 readiness work (a)–(d), which harden/validate already-approved
surfaces. STAB-06 makes only factual corrections + supersession notes; any policy change
it would otherwise make is gated behind D-APP-12.

The `_COORDINATION.md` "Human-Ruling Stops" remain in force: stop and surface a ruling
request before changing product/strategic runtime policy, outbound network or shipped
provider scope, write/edit/bash/tool-execution exposure beyond the active plan item, the
project-truth model, or professional-boundary/release-readiness posture.

## 10. Sequencing and Dependencies

```
STAB-00  (prerequisite: canonical IDs + reconciled baseline)
  ├─► STAB-01  (Section 9; hard-codes canonical IDs; lowest-risk, earliest)
  ├─► STAB-06  (consumes STAB-00 disposition list; runs last among doc edits)
  └─► (informs all)

STAB-02  (a → b → c → d internal order; a–c unblocked now, d = packaging gate)
  └─► D-APP-12 cutover ruling AFTER (a)–(d) + Section 8 + Section 9 green + STAB-05

STAB-01 ──► STAB-03 item B (malformed-tail feeds Section 9)
STAB-01 ──► STAB-04 (needs a validation namespace/ID) ──► after SDK-behavior probe
STAB-02 real-turn artifacts ──► STAB-03 (validate replay against real, not just scripted)
STAB-05 (persona) ──► should precede the D-APP-12 cutover ruling
```

Recommended execution order: **STAB-00 → STAB-01 → (STAB-03 ∥ STAB-05) → STAB-02 →
STAB-04 → STAB-06**, with STAB-02 step (d) and D-APP-12 sequenced after Section 9 is green
and STAB-05 has landed. STAB-04 may begin its SDK-behavior probe in parallel once STAB-01
provides the validation namespace.

## 11. Validation Policy

Use `docs/VALIDATION_STRATEGY.md` and `docs/RELEASE_QUALITY_GATES.md` to choose
tranche-specific checks. Default runtime/shared-behavior validation from `frontend/`:

```bash
npm run test
npm run typecheck
npm run harness:validate:premerge
npm run harness:validate:section9
npm run instruction-root:integrity
```

Add security/network validation when provider, API-key, redaction, or outbound behavior
changes (STAB-02, STAB-04):

```bash
npm run proof:network-policy
```

Add packaging evidence when package layout, SDK subprocess behavior, instruction-root
resources, or release-candidate evidence is in scope (STAB-02 step d):

```bash
npm run build
npm run desktop:pack
npm run desktop:dist
```

Governance-only tranches (STAB-00, STAB-06) use static checks and must explicitly state
why runtime commands were skipped.

## 12. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| "Unit-proven" mistaken for "runtime-proven" for the SDK path | STAB-02 step (b) requires a real/scripted dev-build turn before any cutover; D-APP-12 gated on (a)–(d). |
| API key never reaches the SDK (load-bearing gap) | STAB-02 step (a) lands key-injection + redaction test together before (b)–(d). |
| ID/string drift (adapter_/sdk_/_deny_first; `anthropic` vs `agentSdk`) | STAB-00 canonicalizes; STAB-01 and STAB-06 pull from `SPEC.md` / `runtime.ts` only. |
| New Section 9 aggregator destabilizes the Section 8 gate | Separate TMP root + artifact path; additive premerge; report-only for one cycle then hard-fail. |
| `canUseTool`/hooks may not fire for in-process MCP tools | STAB-04 runs an SDK-behavior probe before committing the wrapper-only diff-evidence design. |
| Packaging blocker (asar/HOME/signing) blocks default cutover | STAB-02 step (d) treats a passed packaged-subprocess turn as a hard prerequisite or records a concrete blocker. |
| Editing PRD/PLAN/SPEC drifts policy | STAB-06 limits to factual corrections + dated supersession notes; policy changes gated behind D-APP-12. |
| `_STATUS.md` mass-edit triggers lifecycle gates | No bulk edits; reconciliation captured as a derived note + matrix; topology authority preserved. |

## 13. Evidence Basis (Research Provenance)

This plan was scoped from a research pass (eight evidence streams + a reconciliation
critic that performed live spot-checks against the live tree). The derivative research
packet is stored under
`domains/chirality-app-dev/_Research/RCH_20260616T1830Z_runtime_stabilization/`
(RESEARCH_NOTE, Evidence_Map.csv, Query_Log.csv, Open_Questions.csv, HANDOFF_STATE.md).
It is a derivative package, not accepted decomposition truth; it aids discovery and does
not replace governed docs, source, tests, or rulings. Material corrections the critic
verified live and that this plan adopts:

- `context.compaction` mirror is LANDED (`sdk-message-mapper.ts:818-840` + tests), not
  partial → it is a Section 9 ID (13-ID first cut, not 12).
- The `agentSdk` API-key supply gap is real and load-bearing → STAB-02 step (a).
- `createAdapterObservedChildRunRecord` has zero callers → the genuine subagent PARTIAL
  (DEL-08-05) → STAB-03 item E.
- `StubPersonaManager` is still the live persona path → STAB-05.

## 14. Explicit Out of Scope

This plan does not authorize:

- concrete non-Anthropic provider implementation or provider routing;
- provider-network expansion beyond current approved policy;
- Pi adapter, fork, package import, Node 22 sidecar, runtime-floor migration, or Pi spike;
- remote MCP servers, plugins, remote execution, or marketplace work;
- broad tool search or exposure of denied/reserved tools;
- child capability inheritance, unrestricted child tools, or nested subagent autonomy;
- direct protected-domain-path writes or domain operation execution (PKG-10);
- Windows/Linux packaging;
- release publication, release-readiness claims, signing, notarization, attestation, or
  external distribution approval;
- lifecycle issuance, professional approval, certification, sealing, authentication, or
  code-compliance acceptance.

## 15. Finalization and Maintenance Rule

This plan is the active development queue as of its acceptance ruling (D-APP-11). It is
maintained per §8. When all tranches land (or the human selects a replacement program),
update `_COORDINATION.md`/`NEXT_INSTANCE_PROMPT.md` to the next active queue, move landed
narrative to `plans/PLAN_COMPLETION_LOG.md`, and mark this plan closed/non-governing.
Human acceptance remains required for every gate inside it; D-APP-12 and D-APP-13 stay
pending until ruled.
