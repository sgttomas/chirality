---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-06
package_id: PKG-02
decomposition_basis: projects/chirality-runtime/execution/_Decomposition/Chirality_Runtime_SOFTWARE_DECOMP_v1_0.md@1aadcc61b2739fdca25c4b07259655836516baa4
project_scope_refs: [SOW-104]
package_objective_refs: [OBJ-001, OBJ-002, OBJ-004, OBJ-007]
---

# Scope of Work — DEL-02-06

## Purpose and Objective Traceability

This contract defines Generic Runtime Stewardship and Release Assurance in
chirality-runtime, contributing SOW-104 to OBJ-001, OBJ-002, OBJ-004 and OBJ-007
in that project's accepted decomposition. It preserves the inherited contract's
52 requirements, outputs and evaluation obligations under the exact ownership
overlay at projects/chirality-runtime/execution/_Decomposition/OWNERSHIP_OVERLAY.md.
The carrier's Type is REQ_SLICE and Context Envelope is M.

Generic runtime product ownership, implementation assurance and release fan-in
belong to chirality-runtime and its accountable human when the recorded transfer
becomes effective. Root retains instruction governance, human ruling authority
and the D-GOV-20 architectural boundary; clients retain their own obligations.
Actual acceptance/application posture is recorded at
projects/chirality-runtime/execution/_Coordination/MIGRATION_APPLICATION.md.
This contract grants no activation, implementation, lifecycle or release act.

Historical semantic choices remain accepted as recorded in
projects/chirality-runtime/execution/_Decomposition/ACCEPTED_EVIDENCE_CONTINUITY.csv;
those source artifacts remain at their original Root paths and hashes.
Historical preparation descriptions and unresolved-item IDs below retain their
source-time meaning and are read with each exact later accepted disposition;
they do not undo accepted semantics or represent current implementation evidence.
The compatibility identity root-runtime-1 and epoch 1 remain unchanged.
The frozen compatibility JSON retains ten historical null/HELD_UNAVAILABLE markers:
nine bindings remain held, while the Tier-0 relationship was disposed separately
by R16-B as continue-separate. R18 closed TM-ROOT-122; TM-ROOT-106 remains open.
Relocation, initialization and validation release none of those nine holds.

The six evidence inputs from chirality-runtime::DEL-02-07 through
chirality-runtime::DEL-02-12 fan in under this carrier's local dependency
surface. No extra lifecycle maturity or ordering is inferred. The historical
no-edge observation in REQ-051 and VER-015 describes the inherited Root basis;
the accepted destination declaration is the six named fan-in inputs, with client
relationships non-gating coordination. REQ-027's first activation stays limited
to specification, read-only inventory, evidence-matrix design and planning.

## Deliverable Definition — Ontology

- **OUT-001** — Runtime semantic-change brief and declared write-locus record:
  one bounded-tranche statement of purpose, accepted basis, semantic change,
  exclusions, exact reads, exact writable targets, integration owner, affected
  surfaces, and return contract.
- **OUT-002** — Versioned compatibility-contract candidate: an exact
  runtime-project-owned compatibility identity, grammar, declaration and comparison
  point, mismatch result, epoch-change criteria, and binding record, or an
  explicit no-change record.
- **OUT-003** — Exact degraded-mode contract candidate: machine-readable
  failure classes, precedence, retryability, redaction, evidence fields,
  recovery and replay rules, and affected presentation mappings conforming to
  the common fail-closed floor.
- **OUT-004** — Actual affected-client census and boundary matrix: evidence for
  which accepted clients have an implementation or migration obligation for
  the exact runtime-project change, which are not affected, and which remain unresolved.
- **OUT-005** — Affected-client conformance or migration matrix: one
  client-owned result per actually affected client, with accepted client basis,
  exact obligation, evidence, gate status, and unresolved disposition.
- **OUT-006** — Proportionate runtime-project regression and semantic-evidence bundle:
  requirement-to-verification traceability, positive and negative cases,
  absence-of-fallback evidence, source/release bindings, and validation
  results.
- **OUT-007** — Cutover, rollback, recovery, and indeterminate-operation plan:
  exact preconditions, effective boundary, abort and restore path, replay
  prohibition or rule, partial-output treatment, and evidence-preservation
  method.
- **OUT-008** — Accountable-human release-disposition packet: exact candidate
  identities, evidence fan-in, open items, waivers or deferrals, notice state,
  rollback readiness, and explicit `ACCEPT`, `RETURN`, or `DEFER` choice.
- **OUT-009** — Activation and work-graph record: one versioned intra-package
  graph with Agent 2 briefs, edges, write ownership, fan-in gates, holds,
  escalation points, and telemetry disposition for the bounded tranche.

## Completion and Reliance Basis — Epistemology

### Grounded claims

- **CLM-001** — `SOW-104` assigns consequential generic-runtime semantics to a
  runtime-project-owned standing carrier with a declared runtime write locus and requires
  preservation of D-GOV-20 boundaries, versioned-contract evidence,
  affected-client conformance or migration, proportionate regression
  evidence, accountable-human release disposition, and no ownership transfer
  to App, PEC, or another client.
- **CLM-002** — D-GOV-20 establishes the generic executable runtime boundary; the approved
  ownership overlay locates its workspace at `projects/chirality-runtime/` and gives one opt-in per-user daemon exclusive ownership of
  engines, credentials, sessions, delegation, tools, turn locks,
  interruption, and local-model residency while checkout-contained files
  retain project authority.
- **CLM-003** — D-GOV-20 authorizes authenticated project-scoped HTTP/1.1 over
  a protected Unix-domain socket and authorizes no TCP control listener,
  automatic model scheduling or fallback, multiple simultaneous primary local
  models, or release/publication/issuance.
- **CLM-004** — D-GOV-28 adopts O-11 and preserves separate gates for
  decomposition, write-locus creation, runtime implementation, App and PEC
  scope, contract repinning, lifecycle, release, and reliance.
- **CLM-005** — At the inherited Root repository basis, that source deliverable's
  `_STATUS.md` is `OPEN`, its live `ScopeOfWork.md` is absent, and its
  anticipated write locus is a planning note rather than authorization.

- **CLM-006** — Root owns shared instruction governance and human ruling authority;
  the runtime project and its accountable human own generic product implementation,
  semantic identity, evidence, and release fan-in. The daemon owns credentials,
  engines, sessions, delegation, tools, locks, interruption and residency as in
  CLM-002. Each client or project/domain adapter owns its project-specific acts
  and conformance; App owns its UI/hosting boundary, PEC owns PEC mutation,
  Piping owns Piping execution, and Tier-0 owns Flow-A coordination. Separate
  named human gates govern exclusions rather than transferring those acts here.

### Root compatibility constraints admitted by SE-A

- **REQ-001** — The generic runtime compatibility identity shall denote one
  compatibility epoch of consequential generic daemon/client contract
  semantics.
- **REQ-002** — The compatibility identity shall not be inferred from or
  equated with the route namespace, npm package version, runtime fingerprint,
  source commit, release commit or distributable identity, or Tier-0 Flow-A
  identity. Any relationship requires an exact accepted record.
- **REQ-003** — The runtime project shall own the identity and its semantic definition
  under the approved ownership overlay to O-11. A Tier-0 relationship act may coordinate Flow-A but shall not transfer
  ownership of generic runtime semantics.
- **REQ-004** — Before a consequential runtime-dependent operation, an
  affected client shall obtain the daemon's declared compatibility identity
  and compare it by exact equality with the identity accepted by that client's
  contract basis.
- **REQ-005** — A mismatch shall stop the consequential operation with a
  distinct typed incompatibility result and shall not silently downgrade,
  select another runtime loop, daemon, model, or transport, or infer
  compatibility from transport success or another version-like label.
- **REQ-006** — Range negotiation, downgrade, and concurrent multi-version
  support shall remain unsupported unless exact evidence and a later owner act
  authorize them.
- **REQ-007** — The compatibility binding record shall connect the exact
  identity to exact contract bytes, source and release identities, affected
  clients and accepted bases, migration or conformance evidence,
  proportionate regression evidence, and accountable-human release
  disposition.
- **REQ-008** — Changing the compatibility identity shall require a
  consequential runtime-project tranche under this deliverable, client-impact
  determination, separately governed affected-client conformance or
  migration, regression evidence, and a separate accountable-human release
  disposition.
- **REQ-009** — A client shall be classified as affected only when it has an
  accepted implementation or migration obligation for the exact runtime-project change.
  Naming a prospective client shall not create work, a closure veto, or a PEC
  obligation.

### Common fail-closed constraints admitted by SE-A

- **REQ-010** — Before consequential runtime-dependent work begins, the client
  shall separately establish usable client-local configuration and
  project-scoped access material, accepted current project registration,
  authorization for the requested project and operation, every required
  project adapter, reachable authorized runtime transport, and compatible
  client/daemon contract identity. The daemon shall separately establish the
  required runtime-owned credentials, engines, sessions, delegation, tools,
  turn locks, interruption, and model-residency readiness without transferring
  custody or ownership to a client.
- **REQ-011** — Failure of any required precondition shall fail the affected
  runtime-dependent operation closed and shall not authorize another runtime
  loop, daemon, model, protocol version, or transport.
- **REQ-012** — Reconnect or rebind to a daemon that passes every precondition
  shall be recovery, not fallback, and shall not silently replay a
  consequential operation whose completion is unknown.
- **REQ-013** — File-native governance and separately owned project functions
  may remain usable but shall not be characterized as an alternate agent
  runtime. Every retained-function claim shall be named and proven by its
  owning client.
- **REQ-014** — The machine-readable failure class shall survive adapter and
  presentation layers; simplified wording shall not erase the class needed for
  recovery, evidence, or support.
- **REQ-015** — The runtime project shall define the generic floor. Each actually affected
  client shall own its client-specific retained-function, presentation,
  migration, and conformance evidence under its own accepted scope and gates.
- **REQ-016** — PEC v2 shall receive no obligation until a separate PEC gate
  establishes an active accepted v2 carrier and an exact affected operation.
  Frozen PEC v0.4 shall remain reference evidence only. Boundary-owner allocation: CLM-006.

### Semantic failure conditions admitted by SE-A

- **REQ-017** — Client-configuration or project-access failure shall prevent
  sending the consequential request and shall not be reported merely as socket
  absence; repair remains with the owning client or project authority.
- **REQ-018** — Runtime credential-readiness failure shall reject the affected
  operation without transferring daemon credential custody or repair authority
  to the client.
- **REQ-019** — Project lookup, identity, manifest currency, registration, or
  enabled-adapter failure shall prevent a project runtime operation until
  separately authorized registration or re-registration succeeds.
- **REQ-020** — Project-scoped identity, required-scope, or operation-
  authorization failure shall prevent the operation, remain distinct from
  provider authentication, and never broaden authority automatically.
- **REQ-021** — Required project-adapter unavailability, lack of authority, or
  protocol inconsistency shall block only operations requiring that adapter;
  generic transport shall acquire no project authority.
- **REQ-022** — Authorized Unix-socket transport failure shall fail the
  runtime-dependent operation closed with no TCP or in-process fallback;
  reconnect or rebind shall rerun all preconditions.
- **REQ-023** — Compatibility mismatch shall reject before consequential work
  with no downgrade or range inference; recovery shall require an accepted
  compatible pair and a new bind.
- **REQ-024** — Malformed or contract-invalid wire behavior shall fail closed
  as a truthful protocol class and shall not be silently recast as transport
  absence.
- **REQ-025** — Provider, engine, or model failure after transport and project
  boundaries pass shall preserve the execution-domain cause and shall not be
  recast as daemon absence.
- **REQ-026** — Failure to establish or truthfully resume required session,
  delegation, tool, turn-lock, interruption, or model-residency state shall
  reject or halt only the affected operation and shall not invent completion,
  replay, authority, or alternate runtime state.

### Tranche, authority, evidence, and boundary requirements

- **REQ-027** — The first activation shall use Context Envelope M and shall be
  limited to exact specification, read-only consumer inventory,
  evidence-matrix design, and change planning. It shall not write
  implementation bytes. Boundary-owner allocation: CLM-006.
- **REQ-028** — Every activation shall bind a current accepted repository
  basis, the accepted decomposition pin, the accepted Scope-of-Work hash,
  owner-gate identities, exact read paths, exact writable targets, explicit
  exclusions, and a return contract before dispatch.
- **REQ-029** — Initial-activation writes shall be confined to the
  deliverable-local run root declared in Praxeology. No activation may infer
  write authority from the decomposition's anticipated locus.
- **REQ-030** — The work graph shall version nodes, dependencies,
  concurrency, integration ownership, fan-in gates, holds, retries,
  escalation points, and returns. Agent 2 nodes shall not delegate.
- **REQ-031** — Actual affected clients shall be established from accepted
  implementation or migration obligations, not from prospect names,
  historical references, shared route labels, or transport reachability.
- **REQ-032** — App, PEC, Tier-0, Piping, and any other client or coordination
  surface shall remain under its own authority. Client writes require
  separately accepted client-owned tranches; Tier-0 coordination cannot amend
  generic runtime semantics. Boundary-owner allocation: CLM-006.
- **REQ-033** — Every semantic requirement shall trace to positive,
  negative, and where applicable adversarial evidence; the evidence matrix
  shall distinguish deterministic fact, human judgment, client-owned evidence,
  and unresolved fields.
- **REQ-034** — Cutover and rollback shall bind exact pre-change and
  post-change identities, preserve file-native evidence, stop on failed
  preconditions, avoid silent replay, and require a separately authorized Git
  or deployment act.
- **REQ-035** — Consequential implementation, client migration, contract
  repinning, lifecycle transition, public export, release, publication,
  issuance, and professional reliance shall each remain behind their named
  later human gate. Boundary-owner allocation: CLM-006.
- **REQ-036** — Every unresolved field listed below shall remain unresolved
  until its owning later gate accepts exact bytes and evidence; no test,
  candidate, version-like label, or implementation behavior shall answer it by
  implication.
- **REQ-037** — Final release fan-in shall include exact compatibility and
  degraded-mode contracts, actual affected-client disposition, runtime-project regression
  evidence, accepted affected-client evidence, Tier-0 relationship
  disposition, notice state, rollback and indeterminate-operation treatment,
  and accountable-human release disposition.
- **REQ-038** — Any basis or relied-source drift shall block application or
  activation until source identities, absence checks, affected-client census,
  next-free external IDs where applicable, and validation are rerun and
  material drift is returned to the owner.
- **REQ-039** — Runtime user-data state, engines, credentials, sessions, and
  caches shall remain operational and non-authoritative; accepted project
  truth and acceptance evidence shall remain checkout-contained.
- **REQ-040** — Public export may include generic runtime, CLI, contracts, and
  safe adapters only after applicable gates and evidence pass; credentials,
  machine state, downloaded models, and private project adapters or evidence
  shall remain excluded. Boundary-owner allocation: CLM-006.
- **REQ-041** — Electron daemon mode shall preserve the existing packaged-App
  identity and encrypted `safeStorage` credential boundary as single-owner;
  no client tranche may repartition credential custody by implication. Boundary-owner allocation: CLM-006.
- **REQ-042** — Tracked project manifests shall remain secret-free and free of
  machine-specific absolute paths; authority-affecting manifest changes shall
  require explicit re-registration and shall not be inferred from local
  registration state.
- **REQ-043** — Agent 0, Agent 1, and Agent 2 shall remain authority and
  responsibility contracts independent of engine or model; Agent 2 shall not
  delegate, and actual model attribution shall not become durable role
  doctrine. Boundary-owner allocation: CLM-006.
- **REQ-044** — Local-model activation shall remain explicit with no automatic
  load, unload, switch, alias, or fallback; residency transitions shall remain
  evidence-bearing and epoch-bound, and unknown helper models shall not be
  unloaded automatically. Boundary-owner allocation: CLM-006.
- **REQ-045** — Runtime evidence shall retain actual engine, provider, model,
  and residency attribution when exposed without making those values
  authority; missing attribution shall be reported rather than invented.
- **REQ-046** — Project-specific tools and deterministic acts shall remain
  owned by their project or domain adapters and shall not acquire or transfer
  authority through generic transport. Boundary-owner allocation: CLM-006.
- **REQ-047** — No tranche under this contract shall silently authorize
  automatic model scheduling, multiple simultaneous primary local models,
  local Agent 1, piping execution, silent adapter fallback, remote oMLX,
  credential entry through an unauthorized CLI surface, production PEC
  mutation, or release, publication, or issuance. Boundary-owner allocation: CLM-006.
- **REQ-048** — A runtime-project client and CLI conformance matrix shall prove that
  client configuration, project access, and daemon credential readiness are
  not conflated with transport absence; registration and authorization remain
  distinct; mismatch stops before consequential work; no TCP, alternate
  daemon, downgrade, alternate model, or automatic replay occurs; and every
  retained local-only command, exact exit behavior, and exact machine-readable
  behavior is individually accepted.
- **REQ-049** — An actually affected App matrix shall classify every surface
  as runtime-dependent, retained read-only, retained read/write, or not
  applicable; stop agent and session work on failed preconditions; preserve
  truthful classes through adapter and UI; prevent silent resend; distinguish
  intervention-required from transient states; name and test retained
  surfaces; and preserve the accepted SCA-APP-005 authority partition.
- **REQ-050** — If PEC v2 later becomes actually affected, its matrix shall
  prove that every applicable condition stops the exact operation, no
  independent PEC runtime loop starts, failed work does not silently mutate
  accepted PEC truth, PEC optionality does not become a Root correctness
  dependency, and retained functions derive from current v2 authority rather
  than frozen v0.4. Boundary-owner allocation: CLM-006.
- **REQ-051** — The inherited Root deliverable-local dependency surface at its source basis
  declares no upstream or downstream edge. Later gate prerequisites in this
  contract shall not become dependency truth unless separately added through
  the owning dependency workflow.
- **REQ-052** — The accepted Root basis contains no project-local
  `software-workflow.json`. The first candidate-only activation shall use
  bounded ephemeral Agent 2 generalists plus explicitly permitted deterministic
  Scope-of-Work tools only; any later software-check or implementation
  activation shall remain held until it identifies a lawful project-local
  profile and exact authorized checks.

### Stable unresolved-item register

- **TBD-001** — `OD6-OPEN-001` (`PROPOSED`): exact Root compatibility identity value and
  permitted grammar.
- **TBD-002** — `OD6-OPEN-002` (`PROPOSED`): exact declaration, handshake or preflight
  location, and comparison behavior.
- **TBD-003** — `OD6-OPEN-003` (`PROPOSED`): exact compatibility-mismatch identifier,
  response envelope, and presentation mapping.
- **TBD-004** — `OD6-OPEN-004` (`OPEN`): exact compatibility binding of contract bytes,
  source identity, release identity, clients, evidence, and disposition.
- **TBD-005** — `OD6-OPEN-005` (`OPEN`): evidence-backed actual affected-client census.
- **TBD-006** — `OD6-OPEN-006` (`PROPOSED`): exact cutover, migration, rollback, replay,
  partial-output, and indeterminate-completion behavior.
- **TBD-007** — `OD6-OPEN-007` (`PROPOSED`): exact configuration, registration,
  authorization, adapter, transport, mismatch, protocol, and execution
  identifiers and envelopes.
- **TBD-008** — `OD6-OPEN-008` (`PROPOSED`): exact failure precedence, retryability,
  retry timing, redaction, and evidence fields.
- **TBD-009** — `OD6-OPEN-009` (`OPEN`): client-specific retained-function matrices and
  accepted proof.
- **TBD-010** — `OD6-OPEN-010` (`PROPOSED`; current disposition `PREPARATION_SELECTED_NOT_ADOPTED`): durable Tier-0 Flow-A relationship act. The
  owner has selected preparation of a CONTINUE-SEPARATE candidate only; no
  Tier-0 record is adopted by this contract.
- **TBD-011** — `OD6-OPEN-011` (`OPEN`): PEC v2 applicability, active carrier, exact
  affected operation, and current evidence.
- **TBD-012** — `OD6-OPEN-012` (`OPEN`): any uncovered ownership seam, returned as a
  source-cited proposal rather than implementation inference.
- **TBD-013** — `OD6-OPEN-013` (`OPEN`): Piping consumer status; it remains metadata-only
  and non-client unless new evidence proves actual generic runtime consumption.
- **TBD-014** — `OD6-OPEN-014` (`PROPOSED`): exact semantic conformance and proportionate
  regression matrix.
- **TBD-015** — `OD6-OPEN-015` (`PROPOSED`): exact criteria for changes that require a new
  compatibility epoch and changes that do not.
- **TBD-016** — `OD6-OPEN-016` (`PROPOSED`): exact daemon operational-state subclasses,
  precedence, resumability, indeterminate completion, and evidence fields.

### Acceptance criteria

- **AC-001** — The runtime change brief binds the exact accepted bases, owner gates, declared reads, declared writes, exclusions, integration owner, tranche envelope, and return contract; no anticipated locus is treated as authorization.
- **AC-002** — The compatibility-contract candidate satisfies every generic runtime identity constraint in this contract, answers only fields explicitly accepted by a later gate, and proves rejection before consequential work for mismatch.
- **AC-003** — The degraded-mode candidate preserves all ten semantic failure conditions, their required distinctions, fail-closed behavior, no-fallback posture, recovery/replay boundary, and presentation-layer class.
- **AC-004** — The affected-client census cites an accepted implementation or migration obligation for every `AFFECTED` classification and records `NOT_AFFECTED`, `PROSPECTIVE_ONLY`, or `UNRESOLVED` without creating work or a closure veto.
- **AC-005** — Every actually affected client has a separately accepted conformance or migration result, or an explicit owner disposition that prevents release reliance on missing evidence.
- **AC-006** — The runtime-project evidence bundle maps every applicable requirement to positive, negative, and adversarial evidence, identifies evidence owner and basis, and reports all failures without weakening the criterion.
- **AC-007** — The cutover and rollback plan binds exact before/after identities, has a tested abort/restore path, preserves evidence, and never silently replays an operation with unknown completion.
- **AC-008** — The release-disposition packet contains the complete required fan-in, preserves every unresolved item or accepted disposition, and leaves the release act to an accountable human.
- **AC-009** — The activation record contains a valid bounded work graph, sealed Agent 2 briefs, disjoint or serialized writes, accepted predecessor gates, retry history, telemetry limitations, and a truthful handoff.
- **AC-010** — No candidate, activation, tool, test, or implementation changes `_STATUS.md`, activates the deliverable, writes `projects/chirality-runtime/`, changes App, PEC, Piping, or Tier-0, repins a contract, or performs a release without the exact later gate that owns that effect.
- **AC-011** — All sixteen stable unresolved items remain one-to-one traceable to their OD6 open-item identities until exact later dispositions are accepted; no unresolved field is silently dropped.
- **AC-012** — Runtime operational state remains non-authoritative, checkout-contained evidence remains sufficient for governance continuity, and retained file-native functions are claimed only where individually proven.
- **AC-013** — The clean Scope-of-Work contract validates as `SOW_V1`, binds `SOW-104` and all four declared objectives, and contains no machine-absolute path, migration-only marker, lifecycle claim, or authority effect.
- **AC-014** — The runtime-project contract and every activation preserve all D-GOV-20 architecture, residency, authority, adapter-ownership, actual-model-attribution, exclusion, and implementation-gate boundaries, with every deviation returned for an exact owner ruling.
- **AC-015** — Runtime-project CLI, App, and conditional PEC proof obligations are present only for actually affected operations, retain their required semantic distinctions, and remain under separately accepted client and runtime-project gates.
- **AC-016** — The first activation records the absence of a Root software-workflow profile, uses only bounded ephemeral Agent 2 generalists and explicitly permitted deterministic Scope-of-Work checks, creates no undeclared dependency, and performs no implementation or unregistered software check.

## Production and Verification Method — Praxeology

### Accepted read basis and exact first-activation read scope

Before dispatch, the first activation shall reproduce the repository basis,
the accepted decomposition pin, the accepted Scope-of-Work hash, and the owner
gate hashes. Its read scope is limited to:

1. this deliverable's accepted clean `ScopeOfWork.md`, `_CONTEXT.md`,
   `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_SEMANTIC.md`;
2. `projects/chirality-runtime/execution/_Decomposition/Chirality_Runtime_SOFTWARE_DECOMP_v1_0.md`,
   its scope, objective, deliverable and trace companions,
   `projects/chirality-runtime/execution/_Decomposition/_AUTHORITY.md`,
   `projects/chirality-runtime/execution/_Decomposition/OWNERSHIP_OVERLAY.md`,
   `projects/chirality-runtime/execution/_Coordination/MIGRATION_APPLICATION.md`,
   and the historical `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`
   with its scope, objective, deliverable, forward-trace, reverse-trace and telemetry
   companions;
3. `docs/PRD_ROOT.md`,
   `docs/governance_harness/_DECISIONS/D-GOV-20_shared_runtime_local_agent_pilot.md`,
   `docs/governance_harness/_DECISIONS/D-GOV-28_root_runtime_stewardship.md`,
   and the following hash-verified copies under the declared RunID root:
   `accepted_inputs/CANDIDATE_SET_MANIFEST.sha256`,
   `accepted_inputs/ROOT_COMPATIBILITY_POLICY_CANDIDATE.md`,
   `accepted_inputs/DEGRADED_MODE_CONTRACT_CANDIDATE.md`,
   `accepted_inputs/OPEN_ITEMS.csv`, `accepted_inputs/OWNER_SELECTION.md`, and
   `accepted_inputs/OWNER_GATE.md`;
4. `projects/chirality-runtime/packages/contracts/src/protocol.ts`,
   `projects/chirality-runtime/packages/contracts/src/errors.ts`,
   `projects/chirality-runtime/packages/client/src/client.ts`, and
   `projects/chirality-runtime/packages/cli/src/cli.ts`, read-only, for current-state inventory;
5. `_DomainEngines/_DECISIONS/D-T0-07_contract_versioning.md`,
   `_DomainEngines/_DECISIONS/D-T0-09_flow_a_contract_version_value.md`,
   `_DomainEngines/_DECISIONS/D-T0-23_shared_runtime_domain_convergence.md`,
   `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-005_2026-07-26_2334_Root_Runtime_Client_Boundary/RUN_SUMMARY.md`,
   `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`,
   `projects/pec/AGENTS.md`,
   `projects/pec/execution/_Decomposition/Deliverables.csv`, and
   `projects/pec/execution/_Decomposition/ScopeLedger.csv`, read-only, solely
   to classify actual obligations or coordination effects; and
6. `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md`,
   `agents/AGENT_WORKING_ITEMS.md`, `agents/AGENT_TASK.md`,
   `skills/scope-of-work/SKILL.md`,
   `skills/scope-of-work/BRIEF_SCHEMA.md`,
   `skills/scope-of-work/TOOL_POLICY.md`,
   `skills/scope-of-work/QA_CHECKS.md`,
   `tools/scope_of_work/validate_scope_of_work.py`, and
   `tools/scope_of_work/derive_review_checklist.py`; and
7. predecessor artifacts under the declared RunID root only after their node
   return has passed its stated fan-in gate.

Any additional read path requires a versioned brief amendment. A read does not
grant write authority or turn a prospective client into an affected client.

### Exact first-activation write scope

The first activation shall use RunID
`DEL-02-06-RUNTIME-SPEC-001`. Its sole writable root, including telemetry, is:

`projects/chirality-runtime/execution/PKG-02_Runtime_Product/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-RUNTIME-SPEC-001/`

Permitted artifacts under that root are the accepted-input copies, activation record, work graph,
sealed child briefs and returns, basis report, exact-contract candidates,
consumer census, evidence matrices, cutover/rollback candidate, validation
reports, review findings, open-item disposition map, telemetry summary, and
handoff. The activation shall not overwrite a pre-existing RunID root.

The following remain read-only and excluded from the first activation:
`ScopeOfWork.md`, `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`,
`_DEPENDENCIES.md`, `_SEMANTIC.md`, all decomposition and governance files,
`projects/chirality-runtime/**` except solely the already declared
`projects/chirality-runtime/execution/PKG-02_Runtime_Product/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-RUNTIME-SPEC-001/`
run root and its already enumerated permitted artifacts; `agents/**`, `skills/**`,
`tools/**`, App, PEC, Piping, Tier-0, and all product or release files remain
excluded. This exception permits no runtime code, metadata, production contract,
client or release write. No client-owned write may be added by brief
amendment; it requires a separate client-owned tranche.

### Required work graph and Agent 2 tasks

The first activation uses `MIXED` posture under one WORKING_ITEMS Agent 1 for
PKG-02 narrowed to this deliverable. The frozen graph is:

```text
N0 basis/currency proof
  ├─> N1 current-contract and identity inventory ─┐
  ├─> N2 read-only affected-client census ────────┼─> N4 exact semantic candidate integration
  └─> N3 evidence and rollback matrix design ─────┘
                                                   └─> N5 fresh read-only adversarial verification
                                                         └─> N6 owner-gate handoff
```

N0 failure holds N1 through N6. N1, N2, and N3 may run concurrently because
their writes are disjoint subdirectories under the run root. N4 is the sole
integration owner for exact-contract candidates. N5 is fresh and read-only on
N4 outputs; it shall not repair them. N6 proceeds only after accepted N0
through N5 returns.

Required Agent 2 briefs:

| Node | Agent 2 form | One objective | Allowed tools | Write target | Required return |
|---|---|---|---|---|---|
| N0 | Bounded ephemeral Agent 2 generalist | Reproduce basis, source hashes, absence checks, lifecycle, profile absence, dependency truth, and write containment | Bounded file read/write plus the two exact Python tools named in read item 6; no Bash or network | `basis/` | Machine-readable pass/fail report with drift blockers |
| N1 | Bounded ephemeral Agent 2 generalist | Inventory current identities, declarations, error classes, transports, and failure behavior without selecting replacements | Bounded file read/write only; no Bash or network | `inventory/` | Source-cited current-state matrix and contradiction list |
| N2 | Bounded ephemeral Agent 2 generalist | Classify actual clients from accepted implementation or migration obligations | Bounded file read/write only; no Bash or network | `clients/` | Evidence-cited census using only allowed classifications |
| N3 | Bounded ephemeral Agent 2 generalist | Design requirement, negative-case, regression, rollback, replay, and retained-function evidence matrices | Bounded file read/write only; no Bash or network | `evidence/` | Complete candidate matrices with owner and gate columns |
| N4 | Bounded ephemeral Agent 2 generalist, serialized integration owner | Assemble exact compatibility and degraded-mode candidates from accepted predecessor evidence without implementation | Bounded file read/write only; no Bash or network | `integration/` | Exact candidates, open-item map, and self-check |
| N5 | Fresh bounded ephemeral Agent 2 generalist, read-only | Attempt to refute semantic completeness, authority containment, evidence sufficiency, and rollback honesty | Bounded file read only; no Bash or network | none | Finding ledger with severity, evidence, and admit/return verdict |
| N6 | Bounded ephemeral Agent 2 generalist | Assemble validated owner handoff without adopting any candidate | Bounded file read/write plus the two exact Python tools named in read item 6; no Bash or network | `handoff/` | Manifest, hashes, blocker list, and exact next owner gate |

Each child brief shall declare one objective, accepted inputs, dependencies,
read paths, tools, write target or read-only status, exclusions, expected
outputs, acceptance checks, and escalation conditions. No Agent 2 may
delegate. The first activation uses ephemeral generalists because no accepted
Root-local `software-workflow.json` exists at the basis; it does not borrow a
client profile or infer software-check authority.

### Evidence matrices

The semantic evidence matrix shall use these columns:

`Requirement | Condition | Positive evidence | Negative/adversarial evidence | Owner | Accepted basis | Artifact SHA-256 | Result | Gate`

The affected-client matrix shall use these columns:

`Client | Classification | Accepted obligation source | Exact affected operation | Retained functions | Conformance/migration artifact | Result | Owning gate`

Allowed client classifications are `AFFECTED`, `NOT_AFFECTED`,
`PROSPECTIVE_ONLY`, and `UNRESOLVED`. Only `AFFECTED` creates a required
client-evidence dependency, and only an accepted obligation source permits
that classification.

The semantic failure matrix shall preserve ten independent condition rows:
client configuration/project access, runtime credential readiness,
registration, authorization, project adapter, Unix-socket transport,
compatibility mismatch, wire/protocol validity, provider/engine/model, and
daemon operational state. Every row shall record boundary, required behavior,
recovery, exact class or unresolved item, retry posture, redaction/evidence,
and positive and negative verification.

The release fan-in matrix shall use these columns:

`Input | Exact identity | Owner | Required gate | Validation | Open findings | Release blocking posture`

### INIT finalization and validation boundary

This deliverable has no legacy four-document source kit and is authored in
`MODE=INIT`. The converter, migration finalizer, source-marker map, parity
report, and CONVERT-only QA conditions are therefore not applicable and shall
not be invoked or fabricated. Candidate finalization evidence consists of the
clean contract's exact SHA-256, source-basis register, semantic and open-item
crosswalks, structural validator result, byte-reproducible deterministic
REVIEW checklist, immutable package manifest, and independent read-only
semantic refutation.

### Verification methods

- **VER-001** — Deterministically reproduce the repository commit, accepted decomposition commit, exact owner-selection and authoring-envelope hashes, source hashes, live `ScopeOfWork.md` presence or absence, `_STATUS.md` lifecycle state, and declared write containment before every application or activation.
- **VER-002** — Run `python3 tools/scope_of_work/validate_scope_of_work.py <candidate-directory> --json` against the clean candidate and require `format: SOW_V1`, `valid: true`, and no issues.
- **VER-003** — Recompute the immutable candidate-package manifest twice from byte-identical files and require byte-identical sorted SHA-256 entries and manifest identity.
- **VER-004** — Compare the clean contract against the hash-bound RC-01 through RC-09, DM-01 through DM-07, semantic failure matrix, and sixteen OD6 open-item rows; require one-to-one coverage with no substantive weakening, invention, or silent omission.
- **VER-005** — Validate the work graph, child briefs, writes, predecessor gates, integration ownership, retries, telemetry status, and terminal returns against WORKING_ITEMS and TASK contracts.
- **VER-006** — For each exact contract candidate, execute deterministic positive and negative tests proving exact-equality comparison, pre-consequential mismatch rejection, truthful failure classes, no fallback, no silent replay, and checkout-contained evidence.
- **VER-007** — Validate every `AFFECTED` census row against its accepted obligation source and run the owning client's separately accepted conformance or migration checks; reject prospect names and historical evidence as obligation.
- **VER-008** — Exercise cutover, failed-cutover, rollback, reconnect, mid-operation interruption, partial-output, and indeterminate-completion scenarios in an isolated test environment; require evidence preservation and no unauthorized replay or authority expansion.
- **VER-009** — Dispatch a fresh read-only Agent 2 to attempt refutation of semantic coverage, source grounding, client boundaries, write containment, regression proportionality, and release-readiness claims; findings are evidence, not repairs or acceptance.
- **VER-010** — Conduct accountable-human review of the complete release fan-in, unresolved dispositions, affected-client evidence, rollback readiness, notices, and exact candidate identities, ending only in an explicit release-gate act.
- **VER-011** — Inspect the Git diff and lifecycle evidence at each later application gate and require that only exact authorized targets changed, `_STATUS.md` changed only when its distinct lifecycle gate authorized it, and no runtime or client byte appeared in a non-implementation tranche.
- **VER-012** — Rebuild the governing and acceptance evidence from the checkout without daemon database, cache, session, credential, engine, or downloaded-model state, and verify public-export exclusions where export is proposed.
- **VER-013** — Compare every runtime-project contract and activation candidate against all ten D-GOV-20 architecture statements, the local-residency boundary, preserved-authority clauses, explicit exclusions, and implementation gates, and return any deviation rather than infer a waiver.
- **VER-014** — For an evidence-proven actually affected runtime-project CLI, App, or PEC operation, run its separately accepted proof matrix and require every client-specific distinction, retained-function claim, no-resend property, optionality boundary, and ownership partition stated in this contract.
- **VER-015** — At the accepted basis and before the first activation, verify the inherited Root basis had no Root-local `software-workflow.json` and declared no edges, reconcile the six approved destination evidence inputs without inferring new edges, child forms are bounded ephemeral Agent 2 generalists, and no registered software check or implementation command is present in any brief.
- **VER-016** — Derive the REVIEW checklist twice from the validated clean contract, require byte identity, require every complete one-line `AC-*` text and linked `VER-*` definition exactly once, and bind both artifacts to the clean contract SHA-256.

### Human gates and rollback

The mandatory human gates are, in order where dependent:

1. exact Scope-of-Work content acceptance;
2. Git application of the exact accepted clean bytes;
3. lifecycle initialization from `OPEN` to `INITIALIZED`;
4. sealed first-activation acceptance;
5. exact compatibility and degraded-mode contract acceptance;
6. actual affected-client census acceptance;
7. each affected client's own conformance or migration acceptance;
8. exact runtime-project implementation and separately owned client implementation gates;
9. exact cutover, rollback, replay, and regression-evidence acceptance; and
10. accountable-human release disposition.

Tier-0 relationship disposition is an independent authority branch that must
fan in before release where the exact runtime-project change affects that relationship.
No gate implies another.

Rollback of a candidate-only preparation is deletion or abandonment of the
unadopted candidate package. Rollback of a Git application restores the last
accepted single-format baseline through CHANGE. Rollback of implementation or
release uses the exact accepted before/after identities and plan in `OUT-007`.
No rollback may rewrite historical evidence, silently replay an operation, or
infer a lifecycle or release act.

## Governing Values and Decisions — Axiology

- **AX-001** — Human authority: exact owner acts are required for scope
  acceptance, lifecycle, activation, implementation, client scope, repinning,
  release, issuance, and reliance. Agent preparation and validation confer
  none of them.
- **AX-002** — Runtime project ownership with client autonomy: the runtime project owns generic runtime
  semantics; clients own their own conformance, migration, presentation, and
  retained-function evidence. Transport and implementation do not transfer
  authority.
- **AX-003** — Fail closed without hidden substitution: no runtime loop,
  daemon, model, protocol, transport, replay, or version relationship is
  chosen by implication.
- **AX-004** — Evidence before reliance: matching labels, route success,
  package versions, source proximity, runtime fingerprints, and candidate
  validation are insufficient without accepted exact contracts and affected-
  client evidence.
- **AX-005** — File-native continuity: daemon state is operational only.
  Authority, accepted bases, evidence, gates, and handoffs remain reconstructible
  from checkout-contained files.
- **AX-006** — Unknowns remain explicit: the sixteen stable open items are
  carried without guessed values, hidden defaults, or implementation-derived
  rulings.
- **AX-007** — Context containment: one M-envelope tranche carries one
  consequential semantic change. A change whose implementation breadth or
  client census exceeds M is split before activation.
- **AX-008** — Candidate separation: preparation artifacts, evidence matrices,
  review reports, and manifests are derivative until separately accepted.
  Generated evidence never substitutes for decomposition truth or the live
  clean Scope of Work.
- **AX-009** — Conflict transparency: source conflict, client-ownership seam,
  dependency cycle, or ambiguous completion is returned as a finding or open
  item; it is not silently linearized or resolved through formatting.
- **AX-010** — Public-boundary discipline: generic safe surfaces may be
  exportable only after their own gates; credentials, machine state,
  downloaded models, and private adapters or evidence remain excluded.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-104 OBJ-001 OBJ-002 OBJ-004 | CLM-001 CLM-004 CLM-005 REQ-027 REQ-028 REQ-029 REQ-030 REQ-038 REQ-041 REQ-042 REQ-043 REQ-044 REQ-045 REQ-046 REQ-047 | AC-001 | VER-001 VER-005 VER-011 | Hash-bound tranche brief, exact read/write lists, exclusions, integration owner, D-GOV-20 boundary crosscheck, work graph, and no-effect evidence. |
| OUT-001 | SOW-104 OBJ-001 OBJ-002 OBJ-004 | CLM-001 CLM-004 CLM-005 REQ-027 REQ-028 REQ-029 REQ-030 REQ-038 REQ-041 REQ-042 REQ-043 REQ-044 REQ-045 REQ-046 REQ-047 | AC-010 | VER-001 VER-011 VER-013 | Hash-bound tranche brief, exact read/write lists, exclusions, integration owner, D-GOV-20 boundary crosscheck, work graph, and no-effect evidence. |
| OUT-001 | SOW-104 OBJ-001 OBJ-002 OBJ-004 | CLM-001 CLM-004 CLM-005 REQ-027 REQ-028 REQ-029 REQ-030 REQ-038 REQ-041 REQ-042 REQ-043 REQ-044 REQ-045 REQ-046 REQ-047 | AC-014 | VER-009 VER-013 | Hash-bound tranche brief, exact read/write lists, exclusions, integration owner, D-GOV-20 boundary crosscheck, work graph, and no-effect evidence. |
| OUT-002 | SOW-104 OBJ-001 OBJ-002 OBJ-004 | REQ-001 REQ-002 REQ-003 REQ-004 REQ-005 REQ-006 REQ-007 REQ-008 REQ-009 REQ-036 | AC-002 | VER-004 VER-006 VER-009 | Exact runtime-project compatibility candidate and binding record, with unresolved fields preserved until accepted. |
| OUT-002 | SOW-104 OBJ-001 OBJ-002 OBJ-004 | REQ-001 REQ-002 REQ-003 REQ-004 REQ-005 REQ-006 REQ-007 REQ-008 REQ-009 REQ-036 | AC-011 | VER-004 VER-009 | Exact runtime-project compatibility candidate and binding record, with unresolved fields preserved until accepted. |
| OUT-003 | SOW-104 OBJ-002 OBJ-004 OBJ-007 | CLM-002 CLM-003 REQ-010 REQ-011 REQ-012 REQ-013 REQ-014 REQ-015 REQ-016 REQ-017 REQ-018 REQ-019 REQ-020 REQ-021 REQ-022 REQ-023 REQ-024 REQ-025 REQ-026 REQ-036 | AC-003 | VER-004 VER-006 VER-009 | Exact failure taxonomy and recovery contract plus positive, negative, and continuity evidence. |
| OUT-003 | SOW-104 OBJ-002 OBJ-004 OBJ-007 | CLM-002 CLM-003 REQ-010 REQ-011 REQ-012 REQ-013 REQ-014 REQ-015 REQ-016 REQ-017 REQ-018 REQ-019 REQ-020 REQ-021 REQ-022 REQ-023 REQ-024 REQ-025 REQ-026 REQ-036 | AC-011 | VER-004 VER-009 | Exact failure taxonomy and recovery contract plus positive, negative, and continuity evidence. |
| OUT-003 | SOW-104 OBJ-002 OBJ-004 OBJ-007 | CLM-002 CLM-003 REQ-010 REQ-011 REQ-012 REQ-013 REQ-014 REQ-015 REQ-016 REQ-017 REQ-018 REQ-019 REQ-020 REQ-021 REQ-022 REQ-023 REQ-024 REQ-025 REQ-026 REQ-036 | AC-012 | VER-008 VER-012 | Exact failure taxonomy and recovery contract plus positive, negative, and continuity evidence. |
| OUT-004 | SOW-104 OBJ-001 OBJ-002 OBJ-004 | REQ-009 REQ-031 REQ-032 REQ-036 REQ-038 | AC-004 | VER-001 VER-007 VER-009 | Accepted-obligation citations for affected clients and explicit non-affected, prospective, or unresolved rows. |
| OUT-004 | SOW-104 OBJ-001 OBJ-002 OBJ-004 | REQ-009 REQ-031 REQ-032 REQ-036 REQ-038 | AC-011 | VER-004 VER-009 | Accepted-obligation citations for affected clients and explicit non-affected, prospective, or unresolved rows. |
| OUT-005 | SOW-104 OBJ-002 OBJ-004 | REQ-015 REQ-016 REQ-031 REQ-032 REQ-033 REQ-035 REQ-037 REQ-048 REQ-049 REQ-050 | AC-005 | VER-007 VER-009 VER-010 | Separately accepted runtime-project CLI or client-owned conformance or migration results, exact proof obligations, and truthful missing-evidence blocks. |
| OUT-005 | SOW-104 OBJ-002 OBJ-004 | REQ-015 REQ-016 REQ-031 REQ-032 REQ-033 REQ-035 REQ-037 REQ-048 REQ-049 REQ-050 | AC-006 | VER-006 VER-008 VER-009 | Separately accepted runtime-project CLI or client-owned conformance or migration results, exact proof obligations, and truthful missing-evidence blocks. |
| OUT-005 | SOW-104 OBJ-002 OBJ-004 | REQ-015 REQ-016 REQ-031 REQ-032 REQ-033 REQ-035 REQ-037 REQ-048 REQ-049 REQ-050 | AC-010 | VER-001 VER-011 VER-013 | Separately accepted runtime-project CLI or client-owned conformance or migration results, exact proof obligations, and truthful missing-evidence blocks. |
| OUT-005 | SOW-104 OBJ-002 OBJ-004 | REQ-015 REQ-016 REQ-031 REQ-032 REQ-033 REQ-035 REQ-037 REQ-048 REQ-049 REQ-050 | AC-015 | VER-007 VER-014 | Separately accepted runtime-project CLI or client-owned conformance or migration results, exact proof obligations, and truthful missing-evidence blocks. |
| OUT-006 | SOW-104 OBJ-001 OBJ-002 OBJ-004 OBJ-007 | REQ-005 REQ-010 REQ-011 REQ-012 REQ-014 REQ-033 REQ-037 REQ-039 REQ-040 | AC-006 | VER-006 VER-008 VER-009 | Requirement-complete runtime-project evidence with failure honesty, no fallback, no silent replay, continuity, and export-boundary results. |
| OUT-006 | SOW-104 OBJ-001 OBJ-002 OBJ-004 OBJ-007 | REQ-005 REQ-010 REQ-011 REQ-012 REQ-014 REQ-033 REQ-037 REQ-039 REQ-040 | AC-012 | VER-008 VER-012 | Requirement-complete runtime-project evidence with failure honesty, no fallback, no silent replay, continuity, and export-boundary results. |
| OUT-007 | SOW-104 OBJ-002 OBJ-004 OBJ-007 | REQ-012 REQ-026 REQ-034 REQ-035 REQ-036 REQ-037 | AC-007 | VER-008 VER-009 VER-011 | Exact before/after bindings, tested abort/restore and interrupted-operation evidence, and separately gated rollback acts. |
| OUT-007 | SOW-104 OBJ-002 OBJ-004 OBJ-007 | REQ-012 REQ-026 REQ-034 REQ-035 REQ-036 REQ-037 | AC-010 | VER-001 VER-011 VER-013 | Exact before/after bindings, tested abort/restore and interrupted-operation evidence, and separately gated rollback acts. |
| OUT-007 | SOW-104 OBJ-002 OBJ-004 OBJ-007 | REQ-012 REQ-026 REQ-034 REQ-035 REQ-036 REQ-037 | AC-011 | VER-004 VER-009 | Exact before/after bindings, tested abort/restore and interrupted-operation evidence, and separately gated rollback acts. |
| OUT-008 | SOW-104 OBJ-001 OBJ-002 OBJ-004 OBJ-007 | CLM-001 CLM-004 REQ-008 REQ-032 REQ-035 REQ-037 REQ-038 REQ-040 | AC-008 | VER-003 VER-009 VER-010 VER-011 | Immutable fan-in manifest, hashes, findings, notice state, open dispositions, rollback readiness, and explicit human choice. |
| OUT-008 | SOW-104 OBJ-001 OBJ-002 OBJ-004 OBJ-007 | CLM-001 CLM-004 REQ-008 REQ-032 REQ-035 REQ-037 REQ-038 REQ-040 | AC-010 | VER-001 VER-011 VER-013 | Immutable fan-in manifest, hashes, findings, notice state, open dispositions, rollback readiness, and explicit human choice. |
| OUT-009 | SOW-104 OBJ-002 OBJ-004 | REQ-027 REQ-028 REQ-029 REQ-030 REQ-033 REQ-038 REQ-051 REQ-052 | AC-009 | VER-005 VER-009 VER-011 | Valid clean contract and exact checklist, profile and dependency checks, versioned work graph, sealed briefs and returns, write-containment proof, review, and truthful handoff. |
| OUT-009 | SOW-104 OBJ-002 OBJ-004 | REQ-027 REQ-028 REQ-029 REQ-030 REQ-033 REQ-038 REQ-051 REQ-052 | AC-013 | VER-002 VER-016 | Valid clean contract and exact checklist, profile and dependency checks, versioned work graph, sealed briefs and returns, write-containment proof, review, and truthful handoff. |
| OUT-009 | SOW-104 OBJ-002 OBJ-004 | REQ-027 REQ-028 REQ-029 REQ-030 REQ-033 REQ-038 REQ-051 REQ-052 | AC-016 | VER-005 VER-015 | Valid clean contract and exact checklist, profile and dependency checks, versioned work graph, sealed briefs and returns, write-containment proof, review, and truthful handoff. |
