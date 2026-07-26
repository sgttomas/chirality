---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-03-04
package_id: PKG-03
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@3623b958b
project_scope_refs: [SOW-020]
package_objective_refs: [OBJ-006]
---

# Scope of Work — DEL-03-04 Practitioner-harness parity diff

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-03-04` —
"Practitioner-harness parity diff" — in `PKG-03` Reconciliation & Parity of the
PEC v2 build. It covers project scope item `SOW-020` in service of package
objective `OBJ-006`.

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.2** (`status: current_basis`, `SCA-002` successor accepted
2026-07-25 under `D-PEC-64`), pinned at commit `3623b958b`. The
deliverable-local `_REFERENCES.md` still names "revision 1.1, accepted working
surface"; that phrase is superseded provenance awaiting a deferred pointer
sweep (`SCA-002` `Handoff_State.md`, open item `OI-B`, dispositioned
`DEFERRED_BY_HUMAN`), and `_CONTEXT.md` records revision 1.1 as "superseded by
revision 1.2 (`current_basis`, SCA-002 successor)". This contract cites
revision 1.2.

**Standing character (load-bearing), and what authorizes it.** Everything below
is written as a contract on a *continuing* comparison: there is no state in
which this deliverable's assertion is finished, and a parity-clean run is
evidence for the source state it compared and for no later state. That framing
is directed by this run's brief under `D-PEC-63`, whose directing sentence
reads, verbatim:

> Author this contract as a STANDING assertion — a continuously re-runnable
> verification, not a one-shot artifact.

That sentence is carried durably at
`execution/_Coordination/WAVE_D-PEC-63/BATCH_B5_FANIN.md`, the batch fan-in
record for the batch this run belongs to, which the dispatcher writes in this
tranche and which records it verbatim. The framing is also **register-directed**
in a way the sibling standing nodes are not: the deliverable's own register
`Description` opens with the word "Permanent" (CLM-006), the `SOW-020` ledger
row's `Notes` cell reads "Permanent (C10)" (CLM-001), and the hard constraint
that note points at is itself stated as a permanence rule (CLM-004). The
framing is additionally informed by, not derived from, the `C-08`
`STANDING_NODES` annotation described in CLM-008 — an annotation whose own
`Provenance` cell cites this deliverable's word "Permanent" as its evidence.
Standing shape is therefore a property of how this contract is written and of
what the register says. It is **not** an owner-ruled gating force, and the
question of whether this parity gate carries release-gating authority is routed
to the owner under CON-001 rather than assumed here.

**Objective warrant.** The `SOW-020` → `OBJ-006` attribution is
**register-direct and pre-`SCA-002`**. It is stated at that strength and no
higher, and it creates no owner-confirmation obligation. Two independent
confirmations, both from the `SCA-002` record. First, `SCA-002`'s action
`A001` enumerates the twenty `IN` ledger rows whose empty `ObjectiveIDs` cells
it populated —

> | A001 | `MODIFY` | `OBJECTIVE` | `ScopeLedger.csv` `ObjectiveIDs` — **20 IN rows** (`SOW-001, 003, 011..017, 021, 025, 040, 042, 052, 053, 054, 056, 088, 089, 094`) | Populate `ObjectiveIDs` with bare `;`-separated `OBJ-NNN` tokens, derived by the intake §4 attribution method. **Binding constraint: `SOW-021` ⊆ `{OBJ-005}`** (see F-2) | Unit Ledger (§6 + `ScopeLedger.csv`) |
>
> (`execution/_ScopeChange/SCA-002_2026-07-25_1042/Brief.md`, action register,
> row `A001`, quoted in full under the register's own columns. ID-shaped text
> inside this quotation is upstream source context, not a local definition or
> reference.)

— and `SOW-020` is not among them: its `ObjectiveIDs` cell already read
`OBJ-006` before that scope change. Second, the `SCA-002` Gate 5 verification
records the `OBJ-006` §3 row as untouched by the amendment:

> | 4v | §3 ↔ register parity | **PASS** — all six objectives MATCH (20/12/12/10/7/9); `OBJ-003` and `OBJ-006` rows untouched; §7 `ContextEnvelopeCounts` unchanged; `status` and `source_corpus` unchanged |
>
> (`execution/_ScopeChange/SCA-002_2026-07-25_1042/Decision_Log.md`, Gate 5
> verification table, row quoted in full. ID-shaped text inside this quotation
> is upstream source context, not a local definition or reference.)

The `Amendment_Preview.md` objective-delta table states the same from the
deliverable side: its `OBJ-006` row reads "| OBJ-006 | 9 | 9 | — |" under the
columns `Objective | Items | Dels | Δ dels` — zero deliverable rows added. The
`Deliverables.csv` `SupportsObjectives` cell `OBJ-006` for this deliverable is
therefore not `SCA-002`-authored, and this contract supplies no fresh
derivation of it, asserts no confidence label for it (the record assigns none),
and mints **no** owner-confirmation acceptance criterion for it. The
owner-confirmation criterion this contract does carry, AC-016, is about the
`C-08` standing classification's gating force (CLM-008, CON-001) — a separate
question that touches neither the scope-item coverage nor the objective
mapping.

- **CLM-001** — The accepted `ScopeLedger.csv` row for `SOW-020` reads in full, with all ten fields shown under the register's column order `ScopeItemID,InOutStatus,ScopeItemStatement,SourceRef,PackageID,DeliverableIDs,ObjectiveIDs,DecisionRef,OpenIssue,Notes`:

  > `SOW-020,IN,Parity-diff PEC derivations against practitioner-harness output; surface discrepancies as DriftFindings resolved against live sources,PEC-RCN-005,PKG-03,DEL-03-04,OBJ-006,,FALSE,Permanent (C10)`
  >
  > (`DecisionRef` **empty** — no boundary decision rides this scope item;
  > `OpenIssue` `FALSE` — no open issue is attached; `Notes` "Permanent (C10)".
  > ID-shaped text inside this quotation is upstream source context, not a local
  > definition or reference.)

  The `SOFTWARE_DECOMP.md` §2 SSOW row for the same item repeats the statement without the register-only columns: "| SOW-020 | IN | Parity-diff PEC derivations against practitioner-harness output; surface discrepancies as DriftFindings resolved against live sources | PEC-RCN-005 | Permanent (C10) |".

- **CLM-002** — `SOW-020`'s `SourceRef` cell names one locus, `PEC-RCN-005`, a `PRD.md` §9.2 reconciliation requirement, quoted here in full as it reads: "PEC derivations shall be parity-diffable against practitioner-harness output; discrepancies are surfaced as DriftFindings and resolved against live sources." Its §9.2 neighbour `PEC-RCN-004` fixes the posture of every finding-producing act in that section, quoted in full: "The reconciler shall classify drift between successive snapshots and report it; it shall never modify a source file." The `PRD.md` §6 invariant-lineage paragraph records the same rule as the lineage of `PEC-K-06`: "verification creates findings, never rewrites sources — cf. PEC-RCN-004".
- **CLM-003** — `OBJ-006` states: "The product thesis remains measurable and falsifiable: adoption, parity, defect, and collision metrics are gathered in system behavior and the §11 falsification clause stays armed", `SourceRef` `§11`, with mapped scope items "SOW-020, SOW-057..060, SOW-064, SOW-084, SOW-085, SOW-093" and `MappedDeliverables` "DEL-01-04, DEL-03-04, DEL-10-01, DEL-10-04, DEL-10-05, DEL-10-09, DEL-10-10, DEL-10-11, DEL-10-12" (`SOFTWARE_DECOMP.md` §3 objectives table; `PRD.md` §11). `SOW-020` is the only `PKG-03` member of that scope-item set: this deliverable is the single behavioural contribution `PKG-03` makes to the falsifiability objective, and it makes it by producing the comparison whose findings the §11 parity metric counts.
- **CLM-004** — The `Notes` token "(C10)" in the `SOW-020` row resolves to decomposition hard constraint `C10`, quoted in full from `SOFTWARE_DECOMP.md` §1.3 "Hard constraints (identified at intake)" under its columns `# | Constraint | Source`: "| C10 | Permanent parity-diff against the practitioner harness; PEC neither directs the harness nor opens its cache half | PEC-RCN-005, PRD §15 |". The resolution is checkable rather than assumed: the row's own `Source` cell names `PEC-RCN-005` as its first locus — the whole of `SOW-020`'s `SourceRef` (CLM-001, CLM-002) — and its `Constraint` text carries the same word — "Permanent" — that the ledger `Notes` cell carries. This `C10` is a **decomposition** constraint label and is distinct from the deliverable-local dependency-register constraint row `C-10` `STRATUM_RULE` recorded in `_DEPENDENCIES.md`; the same distinction is drawn in the accepted `DEL-10-01` contract, which states it of the identical pair. The two labels share no register, no numbering series, and no subject: `C10` fixes the permanence and the non-direction of the harness comparison; `C-10` fixes how a dependency edge's stratum is assigned. Where this contract says `C10` it means the decomposition hard constraint, and where it says `C-10` it means the stratum rule (AX-008).
- **CLM-005** — Three accepted statements place the harness comparison in the product, each quoted in full. The permanent-peer non-goal, `PRD.md` §4.2 ("PEC is not (non-goals, permanent)"): "**Not the practitioner harness's replacement.** The harness remains an independent deterministic checker; PEC parity-diffs against it permanently." The §11 success metric, item 5: "Parity: DriftFindings against practitioner-harness output per reconcile." And the §12 release-strategy row for the phase this deliverable is hinted to, under the columns `Phase | Scope | Exit test`: "| **P1 — One-loop reconciler** | Reconciler + orientation store + API for one loop (piping or root), read-only | Parity-diff vs harness clean or explained; rebuild-from-scratch ≤ bound; kill test passes |". The §11 metric is `DEL-10-11`'s to report (CLM-013) and the §12 exit test binds a release phase rather than this mechanism's authority; what both establish here is that the comparison is a continuing product obligation, not a one-time artifact. The undefined term "explained" in that exit test is CON-002.

## Deliverable Definition — Ontology

`DEL-03-04` is typed `BACKEND_FEATURE_SLICE` at Context Envelope `M` with
`PhaseHint` `P1`. `Deliverables.csv` records its `AnticipatedArtifacts` as
"Parity tool + tests" and leaves `ContextEnvelopeNotes` empty, so there are no
envelope notes to carry forward and `_CONTEXT.md` records "(none)". The outputs
of this contract are bounded by that artifact naming: exactly the parity tool
and its tests, and nothing beyond those two artifacts and the components each
of them declares as part of itself.

- **OUT-001** — A parity-diff tool in the PEC service core: it compares PEC derivations against practitioner-harness output over one examined source state, surfaces each discrepancy as a record-tier DriftFinding carrying the citation to the live source against which it is resolved, and is built so that the comparison is re-performed on every subsequent reconcile and release candidate without further action. The tool's **declared comparison record** — the readable artifact in which it declares which PEC derivations it compares, which harness output each is compared against, and the equivalence rule applied (REQ-012) — is a component of this output rather than a third artifact: it is the tool's own self-declaration, so the register's naming of exactly two artifacts is preserved.
- **OUT-002** — An automated parity test suite covering the comparison, the finding-production path, the read-only posture toward both sources and the harness, and the degraded-input behaviour, implementing the verification methods declared in this contract.

### Identity of record

- **CLM-006** — `DEL-03-04` is named "Practitioner-harness parity diff", Type `BACKEND_FEATURE_SLICE`, Context Envelope `M`, `PhaseHint` `P1`, `ResponsibleParty` `TBD`, `AnticipatedArtifacts` "Parity tool + tests", `CoversScopeItems` `SOW-020`, `SupportsObjectives` `OBJ-006`, `ContextEnvelopeNotes` **empty**, with the register `Description` field reading "Permanent parity diffing of PEC derivations against practitioner-harness output; discrepancies surfaced as DriftFindings resolved against live sources." Sources: `Deliverables.csv` row `DEL-03-04` and the `SOFTWARE_DECOMP.md` §5 `PKG-03` table row "| DEL-03-04 | Practitioner-harness parity diff | BACKEND_FEATURE_SLICE | M | P1 | SOW-020 |". The `Description`'s first word is "Permanent"; that word, and not an inference from the deliverable's function, is the register's own statement of standing character.
- **CLM-007** — The `PKG-03` package charter (`SOFTWARE_DECOMP.md` §4) is "The guaranteed path from file truth to record tier: one-command rebuild, incremental Git-delta reconcile, drift classification, harness parity diffing, stream-loss recovery guarantee, store-only writes, rebuild performance bounds", covering "SOW-010, 018, 019, 020, 021, 038, 054 (7)", with "Stream ingest mechanics (PKG-07); parsers (PKG-02)" recorded as explicitly out of package scope. Of those seven items this deliverable covers exactly one: harness parity diffing under `SOW-020`.
- **CLM-008** — `DEL-03-04` is named in constraint row `C-08` `STANDING_NODES` of the accepted gate exhibit, quoted in full under the constraints register's columns `ConstraintID,Kind,Parties,Provenance,Statement,Notes`:

  > `C-08,STANDING_NODES,"DEL-01-05, DEL-03-04, DEL-10-02, DEL-10-03, DEL-10-10","Own text: ""Automated assertion"" / ""Permanent"" / ""Runs at every release"" / ""tested property"" / ""standing validation""",Standing obligations: excluded from one-shot COMPLETE/UNBLOCKED arithmetic; they gate releases not successors,R3-F9; owner confirmation requested. DEL-10-10 is the bootstrap progression record itself`
  >
  > (`execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` §4,
  > constraints register. The `Provenance` cell's second quoted phrase,
  > "Permanent", is this deliverable's own register `Description` word (CLM-006).
  > ID-shaped text inside this quotation is upstream source context, not a local
  > definition or reference.)

  At `D-PEC-62` §1 item 4 the owner accepted the DAG candidate, and that packet states its own reading of the acceptance, quoted in full:

  > 4. DAG candidate v0.2 (120 edges: 19 DECLARED / 19 DERIVED / 82 PROPOSAL;
  >    10 constraint rows; 5 STANDING nodes): **accepted, all strata as
  >    presented** — exhibit and basis hashes in
  >    `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md`.
  >    This packet reads "as presented" as accepting the exhibit **flags as
  >    flags** — E-A11 (AMBIGUOUS_BASIS), E-P69/E-N02 (PHASE_TENSION),
  >    E-N13/E-N18 (LOW_CONFIDENCE), C-02 direction, C-08 standing-node set
  >    remain recorded-but-unresolved, non-gating annotations; each flag is
  >    carried verbatim into the seeded rows' `Notes`. The ruling text below
  >    lets the owner confirm or override this reading.
  >
  > (`execution/_Coordination/_DECISIONS/D-PEC-62_project_setup_scaffold_and_local_dependency_registers.md`
  > §1 "Owner direction of record", item 4, quoted in full. ID-shaped text
  > inside this quotation is upstream source context, not a local definition or
  > reference.)

  What is settled is therefore the **arithmetic exclusion**: `C-08` is a non-gating constraint row and this deliverable is excluded from one-shot `COMPLETE`/`UNBLOCKED` counting. What is not settled is the classification's force as a release gate; the row's own `Notes` field records "owner confirmation requested", and the exhibit's node-class paragraph repeats the qualification — the `STANDING` class is described there as "excluded from one-shot COMPLETE/UNBLOCKED arithmetic; gate releases, not successors — pending owner confirmation, constraint C-08". The deliverable-local `_DEPENDENCIES.md` compresses this to "(owner-confirmed at D-PEC-62 ruling)"; that phrase is accurate as to the arithmetic exclusion and overstates the rest, and this contract cites the `D-PEC-62` and exhibit texts over the local paraphrase. CON-001 carries the open half and AC-016 routes it.

- **CLM-009** — The comparison counterpart is external to this deliverable and to PEC. The practitioner harness is a shipped root tool, registered at `tools/REGISTRY.md` as `practitioner_harness/harness.py`, a "Governed read-mostly observation CLI over the pilot roots (adapter manifests at `projects/*/_harness/adapter.yaml`)" with subcommands `status`, `drift`, `self-check`, and `brief`. Its registry row's `Description` cell ends:

  > … Every output is a labeled generated view (D-GOV-01); all file writes contained to `_harness_generated/` only
  >
  > (`tools/REGISTRY.md`, row `practitioner_harness/harness.py`, `Description`
  > cell; **elided** at the leading ellipsis, which stands for the whole
  > preceding subcommand description. ID-shaped text inside this quotation is
  > upstream source context, not a local definition or reference.)

  Its own record closes the cache half, quoted in full:

  > For Chirality governance state and harness projections, the only permitted
  > database pattern is a rebuildable, gitignored cache regenerated from files by
  > one command, safe to delete, never cited as authority (D-GOV-01). This rule
  > does not reach developer tooling caches, and it does not reach engine-owned
  > domain stores (K-DOMAIN-1; D-GOV-01 scope note). No cache is implemented:
  > the Phase 5 cache precondition (query pain) was measured unmet on 2026-07-02
  > (slowest command, `self-check`, ~4 s) and the cache half stays closed until
  > the owner directs otherwise.
  >
  > (`tools/practitioner_harness/README.md` §"Cache contract", quoted in full.
  > ID-shaped text inside this quotation is upstream source context, not a local
  > definition or reference.)

  And `PRD.md` §15 states PEC's posture toward it, quoted in full:

  > - The practitioner harness's cache half remains closed by its own record
  >   (`tools/practitioner_harness/README.md` §Cache contract): its query-pain
  >   precondition was measured **unmet** on 2026-07-02 (slowest command ~4 s).
  >   A `D-PEC-57`/`D-PEC-58` ruling directs the PEC product; it neither directs
  >   the harness nor remeasures that precondition. §11 metric 1 re-measures
  >   Step-0 cost before P1.
  >
  > (`projects/pec/docs/PRD.md` §15 "Governance and compliance posture", final
  > bullet, quoted in full. ID-shaped text inside this quotation is upstream
  > source context, not a local definition or reference.)

  Three consequences bind this contract. The harness is an **independent** checker whose outputs are labeled generated views, so harness output is a comparison input and never an authority. Neither the harness's construction, its behaviour, its configuration, nor its closed cache half is within this contract's scope: `C10` states PEC "neither directs the harness nor opens its cache half" (CLM-004), and re-measuring the query-pain precondition is expressly not PEC's act. And the harness's `_harness_generated/` write containment is the harness's own contract, not a surface this deliverable may write into (REQ-005).

- **CLM-010** — `DriftFinding` is a record-tier entity type owned upstream, not defined here. `PRD.md` §7.1 states it in one row, quoted in full: "| DriftFinding | A classified difference between the current reconcile and the prior snapshot, or between PEC and harness parity output |". Its schema and field set are `DEL-01-01`'s obligation under `SOW-001` — whose statement enumerates "Loop, Workplan/Step/Gate, Receipt, DecisionRow, Fence, Package/Deliverable, DependencyEdge, RunRecord, CandidateBrief, OrientationSnapshot, DriftFinding" — and this deliverable defines no entity type, adds no field, and asserts no upstream artifact exists. The accepted register declares no deliverable-level edge from `DEL-01-01` to `DEL-03-04`; the relation is recorded register-wide as the non-gating constraint row `C-03` `PACKAGE_LEVEL` — "Every PKG-03/04/05 deliverable depends on DEL-01-01 directly or transitively" (`_DEPENDENCIES.md`) — so this contract records the information dependency without asserting a graph edge. The row's own text is what makes CON-004 unavoidable: one type serves two different comparisons.

### Placement in the work graph

- **CLM-011** — This deliverable's `Dependencies.csv` register (`RegisterSchemaVersion` `v3.1`) holds exactly **three** rows: two `ANCHOR` rows — `DEP-03-04-001` (package-local to `PKG-03`) and `DEP-03-04-002` (`SOW-020` requirement trace) — and one `EXECUTION` row. There is one accepted `EXECUTION` upstream edge and no second, quoted here in full under the register's column order `RegisterSchemaVersion,DependencyID,FromPackageID,FromDeliverableID,FromDeliverableName,DependencyClass,AnchorType,Direction,DependencyType,TargetType,TargetPackageID,TargetDeliverableID,TargetRefID,TargetName,TargetLocation,Statement,EvidenceFile,SourceRef,EvidenceQuote,Explicitness,RequiredMaturity,ProposedMaturity,SatisfactionStatus,Confidence,Origin,FirstSeen,LastSeen,Status,Notes`:

  > `v3.1,DEP-03-04-003,PKG-03,DEL-03-04,Practitioner-harness parity diff,EXECUTION,NOT_APPLICABLE,UPSTREAM,PREREQUISITE,DELIVERABLE,PKG-03,DEL-03-01,DEL-03-01,Full-rebuild reconciler (one command),execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command,Parity diff runs over PEC derivations produced by reconcile,execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md,location TBD,,IMPLICIT,INITIALIZED,TBD,PENDING,MEDIUM,EXTRACTED,2026-07-25,2026-07-25,ACTIVE,PROPOSAL; Flag=none; EdgeID=E-P28`
  >
  > (`SourceRef` reads "location TBD" and `EvidenceQuote` is **empty**: the
  > edge's basis is its `Statement` and the two deliverables' own accepted
  > contracts, not a quoted source. ID-shaped text inside this quotation is
  > upstream source context, not a local definition or reference.)

  The gate exhibit carries the same edge under its columns `EdgeID,PredecessorID,SuccessorID,Stratum,EdgeKind,Flag,BasisCitation,Rationale`, quoted in full: `E-P28,DEL-03-01,DEL-03-04,PROPOSAL,CONSUMES,,,Parity diff runs over PEC derivations produced by reconcile` — `Flag` **empty** and `BasisCitation` **empty**, consistent with the register row's own empty `EvidenceQuote`. The edge is `PROPOSAL` stratum and accepted at that stratum (AX-007); its `RequiredMaturity` is `INITIALIZED`, and `DEL-03-01` is at lifecycle state `INITIALIZED`, so the threshold is met and the bound input is that deliverable's accepted **contract**, never any artifact of it.

- **CLM-012** — From `[E-P28]`, the "PEC derivations" this diff compares are what the upstream rebuild is obliged to produce, and their shape, their declaration, and their determinism are that contract's obligations rather than this one's. Four of its records bear on this contract directly:

  > - **REQ-006** — The reconciler shall declare, in the entry point's declared-view record — a readable component of OUT-001 — every generated view it writes: what the view is, where it is located, and the fact that it is fully regenerable by a rebuild and safe to delete. An undeclared write target is prohibited. The warrant for this requirement is `D-GOV-01` Option A, which sanctions writing "labeled generated artifacts (reports, briefs, evidence records) under declared generated paths" and holds any such projection to being "a rebuildable, gitignored projection: safe to delete, regenerated from files by one command, never cited as authority" (CLM-021, CON-001): declaration under a declared path, regenerability, and safe deletion are that ruling's own properties, restated here as a checkable obligation rather than invented by this contract. What this requirement does not settle is which views this reconciler generates or where they live, which is CON-001 and TBD-003.
  > - **REQ-009** — Where an upstream unit reports that a feed is absent, unreadable, malformed, stale, or grammar-unrecognized, the rebuild shall carry that limitation through to its result, naming the loop and the feed, and shall never present a rebuild that could not read a feed as a rebuild that read it. Silent omission is prohibited, per `PEC-ORI-006` ("Where a feed is unparseable or stale, the response shall state the measurement limitation explicitly; silent omission is prohibited"). Rendering such a limitation into an orientation response is `DEL-04-05`'s act under `SOW-009` (CLM-019); this deliverable makes the limitation available to that consumer.
  > - **REQ-010** — The rebuild shall be deterministic and idempotent over its inputs: two rebuilds over the same unchanged sources shall produce the same record tier, and a rebuild over a store already rebuilt from those sources shall produce no difference. This is what makes a later difference between two reconciles a structural fact rather than a judgment (`PEC-K-04`).
  > - **REQ-014** — The reconciler shall perform no act owned by another deliverable. In particular it shall perform no Git-delta-keyed incremental reconcile, no drift classification between snapshots, no parity diff against practitioner-harness output, no stream-loss recovery act, no rebuild-bound measurement or assertion, no examined-SHA or freshness stamping and no per-claim citation attachment onto an orientation response, no gate-precondition evaluation or slate rendering, no locality or zero-dependency enforcement act, and no kill test; each is cited to its owner in CLM-019 and none is discharged here.
  >
  > (`DEL-03-01/ScopeOfWork.md`, Epistemology section; all four records quoted
  > in full, none elided. ID-shaped text inside this quotation is upstream source
  > context, not a local definition or reference — this contract's own `REQ-*`,
  > `AC-*`, `CLM-*`, `TBD-*`, and `CON-*` records are separate and differently
  > worded.)

  The division is symmetric and this contract honours it in both directions. The upstream contract names the parity diff among the acts it does **not** perform; this contract performs exactly that act and performs no rebuild (REQ-013). Two of its unresolved records reach this contract as bounds rather than as questions this deliverable may answer:

  > - **CON-005** — `SOW-010` requires the record tier be rebuildable "in full", while every upstream feed unit is contractually obliged to report feeds it could not read as explicit limitations (CLM-016), and `PEC-ORI-006` prohibits silent omission. No accepted source states whether a rebuild that completed with stated coverage limitations counts as a full rebuild for `SOW-010`'s purposes, or whether "in full" is a claim about the command's reach rather than its coverage. This contract takes neither reading as settled: REQ-001 obliges the command to reach every registered loop and every manifest-named feed, and REQ-009 obliges every gap to be carried through as a stated limitation, so that the question is visible in the result rather than answered by silence. `PRD.md` §12's `P1` exit test names "rebuild-from-scratch ≤ bound" without stating the bound, which `PEC-SVC-003` records as "confirmed at Phase 1"; that measurement is `DEL-03-06`'s under `SOW-054` (CLM-019) and this contract asserts no bound.
  >
  > (`DEL-03-01/ScopeOfWork.md`, Epistemology section, `CON-005` quoted in full,
  > not elided. ID-shaped text inside this quotation is upstream source context,
  > not a local definition or reference.)

  A rebuild that completed with stated coverage limitations is therefore a possible input state of this comparison, and the upstream generated-view instance set is undetermined at that contract's own `CON-001` / `TBD-003`. Both are carried here as CON-006 and neither is resolved by any production choice under this contract.

- **CLM-013** — One downstream consumer relation is recorded against this deliverable in `_DEPENDENCIES.md` and marked informational: `DEL-10-11` (Parity metric (DriftFindings per reconcile)) — `MEASURES` `[E-A18]`. The gate exhibit row reads in full, under its columns `EdgeID,PredecessorID,SuccessorID,Stratum,EdgeKind,Flag,BasisCitation,Rationale`: `E-A18,DEL-03-04,DEL-10-11,DECLARED,MEASURES,,"Deliverables.csv DEL-10-11: ""sourced from DEL-03-04's output""; SOW-093 note: ""Measures the output of SOW-020 (DL-14)""",Parity metric reports DEL-03-04's DriftFindings` — `Flag` **empty**, stratum `DECLARED`. The row holds no entry in this deliverable's `Dependencies.csv`, which contains only the two anchors and the single upstream `EXECUTION` row (CLM-011); the downstream row lives in the consumer's own local register, per the deliverable-local storage ruling of `D-PEC-62` §1 item 3. The relation is directional and runs *away* from this deliverable: `DEL-10-11` is the measurer and this deliverable's findings are the measured surface. The `SOW-093` ledger row states the same division in the register's own words — "Report parity DriftFindings per reconcile as the §11 parity metric", `Notes` "Measures the output of SOW-020 (DL-14); the behavior is PKG-03, the metric is PKG-10". This contract produces the behaviour and the findings; it produces no metric, no report, and no threshold, and it imposes no obligation on that deliverable (REQ-013, AX-006).
- **CLM-014** — Phase staging, checked against the `PhaseHint` column of `Deliverables.csv` for every deliverable this contract names in its own voice: `DEL-03-04` itself, its upstream `DEL-03-01`, its consumer `DEL-10-11`, and the neighbours `DEL-01-01`, `DEL-01-04`, `DEL-01-05`, `DEL-03-02`, `DEL-03-03`, `DEL-03-06`, `DEL-04-03`, `DEL-10-02`, `DEL-10-03`, and `DEL-10-10` are all `P1`. Two exceptions are named, each cited only as the owner of scope this deliverable does not touch: `DEL-10-01` (`pre-P1`; the Step-0 cost baseline that re-measures the harness's query-pain precondition) and `DEL-03-05` (`P3`; the stream-loss recovery guarantee). No claim in this contract stages any named deliverable into a different phase, and the `P1` comparison surface is what the `P1` rebuild produces (CLM-012) and nothing later.

### Boundaries

- **CLM-015** — The acts adjacent to this parity diff are owned elsewhere and are cited here, never discharged. Within `PKG-03`: the one-command full rebuild that produces the PEC side of the comparison is `DEL-03-01` (`SOW-010`, `SOW-021`); incremental reconciliation keyed on Git delta since the last examined SHA is `DEL-03-02` (`SOW-018` — "Run reconciliation incrementally, keyed on Git delta since the last examined SHA"); classification of drift **between successive snapshots** is `DEL-03-03` (`SOW-019` — "Classify and report drift between successive snapshots; never modify a source file"); the stream-loss recovery guarantee is `DEL-03-05` (`SOW-038`, `P3`); rebuild performance bounds are `DEL-03-06` (`SOW-054`). Outside it: the record-tier schema that defines the DriftFinding type is `DEL-01-01` (`SOW-001`); self-observability logging is `DEL-01-04` (`SOW-057`); standing zero-dependency and locality enforcement is `DEL-01-05` (`SOW-052`, `SOW-053`); examined-SHA and freshness stamping with per-claim citation attachment is `DEL-04-03` (`SOW-006`, `SOW-007`); the standing kill test is `DEL-10-02` (`SOW-055`); the tested no-ruling-write property is `DEL-10-03` (`SOW-025`); the directed bootstrap self-ingest validation is `DEL-10-10` (`SOW-064`); the Step-0 cost baseline that re-measures the harness's recorded query-pain precondition is `DEL-10-01` (`SOW-058`, `pre-P1`); and the §11 parity metric over this deliverable's findings is `DEL-10-11` (`SOW-093`). The practitioner harness itself is not a deliverable of this decomposition at all: it is a shipped root tool with its own record (CLM-009). This contract produces only the parity tool and its tests.

  `DEL-03-03` deserves the sharpest line, because it and this deliverable both produce DriftFindings. The two comparisons have different operands and different source rows: `SOW-019` compares **successive PEC snapshots** under `PEC-RCN-004`; `SOW-020` compares **PEC derivations against harness output** under `PEC-RCN-005`. Neither absorbs the other, neither's findings are the other's, and this contract asserts nothing about how that deliverable classifies its own drift. Their shared entity type is CON-004.

- **CLM-016** — The deliverable is at lifecycle state `OPEN` (`_STATUS.md`) with no implementation present, and `_SEMANTIC.md` is empty (0 bytes). Every requirement, acceptance criterion, and verification method below states a contract on future production; none asserts that any tool, comparison, finding, or test has been built, and none asserts that the upstream reconciler exists.

- **TBD-001** — `ResponsibleParty` is unassigned; the register records `TBD`, with assignment at WORKING_ITEMS activation and not in this contract (`SOFTWARE_DECOMP.md` §5 preamble; `_CONTEXT.md`).
- **TBD-002** — The tool's concrete invocation surface — its verb name, its host entry-point form, its arguments, its exit-status contract, and where its output is written — is fixed by no accepted source beyond the register phrase "Parity tool". It is chosen during production within REQ-001 and REQ-005, and any output location it chooses is bounded by the upstream declared-view discipline quoted in CLM-012 rather than invented here.
- **TBD-003** — The **comparable-surface instance set** — which specific PEC derivations have a practitioner-harness counterpart, and which harness output each is compared against — is fixed by no accepted source. `SOW-020` says "PEC derivations" without enumerating them; the harness's registered subcommands (`status`, `drift`, `self-check`, `brief`) cover the pilot roots through adapter manifests (CLM-009), while PEC v2 is described in `PRD.md` §2 as addressing the same class of pain "at OS scale (five loops, concurrent sessions)". The overlap is therefore real but unenumerated. REQ-012 obliges the set to be declared rather than left implicit; CON-002 carries the part of this that is not a production choice.
- **TBD-004** — The **equivalence rule** by which two differently shaped outputs are judged the same or different — normalization, ordering, field correspondence, tolerance — is fixed by no accepted source. It is chosen during production within REQ-012 and declared with the comparable-surface set, so that a discrepancy is attributable to a rule rather than to an undocumented convention (`PEC-K-08`).
- **TBD-005** — The **trigger** of a parity run is fixed by no accepted source. The edge `Statement` says "Parity diff runs over PEC derivations produced by reconcile" and the `SOW-093` metric is stated "per reconcile", which fix the relation between a run and a reconcile but not the mechanism that starts one. Whether the comparison is invoked by the reconcile path, scheduled, or run on demand is a production choice within REQ-007, which binds the standing property — every reconcile and every release candidate is compared — rather than the mechanism.

- **CON-001** — Whether this deliverable's parity gate carries *release-gating authority* is unconfirmed. The `C-08` `STANDING_NODES` row that classifies it records "owner confirmation requested" in its own `Notes`, the exhibit's node-class paragraph repeats "pending owner confirmation", and `D-PEC-62` §1 item 4 accepted the standing-node set as a recorded-but-unresolved, non-gating annotation rather than ruling it (CLM-008). The mechanism this contract requires is designed to block and its verdicts are unambiguous; what is open is whether a blocking verdict binds a release candidate or is advisory. `PRD.md` §12's `P1` exit test — "Parity-diff vs harness clean or explained" (CLM-005) — is evidence that the comparison is release-relevant, but it binds the phase's exit rather than conferring authority on this mechanism, and it does not answer the `C-08` question. AC-016 routes that question to an accountable owner. This contract neither asserts the authority nor waives it, and no production choice may settle it.
- **CON-002** — The `P1` exit test's disjunct "or explained" is undefined by any accepted source. No source states what an explanation of a parity discrepancy is, who accepts one, what state an explained discrepancy occupies, or whether an explanation is durable across later runs. This matters because the difference between "clean" and "explained" is the difference between a mechanical verdict and an accepted judgment, and PEC holds no authority to make the second (`PEC-K-02`, `PEC-GAT-004`, AX-004). This contract therefore obliges the mechanism to report a discrepancy, its rule, and its cited live sources (REQ-004, REQ-010), and obliges it never to present an unexplained discrepancy as clean (REQ-008); it does not define, produce, record, or adjudicate an explanation. Doing so would be a scope-change question for `SOW-020`, not a production decision.
- **CON-003** — `SOW-020`'s clause "resolved against live sources" is not defined by any accepted source, and the corpus constrains it from both sides without settling it. `PEC-RCN-005` repeats it; `PEC-RCN-004` and the `PEC-K-06` lineage state that verification "creates findings, never rewrites sources" (CLM-002); `PEC-GAT-004` prohibits any PEC write path that records adoption, ruling, or direction; and `PEC-ORI-004` requires every claim to carry "a citation (file path, anchor, and/or SHA) to its live source". What is unstated is whether *resolution* is an act PEC performs, an act a human performs against PEC's finding, or simply the requirement that the finding be adjudicable against files rather than against either output. This contract takes the position the invariants force and no more: REQ-004 obliges every finding to carry the live-source citation against which it can be resolved and forbids resolution by preferring either side's output, and nothing in this contract closes, dispositions, or records the acceptance of a finding. Whether closure is owed, and by whom, is carried to the owner at AC-017 rather than answered here.
- **CON-004** — The DriftFinding type is shared. `PRD.md` §7.1 defines one type for two different comparisons — "between the current reconcile and the prior snapshot, or between PEC and harness parity output" (CLM-010) — whose producers are two different deliverables (`DEL-03-03` and this one; CLM-015). No accepted source states how a consumer distinguishes a parity finding from a snapshot-drift finding, and the type's field set is `DEL-01-01`'s obligation, not this contract's. The `SOW-093` metric counts specifically "parity DriftFindings per reconcile", so the distinction is load-bearing for a consumer this contract may not oblige (CLM-013). REQ-003 therefore binds only this deliverable's own side — every finding it produces carries its comparison identity — and defines no field, proposes no schema change, and imposes nothing on either neighbour. Whether the shared type needs a discriminating field is an upstream schema question.
- **CON-005** — The mechanism by which PEC obtains harness output is fixed by no accepted source, and the choice is bounded rather than free. Invoking the harness CLI as a subprocess and reading its labeled `_harness_generated/` outputs are both consistent with the register description (CLM-009), but the service core's toolchain is itself unfixed — the accepted `DEL-01-05` contract records the service-core boundary, the runtime-versus-build dependency distinction, and the toolchain as undetermined — and `PEC-SVC-001` (zero third-party runtime dependencies in the service core) and `PEC-SVC-002` (no external network egress) are standing rules whose enforcement is that deliverable's. Whatever mechanism production chooses must leave those assertions intact (REQ-014), must not direct the harness or alter its inputs, configuration, or state, and must not open or implement its cache half (`C10`, CLM-004, REQ-005). This contract records the constraint and does not choose the mechanism.
- **CON-006** — Two of the upstream contract's unresolved records bound the PEC side of this comparison and are carried, not resolved (CLM-012). First, whether a rebuild that completed with stated coverage limitations is a "full" rebuild is unsettled upstream at its `CON-005`; a parity run over such a rebuild is therefore a comparison over a partially covered derivation set, which REQ-009 obliges the result to say rather than silently reporting parity. Second, which generated views the reconciler produces and where they live is unsettled upstream at its `CON-001` / `TBD-003`, so the enumeration of "PEC derivations" available to compare is not fully determined by any accepted source today; REQ-012 obliges the comparable set to be declared against whatever the upstream declared-view record actually names, and TBD-003 records the remainder. Neither question may be answered by a production choice under this contract.

## Completion and Reliance Basis — Epistemology

The requirements below state the contract the future parity tool must satisfy.
Nothing in this section asserts that a tool, a reconciler, a store, a finding,
or a test exists. Under the standing framing established above —
register-directed by the word "Permanent" and brief-directed, and informed by
the `C-08` annotation (CLM-006, CLM-008, CON-001) — these requirements bind the
mechanism's *continuing* behaviour: each is a property that must hold on every
compared state, not a one-time production event.

- **REQ-001** — The tool shall compare PEC derivations against practitioner-harness output and shall report, for each compared pair, either agreement or a discrepancy, per `SOW-020` (CLM-001) and `PEC-RCN-005` (CLM-002). The comparison shall be performed by the tool itself over both sides' actual outputs, and no agreement shall be reported for a pair the tool did not actually compare.
- **REQ-002** — Every comparison shall be **state-bound**: both sides shall be resolved to the same examined-through commit SHA, that SHA shall be carried on the result, and a comparison whose two sides do not share an examined state shall be reported as an unequal-basis condition rather than as agreement or as a discrepancy, per `PEC-K-04` ("Every response carries the examined-through commit SHA and per-feed freshness; consumers detect staleness structurally"). A difference attributable to differing examined states is a staleness fact, not a parity fact.
- **REQ-003** — Every discrepancy shall be surfaced as a record-tier DriftFinding instance carrying its **comparison identity**: which PEC derivation, which harness output, the examined SHA, and the equivalence rule under which the difference was found. The tool shall define no entity type, add no field to the upstream type, and assert no upstream schema artifact exists; the type and its fields are `DEL-01-01`'s obligation (CLM-010, CON-004).
- **REQ-004** — Every DriftFinding the tool produces shall carry a citation to the live file source or sources against which the discrepancy can be resolved — file path, anchor, and/or SHA, per `PEC-ORI-004` — and the resolution basis shall be those live sources. The tool shall not resolve a discrepancy by preferring PEC's output or the harness's output: neither is authority (`PEC-K-02` "PEC output is never citable as authority"; harness output is a labeled generated view under `D-GOV-01`, CLM-009). The tool shall record no adoption, ruling, disposition, or closure of a finding (CON-003).
- **REQ-005** — The tool shall be read-only over everything it reads. It shall create, modify, or delete no source file, no governed file, no register, and no lifecycle file, per `PEC-RCN-004` and `PEC-K-06`; and it shall write nothing into the practitioner harness's inputs, configuration, state, or `_harness_generated/` output area, shall not direct or alter the harness's behaviour, and shall neither open nor implement its cache half, per `C10` and `PRD.md` §15 (CLM-004, CLM-009). Its own writes shall be confined to the store and to declared generated outputs under the upstream declared-view discipline (CLM-012, TBD-002).
- **REQ-006** — Nothing the tool writes — into a DriftFinding, into a result, or into any declared output — shall carry file content or diff content, per `PEC-K-10` ("Paths, counts, SHAs, states, hashes — never file or diff content"). A difference shall be reported by identity, location, and classification, never by reproducing the differing text of either side.
- **REQ-007** — The comparison shall be **standing**: performed on every reconcile and on every release candidate, against that exact state, per the register `Description`'s "Permanent", the `SOW-020` `Notes` "Permanent (C10)", and `C10`'s "Permanent parity-diff against the practitioner harness" (CLM-001, CLM-004, CLM-006). It shall have no completion state, and no earlier parity-clean run shall be carried forward as evidence for a later state.
- **REQ-008** — The tool shall be designed to block: for a release candidate carrying an outstanding discrepancy, and for one against which the comparison has not been executed or could not complete, the mechanism shall return an explicit blocking verdict rather than agreement, a skip, or an absent result. This requirement binds the mechanism's design intent and the verdict it produces. It does not, by itself, establish that a blocking verdict binds a release: whether the parity gate carries release-gating authority follows the pending `C-08` confirmation recorded at CON-001 and is routed to the owner at AC-016. Nor does it define or accept an "explanation" of a discrepancy (CON-002).
- **REQ-009** — The result shall carry every coverage limitation of the comparison, naming the affected derivation and the reason: a PEC derivation outside the declared comparable set, a harness output unavailable for a derivation, a comparison the tool could not perform, and — where the upstream rebuild reported its own coverage limitations (CLM-012, CON-006) — the fact that the compared derivations were produced by a rebuild that stated them. Silent omission is prohibited, per `PEC-ORI-006`; a partially covered comparison shall never be presented as a parity-clean comparison.
- **REQ-010** — Every verdict and every finding shall be explainable: it shall carry the rule under which it was reached, the equivalence rule applied, and the cited sources contributing to it, per `PEC-K-08` ("Every status, verdict, and warning carries rule ID, threshold, and contributing cited sources. Drill-down never dead-ends").
- **REQ-011** — The comparison shall be deterministic over its inputs: two runs over the same unchanged PEC derivations and the same unchanged harness output shall produce the same verdict and the same finding set. This is what makes a parity difference a structural fact rather than a judgment, and it is the property the upstream rebuild's own determinism obligation (CLM-012) makes available on the PEC side.
- **REQ-012** — The tool shall declare, in its declared comparison record — a readable component of OUT-001 — the comparable-surface set and the equivalence rule: which PEC derivations it compares, which harness output each is compared against, and the normalization and correspondence rules under which agreement is judged. A PEC derivation outside the declared set shall be reported as outside the comparison rather than treated as agreeing, and an undeclared comparison shall not be performed. This requirement bounds TBD-003 and TBD-004 without settling CON-002 or CON-006.
- **REQ-013** — The tool shall perform no act owned by another deliverable. In particular it shall perform no full or incremental reconcile, shall not classify drift between successive PEC snapshots, shall produce no metric, report, threshold, or count presented as the §11 parity metric, shall build, configure, extend, or modify no part of the practitioner harness, shall perform no examined-SHA or freshness stamping onto an orientation response, and shall run no kill test, no locality or zero-dependency enforcement, and no no-ruling-write verification; each is cited to its owner in CLM-015 and none is discharged here.
- **REQ-014** — The tool and its tests shall introduce no third-party runtime dependency into the service core and shall make no external network call, per `PEC-SVC-001` and `PEC-SVC-002`, whose standing enforcement is `DEL-01-05` covering `SOW-052` and `SOW-053`; and neither the tool nor the mechanism it uses to obtain harness output shall make any governed act, or any reconcile, depend on PEC or on the harness being present, per `PEC-K-01` (CON-005).
- **REQ-015** — Tests shall implement the verification methods declared in this contract; they shall not define scope, requirements, or acceptance criteria.

- **AC-001** — Over a fixture pair in which PEC derivations and harness output agree, the tool reports agreement; over fixture pairs seeded with a difference of each supported kind, it reports a discrepancy for each; and inspection confirms no pair is reported as agreeing that the tool did not actually compare.
- **AC-002** — Every result carries the examined-through SHA of both compared sides; a fixture pair whose two sides are drawn from different source states is reported as an unequal-basis condition and is reported as neither agreement nor discrepancy.
- **AC-003** — Every discrepancy appears as a DriftFinding instance carrying the compared PEC derivation, the compared harness output, the examined SHA, and the equivalence rule; and this deliverable's source contains no record-tier entity type definition and no field added to the upstream type.
- **AC-004** — Every DriftFinding carries at least one live-source citation resolvable to a file path, anchor, and/or SHA; no finding's outcome changes when the two sides are transposed; and inspection of the tool's outputs finds no adoption, ruling, disposition, or closure record for any finding.
- **AC-005** — A full run over a fixture corpus leaves the source tree, the governed files, and the harness's own files, configuration, and `_harness_generated/` area byte-identical; no write, create, or delete call in this deliverable's source targets a source, governed, register, or lifecycle file or any harness path; and no cache is created, enabled, or configured for the harness.
- **AC-006** — For a content-dense fixture pair carrying long prose bodies, quoted authored text, and diff-shaped differences, inspection field by field of every DriftFinding and every result finds no file content and no diff content — only paths, counts, identifiers, states, SHAs, and hashes.
- **AC-007** — The comparison executes on every reconcile and on every release candidate in a fixture sequence, each execution bound to the exact state it compared, and no earlier parity-clean result is presented as evidence for a later state; disabling or removing the standing comparison is a visible configuration change reported as a missing comparison rather than a silent no-op.
- **AC-008** — On a release candidate carrying an outstanding discrepancy, and on one against which the comparison was withheld or could not complete, the mechanism returns an explicit blocking verdict. Whether that verdict binds the release is CON-001 and AC-016, not this criterion; and no output of the mechanism records or accepts an explanation of a discrepancy.
- **AC-009** — For fixture cases in which a derivation is outside the declared comparable set, a harness output is unavailable, a comparison cannot be performed, and the upstream rebuild reported its own coverage limitations, the result names the affected derivation and the reason in each case, and no such run is presented as parity-clean.
- **AC-010** — Every verdict and every finding produced over the fixture set carries its rule, its equivalence rule, and its contributing cited sources, and each cited source resolves.
- **AC-011** — Two runs over the same unchanged PEC derivations and the same unchanged harness output produce identical verdicts and identical finding sets.
- **AC-012** — The declared comparison record enumerates the comparable-surface set and the equivalence rule; the set actually compared during a run equals the declared set; a derivation outside it is reported as outside the comparison rather than as agreeing; and no comparison absent from the record is performed.
- **AC-013** — This deliverable's source and call graph contain no reconcile path, no successive-snapshot drift-classification path, no metric or threshold computation presented as the §11 parity metric, no harness build or configuration path, no stamping or citation-attachment path onto an orientation response, and no kill-test, locality-enforcement, or no-ruling-write execution; and no test in this deliverable asserts a criterion belonging to any of them.
- **AC-014** — The tool and its tests add no third-party runtime dependency to the service core and make no external network call, leaving the `DEL-01-05` zero-dependency and locality assertions intact; and with the harness absent, refusing, or erroring, the run reports the limitation explicitly, blocks no reconcile, and blocks no governed act.
- **AC-015** — The parity test suite implements VER-001 through VER-014, executes in the `PKG-03` test run, passes, and introduces no acceptance criterion absent from this contract.
- **AC-016** — An accountable owner confirms, or declines to confirm, that the parity gate delivered under this contract carries release-gating authority — that its blocking verdict blocks a release candidate — given that `C-08`'s standing-node classification carries "owner confirmation requested" in its own `Notes` and was accepted at `D-PEC-62` §1 item 4 as a recorded-but-unresolved, non-gating annotation, and given that `PRD.md` §12's `P1` exit test names parity without conferring authority on this mechanism (CLM-005, CLM-008, CON-001). A decline leaves the mechanism's verdicts advisory and invalidates no other criterion in this contract; the standing framing of the contract stands either way, because it is what the register says and how the contract is written rather than a claim about the gate's force.
- **AC-017** — An accountable owner confirms that nothing delivered under this contract defines, produces, or adjudicates an "explanation" of a parity discrepancy or a closure of a finding, that resolution is carried only as a live-source citation, and that the tool neither directs the practitioner harness nor opens its cache half; and states whether the closure question — who resolves a surfaced discrepancy, and what record that resolution takes — is owed elsewhere (CON-002, CON-003, CON-005).

## Production and Verification Method — Praxeology

Production proceeds in the order comparable-surface declaration → equivalence
rule → comparison and verdict path → finding production with live-source
citation → limitation carry-through → standing registration → tests, because
the comparable set and the equivalence rule are what every later stage is
checked against, and because a comparison written before either is declared
would resolve TBD-003 and TBD-004 silently in code. The harness side is
obtained, never built or altered (CLM-009, CON-005). All work is bounded to
this deliverable's artifacts and the service-core surfaces they read; this
contract authorizes no register, decomposition, PRD, harness, or
upstream-deliverable edit, and constraint `C14` keeps every implementation
tranche dependent on its own owner-ruled packet. The verification methods below
are themselves standing: each is re-run on every compared state, not once at
hand-over. Tests implement these methods and create no scope.

- **VER-001** — Execute the comparison against a fixture pair constructed to agree and against fixture pairs seeded with a difference of each supported kind; assert agreement on the former and a reported discrepancy on each of the latter; instrument the comparison to record which pairs were actually compared and assert no agreement is reported for an uncompared pair.
- **VER-002** — State-binding exercise: run the comparison over a matched-SHA fixture pair and over a deliberately mismatched-SHA pair; assert the examined SHA of both sides appears on every result, and that the mismatched pair yields an unequal-basis condition rather than agreement or a discrepancy.
- **VER-003** — Finding-shape inspection: for each seeded discrepancy, inspect the emitted DriftFinding for the compared PEC derivation, the compared harness output, the examined SHA, and the equivalence rule; and search this deliverable's source for record-tier entity type definitions and for fields added to the upstream type, asserting none.
- **VER-004** — Resolution-basis exercise: assert every emitted finding carries a resolvable live-source citation; transpose the two sides of each fixture pair and assert the finding set is unchanged; and inspect the tool's outputs and write surface for any adoption, ruling, disposition, or closure record, asserting none.
- **VER-005** — Read-only boundary exercise: hash the fixture source tree, the governed files, and the harness's own files, configuration, and `_harness_generated/` area before and after a full run and assert byte-identity; capture every filesystem write performed during the run and assert each resolves to the store or a declared output; inspect the source for any harness configuration, cache creation, or harness-directing call, asserting none.
- **VER-006** — Content-minimal inspection: run the comparison over a content-dense fixture pair and dump every field of every DriftFinding and every result, asserting field by field that none carries file or diff content.
- **VER-007** — Standing-registration inspection: run the comparison across a fixture sequence of reconciles and at least one release candidate; assert an execution exists for each state, that each execution is bound to the state it compared, and that no result is reused across states; then, in a scratch state, disable and remove the registration and assert the missing comparison is reported rather than silently skipped.
- **VER-008** — Blocking-verdict demonstration: submit a release candidate carrying an outstanding discrepancy, one against which the comparison was withheld, and one on which the comparison could not complete; assert an explicit blocking verdict in every case; and inspect the outputs for any record that accepts or stores an explanation of a discrepancy, asserting none. The method demonstrates the mechanism's verdict, not the release process's obligation to honour it (CON-001).
- **VER-009** — Limitation carry-through: run the comparison over fixture cases in which a derivation is outside the declared comparable set, a harness output is unavailable, the comparison cannot be performed, and the upstream rebuild's result carries its own stated coverage limitations; assert per case that the affected derivation and the reason are named on the result and that no such run reports parity-clean.
- **VER-010** — Explainability inspection: for every verdict and finding produced over the fixture set, assert the presence of its rule, its equivalence rule, and its contributing cited sources, and resolve each citation to its named source.
- **VER-011** — Determinism: run the comparison twice over the same unchanged PEC derivations and the same unchanged harness output and assert identical verdicts and identical finding sets.
- **VER-012** — Declared-comparison exercise: read the declared comparison record (the component of OUT-001 required by REQ-012), compare it against the set actually compared during a run and assert set equality; point the tool at a derivation outside the declared set and assert it is reported as outside the comparison; and attempt an undeclared comparison and assert it is refused.
- **VER-013** — Boundary inspection: inspect the module's call graph and source for reconcile, successive-snapshot drift-classification, metric-computation, harness-build or harness-configuration, stamping or citation-attachment, kill-test, locality-enforcement, and no-ruling-write paths, asserting each absent; review this deliverable's tests for any criterion belonging to another deliverable, asserting none.
- **VER-014** — Dependency, egress, and absence exercise: inspect the `PKG-03` dependency manifest and this module's import graph for third-party runtime dependencies and external network calls, asserting none; run the comparison with the harness absent, with it refusing (operational refusal), and with it erroring, asserting per case an explicit reported limitation, no parity-clean verdict, and an unblocked reconcile; and re-run the `DEL-01-05` zero-dependency and locality enforcement once that deliverable is available, without discharging it here.
- **VER-015** — Run the `PKG-03` test suite and confirm that each of VER-001 through VER-014 has a corresponding executing automated test and that no test asserts a criterion absent from this contract.

## Governing Values and Decisions — Axiology

- **AX-001** — `OBJ-006` governs: the product thesis remains measurable and falsifiable. Parity against an independent deterministic checker is the one place in `PKG-03` where PEC's derivations are checked against something that is not PEC. A parity diff that could not fail would make the thesis unfalsifiable in exactly the dimension `PRD.md` §11 metric 5 exists to measure, which is why REQ-008 and REQ-009 forbid a comfortable verdict over an incomplete comparison.
- **AX-002** — The permanence is the register's word, not this contract's inference. `Deliverables.csv` opens the `Description` with "Permanent", the `SOW-020` `Notes` cell reads "Permanent (C10)", and `C10` states "Permanent parity-diff against the practitioner harness" (CLM-001, CLM-004, CLM-006). `PRD.md` §4.2 lists the harness relation among the **permanent** non-goals: "PEC parity-diffs against it permanently" (CLM-005). A contract that treated a passing comparison as completion would contradict four accepted statements at once.
- **AX-003** — The standing shape of this contract is register-directed and brief-directed contract design, informed by the `C-08` annotation rather than derived from an owner ruling on it (CLM-006, CLM-008, CON-001). It governs how the obligations above are written: treating a parity-clean run as completion would convert a continuing comparison into a one-shot artifact, which the register's own word and the brief's direction both refuse. It is not a claim that the gate has been ruled release-blocking; that question is CON-001, routed at AC-016.
- **AX-004** — Neither side of this comparison is authority, and that is the whole reason the resolution basis is live sources. `PEC-K-02` holds that PEC output is never citable as authority; the harness's own registry row holds that "Every output is a labeled generated view (D-GOV-01)" (CLM-009). Two non-authoritative derivations disagreeing settles nothing by itself; only the files settle it. REQ-004 encodes that, and CON-003 keeps the unstated closure question open rather than filling it with a PEC act that `PEC-GAT-004` forbids.
- **AX-005** — `PEC-K-06` observation-not-participation and `PEC-RCN-004` govern the tool's posture toward both sources: "verification creates findings, never rewrites sources" (CLM-002). `C10` extends the same discipline to the peer — PEC "neither directs the harness nor opens its cache half" — so the harness is an input to be read, never a surface to be configured, corrected, or optimized. A parity tool that adjusted the harness to agree with PEC would destroy the independence that makes the comparison worth running.
- **AX-006** — Edge direction is a constraint on this contract, not a licence. `[E-P28]` names `DEL-03-01` as this deliverable's predecessor at `RequiredMaturity` `INITIALIZED`, so the bound input is that deliverable's accepted contract and not any artifact of it (CLM-011, CLM-012); consuming a contract imposes no obligation on its owner. `[E-A18]` runs the other way: `DEL-10-11` measures this deliverable's findings, and being measured neither expands this contract's scope nor transfers that deliverable's metric obligation into it (CLM-013). `SOW-093`'s own note keeps the split explicit — "the behavior is PKG-03, the metric is PKG-10".
- **AX-007** — Stratum is provenance, not authority. `[E-P28]` is `PROPOSAL` and `[E-A18]` is `DECLARED`; both carry an empty `Flag` column, and `D-PEC-62` §1 item 4 accepted the exhibit "all strata as presented", read by that packet as taking the flags as flags (CLM-008, CLM-011, CLM-013). Citation does not convert `PROPOSAL` to `DECLARED`, and `_DEPENDENCIES.md` records that blocker output under mode `FULL_GRAPH` at threshold `INITIALIZED` is "advisory visibility only — never work assignment".
- **AX-008** — Two constraint vocabularies meet on this deliverable and are kept apart deliberately (CLM-004). `C10` is a decomposition hard constraint about the permanence and non-direction of the harness comparison; `C-10` is the dependency-register `STRATUM_RULE` whose own text ends "strata are provenance not authority". The `SOW-020` `Notes` token "(C10)" resolves to the first, verified through the shared `PEC-RCN-005` source and the shared word "Permanent". Reading it as the second would convert a product rule into a bookkeeping rule. `C-03` `PACKAGE_LEVEL`, `C-04` `PHASE_PRECEDENCE`, and `C-08` `STANDING_NODES` are the other register-wide non-gating rows recorded in `_DEPENDENCIES.md`.
- **AX-009** — Unknowns remain marked. TBD-001 through TBD-005 and CON-001 through CON-006 are recorded rather than resolved by inference; in particular the comparable-surface set, the equivalence rule, the meaning of "explained", the closure of a resolved finding, and the mechanism for obtaining harness output are not settled by any accepted source, and a production choice that settled the last three would take a decision in the wrong place. Constraint `C12` governs the posture: where an open decision materially affects architecture the affected work is fenced or flagged, never guessed.
- **AX-010** — This contract is lifecycle-neutral. `_STATUS.md` remains the sole lifecycle authority, is untouched by the run that authored this document, and records `OPEN`; nothing here asserts that any tool, comparison, finding, upstream reconciler, or test exists. The accepted basis is `SOFTWARE_DECOMP.md` revision 1.2 at commit `3623b958b`, accepted through `SCA-002` under `D-PEC-64`; the revision 1.1 phrase still present in `_REFERENCES.md` is superseded provenance from a deferred pointer sweep, recorded so the divergence is visible rather than silently normalized.

**Quotation record.** Every quotation in this contract is verbatim from the
named source. Exactly one is elided, marked with an ellipsis at the point of
elision and enumerated here in full: the `tools/REGISTRY.md` `Description`-cell
quotation in CLM-009, elided at its leading ellipsis, which stands for the
whole preceding subcommand description of the row and ends immediately before
the quoted terminal clause. No other quotation in this document omits text from
the span it presents.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-020 OBJ-006 | REQ-001, CLM-001, CLM-002, CLM-006, TBD-002 | AC-001 | VER-001 | Agreement and seeded-difference fixture results with the instrumented record of which pairs were actually compared |
| OUT-001 | SOW-020 OBJ-006 | REQ-002, AX-001 | AC-002 | VER-002 | Matched- and mismatched-SHA fixture results showing both examined SHAs on every result and the unequal-basis condition reported as neither agreement nor discrepancy |
| OUT-001 | SOW-020 OBJ-006 | REQ-003, CLM-010, CON-004 | AC-003 | VER-003 | Per-finding inspection records showing the comparison identity, plus a recorded search of this deliverable's source for entity type definitions and added fields |
| OUT-001 | SOW-020 OBJ-006 | REQ-004, CLM-002, CON-003, AX-004 | AC-004 | VER-004 | Resolvable live-source citations on every finding, the transposition run showing an unchanged finding set, and the output inspection showing no adoption, ruling, disposition, or closure record |
| OUT-001 | SOW-020 OBJ-006 | REQ-005, CLM-004, CLM-009, AX-005 | AC-005 | VER-005 | Before/after hashes of the source tree, governed files, and the harness's own files and generated area; the captured filesystem-write inventory; and the source inspection showing no harness configuration, cache creation, or directing call |
| OUT-001 | SOW-020 OBJ-006 | REQ-006 | AC-006 | VER-006 | Field-by-field dumps of every DriftFinding and result for a content-dense fixture pair, showing no file or diff content |
| OUT-001 | SOW-020 OBJ-006 | REQ-007, CLM-005, CLM-008, AX-002, AX-003 | AC-007 | VER-007 | Execution records binding each reconcile and release candidate to the state it compared, and a mutation run showing the disabled and removed registration reported rather than silently skipped |
| OUT-001 | SOW-020 OBJ-006 | REQ-008, CON-001, CON-002 | AC-008 | VER-008 | Blocking-verdict demonstrations for an outstanding discrepancy, a withheld comparison, and an incomplete comparison, plus the output inspection showing no explanation is recorded or accepted |
| OUT-001 | SOW-020 OBJ-006 | REQ-009, CLM-012, CON-006 | AC-009 | VER-009 | Per-case results for an out-of-set derivation, an unavailable harness output, an unperformable comparison, and an upstream-limited rebuild, each naming the derivation and the reason with no parity-clean verdict |
| OUT-001 | SOW-020 OBJ-006 | REQ-010, TBD-004 | AC-010 | VER-010 | Rule, equivalence rule, and resolved contributing citations recorded for every verdict and finding over the fixture set |
| OUT-001 | SOW-020 OBJ-006 | REQ-011 | AC-011 | VER-011 | Two-run verdict and finding-set comparison over unchanged derivations and unchanged harness output |
| OUT-001 | SOW-020 OBJ-006 | REQ-012, TBD-003, TBD-004, TBD-005 | AC-012 | VER-012 | The declared comparison record, the compared-set equality check for a run, the out-of-set reporting transcript, and the refused undeclared comparison |
| OUT-001 | SOW-020 OBJ-006 | REQ-013, CLM-007, CLM-013, CLM-014, CLM-015, AX-006 | AC-013 | VER-013 | Call-graph and source inspection records showing each named adjacent path absent, plus a review of this deliverable's tests confirming no criterion belonging to another deliverable |
| OUT-001 | SOW-020 OBJ-006 | REQ-014, CLM-016, CON-005 | AC-014 | VER-014 | Dependency-manifest and import-graph inspection records, the absent/refusing/erroring harness transcripts showing reported limitations and unblocked reconciles, and the DEL-01-05 enforcement result once that deliverable is available |
| OUT-002 | SOW-020 OBJ-006 | REQ-015, CLM-016 | AC-015 | VER-015 | PKG-03 test-run output mapping each executed test to its declared verification method, with no criterion asserted that this contract does not state |
| OUT-001 | SOW-020 OBJ-006 | REQ-007, REQ-008, CLM-008, CON-001, AX-003 | AC-016 | HUMAN_REVIEW: accountable owner confirmation or declination that the parity gate carries release-gating authority, given C-08's "owner confirmation requested" note, D-PEC-62 §1 item 4's acceptance of the standing-node set as a recorded-but-unresolved non-gating annotation, and the PRD §12 P1 exit test's silence on this mechanism's authority | Dated owner ruling recorded against this deliverable, stating whether a blocking verdict blocks a release candidate or is advisory, and leaving the contract's standing framing intact either way |
| OUT-001 | SOW-020 OBJ-006 | CLM-003, CLM-009, CON-002, CON-003, CON-005, AX-004, AX-008, AX-009, AX-010 | AC-017 | HUMAN_REVIEW: accountable owner confirmation that no explanation or closure of a parity discrepancy is defined, produced, or adjudicated here, that resolution is carried only as a live-source citation, and that the harness is neither directed nor its cache half opened — and a statement of where the closure question is owed | Dated owner ruling citing the undefined "explained" disjunct of the PRD §12 P1 exit test, the "resolved against live sources" clause of SOW-020, and constraint C10's non-direction rule |
