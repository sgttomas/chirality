# Chirality App vNext Software Decomposition

**Package Role:** Authoritative working surface
**Agent Persona:** SOFTWARE_DECOMP
**Revision:** v3.2 source-governed working surface
**Date:** 2026-05-20
**Source Corpus:** `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PLAN.md`, `docs/PRD.md`
**Method Reference:** `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md`
**Gate Posture:** Gates 1-7 accepted by implicit human approval per user instruction

This document decomposes Chirality App vNext into a software Structured Scope of Work (SSOW), flat work-domain packages, and Type-2-executable deliverables. It is derived from the active documents in `docs/`.

v3.2 adopts the v3.1 source-governed proposal as the basis for the SOFTWARE_DECOMP working surface. It preserves the 10 flat work-domain packages, 51 deliverables, 78 scope items, and 10 objectives while making the non-PRD control plane operationally explicit. DIRECTIVE, CONTRACT, SPEC, TYPES, PLAN, and PRD are all treated as active decomposition sources.

v3.2 does **not** renumber scope items, packages, deliverables, objectives, decisions, or open issues. It tightens the working surface for downstream PREPARATION, TASK / Type 2 execution, and REVIEW by adding explicit revision posture, source-governance rules, invariant coverage expectations, SPEC/TYPES binding notes, PLAN sequencing overlay, and v3.2 downstream execution instructions.

Revision-number note: this decomposition revision is **v3.2**. That is separate from the `Dependencies.csv v3.1` schema referenced in SPEC and deliverable DEL-07-05.

---

## 1. Gate Log

| Gate | Name | Status | Evidence |
|---|---|---|---|
| Gate 1 | Intake understanding | PASSED | Source corpus exists and was read; product intent summarized below. |
| Gate 2 | SSOW and vocabulary | PASSED | Atomic `SOW-NNN` items and vocabulary map created. |
| Gate 3 | Objectives | PASSED | `OBJ-NNN` objectives derived and mapped to scope. |
| Gate 4 | Packages | PASSED | Scope partitioned into flat `PKG-XX` work domains. |
| Gate 5 | Deliverables | PASSED | Deliverables are bounded, package-local, and context-sized. |
| Gate 6 | Coverage and context budget | PASSED | No unassigned scope items; no unmapped objectives; no XL deliverables. |
| Gate 7 | Publish decomposition | PASSED | This working surface includes all required SOFTWARE_DECOMP sections. |

---

## 2. References

| RefID | Source | Role | SHA-256 |
|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Intent, authority, professional boundaries | `dee943d3d87bf261bfd393c4dd9d474c01165a09cf0df94207361a4efa014d82` |
| REF-002 | `docs/CONTRACT.md` | Invariants and enforcement surfaces | `735a85004c157f30c3a48c553b82d543e43bae0272bebf47c7273a41f8e1e8dc` |
| REF-003 | `docs/SPEC.md` | Physical structures, runtime mechanics, API/file contracts | `ba7a62b2383293b54d059a60ce407aa3acdc3043afe61b6932958442e86343fb` |
| REF-004 | `docs/TYPES.md` | Vocabulary, identifiers, enums, type targets | `f5ebe6453a871980a0c1fd3ff11c0132048ce4e765a9c23f48968648b133ebc2` |
| REF-005 | `docs/PLAN.md` | Roadmap and implementation sequencing | `4a8af7de5f6bfdf757cd6a73834c1fa00686b4581d27e13a191735a0b05e467b` |
| REF-006 | `docs/PRD.md` | Product requirements, runtime direction, and approved vNext scope | `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34` |
| REF-007 | `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` | Decomposition method, gate protocol, package/deliverable structure, and Context Envelope discipline | `4f2c0a662fcd9eafdb20664997d05ce4734d99dd55a7ca2bb760ed9c94a60fab` |

### 2.1 Source Authority and Reading Order

This decomposition is not PRD-only. It is derived from the synchronized governance corpus:

1. `DIRECTIVE.md` - intent, professional responsibility, evidence posture, authority, and change discipline.
2. `CONTRACT.md` - binding invariants and enforcement surfaces.
3. `SPEC.md` - physical structures, schemas, runtime mechanics, file contracts, APIs, and validation surfaces.
4. `TYPES.md` - vocabulary, stable identifiers, enums, and runtime type targets.
5. `PLAN.md` - roadmap sequencing and blocker policy.
6. `PRD.md` - current product requirements and accepted implementation direction.

The PRD supplies product requirements. The other governance documents supply controlling constraints, vocabulary, physical mechanics, invariant coverage, and execution sequencing. If a downstream task discovers conflict among these documents, it must surface the conflict rather than silently reconcile it.

### 2.2 v3.2 Revision Posture

v3.2 promotes the v3.1 source-governed proposal to the active SOFTWARE_DECOMP working surface, anchored to the local active `docs/` corpus and SOFTWARE_DECOMP method file. It preserves the full decomposition package as the authoritative home for SSOW, package/deliverable topology, scope ledger, coverage telemetry, context-budget QA, open issues, and decision log.

Required companion registers for v3.2:

| Companion Register | Package Role | Purpose |
|---|---|---|
| `contract_invariant_coverage_register.csv` | Planned authoritative companion register | Maps CONTRACT `K-*` invariants to package/deliverable ownership, enforcement surfaces, validation surfaces, and open issues. It must be created or explicitly deferred before REVIEW closure. |

v3.2 acceptance is conditional on the following invariants remaining true:

- no change to the 10-package / 51-deliverable topology without explicit human renumbering approval;
- no implementation work that exposes write, bash, subagent execution, remote MCP, plugins, or domain operations ahead of PLAN sequencing;
- no product-critical P0 reliance boundary delegated to prompt text or opaque SDK defaults alone;
- no reactivation of retired PKG-08 hardening scope by runtime event logging or validation wording;
- no change to macOS arm64 unsigned DMG release target without governed amendment.


---

## 3. Intake Summary

Chirality App vNext is a local-first desktop agent harness for governed professional work over a selected filesystem working root. The application packages a release-managed instruction root, keeps project truth in plain files and accepted git history, and treats runtime logs as audit evidence rather than approval records.

The approved runtime direction is SDK-privileged, contract-owned, and Chirality-governed. The Claude Agent SDK is the preferred engine for generic agent-loop mechanics, but Chirality owns the runtime contract, permission semantics, audit mirror, filesystem boundaries, persona composition, professional boundaries, and fallback criteria.

The next implementation objective is to mature the existing desktop shell into a governed runtime by establishing `AgentEnginePort` / `RuntimeEngineContract`, SDK conformance, SDK-backed `TurnEngine`, append-only `HarnessEvent` JSONL, prompt/persona composition, settings isolation, run logging, and a reliance-boundary register before expanding read tools, writes, bash, subagents, or domain-engine profiles.

### Hard Constraints Captured

- Packages are flat work domains, not phases.
- Deliverables are the smallest executable unit; no task sub-level is introduced.
- Stable IDs use `PKG-XX` and `DEL-XX-YY`.
- R0/R1 runtime contract and SDK adoption remain the immediate implementation slice.
- Browser-facing route shapes and SSE event names remain stable during the runtime pivot.
- Chirality audit JSONL remains canonical for product-owned runtime audit.
- `settingSources: []` is required for shipped SDK builds.
- `allowedTools` alone is not a restriction boundary.
- Write, bash, subagent, remote MCP, plugin, and domain-operation capabilities remain gated until governance deliverables pass validation.
- Product identity remains Chirality; professional approval remains human-only.
- Retired PKG-08 scope is not reactivated.
- Source authority is layered: DIRECTIVE, CONTRACT, SPEC, TYPES, PLAN, and PRD are all decomposition inputs.
- Project truth lives in versioned working-root files and accepted git history, not chats, SDK transcripts, hidden state, or runtime convenience data.
- Runtime events explain work; they do not approve work or make deliverables professionally reliable.
- Unknowns become `TBD`; assumptions and proposals must remain labeled until human acceptance.
- P0 reliance boundaries must be enforced by Chirality code, verified SDK callbacks/hooks, deterministic tools, release checks, or human gates; prompt text alone is insufficient.
- CONTRACT `K-*` invariant coverage must be reviewable through the decomposition package or companion register.
- PLAN sequencing is a blocker overlay, not a package architecture: work-domain packages are not phases.

---

## 4. Vocabulary Map

| CanonicalTerm | Synonyms | Notes |
|---|---|---|
| Chirality App | Chirality, desktop harness | Product identity remains Chirality, not Claude Code. |
| Instruction Root | release-managed agent OS, bundled resources | Read-only during ordinary project execution. |
| Working Root | `projectRoot`, selected workspace | Mutable project execution location. |
| Project Truth | accepted project state, reliance evidence | Plain files under working root plus git history. |
| Runtime Audit Mirror | Chirality audit JSONL, `events.jsonl` | Canonical runtime audit record under `.chirality/sessions/<id>/`. |
| SDK Transcript | Claude transcript, SDK session transcript | Secondary runtime artifact unless imported as `HarnessEvent`. |
| AgentEnginePort | RuntimeEngineContract boundary | Product-owned engine adapter contract. |
| EngineAdapter | SDK adapter, provider adapter | Provider-specific translator behind Chirality contracts. |
| TurnEngine | turn lifecycle owner | Thin runtime service outside HTTP route. |
| HarnessEvent | runtime event | Persisted, versioned Chirality event. |
| UIEvent | browser SSE event | Compact browser contract, separate from `HarnessEvent`. |
| PersonaComposer | prompt composer, system prompt builder | Reads instruction-root governance and active persona. |
| SdkOptionsBuilder | SDK option mapper | Builds deterministic SDK options and settings posture. |
| ChiralityPermissionOverlay | permission policy, deny-first overlay | Uses SDK modes, deny lists, hooks, and `canUseTool`. |
| Chirality MCP Tool | `mcp__chirality__*` tool | Deterministic in-process tool, not a bypass. |
| Hook | SDK callback, runtime guard | Enforces path, provenance, compaction, subagent, and terminal policy. |
| ToolResultStore | artifact store, result budget | Stores large tool output under session artifacts. |
| SubagentGovernanceBridge | governed SDK agents bridge | Gates Type 2 child runs and records parent-child linkage. |
| SessionRecord | session metadata | Metadata record for a harness session, including SDK linkage where applicable. |
| HarnessPermissionDecision | permission decision record | Structured allow, deny, or application-level ask decision with reason/source metadata. |
| HarnessSubagentRun | subagent child run record | Parent-child runtime record for governed Type 2 subagent execution. |
| SDK built-in tool | `Read`, `Glob`, `Grep`, `LS`, `Write`, `Edit`, `Bash` | SDK-supplied tool names translated and governed at the adapter/permission boundary. |
| allowedTools | SDK auto-approval tool option | Not a restriction boundary by itself. |
| disallowedTools | SDK or overlay denial tool option | Used with mode policy, hooks, and callbacks to prevent execution/exposure. |
| canUseTool | SDK permission callback | Application-mediated permission path; Chirality persists decision before returning allow/deny. |
| Epistemic Label | `FACT`, `ASSUMPTION`, `PROPOSAL`, `TBD` | Labels used to prevent plausible invention from becoming project truth. |
| CoordinationRepresentation | `SCHEDULE_FIRST`, `DEPENDENCY_TRACKED`, `HYBRID` | Coordination representation separate from deliverable-local dependency tracking. |
| DomainEngineProfile | domain profile | Future platform contract, not current runtime core. |
| OperationProposal | domain operation record | Future human-gated domain operation proposal. |
| OpenPipeStress fixture | first domain example | Future fixture profile, not Chirality core. |

---

## 5. SSOW

| ScopeItemID | Status | SourceRef | ScopeItemStatement | Notes |
|---|---|---|---|---|
| SOW-001 | IN | REF-006 Section 8.1 | Provide a desktop shell with PORTAL, PIPELINE, and WORKBENCH navigation. | Current baseline preserved. |
| SOW-002 | IN | REF-006 Section 8.1, REF-003 Section 1 | Support global working-root selection and validation. | Must reject invalid and instruction-root-contained paths. |
| SOW-003 | IN | REF-006 Section 8.1 | Render bounded working-root file tree and scope scans. | Scan limits protect responsiveness. |
| SOW-004 | IN | REF-006 Section 8.1, Section 8.7 | Support professional pane layout, resize/collapse, and local UI state. | Local state is non-authoritative. |
| SOW-005 | IN | REF-006 Section 8.2, REF-004 Section 4 | Render canonical 3x4 matrix and route cells by row semantics. | NORMATIVE/EVALUATIVE to WORKBENCH; OPERATIVE to PIPELINE. |
| SOW-006 | IN | REF-006 Section 8.2 | Present active WORKBENCH agent context from route state. | Includes selected agent, row, and column. |
| SOW-007 | IN | REF-006 Section 8.2 | Expose PIPELINE category and task-scope selectors. | Unsupported options visible and disabled. |
| SOW-008 | IN | REF-006 Section 8.7 | Expose per-turn toolkit options and preserve local drafts/presets. | Must not override runtime governance. |
| SOW-009 | IN | REF-006 Section 8.3, Section 9.1 | Create, list, resume, retrieve, save, and delete harness sessions. | Bound to normalized project root. |
| SOW-010 | IN | REF-006 Section 8.3, Section 8.4 | Session creation and boot bind project root, persona, mode, and options. | Boot fingerprint should reflect real prompt/policy inputs. |
| SOW-011 | IN | REF-006 Section 8.3, Section 9.3 | Execute harness turns over stable SSE events with one active turn per session. | Route remains browser-compatible. |
| SOW-012 | IN | REF-006 Section 8.3, Section 7.10 | Interrupt, cancel, and failure handling must release locks and persist terminal records. | Includes resumability after failure. |
| SOW-013 | IN | REF-006 Section 8.3 | Runtime errors must be typed, actionable, and preserve retry context. | UI maps error to title/message/next step. |
| SOW-014 | IN | REF-006 Section 8.3, Section 8.12 | Persist accepted user input before SDK/model execution starts. | P0 audit boundary. |
| SOW-015 | IN | REF-006 Section 8.3, Section 8.12 | Persist terminal success, failure, cancellation, or interruption events. | Every accepted turn must terminate durably. |
| SOW-016 | IN | REF-006 Section 8.4, REF-003 Section 13 | Runtime option fallback chains must be deterministic and warn on unknown keys. | Model, tools, max turns, mode, persona. |
| SOW-017 | IN | REF-006 Section 8.4, REF-003 Section 13 | Resolve personas and aliases to instruction-root `AGENT_*.md` files and compose real prompt context. | Replaces stub persona prompt. |
| SOW-018 | IN | REF-006 Section 8.4, Section 13 | Support SDK-backed Anthropic provider path behind Chirality runtime contract. | Open issue until R0/R1 SDK probe passes. |
| SOW-019 | IN | REF-006 Section 8.5, REF-003 Section 16 | Resolve Anthropic API key from UI safeStorage then environment without project writes. | Key material is never project truth. |
| SOW-020 | IN | REF-006 Section 8.5, REF-003 Section 16 | Enforce Anthropic base URL and renderer network allowlist. | Loopback plus Anthropic path. |
| SOW-021 | IN | REF-006 Section 8.5 | Classify provider and SDK errors with redaction. | Auth, rate limit, timeout, API, network, policy. |
| SOW-022 | IN | REF-006 Section 8.6, REF-003 Section 16 | Server-side attachment resolver validates paths, type, symlink status, and budgets. | Client metadata is non-authoritative. |
| SOW-023 | IN | REF-006 Section 8.6 | UI supports attachment selection, preview, remove, and failure recovery. | Provider maps supported files to content blocks. |
| SOW-024 | IN | REF-006 Section 8.8, REF-003 Section 2 | Scaffold SPEC-conformant execution roots from decomposition markdown. | Includes tool roots and coordination file. |
| SOW-025 | IN | REF-006 Section 8.8, REF-003 Section 2-3 | Support flat package and deliverable folder layouts. | No nested packages. |
| SOW-026 | IN | REF-006 Section 8.8, REF-003 Section 3-5 | Support canonical deliverable metadata files and document kit buckets. | `_MEMORY.md` disabled; `MEMORY.md` canonical. |
| SOW-027 | IN | REF-006 Section 8.8, REF-002 Section 1.3 | Enforce project-root containment and instruction-root protection. | Runtime code, not prompt text. |
| SOW-028 | IN | REF-006 Section 8.9, REF-003 Section 4 | Parse and enforce `_STATUS.md` lifecycle transitions and approval SHA gates. | `_STATUS.md` is canonical state. |
| SOW-029 | IN | REF-006 Section 8.9, REF-003 Section 6 | Parse, validate, and write `Dependencies.csv` v3.1 with provenance. | Rows retire rather than delete. |
| SOW-030 | IN | REF-006 Section 8.10, REF-003 Section 7 | Package and validate the indexed instruction-root agent suite and governance docs. | Required assets are packaging blockers. |
| SOW-031 | IN | REF-006 Section 8.10, REF-003 Section 7 | Agent instruction files declare required metadata and section markers. | Conformance is auditable. |
| SOW-032 | IN | REF-006 Section 8.10 | Deterministic project tools and scripts remain indexed and locally executable. | Includes validation scripts. |
| SOW-033 | IN | REF-006 Section 8.10, REF-002 Section 1.7 | Snapshot workflows produce immutable timestamped folders and optional `_LATEST.md` pointers. | Accepted snapshots are not overwritten. |
| SOW-034 | IN | REF-006 Section 8.10, REF-002 Section 1.2 | CHANGE/publication workflows require approval tokens and SHA checks. | Human authority remains non-delegable. |
| SOW-035 | IN | REF-006 Section 8.11, Section 12 | Required local checks cover tests, typecheck, harness validation, integrity, and desktop build. | Release-significant changes require checks. |
| SOW-036 | IN | REF-006 Section 8.11, Section 12 | Maintain Section 8 validation and add Section 9 runtime validation IDs as phases land. | Includes stable summary artifact. |
| SOW-037 | IN | REF-006 Section 8.12, Section 9.4 | Define product-owned `AgentEnginePort` / `RuntimeEngineContract`. | SDK APIs do not define public semantics. |
| SOW-038 | IN | REF-006 Section 8.12, REF-003 Section 10 | Extract a thin `TurnEngine` and keep `/api/harness/turn` as transport adapter. | Route validates and streams; runtime owns behavior. |
| SOW-039 | IN | REF-006 Section 8.12, REF-003 Section 9 | Persist versioned `HarnessEvent`s to append-only JSONL. | Includes ordered writes and trailing-line tolerance. |
| SOW-040 | IN | REF-006 Section 8.12, REF-003 Section 11 | Keep browser `UIEvent`s separate from persisted `HarnessEvent`s. | Stable compact UI contract. |
| SOW-041 | IN | REF-006 Section 8.12, REF-003 Section 9 | Redact secrets from runtime logs, provider errors, event data, and tool artifacts. | P0 privacy boundary. |
| SOW-042 | IN | REF-006 Section 8.12, REF-003 Section 8-9 | Replay runtime events into transcript views and diagnostics. | Valid prior JSONL survives malformed tail. |
| SOW-043 | IN | REF-006 Section 8.12, REF-003 Section 8 | Keep legacy session records readable during migration to folder layout. | Existing `.json` sessions remain usable. |
| SOW-044 | IN | REF-006 Section 8.12, Section 9.4 | Map SDK messages deterministically into UI events and `HarnessEvent`s. | Open issue until SDK message probe confirms categories. |
| SOW-045 | IN | REF-006 Section 8.12, REF-003 Section 12 | Enforce SDK settings isolation with `settingSources: []` in shipped builds. | User/local settings forbidden in shipped builds. |
| SOW-046 | IN | REF-006 Section 8.12, Section 10.3 | Persist SDK session ID, transcript/store linkage, and resume metadata without making SDK transcript canonical. | Transcript placement remains an R1 decision. |
| SOW-047 | IN | REF-006 Section 8.13 | Map `opts.tools` only to registered SDK built-ins or Chirality MCP tools. | Unknown names error. |
| SOW-048 | IN | REF-006 Section 8.13, REF-003 Section 14 | Chirality MCP tools declare schema, permissions, execution, and summarization behavior. | In-process tools pass same policy as SDK built-ins. |
| SOW-049 | IN | REF-006 Section 8.13 | Tool-surface construction is deterministic for a session, persona, mode, and policy. | Tool implementation availability is not model exposure. |
| SOW-050 | IN | REF-006 Section 8.13, REF-005 Section 4 | Enable read tools before write/edit/bash capability. | Initial tool sequence is read-only. |
| SOW-051 | IN | REF-006 Section 8.13 | SDK supplies the model/tool loop while Chirality mirrors events. | No custom loop unless fallback triggers. |
| SOW-052 | IN | REF-006 Section 8.13 | Apply max-turn guards to stop runaway loops. | Terminal max-turn errors persist. |
| SOW-053 | IN | REF-006 Section 8.13 | Preserve deterministic replay even if SDK tool activity is concurrent. | Event ordering must be testable. |
| SOW-054 | IN | REF-006 Section 8.14, REF-004 Section 8 | Permission decisions are structured and persisted. | `allow`, `deny`, or application-level `ask`. |
| SOW-055 | IN | REF-006 Section 8.14, REF-002 Section 1.6 | Enforce Chirality permission modes through SDK posture plus deny-first overlay. | `allowedTools` is not a restriction boundary. |
| SOW-056 | IN | REF-006 Section 8.14 | Persist `tool.permission` events for governed tool attempts. | Includes source, reason, SDK metadata. |
| SOW-057 | IN | REF-006 Section 8.14, REF-003 Section 15 | Run hooks before/after tool use and fail closed for write, shell, domain, and subagent actions. | Includes path, provenance, compaction, stop. |
| SOW-058 | IN | REF-006 Section 8.14 | Mediate interactive approvals through `canUseTool` and UI. | Persist decision before SDK allow/deny return. |
| SOW-059 | IN | REF-006 Section 8.15, REF-003 Section 9 | Budget tool outputs and store large results as session artifacts. | Prevent chat/model context flooding. |
| SOW-060 | IN | REF-006 Section 8.15 | Safe write/edit tools enforce containment, symlink rejection, instruction-root block, and edit preconditions. | Applies after write phase lands. |
| SOW-061 | IN | REF-006 Section 8.15 | Mirror SDK compaction boundaries and preserve audit replay. | Full Chirality event log remains on disk. |
| SOW-062 | IN | REF-006 Section 8.15, REF-002 Section 1.6 | Bash remains denied by default; allowed bash needs timeout, capture, interrupt, and audit behavior. | No default shell exposure. |
| SOW-063 | IN | REF-006 Section 8.15, REF-004 Section 10 | Governed subagents create child run records with restricted tools and working directory. | Uses `evaluateSubagentGovernance`. |
| SOW-064 | IN | REF-006 Section 8.15, REF-005 Section 4 | Catalog MCP tools and extension boundaries without remote MCP or marketplace scope. | Collision prevention required. |
| SOW-065 | OUT | REF-006 Section 3.2, Section 6.4 | Remote MCP, plugins, remote execution, and broad tool search are out of current scope. | Requires governed amendment. |
| SOW-066 | IN | REF-006 Section 8.17, REF-003 Section 18 | Preserve future compatibility for generic Domain Engine Profiles. | Future amendment, not immediate runtime slice. |
| SOW-067 | IN | REF-006 Section 8.17, REF-004 Section 11 | Define `DomainEngineProfile` contract before engine-specific integration. | Future platform contract. |
| SOW-068 | IN | REF-006 Section 8.17 | Enforce protected path and proposal path policy for domain engines. | Agents do not write protected model truth. |
| SOW-069 | IN | REF-006 Section 8.17, REF-004 Section 11 | Represent domain operations as `OperationProposal` records with deterministic checks. | Human-gated before application. |
| SOW-070 | IN | REF-006 Section 8.17 | Treat OpenPipeStress as first fixture profile if adopted. | Not core harness behavior. |
| SOW-071 | IN | REF-006 Section 8.17, REF-002 Section 1.10 | Domain outputs must not imply professional approval, code compliance, external validation, or solver truth. | Boundary notices required. |
| SOW-072 | IN | REF-006 Section 6.2, Section 12.8 | Current release target is macOS 15+ Apple Silicon unsigned/unnotarized DMG. | Windows/Linux out of scope. |
| SOW-073 | TBD | REF-006 Section 15 | Required instruction-root source assets may be incomplete in the current source or packaging state. | P0 packaging readiness issue. |
| SOW-074 | IN | REF-001 Section 3, REF-002 Section 1.2 | Human authority and professional boundaries are preserved throughout the app. | No automated approval. |
| SOW-075 | IN | REF-001 Section 2, REF-006 Section 3.2 | Project truth must not depend on external database, hidden app state, chats, caches, or vendor systems. | Local-first requirement. |
| SOW-076 | OUT | REF-006 Section 3.2, REF-002 Section 1.4 | Shipped builds must not load ambient Claude settings or use ordinary `bypassPermissions`. | Developer-only bypass remains guarded. |
| SOW-077 | OUT | REF-006 Section 15, REF-005 Section 9 | Retired PKG-08 items must not be reactivated by runtime event logging. | Event log is separate runtime infrastructure. |
| SOW-078 | OUT | REF-006 Section 6.4, REF-005 Section 11 | Windows/Linux release packaging is out of scope until amendment. | Current release is macOS arm64. |

---

## 6. Objectives

| ObjectiveID | Statement | MappedScopeItems | Notes |
|---|---|---|---|
| OBJ-001 | Preserve a governed local desktop harness with clear WORKBENCH, PIPELINE, PORTAL, file-tree, toolkit, and operator-state behavior. | SOW-001-SOW-008, SOW-023 | UI and operator workflow objective. |
| OBJ-002 | Establish product-owned runtime contracts and thin route boundaries before SDK behavior becomes production default. | SOW-009-SOW-018, SOW-037-SOW-040 | Runtime architecture objective. |
| OBJ-003 | Make accepted turns, SDK messages, terminal outcomes, tool activity, and replay auditable through Chirality-owned session records. | SOW-014-SOW-015, SOW-039-SOW-046, SOW-059, SOW-061 | Audit and session objective. |
| OBJ-004 | Adopt the Claude Agent SDK as a governed, replaceable engine with deterministic options, prompt composition, settings isolation, and provider redaction. | SOW-016-SOW-021, SOW-044-SOW-046, SOW-051 | SDK adapter objective. |
| OBJ-005 | Expose tools only through deterministic, deny-first permission policy, MCP wrappers, hooks, result budgets, and human-mediated approvals. | SOW-047-SOW-064, SOW-076 | Tool governance objective. |
| OBJ-006 | Preserve filesystem project truth through working-root containment, SPEC layouts, lifecycle files, dependencies, snapshots, and change discipline. | SOW-024-SOW-034, SOW-075, SOW-077 | Filesystem governance objective. |
| OBJ-007 | Maintain agent-suite integrity and enable governed subagent delegation without expanding authority. | SOW-030-SOW-031, SOW-063 | Agent governance objective. |
| OBJ-008 | Keep validation, packaging, release, network, key, and instruction-root checks explicit and repeatable. | SOW-019-SOW-022, SOW-035-SOW-036, SOW-072-SOW-073, SOW-078 | Release readiness objective. |
| OBJ-009 | Preserve professional boundary, product identity, and reliance-boundary ownership in docs, UI, runtime, and release behavior. | SOW-065, SOW-071, SOW-074, SOW-076-SOW-077 | Governance identity objective. |
| OBJ-010 | Preserve future domain-engine compatibility without turning domain solvers into Chirality core. | SOW-066-SOW-071 | Future platform objective. |

---

## 7. Packages

| PackageID | Name | ScopeDescription | InclusionCriteria | Exclusions |
|---|---|---|---|---|
| PKG-01 | Product Governance and Reliance Boundaries | Product intent, invariants, professional boundary, reliance-boundary ownership, out-of-scope discipline. | Governance docs, acceptance checks, product identity, scope boundaries. | Runtime implementation details except as required for boundary enforcement. |
| PKG-02 | Desktop Shell, Navigation, and Operator State | User-facing shell, matrix routing, file tree, toolkit, API key UI, local UI state. | UI and operator workflow behavior. | Runtime engine internals. |
| PKG-03 | Runtime Engine Contract and Turn Lifecycle | Product-owned turn lifecycle, route boundary, session locking, SSE compatibility, interrupts. | `AgentEnginePort`, `TurnEngine`, API transport shape. | SDK-specific message translation details. |
| PKG-04 | SDK Adapter, Prompt, Provider, and Settings | SDK adoption probe, SDK options, prompt composition, provider integration, settings isolation. | SDK-facing implementation and provider boundary. | Chirality event store internals beyond metadata handoff. |
| PKG-05 | Session Audit, Replay, and Tool Result Records | Canonical session layout, `HarnessEvent`, JSONL append/replay, redaction, tool result artifacts. | Runtime audit records and replay surfaces. | Tool permission semantics. |
| PKG-06 | Permissioned Tools, MCP, and Hooks | Deny-first permission overlay, tool exposure, MCP wrappers, hooks, writes, bash, compaction hooks. | Runtime tool execution governance. | Domain-engine operation semantics except protected-path hooks. |
| PKG-07 | Filesystem Execution, Lifecycle, and Dependencies | Working-root truth, execution-root scaffolding, deliverable files, `_STATUS.md`, `Dependencies.csv`, snapshots. | Project file mechanics and deterministic filesystem APIs. | UI presentation except scope scan results. |
| PKG-08 | Agent Suite, Pipeline Dispatch, and Subagent Governance | Agent instruction conformance, matrix/pipeline dispatch, Type 2 subagent governance and child records. | Agent OS behavior and delegation. | General SDK adapter mechanics. |
| PKG-09 | Validation, Packaging, Security, and Release | Required checks, CI, Section 8/9 validation, network/key security, macOS DMG packaging. | Release readiness and test infrastructure. | Feature implementation except test fixtures and packaging glue. |
| PKG-10 | Domain Engine Future Boundary | Generic domain profiles, protected paths, operation proposals, OpenPipeStress fixture posture. | Future platform compatibility. | Current-release domain operation execution. |

---

## 8. Deliverables

### PKG-01 Product Governance and Reliance Boundaries

| DeliverableID | Name | ResponsibleParty | Type | Description | AnticipatedArtifacts | CoversScopeItems | SupportsObjectives | ContextEnvelope | ContextEnvelopeNotes |
|---|---|---|---|---|---|---|---|---|---|
| DEL-01-01 | Governance Alignment, Human Authority, and Project Truth | TBD | DOC_UPDATE | Keep PRD, DIRECTIVE, CONTRACT, SPEC, TYPES, PLAN, and active decomposition mutually consistent while preserving human authority, filesystem project truth, accepted git history, and runtime-audit boundaries as the runtime evolves. | Governance consistency notes; human-authority checklist; project-truth checklist; doc diff checklist; acceptance checklist | SOW-074, SOW-075 | OBJ-009 | M | Cross-document review is broad but bounded to governance alignment and reliance-boundary preservation. |
| DEL-01-02 | Reliance Boundary Register | TBD | REQ_SLICE | Map every P0 audit, permission, filesystem, lifecycle, transcript, settings, subagent, and human-gate boundary to a concrete enforcement surface. | `docs/harness/reliance_boundary_register.md`; enforcement matrix; test index | SOW-037, SOW-045, SOW-054, SOW-057, SOW-074 | OBJ-002, OBJ-005, OBJ-009 | M | A documentation/requirements slice with strong implementation implications. |
| DEL-01-03 | Product Identity and Professional Boundary Copy | TBD | DOC_UPDATE | Preserve Chirality identity and human-only professional authority across UI, docs, packaging, runtime messages, and future domain notices. | UI copy guidelines; release review checklist; boundary notice examples | SOW-071, SOW-074 | OBJ-009, OBJ-010 | S | Focused copy and review deliverable. |
| DEL-01-04 | Scope Boundary and Retired Scope Register | TBD | DOC_UPDATE | Keep remote MCP, plugins, shipped bypass, non-macOS packaging, domain operations, and retired PKG-08 items outside active scope unless amended. | Out-of-scope register; retired-scope notes; amendment triggers | SOW-065, SOW-076, SOW-077, SOW-078 | OBJ-009 | S | Focused scope guard. |

### PKG-02 Desktop Shell, Navigation, and Operator State

| DeliverableID | Name | ResponsibleParty | Type | Description | AnticipatedArtifacts | CoversScopeItems | SupportsObjectives | ContextEnvelope | ContextEnvelopeNotes |
|---|---|---|---|---|---|---|---|---|---|
| DEL-02-01 | Desktop Shell and Matrix Navigation | TBD | UX_UI_SLICE | Maintain PORTAL, WORKBENCH, and PIPELINE shell navigation and canonical matrix routing. | Navigation components; matrix UI tests; route query handling | SOW-001, SOW-005 | OBJ-001 | M | One UI domain with several route states. |
| DEL-02-02 | Workbench and Pipeline Selection UX | TBD | UX_UI_SLICE | Preserve active agent context, category controls, task-scope selectors, and disabled coming-soon variants. | Workbench context UI; pipeline selector behavior; stale selection tests | SOW-006, SOW-007 | OBJ-001 | M | Coherent navigation/routing slice. |
| DEL-02-03 | Working Root File Tree and Scope Scan UI | TBD | UX_UI_SLICE | Provide working-root selector integration, bounded file tree display, deliverable summaries, and scan-state feedback. | File tree panel; deliverable summary widgets; scope scan integration | SOW-002, SOW-003 | OBJ-001, OBJ-006 | M | UI consumes workspace APIs but remains presentation-focused. |
| DEL-02-04 | Toolkit Options and Local UI State | TBD | UX_UI_SLICE | Expose runtime options and preserve pane layout, drafts, and local presets as non-authoritative convenience state. | Toolkit controls; pane resize/collapse state; draft/preset storage guards | SOW-004, SOW-008, SOW-016 | OBJ-001, OBJ-004 | S | Focused local UI state slice. |
| DEL-02-05 | API Key UI and Runtime Feedback | TBD | UX_UI_SLICE | Provide API key entry/status UI, secure-storage feedback, typed runtime errors, and retry-preserving failure states. | API key settings panel; typed error display; secure-storage error UI | SOW-013, SOW-019 | OBJ-001, OBJ-008 | S | Focused UI feedback surface. |

### PKG-03 Runtime Engine Contract and Turn Lifecycle

| DeliverableID | Name | ResponsibleParty | Type | Description | AnticipatedArtifacts | CoversScopeItems | SupportsObjectives | ContextEnvelope | ContextEnvelopeNotes |
|---|---|---|---|---|---|---|---|---|---|
| DEL-03-01 | AgentEnginePort and Engine Conformance Suite | TBD | API_CONTRACT | Define the product-owned runtime boundary and conformance tests for stub and SDK-backed adapters. | `agent-engine-port.ts`; runtime contract docs; conformance tests | SOW-037 | OBJ-002 | M | Single contract/test surface. |
| DEL-03-02 | Thin TurnEngine and Session Locking | TBD | BACKEND_FEATURE_SLICE | Move turn lifecycle, session binding, boot metadata, and active-turn locking behind `TurnEngine`. | `turn-engine.ts`; lock cleanup tests; session lifecycle tests | SOW-009, SOW-010, SOW-011, SOW-038 | OBJ-002 | M | Backend refactor with stable external route shape. |
| DEL-03-03 | Harness API and SSE Compatibility Adapter | TBD | API_CONTRACT | Keep `/api/harness/*` shapes and browser SSE event names stable while runtime policy moves behind services. | Route adapter tests; SSE compatibility fixtures; UI event contract docs | SOW-011, SOW-040 | OBJ-001, OBJ-002 | S | Focused compatibility slice. |
| DEL-03-04 | Interrupt, Cancel, and Terminal Outcome Handling | TBD | BACKEND_FEATURE_SLICE | Ensure interrupts, client disconnects, failures, and cancellations release locks and persist terminal outcomes. | Interrupt tests; cancel cleanup tests; terminal event mapper | SOW-012, SOW-015 | OBJ-002, OBJ-003 | M | Runtime lifecycle slice with clear failure modes. |

### PKG-04 SDK Adapter, Prompt, Provider, and Settings

| DeliverableID | Name | ResponsibleParty | Type | Description | AnticipatedArtifacts | CoversScopeItems | SupportsObjectives | ContextEnvelope | ContextEnvelopeNotes |
|---|---|---|---|---|---|---|---|---|---|
| DEL-04-01 | SDK Probe and Version-Pinned Adoption Decision | TBD | REQ_SLICE | Confirm SDK package version, message sequence, permissions, hooks, MCP, sessions, storage, interrupts, packaging, and fallback triggers. | SDK probe notes; version decision; fallback criteria; residual-risk notes | SOW-018, SOW-044, SOW-046 | OBJ-004 | M | Documentation/probe slice with no new user tool exposure. |
| DEL-04-02 | SdkOptionsBuilder and Settings Isolation | TBD | BACKEND_FEATURE_SLICE | Build deterministic SDK options from session, persona, mode, tools, hooks, MCP, subagents, resume, and settings policy. | `sdk-options-builder.ts`; settings isolation tests; visible tool metadata | SOW-016, SOW-045, SOW-047, SOW-052 | OBJ-004, OBJ-005 | M | Configuration/security slice; permissions deepen in PKG-06. |
| DEL-04-03 | SdkMessageMapper and Provider-Neutral Translation | TBD | BACKEND_FEATURE_SLICE | Translate SDK stream messages into stable `UIEvent`s and provider-neutral `HarnessEvent`s without leaking SDK shape into core contracts. | `sdk-message-mapper.ts`; mapper tests; provider-neutral leakage tests | SOW-040, SOW-044, SOW-051 | OBJ-002, OBJ-004 | M | Focused adapter mapping surface. |
| DEL-04-04 | PersonaComposer from Instruction Root | TBD | BACKEND_FEATURE_SLICE | Replace stub prompt behavior with instruction-root governance, active persona, working-root policy, mode, and tool-surface composition. | `persona-composer.ts`; persona content hash tests; boot fingerprint updates | SOW-017, SOW-030 | OBJ-004, OBJ-007 | M | Prompt composition slice with bounded artifacts. |
| DEL-04-05 | Anthropic Provider Key, Base URL, and Network Bridge | TBD | SECURITY_CONTROL | Preserve API key precedence, Anthropic-only network policy, provider error classification, and redacted SDK environment handoff. | Provider wrapper; key handoff tests; base URL/network tests; redaction fixtures | SOW-019, SOW-020, SOW-021 | OBJ-004, OBJ-008 | M | Security/privacy slice spanning provider boundary. |

### PKG-05 Session Audit, Replay, and Tool Result Records

| DeliverableID | Name | ResponsibleParty | Type | Description | AnticipatedArtifacts | CoversScopeItems | SupportsObjectives | ContextEnvelope | ContextEnvelopeNotes |
|---|---|---|---|---|---|---|---|---|---|
| DEL-05-01 | Canonical Session Folder and Legacy Session Migration | TBD | DATA_MODEL_CHANGE | Introduce `.chirality/sessions/<id>/` layout while keeping legacy `.json` session records listable, resumable, and deletable. | Session folder layout; migration helpers; legacy-read tests | SOW-009, SOW-043, SOW-046 | OBJ-003 | M | Data layout slice with compatibility constraints. |
| DEL-05-02 | HarnessEvent Schema and Append-Only JSONL | TBD | DATA_MODEL_CHANGE | Persist `turn.accepted`, runtime events, and terminal outcomes as ordered, append-only JSONL. | Event schema; JSONL writer; accepted-turn and terminal-event tests | SOW-014, SOW-015, SOW-039 | OBJ-003 | M | Audit-log core slice. |
| DEL-05-03 | Redacted RunLogger and Secret Hygiene | TBD | SECURITY_CONTROL | Redact provider, SDK, tool, and run logs so key material and secrets do not enter runtime records. | Redaction helper; run logger tests; provider error fixtures | SOW-021, SOW-041 | OBJ-003, OBJ-008 | S | Focused security utility. |
| DEL-05-04 | Runtime Replay and Transcript View | TBD | BACKEND_FEATURE_SLICE | Reconstruct accepted turns, assistant output, tool summaries, terminal states, and SDK transcript links from Chirality events. | Replay parser; transcript reconstruction tests; malformed-tail tests | SOW-042, SOW-046 | OBJ-003 | M | Replay/reporting slice over one event store. |
| DEL-05-05 | ToolResultStore and Session Artifacts | TBD | BACKEND_FEATURE_SLICE | Store and preview medium/large tool outputs under session artifacts without flooding chat or model context. | Artifact store; output budget tests; metadata fixtures | SOW-053, SOW-059 | OBJ-003, OBJ-005 | M | Output budget slice shared by tool phases. |

### PKG-06 Permissioned Tools, MCP, and Hooks

| DeliverableID | Name | ResponsibleParty | Type | Description | AnticipatedArtifacts | CoversScopeItems | SupportsObjectives | ContextEnvelope | ContextEnvelopeNotes |
|---|---|---|---|---|---|---|---|---|---|
| DEL-06-01 | ChiralityPermissionOverlay and Mode Mapping | TBD | SECURITY_CONTROL | Implement structured permission decisions, deny-overrides-allow semantics, mode mapping, and `canUseTool` approval mediation. | Permission overlay module; decision records; readOnly/dontAsk/ask tests | SOW-054, SOW-055, SOW-056, SOW-058 | OBJ-005 | M | Permission-policy slice; hooks are separated. |
| DEL-06-02 | SDK Read Tool Surface and Tool Validation | TBD | BACKEND_FEATURE_SLICE | Resolve `opts.tools` to registered SDK built-ins or Chirality MCP names, reject unknowns, and expose read tools before writes/bash. | Tool resolver; unknown-tool tests; deterministic ordering fixtures | SOW-047, SOW-049, SOW-050 | OBJ-005 | M | Tool exposure slice bounded to read-first behavior. |
| DEL-06-03 | Initial Chirality MCP Read Tools | TBD | BACKEND_FEATURE_SLICE | Expose in-process deterministic MCP tools for status read, dependency read, scope scan, and scaffold preview/dry-run. | `mcp__chirality__*` definitions; wrapper metadata; MCP tool tests | SOW-048, SOW-050 | OBJ-005, OBJ-006 | M | Related tools share one MCP wrapper contract. |
| DEL-06-04 | Write/Edit Surface and Path Hooks | TBD | SECURITY_CONTROL | Gate write/edit execution with project-root containment, instruction-root block, symlink rejection, exact edit preconditions, and provenance hooks. | PreToolUse hooks; write/edit tests; provenance metadata; path policy fixtures | SOW-027, SOW-057, SOW-060 | OBJ-005, OBJ-006 | L | Spans filesystem policy and SDK tool use but remains one tool-governance domain. |
| DEL-06-05 | Bash Governance and Timeout Policy | TBD | SECURITY_CONTROL | Keep Bash denied by default and require explicit mode, timeout, capture, output storage, interrupt, and audit behavior before enabling. | Bash deny/default tests; timeout/capture policy; output metadata tests | SOW-062 | OBJ-005 | M | Single powerful-tool guardrail. |
| DEL-06-06 | Hook Lifecycle and Compaction Mirror | TBD | BACKEND_FEATURE_SLICE | Record hook start/stop/failure, stop/finalization, and SDK compaction boundaries into Chirality events. | Hook lifecycle mapper; `context.compacted` tests; terminal hook fixtures | SOW-057, SOW-061 | OBJ-003, OBJ-005 | M | Hook event mirror slice. |

### PKG-07 Filesystem Execution, Lifecycle, and Dependencies

| DeliverableID | Name | ResponsibleParty | Type | Description | AnticipatedArtifacts | CoversScopeItems | SupportsObjectives | ContextEnvelope | ContextEnvelopeNotes |
|---|---|---|---|---|---|---|---|---|---|
| DEL-07-01 | Working Root Validation and Instruction Root Protection | TBD | SECURITY_CONTROL | Enforce working-root validity, root separation, path containment, and instruction-root write protection. | Root validation tests; path policy helpers; instruction-root protection fixtures | SOW-002, SOW-027 | OBJ-006, OBJ-008 | M | Filesystem policy slice with security acceptance. |
| DEL-07-02 | Execution Root Scaffolding from Decomposition | TBD | BACKEND_FEATURE_SLICE | Scaffold SPEC-conformant execution roots from decomposition markdown idempotently and recoverably. | Scaffold parser; `INIT.md`; `_COORDINATION.md`; package/deliverable folders; idempotence tests | SOW-024, SOW-025 | OBJ-006 | M | Existing service domain with multiple file outputs. |
| DEL-07-03 | Deliverable Metadata and Document Kit Contracts | TBD | BACKEND_FEATURE_SLICE | Scan and validate deliverable metadata files, canonical memory, semantic placeholders, and document kit buckets. | Metadata scanners; document kit detection; `_MEMORY.md` rejection tests | SOW-026 | OBJ-006 | M | One deliverable-folder contract slice. |
| DEL-07-04 | Status Transition API and MCP Tool | TBD | BACKEND_FEATURE_SLICE | Parse `_STATUS.md` and enforce forward-only actor-authorized transitions with approval SHA for human gates. | Status parser; transition API/tool; approval SHA tests | SOW-028 | OBJ-006 | M | Lifecycle contract slice with known state machine. |
| DEL-07-05 | Dependencies.csv v3.1 Reader, Writer, and Linter | TBD | BACKEND_FEATURE_SLICE | Read, validate, and write dependency registers while preserving schema, provenance, row lifecycle, and warnings. | Dependency parser/writer; linter tests; provenance fixtures | SOW-029 | OBJ-006 | M | Dependency contract slice. |
| DEL-07-06 | Reference Hash and Snapshot Conventions | TBD | DOC_UPDATE | Preserve deterministic tools/scripts, reference hash behavior, immutable snapshots, and SHA approval conventions without reactivating retired scope. | Snapshot/runbook notes; hash bypass convention; CHANGE/SHA checklist | SOW-032, SOW-033, SOW-034 | OBJ-006, OBJ-009 | S | Focused continuity and convention deliverable. |

### PKG-08 Agent Suite, Pipeline Dispatch, and Subagent Governance

| DeliverableID | Name | ResponsibleParty | Type | Description | AnticipatedArtifacts | CoversScopeItems | SupportsObjectives | ContextEnvelope | ContextEnvelopeNotes |
|---|---|---|---|---|---|---|---|---|---|
| DEL-08-01 | Instruction Root Packaging and Agent Conformance | TBD | TEST_SUITE | Verify required instruction-root assets, agent metadata, write scopes, naming, and section markers. | Agent conformance validator; integrity fixtures; source-completeness checklist | SOW-030, SOW-031, SOW-073 | OBJ-007, OBJ-008 | M | Governance assets and checks; no runtime capability expansion. |
| DEL-08-02 | Persona Alias and Agent Matrix Routing Contract | TBD | UX_UI_SLICE | Keep UI aliases, canonical agent names, matrix routes, and persona resolution consistent. | Alias resolver tests; route fixtures; matrix mapping tests | SOW-005, SOW-006, SOW-017 | OBJ-001, OBJ-007 | S | Focused routing/alias slice. |
| DEL-08-03 | Pipeline Category and Task Scope Dispatch | TBD | UX_UI_SLICE | Dispatch DECOMP/PREP/TASK/AUDIT lanes and dynamic task scope from deliverables and knowledge-type buckets. | Pipeline selector tests; knowledge-type discovery; disabled option handling | SOW-007, SOW-026 | OBJ-001, OBJ-007 | M | UI dispatch slice tied to agent architecture. |
| DEL-08-04 | Type 2 Subagent Governance Bridge | TBD | BACKEND_FEATURE_SLICE | Bridge fail-closed subagent governance to SDK agents with allowlists, sealed context, approval refs, and restricted child tools/cwd. | `evaluateSubagentGovernance` bridge; SDK agent definitions; `Agent` hook tests | SOW-063 | OBJ-005, OBJ-007 | M | Focused subagent governance execution. |
| DEL-08-05 | Subagent Child Run Records and Artifacts | TBD | DATA_MODEL_CHANGE | Persist parent-child runtime records, status, timestamps, SDK agent metadata, and output artifact paths. | Parent-child event records; child output artifact paths; subagent replay fixtures | SOW-063 | OBJ-003, OBJ-007 | M | Data record slice separate from permission gate. |

### PKG-09 Validation, Packaging, Security, and Release

| DeliverableID | Name | ResponsibleParty | Type | Description | AnticipatedArtifacts | CoversScopeItems | SupportsObjectives | ContextEnvelope | ContextEnvelopeNotes |
|---|---|---|---|---|---|---|---|---|---|
| DEL-09-01 | Section 8 Harness Validation Preservation | TBD | TEST_SUITE | Preserve baseline harness validation, current local checks, and stable premerge summary behavior. | Section 8 validation preservation tests; premerge summary checks | SOW-035, SOW-036 | OBJ-008 | M | Test runner preservation slice. |
| DEL-09-02 | Section 9 Runtime Validation Additions | TBD | TEST_SUITE | Add runtime validation IDs for engine contract, SDK mapper, event log, settings isolation, permissions, MCP, hooks, compaction, and subagents. | Section 9 validation IDs; harness runner updates; summary schema | SOW-036, SOW-037, SOW-039, SOW-045, SOW-054, SOW-057, SOW-063 | OBJ-002, OBJ-003, OBJ-005, OBJ-007, OBJ-008 | M | Broad but unified by Section 9 runner. |
| DEL-09-03 | Unit and Integration Test Expansion | TBD | TEST_SUITE | Add focused unit/API/integration tests for TurnEngine, SSE, event replay, attachments, status, dependencies, interrupts, and denied actions. | Jest/API/integration tests; fixtures; regression cases | SOW-011, SOW-012, SOW-014, SOW-015, SOW-022, SOW-028, SOW-029 | OBJ-002, OBJ-003, OBJ-006, OBJ-008 | M | Cross-cutting tests, but bounded to named behaviors. |
| DEL-09-04 | macOS DMG Packaging and Instruction Root Integrity | TBD | CI_CD_CHANGE | Produce the macOS arm64 unsigned DMG and prove required instruction-root assets plus SDK packaging posture are valid. | `desktop:dist`; integrity summary; SDK subprocess packaging probe | SOW-030, SOW-072, SOW-073 | OBJ-008 | L | Broad packaging slice but bounded to one release target. |
| DEL-09-05 | CI Artifact and Release Verification Workflow | TBD | CI_CD_CHANGE | Maintain CI premerge workflow, stable artifact upload, local command sequence, and manual release verification checklist. | CI workflow; stable artifact upload; release verification runbook | SOW-035, SOW-036, SOW-072 | OBJ-008 | M | CI/release workflow slice. |
| DEL-09-06 | Network, Key, Attachment, and Renderer Security Checks | TBD | SECURITY_CONTROL | Verify renderer allowlist, API key redaction/storage, provider endpoint policy, and attachment validation/retry behavior. | Security tests; network guard tests; attachment resolver validation; key storage checks | SOW-019, SOW-020, SOW-022, SOW-023 | OBJ-008 | M | Security validation family. |

### PKG-10 Domain Engine Future Boundary

| DeliverableID | Name | ResponsibleParty | Type | Description | AnticipatedArtifacts | CoversScopeItems | SupportsObjectives | ContextEnvelope | ContextEnvelopeNotes |
|---|---|---|---|---|---|---|---|---|---|
| DEL-10-01 | DomainEngineProfile Contract Draft | TBD | API_CONTRACT | Draft the future profile contract for engine identity, protected paths, proposal paths, operations, manifests, and boundary notices. | Profile schema draft; validation notes; future amendment checklist | SOW-066, SOW-067 | OBJ-010 | M | Future-boundary contract, not current implementation. |
| DEL-10-02 | Protected Path and Proposal Path Policy | TBD | SECURITY_CONTROL | Define future path policy so agents write proposals/summaries but not protected domain-engine model truth. | Protected/proposal path policy; hook implications; examples | SOW-068 | OBJ-010 | M | Security boundary slice. |
| DEL-10-03 | OperationProposal Record and Human Gate Workflow | TBD | DATA_MODEL_CHANGE | Define future domain operation proposal records with deterministic checks, intended changes, risks, outputs, and human gates. | Proposal record shape; gate workflow notes; review checklist | SOW-069 | OBJ-010 | M | Future data model slice. |
| DEL-10-04 | Domain Profile Validation and OpenPipeStress Fixture | TBD | TEST_SUITE | Validate generic domain profiles and model OpenPipeStress as a future fixture without hardcoding solver assumptions into core. | Future fixture profile; validation tests; adapter assumptions note | SOW-070 | OBJ-010 | M | Validation/fixture slice, held for amendment. |
| DEL-10-05 | Domain Boundary Notices and Solver Truth Separation | TBD | DOC_UPDATE | Preserve boundary language that domain engines own domain truth and Chirality does not approve, validate, or own solver results. | Boundary notice copy; domain review checklist; UI/doc examples | SOW-071 | OBJ-009, OBJ-010 | S | Focused copy/review deliverable. |

---

## 9. Scope Ledger

| ScopeItemID | InOutStatus | ScopeItemStatement | SourceRef | PackageID | DeliverableID(s) | ObjectiveID(s) | DecisionRef | OpenIssue | Notes |
|---|---|---|---|---|---|---|---|---|---|
| SOW-001 | IN | Desktop shell with main navigation. | REF-006 Section 8.1 | PKG-02 | DEL-02-01 | OBJ-001 | DEC-004 | FALSE |  |
| SOW-002 | IN | Working-root selection and validation. | REF-006 Section 8.1 | PKG-07 | DEL-07-01 | OBJ-006, OBJ-008 | DEC-004 | FALSE | UI touchpoint covered by DEL-02-03. |
| SOW-003 | IN | File tree and scope scans. | REF-006 Section 8.1 | PKG-02 | DEL-02-03 | OBJ-001 | DEC-004 | FALSE |  |
| SOW-004 | IN | Pane layout and local UI state. | REF-006 Section 8.1 | PKG-02 | DEL-02-04 | OBJ-001 | DEC-004 | FALSE |  |
| SOW-005 | IN | Matrix rendering and routing. | REF-006 Section 8.2 | PKG-02 | DEL-02-01, DEL-08-02 | OBJ-001, OBJ-007 | DEC-004 | FALSE | Primary package is UI. |
| SOW-006 | IN | Workbench context. | REF-006 Section 8.2 | PKG-02 | DEL-02-02, DEL-08-02 | OBJ-001, OBJ-007 | DEC-004 | FALSE |  |
| SOW-007 | IN | Pipeline selectors. | REF-006 Section 8.2 | PKG-08 | DEL-08-03 | OBJ-001, OBJ-007 | DEC-004 | FALSE | Primary package is agent dispatch. |
| SOW-008 | IN | Toolkit options and drafts. | REF-006 Section 8.7 | PKG-02 | DEL-02-04 | OBJ-001 | DEC-004 | FALSE |  |
| SOW-009 | IN | Session CRUD. | REF-006 Section 8.3 | PKG-03 | DEL-03-02, DEL-05-01 | OBJ-002, OBJ-003 | DEC-004 | FALSE |  |
| SOW-010 | IN | Session boot metadata. | REF-006 Section 8.3 | PKG-03 | DEL-03-02 | OBJ-002 | DEC-004 | FALSE |  |
| SOW-011 | IN | SSE turn stream and session locking. | REF-006 Section 8.3 | PKG-03 | DEL-03-02, DEL-03-03, DEL-09-03 | OBJ-001, OBJ-002, OBJ-008 | DEC-004 | FALSE |  |
| SOW-012 | IN | Interrupt/cancel/failure cleanup. | REF-006 Section 8.3 | PKG-03 | DEL-03-04, DEL-09-03 | OBJ-002, OBJ-008 | DEC-004 | FALSE |  |
| SOW-013 | IN | Typed runtime errors. | REF-006 Section 8.3 | PKG-02 | DEL-02-05 | OBJ-001 | DEC-004 | FALSE |  |
| SOW-014 | IN | Persist accepted user input before execution. | REF-006 Section 8.12 | PKG-05 | DEL-05-02, DEL-09-03 | OBJ-003, OBJ-008 | DEC-005 | FALSE |  |
| SOW-015 | IN | Persist terminal turn outcomes. | REF-006 Section 8.12 | PKG-05 | DEL-05-02, DEL-03-04, DEL-09-03 | OBJ-002, OBJ-003, OBJ-008 | DEC-005 | FALSE |  |
| SOW-016 | IN | Deterministic runtime option fallback. | REF-006 Section 8.4 | PKG-04 | DEL-04-02, DEL-02-04 | OBJ-001, OBJ-004 | DEC-005 | FALSE |  |
| SOW-017 | IN | Persona resolution and prompt composition. | REF-006 Section 8.4 | PKG-04 | DEL-04-04, DEL-08-02 | OBJ-004, OBJ-007 | DEC-005 | FALSE |  |
| SOW-018 | IN | SDK-backed Anthropic runtime path. | REF-006 Section 8.4 | PKG-04 | DEL-04-01 | OBJ-004 | DEC-005 | TRUE | OI-001 SDK probe. |
| SOW-019 | IN | API key storage and resolution. | REF-006 Section 8.5 | PKG-09 | DEL-09-06, DEL-04-05, DEL-02-05 | OBJ-004, OBJ-008 | DEC-004 | FALSE |  |
| SOW-020 | IN | Base URL and network allowlist. | REF-006 Section 8.5 | PKG-09 | DEL-09-06, DEL-04-05 | OBJ-004, OBJ-008 | DEC-004 | FALSE |  |
| SOW-021 | IN | Provider error classification. | REF-006 Section 8.5 | PKG-04 | DEL-04-05, DEL-05-03 | OBJ-003, OBJ-004 | DEC-005 | FALSE |  |
| SOW-022 | IN | Attachment resolver validation. | REF-006 Section 8.6 | PKG-09 | DEL-09-06, DEL-09-03 | OBJ-008 | DEC-004 | FALSE |  |
| SOW-023 | IN | Attachment UI and recovery. | REF-006 Section 8.6 | PKG-02 | DEL-02-05, DEL-09-06 | OBJ-001, OBJ-008 | DEC-004 | FALSE |  |
| SOW-024 | IN | Execution-root scaffolding. | REF-006 Section 8.8 | PKG-07 | DEL-07-02 | OBJ-006 | DEC-004 | FALSE |  |
| SOW-025 | IN | Package/deliverable layout. | REF-006 Section 8.8 | PKG-07 | DEL-07-02 | OBJ-006 | DEC-003 | FALSE |  |
| SOW-026 | IN | Metadata files and document kit. | REF-006 Section 8.8 | PKG-07 | DEL-07-03, DEL-08-03 | OBJ-006, OBJ-007 | DEC-004 | FALSE |  |
| SOW-027 | IN | Path containment and instruction-root protection. | REF-006 Section 8.8 | PKG-07 | DEL-07-01, DEL-06-04 | OBJ-005, OBJ-006 | DEC-005 | FALSE |  |
| SOW-028 | IN | Status lifecycle and approval SHA. | REF-006 Section 8.9 | PKG-07 | DEL-07-04, DEL-09-03 | OBJ-006, OBJ-008 | DEC-004 | FALSE |  |
| SOW-029 | IN | Dependencies CSV v3.1. | REF-006 Section 8.9 | PKG-07 | DEL-07-05, DEL-09-03 | OBJ-006, OBJ-008 | DEC-004 | FALSE |  |
| SOW-030 | IN | Instruction-root resources. | REF-006 Section 8.10 | PKG-08 | DEL-08-01, DEL-04-04, DEL-09-04 | OBJ-004, OBJ-007, OBJ-008 | DEC-004 | TRUE | OI-004 source completeness. |
| SOW-031 | IN | Agent instruction metadata conformance. | REF-006 Section 8.10 | PKG-08 | DEL-08-01 | OBJ-007 | DEC-004 | FALSE |  |
| SOW-032 | IN | Deterministic tools/scripts indexed. | REF-006 Section 8.10 | PKG-07 | DEL-07-06 | OBJ-006 | DEC-004 | FALSE |  |
| SOW-033 | IN | Immutable snapshots. | REF-006 Section 8.10 | PKG-07 | DEL-07-06 | OBJ-006 | DEC-004 | FALSE |  |
| SOW-034 | IN | CHANGE/publication SHA checks. | REF-006 Section 8.10 | PKG-07 | DEL-07-06 | OBJ-006, OBJ-009 | DEC-004 | FALSE |  |
| SOW-035 | IN | Required local checks. | REF-006 Section 8.11 | PKG-09 | DEL-09-01, DEL-09-05 | OBJ-008 | DEC-004 | FALSE |  |
| SOW-036 | IN | Section 8/9 validation. | REF-006 Section 8.11 | PKG-09 | DEL-09-01, DEL-09-02, DEL-09-05 | OBJ-008 | DEC-004 | FALSE |  |
| SOW-037 | IN | Product-owned engine contract. | REF-006 Section 8.12 | PKG-03 | DEL-03-01, DEL-01-02, DEL-09-02 | OBJ-002, OBJ-009 | DEC-005 | FALSE |  |
| SOW-038 | IN | Thin TurnEngine and route extraction. | REF-006 Section 8.12 | PKG-03 | DEL-03-02 | OBJ-002 | DEC-005 | FALSE |  |
| SOW-039 | IN | Append-only HarnessEvent JSONL. | REF-006 Section 8.12 | PKG-05 | DEL-05-02, DEL-09-02 | OBJ-003, OBJ-008 | DEC-005 | FALSE |  |
| SOW-040 | IN | UIEvent and HarnessEvent separation. | REF-006 Section 8.12 | PKG-03 | DEL-03-03, DEL-04-03 | OBJ-002, OBJ-004 | DEC-005 | FALSE |  |
| SOW-041 | IN | Runtime redaction. | REF-006 Section 8.12 | PKG-05 | DEL-05-03 | OBJ-003, OBJ-008 | DEC-005 | FALSE |  |
| SOW-042 | IN | Runtime replay. | REF-006 Section 8.12 | PKG-05 | DEL-05-04 | OBJ-003 | DEC-005 | FALSE |  |
| SOW-043 | IN | Legacy session migration. | REF-006 Section 8.12 | PKG-05 | DEL-05-01 | OBJ-003 | DEC-005 | FALSE |  |
| SOW-044 | IN | SDK message mapping. | REF-006 Section 8.12 | PKG-04 | DEL-04-01, DEL-04-03 | OBJ-002, OBJ-004 | DEC-005 | TRUE | OI-001 SDK probe. |
| SOW-045 | IN | SDK settings isolation. | REF-006 Section 8.12 | PKG-04 | DEL-04-02, DEL-09-02, DEL-01-02 | OBJ-004, OBJ-008, OBJ-009 | DEC-005 | TRUE | OI-001 SDK probe confirms exact SDK behavior. |
| SOW-046 | IN | SDK session link and transcript placement. | REF-006 Section 8.12 | PKG-05 | DEL-05-01, DEL-05-04, DEL-04-01 | OBJ-003, OBJ-004 | DEC-005 | TRUE | OI-002 transcript placement. |
| SOW-047 | IN | Tool option mapping. | REF-006 Section 8.13 | PKG-06 | DEL-06-02, DEL-04-02 | OBJ-004, OBJ-005 | DEC-005 | FALSE |  |
| SOW-048 | IN | Chirality MCP descriptors. | REF-006 Section 8.13 | PKG-06 | DEL-06-03 | OBJ-005, OBJ-006 | DEC-005 | FALSE |  |
| SOW-049 | IN | Deterministic tool surface. | REF-006 Section 8.13 | PKG-06 | DEL-06-02 | OBJ-005 | DEC-005 | FALSE |  |
| SOW-050 | IN | Read tools before writes/bash. | REF-006 Section 8.13 | PKG-06 | DEL-06-02, DEL-06-03 | OBJ-005 | DEC-005 | FALSE |  |
| SOW-051 | IN | SDK model/tool loop mirrored by events. | REF-006 Section 8.13 | PKG-04 | DEL-04-03 | OBJ-004 | DEC-005 | FALSE |  |
| SOW-052 | IN | Max-turn guards. | REF-006 Section 8.13 | PKG-04 | DEL-04-02 | OBJ-004 | DEC-005 | FALSE |  |
| SOW-053 | IN | Deterministic event ordering under tool concurrency. | REF-006 Section 8.13 | PKG-05 | DEL-05-05 | OBJ-003, OBJ-005 | DEC-005 | FALSE |  |
| SOW-054 | IN | Structured permission decisions. | REF-006 Section 8.14 | PKG-06 | DEL-06-01, DEL-09-02, DEL-01-02 | OBJ-005, OBJ-008, OBJ-009 | DEC-005 | FALSE |  |
| SOW-055 | IN | Permission modes and deny-first overlay. | REF-006 Section 8.14 | PKG-06 | DEL-06-01 | OBJ-005 | DEC-005 | FALSE |  |
| SOW-056 | IN | Tool permission events. | REF-006 Section 8.14 | PKG-06 | DEL-06-01 | OBJ-005 | DEC-005 | FALSE |  |
| SOW-057 | IN | Hooks and fail-closed behavior. | REF-006 Section 8.14 | PKG-06 | DEL-06-04, DEL-06-06, DEL-09-02, DEL-01-02 | OBJ-003, OBJ-005, OBJ-008, OBJ-009 | DEC-005 | FALSE |  |
| SOW-058 | IN | Interactive approval through `canUseTool`. | REF-006 Section 8.14 | PKG-06 | DEL-06-01 | OBJ-005 | DEC-005 | FALSE |  |
| SOW-059 | IN | Tool result budgets and artifacts. | REF-006 Section 8.15 | PKG-05 | DEL-05-05 | OBJ-003, OBJ-005 | DEC-005 | FALSE |  |
| SOW-060 | IN | Safe write/edit behavior. | REF-006 Section 8.15 | PKG-06 | DEL-06-04 | OBJ-005, OBJ-006 | DEC-005 | FALSE |  |
| SOW-061 | IN | Compaction mirror. | REF-006 Section 8.15 | PKG-06 | DEL-06-06 | OBJ-003, OBJ-005 | DEC-005 | FALSE |  |
| SOW-062 | IN | Bash denied by default and governed when enabled. | REF-006 Section 8.15 | PKG-06 | DEL-06-05 | OBJ-005 | DEC-005 | FALSE |  |
| SOW-063 | IN | Governed subagent runtime. | REF-006 Section 8.15 | PKG-08 | DEL-08-04, DEL-08-05, DEL-09-02 | OBJ-003, OBJ-005, OBJ-007, OBJ-008 | DEC-005 | FALSE |  |
| SOW-064 | IN | MCP extension boundaries. | REF-006 Section 8.15 | PKG-06 | DEL-06-02, DEL-06-03 | OBJ-005 | DEC-005 | FALSE |  |
| SOW-065 | OUT | Remote MCP/plugins out of current scope. | REF-006 Section 3.2 | PKG-01 | DEL-01-04 | OBJ-009 | DEC-006 | FALSE | Boundary item, not implementation scope. |
| SOW-066 | IN | Future Domain Engine Profile compatibility. | REF-006 Section 8.17 | PKG-10 | DEL-10-01 | OBJ-010 | DEC-006 | TRUE | OI-005 future amendment. |
| SOW-067 | IN | Generic domain profile contract. | REF-006 Section 8.17 | PKG-10 | DEL-10-01 | OBJ-010 | DEC-006 | TRUE | OI-005 future amendment. |
| SOW-068 | IN | Protected/proposal paths for domain engines. | REF-006 Section 8.17 | PKG-10 | DEL-10-02 | OBJ-010 | DEC-006 | TRUE | OI-005 future amendment. |
| SOW-069 | IN | OperationProposal records. | REF-006 Section 8.17 | PKG-10 | DEL-10-03 | OBJ-010 | DEC-006 | TRUE | OI-005 future amendment. |
| SOW-070 | IN | OpenPipeStress fixture profile. | REF-006 Section 8.17 | PKG-10 | DEL-10-04 | OBJ-010 | DEC-006 | TRUE | OI-005 future amendment. |
| SOW-071 | IN | Domain professional boundary. | REF-006 Section 8.17 | PKG-10 | DEL-10-05, DEL-01-03 | OBJ-009, OBJ-010 | DEC-006 | TRUE | OI-005 future amendment. |
| SOW-072 | IN | macOS arm64 unsigned DMG release target. | REF-006 Section 6.2 | PKG-09 | DEL-09-04, DEL-09-05 | OBJ-008 | DEC-004 | TRUE | OI-003 packaging verification. |
| SOW-073 | TBD | Source completeness for instruction-root assets. | REF-006 Section 15 | PKG-09 | DEL-09-04, DEL-08-01 | OBJ-007, OBJ-008 | DEC-004 | TRUE | OI-004 source completeness. |
| SOW-074 | IN | Human authority/professional boundaries. | REF-001 Section 3 | PKG-01 | DEL-01-01, DEL-01-02, DEL-01-03 | OBJ-009 | DEC-001 | FALSE |  |
| SOW-075 | IN | Local project truth, no hidden project memory. | REF-001 Section 2 | PKG-01 | DEL-01-01, DEL-07-01 | OBJ-006, OBJ-009 | DEC-001 | FALSE |  |
| SOW-076 | OUT | Ambient settings and shipped bypass forbidden. | REF-006 Section 3.2 | PKG-01 | DEL-01-04, DEL-04-02 | OBJ-004, OBJ-009 | DEC-005 | FALSE | Boundary item. |
| SOW-077 | OUT | Retired PKG-08 scope remains retired. | REF-006 Section 15 | PKG-01 | DEL-01-04, DEL-07-06 | OBJ-006, OBJ-009 | DEC-007 | FALSE | Boundary item. |
| SOW-078 | OUT | Windows/Linux packaging out of scope. | REF-006 Section 6.4 | PKG-01 | DEL-01-04, DEL-09-04 | OBJ-008, OBJ-009 | DEC-004 | FALSE | Boundary item. |

---

## 10. Coverage and Telemetry

| Metric | Value |
|---|---:|
| Revision | v3.2 source-governed working surface |
| Date | 2026-05-20 |
| ScopeItemCount | 78 |
| PackageCount | 10 |
| DeliverableCount | 51 |
| ObjectiveCount | 10 |
| UnassignedScopeItems | 0 |
| ScopeItemsWithoutDeliverableMapping | 0 |
| UnmappedObjectives | 0 |
| ContextEnvelopeCounts | S=9, M=40, L=2, XL=0 |
| OpenIssuesByType | SDK_PROBE=1, SDK_TRANSCRIPT=1, PACKAGING=1, SOURCE_COMPLETENESS=1, DOMAIN_FUTURE=1 |
| OpenIssueAffectedScopeCounts | SDK_PROBE=3, SDK_TRANSCRIPT=1, PACKAGING=1, SOURCE_COMPLETENESS=2, DOMAIN_FUTURE=6 |

### Context Budget QA

| Envelope | Deliverables | QA Result |
|---|---|---|
| S | DEL-01-03, DEL-01-04, DEL-02-04, DEL-02-05, DEL-03-03, DEL-05-03, DEL-07-06, DEL-08-02, DEL-10-05 | Acceptable small slices. |
| M | All other deliverables except listed L items | Acceptable bounded Type 2 work. |
| L | DEL-06-04, DEL-09-04 | Accepted large-but-single-domain slices; each has context notes and should be split only if implementation review finds broad cross-domain churn. |
| XL | None | No XL deliverables accepted. |

---

## 10A. Non-PRD Control Coverage

This section is normative for v3.2 downstream review. The decomposition is not considered complete if PRD requirements are covered but DIRECTIVE intent, CONTRACT invariants, SPEC mechanics, TYPES vocabulary, PLAN sequencing, or SOFTWARE_DECOMP method rules are violated.

### 10A.1 CONTRACT Invariant Coverage

The decomposition package maintains CONTRACT invariant coverage as companion machine-truth. CONTRACT `K-*` invariants are binding and should be mapped to primary owner packages, deliverables, enforcement surfaces, validation surfaces, and open issues. This prevents PRD-only execution and gives REVIEW a direct way to check safety, audit, permission, lifecycle, runtime, release, and domain-boundary obligations.

Compact invariant-family ownership:

| Invariant Family | Primary Coverage | Notes |
|---|---|---|
| `K-PRD`, `K-HIER`, `K-ID`, `K-PATH`, `K-FS`, `K-GIT`, `K-NOMEM` | PKG-01, PKG-05, PKG-07 | Product direction, project truth, stable identity, package flatness, path-as-projection, session/event state. |
| `K-AUTH`, `K-BIND`, `K-GATE`, `K-PROF` | PKG-01, PKG-07, PKG-10 | Human gates, binding/non-binding record separation, approval SHA, professional-boundary copy. |
| `K-ROOT`, `K-PACKAGE` | PKG-07, PKG-08, PKG-09 | Instruction-root/working-root separation, instruction-root write protection, packaged resource integrity. |
| `K-CORE`, `K-ENGINE`, `K-RELIANCE`, `K-SDK` | PKG-01, PKG-03, PKG-04, PKG-09 | Product-owned terms, engine contract, SDK isolation, conformance, fallback. |
| `K-EVENT` | PKG-03, PKG-05, PKG-09 | UI/runtime event split, accepted-turn persistence, terminal outcomes, redaction. |
| `K-PERM`, `K-TOOL`, `K-MCP`, `K-HOOK`, `K-PATH`, `K-BASH` | PKG-04, PKG-06, PKG-07, PKG-09 | Deny-first policy, tool exposure, MCP as transport, hooks, path containment, bash denial. |
| `K-STATUS`, `K-DEP`, `K-PROV`, `K-INVENT`, `K-CONFLICT`, `K-SNAP`, `K-REF` | PKG-01, PKG-07 | Lifecycle, dependency, provenance, TBD discipline, conflict surfacing, snapshots, reference tooling. |
| `K-WRITE`, `K-SEAL`, `K-GHOST`, `K-SUBAGENT` | PKG-08 | Agent write scopes, sealed Type 2 context, no ghost inputs, fail-closed subagent governance and child-run records. |
| `K-NET`, `K-KEY`, `K-ATTACH`, `K-RELEASE`, `K-VALIDATE`, `K-RETIRED` | PKG-01, PKG-09 | Network, keys, attachments, release, validation, retired scope. |
| `K-DOMAIN` | PKG-10 | Future domain boundary, protected paths, OperationProposal, solver-truth separation. |

### 10A.2 SPEC Binding Notes

Downstream deliverables must preserve SPEC-defined physical and runtime contracts, including instruction-root and working-root separation, execution-root layout, deliverable metadata files, `_STATUS.md` lifecycle transitions, `Dependencies.csv` v3.1, canonical session layout, `HarnessEvent` schema, browser SSE event names, SDK settings isolation, MCP tool names, hooks, attachment policy, API key policy, network policy, and Section 8/9 validation IDs.

### 10A.3 TYPES Vocabulary and Type Targets

Downstream deliverables must use TYPES vocabulary and stable ID rules. Runtime contracts should preserve the TYPES targets for `HarnessEvent`, `HarnessPermissionDecision`, `HarnessSubagentRun`, `DomainEngineProfile`, and `OperationProposal` unless a governed amendment changes them.

### 10A.4 PLAN Roadmap Overlay

Packages are work domains, not execution phases. PLAN controls near-term sequencing: R0/R1 runtime scope, SDK probe, reliance-boundary register, engine contract, TurnEngine, event log, prompt composer, settings isolation, and run logger precede tool expansion. Read tools precede write/edit/bash. Domain-engine work remains future-boundary scope until core runtime stability.

---

## 10B. v3.2 Acceptance Checklist

| Check | Required Result |
|---|---|
| Source corpus alignment | DIRECTIVE, CONTRACT, SPEC, TYPES, PLAN, PRD, and SOFTWARE_DECOMP method rules are all reflected as active sources. |
| PRD traceability alignment | `docs/PRD.md` Section 16 points to this v3.2 decomposition as the active package/deliverable topology. |
| Topology stability | 78 scope items, 10 packages, 51 deliverables, 10 objectives, S=9/M=40/L=2/XL=0 remain unchanged. |
| Package flatness | No package nesting, phase packages, or sub-package layer. |
| Deliverable ID coupling | Every `DEL-XX-YY` remains coupled to `PKG-XX`. |
| Scope ledger coverage | Every scope item has exactly one owner package and at least one mapped deliverable, except explicit OUT/TBD boundary handling. |
| CONTRACT invariant coverage | `contract_invariant_coverage_register.csv` is created, synchronized with this decomposition, or explicitly deferred before REVIEW closure. |
| SPEC conformance | Execution-root layout, deliverable metadata, session layout, event schema, SSE names, SDK settings, hooks, MCP names, API key policy, network policy, and validation IDs remain intact. |
| TYPES conformance | Stable identifiers, runtime vocabulary, permission decision shape, subagent run shape, and future domain profile/proposal vocabulary remain intact. |
| PLAN sequencing | R0/R1 precedes R2+ capability expansion; read tools precede writes/bash; domain execution stays future-amendment scope. |
| Professional-boundary posture | No automated approval, certification, issue, solver-truth, code-compliance, or external-validation claim is introduced. |
| Retired scope | Retired PKG-08 hardening items remain out of active scope unless governed amendment reactivates them. |

---

## 11. Open Issues

| IssueID | Type | AffectedScope | Description | Required Resolution |
|---|---|---|---|---|
| OI-001 | SDK_PROBE | SOW-018, SOW-044, SOW-045 | SDK viability, message categories, settings behavior, hooks, permissions, MCP, sessions, and packaging must be empirically confirmed. | Complete R0 SDK probe before R1 production default. |
| OI-002 | SDK_TRANSCRIPT | SOW-046 | SDK transcript placement/mirroring under project-controlled storage is not yet decided. | R1 must choose `SessionStore`, `CLAUDE_CONFIG_DIR`, both, or cross-reference default path as residual risk. |
| OI-003 | PACKAGING | SOW-072 | SDK subprocess and macOS DMG packaging must be verified after SDK adoption. | R1 packaging probe and `desktop:dist` validation. |
| OI-004 | SOURCE_COMPLETENESS | SOW-030, SOW-073 | Required instruction-root assets may be missing in the current source or packaging state. | Complete source tree or amend integrity requirements and code paths. |
| OI-005 | DOMAIN_FUTURE | SOW-066-SOW-071 | Domain engine profile work is future platform scope and requires amendment before implementation. | Keep domain deliverables as future-boundary package until core harness stability. |

---

## 12. Decision Log / Change Log

| DecisionRef | Date | Decision | Rationale |
|---|---|---|---|
| DEC-001 | 2026-05-20 | The six active docs are the complete decomposition source corpus. | User specified docs folder as the source set. |
| DEC-002 | 2026-05-20 | Gates 1-7 are recorded as passed by implicit human approval. | User instructed implicit approval through all gates. |
| DEC-003 | 2026-05-20 | Use `PKG-XX` and `DEL-XX-YY` IDs. | SOFTWARE_DECOMP mandates two-digit IDs; current docs permit them. |
| DEC-004 | 2026-05-20 | Partition by work domain, not roadmap phase. | Required by SOFTWARE_DECOMP and CONTRACT flat-package invariant. |
| DEC-005 | 2026-05-20 | SDK scope is decomposed behind Chirality-owned contracts. | Approved PRD says SDK-privileged, contract-owned, Chirality-governed. |
| DEC-006 | 2026-05-20 | Domain-engine requirements are represented as future-boundary deliverables. | PRD keeps domain engines future scope, not first implementation slice. |
| DEC-007 | 2026-05-20 | Retired PKG-08 items are tracked as boundary scope only. | PRD and PLAN prohibit reactivation without amendment. |
| DEC-008 | 2026-05-20 | No XL deliverables are accepted in this decomposition. | Type 2 downstream execution requires bounded context. |
| DEC-009 | 2026-05-20 | v2.5 uses the 10-package runtime-boundary structure and imports execution polish from the alternative decomposition. | The 10-package structure better separates runtime contract, SDK adapter, session audit, permissioned tools, filesystem governance, validation, and future-domain scope; the alternative improved handoff clarity. |
| DEC-010 | 2026-05-20 | Non-PRD governance documents are incorporated as controlling constraints, not optional background. | DIRECTIVE, CONTRACT, SPEC, TYPES, and PLAN provide authority, invariants, mechanics, vocabulary, and roadmap sequencing beyond PRD requirements. |
| DEC-011 | 2026-05-20 | CONTRACT invariant coverage should be maintained as a companion register. | Invariant coverage is machine-truth heavy and better handled as a companion surface than as prose in the main decomposition. |
| DEC-012 | 2026-05-20 | PLAN roadmap sequencing is treated as a blocker overlay, not package architecture. | SOFTWARE_DECOMP packages remain flat work domains; execution order is controlled separately by R0-R7 sequencing. |
| DEC-013 | 2026-05-20 | v3.1 is adopted as the basis for v3.2. | v3.1 is stronger than the local v3 as a source-governed working surface because it makes non-PRD control sources, invariant coverage, SPEC/TYPES conformance, PLAN sequencing, and downstream acceptance explicit. |
| DEC-014 | 2026-05-20 | v3.2 anchors the decomposition to the active local docs corpus and SOFTWARE_DECOMP method file. | Downloaded proposal artifacts are useful inputs, but active decomposition authority should point to the current repo documents and method standard. |
| DEC-015 | 2026-05-20 | `contract_invariant_coverage_register.csv` is a planned required companion register until the artifact exists. | REVIEW should require invariant coverage, but this decomposition should not claim an authoritative companion CSV has already been created. |
| DEC-016 | 2026-05-20 | PRD Section 16 package traceability is updated to point to v3.2. | The active decomposition has 10 packages and 51 deliverables; the PRD now identifies this v3.2 SOFTWARE_DECOMP snapshot as the authority for scaffolding and downstream execution. |

### Change Log

- 2026-05-20: Initial SOFTWARE_DECOMP working surface created from active `docs/` corpus.
- 2026-05-20: v2.5 amalgamated version added: retained 10-package structure, added deliverable descriptions, responsible-party placeholders, context notes, hard constraints, and downstream execution notes.
- 2026-05-20: v3 local full-governance correction added: considered all six active docs, restored SOFTWARE_DECOMP method posture, and emphasized human authority and filesystem/git project truth.
- 2026-05-20: v3.1 source-governed proposal reviewed: accepted as the better basis because it adds source authority, non-PRD control coverage, acceptance checks, and companion-register posture.
- 2026-05-20: v3.2 issued: adopted v3.1 topology, anchored references to active local docs and SOFTWARE_DECOMP, corrected companion-register status, updated source-completeness wording, incorporated v3's human-authority/project-truth emphasis into DEL-01-01, and aligned PRD Section 16 to the v3.2 decomposition authority.

---

## 13. Downstream Execution Notes

- PREPARATION should scaffold from this v3.2 working surface unless a later human ruling replaces it.
- TASK / Type 2 agents should execute one deliverable at a time, preserve the `ResponsibleParty: TBD` field until a human assigns ownership, and treat `ContextEnvelope` as a work-sizing constraint.
- R0/R1 runtime deliverables should execute before R2+ capability expansion: engine contract, SDK probe, settings isolation, TurnEngine, event log, prompt composer, run logger, and conformance suite come first.
- Read tools and read MCP exposure precede write/edit and bash capability.
- Domain engine, remote MCP, plugin, shipped bypass, non-macOS packaging, and retired PKG-08 work require governed amendment before implementation.
- REVIEW should check package flatness, scope ledger coverage, context-envelope posture, no automated professional approval claims, SDK settings isolation, and no domain solver ownership claims.
- REVIEW should also check CONTRACT invariant-family coverage, the companion invariant register, SPEC/TYPES conformance, PLAN sequencing, PRD traceability, and SOFTWARE_DECOMP method conformance before accepting implementation or scaffold outputs.
