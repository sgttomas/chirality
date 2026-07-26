---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-04
package_id: PKG-02
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@3623b958b
project_scope_refs: [SOW-014]
package_objective_refs: [OBJ-001, OBJ-002]
---

# Scope of Work — DEL-02-04 Run-evidence JSON parser

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-02-04` — "Run-evidence
JSON parser" — in `PKG-02` File-Truth Parsers of the PEC v2 build. It covers
project scope item `SOW-014` in service of package objectives `OBJ-001` and
`OBJ-002`.

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.2** (`current_basis`, SCA-002 successor; commit `3623b958b`). The
deliverable-local `_REFERENCES.md` still names "revision 1.1, accepted working
surface"; that phrase is superseded provenance left by a deferred pointer sweep
(SCA-002 `Handoff_State.md` §6), and `_CONTEXT.md`'s own supersession line
records revision 1.1 as "superseded by revision 1.2 (`current_basis`, SCA-002
successor)". This contract cites revision 1.2.

**Objective warrant.** The attribution of this deliverable to `OBJ-001` and
`OBJ-002` is SCA-002-qualified and *indirect*, not register-direct. `SOW-014`
is one of the eight items the SCA-002 Gate 3 package routes as question Q2 and
calls the INDIRECT-8 — `SOW-001` plus the seven parser items `SOW-011..017`.
The warrant is a derivation §3 of the decomposition already carried, which
SCA-002 applied rather than superseded. The Gate 3 record states it this way:

> ### The INDIRECT-8 (`DEL-01-01` + `DEL-02-01..07`) — Q2
>
> §3's mapping notes state a positive derivation: *"parser items (SOW-011..017)
> underlie OBJ-001/OBJ-002 through the record tier (SOW-001)."*
>
> **Recommended — AFFIRM** `[OBJ-001, OBJ-002]` for all eight: it applies the
> accepted §3 rationale rather than superseding it.
>
> (`Amendment_Preview.md`; ID-shaped text inside this quotation is upstream
> source context, not a local definition or reference.)

Two narrower alternatives were defined precisely and recorded, and neither was
adopted: **N1** (the seven parsers map to `OBJ-001`; `SOW-001` keeps both) and
**N2** (all eight map to `OBJ-001`). The same record states the evidence for
narrowing verbatim:

> **Evidence for narrowing, stated because it is real:** OBJ-002's register
> locus is the reconciler layer — `SOW-018` (incremental, Git-delta-keyed),
> `SOW-019` (drift classification), `SOW-006` (SHA stamping). The parsers
> produce facts the SHA comparison operates over; they do not perform it. N1
> would arguably describe the system more precisely than the §3 sentence does.

`Decision_Log.md` decision `D-17` records the same posture. Quoting its two
cells separately and identified by column, without elision — Decision:
*"INDIRECT-8 recommended at the full `[OBJ-001, OBJ-002]` set, **with the
narrower alternative stated and evidenced**"*; Rationale: *"§3's derivation is
explicit about the set, and applying it is faithful to accepted rationale. But
my own measurement shows OBJ-002's register locus is the reconciler layer
(`SOW-006/018/019`), which genuinely supports a parsers-are-`OBJ-001`-only
reading. The owner should choose knowingly rather than inherit my
preference."*

The owner ruled the question at the SCA-002 Gate 3 in-session gate
(2026-07-25), with those alternatives in front of them, in a table whose cells
read — Q: `Q2`; Question: `INDIRECT-8 breadth`; Ruling: **"AFFIRM
`OBJ-001;OBJ-002` for all eight (not N1, not N2)"**. Two consequences bind
this contract. First, the attribution is **ruled, not pending**: it is not an
open rated recommendation awaiting owner confirmation, so this contract creates
no owner-confirmation acceptance criterion for it and supplies no fresh
derivation of it. Second, unlike the nine per-row attributions batched into Q1
and Q5, the Q2 group carries **no confidence label** in the Gate 3 record; this
contract therefore asserts none and states the warrant no more strongly than
the record does. The `OBJ-002` leg rests on the §3 derivation through the
record tier, not on any claim that this deliverable performs SHA comparison —
it does not. `AC-012` puts that qualification in front of the REVIEW gate
rather than leaving it buried in the scope-change package.

- **CLM-001** — The accepted `ScopeLedger.csv` row for `SOW-014` reads in full, including its trailing fields (columns `ScopeItemID,InOutStatus,ScopeItemStatement,SourceRef,PackageID,DeliverableIDs,ObjectiveIDs,DecisionRef,OpenIssue,Notes`):

> ``SOW-014,IN,Parse run-evidence JSON: `STATUS.json` and `RUNTIME_SUMMARY.json` under `execution/**`,"PEC-RCN-002, §7.1 RunRecord",PKG-02,DEL-02-04,OBJ-001;OBJ-002,,FALSE,Daemon user-data state is presence-tier only``
>
> (`DecisionRef` empty; `OpenIssue` `FALSE`; `Notes` "Daemon user-data state is
> presence-tier only" — no open issue rides this scope item.)

- **CLM-002** — The ledger `SourceRef` cell names two loci, and both are quoted here as they read. The first is `PRD.md` §9.2 requirement `PEC-RCN-002`:

> The reconciler shall ingest, at minimum: `_STATUS.md` (declared parser
> dialect), decision registers and packets, `LOOP_RECEIPTS.md` (per-loop
> grammar; the D-APP-57 contract where a ledger has adopted it),
> `WORK_GRAPH.json` / `STATUS.json` / `RUNTIME_SUMMARY.json`, dependency
> registers, workplans/LOOP_INIT, and per-project `_harness/adapter.yaml` as
> the feed manifest.

  The second is the `RunRecord` row of `PRD.md` §7.1 "Record tier (reconciled from file truth; citable with sources)", whose `Purpose` cell reads:

> Summaries of checkout-contained AgentRun evidence (`STATUS.json`,
> `RUNTIME_SUMMARY.json` under `execution/**`); runtime-daemon state under user
> data is operational and non-authoritative (D-GOV-20 §5), is never record-tier
> citable, and enters only the presence tier

- **CLM-003** — The objective statements this deliverable serves are `OBJ-001` "Orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation" (`SOFTWARE_DECOMP.md` §3, `SourceRef` §3.1; `PRD.md` §3 outcome 1) and `OBJ-002` "Staleness is detected structurally by SHA comparison, never by judgment" (§3, `SourceRef` §3.2; `PRD.md` §3 outcome 2). Both attributions are indirect through the record tier per the warrant above.

## Deliverable Definition — Ontology

`DEL-02-04` is typed `BACKEND_FEATURE_SLICE` at Context Envelope `S` with
`PhaseHint` `P1`. `Deliverables.csv` records its `AnticipatedArtifacts` as
"Parser + fixture tests" and leaves `ContextEnvelopeNotes` empty, so there are
no envelope notes to carry forward and `_CONTEXT.md` records "(none)". The
outputs of this contract are bounded by that artifact naming: exactly the
parser and its fixture tests, and nothing beyond them.

- **OUT-001** — A run-evidence JSON parser in the PEC service core: it reads `STATUS.json` and `RUNTIME_SUMMARY.json` files under `execution/**` in the checkouts it is pointed at, parses them under a declared grammar, and emits RunRecord summaries carrying citation provenance to their live sources.
- **OUT-002** — A fixture test suite covering the parser against well-formed, malformed, unreadable, absent, and schema-unrecognized run-evidence fixtures, implementing the verification methods declared in this contract.

### Identity of record

- **CLM-004** — `DEL-02-04` is named "Run-evidence JSON parser", Type `BACKEND_FEATURE_SLICE`, Context Envelope `S`, `PhaseHint` `P1`, `ResponsibleParty` `TBD`, `CoversScopeItems` `SOW-014`, `SupportsObjectives` `OBJ-001;OBJ-002`, `ContextEnvelopeNotes` empty, with the register `Description` field reading "`STATUS.json` / `RUNTIME_SUMMARY.json` under `execution/**` into RunRecord summaries." Sources: `Deliverables.csv` row `DEL-02-04` and the `SOFTWARE_DECOMP.md` §5 PKG-02 table row "| DEL-02-04 | Run-evidence JSON parser | BACKEND_FEATURE_SLICE | S | P1 | SOW-014 |". The `Description` field is the sole register statement of the parser's output target: RunRecord summaries.
- **CLM-005** — The seven-way split of `PEC-RCN-002` into `SOW-011..017` is decision-log entry `DL-4` (2026-07-24), whose Decision cell reads "PEC-RCN-002's enumerated feed list is split into seven scope items (SOW-011..017), one per feed kind" and whose Rationale cell reads "Each feed is a separately testable parser with its own grammar; a single \"ingest everything\" item is not atomic". This deliverable is one feed kind: run-evidence JSON. The other six feeds belong to `DEL-02-01` through `DEL-02-03` and `DEL-02-05` through `DEL-02-07`.
- **CLM-006** — The `PKG-02` package charter (`SOFTWARE_DECOMP.md` §4) is "Read-side grammars over governed files: `_STATUS.md` dialect, decision registers/packets, receipts ledgers, run-evidence JSON, dependency registers, workplans/LOOP_INIT, `adapter.yaml` manifests", covering "SOW-011..017 (7)", with "Writing anything; interpretation beyond declared grammars" recorded as explicitly out of package scope.

### Placement in the work graph

- **CLM-007** — This deliverable has exactly one accepted `EXECUTION` upstream edge, `[E-P06]`, held as `Dependencies.csv` register row `DEP-02-04-003`. Attributed by column: `DependencyClass` `EXECUTION`, `AnchorType` `NOT_APPLICABLE`, `Direction` `UPSTREAM`, `DependencyType` `PREREQUISITE`, `TargetType` `DELIVERABLE`, `TargetPackageID` `PKG-01`, `TargetDeliverableID` and `TargetRefID` `DEL-01-01`, `TargetName` "Record-tier schema & entity model", `TargetLocation` `execution/PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model`, `Statement` "Parser emits RunRecord entities", `EvidenceFile` `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md`, `SourceRef` and `EvidenceQuote` both "§3 mapping notes (as E-P03)", `Explicitness` `IMPLICIT`, `RequiredMaturity` `INITIALIZED`, `ProposedMaturity` `TBD`, `SatisfactionStatus` `PENDING`, `Confidence` `MEDIUM`, `Origin` `EXTRACTED`, `FirstSeen` and `LastSeen` `2026-07-25`, `Status` `ACTIVE`, `Notes` "PROPOSAL; Flag=none; EdgeID=E-P06". The "(as E-P03)" shorthand is a back-reference to the sibling edge whose `BasisCitation` carries the §3 mapping-note text in full; the gate exhibit's own edge-register row for `E-P06` (columns `EdgeID,PredecessorID,SuccessorID,Stratum,EdgeKind,Flag,BasisCitation,Rationale`) reads `E-P06,DEL-01-01,DEL-02-04,PROPOSAL,CONSUMES,,§3 mapping notes (as E-P03),Parser emits RunRecord entities`, with `Flag` empty. The two remaining rows in this deliverable's register are the `ANCHOR` rows `DEP-02-04-001` (package-local to `PKG-02`) and `DEP-02-04-002` (`SOW-014` requirement trace).
- **CLM-008** — `DEL-01-01` is at lifecycle state `INITIALIZED`, which is the maturity `[E-P06]` requires. `INITIALIZED` means its **contract** is the reliable input: `DEL-01-01`'s accepted `ScopeOfWork.md` exists; no schema, no entity model, and no code do. Nothing in this contract asserts that any upstream artifact exists or has been built. The output-typing obligations this parser binds to are that contract's stated obligations, quoted here:

> - **REQ-001** — The schema and entity model shall define exactly the fourteen
>   record-tier entity types named in CLM-005 — Loop, Workplan, Step, Gate,
>   Receipt, DecisionRow, Fence, Package, Deliverable, DependencyEdge,
>   RunRecord, CandidateBrief, OrientationSnapshot, DriftFinding — with none
>   added and none dropped, and each type shall carry a recorded trace to its
>   `PRD.md` §7.1 row and stated purpose (CLM-006).
> - **REQ-003** — Every record-tier entity type shall carry provenance
>   sufficient for a per-claim citation to its live source — file path, anchor,
>   and/or SHA, per `PEC-ORI-004` — because §7.1 defines the tier as "citable
>   with sources". ...
> - **REQ-005** — Every record-tier entity shall be fully regenerable from file
>   sources. No record-tier field may hold state that cannot be reproduced by
>   rebuilding from the same sources, per `PEC-K-02` ...
> - **REQ-006** — No presence-tier entity shall be defined by this deliverable
>   (`PEC-K-05`, CLM-011). RunRecord shall admit only summaries of
>   checkout-contained AgentRun evidence (`STATUS.json`, `RUNTIME_SUMMARY.json`
>   under `execution/**`); runtime-daemon state under user data is operational
>   and non-authoritative per `D-GOV-20` §5, is never record-tier citable, and
>   shall not be representable in this schema.
> - **AC-005** — No presence-tier entity is defined in this schema, and a
>   fixture carrying runtime-daemon user-data state is not representable as a
>   RunRecord.
>
> (`DEL-01-01/ScopeOfWork.md`, Epistemology section; the `REQ-003` and
> `REQ-005` quotations are elided at the ellipses. ID-shaped text inside this quotation is upstream
> source context, not a local definition or reference — this contract's own
> `REQ-*` and `AC-*` records are separate and differently worded.)

- **CLM-009** — The one declared downstream consumer is `DEL-03-01` (Full-rebuild reconciler (one command)) via `[E-P22]`, whose gate-exhibit row carries `BasisCitation` "PEC-RCN-002 feed list (DL-4)" and `Rationale` "Full rebuild ingests run-evidence JSON", with `Flag` empty. That edge is informational here; it lives in the consumer's register and imposes no obligation on this deliverable beyond the outputs declared above.
- **CLM-010** — Phase staging, checked against the `PhaseHint` column of `Deliverables.csv` for every deliverable this contract names in its own voice: `DEL-02-04` itself, its upstream `DEL-01-01`, its sibling parsers `DEL-02-01`, `DEL-02-02`, `DEL-02-03`, `DEL-02-05`, `DEL-02-06`, `DEL-02-07`, and the cited consumers and neighbours `DEL-01-03`, `DEL-01-05`, `DEL-03-01`, `DEL-03-02`, `DEL-03-03`, `DEL-04-03`, `DEL-04-05`, and `DEL-10-02` are all `P1`. The one exception this contract names in its own voice is `DEL-01-02` (Presence-tier schema & entity model), which is `P3`; it is cited only as the owner of scope this deliverable does not touch. No claim in this contract stages any named deliverable into a different phase.

### Boundaries

- **CLM-011** — The acts adjacent to this parser are owned elsewhere and are cited here, never discharged. The record-tier entity model that types this parser's output, RunRecord included, is `DEL-01-01` (`SOW-001`). The other six feed grammars are `DEL-02-01` through `DEL-02-03` and `DEL-02-05` through `DEL-02-07` (`SOW-011`..`SOW-013`, `SOW-015`..`SOW-017`); in particular `WORK_GRAPH.json` belongs to `DEL-02-05` under `SOW-015`, whose ledger `Notes` cell reads "`WORK_GRAPH.json` feeds DependencyEdge, not RunRecord". Full rebuild by one command is `DEL-03-01` (`SOW-010`, `SOW-021`); incremental Git-delta reconcile is `DEL-03-02` (`SOW-018`) and drift classification is `DEL-03-03` (`SOW-019`); examined-SHA and freshness stamping with per-claim citation attachment is `DEL-04-03` (`SOW-006`, `SOW-007`); rendering a measurement limitation into an orientation response is `DEL-04-05` (`SOW-009`); the gitignored store and its ingest-boundary content-minimal guard are `DEL-01-03` (`SOW-056`); standing zero-dependency and locality enforcement is `DEL-01-05` (`SOW-052`, `SOW-053`); the standing kill test is `DEL-10-02` (`SOW-055`); the presence tier is `DEL-01-02` (`SOW-002`). This contract produces only the parser and its fixture tests.
- **CLM-012** — `PEC-K-05` requires the two trust tiers never be blurred: "Record tier: reconciled from file truth, per-claim citations. Presence tier: TTL'd, heartbeat-aged, evaporating, honesty-labeled. Presence facts never enter record-tier citations." The `SOW-014` ledger `Notes` cell and the `PRD.md` §7.1 RunRecord row together place the boundary exactly where this parser meets it: checkout-contained run evidence under `execution/**` is record-tier input; runtime-daemon state under user data is presence-tier only and is not this deliverable's input at all.
- **CLM-013** — The deliverable is at lifecycle state `OPEN` with no implementation present. Every requirement, acceptance criterion, and verification method below states a contract on future production; none asserts that anything has been built.
- **CLM-014** — Observed corpus condition, recorded as observation and not as specification. A census of this checkout on 2026-07-25 finds **342** files named `STATUS.json` and **24** named `RUNTIME_SUMMARY.json` beneath a path segment `execution`, distributed across the root loop's `execution/` tree (272 and 21) and the projects `chirality-app-dev` (54 and 1) and `chirality-piping` (16 and 2). All 366 parse as well-formed JSON today. Their shape is heterogeneous: **189** of the 342 `STATUS.json` files carry no `schema` key at all, those that do carry **24** distinct `schema` values, and the corpus presents **1,096** distinct top-level keys; for `RUNTIME_SUMMARY.json`, 9 of 24 carry no `schema` key, 3 distinct `schema` values appear, and 115 distinct top-level keys. The `projects/pec` tree contains **zero** files of either name. These files are the corpus the parser will meet; they are not a contract, and no accepted PEC source adopts any of their shapes.

- **TBD-001** — `ResponsibleParty` is unassigned; the register records `TBD`, with assignment at WORKING_ITEMS activation and not in this contract (`SOFTWARE_DECOMP.md` §5 preamble; `_CONTEXT.md`).
- **TBD-002** — The grammar this parser declares — which keys of `STATUS.json` and `RUNTIME_SUMMARY.json` it reads, their semantics, how it recognizes a declared `schema` value, and how it treats a file carrying none — is fixed by no accepted source. It is chosen during production within REQ-002 and CLM-006, against the corpus condition of CLM-014.
- **TBD-003** — The field set of a RunRecord summary is not enumerated by any accepted source. `PRD.md` §7.1 says "Summaries of checkout-contained AgentRun evidence" without listing fields, and the upstream contract quoted in CLM-008 obliges the RunRecord type to exist and bounds what it may admit without enumerating what it holds. The concrete summary shape therefore arrives from `DEL-01-01`'s production; this contract binds the parser to that type rather than defining it (REQ-003, CON-002).
- **TBD-004** — How a run-evidence file is bound to the loop, package, or deliverable it belongs to is fixed by no accepted source. Some observed files carry `package_id` or `deliverable_id` keys and most do not (CLM-014); whether binding is derived from path position, from file content, or from the feed manifest is a production choice within TBD-002, and it is not settled here.

## Completion and Reliance Basis — Epistemology

The requirements below state what future production must satisfy. Nothing in
this section asserts that a parser, a fixture, or a test exists.

- **REQ-001** — The parser shall read files named `STATUS.json` and `RUNTIME_SUMMARY.json` located beneath `execution/**` in the checkouts it is pointed at, and shall emit from them RunRecord summaries, per the `SOW-014` statement (CLM-001) and the register `Description` (CLM-004).
- **REQ-002** — The parser shall document the grammar it consumes — every key it reads and that key's semantics — and shall let no undeclared key influence its output, per the `PKG-02` out-of-scope line "interpretation beyond declared grammars" (CLM-006). Where a file declares a `schema` value the parser does not recognize, and where a file declares none, the grammar shall state what the parser does; silent best-effort interpretation of unrecognized shapes is prohibited.
- **REQ-003** — The parser's emitted summaries shall be typed as the RunRecord entity of the upstream record-tier entity model quoted in CLM-008. This deliverable shall define no record-tier entity type of its own, shall add no type to that model, and shall not depend on any upstream artifact existing; it depends on the upstream contract only (CON-002).
- **REQ-004** — The parser shall admit only checkout-contained run evidence beneath `execution/**`. Runtime-daemon state under user data shall not be an input and shall not be representable in any emitted summary, per the `SOW-014` ledger note "Daemon user-data state is presence-tier only", the `PRD.md` §7.1 RunRecord row (CLM-002), `D-GOV-20` §5, and `PEC-K-05` (CLM-012).
- **REQ-005** — Every emitted summary shall carry provenance sufficient for a per-claim citation to its live source — file path, anchor, and/or SHA — per `PEC-ORI-004` and the upstream provenance obligation quoted in CLM-008. Attaching citations to an orientation response is `DEL-04-03`'s act under `SOW-007` (CLM-011); this requirement obliges the parser to carry what that act needs, and no more.
- **REQ-006** — Where a run-evidence file is absent, unreadable, malformed as JSON, or carries a shape the declared grammar does not recognize, the parser shall report that condition explicitly to its caller, naming the file and the fault; a silently dropped, empty, partial, or defaulted summary is prohibited, per `PEC-ORI-006` ("Where a feed is unparseable or stale, the response shall state the measurement limitation explicitly; silent omission is prohibited"). Rendering such a limitation into an orientation response is `SOW-009` / `DEL-04-05` scope (CLM-011); this deliverable makes the limitation available to that consumer.
- **REQ-007** — The parser shall create, modify, or delete no source file, including the run-evidence files it reads, per `PEC-RCN-004` ("it shall never modify a source file"), `PEC-RCN-006` ("The reconciler writes only its own store and generated views"), and the `PKG-02` out-of-scope line "Writing anything".
- **REQ-008** — The emitted summaries shall be content-minimal: paths, counts, identifiers, states, SHAs, and hashes, never file or diff content, per `PEC-K-10`. The observed corpus embeds free prose in fields such as blockers, unknowns, and returns (CLM-014); the parser shall not carry that prose into the record tier. Enforcement at the ingest boundary is `DEL-01-03`'s guard under `SOW-056` (CLM-011); this requirement binds what the parser emits so that the guard has nothing to admit.
- **REQ-009** — The parser shall be deterministic over its inputs: the same file set at the same content shall yield the same summaries, so that the record tier remains fully regenerable from sources per `PEC-K-02` and the upstream regenerability obligation quoted in CLM-008. The rebuild command itself is `DEL-03-01`'s under `SOW-010` (CLM-011).
- **REQ-010** — The parser and its fixtures shall introduce no third-party runtime dependency and no external network egress, per `PEC-SVC-001` and `PEC-SVC-002`, whose standing enforcement is `DEL-01-05` covering `SOW-052` and `SOW-053`.
- **REQ-011** — The parser shall parse no feed owned by a sibling deliverable and shall perform no act owned by another package. In particular it shall not read `WORK_GRAPH.json` (`DEL-02-05` / `SOW-015`), shall emit no DependencyEdge, Receipt, DecisionRow, or Workplan/Step/Gate entity, and shall perform no reconciliation, drift classification, freshness stamping, or citation attachment (CLM-011).
- **REQ-012** — Tests shall implement the verification methods declared in this contract; they shall not define scope, requirements, or acceptance criteria.

- **AC-001** — The parser reads a well-formed fixture pair and yields exactly the RunRecord summaries the fixture declares; every key it reads appears in the documented grammar; altering an undeclared key in the fixture changes nothing in its output; and a fixture with an unrecognized `schema` value and a fixture with no `schema` key are each handled as the documented grammar states.
- **AC-002** — Every emitted summary is an instance of the upstream RunRecord type as that contract obliges it; no record-tier entity type is defined in this deliverable's source; and no element of this deliverable asserts or requires that an upstream schema, entity model, or store exists.
- **AC-003** — Only files beneath `execution/**` are read, and a fixture carrying runtime-daemon user-data state produces no summary and no record-tier field, so no presence fact can reach a record-tier citation through this parser.
- **AC-004** — Every emitted summary resolves to its live source: for a sample of each fixture kind, the recorded provenance is present and locatable by path, anchor, and/or SHA.
- **AC-005** — For absent, unreadable, malformed-JSON, and schema-unrecognized fixtures, the parser returns an explicit limitation naming the file and the fault, and never a silently dropped, empty, partial, or defaulted summary in its place.
- **AC-006** — A parser run over a fixture corpus leaves that corpus byte-identical, and the module contains no write, create, or delete call against any source path.
- **AC-007** — The emitted summaries for a prose-bearing fixture contain no file content, no diff content, and no free-prose payload carried from the run-evidence file; only paths, counts, identifiers, states, SHAs, and hashes appear.
- **AC-008** — Two runs of the parser over the same unchanged fixture corpus produce identical summaries, and inspection finds no emitted field whose value a rebuild from the same sources could not reproduce.
- **AC-009** — The parser and its fixtures add no third-party runtime dependency and make no network call, leaving the `DEL-01-05` zero-dependency and locality assertion intact.
- **AC-010** — The parser reads no sibling feed — `WORK_GRAPH.json` included — emits no entity type other than RunRecord, and performs no reconciliation, drift-classification, stamping, or citation-attachment act owned by `PKG-03` or `PKG-04`.
- **AC-011** — The fixture test suite implements VER-001 through VER-010, executes in the `PKG-02` test run, passes, and introduces no acceptance criterion absent from this contract.
- **AC-012** — The REVIEW gate confirms this contract's traceability to `SOW-014`, `OBJ-001`, and `OBJ-002` as ruled at SCA-002 Gate 3 Q2, confirms that the indirect `OBJ-002` leg is stated no more strongly here than the Gate 3 record states it — including the recorded and unadopted N1 narrowing evidence and the absence of a confidence label on that group — and confirms that no `PKG-01`, sibling `PKG-02`, `PKG-03`, or `PKG-04` scope has been absorbed.

- **CON-001** — No accepted source declares a schema for `STATUS.json` or `RUNTIME_SUMMARY.json`. The corpus measured in CLM-014 is heterogeneous by a wide margin — most `STATUS.json` files declare no schema at all, those that do declare two dozen different ones, and over a thousand distinct top-level keys appear across the set. `PKG-02`'s charter permits a declared grammar and forbids "interpretation beyond declared grammars"; those two facts are in tension for this feed, because a grammar narrow enough to be declarable will not describe most of the corpus, and a grammar wide enough to describe the corpus is interpretation. This contract records the tension rather than resolving it: REQ-002 requires the grammar to be declared and to state its own behaviour on unrecognized shapes, and REQ-006 requires every file the grammar does not cover to surface as an explicit limitation rather than a silent omission. Choosing the grammar's breadth is a production decision bounded by those requirements; extending this deliverable to interpret shapes it has not declared would be a scope-change question, not a production decision.
- **CON-002** — The RunRecord summary field set is owned upstream and does not yet exist. `DEL-01-01` is `INITIALIZED`: its contract obliges the RunRecord type and bounds what it may admit (CLM-008), but neither it nor any accepted source enumerates the type's fields (TBD-003). This parser's output typing therefore binds to an obligation, not to an artifact. Nothing in this contract defines, anticipates, or constrains that field set, and a production choice here that fixed it would take a decision in the wrong place.
- **CON-003** — The corpus this parser is first expected to meet is empty at the point of first reading. `OI-010`, resolved at Gate 2 (2026-07-24), records that "... the first loop the P1 reconciler ingests is PEC v2's own build (bootstrap as thesis validation) ...", and the `projects/pec` tree contains no `STATUS.json` and no `RUNTIME_SUMMARY.json` today (CLM-014). This is recorded as a stated condition, not a defect and not a licence to widen the read scope: the parser's coverage of a loop with no run evidence is a limitation to be stated under REQ-006, and reaching outside `execution/**` to find inputs is prohibited by REQ-004.

## Production and Verification Method — Praxeology

Production proceeds in the order corpus survey → declared grammar → parser →
limitation reporting → fixtures and tests, because each stage is the acceptance
surface of the next and because the grammar cannot be declared honestly before
the corpus condition of CLM-014 has been examined against the accepted sources.
All work is bounded to this deliverable folder and the `PKG-02` service-core
source it names; this contract authorizes no register, decomposition, PRD, or
upstream-deliverable edit, and it neither defines nor reshapes the record-tier
entity model it emits into. Tests implement the verification methods below and
create no scope.

- **VER-001** — Execute the parser over a well-formed fixture pair and assert the emitted summaries equal the fixture's declared expectation; compare the set of keys actually read, by instrumentation or code inspection, against the documented grammar; mutate an undeclared key to assert output invariance; and execute the unrecognized-`schema` and absent-`schema` fixtures, asserting the documented behaviour in each case.
- **VER-002** — Inspect this deliverable's source for any record-tier type definition and assert none is present; assert every emitted summary is constructed against the upstream RunRecord type as the contract quoted in CLM-008 obliges it; and grep the source and fixtures for any assumption that an upstream schema, model, or store exists, asserting none.
- **VER-003** — Tier-boundary exercise: point the parser at a fixture tree containing files beneath and outside `execution/**` plus a runtime-daemon user-data state fixture, and assert that only the `execution/**` files are read and that the daemon-state fixture yields no summary and no record-tier field.
- **VER-004** — Provenance resolution: for a sample summary from each fixture kind, resolve the recorded provenance to a live file source and assert that path, anchor, and/or SHA are present and locatable.
- **VER-005** — Execute the parser against absent, unreadable, malformed-JSON, and schema-unrecognized fixtures and assert, per case, an explicit limitation naming the file and the fault, with no dropped, empty, partial, or defaulted summary returned.
- **VER-006** — Hash the fixture corpus tree before and after a parser run and assert byte-identity; inspect the module's call graph for write, create, or delete operations against any source path.
- **VER-007** — Content-minimal inspection: run the parser over a fixture whose run-evidence fields carry free prose, diff-shaped text, and file content, and assert field by field that the emitted summaries carry none of it, only paths, counts, identifiers, states, SHAs, and hashes.
- **VER-008** — Determinism check: run the parser twice over the same unchanged fixture corpus and assert the emitted summaries are identical; inspect the emitted field inventory for any value the parser did not derive from the source files.
- **VER-009** — Inspect the `PKG-02` dependency manifest and this module's import graph for third-party runtime dependencies and network calls, and re-run the `DEL-01-05` zero-dependency and locality enforcement once that deliverable is available, without discharging it here.
- **VER-010** — Boundary inspection: assert the parser opens no file named `WORK_GRAPH.json` or any other sibling feed, emits no entity type other than RunRecord, and contains no reconciliation, drift-classification, stamping, or citation-attachment code path.
- **VER-011** — Run the `PKG-02` test suite and confirm that each of VER-001 through VER-010 has a corresponding executing automated test and that no test asserts a criterion absent from this contract.

## Governing Values and Decisions — Axiology

- **AX-001** — `OBJ-001` governs: orientation is a sub-second query with per-claim citations. A run-evidence summary that cannot say which file it came from cannot serve a cited orientation, whatever else it holds; provenance is therefore a property of what this parser emits (REQ-005) rather than a decoration added downstream.
- **AX-002** — `OBJ-002` governs indirectly, through the record tier. This deliverable produces facts the SHA comparison operates over; it does not perform that comparison, and no requirement here may be read as claiming otherwise. Its contribution to the objective is that its output is deterministic and regenerable (REQ-009), so a difference between two reconciles is a structural difference and never a judgment.
- **AX-003** — `PEC-K-05` governs the tier boundary, and this feed is where the boundary is most easily blurred: the same run produces checkout-contained evidence and daemon user-data state, and only the first is record-tier. `SOW-014`'s own ledger note draws the line. REQ-004 enforces it at the input, so that presence facts have no route into a record-tier citation through this parser.
- **AX-004** — `PEC-K-10` content-minimal is a residency posture, not a storage optimization, and this feed carries the most prose of any in `PKG-02`: the observed corpus embeds blocker text, unknowns, and whole agent returns inside JSON fields (CLM-014). The strongest available enforcement is emitting a summary that has nowhere to put prose (REQ-008); the ingest-side guard is `DEL-01-03`'s.
- **AX-005** — `PEC-K-02` files govern: run-evidence JSON is authored project truth and PEC's summary of it is a projection, regenerable and never citable as authority over the file itself. `PEC-RCN-004` and `PEC-RCN-006` make the read-only posture a rule rather than a habit (REQ-007).
- **AX-006** — `PEC-K-01` graceful absence governs: no governed act may require a PEC read or write. A loop with no run evidence — which is the pec loop's condition today (CON-003) — is a stated coverage limitation, never a blocked act and never a silent gap.
- **AX-007** — `DL-4` is the decision that makes this deliverable atomic: one feed kind, one separately testable unit, one declared grammar. Absorbing a sibling feed grammar (`DEL-02-01`..`DEL-02-03`, `DEL-02-05`..`DEL-02-07`), the entity model that types this output (`DEL-01-01`), the reconciler that consumes it (`DEL-03-01`), or the limitation-honesty surface (`DEL-04-05`) would undo that decision. REQ-011 states the boundary as a requirement so that it is checkable.
- **AX-008** — The edges `[E-P06]` (upstream, `DEL-01-01` → `DEL-02-04`) and `[E-P22]` (downstream, `DEL-02-04` → `DEL-03-01`) are `PROPOSAL` stratum and are accepted: `D-PEC-62` §1(4) accepted the candidate DAG v0.2 exhibit "all strata as presented", read in that packet as carrying the exhibit's flags as flags, so what remains recorded-but-unresolved is the specific annotated set (E-A11, E-P69/E-N02, E-N13/E-N18, the C-02 direction, the C-08 standing-node set) — none of which touches `E-P06` or `E-P22`, both of which carry an empty `Flag` column in the exhibit. Stratum is provenance, not authority: it records how an edge was derived, not whether it has been accepted, and citation does not convert `PROPOSAL` to `DECLARED`.
- **AX-009** — Edge direction is a constraint on this contract, not a licence. `RequiredMaturity` `INITIALIZED` on `[E-P06]` means the upstream *contract* is the reliable input, not any upstream artifact; this contract is written against the obligations quoted in CLM-008 and asserts nothing about upstream implementation state. Consuming that contract imposes no obligation on `DEL-01-01`, and being consumed by `DEL-03-01` neither expands nor transfers scope in either direction.
- **AX-010** — Unknowns stay marked. TBD-001 through TBD-004 and CON-001 through CON-003 are recorded rather than resolved by inference. `C-04` `PHASE_PRECEDENCE` and `C-10` `STRATUM_RULE` are register-wide non-gating constraints recorded in `_DEPENDENCIES.md`, and blocker output under the `FULL_GRAPH` mode at threshold `INITIALIZED` is advisory visibility only, never work assignment.
- **AX-011** — This contract is lifecycle-neutral. `_STATUS.md` remains the sole lifecycle authority and is untouched by the run that authored this document; the deliverable is at `OPEN` and nothing has been built.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-014 OBJ-001 OBJ-002 | REQ-001, REQ-002, CLM-001, CLM-002, CLM-004, CLM-006, CLM-014, TBD-002, CON-001 | AC-001 | VER-001 | Grammar documentation, the well-formed fixture pair and parser output, the undeclared-key invariance result, and per-case transcripts for the unrecognized-schema and absent-schema fixtures |
| OUT-001 | SOW-014 OBJ-001 OBJ-002 | REQ-003, CLM-008, TBD-003, CON-002 | AC-002 | VER-002 | The summary construction surface against the quoted upstream RunRecord obligation, plus a recorded search of this deliverable's source for record-tier type definitions and upstream-artifact assumptions |
| OUT-001 | SOW-014 OBJ-001 OBJ-002 | REQ-004, CLM-012, AX-003 | AC-003 | VER-003 | Tier-boundary exercise transcript over a mixed fixture tree showing only `execution/**` files read and the daemon-state fixture yielding no summary |
| OUT-001 | SOW-014 OBJ-001 OBJ-002 | REQ-005, CLM-011 | AC-004 | VER-004 | Per-fixture-kind provenance resolution records showing path, anchor, and/or SHA present and locatable |
| OUT-001 | SOW-014 OBJ-001 OBJ-002 | REQ-006, CON-003, TBD-004, AX-006 | AC-005 | VER-005 | Per-case transcripts for absent, unreadable, malformed-JSON, and schema-unrecognized fixtures, each showing the file named and the fault located |
| OUT-001 | SOW-014 OBJ-001 OBJ-002 | REQ-007, AX-005 | AC-006 | VER-006 | Before/after fixture-corpus tree hashes and a call-graph inspection record showing no write path against a source file |
| OUT-001 | SOW-014 OBJ-001 OBJ-002 | REQ-008, AX-004 | AC-007 | VER-007 | Field-by-field inspection of the summaries emitted for a prose-bearing fixture against the declared grammar |
| OUT-001 | SOW-014 OBJ-001 OBJ-002 | REQ-009, AX-002 | AC-008 | VER-008 | Two-run output comparison over an unchanged fixture corpus plus the emitted-field derivation inspection |
| OUT-001 | SOW-014 OBJ-001 OBJ-002 | REQ-010 | AC-009 | VER-009 | Dependency-manifest and import-graph inspection records, plus the DEL-01-05 enforcement result once that deliverable is available |
| OUT-001 | SOW-014 OBJ-001 OBJ-002 | REQ-011, CLM-005, CLM-009, CLM-010, AX-007, AX-009 | AC-010 | VER-010 | Recorded search showing no sibling feed opened and no entity type other than RunRecord emitted, with the reconciliation, stamping, and citation-attachment code paths absent |
| OUT-002 | SOW-014 OBJ-001 OBJ-002 | REQ-012, CLM-013 | AC-011 | VER-011 | PKG-02 test-run output mapping each executed test to its declared verification method, with no criterion asserted that this contract does not state |
| OUT-001 | SOW-014 OBJ-001 OBJ-002 | CLM-003, AX-001, AX-008, AX-010, AX-011 | AC-012 | HUMAN_REVIEW: REVIEW gate confirms traceability to SOW-014 and to OBJ-001/OBJ-002 as ruled at SCA-002 Gate 3 Q2, confirms the indirect OBJ-002 leg is stated no more strongly than that record states it given the unadopted N1 narrowing evidence and the absence of a confidence label, and confirms no sibling or cross-package scope absorption | Review record citing the scope-ledger row, the Gate 3 Q2 ruling and D-17, and the sibling and cross-package deliverable boundaries |
