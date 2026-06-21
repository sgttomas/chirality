# App-Dev Contribution to the Tier-0 Bridge Brief

**Date:** 2026-06-21
**From:** chirality-app-dev (`WORKING_ITEMS`)
**For:** the root-level tier-0 integration agent that owns the `chirality-piping` ⇄ `chirality-app-dev`
bridge plan + brief.
**Status:** CROSS-CHECK INPUT — **not tier-0 authority.** App-dev does not author tier-0.

## 0. How to read this dossier (deference notice)

Read tier-0 (`/Users/ryan/ai-env/projects/chirality/agents/AGENT_DOMAIN_ENGINE.md` operative core +
the OpenPipeStress Example Binding, `:709`) and **both repos COLD first**, then use this dossier to
**cross-check your own reading**. Do not read the bridge through app-dev's framing — two project loops
converging is exactly how a blind spot hardens (we proved that twice this week). Where this dossier and
tier-0 disagree, **tier-0 wins**. App-dev's contract drafts (PKG-10) were derived from in-repo
`docs/TYPES.md §11` without citing tier-0, so several app-dev shapes are known-divergent (§2).

All paths under `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/` unless noted.

## 1. What app-dev brings

### 1a. Flow-A pure-TS contract subset (the dependency-free harness spine)

Derived from the actual import graph in `frontend/src/lib/harness/`. **Caveat:** no written `DEC-041`
text was locatable from app-dev (grep returns nothing) — the package boundary here is *import-graph-derived,
not decision-backed*. Confirm or supply the decision of record (see open question 5).

**Ship as-is (fully dependency-free — no React/Next/Electron/Node/SDK):**

| File | Provides |
|---|---|
| `frontend/src/lib/harness/types.ts` | Spine. `UIEvent` 8-member public union (`:206`), request/response/session/opts interfaces, `IAgentSdkManager` (`:304`). Only import is `import type { HarnessEvent }`. |
| `frontend/src/lib/harness/agent-engine-port.ts` | `AgentEnginePort` (`:12`, `startTurn`→`AsyncIterable<UIEvent>` + interrupt), `PUBLIC_UI_EVENT_NAMES` (`:24`). Core of what piping drives. |
| `frontend/src/lib/harness/engine-conformance.ts` | `runEngineConformance` / `runEngineInterruptConformance` (`:156`/`:175`) — validates any port emits a legal public stream. |
| `frontend/src/lib/harness/tool-catalog.ts` | `renderHarnessToolCatalog()` (`:93`), pure markdown over the descriptor registry. |
| `frontend/src/lib/harness/mcp/tool-names.ts` | Chirality MCP naming contract (zero imports): read/mutating/all tool-name tuples + guards. |
| `frontend/src/lib/harness/sdk-version.ts` | `CLAUDE_AGENT_SDK_PACKAGE_VERSION = '0.3.150'`. |
| `frontend/src/lib/harness/errors.ts` | `HarnessError` (`:3`), `asHarnessError` (`:59`). |
| `frontend/src/lib/harness/transcript-replay.ts` | Pure persisted-events → `TranscriptView` transform (type-only imports). |

**Require a pure/impure SPLIT before shipping as contract:**

| File | Pure part (keep) | Impure part (move to runtime side) |
|---|---|---|
| `event-schema.ts` | `HARNESS_EVENT_TYPES` (`:3`, exactly 42), `HarnessEventType` (`:49`), `HarnessEvent` (`:51`) | `createHarnessEvent` (`:62`) uses `node:crypto` `randomUUID` — move out or inject id |
| `tool-descriptor.ts` | `HarnessToolDescriptor` (`:84`) + type vocab, `HARNESS_TOOL_DESCRIPTORS` (`:347`), lookups | `resolveHarnessToolPool` (`:987`) pulls `permission-overlay.ts` (SDK + `node:crypto` + `node:fs`) |

**NOT contract material (runtime/adapter side):** `sdk-options-builder.ts` (`buildSdkOptions` `:81`, imports
the Agent SDK, reads `process.env`) and its transitive impure deps (`permission-overlay`, `chirality-hooks`,
`permission-broker`, `mcp/read-tools`, `subagent-bridge`, `session-events`). A piping integration **calls**
these; it does not re-implement them. Global scan: 1 Next import in the whole harness lib (`http.ts`), zero
React/Electron, Agent SDK in 8 files (all runtime), `node:` in 24.

### 1b. Reusable MCP / gate machinery (runtime side, the bridge's extension points)

- **`runMutatingMcpToolWithEvidence`** — `mcp/read-tools.ts:300-389`. Generic wrapper: resolves descriptor,
  emits `tool.started`, calls `assertMutatingMcpPermission` (`:239-298`, path-policy + permission, 403 on
  non-allow), captures before/after file SHA evidence, persists artifact, emits `tool.completed`
  (`permissionMetadata` + `fileEvidence`) or `tool.failed`. Callers: `statusTransitionTool` (`:512`),
  `dependenciesWriteTool` (`:554`). A bridge mutating tool calls it identically.
- **`buildChiralityMcpTools`** — `read-tools.ts:635-738`. Single assembly point `{context, mode, allowedToolNames}`;
  registers each `tool()` by allow-set. This is where a bridge surfaces a new allow-gated tool.
- **Non-delegable approval-sha humanGate template** — `tool-descriptor.ts:528-532` on `status_transition`:
  `humanGate: { required: true, gate: 'approval-sha', reason: '…HUMAN actor approvalSha evidence.' }`. Typed
  via `HarnessToolHumanGate` (`:96`). A bridge reuses this verbatim for any human-gated transition; it does
  not weaken or auto-satisfy it.

### 1c. Governing keystones a bridge inherits (`docs/CONTRACT.md`)

`K-DOMAIN-1` (`:135`, engines own truth; Chirality governs, is not the solver), `K-DOMAIN-2` (`:136`,
protected paths write-quarantined), `K-DOMAIN-3` (`:137`, ops need `OperationProposal` + human acceptance),
`K-DOMAIN-4` (`:138`, outputs not professional/compliance/external/solver truth), `K-ENGINE-6` (`:57`,
governance/UI/audit/lifecycle/adapter layer — not a standalone harness; keep the extraction an adapter),
`K-ENGINE-3` (`:54`, Anthropic Agent SDK key-aware default; provider expansion human-gated).

## 2. PKG-10 ⇄ tier-0 drift report (TIER-0 CANONICAL)

**Root cause (confirmed):** the corpora were never cross-referenced. `AGENT_DOMAIN_ENGINE.md` is **absent
from both** DEL-10-01/03 `_REFERENCES.md` (they list only `docs/*.md` REF-001..006 + `AGENT_SOFTWARE_DECOMP.md`
REF-007); grep across both `1_Working` folders finds zero references to it. The divergences are the
predictable artifact of deriving from `docs/TYPES.md §11`; several app-dev "TBD" gaps are **false** gaps
tier-0 already resolves.

**Recommended fix:** add `AGENT_DOMAIN_ENGINE.md` (SHA-pinned) to both `_REFERENCES.md` as the tier-0
authoritative source, then re-run the drafts with tier-0 canonical and `docs/TYPES.md §11` as the in-repo
target to reconcile.

### DomainEngineProfile (DEL-10-01)

| Concept | Verdict | app-dev | tier-0 (canonical) | Reconcile to |
|---|---|---|---|---|
| Field naming/casing | DRIFT | camelCase TS iface (Datasheet `:46-58`) | snake_case YAML (`:671-707`,`:360-376`) | TS draft is a derived view; annotate snake_case mapping, don't redefine |
| `engine_type` | MISSING | absent | required (`:369`,`:676`) | Add (MUST) |
| `schema_version`/`profile_version` | MISSING | absent (`engineVersion?` is engine, not schema) | required (`:366`,`:673`,`:677`) | Add both; don't conflate with engineVersion |
| `domain_root_patterns` | MISSING | absent | required (`:370`,`:679`) | Add |
| Path taxonomy | DRIFT | 2 classes (protected/proposal `:51-52`) | 4 classes: authoritative/readable/protected_write/agent_writable (`:371-374`,`:682-692`) | Expand to 4; proposalPaths→agent_writable; add authoritative + readable (readable absent) |
| `artifactTypes` | DRIFT | flat `string[]` (`:53`) | role-classed path sets (`:682-687`) | Model by ownership role, not type-label array |
| operations vs `deterministic_tools` | DRIFT | `operations`, descriptor "TBD" (Spec `:35`) | concrete `deterministic_tools` (id/mode/requires_human_confirmation/schema `:375`,`:694`) | **False gap** — adopt `deterministic_tools` shape |
| `manifestRules` | DRIFT | `unknown`, "TBD" (`:55`) | no profile-level rules; behavior in readable_artifacts + Integration Record | Confirm tier-0-absent; drop or mark Chirality-extension |
| professional_boundary | DRIFT | scalar string (`:56`) | structured `agent_must_not_claim` list (`:376`,`:699-707`) | Upgrade to structured object |
| ProfileStatus lifecycle | DRIFT | no status field | `NONE\|DRAFT\|VALIDATED\|ADOPTED\|STALE\|INVALID` (`:657`,`:378`) | Add. **Tier-0 self-inconsistency:** `:197`/`:830` say `UNKNOWN` not `INVALID` — root agent to rule |
| IntegrationLevel | MISSING | absent | `MANUAL_BRIDGE..EXTERNAL_RESULT_STATE` L0-4 (`:57`,`:162-172`) | Add 5-token enum; OperationProposal = L3 |

### OperationProposal (DEL-10-03)

| Concept | Verdict | app-dev | tier-0 (canonical) | Reconcile to |
|---|---|---|---|---|
| Contract form | DRIFT | typed field-list (Datasheet `:25`) | 8 prose validity criteria (`:393-404`) | Complementary — map each criterion to a field |
| status / `proposal_only` | DRIFT | draft\|ready\|accepted\|rejected\|applied (`:26`) | single `proposal_only` pre-acceptance (`:399`,`:404`) | `proposal_only` umbrella; accepted/applied stay human-gated |
| cite evidence | AGREE | inputRefs/checks/expectedOutputRefs | manifests/warnings/run/comparison IDs/paths (`:400`) | Ensure refs admit manifest/run/comparison IDs |
| assumptions + blockers | MISSING | only `risks` (`:25`) | MUST list unresolved assumptions + blockers (`:401`) | Add field distinct from risks |
| boundary language in-record | TBD | checklist only (Spec `:19`) | record MUST contain boundary language (`:402`) | Add boundary-notice field |
| under agent-writable path | TBD | standalone proposalPaths (`:18`) | MUST live under profile agent_writable_paths (`:403`) | Bind storage to profile path |
| names base state | TBD | no field | SHOULD name base state (`:398`) | Add optional baseState ref |
| Human Agency Map | AGREE | propose-before-apply + human-accept (`:15-16`) | humans accept/reject + approve mutating calls (`:406-417`) | Map status transitions onto rows `:410-416` |

## 3. Fence / gate map (green-today prep vs gated)

Four hard fences confirmed identically across `D-APP-39_RULING_2026-06-20.md:21-27`, `NEXT_INSTANCE_PROMPT.md:71`,
`docs/PLAN.md:444-457` (§11): **F1** provider/network beyond Anthropic; **F2** release/distribution posture;
**F3** R7 domain-engine impl (PKG-10 stays doc-only); **F4** any `CHECKING→ISSUED`.

| # | Action | Fence | Status | Handling |
|---|---|---|---|---|
| 1 | Extract harness lib into a dependency-free **internal** monorepo package | none | **GREEN — prep today** | Internal refactor only; in-scope under Section 4 validation; K-ENGINE-6 keeps it an adapter. Line it must not cross = action 2. |
| 2 | Publish/distribute that package **externally** | F2 | GATED | PROPOSAL packet, BLOCKED |
| 3 | Implement `DomainEngineProfile`/`OperationProposal` **types in `frontend/src`** | F3 | GATED | Editing the doc contracts is fine; standing up source types crosses F3. PROPOSAL/BLOCKED |
| 4 | Add domain MCP tools (e.g. `piping_propose_operation`) | F3 | GATED | OperationProposal-as-tool = R7 impl; Selection Rule 7 stops for a ruling. PROPOSAL/BLOCKED |
| 5 | Live binding / private-data egress to a cloud agent | F1 | GATED (most irreversible) | Provider/network expansion; §11 bars remote exec/MCP. PROPOSAL/BLOCKED |
| 6 | `CHECKING→ISSUED` | F4 | GATED | Deferred under D-APP-19 Option D; one-way. PROPOSAL/BLOCKED |

**Posture (D-APP-39 decision-latitude):** AUTONOMOUS within the fences — resolve forks under the owner's
standing steer and record the call in closeout; never record an agent decision as an owner ruling or claim
an approval-SHA not held; escalate only the material/hard-to-reverse as a PROPOSAL. So action 1 is
decided + executed autonomously; actions 2-6 are PROPOSAL packets, never self-ruled.

## 4. What stays human-reserved on app-dev's side

- **External distribution** of the extracted package (F2).
- **Source types + any domain MCP tool** (F3) — PKG-10 stays doc-only; doc contracts may be edited as
  governance work; implementation waits for a ruling.
- **Live binding / private-data egress to any non-Anthropic / network destination** (F1) — the bridge may
  reuse the existing Anthropic key-aware loopback path (`PLAN.md:351`), nothing more. PRD `FR-089`/`FR-125`
  make unvalidated provider/network expansion a P0 hard-deny over all allows.
- **Any `CHECKING→ISSUED`** (F4) — one-way, deferred.
- **The non-delegable approval-sha gate** (`tool-descriptor.ts:528-532`) — HUMAN-actor approvalSha is
  mandatory; a bridge reuses the template, never weakens it.
- **Truthful attribution** (K-AUTH) across all of the above.

## 5. Open tier-0 questions app-dev needs the root agent to resolve

1. **Profile-drift reconciliation direction.** Confirm tier-0 (`AGENT_DOMAIN_ENGINE.md`) is canonical for
   `DomainEngineProfile`/`OperationProposal` and `docs/TYPES.md §11` is the in-repo target; authorize adding
   `AGENT_DOMAIN_ENGINE.md` (SHA-pinned) to DEL-10-01/03 `_REFERENCES.md` and re-running the drafts. Also
   rule the tier-0 self-inconsistency: `ProfileStatus` is `INVALID` at `:657/:378` but `UNKNOWN` at
   `:197/:830` (app-dev reads `INVALID` as canonical).
2. **INTEGRATION_LEVEL target + staging.** Which of L0-4 is the first target and in what order?
   `OPERATION_PROPOSAL` = L3 — confirm whether L3 is the destination or an intermediate.
3. **Data-residency / egress for live binding** (action 5, F1). Is any private-data egress to a
   cloud/non-Anthropic agent permitted, under what residency constraints? Until ruled, app-dev holds the
   bridge to the existing Anthropic key-aware loopback only.
4. **Fence-3 opening sequencing.** Order/preconditions for (a) source types then (b) domain MCP tools —
   both currently doc-only.
5. **Flow-B / contract versioning home.** Where does the contract package version live and how is it pinned
   across both repos — extend `CLAUDE_AGENT_SDK_PACKAGE_VERSION` / `HARNESS_TOOL_REGISTRY_VERSION`
   (`tool-descriptor.ts:13`), its own package version, or a tier-0-owned scheme? **And supply the `DEC-041`
   decision of record** — app-dev could not locate its text and derived the Flow-A boundary from the import
   graph.
