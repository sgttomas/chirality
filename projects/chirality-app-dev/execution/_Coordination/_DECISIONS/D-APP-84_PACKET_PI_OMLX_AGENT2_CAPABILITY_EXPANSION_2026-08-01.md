# D-APP-84 — PROPOSAL: Pi/oMLX Agent 2 Capability Expansion

Status: `PROPOSAL / AWAITING_RULING`

DecisionID: `D-APP-84`

Prepared: 2026-08-01

PreparedBy: `HELPS_HUMANS`, managed by `HELP_HUMAN`

Accepted preparation basis: `fc06b3388de17dcd5fc65eb29bf77c7f551a64cc`

Authority posture: this packet is coordination and a proposal only. It does
not amend D-APP-72 or D-APP-73, adopt the recorded owner intent, activate Root
`DEL-02-06`, change a Pi version, expand a capability, authorize source work,
or record an owner act. Only a separate ruling record can do so.

## Decision request

```text
DecisionID: D-APP-84
RequestedBy: HELPS_HUMANS
Question: Which bounded App policy, Root-routing, version, tool, shell, and durable-resume selections should govern a prospective Pi/oMLX Agent 2 expansion beyond D-APP-72?
Options: Select B1 together with one token from each of V, T, S, and R; B2, B3, and D are standalone terminal responses and take no V/T/S/R tokens.
Recommendation: B1 + V1 + T1 + S1 + R1. This is a proposal, not a ruling.
Evidence: OWNER_INTENT_2026-08-01_PI_AGENT2_CAPABILITY_EXPANSION.md; D-APP-72; D-APP-73; D-APP-76; D-APP-83; SCA-APP-002; SCA-APP-003; accepted App decomposition §§2.1/2.2/8; Root DEL-02-06 ScopeOfWork.md OUT-002 and REQ-001..009; live runtime/App seams enumerated below.
DownstreamBlocked: Any Pi multi-tool, write, registered-tool, shell, or durable-resume implementation; any K-ENGINE-6 amendment; any Root runtime semantic change or DEL-02-06 activation; exact Pi-version concordance; affected-client SCOPE_CHANGE and conformance work.
```

## 1. Current accepted state

1. D-APP-72 permits Pi `0.80.10` only as an opt-in, in-process second
   adapter over authenticated literal-loopback oMLX for one governed Agent 2
   child with one declared Chirality-owned read-only tool. It excludes Pi
   write, shell, network, native delegation, direct supervision, attachments,
   ambient discovery, remote providers, and automatic fallback.
2. D-APP-73 extends that posture only for explicit residency status,
   load/unload, drain/readiness, residency evidence, and the bounded pilot. It
   retains the read-only child boundary and the other exclusions.
3. App CONTRACT K-ENGINE-6 says every other provider/harness expansion needs
   a fresh governed tranche. K-PERM-1..6, K-TOOL-1..2, K-MCP-1,
   K-HOOK-1, K-PATH-2..3, and K-BASH-1 require mechanical policy, deny
   precedence, evidence, path containment, and validated shell behavior.
4. The live App Pi adapter rejects any write target, anything other than
   exactly one tool, any non-read-only descriptor, and attachments
   (`frontend/src/lib/harness/pi-agent-engine-adapter.ts:361-445`). The shared
   runtime protocol/coordinator likewise binds one `read_file`
   (`runtime/packages/contracts/src/protocol.ts:55-76`;
   `runtime/packages/core/src/agent1-run-coordinator.ts:213-330,660-758`).
5. Both live Pi descriptors declare `durableResume: false`. The App adapter
   uses an in-memory Pi session, rejects a session file, and disposes after a
   turn. Audit replay reads product events but does not hydrate a new Pi
   session. Interruption and compaction evidence already exist; neither is a
   durable resumed-context carrier.
6. Governing App records say Pi `0.80.10`, while App executable dependency
   surfaces pin `0.82.0` and the Root engine descriptor declares `0.82.0`.
   No governing ruling located in the App or Root
   decision/SCA surfaces accepts that change. Implementation bytes are not an
   approval record.

## 2. Root/App boundary conflict and required interpretation

The App Task Management migration records the owner's direction that this App
loop carries the runtime-identity question. That register is explicitly not
scope or authority. The accepted App decomposition says consequential generic
runtime semantics belong to Root `DEL-02-06`; App retains client integration,
project policy, packaging, presentation, and conformance.

Root `DEL-02-06` is `INITIALIZED`, not activated. Its OUT-002 is a Root-owned
compatibility identity. REQ-003 retains Root ownership, REQ-004 requires an
affected client to bind and compare the identity, and REQ-008 requires a new
consequential Root tranche for identity changes. OUT-001..009 remain
unproduced.

Therefore this packet interprets “App carries it” only as: App carries the
owner-facing coordination and may define its affected-client binding. It does
not transfer Root semantic ownership. If the owner intends an ownership
transfer, neither B1 nor B2 performs it; a separately explicit Root/App scope
and decomposition amendment is required.

## 3. Owner selections

Only B1 opens the V/T/S/R selections in this packet. B2, B3, and D are
standalone terminal responses; combining any of them with V/T/S/R is invalid
and must not be inferred or recorded.

Selection compatibility: S2 requires T1. T2 and T3 may be combined only with
S1 or S3 because they prohibit shell. V and R are independently selectable
within every otherwise valid B1 tuple.

### B — Ownership and sequencing

- **B1 (recommended): App affected-client decision plus separate Root route.**
  Rule the App capability envelope and client binding now. Route an ordinary
  notice/request to Root for a separately sealed `DEL-02-06` decision and
  activation covering the compatibility identity and every required generic
  runtime change. No Root bytes or semantics follow from D-APP-84.
- **B2 (standalone): Hold capability selection behind Root.** Route the Root
  identity and generic-runtime packet first; return through a new or
  superseding App proposal only after Root has an accepted identity and exact
  affected-client obligations. B2 selects no V/T/S/R option.
- **B3 (standalone): Explicitly propose ownership transfer.** Stop this packet without
  capability selection and prepare paired Root/App scope and decomposition
  amendments. This is not a shortcut to App implementation. B3 selects no
  V/T/S/R option.

### V — Exact Pi version disposition

- **V1 (recommended): Prospective App `0.82.0` compatibility target,
  Root-conditioned.** Accept `0.82.0` as the prospective App adapter/client
  target only if Root separately accepts the same runtime adapter version and
  the supply-chain, isolation, event, permission, network, packaging, and
  engine-conformance evidence passes. Until both acts and evidence exist,
  the `0.80.10` authority / `0.82.0` executable conflict remains visible and
  implementation is held.
- **V2: Restore the ruled `0.80.10` target.** Require a bounded rollback plan,
  dependency and lock restoration, security-shim re-evaluation, and full
  conformance before capability work.
- **V3: Defer version selection.** Hold all capability implementation and
  prepare a separate exact-version packet.

No option treats the current `0.82.0` bytes as approval by inference.

### T — Tool and write envelope

- **T1 (recommended): Multi-tool reads plus policy-gated exact-target
  writes and registered deterministic tools.** A sealed child brief declares
  exact read scope, exact writable targets, exact tool registry/version, and
  checkable return. Runtime enforcement canonicalizes paths, rejects symlink
  writes and scope escape, applies explicit deny precedence, denies unknown
  tools without prompting, and records permission/tool/result evidence.
  Registered tools resolve descriptor-to-handler identity before exposure.
  Availability never implies exposure. No network-capable tool is included.
- **T2: Multi-tool reads only.** Permit more than one declared read-only tool;
  retain zero write targets and prohibit write/edit/shell/network tools.
  Registered deterministic read tools may be exposed through the same exact
  registry and evidence rules.
- **T3: Retain D-APP-72.** Keep exactly one read-only tool and zero write
  targets.

For T1, ordinary post-ruling selection of particular tools and paths may be
disposition-class only inside the exact ruled envelope. Creating a new
normative tool class, protected-data exposure, or domain apply path returns to
the owner.

### S — Arbitrary shell/Bash

- **S1 (recommended): Defer arbitrary Bash; prefer registered deterministic
  tools.** This packet grants no shell. A later named-use-case packet may
  reopen it with exact commands/risks and evidence.
- **S2: Allow policy-gated Bash as a prospective capability.** Every
  Bash-bearing Pi child receives explicit project-root read/write scope and is
  the serialized integration owner for that stage. It must use validated
  timeout, bounded output capture, result artifacts, interruption/terminal
  evidence, background/network denial, and audit events. Lexical command
  inspection is not represented as package containment. This broad posture
  carries materially greater write and integration risk.
- **S3: Prohibit arbitrary Bash for Pi until a future owner amendment.** Only
  registered deterministic tools may perform build/test/validation acts.

S2 does not authorize shell implementation by itself; Root runtime semantics,
App affected-client scope, and exact SCOPE_CHANGE implementation bytes remain
separately gated.

### R — Durable resume

- **R1 (recommended): Accept the App replay-and-bind design; hold activation
  behind Root identity and version resolution.** A resume request creates a
  fresh isolated Pi session from the product-owned audit mirror. Before replay
  it compares exact equality over: Root compatibility identity; accepted Pi
  package version; exact model ID; residency epoch; and SHA-256 of the admitted
  transcript/event prefix. Mismatch or missing fields fail closed and offer an
  explicit **new session from transcript** action, never silent resume. The
  binding and replay boundary are persisted as product audit evidence.
- **R2: Defer durable-resume design until Root acts.** Keep
  `durableResume: false`; interruption and compaction remain current behavior.
- **R3: Fresh-session-only posture.** Decline Pi durable resume for this
  capability generation. Historical replay remains observational/read-only.

Under R1, accepted input and terminal events define replay boundaries.
Interrupted or indeterminate operations are not silently re-executed. SDK/Pi
transcripts remain resume/debug artifacts under K-SDK-3; product events remain
the canonical audit mirror under K-EVENT-4.

### D — Decline the expansion

- **D:** Retain D-APP-72/D-APP-73 exactly: one read-only Pi Agent 2 tool,
  `durableResume: false`, and all current exclusions. Route the version
  discrepancy separately because declining expansion does not resolve it.

## 4. Unchanged exclusions under every non-D selection

- No Pi primary interactive session, Agent 0, Agent 1, supervisor, or manager.
- No Pi/native delegation and no Agent 2 delegation.
- No attachments or ambient `.pi`, `~/.pi`, `.agents`, prompt, skill,
  extension, settings, credential, or user-resource discovery.
- No automatic cloud/local or engine/model fallback.
- No remote provider, redirect, embedded URL credential, remote MCP, or
  network-capable child tool.
- Exact model must already be explicitly resident; one managed primary local
  LLM remains the limit.
- No dedicated Agent 2 instruction package is created. TASK, an ephemeral
  generalist, or an already-approved dedicated specialist is selected per the
  live Agent 2 construction rules after capability authority exists.
- No lifecycle, release, publication, professional reliance, protected-data,
  external commitment, push, or merge effect.

## 5. D-APP-60 / D-APP-64 classification

| Matter | Class | Fast-reject basis |
|---|---|---|
| Capability expansion / K-ENGINE-6 change | OWNER_CLASS | New authorized scope; standing fresh-ruling stop. |
| Multi-tool reads | OWNER_CLASS | Exceeds the exact D-APP-72 exception. |
| Write/edit targets | OWNER_CLASS | New write authority, risk, and criteria. |
| Arbitrary Bash | OWNER_CLASS | Express prohibition; full-root/serialized cost; new risk. |
| Durable-resume semantics | OWNER_CLASS | New compatibility, replay, and recovery criteria. |
| Pi version selection | OWNER_CLASS | Unresolved authority conflict and prospective supersession. |
| Root/App ownership or Root activation | OWNER_CLASS | Scope/authority boundary and ruled Root gate. |
| Preserve interruption/compaction as-is | DISPOSITION_CLASS | Existing behavior, provided semantics do not change. |
| Preserve exclusions | DISPOSITION_CLASS | Carry-forward of accepted fences; any relaxation is owner-class. |
| Exact tools/paths/tests inside a ruled envelope | DISPOSITION_CLASS | Bounded implementation selection after the owner fixes scope. |
| Dedicated Agent 2 package | OWNER_CLASS | Persistent new package requires explicit HELPS_HUMANS proposal and approval. |

Packet drafting and evidence organization are disposition-class under
D-APP-64. No case-specific owner selection is attributed in this packet.

## 6. Proposed on-ruling work graph

1. **Record only:** create a separate `D-APP-84_RULING_2026-08-01.md`, copy
   the exact owner tokens, transition only the register row to `RULED`, append
   the post-ruling loop receipt, and preserve this packet.
2. **Root route:** under B1, send a coordination notice with the exact
   selected App requirements; under terminal B2, send only the identity and
   generic-runtime preparation request. Root decides whether and how to activate
   `DEL-02-06`; its output must include the Root compatibility identity,
   runtime semantic changes, affected-client census, regression evidence, and
   release disposition appropriate to its accepted Scope of Work.
3. **App SCOPE_CHANGE:** rederive scope and affected deliverables; freeze
   prospective authority/decomposition/concordance changes with no topology
   change presumed; retain D-APP-72/73 as immutable history; stop at every SCA
   owner gate.
4. **Version gate:** execute V1, V2, or V3 before capability source work. Root
   and App exact-version identities must agree for a coupled runtime/client
   tranche.
5. **Phase 1:** implement only the selected T envelope, first in Root-owned
   runtime contracts/protocol/coordinator/registry/receipts under Root
   authority, then in App-owned client/compatibility/packaging surfaces under
   App authority.
6. **Phase 2:** if selected, enable registered deterministic tool handlers and
   exact registry/fingerprint attribution. Do not treat descriptor presence as
   exposure authority.
7. **Phase 3:** execute S2 only as the serialized integration stage described
   above. S1/S3 perform no Bash work.
8. **Phase 4:** execute R1 only after the Root identity and exact Pi version are
   effective and conformance passes. R2/R3 retain `durableResume: false`.
9. **Fan-in:** Root validates generic semantics; App validates affected-client
   compatibility, policy, packaging, UI/API, security, and conformance. A
   failed node blocks only dependants; no partial return is accepted.

## 7. Prospective affected surfaces — inventory, not authority

### Root-owned or Root-gated

- `runtime/packages/contracts/src/{engine.ts,protocol.ts,session.ts}` and
  `runtime/packages/contracts/src/harness/{agent-engine-port.ts,engine-conformance.ts,tool-descriptor.ts}`.
- `runtime/packages/core/src/{agent1-run-coordinator.ts,runtime-service.ts,session-store.ts,turn-coordinator.ts}` and any new registered-tool/replay binding.
- `runtime/packages/engine-pi-omlx/**`, Root tests, Root DEL-02-06 outputs, and
  any Root compatibility-contract record.

### App-owned affected client

- `frontend/src/lib/harness/{pi-agent-engine-adapter.ts,pi-tool-binder.ts,chirality-tool-bridge.ts,managed-delegation.ts,permission-overlay.ts,tool-path-policy.ts,tool-shell-policy.ts}`.
- `frontend/electron/runtime-host.ts` and App API/UI
  presentation only where the accepted client boundary requires it.
- `frontend/package.json`, lock/notice/supply-chain surfaces, and exact-version
  validation under the selected V token.
- Focused Pi adapter, bridge, policy, path, delegation, engine-conformance,
  fake-loopback, interruption, compaction, session/replay, packaging, network,
  secret, and contract-pin tests.

### App governance and derivative concordance

- App `docs/DIRECTIVE.md`, `CONTRACT.md`, `PRD.md`, `PLAN.md`, `SPEC.md`,
  `TYPES.md`, validation/release docs, and harness reliance boundary as proven
  affected by SCOPE_CHANGE.
- Active App decomposition and invariant coverage register, with no topology
  assumption.
- An immutable SCA snapshot; authority-corpus version bump and affected
  deliverable `_REFERENCES.md` only after actual authority changes.
- Reverified affected-deliverable `_STATUS.md` history/Remaining entries only;
  no lifecycle transition.

TM-APP-001 and TM-APP-024 are linkage evidence only. This packet does not edit
the Task Management register. The parity instrument remains unselected. The
six historical `UNKNOWN` relations remain unchanged.

## 8. Validation and fail-closed acceptance

The selected implementation must add positive, negative, and adversarial
coverage for:

- exact tool-set and registry identity; undeclared/unknown tool denial;
- read/write mode, exact target, canonical path, symlink, and scope escape;
- hard-deny precedence, permission evidence, result artifact budgets, and
  secret redaction;
- direct/manager/supervisor/delegation/attachment/ambient/fallback denials;
- loopback-only provider, manual redirect, exact model, residency epoch, and
  no automatic switching;
- Bash timeout, output capture, result storage, interruption, background and
  network denial if S2 is selected;
- Root compatibility mismatch, version/model/epoch/prefix mismatch, malformed
  or truncated audit replay, interrupted/indeterminate turn boundaries, and
  explicit new-session-from-transcript behavior if R1 is selected;
- engine conformance, Root regression, App client conformance, daemon/client
  compatibility, packaged build, supply chain, secret scan, network policy,
  and unchanged Claude path.

Failure of identity, policy, registry, path, permission, residency, replay, or
evidence preconditions rejects the affected operation. It never silently
downgrades, retries a consequential operation of unknown completion, selects
another engine/model/transport, broadens scope, or invents a resume.

Rollback restores the exact pre-change Root and App identities and retains the
audit/evidence trail. Git reversion is not a semantic approval or release act.

## 9. Risks and tradeoffs

- **B1** permits useful App decision progress but introduces a coupled
  cross-loop dependency; **B2** is simpler but delays all capability work;
  **B3** is the largest governance change.
- **V1** aligns with live bytes but requires fresh owner acceptance and full
  evidence; **V2** risks dependency/security regression; **V3** preserves the
  conflict and blocks implementation.
- **T1** provides the proposed utility with the largest permission and
  evidence surface; **T2** is lower risk but omits write workflows; **T3**
  retains current capability.
- **S1/S3** preserve mechanical containment and encourage deterministic
  tools; **S2** accepts full-project write scope and serial execution for an
  intrinsically broad primitive.
- **R1** provides continuity with strict identity and replay costs; **R2**
  defers design risk; **R3** is simplest but permanently gives up Pi resume for
  this generation.

## 10. Exact response format

To select the recommendation, the owner may return:

```text
APPROVE D-APP-84: B1 + V1 + T1 + S1 + R1.
```

Any other `B1 + V? + T? + S? + R?` combination is valid only when S2 is paired
with T1; T2/T3 require S1 or S3. The standalone
responses are `HOLD D-APP-84: B2.`, `ROUTE D-APP-84 OWNERSHIP TRANSFER: B3.`,
or `DECLINE D-APP-84: D.` The ruling recorder must transcribe the exact
returned text, reject a B2/B3/D combination with V/T/S/R or an incompatible
T/S pair as invalid, and may not infer omitted tokens.

## 11. No-effect fence

Packet preparation and an `AWAITING_RULING` register row create no authority,
implementation, scope-change acceptance, Root activation, tool exposure,
resume state, lifecycle, release, publication, reliance, Git, Task Management,
parity, or historical-UNKNOWN effect.
