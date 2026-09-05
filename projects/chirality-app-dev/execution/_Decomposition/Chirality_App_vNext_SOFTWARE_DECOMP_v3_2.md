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

v3.2 does **not** renumber scope items, packages, deliverables, objectives, decisions, or open issues. SCA-APP-001 preserves the topology and amends the runtime/provider strategy, Pi posture, and permission-governance semantics without changing package or deliverable IDs.

SCA-APP-006 preserves the same topology while making the CONTRACT invariant companion register live, establishing field-level authority precedence and Scope Ledger / Deliverables reverse-view parity, reconciling seven supported mappings, and refreshing the accepted PRD source identity.

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
| REF-001 | `docs/DIRECTIVE.md` | Intent, authority, professional boundaries | `e1a3d00b18fa728f0886f036774c4825ad8f65f3245b56b4545da2714a903031` |
| REF-002 | `docs/CONTRACT.md` | Invariants and enforcement surfaces | `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7` |
| REF-003 | `docs/SPEC.md` | Physical structures, runtime mechanics, API/file contracts | `eee520f783ce0161c84bb8c2bd570b7521b3f6926bceea8cde7d387bbc3df990` |
| REF-004 | `docs/TYPES.md` | Vocabulary, identifiers, enums, type targets | `998785af3a0f14a87424339ccb6b242b8932f7a572c4336ac47538c64f3e3169` |
| REF-005 | `docs/PLAN.md` | Roadmap and implementation sequencing | `c2196a1076a5e2de44faca7df506a72f0401d0a0161f77a8b583a1d0d7e239ff` |
| REF-006 | `docs/PRD.md` | Product requirements, runtime direction, and approved vNext scope | `ef638f43ccae1cd78b26b1ae078a33770cf64cc36c247c5d7da04b35196a4010` |
| REF-007 | `agents/AGENT_SOFTWARE_DECOMP.md` | Decomposition method, gate protocol, package/deliverable structure, and Context Envelope discipline | `ad849d9a927485d8749713070579cf072663a2efab63abef2b7db16efeb43409` |

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
| `contract_invariant_coverage_register.csv` | Authoritative companion register | Maps exactly 81 CONTRACT invariant IDs in 48 families to semantic-owner authority, App obligations and topology, enforcement and validation surfaces, evidence disposition, and open issues. |

v3.2 acceptance is conditional on the following invariants remaining true:

- no change to the 10-package / 51-deliverable topology without explicit human renumbering approval;
- no implementation work that exposes write, bash, subagent execution, remote MCP, plugins, unvalidated provider/network expansion, or domain operations ahead of the approved provider-adapter and capability-policy sequencing;
- no product-critical P0 reliance boundary delegated to prompt text or opaque provider/SDK defaults alone;
- no reactivation of retired PKG-08 hardening scope by runtime event logging or validation wording;
- no change to macOS arm64 unsigned DMG release target without governed amendment.


---

## 3. Intake Summary

Chirality App vNext is a local-first desktop agent harness for governed professional work over a selected filesystem working root. The application packages a release-managed instruction root, keeps project truth in plain files and accepted git history, and treats runtime logs as audit evidence rather than approval records.

The approved runtime direction is a Root-owned provider-neutral generic runtime with App-client integration, compatibility, packaging, and conformance evidence. Root owns the generic contracts, orchestration, daemon, client, CLI, and safe adapters. One opt-in per-user daemon exclusively owns runtime engines, credentials, sessions, delegation, tools, turn locks, interruption, and local-model residency. The packaged Electron application supplies daemon mode so the existing App identity and encrypted `safeStorage` credential boundary remain single-owner. External provider SDKs supply agent-loop mechanics only behind the Root-owned runtime boundary. App retains its browser, API, UI, packaging, project-authority, project-specific deterministic-act, human-gate, and affected-client evidence duties without acquiring generic runtime semantic ownership. Claude Agent SDK / Anthropic remains the first concrete adapter, key-aware default, and supervisor. D-APP-72 / SCA-APP-002 authorizes one bounded second-engine tranche: Electron `43.1.1`, in-process Pi `0.80.10`, authenticated `127.0.0.1` oMLX, and a governed read-only Agent 2 child.

The next App implementation objective is to conform the existing desktop shell, packaged daemon mode, HTTP routes, and compatibility surfaces to the Root-owned runtime: preserve the ruled contract re-export, proxy `/api/harness/*` through the sole daemon, retain browser route and SSE behavior, consume daemon sessions and operational runtime evidence, preserve checkout-contained project authority, and produce affected-client conformance and acceptance evidence. Consequential generic runtime changes activate Root `DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance`; App work does not transfer ownership of generic runtime semantics.

### Hard Constraints Captured

- Packages are flat work domains, not phases.
- Deliverables are the smallest executable unit; no task sub-level is introduced.
- Stable IDs use `PKG-XX` and `DEL-XX-YY`.
- App R0/R1 runtime-client compatibility, thin proxy behavior, and conformance to the Root-owned runtime contract and first adapter remain the immediate App slice; consequential generic runtime changes use Root `DEL-02-06`.
- Browser-facing route shapes and SSE event names remain stable during the runtime pivot.
- Daemon-managed JSON/JSONL is operational runtime evidence; App consumes it for client replay, diagnostics, and acceptance evidence without treating daemon state as checkout-contained project authority.
- `settingSources: []` is required for shipped SDK builds.
- Tool availability alone is not a restriction boundary; exposure requires capability policy, explicit deny precedence, hooks where needed, and evidence records.
- Write, bash, subagent, remote MCP, plugin, concrete non-Anthropic provider, and domain-operation capabilities remain gated until their governance and validation deliverables pass.
- Product identity remains Chirality; professional approval remains human-only.
- Retired PKG-08 scope is not reactivated.
- Source authority is layered: DIRECTIVE, CONTRACT, SPEC, TYPES, PLAN, and PRD are all decomposition inputs.
- Project truth lives in versioned working-root files and accepted git history, not chats, SDK transcripts, hidden state, or runtime convenience data.
- Runtime events explain work; they do not approve work or make deliverables professionally reliable.
- Unknowns become `TBD`; assumptions and proposals must remain labeled until human acceptance.
- P0 reliance boundaries must be enforced by Chirality code, verified adapter callbacks/hooks, deterministic tools, release checks, or human gates; prompt text alone is insufficient.
- Pi remains a pattern corpus/reference outside the exact D-APP-72 / SCA-APP-002 exception. The exception permits App packaging and client conformance for only pinned Pi `0.80.10` in-process after Electron `43.1.1`, authenticated loopback oMLX, Root-owned provider-neutral contracts/tools, and one governed read-only Agent 2 child. Pi fork/sidecar/native capabilities/ambient discovery, remote providers, direct supervisors, automatic fallback, and write/shell/network tools remain out.
- Permission governance is capability-forward and policy-mediated. Useful agent tool use is enabled when allowed by mode, boundary policy, evidence capture, and human gates. Explicit hard denies override allows at reliance boundaries, secrets, protected paths, release/professional claims, destructive actions, and unvalidated provider/network expansion.
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
| Runtime Audit Mirror | Chirality audit JSONL, `events.jsonl` | Daemon-managed operational runtime evidence consumed by App diagnostics, replay, and acceptance evidence; it is not checkout-contained project authority. |
| SDK Transcript | Claude transcript, SDK session transcript | Secondary runtime artifact unless imported as `HarnessEvent`. |
| AgentEnginePort | RuntimeEngineContract boundary | Root-owned generic runtime engine contract consumed by the App client; App verifies compatibility and conformance without redefining it. |
| EngineAdapter | SDK adapter, provider adapter | Provider/SDK-specific translator behind Root-owned generic runtime contracts; App retains only its separately authorized client, packaging, and conformance work. |
| Provider Adapter | engine adapter, provider integration | Concrete integration layer behind the Root-owned generic runtime boundary. Claude Agent SDK / Anthropic remains the first concrete/current adapter; generic-versus-private component classification remains separately governed. |
| Pi Pattern Corpus | Pi reference, pattern source | Stable patterns remain reference material; D-APP-72 adds one bounded runtime exception without authorizing general Pi adoption. |
| Pi Adapter | bounded second engine | Root-runtime engine path using in-process Pi `0.80.10` behind `AgentEnginePort`; App packaging/client conformance remains opt-in and initially restricted to a governed read-only Agent 2 child. |
| oMLX Provider | local model provider | Root-runtime local-model provider over an authenticated OpenAI-compatible endpoint restricted to `127.0.0.1`; App requests and presents explicit status without owning residency. |
| Capability Policy | permission policy, tool policy | Project/App policy inputs constrain the daemon's generic tool exposure and execution for a session, persona, mode, provider adapter, and validation state. |
| Explicit Deny Precedence | hard deny, deny-overrides-allow | Overrides allows at defined reliance, secret, protected-path, professional, destructive-action, or unvalidated expansion boundaries. |
| TurnEngine | turn lifecycle owner | Root-owned daemon turn-lifecycle service behind App client/proxy routes. |
| HarnessEvent | runtime event | Root-owned generic operational runtime event contract consumed by App without transferring project authority or generic persistence ownership. |
| UIEvent | browser SSE event | Compact browser contract, separate from `HarnessEvent`. |
| PersonaComposer | prompt composer, system prompt builder | Reads instruction-root governance and active persona. |
| SdkOptionsBuilder | SDK option mapper | Root-runtime adapter option mapping; App supplies project/client inputs and verifies compatibility without owning generic adapter semantics. |
| ChiralityPermissionOverlay | permission policy, capability policy | App/project policy and human decisions constrain daemon-side tool execution through provider/SDK modes, deny lists, hooks, and `canUseTool`. |
| Chirality MCP Tool | `mcp__chirality__*` tool | Deterministic in-process tool, not a bypass. |
| Hook | SDK callback, runtime guard | Root runtime executes generic hooks; project/App hooks retain project-specific policy, deterministic acts, and human-gate authority. |
| ToolResultStore | artifact store, result budget | Daemon operational store for large tool output; App consumes previews and records separately accepted checkout evidence. |
| SubagentGovernanceBridge | governed SDK agents bridge | App/project authority supplies sealed briefs, permissions, and approval references; the daemon owns operational delegation execution. |
| SessionRecord | session metadata | Daemon-owned operational session metadata consumed by App client/replay surfaces and linked to separately authoritative checkout evidence where applicable. |
| HarnessPermissionDecision | permission decision record | Structured allow, deny, or application-level ask decision with reason/source metadata. |
| HarnessSubagentRun | subagent child run record | Checkout-contained AgentRun/evidence record linked to daemon operational delegation state without transferring project authority. |
| SDK built-in tool | `Read`, `Glob`, `Grep`, `LS`, `Write`, `Edit`, `Bash` | SDK-supplied tool names requested through App/project policy and executed through the Root-owned generic runtime boundary. |
| allowedTools | SDK auto-approval tool option | Not a restriction boundary by itself. |
| disallowedTools | SDK or overlay denial tool option | Used with mode policy, hooks, and callbacks to prevent execution/exposure. |
| canUseTool | SDK permission callback | App-mediated human/project decision path returned to the daemon; checkout approval evidence remains authoritative while daemon tool events remain operational. |
| Epistemic Label | `FACT`, `ASSUMPTION`, `PROPOSAL`, `TBD` | Labels used to prevent plausible invention from becoming project truth. |
| CoordinationRepresentation | `SCHEDULE_FIRST`, `DEPENDENCY_TRACKED`, `HYBRID` | Coordination representation separate from deliverable-local dependency tracking. |
| DomainEngineProfile | domain profile | Future platform contract, not current runtime core. |
| OperationProposal | domain operation record | Future human-gated domain operation proposal. |
| OpenPipeStress fixture | first domain example | Future fixture profile, not Chirality core. |

---

## 5. SSOW

| ScopeItemID | Status | SourceRef | ScopeItemStatement | Notes |
|---|---|---|---|---|
| SOW-001 | IN | REF-006 Section 8.1 | Provide a dialogue-centred desktop shell with persistent human–agent conversation, provenance-bearing artifact views, and Work/Agents coordination surfaces. | Existing routes and the loop-first UI remain compatibility surfaces until separately retired; shared intent is not a stored UI object. |
| SOW-002 | IN | REF-006 Section 8.1, REF-003 Section 1 | Support global working-root selection and validation. | Must reject invalid and instruction-root-contained paths. |
| SOW-003 | IN | REF-006 Section 8.1 | Render bounded working-root file tree and scope scans. | Scan limits protect responsiveness. |
| SOW-004 | IN | REF-006 Section 8.1, Section 8.7 | Support professional resizable Navigator, dialogue, coordination, artifact-focus, and activity layouts with versioned local UI state. | Layout, focus, transcript selection, anchors, and panel state are non-authoritative convenience state and migrate non-destructively. |
| SOW-005 | IN | REF-006 Section 8.2, REF-004 Section 4 | Preserve semantic agent/session routing, guarded dialogue selection, canonical aliases, and legacy matrix-route compatibility without requiring a fixed matrix in the target shell. | Legacy matrix/query behavior remains compatible; hierarchy and replay evidence retain their separate semantic owners. |
| SOW-006 | IN | REF-006 Section 8.2 | Present active dialogue/persona context and a Work/Agents Coordination Panel over explicitly recorded work, canonical session parentage, selectable recorded-session replay, and Agent 0/1/2 role entry for Codex sessions. | The selected-session replay lens is read-only and distinct from the mounted primary live dialogue. Role entry presents accepted state rather than inferring enforcement: Agent 2/TASK is labelled `role not mechanically enforced` when G-ROLE cannot mechanically prove non-delegation, and the product posture is labelled `Opt-in Preview`; missing plans, tasks, relationships, transcripts, or enforcement evidence remain explicitly absent or unknown. |
| SOW-007 | IN | REF-006 Section 8.2 | Expose presentation-neutral PIPELINE category and task-scope controls for DECOMP/PREP/TASK/AUDIT dispatch. | Unsupported options remain visible and disabled; DEL-08-03 retains dispatch semantics independently of Coordination Panel presentation. |
| SOW-008 | IN | REF-006 Section 8.7 | Expose per-turn toolkit options and preserve dialogue drafts, presets, explicit next-turn context references, artifact anchors, and panel selections as local convenience state. | Visible artifacts are not automatically model context; local state must not override runtime governance, rewrite sent-turn history, or transfer primary-session context to a selected replay. |
| SOW-009 | IN | REF-006 Section 8.3, Section 9.1 | Expose App client operations to create, list, resume, retrieve, save, and delete daemon-owned sessions. | Bound to registered project identity and normalized project root; App does not own runtime session state. |
| SOW-010 | IN | REF-006 Section 8.3, Section 8.4 | Bind App client session-creation and boot requests to registered project identity/root, persona, mode, and options while the daemon owns runtime session state. | Boot fingerprint should reflect real project/policy inputs. |
| SOW-011 | IN | REF-006 Section 8.3, Section 9.3 | Submit App client turns through stable browser/SSE proxy surfaces to the daemon, which enforces one active turn per session. | Route remains browser-compatible. |
| SOW-012 | IN | REF-006 Section 8.3, Section 7.10 | Forward App client interrupt, cancel, disconnect, and failure signals to the daemon and verify lock release plus observable terminal records. | App evidence includes resumability after failure; generic interruption and locks remain daemon-owned. |
| SOW-013 | IN | REF-006 Section 8.3 | Runtime errors must be typed, actionable, and preserve retry context. | UI maps error to title/message/next step. |
| SOW-014 | IN | REF-006 Section 8.3, Section 8.12 | Submit accepted App user input to the daemon and verify that operational acceptance is recorded before SDK/model execution starts. | Checkout-contained approval or acceptance evidence remains project authoritative; not every daemon event is thereby promoted to project truth. |
| SOW-015 | IN | REF-006 Section 8.3, Section 8.12 | Reflect daemon terminal success, failure, cancellation, or interruption outcomes in App client surfaces and verify durable operational records. | Every accepted turn must have one observable daemon terminal outcome. |
| SOW-016 | IN | REF-006 Section 8.4, REF-003 Section 13 | Keep App option inputs and presentation compatible with deterministic Root-runtime fallback chains and warnings for unknown keys. | Generic model, tool, max-turn, mode, and persona fallback semantics remain Root-owned. |
| SOW-017 | IN | REF-006 Section 8.4, REF-003 Section 13 | Resolve personas and aliases to instruction-root `AGENT_*.md` files and compose real prompt context. | Replaces stub persona prompt. |
| SOW-018 | IN | REF-006 Section 8.4, Section 13 | Provide App packaged-daemon/client integration and conformance for Root-runtime provider-adapter paths: Claude Agent SDK / Anthropic as first/default/supervisor and the D-APP-72-bounded Pi/oMLX child path. | Generic adapter ownership and unresolved generic-versus-private component classification remain outside App scope; the Pi path stays opt-in and gated. |
| SOW-019 | IN | REF-006 Section 8.5, REF-003 Section 16 | Provide credential entry/status to packaged Electron daemon mode and verify the existing App identity and encrypted `safeStorage` credential boundary remain single-owner without project writes. | The daemon exclusively owns runtime credentials; normal Desktop is a client and key material is never project truth. |
| SOW-020 | IN | REF-006 Section 8.5, REF-003 Section 16 | Conform App packaged-daemon/client networking to the ruled Anthropic and authenticated `127.0.0.1` oMLX endpoint boundary. | Root owns generic provider/network semantics; all other provider expansion requires a bounded future tranche. |
| SOW-021 | IN | REF-006 Section 8.5 | Map daemon/provider/SDK errors into typed App presentation and verify required redaction. | Root retains generic runtime security and error semantics; App evidence covers auth, rate limit, timeout, API, network, and policy presentation. |
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
| SOW-037 | IN | REF-006 Section 8.12, Section 9.4 | Conform the Chirality App client to Root-owned `AgentEnginePort` / `RuntimeEngineContract` semantics and preserve the ruled compatibility re-export plus App-facing API/UI compatibility. | Provider/SDK APIs do not redefine generic runtime or App client semantics. |
| SOW-038 | IN | REF-006 Section 8.12, REF-003 Section 10 | Keep `/api/harness/turn` as a thin daemon-client transport adapter that consumes the Root-owned turn-lifecycle contract. | Route validates, proxies, and streams; the daemon owns runtime behavior. |
| SOW-039 | IN | REF-006 Section 8.12, REF-003 Section 9 | Consume versioned daemon `HarnessEvent`s and verify ordered append-only operational persistence for App replay and diagnostics. | Generic event schema/writer semantics remain Root-owned; trailing-line tolerance is App conformance evidence. |
| SOW-040 | IN | REF-006 Section 8.12, REF-003 Section 11 | Keep browser `UIEvent`s separate from persisted `HarnessEvent`s. | Stable compact UI contract. |
| SOW-041 | IN | REF-006 Section 8.12, REF-003 Section 9 | Redact App-originated provider/client presentation and verify Root-runtime redaction of operational logs, event data, and tool artifacts. | P0 privacy conformance boundary; App does not own the generic run logger. |
| SOW-042 | IN | REF-006 Section 8.12, REF-003 Section 8-9 | Replay runtime events into transcript views and diagnostics. | Valid prior JSONL survives malformed tail. |
| SOW-043 | IN | REF-006 Section 8.12, REF-003 Section 8 | Keep legacy session records readable during App-side migration to folder/daemon-compatible layout, with backup-before-write and rollback preserving source bytes and A13 `legacySource` evidence. | Existing `.json` sessions remain usable; Root owns generic session/storage schema and consent, account-invalidation, resume, and fresh-session semantics. |
| SOW-044 | IN | REF-006 Section 8.12, Section 9.4 | Map daemon/provider outputs deterministically into App `UIEvent`s and verify conformance to Root-owned `HarnessEvent` semantics without redefining the generic adapter contract. | Pi and Claude client mappings remain independently conformance-tested; component ownership classification remains separately governed. |
| SOW-045 | IN | REF-006 Section 8.12, REF-003 Section 12 | Supply App/project settings inputs and verify Root-runtime adapter isolation: Claude uses `settingSources: []`; Pi receives no ambient `.pi`, `~/.pi`, `.agents`, settings, skills, prompts, extensions, or credentials. | Ambient user/local settings remain forbidden; the daemon owns runtime credentials and generic adapter settings semantics. |
| SOW-046 | IN | REF-006 Section 8.12, Section 10.3 | Maintain App client linkage to daemon session IDs, SDK transcript/store references, and resume metadata without making the SDK transcript canonical. | Transcript placement remains unresolved in `OI-002`; daemon session state stays operational and checkout evidence stays authoritative. |
| SOW-047 | IN | REF-006 Section 8.13 | Submit App/project requested tool names only for registered SDK built-ins or project-specific Chirality MCP tools and verify daemon-side resolution. | The daemon owns generic tool execution; unknown names error. |
| SOW-048 | IN | REF-006 Section 8.13, REF-003 Section 14 | Chirality MCP tools declare schema, permissions, execution, and summarization behavior. | In-process tools pass same policy as SDK built-ins. |
| SOW-049 | IN | REF-006 Section 8.13 | Supply deterministic App/project policy inputs for the daemon-owned tool surface and verify the visible client result for session, persona, mode, and policy. | Tool availability is not model exposure and App does not own generic construction or execution. |
| SOW-050 | IN | REF-006 Section 8.13, REF-005 Section 4 | Enable read tools before write/edit/bash capability. | Initial tool sequence is read-only. |
| SOW-051 | IN | REF-006 Section 8.13 | Consume the daemon-owned SDK model/tool loop and map its operational events into App client surfaces. | App does not own a custom generic loop; fallback changes route through Root. |
| SOW-052 | IN | REF-006 Section 8.13 | Supply App/project max-turn policy inputs and verify daemon-side runaway-loop guards. | Terminal max-turn operational errors persist in the daemon and remain observable to App. |
| SOW-053 | IN | REF-006 Section 8.13 | Verify deterministic App replay from daemon operational events even when daemon tool activity is concurrent. | App does not own generic event scheduling or persistence. |
| SOW-054 | IN | REF-006 Section 8.14, REF-004 Section 8 | Permission decisions are structured and persisted. | `allow`, `deny`, or application-level `ask`. |
| SOW-055 | IN | REF-006 Section 8.14, REF-002 Section 1.6 | Supply App/project permission modes and explicit hard-deny inputs and verify daemon enforcement through provider/SDK posture and capability policy. | Tool availability alone is not a restriction boundary; generic permission execution remains Root-owned. |
| SOW-056 | IN | REF-006 Section 8.14 | Consume daemon operational `tool.permission` events while preserving checkout-contained App/project approval and acceptance evidence. | Operational events include source, reason, and SDK metadata but do not replace project authority. |
| SOW-057 | IN | REF-006 Section 8.14, REF-003 Section 15 | Supply project-specific hooks and policy inputs and verify daemon fail-closed generic hook execution for write, shell, domain, and subagent actions. | Project path, provenance, deterministic-act, and human-gate authority remains checkout-contained. |
| SOW-058 | IN | REF-006 Section 8.14 | Mediate interactive human/project approvals through App `canUseTool` UI and return the decision to the daemon. | Persist authoritative checkout approval evidence before the daemon allow/deny response; daemon tool events remain operational. |
| SOW-059 | IN | REF-006 Section 8.15, REF-003 Section 9 | Consume and preview daemon-budgeted tool outputs and preserve separately accepted project artifacts without flooding chat or model context. | Generic operational result storage remains daemon-owned. |
| SOW-060 | IN | REF-006 Section 8.15 | Safe write/edit tools enforce containment, symlink rejection, instruction-root block, and edit preconditions. | Applies after write phase lands. |
| SOW-061 | IN | REF-006 Section 8.15 | Observe daemon SDK compaction boundaries and preserve App replay/conformance evidence. | The full operational event log remains daemon-managed; accepted checkout evidence remains separately authoritative. |
| SOW-062 | IN | REF-006 Section 8.15, REF-002 Section 1.6 | Keep Bash denied by App/project policy by default and verify daemon timeout, capture, interruption, and operational audit behavior when separately authorized. | No default shell exposure; human authorization and project-specific deterministic-act authority remain checkout-contained. |
| SOW-063 | IN | REF-006 Section 8.15, REF-004 Section 10 | Supply governed subagent instructions, sealed context, project permissions, and approval references to daemon-owned operational delegation and preserve checkout-contained AgentRuns. | The daemon owns delegation execution and restricted runtime tools/cwd; project authority is not transferred. |
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
| SOW-079 | IN | SCA-APP-008 Carrier Map WP-02; App v3 pathway seating MAPPING S-1 | Observe exact Root-owned App Server supply, protocol, configuration, and role behavior at the App boundary and produce adoption evidence without owning supply, download, or generic runtime semantics. | Root DEL-02-08 and G1 govern exact supply/download authority and reliance; this App probe does not activate implementation. |
| SOW-080 | IN | SCA-APP-008 Carrier Map WP-03; App v3 pathway seating MAPPING S-2 | Provide an App-side two-job installer transaction through Root-owned runtime-control IPC, including staged launchd-job migration, effective-state inspection, rollback, upgrade/uninstall, and cleanup evidence. | Root owns supervisor, runtime-control, and storage semantics through DEL-02-07/DEL-02-11; F-APP-2 and D-APP-97 remain active, and this seating authorizes no implementation or release act. |

---

## 6. Objectives

| ObjectiveID | Statement | MappedScopeItems | Notes |
|---|---|---|---|
| OBJ-001 | Provide a governed local desktop harness centred on actual human–agent dialogue, with explicit turn context, provenance-bearing inline and focused artifacts, recorded Work/Agents coordination, and evidence-derived supervision. | SOW-001-SOW-008, SOW-023 | Dialogue, artifact collaboration, and operator workflow objective; shared intent remains emergent rather than a stored UI authority object. |
| OBJ-002 | Demonstrate App-client conformance to Root-owned runtime contracts and preserve thin route/proxy boundaries before provider/SDK adapter behavior becomes production default. | SOW-009-SOW-018, SOW-037-SOW-040, SOW-079 | App runtime-client architecture objective. |
| OBJ-003 | Make App-consumed accepted turns, provider/SDK messages, terminal outcomes, tool activity, and replay auditable while distinguishing daemon operational records from checkout-contained project evidence. | SOW-014-SOW-015, SOW-039-SOW-046, SOW-059, SOW-061 | App audit-consumption and session-evidence objective. |
| OBJ-004 | Provide App integration, packaging, and conformance for the Root-owned provider-adapter runtime, with Claude Agent SDK / Anthropic as the first governed adapter and with deterministic project inputs, prompt composition, settings isolation, and presentation redaction. | SOW-016-SOW-021, SOW-044-SOW-046, SOW-051, SOW-079 | App provider/SDK client-conformance objective; generic adapter and App Server supply semantics remain Root-owned. |
| OBJ-005 | Supply project capability policy, deterministic acts, explicit hard-deny inputs, human-mediated approvals, and App conformance evidence while the daemon owns generic tool mediation and execution. | SOW-047-SOW-064, SOW-076 | App/project tool-authority and conformance objective. |
| OBJ-006 | Preserve filesystem project truth through working-root containment, SPEC layouts, lifecycle files, dependencies, snapshots, and change discipline. | SOW-024-SOW-034, SOW-075, SOW-077 | Filesystem governance objective. |
| OBJ-007 | Maintain agent-suite integrity, project delegation authority, sealed briefs, and checkout AgentRuns while consuming daemon-owned operational delegation without expanding authority. | SOW-005-SOW-006, SOW-017, SOW-030-SOW-031, SOW-063 | App/project agent-governance objective. |
| OBJ-008 | Keep validation, packaging, release, network, key, and instruction-root checks explicit and repeatable. | SOW-019-SOW-022, SOW-035-SOW-036, SOW-072-SOW-073, SOW-078, SOW-080 | Release readiness objective. |
| OBJ-009 | Preserve professional boundary, product identity, and reliance-boundary ownership in docs, UI, runtime, and release behavior. | SOW-065, SOW-071, SOW-074, SOW-076-SOW-077 | Governance identity objective. |
| OBJ-010 | Preserve future domain-engine compatibility without turning domain solvers into Chirality core. | SOW-066-SOW-071 | Future platform objective. |

---

## 7. Packages

| PackageID | Name | ScopeDescription | InclusionCriteria | Exclusions |
|---|---|---|---|---|
| PKG-01 | Product Governance and Reliance Boundaries | Product intent, invariants, professional boundary, reliance-boundary ownership, out-of-scope discipline. | Governance docs, acceptance checks, product identity, scope boundaries. | Runtime implementation details except as required for boundary enforcement. |
| PKG-02 | Woven Dialogue Shell, Navigation, and Operator State | Dialogue-centred shell, Woven Dialogue artifact presentation, Navigator, Work/Agents Coordination Panel, activity shelf, re-hosted Workbench/Pipeline/toolkit/settings, compatibility surfaces, and non-authoritative local UI state. | Human–agent dialogue, artifact collaboration, coordination presentation, and operator workflow behavior. | Runtime engine internals, canonical session/evidence ownership, arbitrary orchestration graphs, automatic intent inference, and project-control-plane authority. |
| PKG-03 | Runtime Engine Contract and Turn Lifecycle | App-side runtime-client integration for the Root-owned turn lifecycle, including thin Desktop/HTTP proxy behavior, session request binding, route/SSE compatibility, interrupt/cancel presentation, and conformance evidence. | App daemon client/proxy, contract compatibility, API/SSE transport, affected-client evidence. | Generic runtime contracts, daemon/session/lock/interruption/persistence semantics, and provider-specific message translation details. |
| PKG-04 | SDK Adapter, Prompt, Provider, and Settings | App integration, project-input composition, packaged-daemon credential-boundary participation, provider-adapter compatibility, settings isolation, and conformance evidence. | First-adapter probe; App client/packaging integration; prompt/project inputs; provider and settings conformance. | Generic adapters, engines, credentials, residency, and unresolved generic-versus-private component classification. |
| PKG-05 | Session Audit, Replay, and Tool Result Records | App session/event consumption, legacy migration participation, replay, App-side redaction, accepted project artifacts, and conformance evidence. | Client compatibility, replay/projection, affected-client diagnostics, and checkout acceptance evidence. | Generic session/event/tool-result persistence and daemon operational-state ownership. |
| PKG-06 | Permissioned Tools, MCP, and Hooks | App/project permission policy, explicit hard-deny inputs, human approvals, project-specific deterministic tools/hooks, client presentation, and daemon conformance. | Project authority and policy inputs; App approval UI; project-specific tool acts; affected-client evidence. | Generic runtime tool mediation/execution, interruption, operational event persistence, and domain-engine operation semantics. |
| PKG-07 | Filesystem Execution, Lifecycle, and Dependencies | Working-root truth, execution-root scaffolding, deliverable files, `_STATUS.md`, `Dependencies.csv`, snapshots. | Project file mechanics and deterministic filesystem APIs. | UI presentation except scope scan results. |
| PKG-08 | Agent Suite, Pipeline Dispatch, and Subagent Governance | Agent instruction conformance, matrix/pipeline dispatch, project delegation authority, daemon-client dispatch, sealed child context, and checkout-contained AgentRuns. | Agent OS authority, instructions, approval references, client dispatch, and project evidence. | Generic provider/SDK mechanics and daemon-owned operational delegation execution/state. |
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

### PKG-02 Woven Dialogue Shell, Navigation, and Operator State

| DeliverableID | Name | ResponsibleParty | Type | Description | AnticipatedArtifacts | CoversScopeItems | SupportsObjectives | ContextEnvelope | ContextEnvelopeNotes |
|---|---|---|---|---|---|---|---|---|---|
| DEL-02-01 | Woven Dialogue Shell and Compatibility Navigation | TBD | UX_UI_SLICE | Compose the persistent primary human–agent transcript and composer, provenance-bearing inline/focused artifact views, Navigator, Work/Agents Coordination Panel, Activity Shelf, and compatibility navigation without creating a second evidence store. | Dialogue shell; inline artifact/focus views; Work/Agents panel; activity shelf; route/query and compatibility tests | SOW-001, SOW-005 | OBJ-001 | M | Shell integration owns presentation only; work, hierarchy, transcript, and artifact facts remain governed by their existing semantic owners. |
| DEL-02-02 | Work/Agents Coordination, Workbench, and Pipeline UX | TBD | UX_UI_SLICE | Re-host Workbench and Pipeline around central dialogue and present explicitly recorded plans/tasks, agent/session selections, and Agent 0/1/2 role entry for Codex sessions with source, authority class, responsible reference, currency, and evidence while preserving disabled states and deep-link intent. | Workbench/Pipeline views; Work/Agents coordination presentation; role-entry controls; exact `role not mechanically enforced` and `Opt-in Preview` posture labels; provenance labels; stale/empty-state, label, and query compatibility tests | SOW-006, SOW-007 | OBJ-001, OBJ-007 | M | DEL-08-02 retains routing, DEL-08-03 retains dispatch, DEL-08-04 retains role/delegation semantics, DEL-08-05 retains child records, and DEL-05-04 retains replay/projection semantics; this deliverable only composes accepted presentation and does not infer enforcement. |
| DEL-02-03 | Working Root File Tree and Scope Scan UI | TBD | UX_UI_SLICE | Provide working-root selector integration, bounded file tree display, deliverable summaries, and scan-state feedback. | File tree panel; deliverable summary widgets; scope scan integration | SOW-002, SOW-003 | OBJ-001, OBJ-006 | M | UI consumes workspace APIs but remains presentation-focused. |
| DEL-02-04 | Dialogue Toolkit, Context, and Local UI State | TBD | UX_UI_SLICE | Expose runtime options and preserve versioned layout, drafts, explicit next-turn context references, artifact anchors, selected replay references, panel state, and local presets as non-authoritative convenience state with rollback-safe migration. | Toolkit controls; workspace-state schema; resize/focus/anchor behavior; context-reference, draft/preset, and migration guards | SOW-004, SOW-008, SOW-016 | OBJ-001, OBJ-004 | S | Convenience state stores references and presentation only; it never stores authoritative workflow, hierarchy, permission, or acceptance conclusions. |
| DEL-02-05 | API Key UI and Runtime Feedback | TBD | UX_UI_SLICE | Provide API key entry/status UI, secure-storage feedback, selected-working-root attachment controls, typed runtime errors, and retry-preserving failure states; serve as the explicit App account/consent UX carrier by consuming `HostedEngineConsentPort`, explaining per-root login and root-private app-owned `CODEX_HOME`, presenting login/logout/account and consent/revocation state, distinguishing `missing`, `storageUnavailable`, `decryptFailed`, and `available`, and offering the three per-root command-network postures: no command network by default, ask per destination with host/protocol context and the queued-request caveat plus explicit-user-only `acceptForSession`, or labelled command network on through `network_access = true`. Agent 0/1/2 role entry remains available for Codex sessions; Agent 2/TASK is labelled `role not mechanically enforced` when G-ROLE fails, and the product posture is labelled `Opt-in Preview`. | API key and account settings panel; `HostedEngineConsentPort` UI adapter; per-root login and command-network consent controls; attachment picker and preview chips; typed storage/runtime error display; consent/revocation and retry-state tests | SOW-013, SOW-019, SOW-023 | OBJ-001, OBJ-008 | S | Explicit App account/consent UX carrier; Root retains account/consent semantics. No ambient `~/.codex` read or project-truth secret persistence. DEL-09-06 retains server-side attachment, network, key, credential-IPC, and renderer security validation. Live claims remain gated by the accepted Root/App account/consent contract, G3, G-CSP, and G4. |

### PKG-03 Runtime Engine Contract and Turn Lifecycle

| DeliverableID | Name | ResponsibleParty | Type | Description | AnticipatedArtifacts | CoversScopeItems | SupportsObjectives | ContextEnvelope | ContextEnvelopeNotes |
|---|---|---|---|---|---|---|---|---|---|
| DEL-03-01 | AgentEnginePort and Engine Conformance Suite | TBD | API_CONTRACT | Verify the App client against Root-owned runtime contracts, preserve the compatibility re-export and App-facing API/UI compatibility, and produce conformance evidence without redefining generic runtime semantics. | `@chirality/harness-contract` compatibility re-export; App client conformance tests; API/UI compatibility evidence | SOW-037 | OBJ-002 | M | App client contract-compatibility and conformance surface. |
| DEL-03-02 | Thin TurnEngine and Session Locking | TBD | BACKEND_FEATURE_SLICE | Keep App `/api/harness/*` and Desktop surfaces as daemon clients, bind project/persona/mode/options requests, and verify daemon-owned session lifecycle and one-active-turn behavior. | Daemon-client turn proxy; App session integration tests; daemon locking/lifecycle conformance evidence | SOW-009, SOW-010, SOW-011, SOW-038 | OBJ-002 | M | App backend-integration slice; generic TurnEngine and lock ownership remain Root-owned. |
| DEL-03-03 | Harness API and SSE Compatibility Adapter | TBD | API_CONTRACT | Keep `/api/harness/*` shapes and browser SSE event names stable while runtime policy moves behind services. | Route adapter tests; SSE compatibility fixtures; UI event contract docs | SOW-011, SOW-040 | OBJ-001, OBJ-002 | S | Focused compatibility slice. |
| DEL-03-04 | Interrupt, Cancel, and Terminal Outcome Handling | TBD | BACKEND_FEATURE_SLICE | Forward App client interrupts, cancellations, disconnects, and failures and verify that daemon-owned cleanup and terminal persistence preserve client-visible behavior. | Client interrupt/cancel forwarding tests; daemon cleanup conformance evidence; terminal-event compatibility fixtures | SOW-012, SOW-015 | OBJ-002, OBJ-003 | M | App client lifecycle-integration slice with explicit daemon ownership. |

### PKG-04 SDK Adapter, Prompt, Provider, and Settings

| DeliverableID | Name | ResponsibleParty | Type | Description | AnticipatedArtifacts | CoversScopeItems | SupportsObjectives | ContextEnvelope | ContextEnvelopeNotes |
|---|---|---|---|---|---|---|---|---|---|
| DEL-04-01 | First-Adapter Probe and Version-Pinned Adoption Decision | TBD | REQ_SLICE | Confirm App packaged-daemon/client compatibility with the first Root-runtime adapter, including version, messages, policy inputs, hooks, project MCP acts, session linkage, interruption, packaging, conformance, and unresolved component-classification risks; separately observe exact Root-owned App Server supply, protocol, configuration, and role behavior at the App boundary. | App first-adapter client probe; version decision; conformance criteria; App Server supply/protocol/configuration/role observation and adoption evidence; component-classification open items; residual-risk notes | SOW-018, SOW-044, SOW-046, SOW-079 | OBJ-002, OBJ-004 | M | App client/probe slice; no App Server supply/download ownership, generic adapter ownership, implementation activation, or new tool exposure. Root DEL-02-08 and G1 govern exact supply and reliance. |
| DEL-04-02 | SdkOptionsBuilder and Settings Isolation | TBD | BACKEND_FEATURE_SLICE | Supply deterministic App/project option inputs and verify Root-runtime adapter isolation for session, persona, mode, requested tools, hooks, project MCP acts, subagents, resume, and settings policy. | App option-input adapter; settings-isolation conformance tests; visible tool metadata | SOW-016, SOW-045, SOW-047, SOW-052, SOW-076 | OBJ-004, OBJ-005 | M | App configuration/conformance slice; generic option mapping and credentials remain Root-owned. SOW-076 is a boundary-only trace: ambient settings and shipped bypass remain OUT. |
| DEL-04-03 | SdkMessageMapper and Provider-Neutral Translation | TBD | BACKEND_FEATURE_SLICE | Translate daemon/provider outputs into stable App `UIEvent`s and verify conformance to Root-owned provider-neutral `HarnessEvent` semantics without redefining generic adapter contracts. | App UI-event mapper; conformance fixtures; provider-shape leakage tests | SOW-040, SOW-044, SOW-051 | OBJ-002, OBJ-004 | M | App client mapping surface; generic adapter/event semantics remain Root-owned. |
| DEL-04-04 | PersonaComposer from Instruction Root | TBD | BACKEND_FEATURE_SLICE | Replace stub prompt behavior with instruction-root governance, active persona, working-root policy, mode, and tool-surface composition. | `persona-composer.ts`; persona content hash tests; boot fingerprint updates | SOW-017, SOW-030 | OBJ-004, OBJ-007 | M | Prompt composition slice with bounded artifacts. |
| DEL-04-05 | Anthropic Provider Key, Base URL, and Network Bridge | TBD | SECURITY_CONTROL | Preserve App credential entry/status and packaged-daemon `safeStorage` boundary participation, verify ruled provider/network behavior and redacted client handoff, and prevent unauthorized expansion without creating a second credential owner. | App credential UI/client bridge; packaged-daemon safeStorage conformance; network and provider-expansion tests; redaction fixtures | SOW-019, SOW-020, SOW-021 | OBJ-004, OBJ-008 | M | App security/conformance slice; the daemon exclusively owns runtime credentials and generic network semantics. |

### PKG-05 Session Audit, Replay, and Tool Result Records

| DeliverableID | Name | ResponsibleParty | Type | Description | AnticipatedArtifacts | CoversScopeItems | SupportsObjectives | ContextEnvelope | ContextEnvelopeNotes |
|---|---|---|---|---|---|---|---|---|---|
| DEL-05-01 | Canonical Session Folder and Legacy Session Migration | TBD | DATA_MODEL_CHANGE | Maintain App-client compatibility for daemon-centralized sessions, including lazy non-destructive access to and App-side migration of legacy project-local session records with backup-before-write and rollback preserving source bytes and A13 `legacySource` evidence while preserving list, resume, and delete behavior. | App session-client compatibility layer; legacy-read/migration fixtures; backup-before-write and rollback fixtures; source-byte and `legacySource` preservation evidence; daemon-session conformance evidence | SOW-009, SOW-043, SOW-046 | OBJ-003 | M | App compatibility and migration-participation slice; daemon sessions and generic storage schema remain Root-owned. Consent, account-invalidation, resume, and fresh-session semantics are excluded. |
| DEL-05-02 | HarnessEvent Schema and Append-Only JSONL | TBD | DATA_MODEL_CHANGE | Consume Root-owned daemon `HarnessEvent` records for App audit/replay surfaces and verify accepted-turn and terminal-event persistence without owning the generic event schema or writer. | App runtime-event compatibility fixtures; accepted-turn and terminal persistence conformance tests; daemon evidence samples | SOW-014, SOW-015, SOW-039 | OBJ-003 | M | App event-consumption and conformance slice; generic persistence remains Root-owned. |
| DEL-05-03 | Redacted RunLogger and Secret Hygiene | TBD | SECURITY_CONTROL | Redact App-originated provider/client presentation and verify that Root-runtime operational records exclude credentials and secrets. | App redaction helper; daemon redaction conformance tests; provider/client error fixtures | SOW-021, SOW-041 | OBJ-003, OBJ-008 | S | App source/presentation security and conformance; no generic run-logger ownership. |
| DEL-05-04 | Runtime Replay, Dialogue, and Agent Transcript Projection | TBD | BACKEND_FEATURE_SLICE | Reconstruct accepted turns, recorded-session transcript/replay, tool summaries, terminal states, attribution, and evidence-conditioned Agent projections from canonical Chirality records without replacing the primary dialogue or evidence store. | Replay parser; transcript reconstruction; bounded/stale projection; selected-session read-only replay lens; exact-parentage and malformed-tail tests | SOW-006, SOW-042, SOW-046 | OBJ-001, OBJ-003 | M | Projection is rebuildable and provenance-labelled; live versus replayed state and primary versus observational interaction authority remain explicit. |
| DEL-05-05 | ToolResultStore and Session Artifacts | TBD | BACKEND_FEATURE_SLICE | Consume and preview daemon-managed medium/large tool outputs, preserve separately accepted project artifacts, and verify output budgets without flooding chat or model context. | App artifact preview/client; accepted-project-artifact linkage; output-budget conformance fixtures | SOW-053, SOW-059 | OBJ-003, OBJ-005 | M | App consumption/evidence slice; generic operational result storage remains daemon-owned. |

### PKG-06 Permissioned Tools, MCP, and Hooks

| DeliverableID | Name | ResponsibleParty | Type | Description | AnticipatedArtifacts | CoversScopeItems | SupportsObjectives | ContextEnvelope | ContextEnvelopeNotes |
|---|---|---|---|---|---|---|---|---|---|
| DEL-06-01 | ChiralityPermissionOverlay and Mode Mapping | TBD | SECURITY_CONTROL | Supply App/project permission policy, explicit deny inputs, and human decisions to daemon tool execution; preserve checkout approval evidence and verify operational permission events and `canUseTool` mediation. | App permission-policy bridge; checkout decision records; daemon event conformance; readOnly/dontAsk/ask and hard-deny tests | SOW-054, SOW-055, SOW-056, SOW-058 | OBJ-005 | M | App/project authority and conformance slice; generic tool execution remains daemon-owned. |
| DEL-06-02 | SDK Read Tool Surface and Tool Validation | TBD | BACKEND_FEATURE_SLICE | Maintain deterministic App/project tool catalog and requested tool names, reject unknown or colliding client tool names, and verify daemon read-tool exposure before writes/bash. | App tool catalog/request resolver; catalog metadata; unknown-tool and name-collision tests; daemon visible-surface conformance fixtures | SOW-047, SOW-049, SOW-050, SOW-064 | OBJ-005 | M | Catalog, validation, and collision-prevention share of SOW-064; no MCP wrapper implementation or remote MCP, plugin, or marketplace scope. |
| DEL-06-03 | Initial Chirality MCP Read Tools | TBD | BACKEND_FEATURE_SLICE | Expose in-process deterministic MCP wrappers for status read, dependency read, scope scan, and scaffold preview/dry-run, and document their in-process extension boundary without opening remote MCP, plugins, or marketplace scope. | `mcp__chirality__*` definitions; wrapper metadata; in-process extension-boundary notes; MCP tool tests | SOW-048, SOW-050, SOW-064 | OBJ-005, OBJ-006 | M | In-process wrapper and extension-boundary share of SOW-064; catalog validation and collision prevention remain DEL-06-02. |
| DEL-06-04 | Write/Edit Surface and Path Hooks | TBD | SECURITY_CONTROL | Gate write/edit execution with project-root containment, instruction-root block, symlink rejection, exact edit preconditions, and provenance hooks. | PreToolUse hooks; write/edit tests; provenance metadata; path policy fixtures | SOW-027, SOW-057, SOW-060 | OBJ-005, OBJ-006 | L | Spans filesystem policy and SDK tool use but remains one tool-governance domain. |
| DEL-06-05 | Bash Governance and Timeout Policy | TBD | SECURITY_CONTROL | Keep Bash denied by App/project policy by default, require explicit human authorization, and verify daemon timeout, capture, output, interruption, and operational audit behavior before use. | App Bash policy/human-gate tests; daemon timeout/capture/interruption conformance; output evidence fixtures | SOW-062 | OBJ-005 | M | App authority/conformance guardrail; generic Bash execution remains daemon-owned. |
| DEL-06-06 | Hook Lifecycle and Compaction Mirror | TBD | BACKEND_FEATURE_SLICE | Supply project-specific hook policy and map daemon hook/compaction operational events into App evidence while verifying fail-closed behavior. | App hook-policy bridge; hook-event mapper; compaction and terminal conformance fixtures | SOW-057, SOW-061 | OBJ-003, OBJ-005 | M | App project-hook and conformance slice; generic hook execution remains Root-owned. |

### PKG-07 Filesystem Execution, Lifecycle, and Dependencies

| DeliverableID | Name | ResponsibleParty | Type | Description | AnticipatedArtifacts | CoversScopeItems | SupportsObjectives | ContextEnvelope | ContextEnvelopeNotes |
|---|---|---|---|---|---|---|---|---|---|
| DEL-07-01 | Working Root Validation and Instruction Root Protection | TBD | SECURITY_CONTROL | Enforce working-root validity, root separation, path containment, and instruction-root write protection. | Root validation tests; path policy helpers; instruction-root protection fixtures | SOW-002, SOW-027, SOW-075 | OBJ-006, OBJ-008 | M | Filesystem policy slice with security acceptance. |
| DEL-07-02 | Execution Root Scaffolding from Decomposition | TBD | BACKEND_FEATURE_SLICE | Scaffold SPEC-conformant execution roots from decomposition markdown idempotently and recoverably. | Scaffold parser; `INIT.md`; `_COORDINATION.md`; package/deliverable folders; idempotence tests | SOW-024, SOW-025 | OBJ-006 | M | Existing service domain with multiple file outputs. |
| DEL-07-03 | Deliverable Metadata and Document Kit Contracts | TBD | BACKEND_FEATURE_SLICE | Scan and validate deliverable metadata files, canonical memory, semantic placeholders, and document kit buckets. | Metadata scanners; document kit detection; `_MEMORY.md` rejection tests | SOW-026 | OBJ-006 | M | One deliverable-folder contract slice. |
| DEL-07-04 | Status Transition API and MCP Tool | TBD | BACKEND_FEATURE_SLICE | Parse `_STATUS.md` and enforce forward-only actor-authorized transitions with approval SHA for human gates. | Status parser; transition API/tool; approval SHA tests | SOW-028 | OBJ-006 | M | Lifecycle contract slice with known state machine. |
| DEL-07-05 | Dependencies.csv v3.1 Reader, Writer, and Linter | TBD | BACKEND_FEATURE_SLICE | Read, validate, and write dependency registers while preserving schema, provenance, row lifecycle, and warnings. | Dependency parser/writer; linter tests; provenance fixtures | SOW-029 | OBJ-006 | M | Dependency contract slice. |
| DEL-07-06 | Reference Hash and Snapshot Conventions | TBD | DOC_UPDATE | Preserve deterministic tools/scripts, reference hash behavior, immutable snapshots, and SHA approval conventions without reactivating retired scope. | Snapshot/runbook notes; hash bypass convention; CHANGE/SHA checklist | SOW-032, SOW-033, SOW-034, SOW-077 | OBJ-006, OBJ-009 | S | Focused continuity and convention deliverable. SOW-077 is a boundary-only trace: retired PKG-08 scope remains OUT. |

### PKG-08 Agent Suite, Pipeline Dispatch, and Subagent Governance

| DeliverableID | Name | ResponsibleParty | Type | Description | AnticipatedArtifacts | CoversScopeItems | SupportsObjectives | ContextEnvelope | ContextEnvelopeNotes |
|---|---|---|---|---|---|---|---|---|---|
| DEL-08-01 | Instruction Root Packaging and Agent Conformance | TBD | TEST_SUITE | Verify required instruction-root assets, agent metadata, write scopes, naming, and section markers. | Agent conformance validator; integrity fixtures; source-completeness checklist | SOW-030, SOW-031, SOW-073 | OBJ-007, OBJ-008 | M | Governance assets and checks; no runtime capability expansion. |
| DEL-08-02 | Persona Alias, Agent/Session Routing, and Legacy Matrix Compatibility Contract | TBD | UX_UI_SLICE | Keep UI aliases, canonical agent names, persona resolution, guarded dialogue/session selection, route/query mappings, and legacy matrix behavior consistent. | Alias resolver tests; guarded session-selection tests; route/query fixtures; legacy matrix compatibility and unavailable-persona tests | SOW-005, SOW-006, SOW-017 | OBJ-001, OBJ-007 | S | Does not own shell presentation, work-plan authority, dispatch semantics, replay evidence, or parent-child records. |
| DEL-08-03 | Pipeline Category and Task Scope Dispatch | TBD | UX_UI_SLICE | Own presentation-neutral DECOMP/PREP/TASK/AUDIT lane semantics, category/task-scope interpretation, dynamic scope, and disabled-option rules for contextual Run consumers. | Dispatch contract tests; Pipeline selector tests; knowledge-type discovery; dynamic-scope and disabled-option handling | SOW-007, SOW-026 | OBJ-001, OBJ-007 | M | Semantic dispatch owner; DEL-02-02 owns presentation and may not infer plans/tasks from conversational prose. |
| DEL-08-04 | Type 2 Subagent Governance Bridge | TBD | BACKEND_FEATURE_SLICE | Remain the Chirality-managed delegation bridge and prospectively carry multi-child managed execution plus the root `AGENTS.md` Agent 0/1/2 graph for v3 work, while consuming delegated-harness-native descent as a distinct Root-originated class. Enforce managed hierarchy, named allowlist or declared generalist policy, sealed brief, approvals, context/cwd/tool/write boundaries, active-sibling write-overlap fail-close, cancellation/cleanup, and class-aware routing; native descent assigns no Agent 0/1/2 role. Agent 0/1/2 role entry is offered for Codex sessions, with Agent 2/TASK labelled `role not mechanically enforced` and governed evidence marked `instruction-asserted` when G-ROLE cannot mechanically prove non-delegation. | App project-authority and managed-delegation bridge; daemon-client dispatch; class-aware `subagent-governance` behavior; managed sibling-overlap checks; role/native-origin fixtures; sealed-brief, containment, approval, cancellation, and cleanup conformance tests | SOW-063 | OBJ-005, OBJ-007 | M | Project authority/client-dispatch slice; daemon owns operational managed delegation and Root owns delegated-harness-native semantics. The D-APP-74 exclusion remains historical and tranche-scoped to SCA-APP-004; this v3 carrier prospectively supersedes it without retroactive edit. D-GOV-35 is necessary but App carrier acceptance and WP-03/05 fixtures remain required. |
| DEL-08-05 | Subagent Child Run Records and Artifacts | TBD | DATA_MODEL_CHANGE | Preserve reconstructible checkout-contained records for Chirality-managed and delegated-harness-native descendants without conflating the classes: parentage, native origin/lineage, selected role-entry state, actual adapter/provider/model, instruction/brief and policy/configuration digests, approvals, status, return/output and accepted artifact paths, cancellation/cleanup, and truthful `instruction-asserted` calibration where G-ROLE cannot mechanically prove Agent 2/TASK non-delegation. | Checkout AgentRun and native-descendant evidence records; parentage/origin and daemon linkage metadata; role/config/model attribution; child output evidence paths; managed/native replay and reconstruction fixtures | SOW-063 | OBJ-003, OBJ-007 | M | Project evidence slice; daemon operational state is non-authoritative, native descent assigns no Agent 0/1/2 role, and managed sealed-brief evidence remains distinct and required. Evidence schema follows accepted class semantics. |

### PKG-09 Validation, Packaging, Security, and Release

| DeliverableID | Name | ResponsibleParty | Type | Description | AnticipatedArtifacts | CoversScopeItems | SupportsObjectives | ContextEnvelope | ContextEnvelopeNotes |
|---|---|---|---|---|---|---|---|---|---|
| DEL-09-01 | Section 8 Harness Validation Preservation | TBD | TEST_SUITE | Preserve baseline harness validation, current local checks, and stable premerge summary behavior. | Section 8 validation preservation tests; premerge summary checks | SOW-035, SOW-036 | OBJ-008 | M | Test runner preservation slice. |
| DEL-09-02 | Section 9 Runtime Validation Additions | TBD | TEST_SUITE | Add runtime validation IDs for provider-adapter conformance, first-adapter mapper, event log, settings isolation, permissions, MCP, hooks, compaction, and subagents. | Section 9 validation IDs; harness runner updates; summary schema | SOW-036, SOW-037, SOW-039, SOW-045, SOW-054, SOW-057, SOW-063 | OBJ-002, OBJ-003, OBJ-005, OBJ-007, OBJ-008 | M | Broad but unified by Section 9 runner. |
| DEL-09-03 | Unit and Integration Test Expansion | TBD | TEST_SUITE | Add focused unit/API/integration tests for TurnEngine, SSE, event replay, attachments, status, dependencies, interrupts, and denied actions. | Jest/API/integration tests; fixtures; regression cases | SOW-011, SOW-012, SOW-014, SOW-015, SOW-022, SOW-028, SOW-029 | OBJ-002, OBJ-003, OBJ-006, OBJ-008 | M | Cross-cutting tests, but bounded to named behaviors. |
| DEL-09-04 | macOS DMG Packaging and Instruction Root Integrity | TBD | CI_CD_CHANGE | Produce the macOS arm64 unsigned DMG and prove required instruction-root assets plus SDK packaging posture are valid. | `desktop:dist`; integrity summary; SDK subprocess packaging probe | SOW-030, SOW-072, SOW-073, SOW-078 | OBJ-008 | L | Broad packaging slice but bounded to one release target. SOW-078 is a boundary-only trace: Windows/Linux packaging remains OUT. |
| DEL-09-05 | CI Artifact and Release Verification Workflow | TBD | CI_CD_CHANGE | Maintain CI premerge and stable artifact verification and serve as the explicit release-operations carrier with a strict phase boundary: WP-09 may author and review the exact signing, nested-signing-order, fuses/entitlements, notarization/stapling/Gatekeeper, recovery/rollback, version-identity, custody, GitHub-prerelease, and download-backcheck runbook, but WP-11 may execute release acts only after Ryan Tufts names and rules the exact candidate at G6a. | CI workflow and stable artifact evidence; WP-09 reviewed preparation/release runbook candidate; exact-candidate identity and custody checklist; separately authorized WP-11 owner/CHANGE execution record | SOW-035, SOW-036, SOW-072 | OBJ-008 | M | WP-09 authoring/review is not a signing, notarization, publication, distribution, release-readiness, or lifecycle act. D-APP-97/F-APP-2 remain active through preparation. WP-11 execution is a later owner act requiring G6a and the exact owner artifact ruling; no automatic transition from preparation is permitted. macOS arm64 is the rc.1 target and a second target requires a post-rc.1 scope change. |
| DEL-09-06 | Network, Key, Attachment, and Renderer Security Checks | TBD | SECURITY_CONTROL | Verify renderer allowlist, API key redaction/storage, current provider endpoint policy, no unauthorized provider/network expansion, and attachment validation/retry behavior. | Security tests; network guard tests; provider-expansion guard tests; attachment resolver validation; key storage checks | SOW-019, SOW-020, SOW-022, SOW-023 | OBJ-008 | M | Security validation family. |
| DEL-09-07 | Two-Job Runtime-Control Installer Migration and Rollback | TBD | MIGRATION_SCRIPT | Provide the App-side installer transaction for two Root-owned launchd jobs through Root-owned runtime-control IPC, with staging, effective-state inspection, rollback, upgrade/uninstall, and cleanup evidence. | Two-job installer/migration script; transaction journal; effective-state inspector; rollback, upgrade, uninstall, and cleanup fixtures and evidence | SOW-080 | OBJ-008 | M | App packaging-integration transaction only; Root owns supervisor, runtime-control, and storage semantics through DEL-02-07/DEL-02-11. F-APP-2 and D-APP-97 remain active; no signing, notarization, publication, release-readiness, implementation, or release act is authorized. |

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

For scope-item assignment, this Scope Ledger is authoritative. Section 8 `CoversScopeItems` is its reverse view and must agree exactly. Reconciliation preserves every supported relation; an OUT row remains a boundary trace and does not activate implementation scope.

| ScopeItemID | InOutStatus | ScopeItemStatement | SourceRef | PackageID | DeliverableID(s) | ObjectiveID(s) | DecisionRef | OpenIssue | Notes |
|---|---|---|---|---|---|---|---|---|---|
| SOW-001 | IN | Woven Dialogue shell with persistent transcript/composer, inline and focused artifacts, Work/Agents coordination, and secondary Agent Room presentation. | REF-006 Section 8.1 | PKG-02 | DEL-02-01 | OBJ-001 | DEC-004 | FALSE | Existing routes and loop-first UI remain compatibility surfaces. |
| SOW-002 | IN | Working-root selection and validation. | REF-006 Section 8.1 | PKG-07 | DEL-07-01, DEL-02-03 | OBJ-006, OBJ-008 | DEC-004 | FALSE | DEL-07-01 retains filesystem-policy ownership; DEL-02-03 provides the UI touchpoint. |
| SOW-003 | IN | File tree and scope scans. | REF-006 Section 8.1 | PKG-02 | DEL-02-03 | OBJ-001 | DEC-004 | FALSE |  |
| SOW-004 | IN | Resizable dialogue/navigation/coordination/focus layout and non-authoritative local UI state. | REF-006 Section 8.1 | PKG-02 | DEL-02-04 | OBJ-001 | DEC-004 | FALSE | Versioned migration preserves prior state for rollback. |
| SOW-005 | IN | Semantic persona/agent/session routing, guarded dialogue selection, and legacy route/query/alias/matrix compatibility. | REF-006 Section 8.2 | PKG-02 | DEL-02-01, DEL-08-02 | OBJ-001, OBJ-007 | DEC-004 | FALSE | DEL-02-01 presents; DEL-08-02 owns aliases, routing, selection guards, and legacy compatibility. |
| SOW-006 | IN | Active dialogue/persona plus Work/Agents coordination over provenance-labelled recorded work, canonical hierarchy, selected-session replay, and Agent 0/1/2 role entry for Codex sessions with exact non-enforcement/preview posture labels. | REF-006 Section 8.2 | PKG-02 | DEL-02-02, DEL-05-04, DEL-08-02 | OBJ-001, OBJ-007 | DEC-004; DEC-024 | FALSE | Selected replay is observational and read-only; DEL-08-04 retains role/delegation semantics and DEL-08-05 remains the unchanged parent-child record owner. The UI presents accepted state and never infers enforcement. |
| SOW-007 | IN | Contextual Pipeline category/task-scope controls for DECOMP/PREP/TASK/AUDIT dispatch. | REF-006 Section 8.2 | PKG-08 | DEL-08-03, DEL-02-02 | OBJ-001, OBJ-007 | DEC-004 | FALSE | DEL-08-03 is semantic owner; DEL-02-02 is presentation consumer. |
| SOW-008 | IN | Toolkit, drafts, explicit next-turn context references, artifact anchors, and dialogue workspace state. | REF-006 Section 8.7 | PKG-02 | DEL-02-04 | OBJ-001 | DEC-004 | FALSE | Visible artifacts are not automatic context; convenience state does not transfer session authority. |
| SOW-009 | IN | App-client session CRUD through the sole daemon. | REF-006 Section 8.3 | PKG-03 | DEL-03-02, DEL-05-01 | OBJ-002, OBJ-003 | DEC-004 | FALSE |  |
| SOW-010 | IN | App-client session boot-request binding and daemon-session conformance. | REF-006 Section 8.3 | PKG-03 | DEL-03-02 | OBJ-002 | DEC-004 | FALSE |  |
| SOW-011 | IN | App-client SSE turn proxy and daemon lock conformance. | REF-006 Section 8.3 | PKG-03 | DEL-03-02, DEL-03-03, DEL-09-03 | OBJ-001, OBJ-002, OBJ-008 | DEC-004 | FALSE |  |
| SOW-012 | IN | App-client interrupt/cancel/failure forwarding and daemon cleanup conformance. | REF-006 Section 8.3 | PKG-03 | DEL-03-04, DEL-09-03 | OBJ-002, OBJ-008 | DEC-004 | FALSE |  |
| SOW-013 | IN | Typed runtime errors. | REF-006 Section 8.3 | PKG-02 | DEL-02-05 | OBJ-001 | DEC-004 | FALSE |  |
| SOW-014 | IN | App accepted-input submission and daemon pre-execution record conformance. | REF-006 Section 8.12 | PKG-05 | DEL-05-02, DEL-09-03 | OBJ-003, OBJ-008 | DEC-005 | FALSE |  |
| SOW-015 | IN | App terminal-outcome presentation and durable daemon-record conformance. | REF-006 Section 8.12 | PKG-05 | DEL-05-02, DEL-03-04, DEL-09-03 | OBJ-002, OBJ-003, OBJ-008 | DEC-005 | FALSE |  |
| SOW-016 | IN | App option compatibility with deterministic Root-runtime fallback. | REF-006 Section 8.4 | PKG-04 | DEL-04-02, DEL-02-04 | OBJ-001, OBJ-004 | DEC-005 | FALSE |  |
| SOW-017 | IN | Persona resolution and prompt composition. | REF-006 Section 8.4 | PKG-04 | DEL-04-04, DEL-08-02 | OBJ-004, OBJ-007 | DEC-005 | FALSE |  |
| SOW-018 | IN | App packaged-daemon/client compatibility with the Root-runtime first adapter. | REF-006 Section 8.4 | PKG-04 | DEL-04-01 | OBJ-004 | DEC-005 | TRUE | OI-001 first-adapter probe. |
| SOW-019 | IN | App credential UI and packaged-daemon single-owner safeStorage conformance. | REF-006 Section 8.5 | PKG-09 | DEL-09-06, DEL-04-05, DEL-02-05 | OBJ-004, OBJ-008 | DEC-004 | FALSE |  |
| SOW-020 | IN | App packaged-daemon/client conformance to ruled provider/network boundaries. | REF-006 Section 8.5 | PKG-09 | DEL-09-06, DEL-04-05 | OBJ-004, OBJ-008 | DEC-004 | FALSE | Concrete provider expansion requires bounded future tranche. |
| SOW-021 | IN | App typed provider-error presentation and Root-runtime redaction conformance. | REF-006 Section 8.5 | PKG-04 | DEL-04-05, DEL-05-03 | OBJ-003, OBJ-004 | DEC-005 | FALSE |  |
| SOW-022 | IN | Attachment resolver validation. | REF-006 Section 8.6 | PKG-09 | DEL-09-06, DEL-09-03 | OBJ-008 | DEC-004 | FALSE |  |
| SOW-023 | IN | Attachment UI and recovery. | REF-006 Section 8.6 | PKG-02 | DEL-02-05, DEL-09-06 | OBJ-001, OBJ-008 | DEC-004 | FALSE | DEL-02-05 owns selected-root picker navigation, multi-select previews, remove/clear controls, and retry-preserving UI state; DEL-09-06 retains resolver and attachment-security validation. |
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
| SOW-037 | IN | App-client conformance to Root-owned generic runtime contracts. | REF-006 Section 8.12 | PKG-03 | DEL-03-01, DEL-01-02, DEL-09-02 | OBJ-002, OBJ-009 | DEC-005 | FALSE |  |
| SOW-038 | IN | Thin daemon-client `/api/harness/turn` proxy. | REF-006 Section 8.12 | PKG-03 | DEL-03-02 | OBJ-002 | DEC-005 | FALSE |  |
| SOW-039 | IN | App consumption and conformance for append-only daemon HarnessEvent JSONL. | REF-006 Section 8.12 | PKG-05 | DEL-05-02, DEL-09-02 | OBJ-003, OBJ-008 | DEC-005 | FALSE |  |
| SOW-040 | IN | UIEvent and HarnessEvent separation. | REF-006 Section 8.12 | PKG-03 | DEL-03-03, DEL-04-03 | OBJ-002, OBJ-004 | DEC-005 | FALSE |  |
| SOW-041 | IN | App source/presentation redaction and Root-runtime redaction conformance. | REF-006 Section 8.12 | PKG-05 | DEL-05-03 | OBJ-003, OBJ-008 | DEC-005 | FALSE |  |
| SOW-042 | IN | Runtime replay. | REF-006 Section 8.12 | PKG-05 | DEL-05-04 | OBJ-003 | DEC-005 | FALSE |  |
| SOW-043 | IN | App-side legacy session migration with backup-before-write, rollback, source-byte preservation, and A13 `legacySource` evidence. | REF-006 Section 8.12 | PKG-05 | DEL-05-01 | OBJ-003 | DEC-005; DEC-024 | FALSE | Root owns generic session/storage schema and consent, account-invalidation, resume, and fresh-session semantics. |
| SOW-044 | IN | App UI-event mapping and Root-runtime event/adapter conformance. | REF-006 Section 8.12 | PKG-04 | DEL-04-01, DEL-04-03 | OBJ-002, OBJ-004 | DEC-005 | TRUE | OI-001 first-adapter probe. |
| SOW-045 | IN | App project-input supply and Root-runtime settings-isolation conformance. | REF-006 Section 8.12 | PKG-04 | DEL-04-02, DEL-09-02, DEL-01-02 | OBJ-004, OBJ-008, OBJ-009 | DEC-005 | TRUE | OI-001 first-adapter probe confirms exact SDK behavior. |
| SOW-046 | IN | App client linkage to daemon session and noncanonical SDK transcript references. | REF-006 Section 8.12 | PKG-05 | DEL-05-01, DEL-05-04, DEL-04-01 | OBJ-003, OBJ-004 | DEC-005 | TRUE | OI-002 transcript placement. |
| SOW-047 | IN | App/project tool requests and daemon resolution conformance. | REF-006 Section 8.13 | PKG-06 | DEL-06-02, DEL-04-02 | OBJ-004, OBJ-005 | DEC-005 | FALSE |  |
| SOW-048 | IN | Chirality MCP descriptors. | REF-006 Section 8.13 | PKG-06 | DEL-06-03 | OBJ-005, OBJ-006 | DEC-005 | FALSE |  |
| SOW-049 | IN | Deterministic App/project policy inputs and daemon tool-surface conformance. | REF-006 Section 8.13 | PKG-06 | DEL-06-02 | OBJ-005 | DEC-005 | FALSE |  |
| SOW-050 | IN | Read tools before writes/bash. | REF-006 Section 8.13 | PKG-06 | DEL-06-02, DEL-06-03 | OBJ-005 | DEC-005 | FALSE |  |
| SOW-051 | IN | App consumption of the daemon model/tool loop and event mapping. | REF-006 Section 8.13 | PKG-04 | DEL-04-03 | OBJ-004 | DEC-005 | FALSE |  |
| SOW-052 | IN | App/project max-turn inputs and daemon guard conformance. | REF-006 Section 8.13 | PKG-04 | DEL-04-02 | OBJ-004 | DEC-005 | FALSE |  |
| SOW-053 | IN | App replay conformance for daemon tool-event ordering. | REF-006 Section 8.13 | PKG-05 | DEL-05-05 | OBJ-003, OBJ-005 | DEC-005 | FALSE |  |
| SOW-054 | IN | Structured permission decisions. | REF-006 Section 8.14 | PKG-06 | DEL-06-01, DEL-09-02, DEL-01-02 | OBJ-005, OBJ-008, OBJ-009 | DEC-005 | FALSE |  |
| SOW-055 | IN | App/project permission-policy inputs and daemon enforcement conformance. | REF-006 Section 8.14 | PKG-06 | DEL-06-01 | OBJ-005 | DEC-005 | FALSE |  |
| SOW-056 | IN | Daemon operational permission-event consumption and checkout approval evidence. | REF-006 Section 8.14 | PKG-06 | DEL-06-01 | OBJ-005 | DEC-005 | FALSE |  |
| SOW-057 | IN | Project-specific hook inputs and daemon fail-closed hook conformance. | REF-006 Section 8.14 | PKG-06 | DEL-06-04, DEL-06-06, DEL-09-02, DEL-01-02 | OBJ-003, OBJ-005, OBJ-008, OBJ-009 | DEC-005 | FALSE |  |
| SOW-058 | IN | App/human `canUseTool` approval and daemon decision handoff. | REF-006 Section 8.14 | PKG-06 | DEL-06-01 | OBJ-005 | DEC-005 | FALSE |  |
| SOW-059 | IN | App preview of daemon tool results and accepted project-artifact linkage. | REF-006 Section 8.15 | PKG-05 | DEL-05-05 | OBJ-003, OBJ-005 | DEC-005 | FALSE |  |
| SOW-060 | IN | Safe write/edit behavior. | REF-006 Section 8.15 | PKG-06 | DEL-06-04 | OBJ-005, OBJ-006 | DEC-005 | FALSE |  |
| SOW-061 | IN | App observation of daemon compaction and replay conformance. | REF-006 Section 8.15 | PKG-06 | DEL-06-06 | OBJ-003, OBJ-005 | DEC-005 | FALSE |  |
| SOW-062 | IN | App/project Bash policy and daemon execution/interruption/audit conformance. | REF-006 Section 8.15 | PKG-06 | DEL-06-05 | OBJ-005 | DEC-005 | FALSE |  |
| SOW-063 | IN | Project delegation authority, daemon-client dispatch, and checkout AgentRuns. | REF-006 Section 8.15 | PKG-08 | DEL-08-04, DEL-08-05, DEL-09-02 | OBJ-003, OBJ-005, OBJ-007, OBJ-008 | DEC-005 | FALSE |  |
| SOW-064 | IN | MCP extension boundaries. | REF-006 Section 8.15 | PKG-06 | DEL-06-02, DEL-06-03 | OBJ-005 | DEC-005 | FALSE | DEL-06-02 owns catalog, request validation, and collision prevention; DEL-06-03 owns in-process wrappers and extension-boundary documentation. Remote MCP, plugins, and marketplace scope remain excluded by SOW-065. |
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
| SOW-079 | IN | Observe exact Root-owned App Server supply, protocol, configuration, and role behavior at the App boundary and produce adoption evidence. | SCA-APP-008 Carrier Map WP-02; App v3 pathway seating MAPPING S-1 | PKG-04 | DEL-04-01 | OBJ-002, OBJ-004 | DEC-024 | TRUE | OI-007 shared-runtime boundary; Root DEL-02-08 and G1 govern exact supply/download authority and reliance. No App implementation activation. |
| SOW-080 | IN | App-side two-job installer transaction through Root-owned runtime-control IPC, including staged launchd-job migration, effective-state inspection, rollback, upgrade/uninstall, and cleanup evidence. | SCA-APP-008 Carrier Map WP-03; App v3 pathway seating MAPPING S-2 | PKG-09 | DEL-09-07 | OBJ-008 | DEC-024 | TRUE | OI-003 packaging and OI-007 shared-runtime boundary; Root DEL-02-07/DEL-02-11 own supervisor, control, and storage semantics. F-APP-2/D-APP-97 remain active. |

---

## 10. Coverage and Telemetry

| Metric | Value |
|---|---:|
| Revision | v3.2 source-governed working surface amended by SCA-APP-009 |
| Date | 2026-09-04 |
| ScopeItemCount | 80 |
| PackageCount | 10 |
| DeliverableCount | 52 |
| ObjectiveCount | 10 |
| UnassignedScopeItems | 0 |
| ScopeItemsWithoutDeliverableMapping | 0 |
| UnmappedObjectives | 0 |
| ContextEnvelopeCounts | S=9, M=41, L=2, XL=0 |
| OpenIssuesByType | FIRST_ADAPTER_PROBE=1, SDK_TRANSCRIPT=1, PACKAGING=1, SOURCE_COMPLETENESS=1, DOMAIN_FUTURE=1, PROVIDER_EXPANSION=1, SHARED_RUNTIME=1 |
| OpenIssueAffectedScopeCounts | FIRST_ADAPTER_PROBE=3, SDK_TRANSCRIPT=1, PACKAGING=2, SOURCE_COMPLETENESS=2, DOMAIN_FUTURE=6, PROVIDER_EXPANSION=3, SHARED_RUNTIME=10 |

### Context Budget QA

| Envelope | Deliverables | QA Result |
|---|---|---|
| S | DEL-01-03, DEL-01-04, DEL-02-04, DEL-02-05, DEL-03-03, DEL-05-03, DEL-07-06, DEL-08-02, DEL-10-05 | Acceptable small slices. |
| M | All other deliverables except listed L items, including DEL-09-07 | Acceptable bounded Type 2 work. |
| L | DEL-06-04, DEL-09-04 | Accepted large-but-single-domain slices; each has context notes and should be split only if implementation review finds broad cross-domain churn. |
| XL | None | No XL deliverables accepted. |

---

## 10A. Non-PRD Control Coverage

This section is normative for v3.2 downstream review. The decomposition is not considered complete if PRD requirements are covered but DIRECTIVE intent, CONTRACT invariants, SPEC mechanics, TYPES vocabulary, PLAN sequencing, or SOFTWARE_DECOMP method rules are violated.

### 10A.1 CONTRACT Invariant Coverage

The decomposition package maintains CONTRACT invariant coverage as companion machine-truth in `contract_invariant_coverage_register.csv`. The live register contains one row for each of 81 CONTRACT invariant IDs in 48 families and maps those binding invariants to semantic-owner authority, App obligations and topology, enforcement surfaces, validation surfaces, evidence disposition, and open issues. This prevents PRD-only execution and gives REVIEW a direct way to check safety, audit, permission, lifecycle, runtime, release, and domain-boundary obligations.

Field-level authority precedence is:

| Field group | Authoritative source and limit |
|---|---|
| `InvariantID`, `InvariantFamily`, `SourcePath`, `SourceAnchor`, `ContractSourceSHA256` | CONTRACT controls invariant identity and normative source text. The register records identity and provenance; it does not amend CONTRACT. |
| `AppPackageIDs`, `AppDeliverableIDs`, `AppDecompositionBasis` | The accepted App decomposition controls App package, deliverable, objective, and scope topology. Register references must resolve; the register cannot create or alter topology. |
| `AppObligationClass`, `EnforcementSurfaces`, `ValidationSurfaces`, `OpenIssueIDs`, `CoverageStatus`, `ProvenanceStatus`, `RationaleEvidenceAnchor` | The accepted companion register controls the mapping and coverage/evidence disposition between CONTRACT invariants and App topology, bounded by its cited sources. |
| `SemanticOwnerProduct`, `OwnerAuthorityRef`, `OwnerAuthorityBasis` | The cited owner instrument controls externally owned semantics. Unresolved ownership remains explicit; an App register row cannot supersede, transfer, or silently reinterpret another product's authority. |

The register validator must reject duplicate, missing, or extra invariant IDs; invalid closed-enum values; invented or unresolved App package/deliverable IDs; unsupported semantic-owner assertions; and basis fields that do not match their declared sources.

Within this decomposition, Section 9 Scope Ledger controls scope-item assignment and Section 8 `CoversScopeItems` is its exact reverse view. No supported relation may be deleted merely to force parity, and an OUT relation remains boundary-only.

Compact invariant-family ownership:

The table below is a non-exhaustive human-readable summary. The complete 81-ID/48-family mapping is the live companion register, and this summary does not override it.

| Invariant Family | Primary Coverage | Notes |
|---|---|---|
| `K-PRD`, `K-HIER`, `K-ID`, `K-PATH`, `K-FS`, `K-GIT`, `K-NOMEM` | PKG-01, PKG-05, PKG-07 | Product direction, project truth, stable identity, package flatness, path-as-projection, App session/event consumption, and checkout evidence. |
| `K-AUTH`, `K-BIND`, `K-GATE`, `K-PROF` | PKG-01, PKG-07, PKG-10 | Human gates, binding/non-binding record separation, approval SHA, professional-boundary copy. |
| `K-ROOT`, `K-PACKAGE` | PKG-07, PKG-08, PKG-09 | Instruction-root/working-root separation, instruction-root write protection, packaged resource integrity. |
| `K-CORE`, `K-ENGINE`, `K-RELIANCE`, `K-SDK` | PKG-01, PKG-03, PKG-04, PKG-09 | Root-owned generic terms and engine contracts; App client conformance, provider/SDK isolation evidence, first-adapter compatibility, and affected-client fallback evidence. |
| `K-EVENT` | PKG-03, PKG-05, PKG-09 | Root-owned runtime-event/persistence semantics; App UI/runtime-event separation, terminal-outcome presentation, redaction, and affected-client conformance evidence. |
| `K-PERM`, `K-TOOL`, `K-MCP`, `K-HOOK`, `K-PATH`, `K-BASH` | PKG-04, PKG-06, PKG-07, PKG-09 | App/project policy, deterministic acts, explicit hard denies, human gates, and conformance; daemon-owned generic tool mediation/execution; project path containment and Bash denial. |
| `K-STATUS`, `K-DEP`, `K-PROV`, `K-INVENT`, `K-CONFLICT`, `K-SNAP`, `K-REF` | PKG-01, PKG-07 | Lifecycle, dependency, provenance, TBD discipline, conflict surfacing, snapshots, reference tooling. |
| `K-WRITE`, `K-SEAL`, `K-GHOST`, `K-SUBAGENT` | PKG-08 | Checkout agent write scopes, sealed Type 2 context, no ghost inputs, project delegation authority, daemon-client dispatch, and checkout AgentRuns. |
| `K-NET`, `K-KEY`, `K-ATTACH`, `K-RELEASE`, `K-VALIDATE`, `K-RETIRED` | PKG-01, PKG-09 | Current provider/network scope, no unauthorized provider expansion, keys, attachments, release, validation, retired scope. |
| `K-DOMAIN` | PKG-10 | Future domain boundary, protected paths, OperationProposal, solver-truth separation. |

### 10A.2 SPEC Binding Notes

App deliverables must conform to Root-owned SPEC-defined runtime contracts and preserve App/project-owned physical and client contracts, including instruction-root and working-root separation, execution-root layout, deliverable metadata files, `_STATUS.md` lifecycle transitions, `Dependencies.csv` v3.1, daemon-session client compatibility, browser SSE event names, project-specific MCP acts and hooks, attachment policy, the packaged-daemon credential boundary, network-policy conformance, and Section 8/9 validation IDs. App conformance does not transfer generic runtime semantic ownership.

### 10A.3 TYPES Vocabulary and Type Targets

App deliverables must use TYPES vocabulary and stable ID rules while consuming Root-owned generic runtime types through governed client contracts. App/project authority and evidence types remain checkout-contained. Runtime contracts should preserve the TYPES targets for `HarnessEvent`, `HarnessPermissionDecision`, `HarnessSubagentRun`, `DomainEngineProfile`, and `OperationProposal` unless a governed amendment changes them.

### 10A.4 PLAN Roadmap Overlay

Packages are work domains, not execution phases. PLAN controls near-term App sequencing: client-contract compatibility, thin daemon proxy behavior, first-adapter compatibility, affected-client event/session conformance, prompt composition, settings isolation, and App run-logger integration precede App capability expansion. Read tools precede write/edit/bash. Consequential generic runtime changes activate Root `DEL-02-06`. Concrete non-Anthropic provider implementation and domain-engine work remain future-boundary scope until governed tranches authorize them.

---

## 10B. v3.2 Acceptance Checklist

| Check | Required Result |
|---|---|
| Source corpus alignment | DIRECTIVE, CONTRACT, SPEC, TYPES, PLAN, PRD, and SOFTWARE_DECOMP method rules are all reflected as active sources. |
| PRD traceability alignment | `docs/PRD.md` Section 16 points to this v3.2 decomposition as the active package/deliverable topology. |
| Topology stability | SCA-APP-009 expressly authorizes 80 scope items, 10 packages, 52 deliverables, 10 objectives, and S=9/M=41/L=2/XL=0; no other topology change is accepted. |
| Package flatness | No package nesting, phase packages, or sub-package layer. |
| Deliverable ID coupling | Every `DEL-XX-YY` remains coupled to `PKG-XX`. |
| Scope ledger coverage | Every scope item has exactly one owner package and at least one mapped deliverable, except explicit OUT/TBD boundary handling. |
| CONTRACT invariant coverage | The live `contract_invariant_coverage_register.csv` contains exactly 81 unique CONTRACT invariant IDs in 48 families, with no missing, extra, or duplicate IDs; every row passes closed-enum, source-basis, semantic-owner, and App-topology reference validation. |
| Mapping authority and parity | Field-level precedence preserves CONTRACT identity/text, accepted App topology, cited external-owner authority, and register-bounded mapping/evidence disposition; Section 8 and Section 9 report zero unexplained assignment differences, with supported relations preserved and OUT rows still OUT. |
| SPEC conformance | App execution-root/deliverable metadata, checkout authority/evidence, project-specific deterministic acts, human gates, and client compatibility remain intact while App conforms to Root-owned session, event, adapter, tool-execution, interruption, credential, and residency semantics. |
| TYPES conformance | Stable identifiers and future domain vocabulary remain intact; App consumes Root-owned runtime types while preserving checkout permission, approval, and AgentRun authority/evidence. |
| PLAN sequencing | R0/R1 precedes R2+ capability expansion; read tools precede writes/bash; concrete non-Anthropic provider implementation and domain execution stay future-amendment scope. |
| Professional-boundary posture | No automated approval, certification, issue, solver-truth, code-compliance, or external-validation claim is introduced. |
| Retired scope | Retired PKG-08 hardening items remain out of active scope unless governed amendment reactivates them. |

---

## 11. Open Issues

| IssueID | Type | AffectedScope | Description | Required Resolution |
|---|---|---|---|---|
| OI-001 | FIRST_ADAPTER_PROBE | SOW-018, SOW-044, SOW-045 | Claude Agent SDK / Anthropic first-adapter viability, message categories, settings behavior, hooks, permissions, MCP, sessions, and packaging must be empirically confirmed. | Complete R0 first-adapter probe before R1 production default. |
| OI-002 | SDK_TRANSCRIPT | SOW-046 | Exact SDK transcript placement and linkage across daemon operational session state and checkout-contained project evidence is not yet decided. | A separately governed contract tranche must resolve placement/linkage without making the SDK transcript canonical or transferring project authority to daemon state. |
| OI-003 | PACKAGING | SOW-072, SOW-080 | First-adapter subprocess, macOS DMG packaging, and the App-side two-job installer transaction must be verified after adapter adoption and Root control/storage semantics land. | R1 packaging probe, `desktop:dist` validation, and gated DEL-09-07 transaction evidence. |
| OI-004 | SOURCE_COMPLETENESS | SOW-030, SOW-073 | Required instruction-root assets may be missing in the current source or packaging state. | Complete source tree or amend integrity requirements and code paths. |
| OI-005 | DOMAIN_FUTURE | SOW-066-SOW-071 | Domain engine profile work is future platform scope and requires amendment before implementation. | Keep domain deliverables as future-boundary package until core harness stability. |
| OI-006 | PROVIDER_EXPANSION | SOW-020, SOW-021, SOW-037 | D-APP-72 / SCA-APP-002 activates bounded App packaging/client conformance for the Pi `0.80.10` / authenticated loopback oMLX child path; Root owns generic adapter, network, security, and runtime-contract semantics. | Implement only the authorized read-only Agent 2 client milestone; route generic semantic changes through Root and keep every other provider/harness expansion gated. |
| OI-007 | SHARED_RUNTIME | SOW-009-SOW-011, SOW-037, SOW-043, SOW-046, SOW-063, SOW-072, SOW-079-SOW-080 | D-GOV-20 / D-GOV-28 / Root PRD O-11 and accepted Root decomposition revision 1.1 assign generic runtime stewardship to Root through `SOW-104 → PKG-02 → DEL-02-06`; D-APP-73 / SCA-APP-003 retain App client migration, compatibility, packaged-daemon mode, and conformance work. Root DEL-02-08 governs exact App Server supply/download authority, while Root DEL-02-07/DEL-02-11 govern supervisor, runtime-control, and storage semantics. | Route consequential generic runtime semantic changes through Root; complete App observation, client migration, installer integration, and affected-client conformance only after the named Root gates and separately authorized App tranches; prove one runtime owner and both pilots before export. |

---

## 12. Decision Log / Change Log

| DecisionRef | Date | Decision | Rationale |
|---|---|---|---|
| DEC-001 | 2026-05-20 | The six active docs are the complete decomposition source corpus. | User specified docs folder as the source set. |
| DEC-002 | 2026-05-20 | Gates 1-7 are recorded as passed by implicit human approval. | User instructed implicit approval through all gates. |
| DEC-003 | 2026-05-20 | Use `PKG-XX` and `DEL-XX-YY` IDs. | SOFTWARE_DECOMP mandates two-digit IDs; current docs permit them. |
| DEC-004 | 2026-05-20 | Partition by work domain, not roadmap phase. | Required by SOFTWARE_DECOMP and CONTRACT flat-package invariant. |
| DEC-005 | 2026-05-20 | SDK scope is decomposed behind Chirality-owned contracts. | Superseded in strategic framing by DEC-017; retained as historical basis for first-adapter package topology. |
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
| DEC-017 | 2026-06-13 | SCA-APP-001 reorients runtime strategy to provider-adapter generality, keeps Claude Agent SDK / Anthropic as first concrete adapter, treats Pi as a pattern corpus only, and reframes permission governance as capability-forward with explicit deny precedence. | Human ruled D-APP-01/02/03 and requested formal SCOPE_CHANGE before project-truth mutation. |
| DEC-018 | 2026-07-21 | D-APP-72 / SCA-APP-002 prospectively authorizes the bounded Pi `0.80.10` / authenticated loopback oMLX second-engine tranche after Electron `43.1.1`, initially for one governed read-only Agent 2 child. | Owner accepted the recommendation and explicitly ordered implementation of the decision-complete plan; topology and lifecycle state remain unchanged. |
| DEC-019 | 2026-07-22 | D-GOV-20 / D-APP-73 / D-T0-23 / D-PEC-56 / SCA-APP-003 establish a root-owned shared runtime, one per-user daemon, authenticated Unix-socket clients, explicit one-primary-model residency, app-dev Agent 1 → local Agent 2 pilot, and PEC client migration. | Owner explicitly ordered implementation of the decision-complete plan; existing package/deliverable topology is reused and lifecycle state remains unchanged. |
| DEC-020 | 2026-07-23 | SCA-APP-004 replaces the fixed surface/matrix target UI with owner-selected Woven Dialogue and a Work/Agents Coordination Panel while preserving routing, dispatch, runtime, compatibility, and human-authority boundaries. | The owner selected dialogue as the primary human–agent collaboration surface; structured work and agent hierarchy remain evidence-conditional projections, with no topology, runtime capability, lifecycle, or old-UI retirement change. |
| DEC-021 | 2026-07-27 | SCA-APP-005 corrects the App decomposition from generic runtime semantic owner to affected client while preserving the existing topology and App client integration, packaged-daemon mode, project authority, compatibility, user-experience, and conformance-evidence duties. | D-GOV-20 and adopted Root PRD O-11 assign continuing generic runtime stewardship to Root through Root SOW-104 / DEL-02-06; the owner approved the independently reconciled Revision 2 envelope. |
| DEC-022 | 2026-07-27 | SCA-APP-006 makes the 81-ID/48-family CONTRACT invariant coverage register live, establishes field-level authority precedence and Scope Ledger / Deliverables reverse-view parity, and reconciles seven supported mappings without changing topology or activating OUT scope. | The owner selected OD6-G1-P1 / OD6-G2-I1 / OD6-G2-M1-A; deterministic invariant census and assignment comparison require explicit machine-truth coverage while preserving CONTRACT, accepted App topology, and external-owner authority. |
| DEC-023 | 2026-08-23 | SCA-APP-008 prospectively seats the v3 account/consent, managed/native delegation, descendant-evidence, and release-operations duties on stable DEL-02-05, DEL-08-04, DEL-08-05, and DEL-09-05 carriers without changing the 10-package/51-deliverable topology. | Ryan Tufts accepted the Gate-1/2 assessment and all three SCC moves in A2; exact contract text remains Root/App-concordance-gated, implementation remains separately authorized, and WP-09 runbook authoring remains strictly separate from WP-11 owner release acts. |
| DEC-024 | 2026-09-04 | SCA-APP-009 seats the previously unseated App-boundary duties S-1, S-2, S-4a, and S-7 by adding SOW-079, SOW-080, and DEL-09-07 and by extending existing SOW-006, SOW-043, DEL-02-02, DEL-04-01, and DEL-05-01, changing topology from 51 to 52 deliverables. | Ryan Tufts accepted the Gate-2 impact assessment and expressly accepted ADD DEL-09-07 and the 51→52 topology. Root retains App Server supply/download, supervisor, runtime-control, storage, consent, and session-policy semantics; S-6 and the live nine-node SCC remain separate transactions. |

### Change Log

- 2026-05-20: Initial SOFTWARE_DECOMP working surface created from active `docs/` corpus.
- 2026-05-20: v2.5 amalgamated version added: retained 10-package structure, added deliverable descriptions, responsible-party placeholders, context notes, hard constraints, and downstream execution notes.
- 2026-05-20: v3 local full-governance correction added: considered all six active docs, restored SOFTWARE_DECOMP method posture, and emphasized human authority and filesystem/git project truth.
- 2026-05-20: v3.1 source-governed proposal reviewed: accepted as the better basis because it adds source authority, non-PRD control coverage, acceptance checks, and companion-register posture.
- 2026-05-20: v3.2 issued: adopted v3.1 topology, anchored references to active local docs and SOFTWARE_DECOMP, corrected companion-register status, updated source-completeness wording, incorporated v3's human-authority/project-truth emphasis into DEL-01-01, and aligned PRD Section 16 to the v3.2 decomposition authority.
- 2026-06-13: SCA-APP-001 landed provider-adapter-general runtime strategy, Pi pattern-corpus-only posture, and capability-policy / explicit-hard-deny permission governance without changing package/deliverable topology.
- 2026-07-21: SCA-APP-002 prospectively activated the D-APP-72 bounded Pi/oMLX second-engine tranche without changing package/deliverable topology or lifecycle state.
- 2026-07-22: SCA-APP-003 prospectively activated the shared-runtime extraction, daemon/client/CLI, explicit residency, app-dev pilot, PEC migration, and generic export sequence without changing package/deliverable topology or lifecycle state.
- 2026-07-23: SCA-APP-004 prospectively selected Woven Dialogue with a Work/Agents Coordination Panel, replacing fixed target-shell presentation while preserving legacy route/query/matrix compatibility, runtime capability limits, and the existing package/deliverable topology.
- 2026-07-27: SCA-APP-005 reconciled the App decomposition to Root-owned generic runtime semantics and App client/project-authority/compatibility/conformance duties without changing topology, mappings, context envelopes, lifecycle state, dependencies, or implementation authority.
- 2026-07-27: SCA-APP-006 created the authoritative 81-ID/48-family CONTRACT invariant companion register, established field-level authority and Scope Ledger reverse-view precedence, reconciled seven supported Section 8/9 relations, refreshed REF-006, and added DEC-022 without changing topology, context envelopes, lifecycle state, dependencies, estimates, schedule, or implementation authority.
- 2026-08-23: SCA-APP-008 prospectively assigned v3 account/consent UX, class-aware managed/native delegation, descendant evidence, and owner-gated release-operations duties to existing stable carriers without changing topology, scope-item mappings, context envelopes, lifecycle, dependencies, estimates, schedule, implementation authority, or release authority.
- 2026-09-04: SCA-APP-009 seated S-1/S-2/S-4a/S-7, added SOW-079/SOW-080 and DEL-09-07, updated the affected objective and open-issue mappings, and changed topology from 51 to 52 deliverables without granting S-6 write scope, resolving the separate nine-node SCC, changing lifecycle/dependencies/estimates/schedule, activating implementation, or authorizing a release act.

---

## 13. Downstream Execution Notes

- PREPARATION should scaffold from this v3.2 working surface unless a later human ruling replaces it.
- TASK / Type 2 agents should execute one deliverable at a time, preserve the `ResponsibleParty: TBD` field until a human assigns ownership, and treat `ContextEnvelope` as a work-sizing constraint.
- App R0/R1 client compatibility and conformance deliverables should execute before App R2+ capability expansion; consequential generic runtime contract, daemon, engine, session, event, credential, tool-execution, interruption, delegation, or residency changes route through Root `DEL-02-06`.
- Read tools and read MCP exposure precede write/edit and bash capability.
- The D-APP-72 Pi/oMLX read-only child tranche is the sole active non-Anthropic exception. Other concrete providers, domain engine execution, remote MCP, plugins, shipped bypass, non-macOS packaging, and retired PKG-08 work require governed amendment before implementation.
- D-APP-73 extends that exception only to authenticated loopback oMLX status/load/unload and explicit one-primary-model residency. Runs never switch models automatically; local Agent 1, automatic scheduling, multiple primary local models, and piping remain future-gated.
- Shared runtime promotion preserves this decomposition's existing package/deliverable topology. Root owns generic runtime semantics and `runtime/`; App deliverables retain only their separately governed client integration, packaged-daemon mode, project-authority, compatibility, presentation, and affected-client evidence duties. App implementation does not transfer generic runtime ownership.
- SCA-APP-004 selects Woven Dialogue with a Work/Agents Coordination Panel as the target information architecture. Work plans/tasks are shown only from explicitly recorded sources with visible authority/provenance classes; agent hierarchy and selected-session replay are canonical-evidence-conditioned; replay is read-only and cannot mutate the mounted primary live dialogue. The tranche adds no runtime capability, does not define shared intent as a stored UI object, and preserves existing routes, query parameters, browser APIs, SSE names, provider composition, state rollback, and the loop-first UI through a compatibility period.
- REVIEW should check package flatness, scope ledger coverage, context-envelope posture, no automated professional approval claims, provider/SDK settings isolation, no unauthorized provider/network expansion, and no domain solver ownership claims.
- REVIEW should also check CONTRACT invariant-family coverage, the companion invariant register, SPEC/TYPES conformance, PLAN sequencing, PRD traceability, and SOFTWARE_DECOMP method conformance before accepting implementation or scaffold outputs.
