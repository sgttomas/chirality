---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-10-10
package_id: PKG-10
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@11a494e9a
project_scope_refs: [SOW-064]
package_objective_refs: [OBJ-006]
---

# Scope of Work — DEL-10-10 Directed bootstrap self-ingest validation

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-10-10` — "Directed
bootstrap self-ingest validation" — in `PKG-10` (Validation & Measurement) of
the PEC v2 build. It covers project scope item `SOW-064` in service of package
objective `OBJ-006`.

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.3** (`current_basis`, `SCA-003` successor), pinned at merge
`11a494e9a`. The deliverable-local `_REFERENCES.md` now cites that current
basis under the reference-parity integration at `af62343d3`. `_CONTEXT.md`
retains the revision-1.1 to revision-1.2 supersession trace; SCA-003 in turn
establishes revision 1.3 as the current successor. This contract cites
revision 1.3.

**Standing character (load-bearing), and what authorizes it.** Everything below
is written as a contract on a *continuing* validation: there is no state in
which this deliverable's assertion is finished, and any entry in its record is
evidence for the progression state it observed and for no later state. That
framing is directed by this run's brief under `D-PEC-63`, whose directing
sentence reads, verbatim:

> Author this contract as a STANDING assertion — a continuously re-runnable
> verification, not a one-shot artifact.

That sentence is carried durably at
`execution/_Coordination/WAVE_D-PEC-63/BATCH_B5_FANIN.md`, the batch fan-in
record for the batch this run belongs to, which the dispatcher writes in this
tranche and which records it verbatim. The framing is informed by, not derived
from, the `C-08` `STANDING_NODES` annotation described in CLM-008. It is
therefore a property of how this contract is written. It is not an owner-ruled
gating force, and the question of whether the validation carries release-gating
authority is routed to the owner under CON-001 rather than assumed here.

This deliverable is the one member of the `C-08` set whose standing character
and whose artifact coincide. The constraint row's own `Notes` field says so —
"DEL-10-10 is the bootstrap progression record itself" — and the evidence
phrase `C-08` cites for this member is "standing validation", which is the
`Deliverables.csv` `Description`'s own wording ("used as a standing validation
thereafter"). The record is not a report *about* a standing validation; it is
the standing validation's persistent form (CLM-008, CON-002).

**Objective warrant.** `SOW-064` → `OBJ-006` is **register-direct**, and this
contract states it at record strength: no confidence label is asserted, and no
owner-confirmation criterion is created for it, because the register carries the
mapping directly and no accepted record rates or qualifies it.

The mapping predates `SCA-002`. It was made by `SCA-001` under `D-PEC-61`,
whose decision-log entry `DL-16` records the amendment as one that "adds
construction-specific constraint C16, expands SOW-064 and DEL-10-10 into
directed full-DAG bootstrap progression evidence, maps both to OBJ-006, and
re-envelopes DEL-10-10 S→M". Three verifications were performed against the
live registers and the scope-change evidence before this contract was written,
and all three agree:

1. At the `SCA-001` commit `04a5efbf6` — the accepted revision 1.1 state, before
   `SCA-002` — the `ScopeLedger.csv` row for `SOW-064` already carried
   `ObjectiveIDs` `OBJ-006`, and that row is byte-identical to the row in the
   current accepted basis at `11a494e9a` (CLM-001).
2. `SOW-064` is not among the twenty `IN` rows whose `ObjectiveIDs` `SCA-002`
   populated under action `A001`, and `DEL-10-10` is not among the seventeen
   deliverable rows whose `SupportsObjectives` it populated under `A002`.
   `SCA-002`'s own `Decision_Log.md` control `C-54` records the row being
   restored after an incidental writer renormalisation: "**`ScopeLedger.csv`
   SOW-064 quoting** — restored byte-identical to HEAD", with "**no
   non-`ObjectiveIDs` field change**" across the twenty approved rows.
3. The `SOFTWARE_DECOMP.md` §3 objective row for `OBJ-006` names both
   `SOW-064` and `DEL-10-10` in its mapped cells at revision 1.3 (CLM-005).

The accepted sources also state the substantive link in their own voice, which
this contract cites rather than derives. `OBJ-006`'s `SourceRef` is `PRD.md`
§11 while `SOW-064`'s current `SourceRef` is
"PRD v2.2 §12, D-PEC-61, D-PEC-68"; the §12 text itself joins them, calling
PEC's self-ingestion "the first validation of the thesis" (CLM-002), and
`OBJ-006` is the objective about the thesis remaining measurable and
falsifiable (CLM-005).

Source chain, in order of authority for this contract:

1. `execution/_Decomposition/ScopeLedger.csv`, row `SOW-064` (CLM-001).
2. `docs/PRD.md` v2.2 §12, the `SourceRef` the ledger names (CLM-002).
3. `execution/_Coordination/_DECISIONS/D-PEC-61_directed_full_dag_self_bootstrap.md`,
   the decision the ledger names (CLM-003).
4. `execution/_Coordination/_DECISIONS/D-PEC-68_prd_v2_2_consumer_interface_concordance.md`,
   the PRD v2.2 concordance decision named by `SOW-064`'s current `SourceRef`
   (CLM-002).
5. `execution/_Decomposition/SOFTWARE_DECOMP.md` §1.3 constraint `C16`, §3
   objective row `OBJ-006`, §4 package row `PKG-10`, §5 `PKG-10` deliverable
   row, and §11 decision-log entries `DL-11` and `DL-16` (CLM-004, CLM-005,
   CLM-006, CLM-007, CLM-017).
6. `execution/_Decomposition/Deliverables.csv`, row `DEL-10-10` (CLM-007).
7. The deliverable-local control files (`_CONTEXT.md`, `_REFERENCES.md`,
   `_DEPENDENCIES.md`, `Dependencies.csv`, `_STATUS.md`) and the accepted gate
   exhibit `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md`
   (CLM-008, CLM-009).
8. The two upstream `EXECUTION` predecessors' own accepted contracts, read as
   contracts (CLM-010, CLM-011, CLM-012).

- **CLM-001** — The accepted `ScopeLedger.csv` row for `SOW-064` reads in full, under the column order `ScopeItemID,InOutStatus,ScopeItemStatement,SourceRef,PackageID,DeliverableIDs,ObjectiveIDs,DecisionRef,OpenIssue,Notes`:

> `SOW-064,IN,"Directed bootstrap: P1 first ingests PEC v2's accepted full dependency DAG as its initial file-native coordination state; later DAG nodes consume only PEC capabilities already produced and accepted by predecessors, while observed coordination friction is captured as evidence for candidate functions and boundary or amendment decisions","PRD v2.2 §12, D-PEC-61, D-PEC-68",PKG-10,DEL-10-10,OBJ-006,"DL-10; DL-11; SCA-001",FALSE,"Introduced in P1 and standing thereafter; observations grant no authority or scope, the file-native fallback remains operable, and generality is validated against a structurally different loop"`
>
> (ID-shaped text inside this quotation is upstream source context, not a local
> definition or reference.)

  Attributed by column: `InOutStatus` `IN`; `SourceRef` "PRD v2.2 §12, D-PEC-61, D-PEC-68"; `PackageID` `PKG-10`; `DeliverableIDs` `DEL-10-10`; `ObjectiveIDs` `OBJ-006`; `DecisionRef` "DL-10; DL-11; SCA-001"; `OpenIssue` `FALSE`. The `Notes` cell carries three constraints in the register's own voice and they bind this contract (CLM-016). The `SOFTWARE_DECOMP.md` §2.1 SSOW row for the same item repeats the statement without the register-only columns and appends the same current source chain and ledger-note provenance.

- **CLM-002** — The `SourceRef`'s first locus is `docs/PRD.md` v2.2 §12 "Release strategy", whose two closing paragraphs are the accepted statement of the directed bootstrap and are quoted here in full:

> The PEC v2 build itself runs through the governed pipeline (SOFTWARE_DECOMP →
> PROJECT_SETUP → WORKING_ITEMS), and the first loop the P1 reconciler ingests
> is **its own build** — the bootstrap is the first validation of the thesis.
>
> For PEC v2's own build, PROJECT_SETUP materializes the accepted decomposition
> as a **full dependency DAG**, which is the initial file-native coordination
> state and PEC's first self-ingestion corpus. P1 first ingests that build
> graph. Later DAG nodes may consume only PEC capabilities already produced
> and accepted by predecessor nodes; no node depends on the capability it is
> creating. Coordination friction observed during this progression may produce
> evidence-linked candidate functions, boundary decisions, and scope-change
> requests, but it grants no authority and changes no accepted scope without
> human approval. The file-native fallback remains operable throughout.
> Generality is tested against a structurally different loop after
> self-ingestion.

  The same section's current `P1` release row states the phase this deliverable is introduced in — "**P1 — One-loop reconciler** | Reconciler + orientation store + API for PEC's own build graph, read-only | Parity-diff vs harness clean or explained; rebuild-from-scratch ≤ bound; kill test passes". The former `OI-010` reading about the superseded “piping or root” parenthetical remains historical provenance for how the directed-bootstrap clarification entered the corpus; revision 1.3 already incorporates the own-build-graph wording directly.

- **CLM-003** — The `SourceRef`'s second locus is `D-PEC-61`, ruled 2026-07-24, whose ruled behavior item 1 states the §12 clarification in the decision's own voice:

> **PRD v2.1 clarification.** `projects/pec/docs/PRD.md` advances from v2.0
> to v2.1. Section 12 records that PEC's own build uses the accepted full
> dependency DAG as its initial file-native coordination state; P1 first
> ingests that build graph; later nodes consume only capabilities already
> produced and accepted by predecessors; observed friction may generate
> evidence-linked candidate functions, boundary decisions, and scope-change
> requests but grants no authority and changes no scope without human
> acceptance; the fallback remains operable; generality is tested against a
> structurally different loop after self-ingestion.
>
> (`D-PEC-61_directed_full_dag_self_bootstrap.md`, "Ruled behavior" item 1,
> quoted in full. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference.)

  The same packet's item 2 records `FULL_GRAPH` as "the owner-selected coordination representation for PEC Project Setup", and its closure section records `SCA-001` accepted with the Gate 5 confirmation "I confirm the post-change state and accept decomposition revision 1.1 as the current basis."

- **CLM-004** — Hard constraint `C16` of `SOFTWARE_DECOMP.md` §1.3 is the decomposition-side form of the same rule, quoted in full from the row whose columns are `# | Constraint | Source`: "| C16 | Directed self-bootstrap for PEC's own build: `PROJECT_SETUP` materializes the accepted decomposition as `FULL_GRAPH`; later nodes consume only PEC capabilities produced and accepted by predecessor nodes; no node depends on the capability it creates; observed friction routes to evidence-linked candidates and human gates; the file-native fallback remains operable | PRD v2.2 §12, D-PEC-61, D-PEC-68 |". §2's preamble states how such a constraint relates to the scope items, quoted in full: "Hard constraints C1–C16 (§1.3) bind every item and are not repeated as scope items unless they also require built or verified behavior (DL-7/DL-8)." `DL-16` records that `SCA-001` added `C16` and expanded `SOW-064` in the same amendment (CLM-017), so the constraint and the scope item are two accepted surfaces of one ruled clarification rather than a constraint restated as scope.
- **CLM-005** — `OBJ-006` states "The product thesis remains measurable and falsifiable: adoption, parity, defect, and collision metrics are gathered in system behavior and the §11 falsification clause stays armed", `SourceRef` `§11`. At revision 1.3 its "Mapped Scope Items" cell reads "SOW-020, SOW-057..060, SOW-064, SOW-084, SOW-085, SOW-093" and its `MappedDeliverables` cell reads "DEL-01-04, DEL-03-04, DEL-10-01, DEL-10-04, DEL-10-05, DEL-10-09, DEL-10-10, DEL-10-11, DEL-10-12" (`SOFTWARE_DECOMP.md` §3). The current `PRD.md` §11 heading scopes those metrics more precisely as "measured in observable system and use behavior", and its falsification clause states that, after Phase 3, negligible explicit consumer enablement or enabled-consumer orientation use together with owner non-use of the dashboards falsifies the thesis; PEC is deleted and, by `PEC-K-01`, nothing breaks. The §11 numbered metric list — Step-0 cost, orientation defect rate, collision incidents, consumer uptake, parity, and the kill test — does not name the bootstrap progression among its six measurements; consumer uptake is measured without external conformance. The register maps this scope item to this objective directly and this contract states the mapping at that strength, without deriving it from the §11 list.
- **CLM-006** — `PKG-10` is "Validation & Measurement — Release-gating proof and metrics: kill test, no-ruling-write verification, Step-0 baseline, defect/adoption/collision/parity measurement, seeded-conflict, TTL-honesty and stream-loss tests, usage observability, directed bootstrap progression evidence", assigned "SOW-025, 055, 058..064, 084, 085, 093 (12)", with **Exclusions** "The behaviors under test (their home packages)" (`SOFTWARE_DECOMP.md` §4, columns `PackageID | Name | Scope Description (work domain) | Assigned (count) | Exclusions`). The package charter names this deliverable's contribution in its own words: "directed bootstrap progression evidence".

## Deliverable Definition — Ontology

`DEL-10-10` is typed `TEST_SUITE` at Context Envelope `M` with `PhaseHint`
`P1`. Its `AnticipatedArtifacts` cell names **one** artifact with six
enumerated facets, and its `ContextEnvelopeNotes` cell directs "keep one
cohesive validation record". The output of this contract is bounded by that
naming: exactly one progression record, whose facets are components of it and
not separate deliverable outputs.

- **OUT-001** — One bootstrap progression record for PEC v2's own build, maintained as a standing validation: it evidences ingestion of PEC's accepted full dependency DAG as the initial file-native coordination state; capability cutovers taken only after predecessor acceptance; observed coordination friction; proposed, rejected, and unnecessary functions; the file-native fallback's continued operability; and the routes taken from observations to human-gated decisions or amendments. The record's **declared maintenance-and-rerun statement** — the readable part of the record in which it states where it lives, what appends to it, and at what occasions it is re-run (REQ-008) — is a component of this output rather than a second artifact, so the register's naming of one cohesive record is preserved.

### Identity of record

- **CLM-007** — `DEL-10-10` is named "Directed bootstrap self-ingest validation", Type `TEST_SUITE`, Context Envelope `M`, `PhaseHint` `P1`, `ResponsibleParty` `TBD`, `CoversScopeItems` `SOW-064`, `SupportsObjectives` `OBJ-006`. Its `Deliverables.csv` row reads in full, under the column order `DeliverableID,PackageID,Name,Description,Type,ResponsibleParty,AnticipatedArtifacts,CoversScopeItems,SupportsObjectives,ContextEnvelope,ContextEnvelopeNotes,PhaseHint`:

> `DEL-10-10,PKG-10,Directed bootstrap self-ingest validation,"Introduced in P1 and used as a standing validation thereafter. Maintain one bootstrap progression record showing ingestion of PEC's accepted full dependency DAG, capability cutovers only after predecessor acceptance, observed coordination friction, proposed/rejected/unnecessary functions, fallback operation, and routes to human-gated decisions or amendments.",TEST_SUITE,TBD,"Bootstrap progression record: DAG ingestion; capability cutovers; observed friction; proposed, rejected, and unnecessary functions; fallback evidence; amendment routes",SOW-064,OBJ-006,M,"M because the standing progression evidence spans the full DAG, capability cutovers, negative function dispositions, fallback proof, and human-gated amendment routes; keep one cohesive validation record",P1`
>
> (ID-shaped text inside this quotation is upstream source context, not a local
> definition or reference.)

  The `SOFTWARE_DECOMP.md` §5 `PKG-10` table row carries the compact control fields: "| DEL-10-10 | Directed bootstrap self-ingest validation | TEST_SUITE | M | P1 | SOW-064 |". Two features of the register row shape this contract. First, the `Type` cell says `TEST_SUITE` while the `AnticipatedArtifacts` cell names a *record*; the register carries both and this contract honours both — the artifact is a record and the obligation on it is a re-runnable assertion (REQ-007), not a one-time write. Second, the `ContextEnvelopeNotes` cell gives the `M` envelope its reason and then issues a direction — "keep one cohesive validation record" — which REQ-009 states as a checkable obligation.
- **CLM-008** — `DEL-10-10` is named in constraint row `C-08` `STANDING_NODES` of the accepted gate exhibit. The row reads in full, under the exhibit's constraint-register columns `ConstraintID,Kind,Parties,Provenance,Statement,Notes`:

> `C-08,STANDING_NODES,"DEL-01-05, DEL-03-04, DEL-10-02, DEL-10-03, DEL-10-10","Own text: ""Automated assertion"" / ""Permanent"" / ""Runs at every release"" / ""tested property"" / ""standing validation""",Standing obligations: excluded from one-shot COMPLETE/UNBLOCKED arithmetic; they gate releases not successors,R3-F9; owner confirmation requested. DEL-10-10 is the bootstrap progression record itself`
>
> (`execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` §4,
> constraint register. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference.)

  The exhibit's §4 node-class preamble states the same classification and its status: "**Node classes:** `STANDING` (excluded from one-shot COMPLETE/UNBLOCKED arithmetic; gate releases, not successors — pending owner confirmation, constraint C-08): DEL-01-05, DEL-03-04, DEL-10-02, DEL-10-03, DEL-10-10. All others `COMPLETABLE`." At `D-PEC-62` §1(4) the owner accepted the DAG candidate v0.2 "**accepted, all strata as presented**", and that packet states its own reading of that acceptance in one sentence, quoted here whole: "This packet reads "as presented" as accepting the exhibit **flags as flags** — E-A11 (AMBIGUOUS_BASIS), E-P69/E-N02 (PHASE_TENSION), E-N13/E-N18 (LOW_CONFIDENCE), C-02 direction, C-08 standing-node set remain recorded-but-unresolved, non-gating annotations; each flag is carried verbatim into the seeded rows' `Notes`." What is settled is therefore the arithmetic exclusion — `C-08` is a non-gating constraint row and this deliverable is excluded from one-shot `COMPLETE`/`UNBLOCKED` counting. What is not settled is the classification's force as a release gate; the row's own `Notes` field says "owner confirmation requested" (CON-001). The deliverable-local `_DEPENDENCIES.md` compresses this to "(owner-confirmed at D-PEC-62 ruling)"; that phrase is accurate as to the arithmetic exclusion and overstates the rest, and this contract cites the `D-PEC-62` text over the local paraphrase. The `Provenance` cell's evidence phrase for this member is "standing validation", which is this deliverable's own `Description` wording; the `Notes` sentence "DEL-10-10 is the bootstrap progression record itself" is the register's own statement that the standing obligation and its artifact are the same object (CON-002).

### Placement in the work graph

- **CLM-009** — This deliverable's `Dependencies.csv` (`RegisterSchemaVersion` `v3.1`) holds exactly four rows: two `ANCHOR` rows and two `EXECUTION` upstream rows. The anchors are `DEP-10-10-001` (`AnchorType` `IMPLEMENTS_NODE`, `TargetRefID` `PKG-10`, `Statement` "DEL-10-10 is package-local to PKG-10.", `SatisfactionStatus` `SATISFIED`) and `DEP-10-10-002` (`AnchorType` `TRACES_TO_REQUIREMENT`, `TargetRefID` `SOW-064`, `Statement` "DEL-10-10 covers scope item SOW-064.", `SatisfactionStatus` `SATISFIED`). The two `EXECUTION` rows are `UPSTREAM` `PREREQUISITE` edges at `RequiredMaturity` `INITIALIZED`, `ProposedMaturity` `TBD`, `SatisfactionStatus` `PENDING`, `Confidence` `MEDIUM`, `Explicitness` `IMPLICIT`, `Origin` `EXTRACTED`, `Status` `ACTIVE`, `FirstSeen` and `LastSeen` `2026-07-25`, `EvidenceFile` `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md`, attributed by column below:

  | Register row | `TargetPackageID` / `TargetDeliverableID` | `Statement` | `SourceRef` and `EvidenceQuote` | `Notes` |
  |---|---|---|---|---|
  | `DEP-10-10-003` | `PKG-02` / `DEL-02-05` | "The DAG's file form is read by the dependency register parser" | `SOW-064: P1 "ingests PEC v2's accepted full dependency DAG"; SOW-015: dependency registers into DependencyEdge` | "PROPOSAL; Flag=none; EdgeID=E-P73" |
  | `DEP-10-10-004` | `PKG-03` / `DEL-03-01` | "Self-ingest runs through the reconciler" | "SOW-064 (as E-P73)" | "PROPOSAL; Flag=none; EdgeID=E-P74" |

  In both rows the `SourceRef` and `EvidenceQuote` columns carry the same value; the `Statement` column is the edge's own assertion and is not an evidence quotation. The gate exhibit's edge-register rows for the same two edges, under its columns `EdgeID,PredecessorID,SuccessorID,Stratum,EdgeKind,Flag,BasisCitation,Rationale`, read `E-P73,DEL-02-05,DEL-10-10,PROPOSAL,CONSUMES,,"SOW-064: P1 ""ingests PEC v2's accepted full dependency DAG""; SOW-015: dependency registers into DependencyEdge",The DAG's file form is read by the dependency register parser` and `E-P74,DEL-03-01,DEL-10-10,PROPOSAL,CONSUMES,,SOW-064 (as E-P73),Self-ingest runs through the reconciler`, with `Flag` empty in both. The `"(as E-P73)"` shorthand on `E-P74` is a back-reference to the sibling edge whose basis citation carries the `SOW-064` text.
- **CLM-010** — Both predecessors are at lifecycle state `INITIALIZED`, which is the maturity both edges require. `INITIALIZED` means each upstream **contract** is the reliable input: each accepted `ScopeOfWork.md` exists, and no parser, no reconciler, no store, and no rebuilt record tier does. Nothing in this contract asserts that any upstream artifact exists or has been built. From `[E-P73]`, the reading of the DAG's file form is `DEL-02-05`'s obligation, quoted here:

> - **OUT-001** — A dependency register parser in the PEC service core: it
>   reads `Dependencies.csv` registers and `WORK_GRAPH.json` files in the
>   checkouts it is pointed at, parses each under a declared grammar, and emits
>   DependencyEdge records carrying citation provenance to their live sources.
> - **REQ-001** — The parser shall read `Dependencies.csv` registers and
>   `WORK_GRAPH.json` files in the checkouts it is pointed at, and shall emit
>   from them DependencyEdge records, per the `SOW-015` statement (CLM-001), the
>   register `Description` (CLM-004), and the `PRD.md` §7.1 DependencyEdge
>   source cell (CLM-002). Both named file forms are in scope; neither may be
>   dropped in favour of the other (CLM-006).
> - **REQ-006** — Where a register or work-graph file is absent, unreadable,
>   malformed, or carries a shape the declared grammar does not recognize, the
>   parser shall report that condition explicitly to its caller, naming the file
>   and the fault; a silently dropped, empty, partial, or defaulted record is
>   prohibited, per `PEC-ORI-006` ... Because registers are deliverable-local
>   and a full accounting is assembled by querying many of them (CLM-013), the
>   coverage of a read — which register locations were examined and which were
>   not — shall itself be reportable. ...
>
> (`DEL-02-05/ScopeOfWork.md`, Ontology and Epistemology sections; `OUT-001` and
> `REQ-001` quoted in full, `REQ-006` elided at its two ellipses. ID-shaped text
> inside this quotation is upstream source context, not a local definition or
> reference — this contract's own `REQ-*` and `AC-*` records are separate and
> differently worded.)

  That contract also records this deliverable as one of its two declared downstream consumers, carrying `[E-P73]`'s basis citation and rationale; the relation is informational there and imposes no obligation on `DEL-02-05` beyond the outputs it declares. What this contract binds to is the obligation that the DAG's file form is readable and that coverage and faults are reportable — not that a parser exists (REQ-012).
- **CLM-011** — From `[E-P74]`, the reconciliation through which self-ingestion runs is `DEL-03-01`'s obligation, quoted here:

> - **OUT-001** — A full-rebuild reconciler entry point in the PEC service
>   core: one command that rebuilds the record tier in full from file sources
>   for the loops the registry names, writing only into the store and into the
>   generated views it declares. The entry point's **declared-view record** —
>   the readable artifact in which it declares every generated view it writes
>   (REQ-006) — is a component of this output rather than a third artifact: it
>   is the entry point's own self-declaration, so the register's
>   `AnticipatedArtifacts` naming of exactly two artifacts is preserved.
> - **REQ-001** — The reconciler shall expose a single command that rebuilds the
>   record tier in full from file sources for every loop the registry names, per
>   `SOW-010` (CLM-001) and `PEC-RCN-001` (CLM-003). A rebuild shall require no
>   operator step, repair action, or manual sequence beyond that one invocation.
> - **REQ-009** — Where an upstream unit reports that a feed is absent,
>   unreadable, malformed, stale, or grammar-unrecognized, the rebuild shall
>   carry that limitation through to its result, naming the loop and the feed,
>   and shall never present a rebuild that could not read a feed as a rebuild
>   that read it. Silent omission is prohibited, per `PEC-ORI-006` ("Where a
>   feed is unparseable or stale, the response shall state the measurement
>   limitation explicitly; silent omission is prohibited"). Rendering such a
>   limitation into an orientation response is `DEL-04-05`'s act under `SOW-009`
>   (CLM-019); this deliverable makes the limitation available to that consumer.
>
> (`DEL-03-01/ScopeOfWork.md`, Ontology and Epistemology sections; all three
> records quoted in full, none elided. ID-shaped text inside this quotation is
> upstream source context, not a local definition or reference.)

- **CLM-012** — The `DEL-03-01` contract carries two conditions on what a rebuild delivers, and this contract carries them forward rather than smoothing them, because the progression record's DAG-ingestion evidence is evidence *about* that rebuild. The first is the "in full" question, quoted in full:

> - **CON-005** — `SOW-010` requires the record tier be rebuildable "in full",
>   while every upstream feed unit is contractually obliged to report feeds it
>   could not read as explicit limitations (CLM-016), and `PEC-ORI-006`
>   prohibits silent omission. No accepted source states whether a rebuild that
>   completed with stated coverage limitations counts as a full rebuild for
>   `SOW-010`'s purposes, or whether "in full" is a claim about the command's
>   reach rather than its coverage. This contract takes neither reading as
>   settled: REQ-001 obliges the command to reach every registered loop and
>   every manifest-named feed, and REQ-009 obliges every gap to be carried
>   through as a stated limitation, so that the question is visible in the
>   result rather than answered by silence. `PRD.md` §12's `P1` exit test names
>   "rebuild-from-scratch ≤ bound" without stating the bound, which
>   `PEC-SVC-003` records as "confirmed at Phase 1"; that measurement is
>   `DEL-03-06`'s under `SOW-054` (CLM-019) and this contract asserts no bound.
>
> (`DEL-03-01/ScopeOfWork.md`, Epistemology section; quoted in full, not elided.
> ID-shaped text inside this quotation is upstream source context, not a local
> definition or reference.)

  The second is an instance-level gap in the same contract's generated-views permission, quoted at its two governing sentences with the remainder of each paragraph elided:

> - **CON-001** — `SOW-021`'s second limb permits writes to "generated views",
>   and the gap this contract carries is **instance-level, not class-level**. ...
>
>   What no accepted source states is **which** views this reconciler generates
>   and **where they live**. ...
>
> (`DEL-03-01/ScopeOfWork.md`, Epistemology section, `CON-001`; elided after the
> first sentence of its first paragraph and after the first sentence of its
> second paragraph. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference.)

  Neither condition is this deliverable's to resolve, and neither may be reported away. A progression record that described the self-ingestion as a completed full rebuild without carrying the limitations the upstream contract obliges the rebuild to report would be asserting more than the accepted sources support (REQ-012, CON-004).
- **CLM-013** — `DEL-02-05`'s contract records a corpus observation about the loop this deliverable's self-ingestion first meets. It is that contract's observation, recorded in its voice and cited here as such — not a claim of this contract and not a specification for anything:

> - **CON-004** — The corpus this parser is first expected to meet holds only
>   half of its feed. `OI-010`, resolved at Gate 2 (2026-07-24), records that
>   "the §12 closing paragraph governs — the first loop the P1 reconciler
>   ingests is PEC v2's own build (bootstrap as thesis validation) ...", and the
>   `projects/pec` tree contains 64 `Dependencies.csv` registers and **zero**
>   `WORK_GRAPH.json` files today (CLM-016). This is recorded as a stated
>   condition, not a defect and not a licence to widen the read scope: the
>   parser's coverage of a loop with no work graph is a limitation to be stated
>   under REQ-006, and dropping the `WORK_GRAPH.json` form because the first
>   loop lacks it is prohibited by REQ-001 and by the `DL-9` correction the
>   `SOW-015` note carries (CLM-006).
>
> (`DEL-02-05/ScopeOfWork.md`, Epistemology section; quoted in full, with no
> elision by this contract — the ellipsis inside it is the upstream contract's
> own elision of the `OI-010` text it quotes. ID-shaped text inside this
> quotation is upstream source context, not a local definition or reference.)

  The same contract's `CLM-016` records that census as "Observed corpus condition, recorded as observation and not as specification". This contract cites it because it conditions what DAG-ingestion evidence can honestly show for the `pec` loop, and for no other purpose (CON-005).
- **CLM-014** — No accepted edge names a consumer of this deliverable. Its `Dependencies.csv` holds only the two anchors and the two upstream rows (CLM-009); the gate exhibit's edge register contains no row in which `DEL-10-10` is the `PredecessorID`; and a search of every `Dependencies.csv` in this project finds `DEL-10-10` named only in its own register. The two upstream contracts each record this deliverable in their `_DEPENDENCIES.md` downstream tables as informational — "DEL-10-10 (Directed bootstrap self-ingest validation) — CONSUMES [E-P73]" and "DEL-10-10 (Directed bootstrap self-ingest validation) — CONSUMES [E-P74]" — and neither table is a register edge. This zero-consumer shape is what `C-08` describes: standing obligations "gate releases not successors" (CLM-008).
- **CLM-015** — Phase staging, checked against the `PhaseHint` column of `Deliverables.csv` for every deliverable this contract names in its own voice. Twelve are `P1`: `DEL-10-10` itself, its upstreams `DEL-02-05` and `DEL-03-01`, the sibling standing nodes `DEL-01-05`, `DEL-03-04`, `DEL-10-02`, and `DEL-10-03`, and the neighbours `DEL-01-04`, `DEL-03-02`, `DEL-03-03`, `DEL-03-06`, and `DEL-10-11`. Five exceptions are named, each cited only as a co-member of `OBJ-006`'s mapped set or as the owner of scope this deliverable does not touch: `DEL-10-01` is `pre-P1`; `DEL-10-04` and `DEL-10-05` are `P2`; `DEL-10-09` and `DEL-10-12` are `P3`. No claim in this contract stages any named deliverable into a different phase.

### Boundaries

- **CLM-016** — The `SOW-064` `Notes` cell carries three constraints in the register's own voice, and all three bind this contract: "observations grant no authority or scope, the file-native fallback remains operable, and generality is validated against a structurally different loop". The first is a governing value, not a caveat: the record's observations feed human-gated decisions or amendments and never self-authorize (AX-002, REQ-006). The second is a continuing condition the record must evidence rather than assume (REQ-005). The third bounds what self-ingestion alone can be said to demonstrate (REQ-010, TBD-005). The `PRD.md` §12 text and `D-PEC-61` item 1 state the same three in their own words (CLM-002, CLM-003), and `C16` states the first and second again as a hard constraint (CLM-004).
- **CLM-017** — The ledger row's `DecisionRef` cell reads "DL-10; DL-11; SCA-001". These are the ledger's own cross-references to decision-log entries and a scope-change session, not register edges and not dependencies. `DL-10` (2026-07-24) records the owner's Gate 2 resolution of `OI-010` and `OI-011`, whose Rationale cell quotes the Gate 2 confirmation "…based on acceptance of your recommendations for OI-010 and OI-011". `DL-11` (2026-07-24) records the Phase 4 forced boundary assignment for this scope item; quoting the clause that bears on it, with the preceding clauses elided: "Phase 4 forced boundary assignments: ... SOW-064 (bootstrap) → PKG-10 as a validation act, not a reconciler feature", with the Rationale cell recording "Each was assignable to two domains; ledger rows carry `DL-11` in DecisionRef." `SCA-001` is the scope-change session opened by `D-PEC-61` and closed at revision 1.1, recorded at `DL-16` (CLM-003, and the Purpose section above). `DL-11`'s "not a reconciler feature" is the accepted statement of this deliverable's boundary with `DEL-03-01` (REQ-011).
- **CLM-018** — The acts adjacent to this validation are owned elsewhere and are cited here, never discharged. Reading the DAG's file form — parsing `Dependencies.csv` registers and `WORK_GRAPH.json` under a declared grammar and emitting DependencyEdge records — is `DEL-02-05` (`SOW-015`, CLM-010). The one-command full rebuild through which self-ingestion runs is `DEL-03-01` (`SOW-010`, `SOW-021`, CLM-011). Incremental reconcile keyed on Git delta is `DEL-03-02` (`SOW-018`), and drift classification between successive snapshots is `DEL-03-03` (`SOW-019`). The standing kill test is `DEL-10-02` (`SOW-055`); the tested no-ruling-write property of the API surface is `DEL-10-03` (`SOW-025`); standing zero-dependency and locality enforcement is `DEL-01-05` (`SOW-052`, `SOW-053`); harness parity diffing is `DEL-03-04` (`SOW-020`) and the parity metric is `DEL-10-11` (`SOW-093`); rebuild performance bounds are `DEL-03-06` (`SOW-054`); the Step-0 cost baseline is `DEL-10-01` (`SOW-058`); self-observability logging is `DEL-01-04` (`SOW-057`). Materializing the dependency DAG, computing blocker state, and scaffolding are `PROJECT_SETUP`'s acts under `D-PEC-62`, not this deliverable's. Amending decomposition truth is the scope-change workflow's. This contract produces only the progression record.
- **CLM-019** — "Capability cutovers only after predecessor acceptance" is a property this record **evidences**; it is not a scheduling or sequencing authority this deliverable holds. The rule's own source states it as a constraint on the build (`C16`: "later nodes consume only PEC capabilities produced and accepted by predecessor nodes; no node depends on the capability it creates"), and the deliverable's `Description` states this deliverable's part as "showing" it. The deliverable-local `_DEPENDENCIES.md` states the same posture for the register from which cutover order is read: mode `FULL_GRAPH`, `RequiredMaturity` `INITIALIZED`, and "Blocker output is advisory visibility only — never work assignment." A record that assigned, sequenced, authorized, or withheld a cutover would be exercising an authority no accepted source grants it (REQ-006, REQ-011, AX-002).
- **CLM-020** — The deliverable is at lifecycle state `INITIALIZED` with no implementation present. Every requirement, acceptance criterion, and verification method below states a contract on future production; none asserts that a record, an entry, a check, or a mechanism exists.

- **TBD-001** — `ResponsibleParty` is unassigned; the register records `TBD`, with assignment at WORKING_ITEMS activation and not in this contract (`SOFTWARE_DECOMP.md` §5 preamble; `_CONTEXT.md`).
- **TBD-002** — What mechanism runs this standing validation — what re-runs it, on what occasions, and whether re-running is an automated check, a governed workflow act, or a human review pass — is fixed by no accepted source. `C-08` says standing nodes "gate releases", and the `Type` cell says `TEST_SUITE`, but neither states a runner. It is chosen during production within REQ-007 and REQ-008 and is part of CON-002; this contract does not choose it.
- **TBD-003** — Where the progression record lives — its path, its format, and whether it is one file or a directory of dated entries — is fixed by no accepted source. `AnticipatedArtifacts` names the record and its facets and no location; `ContextEnvelopeNotes` requires cohesion, not a filename. It is chosen during production within REQ-008 and REQ-009.
- **TBD-004** — What constitutes "acceptance" of a predecessor for the purposes of a capability cutover is fixed by no accepted source at this deliverable's level. `_DEPENDENCIES.md` records the Phase 1.3 owner-ruled dependency maturity threshold `INITIALIZED` for blocker computation, and `_STATUS.md` is the sole lifecycle authority; whether a cutover's evidence cites a lifecycle state, a review outcome, an owner ruling, or several is a production choice bounded by REQ-002. Nothing in this contract settles it, and no choice made under it may function as an authority over cutover order (CLM-019).
- **TBD-005** — The "structurally different loop" against which generality is validated after self-ingestion is named by no accepted source. `SOW-064`'s `Notes`, `PRD.md` §12, `D-PEC-61` item 1, and `C16` each state the obligation without naming a loop. REQ-010 obliges the record to carry the obligation and its unmet-or-met state; selecting the loop is not a production choice this contract authorizes.

## Completion and Reliance Basis — Epistemology

The requirements below state what future production must satisfy. Nothing in
this section asserts that a record, a progression entry, a check, or a runner
exists. They are written as obligations on a *continuing* validation —
informed by, not derived from, the `C-08` annotation (CLM-008, CON-001) — so
that no single passing state can be presented as the deliverable's completion.

- **REQ-001** — The record shall evidence that PEC's accepted full dependency DAG was ingested as P1's initial file-native coordination state, identifying the accepted DAG basis ingested, the loop it describes, and the point in the progression at which the ingestion occurred, per `SOW-064` (CLM-001), `PRD.md` §12 (CLM-002), and `C16` (CLM-004).
- **REQ-002** — The record shall evidence, for each capability cutover in the progression, that the consuming node consumed only PEC capabilities already produced and **accepted** by predecessor nodes, and that no node depended on the capability it was creating, per `C16` and `PRD.md` §12. Each cutover entry shall identify the capability, the predecessor whose acceptance it relied on, and the evidence of that acceptance (TBD-004). The record evidences this property; it does not schedule, authorize, or withhold a cutover (CLM-019, REQ-011).
- **REQ-003** — The record shall capture coordination friction observed during the progression, each observation attributed to the occasion on which it was observed and to the evidence that supports it, per `SOW-064` ("observed coordination friction is captured as evidence") and `PRD.md` §12 ("Coordination friction observed during this progression may produce evidence-linked candidate functions, boundary decisions, and scope-change requests").
- **REQ-004** — The record shall carry the **negative** dispositions as first-class content: functions proposed, functions rejected, and functions found unnecessary, each with the disposition and the basis for it. A disposition once recorded shall not be pruned from the record because it did not lead to work; the `AnticipatedArtifacts` cell names "proposed, rejected, and unnecessary functions" as facets of the record, and the `ContextEnvelopeNotes` cell names "negative function dispositions" among the reasons the envelope is `M` (CLM-007).
- **REQ-005** — The record shall evidence that the file-native fallback remained operable throughout the progression — that governed work proceeded without requiring a PEC read or write — per `SOW-064`'s `Notes` ("the file-native fallback remains operable"), `C16`, and `PEC-K-01` ("No governed act may require a PEC read or write. Deleting PEC blocks nothing."). Operability shall be evidenced at the occasions the record covers rather than asserted once.
- **REQ-006** — For every observation the record carries that led anywhere, the record shall state the route it took — to a candidate function, a boundary decision, a scope-change request, or a human-gated decision or amendment — and the state of that route. The record shall state no observation as authorizing, granting, or changing anything: per `SOW-064`'s `Notes` "observations grant no authority or scope", and per `PRD.md` §12, friction "grants no authority and changes no accepted scope without human approval" (AX-002).
- **REQ-007** — The record shall be a standing validation with no terminal state: it shall remain re-runnable and appendable for as long as the progression continues, and each entry shall be evidence for the progression state it observed and for no later state. No entry, no passing check, and no completed facet shall be expressible as completion of this deliverable, per the `Description` ("Introduced in P1 and used as a standing validation thereafter") and `C-08` (CLM-008).
- **REQ-008** — The record shall carry a declared maintenance-and-rerun statement — a readable component of OUT-001 — stating where the record lives, what appends to it, and at what occasions it is re-run. This requirement obliges the declaration; it does not choose the runner, the occasions, or the location, which are TBD-002 and TBD-003 and are production choices bounded by this requirement and by CON-002.
- **REQ-009** — The record shall be **one** cohesive validation record. The six facets named in `AnticipatedArtifacts` — DAG ingestion, capability cutovers, observed friction, proposed/rejected/unnecessary functions, fallback evidence, and amendment routes — shall be components of that one record and shall not be delivered as separate artifacts, per the `ContextEnvelopeNotes` direction "keep one cohesive validation record" (CLM-007).
- **REQ-010** — The record shall carry the generality obligation and its state: that generality is validated against a structurally different loop after self-ingestion, that the loop is named by no accepted source (TBD-005), and whether that validation has occurred. The record shall not present self-ingestion evidence as generality evidence, per `SOW-064`'s `Notes`, `PRD.md` §12, and `D-PEC-61` item 1.
- **REQ-011** — This deliverable shall perform no act owned by another deliverable or workflow. In particular it shall define no register or work-graph grammar and parse no dependency register or work graph itself (`DEL-02-05`); it shall implement no rebuild, no incremental reconcile, no drift classification, and no parity diff (`DEL-03-01`, `DEL-03-02`, `DEL-03-03`, `DEL-03-04`); it shall run no kill test (`DEL-10-02`) and no no-ruling-write verification (`DEL-10-03`); it shall assert no rebuild bound (`DEL-03-06`); it shall materialize no dependency edge, compute no blocker state, and scaffold nothing (`PROJECT_SETUP` under `D-PEC-62`); and it shall create, modify, or delete no register, decomposition, ledger, decision, or lifecycle file (CLM-018). `DL-11` states the boundary in the accepted record's own words: this scope item is "a validation act, not a reconciler feature" (CLM-017).
- **REQ-012** — The record shall bind to upstream **contracts**, not upstream artifacts, and shall assert nothing about upstream implementation state (CLM-010, CLM-011). Where an upstream contract conditions what it delivers, the record shall carry that conditioning rather than smooth it: it shall not present a rebuild that carried stated coverage limitations as an unqualified full rebuild (`DEL-03-01`/CON-005), and it shall not treat the instance set of generated views as settled (`DEL-03-01`/CON-001). Where an upstream unit reports a feed as absent, unreadable, malformed, stale, or grammar-unrecognized, the record shall carry that report as part of its DAG-ingestion evidence (CLM-012, CON-004).
- **REQ-013** — The validation shall be designed to block: for a release candidate on which the progression evidence required by REQ-001 through REQ-006 is absent, or on which the standing assertion fails, the mechanism shall return an explicit blocking verdict rather than a pass, a skip, or an absent result. This requirement binds the mechanism's design intent and the verdict it produces. It does not, by itself, establish that a blocking verdict binds a release: whether this validation carries release-gating authority follows the pending `C-08` confirmation recorded at CON-001 and is routed to the owner at AC-015.
- **REQ-014** — Checks and tests shall implement the verification methods declared in this contract; they shall not define scope, requirements, or acceptance criteria.

- **AC-001** — The record identifies the accepted dependency-DAG basis it ingested, the loop that DAG describes, and where in the progression the ingestion occurred, and each is resolvable to its live source.
- **AC-002** — Every capability cutover in the record names the capability, the predecessor whose acceptance it relied on, and that acceptance's evidence; no cutover entry relies on a capability its own node was creating; and the record contains no cutover authorization, assignment, sequencing instruction, or withholding.
- **AC-003** — Every friction observation in the record is attributed to the occasion observed and to supporting evidence, and no observation is recorded without both.
- **AC-004** — The record contains proposed, rejected, and unnecessary function dispositions with their bases; removing a disposition because it produced no work is detectable as a gap against the record's own prior state.
- **AC-005** — For the occasions the record covers, it evidences that governed work proceeded without requiring a PEC read or write, rather than asserting fallback operability once and generally.
- **AC-006** — Every observation that led anywhere carries its route and that route's state; and no statement in the record presents an observation as granting authority, expanding scope, or changing accepted state.
- **AC-007** — The record has no terminal or "complete" state: it remains appendable and re-runnable, each entry is scoped to the progression state it observed, and no entry or check result is expressible as completion of this deliverable.
- **AC-008** — The record carries its declared maintenance-and-rerun statement as a component, naming where it lives, what appends to it, and at what occasions it is re-run; and that statement matches the record's actual location and maintenance.
- **AC-009** — All six named facets are present within one cohesive record; no facet is delivered as a separate artifact.
- **AC-010** — The record states the generality obligation, states that the structurally different loop is named by no accepted source, and states whether validation against such a loop has occurred; and no part of the record presents self-ingestion evidence as generality evidence.
- **AC-011** — Inspection finds no grammar definition, register or work-graph parsing, rebuild, reconcile, drift-classification, parity-diff, kill-test, no-ruling-write, rebuild-bound, edge-materialization, blocker-computation, or scaffolding act performed by this deliverable, and no write by it to any register, decomposition, ledger, decision, or lifecycle file.
- **AC-012** — No element of the record asserts or requires that an upstream parser, reconciler, store, or rebuilt record tier exists; the record carries the upstream "in full" conditioning and the unsettled generated-view instance set as the upstream contracts state them; and any upstream-reported feed limitation appears in the DAG-ingestion evidence.
- **AC-013** — For a release candidate on which the required progression evidence is absent, and for one on which the standing assertion fails, the mechanism returns an explicit blocking verdict rather than a pass, a skip, or an absent result.
- **AC-014** — Each of VER-001 through VER-013 has a corresponding executed check recorded against the record, and no check asserts a criterion absent from this contract.
- **AC-015** — An accountable owner confirms, or declines to confirm, that the validation delivered under this contract carries release-gating authority — that its blocking verdict blocks a release candidate — given that `C-08`'s standing-node classification carries "owner confirmation requested" in its own `Notes` and was accepted at `D-PEC-62` §1(4) as a recorded-but-unresolved, non-gating annotation (CLM-008, CON-001). A decline leaves the mechanism's verdicts advisory and invalidates no other criterion in this contract; the standing framing of the contract stands either way, because it is how the contract is written rather than a claim about the validation's force.
- **AC-016** — The REVIEW gate confirms this contract's traceability to `SOW-064` and `OBJ-006` as a register-direct mapping carried from `SCA-001` and untouched by `SCA-002`; confirms that no `PKG-02`, `PKG-03`, sibling `PKG-10`, or `PROJECT_SETUP` scope has been absorbed; and confirms that the record holds no authority over cutover order, scope, or amendment.

- **CON-001** — Whether this deliverable's validation carries *release-gating authority* is unconfirmed. The `C-08` `STANDING_NODES` row that classifies it records "owner confirmation requested" in its own `Notes`, and `D-PEC-62` §1(4) accepted the standing-node set as a recorded-but-unresolved, non-gating annotation rather than ruling it (CLM-008). The validation this contract requires is designed to block and its verdicts are unambiguous; what is open is whether a blocking verdict binds a release candidate or is advisory. AC-015 routes that question to an accountable owner. This contract neither asserts the authority nor waives it, and no production choice may settle it.
- **CON-002** — The standing obligation and its artifact are the same object, and no accepted source states what runs it. `C-08`'s `Notes` says "DEL-10-10 is the bootstrap progression record itself" (CLM-008); the register types the deliverable `TEST_SUITE` while naming a record as its artifact (CLM-007). A record is a thing that is written; a standing validation is a thing that is re-run. No accepted source states the mechanism that re-runs this one (TBD-002) or where the record lives (TBD-003). This contract records the tension rather than resolving it: REQ-007 binds the standing character, REQ-008 obliges the record to declare its own maintenance and re-run, and REQ-013 binds the verdict's design — so that whatever mechanism production settles on is declared and checkable. Choosing that mechanism is a production decision bounded by those requirements; treating a single written record as discharging the standing obligation would not be.
- **CON-003** — This deliverable observes a progression it is itself part of. `DEL-10-10` is a node of the same accepted DAG whose ingestion it records, and the friction it observes includes friction arising in its own production. No accepted source states how that reflexivity is handled — whether the record's own production is in the progression it records, and if so how an observation about itself is evidenced without becoming self-justifying. `PRD.md` §12 and `SOW-064` bound the consequence rather than the mechanism: an observation grants no authority whatever its subject (REQ-006, AX-002). This contract records the reflexivity and binds its consequence; it does not resolve how the record positions itself in its own account.
- **CON-004** — The evidence this record can honestly show about DAG ingestion is conditioned by an upstream question the upstream contract itself leaves open. `DEL-03-01`/CON-005 records that no accepted source states whether a rebuild completing with stated coverage limitations counts as a rebuild "in full" (CLM-012). The progression record's DAG-ingestion facet is evidence about exactly such a rebuild. This contract takes neither reading: REQ-012 obliges the record to carry the limitations and the conditioning as the upstream contract states them, so the question stays visible in the evidence rather than being answered by a phrasing choice in this record. Resolving it is a scope-change question for `SOW-010`, not a production decision here.
- **CON-005** — The self-ingestion corpus is not uniform across the feeds the upstream parser is obliged to read. `DEL-02-05`'s contract records, as its own observation, that the `projects/pec` tree contains 64 `Dependencies.csv` registers and zero `WORK_GRAPH.json` files (CLM-013). This contract neither adopts that census as its own measurement nor treats it as a specification; it records that DAG-ingestion evidence for this loop will meet a corpus whose coverage the upstream contract already obliges it to report as a limitation, and REQ-012 requires that report to appear in the record rather than be absorbed into a clean-looking result. Nothing here widens, narrows, or settles the upstream read scope.

## Production and Verification Method — Praxeology

Production proceeds in the order source and register survey → record shape and
declared maintenance-and-rerun statement → the six facets instantiated against
the progression as it runs → route and disposition capture → standing re-run
and blocking verdict → checks, because the record cannot honestly evidence a
progression it did not observe as it happened, and because the standing
character (REQ-007) makes the maintenance declaration a precondition of the
first entry rather than documentation added after one. The facets are
instantiated within one record from the first entry rather than assembled from
six streams, because REQ-009's cohesion direction is easiest to lose at the
start. All work is bounded to this deliverable folder and the record's declared
location; this contract authorizes no register, decomposition, ledger, PRD,
decision, lifecycle, or upstream-deliverable edit, and it neither defines nor
reshapes the parsers, the rebuild, or the DAG it observes. Checks implement the
verification methods below and create no scope.

- **VER-001** — Resolve the record's stated DAG basis, loop, and ingestion point to their live sources and assert each is locatable; compare the stated basis against the accepted decomposition basis and the accepted gate exhibit and assert the record names what it ingested rather than describing it generically.
- **VER-002** — Cutover exercise: for every cutover entry, assert the named capability, the named predecessor, and the acceptance evidence are present and resolvable; construct the consumption graph the entries describe and assert no entry consumes a capability its own node was creating; and inspect the record for imperative, assigning, sequencing, authorizing, or withholding language about cutovers, asserting none.
- **VER-003** — For every friction observation, assert an attributed occasion and supporting evidence are present and resolvable; sample the progression's occasions and assert no observation is carried without both.
- **VER-004** — Disposition inspection: assert the record carries proposed, rejected, and unnecessary function entries with their bases; compare the record against its own prior state across two maintenance points and assert no disposition was removed for having produced no work.
- **VER-005** — Fallback exercise: for the occasions the record covers, assert the record evidences governed work proceeding without a PEC read or write at those occasions; assert the record carries no single general assertion of fallback operability in place of occasion-level evidence.
- **VER-006** — Route inspection: for every observation that led anywhere, assert a route and a route state are recorded and resolvable; then read the record end to end for any statement presenting an observation as granting authority, expanding scope, or changing accepted state, asserting none.
- **VER-007** — Standing exercise: assert the record exposes no terminal or "complete" state; append a new entry at a later progression state and assert prior entries remain scoped to what they observed; and inspect the record and its declared statement for any expression that would let one entry or one passing result stand as completion of the deliverable.
- **VER-008** — Maintenance-statement exercise: read the declared maintenance-and-rerun statement, assert it names the record's location, what appends to it, and the re-run occasions, and compare each against the record's actual location and observed maintenance, asserting agreement.
- **VER-009** — Cohesion inspection: assert all six named facets are present within one record and that no facet exists as a separate deliverable artifact.
- **VER-010** — Generality inspection: assert the record states the generality obligation, states that no accepted source names the structurally different loop, and states whether that validation has occurred; then read the self-ingestion facets for any claim of generality, asserting none.
- **VER-011** — Boundary inspection: inspect this deliverable's outputs and working surface for grammar definitions, register or work-graph parsing, rebuild, reconcile, drift-classification, parity-diff, kill-test, no-ruling-write, rebuild-bound, edge-materialization, blocker-computation, and scaffolding acts, asserting each absent; and assert no write by this deliverable to any register, decomposition, ledger, decision, or lifecycle file.
- **VER-012** — Upstream-conditioning inspection: read the record for any assertion that an upstream parser, reconciler, store, or rebuilt record tier exists, asserting none; compare the record's characterization of the rebuild against `DEL-03-01`'s CON-005 and CON-001 as quoted in CLM-012 and assert the conditioning is carried, not smoothed; and assert every upstream-reported feed limitation available at the occasion appears in the DAG-ingestion evidence.
- **VER-013** — Blocking-verdict exercise: present a release candidate on which the required progression evidence is absent and one on which the standing assertion fails, and assert in each case an explicit blocking verdict rather than a pass, a skip, or an absent result. Scope boundary: no output of this method may be presented as establishing that the verdict binds a release, which is CON-001 and is routed at AC-015.
- **VER-014** — Run the check set declared for this deliverable and confirm that each of VER-001 through VER-013 has a corresponding executing check and that no check asserts a criterion absent from this contract.

## Governing Values and Decisions — Axiology

- **AX-001** — `OBJ-006` governs: the product thesis remains measurable and falsifiable. `PRD.md` §12 calls this bootstrap "the first validation of the thesis" (CLM-002), which makes the progression record the place where that validation is either evidenced or merely claimed. A record assembled after the fact from what turned out well would still read as a validation and would measure nothing; occasion-level attribution (REQ-003, REQ-005) is what keeps it evidence.
- **AX-002** — Observations grant no authority. This is stated three times in the accepted sources — in `SOW-064`'s `Notes`, in `PRD.md` §12 ("grants no authority and changes no accepted scope without human approval"), and in `C16` ("observed friction routes to evidence-linked candidates and human gates") — and it is the value most at risk in a deliverable whose content is observations about how the work is going. The register that carries cutover order says the same thing from the other side: blocker output is "advisory visibility only — never work assignment" (`_DEPENDENCIES.md`). REQ-006 and REQ-011 make the restraint checkable rather than intentional, and CLM-019 states the consequence for the property this record is most tempted to enforce.
- **AX-003** — The standing shape of this contract is brief-directed contract design, informed by the `C-08` annotation rather than derived from an owner ruling on it (CLM-008, CON-001). It governs how the obligations above are written: treating one written record as completion would convert a continuing validation into a one-shot artifact, which the brief's direction and the deliverable's own `Description` ("used as a standing validation thereafter") both refuse. It is not a claim that the validation has been ruled release-blocking; that question is CON-001, routed at AC-015.
- **AX-004** — `PEC-K-01` graceful absence is the property REQ-005 evidences, and it is the one the bootstrap could quietly erode. If PEC's own build came to depend on PEC, the fallback clause would be false exactly where it is being tested. `SOW-064`'s `Notes` and `C16` both keep the fallback operable as a standing condition of the bootstrap, and `PRD.md` §11's falsification clause depends on it: "PEC is deleted and, by PEC-K-01, nothing breaks."
- **AX-005** — `PEC-K-06` observation-not-participation is this deliverable's operating posture, not a downstream constraint on it: "Read-only over Git; no leases, no claim arbitration, no merge opinions, no dispatch; conflicts surfaced, never prevented." A progression record that surfaced friction is doing its work; one that resolved it would be participating in the coordination it is supposed to observe.
- **AX-006** — Negative dispositions are evidence, not waste. `AnticipatedArtifacts` names "proposed, rejected, and unnecessary functions" and `ContextEnvelopeNotes` counts "negative function dispositions" among the reasons the envelope is `M` (CLM-007). A record that kept only the functions that were built would make the thesis unfalsifiable by construction, because the discarded candidates are the evidence that the friction was assessed rather than converted straight into scope (REQ-004).
- **AX-007** — `DL-11` is the decision that gives this deliverable its shape: `SOW-064` came to `PKG-10` as "a validation act, not a reconciler feature" (CLM-017), and the `PKG-10` charter excludes "The behaviors under test (their home packages)" (CLM-006). Absorbing the parsing (`DEL-02-05`), the rebuild (`DEL-03-01`), the kill test (`DEL-10-02`), or `PROJECT_SETUP`'s materialization and blocker computation would undo that decision. REQ-011 states the boundary as a requirement so that it is checkable.
- **AX-008** — The edges `[E-P73]` (`DEL-02-05` → `DEL-10-10`) and `[E-P74]` (`DEL-03-01` → `DEL-10-10`) are `PROPOSAL` stratum and are accepted: `D-PEC-62` §1(4) records the owner accepting the DAG candidate v0.2 exhibit "accepted, all strata as presented", read in that packet as taking the exhibit's **flags as flags**, so what remains recorded-but-unresolved is the specific annotated set — `E-A11`, `E-P69`/`E-N02`, `E-N13`/`E-N18`, the `C-02` direction, and the `C-08` standing-node set. Of those, only `C-08` touches this deliverable, and it touches its classification rather than either edge; both edges carry an empty `Flag` column in the exhibit (CLM-009). Stratum is provenance, not authority: it records how an edge was derived, not whether it has been accepted, and citation does not convert `PROPOSAL` to `DECLARED`. That this contract's subject matter is the dependency DAG changes nothing about the status of the edges it is placed by.
- **AX-009** — Edge direction is a constraint on this contract, not a licence. `RequiredMaturity` `INITIALIZED` on both edges means each upstream *contract* is the reliable input, not any upstream artifact; this contract is written against the obligations quoted in CLM-010 and CLM-011 and asserts nothing about upstream implementation state. Consuming those contracts imposes no obligation on `DEL-02-05` or `DEL-03-01`, and this deliverable's having no accepted consumer (CLM-014) is the `C-08` shape — it gates releases, not successors — and confers no authority over any deliverable it observes.
- **AX-010** — Unknowns stay marked. TBD-001 through TBD-005 and CON-001 through CON-005 are recorded rather than resolved by inference. `C-04` `PHASE_PRECEDENCE`, `C-08` `STANDING_NODES`, and `C-10` `STRATUM_RULE` are register-wide non-gating constraints recorded in `_DEPENDENCIES.md`, and blocker output under the `FULL_GRAPH` mode at threshold `INITIALIZED` is advisory visibility only, never work assignment.
- **AX-011** — This contract is lifecycle-neutral. `_STATUS.md` remains the sole lifecycle authority and is untouched by this reconciliation; the deliverable is at `INITIALIZED` and nothing has been built.

**Quotation record.** Every quotation in this contract is verbatim from the
named source. Exactly five omissions are made by this contract, each marked with
an ellipsis at the point of omission and enumerated here in full:

1. The `DEL-02-05` `REQ-006` quotation in CLM-010, omitting the text between
   "per `PEC-ORI-006`" and "Because registers are deliverable-local".
2. The same `REQ-006` quotation, omitting the text following "shall itself be
   reportable" to the end of that record.
3. The `DEL-03-01` `CON-001` quotation in CLM-012, omitting the text following
   the first sentence of its first paragraph to the end of that paragraph.
4. The same `CON-001` quotation, omitting the text following the first sentence
   of its second paragraph to the end of that paragraph, and omitting its third
   paragraph entirely.
5. The `DL-11` Decision-cell quotation in CLM-017, omitting the clauses
   preceding the `SOW-064` clause.

Two further ellipses appear in this document and both are the sources' own
rather than this contract's. The first is inside the `DEL-02-05` `CON-004`
quotation in CLM-013: it is the upstream contract's own omission of the
`OI-010` text it quotes, not an omission by this contract, which quotes
`CON-004` in full. The second is the leading ellipsis on the Gate 2
confirmation quoted in CLM-017, which is the `SOFTWARE_DECOMP.md` Gate Log
`DL-10` Rationale cell's own wording, carried verbatim rather than introduced
here. No other quotation in this document omits text from the span it presents.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-064 OBJ-006 | REQ-001, CLM-001, CLM-002, CLM-003, CLM-004 | AC-001 | VER-001 | The record's stated DAG basis, loop, and ingestion point resolved to their live sources, compared against the accepted decomposition basis and gate exhibit |
| OUT-001 | SOW-064 OBJ-006 | REQ-002, CLM-019, TBD-004 | AC-002 | VER-002 | Per-cutover entries naming capability, predecessor, and acceptance evidence; the consumption graph reconstructed from them; and a recorded search finding no authorizing or sequencing language |
| OUT-001 | SOW-064 OBJ-006 | REQ-003, CLM-016 | AC-003 | VER-003 | Friction observations with attributed occasions and resolvable supporting evidence, sampled against the progression's occasions |
| OUT-001 | SOW-064 OBJ-006 | REQ-004, CLM-007, AX-006 | AC-004 | VER-004 | Proposed, rejected, and unnecessary function entries with their bases, plus a two-point comparison of the record against its own prior state showing no disposition removed |
| OUT-001 | SOW-064 OBJ-006 | REQ-005, AX-004 | AC-005 | VER-005 | Occasion-level evidence that governed work proceeded without a PEC read or write, with no general assertion standing in for it |
| OUT-001 | SOW-064 OBJ-006 | REQ-006, CLM-016, CON-003, AX-002, AX-005 | AC-006 | VER-006 | Per-observation route and route state, resolvable, plus a recorded end-to-end read finding no observation presented as granting authority or changing accepted state |
| OUT-001 | SOW-064 OBJ-006 | REQ-007, CLM-020, AX-003 | AC-007 | VER-007 | The record after a later-state append, showing prior entries still scoped to what they observed and no terminal or completion state expressible |
| OUT-001 | SOW-064 OBJ-006 | REQ-008, TBD-002, TBD-003, CON-002 | AC-008 | VER-008 | The declared maintenance-and-rerun statement compared against the record's actual location and observed maintenance |
| OUT-001 | SOW-064 OBJ-006 | REQ-009, CLM-007 | AC-009 | VER-009 | The one record with all six facets present as components, and a check that no facet exists as a separate artifact |
| OUT-001 | SOW-064 OBJ-006 | REQ-010, TBD-005 | AC-010 | VER-010 | The recorded generality obligation, its unnamed-loop statement, its occurrence state, and a recorded read of the self-ingestion facets finding no generality claim |
| OUT-001 | SOW-064 OBJ-006 | REQ-011, CLM-006, CLM-017, CLM-018, AX-007 | AC-011 | VER-011 | Inspection records showing each named adjacent act absent from this deliverable's outputs and working surface, and no write to a register, decomposition, ledger, decision, or lifecycle file |
| OUT-001 | SOW-064 OBJ-006 | REQ-012, CLM-010, CLM-011, CLM-012, CLM-013, CON-004, CON-005, AX-009 | AC-012 | VER-012 | A recorded read finding no upstream-artifact assertion; the record's rebuild characterization compared against the quoted upstream CON records; and the upstream-reported feed limitations located in the DAG-ingestion evidence |
| OUT-001 | SOW-064 OBJ-006 | REQ-013, CLM-008, CON-001 | AC-013 | VER-013 | Per-case blocking verdicts for an evidence-absent and an assertion-failing release candidate, with no pass, skip, or absent result |
| OUT-001 | SOW-064 OBJ-006 | REQ-014, CLM-015 | AC-014 | VER-014 | The declared check-set run mapping each executed check to its verification method, with no criterion asserted that this contract does not state |
| OUT-001 | SOW-064 OBJ-006 | CLM-008, CON-001, AX-003 | AC-015 | HUMAN_REVIEW: accountable owner confirmation or declination that the validation carries release-gating authority, given C-08's "owner confirmation requested" note and D-PEC-62 §1(4)'s acceptance of the standing-node set as a recorded-but-unresolved non-gating annotation | Dated owner ruling recorded against this deliverable, stating whether a blocking verdict blocks a release candidate or is advisory, and leaving the contract's standing framing intact either way |
| OUT-001 | SOW-064 OBJ-006 | CLM-005, CLM-009, CLM-014, AX-001, AX-008, AX-010, AX-011 | AC-016 | HUMAN_REVIEW: REVIEW gate confirms traceability to SOW-064 and OBJ-006 as a register-direct mapping carried from SCA-001 and untouched by SCA-002, confirms no PKG-02, PKG-03, sibling PKG-10, or PROJECT_SETUP scope absorption, and confirms the record holds no authority over cutover order, scope, or amendment | Review record citing the SOW-064 ledger row, the SCA-001 and SCA-002 evidence for the register-direct mapping, the DL-11 boundary decision, and the upstream and sibling deliverable boundaries |
