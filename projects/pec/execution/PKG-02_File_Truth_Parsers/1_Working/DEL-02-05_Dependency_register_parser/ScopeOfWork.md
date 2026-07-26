---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-05
package_id: PKG-02
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@3623b958b
project_scope_refs: [SOW-015]
package_objective_refs: [OBJ-001, OBJ-002]
---

# Scope of Work — DEL-02-05 Dependency register parser

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-02-05` — "Dependency
register parser" — in `PKG-02` File-Truth Parsers of the PEC v2 build. It
covers project scope item `SOW-015` in service of package objectives `OBJ-001`
and `OBJ-002`.

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.2** (`current_basis`, SCA-002 successor; commit `3623b958b`). The
deliverable-local `_REFERENCES.md` still names "revision 1.1, accepted working
surface"; that phrase is superseded provenance left by a deferred pointer sweep
(SCA-002 `Handoff_State.md` §6), and `_CONTEXT.md`'s own supersession line
records revision 1.1 as "superseded by revision 1.2 (`current_basis`, SCA-002
successor)". This contract cites revision 1.2.

**Objective warrant.** The attribution of this deliverable to `OBJ-001` and
`OBJ-002` is SCA-002-qualified and *indirect*, not a register-direct
derivation restated here. `SOW-015` is one of the eight items the SCA-002
Gate 3 package routes as question Q2 and names the INDIRECT-8 — `SOW-001` plus
the seven parser items `SOW-011..017`. The warrant is a §3 derivation the
decomposition already carried, which SCA-002 applied rather than superseded.
The Gate 3 record states it this way:

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

Two narrower variants were defined precisely in the same record and neither was
adopted: **N1** (the seven parsers map to `OBJ-001`; `SOW-001` keeps both) and
**N2** (all eight map to `OBJ-001`). The record states the evidence for
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
(2026-07-25) with those alternatives in front of them, in a table whose cells
read — Q: `Q2`; Question: `INDIRECT-8 breadth`; Ruling: **"AFFIRM
`OBJ-001;OBJ-002` for all eight (not N1, not N2)"**. Two consequences bind this
contract. First, the attribution is **ruled, not pending**: it is not an open
rated recommendation awaiting owner confirmation, so this contract creates no
owner-confirmation acceptance criterion for it and supplies no fresh derivation
of it. Second, unlike the nine per-row attributions batched into Q1 and Q5, the
Q2 group carries **no confidence label** in the Gate 3 record; this contract
therefore asserts none and states the warrant no more strongly than the record
does. The `OBJ-002` leg rests on the §3 derivation through the record tier, not
on any claim that this deliverable performs SHA comparison — it does not.
`AC-012` puts that qualification in front of the REVIEW gate rather than
leaving it buried in the scope-change package.

- **CLM-001** — The accepted `ScopeLedger.csv` row for `SOW-015` reads in full, including its trailing fields (columns `ScopeItemID,InOutStatus,ScopeItemStatement,SourceRef,PackageID,DeliverableIDs,ObjectiveIDs,DecisionRef,OpenIssue,Notes`):

> ``SOW-015,IN,Parse dependency registers: `Dependencies.csv` and `WORK_GRAPH.json`,"PEC-RCN-002, §7.1 DependencyEdge",PKG-02,DEL-02-05,OBJ-001;OBJ-002,,FALSE,"`WORK_GRAPH.json` feeds DependencyEdge, not RunRecord"``

> (`DecisionRef` empty; `OpenIssue` `FALSE`; `Notes` "`WORK_GRAPH.json` feeds
> DependencyEdge, not RunRecord" — no open issue rides this scope item.)

- **CLM-002** — The ledger `SourceRef` cell names two loci, and both are quoted here as they read. The first is `PRD.md` §9.2 requirement `PEC-RCN-002`:

> The reconciler shall ingest, at minimum: `_STATUS.md` (declared parser
> dialect), decision registers and packets, `LOOP_RECEIPTS.md` (per-loop
> grammar; the D-APP-57 contract where a ledger has adopted it),
> `WORK_GRAPH.json` / `STATUS.json` / `RUNTIME_SUMMARY.json`, dependency
> registers, workplans/LOOP_INIT, and per-project `_harness/adapter.yaml` as
> the feed manifest.

  The second is the `DependencyEdge` row of `PRD.md` §7.1 "Record tier (reconciled from file truth; citable with sources)", whose `Purpose` cell reads in full:

> From `Dependencies.csv` registers and `WORK_GRAPH.json`

  That one-line cell is the whole of what accepted PRD text says about this entity's sources, and it is the reason the ledger `Notes` cell exists (CLM-006).

- **CLM-003** — The objective statements this deliverable serves are `OBJ-001` "Orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation" (`SOFTWARE_DECOMP.md` §3, `SourceRef` §3.1; `PRD.md` §3 outcome 1) and `OBJ-002` "Staleness is detected structurally by SHA comparison, never by judgment" (§3, `SourceRef` §3.2; `PRD.md` §3 outcome 2). Both attributions are indirect through the record tier per the warrant above.

## Deliverable Definition — Ontology

`DEL-02-05` is typed `BACKEND_FEATURE_SLICE` at Context Envelope `S` with
`PhaseHint` `P1`. `Deliverables.csv` records its `AnticipatedArtifacts` as
"Parser + fixture tests" and leaves `ContextEnvelopeNotes` empty, so there are
no envelope notes to carry forward and `_CONTEXT.md` records "(none)". The
outputs of this contract are bounded by that artifact naming: exactly the
parser and its fixture tests, and nothing beyond them.

- **OUT-001** — A dependency register parser in the PEC service core: it reads `Dependencies.csv` registers and `WORK_GRAPH.json` files in the checkouts it is pointed at, parses each under a declared grammar, and emits DependencyEdge records carrying citation provenance to their live sources.
- **OUT-002** — A fixture test suite covering the parser against well-formed, shape-variant, malformed, unreadable, absent, and schema-unrecognized fixtures of both feeds, implementing the verification methods declared in this contract.

### Identity of record

- **CLM-004** — `DEL-02-05` is named "Dependency register parser", Type `BACKEND_FEATURE_SLICE`, Context Envelope `S`, `PhaseHint` `P1`, `ResponsibleParty` `TBD`, `CoversScopeItems` `SOW-015`, `SupportsObjectives` `OBJ-001;OBJ-002`, `AnticipatedArtifacts` "Parser + fixture tests", `ContextEnvelopeNotes` empty, with the register `Description` field reading "`Dependencies.csv` and `WORK_GRAPH.json` into DependencyEdge." Sources: `Deliverables.csv` row `DEL-02-05` and the `SOFTWARE_DECOMP.md` §5 PKG-02 table row "| DEL-02-05 | Dependency register parser | BACKEND_FEATURE_SLICE | S | P1 | SOW-015 |". The `Description` field is the sole register statement of the parser's output target: DependencyEdge.
- **CLM-005** — The seven-way split of `PEC-RCN-002` into `SOW-011..017` is decision-log entry `DL-4` (2026-07-24), whose Decision cell reads "PEC-RCN-002's enumerated feed list is split into seven scope items (SOW-011..017), one per feed kind" and whose Rationale cell reads "Each feed is a separately testable parser with its own grammar; a single \"ingest everything\" item is not atomic". This deliverable is one such item — but it is the one whose scope statement names **two** file forms, `Dependencies.csv` and `WORK_GRAPH.json` (CLM-001, CON-001). The other six feeds belong to `DEL-02-01` through `DEL-02-04` and `DEL-02-06` through `DEL-02-07`.
- **CLM-006** — The `WORK_GRAPH.json` routing this contract inherits was a corrected defect, not an original reading. Decision-log entry `DL-9` (2026-07-24) records the adversarial verification pass, and its Notable cell states, quoted at the relevant clause with the surrounding clauses elided: *"... `WORK_GRAPH.json` was routed to the wrong entity ..."*. The `SOW-015` ledger `Notes` cell is that correction as the ledger carries it: "`WORK_GRAPH.json` feeds DependencyEdge, not RunRecord". The sibling `SOW-014` ledger `Notes` cell — "Daemon user-data state is presence-tier only" — states the same boundary from the other side, but no accepted source pairs it with `DL-9`, whose Notable cell records only the `WORK_GRAPH.json` misrouting; its own basis is the `PRD.md` §7.1 RunRecord row ("runtime-daemon state under user data is operational and non-authoritative (D-GOV-20 §5), is never record-tier citable, and enters only the presence tier") read under `PEC-K-05`, and it is cited here on that basis rather than as part of the `DL-9` correction. This contract therefore treats the `WORK_GRAPH.json` → DependencyEdge routing as accepted truth to be honoured exactly, and reading that file is this deliverable's duty and no sibling's.
- **CLM-007** — The `PKG-02` package charter (`SOFTWARE_DECOMP.md` §4) is "Read-side grammars over governed files: `_STATUS.md` dialect, decision registers/packets, receipts ledgers, run-evidence JSON, dependency registers, workplans/LOOP_INIT, `adapter.yaml` manifests", covering "SOW-011..017 (7)", with "Writing anything; interpretation beyond declared grammars" recorded as explicitly out of package scope.

### Placement in the work graph

- **CLM-008** — This deliverable has exactly one accepted `EXECUTION` upstream edge, `[E-P07]`, held as `Dependencies.csv` register row `DEP-02-05-003`. Attributed by column: `RegisterSchemaVersion` `v3.1`, `DependencyID` `DEP-02-05-003`, `FromPackageID` `PKG-02`, `FromDeliverableID` `DEL-02-05`, `FromDeliverableName` "Dependency register parser", `DependencyClass` `EXECUTION`, `AnchorType` `NOT_APPLICABLE`, `Direction` `UPSTREAM`, `DependencyType` `PREREQUISITE`, `TargetType` `DELIVERABLE`, `TargetPackageID` `PKG-01`, `TargetDeliverableID` and `TargetRefID` `DEL-01-01`, `TargetName` "Record-tier schema & entity model", `TargetLocation` `execution/PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model`, `Statement` "Parser emits DependencyEdge entities", `EvidenceFile` `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md`, `SourceRef` and `EvidenceQuote` both "§3 mapping notes (as E-P03)", `Explicitness` `IMPLICIT`, `RequiredMaturity` `INITIALIZED`, `ProposedMaturity` `TBD`, `SatisfactionStatus` `PENDING`, `Confidence` `MEDIUM`, `Origin` `EXTRACTED`, `FirstSeen` and `LastSeen` `2026-07-25`, `Status` `ACTIVE`, `Notes` "PROPOSAL; Flag=none; EdgeID=E-P07". The "(as E-P03)" shorthand is a back-reference to the sibling edge whose `BasisCitation` carries the §3 mapping-note text in full; the gate exhibit's own edge-register row for `E-P07` (columns `EdgeID,PredecessorID,SuccessorID,Stratum,EdgeKind,Flag,BasisCitation,Rationale`) reads `E-P07,DEL-01-01,DEL-02-05,PROPOSAL,CONSUMES,,§3 mapping notes (as E-P03),Parser emits DependencyEdge entities`, with `Flag` empty. The two remaining rows in this deliverable's register are the `ANCHOR` rows `DEP-02-05-001` (package-local to `PKG-02`) and `DEP-02-05-002` (`SOW-015` requirement trace).
- **CLM-009** — `DEL-01-01` is at lifecycle state `INITIALIZED`, which is the maturity `[E-P07]` requires. `INITIALIZED` means its **contract** is the reliable input: `DEL-01-01`'s accepted `ScopeOfWork.md` exists; no schema, no entity model, and no code do. Nothing in this contract asserts that any upstream artifact exists or has been built. The output-typing obligations this parser binds to are that contract's stated obligations, quoted here:

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
> - **REQ-007** — No field of any type shall admit file content or diff content
>   (`PEC-K-10`: "Paths, counts, SHAs, states, hashes — never file or diff
>   content"). ... Enforcement at the ingest boundary is `DEL-01-03`'s guard
>   under `SOW-056`; this requirement binds the shape of the schema so that the
>   guard has nothing to admit into.
> - **AC-006** — No field type admits file or diff content; DecisionRow has no
>   prose-bearing field; and a fixture carrying file content, diff hunks, and
>   register-row prose cannot be expressed in the model.
>
> (`DEL-01-01/ScopeOfWork.md`, Epistemology section; the `REQ-003`, `REQ-005`,
> and `REQ-007` quotations are elided at the ellipses. ID-shaped text inside
> this quotation is upstream source context, not a local definition or
> reference — this contract's own `REQ-*` and `AC-*` records are separate and
> differently worded.)

  Its enumeration of the record-tier types names DependencyEdge, and its `DEL-01-01/CLM-006` carries the `PRD.md` §7.1 purpose cell for that type verbatim as "From `Dependencies.csv` registers and `WORK_GRAPH.json`". That is the whole of the upstream obligation this parser's output binds to: a DependencyEdge type must exist, must carry citation provenance, must be regenerable, and must have no field able to hold prose. Its field set is not enumerated anywhere (TBD-003, CON-003).

- **CLM-010** — Two declared downstream consumers are recorded in `_DEPENDENCIES.md`, both `CONSUMES` at `PROPOSAL` stratum and both unflagged. `DEL-03-01` (Full-rebuild reconciler (one command)) via `[E-P23]`, whose gate-exhibit row carries `BasisCitation` "PEC-RCN-002 feed list (DL-4)" and `Rationale` "Full rebuild ingests dependency registers". `DEL-10-10` (Directed bootstrap self-ingest validation) via `[E-P73]`, whose row carries `BasisCitation` `SOW-064: P1 "ingests PEC v2's accepted full dependency DAG"; SOW-015: dependency registers into DependencyEdge` and `Rationale` "The DAG's file form is read by the dependency register parser". Both edges are informational here; they live in the consumers' registers and impose no obligation on this deliverable beyond the outputs declared above.
- **CLM-011** — Phase staging, checked against the `PhaseHint` column of `Deliverables.csv` for every deliverable this contract names in its own voice: `DEL-02-05` itself, its upstream `DEL-01-01`, its sibling parsers `DEL-02-01`, `DEL-02-02`, `DEL-02-03`, `DEL-02-04`, `DEL-02-06`, `DEL-02-07`, and the cited consumers and neighbours `DEL-01-03`, `DEL-01-05`, `DEL-03-01`, `DEL-03-02`, `DEL-03-03`, `DEL-04-03`, `DEL-04-05`, `DEL-10-02`, and `DEL-10-10` are all `P1`. The one exception this contract names in its own voice is `DEL-01-02` (Presence-tier schema & entity model), which is `P3`; it is cited only as the owner of scope this deliverable does not touch. No claim in this contract stages any named deliverable into a different phase.

### Boundaries

- **CLM-012** — The acts adjacent to this parser are owned elsewhere and are cited here, never discharged. The record-tier entity model that types this parser's output, DependencyEdge included, is `DEL-01-01` (`SOW-001`). The other six feed grammars are `DEL-02-01` through `DEL-02-04` and `DEL-02-06` through `DEL-02-07` (`SOW-011`..`SOW-014`, `SOW-016`, `SOW-017`); in particular `STATUS.json` and `RUNTIME_SUMMARY.json` belong to `DEL-02-04` under `SOW-014`, and the `SOW-015` ledger note draws that line from this side ("`WORK_GRAPH.json` feeds DependencyEdge, not RunRecord"). Full rebuild by one command is `DEL-03-01` (`SOW-010`, `SOW-021`); incremental Git-delta reconcile is `DEL-03-02` (`SOW-018`) and drift classification is `DEL-03-03` (`SOW-019`); examined-SHA and freshness stamping with per-claim citation attachment is `DEL-04-03` (`SOW-006`, `SOW-007`); rendering a measurement limitation into an orientation response is `DEL-04-05` (`SOW-009`); the gitignored store and its ingest-boundary content-minimal guard are `DEL-01-03` (`SOW-056`); standing zero-dependency and locality enforcement is `DEL-01-05` (`SOW-052`, `SOW-053`); the standing kill test is `DEL-10-02` (`SOW-055`); the bootstrap progression record that self-ingests the accepted DAG is `DEL-10-10` (`SOW-064`); the presence tier is `DEL-01-02` (`SOW-002`). This contract produces only the parser and its fixture tests.
- **CLM-013** — This parser reads dependency registers as a data feed. It does not own, validate, amend, or adjudicate the registers themselves, nor the dependency governance they carry. Registers are decomposition truth produced by the decomposition and scope-change workflows; `D-PEC-62` §1(3) is the owner ruling that placed them, verbatim: "I think we've tried central dependency registries before and not found that desirable because it creates another surface for authority, while the deliverable local dependencies can be queried to construct a full accounting of all dependencies if needed." This deliverable's own `_DEPENDENCIES.md` restates the consequences that bind a reader of those files: "Register storage is deliverable-local by owner ruling (no central register)"; blocker output at mode `FULL_GRAPH` and threshold `INITIALIZED` "is advisory visibility only — never work assignment"; and register-wide constraint `C-10` `STRATUM_RULE` ends "All strata require owner acceptance; strata are provenance not authority". `PEC-K-06` states the same posture as an invariant: "**Observation, not participation.** Read-only over Git; no leases, no claim arbitration, no merge opinions, no dispatch; conflicts surfaced, never prevented." A cycle, a contradiction, an unsatisfied prerequisite, or a disputed stratum found in a register is a fact this parser may carry and never a verdict it may issue (REQ-008).
- **CLM-014** — `PEC-K-10` content-minimal is where this feed is most exposed, because the register schema is unusually prose-bearing: of its 29 columns, `Statement`, `EvidenceQuote`, and `Notes` hold authored natural-language text, and `SourceRef`, `TargetName`, and `FromDeliverableName` hold short authored strings. `PEC-K-10` reads "**Content-minimal.** Paths, counts, SHAs, states, hashes — never file or diff content", and `DEL-01-01`'s quoted `REQ-007` and `AC-006` bind the upstream type so that "register-row prose cannot be expressed in the model" (CLM-009). The line this parser meets is therefore drawn on its own output, not on its input: it may read a prose column in order to derive an identifier or a state, and it may not carry that column's text into an emitted edge (REQ-004, CON-002).
- **CLM-015** — The deliverable is at lifecycle state `OPEN` with no implementation present. Every requirement, acceptance criterion, and verification method below states a contract on future production; none asserts that anything has been built.
- **CLM-016** — Observed corpus condition, recorded as observation and not as specification. A census of this checkout on 2026-07-25 finds **936** files named `Dependencies.csv` and **35** named `WORK_GRAPH.json`. The two feeds are structurally unlike each other by a wide margin. All 936 registers parse as CSV; every one of their **13,452** data rows carries `RegisterSchemaVersion` `v3.1`; **930** files use one 29-column header and **6** use a 31-column header adding `EstimateImpactClass` and `ConsumerHint`; **17** quote every header cell; **64** use CRLF line endings, and those 64 are exactly the `projects/pec` registers, this deliverable's own included. `DependencyClass` takes two values across the corpus — `EXECUTION` (9,550 rows) and `ANCHOR` (3,902). By loop the registers distribute as root `execution/` 728, `chirality-piping` 93, `projects/pec` 64, `chirality-app-dev` 51. `WORK_GRAPH.json` shows the opposite condition: all 35 parse as JSON, but they present **31** distinct top-level key sets and **82** distinct top-level keys; `nodes` appears in all 35 and `edges` in only **10**; the version key is spelled `schema` in 17 files, `schema_version` in 2, and `schemaVersion` in 2, while **14** declare none at all, and the 21 that declare one carry **9** distinct values; node objects across the corpus present **220** distinct keys. They distribute as `chirality-piping` 14, root `execution/` 11, `chirality-app-dev` 10, and `projects/pec` **zero**. These files are the corpus the parser will meet; they are not a contract, and no accepted PEC source adopts any of their shapes.

- **TBD-001** — `ResponsibleParty` is unassigned; the register records `TBD`, with assignment at WORKING_ITEMS activation and not in this contract (`SOFTWARE_DECOMP.md` §5 preamble; `_CONTEXT.md`).
- **TBD-002** — The grammar this parser declares — which register columns and which `WORK_GRAPH.json` keys it reads, their semantics, how it recognizes a `RegisterSchemaVersion` and a work-graph version declaration, and how it treats a file carrying an unrecognized one or none — is fixed by no accepted source. It is chosen during production within REQ-002 and CLM-007, against the corpus condition of CLM-016.
- **TBD-003** — The field set of a DependencyEdge is not enumerated by any accepted source. `PRD.md` §7.1 gives the type a one-line source cell and no fields (CLM-002), and the upstream contract quoted in CLM-009 obliges the type to exist and bounds what it may admit without enumerating what it holds. The concrete edge shape therefore arrives from `DEL-01-01`'s production; this contract binds the parser to that type rather than defining it (REQ-003, CON-003).
- **TBD-004** — Edge identity in the register is not carried in a column. In the seeded `v3.1` rows the edge identifier, stratum, and flag live inside the free-text `Notes` cell — this deliverable's own upstream row reads `Notes` "PROPOSAL; Flag=none; EdgeID=E-P07" — and the census finds **120** rows repo-wide carrying an `EdgeID=` token in `Notes` against 13,452 rows total (CLM-016). Whether the parser recovers edge identity, stratum, and flag from that cell, derives them structurally, or declines to represent them is fixed by no accepted source; it is a production choice bounded by REQ-002 and REQ-004 and it interacts directly with CON-002.
- **TBD-005** — How a `WORK_GRAPH.json` maps to DependencyEdge records is fixed by no accepted source. `nodes` is the only universal key and `edges` appears in fewer than a third of the files (CLM-016), so whether an edge is read from an explicit `edges` array, derived from a node-level dependency key, or reported as uncovered is a production choice within TBD-002 and CON-001. Nothing in this contract settles it.

## Completion and Reliance Basis — Epistemology

The requirements below state what future production must satisfy. Nothing in
this section asserts that a parser, a fixture, or a test exists.

- **REQ-001** — The parser shall read `Dependencies.csv` registers and `WORK_GRAPH.json` files in the checkouts it is pointed at, and shall emit from them DependencyEdge records, per the `SOW-015` statement (CLM-001), the register `Description` (CLM-004), and the `PRD.md` §7.1 DependencyEdge source cell (CLM-002). Both named file forms are in scope; neither may be dropped in favour of the other (CLM-006).
- **REQ-002** — The parser shall document the grammar it consumes for each feed — every column and every key it reads, and that column's or key's semantics — and shall let no undeclared column or key influence its output, per the `PKG-02` out-of-scope line "interpretation beyond declared grammars" (CLM-007). The declared grammar shall state what the parser does with a register whose `RegisterSchemaVersion` it does not recognize, a register whose header carries columns the grammar does not declare, a `WORK_GRAPH.json` whose declared version it does not recognize, and a `WORK_GRAPH.json` that declares none. Silent best-effort interpretation of unrecognized shapes is prohibited. Line-ending and header-quoting variance across otherwise identical registers (CLM-016) shall not change the records emitted.
- **REQ-003** — The parser's emitted records shall be typed as the DependencyEdge entity of the upstream record-tier entity model quoted in CLM-009. This deliverable shall define no record-tier entity type of its own, shall add no type to that model, and shall not depend on any upstream artifact existing; it depends on the upstream contract only (CON-003).
- **REQ-004** — No emitted record shall carry the prose held in the register's `Statement`, `EvidenceQuote`, or `Notes` columns, or free-prose text from any `WORK_GRAPH.json` field; only paths, counts, identifiers, states, SHAs, and hashes shall appear, per `PEC-K-10` and the upstream field-shape obligation quoted in CLM-009 (CLM-014). Reading such a column in order to derive an identifier or a state is permitted; carrying its text is not. Enforcement at the ingest boundary is `DEL-01-03`'s guard under `SOW-056` (CLM-012); this requirement binds what the parser emits so that the guard has nothing to admit.
- **REQ-005** — Every emitted record shall carry provenance sufficient for a per-claim citation to its live source — register file path and row identity, work-graph file path and node or edge position, and/or SHA — per `PEC-ORI-004` and the upstream provenance obligation quoted in CLM-009. Attaching citations to an orientation response is `DEL-04-03`'s act under `SOW-007` (CLM-012); this requirement obliges the parser to carry what that act needs, and no more.
- **REQ-006** — Where a register or work-graph file is absent, unreadable, malformed, or carries a shape the declared grammar does not recognize, the parser shall report that condition explicitly to its caller, naming the file and the fault; a silently dropped, empty, partial, or defaulted record is prohibited, per `PEC-ORI-006` ("Where a feed is unparseable or stale, the response shall state the measurement limitation explicitly; silent omission is prohibited"). Because registers are deliverable-local and a full accounting is assembled by querying many of them (CLM-013), the coverage of a read — which register locations were examined and which were not — shall itself be reportable. The location set examined is supplied to this parser rather than discovered by it: the per-project `_harness/adapter.yaml` feed manifest is `DEL-02-07`'s deliverable under `SOW-017` (CLM-012), and feed discovery is no part of this deliverable's scope (REQ-011, AC-010), so what this requirement obliges is coverage reporting over the location set the parser is given — the same posture as REQ-001's "in the checkouts it is pointed at". Rendering such a limitation into an orientation response is `SOW-009` / `DEL-04-05` scope (CLM-012); this deliverable makes the limitation available to that consumer.
- **REQ-007** — The parser shall create, modify, or delete no source file, including the registers and work graphs it reads, per `PEC-RCN-004` ("it shall never modify a source file"), `PEC-RCN-006` ("The reconciler writes only its own store and generated views"), and the `PKG-02` out-of-scope line "Writing anything".
- **REQ-008** — The parser shall report what the registers state and shall issue no judgment of its own about them (CLM-013, `PEC-K-06`). It shall not validate a register against a schema contract, adjudicate `SatisfactionStatus`, `Confidence`, `Explicitness`, `RequiredMaturity`, or stratum, detect or rule on cycles, compute or assign blockers or work, reconcile contradictions between registers, or amend a register. Where such a field is emitted, it shall be emitted as a value read from the source and attributed to it, never as a parser verdict; strata and flags are carried as recorded provenance, and citation of an edge converts no stratum.
- **REQ-009** — The parser shall be deterministic over its inputs: the same file set at the same content shall yield the same records, so that the record tier remains fully regenerable from sources per `PEC-K-02` and the upstream regenerability obligation quoted in CLM-009. The rebuild command itself is `DEL-03-01`'s under `SOW-010` (CLM-012).
- **REQ-010** — The parser and its fixtures shall introduce no third-party runtime dependency and no external network egress, per `PEC-SVC-001` and `PEC-SVC-002`, whose standing enforcement is `DEL-01-05` covering `SOW-052` and `SOW-053`.
- **REQ-011** — The parser shall parse no feed owned by a sibling deliverable and shall perform no act owned by another package. In particular it shall not read `_STATUS.md`, decision registers or packets, `LOOP_RECEIPTS.md`, `STATUS.json`, `RUNTIME_SUMMARY.json`, workplans or `LOOP_INIT.md`, or `_harness/adapter.yaml`; shall emit no RunRecord, Receipt, DecisionRow, Package, Deliverable, or Workplan/Step/Gate entity; and shall perform no reconciliation, drift classification, freshness stamping, or citation attachment (CLM-012).
- **REQ-012** — Tests shall implement the verification methods declared in this contract; they shall not define scope, requirements, or acceptance criteria.

- **AC-001** — The parser reads a well-formed register fixture and a well-formed `WORK_GRAPH.json` fixture and yields exactly the DependencyEdge records each fixture declares; every column and key it reads appears in the documented grammar; altering an undeclared column or key in a fixture changes nothing in its output; the four unrecognized- and absent-version cases of REQ-002 are each handled as the documented grammar states; and a register fixture presented in CRLF and LF, with and without quoted header cells, and with the 29- and 31-column headers, yields identical records where the declared columns are identical.
- **AC-002** — Every emitted record is an instance of the upstream DependencyEdge type as that contract obliges it; no record-tier entity type is defined in this deliverable's source; and no element of this deliverable asserts or requires that an upstream schema, entity model, or store exists.
- **AC-003** — For a fixture whose `Statement`, `EvidenceQuote`, and `Notes` columns and whose work-graph fields carry free prose, diff-shaped text, and file content, the emitted records contain none of it; only paths, counts, identifiers, states, SHAs, and hashes appear.
- **AC-004** — Every emitted record resolves to its live source: for a sample of each fixture kind, the recorded provenance is present and locatable by register path and row identity, by work-graph path and position, and/or by SHA.
- **AC-005** — For absent, unreadable, malformed, and version-unrecognized fixtures of both feeds, the parser returns an explicit limitation naming the file and the fault, and never a silently dropped, empty, partial, or defaulted record in its place; and a read over a fixture tree reports which register locations were examined and which were not.
- **AC-006** — A parser run over a fixture corpus leaves that corpus byte-identical, and the module contains no write, create, or delete call against any source path.
- **AC-007** — The parser issues no verdict about its sources: a fixture set containing a cycle, a contradiction between two registers, an unsatisfied prerequisite, and a disputed stratum produces records that carry those source values attributed to their rows and no parser-originated validation result, blocker assignment, satisfaction determination, or stratum change.
- **AC-008** — Two runs of the parser over the same unchanged fixture corpus produce identical records, and inspection finds no emitted field whose value a rebuild from the same sources could not reproduce.
- **AC-009** — The parser and its fixtures add no third-party runtime dependency and make no network call, leaving the `DEL-01-05` zero-dependency and locality assertion intact.
- **AC-010** — The parser reads no sibling feed — `_STATUS.md`, decision registers and packets, `LOOP_RECEIPTS.md`, `STATUS.json`, `RUNTIME_SUMMARY.json`, workplans and `LOOP_INIT.md`, and `adapter.yaml` included — emits no entity type other than DependencyEdge, and performs no reconciliation, drift-classification, stamping, or citation-attachment act owned by `PKG-03` or `PKG-04`.
- **AC-011** — The fixture test suite implements VER-001 through VER-010, executes in the `PKG-02` test run, passes, and introduces no acceptance criterion absent from this contract.
- **AC-012** — The REVIEW gate confirms this contract's traceability to `SOW-015`, `OBJ-001`, and `OBJ-002` as ruled at SCA-002 Gate 3 Q2, confirms that the indirect `OBJ-002` leg is stated no more strongly here than the Gate 3 record states it — including the recorded and unadopted N1 narrowing evidence and the absence of a confidence label on that group — and confirms that no `PKG-01`, sibling `PKG-02`, `PKG-03`, or `PKG-04` scope, and no dependency-register governance owned by the decomposition workflows, has been absorbed.

- **CON-001** — One deliverable at Context Envelope `S` carries two structurally unlike feeds under a single declarable grammar. `SOW-015` names both `Dependencies.csv` and `WORK_GRAPH.json` and `DL-4` calls each scope item "a separately testable parser with its own grammar" (CLM-005); the corpus shows why that is one item and not two only by decision. The registers are near-uniform — 936 files, one schema version, two header shapes, two `DependencyClass` values. The work graphs are near-arbitrary — 35 files, 31 distinct top-level key sets, `edges` present in 10 of them, and no version declaration at all in 14 (CLM-016). A grammar narrow enough to be declarable will not describe most of the `WORK_GRAPH.json` corpus, and a grammar wide enough to describe it is the "interpretation beyond declared grammars" the `PKG-02` charter excludes. This contract records the tension rather than resolving it: REQ-002 requires the grammar to be declared per feed and to state its own behaviour on unrecognized shapes, and REQ-006 requires every file the grammar does not cover to surface as an explicit limitation rather than a silent omission. Choosing the grammar's breadth is a production decision bounded by those requirements; extending this deliverable to interpret shapes it has not declared, or dropping either named file form, would be a scope-change question, not a production decision.
- **CON-002** — Edge identity and content-minimality pull against each other in this feed. The register's edge identifier, stratum, and flag are carried inside the free-text `Notes` column rather than in columns of their own (TBD-004), while `PEC-K-10` and the upstream obligation quoted in CLM-009 require that no emitted field hold register-row prose (CLM-014). Deriving `EdgeID=E-P07` from a `Notes` cell is a read of prose; emitting the derived identifier is not the same act as emitting the cell, but the boundary between them is not drawn by any accepted source. This contract records the tension: REQ-004 forbids carrying the text and REQ-002 requires the grammar to declare exactly which cells are read and what is derived from them, so the boundary is visible and checkable wherever production draws it. A structural fix — promoting edge identity to a register column — would be an amendment to the register schema, which this deliverable does not own (CLM-013, REQ-008).
- **CON-003** — The DependencyEdge field set is owned upstream and does not yet exist. `DEL-01-01` is `INITIALIZED`: its contract obliges the DependencyEdge type and bounds what it may admit (CLM-009), but neither it nor any accepted source enumerates the type's fields (TBD-003), and `PRD.md` §7.1 gives the entity a source cell rather than a definition (CLM-002). This parser's output typing therefore binds to an obligation, not to an artifact. Nothing in this contract defines, anticipates, or constrains that field set, and a production choice here that fixed it would take a decision in the wrong place.
- **CON-004** — The corpus this parser is first expected to meet holds only half of its feed. `OI-010`, resolved at Gate 2 (2026-07-24), records that "the §12 closing paragraph governs — the first loop the P1 reconciler ingests is PEC v2's own build (bootstrap as thesis validation) ...", and the `projects/pec` tree contains 64 `Dependencies.csv` registers and **zero** `WORK_GRAPH.json` files today (CLM-016). This is recorded as a stated condition, not a defect and not a licence to widen the read scope: the parser's coverage of a loop with no work graph is a limitation to be stated under REQ-006, and dropping the `WORK_GRAPH.json` form because the first loop lacks it is prohibited by REQ-001 and by the `DL-9` correction the `SOW-015` note carries (CLM-006).

## Production and Verification Method — Praxeology

Production proceeds in the order corpus survey → declared grammar per feed →
parser → limitation and coverage reporting → fixtures and tests, because each
stage is the acceptance surface of the next and because neither grammar can be
declared honestly before the corpus condition of CLM-016 has been examined
against the accepted sources. The register grammar and the work-graph grammar
are declared separately even though one deliverable carries both, since CON-001
is a tension about breadth and a single blended grammar would hide it. All work
is bounded to this deliverable folder and the `PKG-02` service-core source it
names; this contract authorizes no register, decomposition, PRD, or
upstream-deliverable edit, and it neither defines nor reshapes the record-tier
entity model it emits into. Tests implement the verification methods below and
create no scope.

- **VER-001** — Execute the parser over a well-formed register fixture and a well-formed `WORK_GRAPH.json` fixture and assert the emitted records equal each fixture's declared expectation; compare the set of columns and keys actually read, by instrumentation or code inspection, against the documented grammar; mutate an undeclared column and an undeclared key to assert output invariance; execute the unrecognized- and absent-version fixtures of both feeds, asserting the documented behaviour in each case; and execute the CRLF/LF, quoted/unquoted-header, and 29-/31-column register variants, asserting identical records across them where the declared columns are identical.
- **VER-002** — Inspect this deliverable's source for any record-tier type definition and assert none is present; assert every emitted record is constructed against the upstream DependencyEdge type as the contract quoted in CLM-009 obliges it; and grep the source and fixtures for any assumption that an upstream schema, model, or store exists, asserting none.
- **VER-003** — Content-minimal inspection: run the parser over a fixture whose `Statement`, `EvidenceQuote`, and `Notes` columns and whose work-graph fields carry free prose, diff-shaped text, and file content, and assert field by field that the emitted records carry none of it; where an identifier or state is derived from a prose cell, assert that the grammar declares that derivation and that only the derived value appears.
- **VER-004** — Provenance resolution: for a sample record from each fixture kind, resolve the recorded provenance to a live file source and assert that register path and row identity, work-graph path and position, and/or SHA are present and locatable.
- **VER-005** — Execute the parser against absent, unreadable, malformed, and version-unrecognized fixtures of both feeds and assert, per case, an explicit limitation naming the file and the fault, with no dropped, empty, partial, or defaulted record returned; then run it over a fixture tree containing register locations inside and outside the read set and assert that the coverage report distinguishes examined from unexamined locations.
- **VER-006** — Hash the fixture corpus tree before and after a parser run and assert byte-identity; inspect the module's call graph for write, create, or delete operations against any source path.
- **VER-007** — Non-adjudication exercise: construct a fixture set containing a dependency cycle, two registers whose rows contradict each other, a `PENDING` prerequisite whose target is unbuilt, and a row whose `Notes` records a disputed stratum or flag; assert that the emitted records carry those source values attributed to their rows, and inspect the output and the source for any parser-originated validation verdict, cycle ruling, blocker assignment, satisfaction determination, or stratum promotion, asserting none.
- **VER-008** — Determinism check: run the parser twice over the same unchanged fixture corpus and assert the emitted records are identical; inspect the emitted field inventory for any value the parser did not derive from the source files.
- **VER-009** — Inspect the `PKG-02` dependency manifest and this module's import graph for third-party runtime dependencies and network calls, and re-run the `DEL-01-05` zero-dependency and locality enforcement once that deliverable is available, without discharging it here.
- **VER-010** — Boundary inspection: assert the parser opens no file named `_STATUS.md`, `LOOP_RECEIPTS.md`, `STATUS.json`, `RUNTIME_SUMMARY.json`, `LOOP_INIT.md`, or `adapter.yaml` and no decision register or packet, emits no entity type other than DependencyEdge, and contains no reconciliation, drift-classification, stamping, or citation-attachment code path.
- **VER-011** — Run the `PKG-02` test suite and confirm that each of VER-001 through VER-010 has a corresponding executing automated test and that no test asserts a criterion absent from this contract.

## Governing Values and Decisions — Axiology

- **AX-001** — `OBJ-001` governs: orientation is a sub-second query with per-claim citations. A dependency edge that cannot say which register row or work-graph position it came from cannot serve a cited orientation, whatever else it holds; provenance is therefore a property of what this parser emits (REQ-005) rather than a decoration added downstream.
- **AX-002** — `OBJ-002` governs indirectly, through the record tier. This deliverable produces facts the SHA comparison operates over; it does not perform that comparison, and no requirement here may be read as claiming otherwise. Its contribution to the objective is that its output is deterministic and regenerable (REQ-009), so a difference between two reconciles is a structural difference and never a judgment.
- **AX-003** — `PEC-K-06` observation-not-participation governs this feed more sharply than any other in `PKG-02`, because a dependency register is the one file kind whose content looks like an instruction. A row states a prerequisite, a maturity threshold, and a satisfaction status; reading it and acting on it are one keystroke apart. `D-PEC-62` §1(3) placed the registers deliverable-locally precisely to avoid "another surface for authority" (CLM-013), and `_DEPENDENCIES.md` records that blocker output is "advisory visibility only — never work assignment". REQ-008 makes the restraint a checkable requirement rather than an intention.
- **AX-004** — `PEC-K-10` content-minimal is a residency posture, not a storage optimization, and this feed's schema is prose-bearing by design: `Statement`, `EvidenceQuote`, and `Notes` exist to hold the authored reasoning behind an edge. The strongest available enforcement is emitting a record that has nowhere to put that reasoning (REQ-004); the ingest-side guard is `DEL-01-03`'s. CON-002 records where this posture and edge identity genuinely conflict rather than papering over it.
- **AX-005** — `PEC-K-02` files govern: dependency registers and work graphs are authored project truth and PEC's edge records are a projection, regenerable and never citable as authority over the file itself. `PEC-RCN-004` and `PEC-RCN-006` make the read-only posture a rule rather than a habit (REQ-007). A register is amended by the workflow that owns it, never by its reader.
- **AX-006** — `PEC-K-01` graceful absence governs: no governed act may require a PEC read or write. A loop with no work graph — which is the pec loop's condition today (CON-004) — is a stated coverage limitation, never a blocked act and never a silent gap. The same holds for the register locations a given read did not reach, which is why REQ-006 makes coverage itself reportable.
- **AX-007** — `DL-4` is the decision that makes this deliverable atomic, and `DL-9` is the decision that fixes its boundary with `DEL-02-04`: one feed kind, one separately testable unit — and for this item, the two file forms that `PRD.md` §7.1 routes to DependencyEdge, `WORK_GRAPH.json` included (CLM-005, CLM-006). Absorbing a sibling feed grammar (`DEL-02-01`..`DEL-02-04`, `DEL-02-06`..`DEL-02-07`), the entity model that types this output (`DEL-01-01`), the reconciler that consumes it (`DEL-03-01`), the bootstrap progression record that self-ingests the DAG (`DEL-10-10`), or the limitation-honesty surface (`DEL-04-05`) would undo those decisions. REQ-011 states the boundary as a requirement so that it is checkable.
- **AX-008** — The edges `[E-P07]` (upstream, `DEL-01-01` → `DEL-02-05`), `[E-P23]` (downstream, `DEL-02-05` → `DEL-03-01`), and `[E-P73]` (downstream, `DEL-02-05` → `DEL-10-10`) are `PROPOSAL` stratum and are accepted: `D-PEC-62` §1(4) accepted the candidate DAG v0.2 exhibit "accepted, all strata as presented", read in that packet as carrying the exhibit's flags as flags, so what remains recorded-but-unresolved is the specific annotated set (E-A11, E-P69/E-N02, E-N13/E-N18, the C-02 direction, the C-08 standing-node set) — none of which touches `E-P07`, `E-P23`, or `E-P73`, each of which carries an empty `Flag` column in the exhibit. Stratum is provenance, not authority: it records how an edge was derived, not whether it has been accepted, and citation does not convert `PROPOSAL` to `DECLARED`. That this contract's subject matter is dependency edges changes nothing about the status of the edges it is placed by.
- **AX-009** — Edge direction is a constraint on this contract, not a licence. `RequiredMaturity` `INITIALIZED` on `[E-P07]` means the upstream *contract* is the reliable input, not any upstream artifact; this contract is written against the obligations quoted in CLM-009 and asserts nothing about upstream implementation state. Consuming that contract imposes no obligation on `DEL-01-01`, and being consumed by `DEL-03-01` and `DEL-10-10` neither expands nor transfers scope in either direction.
- **AX-010** — Unknowns stay marked. TBD-001 through TBD-005 and CON-001 through CON-004 are recorded rather than resolved by inference. `C-04` `PHASE_PRECEDENCE` and `C-10` `STRATUM_RULE` are register-wide non-gating constraints recorded in `_DEPENDENCIES.md`, and blocker output under the `FULL_GRAPH` mode at threshold `INITIALIZED` is advisory visibility only, never work assignment.
- **AX-011** — This contract is lifecycle-neutral. `_STATUS.md` remains the sole lifecycle authority and is untouched by the run that authored this document; the deliverable is at `OPEN` and nothing has been built.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-015 OBJ-001 OBJ-002 | REQ-001, REQ-002, CLM-001, CLM-002, CLM-004, CLM-006, CLM-007, CLM-016, TBD-002, TBD-005, CON-001 | AC-001 | VER-001 | Per-feed grammar documentation, the well-formed register and work-graph fixtures with parser output, the undeclared-column and undeclared-key invariance results, per-case transcripts for the four unrecognized- and absent-version cases, and the register shape-variance comparison across CRLF/LF, quoted/unquoted headers, and the 29- and 31-column forms |
| OUT-001 | SOW-015 OBJ-001 OBJ-002 | REQ-003, CLM-009, TBD-003, CON-003 | AC-002 | VER-002 | The record construction surface against the quoted upstream DependencyEdge obligation, plus a recorded search of this deliverable's source for record-tier type definitions and upstream-artifact assumptions |
| OUT-001 | SOW-015 OBJ-001 OBJ-002 | REQ-004, CLM-014, TBD-004, CON-002, AX-004 | AC-003 | VER-003 | Field-by-field inspection of the records emitted for a prose-bearing register and work-graph fixture, with the declared derivations from `Statement`, `EvidenceQuote`, and `Notes` shown against the values actually emitted |
| OUT-001 | SOW-015 OBJ-001 OBJ-002 | REQ-005, CLM-012, AX-001 | AC-004 | VER-004 | Per-fixture-kind provenance resolution records showing register path and row identity, work-graph path and position, and/or SHA present and locatable |
| OUT-001 | SOW-015 OBJ-001 OBJ-002 | REQ-006, CON-004, AX-006 | AC-005 | VER-005 | Per-case transcripts for absent, unreadable, malformed, and version-unrecognized fixtures of both feeds, each showing the file named and the fault located, plus a coverage report distinguishing examined from unexamined register locations |
| OUT-001 | SOW-015 OBJ-001 OBJ-002 | REQ-007, AX-005 | AC-006 | VER-006 | Before/after fixture-corpus tree hashes and a call-graph inspection record showing no write path against a source file |
| OUT-001 | SOW-015 OBJ-001 OBJ-002 | REQ-008, CLM-013, AX-003, AX-008 | AC-007 | VER-007 | Non-adjudication exercise transcript over the cycle, contradiction, unsatisfied-prerequisite, and disputed-stratum fixtures, with the source-attributed record values and a recorded search finding no parser-originated verdict |
| OUT-001 | SOW-015 OBJ-001 OBJ-002 | REQ-009, AX-002 | AC-008 | VER-008 | Two-run output comparison over an unchanged fixture corpus plus the emitted-field derivation inspection |
| OUT-001 | SOW-015 OBJ-001 OBJ-002 | REQ-010 | AC-009 | VER-009 | Dependency-manifest and import-graph inspection records, plus the DEL-01-05 enforcement result once that deliverable is available |
| OUT-001 | SOW-015 OBJ-001 OBJ-002 | REQ-011, CLM-005, CLM-010, CLM-011, AX-007, AX-009 | AC-010 | VER-010 | Recorded search showing no sibling feed opened and no entity type other than DependencyEdge emitted, with the reconciliation, stamping, and citation-attachment code paths absent |
| OUT-002 | SOW-015 OBJ-001 OBJ-002 | REQ-012, CLM-015 | AC-011 | VER-011 | PKG-02 test-run output mapping each executed test to its declared verification method, with no criterion asserted that this contract does not state |
| OUT-001 | SOW-015 OBJ-001 OBJ-002 | CLM-003, AX-010, AX-011 | AC-012 | HUMAN_REVIEW: REVIEW gate confirms traceability to SOW-015 and to OBJ-001/OBJ-002 as ruled at SCA-002 Gate 3 Q2, confirms the indirect OBJ-002 leg is stated no more strongly than that record states it given the unadopted N1 narrowing evidence and the absence of a confidence label, and confirms no sibling, cross-package, or dependency-register governance scope absorption | Review record citing the scope-ledger row, the Gate 3 Q2 ruling and D-17, the D-PEC-62 §1(3) register-storage ruling, and the sibling and cross-package deliverable boundaries |
