# A2 Runtime, Work-order, and Validation Review Return

RunID: `APPDEV_DAPP87_DUAL_TARGET_REPLAN_2026-08-03`

Role: ephemeral Agent 2 generalist; runtime/work-order/validation review only

Status: `PASS_FOR_DERIVATIVE_OWNER_PROPOSAL — BLOCKED_FOR_IMPLEMENTATION`

## 1. Sufficiency verdict

The frozen basis is sufficient to state App affected-client requirements for
both adopted targets, partition the existing deliverable inventory, propose a
domain-first work order, and define a target-by-target evidence matrix. It is
not sufficient to amend project truth, select architecture, define a generic
runtime contract, or begin implementation.

The controlling conclusions are:

1. The two required product targets are standalone Chirality Desktop and a
   per-domain control plane. Domain applications are the primary delivery
   vehicle for agents, so the first owner-gated product and implementation
   slice must be domain-first while preserving Desktop.
2. The implementation form remains unselected. This return does not choose a
   lightly skinned codebase, shared core with target-specific shells, or any
   third form.
3. App may define client-side product behavior, policy inputs, UI/API
   compatibility, packaging participation, and conformance evidence. Generic
   runtime, sandbox, runtime identity, version, resume, and Bash semantics are
   `BLOCKED_BY_ROOT`.
4. D-APP-89 is accepted derivative evidence for a validated migration
   candidate: ordinary App consumers use direct Root runtime-contract imports
   and the facade is no longer load-bearing. The candidate still awaits
   ordinary Git fan-in; the deprecated facade remains intact as rollback and
   cannot be treated as retired.
5. D-APP-88 R2 is accepted only as `BLOCKED/PARTIAL` diagnostic and rollback
   evidence. It proves that a distinct helper bundle was structurally
   buildable, not that target packaging or post-GUI graceful stop was accepted.
   Its Unix-socket/SSE explanation is a hypothesis, not a cause.

No implementation readiness, lifecycle closure, release readiness, signing,
notarization, publication, distribution, professional reliance, or foreign
loop acceptance is claimed.

## 2. Evidence and authority discipline

| Class | Inputs | Permitted use in this return |
|---|---|---|
| Adopted authority for this run | D-APP-87 ruling at SHA-256 `d13543f7164a688cd6ee5472455564e76eeba5f30acc1c157beb87017a82f0fe` | Fixes two targets and domain-first emphasis; authorizes planning only; keeps architecture unselected and named runtime lanes Root-blocked. |
| Selected proposal | D-APP-87 packet at SHA-256 `079d9b9874a3a0e37d6778d907329a360efab63996a134fa67738ef3f186a577` | Defines the six-lane planning output and later-owner-gate requirement. |
| Accepted product/decomposition basis | `docs/PRD.md`; SOFTWARE_DECOMP v3.2; active SCA pointer; SCA-APP-004, SCA-APP-005, and SCA-APP-007 handoffs; validation/build guidance; D-APP-36 | Supplies current requirements, 10/51/78/10 topology, App/Root ownership boundary, Woven Dialogue posture, preserved lifecycle rules, and evidence vocabulary. It is not changed here. |
| Live working state | `frontend/package.json`, `next.config.mjs`, Woven Dialogue shell, closed domain-profile registry, and `electron/main.ts` | Shows one Next/Electron workspace, one current package identity, shared UI composition, two ruled profile entries rather than a skin system, and one Electron entry serving GUI/daemon modes. Live source is not authority for a new architecture. |
| Accepted derivative evidence | D-APP-89 manager return and handoff | Supports the direct-Root-import migration candidate and its validation. It does not prove landing, facade retirement, DEL-03-01 closure, or generic-contract selection. |
| Blocked derivative evidence | D-APP-88 R2 manager return and handoff | Supports separate-helper structural feasibility, the exact failed evidence conjunct, complete rollback, and required rerun boundary. It is not accepted product or packaging state. |
| Coordination only | 2026-08-02 Root response notice; 2026-08-03 graceful-stop investigation notice | Traces open/deferred Root rows and routes a hypothesis for Root investigation. Neither notice establishes authority, causality, or completion. |
| Gaps / later decisions | Architecture, per-domain artifact identity, client target wire representation, Root contract semantics, complete cross-loop consumer needs, release posture | Remain `TBD`, `BLOCKED_BY_ROOT`, or owner-gated as identified below. |

The source/package observations therefore constrain planning but do not turn a
current one-workspace implementation into a ruled one-codebase architecture.
Likewise, the closed `open_pipe_stress` / `pec` registry is a live ruled-profile
registry, not a general product-skin or dynamic domain-discovery mechanism.

## 3. Findings

### 3.1 Current affected-client baseline

- The App is presently one npm workspace, one Next application, one Electron
  main entry, one `appId` (`com.chirality.app`), one product name (`Chirality`),
  and one packaging manifest. There are no accepted second product-shell or
  second packaging-manifest bytes.
- Woven Dialogue is the primary collaboration surface. Work/Agents remains an
  evidence-conditioned projection, selected replay remains read-only, and
  routes `/`, `/chat`, `/workbench`, and `/pipeline` retain compatibility
  obligations.
- App client surfaces already consume `RuntimeClient` over the local runtime
  control path and project binding, while Root owns generic session, event,
  lock, interrupt, tool, credential, identity, version, and resume semantics.
- The per-domain target must be a product target that focuses a user into typed
  agent interactions, structured information, workflows, and human decision
  gates. It must not be inferred to authorize domain-operation apply, direct
  protected-path writes, general domain-runtime activation, dynamic profile
  discovery, or solver-truth ownership.
- The standalone target remains a full Desktop product and compatibility
  baseline; domain-first does not permit Desktop regression or replacement.

### 3.2 D-APP-89 integration finding

D-APP-89 evidence may be consumed as follows:

- candidate state: 67 production and 39 ordinary test files migrated from the
  App facade to exact Root runtime-contract imports;
- candidate result: zero ordinary executable facade consumers, no load-bearing
  App config/build dependency, and 13 dedicated facade/Root rollback identity
  probes;
- validation: Root/App focused/full/type/build/package and standing checks
  passed for the frozen candidate;
- current residual: ordinary Git fan-in, then a fresh landed-tree zero-consumer
  census, then a later D-APP-76-compliant owner gate before facade deletion.

Therefore both targets should be planned against the direct Root-contract
client posture, while retaining facade rollback compatibility until the later
retirement ruling. This is an App import/client migration fact, not a generic
runtime-contract selection.

### 3.3 D-APP-88 integration finding

D-APP-88 R2 may be consumed only as a negative/diagnostic constraint:

- a separately built `Chirality Runtime Service.app` with helper bundle ID
  `com.chirality.app.runtime-helper` was structurally coherent in the frozen
  derivative run;
- final post-GUI first-signal graceful-stop evidence was not auditable and the
  mandatory conjunct failed;
- full later validation conjuncts were not completed, the TASK run had a tool
  policy violation, and every R2 product/config/test byte was rolled back;
- the routed Root notice asks Root to reproduce or disprove whether active
  Unix-socket/SSE or other long-lived clients hold awaited shutdown open. That
  mechanism is explicitly `HYPOTHESIS — NOT PROVEN`.

No dual-target plan may cite R2 as accepted helper packaging, accepted bundle
identity, accepted graceful-stop behavior, or proof of a Root defect. A later
target package that uses a separate runtime helper would have to rebuild from
an accepted source snapshot and rerun all D-APP-88 conjuncts after Root/App
disposition of the graceful-stop seam.

## 4. Affected-client interface inventory

The inventory below states App requirements only. Any field name, protocol
shape, semantic version rule, resume token, runtime principal, or sandbox
meaning needed across the Root boundary remains `BLOCKED_BY_ROOT` unless
already accepted by Root authority.

| Interface area | Common App requirement | Standalone Desktop target | Per-domain control-plane target | Boundary / gap |
|---|---|---|---|---|
| Product target context | App presentation and evidence must unambiguously identify which product target a result concerns. | Identify Desktop behavior and preserve current Chirality product identity until an App owner amendment says otherwise. | Identify the selected ruled domain application/profile and keep domain-specific copy/resources/config explicit. | Exact runtime wire identity or target-principal semantics: `BLOCKED_BY_ROOT`; exact package/bundle identity: later App owner gate. |
| UI composition | Preserve mounted primary dialogue, provenance-labelled artifacts, Work/Agents projection, read-only replay, disabled states, accessibility, and human authority. | Preserve the broad Woven/Workbench/Pipeline/working-root experience and legacy routes/queries/aliases. | Focus the user into typed agents, structured information, governed workflows, and decision gates; omit or disable unsupported breadth without changing underlying authority. | Architecture and skin/config implementation form remain unselected. |
| Project/domain binding | Supply checkout-contained project policy, working-root, persona, mode, and explicit context inputs; present missing/stale/conflicting state. | Bind the operator-selected working root and current project registration. | Bind an explicit domain application/profile plus project root; reject unknown/unruled profiles and do not use filesystem discovery. | Generic runtime identity/auth binding is Root-owned; profile expansion requires its own App/domain authority. |
| Runtime transport client | Preserve the App client boundary, local authenticated transport use, typed connectivity feedback, and no direct generic-runtime ownership. | Connect/reconnect from the packaged Desktop process and preserve current control/UI behavior. | Connect/reconnect from the domain control plane with equivalent isolation and project/domain attribution evidence. | Transport semantics, sandbox, runtime identity, and connection-drain behavior are Root-owned. |
| Session and turn client | Preserve public App route/SSE compatibility, typed errors, one-active-turn observation, interrupt/cancel forwarding, and terminal outcome presentation. | Prove create/list/resume/turn/interrupt/replay for Desktop against the accepted Root contract. | Prove the same affected-client behaviors from the domain target and prevent cross-domain or cross-target state confusion. | Generic session/resume/version semantics: `BLOCKED_BY_ROOT`; App may only prove client conformance. |
| Event/replay projection | Keep `UIEvent` separate from Root `HarnessEvent`; show provenance/currency; never promote runtime evidence to project truth. | Prove real-daemon transcript rendering and same-session Desktop/CLI replay residuals. | Prove domain-target event mapping, replay isolation, correct domain/project attribution, and no accidental interaction with a selected historical session. | Canonical event/persistence semantics remain Root-owned. |
| Policy, tools, and approvals | Supply App/project policy inputs and human decisions; display effective capability and permission evidence without redefining mediation. | Preserve existing governed tool/approval UI and disabled behavior. | Expose only tools/workflows ruled for that domain; keep unsupported domain operations disabled and protected paths unchanged. | Generic sandbox and Bash semantics: `BLOCKED_BY_ROOT`; domain operation execution remains separately gated. |
| Credentials and network presentation | Preserve App `safeStorage` participation, redaction, typed provider/network errors, and no project-secret writes. | Preserve current Desktop credential UI/client bridge and allowed endpoint posture. | Provide only the target-specific presentation needed for the ruled provider/domain path; no new provider or endpoint follows from product targeting. | Generic credential/network semantics remain Root-owned; any new provider/network or domain endpoint needs separate authority. |
| Shutdown, restart, and recovery | Show connectivity state, preserve user work, and collect client-visible reconnect/terminal evidence. | Prove GUI contact, graceful shutdown/restart, socket cleanup, and same-session recovery when the accepted contract permits it. | Prove equivalent shutdown/reconnect behavior with the domain client active. | D-APP-88 post-GUI first-signal proof is missing; Root investigation is routed and causal mechanism is unknown. |
| Packaging/resources | Bind source revision, target, configuration/resources, dependency boundary, instruction-root integrity, and unsigned/unnotarized state. | Produce and inspect the standalone macOS arm64 App/DMG under the current release posture. | Produce and inspect a separately identifiable per-domain artifact or target output only after architecture and package identity are ruled. | Artifact topology, bundle/product names, shared-vs-separate manifest form, signing, publication, and distribution are unselected. |
| Evidence identity | Every source/UI/package/runtime-client claim must name target and source snapshot; common evidence may be reused only where it actually proves both. | Desktop-specific evidence must not prove the domain target. | Domain-target evidence must not be inferred from Desktop-only results. | Common evidence is derivative and does not replace product/decomposition truth. |

## 5. Deliverable partition

This is a candidate amendment partition over the 35 deliverables named in the
frozen impact inventory. It creates no amendment, topology, lifecycle, or
assignment effect. The remaining 16 accepted deliverables outside that
inventory are `NO_CHANGE` by default.

### 5.1 Candidate direct amendments

| Deliverables | Candidate amendment purpose | Constraint |
|---|---|---|
| `DEL-01-03` | Add two-target product identity/copy and domain-control-plane professional-boundary acceptance. | Do not select bundle identity or imply solver/professional approval. |
| `DEL-02-01`, `DEL-02-02`, `DEL-02-04`, `DEL-02-05` | State shared versus target-specific Woven UI, domain-first workflow focus, target-scoped local state/config, typed errors, credentials/runtime feedback, and two-target accessibility/compatibility evidence. | Preserve mounted dialogue, Work/Agents authority limits, legacy routes/queries/aliases, and Desktop breadth. |
| `DEL-03-01` through `DEL-03-04` | Require both targets to conform to the accepted Root client boundary, API/SSE projection, session/turn client behavior, and interrupt/cancel/terminal presentation. | D-APP-89 direct-import candidate may be cited; facade retirement is not complete; generic semantics are not amended. |
| `DEL-04-01`, `DEL-04-02`, `DEL-04-05` | Add target-aware client probe/config-input and credential/network presentation evidence for both targets. | Exact generic identity, version, resume, sandbox, provider/network, and runtime semantics stay Root-owned and blocked. |
| `DEL-05-01`, `DEL-05-02`, `DEL-05-04` | Add two-target session-client compatibility, Root-event consumption, real-daemon replay, target/domain attribution, and primary-dialogue isolation evidence. | Runtime records remain operational evidence; checkout truth and human gates remain authoritative. |
| `DEL-08-02`, `DEL-08-03` | Add target-aware route/persona/session compatibility and domain-first DECOMP/PREP/TASK/AUDIT presentation/dispatch acceptance. | No inferred plan/task, no dynamic unruled domain profile, and no new dispatch authority. |
| `DEL-09-01` through `DEL-09-06` | Expand validation, focused tests, package evidence, CI/release verification, and security checks into common plus Desktop plus per-domain target matrices. | D-APP-88 is negative/blocked evidence only; current signing/publication posture is unchanged. |

### 5.2 Dependencies and cross-references, not direct semantic amendments

| Deliverables | Dependency / cross-reference role | Reason to avoid direct semantic amendment now |
|---|---|---|
| `DEL-02-03` | Reuse working-root/file-tree/scope behavior in both clients and include it in target UI evidence. | The adopted direction does not change filesystem truth or scan semantics. |
| `DEL-05-03`, `DEL-05-05` | Apply existing redaction and tool-result/provenance rules to both target evidence sets. | Targeting changes consumers/presentation, not generic redaction or result-storage ownership. |
| `DEL-06-01`, `DEL-06-02` | Supply existing App/project policy and registered-tool inputs; include per-target visible capability/denial evidence. | Generic sandbox/tool mediation/Bash semantics are Root-owned and cannot be selected here. |
| `DEL-08-04`, `DEL-08-05` | Preserve sealed-brief, approval, parentage, child-record, and accepted-artifact evidence when agents are reached through either target. | The two-target direction does not expand delegation authority or make daemon state project truth. |
| `DEL-10-01` | Record the governed-next-capability dependency for any target/profile contract change and preserve PEC client residuals. | A per-domain product target is not authorization for general domain-engine profile/runtime execution. |
| `DEL-10-05` | Reuse domain boundary notices and solver-truth separation in domain-target copy/review. | Boundary wording is required; no domain operation or solver ownership is activated. |

### 5.3 No-change preservation inside the impact inventory

| Deliverables | Preservation |
|---|---|
| `DEL-10-02`, `DEL-10-03`, `DEL-10-04` | Keep protected/proposal path policy, `OperationProposal` workflow, and domain-profile validation/OpenPipeStress fixture posture unchanged and future-gated. The product-target decision does not authorize implementation or execution of these domain-engine lanes. |

Additional preservation rules for every category:

- topology remains exactly 10 packages / 51 deliverables / 78 SOW rows / 10
  objectives until a governed amendment is accepted;
- lifecycle states, Checking Approval SHAs, dependencies, and ResponsibleParty
  fields do not change through this planning package;
- the six D-APP-81 `HISTORICAL_RELATION_UNKNOWN` relations remain untouched;
- existing remaining anchors persist, including Desktop packaged smoke,
  real-daemon replay, D-APP-89 facade retirement, D-APP-88/DEL-09-04 packaging
  residuals, DEL-09-05/06 release-preparation evidence, and DEL-10-01's
  governed-next-capability/PEC residuals.

## 6. Proposed domain-first work order

This sequence is a proposed governance and evidence order. No implementation
step is authorized by this return.

### Phase A — owner gates before source change

1. **Fan in the six-lane D-APP-87 derivative package.** Present architecture
   alternatives from the separate UI/packaging lane together with this App
   client/work-order analysis. Do not silently select an implementation form.
2. **App owner product/architecture gate.** Rule the common requirements,
   standalone requirements, per-domain requirements, architecture form, and
   whether package identities/config/resource boundaries are accepted,
   amended, deferred, or declined.
3. **Product-basis gate.** If approved, route exact PRD changes through the App
   authority-corpus/reconciliation process. The adopted two-target/domain-first
   ruling is planning authority today; the current PRD has not yet been amended
   to make it implemented product truth.
4. **Scope/decomposition gate.** Determine through the owning App instrument
   whether the existing 10/51/78/10 topology needs wording/mapping amendments.
   Apply only accepted candidate amendments; do not create deliverables or
   treat the impact inventory as an amendment.
5. **Foreign-input gate.** Obtain the Piping runtime-surface response required
   for the full consumer set and exact PEC/domain-loop statements needed for
   any per-domain target/profile/client dependency. A foreign loop must act
   through its own instruments.
6. **Root gate.** Require Root disposition of `TM-ROOT-105`, `TM-ROOT-107`,
   and `TM-ROOT-109`, plus a response to or bounded handling of the routed
   D-APP-88 graceful-stop investigation, before any App work depends on generic
   runtime, sandbox, identity, version, resume, Bash, or graceful-drain
   semantics.
7. **Deliverable activation gate.** The App owner/WORKING_ITEMS flow approves
   exact amended deliverables, write scopes, serialized overlaps, acceptance
   checks, and predecessor evidence. D-APP-89 landing and facade retirement
   remain separate gates.

### Phase B — implementation only after Phase A acceptance

8. **Domain-first vertical slice.** Make the first user-visible target slice
   the per-domain control plane: ruled domain config/profile, typed-agent
   entry, structured information, governed workflow/decision gates, App client
   binding, and source/UI evidence. Common prerequisites may precede it only
   when the selected architecture requires them; this does not authorize
   domain-operation apply or generic runtime work.
9. **Domain target package/client proof.** Produce the ruled per-domain artifact
   and collect source, UI, packaged, runtime-client, boundary, and negative
   evidence before claiming the target exists.
10. **Standalone preservation/extension.** Apply common changes to Desktop,
    close its named packaged/replay residuals, and prove all legacy and broad
    Woven/Workbench/Pipeline behavior remains intact.
11. **Cross-target convergence.** Run the common suite plus both target suites
    against the same accepted source snapshot; record target-specific skips,
    limitations, identities/config, and package hashes. Neither target may
    borrow the other's evidence.
12. **Independent review and Git/release gates.** REVIEW/EVALUATION inspect
    authority, semantic ownership, accessibility, compatibility, security,
    packaging, and evidence sufficiency. CHANGE handles Git only after
    acceptance. Signing, notarization, publication, distribution, lifecycle
    transition, and release remain separately ruled.

This ordering is domain-first because the per-domain product vertical and its
owner-gated evidence precede Desktop convergence, while common prerequisites
are kept to the minimum required by the subsequently selected architecture.

## 7. Validation matrix

Each evidence record must bind the command/check, source revision or explicit
dirty snapshot, target, configuration/resources, affected paths, result,
artifact path/hash where applicable, skips, limitations, and human/Root gate
state. Generated evidence remains derivative.

| Layer | Common evidence required | Standalone Desktop evidence | Per-domain control-plane evidence |
|---|---|---|---|
| Source topology | Frozen manifest of shared and target-specific paths; import/dependency census; no unruled facade reliance; target-config schema/fixture checks; `git diff --check`; no unauthorized runtime/foreign changes. | Current route/Electron/packaging paths preserved; direct Root-contract imports after D-APP-89 landing; facade rollback probes remain until retirement. | Ruled domain config/profile resolves deterministically; unknown/unruled profile fails; no filesystem discovery; no operation-apply/protected-write path introduced. |
| Source contract | Typecheck; common App client/API/UI contract tests; no provider/SDK shape leakage into App public contract. | Desktop request/project/persona/mode/options binding and legacy route/query/alias fixtures. | Domain/project/target attribution, typed-agent/workflow config, and cross-domain isolation fixtures. |
| UI component | D-APP-36 component/render tests for user-facing controls, disabled/active/error/loading/stale/unknown/read-only states; accessibility keyboard/focus/resize checks. | Woven Dialogue, Workbench, Pipeline, working-root, credentials/runtime feedback, legacy deep links, and broad Desktop states. | Domain-focused entry, structured information, workflow and decision gates, profile/domain labels, unsupported-operation disabled states, and professional-boundary copy. |
| UI high-risk browser/manual | Browser evidence where viewport/layout/overlap/interaction risk is high; primary dialogue remains mounted; selected replay is observational. | Desktop target viewports, navigator/coordination/activity regions, guarded selection, return focus, and legacy compatibility. | Domain target viewports, target/domain identity visibility, focused navigation, decision-gate clarity, and no accidental Desktop-only control exposure. |
| Build | Common test/type/build prerequisites and target-source manifest binding. | `npm run build` under the ruled Desktop configuration. | Ruled domain-target build command/configuration; exact command remains `TBD` until architecture/package decision. |
| Packaged common | Instruction-root integrity, packaged dependency boundary, artifact path/hash, source revision, unsigned/unnotarized state, resource/config provenance, secret/network review. | `desktop:pack`/`desktop:dist` evidence for macOS arm64 Chirality artifact and DMG under current posture. | Package/layout proof for the ruled domain target, distinct target/config/resource identity, launch smoke, and source-aligned artifact. A Desktop-only package cannot prove this row. |
| Package lifecycle | Clean launch/quit/relaunch, connectivity feedback, no stale socket/process/job/temp/token residue, and package-to-source parity. | GUI contact plus graceful stop/restart and recovery; retain the current D-APP-88 blocker until an accepted proof exists. | Equivalent lifecycle proof with an active domain client; include client connection/drain observations required by the accepted Root contract. |
| Runtime-client contract | Focused App conformance tests for direct Root contracts, typed errors, stable API/SSE/UI projection, terminal events, redaction, policy-input handoff, and target-labelled evidence. | Session CRUD/boot/turn/interrupt/cancel/reconnect from Desktop; real-daemon transcript rendering; same-session Desktop/CLI replay. | Same client operations from the domain target; correct project/domain binding; no cross-target/session leakage; unsupported domain execution denied. |
| Runtime generic negative | Evidence that the App did not define or mutate generic runtime, sandbox, identity, version, resume, or Bash semantics; record Root contract/version consumed only after Root acceptance. | Same. | Same. |
| Security/claims | Redaction, no project secrets, current ruled endpoint policy, no professional/release/solver-truth claims, and protected-path preservation. | Current Desktop `safeStorage`/renderer/client posture. | No new provider/network endpoint or protected-domain write follows from the domain target; explicit boundary notices remain visible. |
| Cross-target acceptance | Common evidence is counted once only when target-independent; a coverage map identifies every common and per-target requirement. | All Desktop-only requirements pass or have explicit owner-approved residuals. | All domain-only requirements pass or have explicit owner-approved residuals. |

Minimum package/runtime negative regression from D-APP-88: do not count a
fresh-helper graceful stop as proof of post-GUI behavior; preserve signal,
process-survival, socket, connection, cleanup, and terminal-log evidence for
the actual active-client arm required by the accepted Root/App contract.

Minimum import/retirement regression from D-APP-89: after landing, repeat the
zero-ordinary-consumer and config/build census on the landed tree. Keep all 13
facade exports and rollback identity probes until a later owner retirement
decision; deletion is not part of dual-target implementation by implication.

## 8. `BLOCKED_BY_ROOT` register

| Lane | State | Current trace | What App may do now | What App may not do |
|---|---|---|---|---|
| Generic runtime contract | `BLOCKED_BY_ROOT` | D-APP-87 ruling/packet; SCA-APP-005 boundary; Root response `TM-ROOT-105` deferred and `TM-ROOT-107` open | State affected-client requirements and conformance needs for both targets. | Define, select, amend, or implement generic runtime semantics. |
| Sandbox | `BLOCKED_BY_ROOT` | Root response `TM-ROOT-105`: generic role/run-specific sandbox identity and native-tool semantics wait for the Piping response; `TM-ROOT-107` requires a ruled SCOPE_CHANGE reference | State target-visible denial/approval and evidence requirements. | Define sandbox model, capability inheritance, native-tool semantics, or grants. |
| Runtime/client identity | `BLOCKED_BY_ROOT` | D-APP-87 ruling; `TM-ROOT-105` identity semantics; `TM-ROOT-107` scope-change gate | Require each App evidence item to name product target/domain and consumed Root contract. | Define Root principal, token, session-owner, target-wire, or sandbox identity semantics. App package identity remains a separate App owner gate. |
| Version | `BLOCKED_BY_ROOT` | D-APP-87 ruling; Root response `TM-ROOT-109` deferred with the same Piping trigger and comparison-basis definitions kept local | Require source/package/config version evidence and report the accepted Root version when one exists. | Select generic compatibility/version-negotiation semantics or use local comparison prose as a Root contract. |
| Resume | `BLOCKED_BY_ROOT` | D-APP-87 ruling; SCA-APP-005 assigns generic session/persistence semantics to Root; `TM-ROOT-105`/`107` keep the generic contract unopened/unruled | Require both targets to prove client-visible resume/replay conformance after Root acceptance. | Define resume tokens, store authority, migration semantics, or cross-target session identity. |
| Bash | `BLOCKED_BY_ROOT` | D-APP-87 ruling/packet; Root response `TM-ROOT-105` native-tool/sandbox lane; no current notice grants Bash | Preserve App/project deny/human-gate requirements and negative evidence. | Grant, expose, implement, or infer Bash from target choice or domain-first delivery. |
| Graceful connection drain/stop | `BLOCKED_BY_ROOT` for Root semantics; App diagnostic seam also open | Routed 2026-08-03 graceful-stop investigation; D-APP-88 R2 `BLOCKED/PARTIAL` handoff | Preserve exact failure evidence and request Root reproduction/disproof; later prove App client behavior against accepted semantics. | Treat the Unix-socket/SSE hypothesis as cause, accept helper packaging, or weaken the post-GUI evidence conjunct. |

The Root response leaves `TM-ROOT-105`, `TM-ROOT-107`, and `TM-ROOT-109`
open/deferred behind Root instruments and the Piping response. The D-APP-88
notice adds an investigation request and `TM-CANDIDATE`; it does not show that
Root has accepted a row, cause, or remediation.

## 9. Later owner and foreign-loop gates

| Gate owner | Required later act |
|---|---|
| App owner | Rule the six-lane owner proposal, architecture form, common/per-target requirements, and domain-first acceptance order. |
| App product authority / reconciliation | Amend PRD and regenerate/reconcile the authority corpus if the owner adopts exact product-basis changes. |
| App SCOPE_CHANGE / decomposition owner | Determine and rule exact 10/51/78/10 wording/mapping amendments; preserve topology unless explicitly changed through the governed protocol. |
| App packaging identity owner | Rule domain-target artifact topology, `appId`/bundle/product naming, configuration/resource boundary, signing/notarization/publication posture, and whether any helper is shared or target-specific. |
| Root runtime owner | Disposition `TM-ROOT-105`, `TM-ROOT-107`, `TM-ROOT-109`; accept/amend/decline the generic contract and the graceful-stop investigation through Root instruments; return exact contract/source/test evidence. |
| Piping loop | Record the runtime-surface response needed by the full consumer set; App cannot stand in for it. |
| PEC / applicable domain loop | State the per-domain client/profile needs and govern any PEC/profile/protected-path/operation change through its own instruments. A domain target alone grants no domain operation authority. |
| WORKING_ITEMS | Activate exact deliverables and serialize overlapping UI/runtime/packaging writes only after accepted product/decomposition gates. |
| REVIEW / EVALUATION | Independently assess semantic ownership, authority boundaries, accessibility, compatibility, security, package/source parity, per-target evidence, and unresolved blockers. |
| CHANGE | Perform Git fan-in only after acceptance. D-APP-89 landing precedes a fresh census; facade retirement requires the later owner gate. |
| Release authority | Separately rule lifecycle, signing, notarization, publication, distribution, and release. Current evidence remains local unsigned/unnotarized support only. |

## 10. Remaining gaps

- Exact architecture form and source/package boundary: `TBD — OWNER GATE`.
- Exact per-domain product artifact, bundle/product identity, configuration and
  resource boundary, launch command, and validation command: `TBD — APP OWNER
  GATE`.
- Exact domain application/profile requirements beyond the currently ruled
  closed `open_pipe_stress` and `pec` registry: `TBD — DOMAIN/APP GATE`.
- Full consumer-set runtime surface requirements: pending the Piping response.
- Generic runtime, sandbox, runtime identity, version, resume, and Bash
  semantics: `BLOCKED_BY_ROOT`.
- D-APP-88 active-client graceful-stop cause and accepted behavior: unknown;
  routed for Root reproduction or disproof.
- D-APP-89 landed-tree status and facade retirement: migration candidate is
  validated but not yet landed/retired by the frozen evidence.
- Exact deliverable amendment text, owners, write tranches, estimates, and
  schedule: not selected by this planning return.
- Release matrix beyond current macOS 15+ arm64 unsigned/unnotarized local
  evidence, including signing/notarization/publication: unselected and
  separately governed.

## 11. Final return

`PASS_FOR_DERIVATIVE_OWNER_PROPOSAL`: the App can now fan this runtime,
work-order, and validation analysis into the D-APP-87 owner proposal. The
proposal must carry the `BLOCKED_BY_ROOT` register, the D-APP-89
migration-without-retirement boundary, the D-APP-88 blocked/rollback boundary,
the 35-deliverable partition, domain-first pre-implementation gates, and the
common-plus-two-target evidence matrix.

`NOT_READY_FOR_IMPLEMENTATION`: no architecture, generic contract, deliverable
amendment, source write, package identity, runtime semantic, foreign-loop act,
or release action is authorized or sufficiently decided by this return.
