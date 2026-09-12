# CONTRACT — Invariant Catalog

**Status:** vNext governance rewrite aligned to the approved `docs/PRD.md` dated 2026-05-20
**Date:** 2026-05-20
**Product:** Chirality desktop harness and bundled agent operating system
**Applies to:** Chirality App vNext runtime, docs, frontend implementation, packaged app, and governed project workspaces
**Amended:** Amended under D-GOV-43 (A2), 2026-09-12: daemon, admission, supplier, event-schema and shared-runtime clauses revised to the application-owned Runtime service; K-CONSENT-1 and K-RESIDENCY-1 retired in §4

This document is the authoritative catalog of binding invariants for Chirality App. Invariants listed here are enforceable constraints that agents, tooling, implementation code, governance documents, human processes, and release operations must respect. Enforcement may occur in code, tests, release checks, instructions, human gates, or the reliance-boundary register. Prompt text alone is not sufficient enforcement for P0 safety, audit, filesystem, or human-gate boundaries.

Invariant IDs (`K-*`) are stable and never reused. Retired invariants move to §4 with retirement rationale.

## Current Codex-only MVP release basis

For the current MVP release, Codex is the sole model engine. Claude/Anthropic and Pi/oMLX descriptions, default-provider rules and engine-specific proof records below describe compatibility history; they do not require shipping or enabling those engines, and their historical qualification does not establish Codex qualification. Existing conversation history remains readable without reactivating unavailable providers or inheriting their authority.

Codex account sign-in and native Plan Mode are required. Under D-GOV-43 (A2, 2026-09-12) the App hosts the stock, lockfile-pinned `codex app-server` (npm `@openai/codex`) inside a Runtime service that the App starts, owns and stops as a child process; no supplier admission, certification, payload hashing or identity binding exists under any name. Ordinary software integrity applies: the lockfile pin, bundle signing and notarization, renderer isolation, validated IPC and no credential material in the renderer. Credentials are custodied by Codex in Chirality's effective Codex home; the user signs in through Codex's own flow. K-PACKAGE-1 remains unchanged; K-NET-1 and K-RELEASE-1 are read with D-GOV-43 items 1 and 4. Source tests, controlled adapters and package generation do not substitute for required actual packaged provider and native lifecycle evidence. Publication remains separately human-authorized.

Release artifact identity is the explicitly recorded candidate version in frontend/package.json and both root version fields of frontend/package-lock.json. `Chirality-<candidate-version>-arm64.dmg`, the actual App Info.plist identity and the candidate evidence must agree. This amendment selects no version.

---

## 1. Invariant Catalog

### 1.1 Hierarchy, Identity, and Project State

| ID | Invariant | Enforcement |
|---|---|---|
| **K-PRD-1** | `docs/PRD.md` is the approved vNext product-direction source for the current runtime posture. The synchronized governance set controls operations once updated. | Governance review; document traceability; change-control review. |
| **K-HIER-1** | Projects are decomposed as flat **packages containing deliverables**. Packages do not nest; there is no phase or sub-package layer inside the project hierarchy. | PROJECT_DECOMP; scaffold service; deliverable scanner; human review. |
| **K-ID-1** | Stable identifiers are identity. Package IDs, deliverable IDs, dependency IDs, scope IDs, objective IDs, session IDs, turn IDs, and event IDs persist across renames, path changes, and UI labels. | SPEC/TYPES; scanners; event schema; dependency writer; human review. |
| **K-PATH-1** | Path is a physical projection of identity, not identity itself. Runtime records and project files must preserve stable IDs when paths change. | Session events; `_CONTEXT.md`; dependency registers; scanners. |
| **K-FS-1** | Project truth lives in plain files under the working root and accepted git history, not in hidden app state, chats, SDK transcripts, model context, vendor systems, or Work/Agents Coordination Panel projections. Rendering or locally organizing a plan, task, status, assignment, session, or relationship does not create project truth; the admitted source remains controlling and missing, stale, conflicting, or unrecorded facts remain explicit. | DIRECTIVE; SPEC; runtime session store; projection source-class/currency/stale/unknown tests; human review; git workflow. |
| **K-GIT-1** | Accepted project decisions bind to versioned files. Gate-relevant decisions not represented in git-tracked project artifacts are not reliance evidence. | Human gate review; CHANGE workflow; release discipline. |
| **K-NOMEM-1** | No hidden memory may become authoritative project state. Runtime and UI convenience state is allowed only when explicitly non-authoritative. Dialogue drafts, explicit next-turn context references, artifact anchors, layout/panel state, and selected replay references store presentation or references only; visible artifacts are not automatic model context, conversational prose is not a structured work record, and selected replay cannot inherit or mutate primary-session state. | Runtime contracts; UI local-state and migration policy; session storage rules; draft/context/replay-separation tests. |

### 1.2 Human Authority, Approval, and Professional Boundaries

| ID | Invariant | Enforcement |
|---|---|---|
| **K-AUTH-1** | Only humans author binding approval records. No agent, SDK, tool, runtime event, validator, or domain adapter may claim to certify, approve, sign, seal, issue, transmit, or externally validate work for reliance. | Agent instructions; UI copy; status transition API; human review; release checks. |
| **K-AUTH-2** | Human approvals bind to specific content evidence, normally a git SHA. Content changes after approval void the approval until re-reviewed. | `_STATUS.md` transition rules; CHANGE workflow; human review. |
| **K-BIND-1** | Binding and non-binding records must not be conflated. Drafts, proposals, summaries, runtime transcripts, projected plans/tasks/statuses/assignments, and locally annotated coordination views are not approval records. Structured Work items must expose source class/reference, status basis, currency, and recorded responsible or related references; runtime completion is not deliverable acceptance, and a selected-session replay is observational and read-only. | DIRECTIVE; SPEC; UI language; project file templates; provenance/exact-link/no-panel-approval/replay-separation tests. |
| **K-GATE-1** | Human gates are non-delegable. CHECKING, ISSUED, domain-operation acceptance, and other reliance-affecting states require accountable human evidence. | Status transition API; operation-proposal workflow; human review. |
| **K-PROF-1** | Chirality must not claim code compliance, external validation, solver truth, or professional adequacy by itself. | PRD acceptance checks; DIRECTIVE; UI/documentation review. |

### 1.3 Instruction Root and Working Root Separation

| ID | Invariant | Enforcement |
|---|---|---|
| **K-ROOT-1** | Instruction root and working root are separate. The working root must not be inside the instruction root. | `/api/working-root/validate`; instruction-root resolver; packaging tests. |
| **K-ROOT-2** | Ordinary project execution must not mutate the instruction root. Instruction-root writes require governed release/change operations. | Chirality hooks; path containment; packaging/integrity checks; human review. |
| **K-ROOT-3** | The working root is the only ordinary location where agents may write project truth. | Tool path policy; MCP wrappers; hook denials; git review. |
| **K-PACKAGE-1** | Packaged builds must contain the required instruction-root resources and verify integrity before distribution. | `instruction-root:integrity`; `desktop:dist`; manual release verification. |

### 1.4 Runtime Engine Boundary and Provider/SDK Governance

| ID | Invariant | Enforcement |
|---|---|---|
| **K-CORE-1** | Core runtime APIs, events, tests, and records use Chirality terms. Provider/SDK-specific terms are translated at adapter boundaries. | `EngineAdapter`; event-schema tests; API review. |
| **K-ENGINE-1** | Chirality owns `AgentEnginePort` / `RuntimeEngineContract`; provider and SDK APIs do not define public harness semantics. | Runtime contract docs; engine conformance tests; adapter boundary. |
| **K-ENGINE-2** | Any provider/SDK-backed adapter must pass engine conformance tests before becoming the default production path. | `EngineConformanceSuite`; Section 9 validation; CI. |
| **K-ENGINE-3** | External SDKs and providers are implementation substrates behind Chirality adapters, not product identity or governance authority. Codex is the sole current MVP engine under the owner release direction. The engine is the stock, lockfile-pinned Codex App Server owned by the App's Runtime service child; sign-in is through Codex's own flow; no ambient fallback or automatic egress is permitted. Earlier Claude/Anthropic key-aware default and Pi/oMLX paths remain compatibility history, not current engine selections. | Current release basis; D-GOV-43 (A2); lockfile pin; adapter implementation and the S-1 to S-8 checks. |
| **K-ENGINE-4** | Public APIs, `UIEvent`, `HarnessEvent`, session storage, permission decisions, and governance records must not become provider/SDK-shaped except as adapter metadata. | Type tests; mapper tests; event-schema review. |
| **K-ENGINE-5** | A governed fallback/custom-runtime path must remain available if a product-critical boundary cannot be satisfied or verified through the current adapter. | R0/R1 adapter probe; reliance-boundary register; plan updates. |
| **K-ENGINE-6** | Chirality builds a governance, UI, audit, lifecycle, and adapter layer **over** provider harness mechanics — not a standalone general agent harness, and not feature parity with Claude Code, Pi, or Codex. Generic harness primitives are reused only behind Chirality-owned contracts. D-APP-72 / SCA-APP-002 authorizes one bounded exception to the historical Pi-reference-only posture: Pi `0.80.10` may run in-process as an opt-in second adapter over authenticated loopback oMLX for a governed read-only Agent 2 child after the Electron `43.2.0` prerequisite passes (D-APP-98 successor authority; D-APP-72's `43.1.1` is historical). Every other provider/harness expansion requires a fresh governed tranche. | DIRECTIVE 2.8; PLAN §11 fences; D-APP-01/02/03 historical rulings; D-APP-72; decision register; product copy review. |
| **K-RELIANCE-1** | Product-critical safety, audit, filesystem, lifecycle, transcript, settings, subagent, and human-gate boundaries must be mapped in the reliance-boundary register. | R0/R1 deliverables; conformance tests; governance review. |
| **K-RELIANCE-2** | P0 reliance boundaries cannot be prompt-only or opaque provider/SDK-default-only. | Reliance-boundary review; adapter probe; runtime tests. |
| **K-SDK-1** | Shipped builds for the Claude Agent SDK / Anthropic adapter must not load ambient user/global Claude Code settings or local `.claude/settings.local.json`. | `settingSources: []`; SDK options builder tests; release verification. |
| **K-SDK-2** | Provider/SDK adapter behavior must be version-pinned and regression-tested on upgrade. | package lock; adapter probe; conformance suite; release notes. |
| **K-SDK-3** | SDK transcripts are resume/debug artifacts, not canonical Chirality audit records unless explicitly imported into `HarnessEvent` form. | Session store; event mirror; replay code; documentation. |
| **K-SDK-4** | Product identity remains Chirality. The app must not appear to be Claude Code or an Anthropic product. | UI/copy review; packaging metadata; release checklist. |

### 1.5 Runtime Events, Sessions, and Audit Mirror

| ID | Invariant | Enforcement |
|---|---|---|
| **K-EVENT-1** | Browser events and persisted `HarnessEvent`s are separate contracts. Under D-GOV-43 the browser stream carries an extensible representation that preserves upstream method names, identifiers and payloads, with normalized views for known items (tool activity, file changes, reasoning summaries, plan, sub-agents, usage, approvals, questions); the fixed eight-name `UIEvent` set is superseded. Persisted events may be richer and versioned. | Event representation tests; API route tests. |
| **K-EVENT-2** | Accepted user input must be persisted before model/SDK execution begins. A killed or interrupted process must leave a recoverable accepted-turn event. | `TurnEngine`; `SessionEvents`; integration tests. |
| **K-EVENT-3** | Every accepted turn ends with exactly one durable terminal outcome: completed, failed, interrupted, or cancelled. Upstream terminals are mapped before the coordinator; retirement/recovery must not invent success or duplicate terminals; unexpected termination of the Runtime or Codex child is never presented as completion. The closed schema v2 union of D-GOV-43 family 2 is retired. | Closed-union type validation; exact-pin codec; terminal mapping/recovery tests; replay and sink backchecks; G-WIRE/AT-032/055. |
| **K-EVENT-4** | The Root-owned shared-runtime session store at `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/events.jsonl`, where `{userData}` resolves to `~/Library/Application Support/Chirality`, using event schema `chirality.event/v1` with adjacent `session.json` session record schema `chirality.session/v2`, is the canonical runtime audit record. The App-owned Runtime service is the sole active writer under Root K-RUNTIME-1 as re-expressed by D-GOV-43 (A2). Project-local `.chirality/sessions/<id>/events.jsonl` is a legacy App compatibility source read and lazily migrated non-destructively under Root K-STORE-2; it is never a second active writer or an authority replacement. App `UIEvent` streaming and replay remain projections of accepted runtime records. | Root/App storage-contract concordance; canonical-path/schema fixtures; one-writer tests; lazy non-destructive migration/source-preservation; replay/path/version tests; no-dual-store inspection. |
| **K-EVENT-5** | JSONL event replay must tolerate malformed trailing lines and preserve valid prior events. | Session replay tests; reader implementation. |
| **K-EVENT-6** | Structural redaction runs before every sink (coordinator, persistence, browser SSE projection, status/replay views, logs, App Server diagnostics, support bundles). Under D-GOV-43 upstream notifications cross with their method names, identifiers and payloads preserved after redaction; unfamiliar notifications remain inspectable in a generic card and the event log and are never dropped; the closed schema v2 whitelist and quarantine are retired. Secrets, tokens, device-login ceremony values, callback parameters, cookies, credentials, and private machine state are excluded; ephemeral ceremony display data is destroyed with its view. | Generated schema/type exhaustiveness; synthetic-secret corpus across JSONL, both SSE hops, logs and bundles; unknown-type fixtures; scanner extension coverage; G-WIRE/AT-024/025/057. |
| **K-EVENT-7** | Large or sensitive tool results must be budgeted, previewed, stored as artifacts, or redacted according to policy. | `ToolResultStore`; hook policy; tool event tests. |

### 1.6 Permission, Tool Exposure, Hooks, and MCP

| ID | Invariant | Enforcement |
|---|---|---|
| **K-PERM-1** | Permission governance is capability-forward and policy-mediated: useful agent tool use may be exposed when mode, adapter, descriptor, hook, evidence, and human-gate policy allow it. Explicit hard denies override allows. | `ChiralityPermissionOverlay`; hooks; MCP wrappers; tests. |
| **K-PERM-2** | Prompt text is not a safety boundary. Filesystem writes, tool exposure, bash, subagents, and domain operations require runtime enforcement. | Permission overlay; hooks; runtime contract. |
| **K-PERM-3** | Tool availability or `allowedTools` alone is not a restriction boundary. Restriction requires explicit deny precedence, disallowed tools, mode policy, hooks, `canUseTool`, and/or `dontAsk` posture. | SDK options builder; validation tests. |
| **K-PERM-4** | `readOnly` mode must not expose or allow write/edit/bash/network-capable actions. | SDK options; tool exposure tests; hook denials. |
| **K-PERM-5** | `dontAsk` mode denies unapproved writes, shell, network, and unknown tools without prompting. | Permission overlay; integration tests. |
| **K-PERM-6** | `bypassPermissions` is developer-local only and never shipped as ordinary operator behavior. Chirality deny hooks still apply. | Options builder; environment guard; release checklist. |
| **K-TOOL-1** | Tool exposure is deterministic for a given session, persona, mode, option set, SDK version, MCP server set, and permission policy. | SDK options builder; tool registry/MCP tests. |
| **K-TOOL-2** | Tool implementation availability does not imply model exposure. A tool must pass tool-surface and permission resolution before exposure. | Tool pool/options builder; tests. |
| **K-MCP-1** | MCP is a transport, not a bypass. In-process Chirality MCP tools pass through the same permission, hook, path, redaction, and event logging policy as SDK built-ins. | MCP wrappers; hook implementation; Section 9 validation. |
| **K-HOOK-1** | Hook failures fail closed for write, shell, domain, and subagent actions. | `ChiralityHooks`; integration tests. |
| **K-PATH-2** | Runtime tools must enforce working-root containment and reject writes outside the active project root. | Path helpers; PreToolUse hooks; MCP tools. |
| **K-PATH-3** | Symlink writes are rejected in the initial policy. Any relaxation requires governed amendment and tests. | PreToolUse hooks; write tests. |
| **K-BASH-1** | Bash is unavailable unless an explicitly governed mode enables it after timeout, output capture, result storage, interrupt behavior, and audit events are validated. This bash gate must not suppress unrelated safe read/tool capabilities. | Options builder; hooks; R4 validation. |

### 1.7 Filesystem Execution, Lifecycle, Dependencies, and Provenance

| ID | Invariant | Enforcement |
|---|---|---|
| **K-STATUS-1** | `_STATUS.md` is the canonical human-readable lifecycle state file for each deliverable. No other file determines deliverable state. | Status parser; transition API; SPEC. |
| **K-STATUS-2** | Lifecycle transitions are forward-only and actor-authorized. Transitions to human-gate states require approval SHA evidence. | Status transition API; MCP status tool; tests. |
| **K-DEP-1** | Deliverable-local `_DEPENDENCIES.md` and `Dependencies.csv` are authoritative for dependencies. Aggregation is on-demand, not a separate central truth store. | Dependency APIs; MCP dependency tool; DEPENDENCIES agent. |
| **K-DEP-2** | Dependency references to deliverables must resolve to existing stable deliverable IDs. Unresolvable targets use `TargetType=UNKNOWN`. | Dependency linter; scanner; writer. |
| **K-PROV-1** | Active extracted dependency rows must cite evidence: `EvidenceFile` plus `SourceRef`, or explicit `location TBD`. | `Dependencies.csv` validation; dependency writer. |
| **K-INVENT-1** | Unknown values become `TBD`, not guesses. Agents and tools must not invent scope items, dependency targets, parameters, or professional conclusions. | Agent instructions; human review; validation. |
| **K-CONFLICT-1** | Source conflicts are surfaced, not silently resolved. | Agent instructions; reconciliation workflows; review. |
| **K-SNAP-1** | Snapshot-producing workflows write immutable timestamped folders. Mutable `_LATEST.md` pointers may move; snapshots must not be overwritten. | Tool-root policy; human review; tests. |
| **K-REF-1** | Accepted reference hash tooling and dependency-linter tooling remain available; retired hardening scope is not reintroduced by runtime event logging. | PKG-08 status; plan; scope-change records. |

### 1.8 Agent and Subagent Governance

| ID | Invariant | Enforcement |
|---|---|---|
| **K-WRITE-1** | Every agent instruction file declares explicit write scope. Agents must not write outside their declared scope. | Agent instruction conformance; tool hooks; human diff review. |
| **K-SEAL-1** | Every delegated child requires sealed context, approval at the applicable human gate, a citation to that human approval record, declared inputs/tools/writes, and a checkable return contract. Runtime checks validate presence and structure; they do not manufacture or authenticate the human act. | Human approval record and review; `ManagedDelegationService`; compatibility `evaluateSubagentGovernance`; coordination records and tests. |
| **K-GHOST-1** | Agent 2 context is limited to declared read scopes and accepted references. No ghost inputs. | Sealed brief; managed session metadata; permission overlay and path hooks; subagent tool config. |
| **K-SUBAGENT-1** | Delegation fails closed unless the 0→1 or 1→2 hierarchy, named allowlist or declared generalist policy, context seal, run approval, approval reference, instruction/brief evidence, and path/write boundaries all pass. The legacy SDK adapter is disabled and fails closed. | `ManagedDelegationService`; `SubagentGovernanceBridge`; tests. |
| **K-SUBAGENT-2** | Child capabilities are explicit and bounded by declared child policy; no capability is inherited implicitly. Child tools, context, cwd, and write targets are recorded and restricted. | Managed child session metadata; SDK compatibility config; permission overlay; records. |
| **K-SUBAGENT-3** | Child runs produce reconstructible parentage, plan/brief/instruction hashes, status, return/output references, and any notice/update/amendment/acknowledgment evidence. | `HarnessEvent`; `execution/_Coordination/AgentRuns`; Section 9 validation. |
| **K-UNTYPED-1** | An untyped primary Codex session may use delegated-harness-native descent only inside the user-chosen approval policy and sandbox mode of the project (D-GOV-43 item 4; the former hard envelope is re-expressed as that chosen policy). Native descent does not assign an Agent 0/1/2 role, does not enter managed delegation, and does not imply inherited authority or capability. Chirality-managed descendants remain subject to their separate hierarchy, sealed brief, approval, allowlist/generalist, tool, context, cwd, write-scope, and durable-evidence checks. Native origin/lineage and instruction/config-asserted non-delegation are recorded truthfully. | Origin/lineage fixtures; managed-vs-native route tests; containment and cancellation tests; AgentRun evidence calibration; no-role-by-descent checks; G-ROLE/G-APPR/G-SBX/G4. |

### 1.9 Security, Network, Release, and Packaging

| ID | Invariant | Enforcement |
|---|---|---|
| **K-NET-1** | Outbound network is deny-by-default and limited to enumerated product transports: the existing loopback/Anthropic path (compatibility history), the bounded D-APP-72 authenticated `127.0.0.1` oMLX exception (compatibility history), and the stock Codex App Server's own account, model and turn endpoints. There is no generic service-traffic exemption. Under D-GOV-43 item 4 command network follows the user's Codex configuration and chosen sandbox mode, shown in the composer and recorded in evidence; the former per-root consent postures read as that choice: (1) no command network, the default; (2) ask per destination through managed-network prompts that show the available host/protocol context and warn that an upstream grant may unblock queued requests to the same destination, with `acceptForSession` permitted only as an explicit user act; or (3) command network on through `network_access = true`, visibly labelled. Redirects, embedded URL credentials, remote MCP/providers, undeclared endpoints, and network outside the selected posture fail closed. | Endpoint allowlist and redirect tests; root-consent/state fixtures; prompt delivery and empirical grouping evidence at the exact pin; `networkApprovalContext` projection tests; no-network default; account/root continuity; G-APPR/G-SBX/AT-020. |
| **K-KEY-1** | Credentials and authentication ceremony data—including API keys, OAuth access/refresh tokens, device codes, browser callback parameters, cookies, Keychain items, App Server keyring state, and Electron `safeStorage` ciphertext/plaintext—are non-project private state. They must not appear in project files, durable event payloads, logs, support bundles, tool artifacts, or SDK transcripts where avoidable. Storage and UI contracts distinguish at least `missing`, `storageUnavailable`, `decryptFailed`, and `available`; a decrypt or signature-transition failure is typed, non-destructive, redacted, and requires explicit reauthentication rather than null-collapse or silent loss. Chirality's effective Codex home keeps `auth.json` and the models cache private with `cli_auth_credentials_store=file`; credential material is never copied from or into ambient `~/.codex`. | safeStorage/keyring and A→B identity-transition tests; six-channel IPC sender authorization; secret-evidence scanner; redaction fixtures; root-account transition/logout tests; G-KEY/G-CSP/AT-044/051/057. |
| **K-CONSENT-1** | RETIRED under D-GOV-43 (A2), 2026-09-12; see §4. Historical text: `HostedEngineConsentPort` is the sole App coordinator boundary for admitting a hosted-engine worker, thread, or turn. Before worker boot/acquisition, thread creation/resume, and every turn, it validates server-owned canonical root, project identity, adapter, exact non-secret account digest or volatile null-email epoch, notice/policy digest, selected role posture, effective configuration digest, and worker generation. Consent is per canonical root and cannot be reused across root, account, policy, or generation changes. Revocation retires the affected root generation and invalidates its private home. Caller-supplied `cwd` never overrides the stored canonical root. | Contract injection tests; account A/B/null-email fixtures; root/policy/generation mismatch denials; revocation/retirement journal; stored-root mutation rejection; G-SENT/G-DUAL/AT-003/007/044/056. |
| **K-ATTACH-1** | Attachments are server-validated; client metadata is non-authoritative. Symlinks, directories, special files, unsupported extensions, and over-budget files are rejected. | Attachment resolver; route tests. |
| **K-RELEASE-1** | Current release target is macOS 15+ Apple Silicon unsigned/unnotarized local-builder DMG unless amended. | `desktop:dist`; manual release verification. |
| **K-VALIDATE-1** | Required local checks must pass before release-significant changes are accepted. | `npm run test`; `typecheck`; `harness:validate:premerge`; `instruction-root:integrity`; `desktop:dist`. |
| **K-RETIRED-1** | Retired execution-scope items, including retired PKG-08 deliverables, remain out of scope unless reactivated by governed amendment. | PLAN; scope-change records; PRD acceptance checks. |

### 1.10 Domain Engine Future Scope

App-dev K-DOMAIN-1..4 specialize framework `docs/CONTRACT.md` §1.12 `K-DOMAIN-*` at commit
`77a327727605f05da5f304288f1ddd87dc09659d` and MUST NOT weaken the framework invariants.

| ID | Invariant | Enforcement |
|---|---|---|
| **K-DOMAIN-1** | Domain engines own authoritative domain truth. Chirality governs interaction, profiles, manifests, proposals, review notes, records, and human gates; it does not become the solver or accepted engineering truth. Specializes framework `K-DOMAIN-1`; MUST NOT weaken. | Domain profile spec; adapter policy; UI copy; DOMAIN_ENGINE persona. |
| **K-DOMAIN-2** | Protected domain paths are write-quarantined. Agents may write proposals and summaries only in profile-approved agent-writable paths; protected domain-engine model truth is not directly writable by agents. Specializes framework `K-DOMAIN-2`; MUST NOT weaken. | Domain profile policy; path hooks; operation workflow; DOMAIN_ENGINE persona. |
| **K-DOMAIN-3** | Domain operations require `OperationProposal` records and explicit human acceptance before application; accepted/applied transitions bind to human approval evidence per K-AUTH-2 and domain-engine-controlled apply or external terminal acceptance records. Specializes framework `K-DOMAIN-3`; MUST NOT weaken. | Future domain APIs; human gate; audit events; DOMAIN_ENGINE persona. |
| **K-DOMAIN-4** | Domain-engine outputs must not be represented as professional approval, code compliance, certification, sealing, authentication, external validation, ready-for-construction status, or solver truth owned by Chirality absent a cited human authoritative record. Specializes framework `K-DOMAIN-4`; MUST NOT weaken. | UI/documentation review; boundary notices; DOMAIN_ENGINE persona. |

---

## 2. Enforcement Map Summary

| Enforcement Point | Invariants Checked |
|---|---|
| `DIRECTIVE.md` | K-FS-1, K-NOMEM-1, K-GIT-1, K-AUTH-1, K-BIND-1, K-PROF-1, K-ROOT-1, K-ENGINE-3, K-DOMAIN-1 |
| `SPEC.md` | K-HIER-1, K-ID-1, K-ROOT-1, K-FS-1, K-NOMEM-1, K-BIND-1, K-EVENT-1 through K-EVENT-7, K-STATUS-1, K-DEP-1, K-ATTACH-1 |
| `TYPES.md` | K-ID-1, K-PATH-1, K-FS-1, K-NOMEM-1, K-BIND-1, K-EVENT-1, K-PERM-1, K-TOOL-1, K-DOMAIN-3 |
| `PLAN.md` | K-VALIDATE-1, K-RETIRED-1, K-ENGINE-5, K-DOMAIN-1 through K-DOMAIN-4 |
| Working-root validator | K-ROOT-1, K-PATH-2 |
| `AgentEnginePort` / `RuntimeEngineContract` | K-ENGINE-1 through K-ENGINE-5 |
| Engine conformance tests | K-ENGINE-2, K-ENGINE-4, K-EVENT-1 through K-EVENT-5, K-PERM-1 |
| SDK options builder | K-SDK-1, K-SDK-2, K-PERM-3, K-TOOL-1, K-BASH-1 |
| SDK message mapper | K-EVENT-1, K-EVENT-3, K-ENGINE-4 |
| Session event store | K-EVENT-2 through K-EVENT-6, K-SDK-3 |
| Work/Agents projection and selected replay tests | K-FS-1, K-NOMEM-1, K-BIND-1, K-ID-1, K-EVENT-5 |
| Run logger/redaction | K-EVENT-6, K-KEY-1 |
| Permission overlay | K-PERM-1 through K-PERM-6 |
| Chirality hooks | K-PATH-2, K-PATH-3, K-HOOK-1, K-ROOT-2, K-BASH-1, K-SUBAGENT-1 |
| MCP wrappers | K-MCP-1, K-STATUS-2, K-DEP-1, K-PATH-2 |
| Status/dependency APIs | K-STATUS-1, K-STATUS-2, K-DEP-1, K-DEP-2, K-PROV-1 |
| Agent instructions | K-WRITE-1, K-SEAL-1, K-GHOST-1, K-INVENT-1, K-CONFLICT-1 |
| Human review | K-AUTH-1, K-AUTH-2, K-BIND-1, K-GATE-1, K-PROF-1 |
| Release validation | K-PACKAGE-1, K-RELEASE-1, K-VALIDATE-1, K-NET-1, K-SDK-1 |
| App-owned Runtime service child and its socket API | K-RUNTIME-1, K-CONTROL-1, K-ROOT-1, K-PATH-2, K-KEY-1 |
| Effective Codex home and Codex-custodied sign-in | K-NET-1, K-KEY-1, K-ROLE-2 (K-CONSENT-1 retired) |
| Role entry and managed/native descendant classification | K-ROLE-2, K-UNTYPED-1, K-SUBAGENT-1, K-SUBAGENT-2, K-SUBAGENT-3 |
| Event representation, coordinator, persistence, SSE, replay, diagnostics, and support sinks | K-EVENT-1, K-EVENT-3, K-EVENT-4, K-EVENT-6, K-KEY-1 |
| Renderer IPC | K-KEY-1, K-AUTH-1 |
| Exact-candidate release validation | K-PACKAGE-1, K-RELEASE-1, K-VALIDATE-1, K-NET-1, K-SDK-1, K-CONTROL-1, K-KEY-1 |
| Future domain profile validator | K-DOMAIN-1 through K-DOMAIN-4 |

---

## 3. Change Policy

A change that modifies any invariant, introduces an exception, or changes an enforcement point must be treated as a governed product change. It must update the relevant governance documents, tests, validation runbooks, and implementation artifacts before being considered accepted.

New invariants may be added with new IDs. Existing IDs must not be reused for different meanings. If an invariant no longer applies, retire it in §4 rather than deleting it.

---

## 4. Retired Invariants

No invariants were retired in the vNext rewrite. Retired under D-GOV-43 (A2), 2026-09-12:

| ID | Retirement rationale |
|---|---|
| **K-CONSENT-1** | Family 1 (private supplier admission and certification) is retired whole; `HostedEngineConsentPort`, identity binding and per-root consent digests are not re-created under another name. Ordinary software integrity (family 4) replaces them. |
| **K-RESIDENCY-1** | D-GOV-43 item 13 retires the residency requirements with the daemon; local models, when taken up, use Codex model providers. History is preserved. |

---

## 5. Accepted Scope Changes

| Scope Change | Date | Effect |
|---|---|---|
| `SCA-APP-001` | 2026-06-13 | Approved provider-adapter generality, retained Claude Agent SDK / Anthropic as first concrete adapter, ruled Pi pattern-corpus-only, and reframed permission governance as capability-forward with explicit hard-deny precedence. D-APP-12 later clarified that `agentSdk` remains opt-in pending further proof/ruling. |
| `SCA-APP-002` | 2026-07-21 | Prospectively authorizes the D-APP-72 bounded Pi `0.80.10` / authenticated loopback oMLX second-engine tranche after Electron `43.1.1` (Electron authority since superseded by D-APP-98: `43.2.0`); preserves Claude as default/supervisor and excludes Pi-native capabilities, remote providers, automatic fallback, direct Pi supervisors, write/shell/network tools, release, issuance, and lifecycle advancement. |
| `SCA-APP-003` | 2026-07-22 | Promotes the provider-neutral harness to a root-owned shared runtime; establishes the authenticated Unix-socket daemon/client/CLI boundary, central lazy-migrating sessions, explicit one-primary-model residency, app-dev Agent 1 → local Agent 2 pilot, PEC client migration, and generic public-export boundary. |
| `SCA-APP-004` | 2026-07-23 | Selects Woven Dialogue with a Work/Agents Coordination Panel as the target information architecture; extends K-FS-1, K-NOMEM-1, and K-BIND-1 for provenance-labelled informational projection and strict primary-dialogue/read-only-replay separation while preserving runtime, API, SSE, security, history, compatibility, and human-authority boundaries. |
| `SCA-APP-008` | 2026-08-23 | Prospectively seats stable v3 account/consent UX, class-aware managed/native delegation, descendant evidence, and owner-gated release-operations carriers; carries the concordance-approved K-CONTROL-1, K-ROLE-2, K-NET-1, K-KEY-1, K-EVENT-3/4/6, K-CONSENT-1, K-UNTYPED-1, and enforcement-map amendments without changing App topology, Root ownership, lifecycle, or release authority. Not accepted; D-GOV-43 requires its revision before any acceptance. |

The SCA-APP-003 and SCA-APP-008 rows are historical effects. D-GOV-43 (A2, 2026-09-12) supersedes their daemon, supervisor-socket, consent and residency parts as recorded in §4 and §5.1.

### 5.1 Shared Runtime Invariants

| ID | Invariant | Verification |
|---|---|---|
| **K-RUNTIME-1** | Re-expressed under D-GOV-43 (A2): the App starts, owns and stops one Runtime service as a child process (no per-user LaunchAgent, no exclusive daemon), and that service owns the stock Codex child, the sessions, delegation, tools, the active turn and interruption. Credentials are custodied by Codex. The renderer, routes and CLI MUST NOT construct another runtime. | Child spawn, ready-line, restart-with-backoff and teardown tests; S-6; no-dual-runtime inspection. |
| **K-CONTROL-1** | Re-expressed under D-GOV-43 (A2): the App-owned Runtime service owns the `{userData}/runtime` control surfaces. Exactly one control socket is live: the service's Unix-socket API, reached by the App with a per-launch client token kept under `userData`; the renderer reaches the App only through loopback HTTP and SSE in the in-process Next server. The supervisor's second socket and job are retired. The socket resides beneath a `0700` parent, is mode `0600`, fails closed on a stale or mismatched token, and recovers stale sockets explicitly. No peer-credential guarantee is claimed where the runtime cannot inspect peer credentials. No second socket and no TCP control listener are permitted under any configuration. | Socket permission, token, stale-recovery, listener-inventory and no-TCP tests; renderer isolation and validated IPC tests. |
| **K-PROJECT-1** | Tracked project manifests contain stable identity and relative authority references only. Resolved roots, client credentials, and registration approvals remain user-data state. Authority-affecting changes disable adapters until explicit re-registration. | Manifest schema/hash tests; re-registration tests; secret/absolute-path scan. |
| **K-STORE-2** | Central Runtime service sessions use JSON/JSONL and lazily read/migrate project-local legacy records without bulk rewrite or destructive move; chats are indexed by Codex thread id, and daemon-era chats are preserved in place. Runtime state and Codex's session store are operational and do not replace checkout-contained governance truth. | Cross-store migration, replay, persistence, and restart tests. |
| **K-RESIDENCY-1** | RETIRED under D-GOV-43 item 13, 2026-09-12; see §4. Historical text: the daemon manages at most one primary local LLM with explicit activation, drain, no force-interrupt, no unknown-helper unload, a residency epoch, and fail-closed `NO_MODEL`. | None (retired). |
| **K-ROLE-2** | Agent 0/1/2 roles describe authority and responsibility, not a durable engine or model assignment. A deliberately selected role-posture/configuration digest may participate in worker identity solely to enforce that role's accepted authority semantics. Agent 0/1/2 role entry is always offered for Codex sessions. If G-ROLE cannot mechanically prove non-delegation, Agent 2/TASK entry remains available only with the label `role not mechanically enforced`, and governed-workflow evidence is marked `instruction-asserted`. Native descendants acquire no Agent 0/1/2 role by descent. Every run records selected role state, actual adapter/provider/model, configuration/policy digest, and any substitution. | G-ROLE profile/readback tests; role/native-class fixtures; label/copy checks; AgentRun/session attribution; actual-model evidence; governance scan for model-to-role prescriptions. |
| **K-EXPORT-1** | Public export may include generic runtime, CLI, contracts, and safe adapters only. Credentials, machine state, and private PEC/Piping adapters are excluded. | Allowlist/export-boundary checks and secret scan. |
