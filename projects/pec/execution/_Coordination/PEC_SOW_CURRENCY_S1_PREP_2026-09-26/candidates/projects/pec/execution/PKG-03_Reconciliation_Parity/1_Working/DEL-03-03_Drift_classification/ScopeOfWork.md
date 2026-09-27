---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-03-03
package_id: PKG-03
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@189f205ff02df4111b33c20be441ce06e65ada7a
project_scope_refs: [SOW-019]
package_objective_refs: [OBJ-002]
---

# Scope of Work — DEL-03-03 Drift classification

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-03-03` — "Drift
classification" — in `PKG-03` Reconciliation & Parity of the PEC v2 build. It
covers project scope item `SOW-019` in service of package objective `OBJ-002`.
It brings the deliverable's earlier contract (SHA-256 `5ce8ab72425a…eaa7`)
current as a whole; AX-013 records what changed.

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.6** (`current_basis`, SCA-006 successor), accepted by the owner at
SCA-006 checkpoint group 3 on 2026-09-26. The frontmatter pin
`189f205ff02df4111b33c20be441ce06e65ada7a` is the checkpoint-3 acceptance
commit, an ancestor of `origin/main` `125cfacc1`. At the pin
`SOFTWARE_DECOMP.md` has SHA-256 `9374c21fb87b…8eb1`, `Deliverables.csv`
`94ee5d182ae9…9805`, `ScopeLedger.csv` `1d24a4b86f05…916e` and
`ContextBudgetQA.csv` `93b0bb075a0e…4c7c`, the decomposition, ledger and
deliverable values `_Decomposition/_LATEST.md` records, and `docs/PRD.md` v2.4
has SHA-256 `ae49b8065698…3fbe`. This contract was authored against revision
1.2 (SCA-002 successor; accepted 2026-07-25 at `D-PEC-64` closure), kept here
as its dated basis. The deliverable-local `_REFERENCES.md` and `_CONTEXT.md`
carry their own revision pins; this contract asserts nothing about their
present text.

**Observation commit.** The pin binds the accepted decomposition bytes only.
Unless a claim names another commit, every statement below about the state of a
file, record, lifecycle or decision is an observation at `origin/main`
`125cfacc1`. There `SOFTWARE_DECOMP.md`, the three registers and the PRD are
byte-identical to the pin, so every decomposition passage, register cell and
PRD passage quoted below reads the same at both commits.

**Objective warrant.** `CoversScopeItems` is a single row, and its `OBJ-002`
provenance is **register-direct and pre-SCA-002**. It is stated here at the
strength its own record carries, and no further.

Three independent parts of the SCA-002 record agree. First, the scope-change
packet's action `A001` — the action that populated empty `ObjectiveIDs` cells —
enumerates the twenty `IN` rows it targeted:

> `SOW-001, 003, 011..017, 021, 025, 040, 042, 052, 053, 054, 056, 088, 089, 094`
>
> (`Brief.md`, action-register row `A001`, target cell description. ID-shaped
> text inside this quotation is upstream source context, not a local definition
> or reference.)

`SOW-019` is not among them, and the same action's validation record states
that its candidate set was rows whose `ObjectiveIDs` cell was empty —
"31 `IN` rows have empty `ObjectiveIDs`" (`Brief.md`, `A001` validation row).
`SOW-019`'s cell was not empty, so `A001` did not write it.

Second, the §3 objective row confirms the same from the other side. The
recorded old and new text of the `OBJ-002` "Mapped Scope Items" and
"MappedDeliverables" cells reads

> ```
> OLD col4: SOW-006, SOW-018, SOW-019; supported by SOW-005
> NEW col4: SOW-001, SOW-006, SOW-011..019; supported by SOW-005
> OLD col5: DEL-03-02, DEL-03-03, DEL-04-02, DEL-04-03
> NEW col5: DEL-01-01, DEL-02-01..07, DEL-03-02, DEL-03-03, DEL-04-02, DEL-04-03
> ```
>
> (`Amendment_Preview.md`, action `A003b`, "Line 321 · `OBJ-002`". ID-shaped
> text inside this quotation is upstream source context, not a local definition
> or reference.)

Both legs of this deliverable's mapping stand unchanged across the amendment:
the scope item was already named on the old side and remains inside the new
side's compressed range, and the deliverable was already named on the old side.

Third, the SCA-002 record measures the strength of that pre-existing mapping,
in a table whose columns are `Precedent | Mapping | Status`:

> | `SOW-018`, `SOW-019` (PEC-RCN-003/004) | `OBJ-002` | **Valid** — OBJ-002's register locus is the reconciler layer |
>
> (`Amendment_Preview.md`, "Register precedents (measured) — and one I
> withdraw". ID-shaped text inside this quotation is upstream source context,
> not a local definition or reference.)

The mapping is therefore **register-direct and independently measured Valid**
rather than ruled, drafted, or confidence-labelled, and it is neither pending
nor SCA-002-authored. This contract creates no owner-confirmation acceptance
criterion for it, supplies no fresh derivation of it, and asserts no confidence
label, because the record — which assigns graded confidence labels to the nine
per-row attributions it derived — assigns none here: this row was never one of
the rows it derived.

- **CLM-001** — The accepted `ScopeLedger.csv` row for `SOW-019` reads in full, with its trailing fields as they stand (columns `ScopeItemID,InOutStatus,ScopeItemStatement,SourceRef,PackageID,DeliverableIDs,ObjectiveIDs,DecisionRef,OpenIssue,Notes`):

> `SOW-019,IN,Classify and report drift between successive snapshots; never modify a source file,PEC-RCN-004,PKG-03,DEL-03-03,OBJ-002,,FALSE,`
>
> (`DecisionRef` empty; `OpenIssue` `FALSE`; `Notes` empty — no boundary
> decision, no open issue, and no invariant note rides this scope item, unlike
> its `PKG-03` neighbours `SOW-010` (`DL-11`, "Carries PEC-K-02/-05") and
> `SOW-020` ("Permanent (C10)"). ID-shaped text inside this quotation is
> upstream source context, not a local definition or reference.)

  The `SOFTWARE_DECOMP.md` §2 SSOW row for the same item repeats the statement without the register-only columns and likewise leaves its `Notes` column empty: "| SOW-019 | IN | Classify and report drift between successive snapshots; never modify a source file | PEC-RCN-004 | |".

- **CLM-002** — `SOW-019`'s `SourceRef` cell names one locus, `PEC-RCN-004`, the `PRD.md` §9.2 reconciliation requirement, quoted here in full as it reads: "The reconciler shall classify drift between successive snapshots and report it; it shall never modify a source file." The scope item carries both limbs of that requirement forward verbatim in substance — the classify-and-report duty and the never-modify-a-source-file duty — and the second limb is part of this deliverable's own row text, not an inherited neighbour's rule.
- **CLM-003** — `OBJ-002` states "Staleness is detected structurally by SHA comparison, never by judgment", `SourceRef` `§3.2` (`SOFTWARE_DECOMP.md` §3; `PRD.md` §3 outcome 2). At revision 1.6 its "Mapped Scope Items" cell reads "SOW-001, SOW-006, SOW-011..019, SOW-095..097; supported by SOW-005" and its `MappedDeliverables` cell names fourteen deliverables: "DEL-01-01, DEL-02-01..09, DEL-03-02, DEL-03-03, DEL-04-02, DEL-04-03". The objective's product invariant is `PEC-K-04`, quoted in full: "**Staleness is a comparison.** Every response carries the examined-through commit SHA and per-feed freshness; consumers detect staleness structurally."
- **CLM-004** — The reported unit of this deliverable's output is the record-tier `DriftFinding`. `PRD.md` §7.1 defines it in one row, quoted in full: "A classified difference between the current reconcile and the prior snapshot, or between PEC and harness parity output". The `SOFTWARE_DECOMP.md` §9 vocabulary map records the same term with its aliases and gloss: "| DriftFinding | drift, parity discrepancy | Classified difference between snapshots or vs harness output |". Both statements name **two** production paths for one type; the snapshot-to-snapshot path is this deliverable's and the parity path is `DEL-03-04`'s under `SOW-020` (CLM-012, CON-005).

## Deliverable Definition — Ontology

`DEL-03-03` is typed `BACKEND_FEATURE_SLICE` at Context Envelope `M` with
`PhaseHint` `P1`. `Deliverables.csv` records its `AnticipatedArtifacts` as
"Drift classifier + tests" and leaves `ContextEnvelopeNotes` empty, so there
are no envelope notes to carry forward. The outputs of this contract are bounded by that artifact naming: exactly the drift
classifier and its tests, and nothing beyond those two artifacts and the
components each of them declares as part of itself.

- **OUT-001** — A drift classifier in the PEC service core: given a pair of successive reconcile snapshots, it determines every difference between them, assigns each difference a class from a declared closed class set, and reports each as a record-tier DriftFinding carrying the basis of its classification. The classifier's **declared class-set record** — the readable artifact in which it documents every class it can assign and the rule that assigns it (REQ-001, REQ-006) — is a component of this output rather than a third artifact: it is the classifier's own self-declaration, so the register's `AnticipatedArtifacts` naming of exactly two artifacts is preserved.
- **OUT-002** — An automated test suite covering the classification path, the reporting path, and the never-modify-a-source-file restriction, implementing the verification methods declared in this contract.

### Identity of record

- **CLM-005** — `DEL-03-03` is named "Drift classification", Type `BACKEND_FEATURE_SLICE`, Context Envelope `M`, `PhaseHint` `P1`, `ResponsibleParty` `TBD`, `AnticipatedArtifacts` "Drift classifier + tests", `CoversScopeItems` `SOW-019`, `SupportsObjectives` `OBJ-002`, `ContextEnvelopeNotes` empty, with the register `Description` field reading in full "Classified drift between successive snapshots, reported as DriftFindings; sources never modified. Lag classes: terminal-node lag after the final-PR merge is "trailing by method design" (derived completion, not drift); non-terminal graph-behind-Git is a DriftFinding; unchanged historical surfaces are never staleness." Its second sentence was added by SCA-005 action `A-21` (CLM-015). Sources: `Deliverables.csv` row `DEL-03-03` and the `SOFTWARE_DECOMP.md` §5 PKG-03 table row "| DEL-03-03 | Drift classification | BACKEND_FEATURE_SLICE | M | P1 | SOW-019 |". The register `Description` is the only accepted source that names DriftFindings as this deliverable's reporting unit; `SOW-019` and `PEC-RCN-004` say "report it" without naming the type (CLM-002, CLM-004).
- **CLM-006** — The `PKG-03` package charter (`SOFTWARE_DECOMP.md` §4) is "The guaranteed path from file truth to record tier: one-command rebuild, incremental Git-delta reconcile, drift classification, harness parity diffing, stream-loss recovery guarantee, store-only writes, rebuild performance bounds", covering "SOW-010, 018, 019, 020, 021, 038, 054 (7)", with "Stream ingest mechanics (PKG-07); parsers (PKG-02)" recorded as explicitly out of package scope. Of those seven items this deliverable covers exactly one — drift classification — and each of the other six is cited in CLM-012 to its owner.
- **CLM-007** — The DriftFinding type this classifier reports into is defined upstream and not here. `DEL-01-01` "Record-tier schema & entity model" covers `SOW-001` and is at lifecycle state `INITIALIZED`; its accepted contract, rebuilt under the owner-ruled `D-PEC-100`, obliges the type, obliges the snapshot comparability this classifier depends on, and names this deliverable as the performer of the comparison:

> - **REQ-001** — The schema and entity model shall define exactly the sixteen
>   record-tier entity types named in CLM-005 — Loop, Workplan, Step, Gate,
>   Receipt, DecisionRow, Fence, Package, Deliverable, DependencyEdge,
>   RunRecord, CandidateBrief, OrientationSnapshot, DriftFinding, WorkGraph,
>   WorkNode — with none added and none dropped, and each type shall carry a
>   recorded trace to its `PRD.md` §7.1 row and stated purpose (CLM-006).
> - **REQ-004** — The model shall represent examined-through SHA provenance
>   structurally, so that staleness is a comparison and never a judgment
>   (`PEC-K-04`, `OBJ-002`): OrientationSnapshot shall be stamped with the
>   examined SHA, and two successive snapshots shall be comparable field by
>   field such that a DriftFinding can record a classified difference.
>   Performing that comparison is `DEL-03-02`'s and `DEL-03-03`'s (CLM-012); the
>   model shall not require a human or agent judgment input for any field on
>   which staleness turns.
> - **REQ-005** — Every record-tier entity shall be fully regenerable from
>   file sources. No record-tier field may hold state that cannot be reproduced
>   by rebuilding from the same sources, per `PEC-K-02` ("The record tier is
>   regenerated from sources by one command") and `PEC-RCN-001`. The rebuild
>   command itself is `DEL-03-01`'s under `SOW-010` (CLM-012).
> - **REQ-007** — No field of any type shall admit file content or diff
>   content (`PEC-K-10`: "Paths, counts, SHAs, states, hashes — never file or
>   diff content"). DecisionRow shall carry register-row identity and status
>   only — decision ID, packet path, anchor, state — and shall have no field
>   capable of holding the row's prose; no WorkGraph or WorkNode field shall be
>   capable of holding graph prose, and no RunRecord field a run description.
>   Enforcement at the ingest boundary is `DEL-01-03`'s guard under `SOW-056`
>   (CLM-012); this requirement binds the shape of the schema so that the guard
>   has nothing to admit into.
>
> (`DEL-01-01/ScopeOfWork.md`, Epistemology section; all four records quoted in
> full, none elided. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference — this contract's own `REQ-*`
> and `AC-*` records are separate and differently worded.)

  That contract is cited here for the entity and its comparability obligation only. It is **not** a declared upstream edge of this deliverable: no `Dependencies.csv` row and no accepted DAG edge joins the two (CLM-008). The relation is the register-wide constraint `C-03` recorded in `_DEPENDENCIES.md` — "Every PKG-03/04/05 deliverable depends on DEL-01-01 directly or transitively" — and this deliverable's route is the transitive one, through its single declared predecessor. The regenerability obligation quoted above is also the source of CON-001, which this contract records rather than resolves.

### Placement in the work graph

- **CLM-008** — This deliverable has exactly one accepted `EXECUTION` upstream edge and two `ANCHOR` rows, held as `Dependencies.csv` register rows `DEP-03-03-001` through `DEP-03-03-003` at `RegisterSchemaVersion` `v3.1`; the register contains no other row and no downstream row. The two anchors are `DEP-03-03-001` (`IMPLEMENTS_NODE`: "DEL-03-03 is package-local to PKG-03.", `TargetType` `PACKAGE`, `SatisfactionStatus` `SATISFIED`) and `DEP-03-03-002` (`TRACES_TO_REQUIREMENT`: "DEL-03-03 covers scope item SOW-019.", `TargetRefID` `SOW-019`, `EvidenceQuote` "DeliverableIDs include DEL-03-03", `SatisfactionStatus` `SATISFIED`). The single `EXECUTION` row is `DEP-03-03-003`, attributed by column: `FromPackageID` `PKG-03`, `FromDeliverableID` `DEL-03-03`, `FromDeliverableName` "Drift classification", `DependencyClass` `EXECUTION`, `AnchorType` `NOT_APPLICABLE`, `Direction` `UPSTREAM`, `DependencyType` `PREREQUISITE`, `TargetType` `DELIVERABLE`, `TargetPackageID` `PKG-03`, `TargetDeliverableID` and `TargetRefID` `DEL-03-01`, `TargetName` "Full-rebuild reconciler (one command)", `Statement` "Drift classification compares successive reconcile snapshots", `EvidenceFile` `docs/PRD.md`, `Explicitness` `IMPLICIT`, `RequiredMaturity` `INITIALIZED`, `ProposedMaturity` `TBD`, `SatisfactionStatus` `PENDING`, `Confidence` `MEDIUM`, `Origin` `EXTRACTED`, `FirstSeen` and `LastSeen` `2026-07-25`, `Status` `ACTIVE`, `Notes` "PROPOSAL; Flag=none; EdgeID=E-P27". Its `SourceRef` reads "PRD.md §9.2 requirement PEC-RCN-004" and its `EvidenceQuote` reads "The reconciler shall classify drift between successive snapshots and report it; it shall never modify a source file." These three cells were repaired under `D-PEC-65`; at this contract's 2026-07-25 authoring they read `EvidenceFile` `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md`, `SourceRef` "location TBD" and an empty `EvidenceQuote`. The corresponding frozen DAG exhibit row still carries the authoring-time gap — `E-P27,DEL-03-01,DEL-03-03,PROPOSAL,CONSUMES,,,Drift classification compares successive reconcile snapshots` under the exhibit's columns `EdgeID,PredecessorID,SuccessorID,Stratum,EdgeKind,Flag,BasisCitation,Rationale`, with both `Flag` and `BasisCitation` empty. The edge's basis is its `Statement`, the two deliverables' own accepted contracts and the quoted requirement; the quote changes neither its acceptance, its `PROPOSAL` stratum nor its `PENDING` satisfaction.
- **CLM-009** — The single predecessor is at lifecycle state `INITIALIZED`, which is the maturity the edge requires. `INITIALIZED` means the upstream **contract** is the reliable input: its accepted `ScopeOfWork.md` exists, and no reconciler or record-tier schema does. Nothing in this contract asserts that any upstream artifact exists. The obligations this contract binds to are that contract's stated obligations, quoted here in full:

> - **OUT-001** — A full-rebuild reconciler entry point in the PEC service
>   core: one command that rebuilds the record tier in full from file sources
>   for the loops the registry names, writing only into the store and into the
>   generated views it declares. The entry point's **declared-view record** —
>   the readable artifact in which it declares every generated view it writes
>   (REQ-006) — is a component of this output rather than a third artifact: it
>   is the entry point's own self-declaration, so the register's
>   `AnticipatedArtifacts` naming of exactly two artifacts is preserved.
> - **REQ-002** — Every record-tier fact the rebuild produces shall be derived
>   from file sources read through the declared upstream feed units of CLM-016.
>   No record-tier fact shall rest on prior store state, on a cached artifact,
>   on a stream or event input, or on any input the same sources cannot
>   reproduce, per `PEC-K-07` ("the reconciler over file truth is the source of
>   every record-tier fact") and the upstream regenerability obligation quoted
>   in CLM-012.
> - **REQ-005** — The reconciler shall write only into the store, through the
>   single declared ingest boundary quoted in CLM-013, and into the generated
>   views it declares under REQ-006. It shall create, modify, or delete no
>   source file, no governed file, no register, no lifecycle file, and no path
>   outside that declared write set, per `SOW-021` and `PEC-RCN-006` (CLM-002,
>   CLM-004), `PEC-RCN-004` ("it shall never modify a source file"),
>   `PEC-GAT-004` ("PEC shall provide no write path that records adoption,
>   ruling, or direction"), and `PEC-K-06` observation-not-participation.
> - **REQ-009** — Where an upstream unit reports that a feed is absent,
>   unreadable, malformed, stale, or grammar-unrecognized, the rebuild shall
>   carry that limitation through to its result, naming the loop and the feed,
>   and shall never present a rebuild that could not read a feed as a rebuild
>   that read it. Silent omission is prohibited, per `PEC-ORI-006` ("Where a
>   feed is unparseable or stale, the response shall state the measurement
>   limitation explicitly; silent omission is prohibited"). Rendering such a
>   limitation into an orientation response is `DEL-04-05`'s act under
>   `SOW-009` (CLM-019); this deliverable makes the limitation available to
>   that consumer.
> - **REQ-010** — The rebuild shall be deterministic and idempotent over its
>   inputs: two rebuilds over the same unchanged sources shall produce the same
>   record tier, and a rebuild over a store already rebuilt from those sources
>   shall produce no difference. This is what makes a later difference between
>   two reconciles a structural fact rather than a judgment (`PEC-K-04`).
> - **REQ-013** — Nothing the reconciler writes — into the store or into a
>   generated view — shall carry file content or diff content, per `PEC-K-10`
>   ("Paths, counts, SHAs, states, hashes — never file or diff content").
>   Enforcement at the store's ingest boundary is the upstream guard's
>   (CLM-013); this requirement binds what the reconciler presents to that
>   boundary and extends the same restriction to every generated view, which
>   the guard does not cover (CON-004).
> - **REQ-014** — The reconciler shall perform no act owned by another
>   deliverable. In particular it shall perform no Git-delta-keyed incremental
>   reconcile, no drift classification between snapshots, no parity diff
>   against practitioner-harness output, no stream-loss recovery act, no
>   rebuild-bound measurement or assertion, no examined-SHA or freshness
>   stamping and no per-claim citation attachment onto an orientation response,
>   no gate-precondition evaluation or slate rendering, no locality or
>   zero-dependency enforcement act, and no kill test; each is cited to its
>   owner in CLM-019 and none is discharged here.
>
> (`DEL-03-01/ScopeOfWork.md`, Ontology and Epistemology sections; all seven
> records quoted in full, none elided. ID-shaped text inside this quotation is
> upstream source context, not a local definition or reference.)

  Four of those obligations are load-bearing for this contract and are named as such. The record tier the rebuild produces is what "successive snapshots" refers to: its determinism obligation is what makes a difference between two of them "a structural fact rather than a judgment", which is `OBJ-002` in the upstream contract's own voice. Its store-write restriction and its content-minimal duty establish the write posture this classifier inherits at its own boundary (REQ-004, REQ-005). Its limitation carry-through is the input to this contract's own carry-through duty (REQ-009). And its boundary requirement names drift classification between snapshots as an act it does not perform — the clearest statement in the accepted corpus that this act is discharged here.

- **CLM-010** — One downstream consumer relation is recorded against this deliverable in `_DEPENDENCIES.md` and marked informational: `DEL-09-07` "Explain-shaped pressure rules" `[E-P67]`. It holds **no** row in this deliverable's `Dependencies.csv`, which contains only the two anchors and the one upstream `EXECUTION` row (CLM-008); the downstream row lives in the consumer's own local register, per the deliverable-local storage ruling of `D-PEC-62`. The gate exhibit row reads `E-P67,DEL-03-03,DEL-09-07,DERIVED,CONSUMES,,"SOW-051: pressure rules include ""drift density""",Drift classification output feeds the rule` under the exhibit's columns `EdgeID,PredecessorID,SuccessorID,Stratum,EdgeKind,Flag,BasisCitation,Rationale`, with `Flag` empty. `DEL-09-07` is `PKG-09`, `P2`, and covers `SOW-051` for `OBJ-004`: "Implement derived pressure/status rules (stuck-in-state age, gate-blocked, drift density, staleness, collision risk) as Explain-shaped, individually documented rules". Deriving a drift-density rule is that deliverable's act; this contract produces the findings such a rule would consume and defines no pressure rule, threshold, or density measure (REQ-011).
- **CLM-011** — Phase staging, checked against the `PhaseHint` column of `Deliverables.csv` for every deliverable this contract names in its own voice: `DEL-03-03` itself, its predecessor `DEL-03-01`, its `PKG-03` siblings `DEL-03-02`, `DEL-03-04`, and `DEL-03-06`, the entity-model owner `DEL-01-01`, the store owner `DEL-01-03`, the zero-dependency enforcer `DEL-01-05`, the loop-registry owner `DEL-01-06`, the work-graph parser `DEL-02-08`, the orientation-return owner `DEL-04-01`, the `OBJ-002` co-members `DEL-04-02` and `DEL-04-03`, the kill-test owner `DEL-10-02`, and the parity-metric owner `DEL-10-11` are all `P1`. Two exceptions are named in this contract's own voice, each cited only as the owner of scope this deliverable does not touch: `DEL-09-07` (`P2`) and `DEL-03-05` (`P3`). No claim in this contract stages any named deliverable into a different phase.

### Boundaries

- **CLM-012** — The acts adjacent to this classifier are owned elsewhere and are cited here, never discharged. Within `PKG-03`: the one-command full rebuild that produces the record tier is `DEL-03-01` (`SOW-010`, `SOW-021`); incremental reconciliation keyed on Git delta since the last examined SHA is `DEL-03-02` (`SOW-018`, `PEC-RCN-003`); parity-diffing PEC derivations against practitioner-harness output, with discrepancies surfaced as DriftFindings resolved against live sources, is `DEL-03-04` (`SOW-020`, `PEC-RCN-005`) — a **second, distinct** producer of the same entity type (CLM-004, CON-005); the stream-loss recovery guarantee is `DEL-03-05` (`SOW-038`, `P3`); rebuild performance bounds are `DEL-03-06` (`SOW-054`). Outside it: the record-tier schema and the DriftFinding type are `DEL-01-01` (`SOW-001`, CLM-007); the gitignored store, its safe-delete lifecycle, and its ingest-boundary content-minimal guard are `DEL-01-03` (`SOW-056`); standing zero-dependency and locality enforcement is `DEL-01-05` (`SOW-052`, `SOW-053`); the delta service over a caller-supplied SHA is `DEL-04-02` (`SOW-005`); examined-SHA and freshness stamping with per-claim citation attachment is `DEL-04-03` (`SOW-006`, `SOW-007`); Explain-shaped pressure and status rules including drift density are `DEL-09-07` (`SOW-051`, `P2`, CLM-010); the §11 parity metric "DriftFindings against practitioner-harness output per reconcile" is `DEL-10-11` (`SOW-093`), whose register note records that it "Measures the output of SOW-020 (DL-14); the behavior is PKG-03, the metric is PKG-10"; the standing kill test is `DEL-10-02` (`SOW-055`). This contract produces only the drift classifier and its tests.
- **CLM-013** — The edges cited in this contract carry a declared semantics that bounds what may be inferred from them. The accepted exhibit states it before the edge list: "build-order capability-consumption precedence for PEC v2's directed self-bootstrap under C16 — an edge `A → B` means *B consumes a capability or artifact produced by A; B's start or acceptance is gated on A reaching the (owner-ruled) maturity threshold*", and it records that "Non-precedence relations (co-landing, co-obligation, package-level, phase-precedence, standing obligations) are in the constraints register, **not** encoded as blocking edges." An edge is therefore a build-order statement, not a runtime data-flow statement, and the absence of an edge is not a statement that a runtime relation is absent. CON-003 records the one place where that distinction matters for this deliverable.
- **CLM-014** — At `125cfacc1` the deliverable is at lifecycle state `INITIALIZED` with no implementation present: of the eleven files under `projects/pec/v2/src/pec_v2/`, none contains the string `DriftFinding` or `drift`. Every requirement, acceptance criterion, and verification method below states a contract on future production; none asserts that anything has been built.
- **CLM-015** — The lag classes are revision-1.6 register content carried by the `Description` of CLM-005 and by no other accepted source of this deliverable: SCA-005 action `A-21` added them to the `Deliverables.csv` row ("DEL-03-03 description adds the lag classes (terminal lag = trailing by method design; non-terminal graph-behind-Git = DriftFinding; historical surfaces never staleness). Supersession binding: **NO**."), while `SOW-019` (CLM-001) and `PEC-RCN-004` (CLM-002) read as they did, and `PRD.md` v2.4 does not contain the phrase "trailing by method design". The SCA-005 impact assessment records the condition they answer, in its row `R-01`: "All three 2026-09-23 trial graphs show `F1 ACTIVE` after their final PRs merged", and "the method forbids write-back". The PRD v2.4 §7.1 WorkGraph / WorkNode row states the related rule: "a node state is declared activity, never a liveness assertion; terminal completion is derived from local Git merge reachability of cited PRs". The facts the lag classes turn on are produced elsewhere: parsing work graphs and resolving their cited PR numbers to local merge commits by read-only plumbing is `DEL-02-08` (`SOW-095`), serving terminal completion "derived from local Git merge reachability of cited PRs" in the loop orientation return is `DEL-04-01` (`SOW-004`), and declaring each loop's feed profiles, including which are historical, is `DEL-01-06` (`SOW-077`, `SOW-094`). This deliverable classifies over those facts as its snapshot inputs carry them (REQ-002) and produces none of them.

- **TBD-001** — `ResponsibleParty` is unassigned; the register records `TBD`, with assignment at WORKING_ITEMS activation and not in this contract (`SOFTWARE_DECOMP.md` §5 preamble).
- **TBD-002** — The class set itself — which classes of difference exist, what each is named, and how a difference is assigned to exactly one — is fixed by no accepted source beyond the three lag classes of the register `Description` (CLM-005, CLM-015), which REQ-015 through REQ-017 carry. `SOW-019` and `PEC-RCN-004` require classification and name no class; `PRD.md` §7.1 says "A classified difference between the current reconcile and the prior snapshot" and the §9 vocabulary map "Classified difference between snapshots", and neither names a class. The rest of the set is chosen during production within REQ-001 and documented under REQ-006.
- **TBD-003** — The classifier's invocation surface — whether classification runs as part of each reconcile, on demand against a named snapshot pair, or as a separate command, and what its result surface is — is fixed by no accepted source. `PEC-RCN-004` attributes the act to "the reconciler" without stating when it runs. It is chosen during production within REQ-001 and REQ-002.
- **TBD-004** — How the prior member of a snapshot pair is obtained — retained as store state, re-derived from the source state its examined-through SHA identifies, or supplied by the caller — is fixed by no accepted source. This is the informational side of CON-001 and is not settled here.
- **TBD-005** — Whether and in what form the classifier's result surfaces a difference classified "trailing by method design", which REQ-015 keeps out of the DriftFinding set, is fixed by no accepted source: the register `Description` names the class and calls it "derived completion, not drift", and says nothing of reporting it (CLM-005). It is chosen during production within REQ-001, REQ-006 and REQ-015, by the party TBD-001 assigns.

## Completion and Reliance Basis — Epistemology

The requirements below state what future production must satisfy. Nothing in
this section asserts that a classifier, a reconciler, a snapshot, a store, or a
test exists.

- **REQ-001** — The classifier shall, for a pair of successive reconcile snapshots presented to it, determine every difference between the two and assign each difference exactly one class from a declared, closed, documented class set, per `SOW-019` (CLM-001) and `PEC-RCN-004` (CLM-002). A difference the class set cannot classify shall be reported as unclassified with its reason stated, never dropped.
- **REQ-002** — Both members of the pair shall be obtained from the record tier the upstream rebuild is obliged to produce (CLM-009). The classifier shall itself perform no reconcile, produce no snapshot, define no feed grammar, and read no feed file to construct either member; its inputs are snapshots, not sources.
- **REQ-003** — Every classified difference, except one REQ-015 classifies as trailing by method design, shall be reported as an instance of the upstream-obliged record-tier DriftFinding type (CLM-004, CLM-007). This deliverable shall define no record-tier entity type, shall add no type and no presence-tier type to that model, and shall not depend on any upstream artifact existing; it depends on the upstream contracts only. Two unresolved questions ride this type and this requirement settles neither: which snapshot entity the comparison is over (CON-002) and how the type's two producers are told apart (CON-005).
- **REQ-004** — The classifier shall create, modify, or delete no source file, no governed file, no register, and no lifecycle file, per `SOW-019`'s own second limb — "never modify a source file" — and `PEC-RCN-004` (CLM-001, CLM-002), `PEC-K-06` observation-not-participation, and `PEC-GAT-004`. Because its inputs are snapshots rather than live sources (REQ-002), it shall hold no source-file handle at all, for reading or writing. Its writes shall reach the store through the single declared upstream ingest boundary (CLM-007) and shall target no other path; this contract claims no generated-view write authority, that limb being `SOW-021`'s and its owner's (CLM-012).
- **REQ-005** — No DriftFinding field the classifier populates, and nothing else it reports, shall carry file content or diff content, per `PEC-K-10` ("Paths, counts, SHAs, states, hashes — never file or diff content") and the upstream schema obligation quoted in CLM-007. A classified difference shall be expressed in paths, counts, identifiers, states, SHAs, and hashes, and in the class assigned; the changed text itself shall never be carried, quoted, excerpted, or reconstructed.
- **REQ-006** — Every reported finding shall carry the basis of its own classification: the identity of the two snapshots compared, each by its examined-through SHA; the class assigned; and the identity of the declared rule that assigned it, resolving to the class-set record that is a component of OUT-001. This satisfies `PEC-K-08` ("Every status, verdict, and warning carries rule ID, threshold, and contributing cited sources. Drill-down never dead-ends.") at this deliverable's own surface. Deriving pressure or status rules over these findings, and rendering them, are other deliverables' acts (CLM-010, CLM-012).
- **REQ-007** — Classification shall require and admit no human or agent judgment input. Every class assigned shall be reproducible from the two snapshots and the declared rule set alone, per `OBJ-002` ("never by judgment"), `PEC-K-04` (CLM-003), and the upstream model obligation that no field on which staleness turns requires a judgment input (CLM-007).
- **REQ-008** — Classification shall be deterministic over its inputs: the same snapshot pair shall yield the same set of findings, with the same classes and a stable order, and re-running the classifier over an already-classified pair shall produce no difference. The warrant is the upstream determinism and idempotence obligation quoted in CLM-009, which is what makes a difference between two snapshots a property of the sources rather than of the run.
- **REQ-009** — Where either snapshot carries a stated coverage limitation — a feed reported absent, unreadable, malformed, stale, or grammar-unrecognized — the classifier shall carry that limitation into its result, naming the loop and the feed, and shall never present a difference that arises from a feed one snapshot could not read as though it were drift in the sources. Silent omission is prohibited, per `PEC-ORI-006` and the upstream carry-through obligation quoted in CLM-009. What class such a case takes, if any, is CON-004 and is not settled by this requirement.
- **REQ-010** — Findings this classifier produces shall be attributable to snapshot-to-snapshot classification and shall never be presented, exported, or counted as practitioner-harness parity output, which is the other producer's under `SOW-020` (CLM-004, CLM-012). The field or mechanism by which the shared type carries that attribution is the upstream schema owner's decision, not this contract's (CON-005).
- **REQ-011** — The classifier shall perform no act owned by another deliverable. In particular it shall perform no full rebuild, no Git-delta-keyed incremental reconcile, no parity diff against practitioner-harness output, no resolution of any discrepancy against live sources, no stream-loss recovery act, no rebuild-bound or performance measurement, no delta service over a caller-supplied SHA, no examined-SHA or freshness stamping and no citation attachment onto an orientation response, no pressure-rule, density, or threshold derivation, no dashboard or census rendering, no metric report, no gate evaluation, and no store lifecycle act; each is cited to its owner in CLM-012 and none is discharged here.
- **REQ-012** — Nothing in this deliverable shall assert or require that an upstream schema, store, reconciler, parser, or snapshot artifact exists. Every dependency shall be on an accepted upstream contract obligation, exercised in production against an interface-level fixture stand-in until the upstream artifact is available, and re-exercised against the live upstream without discharging that deliverable here (CLM-007, CLM-009).
- **REQ-013** — The classifier and its tests shall introduce no third-party runtime dependency and no external network egress, per `PEC-SVC-001` and `PEC-SVC-002`, whose standing enforcement is `DEL-01-05` covering `SOW-052` and `SOW-053`.
- **REQ-014** — Tests shall implement the verification methods declared in this contract; they shall not define scope, requirements, or acceptance criteria.
- **REQ-015** — A difference showing terminal-node lag after the final-PR merge — a terminal work-graph node whose declared state still lags the merge of the undertaking's final PR — shall be assigned the class "trailing by method design" as "derived completion, not drift", per the register `Description` (CLM-005, CLM-015). It shall not be reported as a DriftFinding or counted as drift (TBD-005). The classifier shall take a node's terminal status and the local merge reachability of its cited PRs only as facts its snapshot inputs carry (REQ-002, CON-006): it shall parse no work graph and resolve no PR number to a merge commit, those two acts being `DEL-02-08`'s, and it shall derive no terminal completion, that act being `DEL-04-01`'s (CLM-015). Where its inputs do not carry those facts, the difference shall be reported unclassified with its reason under REQ-001, never classified by inference.
- **REQ-016** — A difference showing non-terminal graph-behind-Git — a non-terminal work-graph node whose declared state is behind what Git records — shall be classified as drift and reported as a DriftFinding under REQ-003 and REQ-006, per the register `Description` ("non-terminal graph-behind-Git is a DriftFinding"; CLM-005, CLM-015), on the same snapshot facts and under the same limits as REQ-015. Which comparison detects it is not settled here (CON-006).
- **REQ-017** — An unchanged historical surface shall never be classified or reported as stale, per the register `Description` ("unchanged historical surfaces are never staleness"; CLM-005, CLM-015). Whether a surface is historical shall be taken from what the snapshot inputs declare, never decided by the classifier; which surfaces count is CON-007 and is not settled by this requirement.

- **AC-001** — For fixture snapshot pairs exercising addition, removal, modification, and no-change, every difference between the pair is found and assigned exactly one class from the declared closed class set; a seeded difference the class set does not cover is reported as unclassified with a stated reason and is not dropped.
- **AC-002** — Both snapshots in every exercised pair are acquired through the upstream record-tier interface; this deliverable's source contains no reconcile path, no snapshot construction path, no feed grammar, and no feed-file read.
- **AC-003** — Every finding produced is an instance of the upstream-obliged DriftFinding type; this deliverable's source defines no record-tier or presence-tier entity type; and no element of this deliverable asserts that an upstream schema, store, reconciler, or parser artifact exists.
- **AC-004** — A classification run over a fixture source corpus leaves that corpus byte-identical, opens no source file for reading or writing, and touches no path outside the store; every store write in this deliverable's source reaches the store through the upstream declared ingest boundary; and the module contains no write, create, or delete call against any source file, governed file, register, or lifecycle file, and no write to any generated view.
- **AC-005** — For a content-dense fixture pair whose differences fall in long prose bodies, quoted authored text, and diff-shaped content, inspection of every field of every finding produced shows only paths, counts, identifiers, states, SHAs, hashes, and class tokens, and no changed text is carried, quoted, excerpted, or reconstructible from the finding.
- **AC-006** — Every finding produced carries both snapshots' examined-through SHAs, its assigned class, and a rule identity that resolves to an entry in the classifier's declared class-set record; that record documents every class the classifier can assign; and no finding's basis dead-ends.
- **AC-007** — Classification exposes no judgment, override, or manual-adjustment input; re-deriving every class from the two snapshots and the declared rule set alone reproduces the classifier's output exactly.
- **AC-008** — Two classification runs over the same fixture snapshot pair produce identical finding sets in identical order, and a run over an already-classified pair produces no difference.
- **AC-009** — For fixture pairs in which one snapshot reports a feed absent, unreadable, malformed, stale, and grammar-unrecognized in turn, the result carries the reported limitation naming the loop and the feed, and no such case is presented as drift in the sources.
- **AC-010** — Every finding this classifier produces is attributable to snapshot-to-snapshot classification and none is presented, exported, or counted as practitioner-harness parity output; this deliverable's source contains no parity-diff path and no harness-output reader.
- **AC-011** — The module contains no full-rebuild path, no Git-delta incremental path, no parity-diff or source-resolution path, no stream-loss recovery path, no performance measurement or assertion, no caller-SHA delta path, no stamping or citation-attachment path, no pressure-rule, density, or threshold derivation, no dashboard, census, or metric path, no gate-evaluation path, and no store lifecycle act; and no test in this deliverable asserts a criterion belonging to any of them.
- **AC-012** — Every upstream dependency in this deliverable's source and tests resolves to an interface-level fixture stand-in for a contract obligation rather than to an assumed artifact, and a recorded search of source, fixtures, and call surface finds no assumption that any upstream artifact exists.
- **AC-013** — The classifier and its tests add no third-party runtime dependency and make no network call, leaving the `DEL-01-05` zero-dependency and locality assertion intact.
- **AC-014** — The test suite implements VER-001 through VER-013 and VER-015 through VER-017, executes in the `PKG-03` test run, passes, and introduces no acceptance criterion absent from this contract.
- **AC-015** — The REVIEW gate confirms this contract's traceability to `SOW-019` and `OBJ-002`; confirms that the objective mapping is stated as register-direct and pre-SCA-002, carrying no confidence label the record does not assign; and confirms that no `PKG-01`, sibling `PKG-03`, `PKG-04`, `PKG-09`, or `PKG-10` scope has been absorbed — in particular neither reconcile path, the parity diff, the pressure rules, nor the parity metric.
- **AC-016** — For fixture snapshot pairs carrying a terminal work-graph node whose declared state lags after its final-PR merge, the result assigns the class "trailing by method design" and produces no DriftFinding for that difference; where the fixture omits the node's terminal status or the merge reachability of its cited PRs, the difference is reported unclassified with a stated reason; and this deliverable's source contains no work-graph parsing, no PR-to-merge-commit resolution and no terminal-completion derivation.
- **AC-017** — For fixture snapshot pairs carrying a non-terminal work-graph node whose declared state is behind Git, the result reports a DriftFinding carrying the classification basis REQ-006 requires.
- **AC-018** — For fixture snapshot pairs in which surfaces the inputs declare historical are unchanged, no finding and no class reports any of them as stale.

- **CON-001** — A DriftFinding is a record-tier entity, and the record tier is contractually obliged to be fully regenerable from file sources with no field holding state the same sources cannot reproduce (CLM-007), while the store that holds it is gitignored and safe to delete at any moment (`PEC-K-02`, `OBJ-005`'s deletability claim). But a DriftFinding is by definition a difference against "the prior snapshot" (CLM-004), and the prior snapshot reflects an **earlier** source state, which the current sources do not contain. Deleting the store therefore deletes the only recorded prior snapshot, and no accepted source states what "successive snapshots" means on the first reconcile after a deletion, or whether a DriftFinding survives a rebuild at all. A resolution is available in principle and is not taken here: every snapshot is stamped with an examined-through commit SHA (`PEC-K-04`), PEC is read-only over Git (`PEC-K-06`), and the incremental reconciler is keyed on "Git delta since the last examined SHA" (`PEC-RCN-003`), so the prior source state is identifiable and reachable in Git history — but no accepted source states that the prior snapshot is re-derived that way rather than retained, and re-deriving it would be a reconcile act this contract does not own (REQ-002, REQ-011). This contract records the question: REQ-002 binds the classifier to whatever pair it is given, TBD-004 records the acquisition gap, and settling either the retention model or the re-derivation path is a decision for the store and reconciler owners or a scope-change question, not a production choice made here.
- **CON-002** — The unit of comparison named "snapshot" has two candidate referents in accepted truth and no accepted source selects between them. `PRD.md` §7.1 defines a DriftFinding as a difference "between the current reconcile and the prior snapshot" — a reconcile result, that is, the record-tier state — while the same section defines OrientationSnapshot as "A generated orientation return, stamped with examined SHA", and the upstream model obligation phrases the comparability duty over OrientationSnapshot: "two successive snapshots shall be comparable field by field such that a DriftFinding can record a classified difference" (CLM-007). `SOW-019` and `PEC-RCN-004` say "successive snapshots" unqualified (CLM-001, CLM-002), and the §9 vocabulary map records OrientationSnapshot as `Distinct from the general term "orientation"` without ruling on this usage. The two readings are not equivalent: an orientation return is a scope-parameterized projection (`PEC-ORI-005`), so a drift set computed over orientation returns is relative to a scope parameterization that a record-tier comparison is not. This contract takes neither reading as settled; REQ-001 and REQ-002 are written over "a pair of successive reconcile snapshots" as the register statement has it, and a production choice that fixed the unit would settle a question the accepted sources leave open.
- **CON-003** — Which reconcile paths supply the snapshot pair is not stated. This deliverable's only accepted upstream edge is from the full-rebuild reconciler (CLM-008), yet at steady state the reconciler that produces successive snapshots is the incremental one — `PEC-RCN-003` keys reconciliation on Git delta since the last examined SHA, and `PEC-RCN-004` attributes drift classification to "the reconciler" without distinguishing the two paths. The absence of an edge from the incremental reconciler is not evidence against a runtime relation: edges are build-order capability-consumption precedence, and non-precedence relations are recorded in the constraints register rather than as edges (CLM-013). So the edge set is consistent with either reading and settles neither. This contract binds the classifier to the pair it is given rather than to a producer (REQ-002), so that whichever reconcile paths feed it, the classification contract is unchanged; naming the producers would be a scope question for `SOW-019`, not a production decision.
- **CON-004** — Whether a difference arising from a coverage limitation is drift is not settled. Every upstream feed unit is obliged to report a feed it could not read as an explicit limitation rather than as an absence, and the rebuild is obliged to carry that limitation through (CLM-009); `PEC-ORI-006` prohibits silent omission. A feed read into one snapshot and reported unreadable in the next therefore presents, structurally, exactly as a deletion. No accepted source states whether that is drift in the sources, a coverage limitation of the comparison, or both, and the answer changes what a drift count means to the downstream density rule (CLM-010). REQ-009 makes the case visible either way — the limitation is carried, naming the loop and the feed, and the case is never silently presented as source drift — without asserting which reading is correct. Choosing a class for it would answer the question by implementation.
- **CON-005** — One entity type has two producers and no accepted source states how they are told apart. `PRD.md` §7.1 and the §9 vocabulary map define DriftFinding over both the snapshot-to-snapshot path (this deliverable) and the practitioner-harness parity path (`DEL-03-04`, `SOW-020`) (CLM-004). The distinction is load-bearing downstream: `PRD.md` §11 metric 5 is "Parity: DriftFindings against practitioner-harness output per reconcile", and the `SOW-093` `Notes` cell on the deliverable that reports it reads in full "Measures the output of SOW-020 (DL-14); the behavior is PKG-03, the metric is PKG-10" (CLM-012) — a metric that counted this classifier's findings as well would over-count, and so would corrupt the §11 parity metric that `SOW-093` reports. It would not mis-arm the §11 falsification clause, which is not armed on this count: the ledger ties that clause to other scope items — `SOW-060`, whose `Notes` cell reads in full "Measures uptake of SOW-004; no receiving-loop conformance criterion; supports the §11 falsification clause together with SOW-085", and `SOW-085`, whose own scope-item statement names the clause — while `SOW-093` carries no falsification annotation. The upstream schema contract obliges the type but no accepted source obliges a producer discriminator on it. REQ-010 binds this deliverable's side of the boundary — its findings are attributable to this path and never presented or counted as parity output — while recording that the field or mechanism carrying that attribution is the schema owner's decision. Neither this contract nor its production may fix that field. `PRD.md` v2.4 `PEC-RCN-002` further names a divergence between PEC's declared census population and the harness `status_glob` as a DriftFinding ("divergence is a DriftFinding"); the upstream schema contract records that case as `DEL-01-01/CON-008`, it is not this classifier's path, and REQ-010 is unchanged by it.

- **CON-006** — The lag classes are stated over a relation between a work graph and Git — a node's declared state lagging, or behind, what Git records — while `SOW-019`, `PEC-RCN-004` and the §7.1 DriftFinding row define drift over successive snapshots (CLM-001, CLM-002, CLM-004, CLM-015). No accepted source states whether graph-behind-Git is detected as a difference between two successive snapshots, such as a later snapshot recording a cited PR merged while the node's declared state is unchanged, or by comparing one snapshot's declared node states with the merge reachability that snapshot records; the second is a comparison the §7.1 row does not name. Nor does any accepted source state that the snapshot pair carries a node's terminal status and its cited PRs' local merge reachability as record-tier facts, although the work-graph parser is obliged to resolve cited PR numbers to local merge commits (CLM-015). REQ-015 and REQ-016 bind the classifier to those facts as its inputs carry them and to deriving neither; which comparison the lag classes denote is a scope question for `SOW-019` and the register `Description`, not a production decision.
- **CON-007** — The register `Description` does not define "historical surfaces". `PRD.md` v2.4 declares historical status per loop and per feed — a receipt ledger "is live or declared historical per its loop's feed profile" — and indexes workplans "as history only", and the applied `D-PEC-96` registry lists PEC's `loop-receipts-ledger` and `agentruns-json` profiles as historical and `shared-dev-loop` as live (`v2/config/loops.json`). Whether the lag class's "historical surfaces" means exactly the surfaces a loop's feed profile declares historical, or also other surfaces the method keeps as history, is not stated, and the answer changes which unchanged surfaces REQ-017 protects. REQ-017 takes historical status from what the inputs declare and decides none; settling the set belongs to the feed-profile owner `DEL-01-06` or to a scope-change question.

## Production and Verification Method — Praxeology

Production proceeds in the order upstream-contract survey → snapshot-pair
acquisition and comparison surface → class set and its declared record →
content-minimal and never-modify boundaries → limitation carry-through and
producer attribution → determinism → tests, because each stage is the
acceptance surface of the next and because the class set cannot be declared
until there is exactly one comparison surface to classify over. The
upstream-contract survey comes first because the single predecessor at
`INITIALIZED` supplies obligations rather than artifacts, and a comparison
written against an imagined snapshot artifact would violate CON-002 before any
code existed. All work is bounded to this deliverable folder and the `PKG-03`
service-core source it names; this contract authorizes no register,
decomposition, PRD, or upstream-deliverable edit, and it neither defines nor
reshapes the entity type it reports into, the store it writes through, or the
reconcile paths that produce its inputs. Tests implement the verification
methods below and create no scope.

- **VER-001** — Classification exercise: run the classifier over fixture snapshot pairs seeded with addition, removal, modification, and no-change cases, and assert per case that every seeded difference is found and carries exactly one declared class; seed a difference outside the declared class set and assert it is reported unclassified with a stated reason rather than dropped.
- **VER-002** — Input-boundary inspection: instrument or inspect the classifier's acquisition surface and assert both snapshots are obtained through the upstream record-tier interface; grep this deliverable's source for reconcile paths, snapshot construction, feed grammar definitions, and feed-file reads, asserting none is present.
- **VER-003** — Type-boundary inspection: assert every finding produced is constructed against the upstream-obliged DriftFinding type; grep this deliverable's source for record-tier and presence-tier type definitions and assert none; grep source and fixtures for any assumption that an upstream schema, store, reconciler, or parser artifact exists, asserting none.
- **VER-004** — Write-boundary exercise: hash the fixture source corpus tree before and after a classification run and assert byte-identity; capture every filesystem open and write performed during the run and assert no source file is opened for reading or writing and every write resolves under the store through the upstream ingest boundary; inspect the module's call graph and assert no write, create, or delete call targets a source file, governed file, register, lifecycle file, or generated view.
- **VER-005** — Content-minimal inspection: run the classifier over a content-dense fixture pair whose differences fall in long prose bodies, quoted authored text, and diff-shaped content, then dump every field of every finding produced and assert field by field that none carries file or diff content and that the changed text cannot be reconstructed from the finding.
- **VER-006** — Explainability exercise: for every finding produced across the VER-001 fixture set, assert the presence of both snapshots' examined-through SHAs, the assigned class, and a rule identity; resolve each rule identity against the declared class-set record and assert it is present there; compare the record's class enumeration against the classes the classifier can assign and assert set equality.
- **VER-007** — Judgment-boundary inspection: inspect the classifier's parameter and configuration surface and assert no judgment, override, or manual-adjustment input exists; independently re-derive every class from the two snapshots and the declared rule set and assert the re-derivation reproduces the classifier's output exactly.
- **VER-008** — Determinism: run the classifier twice over the same fixture snapshot pair and assert identical finding sets in identical order; run it a third time over the already-classified pair and assert no difference.
- **VER-009** — Limitation carry-through: run the classifier over fixture pairs in which one snapshot reports a feed absent, unreadable, malformed, stale, and grammar-unrecognized in turn, and assert per case that the result carries the reported limitation naming the loop and the feed and that no case is presented as drift in the sources.
- **VER-010** — Producer-attribution exercise: assert every finding produced is attributable to snapshot-to-snapshot classification; grep this deliverable's source for parity-diff paths and practitioner-harness output readers and assert none; inspect the export and counting surface and assert no finding is emitted in a form that presents it as parity output.
- **VER-011** — Boundary inspection: inspect the module's call graph and source for full-rebuild, Git-delta incremental, parity-diff, source-resolution, stream-loss recovery, performance measurement, caller-SHA delta, stamping, citation-attachment, pressure-rule, density, threshold, dashboard, census, metric, gate-evaluation, and store-lifecycle paths, asserting each absent; review this deliverable's tests for any criterion belonging to another deliverable, asserting none.
- **VER-012** — Stand-in discipline: enumerate every upstream dependency in source and tests and assert each resolves to an interface-level fixture stand-in for a contract obligation; re-run the exercise against the live upstream reconciler and schema once those deliverables are available, without discharging either here.
- **VER-013** — Inspect the `PKG-03` dependency manifest and this module's import graph for third-party runtime dependencies and network calls, and re-run the `DEL-01-05` zero-dependency and locality enforcement once that deliverable is available, without discharging it here.
- **VER-014** — Run the `PKG-03` test suite and confirm that each of VER-001 through VER-013 and VER-015 through VER-017 has a corresponding executing automated test and that no test asserts a criterion absent from this contract.
- **VER-015** — Terminal-lag exercise: run the classifier over fixture pairs with a terminal work-graph node lagging after its final-PR merge and assert the class "trailing by method design" with no DriftFinding for that difference; repeat with the node's terminal status or its cited PRs' merge reachability absent from the fixture and assert an unclassified result with a stated reason; grep this deliverable's source for work-graph parsing, PR-to-merge-commit resolution and terminal-completion derivation, asserting none.
- **VER-016** — Graph-behind-Git exercise: run the classifier over fixture pairs with a non-terminal work-graph node behind Git and assert a DriftFinding carrying both snapshots' examined-through SHAs, its class and a rule identity that resolves to the declared class-set record.
- **VER-017** — Historical-surface exercise: run the classifier over fixture pairs in which surfaces the inputs declare historical are unchanged and assert that no finding and no class reports any of them as stale.

## Governing Values and Decisions — Axiology

- **AX-001** — `OBJ-002` governs: staleness is detected structurally by SHA comparison, never by judgment. This deliverable is where the second half of that claim is either true or false, because classification is the step at which a judgment would most naturally enter — someone deciding which differences matter. REQ-007 removes the opportunity rather than discouraging it: there is no input through which a judgment could be supplied.
- **AX-002** — `PEC-K-04` is `OBJ-002`'s product invariant and reads "Staleness is a comparison." The upstream determinism obligation is what makes that literally true here: because two reconciles over unchanged sources are obliged to produce the same record tier, a difference between successive snapshots is a property of the sources and not of the run (CLM-009). A non-deterministic classifier would convert the same evidence into a different verdict on a second look, which is the failure `PEC-K-04` names one level up. REQ-008 is the inward form of the same rule.
- **AX-003** — The never-modify-a-source-file limb is not hygiene, and the PRD says so in this deliverable's own requirement. The §6 invariant-lineage paragraph records that "PEC-K-06 carries PEC-I-12 (verification creates findings, never rewrites sources — cf. PEC-RCN-004)" — the one place in the accepted corpus where an invariant's lineage cites this deliverable's source requirement by name. A drift classifier that could write a source file would be a verifier that resolves its own findings, and the finding would stop being evidence about the sources. REQ-004 states the restriction as a checkable boundary, and REQ-002 makes it structural: a classifier whose inputs are snapshots has no source-file handle to misuse.
- **AX-004** — The same PRD limb is carried by two contracts and that is by design, not duplication. `PEC-RCN-004`'s second limb is discharged by the full-rebuild reconciler for its own act, under `SOW-021`'s store-only write restriction (CLM-009), and it is discharged here for this act because it is the literal text of this deliverable's own scope-ledger row (CLM-001). Neither discharge covers the other: each act needs its own boundary, and a shared invariant enforced in one place only is enforced nowhere the enforcer does not run.
- **AX-005** — `PEC-K-10` content-minimal is a residency posture, and this deliverable is the single place in `P1` where it is under the most pressure. A classifier's natural output is "here is what changed", and the most useful form of that answer is the changed text — which is exactly what PEC may never hold. The strongest enforcement is upstream, in a schema with nowhere to put prose and a guard that refuses it at ingest (CLM-007), but neither knows what a classifier was tempted to compute, so REQ-005 binds the finding's content directly and VER-005 exercises it against the densest fixture available.
- **AX-006** — `PEC-K-08` explainability is why a class token is not a sufficient output. "Every status, verdict, and warning carries rule ID, threshold, and contributing cited sources. Drill-down never dead-ends." A classified difference is a derived verdict; without the two snapshot SHAs and the rule that assigned the class it is an assertion the consumer cannot check, and the downstream pressure rule that would consume it is itself obliged to be Explain-shaped (CLM-010). REQ-006 makes this deliverable's half of that chain resolvable.
- **AX-007** — `PEC-ORI-006` honesty governs the boundary between drift and coverage. An unread feed and a deleted fact are structurally identical at the comparison surface, and the difference between them is the difference between a system that reports what changed and one that reports what it failed to read as though it changed. CON-004 records that the accepted sources do not settle which it is; REQ-009 makes the answer visible either way rather than resolving it by implementation.
- **AX-008** — One entity type with two producers is a boundary that erodes silently. The §11 parity metric counts one producer's findings; the §11 falsification clause rests on other scope items, which the ledger names — the `SOW-060` `Notes` cell reads in full "Measures uptake of SOW-004; no receiving-loop conformance criterion; supports the §11 falsification clause together with SOW-085", and `SOW-085`'s own scope-item statement names the clause, while `SOW-093`, the parity-metric row, carries no falsification annotation at all — and nothing in the accepted corpus obliges the type to say which producer made a given finding (CON-005). This contract holds its own side of the line — REQ-010 — and declines to fix the discriminator, because a production choice here would settle a schema question in the wrong deliverable.
- **AX-009** — The edges cited in this contract are `PROPOSAL` and `DERIVED` stratum and are *accepted* at those strata: `D-PEC-62` §1 item 4 records the owner accepting the DAG candidate v0.2 exhibit "accepted, all strata as presented", and that packet reads "as presented" as accepting the exhibit's **flags as flags**, so what remains recorded-but-unresolved is the specific annotated set — `E-A11` (AMBIGUOUS_BASIS), `E-P69`/`E-N02` (PHASE_TENSION), `E-N13`/`E-N18` (LOW_CONFIDENCE), the `C-02` direction, and the `C-08` standing-node set — none of which touches either edge cited here; both edges named in this contract carry an empty `Flag` column in the exhibit. Stratum is provenance, not authority: it records how an edge was derived, not whether it has been accepted, and citation does not convert `PROPOSAL` to `DECLARED`. Nor does an edge's thin evidence trail weaken its acceptance — the upstream edge's empty exhibit `BasisCitation` (CLM-008) leaves its accepted basis in the two contracts, which is what this contract binds to; the register row's `EvidenceQuote`, empty at authoring, now quotes `PEC-RCN-004` (CLM-008).
- **AX-010** — Edge direction is a constraint on this contract, not a licence. `RequiredMaturity` `INITIALIZED` on the single upstream edge means the upstream *contract* is the reliable input, not any upstream artifact; this contract is written against the obligations quoted in CLM-007 and CLM-009 and asserts nothing about upstream implementation state. Consuming one contract imposes no obligation on it, and being consumed by a downstream pressure-rule deliverable neither expands this contract's scope nor transfers any of that deliverable's into it — this contract defines no density, no threshold, and no rule.
- **AX-011** — Unknowns stay marked. TBD-001 through TBD-005 and CON-001 through CON-007 are recorded rather than resolved by inference, and three of them — the regenerability of a difference against a deleted prior state, the referent of "snapshot", and the producer discriminator — are questions this deliverable is merely the first to meet, not questions it is entitled to answer. `C-03` `PACKAGE_LEVEL`, `C-04` `PHASE_PRECEDENCE`, and `C-10` `STRATUM_RULE` are register-wide non-gating constraints recorded in `_DEPENDENCIES.md`, and blocker output under the `FULL_GRAPH` mode at threshold `INITIALIZED` is advisory visibility only, never work assignment.
- **AX-012** — This contract is lifecycle-neutral. `_STATUS.md` remains the sole lifecycle authority and is untouched by the run that authored this document; at `125cfacc1` the deliverable is at `INITIALIZED` and nothing has been built (CLM-014).
- **AX-013** — Currency provenance. This contract is the prior contract (SHA-256 `5ce8ab72425ab417c90c3e64a152912a7e39b243f3905e65477dbfd91a40eaa7`) brought current under the S1 Scope of Work currency packet (provisional `D-PEC-104`), authored under `MODE=INIT` discipline against revision 1.6 and PRD v2.4. What changed: the frontmatter pin, which formerly named the unresolvable `3623b958b`; the basis paragraph, which keeps revision 1.2 as the dated authoring basis; the observation-commit paragraph; the false statement that `_REFERENCES.md` still names revision 1.1, replaced by the ruled `D-PEC-99` wording, with the Ontology and TBD-001 references to `_CONTEXT.md` text removed to match it; re-quotations at `125cfacc1` (the revision-1.6 `OBJ-002` cells in CLM-003, the §9 locator of the vocabulary map, the verbatim OrientationSnapshot gloss in CON-002, the PRD §7.1 and vocabulary-map wording in TBD-002, and the `SOW-060` `Notes` cell in CON-005 and AX-008); the `DEL-01-01` quotation in CLM-007, brought current to its `D-PEC-100` contract (sixteen types); stale state claims (lifecycle `INITIALIZED` in CLM-014 and AX-012, and the CLM-009 existence statement, narrowed to what is observable, since a store slice of another deliverable now exists under `v2/src/pec_v2/`); the SCA-005 cause, action `A-21`'s lag classes, carried as CLM-015, REQ-015 through REQ-017, AC-016 through AC-018, VER-015 through VER-017, TBD-005, CON-006 and CON-007, with the consequential REQ-003 exception, TBD-002 narrowing, CLM-005 re-quotation, CLM-011 phase check, AC-014, VER-014 and AX-011 ranges, and a CON-005 note on the PRD v2.4 `PEC-RCN-002` DriftFinding text; and the `D-PEC-99` exhibit Part B item `DEL-03-03-REM-004`, applied verbatim in CLM-008 and AX-009 under its gate. No ID is retired. Every other ID is kept with its meaning. New: CLM-015, TBD-005, REQ-015 through REQ-017, AC-016 through AC-018, VER-015 through VER-017, CON-006, CON-007 and AX-013.

**Quotation record.** Every quotation in this contract is verbatim from the
named source, and **none is elided**: no quotation in this document omits text
from the span it presents, and there is therefore no truncated quotation to
enumerate. Where a quotation presents one cell, one row, or one record, that is
stated at the point of quotation and the cell, row, or record is complete.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-019 OBJ-002 | REQ-001, CLM-001, CLM-002, CLM-005, TBD-002, TBD-003 | AC-001 | VER-001 | Classification results over the seeded fixture pairs (addition, removal, modification, no-change) with each difference carrying exactly one declared class, plus the unclassified-with-reason case |
| OUT-001 | SOW-019 OBJ-002 | REQ-002, CLM-009, CLM-013, CON-003 | AC-002 | VER-002 | The instrumented snapshot-acquisition surface for a classification run, plus a recorded search of this deliverable's source for reconcile paths, snapshot construction, feed grammars, and feed-file reads |
| OUT-001 | SOW-019 OBJ-002 | REQ-003, CLM-004, CLM-007, CON-002 | AC-003 | VER-003 | The finding construction surface against the quoted upstream type obligation, plus recorded searches for record-tier and presence-tier type definitions and for upstream-artifact assumptions |
| OUT-001 | SOW-019 OBJ-002 | REQ-004, CLM-001, CLM-002, CLM-012, AX-003, AX-004 | AC-004 | VER-004 | Before/after fixture-corpus tree hashes; the captured filesystem open/write inventory for a classification run showing no source-file handle; the call-graph inspection record showing every store write through the upstream ingest boundary and no write against a source, governed, register, lifecycle, or view path |
| OUT-001 | SOW-019 OBJ-002 | REQ-005, CLM-007, AX-005 | AC-005 | VER-005 | Field-by-field dumps of every finding produced over the content-dense fixture pair, showing no file or diff content and no reconstructible changed text |
| OUT-001 | SOW-019 OBJ-002 | REQ-006, CLM-010, AX-006 | AC-006 | VER-006 | The classifier's declared class-set record; per-finding basis fields (two examined-through SHAs, class, rule identity) resolved against that record; the class-set-versus-assignable-classes set-equality result |
| OUT-001 | SOW-019 OBJ-002 | REQ-007, CLM-003, CLM-007, AX-001 | AC-007 | VER-007 | The parameter and configuration surface inspection showing no judgment input, plus the independent re-derivation reproducing the classifier's output exactly |
| OUT-001 | SOW-019 OBJ-002 | REQ-008, CLM-009, AX-002 | AC-008 | VER-008 | Two-run finding-set comparison over an unchanged fixture pair plus the third-run idempotence result over the already-classified pair |
| OUT-001 | SOW-019 OBJ-002 | REQ-009, CON-004, AX-007 | AC-009 | VER-009 | Per-case classification results for absent, unreadable, malformed, stale, and grammar-unrecognized feeds, each showing the loop and feed named and the limitation carried rather than classified as source drift |
| OUT-001 | SOW-019 OBJ-002 | REQ-010, CLM-004, CLM-012, CON-005, AX-008 | AC-010 | VER-010 | The producer-attribution record for every finding produced, a recorded search for parity-diff paths and harness-output readers, and the export/counting surface inspection |
| OUT-001 | SOW-019 OBJ-002 | REQ-011, CLM-006, CLM-011, CLM-012, AX-010 | AC-011 | VER-011 | Call-graph and source inspection records showing each named adjacent path absent, plus a review of this deliverable's tests confirming no criterion belonging to another deliverable |
| OUT-001 | SOW-019 OBJ-002 | REQ-012, CLM-008, CLM-009, CON-001 | AC-012 | VER-012 | The enumerated upstream-dependency list with each resolved to an interface-level fixture stand-in, plus a recorded search of source, fixtures, and call surface for upstream-artifact assumptions |
| OUT-001 | SOW-019 OBJ-002 | REQ-013 | AC-013 | VER-013 | Dependency-manifest and import-graph inspection records, plus the DEL-01-05 enforcement result once that deliverable is available |
| OUT-001 | SOW-019 OBJ-002 | REQ-015, CLM-005, CLM-015, TBD-005, CON-006 | AC-016 | VER-015 | Per-case results over terminal-lag fixture pairs showing the "trailing by method design" class and no DriftFinding, the unclassified-with-reason result where the fixture omits the node's terminal status or merge reachability, and a recorded search of this deliverable's source for work-graph parsing, PR resolution and terminal-completion derivation |
| OUT-001 | SOW-019 OBJ-002 | REQ-016, CLM-005, CLM-015, CON-006 | AC-017 | VER-016 | DriftFindings over graph-behind-Git fixture pairs, each with its basis fields resolved against the declared class-set record |
| OUT-001 | SOW-019 OBJ-002 | REQ-017, CLM-005, CLM-015, CON-007 | AC-018 | VER-017 | Classification results over fixture pairs with unchanged declared-historical surfaces, showing none reported as stale |
| OUT-002 | SOW-019 OBJ-002 | REQ-014, CLM-014 | AC-014 | VER-014 | PKG-03 test-run output mapping each executed test to its declared verification method, with no criterion asserted that this contract does not state |
| OUT-001 | SOW-019 OBJ-002 | CLM-003, AX-009, AX-011, AX-012, AX-013, TBD-001, TBD-004 | AC-015 | HUMAN_REVIEW: REVIEW gate confirms traceability to SOW-019 and OBJ-002, confirms the objective mapping is stated as register-direct and pre-SCA-002 with no confidence label the record does not assign, and confirms no upstream, sibling, or cross-package scope absorption | Review record citing the scope-ledger row, the SCA-002 A001 target list and A003b OBJ-002 old/new cells, the register-precedent measurement, and the upstream, sibling, and cross-package deliverable boundaries |
