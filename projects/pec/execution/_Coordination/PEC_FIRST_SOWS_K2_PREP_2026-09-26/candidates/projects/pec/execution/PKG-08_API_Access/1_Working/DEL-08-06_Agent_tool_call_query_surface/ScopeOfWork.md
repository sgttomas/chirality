---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-08-06
package_id: PKG-08
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@189f205ff02df4111b33c20be441ce06e65ada7a
project_scope_refs: [SOW-099]
package_objective_refs: [OBJ-001]
---

# Scope of Work — DEL-08-06 Agent tool-call query surface

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-08-06` — "Agent tool-call
query surface" — in `PKG-08` API & Access of the PEC v2 build. It covers project
scope item `SOW-099` in service of package objective `OBJ-001`. It is the
deliverable's first contract; no earlier production contract exists. It fixes
the shape of the tool surface at contract level — inputs, outputs, paths, mode,
side effects, failure behaviour, result schema, access class and human gates —
without choosing a token mechanism, a harness, an App or an agent
configuration, and without declaring or invoking any tool.

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.6** (`current_basis`, SCA-006 successor), accepted by the owner at
SCA-006 checkpoint group 3 on 2026-09-26. The frontmatter pin
`189f205ff02df4111b33c20be441ce06e65ada7a` is the checkpoint-3 acceptance
commit, an ancestor of `origin/main`. At that commit `SOFTWARE_DECOMP.md` has
SHA-256 `9374c21fb87b…8eb1`, `Deliverables.csv` `94ee5d182ae9…9805`,
`ScopeLedger.csv` `1d24a4b86f05…916e` and `ContextBudgetQA.csv`
`93b0bb075a0e…4c7c`, and `docs/PRD.md` v2.4 has SHA-256 `ae49b8065698…3fbe`.

**Observation commit.** The pin binds the accepted decomposition bytes only.
Unless a claim names another commit, every statement below about the state of a
file, record, lifecycle or decision is an observation at `origin/main`
`125cfacc1` (`125cfacc10f664685cb91802a9166b1041f42a25`). At that commit the
four decomposition files named above and the PRD are byte-identical to the pin,
so every locus this contract quotes from them reads the same at both commits.
The deliverable folder, its control files and the `D-PEC-101` records it cites
exist at `125cfacc1` and not at the pin.

**Objective warrant.** `SOW-099` carries `OBJ-001` in the ledger, and
decomposition §3 lists `SOW-099` among the mapped scope items of `OBJ-001` and
`DEL-08-06` among its mapped deliverables. Decision-log entry `DL-21` records
the mapping: SCA-006 added "SOW-099 (agent tool-call query surface, PEC-API-007
→ new DEL-08-06, P3)" with the other three new items, "all mapped to OBJ-001".
The contribution is packaging, not derivation: the surface makes the same cited,
stamped orientation query that other deliverables produce reachable by an agent
through a tool call. The per-claim citations, the sub-second read and the
orientation content that `OBJ-001` names are produced and measured elsewhere
(CLM-011); this contract states the attribution no more strongly than that, and
`AC-017` puts the qualification before the review gate.

- **CLM-001** — The accepted `ScopeLedger.csv` row for `SOW-099` reads in full (columns `ScopeItemID,InOutStatus,ScopeItemStatement,SourceRef,PackageID,DeliverableIDs,ObjectiveIDs,DecisionRef,OpenIssue,Notes`):

> `SOW-099,IN,Offer a read-only query interface for agent tool calls over the versioned API under the agent access class; enabling it is consumer-owned,"PEC-API-007, §8",PKG-08,DEL-08-06,OBJ-001,SCA-006,FALSE,New under SCA-006 (D-PEC-90 owner answer; DQ-a); token mechanism OI-006; tier-0 profile amendment before any tool is declared or invoked; P3`

- **CLM-002** — The ledger `SourceRef` resolves to two PRD v2.4 loci. `PEC-API-007` (§9.6) reads in full:

> PEC shall offer a read-only query interface packaged for agent tool calls,
> over the same versioned API and responses (PEC-API-003, PEC-API-004,
> PEC-API-006, PEC-ORI-007), under the `agent` access class. Enabling it in any
> harness, App or agent configuration is consumer-owned (PEC-K-03, PEC-K-11);
> PEC never injects or schedules. Before any such tool is declared or invoked,
> the PEC Domain Engine Profile (`_DomainEngines/profiles/pec.yaml`) is amended
> under its own tier-0 act. P3 capability.

  PRD §8 says of agents that they "may act on PEC data received through an explicitly enabled consumer, and may query PEC directly through tool calls under the read-only `agent` access class (PEC-API-007) where that surface is enabled", and of the access classes:

> The `agent` class is read-only query access for tool calls: orientation,
> deltas, gate verdicts, decision-slate and presence reads, with no event
> ingest, no presence reports and no admin act. Every class is local-only and
> token-scoped; the token mechanism, including credentials for the `agent`
> class, is the open §16.6 decision.

- **CLM-003** — The objective this deliverable serves is `OBJ-001` "Orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation" (§3, `SourceRef` §3.1). The direction behind `SOW-099` is the owner's answer recorded with the `D-PEC-90` ruling, "agents may eventually query PEC directly, yes.  Through tool calls.", carried into SCA-006 by the checkpoint-1 acceptance "SCA-006 CP1: accept; DQ a; ENV a; BUD a; GATE a; INS a; R-C excluded". Option DQ-a is the read-only `agent` access class; Impact Assessment §13.1 gives its rationale as "Least privilege: an owner can enable agent query without giving the tool host harness ingest rights."

## Deliverable Definition — Ontology

`DEL-08-06` is typed `BACKEND_FEATURE_SLICE` at Context Envelope **`M`** with
`PhaseHint` `P3`. Its `AnticipatedArtifacts` field is "Tool definitions over the
read API + access-class binding + tests", and the three outputs below are that
list and nothing beyond it.

- **OUT-001** — Tool definitions over the read API: read-only tool definitions whose inputs are the query kinds the `agent` access class admits and the versioned API serves, whose results are the versioned API responses unchanged, and which state, per definition, the inputs, output and result schema, the paths read, the read-only mode, the absence of side effects, the failure behaviour and the human gates fixed by this contract.
- **OUT-002** — The access-class binding: the association of every tool definition with the read-only `agent` access class, under which each tool-call query is issued as an `agent`-class request through the service's token-scoped access path and under no other class.
- **OUT-003** — A test suite implementing the verification methods declared in this contract.

### Identity of record

- **CLM-004** — `DEL-08-06` is named "Agent tool-call query surface", Type `BACKEND_FEATURE_SLICE`, Context Envelope `M`, `PhaseHint` `P3`, `ResponsibleParty` `TBD`, `CoversScopeItems` `SOW-099`, `SupportsObjectives` `OBJ-001`, with `ContextEnvelopeNotes` "Token mechanism follows OI-006; the tier-0 profile is amended before any tool is declared or invoked"; sources `execution/_Decomposition/Deliverables.csv` row `DEL-08-06` and `SOFTWARE_DECOMP.md` §5 PKG-08 table ("| DEL-08-06 | Agent tool-call query surface | BACKEND_FEATURE_SLICE | M | P3 | SOW-099 |"). `ContextBudgetQA.csv` rates it `MEDIUM` risk with `RecommendedAction` "Hold envelope; re-assess on the linked OI's ruling", and decomposition §8 records that "DEL-08-06 (agent tool-call query surface) is M with MEDIUM risk, coupled to OI-006 like DEL-08-01 and held at its envelope until that ruling". The folder was scaffolded under `D-PEC-101` on 2026-09-26, and its `_STATUS.md` reads `OPEN`.
- **CLM-005** — The register `Description` of record is: "Read-only query interface packaged for agent tool calls over the versioned API and responses, bound to the read-only agent access class; enabling it is consumer-owned; writes nothing." Five terms are carried as written and not strengthened: the surface is **read-only** and **writes nothing**; it is **packaged for agent tool calls**, not a new query service; it runs **over the versioned API and responses**; it is **bound to the read-only agent access class**; and **enabling it is consumer-owned**.
- **CLM-006** — The `SOW-099` Notes cell (CLM-001) and the envelope note (CLM-004) carry two conditions that this contract records and does not discharge: the token mechanism follows `OI-006`, whose open choice "also covers credentials for the agent access class (tool-call query, SOW-099; SCA-006)" (decomposition §10), and the tier-0 profile is amended before any tool is declared or invoked (CLM-013). Constraint `C12` requires that where an open §16 decision "materially affects architecture the affected work is fenced or flagged, never guessed".

### Placement in the work graph

- **CLM-007** — `Dependencies.csv` holds six rows. `DEP-08-06-001` and `DEP-08-06-002` are `ANCHOR` rows (package-local to `PKG-08`; the `SOW-099` requirement trace). Four are `EXECUTION` upstream edges, each `DependencyType` `PREREQUISITE`, `RequiredMaturity` `INITIALIZED`, `SatisfactionStatus` `PENDING`, `Confidence` `MEDIUM`, `Origin` `EXTRACTED`, `Status` `ACTIVE`, seeded under `D-PEC-101` (SCA-006 B2): `DEP-08-06-003` to `DEL-08-01` "Unix-socket server + token-scoped access", `EdgeID` `E-P84`, stratum `DERIVED`, `Explicitness` `EXPLICIT`, `Statement` "Tool-call queries run under the read-only agent access class of the socket server"; `DEP-08-06-004` to `DEL-08-02` "Versioned additive API schema", `E-P85`, `DERIVED`, `Statement` "Tool calls query over the versioned API schema (PEC-API-003)"; `DEP-08-06-005` to `DEL-08-03` "Compact citation-bearing response format", `E-P86`, `DERIVED`, `Statement` "Tool calls return the compact citation-bearing, budget-bounded responses (PEC-API-004, PEC-API-006)"; and `DEP-08-06-006` to `DEL-04-01` "Loop orientation return", `E-P87`, stratum `PROPOSAL`, `Explicitness` `IMPLICIT`, `Statement` "Tool-call queries serve orientation reads". `_DEPENDENCIES.md` records "No deliverable depends on this one at setup." No `ACTIVE` row of any deliverable `Dependencies.csv` names this contract as its `EvidenceFile`.
- **CLM-008** — The `D-PEC-101` proposal records, among its disclosed findings, that an edge to the owner of the reliance envelope was not seeded:

> **DEL-08-06 → DEL-04-03 is not added.** PEC-API-007 cites PEC-ORI-007
> (SOW-097, DEL-04-03), but the accepted plan lists DEL-04-01, and DEL-08-06
> already reaches DEL-04-03 through DEL-08-03 → DEL-04-03 (E-P53).

  The finding closes "Adding it is an amend." No register row links this deliverable to the producers of deltas (`DEL-04-02`), gate verdicts (`DEL-05-01`), the decision slate (`DEL-05-02`) or presence reads (`DEL-06-01`, `DEL-06-02`, `DEL-06-03`), which the `agent` class admits (CLM-002). This contract adds and presumes no edge (CON-003).
- **CLM-009** — Phase staging, checked against the `PhaseHint` column of `Deliverables.csv`: `DEL-08-06` is `P3`; its four predecessors `DEL-08-01`, `DEL-08-02`, `DEL-08-03` and `DEL-04-01` are `P1`. The PRD §12 P3 row scopes "PEC-side interfaces/adapters usable by hooks CLI or application-owned Runtime service consumers, and the agent tool-call query surface (PEC-API-007)", with live use requiring a separately authorized receiving consumer, and §12 adds that P3 and P4 "do not themselves authorize Root, App, a harness, an agent's tool host, or another loop to poll, push, inject, subscribe, or consume".
- **CLM-010** — Upstream contracts at `125cfacc1` predate SCA-006. The accepted `DEL-08-01` contract (SHA-256 `8ac1dc050efb…3d76`) states "The delivered access-class set shall be exactly owner, harness, and admin", with no `agent` class. SCA-006 `Propagation_Plan.md` §B4 places the `DEL-08-01`, `DEL-08-03` (`013c615a0c91…3138`) and `DEL-04-01` (`6f4e8c66a571…30ae`) contracts in the Scope of Work currency set at graph node S4 with combined class `STALE_REBUILD_REQUIRED`. This contract grounds its requirements on register rows and PRD v2.4 text, not on those contracts' current wording (CON-001).

### Boundaries

- **CLM-011** — The `PKG-08` charter (decomposition §4) is "The machine-consumer surface: Unix-socket binding, token-scoped access classes, p95 latency, versioned additive schema, compact citation-bearing responses, SSE subscription, response-size budgets, and the agent tool-call query surface", with "Dashboard rendering (PKG-09)" out of package scope. The acts adjacent to this surface are owned elsewhere and are cited, never discharged: the socket binding, token acceptance and access-class decision logic, including the `agent` class, are `DEL-08-01` (`SOW-040`, `SOW-003`); the versioned additive API schema is `DEL-08-02` (`SOW-042`); the compact citation-bearing format and the declared response-size budgets are `DEL-08-03` (`SOW-043`, `SOW-098`); the p95 latency budget is `DEL-08-04` (`SOW-041`); the SSE subscription is `DEL-08-05` (`SOW-044`); orientation derivation is `DEL-04-01` (`SOW-004`); deltas since a caller SHA are `DEL-04-02` (`SOW-005`); per-claim citation, response stamping and the reliance envelope are `DEL-04-03` (`SOW-006`, `SOW-007`, `SOW-097`); scope parameterization is `DEL-04-04` (`SOW-008`); measurement-limitation statements are `DEL-04-05` (`SOW-009`); gate verdicts are `DEL-05-01` (`SOW-022`, `SOW-023`); the decision slate is `DEL-05-02` (`SOW-024`); presence records, the Git/worktree scan, their correlation, TTL and heartbeat discipline with citation exclusion, and overlap detection are `DEL-06-01`, `DEL-06-02`, `DEL-06-03`, `DEL-06-05` and `DEL-06-06` (`SOW-026`, `SOW-027`, `SOW-028`, `SOW-030`, `SOW-032`, `SOW-031`); the content-minimal ingest guard is `DEL-01-03` (`SOW-056`); the service-core dependency and egress assertions are `DEL-01-05` (`SOW-052`, `SOW-053`); no-ruling-write verification is `DEL-10-03` (`SOW-025`); the kill test is `DEL-10-02` (`SOW-055`); consumer-uptake measurement, which counts "enabled agent tool-call surfaces" among candidate consumers, is `DEL-10-12` (`SOW-060`); and the standing reliance-advertisement gate is `DEL-10-13` (`SOW-100`).
- **CLM-012** — Four acts belong to no deliverable and are owned by named instruments: the choice of PEC's token mechanism, including the `agent` credentials, is the §16.6 owner ruling (`OI-006`, `SOW-080` `TBD`), where PRD §16.6 says "The decision on PEC's own token mechanism stays open; it includes the credentials of the `agent` access class for tool-call query (PEC-API-007)."; the tier-0 profile act is the tier-0 owner's (CLM-013); enabling the surface in any harness, App or agent configuration is the consumer's (`PEC-API-007`, CLM-002); and whether a release advertises operational reliance is a separate human release act after the §12 gate, which "creates no consumer duty and does not change the phase exit tests above". The additive API schema fields for the `agent` class are assigned by SCA-006 `Propagation_Plan.md` §B8 to a "later `D-PEC` source packet (PEC-API-003 additive evolution)".
- **CLM-013** — The live tier-0 profile `_DomainEngines/profiles/pec.yaml` (SHA-256 `6858d567ee27…314f`) carries `execution_policy: "DECLARED_READ_ONLY_AND_SUMMARY_TOOLS_ONLY"`, `profile_status: "ADOPTED"` and `integration_level: "READ_ONLY"`, declares two deterministic tools and no tool-call query tool, and binds the tool surface through a human gate and an open issue:

> profile amendment before any runtime, adapter-client, mutating, proposal, or external-result tool is declared or invoked
>
> Before any future adapter or runtime-client invocation, amend this profile with exact inputs, outputs, paths, modes, side effects, failure behavior, result schemas, and human gates.

  SCA-006 `Propagation_Plan.md` §B6 plans that act and places it after this contract: "After DEL-08-06's first Scope of Work fixes the tool's shape, and **before** any agent tool-call query tool is declared or invoked in the profile, a harness, the App or an agent configuration." Its planned change is:

> One declared tool entry for the agent tool-call query surface, with exact
> inputs (query kinds), outputs (the versioned response carrying the reliance
> envelope and budgets), paths (reads only PEC's own store through the
> versioned API), mode `read_only`, side effects (none), failure behavior (the
> file-fallback signal), result schemas and human gates (enabling it stays
> consumer-owned)

  On ownership the plan says "The tier-0 owner rules it. PEC prepares it and brings it to the owner; it is outside PEC's default write scope", and on sequence that the act "is not a precondition of checkpoint 3, of the B1 setup packet or of Scope of Work authoring, which declare and invoke nothing". The undertaking graph carries the act as node K3, where "the profile act follows DEL-08-06's first Scope of Work, which fixes the tool's shape (plan §B6)". This contract neither performs that act nor presumes its content; it supplies the shape the act may transcribe.
- **CLM-014** — Operational reliance is bounded by `PEC-K-03`: "Within the pin, coverage and trust tier that a response declares (PEC-ORI-007), a consumer, or an agent acting through one or through the tool-call surface (PEC-API-007), may take a record-tier claim as true as of its examined-through SHA and act on it without re-reading the cited source (operational reliance); wherever PEC is absent, degraded, failing its own checks or stating a limitation, it falls back to the files (PEC-K-01). Operational reliance is available only from a PEC release that has passed the §12 reliance-advertisement gate." `PEC-ORI-007` requires "a file-fallback signal whenever PEC is absent, degraded or failing its own checks" and says "No consumer may treat silence as a claim." `PEC-API-006` requires that "A budget is never met by dropping citations, stamps or stated limitations, and any truncation is stated in the response, never silent." `projects/pec/AGENTS.md` says that "An explicitly enabled consumer, whether a harness or an agent querying through tool calls under the read-only `agent` access class, owns whether and when it consumes and whether it injects labeled PEC data".
- **CLM-015** — The permanent non-goals of PRD §4.2 bind the surface as they bind PEC: not a system of record (`SOW-065`), not a ruling surface (`SOW-066`), not an orchestrator (`SOW-067`), not a lock manager (`SOW-068`) and not a Git actor (`SOW-070`). `PEC-K-01` reads "No governed act may require a PEC read or write. Deleting PEC blocks nothing." `PEC-K-11` reads "Pipeline and unscoped-conversation modes support testable zero-contact operation." The decomposition vocabulary records that "An agent may also query directly through tool calls under the agent access class; that agent is not a harness".
- **CLM-016** — The deliverable is at lifecycle `OPEN` with no implementation present: its folder holds six files and no `ScopeOfWork.md`, and the accepted API contract `v2/contracts/api/v1/schema.json` (SHA-256 `0a4e42737e62…5c67`) contains no `agent` term. Every requirement, acceptance criterion and verification method below states a contract on future production; none asserts that anything has been built.

- **TBD-001** — `ResponsibleParty` is unassigned; the register records `TBD`, with assignment at WORKING_ITEMS activation.
- **TBD-002** — The token mechanism and the `agent` credentials are the open §16.6 decision (`OI-006`, CLM-012). They arrive with that ruling and through the access path of `DEL-08-01`; this contract fixes the binding of REQ-008 without them.
- **TBD-003** — The representation of a tool definition — its file format, naming, and whether one definition serves each query kind or one parameterized definition serves several — is fixed by no accepted source. It is chosen during production within REQ-001 through REQ-007 and recorded in the tool definitions themselves; no harness, App or agent-configuration format is selected by this contract.
- **TBD-004** — The exact API operations and parameters that realize each admitted query kind, and the operation-to-class mapping that admits them to the `agent` class, are fixed by the versioned API schema and the access-class decision logic of their owners (CLM-011), not by this contract.
- **TBD-005** — The numeric response-size budgets are unconfirmed at `125cfacc1`; `PEC-API-006` says "Numeric budgets are confirmed at Phase 1", and the format that carries them is `DEL-08-03`'s. The surface passes budgets and continuation through (REQ-002) and sets none of its own.
- **TBD-006** — The representation of the file-fallback signal in a tool result when no API response exists (PEC unreachable, service stopped, request refused) is not fixed: the envelope that carries the signal is `DEL-04-03`'s and its schema fields are the §B8 source packet's (CLM-012). It is chosen during production consistent with them and recorded in the tool definitions.
- **TBD-007** — The content of the tier-0 profile entry is not made at `125cfacc1`; it is the K3 act's (CLM-013).
- **TBD-008** — The transport a tool call uses is the service's local-only binding, a Unix socket by default; any loopback listener is the open §16.9 decision (`OI-009`, `SOW-083`), not this contract's.

## Completion and Reliance Basis — Epistemology

The requirements below state what future production must satisfy. Nothing in
this section asserts that a tool definition, a binding or a test exists.

- **REQ-001** — Inputs. The tool definitions shall accept as inputs only the query kinds the `agent` access class admits — orientation, deltas since a caller-supplied commit SHA, gate verdicts, decision-slate reads and presence reads (CLM-002) — together with the parameters the versioned API defines for them, including scope parameters, the caller SHA and continuation inputs. A tool definition shall be declared only for a query kind the versioned API serves, and no input shall express event ingest, a presence report, an admin act or any write.
- **REQ-002** — Outputs. Each tool result shall be the versioned API response for the query, unchanged: its schema version, claims, per-claim citations, stamps, stated limitations, truncation statements, continuation and reliance envelope shall be carried through, and nothing shall be summarized, re-derived, recombined into new claims, or dropped. Where the API response is paginated or truncated under a declared budget, the tool result shall carry the continuation and the truncation statement as the API states them, per `PEC-API-006` (CLM-014).
- **REQ-003** — Paths. The surface shall read only PEC's own store, and only through the versioned API; it shall read no governed file, Git object, registry, other store or network resource directly (CLM-013).
- **REQ-004** — Mode and side effects. Every tool definition shall declare mode read-only and no side effects, and a tool call shall perform no event ingest, presence report, admin act, file write, store write, Git act, dispatch or ruling write, per the Description "writes nothing" (CLM-005) and the non-goals of CLM-015.
- **REQ-005** — Failure behaviour. Where PEC is absent or unreachable, degraded, failing its own checks, or refuses the request, the tool result shall carry the file-fallback signal and no claim; it shall never return an empty, default or partial result presented as a claim, because "No consumer may treat silence as a claim" (CLM-014). Where an API response carries the signal, the tool result shall carry it unchanged.
- **REQ-006** — Result schema. Each tool definition shall name the versioned API schema, and the version of it, whose response is its result, and shall define no result schema of its own; evolution of the result follows the API's additive evolution (`PEC-API-003`).
- **REQ-007** — Human gates. The tool definitions shall state, as gates, that enabling the surface in any harness, App or agent configuration is consumer-owned and that no tool is declared or invoked before the tier-0 profile act is effective (CLM-013). PEC shall enable, register, inject or schedule nothing on a consumer's behalf, and no tool definition shall be declared to, registered in or invoked by any profile, harness, App or agent configuration before that act is effective (CON-002).
- **REQ-008** — Access-class binding. Every tool-call query shall be issued as an `agent`-class request through the service's token-scoped access path and served under that class only. The surface shall hold or present no owner, harness or admin credential, shall never retry or escalate under another class, and shall treat a refused request as a failure under REQ-005 with the refusal stated. The binding shall not depend on the choice of token mechanism (TBD-002).
- **REQ-009** — Labeling. The tool definitions shall describe their results as labeled, non-authoritative PEC data, never citable as authority, point the caller to the reliance envelope and the file fallback, and shall not themselves assert that operational reliance is available (CLM-014).
- **REQ-010** — Graceful absence. Nothing in the tool definitions shall require any consumer, agent, harness or loop to use them, and every tool definition shall state that the files remain the consumer's route whenever the surface is absent, not enabled, or failing. No other behaviour of PEC's API shall change with the surface absent, and no governed act shall depend on it, per `PEC-K-01` (CLM-015).
- **REQ-011** — Pull only. The surface shall act only when a consumer's tool call arrives. It shall not poll, push, subscribe, schedule, inject, or claim a cadence, and with no tool call it shall make zero contact, per `PEC-K-03` and `PEC-K-11` (CLM-015).
- **REQ-012** — Content-minimal. The tool definitions and tool results shall add no file or diff content: a result carries only what the API response carries, and the definitions carry no content of any governed file, per `PEC-K-10` and constraint `C6`.
- **REQ-013** — Locality and dependencies. The surface shall reach PEC only over the service's local-only binding, make no external network call, and introduce no third-party runtime dependency into the service core, per `PEC-API-001`, `PEC-SVC-001` and `PEC-SVC-002` (constraints `C7`, `C8`).
- **REQ-014** — The surface shall perform no act owned by another deliverable and shall perform no act owned by another package. In particular it shall bind no socket and decide no access class (`DEL-08-01`), define no API schema element (`DEL-08-02`), define no response format or size budget (`DEL-08-03`), set no latency budget (`DEL-08-04`), offer no subscription (`DEL-08-05`), derive no orientation (`DEL-04-01`), compute no delta (`DEL-04-02`), attach no citation, stamp or reliance envelope of its own (`DEL-04-03`), define no scope parameter (`DEL-04-04`), compose no limitation statement (`DEL-04-05`), evaluate no gate (`DEL-05-01`), assemble no decision slate (`DEL-05-02`), produce no presence record, scan, correlation, TTL or overlap finding (`DEL-06-01`, `DEL-06-02`, `DEL-06-03`, `DEL-06-05`, `DEL-06-06`), enforce no ingest guard (`DEL-01-03`), discharge no locality or dependency assertion (`DEL-01-05`), no no-ruling-write verification (`DEL-10-03`), no kill test (`DEL-10-02`), no uptake measurement (`DEL-10-12`) and no reliance-advertisement gate (`DEL-10-13`); each is cited to its owner in CLM-011.
- **REQ-015** — The surface shall make no decision reserved to an instrument outside the deliverables: it shall choose no token mechanism or `agent` credential (the §16.6 owner ruling), write or presume no tier-0 profile entry (the tier-0 owner's act), enable itself in no consumer (the consumer's decision), advertise no operational reliance (the human release act after the §12 gate) and add no API schema field outside its source packet; each is cited to its owner in CLM-012 and CLM-013.
- **REQ-016** — Tests shall implement the verification methods declared in this contract; they shall not define scope, requirements or acceptance criteria.

- **AC-001** — Each tool definition accepts only admitted query kinds and their API parameters, is declared only for a kind the versioned API serves, and has no input able to express ingest, a presence report, an admin act or a write.
- **AC-002** — For each declared query kind, the tool result equals the versioned API response for the same query field for field, including citations, stamps, limitations, envelope, truncation statements and continuation; nothing is summarized, re-derived or dropped.
- **AC-003** — During tool calls the surface reads only the versioned API; it opens no governed file, Git object, registry or other store and makes no other request.
- **AC-004** — Every tool definition declares read-only mode and no side effects, and a tool call leaves governed files, PEC's store, presence records and Git state unchanged and issues no write, ingest, presence, admin, dispatch or ruling operation.
- **AC-005** — With PEC absent, the service stopped, a degraded or check-failing service, and a refused request, each tool result carries the file-fallback signal and no claim; no empty, default or partial result is presented as a claim; an API-supplied signal passes through unchanged.
- **AC-006** — Each tool definition names the API schema and version of its result and defines no result schema of its own.
- **AC-007** — The tool definitions state the consumer-owned enabling gate and the tier-0 gate; the delivered surface contains no enabling, registration, injection or scheduling act, and no definition is declared to or invoked by any profile, harness, App or agent configuration before the tier-0 act is effective.
- **AC-008** — Every tool-call query reaches the service as an `agent`-class request; no owner, harness or admin credential is held or presented; a refused request yields a stated refusal under the failure behaviour and no retry under another class; the binding code contains no token-mechanism choice.
- **AC-009** — Each tool definition labels its results non-authoritative and never citable as authority, points to the reliance envelope and file fallback, and contains no statement that operational reliance is available.
- **AC-010** — No tool definition requires use; each states the file route; PEC's API behaves identically with the surface absent; no governed act or other PEC component depends on the surface.
- **AC-011** — With no tool call the surface makes no contact of any kind, and the surface contains no polling, push, subscription, scheduling, injection or cadence mechanism.
- **AC-012** — Tool definitions contain no governed-file content, and tool results contain no field absent from the corresponding API response.
- **AC-013** — The surface connects only through the local-only binding, makes no external network call, and adds no third-party runtime dependency, leaving the `DEL-01-05` assertion intact.
- **AC-014** — The surface performs none of the excluded acts of REQ-014 and defines none of the owned artifacts it names.
- **AC-015** — The delivered surface contains no token-mechanism choice, tier-0 profile content, consumer enabling, reliance advertisement or API schema field outside its source packet.
- **AC-016** — The test suite implements VER-001 through VER-015, executes in the `PKG-08` test run, passes, and introduces no acceptance criterion absent from this contract.
- **AC-017** — The review gate confirms this contract's traceability to `SOW-099` and `OBJ-001` as recorded under `DL-21`, confirms the objective contribution is stated as packaging no more strongly than the warrant above states it, and confirms that no access-class, schema, format, budget, orientation, delta, gate, slate, presence, validation or tier-0 scope has been absorbed.

- **CON-001** — **Upstream contracts predate SCA-006.** PRD v2.4 §8, `SOW-003` and the `DEL-08-01` register row include the `agent` class, but the accepted `DEL-08-01` contract at `125cfacc1` delivers exactly owner, harness and admin (CLM-010), so REQ-008 has no conforming upstream contract until the S4 rebuild; the `DEL-08-03` and `DEL-04-01` contracts are in the same rebuild set. This contract relies on none of their current wording. Whether production waits for the S4 rebuilds or proceeds against the register text is an ordering decision for the undertaking graph and its owner.
- **CON-002** — **What "declared or invoked" covers.** `PEC-API-007` and the profile gate (CLM-013) bar declaring or invoking any such tool before the tier-0 act, and §B6 says Scope of Work authoring declares and invokes nothing. No accepted source says whether authoring tool definitions as source and exercising them in PEC's own test suite before the act counts as declaring or invoking a tool. REQ-007 bars declaration to, registration in and invocation by any profile, harness, App or agent configuration; the question for production source and tests is the owner's, at the K3 act or in the production packet, and is not resolved here.
- **CON-003** — **Dependency coverage.** The `agent` class admits deltas, gate verdicts, decision-slate and presence reads, but the register holds edges only to `DEL-08-01`, `DEL-08-02`, `DEL-08-03` and `DEL-04-01`, and the edge to the reliance-envelope owner was left as an amend (CLM-008). This contract adds no edge; REQ-001 declares a tool only for a kind the API serves. Whether further edges are recorded is a dependency-register question for its owning workflow.
- **CON-004** — **Envelope on non-orientation reads.** `PEC-ORI-007` requires the reliance envelope on every orientation response, and `PEC-API-007` places the tool surface over responses that include it, but the `agent` class also serves gate-verdict, decision-slate and presence reads, and no accepted source says whether those responses carry an envelope. The surface neither adds nor strips an envelope (REQ-002, REQ-014); which responses carry one is decided under `DEL-04-03`, `DEL-08-03` and the API schema.

## Production and Verification Method — Praxeology

Production proceeds in the order tool-shape declaration → access-class binding
→ result pass-through → failure behaviour → tests. The tool shape is fixed by
this contract before any code exists, so that the tier-0 act can transcribe it
and the code cannot widen it. All work is bounded to this deliverable folder,
the `PKG-08` source and the test paths a ruled packet names; this contract
authorizes no register, decomposition, PRD, profile, API schema,
upstream-deliverable or consumer-configuration edit, and no v2 source write by
itself. Tests implement the verification methods below and create no scope.

- **VER-001** — Inspect every tool definition's input declaration against the `agent`-class query kinds and the served API operations; attempt inputs expressing ingest, a presence report, an admin act and a write, and assert each is inexpressible or rejected before any request is issued.
- **VER-002** — For each declared query kind, issue the same query through the tool surface and directly against the API over a fixture store, including a paginated and a truncated response, and assert field-for-field equality of the results.
- **VER-003** — Run tool calls under file-access and network tracing over a fixture tree and assert that the only resource reached is the API binding.
- **VER-004** — Inspect each definition's declared mode and side effects; hash the fixture files, store and Git state before and after a series of tool calls and assert byte-identity; inspect the call surface for any write, ingest, presence, admin, dispatch or ruling operation.
- **VER-005** — Execute tool calls with the service absent, stopped, degraded, failing its own checks and refusing the request, and with an API response carrying the signal; assert per case the file-fallback signal, no claim, and pass-through of the API-supplied signal.
- **VER-006** — Inspect each tool definition for its named API schema and version, and search the deliverable for any result-schema definition of its own.
- **VER-007** — Inspect the tool definitions for the two gate statements; inspect the delivered source for enabling, registration, injection or scheduling code; confirm against the profile at test time that no declaration or invocation precedes an effective tier-0 act.
- **VER-008** — Execute tool calls against a fixture access path that records the class of each request; assert every request is `agent`-class; present a refusal and assert the stated refusal and no retry; inspect the binding for owner, harness or admin credentials and for any token-mechanism choice.
- **VER-009** — Review each tool definition's description text for the non-authoritative label, the envelope and fallback pointers, and the absence of any reliance-availability statement.
- **VER-010** — Review the tool definitions for any usage requirement and for the file-route statement; run the `PKG-08` API tests with the surface absent and present and assert identical results; search PEC's other components for any dependency on the surface.
- **VER-011** — Observe the surface over an idle interval with no tool call and assert zero contact; inspect the source for timers, polling loops, push, subscription or injection hooks.
- **VER-012** — Inspect the tool definitions for governed-file content, and compare each tool result's field set against its API response for any added field.
- **VER-013** — Inspect the `PKG-08` dependency manifest and the surface's import graph for third-party runtime dependencies and network calls, and re-run the `DEL-01-05` enforcement once that deliverable is available, without discharging it here.
- **VER-014** — Inspect the surface's source and call graph for each excluded act of REQ-014 and for definitions of any artifact REQ-014 assigns to another owner.
- **VER-015** — Review the delivered source and tool definitions for a token-mechanism choice, tier-0 profile content, consumer enabling, reliance advertisement or an API schema field added outside its source packet.
- **VER-016** — Run the `PKG-08` test suite and confirm that each of VER-001 through VER-015 has a corresponding executing test or review record and that no test asserts a criterion absent from this contract.

## Governing Values and Decisions — Axiology

- **AX-001** — `PEC-K-02` files govern. A tool result is labeled, non-authoritative PEC data; it is never citable as authority over the files it cites (REQ-009).
- **AX-002** — `PEC-K-01` graceful absence. The surface is one enabled path to PEC data among others and is never required; with it absent, disabled or failing, consumers read the files (REQ-005, REQ-010).
- **AX-003** — `PEC-K-03` and `PEC-K-11` consumer-owned use. PEC offers the surface and never enables, injects or schedules it; the consumer decides whether and when to call (REQ-007, REQ-011).
- **AX-004** — Least privilege under DQ-a (CLM-003). The read-only `agent` class lets an owner enable agent query without harness ingest rights, which is why REQ-008 forbids any other credential and any escalation.
- **AX-005** — Packaging, not derivation. The surface adds no claim, citation, envelope or budget; carrying the API response unchanged keeps one state with many views and keeps each derivation with its owner (REQ-002, REQ-014).
- **AX-006** — Silence is not a claim (`PEC-ORI-007`). A failed call must say so and point to the files, which is why REQ-005 forbids empty or default results.
- **AX-007** — Open decisions stay open (`C12`). The token mechanism (`OI-006`), the transport (`OI-009`) and the tier-0 profile content are recorded as TBD-002, TBD-008 and TBD-007, not decided by this contract.
- **AX-008** — The tier-0 act is separate. This contract fixes the tool's shape so that the K3 act can transcribe it; it writes nothing under `_DomainEngines/**` and presumes no ruling (CLM-013, REQ-015).
- **AX-009** — Operational reliance is a release property. It is available only from a release that has passed the §12 gate, whose record is `DEL-10-13`'s and whose advertisement is a human release act; operational reliance is distinct from the reliance-hold control and from professional reliance (CLM-014, REQ-009).
- **AX-010** — The edges cited are `[E-P84]`, `[E-P85]` and `[E-P86]` (`DERIVED`) and `[E-P87]` (`PROPOSAL`), all seeded under `D-PEC-101`. Stratum is provenance, not authority. `RequiredMaturity` `INITIALIZED` makes the upstream *contracts* the reliable inputs, which is why CON-001 is recorded.
- **AX-011** — `C-04` `PHASE_PRECEDENCE` and `C-10` `STRATUM_RULE` are register-wide, non-gating constraints recorded in `_DEPENDENCIES.md`. Blocker output under `FULL_GRAPH` at threshold `INITIALIZED` is advisory visibility only and never work assignment.
- **AX-012** — Unknowns stay marked. TBD-001 through TBD-008 and CON-001 through CON-004 are recorded rather than resolved by inference.
- **AX-013** — This contract is lifecycle-neutral. `_STATUS.md` remains the sole lifecycle authority and is untouched by the run that authored this document; the deliverable is at `OPEN` and nothing has been built.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-099 OBJ-001 | REQ-001, CLM-002, CON-003, TBD-003, TBD-004 | AC-001 | VER-001 | Input-declaration inspection record and rejection transcripts for ingest, presence, admin and write inputs |
| OUT-001 | SOW-099 OBJ-001 | REQ-002, CLM-005, CLM-014, CON-004, TBD-005, AX-005 | AC-002 | VER-002 | Paired tool and direct API results per query kind, including paginated and truncated cases, compared field for field |
| OUT-001 | SOW-099 OBJ-001 | REQ-003, CLM-013 | AC-003 | VER-003 | File-access and network traces of tool calls over a fixture tree |
| OUT-001 | SOW-099 OBJ-001 | REQ-004, CLM-015 | AC-004 | VER-004 | Declared mode and side-effect records, before/after hashes and a call-surface inspection record |
| OUT-001 | SOW-099 OBJ-001 | REQ-005, TBD-006, AX-006 | AC-005 | VER-005 | Per-case failure transcripts showing the file-fallback signal and no claim |
| OUT-001 | SOW-099 OBJ-001 | REQ-006 | AC-006 | VER-006 | Schema-version records per definition and a search record for own result schemas |
| OUT-001 | SOW-099 OBJ-001 | REQ-007, CLM-006, CLM-013, CON-002, TBD-007, AX-003, AX-008 | AC-007 | VER-007 | Gate statements, a source inspection record and the profile state at test time |
| OUT-002 | SOW-099 OBJ-001 | REQ-008, CLM-010, CON-001, TBD-002, AX-004 | AC-008 | VER-008 | Recorded request classes, refusal transcripts and a credential and mechanism inspection record |
| OUT-001 | SOW-099 OBJ-001 | REQ-009, AX-001, AX-009 | AC-009 | VER-009 | Description-text review record per tool definition |
| OUT-001 | SOW-099 OBJ-001 | REQ-010, AX-002 | AC-010 | VER-010 | Definition review, paired API test runs with and without the surface, and a dependency search record |
| OUT-001 | SOW-099 OBJ-001 | REQ-011 | AC-011 | VER-011 | Idle-interval contact record and a source inspection record |
| OUT-001 | SOW-099 OBJ-001 | REQ-012 | AC-012 | VER-012 | Definition content inspection and result field-set comparisons |
| OUT-002 | SOW-099 OBJ-001 | REQ-013, TBD-008 | AC-013 | VER-013 | Dependency-manifest and import-graph records, plus the DEL-01-05 result once available |
| OUT-001 | SOW-099 OBJ-001 | REQ-014, CLM-011, CLM-008 | AC-014 | VER-014 | Source and call-graph inspection record against the excluded acts |
| OUT-001 | SOW-099 OBJ-001 | REQ-015, CLM-012 | AC-015 | VER-015 | Review record against the reserved decisions |
| OUT-003 | SOW-099 OBJ-001 | REQ-016, CLM-016, TBD-001 | AC-016 | VER-016 | PKG-08 test-run output mapping each executed test to its verification method |
| OUT-001 | SOW-099 OBJ-001 | CLM-001, CLM-003, CLM-004, CLM-007, CLM-009, AX-007, AX-010, AX-011, AX-012, AX-013 | AC-017 | HUMAN_REVIEW: review gate confirms traceability to SOW-099 and OBJ-001 as recorded under DL-21, confirms the packaging contribution is stated no more strongly than the objective warrant, and confirms no access-class, schema, format, budget, orientation, delta, gate, slate, presence, validation or tier-0 scope absorption | Review record citing the ledger row, the §3 objective row, DL-21 and the sibling and cross-package boundaries |
