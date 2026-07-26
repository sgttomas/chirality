---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-03-06
package_id: PKG-03
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@3623b958b
project_scope_refs: [SOW-054]
package_objective_refs: [OBJ-005]
---

# Scope of Work — DEL-03-06 Rebuild performance bounds

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-03-06` — "Rebuild
performance bounds" — in `PKG-03` Reconciliation & Parity of the PEC v2 build.
It covers project scope item `SOW-054` in service of package objective
`OBJ-005`.

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.2** (`current_basis`, SCA-002 successor; accepted 2026-07-25 at
D-PEC-64 closure, commit `3623b958b`). The deliverable-local `_REFERENCES.md`
still names "revision 1.1, accepted working surface"; that phrase is superseded
provenance left by a deferred pointer sweep (SCA-002 `Handoff_State.md`, open
item `OI-B`, dispositioned `DEFERRED_BY_HUMAN`), and `_CONTEXT.md`'s own
supersession line records revision 1.1 as "superseded by revision 1.2
(`current_basis`, SCA-002 successor)". This contract cites revision 1.2.

**Objective warrant.** `CoversScopeItems` is one row, and its `OBJ-005`
attribution is **SCA-002-authored and owner-ruled at Gate 3** — not
register-direct. It is stated here at the strength its own record carries, and
no further, because that record rates it **MEDIUM-LOW** and recommends it
weakly with an honest alternative range.

`SOW-054` is one of the twenty ledger rows whose empty `ObjectiveIDs` cell
SCA-002's action `A001` populated. That action's target cell reads in full:

> `ScopeLedger.csv` `ObjectiveIDs` — **20 IN rows** (`SOW-001, 003, 011..017,
> 021, 025, 040, 042, 052, 053, 054, 056, 088, 089, 094`)
>
> (`Brief.md`, action-register row `A001`, target cell, quoted in full without
> elision. ID-shaped text inside this quotation is upstream source context, not
> a local definition or reference.)

The deliverable-level cell was authored by the same amendment. `DEL-03-06` is
one of the seventeen `Deliverables.csv` rows action `A002` changed, and that
action's own preamble records how those values were obtained:

> Derived from A001 by the union invariant, not authored independently.
>
> (`Amendment_Preview.md`, action `A002` preamble, quoted in full without
> elision.)

and the entry itself. That table repeats the column triple `DEL | Covers | new`
twice per line; this deliverable's entry is the right-hand triple of one such
line, quoted here as that triple:

> | 03-06 | 054 | `OBJ-005` |
>
> (`Amendment_Preview.md`, action `A002` row set, right-hand triple of the
> line whose left-hand triple is `01-06 | 094 | OBJ-004`. ID-shaped text inside
> this quotation is upstream source context, not a local definition or
> reference.)

The §3 objective row moved with it. The recorded old and new text of the
`OBJ-005` row's two amended columns reads in full:

> ```
> OLD col4: SOW-010, SOW-055; bound by C1/C2 across all items
> NEW col4: SOW-010, SOW-021, SOW-025, SOW-052..056, SOW-088; bound by C1/C2 across all items
> OLD col5: DEL-03-01, DEL-10-02
> NEW col5: DEL-00-01, DEL-01-03, DEL-01-05, DEL-03-01, DEL-03-06, DEL-10-02, DEL-10-03
> ```
>
> (`Amendment_Preview.md`, action `A003b`, `OBJ-005` block, quoted in full
> without elision. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference.)

`SOW-054` enters the objective's mapped-items cell inside the contiguous range
`SOW-052..056`, and `DEL-03-06` enters its mapped-deliverables cell. Neither
was there before the amendment.

The strength of that attribution is recorded, and it is qualified. In a per-row
attribution table whose columns are `# | DEL | SOW | SourceRef | Recommended |
Confidence | Ruling`, this row reads:

> | 6 | DEL-03-06 | 054 | PEC-SVC-003 | `OBJ-005` | **MEDIUM-LOW** | **Q1.4** |
>
> (`Amendment_Preview.md`, "Per-row attributions". ID-shaped text inside this
> quotation is upstream source context, not a local definition or reference.)

The question routed to the owner is headed:

> **Q1.4 · DEL-03-06 / SOW-054 — `OBJ-005` vs `OBJ-002` vs both. MEDIUM-LOW.**
>
> (`Amendment_Preview.md`, Part 1 per-row warrant, heading line, quoted in full
> without elision. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference.)

That warrant is where the packet corrected its own earlier quoting of the
source. Its correction note reads in full:

> v1 truncated this at "(target: minutes)" — cutting it at exactly the clause
> that points somewhere else. The most consequential quoting error in the
> package.
>
> (`Amendment_Preview.md`, Q1.4 blockquote, quoted in full without elision.)

and the Part 7 correction log records the same at `C-20`, under the columns
`# | Correction`:

> | C-20 | **DEL-03-06 warrant quote was truncated at exactly the clause pointing elsewhere.** Full PEC-SVC-003 quoted; `OBJ-002` and both-objectives alternatives presented; escalated to per-row |
>
> (`Amendment_Preview.md`, Part 7 correction log. ID-shaped text inside this
> quotation is upstream source context, not a local definition or reference.)

The reasoning that follows from the untruncated requirement reads in full:

> Two clauses pointing at different objectives:
> - *full rebuild within a bound* → `OBJ-005` kinship (a fast rebuild is what
>   makes deletion survivable), continuous with `SOW-010`;
> - *incremental reconcile within seconds* → incremental reconcile is
>   SHA-delta-keyed by PEC-RCN-003, which is `SOW-018` → **`OBJ-002`**.
>
> (`Amendment_Preview.md`, Q1.4. ID-shaped text inside this quotation is
> upstream source context, not a local definition or reference.)

and the options it presents, in full:

> Options: **`OBJ-005`** *(recommended, weakly — the row is a PKG-03 performance
> bound on the rebuild path)*; **`OBJ-002`**; or **`OBJ-005;OBJ-002`**, the most
> faithful to the two-clause text and defensible if you prefer completeness over
> minimality. **`OBJ-002` or both edits the `OBJ-002` §3 row beyond the drafted
> text.**
>
> (`Amendment_Preview.md`, Q1.4. ID-shaped text inside this quotation is
> upstream source context, not a local definition or reference.)

The Part 8 question table records the same alternatives compactly, under the
columns `# | Row | Recommended | Alternatives | Conf.`:

> | Q1.4 | DEL-03-06 / SOW-054 | `OBJ-005` | `OBJ-002` · `OBJ-005;OBJ-002` | MED-LOW |
>
> (`Amendment_Preview.md`, Part 8 Q1 table. ID-shaped text inside this
> quotation is upstream source context, not a local definition or reference.)

The owner ruled it. The Gate 3 ruling table row reads in full, under the
columns `Q | Question | Ruling`:

> | Q1 | Seven per-row attributions | **All seven as recommended** — `OBJ-005`: DEL-00-01, DEL-01-05, DEL-03-06, DEL-10-03; `OBJ-001`: DEL-00-03, DEL-08-01, DEL-08-02 |
>
> (`Decision_Log.md`, "Gate 3 owner ruling — APPROVED 2026-07-25". ID-shaped
> text inside this quotation is upstream source context, not a local definition
> or reference.)

Three consequences bind this contract. First, the ruled attribution is the
accepted one and is used throughout: `OBJ-005` is this contract's objective and
nothing here reinterprets it. Second, the qualification travels with it rather
than being smoothed away — the record rates the row **MEDIUM-LOW**, recommends
`OBJ-005` **weakly**, and preserves `OBJ-002` and `OBJ-005;OBJ-002` as recorded
alternatives, so this contract asserts the attribution at exactly that strength
and supplies no fresh derivation that the record does not contain. Third,
because the recommendation is recorded as weak with a live alternative range,
AC-014 routes the qualification to an accountable owner at REVIEW rather than
leaving it buried in the scope-change package (CON-005).

- **CLM-001** — The accepted `ScopeLedger.csv` row for `SOW-054` reads in full, under the register's ten columns `ScopeItemID,InOutStatus,ScopeItemStatement,SourceRef,PackageID,DeliverableIDs,ObjectiveIDs,DecisionRef,OpenIssue,Notes`:

> `SOW-054,IN,Complete full rebuild within a bound confirmed at P1 (target minutes); incremental reconcile within seconds,PEC-SVC-003,PKG-03,DEL-03-06,OBJ-005,DL-11,FALSE,`
>
> (Field-by-field: `DecisionRef` `DL-11`; `OpenIssue` `FALSE`; `Notes` empty and
> trailing — one of the ten fields is unpopulated. ID-shaped text inside this
> quotation is upstream source context, not a local definition or reference.)

  The `SOFTWARE_DECOMP.md` §2 SSOW row for the same item repeats the statement without the register-only columns and likewise leaves its `Notes` column empty: "| SOW-054 | IN | Complete full rebuild within a bound confirmed at P1 (target minutes); incremental reconcile within seconds | PEC-SVC-003 | |".

- **CLM-002** — `SOW-054`'s `SourceRef` cell names one locus, `PEC-SVC-003`, the `PRD.md` §10 service requirement, quoted here in full as it reads: "Full rebuild of the current corpus completes within a bound confirmed at Phase 1 (target: minutes); incremental reconcile within seconds." It is one of six `PEC-SVC-*` requirements in that block, and the other five are covered elsewhere: `PEC-SVC-001` and `PEC-SVC-002` by zero-dependency and locality enforcement under `SOW-052` and `SOW-053`, `PEC-SVC-004` by the standing kill test under `SOW-055`, `PEC-SVC-005` by the store path and content-minimal rule under `SOW-056`, and `PEC-SVC-006` by self-observability logging under `SOW-057` (CLM-017). This contract covers exactly one of the six.
- **CLM-003** — The requirement's two clauses are not symmetrically stated, and this contract does not average them. The rebuild clause states a **bound confirmed at Phase 1** with "minutes" marked explicitly as a *target*; the incremental clause states "within seconds" flat, with no confirmation act and no target marker. The scope-item restatement preserves the same asymmetry ("a bound confirmed at P1 (target minutes); incremental reconcile within seconds"). What neither states is the numeric bound itself, who performs the confirmation, or by what act it is confirmed (CON-001).
- **CLM-004** — `OBJ-005` states "Everything PEC holds can be deleted at any moment without blocking any governed act", `SourceRef` `§3.5` (`SOFTWARE_DECOMP.md` §3; `PRD.md` §3 outcome 5, which reads "All of the above can be deleted at any moment without blocking any governed act."). At revision 1.2 its "Mapped Scope Items" cell reads "SOW-010, SOW-021, SOW-025, SOW-052..056, SOW-088; bound by C1/C2 across all items" and its `MappedDeliverables` cell reads "DEL-00-01, DEL-01-03, DEL-01-05, DEL-03-01, DEL-03-06, DEL-10-02, DEL-10-03". The objective's product invariant is `PEC-K-01` **Graceful absence**, whose statement reads in full: "No governed act may require a PEC read or write. Deleting PEC blocks nothing. The kill test (§12) passes at every release."
- **CLM-005** — The two clauses of `PEC-SVC-003` correspond one-to-one with this deliverable's two accepted upstream edges, and the register shows the correspondence directly: the full-rebuild clause is measured over `[E-P30]`'s predecessor `DEL-03-01`, whose exhibit rationale reads "Perf bounds test the full rebuild"; the incremental clause is measured over `[E-P31]`'s predecessor `DEL-03-02`, whose exhibit rationale reads "Perf bounds test incremental reconcile" (CLM-008). This contract states that correspondence as the register carries it and draws no further inference from it. In particular it does not use the correspondence to settle the Q1.4 tension between `OBJ-005` and `OBJ-002`: that tension arises from the same two clauses, it was routed to the owner, and it was ruled (CON-005). The correspondence is a fact about what this deliverable measures, not an argument about which objective the row serves.
- **CLM-006** — The assignment of `SOW-054` to `PKG-03` is decision-log entry `DL-11` (2026-07-24), whose Decision cell records the forced boundary calls of Phase 4. Quoting the clause that bears on this deliverable, with the preceding and following clauses elided:

> Phase 4 forced boundary assignments: ... SOW-054 (rebuild bounds) → PKG-03
> as reconcile performance; ...
>
> (`SOFTWARE_DECOMP.md` decision log, `DL-11` Decision cell; **elided** at both
> ellipses. ID-shaped text inside this quotation is upstream source context, not
> a local definition or reference.)

  That entry's Rationale cell, quoted here in full and without elision, is also the register's own account of how the ledger was produced:

> Each was assignable to two domains; ledger rows carry `DL-11` in DecisionRef.
> The `ScopeLedger.csv` register was generated from this document's SSOW tables
> by a session-local script (see OI-013) to prevent transcription drift
>
> (`SOFTWARE_DECOMP.md` decision log, `DL-11` Rationale cell. ID-shaped text
> inside this quotation is upstream source context, not a local definition or
> reference.)

  The `DL-11` token in the `SOW-054` row's `DecisionRef` cell (CLM-001) is therefore the ledger's own cross-reference to that boundary decision. It is a decision reference, not a dependency edge and not a register relation of any other kind; this contract cites it only for the boundary it records — the bound belongs to `PKG-03` as reconcile performance, the reconciler entry point and the incremental engine belong to their own deliverables, and this deliverable measures rather than builds either.

## Deliverable Definition — Ontology

`DEL-03-06` is typed `TEST_SUITE` at Context Envelope `S` with `PhaseHint`
`P1`. `Deliverables.csv` records its `AnticipatedArtifacts` as "Perf tests +
recorded bound" and leaves `ContextEnvelopeNotes` empty, so there are no
envelope notes to carry forward and `_CONTEXT.md` records "(none)". The outputs
of this contract are bounded by that artifact naming: exactly the performance
tests and the recorded bound, and nothing beyond those two artifacts and the
components each of them declares as part of itself.

- **OUT-001** — A performance test suite in the PEC service core's test surface: it exercises the full-rebuild path through the upstream entry point and the incremental reconcile path through the upstream engine over a declared measurement corpus under declared measurement conditions, and produces timing measurements together with the conditions under which each was taken.
- **OUT-002** — The recorded bound: a durable, readable record of what the suite measured for each of the two paths, of the measurement conditions and corpus identity each measurement was taken under, of the register-stated target ("minutes" for the rebuild) and the register-stated seconds clause for the incremental path as distinct from any measured value, and of the conditioning each measurement carries (CON-003, CON-004). Its **confirmation state** — whether a bound has been confirmed for Phase 1, by whom, and by what act — is a field of this record rather than a third artifact, and it is a field this contract obliges to be recorded honestly, including as unconfirmed, rather than a claim this deliverable may make on its own authority (CON-001, REQ-013).

### Identity of record

- **CLM-007** — `DEL-03-06` is named "Rebuild performance bounds", Type `TEST_SUITE`, Context Envelope `S`, `PhaseHint` `P1`, `ResponsibleParty` `TBD`, `AnticipatedArtifacts` "Perf tests + recorded bound", `CoversScopeItems` `SOW-054`, `SupportsObjectives` `OBJ-005`, `ContextEnvelopeNotes` empty, with the register `Description` field reading "Confirm the P1 rebuild bound (target minutes) and seconds-scale incremental reconcile against the current corpus." Sources: `Deliverables.csv` row `DEL-03-06` and the `SOFTWARE_DECOMP.md` §5 PKG-03 table row "| DEL-03-06 | Rebuild performance bounds | TEST_SUITE | S | P1 | SOW-054 |".
- **CLM-008** — The `PKG-03` package charter (`SOFTWARE_DECOMP.md` §4) is "The guaranteed path from file truth to record tier: one-command rebuild, incremental Git-delta reconcile, drift classification, harness parity diffing, stream-loss recovery guarantee, store-only writes, rebuild performance bounds", covering "SOW-010, 018, 019, 020, 021, 038, 054 (7)", with "Stream ingest mechanics (PKG-07); parsers (PKG-02)" recorded as explicitly out of package scope. Of those seven items this deliverable covers exactly one: the rebuild performance bounds, which the charter names last.

### Placement in the work graph

- **CLM-009** — This deliverable has **two** accepted `EXECUTION` upstream edges and **two** `ANCHOR` rows, held as `Dependencies.csv` register rows `DEP-03-06-001` through `DEP-03-06-004` at `RegisterSchemaVersion` `v3.1`, under the v3.1 column order `RegisterSchemaVersion,DependencyID,FromPackageID,FromDeliverableID,FromDeliverableName,DependencyClass,AnchorType,Direction,DependencyType,TargetType,TargetPackageID,TargetDeliverableID,TargetRefID,TargetName,TargetLocation,Statement,EvidenceFile,SourceRef,EvidenceQuote,Explicitness,RequiredMaturity,ProposedMaturity,SatisfactionStatus,Confidence,Origin,FirstSeen,LastSeen,Status,Notes`. The two anchors are `DEP-03-06-001` (`IMPLEMENTS_NODE`: package-local to `PKG-03`) and `DEP-03-06-002` (`TRACES_TO_REQUIREMENT`: the `SOW-054` requirement trace). Both `EXECUTION` rows share the following column values, attributed by column: `FromPackageID` `PKG-03`, `FromDeliverableID` `DEL-03-06`, `FromDeliverableName` "Rebuild performance bounds", `DependencyClass` `EXECUTION`, `AnchorType` `NOT_APPLICABLE`, `Direction` `UPSTREAM`, `DependencyType` `PREREQUISITE`, `TargetType` `DELIVERABLE`, `TargetPackageID` `PKG-03`, `EvidenceFile` `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md`, `SourceRef` "location TBD", `EvidenceQuote` **empty**, `Explicitness` `IMPLICIT`, `RequiredMaturity` `INITIALIZED`, `ProposedMaturity` `TBD`, `SatisfactionStatus` `PENDING`, `Confidence` `MEDIUM`, `Origin` `EXTRACTED`, `FirstSeen` and `LastSeen` `2026-07-25`, `Status` `ACTIVE`. They differ as follows:

  | Register row | `TargetDeliverableID` / `TargetRefID` | `TargetName` | `TargetLocation` | `Statement` | `Notes` |
  |---|---|---|---|---|---|
  | `DEP-03-06-003` | `DEL-03-01` | "Full-rebuild reconciler (one command)" | `execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command` | "Perf bounds test the full rebuild" | "PROPOSAL; Flag=none; EdgeID=E-P30" |
  | `DEP-03-06-004` | `DEL-03-02` | "Incremental reconcile on Git delta" | `execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-02_Incremental_reconcile_on_Git_delta` | "Perf bounds test incremental reconcile" | "PROPOSAL; Flag=none; EdgeID=E-P31" |

  The corresponding accepted DAG exhibit rows, under that exhibit's columns `EdgeID,PredecessorID,SuccessorID,Stratum,EdgeKind,Flag,BasisCitation,Rationale`, read `E-P30,DEL-03-01,DEL-03-06,PROPOSAL,TESTS,,,Perf bounds test the full rebuild` and `E-P31,DEL-03-02,DEL-03-06,PROPOSAL,TESTS,,,Perf bounds test incremental reconcile` — `Flag` empty and `BasisCitation` **also empty** on both.

  **Register-hygiene observation, carried rather than smoothed.** Both `EXECUTION` rows have an empty `EvidenceQuote` and a `SourceRef` reading "location TBD", and both exhibit rows have an empty `BasisCitation`. This contract does not supply evidence for those cells, and no statement here may be read as filling them. The edges' warrant is therefore their `Statement` cells and the two predecessors' own accepted contracts, not a quoted source — the same disposition the accepted `DEL-03-02` contract records for the structurally identical `DEP-03-02-003` row and the accepted `DEL-03-01` contract records for `DEP-03-01-006`. The absence of a durable register validator behind such cells is itself a recorded open issue, `OI-013`, whose text reads in full: "No durable register validator exists: the coverage/coupling assertions ran in a session-local generator, which is not part of this package and enforces nothing after acceptance" (`SOFTWARE_DECOMP.md` §10 Open Issues register, `OI-013` `Issue` cell, under that table's columns `ID | Refs | Issue | Owner action that closes it`). Both edges' direction is nonetheless unambiguous: the predecessors are the measured surfaces and this deliverable is the measurer.

- **CLM-010** — Both predecessors are at lifecycle state `INITIALIZED`, which is the maturity both edges require. `INITIALIZED` means each upstream **contract** is the reliable input: each accepted `ScopeOfWork.md` exists, and no reconciler, engine, store, schema, parser, or registry does. Nothing in this contract asserts that any upstream artifact exists or has been built, and nothing in it asserts that any bound has been measured or confirmed. From `[E-P30]`, the full-rebuild path this suite measures is `DEL-03-01`'s obligation, quoted here in full and without elision:

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
> - **REQ-003** — The rebuild shall complete against a store that is absent,
>   newly deleted, or empty, obtaining the store through the upstream
>   store-lifecycle interface quoted in CLM-013 and requiring no manual repair.
>   This deliverable shall implement no store path resolution, no ignore-rule
>   registration, no store creation, and no store deletion of its own; those are
>   the upstream deliverable's under `SOW-056` (CLM-008, CLM-013).
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
> - **REQ-014** — The reconciler shall perform no act owned by another
>   deliverable. In particular it shall perform no Git-delta-keyed incremental
>   reconcile, no drift classification between snapshots, no parity diff against
>   practitioner-harness output, no stream-loss recovery act, no rebuild-bound
>   measurement or assertion, no examined-SHA or freshness stamping and no
>   per-claim citation attachment onto an orientation response, no
>   gate-precondition evaluation or slate rendering, no locality or
>   zero-dependency enforcement act, and no kill test; each is cited to its owner
>   in CLM-019 and none is discharged here.
>
> (`DEL-03-01/ScopeOfWork.md`, Ontology and Epistemology sections; all six
> records quoted in full, none elided. ID-shaped text inside this quotation is
> upstream source context, not a local definition or reference — this contract's
> own records are separate and differently worded.)

  Four consequences follow for this contract. The measured surface is one command, so this suite measures through that command and defines no rebuild path of its own (REQ-001). The command is contractually obliged to complete against an absent, deleted, or empty store, so a cold-start measurement is measuring the obliged behaviour rather than an exceptional one. The rebuild is contractually obliged to be deterministic and idempotent, which is what makes repeated timing over an unchanged corpus a measurement rather than a sample of two different acts (REQ-010). And the upstream contract explicitly excludes "rebuild-bound measurement or assertion" from its own scope, which is the clearest statement in the accepted corpus that the measurement is this deliverable's — written in another contract's voice, not in this one's.

- **CLM-011** — From `[E-P30]`, the upstream contract also records the conflict that conditions what a rebuild-bound measurement means. Its record reads in full:

> - **CON-005** — `SOW-010` requires the record tier be rebuildable "in full",
>   while every upstream feed unit is contractually obliged to report feeds it
>   could not read as explicit limitations (CLM-016), and `PEC-ORI-006` prohibits
>   silent omission. No accepted source states whether a rebuild that completed
>   with stated coverage limitations counts as a full rebuild for `SOW-010`'s
>   purposes, or whether "in full" is a claim about the command's reach rather
>   than its coverage. This contract takes neither reading as settled: REQ-001
>   obliges the command to reach every registered loop and every manifest-named
>   feed, and REQ-009 obliges every gap to be carried through as a stated
>   limitation, so that the question is visible in the result rather than
>   answered by silence. `PRD.md` §12's `P1` exit test names "rebuild-from-scratch
>   ≤ bound" without stating the bound, which `PEC-SVC-003` records as "confirmed
>   at Phase 1"; that measurement is `DEL-03-06`'s under `SOW-054` (CLM-019) and
>   this contract asserts no bound.
>
> (`DEL-03-01/ScopeOfWork.md`, Epistemology section; quoted in full, not elided.
> ID-shaped text inside this quotation is upstream source context, not a local
> definition or reference.)

  That record names this deliverable as the owner of the measurement and, in the same breath, leaves open what the measured act is. A rebuild that completed with stated coverage limitations and a rebuild that read every manifest-named feed are different acts, and a duration measured over the first is a different claim from a duration measured over the second. This contract neither resolves that question nor measures across it silently: REQ-005 obliges the coverage state of every measured rebuild to be recorded with its measurement, so that the ambiguity is visible in the recorded bound rather than absorbed into a number (CON-003). The same upstream record also carries the instance-level generated-views gap that its own conflict register opens on — "`SOW-021`'s second limb permits writes to \"generated views\", and the gap this contract carries is **instance-level, not class-level**." (`DEL-03-01/ScopeOfWork.md`, Epistemology section, first sentence of a longer record; ID-shaped text in this quotation is upstream source context, not a local definition or reference) — which reaches this contract only as a fact about the measured surface's write set: whatever view set production settles on upstream is inside the act this suite times, and this contract names no view, adds none, and settles nothing about the instance set.

- **CLM-012** — From `[E-P31]`, the incremental reconcile path this suite measures is `DEL-03-02`'s obligation, quoted here in full and without elision:

> - **OUT-001** — An incremental reconcile engine in the PEC service core: it
>   determines, from the Git delta between the commit state it observes now and
>   the commit SHA it last examined through, which sources have changed for each
>   registered loop, reconciles the record tier over that selection, and records
>   the new examined-through baseline. The engine's **baseline record** — the
>   durable statement of the commit SHA a completed reconcile examined through —
>   is a component of this output rather than a third artifact, since it is the
>   engine's own state and the register names exactly two artifacts.
> - **REQ-001** — The engine shall reconcile incrementally, keyed on the Git
>   delta between the commit state it observes at the start of a run and the
>   commit SHA recorded as last examined, per `SOW-018` (CLM-001) and
>   `PEC-RCN-003` (CLM-002). The delta shall select the work: sources the delta
>   does not name shall not be re-derived, and sources it does name shall be.
> - **REQ-005** — An incremental reconcile over a delta shall produce the record
>   tier that a full rebuild over the same end commit state would produce. Where
>   the engine cannot establish that equivalence for a class of change —
>   including a change it cannot resolve to affected record-tier facts (TBD-003)
>   — it shall fall back to the full-rebuild path rather than emit a partial
>   result as a reconciled one, per `PEC-K-07` ("Ingest is best-effort;
>   reconciliation is guaranteed") and the upstream determinism obligation quoted
>   in CLM-008.
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
> (`DEL-03-02/ScopeOfWork.md`, Ontology and Epistemology sections; all four
> records quoted in full, none elided. ID-shaped text inside this quotation is
> upstream source context, not a local definition or reference.)

  Three consequences follow. The measured act is delta-selected, so its duration is a function of the delta the run was given, and a measurement that does not record the delta it measured over reports a number without a subject (REQ-006). The engine is contractually obliged to fall back to the full-rebuild path for change classes it cannot resolve, so a measured incremental run that fell back is timing a rebuild rather than an incremental reconcile, and the recorded bound must say which occurred. And that contract, like its sibling, excludes "rebuild or incremental performance measurement or bound" from its own scope, so both clauses of `PEC-SVC-003` are measured here and asserted nowhere upstream.

- **CLM-013** — From `[E-P31]`, the upstream contract also records that the examined-SHA baseline the incremental path turns on is unowned in the accepted corpus. The relevant part of its record reads in full:

> - **CON-001** — The edge that places this deliverable presupposes an
>   examined-SHA baseline that no accepted source obliges anyone to produce. The
>   upstream full-rebuild contract states no obligation to record the commit SHA
>   a rebuild examined through; its boundary requirement excludes examined-SHA
>   stamping only in the orientation-response form owned by `DEL-04-03` under
>   `SOW-006`, so the reconcile-side baseline is unaddressed there rather than
>   prohibited or assigned. The transitively reached entity-model contract stamps
>   OrientationSnapshot with the examined SHA and obliges the model to represent
>   examined-through SHA provenance structurally (CLM-010), but OrientationSnapshot
>   is an orientation artifact whose stamping act is owned elsewhere. That contract
>   obliges specific properties of the model — citation provenance on every type,
>   structural examined-through-SHA provenance with OrientationSnapshot stamped,
>   and explicit per-loop Receipt availability — while enumerating no complete
>   field set for the fourteen record-tier types and naming no holder for a
>   *reconcile's* examined-through SHA, so where that value would live is
>   unsettled at the level of accepted truth.
>
> (`DEL-03-02/ScopeOfWork.md`, Epistemology section, first paragraph of a
> two-paragraph record; the second paragraph is not presented here and this
> quotation therefore reproduces the first paragraph in full and without
> internal elision. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference.)

  A seconds-scale measurement of the incremental path is a measurement of a run that started from some baseline, and the accepted corpus fixes neither where that baseline lives nor who is obliged to produce it. This contract does not resolve that question in either direction and assigns no obligation upstream: REQ-006 obliges the baseline provenance and the delta the run was given to be recorded with every incremental measurement, so the measurement's subject is stated rather than assumed (CON-004). That same upstream contract records this deliverable as the owner of the measurement in its own voice, and this contract states the relation only in that direction: the predecessors are measured from outside, and being measured imposes nothing on them.

- **CLM-014** — The record-tier entity model both measured surfaces write into is not a declared edge of this deliverable. Register-wide constraint `C-03` `PACKAGE_LEVEL` states "Every PKG-03/04/05 deliverable depends on DEL-01-01 directly or transitively", with the exhibit's `Notes` cell recording "Deliverable-level entry edges (E-P10..13) are PROPOSAL; validator proves transitive closure 13/13" and its validation summary reading "C-03 transitive closure: 13/13 PKG-03/04/05 members reachable from DEL-01-01". This deliverable's paths are `[E-P30]` to `DEL-03-01` and `[E-P31]` to `DEL-03-02`, and thence to `DEL-01-01` by those deliverables' own declared and transitive paths. This contract writes no record-tier fact of its own and therefore binds to no entity type; the model reaches it only as a property of the acts it times (CON-002).
- **CLM-015** — **No downstream consumer relation is recorded against this deliverable.** `_DEPENDENCIES.md` records an Upstream table with two rows and no downstream table, `Dependencies.csv` contains only the two anchors and the two upstream `EXECUTION` rows, and `DEL-03-06` appears in the accepted DAG exhibit's edge register exactly twice — as the `SuccessorID` of `E-P30` and of `E-P31` — and never as a `PredecessorID` (CLM-009). In the accepted graph this deliverable is a terminal node. It is also **not** a member of the exhibit's standing-node set: constraint row `C-08` `STANDING_NODES` names its parties as "DEL-01-05, DEL-03-04, DEL-10-02, DEL-10-03, DEL-10-10", and this deliverable is not among them. This contract therefore makes no claim to standing or release-gating force of its own, and nothing in it may be read as asserting one. Its relation to the `P1` exit test is stated in CLM-016 as the accepted source states it, and no further.
- **CLM-016** — The `P1` exit test names a bound this deliverable measures and does not state its value. The `PRD.md` §12 release-strategy row reads in full, under that table's columns `Phase | Scope | Exit test`: "| **P1 — One-loop reconciler** | Reconciler + orientation store + API for one loop (piping or root), read-only | Parity-diff vs harness clean or explained; rebuild-from-scratch ≤ bound; kill test passes |". Three exit conditions are named there and this deliverable serves one of them: "rebuild-from-scratch ≤ bound". The parity-diff condition is `DEL-03-04`'s under `SOW-020` and the kill test is `DEL-10-02`'s under `SOW-055` (CLM-017). The bound in that clause is the bound `PEC-SVC-003` records as "confirmed at Phase 1", and no accepted source states its value or names the act that confirms it (CLM-003, CON-001). This deliverable is also absent from the `PRD.md` §11 success-metric list, whose six numbered metrics are Step-0 cost, orientation defect rate, collision incidents, harness poll adoption, parity DriftFindings per reconcile, and the kill test — no performance or rebuild-duration metric appears among them. Reporting the §11 parity metric is `DEL-10-11`'s under `SOW-093`; this contract reports no §11 metric.

### Boundaries

- **CLM-017** — The acts adjacent to this measurement are owned elsewhere and are cited here, never discharged. Within `PKG-03`: the one-command full rebuild and the reconciler write restriction are `DEL-03-01` (`SOW-010`, `SOW-021`); the Git-delta-keyed incremental reconcile is `DEL-03-02` (`SOW-018`); classifying and reporting drift between successive snapshots is `DEL-03-03` (`SOW-019`); parity-diffing PEC derivations against practitioner-harness output is `DEL-03-04` (`SOW-020`); the stream-loss recovery guarantee is `DEL-03-05` (`SOW-038`, `P3`). Outside it: the record-tier schema and entity model are `DEL-01-01` (`SOW-001`); the gitignored store, its safe-delete lifecycle, and its ingest-boundary content-minimal guard are `DEL-01-03` (`SOW-056`); self-observability logging is `DEL-01-04` (`SOW-057`); standing zero-dependency and locality enforcement is `DEL-01-05` (`SOW-052`, `SOW-053`); the loop-registration configuration is `DEL-01-06` (`SOW-094`); the seven feed grammars and the feed manifest are `DEL-02-01` through `DEL-02-07` (`SOW-011`..`SOW-017`); serving deltas since a caller-supplied commit SHA is `DEL-04-02` (`SOW-005`); stamping every orientation response with examined-through SHA, generation time, and per-feed freshness is `DEL-04-03` (`SOW-006`, `SOW-007`); rendering a measurement limitation into an orientation response is `DEL-04-05` (`SOW-009`); the **orientation latency budget** — "Complete orientation reads in ≤100 ms at p95 against the current corpus" — is `DEL-08-04` (`SOW-041`, `PEC-API-002`), the corpus's other performance `TEST_SUITE` and the one most easily confused with this deliverable; the standing kill test is `DEL-10-02` (`SOW-055`); the tested no-ruling-write property of the API surface is `DEL-10-03` (`SOW-025`); the §11 parity metric report is `DEL-10-11` (`SOW-093`); the directed bootstrap self-ingest validation is `DEL-10-10` (`SOW-064`). This contract produces only the performance tests and the recorded bound.
- **CLM-018** — Phase staging, checked against the `PhaseHint` column of `Deliverables.csv` for every one of the twenty-eight deliverables this contract names in its own voice. Twenty-five are `P1`: `DEL-03-06` itself, its predecessors `DEL-03-01` and `DEL-03-02`, and `DEL-01-01`, `DEL-01-03`, `DEL-01-04`, `DEL-01-05`, `DEL-01-06`, `DEL-02-01`, `DEL-02-02`, `DEL-02-03`, `DEL-02-04`, `DEL-02-05`, `DEL-02-06`, `DEL-02-07`, `DEL-03-03`, `DEL-03-04`, `DEL-04-02`, `DEL-04-03`, `DEL-04-05`, `DEL-08-04`, `DEL-10-02`, `DEL-10-03`, `DEL-10-10`, and `DEL-10-11`. **Three** are exceptions, each cited only as a member of a quoted register cell or as the owner of scope this deliverable does not touch: `DEL-00-01` (`pre-P1`, named only as a member of the `OBJ-005` `MappedDeliverables` cell quoted at CLM-004), `DEL-10-01` (the Step-0 cost baseline, `pre-P1`, named at CLM-019 only as one of the corpus's `MEASUREMENT`-typed rows), and `DEL-03-05` (stream-loss recovery, `P3`). No claim in this contract stages any named deliverable into a different phase, and the `P1` measurement boundary of this suite is therefore the two `P1` reconcile paths of `PKG-03` and nothing later: no stream or event path and no presence-tier path is a measured subject of this suite.
- **CLM-019** — This deliverable is typed `TEST_SUITE`, not `MEASUREMENT`. The corpus distinguishes the two types and uses both — among the `MEASUREMENT`-typed rows are `DEL-10-01` (Step-0 cost baseline, `pre-P1`) and `DEL-10-11` (parity metric report, `P1`); among the `TEST_SUITE`-typed rows are `DEL-08-04`, `DEL-10-02`, `DEL-10-03`, `DEL-10-10`, and this deliverable. Decision-log entry `DL-13` records that the `MEASUREMENT` type was added for §11 metric work, and §11 contains no performance metric (CLM-016). The typing is consistent with what the register asks of this deliverable — executable tests that exercise two paths, plus the record of what they measured — and this contract states no §11 metric obligation and no reporting cadence that no accepted source states.
- **CLM-020** — The deliverable is at lifecycle state `OPEN` with no implementation present. Every requirement, acceptance criterion, and verification method below states a contract on future production; none asserts that anything has been built, that any measurement has been taken, or that any bound has been confirmed.

- **TBD-001** — `ResponsibleParty` is unassigned; the register records `TBD`, with assignment at WORKING_ITEMS activation and not in this contract (`SOFTWARE_DECOMP.md` §5 preamble; `_CONTEXT.md`).
- **TBD-002** — The concrete identity of the measurement corpus — which loop or loops, which checkouts, which commit state, and what its size is in the counts the record-tier ingest is a function of — is fixed by no accepted source. This is the informational side of CON-002: REQ-004 obliges the corpus identity to be declared and recorded with every measurement, and settles nothing about which corpus is chosen.
- **TBD-003** — The measurement environment and method parameters — the machine and operating environment, whether the store, filesystem cache, and process are cold or warm at the start of a timed run, how many repetitions are taken, which statistic is reported, and what repeatability tolerance is applied — are fixed by no accepted source. They are chosen during production within REQ-004 and REQ-010 and recorded with the measurement.
- **TBD-004** — Where the recorded bound durably lives, and in what form, is fixed by no accepted source beyond the register phrase "recorded bound". It is chosen during production within REQ-003 and REQ-007, inside this deliverable's own write set.
- **TBD-005** — The suite's concrete invocation surface — its verb, its arguments, its exit-status contract, and whether it executes inside the `PKG-03` test run or as a separately invoked performance run — is fixed by no accepted source beyond the register phrase "Perf tests". It is chosen during production within REQ-001, REQ-002, and REQ-014.

## Completion and Reliance Basis — Epistemology

The requirements below state what future production must satisfy. Nothing in
this section asserts that a reconciler, an incremental engine, a store, a
corpus, a test, or a measurement exists, or that any bound has been confirmed.

- **REQ-001** — The suite shall measure the elapsed duration of a full rebuild executed through the upstream reconciler's single command as that contract obliges it (CLM-010), for the loops the declared measurement corpus spans. It shall implement no rebuild of its own, shall define no second rebuild command, and shall not reach the rebuild by any path other than that entry point.
- **REQ-002** — The suite shall measure the elapsed duration of an incremental reconcile executed through the upstream incremental engine as that contract obliges it (CLM-012). It shall implement no delta acquisition, no delta-to-work resolution, and no reconcile path of its own, and shall not reach the incremental path by any path other than that engine.
- **REQ-003** — The recorded bound shall distinguish, in every statement it makes, between (a) the register-stated target and clause text of `PEC-SVC-003` — "minutes" as an explicitly marked target for the rebuild, "within seconds" as the incremental clause — and (b) any value this suite measured. It shall present no register-stated target or clause as a measured value, and no measured value as a confirmed bound (REQ-013). Where a value is absent, the record shall say so explicitly rather than omit the field.
- **REQ-004** — Every measurement the suite records shall carry its measurement conditions: the identity of the corpus measured over, including the commit state and the size counts that identify it (TBD-002); the measurement environment and the cold-or-warm state of store, cache, and process at the start of the timed run; the repetition count; and the statistic reported (TBD-003). A measurement recorded without its conditions is prohibited.
- **REQ-005** — Every recorded rebuild measurement shall carry the coverage state of the rebuild it timed: whether that rebuild completed over every manifest-named feed for every loop in the corpus, or completed carrying stated coverage limitations, and if the latter, which loops and feeds those limitations named. The suite shall neither treat the two as interchangeable nor aggregate across them into a single reported figure. This requirement records the upstream open question (CLM-011, CON-003); it does not answer it, and no measurement or record produced under it may be read as answering it.
- **REQ-006** — Every recorded incremental measurement shall carry the subject of the run it timed: the baseline the run started from and where that baseline came from, the delta the run was given, and whether the run completed on the incremental path or fell back to the full-rebuild path as the upstream contract obliges for unresolvable change classes (CLM-012). A run that fell back shall not be recorded as an incremental measurement. This requirement records the upstream baseline-ownership gap (CLM-013, CON-004); it does not assign the missing obligation to any deliverable, and the suite shall not read a baseline out of, or write one into, another deliverable's artifact.
- **REQ-007** — The suite shall write only into its own test workspace and into the recorded bound. It shall create, modify, or delete no source file, no governed file, no register, no lifecycle file, and no path outside that write set. Where a measured run itself writes — the rebuild and the incremental reconcile write into the store and into the views the upstream entry point declares — those writes are the measured deliverable's under its own contract and are not this suite's write set; the suite shall add nothing to that set, declare no generated view of its own, and shall leave the measured corpus byte-identical across a measurement run.
- **REQ-008** — The suite shall perform no act owned by another deliverable. In particular it shall implement no reconciler, no incremental engine, no drift classification, no parity diff against practitioner-harness output, no stream-loss recovery act, no orientation-latency measurement, no examined-SHA or freshness stamping and no per-claim citation attachment, no §11 metric report, and no kill test; each is cited to its owner in CLM-016 and CLM-017, and none is discharged here. No test in this deliverable shall assert a criterion belonging to any of them.
- **REQ-009** — Nothing the suite captures, retains, or writes into the recorded bound shall carry file content or diff content, per `PEC-K-10`, whose statement reads in full: "**Content-minimal.** Paths, counts, SHAs, states, hashes — never file or diff content." A measurement record may carry paths, counts, identifiers, states, SHAs, hashes, and durations, and nothing else drawn from the corpus.
- **REQ-010** — The suite's measurement method shall be repeatable: repeated execution over the same corpus, the same commit state, and the same declared conditions shall reproduce each measurement within a declared tolerance, and that tolerance together with the repetition discipline that produced it shall be recorded with the measurement (TBD-003). A single unrepeated timing shall not be recorded as a measurement.
- **REQ-011** — The suite and the recorded bound shall introduce no third-party runtime dependency and no external network egress, per `PEC-SVC-001` and `PEC-SVC-002`, whose standing enforcement is `DEL-01-05` covering `SOW-052` and `SOW-053` (CLM-017).
- **REQ-012** — Nothing in this deliverable shall assert or require that an upstream reconciler, engine, store, schema, parser, registry, or corpus artifact exists. The suite is written against the upstream contracts quoted in CLM-010 through CLM-013, and where production must exercise a measurement path before a measured surface exists, it shall do so against an explicit interface-level stand-in identified as such, without discharging or constraining the deliverable that owns the real surface (CON-002).
- **REQ-013** — The suite shall not itself rule any bound confirmed. `PEC-SVC-003` states the rebuild bound as "confirmed at Phase 1" and no accepted source states its value, names the act that confirms it, or names who performs that act (CLM-003, CLM-016, CON-001). The recorded bound shall therefore state its confirmation field as unconfirmed, or as confirmed by a named dated act with a citation to that act, and shall never present this deliverable's own measurement as the confirmation. AC-015 routes the missing act to an accountable owner.
- **REQ-014** — Tests shall implement the verification methods declared in this contract; they shall not define scope, requirements, or acceptance criteria.

- **AC-001** — Every rebuild measurement is produced by invoking the upstream reconciler's single command; this deliverable's source contains no rebuild implementation and no second rebuild command; and the loops timed are exactly those the declared corpus spans.
- **AC-002** — Every incremental measurement is produced by invoking the upstream incremental engine; this deliverable's source contains no delta acquisition, no delta-to-work resolution, and no reconcile implementation of its own.
- **AC-003** — The recorded bound states the `PEC-SVC-003` target and clause text and any measured value as separately labelled fields; no register-stated target appears as a measured value and no measured value appears as a confirmed bound; the confirmation field is present and reads either unconfirmed or a named dated confirming act with its citation; and every absent value is stated as absent rather than omitted.
- **AC-004** — Every measurement in the recorded bound carries corpus identity including commit state and size counts, measurement environment, cold-or-warm start state, repetition count, and reported statistic; and no measurement appears without a complete conditions set.
- **AC-005** — Every rebuild measurement carries the coverage state of the rebuild it timed; for a fixture corpus seeded to produce stated coverage limitations, the limitation-bearing measurement is recorded separately from an unlimited one and the two are not aggregated; and no record or output of this deliverable states or implies a resolution of whether a limitation-bearing rebuild is a rebuild "in full".
- **AC-006** — Every incremental measurement carries its baseline, that baseline's provenance, the delta the run was given, and its completion path; a seeded run that falls back to the full-rebuild path is not recorded as an incremental measurement; and this deliverable's source contains no baseline write into, and no baseline read out of, another deliverable's artifact.
- **AC-007** — A measurement run leaves the measured corpus byte-identical; every filesystem write this deliverable itself performs resolves under its own test workspace or the recorded bound; and the module contains no write, create, or delete call against any source file, governed file, register, or lifecycle file, and declares no generated view of its own.
- **AC-008** — This deliverable's source contains no reconciler, incremental engine, drift-classification, parity-diff, stream-loss-recovery, orientation-latency, stamping, citation-attachment, §11-metric-report, or kill-test path; and no test in this deliverable asserts a criterion belonging to any of them.
- **AC-009** — For a content-dense fixture corpus, inspection of everything the suite captures, retains, and writes into the recorded bound finds no file content and no diff content — only paths, counts, identifiers, states, SHAs, hashes, and durations.
- **AC-010** — Repeated execution over the same corpus, commit state, and declared conditions reproduces each measurement within the declared tolerance; the tolerance and the repetition discipline appear in the recorded bound; and no single unrepeated timing is recorded as a measurement.
- **AC-011** — The suite and the recorded bound add no third-party runtime dependency and make no network call, leaving the standing zero-dependency and locality assertion intact.
- **AC-012** — No element of this deliverable asserts or requires that an upstream reconciler, engine, store, schema, parser, registry, or corpus artifact exists; every measurement path exercised before its measured surface exists runs against a stand-in explicitly identified as a stand-in; and no stand-in result is presented as a measurement of the real surface.
- **AC-013** — The performance test suite implements VER-001 through VER-012, executes in its declared run, passes, and introduces no acceptance criterion absent from this contract.
- **AC-014** — An accountable owner confirms that the attribution `SOW-054` → `OBJ-005` remains acceptable given the recorded **MEDIUM-LOW** rating at Q1.4, the record's own characterization of the recommendation as made "weakly — the row is a PKG-03 performance bound on the rebuild path", the recorded alternatives `OBJ-002` and `OBJ-005;OBJ-002`, and the recorded finding that `PEC-SVC-003`'s two clauses point at different objectives (CON-005).
- **AC-015** — An accountable owner records who confirms the Phase 1 rebuild bound, by what act, and against what value, or records that no such act is owed and that the recorded bound stands as measurement only; and states whether the seconds clause of `PEC-SVC-003` is itself a bound or a target, which its text does not mark (CON-001, CLM-003).
- **AC-016** — The REVIEW gate confirms this contract's traceability to `SOW-054` and `OBJ-005`; confirms that the attribution is stated as SCA-002-authored and owner-ruled at Gate 3, at the MEDIUM-LOW strength the record carries and no more; and confirms that no `PKG-01`, `PKG-02`, sibling `PKG-03`, `PKG-04`, `PKG-08`, or `PKG-10` scope has been absorbed.

- **CON-001** — The bound this deliverable exists to confirm is stated by no accepted source, and the confirming act is unowned. `PEC-SVC-003` records the rebuild bound as "confirmed at Phase 1 (target: minutes)" and the `PRD.md` §12 `P1` exit test names "rebuild-from-scratch ≤ bound" (CLM-016); neither states a value, names the act by which a bound becomes confirmed, nor names who performs it. The register `Description` for this deliverable uses the verb — "Confirm the P1 rebuild bound (target minutes)" — and the accepted corpus supplies no method for it. The incremental clause compounds the gap by asymmetry: "within seconds" carries no target marker and no confirmation act at all, so whether it is a bound already stated or a target still to be confirmed is undetermined by its own text (CLM-003). This contract records the gap rather than closing it. REQ-013 forbids the suite from ruling any bound confirmed on its own authority and obliges the confirmation state to be a recorded field, and AC-015 routes the missing act to an accountable owner. A production choice that fixed a numeric bound, or that treated this deliverable's measurement as the confirmation, would take a decision in the wrong place.
- **CON-002** — Both measured surfaces are owned upstream and neither exists. `INITIALIZED` on both edges means each upstream contract is the reliable input and no artifact is (CLM-010, CLM-012), so a measurement method written here binds to obligations rather than to implementations. That is a real limit on what production may fix: the concrete shape of a rebuild invocation, the incremental engine's invocation surface, the store's engine, and the record-tier field sets are all unsettled upstream and are cited in those contracts' own unresolved records. Production may exercise a measurement path against an explicit stand-in (REQ-012), but a stand-in result is not a measurement of the real surface, and a production choice here that fixed an upstream invocation surface, field set, or schema shape would take a decision in the wrong place.
- **CON-003** — Upstream-carried, not resolved here: the full-rebuild contract records that no accepted source states whether a rebuild that completed with stated coverage limitations counts as a rebuild "in full" for `SOW-010`'s purposes (CLM-011). The question lands on this deliverable with a sharpness it does not have upstream, because a duration is a single number and it is exactly the kind of claim into which a conditioning can silently disappear: a bound measured over a limitation-bearing rebuild is a different claim from a bound measured over an unconditioned one, and the two would be indistinguishable once reported as "the rebuild takes N minutes". REQ-005 therefore obliges the coverage state to travel with every rebuild measurement and prohibits aggregation across the two cases. That obligation makes the ambiguity visible in the recorded bound; it does not settle the upstream question, which remains open in its own contract and is neither resolved nor narrowed here.
- **CON-004** — Upstream-carried, not resolved here: the incremental contract records that the examined-SHA baseline its path presupposes is obliged by no accepted source and that no holder for a reconcile's examined-through SHA is named anywhere in the accepted corpus (CLM-013). A seconds-scale measurement of that path is a measurement of a run from some baseline over some delta, and both are undetermined at the level of accepted truth. REQ-006 obliges both to be recorded with every incremental measurement and prohibits the suite from reading a baseline out of, or writing one into, another deliverable's artifact. This contract assigns the missing obligation to no one; whether the reconcile-side baseline should be a shared obligation stated once for `PKG-03` is a scope-change question, not a production decision, and it is not answered by anything recorded here.
- **CON-005** — The objective attribution is qualified and the qualification is carried rather than smoothed. SCA-002 rated `SOW-054` → `OBJ-005` **MEDIUM-LOW** at Q1.4 — one of the lower ratings among the nine per-row attributions in that record, whose `Confidence` column carries `HIGH` twice, `MEDIUM-HIGH` once, `MEDIUM` three times, `MEDIUM-LOW` once (this row), `LOW-MEDIUM` once, and `LOW` once — recommended `OBJ-005` explicitly "weakly", and recorded `OBJ-002` and `OBJ-005;OBJ-002` as live alternatives on the ground that the two clauses of `PEC-SVC-003` point at different objectives. The same package corrected its own earlier truncation of that requirement at `C-20`, having cut the quotation "at exactly the clause pointing elsewhere". The owner ruled the question at Gate 3, all seven per-row attributions as recommended, and that ruled attribution is the accepted one and is used throughout this contract without reinterpretation. What this contract declines to do is restate a weakly recommended MEDIUM-LOW attribution as though it were unconditional: AC-014 routes the qualification, with its recorded alternatives, to an accountable owner at REVIEW. The clause-to-edge correspondence recorded at CLM-005 is deliberately not used as an argument here in either direction — it is the same two clauses the packet reasoned from, and reasoning from them again locally would be substituting this contract's judgment for a ruling that has already been made.
- **CON-006** — What "the current corpus" denotes is fixed by no accepted source. The phrase occurs three times in the accepted basis and its source corpus and is defined at none of them: `PEC-SVC-003` ("Full rebuild of the current corpus"), `PEC-API-002` ("≤100 ms at p95 against the current corpus"), and the `SOW-041` SSOW row that restates the latter. The register `Description` for this deliverable repeats it once more ("against the current corpus"). A performance bound is meaningless without the corpus it is a bound over, and a bound measured over a corpus of one loop is a different claim from the same bound measured over five. This contract does not choose the corpus and does not read the phrase as fixing one: REQ-004 obliges the corpus actually measured over to be identified in the record, with the commit state and the size counts that make the identification checkable, so that the recorded bound states its own subject (TBD-002). Whether `PEC-SVC-003`'s "current corpus" denotes a particular loop set at a particular time is a question for the accepted sources, not for this deliverable's production.

## Production and Verification Method — Praxeology

Production proceeds in the order upstream-contract survey → measurement-record
schema and conditions vocabulary → corpus declaration and fixture construction
→ rebuild-path measurement → incremental-path measurement → conditioning and
repeatability → recorded bound → tests. The upstream-contract survey comes
first because both predecessors are at `INITIALIZED` and supply obligations
rather than artifacts, so a measurement harness written against an imagined
invocation surface would violate CON-002 before any code existed. The
measurement-record schema comes second, ahead of any timing, because this
deliverable's characteristic failure is a number recorded without its subject:
if the conditioning fields (REQ-004, REQ-005, REQ-006) are added after the
first measurements exist, the first measurements will not have them. All work
is bounded to this deliverable folder and the `PKG-03` test surface it names;
this contract authorizes no register, decomposition, PRD, or
upstream-deliverable edit, and it neither builds nor reshapes the reconciler,
the incremental engine, the store, the entity model, or the corpus it measures
over. Tests implement the verification methods below and create no scope.

- **VER-001** — Rebuild-path measurement exercise: execute the timed rebuild through the upstream entry point over the declared corpus and capture the invocation record showing the command used; grep this deliverable's source for a rebuild implementation and for any second rebuild command, asserting none; and compare the loop set actually timed against the declared corpus, asserting equality.
- **VER-002** — Incremental-path measurement exercise: execute the timed incremental reconcile through the upstream engine and capture the invocation record; grep this deliverable's source for delta acquisition, delta-to-work resolution, and reconcile implementation, asserting none is present.
- **VER-003** — Recorded-bound field inspection: read the recorded bound and assert field by field that the `PEC-SVC-003` target and clause text and any measured value occupy separately labelled fields, that no target appears as a measured value and no measured value as a confirmed bound, that the confirmation field is present and reads either unconfirmed or a named dated confirming act with its citation, and that every absent value is explicitly stated absent.
- **VER-004** — Conditions-completeness inspection: for every measurement in the recorded bound, assert the presence of corpus identity with commit state and size counts, measurement environment, cold-or-warm start state, repetition count, and reported statistic; assert that no measurement lacks any of them.
- **VER-005** — Coverage-conditioning exercise: run the timed rebuild over a fixture corpus seeded to produce stated coverage limitations and over one seeded to produce none; assert each resulting measurement carries its coverage state and names the limited loops and feeds where applicable; assert the two are recorded separately and no aggregate figure spans them; and inspect the recorded bound and this deliverable's source for any statement resolving whether a limitation-bearing rebuild is a rebuild "in full", asserting none.
- **VER-006** — Incremental-subject exercise: run the timed incremental reconcile from a recorded baseline over a seeded delta and assert the measurement carries the baseline, its provenance, the delta, and the completion path; seed a change class that forces the upstream fallback and assert the resulting run is not recorded as an incremental measurement; grep this deliverable's source for a baseline write into or read out of another deliverable's artifact, asserting none.
- **VER-007** — Write-boundary exercise: hash the measured corpus tree before and after a measurement run and assert byte-identity; capture every filesystem write this deliverable itself performs and assert each resolves under its own test workspace or the recorded bound; inspect the module for write, create, or delete calls against source files, governed files, registers, or lifecycle files and for any generated-view declaration, asserting none.
- **VER-008** — Boundary inspection: inspect this deliverable's source and call graph for reconciler, incremental-engine, drift-classification, parity-diff, stream-loss-recovery, orientation-latency, stamping, citation-attachment, §11-metric-report, and kill-test paths, asserting each absent; review this deliverable's tests for any criterion belonging to another deliverable, asserting none.
- **VER-009** — Content-minimal inspection: run the suite over a content-dense fixture corpus carrying long prose bodies, quoted authored text, and diff-shaped content, then dump everything the suite captures, retains, and writes into the recorded bound and assert field by field that it carries only paths, counts, identifiers, states, SHAs, hashes, and durations.
- **VER-010** — Repeatability exercise: execute the full measurement set at least twice over the same corpus, commit state, and declared conditions and assert each measurement reproduces within the declared tolerance; read the recorded bound and assert the tolerance and repetition discipline are recorded; inspect the record for any measurement derived from a single unrepeated timing, asserting none.
- **VER-011** — Inspect this deliverable's dependency manifest and import graph for third-party runtime dependencies and network calls, and re-run the zero-dependency and locality enforcement once the deliverable that owns it is available, without discharging it here.
- **VER-012** — Upstream-assumption inspection: grep this deliverable's source, fixtures, and call surface for any assertion or requirement that an upstream reconciler, engine, store, schema, parser, registry, or corpus artifact exists, asserting none; enumerate every stand-in used and assert each is identified as a stand-in at its use site and in any record it contributes to; assert no stand-in result appears in the recorded bound as a measurement of the real surface.
- **VER-013** — Run this deliverable's declared test run and confirm that each of VER-001 through VER-012 has a corresponding executing automated test and that no test asserts a criterion absent from this contract.

## Governing Values and Decisions — Axiology

- **AX-001** — `OBJ-005` governs: everything PEC holds can be deleted at any moment without blocking any governed act. A rebuild is what makes deletion survivable, and a rebuild whose duration is unknown makes deletability a claim nobody has priced. This deliverable is where that price is measured. It does not make the record tier deletable — the store lifecycle and the rebuild command do — but an unmeasured rebuild leaves `OBJ-005` true in principle and untested in practice, which is the condition `PEC-SVC-003` exists to end.
- **AX-002** — `PEC-K-01` graceful absence is `OBJ-005`'s product invariant and it sets this deliverable's honesty standard rather than its scope. "Deleting PEC blocks nothing" is only credible if what deletion costs is known and stated; a bound recorded without the conditions under which it was measured would substitute a reassuring number for that knowledge. REQ-004, REQ-005, and REQ-006 are that standard written as checkable obligations, and they are why this contract treats a conditioning field as part of the measurement rather than as commentary on it.
- **AX-003** — A measurement is a claim about a subject, and this deliverable's characteristic failure mode is losing the subject. Durations aggregate easily, read authoritatively, and carry none of their own qualifications; "the rebuild takes N minutes" survives every context it is cut from. That is why the conditioning requirements are stated as prohibitions on recording rather than as recommendations for reporting, and why REQ-010 refuses a single unrepeated timing the status of a measurement.
- **AX-004** — `PEC-K-10` content-minimal binds this deliverable even though it writes no record-tier fact. A performance record is a natural place for a corpus excerpt to appear as an explanatory aid — a sample of the file that made a rebuild slow, a diff that shows why a delta was large — and the rule admits no such exception. REQ-009 restates the restriction over the suite's own surface so that the recorded bound cannot become the one durable artifact in `P1` that holds what the store may not.
- **AX-005** — `PEC-K-07` — "Ingest is best-effort; reconciliation is guaranteed. Streams optimize freshness; the reconciler over file truth is the source of every record-tier fact." — is why both measured paths matter and why they are not interchangeable. The incremental path is an optimization inside the guarantee, not a second guarantee, and its upstream contract obliges it to fall back to the rebuild where equivalence cannot be established. A seconds-scale figure taken from a run that fell back would be timing the guarantee and reporting the optimization, which is why REQ-006 makes the completion path a recorded field.
- **AX-006** — `PEC-K-02` files govern, and it bounds what this deliverable's own output is: "**Files govern.** The record tier is regenerated from sources by one command; the presence tier is expected to be lost on rebuild; the database is gitignored and safe to delete; PEC output is never citable as authority; rulings and lifecycle state remain file-native." The recorded bound is a measurement record, not a ruling. It can state what was measured and under what conditions; it cannot make a bound confirmed, and REQ-013 states that limit as an obligation rather than leaving it to restraint.
- **AX-007** — `DL-11` is the decision that gives this deliverable its shape: the rebuild bounds came to `PKG-03` "as reconcile performance" while the reconciler entry point and the incremental engine stayed with their own deliverables (CLM-006). Absorbing either measured surface — building a faster rebuild path to measure, or an incremental engine to time — would undo that decision under the appearance of thoroughness. This contract measures and records; it builds neither thing it measures.
- **AX-008** — Edge direction is a constraint on this contract, not a licence. `RequiredMaturity` `INITIALIZED` on both upstream edges means each upstream *contract* is the reliable input, not any upstream artifact; this contract is written against the obligations quoted in CLM-010 through CLM-013 and asserts nothing about upstream implementation state. Measuring two contracts imposes no obligation on either of them: CON-003 and CON-004 record gaps in the upstream record and assign work in neither place, and the two predecessors' own contracts already record this deliverable as the measurer, measured from outside.
- **AX-009** — Both edges cited here are `PROPOSAL` stratum and are *accepted* at that stratum: `D-PEC-62` §1(4) records the owner accepting the DAG candidate v0.2 exhibit "accepted, all strata as presented", and that packet reads "as presented" as accepting the exhibit's **flags as flags**, so what remains recorded-but-unresolved is the specific annotated set — `E-A11` (AMBIGUOUS_BASIS), `E-P69`/`E-N02` (PHASE_TENSION), `E-N13`/`E-N18` (LOW_CONFIDENCE), the `C-02` direction, and the `C-08` standing-node set — none of which touches `[E-P30]` or `[E-P31]`, both of which carry an empty `Flag` column in the exhibit. Register-wide constraint `C-10` `STRATUM_RULE` ends "strata are provenance not authority"; citation does not convert `PROPOSAL` to `DECLARED`. That both edges additionally carry an empty `BasisCitation` in the exhibit and an empty `EvidenceQuote` with a "location TBD" `SourceRef` in the register (CLM-009) is a fact about the evidence trail, not a defect in their acceptance, and this contract records it rather than supplying the missing evidence.
- **AX-010** — This deliverable is not a standing node and does not claim to be one. The `C-08` `STANDING_NODES` set names five deliverables and this is not among them (CLM-015), and the accepted graph records it as terminal, with no downstream consumer. The `P1` exit test names the bound it measures (CLM-016), but naming is not the same as gating, and the corpus's own record of which nodes gate releases excludes this one. This contract therefore states the relation exactly as the sources state it and asserts no release-gating force of its own — a discipline that matters precisely because a performance bound is the kind of artifact whose authority is easy to assume.
- **AX-011** — The objective mapping is stated at record strength and no higher. `SOW-054` → `OBJ-005` is SCA-002-authored and owner-ruled at Gate 3, and the same record rates it MEDIUM-LOW, recommends it weakly, and preserves two alternatives (CON-005). This contract uses the ruled attribution and supplies no fresh derivation of it; AC-014 asks an accountable owner to confirm the qualification rather than asking REVIEW to re-derive a ruling, and AC-016 asks REVIEW to check that this contract has stated the warrant at that strength and not above it.
- **AX-012** — Unknowns stay marked. TBD-001 through TBD-005 and CON-001 through CON-006 are recorded rather than resolved by inference, and two of the six conflicts are explicitly upstream-carried. `C-03` `PACKAGE_LEVEL`, `C-04` `PHASE_PRECEDENCE`, and `C-10` `STRATUM_RULE` are register-wide non-gating constraints recorded in `_DEPENDENCIES.md`, and blocker output under the `FULL_GRAPH` mode at threshold `INITIALIZED` is advisory visibility only, never work assignment. This contract is lifecycle-neutral: `_STATUS.md` remains the sole lifecycle authority and is untouched by the run that authored this document; the deliverable is at `OPEN` and nothing has been built.

**Quotation record.** Every quotation in this contract is verbatim from the
named source. **Exactly one quotation is elided**, at two points, both marked
with ellipses at the point of elision and enumerated here in full: the `DL-11`
Decision-cell quotation in CLM-006, elided before the `SOW-054` clause (from
"Phase 4 forced boundary assignments:" through the clauses preceding it) and
after the `SOW-054` clause (the clauses following it). No other quotation in
this document omits text from the span it presents. Quoted spans shorter than
their containing record are presented as whole sentences, whole table rows,
whole register rows, whole cells, whole action-register cells, or short
verbatim phrases, and are attributed as such at the point of quotation: the
`A001` target cell, the `A002` preamble and its `DEL-03-06` row, the `A003b`
`OBJ-005` old/new block, the per-row attribution table row, the Q1.4 heading
and its truncation note, two-clause block and options block, the `C-20`
correction row, the Part 8 Q1 table row, and the Gate 3 ruling row are each
complete lines, rows, or blocks of the SCA-002 package; the `DL-11` Rationale
cell, the `OI-013` Finding cell, the `SOW-054` ledger row and its SSOW row, the
`C-03` and `C-08` register cells, and the `PKG-03` charter cells are complete
register cells or rows; the `PEC-SVC-003`, `PEC-K-01`, `PEC-K-02`, `PEC-K-07`,
`PEC-K-10`, `OBJ-005`, and `PRD.md` §12 quotations are each complete rows or
complete sentences of their sources; the `SOW-041` statement quoted in CLM-017
is a complete register cell, while the `PEC-API-002` span quoted in CON-006 —
"≤100 ms at p95 against the current corpus" — is a short verbatim phrase of that
requirement's `PRD.md` §9.6 row rather than the whole row; the twelve upstream
records quoted in CLM-010 through CLM-013 — six from `DEL-03-01` at CLM-010,
one at CLM-011, four from `DEL-03-02` at CLM-012, and one at CLM-013 — are each
quoted in full, except the `DEL-03-02` conflict record quoted in CLM-013, which
is identified there as the first paragraph of a two-paragraph record and is
complete within that paragraph; the additional `DEL-03-01` conflict-record
sentence quoted in CLM-011 is identified there as the first sentence of a
longer record; and the
`D-PEC-62` acceptance phrases quoted in AX-009 are short verbatim phrases,
identified there as such.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-054 OBJ-005 | REQ-001, CLM-002, CLM-005, CLM-010, TBD-005 | AC-001 | VER-001 | The rebuild invocation record showing the upstream command used, a recorded search of this deliverable's source for a rebuild implementation or second command, and the timed loop set compared against the declared corpus |
| OUT-001 | SOW-054 OBJ-005 | REQ-002, CLM-012, TBD-005 | AC-002 | VER-002 | The incremental invocation record showing the upstream engine used, plus a recorded search of this deliverable's source for delta acquisition, delta-to-work resolution, and reconcile implementation |
| OUT-002 | SOW-054 OBJ-005 | REQ-003, REQ-013, CLM-003, CLM-016, CON-001, TBD-004 | AC-003 | VER-003 | Field-by-field inspection of the recorded bound showing separately labelled target, clause, measured-value, and confirmation fields, with absent values stated absent |
| OUT-002 | SOW-054 OBJ-005 | REQ-004, CLM-007, CON-006, TBD-002, TBD-003 | AC-004 | VER-004 | The conditions set attached to every recorded measurement — corpus identity with commit state and size counts, environment, cold-or-warm start, repetition count, reported statistic |
| OUT-002 | SOW-054 OBJ-005 | REQ-005, CLM-011, CON-003, AX-003 | AC-005 | VER-005 | Limitation-seeded and unlimited rebuild measurements recorded separately, each carrying its coverage state and named limited loops and feeds, plus a recorded search for any statement resolving the upstream "in full" question |
| OUT-002 | SOW-054 OBJ-005 | REQ-006, CLM-013, CON-004, AX-005 | AC-006 | VER-006 | Incremental measurements carrying baseline, baseline provenance, delta, and completion path; the forced-fallback run shown excluded from the incremental record; a recorded search for cross-deliverable baseline reads or writes |
| OUT-001 | SOW-054 OBJ-005 | REQ-007, CLM-009, TBD-004 | AC-007 | VER-007 | Before/after measured-corpus tree hashes, the captured inventory of this deliverable's own filesystem writes each resolved to its workspace or the recorded bound, and the source inspection record for governed-file writes and view declarations |
| OUT-001 | SOW-054 OBJ-005 | REQ-008, CLM-006, CLM-016, CLM-017, CLM-018, CLM-019, AX-007 | AC-008 | VER-008 | Source and call-graph inspection records showing each named adjacent path absent, plus a review of this deliverable's tests confirming no criterion belonging to another deliverable |
| OUT-002 | SOW-054 OBJ-005 | REQ-009, AX-004 | AC-009 | VER-009 | Field-by-field dumps of everything captured, retained, and written into the recorded bound for a content-dense fixture corpus, showing only paths, counts, identifiers, states, SHAs, hashes, and durations |
| OUT-001 | SOW-054 OBJ-005 | REQ-010, TBD-003, AX-003 | AC-010 | VER-010 | The repeated measurement set with per-measurement reproduction inside the declared tolerance, the tolerance and repetition discipline as recorded, and the inspection record showing no single-timing measurement |
| OUT-001 | SOW-054 OBJ-005 | REQ-011, CLM-017 | AC-011 | VER-011 | Dependency-manifest and import-graph inspection records, plus the zero-dependency and locality enforcement result once the deliverable that owns it is available |
| OUT-001 | SOW-054 OBJ-005 | REQ-012, CLM-010, CLM-012, CLM-014, CON-002, AX-008 | AC-012 | VER-012 | Recorded searches of source, fixtures, and call surface for upstream-artifact assumptions, the enumerated stand-in inventory with its use-site identifications, and the recorded bound checked for stand-in results |
| OUT-001 | SOW-054 OBJ-005 | REQ-014, CLM-020 | AC-013 | VER-013 | Declared test-run output mapping each executed test to its declared verification method, with no criterion asserted that this contract does not state |
| OUT-002 | SOW-054 OBJ-005 | CLM-001, CLM-004, CLM-005, CON-005, AX-011 | AC-014 | HUMAN_REVIEW: accountable owner confirmation that the MEDIUM-LOW attribution of SOW-054 to OBJ-005 stands, given the Q1.4 rating, the recommendation recorded as made weakly, the recorded alternatives OBJ-002 and OBJ-005;OBJ-002, and the recorded finding that PEC-SVC-003's two clauses point at different objectives | Dated owner ruling recorded against this deliverable, explicitly addressing the Q1.4 qualification and its recorded alternatives rather than restating the attribution |
| OUT-002 | SOW-054 OBJ-005 | CLM-003, CLM-015, CLM-016, CON-001, AX-006, AX-010 | AC-015 | HUMAN_REVIEW: accountable owner record of who confirms the Phase 1 rebuild bound, by what act and against what value, or that no such act is owed and the recorded bound stands as measurement only, and of whether the seconds clause of PEC-SVC-003 is a bound or a target | Dated owner ruling recorded against this deliverable, naming the confirming act and its owner or declining one, and dispositioning the unmarked seconds clause |
| OUT-001 | SOW-054 OBJ-005 | CLM-008, CLM-009, AX-001, AX-002, AX-009, AX-012 | AC-016 | HUMAN_REVIEW: REVIEW gate confirms traceability to SOW-054 and OBJ-005, confirms the attribution is stated as SCA-002-authored and owner-ruled at Gate 3 at the MEDIUM-LOW strength the record carries, and confirms no upstream, sibling, or cross-package scope absorption | Review record citing the SOW-054 ledger row, the A001 target cell and A002 row, the A003b OBJ-005 block, the Q1.4 rating and Gate 3 ruling, and the upstream, sibling, and cross-package deliverable boundaries |
