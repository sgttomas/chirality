# D-APP-84 — PROPOSAL REVISION 2: Native Pi Primitives and Agent Sandboxes

Status: `PROPOSAL REVISION 2 / AWAITING_RULING`

DecisionID: `D-APP-84`

ProposalRevision: `2`

Prepared: `2026-08-01`

Amended: `2026-08-02`

PreparedBy: `HELPS_HUMANS`, managed by `HELP_HUMAN`

Accepted preparation basis: branch
`codex/appdev-pi-agent2-capability-packet@fc06b3388de17dcd5fc65eb29bf77c7f551a64cc`;
scoped comparison through refreshed `origin/main@23d15899fd0acf5d1d0513f3fe396438375c9e25`
shows no intervening change to `AGENTS.md`, the applicable agent instructions,
`runtime/**`, or `projects/chirality-app-dev/**`.

SupersedesProposal:
`execution/_Coordination/_DECISIONS/D-APP-84_PACKET_PI_OMLX_AGENT2_CAPABILITY_EXPANSION_2026-08-01.md`
at SHA-256
`0f4ddfb3c71b1862225ce35430fc18b275588b2dfafbca7d884aaef524a9830e`.

AmendmentRecord:
`execution/_Coordination/AgentRuns/APPDEV_PI_AGENT2_CAPABILITY_PACKET_2026-08-01/amendments/H1-HELPS_HUMANS/V2.md`.

OwnerChallengePosture: `EVIDENCE / DIRECTION TO REVISE — NOT A RULING`.

This revision is coordination and proposal only. It creates no sandbox,
capability, Root doctrine, runtime semantic, version, resume behavior, source
write, or approval. A separate owner ruling is required.

## Decision request

```text
DecisionID: D-APP-84
RequestedBy: HELPS_HUMANS
Question: Which Root-routed Pi-native primitive, role-specific sandbox, Agent-2 Bash, version, and durable-resume posture should govern prospective App affected-client expansion beyond D-APP-72?
Options: Select B1 with one token each from V, P, X, H, and R, subject to the compatibility rules below; B2, B3, and D are standalone terminal responses.
Recommendation: B1 + V1 + P1 + X1 + H1 + R1. This is non-binding.
Evidence: This packet §§1-12; D-APP-60/64/72/73/76/83; SCA-APP-002/003; App authority and accepted decomposition; Root AGENTS doctrine and DEL-02-06; live App/Root runtime seams; Amendment V2 Agent 2 returns.
DownstreamBlocked: Any agent sandbox, Pi native tool exposure, write/edit/Bash capability, Root doctrine/runtime amendment, DEL-02-06 activation, Pi-version concordance, durable resume, App SCOPE_CHANGE, implementation, or reliance effect.
```

## 1. Proposal revision history

| Revision | Status | Identity | Disposition |
|---|---|---|---|
| 1 | Superseded proposal evidence; never ruled | 2026-08-01 packet, SHA-256 `0f4ddfb3c71b1862225ce35430fc18b275588b2dfafbca7d884aaef524a9830e` | Owner challenged the custom-tool/defer-Bash posture and directed a native-primitive/sandbox revision. |
| 2 | Current owner-decision surface | This file; final hash bound in the v2 manager return/handoff | Presents Pi-native reuse, role-specific sandboxes, and sandboxed Agent-2 Bash without inferring Root authority. |

Revision 1 remains byte-preserved. Neither revision is a ruling.

## 2. Current facts and gaps

1. D-APP-72 authorizes Pi `0.80.10` only for one governed read-only Agent 2
   child with one Chirality-owned tool. It excludes Pi built-ins, native
   delegation, write, shell, network tools, direct supervision, ambient
   resources, attachments, remote providers, and automatic fallback.
2. D-APP-73 adds explicit local-model residency control but retains those
   boundaries and forbids local Agent 1.
3. The live App adapter already reuses Pi's native `createAgentSession`,
   `ModelRuntime`, `SessionManager`, event subscription, prompt loop,
   interruption, and compaction machinery. It currently sets `noTools: 'all'`
   and supplies only Chirality custom tools
   (`frontend/src/lib/harness/pi-agent-engine-adapter.ts:527-585`).
4. The Pi resource loader is deliberately stripped of extensions, skills,
   prompt templates, themes, context/AGENTS files, settings, and ambient
   resources (`pi-agent-engine-adapter.ts:488-520`). Revision 2 preserves that
   isolation; native primitive reuse is not ambient Pi-product adoption.
5. There is **no live agent/tool OS sandbox implementation** in App or Root.
   Electron `BrowserWindow` uses `sandbox: true` for renderer isolation only
   (`frontend/electron/main.ts:501-511`); the runtime daemon creates no
   BrowserWindow and this setting does not contain agent tools.
6. Current Bash control is descriptor/permission/hook plus lexical command
   inspection. It rejects a requested `dangerouslyDisableSandbox`, background
   execution, obvious network commands/URLs, traversal, and visible path
   escapes (`tool-shell-policy.ts:157-340`). No sandbox backend is thereby
   created. Lexical command inspection is **not containment**.
7. Root doctrine currently says any Bash-bearing managed child has explicit
   project-root read/write scope and is the serialized integration owner for
   its stage (`AGENTS.md`, Multi-Agent Orchestration; `AGENT_WORKING_ITEMS`).
   This remains binding until a separate Root owner ruling changes it.
8. App dependency surfaces pin Pi `0.82.0` and the Root engine descriptor
   declares `0.82.0`, while D-APP-72/App authority says `0.80.10`. Git bytes
   are not approval.
9. Pi descriptors still declare `durableResume: false`; canonical event replay
   does not hydrate a fresh Pi session.

## 3. Recommended X1 execution-plane architecture and common invariants

The table is the recommended X1 target. It becomes binding only if X1 is
selected and the later Root/App gates accept its exact design. X2 and X3 use
the same plane distinction and non-bypass invariants but place only the
instances or tool effects stated in their option text inside sandboxes. No
option uses one shared sandbox.

| Plane | Recommended responsibility | Trust and isolation |
|---|---|---|
| Trusted daemon/control plane | Project authorization, hierarchy/seals, credentials, provider/model brokerage, exact policy decision, sandbox-profile construction, session/run identity, canonical audit append, interruption, evidence fan-in | Outside agent sandboxes; exposes only authenticated, capability-scoped IPC; remains Root-owned. |
| Per-agent model/session worker | One Agent 0, 1, or 2 instance/run; provider adapter session, prompt/model loop, Pi/SDK event and tool loop | Under X1, one fresh role/run-specific OS sandbox; never shared with a sibling or reused across authority contexts. X2 and X3 placement is governed by their option text. |
| Tool executor | Native or Chirality tool implementation and any subprocess tree | Runs inside the worker sandbox or a strictly narrower per-invocation child sandbox/broker; cannot escape mounts, environment, process, IPC, or network policy. |

For Pi-native Read/Write/Edit/Bash under any X1/X2/X3 selection, sandboxing
only a spawned Bash process is insufficient: in-process native file tools
could otherwise read or mutate from the daemon process. A conforming
implementation must do one of:

1. place the Pi agent session and its native tool implementations inside the
   per-run sandboxed worker; or
2. prove that every native tool execution boundary is replaced by a sandbox
   broker, so no native file/process operation executes in the trusted daemon.

The trusted daemon brokers provider/model transport separately from tool
network. A model's allowed oMLX channel never grants DNS, socket, or general
network capability to tools. Credentials are not ambient worker resources.

## 4. Owner selections and compatibility rules

Only B1 opens V/P/X/H/R. B2, B3, and D are standalone. Compatibility:

- P1 or P2 requires a real sandbox posture X1, X2, or X3 before any native or
  mutating tool runs. X4 is compatible only with P3 and H3.
- H1 or H2 requires X1, X2, or X3. H1 is additionally Root-conditioned: it
  has no Bash effect unless Root separately replaces the current doctrine.
- X1/X2/X3 select architecture and acceptance criteria, not an already
  existing sandbox backend.
- V and R are independently selectable inside every otherwise valid B1 tuple.

### B — Root/App ownership and sequencing

- **B1 (recommended): App affected-client envelope plus separate Root routes.**
  App selects its desired client/policy/conformance posture. Root separately
  decides generic sandbox/runtime semantics, DEL-02-06 activation, and any
  doctrine amendment. D-APP-84 changes no Root byte.
- **B2 (standalone): Root first.** Hold App capability selection; ask Root to
  decide identity, sandbox, primitive, and Bash doctrine first; return through
  a later App proposal. No V/P/X/H/R token is selected.
- **B3 (standalone): Propose ownership transfer.** Stop and prepare explicit
  paired Root/App scope and decomposition amendments. No V/P/X/H/R token is
  selected.

### V — Pi version

- **V1 (recommended): Root-conditioned `0.82.0` App compatibility target.**
  Accept it prospectively only after Root accepts the same adapter identity and
  supply-chain, native-primitive, sandbox, security, packaging, and conformance
  evidence passes.
- **V2: Restore `0.80.10`.** Require exact dependency rollback plus full
  regression and native-primitive API verification.
- **V3: Defer.** Hold implementation for a separate exact-version decision.

### P — Pi harness primitive strategy

- **P1 (recommended): Native-first behind Chirality contracts.** Reuse Pi's
  agent/model/session/tool loop and conforming native Read/Write/Edit/Bash
  implementations inside the selected sandbox architecture. Chirality retains
  public tool identity/schema, exposure policy, pre-execution authorization,
  path/mount derivation, human gates, result budgets, redaction, canonical
  events, evidence, interruption, and audit. Pi-native permission defaults are
  not authority. Each public tool selects exactly one implementation—a
  conforming Pi-native primitive or a registered Chirality tool—when its
  versioned capability profile/registration is accepted. There is no silent
  runtime tool fallback. If the selected implementation is unavailable, fails,
  or cannot be wrapped or brokered without bypass, the affected operation fails
  closed. Changing implementations requires an explicit versioned
  profile/registration update, renewed conformance evidence, and a new
  session; an active session never changes implementation family.
- **P2: Hybrid.** Reuse Pi's agent/model/session/tool loop, interruption, and
  compaction, but use Chirality implementations for filesystem and shell tools.
  Native implementations remain disabled; registered deterministic tools are
  preferred for stable operations.
- **P3: Custom-tool posture.** Retain `noTools: 'all'` and expand only the
  Chirality custom bridge. This maximizes policy uniformity but duplicates more
  harness behavior and rejects the owner's native-first preference.

No P option permits native subagents, ambient resources, provider selection,
credentials, settings, prompts, extensions, skills, or public Pi-shaped
governance semantics.

### X — Which agents App-dev should sandbox

- **X1 (recommended): Every tool-executing Agent 0/1/2 instance, with
  role/run-specific profiles.** Each instance receives a separate sandbox.
  HELP_HUMAN/Agent 0 remains no-project-content-write and normally read-only
  plus control-plane IPC; Agent 1 receives only its manager/brief scope; Agent 2
  receives the narrowest sealed read/write/tool mounts. Parent and child never
  share a writable sandbox. A sandbox narrows an instance; it never widens role
  authority, changes hierarchy, or permits Pi in Agent 0/1.
- **X2: Agent 2 only.** Sandbox every tool-executing Agent 2 run, including Pi;
  retain current Agent 0/1 process posture. This reduces the immediate Pi risk
  but leaves manager/supervisor tool processes outside the new boundary.
- **X3: Tool-broker sandbox.** Keep model/session loops in the daemon or an
  unsandboxed worker, but broker **every** filesystem/process tool into a fresh
  role/run-specific sandbox. This is valid only with proof that no SDK/Pi native
  tool or extension executes outside the broker.
- **X4: No OS sandbox.** Retain permission/hooks/lexical controls only. This is
  current behavior, not a containment claim, and is incompatible with native
  mutation or Bash selections in this packet.

X1 is a Root-wide runtime preference, not App authority over Agent 0/1. Root
must define the generic profiles; App supplies affected-client policy,
packaging, presentation, and conformance evidence.

### H — Arbitrary Bash

- **H1 (recommended): Agent-2-only Bash in an enforced narrow sandbox,
  Root-conditioned.** The App requests a Root doctrine successor under which a
  Pi Agent 2 Bash run receives only mechanically enforced mounts/capabilities
  derived from its sealed brief, default-denied tool network, bounded process
  tree, timeout/output/artifact/interruption evidence, and serialized ownership
  only where actual mounted write overlap requires it. This is the target
  architecture; **until Root separately rules and implements it, the current
  project-root read/write plus serialized-integration-owner rule remains in
  force and H1 authorizes no Bash.** This App tranche grants no Bash to Agent 0
  or Agent 1.
- **H2: Current Root doctrine plus sandbox defense-in-depth.** Permit Pi Agent 2
  Bash only with full project-root read/write scope and serialized integration
  ownership. A real sandbox may deny outside-project/process/network access but
  does not narrow logical project scope or permit parallel Bash.
- **H3: No arbitrary Bash.** Use native or registered deterministic bounded
  tools only.

Lexical inspection remains a deny heuristic under H1/H2; it is never the
containment boundary.

### R — Durable resume

- **R1 (recommended): Strict replay-and-bind, held behind Root identity.** A
  fresh sandboxed worker is created; resume replays admitted product audit
  events only after exact equality over Root compatibility identity, accepted
  Pi version, sandbox-profile identity, exact model, residency epoch, and
  transcript/event-prefix SHA-256. Mismatch offers explicit new-session-from-
  transcript, never silent resume or operation replay.
- **R2: Defer.** Retain `durableResume: false` until Root identity and sandbox
  semantics are effective.
- **R3: Fresh sessions only.** Decline Pi durable resume for this generation.

### D — Decline

- **D:** Retain D-APP-72/D-APP-73 exactly. Route version drift separately.

## 5. Sandbox backend acceptance contract

No backend is selected or implemented by this packet. The Root design tranche
must select or create an actual OS-enforced backend—such as a proven macOS
Seatbelt/`sandbox-exec` profile or another process/filesystem/network isolation
mechanism—behind a portable fail-closed interface. A named technology is not
proof. Minimum acceptance:

1. exact read-only/read-write mounts plus isolated temporary/output roots;
2. denial outside mounts, instruction/protected roots, undeclared IPC, device,
   process, environment, credential, and network surfaces;
3. child-process inheritance with no background orphan or privilege widening;
4. provider/model communication only through the declared broker/channel;
5. fail-closed behavior when backend/profile creation, platform support, mount
   resolution, canonicalization, or evidence capture fails;
6. no shared sandbox between runs, roles, siblings, or changed authority;
7. stable profile/backend/version identity in session, tool, resume, and audit
   records; and
8. escape/adversarial tests for symlink, hardlink, rename/race, inherited file
   descriptor, environment/HOME, nested shell, subprocess, socket/DNS/URL,
   IPC, signal, sibling-run, output-budget, interruption, and cleanup paths.

`dangerouslyDisableSandbox` remains denied. Unsupported platforms do not
silently fall back to unsandboxed tool execution.

## 6. Role/instance semantics

Sandboxing applies to an **agent instance/run**, not to the abstract Agent
0/1/2 authority contract. The same backend may construct different profiles;
the same capability set must not be copied across roles.

- Agent 0 remains HELP_HUMAN, delegates only Agent 1, and gains no project
  content write through sandboxing.
- Agent 1 retains its named manager authority and may delegate only Agent 2.
- Agent 2 remains bounded, sealed, and non-delegating.
- Pi remains Agent-2-only. X1 does not authorize Pi as primary, supervisor,
  Agent 0, or Agent 1.

## 7. Root doctrine conflict and required route

H1's narrow-mount target conflicts with current Root Bash doctrine. It cannot
be inferred from App policy or from a future sandbox implementation. Under B1
and H1, route an ordinary App request to Root HELP_HUMAN for:

1. a Root HELPS_HUMANS decision packet defining per-run sandbox semantics and
   whether mechanical mounts replace the full-root/serialized rule;
2. explicit Root owner rulings for `AGENTS.md`,
   `agents/AGENT_WORKING_ITEMS.md`, shared tool/shell contracts, overlap and
   concurrency criteria, and any affected instruction mirrors/notices;
3. Root SCOPE_CHANGE impact over at least DEL-02-04, DEL-03-01, DEL-02-06,
   Root decomposition/authority, validators, and runtime packages;
4. separately authorized DEL-02-06 planning/identity/sandbox work and later
   runtime implementation; and
5. App SCOPE_CHANGE only after Root accepts generic semantics.

Until that route is effective, a Bash-bearing managed child still takes
project-root read/write scope and serialized integration ownership.

## 8. D-APP-60 / D-APP-64 classification

| Matter | Class | Basis |
|---|---|---|
| Native Pi tool primitive reuse/exposure | OWNER_CLASS | D-APP-72 exclusion and new capability/acceptance criteria. |
| Sandbox semantics for A0/A1/A2 | OWNER_CLASS | Root-wide runtime/role boundary and new safety criteria. |
| Pi writes or Bash | OWNER_CLASS | Express current exclusion. |
| Narrow mounts replacing full-root/serialization | OWNER_CLASS ROOT | Changes authoritative doctrine, concurrency, and risk allocation. |
| Exact Pi version and durable resume | OWNER_CLASS | Unresolved authority conflict/new compatibility semantics. |
| Preserve ambient/delegation/attachment/fallback/remote fences | DISPOSITION_CLASS | Unchanged carry-forward; any relaxation is owner-class. |
| Exact backend/tool/profile after envelope is accepted | Potentially DISPOSITION_CLASS | Only if it satisfies every ruled criterion without changing authority or risk. |

## 9. Proposed on-ruling work graph

1. Record the exact D-APP-84 ruling separately; keep both proposal revisions.
2. Route Root identity, sandbox, primitive, and doctrine requests.
3. Root performs planning/decision/SCOPE_CHANGE before implementation.
4. App performs its own affected-client SCOPE_CHANGE after accepted Root
   semantics; presume no topology outcome.
5. Version gate precedes native-primitive or sandbox source work.
6. Build the trusted daemon/sandbox-worker/broker contract and backend first;
   prove fail-closed isolation before enabling write/edit/Bash.
7. Accept a versioned capability profile/registration that maps each public
   tool identity to exactly one conforming implementation; do not select or
   substitute implementations dynamically during an operation.
8. Enable selected native primitives behind Chirality policy/audit contracts.
9. Enable H1/H2 only after its prerequisites; enable R1 last.
10. Root and App validate independently and fan in; partial evidence does not
   authorize production, release, or reliance.

## 10. Prospective affected surfaces — inventory, not write authority

Root-owned/gated: `AGENTS.md`, `agents/AGENT_WORKING_ITEMS.md`, applicable
workflow/tool standards, Root DEL-02-06, Root decomposition/authority, and
`runtime/packages/{contracts,core,daemon,engine-pi-omlx}/**`, including new
sandbox-worker/broker/backend contracts and tests.

App-owned affected client: App authority/decomposition as proven by SCOPE_CHANGE;
`frontend/src/lib/harness/{pi-agent-engine-adapter.ts,pi-tool-binder.ts,chirality-tool-bridge.ts,managed-delegation.ts,permission-overlay.ts,tool-path-policy.ts,tool-shell-policy.ts}`;
`frontend/electron/runtime-host.ts`; packaging/dependency/notice surfaces; and
focused isolation, permission, native-tool, sandbox escape, network, secret,
resume, packaging, and contract tests.

No path in this inventory is authorized for change by proposal preparation.

## 11. Preserved exclusions

- No ambient Pi resources, native delegation/subagents, or Agent 2 delegation.
- No Pi primary, supervisor, Agent 0, Agent 1, or direct interactive role.
- No attachments, remote provider, redirect, embedded credential, automatic
  cloud/local or engine/model fallback, remote MCP, or undeclared tool network.
- Exact already-resident local model and one-primary-local-model posture remain.
- No protected-data/domain authority, lifecycle, release, publication,
  professional reliance, Task Management, receipt, parity, historical-UNKNOWN,
  commit, push, or merge effect.

## 12. Validation, rollback, and exact response

Validation must prove primitive-wrapper non-bypass, pre/post policy and audit,
sandbox profile identity, process/filesystem/network escape resistance,
role/run separation, provider/tool-network separation, current exclusion
denials, full engine/Claude regression, packaged behavior, and Root/App
conformance. Failure rejects the affected operation; no unsandboxed fallback.
Failure of a selected tool implementation also rejects the operation; it does
not invoke a different registered or native implementation at runtime.

Rollback disables the selected native/mutating tools and sandbox worker by
exact versioned policy, restores the last accepted Root/App identities, and
retains audit/evidence. Rollback is not release approval.

Recommended response:

```text
APPROVE D-APP-84 REVISION 2: B1 + V1 + P1 + X1 + H1 + R1.
```

Other valid B1 tuples select one V/P/X/H/R token and satisfy §4 compatibility.
Standalone responses:

```text
HOLD D-APP-84 REVISION 2: B2.
ROUTE D-APP-84 REVISION 2 OWNERSHIP TRANSFER: B3.
DECLINE D-APP-84 REVISION 2: D.
```

The recorder rejects incomplete or incompatible tuples and never infers an
omitted token.

## 13. No-effect fence

Revision 2 and the `AWAITING_RULING` row create no authority, sandbox,
capability, Root doctrine/runtime change, Pi native tool exposure, Bash,
version, resume, SCOPE_CHANGE acceptance, implementation, lifecycle, release,
publication, reliance, Task Management, receipt, parity, historical-UNKNOWN,
or Git effect.
