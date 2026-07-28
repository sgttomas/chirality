---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-04-01
package_id: PKG-04
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@11a494e9a
project_scope_refs: [SOW-004]
package_objective_refs: [OBJ-001]
---

# Scope of Work — DEL-04-01 Loop orientation return

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-04-01` — "Loop
orientation return" — in `PKG-04` Orientation Services of the PEC v2 build. It
covers project scope item `SOW-004` in service of package objective `OBJ-001`.

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.3** (`current_basis`, SCA-003 successor; accepted 2026-07-28 at
merge `11a494e9a`). The deliverable-local `_REFERENCES.md` now cites that
current basis under the reference-parity integration at `af62343d3`.
`_CONTEXT.md` retains the revision-1.1 to revision-1.2 supersession trace;
SCA-003 in turn establishes revision 1.3 as the current successor. This
contract cites revision 1.3.

**Objective warrant (register-direct, pre-SCA-002).** `CoversScopeItems` is one
row and its `OBJ-001` provenance is the register's own, unchanged by the
scope-change amendment. Three independent checks in the SCA-002 record agree.
First, the `SOW-004` ledger row is not one of the twenty rows whose empty
`ObjectiveIDs` cell `A001` populated; that action's target is stated as

> `ScopeLedger.csv` `ObjectiveIDs` — **20 IN rows** (`SOW-001, 003, 011..017,
> 021, 025, 040, 042, 052, 053, 054, 056, 088, 089, 094`)
>
> (`Brief.md`, action-register row `A001`, target cell; the `..` ranges are the
> source's own notation, not an elision. ID-shaped text inside this quotation is
> upstream source context, not a local definition or reference.)

and `SOW-004` is not among them. Second, `DEL-04-01` is not one of the
seventeen deliverable rows whose `SupportsObjectives` cell `A002` derived "by
the union invariant, not authored independently". Third, the §3 objective row
confirms the same from the objective side: the recorded old and new text of the
`OBJ-001` row's mapped cells reads

> ```
> OLD col4: SOW-004..009, SOW-041, SOW-043; instruments: SOW-058, SOW-059
> NEW col4: SOW-001, SOW-003, SOW-004..009, SOW-011..017, SOW-040..043, SOW-089; instruments: SOW-058, SOW-059
> OLD col5: DEL-04-01..05, DEL-08-03, DEL-08-04, DEL-10-01, DEL-10-04
> NEW col5: DEL-00-03, DEL-01-01, DEL-02-01..07, DEL-04-01..05, DEL-08-01..04, DEL-10-01, DEL-10-04
> ```
>
> (`Amendment_Preview.md`, action `A003b`, "Line 320 · `OBJ-001`"; all four lines
> quoted in full, none elided. The `..` ranges are the source's own notation.
> ID-shaped text inside this quotation is upstream source context, not a local
> definition or reference.)

`SOW-004` stands inside `OBJ-001`'s mapped scope items and `DEL-04-01` inside
its mapped deliverables on both sides of the amendment. The mapping is
therefore register-direct at both levels and predates SCA-002: this contract
records it rather than deriving it, asserts no confidence label for it because
the record assigns none, and creates no owner-confirmation acceptance criterion
for it.

- **CLM-001** — The accepted `ScopeLedger.csv` row for `SOW-004` reads in full, including its two empty trailing-region fields (columns `ScopeItemID,InOutStatus,ScopeItemStatement,SourceRef,PackageID,DeliverableIDs,ObjectiveIDs,DecisionRef,OpenIssue,Notes`):

> `SOW-004,IN,"Serve per-loop orientation: newest applicable receipt, examined-through SHA, gate states, owner directions of record, open tranches/candidate briefs, parked lanes each with its unparking owner action",PEC-ORI-001,PKG-04,DEL-04-01,OBJ-001,,FALSE,`
>
> (`DecisionRef` empty; `OpenIssue` `FALSE`; `Notes` empty — no boundary
> decision, no open issue, and no invariant note rides this scope item, unlike
> its `PKG-04` siblings `SOW-006` ("Carries PEC-K-04") and `SOW-009`
> ("Coverage-honesty carry-forward"). ID-shaped text inside this quotation is
> upstream source context, not a local definition or reference.)

  The `SOFTWARE_DECOMP.md` §2 SSOW row for the same item repeats the statement without the register-only columns and likewise leaves `Notes` empty: "| SOW-004 | IN | Serve per-loop orientation: newest applicable receipt, examined-through SHA, gate states, owner directions of record, open tranches/candidate briefs, parked lanes each with its unparking owner action | PEC-ORI-001 | |".

- **CLM-002** — `SOW-004`'s `SourceRef` cell names one locus, `PEC-ORI-001`, the `PRD.md` §9.1 orientation requirement, quoted here in full as it reads: "PEC shall serve, per loop: the newest applicable receipt, examined-through SHA, gate states, owner directions of record, open tranches/candidate briefs, and parked lanes each with the owner action that would unpark it." Its enumeration is six components — (i) the newest applicable receipt, (ii) the examined-through SHA, (iii) gate states, (iv) owner directions of record, (v) open tranches/candidate briefs, and (vi) parked lanes each with the owner action that would unpark it. Those six are register truth, carried here exactly, none added and none dropped, and they are the content of this deliverable's return. `PEC-ORI-001` is one of six `PRD.md` §9.1 requirements; the other five are covered by `PKG-04` siblings and are not this deliverable's (CLM-015).
- **CLM-003** — `OBJ-001` states "Orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation", `SourceRef` `§3.1` (`SOFTWARE_DECOMP.md` §3; `PRD.md` §3 outcome 1). At revision 1.2 its "Mapped Scope Items" cell reads "SOW-001, SOW-003, SOW-004..009, SOW-011..017, SOW-040..043, SOW-089; instruments: SOW-058, SOW-059" and its `MappedDeliverables` cell reads "DEL-00-03, DEL-01-01, DEL-02-01..07, DEL-04-01..05, DEL-08-01..04, DEL-10-01, DEL-10-04". Two clauses of that objective statement are quoted here rather than re-obliged. "Sub-second" is the objective's own word and its buildable form is `SOW-041` — "Complete orientation reads in ≤100 ms at p95 against the current corpus" (`PEC-API-002`) — covered by `DEL-08-04` in `PKG-08`, which tests this deliverable from outside `[E-P51]`; this contract asserts no latency bound and produces no latency evidence. "Per-claim citations" is likewise the objective's word and its buildable form is `SOW-007` (`PEC-ORI-004`), covered by `DEL-04-03`; this contract carries the provenance that act needs and performs no attachment (REQ-005, CON-003).

## Deliverable Definition — Ontology

`DEL-04-01` is typed `BACKEND_FEATURE_SLICE` at Context Envelope `M` with
`PhaseHint` `P1`. `Deliverables.csv` records its `AnticipatedArtifacts` as
"Orientation builder + tests" and leaves `ContextEnvelopeNotes` empty, so there
are no envelope notes to carry forward and `_CONTEXT.md` records "(none)". The
outputs of this contract are bounded by that artifact naming: exactly the
orientation builder and its tests, and nothing beyond those two artifacts and
the components each of them declares as part of itself.

- **OUT-001** — A per-loop orientation builder in the PEC service core: given a loop, it composes from record-tier entities the return required by `SOW-004` — the six components of CLM-002 — carrying each component's citation provenance and each component's stated absence or limitation, and exposes that return through an in-process interface. The builder's **component-derivation record** — the readable artifact in which it declares, per component, the record-tier entities it derives from, the selection rule it applies, and its absence semantics (REQ-004) — is a component of this output rather than a third artifact: it is the builder's own self-declaration, so the register's `AnticipatedArtifacts` naming of exactly two artifacts is preserved.
- **OUT-002** — An automated test suite covering the composition, the derivation boundary, and the absence and limitation behaviour, implementing the verification methods declared in this contract.

### Identity of record

- **CLM-004** — `DEL-04-01` is named "Loop orientation return", Type `BACKEND_FEATURE_SLICE`, Context Envelope `M`, `PhaseHint` `P1`, `ResponsibleParty` `TBD`, `AnticipatedArtifacts` "Orientation builder + tests", `CoversScopeItems` `SOW-004`, `SupportsObjectives` `OBJ-001`, `ContextEnvelopeNotes` empty, with the register `Description` field reading "Per-loop orientation: newest applicable receipt, examined-through SHA, gate states, owner directions of record, open tranches/candidate briefs, parked lanes with unparking acts." Sources: `Deliverables.csv` row `DEL-04-01` and the `SOFTWARE_DECOMP.md` §5 PKG-04 table row "| DEL-04-01 | Loop orientation return | BACKEND_FEATURE_SLICE | M | P1 | SOW-004 |". `ResponsibleParty` is `TBD` throughout the register by the §5 preamble — "assignment happens at WORKING_ITEMS activation, not here" (TBD-001).
- **CLM-005** — The `PKG-04` package charter (`SOFTWARE_DECOMP.md` §4) is "Derivation and serving of orientation: per-loop returns, deltas since SHA, SHA/freshness stamping, per-claim citations, scope parameterization, explicit measurement limits", covering "SOW-004..009 (6)", with "Transport (PKG-08); rendering (PKG-09)" recorded as explicitly out of package scope. Of those six items this deliverable covers exactly one — the per-loop return — and the package's two exclusions bind it directly: no transport surface and no rendering surface is produced here (REQ-011).
- **CLM-006** — The six components of CLM-002 do not map uniformly onto the accepted record-tier entity set, and this contract states the difference rather than averaging it. Three map to a declared type in `PRD.md` §7.1 and in the upstream entity model quoted in CLM-011: the newest applicable receipt to **Receipt** ("Parsed `LOOP_RECEIPTS.md` entries", with per-loop field availability); gate states to **Gate** (the standing plan's "protocol steps and owner gates, with gate state"); and open tranches/candidate briefs to **CandidateBrief** ("Adopted-but-unexecuted and proposed briefs (the work-selection queue)") for the candidate-brief limb. The examined-through SHA is carried structurally rather than as an entity of its own: §7.1 defines **OrientationSnapshot** as "A generated orientation return, stamped with examined SHA — the machine generalization of a receipt", which is the type an instance of this deliverable's return is, and the Receipt row of the same table records an "Examined-Through SHA" field where a ledger has adopted the `D-APP-57` contract. The remaining components — owner directions of record, the "open tranches" limb, and parked lanes each with its unparking owner action — resolve to no declared record-tier type; **DecisionRow** is the nearest and is constrained to "Register-row identity and status only (decision ID, packet path, anchor, state — never the row's prose; PEC-K-10)". That gap is CON-001.
- **CLM-007** — The `SOFTWARE_DECOMP.md` §9 Vocabulary Map fixes two terms this contract uses and keeps them apart. Its two rows read in full, under the map's columns `CanonicalTerm | Synonyms | Notes`:

> | orientation | Step-0 return | The per-loop/scope serve of PEC-ORI-001..006 |
> | OrientationSnapshot | — | Record-tier entity (§7.1): a generated orientation return stamped with examined SHA — the machine generalization of a receipt. Distinct from the general term "orientation" |
>
> (`SOFTWARE_DECOMP.md` §9 Vocabulary Map; both rows quoted in full, neither
> elided. ID-shaped text inside this quotation is upstream source context, not a
> local definition or reference.)

  This contract therefore owns one limb of the general term — `PEC-ORI-001`'s composition — while the other five limbs are its `PKG-04` siblings' (CLM-015), and it defines no entity type for the snapshot its returns are instances of (REQ-003).

### Placement in the work graph

- **CLM-008** — This deliverable has three accepted `EXECUTION` upstream edges and two `ANCHOR` rows, held as `Dependencies.csv` register rows `DEP-04-01-001` through `DEP-04-01-005` at `RegisterSchemaVersion` `v3.1`. The two anchors are `DEP-04-01-001` (package-local to `PKG-04`) and `DEP-04-01-002` (`SOW-004` requirement trace). The three `EXECUTION` rows share the following column values, attributed by column: `FromPackageID` `PKG-04`, `FromDeliverableID` `DEL-04-01`, `FromDeliverableName` "Loop orientation return", `DependencyClass` `EXECUTION`, `AnchorType` `NOT_APPLICABLE`, `Direction` `UPSTREAM`, `DependencyType` `PREREQUISITE`, `TargetType` `DELIVERABLE`, `EvidenceFile` `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md`, `RequiredMaturity` `INITIALIZED`, `ProposedMaturity` `TBD`, `SatisfactionStatus` `PENDING`, `FirstSeen` and `LastSeen` `2026-07-25`, `Status` `ACTIVE`. They differ in target, provenance, and stratum:

  | Register row | `TargetDeliverableID` | `Statement` | `Explicitness` / `Confidence` / `Origin` | `Notes` |
  |---|---|---|---|---|
  | `DEP-04-01-003` | `DEL-10-01` | "Declared pre-P1 sequencing against SOW-004" | `EXPLICIT` / `HIGH` / `DECLARED` | "DECLARED; Flag=none; EdgeID=E-A27" |
  | `DEP-04-01-004` | `DEL-01-01` | "Orientation derivation entry point of PKG-04" | `IMPLICIT` / `MEDIUM` / `EXTRACTED` | "PROPOSAL; Flag=none; EdgeID=E-P11" |
  | `DEP-04-01-005` | `DEL-03-01` | "Orientation derives from a populated record tier" | `IMPLICIT` / `MEDIUM` / `EXTRACTED` | "PROPOSAL; Flag=none; EdgeID=E-P32" |

  The two strata are different things and this contract states each separately. `[E-A27]` is **DECLARED**: under the register-wide rule `C-10` recorded in `_DEPENDENCIES.md`, "DECLARED = both endpoints ID-named with a dependency-bearing verb (consumes/renders/tests/measures/sourced-from/lands-with/grounded-in/stated-in/baselines)", and the exhibit states the same as "both endpoints ID-named in revision 1.1 with a dependency-bearing verb". The verb here is *baselines*: the `SOW-058` ledger row's `Notes` cell reads "Sequencing obligation, pre-P1; baselines SOW-004/041". The edge was therefore read out of accepted decomposition text, not proposed by extraction — which is what its `Explicitness` `EXPLICIT`, `Confidence` `HIGH`, and `Origin` `DECLARED` cells record. `[E-P11]` and `[E-P32]` are **PROPOSAL**: the exhibit defines that stratum as "heuristic candidates under my instruction's candidate-proposal duty; require explicit owner acceptance", and their `IMPLICIT` / `MEDIUM` / `EXTRACTED` cells record that origin. All three are equally *accepted* — `D-PEC-62` §1(4) records the owner accepting the DAG candidate v0.2 exhibit "accepted, all strata as presented" — and equally non-authoritative as to content, because `C-10`'s own text ends "strata are provenance not authority". Citation converts neither stratum into the other (AX-010).

  The three exhibit rows read, under the exhibit's columns `EdgeID,PredecessorID,SuccessorID,Stratum,EdgeKind,Flag,BasisCitation,Rationale`:

> ```
> E-A27,DEL-10-01,DEL-04-01,DECLARED,SEQUENCING,,"SOW-058: ""Measure the Step-0 cost baseline ... before P1 begins""; note: ""baselines SOW-004/041""",Declared pre-P1 sequencing against SOW-004
> E-P11,DEL-01-01,DEL-04-01,PROPOSAL,CONSUMES,,DEL-01-01 envelope note (as E-P10),Orientation derivation entry point of PKG-04
> E-P32,DEL-03-01,DEL-04-01,PROPOSAL,CONSUMES,,,Orientation derives from a populated record tier
> ```
>
> (`PLAN_2026-07-25_project_setup_dag_gate.md` §4.1, rows quoted in full. The
> ellipsis inside `E-A27`'s `BasisCitation` is the exhibit's own abbreviation of
> the `SOW-058` statement, not an elision by this contract; the full statement is
> quoted unabbreviated in CLM-010. The `Flag` column is empty on all three rows,
> and `E-P32`'s `BasisCitation` cell is empty — the only one of the three with no
> cited basis, so that edge rests on its `Statement` and the two deliverables'
> own accepted contracts. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference.)

- **CLM-009** — Every one of the three predecessors is at lifecycle state `INITIALIZED`, which is the maturity all three edges require. `INITIALIZED` means each upstream **contract** is the reliable input: each accepted `ScopeOfWork.md` exists, and no baseline report, no schema, no entity model, and no reconciler does. Nothing in this contract asserts that any upstream artifact exists or has been produced. The obligations this contract binds to are those contracts' stated obligations, quoted in CLM-010 through CLM-012.
- **CLM-010** — From `[E-A27]`, the DECLARED sequencing predecessor, what is owed is a pre-P1 measurement, and it is owed to the phase rather than to this deliverable's content. `SOW-058` states, in full and unabbreviated: "Measure the Step-0 cost baseline (LLM tokens per loop-iteration orientation) before P1 begins; this re-tests the harness query-pain precondition recorded unmet 2026-07-02". Its ledger `Notes` read "Sequencing obligation, pre-P1; baselines SOW-004/041", which is the ID-named dependency-bearing verb the edge's stratum rests on, and `SOW-004` is this deliverable. The upstream contract states its side of the edge in its own voice:

> - **REQ-010** — Both outputs shall be complete and consumable before any P1
>   node starts, satisfying the `PRE_P1_OBLIGATION` constraint, and shall be
>   consumable by `DEL-04-01` and `DEL-08-04` as their declared sequencing
>   predecessor (`CLM-010`, `CLM-011`, `CLM-012`).
> - **REQ-008** — Neither output shall create scope, requirements, or acceptance
>   criteria for the behaviors it measures; those remain with their home
>   packages (`CLM-009`). The measurement instrument records what is observed,
>   and its own method, only.
>
> (`DEL-10-01/ScopeOfWork.md`, Epistemology section; both records quoted in full,
> neither elided. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference — this contract's own `REQ-*` and
> `AC-*` records are separate and differently worded.)

  What the sequencing edge binds, therefore, is order and not content: the baseline exists before `P1` work starts and is not authored by this deliverable, and the upstream contract explicitly disclaims creating any requirement here. The same contract fixes what the baseline measures, in its own voice:

> - **AX-002** — `OBJ-001` governs the subject: the metric exists to test whether
>   orientation becomes a sub-second cited query rather than a session-length
>   prose derivation. What is measured before P1 is therefore the cost of the
>   derivation PRD §2 describes, not the cost of any PEC capability, which does
>   not yet exist at `pre-P1`.
> - **AX-004** — The instrument never becomes the behavior. DL-6 and `PKG-10`'s
>   declared exclusion keep the behaviors under test in their home packages; a
>   measurement artifact that starts specifying `DEL-04-01` or `DEL-08-04` has
>   left this deliverable's scope.
>
> (`DEL-10-01/ScopeOfWork.md`, Axiology section; both records quoted in full,
> neither elided. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference.)

  The baseline is the "before" leg of the comparison this deliverable's existence is meant to change; it measures the pre-PEC prose derivation, not this builder. This contract accordingly binds to the record of that sequencing (REQ-014) and imports none of `PKG-10`'s measurement scope. The register-wide constraint the exhibit records behind this edge is `C-05` `PRE_P1_OBLIGATION` — "All three complete before any P1 node starts", with "E-A27/E-A28 carry the two ID-named baseline targets as edges" — recorded in the exhibit's constraint register and in the upstream contract; this deliverable's own `_DEPENDENCIES.md` names three constraints (`C-03`, `C-04`, `C-10`) and does not name `C-05`, so `C-05` reaches this deliverable through `[E-A27]` and is cited here at that strength.

- **CLM-011** — From `[E-P11]`, the entity model this builder composes from is `DEL-01-01`'s obligation, not this deliverable's:

> - **REQ-001** — The schema and entity model shall define exactly the fourteen
>   record-tier entity types named in CLM-005 — Loop, Workplan, Step, Gate,
>   Receipt, DecisionRow, Fence, Package, Deliverable, DependencyEdge,
>   RunRecord, CandidateBrief, OrientationSnapshot, DriftFinding — with none
>   added and none dropped, and each type shall carry a recorded trace to its
>   `PRD.md` §7.1 row and stated purpose (CLM-006).
> - **REQ-003** — Every record-tier entity type shall carry provenance
>   sufficient for a per-claim citation to its live source — file path, anchor,
>   and/or SHA, per `PEC-ORI-004` — because §7.1 defines the tier as "citable
>   with sources". The act of attaching citations to an orientation response is
>   `DEL-04-03`'s under `SOW-007` (CLM-012); this requirement obliges the model
>   to hold what that act needs, and no more.
> - **REQ-004** — The model shall represent examined-through SHA provenance
>   structurally, so that staleness is a comparison and never a judgment
>   (`PEC-K-04`, `OBJ-002`): OrientationSnapshot shall be stamped with the
>   examined SHA, and two successive snapshots shall be comparable field by
>   field such that a DriftFinding can record a classified difference.
>   Performing that comparison is `DEL-03-02`'s and `DEL-03-03`'s (CLM-012); the
>   model shall not require a human or agent judgment input for any field on
>   which staleness turns.
> - **REQ-007** — No field of any type shall admit file content or diff content
>   (`PEC-K-10`: "Paths, counts, SHAs, states, hashes — never file or diff
>   content"). DecisionRow shall carry register-row identity and status only —
>   decision ID, packet path, anchor, state — and shall have no field capable of
>   holding the row's prose. Enforcement at the ingest boundary is `DEL-01-03`'s
>   guard under `SOW-056`; this requirement binds the shape of the schema so
>   that the guard has nothing to admit into.
> - **REQ-008** — The Receipt type shall represent field availability explicitly
>   per loop, so that a coverage limitation can be stated rather than silently
>   omitted (`PEC-ORI-006`: "Where a feed is unparseable or stale, the response
>   shall state the measurement limitation explicitly; silent omission is
>   prohibited"). The representation shall accommodate both the `D-APP-57` field
>   set and prose-structured ledgers with no validated schema, without
>   presupposing any outcome of `OI-008` (CON-002).
>
> (`DEL-01-01/ScopeOfWork.md`, Epistemology section; all five records quoted in
> full, none elided. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference — this contract's own `REQ-*`,
> `AC-*`, and `CON-*` records are separate and differently worded.)

  Three consequences bind this contract. The composition draws only on those fourteen types and defines none (REQ-003). The per-claim citation provenance the model is obliged to carry is what this builder carries through so that the stamping deliverable can attach it, and no more: the upstream contract names `DEL-04-03` as the owner of the attaching act in its own voice, so this contract does not absorb it (REQ-005, CON-003). And the Receipt type's per-loop field availability is the mechanism by which "newest applicable" can be qualified or reported as unqualifiable rather than guessed (REQ-004, REQ-006, CON-002).

- **CLM-012** — From `[E-P32]`, the populated record tier this builder reads is `DEL-03-01`'s obligation:

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
> (`DEL-03-01/ScopeOfWork.md`, Epistemology section; all four records quoted in
> full, none elided. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference.)

  That contract also states the division of duty around the orientation return in its own voice, quoted here with the surrounding enumeration elided at both ends:

> ... the per-loop orientation return is `DEL-04-01` (`SOW-004`); examined-SHA
> and freshness stamping with per-claim citation attachment is `DEL-04-03`
> (`SOW-006`, `SOW-007`); rendering a measurement limitation into an orientation
> response is `DEL-04-05` (`SOW-009`) ...
>
> (`DEL-03-01/ScopeOfWork.md`, CLM-019; **elided** before "the per-loop" and
> after "(`SOW-009`)", where the same claim continues its enumeration of
> neighbouring deliverables on both sides. ID-shaped text inside this quotation
> is upstream source context, not a local definition or reference.)

  Two consequences bind this contract. The record tier this builder reads exists only where a rebuild has run, and the rebuild contract asserts no standing populated state; a loop for which no reconcile has occurred therefore yields explicit absence rather than a composed return (REQ-006, CON-004). And the limitation the rebuild is obliged to carry through is an input this builder must not drop: it is carried into the return so that the rendering deliverable can state it, which is that contract's own reading of the boundary (REQ-006).

- **CLM-013** — Seven downstream consumer relations are recorded against this deliverable in `_DEPENDENCIES.md` and marked informational: `DEL-10-12` `[E-A22]` (`MEASURES`), `DEL-04-03` `[E-P34]`, `DEL-04-04` `[E-P35]`, `DEL-04-05` `[E-P36]`, `DEL-08-04` `[E-P51]` (`TESTS`), `DEL-09-01` `[E-P59]`, and `DEL-10-05` `[E-P75]` (`MEASURES`). **None of the seven holds a row in this deliverable's `Dependencies.csv`**, which contains only the two anchors and the three upstream `EXECUTION` rows; the downstream rows live in each consumer's own local register, per the deliverable-local storage ruling of `D-PEC-62`. Their strata are not uniform and this contract does not flatten them: `[E-A22]` is `DECLARED` (exhibit basis `SOW-060` note "Measures uptake of SOW-004; arms limb 1 of the falsification clause"), `[E-P59]` is `DERIVED` (basis `SOW-045`: "Dashboard — Overview: the orientation return per loop", with the rationale "'The orientation return' is DEL-04-01's serve (Vocabulary Map)"), and the remaining five are `PROPOSAL`; all seven carry an empty `Flag` column. Every one of the seven runs *from* this deliverable outward: being consumed, measured, or tested by them transfers none of their scope into this contract and imposes no obligation on them (AX-009).
- **CLM-014** — Phase staging, checked against the `PhaseHint` column of `Deliverables.csv` for every deliverable this contract names in its own voice: this deliverable is `P1`; its upstreams are `DEL-10-01` at `pre-P1` and `DEL-01-01` and `DEL-03-01` at `P1`. Its recorded consumers are `P1` (`DEL-04-03`, `DEL-04-05`, `DEL-08-04`), `P2` (`DEL-04-04`, `DEL-09-01`, `DEL-10-05`), and `P3` (`DEL-10-12`). Other deliverables named as owners of adjacent scope are `P1` (`DEL-01-06`, `DEL-04-02`, `DEL-08-01`, `DEL-08-02`, `DEL-10-02`), `P2` (`DEL-05-02`, `DEL-10-04`), and `P3` (`DEL-01-02`). No consumer precedes this deliverable's phase, and no claim in this contract stages any named deliverable into a different phase. The `P3` presence tier (`DEL-01-02`) is not an input of this `P1` return (REQ-002).

### Boundaries

- **CLM-015** — The acts adjacent to this return are owned elsewhere and are cited here, never discharged. Within `PKG-04`: serving deltas since a caller-supplied commit SHA is `DEL-04-02` (`SOW-005`, `PEC-ORI-002`); stamping every response with examined-through SHA, generation time, and per-feed freshness and attaching a citation to every claim is `DEL-04-03` (`SOW-006`, `SOW-007`, `PEC-ORI-003`, `PEC-ORI-004`, carrying `PEC-K-04`); scope parameterization by loop / project / package per the modes ladder is `DEL-04-04` (`SOW-008`, `PEC-ORI-005`, `P2`); stating the measurement limitation where a feed is unparseable or stale is `DEL-04-05` (`SOW-009`, `PEC-ORI-006`). Outside it: the record-tier schema and entity model are `DEL-01-01` (`SOW-001`); the one-command full rebuild that populates the record tier is `DEL-03-01` (`SOW-010`); the Step-0 cost baseline is `DEL-10-01` (`SOW-058`); the Unix-socket server and token-scoped access are `DEL-08-01` (`SOW-003`, `SOW-040`) and the versioned additive API schema is `DEL-08-02` (`SOW-042`); the orientation latency budget of ≤100 ms at p95 is `DEL-08-04` (`SOW-041`); the Overview dashboard that renders the orientation return per loop is `DEL-09-01` (`SOW-045`, `P2`); the cross-loop decision slate is `DEL-05-02` (`SOW-024`, `P2`); the orientation defect-rate spot-check is `DEL-10-04` (`SOW-059`, `P2`), owner-consultation logging is `DEL-10-05` (`SOW-085`, `P2`), and poll-adoption measurement is `DEL-10-12` (`SOW-060`, `P3`); the standing kill test is `DEL-10-02` (`SOW-055`). This contract produces only the orientation builder and its tests.
- **CLM-016** — Consumption of this return is not this deliverable's act. Under `PEC-K-03`, PEC provides labeled, non-authoritative orientation data on request and never self-polls, schedules a consumer, injects into an agent, or claims an external cadence; an explicitly PEC-enabled consumer decides under its own authority whether and when to consume, and any injection is optional and subject to verify-before-rely. Under `PEC-K-11`, that consumer also owns its mode mapping and contact cadence unless its owner separately adopts an exact duty, while pipeline and unscoped-conversation modes support zero-contact operation. PEC declares no polling moment: session start or a mode transition is a contact point only if separately adopted by the consumer owner. This builder therefore composes on request and initiates nothing: it schedules no poll, pushes to no consumer, and asserts no consumption cadence (REQ-010).
- **CLM-017** — Two components of this return point at authored owner text, and the corpus rule for that is link-not-restate. `PEC-K-10` states "Paths, counts, SHAs, states, hashes — never file or diff content"; `PEC-GAT-003`, for the sibling surface that aggregates the same material, reads "PEC shall render a cross-loop decision slate: every AWAITING_RULING row and every parked lane awaiting an owner act, linking to the authored file content rather than restating it"; and `PKG-09`'s package exclusions record "restating authored text (C6)" as out of scope for the rendering package. The upstream DecisionRow shape quoted in CLM-011 enforces the same at the model level. Owner directions of record, candidate briefs, and parked-lane entries are therefore carried in this return as identity, status, and citation (REQ-007).
- **CLM-018** — The deliverable is at lifecycle state `INITIALIZED` with no implementation present. Every requirement, acceptance criterion, and verification method below states a contract on future production; none asserts that anything has been built.

- **TBD-001** — `ResponsibleParty` is unassigned; the register records `TBD`, with assignment at WORKING_ITEMS activation and not in this contract (`SOFTWARE_DECOMP.md` §5 preamble; `_CONTEXT.md`).
- **TBD-002** — The builder's concrete in-process interface — its entry-point name, its parameters, and the shape of the value it returns — is fixed by no accepted source beyond the register phrase "Orientation builder" and `PEC-ORI-001`'s "serve, per loop". It is chosen during production within REQ-011, which bounds it to an interface carrying no transport, serialization, or rendering concern.
- **TBD-003** — How a loop is named and located for a per-loop return is not fixed for this deliverable by any accepted source. The loop-registration configuration is `SOW-094` / `DEL-01-06`, and this deliverable's local register records **no** edge to it: the three `EXECUTION` rows of CLM-008 are the whole of its upstream set. This contract therefore obtains loop identity from the record tier's Loop entity (CLM-011) and settles nothing about the registry, whose home and shape are the open `SOW-077` / `OI-003` question in any case.
- **TBD-004** — Where the component-derivation record of OUT-001 lives and in what form it is published are fixed by no accepted source; they are chosen during production within REQ-004, which fixes what it must declare rather than where it sits.

## Completion and Reliance Basis — Epistemology

The requirements below state what future production must satisfy. Nothing in
this section asserts that a builder, a record tier, a schema, a baseline, or a
test exists.

- **REQ-001** — The builder shall compose, for a named loop, a return carrying all six components enumerated at `SOW-004` and `PEC-ORI-001` (CLM-001, CLM-002): the newest applicable receipt, the examined-through SHA, gate states, owner directions of record, open tranches and candidate briefs, and parked lanes each with the owner action that would unpark it. No component shall be dropped, merged away, or silently substituted, and no seventh component shall be added.
- **REQ-002** — Every component value shall be derived from record-tier entities as obliged by the upstream entity-model contract quoted in CLM-011 and populated by the reconcile obliged in CLM-012. No component shall rest on a presence-tier fact, on a stream or event input, on a cached artifact, or on any value the record tier does not carry, per `PEC-K-05` ("Presence facts never enter record-tier citations"), `PEC-PRS-007` ("Presence data is operational only and shall never appear in record-tier citations"), and `PEC-K-07` ("the reconciler over file truth is the source of every record-tier fact").
- **REQ-003** — This deliverable shall define no record-tier entity type, no schema field, no feed grammar, and no reconcile path, and shall not depend on any upstream artifact existing. The fourteen types are the upstream model's (CLM-011), the rebuild is `DEL-03-01`'s (CLM-012), and the return this builder produces is an instance of the upstream OrientationSnapshot type rather than a type this contract defines (CLM-006, CLM-007, CON-001).
- **REQ-004** — The builder shall declare, in the component-derivation record — a readable component of OUT-001 — for each of the six components: the record-tier entity or entities it is derived from, the selection rule applied (including, for the newest applicable receipt, both the applicability test and the recency ordering, CON-002), and its absence semantics. A component produced by an undeclared entity source or an undeclared selection rule is prohibited.
- **REQ-005** — Each component value shall carry through the citation provenance the upstream model is obliged to hold — file path, anchor, and/or SHA to the live source — so that the stamping-and-citation deliverable can attach it. This deliverable shall attach no citation to a response, shall stamp no response with generation time or per-feed freshness, and shall compute no freshness value; those acts are `DEL-04-03`'s under `SOW-006` and `SOW-007` (CLM-011, CLM-015, CON-003).
- **REQ-006** — Where the record tier holds no reconciled state for the named loop, where the loop is unknown to the record tier, or where the reconcile reported a feed as absent, unreadable, malformed, stale, or grammar-unrecognized, the return shall state that absence or limitation explicitly against the affected component and shall present no derived, defaulted, inferred, or carried-forward value in its place. Silent omission is prohibited (`PEC-ORI-006`), the posture is `PRD.md` §7.3's coverage honesty — "a figure the records don't support is absent and said to be absent" — and `PEC-K-01` graceful absence governs the outer case. Rendering such a limitation into an orientation response is `DEL-04-05`'s act under `SOW-009` (CLM-012, CLM-015); this deliverable carries it through so that act has something to render.
- **REQ-007** — The return shall carry no file content and no diff content, per `PEC-K-10`. Owner directions of record, candidate briefs, and parked-lane entries shall be carried as identity, status, and citation — linking to the authored file content rather than restating it (CLM-017) — so that no authored owner text is reproduced in the return.
- **REQ-008** — The builder shall be read-only over the record tier and over Git: it shall create, modify, or delete no source file, governed file, register, lifecycle file, or store record, and shall provide no path that records an adoption, a ruling, or a direction, per `PEC-GAT-004` ("PEC shall provide no write path that records adoption, ruling, or direction") and `PEC-K-06` observation-not-participation.
- **REQ-009** — The examined-through SHA component shall be the value the record tier carries for the loop's examined state, obtained structurally and never re-derived, inferred, or judged by this builder, so that staleness remains a comparison rather than a judgment (`PEC-K-04`). Where the record tier carries no examined-through SHA for the loop, REQ-006 governs and no substitute value is presented.
- **REQ-010** — The builder shall produce a return only when called, and shall schedule no poll, push to no consumer, initiate no session act, and assert no consumption cadence. Whether and when to request, the consumer's mode mapping and contact cadence, and any optional injection are owned by an explicitly enabled consumer under separately adopted authority; this contract creates no contact event or receiving-loop duty (CLM-016).
- **REQ-011** — The builder shall expose the return through an in-process interface and shall implement no socket binding, no token or access-class check, no wire schema or serialization format, no subscription, and no rendering; those are `PKG-08`'s and `PKG-09`'s under the package exclusions recorded in CLM-005. The return shall be shaped so that the transport deliverables can serialize it without this deliverable's participation (TBD-002).
- **REQ-012** — The builder shall perform no act owned by another deliverable. In particular it shall perform no rebuild or incremental reconcile, no drift classification, no delta-since-a-caller-supplied-SHA service, no response stamping or citation attachment, no scope parameterization beyond a single named loop, no limitation rendering, no gate-precondition evaluation or decision-slate aggregation, no dashboard rendering, no latency measurement or budget assertion, and no adoption, consultation, defect-rate, or cost measurement; each is cited to its owner in CLM-015 and none is discharged here.
- **REQ-013** — The builder and its tests shall introduce no third-party runtime dependency and no external network egress, per `PEC-SVC-001` and `PEC-SVC-002`, whose standing enforcement is `DEL-01-05` covering `SOW-052` and `SOW-053`.
- **REQ-014** — Neither output shall be presented as satisfying, substituting for, amending, or re-testing the Step-0 cost baseline, and neither shall assert a token cost, a before-versus-after comparison, or a query-pain result; the baseline is the declared sequencing predecessor's under `SOW-058` and measures the pre-PEC derivation rather than this builder (CLM-010). This deliverable's own production shall be sequenced consistently with that recorded pre-P1 obligation and shall assert no ruling about it.
- **REQ-015** — Tests shall implement the verification methods declared in this contract; they shall not define scope, requirements, or acceptance criteria.

- **AC-001** — For a fixture record tier, a return composed for a named loop contains all six components of CLM-002, each identifiable in the return by name; no component is absent from the return's structure; and the return carries no component outside those six.
- **AC-002** — Every component value in a composed return traces to a record-tier entity instance; inspection of the builder's input surface finds no presence-tier, stream, event, or cached input contributing to any component; and a fixture carrying presence-shaped data alongside the record tier produces a return in which no component value derives from it.
- **AC-003** — This deliverable's source defines no record-tier entity type, no schema field, no feed grammar, and no reconcile path; the composed return is constructed against upstream-obliged types; and no element of this deliverable asserts or requires that an upstream schema, entity model, reconciler, store, or baseline artifact exists.
- **AC-004** — The component-derivation record — the component of OUT-001 required by REQ-004 — names, for each of the six components, its source entity or entities, its selection rule including the applicability test and recency ordering for the newest applicable receipt, and its absence semantics; and every component value produced in a fixture run is traceable to the rule the record declares for it.
- **AC-005** — Every component value in a composed return carries the citation provenance held by the record-tier entity it came from, and that provenance resolves to a file path, anchor, and/or SHA; and this deliverable's source contains no citation-attachment, generation-time stamping, or freshness-computation path.
- **AC-006** — For fixture cases in which the record tier is empty for the loop, the loop is unknown, and a feed was reported absent, unreadable, malformed, stale, and grammar-unrecognized in turn, the return states the absence or limitation against the affected component, names the loop and the affected component, and presents no derived, defaulted, inferred, or carried-forward value in its place.
- **AC-007** — For a content-dense fixture corpus carrying long prose bodies, authored ruling text, and diff-shaped content, inspection of every field of a composed return finds no file content and no diff content; and every direction-of-record, candidate-brief, and parked-lane entry in the return carries identity, status, and a citation rather than the authored text.
- **AC-008** — A composed return leaves the fixture source corpus and the fixture store byte-identical; the captured filesystem and store write inventory for a composition run is empty; and this deliverable's source contains no write, create, or delete call against any source file, governed file, register, lifecycle file, or store record, and no path that records an adoption, ruling, or direction.
- **AC-009** — The examined-through SHA in a composed return equals the value the fixture record tier carries for that loop, byte for byte; this deliverable's source contains no SHA derivation, inference, or comparison path; and where the fixture record tier carries no examined-through SHA, the return states the absence per AC-006 rather than supplying a value.
- **AC-010** — A composition occurs only in response to a call: instrumentation of a fixture run shows no timer, scheduler, subscription, push, or session-lifecycle act originating in this deliverable, and this deliverable's source contains no polling or cadence logic.
- **AC-011** — The builder is reachable only through its declared in-process interface; this deliverable's source contains no socket binding, token or access-class check, wire schema, serialization format, subscription, or rendering code; and a consumer can serialize a composed return without modifying this deliverable.
- **AC-012** — This deliverable's source and call graph contain no rebuild or incremental reconcile path, no drift-classification path, no delta-since-SHA path, no stamping or citation-attachment path, no scope-parameterization path beyond a single named loop, no limitation-rendering path, no gate-evaluation or slate-aggregation path, no rendering path, no latency measurement or assertion, and no adoption, consultation, defect-rate, or cost measurement; and no test in this deliverable asserts a criterion belonging to any of them.
- **AC-013** — The builder and its tests add no third-party runtime dependency and make no network call, leaving the `DEL-01-05` zero-dependency and locality assertion intact.
- **AC-014** — Neither output states a token cost, a before-versus-after cost comparison, or a query-pain re-test result; neither is presented as the Step-0 baseline or its substitute; and the production record shows this deliverable's sequencing stated against the recorded pre-P1 obligation rather than against a ruling made here.
- **AC-015** — The test suite implements VER-001 through VER-014, executes in the `PKG-04` test run, passes, and introduces no acceptance criterion absent from this contract.
- **AC-016** — The REVIEW gate confirms this contract's traceability to `SOW-004` and `OBJ-001`; confirms that the objective mapping is stated as register-direct and pre-SCA-002, with no confidence label asserted that the record does not carry; confirms that the DECLARED sequencing edge and the two PROPOSAL consumption edges are each stated at their own stratum; and confirms that no `PKG-01`, `PKG-03`, sibling `PKG-04`, `PKG-05`, `PKG-08`, `PKG-09`, or `PKG-10` scope has been absorbed.

- **CON-001** — Three of the six components `SOW-004` requires have no declared record-tier entity type, and the gap is at the level of accepted truth rather than of production choice. `PRD.md` §7.1 enumerates the tier's eleven rows and the upstream entity-model contract fixes the fourteen types they decompose into (CLM-006, CLM-011). "Owner directions of record", the "open tranches" limb, and "parked lanes each with its unparking owner action" appear in none of them. The corpus uses the terms without defining them: "parked lane" occurs at `PEC-ORI-001`, at `PEC-GAT-003` ("every parked lane awaiting an owner act"), at `PEC-DSH-001` ("parked lanes + unparking act"), and in the §9 Vocabulary Map's decision-slate row ("Aggregated AWAITING_RULING rows + parked lanes; link-only"), and is defined by none of them; "open tranche" and "direction of record" occur in `SOW-004`'s own statement and its `PRD.md` source and nowhere else in the accepted PEC sources. The nearest declared types are DecisionRow, constrained by the upstream contract to register-row identity and status only, and CandidateBrief, "Adopted-but-unexecuted and proposed briefs (the work-selection queue)", which plausibly carries the candidate-brief limb but is not stated to carry the "open tranches" limb. This contract records the gap rather than closing it: REQ-001 obliges all six components to appear, REQ-003 forbids defining a record-tier type here, and REQ-004 obliges the derivation of each component to be declared, so that whatever entity mapping production settles on is visible and reviewable. Defining a new record-tier type to hold these three would take `DEL-01-01`'s decision in the wrong place; concluding that the components may be omitted would contradict `SOW-004`. Which existing types carry them, or whether the model must be amended, is a question for the entity-model contract and, if it changes the model, for a scope change.
- **CON-002** — "Newest applicable receipt" carries two undefined operators and one known data limitation. No accepted source states what makes a receipt *applicable* to a per-loop orientation, and no accepted source states the ordering by which one is *newest* — whether by receipt timestamp, by ledger position, by examined-through SHA ancestry, or otherwise. The data side is not merely unstated but recorded as uneven: `PRD.md` §7.1 records that "the app-dev ledger carries the D-APP-57 contract (Receipt-ID, Examined-Through SHA, Parent-Receipt, Gate-Outcome); the pec/bridge ledgers are prose-structured with no validated schema — coverage limits stated per PEC-ORI-006", the `SOW-001` ledger note repeats "Receipt field availability is per-loop (PEC-ORI-006 limits apply)", and `OI-008` — "§16.8 receipt-contract adoption by non-app-dev ledgers undecided" — is open pending a per-loop §16 ruling. For a loop whose ledger carries no validated schema, the fields an ordering or an applicability test would need may simply be absent. This contract requires the applied rule to be declared (REQ-004) and requires the unqualifiable case to be stated as a limitation rather than resolved by a guess (REQ-006); it selects no rule, presupposes no `OI-008` outcome, and no selection may be inferred from this document.
- **CON-003** — The examined-through SHA appears twice in the accepted scope, once as a component of this deliverable's return (`SOW-004`, `PEC-ORI-001`) and once inside the response-level stamp of another (`SOW-006`, `PEC-ORI-003`: "Every orientation response shall carry the examined-through SHA, generation time, and per-feed freshness"), and no accepted source states whether the two are the same field. The register is unambiguous about ownership — the stamping act is `DEL-04-03`'s, and the upstream entity model names that deliverable as the owner of citation attachment in its own voice (CLM-011) — but not about representation. This contract takes the narrow reading that its own row supports: the SHA is composed as a content component of the return, obtained structurally from the record tier (REQ-009), while the response-level stamp of SHA, generation time, and per-feed freshness, and the attachment of per-claim citations, are performed elsewhere and are not duplicated here (REQ-005). Whether the consuming deliverable reads this component or stamps an independently obtained value is left open by the accepted sources and is not settled here.
- **CON-004** — No accepted source states what a per-loop orientation return *is* when the record tier has never been reconciled for that loop, or when the loop is unknown. `SOW-004` says "Serve per-loop orientation" and the reconciler contract asserts no standing populated state (CLM-012). The invariants nevertheless fix the posture rather than leaving it open: `PEC-K-01` graceful absence ("No governed act may require a PEC read or write. Deleting PEC blocks nothing."), `PRD.md` §7.3 coverage honesty ("a figure the records don't support is absent and said to be absent"), and `PEC-K-08` explainability ("Every status, verdict, and warning carries rule ID, threshold, and contributing cited sources. Drill-down never dead-ends") together forbid a fabricated or partially guessed return. REQ-006 states that obligation as a checkable requirement. What remains genuinely unsettled is the *shape* of the honest answer — an empty return carrying six stated absences, a single stated absence for the loop, or a distinguishable not-found condition — which is a production choice bounded by REQ-006 and not a scope question.

## Production and Verification Method — Praxeology

Production proceeds in the order upstream-contract survey → component
derivation map → composition path → absence and limitation carry-through →
provenance carry-through → tests, because the component derivation map is the
acceptance surface of everything after it and because three of the six
components have no settled entity source (CON-001). The upstream-contract
survey comes first because all three predecessors are at `INITIALIZED` and
supply obligations rather than artifacts, so a composition path written against
an imagined schema or an assumed populated store would violate REQ-003 before
any code existed. Absence handling is built before provenance rather than after
it, because a return that composes successfully only over complete fixtures
tends to acquire defaults that REQ-006 forbids. All work is bounded to this
deliverable folder and the `PKG-04` service-core source it names; this contract
authorizes no register, decomposition, PRD, or upstream-deliverable edit, and it
neither defines nor reshapes the entity model it reads, the reconcile that
populates it, the transport that serves it, or the surfaces that stamp, cite,
parameterize, render, or measure it. Tests implement the verification methods
below and create no scope.

- **VER-001** — Component-completeness exercise: compose a return for a named loop over a fixture record tier and assert, component by component, that all six of CLM-002 are present and identifiable by name, that none is absent from the return's structure, and that the return carries no seventh component.
- **VER-002** — Derivation-boundary trace: for each of the six components, trace the composed value back to the record-tier entity instance that produced it; inspect the builder's input surface for presence-tier, stream, event, and cached inputs and assert none contributes; and compose over a fixture carrying presence-shaped data alongside the record tier, asserting no component value derives from it.
- **VER-003** — Definition inspection: search this deliverable's source for record-tier entity type definitions, schema field definitions, feed grammar definitions, and reconcile paths and assert none is present; assert the composed return is constructed against upstream-obliged types; and search source, fixtures, and call surface for any assumption that an upstream schema, entity model, reconciler, store, or baseline artifact exists, asserting none.
- **VER-004** — Derivation-record exercise: read the component-derivation record (the component of OUT-001 required by REQ-004) and assert it declares, per component, its source entities, its selection rule — including the applicability test and recency ordering for the newest applicable receipt — and its absence semantics; then compose over fixtures and assert each produced value follows the rule the record declares for it.
- **VER-005** — Provenance carry-through: for each component of a composed return, assert the citation provenance of its source entity is present in the return and resolves to a file path, anchor, and/or SHA; and search this deliverable's source for citation-attachment, generation-time stamping, and freshness-computation paths, asserting none.
- **VER-006** — Absence and limitation exercise: compose over fixture cases in which the record tier is empty for the loop, the loop is unknown, and a feed was reported absent, unreadable, malformed, stale, and grammar-unrecognized in turn; assert per case that the return states the absence or limitation against the affected component and names the loop and component, and that no derived, defaulted, inferred, or carried-forward value is presented in its place.
- **VER-007** — Content inspection: compose over a content-dense fixture corpus carrying long prose bodies, authored ruling text, and diff-shaped content, then dump every field of the return and assert field by field that none carries file or diff content, and that every direction-of-record, candidate-brief, and parked-lane entry carries identity, status, and a citation rather than authored text.
- **VER-008** — Write-boundary exercise: hash the fixture source corpus and the fixture store before and after a composition and assert byte-identity; capture every filesystem and store write performed during the run and assert the inventory is empty; and inspect this deliverable's source for write, create, or delete calls against source, governed, register, lifecycle, or store targets and for any adoption-, ruling-, or direction-recording path, asserting none.
- **VER-009** — SHA-component check: compare the examined-through SHA in a composed return against the value the fixture record tier carries for that loop and assert byte equality; inspect this deliverable's source for SHA derivation, inference, or comparison logic and assert none; and compose over a fixture carrying no examined-through SHA, asserting the absence is stated rather than filled.
- **VER-010** — Initiation inspection: instrument a fixture run and assert no timer, scheduler, subscription, push, or session-lifecycle act originates in this deliverable; inspect the source for polling or cadence logic and assert none.
- **VER-011** — Interface-boundary inspection: assert the builder is reachable only through its declared in-process interface; search this deliverable's source for socket binding, token or access-class checks, wire schemas, serialization formats, subscription code, and rendering code, asserting none; and serialize a composed return from a consumer stand-in without modifying this deliverable.
- **VER-012** — Adjacent-act inspection: inspect this deliverable's call graph and source for rebuild, incremental reconcile, drift-classification, delta-since-SHA, stamping, citation-attachment, scope-parameterization, limitation-rendering, gate-evaluation, slate-aggregation, rendering, latency-measurement, and adoption/consultation/defect/cost-measurement paths, asserting each absent; and review this deliverable's tests for any criterion belonging to another deliverable, asserting none.
- **VER-013** — Inspect the `PKG-04` dependency manifest and this module's import graph for third-party runtime dependencies and network calls, and re-run the `DEL-01-05` zero-dependency and locality enforcement once that deliverable is available, without discharging it here.
- **VER-014** — Sequencing and measurement-boundary review: read both outputs and assert that neither states a token cost, a before-versus-after comparison, or a query-pain re-test result, and that neither is presented as the Step-0 baseline or its substitute; and confirm the production record states this deliverable's sequencing against the recorded pre-P1 obligation without asserting a ruling about it.
- **VER-015** — Run the `PKG-04` test suite and confirm that each of VER-001 through VER-014 has a corresponding executing automated test and that no test asserts a criterion absent from this contract.

## Governing Values and Decisions — Axiology

- **AX-001** — `OBJ-001` governs: orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation. This deliverable is the composition step where that promise becomes a concrete return, and it is the only place in `PKG-04` where the *content* of the per-loop answer is decided; everything else in the package qualifies, stamps, parameterizes, or reports on that content. A return that omitted a component would falsify the objective quietly, because the caller has no way to know what was not offered.
- **AX-002** — `PEC-K-01` graceful absence is the invariant behind REQ-006, and it cuts inward. PEC exists to be deletable, which means the ordinary case includes a store that has never been reconciled. An orientation builder that filled such a gap with a default, a stale carry-forward, or an inferred value would make PEC's own emptiness invisible at exactly the moment a caller most needs to see it, and would convert a deletable projection into something a consumer could be misled by.
- **AX-003** — `PEC-K-05` two tiers, never blurred, and `PEC-K-07` reconciliation-is-guaranteed jointly fix where this return's content may come from. Presence data is fresher and would often be more convenient — who is working where, what is live right now — and `PEC-PRS-007` forbids it entering record-tier citations. A cited orientation is only as trustworthy as the tier it draws on, so REQ-002 restricts the composition to the reconciled tier even where the presence tier holds a newer-looking answer.
- **AX-004** — `PEC-K-04` staleness-is-a-comparison is why REQ-009 forbids this builder from deriving the examined-through SHA. The SHA's value to a consumer is that it is a structural fact they can compare against their own state; a SHA computed, inferred, or chosen by the orientation layer would look identical and mean nothing.
- **AX-005** — `PEC-K-06` observation-not-participation and `PEC-GAT-004` govern REQ-008's outer edge. This return surfaces owner directions, gates, and parked lanes — the exact material a write path would be tempting to attach to — and `PEC-GAT-004` prohibits any PEC write path that records adoption, ruling, or direction. The restriction is stated as a checkable boundary rather than a discipline.
- **AX-006** — `PEC-K-10` content-minimal and the link-not-restate rule are a residency posture, and this deliverable is where authored owner text comes closest to being convenient to copy. The strongest enforcement is upstream — DecisionRow has nowhere to put prose — but the return assembles several such rows into one payload, which is exactly where a helpful summary would appear. REQ-007 binds the return side directly.
- **AX-007** — `PEC-K-03` and `PEC-K-11` keep consumption outside this contract. PEC serves labeled non-authoritative orientation on request; an explicitly enabled consumer decides whether and when to consume, owns its mode mapping and cadence, and may choose whether to inject subject to verify-before-rely. Zero contact remains valid. A builder that scheduled its own refresh would take a decision that belongs to the consumer owner.
- **AX-008** — The DECLARED sequencing edge is respected as sequencing and nothing more. `[E-A27]` records that the Step-0 baseline is measured before `P1` begins and that it *baselines* `SOW-004`; it does not make the baseline an input this builder reads, nor make this builder a subject the baseline measures — the upstream contract states in its own voice that what is measured before `P1` is the cost of the prose derivation, "not the cost of any PEC capability, which does not yet exist at `pre-P1`". Reading a DECLARED stratum as a stronger claim on this contract's content than its own text supports would be the same error in the opposite direction from ignoring it.
- **AX-009** — Edge direction is a constraint on this contract, not a licence. Upstream, `RequiredMaturity` `INITIALIZED` on all three edges means each upstream *contract* is the reliable input, not any upstream artifact; this contract is written against the obligations quoted in CLM-010 through CLM-012 and asserts nothing about upstream implementation state. Downstream, being consumed by the stamping, parameterization, and limitation deliverables, rendered by a dashboard, tested by a latency budget, and measured by three `PKG-10` instruments neither expands this contract's scope nor transfers any of theirs into it — least of all the latency budget, which tests this deliverable from outside under `SOW-041`.
- **AX-010** — `C-10` `STRATUM_RULE` is a register-wide non-gating constraint whose own text ends "strata are provenance not authority", and this deliverable's upstream set spans two strata, so the distinction is load-bearing here rather than decorative. `[E-A27]`'s `DECLARED` records that both endpoints were ID-named in accepted decomposition text with a dependency-bearing verb; `[E-P11]`'s and `[E-P32]`'s `PROPOSAL` records that they were proposed heuristically under the extraction's candidate-proposal duty. `D-PEC-62` §1(4) accepts all three — "accepted, all strata as presented" — and that packet reads "as presented" as accepting the exhibit's flags as flags, leaving a specific annotated set (`E-A11`, `E-P69`/`E-N02`, `E-N13`/`E-N18`, the `C-02` direction, the `C-08` standing-node set) recorded-but-unresolved. None of those annotations touches any edge cited in this contract; every upstream and downstream edge named here carries an empty `Flag` column. Provenance is not authority in either direction: a `DECLARED` edge is not thereby a stronger obligation on content, and a `PROPOSAL` edge is not thereby a weaker one.
- **AX-011** — `C-03` `PACKAGE_LEVEL` — "Every PKG-03/04/05 deliverable depends on DEL-01-01 directly or transitively" — is the accepted statement behind `[E-P11]`, whose exhibit basis is recorded for its edge class as "package-level accepted; deliverable pairing proposed — constraint C-03". `C-04` `PHASE_PRECEDENCE` is recorded with hard-versus-soft classification still a Phase 1.3 owner ruling. Both are register-wide non-gating constraints, and blocker output under the `FULL_GRAPH` mode at threshold `INITIALIZED` is advisory visibility only, never work assignment.
- **AX-012** — Unknowns stay marked. TBD-001 through TBD-004 and CON-001 through CON-004 are recorded rather than resolved by inference. `OI-008` is a per-loop §16 ruling and `OI-003` is a §16 ruling on the loop registry's home and shape; a production choice that settled either would be a decision taken in the wrong place. Revision 1.3 supersedes the former `OI-011` polling-moment interpretation: PEC declares no polling moment, and session start or a mode transition becomes a contact point only through separately adopted consumer authority (CLM-016).
- **AX-013** — This contract is lifecycle-neutral. `_STATUS.md` remains the sole lifecycle authority and is untouched by this reconciliation; the deliverable is at `INITIALIZED` and nothing has been built.

**Quotation record.** Every quotation in this contract is verbatim from the
named source. Exactly one quotation is elided by this contract, and it is
marked at the point of elision and enumerated here in full: the boundary-claim
quotation from `DEL-03-01`'s Ontology section in CLM-012, whose upstream claim
identifier is recorded in that quotation's own attribution line, elided before
"the per-loop orientation return"
and after "(`SOW-009`)", where the source claim continues its enumeration of
neighbouring deliverables on both sides. Two further points are noted so they are not
mistaken for elisions of this contract's making. The ellipsis inside the
`E-A27` exhibit row quoted in CLM-008 is the exhibit's own abbreviation of the
`SOW-058` statement, which CLM-010 quotes unabbreviated. The `..` ranges inside
the `A001` and `A003b` quotations in the objective warrant are the source's own
range notation. No annotation of this contract's making appears inside any
quotation, and no other quotation in this document omits text from the span it
presents.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-004 OBJ-001 | REQ-001, CLM-001, CLM-002, CLM-006 | AC-001 | VER-001 | Composed returns over a fixture record tier with a component-by-component completeness table showing all six SOW-004 components present and no seventh |
| OUT-001 | SOW-004 OBJ-001 | REQ-002, CLM-011, CLM-012, CLM-014, AX-003 | AC-002 | VER-002 | Per-component derivation traces from return value to record-tier entity instance; the input-surface inspection record showing no presence, stream, event, or cached contribution; the presence-shaped fixture run |
| OUT-001 | SOW-004 OBJ-001 | REQ-003, CLM-007, CLM-009, CON-001 | AC-003 | VER-003 | Recorded searches of this deliverable's source for entity-type, schema-field, feed-grammar, and reconcile definitions and for upstream-artifact assumptions, plus the construction record showing composition against upstream-obliged types |
| OUT-001 | SOW-004 OBJ-001 | REQ-004, TBD-004, CON-002 | AC-004 | VER-004 | The component-derivation record (a component of OUT-001) with per-component source entities, selection rules including the applicability test and recency ordering, and absence semantics, plus fixture values traced to the declared rules |
| OUT-001 | SOW-004 OBJ-001 | REQ-005, CLM-003, CON-003 | AC-005 | VER-005 | Per-component provenance resolutions to path, anchor, and/or SHA, plus a recorded search for citation-attachment, stamping, and freshness-computation paths |
| OUT-001 | SOW-004 OBJ-001 | REQ-006, CON-004, AX-002 | AC-006 | VER-006 | Per-case returns for empty record tier, unknown loop, and absent, unreadable, malformed, stale, and grammar-unrecognized feeds, each naming the loop and component and presenting no substitute value |
| OUT-001 | SOW-004 OBJ-001 | REQ-007, CLM-017, AX-006 | AC-007 | VER-007 | Field-by-field dumps of a return composed over a content-dense fixture corpus, showing no file or diff content and identity-status-citation form for directions of record, candidate briefs, and parked lanes |
| OUT-001 | SOW-004 OBJ-001 | REQ-008, AX-005 | AC-008 | VER-008 | Before/after hashes of the fixture corpus and store, the empty write inventory for a composition run, and the source inspection record showing no write path and no adoption-, ruling-, or direction-recording path |
| OUT-001 | SOW-004 OBJ-001 | REQ-009, AX-004 | AC-009 | VER-009 | Byte comparison of the returned examined-through SHA against the fixture record-tier value, the search record showing no derivation or comparison logic, and the no-SHA fixture return stating absence |
| OUT-001 | SOW-004 OBJ-001 | REQ-010, CLM-016, AX-007 | AC-010 | VER-010 | Instrumented fixture-run trace showing no timer, scheduler, subscription, push, or session act originating here, plus the source search for polling or cadence logic |
| OUT-001 | SOW-004 OBJ-001 | REQ-011, CLM-005, TBD-002 | AC-011 | VER-011 | The declared in-process interface, a recorded search for socket, token, wire-schema, serialization, subscription, and rendering code, and a consumer stand-in serializing a composed return unmodified |
| OUT-001 | SOW-004 OBJ-001 | REQ-012, CLM-013, CLM-015, AX-009 | AC-012 | VER-012 | Call-graph and source inspection records showing each named adjacent path absent, plus a review of this deliverable's tests confirming no criterion belonging to another deliverable |
| OUT-001 | SOW-004 OBJ-001 | REQ-013 | AC-013 | VER-013 | Dependency-manifest and import-graph inspection records, plus the DEL-01-05 enforcement result once that deliverable is available |
| OUT-001 | SOW-004 OBJ-001 | REQ-014, CLM-010, AX-008 | AC-014 | VER-014 | Output review showing no token cost, comparison, or query-pain result asserted, and the production sequencing record stated against the recorded pre-P1 obligation |
| OUT-002 | SOW-004 OBJ-001 | REQ-015, CLM-018 | AC-015 | VER-015 | PKG-04 test-run output mapping each executed test to its declared verification method, with no criterion asserted that this contract does not state |
| OUT-001 | SOW-004 OBJ-001 | CLM-004, CLM-008, TBD-001, TBD-003, AX-001, AX-010, AX-011, AX-012, AX-013 | AC-016 | HUMAN_REVIEW: REVIEW gate confirms traceability to SOW-004 and OBJ-001, confirms the objective mapping is stated as register-direct and pre-SCA-002 with no unrecorded confidence label, confirms the DECLARED and PROPOSAL upstream edges are each stated at their own stratum, and confirms no upstream, sibling, or cross-package scope absorption | Review record citing the SOW-004 ledger row, the A001/A002/A003b evidence for the pre-existing objective mapping, the three upstream register rows with their strata, and the sibling and cross-package deliverable boundaries |
