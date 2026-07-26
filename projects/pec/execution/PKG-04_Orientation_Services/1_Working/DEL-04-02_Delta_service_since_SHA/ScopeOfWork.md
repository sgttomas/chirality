---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-04-02
package_id: PKG-04
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@3623b958b
project_scope_refs: [SOW-005]
package_objective_refs: [OBJ-001, OBJ-002]
---

# Scope of Work — DEL-04-02 Delta service since SHA

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-04-02` — "Delta service
since SHA" — in `PKG-04` Orientation Services of the PEC v2 build. It covers
project scope item `SOW-005` in service of package objectives `OBJ-001` and
`OBJ-002`.

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.2** (`current_basis`, SCA-002 successor; accepted 2026-07-25 at
D-PEC-64 closure, commit `3623b958b`). The deliverable-local `_REFERENCES.md`
still names "revision 1.1, accepted working surface"; that phrase is superseded
provenance left by a deferred pointer sweep (SCA-002 `Handoff_State.md`, open
item `OI-B`), and `_CONTEXT.md`'s own supersession line records revision 1.1 as
"superseded by revision 1.2 (`current_basis`, SCA-002 successor)". This
contract cites revision 1.2.

**Objective warrant (register-direct, pre-SCA-002).** `CoversScopeItems` is one
row, and both of its objective tokens are the register's own, unchanged by the
scope-change amendment. Three checks in the SCA-002 record agree, and this
contract states the mapping at the strength the record carries — no confidence
label, no owner-confirmation acceptance criterion, no fresh derivation.

First, the `SOW-005` ledger row is not one of the twenty rows whose empty
`ObjectiveIDs` cell action `A001` populated. That action's target cell reads in
full:

> `ScopeLedger.csv` `ObjectiveIDs` — **20 IN rows** (`SOW-001, 003, 011..017,
> 021, 025, 040, 042, 052, 053, 054, 056, 088, 089, 094`)
>
> (`Brief.md`, action-register row `A001`, target cell, quoted in full without
> elision; the `..` ranges are the source's own notation. ID-shaped text inside
> this quotation is upstream source context, not a local definition or
> reference.)

`SOW-005` is not among the twenty. Second, `DEL-04-02` is not among the
seventeen deliverable rows whose empty `SupportsObjectives` cell action `A002`
populated; that action's target cell reads in full:

> `Deliverables.csv` `SupportsObjectives` — **17 deliverable rows** (`DEL-00-01,
> 00-03, 01-01, 01-03, 01-05, 01-06, 02-01..07, 03-06, 08-01, 08-02, 10-03`)
>
> (`Brief.md`, action-register row `A002`, target cell, quoted in full without
> elision; the `..` ranges are the source's own notation. ID-shaped text inside
> this quotation is upstream source context, not a local definition or
> reference.)

Third, the §3 objective rows confirm the same from the objective side, for both
objectives. The recorded old and new text of the two amended columns reads in
full:

> ```
> OLD col4: SOW-004..009, SOW-041, SOW-043; instruments: SOW-058, SOW-059
> NEW col4: SOW-001, SOW-003, SOW-004..009, SOW-011..017, SOW-040..043, SOW-089; instruments: SOW-058, SOW-059
> OLD col5: DEL-04-01..05, DEL-08-03, DEL-08-04, DEL-10-01, DEL-10-04
> NEW col5: DEL-00-03, DEL-01-01, DEL-02-01..07, DEL-04-01..05, DEL-08-01..04, DEL-10-01, DEL-10-04
> ```
>
> (`Amendment_Preview.md`, action `A003b`, "Line 320 · `OBJ-001`"; all four
> lines quoted in full, none elided. The `..` ranges are the source's own
> notation. ID-shaped text inside this quotation is upstream source context, not
> a local definition or reference.)

> ```
> OLD col4: SOW-006, SOW-018, SOW-019; supported by SOW-005
> NEW col4: SOW-001, SOW-006, SOW-011..019; supported by SOW-005
> OLD col5: DEL-03-02, DEL-03-03, DEL-04-02, DEL-04-03
> NEW col5: DEL-01-01, DEL-02-01..07, DEL-03-02, DEL-03-03, DEL-04-02, DEL-04-03
> ```
>
> (`Amendment_Preview.md`, action `A003b`, "Line 321 · `OBJ-002`"; all four
> lines quoted in full, none elided. ID-shaped text inside this quotation is
> upstream source context, not a local definition or reference.)

`SOW-005` stands inside `OBJ-001`'s mapped scope items — within the `SOW-004..009`
range — and `DEL-04-02` inside its mapped deliverables, within `DEL-04-01..05`,
on both sides of the amendment. On the `OBJ-002` row, `DEL-04-02` likewise
stands in the mapped-deliverables cell unchanged on both sides, and `SOW-005`
appears on both sides in the qualified form "supported by `SOW-005`" rather than
in the plain mapped-item enumeration. This contract states that difference
rather than smoothing it: the objective-side view carries the scope item as
supporting material on the `OBJ-002` row and as an enumerated member on the
`OBJ-001` row, while the two register cells that govern attribution — the ledger
row's `ObjectiveIDs` and the deliverable row's `SupportsObjectives` — each carry
`OBJ-001;OBJ-002` flatly and neither was authored by SCA-002.

One reading is expressly not taken. `SOW-005` also appears in the SCA-002
Q2 discussion of the eight indirect parser rows, where the recommended AFFIRM
variant reproduces the unchanged `supported by SOW-005` text in its comparison
table. That discussion is about whether `SOW-001` and `SOW-011`..`SOW-017` map
to `OBJ-002`; it neither reclassifies `SOW-005`'s own mapping nor derives it.
This contract does not treat that passage as the warrant for anything here.

- **CLM-001** — The accepted `ScopeLedger.csv` row for `SOW-005` reads in full, under the register's ten columns `ScopeItemID,InOutStatus,ScopeItemStatement,SourceRef,PackageID,DeliverableIDs,ObjectiveIDs,DecisionRef,OpenIssue,Notes`:

> `SOW-005,IN,Serve deltas since a caller-supplied commit SHA,PEC-ORI-002,PKG-04,DEL-04-02,OBJ-001;OBJ-002,,FALSE,`
>
> (Field by field: the statement is unquoted in the source because it contains
> no comma; `DecisionRef` empty and `Notes` empty — two of the ten fields are
> unpopulated, `Notes` trailing; `OpenIssue` `FALSE`. Unlike its `PKG-04`
> siblings `SOW-006` ("Carries PEC-K-04") and `SOW-009`
> ("Coverage-honesty carry-forward"), no boundary decision, no open issue, and
> no invariant note rides this scope item. ID-shaped text inside this quotation
> is upstream source context, not a local definition or reference.)

  The `SOFTWARE_DECOMP.md` §2.1 SSOW row for the same item repeats the statement without the register-only columns and likewise leaves its `Notes` column empty: "| SOW-005 | IN | Serve deltas since a caller-supplied commit SHA | PEC-ORI-002 | |".

- **CLM-002** — `SOW-005`'s `SourceRef` cell names one locus, `PEC-ORI-002`, the `PRD.md` §9.1 orientation requirement, quoted here in full as it reads: "PEC shall serve deltas since a caller-supplied commit SHA." That is the entire accepted statement of this deliverable's subject. It fixes three things and no more: that the act is *serving*, that what is served is *deltas since* an anchor, and that the anchor is a *caller-supplied commit SHA*. It does not state what a delta ranges over (CON-003), over what scope unit it is computed (CON-004), how the caller-supplied SHA is resolved (CON-005), or what the served value looks like (TBD-002). `PEC-ORI-002` is one of six `PRD.md` §9.1 requirements; the other five are covered by `PKG-04` siblings and are not this deliverable's (CLM-015).
- **CLM-003** — `OBJ-001` states "Orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation", `SourceRef` `§3.1` (`SOFTWARE_DECOMP.md` §3; `PRD.md` §3 outcome 1). At revision 1.2 its "Mapped Scope Items" cell reads "SOW-001, SOW-003, SOW-004..009, SOW-011..017, SOW-040..043, SOW-089; instruments: SOW-058, SOW-059" and its `MappedDeliverables` cell reads "DEL-00-03, DEL-01-01, DEL-02-01..07, DEL-04-01..05, DEL-08-01..04, DEL-10-01, DEL-10-04". Two clauses of that objective statement are quoted here rather than re-obliged by this contract. "Sub-second" is the objective's own word and its buildable form is `SOW-041` — "Complete orientation reads in ≤100 ms at p95 against the current corpus" (`PEC-API-002`) — covered by `DEL-08-04` in `PKG-08`; this deliverable holds no edge to it in either direction (CLM-008), and this contract asserts no latency bound and produces no latency evidence (REQ-011). "Per-claim citations" is likewise the objective's word and its buildable form is `SOW-007` (`PEC-ORI-004`), covered by `DEL-04-03`; this contract carries the provenance that act needs and performs no attachment (REQ-007).
- **CLM-004** — `OBJ-002` states "Staleness is detected structurally by SHA comparison, never by judgment", `SourceRef` `§3.2` (`SOFTWARE_DECOMP.md` §3; `PRD.md` §3 outcome 2). At revision 1.2 its "Mapped Scope Items" cell reads "SOW-001, SOW-006, SOW-011..019; supported by SOW-005" and its `MappedDeliverables` cell reads "DEL-01-01, DEL-02-01..07, DEL-03-02, DEL-03-03, DEL-04-02, DEL-04-03". The objective's product invariant is `PEC-K-04` **Staleness is a comparison**, whose statement reads in full: "Every response carries the examined-through commit SHA and per-feed freshness; consumers detect staleness structurally." This deliverable is the objective's *caller-anchored* member: the comparison it performs is between what PEC holds now and what a caller says it already knew, expressed as a commit SHA the caller supplies. It is not where a response is stamped (`SOW-006`, `DEL-04-03`), where the reconcile selects work from its own baseline (`SOW-018`, `DEL-03-02`), or where a difference between successive snapshots is classified (`SOW-019`, `DEL-03-03`).

## Deliverable Definition — Ontology

`DEL-04-02` is typed `BACKEND_FEATURE_SLICE` at Context Envelope `M` with
`PhaseHint` `P1`. `Deliverables.csv` records its `AnticipatedArtifacts` as
"Delta service + tests" and leaves `ContextEnvelopeNotes` empty, so there are no
envelope notes to carry forward and `_CONTEXT.md` records "(none)". The outputs
of this contract are bounded by that artifact naming: exactly the delta service
and its tests, and nothing beyond those two artifacts and the components each of
them declares as part of itself.

- **OUT-001** — A delta service in the PEC service core: given a caller-supplied commit SHA, it composes from record-tier entities the differences in what PEC holds since that anchor, carrying each element's citation provenance and each element's stated absence or limitation, and exposes that value through an in-process interface. The service's **delta-composition record** — the readable artifact in which it declares, per delta element class, the record-tier entities it derives from, the rule by which the caller-supplied SHA is resolved, the scope unit over which the difference is taken, and its absence semantics (REQ-005) — is a component of this output rather than a third artifact: it is the service's own self-declaration, so the register's `AnticipatedArtifacts` naming of exactly two artifacts is preserved.
- **OUT-002** — An automated test suite covering the composition, the anchor resolution, the derivation and residency boundaries, and the absence and limitation behaviour, implementing the verification methods declared in this contract.

### Identity of record

- **CLM-005** — `DEL-04-02` is named "Delta service since SHA", Type `BACKEND_FEATURE_SLICE`, Context Envelope `M`, `PhaseHint` `P1`, `ResponsibleParty` `TBD`, `AnticipatedArtifacts` "Delta service + tests", `CoversScopeItems` `SOW-005`, `SupportsObjectives` `OBJ-001;OBJ-002`, `ContextEnvelopeNotes` empty, with the register `Description` field reading "Deltas since a caller-supplied commit SHA." Sources: `Deliverables.csv` row `DEL-04-02` and the `SOFTWARE_DECOMP.md` §5 PKG-04 table row "| DEL-04-02 | Delta service since SHA | BACKEND_FEATURE_SLICE | M | P1 | SOW-005 |". `ResponsibleParty` is `TBD` throughout the register by the §5 preamble — "assignment happens at WORKING_ITEMS activation, not here" (TBD-001).
- **CLM-006** — The `PKG-04` package charter (`SOFTWARE_DECOMP.md` §4) is "Derivation and serving of orientation: per-loop returns, deltas since SHA, SHA/freshness stamping, per-claim citations, scope parameterization, explicit measurement limits", covering "SOW-004..009 (6)", with "Transport (PKG-08); rendering (PKG-09)" recorded as explicitly out of package scope. Of those six items this deliverable covers exactly one — deltas since SHA — and the package's two exclusions bind it directly: no transport surface and no rendering surface is produced here (REQ-010). The charter's leading noun pair also fixes this package's posture as *derivation and serving*, not reconciliation: the guaranteed path from file truth to record tier is `PKG-03`'s charter, whose exclusions in turn record "parsers (PKG-02)".
- **CLM-007** — The `SOFTWARE_DECOMP.md` §9 Vocabulary Map fixes three terms this contract uses. The relevant rows read in full, under the map's columns `CanonicalTerm | Synonyms | Notes`:

> | orientation | Step-0 return | The per-loop/scope serve of PEC-ORI-001..006 |
> | OrientationSnapshot | — | Record-tier entity (§7.1): a generated orientation return stamped with examined SHA — the machine generalization of a receipt. Distinct from the general term "orientation" |
> | examined-through SHA | examined SHA, freshness SHA | The staleness comparator (PEC-K-04) |
>
> (`SOFTWARE_DECOMP.md` §9 Vocabulary Map; all three rows quoted in full, none
> elided. ID-shaped text inside this quotation is upstream source context, not a
> local definition or reference.)

  Two consequences follow. The delta serve is *within* the general term "orientation" — the map defines that term as the serve of `PEC-ORI-001..006`, and `PEC-ORI-002` is a member — so `PEC-ORI-003` response stamping and `PEC-ORI-004` per-claim citation apply to what this service returns and are `DEL-04-03`'s acts under `SOW-006` and `SOW-007`, not this contract's (REQ-007, CLM-015). And the map keeps "examined-through SHA" as the *staleness comparator* under `PEC-K-04`, which is the value the record tier carries — a different thing from the SHA a caller supplies as a request parameter (CLM-010, CON-001).

### Placement in the work graph

- **CLM-008** — This deliverable has **one** accepted `EXECUTION` upstream edge and **two** `ANCHOR` rows, held as `Dependencies.csv` register rows `DEP-04-02-001` through `DEP-04-02-003` at `RegisterSchemaVersion` `v3.1`. The two anchors are `DEP-04-02-001` (`IMPLEMENTS_NODE`: package-local to `PKG-04`) and `DEP-04-02-002` (`TRACES_TO_REQUIREMENT`: the `SOW-005` requirement trace). The single `EXECUTION` row is `DEP-04-02-003`, attributed by column: `FromPackageID` `PKG-04`, `FromDeliverableID` `DEL-04-02`, `FromDeliverableName` "Delta service since SHA", `DependencyClass` `EXECUTION`, `AnchorType` `NOT_APPLICABLE`, `Direction` `UPSTREAM`, `DependencyType` `PREREQUISITE`, `TargetType` `DELIVERABLE`, `TargetPackageID` `PKG-03`, `TargetDeliverableID` and `TargetRefID` `DEL-03-02`, `TargetName` "Incremental reconcile on Git delta", `TargetLocation` `execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-02_Incremental_reconcile_on_Git_delta`, `Statement` "Deltas since SHA ride the incremental examined-SHA machinery", `EvidenceFile` `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md`, `SourceRef` "location TBD", `EvidenceQuote` **empty**, `Explicitness` `IMPLICIT`, `RequiredMaturity` `INITIALIZED`, `ProposedMaturity` `TBD`, `SatisfactionStatus` `PENDING`, `Confidence` `MEDIUM`, `Origin` `EXTRACTED`, `FirstSeen` and `LastSeen` `2026-07-25`, `Status` `ACTIVE`, `Notes` "PROPOSAL; Flag=none; EdgeID=E-P33".

  The corresponding accepted DAG exhibit row, under that exhibit's columns `EdgeID,PredecessorID,SuccessorID,Stratum,EdgeKind,Flag,BasisCitation,Rationale`, reads `E-P33,DEL-03-02,DEL-04-02,PROPOSAL,CONSUMES,,,Deltas since SHA ride the incremental examined-SHA machinery` — `Flag` empty and `BasisCitation` **also empty**. This contract records, as an observation and not as a defect finding it is authorized to resolve, that the register row's empty `EvidenceQuote` and its `SourceRef` value "location TBD" agree with that empty `BasisCitation`: the edge is warranted by its `Statement` and by the two deliverables' own accepted contracts, and by no quoted source. The same pattern is recorded on `DEL-03-01` → `DEL-03-02` `[E-P26]` and was accepted at the batch-4 fan-in as register hygiene of the class `OI-013` names — "No durable register validator exists: the coverage/coupling assertions ran in a session-local generator, which is not part of this package and enforces nothing after acceptance" (`SOFTWARE_DECOMP.md` §10). No evidence is invented here to fill those cells. The edge's *direction* is nonetheless unambiguous: `DEL-03-02` is the predecessor and this deliverable the successor.

- **CLM-009** — The single predecessor is at lifecycle state `INITIALIZED`, which is the maturity the edge requires. `INITIALIZED` means the upstream **contract** is the reliable input: its accepted `ScopeOfWork.md` exists, and no reconcile engine, baseline record, store, schema, parser, or registry does. Nothing in this contract asserts that any upstream artifact exists. The obligations this contract binds to are that contract's stated obligations, quoted here in full and without elision:

> - **REQ-003** — Nothing the engine captures from Git, retains in memory beyond
>   the run, presents to the store, or writes into a declared view shall carry
>   file content or diff content; the delta shall be reduced to paths, counts,
>   SHAs, states, and hashes at the point it is read, per `PEC-K-10` (CLM-013).
>   This restriction binds the engine's own surface and is additional to, not a
>   substitute for, the store-side ingest guard owned elsewhere (CLM-012).
> - **REQ-004** — The engine shall record, as the baseline component of OUT-001
>   and through the write set of REQ-007, the commit SHA each completed
>   reconcile examined through, and shall advance that baseline only for a
>   reconcile that completed over the sources the delta named. Where no baseline
>   is recorded, the engine shall not synthesize one and shall not infer one from
>   store contents: it shall defer to the full-rebuild path (REQ-006) and
>   establish the baseline from the commit state it observed for that run.
>   Nothing in this requirement asserts that any other deliverable records or
>   maintains a baseline (CLM-009, CON-001).
> - **REQ-008** — Where a feed the delta selects is reported absent, unreadable,
>   malformed, stale, or grammar-unrecognized, the engine shall carry that
>   limitation through to its result, naming the loop and the feed, and shall
>   never present a reconcile that could not read a selected source as one that
>   read it, per `PEC-ORI-006` and the upstream carry-through obligation quoted
>   in CLM-008. It shall not advance the baseline past a source the delta named
>   and the run did not successfully examine.
> - **REQ-009** — The engine shall be deterministic and idempotent over its
>   inputs: two incremental reconciles over the same baseline and the same end
>   commit state shall produce the same record tier, and a reconcile run when the
>   delta is empty shall change no record-tier fact and shall leave the baseline
>   at the same SHA. This is what keeps the SHA comparison structural rather than
>   a judgment (`PEC-K-04`, `OBJ-002`, CLM-003).
> - **REQ-011** — The engine shall perform no act owned by another deliverable.
>   In particular it shall classify no drift between successive snapshots, run no
>   parity diff against practitioner-harness output, perform no stream-loss
>   recovery act, make or assert no rebuild or incremental performance
>   measurement or bound, stamp no orientation response with examined-through
>   SHA, generation time, or per-feed freshness and attach no per-claim citation,
>   serve no caller-supplied-SHA delta query, perform no presence-tier or
>   worktree scan, and run no kill test; each is cited to its owner in CLM-004,
>   CLM-011, and CLM-012, and none is discharged here.
>
> (`DEL-03-02/ScopeOfWork.md`, Epistemology section; all five records quoted in
> full, none elided. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference — this contract's own records are
> separate and differently worded.)

  Four design constraints on this service follow from those five records. The upstream reduction of a delta to paths, counts, SHAs, states, and hashes is contractual, so what this service can obtain from the reconcile path is already content-minimal and this service adds the same restriction on its own serving surface rather than a weaker one (REQ-003). The upstream engine keeps and advances a baseline of its own and is expressly not obliged to hold anyone else's, so this contract binds to that baseline as an upstream-owned value and never as a substitute for the caller's anchor (REQ-001, CON-001). The upstream limitation carry-through is contractual, so a limitation reaching this service is an input it must not drop (REQ-006). And upstream determinism and idempotence are what make any comparison this service performs a structural fact rather than a judgment (REQ-012).

- **CLM-010** — The edge's `Statement` and the exhibit's `Rationale` both read "Deltas since SHA ride the incremental examined-SHA machinery", and the upstream contract's own text bounds what "ride" can mean. Two of that contract's records address this deliverable directly. Its boundary record quoted in CLM-009 obliges the engine to "serve no caller-supplied-SHA delta query". Its downstream-relations claim states the same from the other side, in the sentence that names this deliverable:

> The delta-service relation likewise imposes nothing on this contract: serving
> deltas since a **caller-supplied** commit SHA is `DEL-04-02`'s act under
> `SOW-005`, and being consumed by it neither transfers that scope here nor
> obliges this engine to expose a caller-parameterized query (REQ-011).
>
> (`DEL-03-02/ScopeOfWork.md`, CLM-011, final sentence of that record, quoted in
> full as a whole sentence and not elided; the record continues before it with
> the parallel treatment of the performance relation. ID-shaped text inside this
> quotation is upstream source context, not a local definition or reference.)

  Two facts follow and are carried, not resolved, by this contract. First, the anchors differ: the upstream machinery is anchored on the commit SHA *the engine itself last examined through*, while `SOW-005` anchors on the commit SHA *a caller supplies*. Nothing in the accepted corpus states that the two coincide, that the caller's SHA must relate to the engine's baseline, or how a difference between them is taken (CON-001, CON-005). Second, the edge delivers obligations, not a query surface: the upstream contract declines a caller-parameterized query in its own voice, so the derivation path from a caller's anchor to a served delta is assigned to no accepted source and is this contract's own open surface (CON-002). This contract does not read the edge's rationale as a licence to assume upstream machinery it names, and it assigns no obligation upstream.

- **CLM-011** — The record-tier entity model this service composes from is not a declared edge of this deliverable, and unlike its `PKG-04` sibling `DEL-04-01` this deliverable holds no direct entry edge to it at all: the whole of its upstream set is the single `EXECUTION` row of CLM-008. Register-wide constraint `C-03` `PACKAGE_LEVEL` states "Every PKG-03/04/05 deliverable depends on DEL-01-01 directly or transitively", with the exhibit `Notes` cell recording "Deliverable-level entry edges (E-P10..13) are PROPOSAL; validator proves transitive closure 13/13" and the exhibit's own validation summary reading "C-03 transitive closure: 13/13 PKG-03/04/05 members reachable from DEL-01-01". Counted against the §5 tables, those thirteen members are `PKG-03`'s six, `PKG-04`'s five, and `PKG-05`'s two. This deliverable's path is three edges long — `DEL-01-01` `[E-P10]` `DEL-03-01`, `DEL-03-01` `[E-P26]` `DEL-03-02` (both recorded in the exhibit and in the upstream contract's own register), then `[E-P33]` to this deliverable. Its dependence on the entity model is therefore transitive across three edges rather than local, and the record-tier types are `DEL-01-01`'s under `SOW-001`; this contract defines none of them (REQ-008, CON-003).
- **CLM-012** — One downstream consumer relation is recorded against this deliverable in `_DEPENDENCIES.md` and marked informational: `DEL-08-05` `[E-P56]` (`CONSUMES`). It holds **no** row in this deliverable's `Dependencies.csv`, which contains only the two anchors and the one upstream `EXECUTION` row; the downstream row lives in the consumer's own local register, per the deliverable-local storage ruling of `D-PEC-62`. Its exhibit row reads `E-P56,DEL-04-02,DEL-08-05,PROPOSAL,CONSUMES,,"SOW-044: ""SSE subscription for deltas and presence changes""",Delta stream source`, with `Flag` empty and — unlike the upstream edge — a non-empty `BasisCitation`. The relation runs *from* this deliverable outward and imposes nothing on this contract: the SSE subscription is `DEL-08-05`'s act under `SOW-044` in `PKG-08` at `P4`, and the exhibit additionally records constraint `C-07` `DEFERRED_CONSUMPTION` for that deliverable — "No P2/P3 edge by declaration; P4 SSE consumption recorded as deferred". Being a declared stream source at `P4` neither transfers subscription scope here nor obliges this `P1` service to expose a stream, a push, or a subscription (REQ-010, REQ-013).
- **CLM-013** — PEC's Git posture and residency rule are permanent product boundaries, and this deliverable is where the residency rule is tested on the *serving* side. `PRD.md` §4.2 states the non-goal in full: "**Not a Git actor.** Read-only plumbing access; CHANGE owns Git state." `PEC-K-06` states the same standing: "**Observation, not participation.** Read-only over Git; no leases, no claim arbitration, no merge opinions, no dispatch; conflicts surfaced, never prevented." `PEC-K-10` bounds what may be held or served: "**Content-minimal.** Paths, counts, SHAs, states, hashes — never file or diff content." A caller who asks "what changed since this SHA" is asking the question whose most natural answer is a diff, so `PEC-K-10` bites on this deliverable's response surface more directly than anywhere else in `PKG-04`. The reconcile-side form of the same restriction is the upstream obligation quoted in CLM-009; the read-only Git scan of worktrees, branches, HEAD, ahead/behind counts, and dirty path names/counts is `DEL-06-02`'s presence-tier act at `P3` under `SOW-027` and `PEC-PRS-002`, not this deliverable's (REQ-004, CLM-015).
- **CLM-014** — Phase staging, checked against the `PhaseHint` column of `Deliverables.csv` for every deliverable this contract names in its own voice: this deliverable is `P1`; its single upstream `DEL-03-02` is `P1`; its recorded consumer `DEL-08-05` is `P4`. Other deliverables named as owners of adjacent scope are `P1` (`DEL-01-01`, `DEL-01-05`, `DEL-03-01`, `DEL-03-03`, `DEL-03-04`, `DEL-04-01`, `DEL-04-03`, `DEL-04-05`, `DEL-08-01`, `DEL-08-02`, `DEL-08-03`, `DEL-08-04`, `DEL-10-02`), `P2` (`DEL-04-04`, `DEL-05-01`), and `P3` (`DEL-06-02`). No upstream follows this deliverable's phase, the one consumer is three phases later, and no claim in this contract stages any named deliverable into a different phase. Two consequences bind: the scope-parameterization deliverable is `P2` while this service is `P1` (CON-004), and the gate-precondition evaluator that owns commit-reachability evaluation is also `P2` (CON-005).

### Boundaries

- **CLM-015** — The acts adjacent to this service are owned elsewhere and are cited here, never discharged. Within `PKG-04`: the per-loop orientation return of the six `PEC-ORI-001` components is `DEL-04-01` (`SOW-004`); stamping every orientation response with examined-through SHA, generation time, and per-feed freshness and attaching a citation to every claim is `DEL-04-03` (`SOW-006`, `SOW-007`, `PEC-ORI-003`, `PEC-ORI-004`, carrying `PEC-K-04`) — checked against the ledger, both of those scope items resolve to `DEL-04-03` and neither to this deliverable; scope parameterization by loop / project / package per the modes ladder is `DEL-04-04` (`SOW-008`, `PEC-ORI-005`, `P2`); stating the measurement limitation where a feed is unparseable or stale is `DEL-04-05` (`SOW-009`, `PEC-ORI-006`). Outside it: the record-tier schema and entity model are `DEL-01-01` (`SOW-001`); the standing zero-dependency and locality enforcement is `DEL-01-05` (`SOW-052`, `SOW-053`); the one-command full rebuild and the reconciler write restriction are `DEL-03-01` (`SOW-010`, `SOW-021`); the incremental Git-delta reconcile and its examined-SHA baseline are `DEL-03-02` (`SOW-018`); classifying and reporting drift between successive snapshots is `DEL-03-03` (`SOW-019`); parity-diffing PEC derivations against practitioner-harness output is `DEL-03-04` (`SOW-020`); deterministic evaluation of gate preconditions reducible to file/Git facts, including "ruling-SHA commit reachability", is `DEL-05-01` (`SOW-022`, `PEC-GAT-001`, `P2`); the read-only Git/worktree presence scan is `DEL-06-02` (`SOW-027`, `P3`); the Unix-socket server and token-scoped access classes are `DEL-08-01` (`SOW-003`, `SOW-040`), the versioned additive API schema is `DEL-08-02` (`SOW-042`), the compact citation-bearing response format is `DEL-08-03` (`SOW-043`), the orientation latency budget of ≤100 ms at p95 is `DEL-08-04` (`SOW-041`), and the SSE delta/presence subscription is `DEL-08-05` (`SOW-044`, `P4`); the standing kill test is `DEL-10-02` (`SOW-055`). This contract produces only the delta service and its tests.
- **CLM-016** — Consumption of this service is not this deliverable's act, and the accepted corpus names its callers only at one remove. `PEC-K-03` states: "Polling is performed by harnesses at moments of consequence (session start, mode transition, claim, write, dispatch, fan-in) and injected as labeled non-authoritative data. The only agent behavior is verify-before-rely", and `PRD.md` §8 records that agents "never call PEC directly by instruction; they receive harness-injected orientation as labeled data (PEC-K-03)". The only accepted statements naming deltas as consumed are two rows of the `PRD.md` §5 modes ladder, quoted here in full under that table's columns `Mode | Coordination contexts | PEC consumes | PEC produces | Posture`:

> | Agent 0, single (human-paired, cross-package) | 1 | loop-scoped orientation + deltas | status, presence, notices | efficiency; frees orchestrator context budget |
> | Agent 0s, concurrent | N, overlapping scope | orientation, deltas, presence, notices | everything | **essential for throughput** (not for soundness — file fallback remains) |
>
> (`PRD.md` §5 "Operating model — the modes ladder"; both rows quoted in full,
> neither elided. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference.)

  The caller population is therefore a harness polling on behalf of an Agent 0 session, and `PEC-K-11` mode-proportionality governs when it polls: "Consumption follows §5; zero-coordination modes remain zero-contact." This service composes on request and initiates nothing (REQ-013). The same two rows are the corpus's only scope qualifier for deltas and they do not agree with each other, which is CON-004.

- **CLM-017** — The deliverable is at lifecycle state `OPEN` with no implementation present. Every requirement, acceptance criterion, and verification method below states a contract on future production; none asserts that anything has been built.

- **TBD-001** — `ResponsibleParty` is unassigned; the register records `TBD`, with assignment at WORKING_ITEMS activation and not in this contract (`SOFTWARE_DECOMP.md` §5 preamble; `_CONTEXT.md`).
- **TBD-002** — The service's concrete in-process interface — its entry-point name, the form in which the caller-supplied SHA is passed, its other parameters, and the shape of the value it returns — is fixed by no accepted source beyond the register phrase "Delta service" and `PEC-ORI-002`'s "shall serve". It is chosen during production within REQ-010, which bounds it to an interface carrying no transport, serialization, or rendering concern.
- **TBD-003** — The internal representation of a difference — whether the service holds a per-element before/after pair, a change classification, an added/changed/removed partition, or an element list with no classification — is fixed by no accepted source. This is the representational side of CON-003 and is chosen during production within REQ-003 and REQ-005; the corpus's only declared difference type, DriftFinding, is a different act's output (CLM-015) and is not made this service's representation by this contract.
- **TBD-004** — Where the delta-composition record of OUT-001 lives and in what form it is published are fixed by no accepted source; they are chosen during production within REQ-005, which fixes what it must declare rather than where it sits.

## Completion and Reliance Basis — Epistemology

The requirements below state what future production must satisfy. Nothing in
this section asserts that a service, a record tier, a reconcile engine, a
baseline, a schema, or a test exists.

- **REQ-001** — The service shall serve, for a commit SHA supplied by the caller, the differences in what PEC holds since that anchor, per `SOW-005` (CLM-001) and `PEC-ORI-002` (CLM-002). The caller-supplied SHA shall be an input of the request and shall never be defaulted, substituted, inferred, silently widened, or replaced by any value the service or the record tier already holds — in particular not by the upstream reconcile engine's own examined-through baseline, which is a different anchor owned upstream (CLM-009, CLM-010, CON-001).
- **REQ-002** — Every fact the service serves shall be derived from record-tier entities as obliged by the entity-model contract reached transitively under `C-03` (CLM-011) and populated by the reconcile path (CLM-009). No served fact shall rest on a presence-tier fact, on a stream or event input, on a cached artifact, or on any value the record tier does not carry, per `PEC-K-07` ("the reconciler over file truth is the source of every record-tier fact"), `PEC-K-05` ("Presence facts never enter record-tier citations"), and `PEC-PRS-007` ("Presence data is operational only and shall never appear in record-tier citations").
- **REQ-003** — Nothing the service composes, retains, or serves shall carry file content or diff content; every delta element shall be expressed in paths, counts, identifiers, states, SHAs, and hashes, per `PEC-K-10` (CLM-013). This restriction binds the served value itself and not only the service's internals, and it is additional to, not a substitute for, the reduction obliged upstream at the point of the Git read and the store-side ingest guard owned elsewhere (CLM-009, CLM-015).
- **REQ-004** — The service shall be read-only over the record tier and over Git: it shall create, modify, or delete no source file, governed file, register, lifecycle file, or store record; it shall perform no Git state change of any kind — no commit, branch, ref, index, stash, checkout, worktree, or configuration write; and it shall provide no path that records an adoption, a ruling, or a direction, per `PEC-GAT-004` ("PEC shall provide no write path that records adoption, ruling, or direction (PEC-K-02; K-AUTH-1)"), `PEC-K-06` observation-not-participation, and the permanent non-goal "Not a Git actor. Read-only plumbing access; CHANGE owns Git state" (CLM-013).
- **REQ-005** — The service shall declare, in the delta-composition record — a readable component of OUT-001 — for each class of element it can serve: the record-tier entity or entities it is derived from, the rule by which the caller-supplied SHA is resolved against the state the record tier carries, the scope unit over which the difference is taken, and its absence semantics. An element produced by an undeclared entity source, an undeclared resolution rule, or an undeclared scope unit is prohibited. This requirement makes the four open surfaces of CON-002 through CON-005 visible and reviewable in the artifact rather than settled by this contract.
- **REQ-006** — Where the caller-supplied SHA cannot be resolved against the state the record tier carries, where the record tier holds no reconciled state for the requested scope, or where the reconcile reported a feed as absent, unreadable, malformed, stale, or grammar-unrecognized, the served value shall state that limitation explicitly against the affected element and shall present no derived, defaulted, inferred, or carried-forward value in its place. Silent omission is prohibited (`PEC-ORI-006`: "Where a feed is unparseable or stale, the response shall state the measurement limitation explicitly; silent omission is prohibited"), the posture is `PRD.md` §7.3 coverage honesty — "a figure the records don't support is absent and said to be absent" — and `PEC-K-01` graceful absence governs the outer case. Rendering such a limitation into an orientation response is `DEL-04-05`'s act under `SOW-009` (CLM-015); this service carries it through so that act has something to render.
- **REQ-007** — Each served element shall carry through the citation provenance the record-tier entity it came from holds — file path, anchor, and/or SHA to the live source — so that the stamping-and-citation deliverable can attach it. This deliverable shall attach no citation to a response, shall stamp no response with examined-through SHA, generation time, or per-feed freshness, and shall compute no freshness value; those acts are `DEL-04-03`'s under `SOW-006` and `SOW-007`, and they apply to this service's returns because the delta serve is within the general term "orientation" as the Vocabulary Map defines it (CLM-007, CLM-015).
- **REQ-008** — This deliverable shall define no record-tier entity type, no schema field, no feed grammar, and no reconcile path, and shall not depend on any upstream artifact existing. The record-tier types are `DEL-01-01`'s under `SOW-001`, reached transitively across three edges rather than by a local edge (CLM-011), and every element this service serves shall be constructed against a type that model obliges (CON-003).
- **REQ-009** — The service shall implement no reconcile of its own: no full rebuild, no incremental reconcile, no delta-to-work resolution, and no baseline record or baseline advance. It shall neither maintain an examined-through value of its own nor treat the upstream engine's baseline as a value it may write, correct, or advance; where it reads such a value it reads it as record-tier state, per the upstream obligations quoted in CLM-009 (CON-001).
- **REQ-010** — The service shall expose its value through an in-process interface and shall implement no socket binding, no token or access-class check, no wire schema or serialization format, no subscription or stream endpoint, and no rendering; those are `PKG-08`'s and `PKG-09`'s under the package exclusions recorded in CLM-006, and the SSE subscription in particular is `DEL-08-05`'s deferred `P4` act (CLM-012). The served value shall be shaped so that the transport deliverables can serialize it without this deliverable's participation (TBD-002).
- **REQ-011** — The service shall perform no act owned by another deliverable. In particular it shall compose no per-loop orientation return of the six `PEC-ORI-001` components, perform no rebuild or incremental reconcile, classify no drift between successive snapshots, run no parity diff, evaluate no gate precondition and produce no Explain-shaped verdict, perform no scope parameterization by loop / project / package, render no measurement limitation into an orientation response, stamp no response and attach no citation, perform no presence-tier or worktree scan, expose no subscription, assert or measure no latency bound, and run no kill test; each is cited to its owner in CLM-015 and none is discharged here.
- **REQ-012** — The service shall be deterministic over its inputs: two serves for the same caller-supplied SHA against the same record-tier state shall produce the same value, and a serve for a caller-supplied SHA against which the record tier carries no difference shall produce an explicitly empty delta rather than an omission, an error presented as emptiness, or a fabricated element. This is what keeps the comparison structural rather than a judgment (`PEC-K-04`, `OBJ-002`, CLM-004).
- **REQ-013** — The service shall produce a value only when called, and shall schedule no poll, push to no consumer, initiate no session act, open no subscription, and assert no consumption cadence; polling moments and mode-proportional contact are the harness's under `PEC-K-03` and `PEC-K-11` (CLM-016).
- **REQ-014** — The service and its tests shall introduce no third-party runtime dependency and no external network egress, per `PEC-SVC-001` and `PEC-SVC-002`, whose standing enforcement is `DEL-01-05` covering `SOW-052` and `SOW-053` (CLM-015).
- **REQ-015** — Tests shall implement the verification methods declared in this contract; they shall not define scope, requirements, or acceptance criteria.

- **AC-001** — For a fixture record tier and a caller-supplied SHA, the served value is anchored on exactly the SHA the caller supplied, byte for byte; instrumentation of the call shows no substitution, defaulting, widening, or fallback to any examined-through, baseline, or otherwise service-held value; and this deliverable's source contains no path that supplies an anchor the caller did not.
- **AC-002** — Every element of a served value traces to a record-tier entity instance; inspection of the service's input surface finds no presence-tier, stream, event, or cached input contributing to any element; and a fixture carrying presence-shaped data alongside the record tier produces a served value in which no element derives from it.
- **AC-003** — For a content-dense fixture corpus whose changes since the caller's SHA span long prose bodies, quoted authored text, and diff-shaped content, inspection of every field of the served value and of everything the service retains finds no file content and no diff content — only paths, counts, identifiers, states, SHAs, and hashes.
- **AC-004** — A serve leaves the fixture source corpus, the fixture store, and the fixture repository's Git state byte-identical — same HEAD, refs, index, stash, worktree list, and configuration; the captured filesystem and store write inventory for a serve is empty; and this deliverable's source contains no Git write operation, no write, create, or delete call against any source file, governed file, register, lifecycle file, or store record, and no path that records an adoption, ruling, or direction.
- **AC-005** — The delta-composition record — the component of OUT-001 required by REQ-005 — names, for every class of element the service can serve, its source entity or entities, its caller-SHA resolution rule, its scope unit, and its absence semantics; and every element produced in a fixture run is traceable to the rule the record declares for it, with no element produced by an undeclared source, rule, or scope unit.
- **AC-006** — For fixture cases in which the caller-supplied SHA is unknown to the record tier, the record tier holds no reconciled state for the requested scope, and a feed was reported absent, unreadable, malformed, stale, and grammar-unrecognized in turn, the served value states the limitation against the affected element, names the affected element and the condition, and presents no derived, defaulted, inferred, or carried-forward value in its place.
- **AC-007** — Every element of a served value carries the citation provenance held by the record-tier entity it came from, and that provenance resolves to a file path, anchor, and/or SHA; and this deliverable's source contains no citation-attachment path, no examined-through-SHA or generation-time stamping path, and no freshness-computation path.
- **AC-008** — This deliverable's source defines no record-tier entity type, no schema field, no feed grammar, and no reconcile path; every served element is constructed against an upstream-obliged type; and no element of this deliverable asserts or requires that an upstream schema, entity model, reconcile engine, baseline record, store, parser, or registry artifact exists.
- **AC-009** — This deliverable's source and call graph contain no rebuild path, no incremental-reconcile path, no delta-to-work resolution, and no baseline record, write, or advance; and for a fixture in which an upstream-owned examined-through value is present in the record tier, a serve leaves that value unchanged and this deliverable's source contains no write against it.
- **AC-010** — The service is reachable only through its declared in-process interface; this deliverable's source contains no socket binding, token or access-class check, wire schema, serialization format, subscription or stream endpoint, or rendering code; and a consumer can serialize a served value without modifying this deliverable.
- **AC-011** — This deliverable's source and call graph contain no per-loop orientation composition of the six PEC-ORI-001 components, no rebuild or reconcile path, no drift-classification path, no parity-diff path, no gate-evaluation or Explain-verdict path, no scope-parameterization path, no limitation-rendering path, no stamping or citation-attachment path, no presence or worktree scan, no subscription, no latency measurement or bound assertion, and no kill-test execution; and no test in this deliverable asserts a criterion belonging to any of them.
- **AC-012** — Two serves for the same caller-supplied SHA against the same fixture record-tier state produce identical values; and for a caller-supplied SHA against which the fixture record tier carries no difference, the served value is an explicit empty delta distinguishable in the return from both an unresolved-anchor condition and a stated limitation.
- **AC-013** — A serve occurs only in response to a call: instrumentation of a fixture run shows no timer, scheduler, subscription, push, or session-lifecycle act originating in this deliverable, and this deliverable's source contains no polling or cadence logic.
- **AC-014** — The service and its tests add no third-party runtime dependency and make no network call, leaving the `DEL-01-05` zero-dependency and locality assertion intact.
- **AC-015** — The test suite implements VER-001 through VER-014, executes in the `PKG-04` test run, passes, and introduces no acceptance criterion absent from this contract.
- **AC-016** — The REVIEW gate confirms this contract's traceability to `SOW-005`, `OBJ-001`, and `OBJ-002`; confirms that both objective mappings are stated as register-direct and pre-SCA-002 at the strength the record carries, including the difference between the `OBJ-001` enumerated membership and the `OBJ-002` "supported by" form; confirms that the single upstream edge is stated at its own `PROPOSAL` stratum with its empty evidence cells recorded as an observation rather than repaired; and confirms that no `PKG-01`, `PKG-03`, sibling `PKG-04`, `PKG-05`, `PKG-06`, `PKG-08`, or `PKG-10` scope has been absorbed.

- **CON-001** — The scope item's anchor and the upstream edge's anchor are different values, and no accepted source relates them. `SOW-005` anchors on a commit SHA the caller supplies. The edge that places this deliverable says deltas "ride the incremental examined-SHA machinery", and that machinery is anchored on the commit SHA the upstream engine itself last examined through — a value that contract obliges the engine to record and advance for its own runs, expressly without asserting that any other deliverable records or maintains one (CLM-009). The upstream contract further carries its own conflict record on exactly that value: its first sentence reads "The edge that places this deliverable presupposes an examined-SHA baseline that no accepted source obliges anyone to produce." (`DEL-03-02/ScopeOfWork.md`, CON-001, first sentence of that record, quoted in full as a whole sentence; ID-shaped text in this quotation is upstream source context, not a local definition or reference), and its informational twin states in full:

> - **TBD-004** — Where the baseline record durably lives is fixed by no accepted
>   source. This is the informational side of CON-001: REQ-004 obliges the engine
>   to keep and advance a baseline and to write it only through the
>   upstream-declared write set, and settles nothing about which store object
>   holds it.
>
> (`DEL-03-02/ScopeOfWork.md`, Ontology section; quoted in full, not elided.
> ID-shaped text inside this quotation is upstream source context, not a local
> definition or reference.)

  This contract records the gap rather than closing it in either direction. It does not conflate the two SHAs: REQ-001 forbids substituting any service-held or upstream-held value for the caller's anchor, and REQ-009 forbids this service from owning, writing, or advancing a baseline. It does not answer the upstream ownership question or fix the baseline's home, and no requirement here imposes anything on the upstream deliverable. Whether a caller-supplied SHA must relate to the engine's baseline at all — and if so, whether that relation is an obligation of this package, of the reconcile package, or of a shared record-tier representation — is a scope-change question, not a production decision.
- **CON-002** — The edge delivers obligations but not the query surface its rationale names. The upstream contract states in its own voice that the engine shall "serve no caller-supplied-SHA delta query" and that being consumed by this deliverable does not oblige it "to expose a caller-parameterized query" (CLM-009, CLM-010). No other accepted source assigns a caller-parameterized derivation path to any deliverable. The consequence is that how a caller's anchor becomes a served difference — whether by comparing record-tier state against an anchor the record tier can locate, by comparing successive stored snapshots, or otherwise — is assigned by nothing in the accepted corpus. This contract does not fill that gap by assuming upstream machinery: REQ-002 binds the served facts to record-tier entities, REQ-005 obliges the chosen resolution rule to be declared, and REQ-009 forbids building a reconcile here. A production choice that added a query surface to the upstream engine, or that read a baseline out of another deliverable's artifact, would take a decision in the wrong place.
- **CON-003** — What a delta ranges over is fixed by no accepted source. `PEC-ORI-002` and `SOW-005` say "deltas" and stop; the `PRD.md` §7.1 record tier enumerates eleven rows and states a purpose for each without saying which of them a difference is taken over, or what constitutes a difference for each. The corpus's one declared difference type is DriftFinding — "A classified difference between the current reconcile and the prior snapshot, or between PEC and harness parity output" — and both of its stated forms belong to other acts: classification between successive snapshots is `DEL-03-03`'s under `SOW-019`, and parity output is `DEL-03-04`'s under `SOW-020`. Neither form is a difference against a caller-supplied anchor. This contract records the gap rather than closing it: REQ-008 forbids defining a record-tier type here, REQ-002 binds every element to an entity the model obliges, and REQ-005 obliges the entity coverage to be declared per element class, so that whatever mapping production settles on is visible and reviewable. Defining a new record-tier type to represent a caller-anchored difference would take `DEL-01-01`'s decision in the wrong place; concluding that the service may serve an arbitrary subset would leave `SOW-005` unbounded.
- **CON-004** — The scope unit over which the difference is taken is unstated, and the two accepted passages that touch it do not agree. `SOW-004`'s statement carries the qualifier "per-loop"; `SOW-005`'s carries no scope qualifier at all. The `PRD.md` §5 modes ladder, quoted in CLM-016, describes the single-Agent-0 mode as consuming "loop-scoped orientation + deltas" and the concurrent-Agent-0 mode, at "N, overlapping scope", as consuming "orientation, deltas, presence, notices" without a scope word. Scope parameterization by loop / project / package is itself a separate scope item, `SOW-008`, owned by `DEL-04-04` at `P2` — one phase after this service. This contract therefore neither fixes a scope unit nor absorbs the parameterization act: REQ-005 obliges the unit actually used to be declared, REQ-011 forbids implementing the parameterization deliverable's scope, and REQ-006 governs a request whose scope the record tier cannot serve. Whether `P1`'s delta serve is loop-scoped by default, corpus-wide, or parameter-bearing ahead of `SOW-008` is a question for the accepted sources and, if it changes either scope item, for a scope change.
- **CON-005** — How a caller-supplied SHA is resolved, and what the honest answer is when it cannot be, are fixed by no accepted source. Nothing states that the caller's SHA must be an ancestor of, reachable from, or otherwise related to the commit state PEC has examined; nothing states the behaviour for a SHA that is unknown, unreachable, from an unrelated history, or ahead of what PEC has seen. The corpus's only reachability act is `PEC-GAT-001`'s gate precondition — "PEC shall deterministically evaluate gate preconditions that reduce to file/Git facts: ruling presence, ruling-SHA commit reachability, receipt ancestry, snapshot/freeze presence, register-row status" — owned by `DEL-05-01` under `SOW-022` at `P2`, to which this deliverable holds no edge (CLM-008, CLM-014). The posture of the answer is nevertheless fixed rather than open: `PEC-ORI-006`, `PRD.md` §7.3 coverage honesty, and `PEC-K-01` graceful absence forbid a fabricated or partially guessed value, and REQ-006 states that as a checkable obligation. What remains genuinely unsettled is whether resolving the anchor requires a Git read at all — and, if it does, whether performing one here is consistent with the read-only plumbing posture of CLM-013 or belongs with an act already declared to own reachability. That question is not answered by this contract.

## Production and Verification Method — Praxeology

Production proceeds in the order upstream-contract survey → anchor resolution
and its absence semantics → element coverage and the composition path →
content-minimal reduction of the served value → provenance carry-through and
limitation carry-through → determinism and the empty case → tests. The
upstream-contract survey comes first because the single predecessor at
`INITIALIZED` supplies obligations rather than artifacts, and because that
contract's own text is what bounds the edge rationale's word "ride" (CLM-010);
a composition path written against an imagined caller-parameterized query would
violate CON-002 before any code existed. Anchor resolution precedes element
coverage because the caller's SHA is the parameter the whole act turns on and
because CON-005's honest-absence case cannot be specified after a composition
path already assumes a resolvable anchor. The content-minimal reduction is
treated as a property of how each element is constructed rather than as a filter
applied to a finished value, because a caller asking what changed since a SHA is
asking the one question whose natural answer `PEC-K-10` forbids (CLM-013). All
work is bounded to this deliverable folder and the `PKG-04` service-core source
it names; this contract authorizes no register, decomposition, PRD, or
upstream-deliverable edit, and it neither defines nor reshapes the entity model
it reads, the store it reads through, the reconcile that populates it, or the
grammars that feed it. Tests implement the verification methods below and create
no scope.

- **VER-001** — Anchor-fidelity exercise: serve for a set of caller-supplied SHAs over a fixture record tier and assert per case that the value's anchor equals the supplied SHA byte for byte; instrument the call path and assert no substitution, defaulting, widening, or fallback occurs; and inspect this deliverable's source for any path that supplies an anchor the caller did not, asserting none.
- **VER-002** — Provenance and tier inspection: for a sample element of each class a serve produces, trace it to the record-tier entity instance that yielded it; inspect the service's input surface for presence-tier, stream, event, and cached inputs and assert none contributes; and serve over a fixture carrying presence-shaped data alongside the record tier and assert no element derives from it.
- **VER-003** — Content-minimal inspection: serve over a content-dense fixture corpus whose changes since the caller's SHA carry long prose bodies, quoted authored text, and diff-shaped content, then dump every field of the served value and everything the service retains, and assert field by field that none carries file or diff content.
- **VER-004** — Read-only exercise: hash the fixture source corpus tree and store before and after a serve and assert byte-identity; capture HEAD, all refs, the index, the stash list, the worktree list, and the configuration of a fixture repository before and after and assert equality on each; capture every filesystem and store write performed during the run and assert the inventory is empty; and inspect this deliverable's source and call graph for Git write operations, for write, create, or delete calls against source files, governed files, registers, lifecycle files, or store records, and for any adoption-, ruling-, or direction-recording path, asserting each absent.
- **VER-005** — Composition-record exercise: read the delta-composition record and assert it names, for every element class the service can serve, its source entities, its caller-SHA resolution rule, its scope unit, and its absence semantics; then run a fixture serve and trace each produced element to the declared rule, asserting no element arises from an undeclared source, rule, or scope unit.
- **VER-006** — Limitation and unresolvable-anchor exercise: serve over fixtures in which the caller-supplied SHA is unknown to the record tier, the record tier holds no reconciled state for the requested scope, and a feed was reported absent, unreadable, malformed, stale, and grammar-unrecognized in turn, and assert per case that the value states the limitation against the affected element, names the element and the condition, and presents no derived, defaulted, inferred, or carried-forward substitute.
- **VER-007** — Citation carry-through: for each element of a fixture serve, assert the citation provenance of its source entity is present in the served value and resolves to a file path, anchor, and/or SHA; and inspect this deliverable's source for citation-attachment, examined-through-SHA or generation-time stamping, and freshness-computation paths, asserting each absent.
- **VER-008** — Type-boundary inspection: assert every served element is constructed against an entity type the upstream model obliges; inspect this deliverable's source for record-tier and presence-tier type definitions, schema fields, feed grammars, and reconcile paths and assert none; and inspect source and fixtures for any assumption that an upstream schema, entity model, reconcile engine, baseline, store, parser, or registry artifact exists, asserting none.
- **VER-009** — Reconcile-boundary inspection: inspect this deliverable's source and call graph for a rebuild path, an incremental-reconcile path, a delta-to-work resolution, and any baseline record, write, or advance, asserting each absent; then serve over a fixture whose record tier carries an upstream-owned examined-through value and assert that value is unchanged after the run.
- **VER-010** — Interface-boundary inspection: assert the service is reachable only through its declared in-process interface; inspect its source for socket binding, token or access-class checks, wire schemas, serialization formats, subscription or stream endpoints, and rendering code, asserting each absent; and serialize a served value from a separate consumer module without modifying this deliverable.
- **VER-011** — Adjacent-act inspection: inspect the module's call graph and source for per-loop orientation composition, rebuild or reconcile, drift classification, parity diffing, gate evaluation or Explain-verdict construction, scope parameterization, limitation rendering, stamping, citation attachment, presence or worktree scanning, subscription, latency measurement or bound assertion, and kill-test paths, asserting each absent; and review this deliverable's tests for any criterion belonging to another deliverable, asserting none.
- **VER-012** — Determinism and empty-case exercise: serve twice for the same caller-supplied SHA against an unchanged fixture record tier and assert the two values are identical; then serve for a SHA against which the fixture carries no difference and assert the value is an explicit empty delta distinguishable in the return from an unresolved-anchor condition and from a stated limitation.
- **VER-013** — Initiation inspection: instrument a fixture run and assert no timer, scheduler, subscription, push, or session-lifecycle act originates in this deliverable; and inspect its source for polling or cadence logic, asserting none.
- **VER-014** — Inspect the `PKG-04` dependency manifest and this module's import graph for third-party runtime dependencies and network calls, and re-run the zero-dependency and locality enforcement once the deliverable that owns it is available, without discharging it here.
- **VER-015** — Run the `PKG-04` test suite and confirm that each of VER-001 through VER-014 has a corresponding executing automated test and that no test asserts a criterion absent from this contract.

## Governing Values and Decisions — Axiology

- **AX-001** — Two objectives govern this deliverable and they pull on different parts of it. `OBJ-001` makes orientation a query rather than a derivation; `OBJ-002` makes staleness a comparison rather than a judgment. A delta since a caller-supplied SHA is the point where those two meet: the caller states what it already knew as a structural value, and the answer is the difference — not a summary, not an assessment, and not a recomposed full orientation the caller must diff for itself. A service that answered by returning everything and letting the consumer decide what was new would satisfy neither objective while appearing to satisfy both.
- **AX-002** — `PEC-K-04` is `OBJ-002`'s product invariant, and this deliverable is the one place where the comparator is supplied from outside. Everywhere else in the corpus a SHA comparison is between two values PEC holds — the engine's baseline against the commit state it observes, or one snapshot against its successor. Here one side of the comparison is the caller's assertion about its own state. REQ-001 keeps that asymmetry honest by forbidding the service to quietly answer a question the caller did not ask, which is what substituting PEC's own anchor would be.
- **AX-003** — The distinction between the two SHAs is the single most absorbable error available to this contract, and it is why CON-001 stays open rather than being resolved by a plausible reading. The edge rationale's phrase "ride the incremental examined-SHA machinery" is easy to read as an instruction to answer from the engine's baseline. The upstream contract forecloses that reading twice in its own voice — it declines to expose a caller-parameterized query and it records the baseline itself as owned by no accepted source. Treating the rationale as an obligation on the upstream deliverable, or as a guarantee that machinery exists, would convert a `PROPOSAL`-stratum rationale into scope neither contract states.
- **AX-004** — `PEC-K-10` content-minimal is a residency posture, and this deliverable is its sharpest serving-side test. The upstream engine's exposure is a diff it reads; this service's exposure is a diff it is *asked for*. A consumer that wants to know what changed since a SHA has an obvious use for the changed text, and the pressure to include it comes from the caller rather than from the implementation. REQ-003 therefore binds the served value itself, not only the internals, and AC-003 makes the boundary falsifiable against a fixture built to tempt it.
- **AX-005** — `PEC-ORI-006` honesty governs the failure mode, and the unresolvable-anchor case is this deliverable's version of it. A caller supplying a SHA PEC cannot place is asking a question PEC cannot answer, and the two dishonest answers are symmetric: an empty delta implying nothing changed, or a full state implying everything did. REQ-006 and REQ-012 keep the empty case and the unresolvable case distinguishable in the return, because `PEC-K-01` graceful absence is only meaningful if absence can be told apart from emptiness.
- **AX-006** — Unknowns stay marked, and four of the five conflicts here are gaps at the level of accepted truth rather than production choices. What a delta ranges over (CON-003), over what scope unit (CON-004), and how the anchor resolves (CON-005) are each unstated by every accepted source this contract reads, and CON-002 records that the derivation path itself is assigned to nobody. REQ-005 is the response: rather than choosing silently, the service is obliged to declare what it chose, so a later scope change or entity-model amendment can see the choice instead of reverse-engineering it. TBD-001 through TBD-004 are recorded on the same terms and resolved by inference nowhere.
- **AX-007** — Edge direction is a constraint on this contract, not a licence. `RequiredMaturity` `INITIALIZED` on the single upstream edge means the upstream *contract* is the reliable input, not any upstream artifact; this contract is written against the obligations quoted in CLM-009 and asserts nothing about upstream implementation state. Consuming one contract imposes no obligation on it — CON-001 and CON-002 record gaps in the upstream and accepted record and assign no work there — and being consumed by the `P4` subscription deliverable neither expands this contract's scope nor transfers any of that deliverable's into it (CLM-012).
- **AX-008** — This deliverable sits between three neighbours whose scope is easy to absorb by mistake, and the register settles all three. `DEL-04-01` composes the six-component per-loop return; this service serves a difference. `DEL-04-03` stamps every orientation response and attaches per-claim citations; this service carries provenance so that act has material. `DEL-04-04` parameterizes orientation by scope at `P2`; this service takes a SHA parameter under its own scope item and builds no scope parameterization. That the delta serve is itself within the general term "orientation" (CLM-007) is what makes the second boundary load-bearing rather than decorative: this service's returns are stampable material, and stamping them is not this contract's act.
- **AX-009** — One adjacent surface is noted with its actual basis, which is no edge. The sibling `DEL-04-01` contract records an open question about whether the examined-through SHA is one field or two — a component of the `SOW-004` return and a `SOW-006` response stamp — and this deliverable's own anchor question is a third occurrence of the same value. No dependency edge exists between the two deliverables in either direction: this deliverable's `Dependencies.csv` holds one `EXECUTION` row and it targets `DEL-03-02` (CLM-008). The adjacency is therefore cited as adjacency and nothing is inferred from it; no obligation, no representation, and no shared field is asserted between the two contracts.
- **AX-010** — The one upstream edge and the one downstream relation cited here are `PROPOSAL` stratum and are *accepted* at that stratum: `D-PEC-62` §1(4) records the owner accepting the DAG candidate v0.2 exhibit as "accepted, all strata as presented", and that packet reads "as presented" as accepting the exhibit's **flags as flags**, so what remains recorded-but-unresolved is the specific annotated set — `E-A11` (AMBIGUOUS_BASIS), `E-P69`/`E-N02` (PHASE_TENSION), `E-N13`/`E-N18` (LOW_CONFIDENCE), the `C-02` direction, and the `C-08` standing-node set — neither of which touches `[E-P33]` or `[E-P56]`, each of which carries an empty `Flag` column in the exhibit. Register-wide constraint `C-10` `STRATUM_RULE` ends "strata are provenance not authority": stratum records how an edge was derived, not whether it has been accepted, and citation converts no `PROPOSAL` into a `DECLARED`. That `[E-P33]` additionally carries an empty `BasisCitation`, and its register row an empty `EvidenceQuote` and a `SourceRef` of "location TBD", is a fact about the exhibit's evidence trail recorded in CLM-008 as an observation of the `OI-013` register-hygiene class — not a defect this contract is authorized to repair and not a reason to invent evidence.
- **AX-011** — `C-03` `PACKAGE_LEVEL`, `C-04` `PHASE_PRECEDENCE`, and `C-10` `STRATUM_RULE` are the three register-wide non-gating constraints recorded in this deliverable's `_DEPENDENCIES.md`, and blocker output under the `FULL_GRAPH` mode at threshold `INITIALIZED` is advisory visibility only, never work assignment. `C-03` reaches this deliverable transitively across three edges rather than by a local one (CLM-011), which is why this contract binds to the entity model as an obligation rather than as an interface it can see.
- **AX-012** — The objective mapping is stated at record strength and no higher. `SOW-005` → `OBJ-001;OBJ-002` is register-direct and pre-SCA-002 at both the ledger and deliverable levels; this contract therefore supplies no fresh derivation, asserts no confidence label the record does not carry, and creates no owner-confirmation criterion for it. It also declines to launder the one asymmetry it found: on the objective-side view the `OBJ-002` row carries `SOW-005` as "supported by" rather than as an enumerated mapped item, on both sides of the amendment, and AC-016 puts that difference in front of REVIEW as a check rather than resolving it here.
- **AX-013** — This contract is lifecycle-neutral. `_STATUS.md` remains the sole lifecycle authority and is untouched by the run that authored this document; the deliverable is at `OPEN` and nothing has been built.

**Quotation record.** Every quotation in this contract is verbatim from the
named source, and **no quotation in this document is elided** — none omits text
from the span it presents, and no ellipsis appears anywhere in this document.
The `..` sequences inside the SCA-002 `A001`, `A002`, and `A003b` quotations are
the sources' own range notation and are identified as such at the point of
quotation. Quoted spans shorter than their containing record are presented as
whole sentences, whole table rows, whole register rows, whole cells, or short
verbatim phrases, and are attributed as such where they appear: the `A001` and
`A002` target cells; the `A003b` `OBJ-001` and `OBJ-002` old/new blocks; the
`SOW-005` ledger row and its §2.1 SSOW row; the three §9 Vocabulary Map rows;
the `E-P33` and `E-P56` exhibit rows; the two `PRD.md` §5 modes-ladder rows; the
five `DEL-03-02` records quoted in CLM-009; that contract's `CLM-011` final
sentence, identified in CLM-010 as the final sentence of a longer record; its
`CON-001` first sentence, identified in CON-001 as the first sentence of a
longer record; and its `TBD-004`, quoted whole. The `PEC-K-*` quotations other
than `PEC-K-07`, and the `PEC-ORI-*`, `PEC-GAT-*`, `PEC-API-002`, `OBJ-001`,
`OBJ-002`, `PRD.md` §4.2, §7.3, and §8 quotations, are each complete rows,
complete cells, or complete sentences of their sources; the `PKG-04` and
`PKG-03` charter texts, the `C-03` `Statement` and `Notes` texts, the `C-07`
`Notes` text, the `C-10` closing clause, the `OI-013` issue text, and the
`SOW-004`, `SOW-041`, and `SOW-006` statements are complete register cells; the
`D-PEC-62` acceptance phrases quoted in AX-010 are short verbatim phrases,
identified there as such; and two further short verbatim phrases are quoted in
REQ-002 — the `PEC-K-07` span, which is the post-semicolon clause of that row
rather than the whole row, and the `PEC-PRS-007` span, which presents that row
without its trailing parenthetical "(PEC-K-05)".

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-005 OBJ-001 OBJ-002 | REQ-001, CLM-001, CLM-002, CLM-005, CLM-010, CON-001, AX-002 | AC-001 | VER-001 | Per-SHA serve records showing the returned anchor equal to the supplied SHA, the instrumented call path showing no substitution or fallback, and a recorded search of this deliverable's source for any service-supplied anchor |
| OUT-001 | SOW-005 OBJ-001 OBJ-002 | REQ-002, CLM-011, CON-003 | AC-002 | VER-002 | Per-element-class provenance traces from served element to record-tier entity, the input-surface inspection record, and the presence-shaped fixture run showing no element derived from presence data |
| OUT-001 | SOW-005 OBJ-001 OBJ-002 | REQ-003, CLM-013, AX-004 | AC-003 | VER-003 | Field-by-field dumps of the served value and of everything retained for a content-dense fixture corpus, showing no file or diff content |
| OUT-001 | SOW-005 OBJ-001 OBJ-002 | REQ-004, CLM-013 | AC-004 | VER-004 | Before/after corpus, store, and Git-state captures for a fixture serve; the captured filesystem and store write inventory showing empty; and call-graph inspection records for Git writes, governed-file writes, and adoption/ruling/direction paths |
| OUT-001 | SOW-005 OBJ-001 OBJ-002 | REQ-005, TBD-003, TBD-004, CON-002, CON-004, AX-006 | AC-005 | VER-005 | The delta-composition record itself, plus a fixture serve in which every produced element is traced to the source, resolution rule, and scope unit that record declares for it |
| OUT-001 | SOW-005 OBJ-001 OBJ-002 | REQ-006, CON-005, AX-005 | AC-006 | VER-006 | Per-case served values for an unknown anchor, an unreconciled scope, and absent, unreadable, malformed, stale, and grammar-unrecognized feeds, each naming the affected element and condition with no substituted value |
| OUT-001 | SOW-005 OBJ-001 OBJ-002 | REQ-007, CLM-007, CLM-015, AX-008 | AC-007 | VER-007 | Per-element citation-provenance traces resolving to file path, anchor, and/or SHA, plus recorded searches of this deliverable's source for citation-attachment, stamping, and freshness-computation paths |
| OUT-001 | SOW-005 OBJ-001 OBJ-002 | REQ-008, CLM-011, AX-011 | AC-008 | VER-008 | The element construction surface against the upstream-obliged types, plus recorded searches for record-tier and presence-tier type definitions, schema fields, feed grammars, reconcile paths, and upstream-artifact assumptions |
| OUT-001 | SOW-005 OBJ-001 OBJ-002 | REQ-009, CLM-009, CON-001, AX-003 | AC-009 | VER-009 | Recorded searches for rebuild, reconcile, delta-to-work, and baseline write or advance paths, plus the fixture run showing an upstream-owned examined-through value unchanged after a serve |
| OUT-001 | SOW-005 OBJ-001 OBJ-002 | REQ-010, CLM-006, CLM-012, TBD-002 | AC-010 | VER-010 | Interface-reachability evidence, recorded searches for socket, token, wire-schema, serialization, subscription, and rendering code, and a separate consumer module serializing a served value unmodified |
| OUT-001 | SOW-005 OBJ-001 OBJ-002 | REQ-011, CLM-003, CLM-015, AX-008 | AC-011 | VER-011 | Call-graph and source inspection records showing each named adjacent path absent, plus a review of this deliverable's tests confirming no criterion belonging to another deliverable |
| OUT-001 | SOW-005 OBJ-001 OBJ-002 | REQ-012, CLM-004, AX-001 | AC-012 | VER-012 | The two-serve comparison for an identical anchor and record-tier state, plus the no-difference serve showing an explicit empty delta distinguishable from an unresolved anchor and from a stated limitation |
| OUT-001 | SOW-005 OBJ-001 OBJ-002 | REQ-013, CLM-016 | AC-013 | VER-013 | Instrumented fixture-run records showing no timer, scheduler, subscription, push, or session-lifecycle act originating here, plus the source search for polling or cadence logic |
| OUT-001 | SOW-005 OBJ-001 OBJ-002 | REQ-014 | AC-014 | VER-014 | Dependency-manifest and import-graph inspection records, plus the zero-dependency and locality enforcement result once the deliverable that owns it is available |
| OUT-002 | SOW-005 OBJ-001 OBJ-002 | REQ-015, CLM-017 | AC-015 | VER-015 | PKG-04 test-run output mapping each executed test to its declared verification method, with no criterion asserted that this contract does not state |
| OUT-001 | SOW-005 OBJ-001 OBJ-002 | AX-007, AX-009, AX-010, AX-012, AX-013 | AC-016 | HUMAN_REVIEW: REVIEW gate confirms traceability to SOW-005, OBJ-001, and OBJ-002, confirms both mappings are stated as register-direct and pre-SCA-002 at the strength the record carries including the OBJ-002 "supported by" form, confirms the single upstream edge is stated at its PROPOSAL stratum with its empty evidence cells recorded rather than repaired, and confirms no upstream, sibling, or cross-package scope absorption | Review record citing the SOW-005 ledger row, the A001 and A002 target cells, the A003b OBJ-001 and OBJ-002 blocks, the E-P33 register row and exhibit row with their empty evidence cells, and the upstream, sibling, and cross-package deliverable boundaries |
