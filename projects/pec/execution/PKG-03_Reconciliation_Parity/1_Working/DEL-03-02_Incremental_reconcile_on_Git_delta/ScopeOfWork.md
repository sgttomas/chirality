---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-03-02
package_id: PKG-03
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@3623b958b
project_scope_refs: [SOW-018]
package_objective_refs: [OBJ-002]
---

# Scope of Work — DEL-03-02 Incremental reconcile on Git delta

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-03-02` — "Incremental
reconcile on Git delta" — in `PKG-03` Reconciliation & Parity of the PEC v2
build. It covers project scope item `SOW-018` in service of package objective
`OBJ-002`.

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.2** (`current_basis`, SCA-002 successor; accepted 2026-07-25 at
D-PEC-64 closure, commit `3623b958b`). The deliverable-local `_REFERENCES.md`
still names "revision 1.1, accepted working surface"; that phrase is superseded
provenance left by a deferred pointer sweep (SCA-002 `Handoff_State.md`, open
item `OI-B`, dispositioned `DEFERRED_BY_HUMAN`), and `_CONTEXT.md`'s own
supersession line records revision 1.1 as "superseded by revision 1.2
(`current_basis`, SCA-002 successor)". This contract cites revision 1.2.

**Objective warrant.** `CoversScopeItems` is one row, and its `OBJ-002`
provenance is **register-direct, pre-SCA-002**. The `SOW-018` ledger row
already carried `OBJ-002` in its `ObjectiveIDs` cell before the scope change,
and the record shows this from three independent sides.

First, SCA-002's action `A001` is the action that populated empty
`ObjectiveIDs` cells, and it enumerates its twenty target rows. Its
action-register target cell reads in full:

> `ScopeLedger.csv` `ObjectiveIDs` — **20 IN rows** (`SOW-001, 003, 011..017,
> 021, 025, 040, 042, 052, 053, 054, 056, 088, 089, 094`)
>
> (`Brief.md`, action-register row `A001`, target cell, quoted in full without
> elision. ID-shaped text inside this quotation is upstream source context, not
> a local definition or reference.)

`SOW-018` is not among the twenty, and the preview's own preamble to that row
set records "All cells currently empty; only this column changes on these
rows" — so the twenty were the empty cells, and `SOW-018` was not one of them.

Second, the §3 objective row confirms the same from the other side. The
recorded old and new text of the `OBJ-002` row's two amended columns reads in
full:

> ```
> OLD col4: SOW-006, SOW-018, SOW-019; supported by SOW-005
> NEW col4: SOW-001, SOW-006, SOW-011..019; supported by SOW-005
> OLD col5: DEL-03-02, DEL-03-03, DEL-04-02, DEL-04-03
> NEW col5: DEL-01-01, DEL-02-01..07, DEL-03-02, DEL-03-03, DEL-04-02, DEL-04-03
> ```
>
> (`Amendment_Preview.md`, action `A003b`, line 321 block, quoted in full
> without elision. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference.)

Both `SOW-018` and `DEL-03-02` stand unchanged on both sides of the amendment:
the scope item was already in the objective's mapped-items cell and the
deliverable was already in its mapped-deliverables cell. What SCA-002 widened
around them was the parser layer, not this row.

Third, SCA-002 measured the strength of that pre-existing mapping and used it
as an attribution anchor for other rows. In a table whose columns are
`Precedent | Mapping | Status` the measurement reads:

> | `SOW-018`, `SOW-019` (PEC-RCN-003/004) | `OBJ-002` | **Valid** — OBJ-002's register locus is the reconciler layer |
>
> (`Amendment_Preview.md`, "Register precedents (measured) — and one I
> withdraw". ID-shaped text inside this quotation is upstream source context,
> not a local definition or reference.)

The packet states the same reading in prose, in a sentence it labels evidence
against its own recommendation:

> OBJ-002's register locus is the reconciler layer — `SOW-018` (incremental,
> Git-delta-keyed), `SOW-019` (drift classification), `SOW-006` (SHA stamping).
>
> (`Amendment_Preview.md`, Q2 "Evidence for narrowing, stated because it is
> real". ID-shaped text inside this quotation is upstream source context, not a
> local definition or reference.)

Two consequences bind this contract. First, the deliverable-level
`SupportsObjectives` value `OBJ-002` in `Deliverables.csv` is **not**
SCA-002-authored: `DEL-03-02` is not among the seventeen deliverable rows that
amendment changed, and the cell's warrant is the ledger row's own
register-direct mapping. Second, because the mapping is register-direct and
independently measured **Valid** rather than ruled, drafted, or
confidence-labelled, this contract creates no owner-confirmation acceptance
criterion for it and supplies no fresh derivation of it. `AC-015` puts the
traceability in front of the REVIEW gate as a check, not as an open question.

- **CLM-001** — The accepted `ScopeLedger.csv` row for `SOW-018` reads in full, under the register's ten columns `ScopeItemID,InOutStatus,ScopeItemStatement,SourceRef,PackageID,DeliverableIDs,ObjectiveIDs,DecisionRef,OpenIssue,Notes`:

> `SOW-018,IN,"Run reconciliation incrementally, keyed on Git delta since the last examined SHA",PEC-RCN-003,PKG-03,DEL-03-02,OBJ-002,,FALSE,`
>
> (Field-by-field: `DecisionRef` empty and `Notes` empty — two of the ten
> fields are unpopulated, `Notes` trailing; `OpenIssue` `FALSE`. Unlike the
> sibling rebuild row, no boundary decision and no product-invariant note rides
> this scope item. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference.)

  The `SOFTWARE_DECOMP.md` §2 SSOW row for the same item repeats the statement without the register-only columns and likewise leaves its `Notes` column empty: "| SOW-018 | IN | Run reconciliation incrementally, keyed on Git delta since the last examined SHA | PEC-RCN-003 | |".

- **CLM-002** — `SOW-018`'s `SourceRef` cell names one locus, `PEC-RCN-003`, the `PRD.md` §9.2 reconciliation requirement, quoted here in full as it reads: "Reconciliation shall run incrementally, keyed on Git delta since the last examined SHA." It is one of six `PEC-RCN-*` requirements in that block, and the other five are covered elsewhere: `PEC-RCN-001` and `PEC-RCN-006` by the full-rebuild reconciler under `SOW-010` and `SOW-021`, `PEC-RCN-002` by the seven `PKG-02` feed units under `SOW-011`..`SOW-017`, `PEC-RCN-004` by drift classification under `SOW-019`, and `PEC-RCN-005` by harness parity diffing under `SOW-020` (CLM-012). This contract covers exactly one of the six.
- **CLM-003** — `OBJ-002` states "Staleness is detected structurally by SHA comparison, never by judgment", `SourceRef` `§3.2` (`SOFTWARE_DECOMP.md` §3; `PRD.md` §3 outcome 2, which reads "Staleness is detected structurally (SHA comparison), not by judgment"). At revision 1.2 its "Mapped Scope Items" cell reads "SOW-001, SOW-006, SOW-011..019; supported by SOW-005" and its `MappedDeliverables` cell reads "DEL-01-01, DEL-02-01..07, DEL-03-02, DEL-03-03, DEL-04-02, DEL-04-03". The objective's product invariant is `PEC-K-04` **Staleness is a comparison**, whose statement reads in full: "Every response carries the examined-through commit SHA and per-feed freshness; consumers detect staleness structurally." This deliverable is the reconcile-side member of that objective: it is where the SHA comparison selects work, rather than where a response is stamped or a difference is classified.
- **CLM-004** — The register's own note on the `SOW-054` performance row records the alternative reading that was considered and not taken, which fixes a boundary this contract must respect. `SOW-054`'s statement is "Complete full rebuild within a bound confirmed at P1 (target minutes); incremental reconcile within seconds", `SourceRef` `PEC-SVC-003`; SCA-002 recorded that its second clause points at this deliverable's objective and still ruled the row to `OBJ-005` for `DEL-03-06`. The seconds-scale incremental bound is therefore `DEL-03-06`'s measurement under `SOW-054`, not this contract's, and this contract asserts no bound (REQ-011, CLM-012).

## Deliverable Definition — Ontology

`DEL-03-02` is typed `BACKEND_FEATURE_SLICE` at Context Envelope `M` with
`PhaseHint` `P1`. `Deliverables.csv` records its `AnticipatedArtifacts` as
"Incremental engine + tests" and leaves `ContextEnvelopeNotes` empty, so there
are no envelope notes to carry forward and `_CONTEXT.md` records "(none)". The
outputs of this contract are bounded by that artifact naming: exactly the
incremental engine and its tests, and nothing beyond those two artifacts and
the components each of them declares as part of itself.

- **OUT-001** — An incremental reconcile engine in the PEC service core: it determines, from the Git delta between the commit state it observes now and the commit SHA it last examined through, which sources have changed for each registered loop, reconciles the record tier over that selection, and records the new examined-through baseline. The engine's **baseline record** — the durable statement of the commit SHA a completed reconcile examined through — is a component of this output rather than a third artifact, since it is the engine's own state and the register names exactly two artifacts.
- **OUT-002** — An automated test suite covering the incremental path, its baseline handling, and its equivalence to the full-rebuild result, implementing the verification methods declared in this contract.

### Identity of record

- **CLM-005** — `DEL-03-02` is named "Incremental reconcile on Git delta", Type `BACKEND_FEATURE_SLICE`, Context Envelope `M`, `PhaseHint` `P1`, `ResponsibleParty` `TBD`, `AnticipatedArtifacts` "Incremental engine + tests", `CoversScopeItems` `SOW-018`, `SupportsObjectives` `OBJ-002`, `ContextEnvelopeNotes` empty, with the register `Description` field reading "Reconciliation keyed on Git delta since last examined SHA." Sources: `Deliverables.csv` row `DEL-03-02` and the `SOFTWARE_DECOMP.md` §5 PKG-03 table row "| DEL-03-02 | Incremental reconcile on Git delta | BACKEND_FEATURE_SLICE | M | P1 | SOW-018 |".
- **CLM-006** — The `PKG-03` package charter (`SOFTWARE_DECOMP.md` §4) is "The guaranteed path from file truth to record tier: one-command rebuild, incremental Git-delta reconcile, drift classification, harness parity diffing, stream-loss recovery guarantee, store-only writes, rebuild performance bounds", covering "SOW-010, 018, 019, 020, 021, 038, 054 (7)", with "Stream ingest mechanics (PKG-07); parsers (PKG-02)" recorded as explicitly out of package scope. Of those seven items this deliverable covers exactly one: the incremental Git-delta reconcile.

### Placement in the work graph

- **CLM-007** — This deliverable has **one** accepted `EXECUTION` upstream edge and **two** `ANCHOR` rows, held as `Dependencies.csv` register rows `DEP-03-02-001` through `DEP-03-02-003` at `RegisterSchemaVersion` `v3.1`. The two anchors are `DEP-03-02-001` (`IMPLEMENTS_NODE`: package-local to `PKG-03`) and `DEP-03-02-002` (`TRACES_TO_REQUIREMENT`: the `SOW-018` requirement trace). The single `EXECUTION` row is `DEP-03-02-003`, attributed by column: `FromPackageID` `PKG-03`, `FromDeliverableID` `DEL-03-02`, `FromDeliverableName` "Incremental reconcile on Git delta", `DependencyClass` `EXECUTION`, `AnchorType` `NOT_APPLICABLE`, `Direction` `UPSTREAM`, `DependencyType` `PREREQUISITE`, `TargetType` `DELIVERABLE`, `TargetPackageID` `PKG-03`, `TargetDeliverableID` and `TargetRefID` `DEL-03-01`, `TargetName` "Full-rebuild reconciler (one command)", `TargetLocation` `execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command`, `Statement` "Incremental reconcile presupposes the full-rebuild path and examined-SHA baseline", `EvidenceFile` `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md`, `SourceRef` "location TBD", `EvidenceQuote` **empty**, `Explicitness` `IMPLICIT`, `RequiredMaturity` `INITIALIZED`, `ProposedMaturity` `TBD`, `SatisfactionStatus` `PENDING`, `Confidence` `MEDIUM`, `Origin` `EXTRACTED`, `FirstSeen` and `LastSeen` `2026-07-25`, `Status` `ACTIVE`, `Notes` "PROPOSAL; Flag=none; EdgeID=E-P26".

  The corresponding accepted DAG exhibit row, under that exhibit's columns `EdgeID,PredecessorID,SuccessorID,Stratum,EdgeKind,Flag,BasisCitation,Rationale`, reads `E-P26,DEL-03-01,DEL-03-02,PROPOSAL,CONSUMES,,,Incremental reconcile presupposes the full-rebuild path and examined-SHA baseline` — `Flag` empty and `BasisCitation` **also empty**. The register row's empty `EvidenceQuote` and "location TBD" `SourceRef` agree with that: this edge is warranted by its `Statement` and by the two deliverables' own accepted contracts, not by a quoted source. Its direction is nonetheless unambiguous — `DEL-03-01` is the predecessor and this deliverable the successor.

- **CLM-008** — The single predecessor is at lifecycle state `INITIALIZED`, which is the maturity the edge requires. `INITIALIZED` means the upstream **contract** is the reliable input: its accepted `ScopeOfWork.md` exists, and no reconciler, store, schema, parser, or registry does. Nothing in this contract asserts that any upstream artifact exists. The obligations this contract binds to are that contract's stated obligations. From `[E-P26]`, the full-rebuild path this engine presupposes, its write posture, and its honesty posture are `DEL-03-01`'s, quoted here in full and without elision:

> - **OUT-001** — A full-rebuild reconciler entry point in the PEC service core:
>   one command that rebuilds the record tier in full from file sources for the
>   loops the registry names, writing only into the store and into the generated
>   views it declares. The entry point's **declared-view record** — the readable
>   artifact in which it declares every generated view it writes (REQ-006) — is a
>   component of this output rather than a third artifact: it is the entry
>   point's own self-declaration, so the register's `AnticipatedArtifacts`
>   naming of exactly two artifacts is preserved.
> - **REQ-001** — The reconciler shall expose a single command that rebuilds the
>   record tier in full from file sources for every loop the registry names, per
>   `SOW-010` (CLM-001) and `PEC-RCN-001` (CLM-003). A rebuild shall require no
>   operator step, repair action, or manual sequence beyond that one invocation.
> - **REQ-002** — Every record-tier fact the rebuild produces shall be derived
>   from file sources read through the declared upstream feed units of CLM-016.
>   No record-tier fact shall rest on prior store state, on a cached artifact, on
>   a stream or event input, or on any input the same sources cannot reproduce,
>   per `PEC-K-07` ("the reconciler over file truth is the source of every
>   record-tier fact") and the upstream regenerability obligation quoted in
>   CLM-012.
> - **REQ-005** — The reconciler shall write only into the store, through the
>   single declared ingest boundary quoted in CLM-013, and into the generated
>   views it declares under REQ-006. It shall create, modify, or delete no source
>   file, no governed file, no register, no lifecycle file, and no path outside
>   that declared write set, per `SOW-021` and `PEC-RCN-006` (CLM-002, CLM-004),
>   `PEC-RCN-004` ("it shall never modify a source file"), `PEC-GAT-004` ("PEC
>   shall provide no write path that records adoption, ruling, or direction"),
>   and `PEC-K-06` observation-not-participation.
> - **REQ-009** — Where an upstream unit reports that a feed is absent,
>   unreadable, malformed, stale, or grammar-unrecognized, the rebuild shall
>   carry that limitation through to its result, naming the loop and the feed,
>   and shall never present a rebuild that could not read a feed as a rebuild
>   that read it. Silent omission is prohibited, per `PEC-ORI-006` ("Where a feed
>   is unparseable or stale, the response shall state the measurement limitation
>   explicitly; silent omission is prohibited"). Rendering such a limitation into
>   an orientation response is `DEL-04-05`'s act under `SOW-009` (CLM-019); this
>   deliverable makes the limitation available to that consumer.
> - **REQ-010** — The rebuild shall be deterministic and idempotent over its
>   inputs: two rebuilds over the same unchanged sources shall produce the same
>   record tier, and a rebuild over a store already rebuilt from those sources
>   shall produce no difference. This is what makes a later difference between
>   two reconciles a structural fact rather than a judgment (`PEC-K-04`).
>
> (`DEL-03-01/ScopeOfWork.md`, Ontology and Epistemology sections; all six
> records quoted in full, none elided. ID-shaped text inside this quotation is
> upstream source context, not a local definition or reference — this contract's
> own records are separate and differently worded.)

  Four design constraints on this engine follow from those six records. The full-rebuild path exists as one command over every registered loop, so this contract implements no second rebuild (REQ-006). The upstream write set is the store through one declared ingest boundary plus the views that entry point declares, so this engine's own writes stay inside that same set and add nothing to it (REQ-007). The limitation carry-through is contractual upstream, so an incremental reconcile inherits the same honesty obligation rather than a weaker one (REQ-009). Determinism and idempotence upstream are what make a like-for-like comparison between an incremental result and a rebuilt result meaningful at all (REQ-005, REQ-010).

- **CLM-009** — The edge's `Statement` cell asserts that incremental reconcile "presupposes the full-rebuild path **and examined-SHA baseline**". The full-rebuild path is contractual upstream, quoted in CLM-008. The examined-SHA baseline is **not**: no record in the upstream contract obliges a rebuild to record the commit SHA it examined through, and that contract's boundary requirement excludes examined-SHA stamping only in its orientation-response form, leaving the reconcile-side baseline unaddressed rather than prohibited. The presupposition of the edge is therefore satisfied on one limb by an upstream obligation and on the other by nothing in the accepted corpus. This contract does not read the gap as a licence to assign the missing obligation upstream; it establishes and advances the baseline itself (REQ-004) and records the ownership question as CON-001.
- **CLM-010** — The record-tier entity model this engine writes into is not a declared edge of this deliverable, and the accepted graph says so deliberately rather than by omission. Register-wide constraint `C-03` `PACKAGE_LEVEL` states "Every PKG-03/04/05 deliverable depends on DEL-01-01 directly or transitively", and its exhibit `Notes` cell records "Deliverable-level entry edges (E-P10..13) are PROPOSAL; validator proves transitive closure 13/13", with the gate exhibit's own validation summary reading "C-03 transitive closure: 13/13 PKG-03/04/05 members reachable from DEL-01-01". This deliverable's path is `[E-P26]` to `DEL-03-01` and that deliverable's `[E-P10]` to `DEL-01-01`. Reached transitively on that declared path — and not as a local edge of this deliverable — the accepted upstream entity-model contract names this deliverable by ID as a performer:

> - **REQ-004** — The model shall represent examined-through SHA provenance
>   structurally, so that staleness is a comparison and never a judgment
>   (`PEC-K-04`, `OBJ-002`): OrientationSnapshot shall be stamped with the
>   examined SHA, and two successive snapshots shall be comparable field by field
>   such that a DriftFinding can record a classified difference. Performing that
>   comparison is `DEL-03-02`'s and `DEL-03-03`'s (CLM-012); the model shall not
>   require a human or agent judgment input for any field on which staleness
>   turns.
>
> (`DEL-01-01/ScopeOfWork.md`, Epistemology section; quoted in full, not elided.
> ID-shaped text inside this quotation is upstream source context, not a local
> definition or reference.)

  That record names two performers of one comparison and does not divide it between them. This contract takes only the limb its own scope item states — the SHA-keyed selection of what a reconcile must re-derive — and leaves the classification of a difference between successive snapshots to `DEL-03-03` under `SOW-019` (CLM-012, REQ-011). The stamped object that record names, OrientationSnapshot, is an orientation artifact whose stamping act is `DEL-04-03`'s under `SOW-006`; it is not the reconcile-side baseline this contract owns, which is why CON-001 survives this quotation rather than being answered by it.

- **CLM-011** — Two downstream consumer relations are recorded against this deliverable in `_DEPENDENCIES.md` and marked informational: `DEL-03-06` `[E-P31]` (`TESTS`) and `DEL-04-02` `[E-P33]` (`CONSUMES`). **Neither holds a row in this deliverable's `Dependencies.csv`**, which contains only the two anchors and the one upstream `EXECUTION` row; the downstream rows live in each consumer's own local register, per the deliverable-local storage ruling of `D-PEC-62`. Their exhibit rows read `E-P31,DEL-03-02,DEL-03-06,PROPOSAL,TESTS,,,Perf bounds test incremental reconcile` and `E-P33,DEL-03-02,DEL-04-02,PROPOSAL,CONSUMES,,,Deltas since SHA ride the incremental examined-SHA machinery`, both with `Flag` and `BasisCitation` empty. The performance relation is directional and runs *toward* this deliverable: `DEL-03-06` is the tester and this engine the tested surface, under `SOW-054`, measured from outside and neither run nor discharged here. The delta-service relation likewise imposes nothing on this contract: serving deltas since a **caller-supplied** commit SHA is `DEL-04-02`'s act under `SOW-005`, and being consumed by it neither transfers that scope here nor obliges this engine to expose a caller-parameterized query (REQ-011).

### Boundaries

- **CLM-012** — The acts adjacent to this engine are owned elsewhere and are cited here, never discharged. Within `PKG-03`: the one-command full rebuild and the reconciler write restriction are `DEL-03-01` (`SOW-010`, `SOW-021`); classifying and reporting drift between successive snapshots is `DEL-03-03` (`SOW-019`); parity-diffing PEC derivations against practitioner-harness output is `DEL-03-04` (`SOW-020`); the stream-loss recovery guarantee is `DEL-03-05` (`SOW-038`, `P3`); the rebuild and incremental performance bounds are `DEL-03-06` (`SOW-054`, CLM-004). Outside it: the record-tier schema and entity model are `DEL-01-01` (`SOW-001`); the gitignored store, its safe-delete lifecycle, and its ingest-boundary content-minimal guard are `DEL-01-03` (`SOW-056`); self-observability logging is `DEL-01-04` (`SOW-057`); standing zero-dependency and locality enforcement is `DEL-01-05` (`SOW-052`, `SOW-053`); the loop-registration configuration is `DEL-01-06` (`SOW-094`); the presence-tier entity model is `DEL-01-02` (`SOW-002`, `P3`); the seven feed grammars and the feed manifest are `DEL-02-01` through `DEL-02-07` (`SOW-011`..`SOW-017`); the per-loop orientation return is `DEL-04-01` (`SOW-004`); serving deltas since a caller-supplied commit SHA is `DEL-04-02` (`SOW-005`); stamping every orientation response with examined-through SHA, generation time, and per-feed freshness, and attaching a per-claim citation, is `DEL-04-03` (`SOW-006`, `SOW-007`) — checked against the ledger, both of those scope items resolve to `DEL-04-03` and neither to `DEL-04-02`; rendering a measurement limitation into an orientation response is `DEL-04-05` (`SOW-009`); read-only scanning of Git for worktrees, branches, HEAD, ahead/behind counts, and dirty path names/counts is `DEL-06-02` (`SOW-027`, `P3`, presence tier); event ingest is `DEL-07-01` (`SOW-033`, `SOW-039`, `P3`); the standing kill test is `DEL-10-02` (`SOW-055`); the directed bootstrap self-ingest validation is `DEL-10-10` (`SOW-064`). This contract produces only the incremental engine and its tests.
- **CLM-013** — PEC's Git posture is a permanent product boundary, and this deliverable is the only `P1` record-tier act that reads Git at all. `PRD.md` §4.2 states it as a non-goal in full: "**Not a Git actor.** Read-only plumbing access; CHANGE owns Git state." `PEC-K-06` states the same standing: "**Observation, not participation.** Read-only over Git; no leases, no claim arbitration, no merge opinions, no dispatch; conflicts surfaced, never prevented." `PEC-K-10` bounds what a Git read may yield: "**Content-minimal.** Paths, counts, SHAs, states, hashes — never file or diff content." A delta is the one input in the corpus whose most natural representation is a diff, so the content-minimal rule bites here more directly than anywhere else in `P1`; `PEC-PRS-002` states the same restriction for the presence-tier scan, reading in full: "PEC shall scan Git for worktrees, branches, HEAD, ahead/behind counts, and dirty path names/counts; file and diff content shall never be captured (PEC-K-10)." That scan is `DEL-06-02`'s at `P3`, not this deliverable's (REQ-002, REQ-003).
- **CLM-014** — Phase staging, checked against the `PhaseHint` column of `Deliverables.csv` for every deliverable this contract names in its own voice: `DEL-03-02` itself, its predecessor `DEL-03-01`, its consumers `DEL-03-06` and `DEL-04-02`, and `DEL-01-01`, `DEL-01-03`, `DEL-01-04`, `DEL-01-05`, `DEL-01-06`, `DEL-02-01`, `DEL-02-02`, `DEL-02-03`, `DEL-02-04`, `DEL-02-05`, `DEL-02-06`, `DEL-02-07`, `DEL-03-03`, `DEL-03-04`, `DEL-04-01`, `DEL-04-03`, `DEL-04-05`, `DEL-10-02`, and `DEL-10-10` are all `P1`. **Four** exceptions are named in this contract's own voice, each cited only as the owner of scope this deliverable does not touch: `DEL-01-02` (presence-tier model), `DEL-03-05` (stream-loss recovery), `DEL-06-02` (Git/worktree presence scanner), and `DEL-07-01` (event ingest) are all `P3`. The `P1` input boundary of this engine is therefore file truth reached through the same feed path the full rebuild uses, plus a read-only Git delta over those files, and nothing later: no stream or event input and no presence-tier input is a source of this reconcile, and no claim in this contract stages any named deliverable into a different phase.
- **CLM-015** — The deliverable is at lifecycle state `OPEN` with no implementation present. Every requirement, acceptance criterion, and verification method below states a contract on future production; none asserts that anything has been built.

- **TBD-001** — `ResponsibleParty` is unassigned; the register records `TBD`, with assignment at WORKING_ITEMS activation and not in this contract (`SOFTWARE_DECOMP.md` §5 preamble; `_CONTEXT.md`).
- **TBD-002** — The engine's concrete invocation surface — whether the incremental reconcile is a mode of the upstream entry point or a separate verb, its arguments, and its exit-status contract — is fixed by no accepted source beyond the register phrase "Incremental engine" and `PEC-RCN-003`'s "run incrementally". It is chosen during production within REQ-001 and REQ-006.
- **TBD-003** — The mapping from a changed path in the delta to the record-tier facts that must be re-derived, and the granularity at which the engine re-derives them, are fixed by no accepted source. `PEC-RCN-003` keys the reconcile on the delta and says nothing about how a changed file resolves to affected entities. It is chosen during production within REQ-001 and bounded by the equivalence obligation of REQ-005.
- **TBD-004** — Where the baseline record durably lives is fixed by no accepted source. This is the informational side of CON-001: REQ-004 obliges the engine to keep and advance a baseline and to write it only through the upstream-declared write set, and settles nothing about which store object holds it.
- **TBD-005** — Which repository checkouts a registered loop's delta spans, and how the engine resolves a loop to them, are fixed by no accepted source; the upstream contract records the same loop-to-project resolution gap in its own terms. This contract obtains the loop set through the upstream path (REQ-006) and settles nothing about the resolution between a loop and the checkouts whose commit history it reads.

## Completion and Reliance Basis — Epistemology

The requirements below state what future production must satisfy. Nothing in
this section asserts that a reconciler, a store, a parser, a registry, or a
test exists.

- **REQ-001** — The engine shall reconcile incrementally, keyed on the Git delta between the commit state it observes at the start of a run and the commit SHA recorded as last examined, per `SOW-018` (CLM-001) and `PEC-RCN-003` (CLM-002). The delta shall select the work: sources the delta does not name shall not be re-derived, and sources it does name shall be.
- **REQ-002** — The engine shall obtain the delta through read-only Git access and shall perform no Git state change of any kind — no commit, branch, ref, index, stash, checkout, worktree, or configuration write — per `PEC-K-06` and the permanent non-goal "Not a Git actor. Read-only plumbing access; CHANGE owns Git state" (CLM-013).
- **REQ-003** — Nothing the engine captures from Git, retains in memory beyond the run, presents to the store, or writes into a declared view shall carry file content or diff content; the delta shall be reduced to paths, counts, SHAs, states, and hashes at the point it is read, per `PEC-K-10` (CLM-013). This restriction binds the engine's own surface and is additional to, not a substitute for, the store-side ingest guard owned elsewhere (CLM-012).
- **REQ-004** — The engine shall record, as the baseline component of OUT-001 and through the write set of REQ-007, the commit SHA each completed reconcile examined through, and shall advance that baseline only for a reconcile that completed over the sources the delta named. Where no baseline is recorded, the engine shall not synthesize one and shall not infer one from store contents: it shall defer to the full-rebuild path (REQ-006) and establish the baseline from the commit state it observed for that run. Nothing in this requirement asserts that any other deliverable records or maintains a baseline (CLM-009, CON-001).
- **REQ-005** — An incremental reconcile over a delta shall produce the record tier that a full rebuild over the same end commit state would produce. Where the engine cannot establish that equivalence for a class of change — including a change it cannot resolve to affected record-tier facts (TBD-003) — it shall fall back to the full-rebuild path rather than emit a partial result as a reconciled one, per `PEC-K-07` ("Ingest is best-effort; reconciliation is guaranteed") and the upstream determinism obligation quoted in CLM-008.
- **REQ-006** — The engine shall implement no full rebuild of its own. It shall reach the full-rebuild path only through the upstream entry point quoted in CLM-008, shall define no second rebuild command, and shall obtain the set of loops it reconciles by the same upstream path rather than by its own registry read. `PKG-03`'s package exclusions record "parsers (PKG-02)" as outside this package, and this deliverable declares no `PKG-02` edge (CLM-007): it shall therefore declare no feed grammar, parse no feed file directly, and consume parsed feed content only through the path the full rebuild already uses.
- **REQ-007** — The engine shall write only into the store, through the single declared ingest boundary the upstream contract binds, and into the generated views that contract's entry point declares. It shall create, modify, or delete no source file, no governed file, no register, no lifecycle file, and no path outside that write set, and shall declare no generated view of its own. This contract does not cover `SOW-021` — that scope item is the upstream deliverable's (CLM-012) — but `PEC-RCN-004` ("The reconciler shall classify drift between successive snapshots and report it; it shall never modify a source file"), `PEC-RCN-006` ("The reconciler writes only its own store and generated views"), and `PEC-GAT-004` ("PEC shall provide no write path that records adoption, ruling, or direction (PEC-K-02; K-AUTH-1).") constrain any reconciler act, and this engine is a reconciler act.
- **REQ-008** — Where a feed the delta selects is reported absent, unreadable, malformed, stale, or grammar-unrecognized, the engine shall carry that limitation through to its result, naming the loop and the feed, and shall never present a reconcile that could not read a selected source as one that read it, per `PEC-ORI-006` and the upstream carry-through obligation quoted in CLM-008. It shall not advance the baseline past a source the delta named and the run did not successfully examine.
- **REQ-009** — The engine shall be deterministic and idempotent over its inputs: two incremental reconciles over the same baseline and the same end commit state shall produce the same record tier, and a reconcile run when the delta is empty shall change no record-tier fact and shall leave the baseline at the same SHA. This is what keeps the SHA comparison structural rather than a judgment (`PEC-K-04`, `OBJ-002`, CLM-003).
- **REQ-010** — The engine shall derive every record-tier fact it writes from file sources reached through the upstream path of REQ-006. No record-tier fact it writes shall rest on a stream or event input, on presence-tier data, or on any input the same sources cannot reproduce, per `PEC-K-07`; and no presence-tier fact shall be reconstructed, populated, or asserted, per `PEC-K-05` (CLM-014).
- **REQ-011** — The engine shall perform no act owned by another deliverable. In particular it shall classify no drift between successive snapshots, run no parity diff against practitioner-harness output, perform no stream-loss recovery act, make or assert no rebuild or incremental performance measurement or bound, stamp no orientation response with examined-through SHA, generation time, or per-feed freshness and attach no per-claim citation, serve no caller-supplied-SHA delta query, perform no presence-tier or worktree scan, and run no kill test; each is cited to its owner in CLM-004, CLM-011, and CLM-012, and none is discharged here.
- **REQ-012** — Every record-tier fact the engine writes shall be an instance of an entity type the upstream entity-model contract obliges (CLM-010). This deliverable shall define no record-tier entity type, shall add no type to that model, shall define no presence-tier type, and shall not depend on any upstream artifact existing; it depends on the upstream contracts only (CON-002).
- **REQ-013** — The engine and its tests shall introduce no third-party runtime dependency and no external network egress, per `PEC-SVC-001` and `PEC-SVC-002`, whose standing enforcement is `DEL-01-05` covering `SOW-052` and `SOW-053` (CLM-012).
- **REQ-014** — Tests shall implement the verification methods declared in this contract; they shall not define scope, requirements, or acceptance criteria.

- **AC-001** — For a fixture corpus with a known commit history, a reconcile run from a recorded baseline re-derives exactly the record-tier facts the changed paths account for and re-derives nothing attributable only to unchanged paths; and for a delta that names a source, that source is re-derived.
- **AC-002** — A reconcile run against a fixture repository leaves the repository's Git state byte-identical — same HEAD, refs, index, stash, worktree list, and configuration — and this deliverable's source contains no Git write operation of any kind.
- **AC-003** — For a content-dense fixture corpus whose delta spans long prose bodies, quoted authored text, and diff-shaped content, inspection of everything the engine retains, presents to the store, and writes into a declared view finds no file content and no diff content — only paths, counts, identifiers, states, SHAs, and hashes.
- **AC-004** — After a completed reconcile the baseline record names the commit SHA that run examined through; after a run that did not complete over its selected sources the baseline is unchanged; and with no baseline recorded the engine takes the full-rebuild path and then records a baseline, with no baseline value derived from store contents anywhere in this deliverable's source.
- **AC-005** — For each fixture change class exercised, the record tier produced by an incremental reconcile is identical to the record tier produced by a full rebuild over the same end commit state; and for a seeded change class the engine cannot resolve, the run takes the full-rebuild path and no partial result is presented as reconciled.
- **AC-006** — This deliverable's source contains no rebuild implementation, no second rebuild command, no registry read of its own, no feed grammar definition, and no direct feed-file parse; the full-rebuild path and the loop set are reached only through the upstream entry point.
- **AC-007** — A reconcile over a fixture corpus leaves that corpus byte-identical and touches no path outside the store and the views the upstream entry point declares; every store write in this deliverable's source reaches the store through the upstream ingest boundary; the module contains no write, create, or delete call against any source file, governed file, register, or lifecycle file; and it declares no generated view of its own.
- **AC-008** — For fixture corpora in which a selected feed is absent, unreadable, malformed, stale, and grammar-unrecognized in turn, the reconcile result carries the reported limitation naming the loop and the feed, no such result presents that feed as read, and the baseline is not advanced past the unexamined source.
- **AC-009** — Two reconciles from the same baseline over the same end commit state produce identical record tiers; a reconcile over an empty delta changes no record-tier fact and leaves the baseline SHA unchanged.
- **AC-010** — Every record-tier fact an incremental reconcile writes traces to a file source reached through the upstream path; inspection finds no stream, event, presence-tier, or otherwise non-source input contributing to any record-tier fact; and a reconcile over a fixture corpus carrying presence-shaped input produces no presence-tier record.
- **AC-011** — The module contains no drift-classification path, no parity-diff path, no stream-loss recovery path, no performance measurement or bound assertion, no stamping or citation-attachment path, no caller-supplied-SHA delta query surface, no presence or worktree scan, and no kill-test execution; and no test in this deliverable asserts a criterion belonging to any of them.
- **AC-012** — Every record-tier fact written is an instance of an entity type the upstream contract obliges; no record-tier or presence-tier type is defined in this deliverable's source; and no element of this deliverable asserts or requires that an upstream schema, store, parser, registry, or reconciler artifact exists.
- **AC-013** — The engine and its tests add no third-party runtime dependency and make no network call, leaving the standing zero-dependency and locality assertion intact.
- **AC-014** — The test suite implements VER-001 through VER-013, executes in the `PKG-03` test run, passes, and introduces no acceptance criterion absent from this contract.
- **AC-015** — The REVIEW gate confirms this contract's traceability to `SOW-018` and `OBJ-002`; confirms that the mapping is stated as register-direct and pre-SCA-002, at the strength the record carries and no more; and confirms that no `PKG-01`, `PKG-02`, sibling `PKG-03`, `PKG-04`, `PKG-06`, `PKG-07`, or `PKG-10` scope has been absorbed.

- **CON-001** — The edge that places this deliverable presupposes an examined-SHA baseline that no accepted source obliges anyone to produce. The upstream full-rebuild contract states no obligation to record the commit SHA a rebuild examined through; its boundary requirement excludes examined-SHA stamping only in the orientation-response form owned by `DEL-04-03` under `SOW-006`, so the reconcile-side baseline is unaddressed there rather than prohibited or assigned. The transitively reached entity-model contract stamps OrientationSnapshot with the examined SHA and obliges the model to represent examined-through SHA provenance structurally (CLM-010), but OrientationSnapshot is an orientation artifact whose stamping act is owned elsewhere. That contract obliges specific properties of the model — citation provenance on every type, structural examined-through-SHA provenance with OrientationSnapshot stamped, and explicit per-loop Receipt availability — while enumerating no complete field set for the fourteen record-tier types and naming no holder for a *reconcile's* examined-through SHA, so where that value would live is unsettled at the level of accepted truth.

  This contract records the gap rather than closing it in either direction. It does not assign the missing obligation upstream: no requirement here imposes anything on the full-rebuild deliverable, and REQ-004 is written so that a first run with no recorded baseline falls back to the full rebuild and establishes the baseline from the commit state this engine observed. It also does not fix the holder: REQ-004 obliges the baseline to be written only through the upstream-declared write set and says nothing about which store object carries it (TBD-004). A production choice that fixed an upstream field set, or that read a baseline out of another deliverable's artifact, would take a decision in the wrong place. Whether the baseline should instead be a shared reconcile-side obligation stated once for the whole package is a scope-change question, not a production decision.

- **CON-002** — The record-tier entity types this engine writes into are owned upstream and do not yet exist, and this deliverable holds no direct edge to them — its dependence is transitive by `C-03` and validated as such (CLM-010). Its write surface therefore binds to an obligation reached across two edges rather than to an artifact, and no accepted source enumerates those types' complete field sets. This contract asserts no field, no schema shape, and no isolation style, and nothing here may be read as settling one.
- **CON-003** — Upstream-carried, not resolved here: the full-rebuild contract records that no accepted source states whether a rebuild that completed with stated coverage limitations counts as a rebuild "in full" for `SOW-010`'s purposes. That question has an incremental twin — whether a reconcile that could not read a source the delta named has reconciled through the end commit state — and this contract answers only the baseline limb of its own case, by prohibiting the baseline from advancing past an unexamined source (REQ-008). The upstream question remains open in its own contract and is neither resolved nor narrowed by that local obligation.
- **CON-004** — Upstream-carried, not resolved here: the full-rebuild contract carries an instance-level gap about which generated views its entry point writes and where they live. The upstream record states it in full:

> - **TBD-003** — Which views this reconciler generates, and where they live, are
>   fixed by no accepted source. What a "generated view" *is* as a class is not
>   open: `D-GOV-01` Option A rules the category and its properties, and
>   `tools/REGISTRY.md` glosses the shipped harness outputs in the same terms
>   (CON-001). What remains undetermined is the instance set, chosen during
>   production within REQ-006. This is the informational side of CON-001.
>
> (`DEL-03-01/ScopeOfWork.md`, Ontology section; quoted in full, not elided.
> ID-shaped text inside this quotation is upstream source context, not a local
> definition or reference.)

  Its conflict record opens on the same distinction — "`SOW-021`'s second limb permits writes to \"generated views\", and the gap this contract carries is **instance-level, not class-level**." (`DEL-03-01/ScopeOfWork.md`, Epistemology section, first sentence of that record; ID-shaped text in this quotation is upstream source context, not a local definition or reference). This contract touches that gap only because REQ-007 confines its own writes to the view set the upstream entry point declares. It names no view, adds none, and settles nothing about the instance set; whichever set production settles on upstream is the set this engine is bounded by.

## Production and Verification Method — Praxeology

Production proceeds in the order upstream-interface survey → read-only delta
acquisition and content reduction → delta-to-work resolution and the reconcile
path → baseline record and fallback → equivalence against the full rebuild →
limitation carry-through and determinism → tests. The upstream-interface survey
comes first because the single predecessor at `INITIALIZED` supplies
obligations rather than artifacts, and a reconcile path written against an
imagined artifact would violate CON-002 before any code existed. Delta
acquisition precedes the reconcile path because the content-minimal reduction
has to be a property of how the delta is read, not a filter applied afterwards
(CLM-013). Equivalence comes after the reconcile path because it is that path's
acceptance surface and because the fallback of REQ-005 cannot be specified
until there is a resolution step that can fail to resolve. All work is bounded
to this deliverable folder and the `PKG-03` service-core source it names; this
contract authorizes no register, decomposition, PRD, or upstream-deliverable
edit, and it neither defines nor reshapes the entity model it writes into, the
store it writes through, the rebuild it falls back to, or the grammars it
consumes. Tests implement the verification methods below and create no scope.

- **VER-001** — Delta-selection exercise: build a fixture corpus with a known commit history, record a baseline, apply a seeded set of changes, run the reconcile, and assert fact by fact that every record-tier fact attributable to a changed path was re-derived and that no fact attributable only to unchanged paths was; repeat across change classes (added, modified, deleted, renamed source).
- **VER-002** — Git read-only exercise: capture HEAD, all refs, the index, the stash list, the worktree list, and the configuration of a fixture repository before and after a reconcile and assert equality on each; inspect this deliverable's source and call graph for Git write operations and assert none is present.
- **VER-003** — Content-minimal inspection: run the reconcile over a content-dense fixture corpus carrying long prose bodies, quoted authored text, and diff-shaped changes, then dump the engine's retained delta representation, every field presented to the store, and every declared view written, and assert field by field that none carries file or diff content.
- **VER-004** — Baseline exercise: assert after a completed reconcile that the recorded baseline equals the examined commit SHA; interrupt or fail a run over its selected sources and assert the baseline is unchanged; start with no baseline recorded and assert the full-rebuild path is taken and a baseline then recorded; and inspect this deliverable's source for any derivation of a baseline value from store contents, asserting none.
- **VER-005** — Equivalence exercise: for each fixture change class, run an incremental reconcile from a baseline and a full rebuild over the same end commit state and assert the resulting record tiers are identical; seed a change class the resolution step cannot resolve and assert the run takes the full-rebuild path and presents no partial result as reconciled.
- **VER-006** — Boundary inspection of the upstream path: inspect this deliverable's source for a rebuild implementation, a second rebuild command, a registry read, a feed grammar definition, and a direct feed-file open, asserting each absent; instrument the call surface and assert the full-rebuild path and the loop set are reached only through the upstream entry point.
- **VER-007** — Write-boundary exercise: hash the fixture source corpus tree before and after a reconcile and assert byte-identity; capture every filesystem write performed during the run and assert each resolves under the store or a view the upstream entry point declares; inspect the call graph and assert every store write reaches the store through the upstream ingest boundary, that no write, create, or delete call targets a source file, governed file, register, or lifecycle file, and that the module declares no view of its own.
- **VER-008** — Limitation carry-through: run the reconcile over fixture corpora in which a selected feed is absent, unreadable, malformed, stale, and grammar-unrecognized in turn, and assert per case that the result carries the reported limitation naming the loop and the feed, that no result presents that feed as read, and that the baseline was not advanced past the unexamined source.
- **VER-009** — Determinism and idempotence: run the reconcile twice from the same baseline over the same end commit state and assert identical record tiers; run it once with an empty delta and assert no record-tier change and an unchanged baseline SHA.
- **VER-010** — Provenance and tier inspection: for a sample record-tier fact of each entity type an incremental reconcile produces, trace it to the file source and the upstream path that yielded it; inspect the engine's input surface for stream, event, and presence-tier inputs and assert none contributes; run the reconcile over a fixture corpus carrying presence-shaped input and assert no presence-tier record is written.
- **VER-011** — Adjacent-act inspection: inspect the module's call graph and source for drift-classification, parity-diff, stream-loss recovery, performance-measurement, stamping, citation-attachment, caller-supplied-SHA delta-query, presence or worktree scan, and kill-test paths, asserting each absent; review this deliverable's tests for any criterion belonging to another deliverable, asserting none.
- **VER-012** — Type-boundary inspection: assert every record-tier fact written is constructed against an entity type the upstream contract obliges; inspect this deliverable's source for record-tier and presence-tier type definitions and assert none; inspect source and fixtures for any assumption that an upstream schema, store, parser, registry, or reconciler artifact exists, asserting none.
- **VER-013** — Inspect the `PKG-03` dependency manifest and this module's import graph for third-party runtime dependencies and network calls, and re-run the zero-dependency and locality enforcement once the deliverable that owns it is available, without discharging it here.
- **VER-014** — Run the `PKG-03` test suite and confirm that each of VER-001 through VER-013 has a corresponding executing automated test and that no test asserts a criterion absent from this contract.

## Governing Values and Decisions — Axiology

- **AX-001** — `OBJ-002` governs: staleness is detected structurally by SHA comparison, never by judgment. This deliverable is where that claim becomes an act rather than a property of a response. Stamping a response with a SHA (owned elsewhere) makes staleness *visible*; keying the reconcile on the delta since the last examined SHA makes staleness *consequential* — the system does work because a comparison said so, and for no other reason. A reconcile that re-derived on a schedule, a heuristic, or an operator's sense that something had changed would leave `OBJ-002` true of the display and false of the machine.
- **AX-002** — `PEC-K-04` is the objective's product invariant and it cuts inward. Every response carries the examined-through commit SHA; this engine is what makes that SHA mean something on the production side, because the SHA a response reports is only honest if a reconcile actually examined through it. REQ-004's prohibition on advancing the baseline past an unexamined source is that honesty stated as a checkable obligation.
- **AX-003** — `PEC-K-07` is why REQ-005's fallback is not a weakness. Ingest is best-effort and reconciliation is guaranteed; an incremental reconcile is an *optimization of* the guaranteed path, not a second, cheaper path with its own weaker guarantee. The moment the incremental result could differ from the rebuilt result, the guarantee would have been traded for speed, and every downstream citation would inherit the trade. Falling back to the full rebuild is what keeps the optimization inside the guarantee.
- **AX-004** — `PEC-K-06` observation-not-participation and the permanent "Not a Git actor" non-goal govern the delta read. This deliverable is the first and, at `P1`, the only record-tier act that touches Git, so it is where a read-only posture would first quietly become a read-write one. REQ-002 states it as a boundary that a fixture repository's before/after state can falsify, rather than as a discipline.
- **AX-005** — `PEC-K-10` content-minimal is a residency posture, and a delta is the corpus's sharpest test of it. Every other feed in `P1` is a file whose parse is content-shaped by design and guarded upstream; a delta is natively a diff, and a diff is precisely the thing PEC may never hold. REQ-003 therefore binds the reduction at the point of the Git read rather than relying on a boundary that sits further downstream and, for the view surface, does not sit there at all.
- **AX-006** — `PEC-ORI-006` honesty governs the failure mode, and its incremental form is stricter than its rebuild form. A rebuild that could not read a feed is wrong about one feed; an incremental reconcile that could not read a feed and advanced its baseline anyway is wrong about that feed *for every subsequent run*, because the delta will never name it again. That asymmetry is why REQ-008 carries a baseline clause the upstream carry-through obligation does not have, and it is the strongest reason this contract keeps CON-003 open rather than assuming the upstream reading settles it.
- **AX-007** — Edge direction is a constraint on this contract, not a licence. `RequiredMaturity` `INITIALIZED` on the single upstream edge means the upstream *contract* is the reliable input, not any upstream artifact; this contract is written against the obligations quoted in CLM-008 and CLM-010 and asserts nothing about upstream implementation state. Consuming one contract imposes no obligation on it — CON-001 records a gap in the upstream record and assigns no work there — and being tested by one deliverable and consumed by another neither expands this contract's scope nor transfers any of theirs into it.
- **AX-008** — This deliverable sits between two neighbours whose scope is easy to absorb by mistake, and the record settles both. `DEL-03-03` classifies drift between successive snapshots; this engine decides what to re-derive. `DEL-03-06` measures the seconds-scale incremental bound; this engine asserts none — SCA-002 recorded the argument that the incremental clause of `SOW-054` points at `OBJ-002` and still ruled that row to `OBJ-005` for `DEL-03-06` (CLM-004), so taking the bound here would reverse a ruling, not fill a gap.
- **AX-009** — The one upstream edge and the two downstream relations cited in this contract are `PROPOSAL` stratum and are *accepted* at that stratum: `D-PEC-62` §1(4) records the owner accepting the DAG candidate v0.2 exhibit "accepted, all strata as presented", and that packet reads "as presented" as accepting the exhibit's **flags as flags**, so what remains recorded-but-unresolved is the specific annotated set — `E-A11` (AMBIGUOUS_BASIS), `E-P69`/`E-N02` (PHASE_TENSION), `E-N13`/`E-N18` (LOW_CONFIDENCE), the `C-02` direction, and the `C-08` standing-node set — none of which touches `[E-P26]`, `[E-P31]`, or `[E-P33]`, each of which carries an empty `Flag` column in the exhibit. Stratum is provenance, not authority: it records how an edge was derived, not whether it has been accepted, and citation does not convert `PROPOSAL` to `DECLARED`. That `[E-P26]` additionally carries an empty `BasisCitation` (CLM-007) is a fact about the exhibit's evidence trail, not a defect in its acceptance.
- **AX-010** — Unknowns stay marked. TBD-001 through TBD-005 and CON-001 through CON-004 are recorded rather than resolved by inference, and two of the four conflicts are explicitly upstream-carried. `C-03` `PACKAGE_LEVEL`, `C-04` `PHASE_PRECEDENCE`, and `C-10` `STRATUM_RULE` are register-wide non-gating constraints recorded in `_DEPENDENCIES.md`, and blocker output under the `FULL_GRAPH` mode at threshold `INITIALIZED` is advisory visibility only, never work assignment.
- **AX-011** — The objective mapping is stated at record strength and no higher. `SOW-018` → `OBJ-002` is register-direct and pre-SCA-002, and SCA-002 measured it **Valid** as a precedent it then used to anchor other rows; this contract therefore supplies no fresh derivation and creates no owner-confirmation criterion for it. AC-015 asks REVIEW to check the traceability, not to ratify a mapping the register already carries.
- **AX-012** — This contract is lifecycle-neutral. `_STATUS.md` remains the sole lifecycle authority and is untouched by the run that authored this document; the deliverable is at `OPEN` and nothing has been built.

**Quotation record.** Every quotation in this contract is verbatim from the
named source, and **no quotation in this document is elided** — none omits text
from the span it presents, and no ellipsis appears anywhere in this document.
Quoted spans that are shorter than their containing record are presented as
whole sentences, whole table rows, whole register rows, whole cells, or short
verbatim phrases, and are attributed as such at the point of quotation: the
`A001` target cell, the
`A003b` `OBJ-002` old/new block, the register-precedent table row, the Q2
evidence sentence, the `SOW-018` ledger row and its SSOW row, the six
`DEL-03-01` records of CLM-008, the `DEL-01-01` record of CLM-010, the
`DEL-03-01` informational record quoted in CON-004, and that contract's
conflict-record opening sentence, also in CON-004 and identified there as the
first sentence of a longer record. The `PEC-K-*`, `PEC-RCN-*`, `PEC-GAT-004`,
`PEC-PRS-002`, `OBJ-002`, and `PRD.md` §4.2 quotations are each complete rows
or complete sentences of their sources; the `SOW-054` and `SOW-018` statements
and the `C-03` `Statement` and `Notes` texts are complete register cells; and
the `D-PEC-62` acceptance phrases quoted in AX-009 are short verbatim phrases,
identified there as such.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-018 OBJ-002 | REQ-001, CLM-001, CLM-002, CLM-005, TBD-002, TBD-003 | AC-001 | VER-001 | Seeded-change-history fixture runs with a fact-by-fact record of what was and was not re-derived, across added, modified, deleted, and renamed sources |
| OUT-001 | SOW-018 OBJ-002 | REQ-002, CLM-013, AX-004 | AC-002 | VER-002 | Before/after captures of HEAD, refs, index, stash, worktree list, and configuration for a fixture repository, plus a recorded search of this deliverable's source and call graph for Git write operations |
| OUT-001 | SOW-018 OBJ-002 | REQ-003, CLM-013, AX-005 | AC-003 | VER-003 | Dumps of the retained delta representation, every field presented to the store, and every declared view written for a content-dense fixture corpus, showing no file or diff content |
| OUT-001 | SOW-018 OBJ-002 | REQ-004, CLM-009, TBD-004, CON-001, AX-002 | AC-004 | VER-004 | The baseline record after a completed run, after an interrupted run, and from a no-baseline start, plus a recorded search of this deliverable's source for any baseline value derived from store contents |
| OUT-001 | SOW-018 OBJ-002 | REQ-005, CLM-008, AX-003 | AC-005 | VER-005 | Per-change-class comparisons of the incremental record tier against the full-rebuild record tier over the same end commit state, plus the unresolvable-change fallback transcript |
| OUT-001 | SOW-018 OBJ-002 | REQ-006, CLM-006, CLM-007, TBD-005 | AC-006 | VER-006 | Recorded searches for a rebuild implementation, a second rebuild command, a registry read, a feed grammar definition, and a direct feed-file open, plus the instrumented call surface showing the upstream-only path |
| OUT-001 | SOW-018 OBJ-002 | REQ-007, CON-004, AX-007 | AC-007 | VER-007 | Before/after fixture-corpus tree hashes; the captured filesystem-write inventory with each write resolved to the store or an upstream-declared view; the call-graph inspection record showing every store write through the upstream ingest boundary and no view declared here |
| OUT-001 | SOW-018 OBJ-002 | REQ-008, CON-003, AX-006 | AC-008 | VER-008 | Per-case reconcile results for absent, unreadable, malformed, stale, and grammar-unrecognized selected feeds, each naming the loop and the feed and each showing the baseline held back |
| OUT-001 | SOW-018 OBJ-002 | REQ-009, CLM-003, AX-001 | AC-009 | VER-009 | The two-run record-tier comparison from an identical baseline and end state, plus the empty-delta run showing no record-tier change and an unchanged baseline SHA |
| OUT-001 | SOW-018 OBJ-002 | REQ-010, CLM-014 | AC-010 | VER-010 | Per-entity-type provenance traces from record-tier fact to file source and upstream path, the input-surface inspection record, and the presence-shaped fixture run showing no presence-tier record written |
| OUT-001 | SOW-018 OBJ-002 | REQ-011, CLM-004, CLM-011, CLM-012, AX-008 | AC-011 | VER-011 | Call-graph and source inspection records showing each named adjacent path absent, plus a review of this deliverable's tests confirming no criterion belonging to another deliverable |
| OUT-001 | SOW-018 OBJ-002 | REQ-012, CLM-010, CON-002 | AC-012 | VER-012 | The entity construction surface against the quoted upstream obligation, plus recorded searches of this deliverable's source for record-tier and presence-tier type definitions and for upstream-artifact assumptions |
| OUT-001 | SOW-018 OBJ-002 | REQ-013 | AC-013 | VER-013 | Dependency-manifest and import-graph inspection records, plus the zero-dependency and locality enforcement result once the deliverable that owns it is available |
| OUT-002 | SOW-018 OBJ-002 | REQ-014, CLM-015 | AC-014 | VER-014 | PKG-03 test-run output mapping each executed test to its declared verification method, with no criterion asserted that this contract does not state |
| OUT-001 | SOW-018 OBJ-002 | AX-009, AX-010, AX-011, AX-012 | AC-015 | HUMAN_REVIEW: REVIEW gate confirms traceability to SOW-018 and OBJ-002, confirms the mapping is stated as register-direct and pre-SCA-002 at the strength the record carries, and confirms no upstream, sibling, or cross-package scope absorption | Review record citing the SOW-018 ledger row, the A001 target cell and the A003b OBJ-002 block, the measured register precedent, and the upstream, sibling, and cross-package deliverable boundaries |
