---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-10-02
package_id: PKG-10
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@3623b958b
project_scope_refs: [SOW-055]
package_objective_refs: [OBJ-005]
---

# Scope of Work — DEL-10-02 Kill test (standing release gate)

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-10-02` — "Kill test
(standing release gate)" — in `PKG-10` (Validation & Measurement) of the PEC v2
build. It covers project scope item `SOW-055` in service of package objective
`OBJ-005`.

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.2** (`status: current_basis`, `SCA-002` successor accepted
2026-07-25 under `D-PEC-64`), pinned at commit `3623b958b`. The
deliverable-local `_REFERENCES.md` still names "revision 1.1, accepted working
surface"; that phrase is superseded provenance left by a deferred pointer sweep
(`SCA-002` `Handoff_State` open item `OI-B`), and `_CONTEXT.md`'s own
supersession line records revision 1.1 as "superseded by revision 1.2
(`current_basis`, SCA-002 successor)". This contract cites revision 1.2.

**Standing character (load-bearing), and what authorizes it.** Everything below
is written as a contract on a *continuing* verification: there is no state in
which this deliverable's assertion is finished, and a passing run is evidence
for the release candidate it evaluated and for no later one. That framing is
directed by this run's brief under `D-PEC-63`, whose directing sentence reads,
verbatim:

> Author this contract as a STANDING assertion — a continuously re-runnable
> verification, not a one-shot artifact.

That sentence is carried durably at
`execution/_Coordination/WAVE_D-PEC-63/BATCH_B5_FANIN.md`, the batch fan-in
record for the batch this run belongs to, which the dispatcher writes in this
tranche and which records it verbatim. The framing is additionally
supported — for this deliverable and unlike its sibling standing nodes — by the
accepted sources themselves, which state the standing release-gate character in
their own words (CLM-001, CLM-002, CLM-004). What those sources do *not* settle
is the register-level `C-08` classification's force, which remains
owner-unconfirmed and is carried at CON-001 and routed at AC-013 rather than
resolved here (CLM-009).

**Objective warrant.** The `SOW-055` → `OBJ-005` attribution is
**register-direct and pre-`SCA-002`**, and this contract states it at that
strength. Two accepted records establish it. First, the live `ScopeLedger.csv`
row for `SOW-055` carries `OBJ-005` in its `ObjectiveIDs` column (CLM-001).
Second, `SCA-002` — the amendment that populated objective mappings for the
Phase 2.2 wave — records the `OBJ-005` §3 cells it changed, and both the scope
item and this deliverable stand unchanged on either side of that change:

> ```
> OLD col4: SOW-010, SOW-055; bound by C1/C2 across all items
> NEW col4: SOW-010, SOW-021, SOW-025, SOW-052..056, SOW-088; bound by C1/C2 across all items
> OLD col5: DEL-03-01, DEL-10-02
> NEW col5: DEL-00-01, DEL-01-03, DEL-01-05, DEL-03-01, DEL-03-06, DEL-10-02, DEL-10-03
> ```
>
> (`execution/_ScopeChange/SCA-002_2026-07-25_1042/Amendment_Preview.md`, action
> `A003b`, "Line 324 · `OBJ-005`". Quoted in full, not elided. ID-shaped text
> inside this quotation is upstream source context, not a local definition or
> reference.)

`SOW-055` appears in the OLD column-4 value and `DEL-10-02` in the OLD column-5
value; neither was added by the amendment, and `DEL-10-02` was not in the
amendment's deliverable-row target set. The warrant is therefore a register
fact, not an `SCA-002` derivation, and this contract asserts no confidence label
for it and creates no owner-confirmation criterion for it.

One qualification belongs in the record and is stated rather than smoothed.
`SCA-002` withdrew this row's use as an *attribution precedent for other rows*:

> | ~~`SOW-055` kill test → `DEL-10-02` → `OBJ-005`~~ | — | **WITHDRAWN.** `SOW-055` reads "delete the store, run representative governed workflows, nothing blocks"; `OBJ-005` reads "Everything PEC holds can be deleted at any moment without blocking any governed act". The scope item is a near-verbatim restatement of the objective, so its mapping is a tautology. It explains nothing about `SOW-025` and cannot select between candidates. Using it to give `DEL-10-03` HIGH confidence was wrong |
>
> (`Amendment_Preview.md`, "Register precedents (measured) — and one I
> withdraw", columns `Precedent | Mapping | Status`; the correction is logged as
> `C-18`: "**`SOW-055` precedent withdrawn as tautological** — it restates
> OBJ-005 nearly verbatim and selects nothing for `SOW-025`". Both quoted in
> full, neither elided. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference.)

What was withdrawn is the row's power to *select an objective for a different
scope item*. What the same text affirms is that this scope item restates this
objective near-verbatim — which is the strongest possible form of the mapping
for this row and the reason no confidence label is needed here. AX-001 records
the consequence: the near-identity is why this deliverable is where `OBJ-005` is
executably tested, and why absorbing neighbouring scope into it would be a
category error rather than a convenience.

Source chain, in order of authority for this contract:

1. `execution/_Decomposition/ScopeLedger.csv`, row `SOW-055` (CLM-001) and its
   two-part `SourceRef` into `docs/PRD.md` — `PEC-SVC-004` (CLM-002) and §11
   metric 6 (CLM-003).
2. The product invariants the ledger row and the accepted edges carry:
   `PEC-K-01` (ledger `Notes` "Carries PEC-K-01"; CLM-004) and `PEC-K-02`
   (cited by edge `[E-P72]`'s `EvidenceQuote`; CLM-005).
3. `execution/_Decomposition/SOFTWARE_DECOMP.md` §3 objective row `OBJ-005`
   (CLM-006), §5 `PKG-10` deliverable row and the `Deliverables.csv` row
   (CLM-007), and §4 `PKG-10` package charter (CLM-008).
4. The accepted dependency-DAG gate exhibit and its `C-08` constraint row, as
   ruled at `D-PEC-62` (CLM-009), and the two `EXECUTION` upstream edges
   `[E-P71]` and `[E-P72]` (CLM-010, CLM-011).
5. The two upstream `INITIALIZED` contracts, read as contracts (CLM-010,
   CLM-011), and the deliverable-local control files (`_CONTEXT.md`,
   `_REFERENCES.md`, `_DEPENDENCIES.md`, `Dependencies.csv`, `_STATUS.md`).

- **CLM-001** — The accepted `ScopeLedger.csv` row for `SOW-055` reads in full, under the register's column order `ScopeItemID,InOutStatus,ScopeItemStatement,SourceRef,PackageID,DeliverableIDs,ObjectiveIDs,DecisionRef,OpenIssue,Notes`:

  > `SOW-055,IN,"Maintain the kill test — delete the store, run representative governed workflows, nothing blocks — as a standing, executable release gate","PEC-SVC-004, §11.6",PKG-10,DEL-10-02,OBJ-005,,FALSE,Carries PEC-K-01`
  >
  > (`DecisionRef` empty; `OpenIssue` `FALSE`; `Notes` "Carries PEC-K-01".
  > Quoted in full, not elided. ID-shaped text inside this quotation is upstream
  > source context, not a local definition or reference.)

  The scope item's own text carries three things this contract must hold apart: the executable act (delete, run, assert), the *standing* character ("as a standing, executable release gate"), and the maintenance obligation ("Maintain"). None of the three is a later inference; all three are the ledger's own words.

- **CLM-002** — The first limb of the `SourceRef` cell is `PEC-SVC-004`, `docs/PRD.md` §10 (Service requirements), quoted in full: "The kill test — delete the store, run representative governed workflows, nothing blocks — is a standing release gate (PEC-K-01)."
- **CLM-003** — The second limb is `docs/PRD.md` §11 (Success metrics), item 6, quoted in full: "Kill test: pass, at every release."
- **CLM-004** — The product invariant the ledger `Notes` cell names is `PEC-K-01`, `docs/PRD.md` §6, quoted in full: "**Graceful absence.** No governed act may require a PEC read or write. Deleting PEC blocks nothing. The kill test (§12) passes at every release." The §12 cross-reference resolves to the release-strategy table, whose `P1` row names the kill test among its exit tests — "Parity-diff vs harness clean or explained; rebuild-from-scratch ≤ bound; kill test passes" — but does not define the test; the definition of record is `PEC-SVC-004` (CLM-002). This contract cites the definition to `PEC-SVC-004` and treats §12 as the release-strategy locus that names it, not as a second definition.
- **CLM-005** — `PEC-K-02`, cited by edge `[E-P72]`'s `EvidenceQuote` (CLM-011), reads in full (`docs/PRD.md` §6): "**Files govern.** The record tier is regenerated from sources by one command; the presence tier is expected to be lost on rebuild; the database is gitignored and safe to delete; PEC output is never citable as authority; rulings and lifecycle state remain file-native." Three clauses bear on this contract: the store is safe to delete, the record tier is regenerated by one command, and the presence tier is *expected* to be lost — so a kill test that treated presence loss as a failure would be testing against the invariant rather than for it.
- **CLM-006** — The `OBJ-005` row of `SOFTWARE_DECOMP.md` §3 reads in full, under the columns `ObjectiveID | Statement | SourceRef | Mapped Scope Items | MappedDeliverables`:

  > | OBJ-005 | Everything PEC holds can be deleted at any moment without blocking any governed act | §3.5 | SOW-010, SOW-021, SOW-025, SOW-052..056, SOW-088; bound by C1/C2 across all items | DEL-00-01, DEL-01-03, DEL-01-05, DEL-03-01, DEL-03-06, DEL-10-02, DEL-10-03 |
  >
  > (Quoted in full, not elided. ID-shaped text inside this quotation is
  > upstream source context, not a local definition or reference.)

  Its `SourceRef` §3.5 is `docs/PRD.md` §3 product outcome 5: "All of the above can be deleted at any moment without blocking any governed act." Seven deliverables are mapped to the objective at revision 1.2; this is one of them.

- **CLM-007** — The identity of record. `Deliverables.csv`, row `DEL-10-02`, reads in full under the columns `DeliverableID,PackageID,Name,Description,Type,ResponsibleParty,AnticipatedArtifacts,CoversScopeItems,SupportsObjectives,ContextEnvelope,ContextEnvelopeNotes,PhaseHint`:

  > `DEL-10-02,PKG-10,Kill test (standing release gate),"Executable: delete the store, run representative governed workflows, nothing blocks. Runs at every release.",TEST_SUITE,TBD,Kill-test harness + gate wiring,SOW-055,OBJ-005,M,,P1`
  >
  > (Quoted in full, not elided. ID-shaped text inside this quotation is
  > upstream source context, not a local definition or reference.)

  The `SOFTWARE_DECOMP.md` §5 `PKG-10` table row for the same deliverable reads "| DEL-10-02 | Kill test (standing release gate) | TEST_SUITE | M | P1 | SOW-055 |". The `ContextEnvelopeNotes` field is empty and `_CONTEXT.md` records "(none)"; there are no envelope notes to carry. The `AnticipatedArtifacts` value is a **two-part** artifact bound — "Kill-test harness + gate wiring" — and it bounds this contract's outputs to exactly those two and to the components each declares as part of itself.

- **CLM-008** — The package charter. `SOFTWARE_DECOMP.md` §4, row `PKG-10`, under the columns `PackageID | Name | Scope Description (work domain) | Assigned (count) | Exclusions`, reads in full:

  > | PKG-10 | Validation & Measurement | Release-gating proof and metrics: kill test, no-ruling-write verification, Step-0 baseline, defect/adoption/collision/parity measurement, seeded-conflict, TTL-honesty and stream-loss tests, usage observability, directed bootstrap progression evidence | SOW-025, 055, 058..064, 084, 085, 093 (12) | The behaviors under test (their home packages) |
  >
  > (Quoted in full, not elided. ID-shaped text inside this quotation is
  > upstream source context, not a local definition or reference.)

  The package's `Exclusions` cell excludes "The behaviors under test (their home packages)" from `PKG-10`'s scope. §4 declares no dependency column and none is claimed here; the boundary conclusion in AX-006 rests on that exclusion.

- **CLM-009** — `DEL-10-02` is named in constraint row `C-08` `STANDING_NODES` of the accepted dependency-DAG gate exhibit (`execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md`), whose row reads in full under the exhibit's constraint columns:

  > `C-08,STANDING_NODES,"DEL-01-05, DEL-03-04, DEL-10-02, DEL-10-03, DEL-10-10","Own text: ""Automated assertion"" / ""Permanent"" / ""Runs at every release"" / ""tested property"" / ""standing validation""",Standing obligations: excluded from one-shot COMPLETE/UNBLOCKED arithmetic; they gate releases not successors,R3-F9; owner confirmation requested. DEL-10-10 is the bootstrap progression record itself`
  >
  > (Quoted in full, not elided. ID-shaped text inside this quotation is
  > upstream source context, not a local definition or reference.)

  The evidence cell's phrase "Runs at every release" is this deliverable's own register `Description` text (CLM-007). Five deliverables are members. At `D-PEC-62` §1(4) the owner accepted the DAG candidate "**accepted, all strata as presented**", and that packet fixes the reading:

  > This packet reads "as presented" as accepting the exhibit **flags as flags** — E-A11 (AMBIGUOUS_BASIS), E-P69/E-N02 (PHASE_TENSION), E-N13/E-N18 (LOW_CONFIDENCE), C-02 direction, C-08 standing-node set remain recorded-but-unresolved, non-gating annotations; each flag is carried verbatim into the seeded rows' `Notes`.
  >
  > (`execution/_Coordination/_DECISIONS/D-PEC-62_project_setup_scaffold_and_local_dependency_registers.md`
  > §1(4). Quoted in full, not elided. ID-shaped text inside this quotation is
  > upstream source context, not a local definition or reference.)

  What is settled is the arithmetic exclusion: `C-08` is a non-gating constraint row and this deliverable is excluded from one-shot `COMPLETE`/`UNBLOCKED` counting. What is not settled is the classification's force — what a standing node's "they gate releases not successors" operationally binds. The deliverable-local `_DEPENDENCIES.md` compresses this to "(owner-confirmed at D-PEC-62 ruling)"; that phrase is accurate as to the arithmetic exclusion and overstates the rest, and this contract cites the `D-PEC-62` text over the local paraphrase. CON-001 records the residue.

- **CLM-010** — `[E-P71]`, the first of this deliverable's two `EXECUTION` upstream edges, is `Dependencies.csv` row `DEP-10-02-003` (`RegisterSchemaVersion` `v3.1`). Attributed by column: `DependencyClass` `EXECUTION`, `AnchorType` `NOT_APPLICABLE`, `Direction` `UPSTREAM`, `DependencyType` `PREREQUISITE`, `TargetType` `DELIVERABLE`, `TargetPackageID` `PKG-01`, `TargetDeliverableID` `DEL-01-03`, `TargetName` "Store bootstrap & content-minimal guard", `Statement` "Kill test exercises store safe-delete semantics", `EvidenceFile` `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md`, `SourceRef` and `EvidenceQuote` both `SOW-055: "delete the store"`, `Explicitness` `IMPLICIT`, `RequiredMaturity` `INITIALIZED`, `ProposedMaturity` `TBD`, `SatisfactionStatus` `PENDING`, `Confidence` `MEDIUM`, `Origin` `EXTRACTED`, `Status` `ACTIVE`, `Notes` "PROPOSAL; Flag=none; EdgeID=E-P71". The gate exhibit's own edge row reads `E-P71,DEL-01-03,DEL-10-02,PROPOSAL,TESTS,,"SOW-055: ""delete the store""",Kill test exercises store safe-delete semantics` under the exhibit columns `EdgeID,PredecessorID,SuccessorID,Stratum,EdgeKind,Flag,BasisCitation,Rationale`, with `Flag` empty and `EdgeKind` `TESTS`.

  The upstream deliverable's own accepted contract obliges the store lifecycle this test exercises:

  > - **REQ-002** — The store shall be safe to delete at any moment. The lifecycle
  >   module shall provide an explicit delete operation and shall recreate a valid
  >   empty store on next start without manual repair. Deletion shall block no
  >   governed act, per `PEC-K-01`.
  > - **REQ-003** — Every write into the store shall pass through one declared
  >   ingest boundary. No store write path may bypass the guard, including writes
  >   originating inside the service core.
  >
  > (`DEL-01-03/ScopeOfWork.md`, Epistemology section; both records quoted in
  > full, neither elided. ID-shaped text inside this quotation is upstream source
  > context, not a local definition or reference.)

  That contract records the division of duty from its own side, and records it twice — once as a claim and once as a governing value:

  > - **CLM-010** — The system-level kill test is not this deliverable's scope.
  >   `SOW-055` — "delete the store, run representative governed workflows,
  >   nothing blocks" — is covered by `DEL-10-02` (Kill test, standing release
  >   gate), and the accepted edge `[E-P71]` runs `DEL-01-03` → `DEL-10-02` with
  >   `EdgeKind` `TESTS`: `DEL-10-02` is the tester and this deliverable is the
  >   tested surface. `DEL-10-02` will exercise this deliverable's safe-delete
  >   behaviour from outside, against representative governed workflows. This
  >   contract binds only the store-local property that makes that outside test
  >   possible; it neither runs nor discharges the kill test.
  > - **AX-004** — Enforcement duties are separated across deliverables and this
  >   contract produces only its own: the standing kill-test gate is `DEL-10-02`
  >   (`SOW-055`), the reconciler write restriction is `DEL-03-01` (`SOW-021`,
  >   `PEC-RCN-006`), zero-dependency and locality enforcement is `DEL-01-05`
  >   (`SOW-052`, `SOW-053`), and ingest-activity logging is `DEL-01-04`
  >   (`SOW-057`, serving `OBJ-006`). Nothing here discharges those obligations.
  >
  > (`DEL-01-03/ScopeOfWork.md`, Ontology and Axiology sections; both records
  > quoted in full, neither elided. ID-shaped text inside this quotation is
  > upstream source context, not a local definition or reference.)

  This contract is the other side of that division. It binds to the upstream *obligations* — an explicit delete operation, recreation without manual repair, and a store whose deletion blocks no governed act — as the store-side behaviour it exercises, and it defines no store path, no ignore rule, no delete operation, and no recreate semantics of its own.

- **CLM-011** — `[E-P72]`, the second `EXECUTION` upstream edge, is `Dependencies.csv` row `DEP-10-02-004`. Attributed by column: the shared field values of `DEP-10-02-003` above apply unchanged for `DependencyClass`, `AnchorType`, `Direction`, `DependencyType`, `TargetType`, `EvidenceFile`, `Explicitness`, `RequiredMaturity`, `ProposedMaturity`, `SatisfactionStatus`, `Confidence`, `Origin`, and `Status`; the row differs at `TargetPackageID` `PKG-03`, `TargetDeliverableID` `DEL-03-01`, `TargetName` "Full-rebuild reconciler (one command)", `Statement` "Kill test proves rebuildability after deletion", `SourceRef` and `EvidenceQuote` both "SOW-055 + PEC-K-02", and `Notes` "PROPOSAL; Flag=none; EdgeID=E-P72". The gate exhibit's edge row reads `E-P72,DEL-03-01,DEL-10-02,PROPOSAL,TESTS,,SOW-055 + PEC-K-02,Kill test proves rebuildability after deletion`, `Flag` empty, `EdgeKind` `TESTS`.

  Two points of care. First, "proves rebuildability after deletion" is the register's statement of *why this edge exists*, sourced to `SOW-055` plus `PEC-K-02` — it is the recorded basis of a dependency relation, not an additional scope item. `SOW-055`'s own three-part act remains delete → run → assert nothing blocks. REQ-008 binds the rebuild leg only to the extent this accepted edge states it, and mints no rebuild obligation of its own.

  Second, the upstream contract's rebuild obligation is conditioned in its own text, and this contract carries the conditioning rather than smoothing it:

  > - **REQ-001** — The reconciler shall expose a single command that rebuilds the
  >   record tier in full from file sources for every loop the registry names,
  >   per `SOW-010` (CLM-001) and `PEC-RCN-001` (CLM-003). A rebuild shall
  >   require no operator step, repair action, or manual sequence beyond that one
  >   invocation.
  > - **REQ-003** — The rebuild shall complete against a store that is absent,
  >   newly deleted, or empty, obtaining the store through the upstream
  >   store-lifecycle interface quoted in CLM-013 and requiring no manual repair.
  >   This deliverable shall implement no store path resolution, no ignore-rule
  >   registration, no store creation, and no store deletion of its own; those
  >   are the upstream deliverable's under `SOW-056` (CLM-008, CLM-013).
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
  > (`DEL-03-01/ScopeOfWork.md`, Epistemology section; all four records quoted in
  > full, none elided. ID-shaped text inside this quotation is upstream source
  > context, not a local definition or reference.)

  That contract also records the direction of this edge from its own side:

  > `DEL-10-02` is the tester and this deliverable is the tested surface; the
  > kill test is exercised on this deliverable from outside, under `SOW-055`,
  > and is neither run nor discharged here (REQ-014).
  >
  > (`DEL-03-01/ScopeOfWork.md`, `CLM-017`, closing sentence quoted in full, not
  > elided. ID-shaped text inside this quotation is upstream source context, not
  > a local definition or reference.)

  The limitation-bearing-rebuild question is therefore live for this contract too: a rebuild that completes with stated coverage limitations may or may not satisfy "in full", and CON-003 carries that forward unresolved rather than deciding it inside a test.

- **CLM-012** — A sibling relation, stated as an observation with its actual basis and not as a dependency. `DEL-10-03` (No-ruling-write verification) is a fellow `C-08` standing node in `PKG-10` (CLM-009) and its accepted contract obliges a suite that "shall expose a binding interface through which an externally owned change path or release gate can invoke it without modification to the suite", stating expressly that "this contract delivers no gate wiring and places no obligation on any other deliverable to re-run, re-certify, or maintain anything", and locating gate wiring by register fact — "it is the sibling row `DEL-10-02` that carries 'Kill-test harness + gate wiring' in its `AnticipatedArtifacts`". **No register edge exists between `DEL-10-02` and `DEL-10-03`**: this deliverable's `Dependencies.csv` holds exactly four rows — two `ANCHOR` rows (`DEP-10-02-001` package anchor, `DEP-10-02-002` `SOW-055` requirement trace) and the two `EXECUTION` rows of CLM-010 and CLM-011 — and names no sibling. The observation is recorded because it bears on OUT-002's shape, not because it creates an obligation in either direction: nothing in this contract requires `DEL-10-03` to be invoked, and nothing here may be read as claiming a dependency the register does not state. One residue follows and is stated positively rather than left as a disclaimer: that sibling's `OUT-001` locates the binding of its negative-surface suite into an actual release gate as owned downstream, and as at this contract's fan-in date no accepted contract owns that binding — this contract's OUT-002 wiring covers the kill-test harness of OUT-001 and nothing else. That is an observation of the accepted corpus at fan-in, not a new constraint on this contract or on any other, and it neither creates nor implies an obligation here.
- **CLM-013** — Both upstream predecessors are at lifecycle state `INITIALIZED`, the maturity both edges require. `INITIALIZED` means each upstream **contract** is the reliable input: each accepted `ScopeOfWork.md` exists, and no store, delete operation, reconciler, or rebuild command does. `DEL-10-02` is itself at lifecycle state `OPEN` (`_STATUS.md`) with no implementation present. Every requirement, acceptance criterion, and verification method below states a contract on future production; none asserts that any harness, wiring, workflow, store, or rebuild has been built.

## Deliverable Definition — Ontology

`DEL-10-02` is typed `TEST_SUITE` at Context Envelope `M` with `PhaseHint` `P1`
and no `ContextEnvelopeNotes`. Its description of record is "Executable: delete
the store, run representative governed workflows, nothing blocks. Runs at every
release", and its anticipated artifacts are "Kill-test harness + gate wiring"
(CLM-007). That two-part artifact bound is the outer edge of this contract's
outputs: there are exactly two, and no third is minted.

- **OUT-001** — The kill-test harness: an executable, re-runnable mechanism that places the system in a no-store state, runs a recorded set of representative governed workflows against that state, and asserts that none is blocked — failing, and naming what blocked, whenever one is. Two records are components of this output rather than further artifacts, because each is the harness's own declaration of what it did and against what standard: the **recorded workflow set**, naming each representative governed workflow the harness runs and the basis on which it was selected (REQ-002, TBD-002), and the **recorded blocking definition**, the operative test by which the harness classifies a workflow as blocked (REQ-003, TBD-003). `Deliverables.csv` names the harness as one of exactly two artifact classes for this deliverable and admits no third.
- **OUT-002** — The gate wiring: the binding that makes OUT-001 a standing release gate rather than a script someone remembers to run — the registration through which the harness is invoked for each release candidate without further action, together with its own record of what release path it binds into and what it does when there is none. The wiring is the second of the register's two named artifact classes and is owned here, not by any sibling deliverable (CLM-012). Whether an accepted release path exists to bind into is not established by any accepted source; CON-002 carries that gap and REQ-010 requires it to be reported rather than papered over.

Unresolved information carried forward, not invented:

- **TBD-001** — `ResponsibleParty` is unassigned; `Deliverables.csv` and `_CONTEXT.md` both record `TBD`, with assignment at WORKING_ITEMS activation.
- **TBD-002** — Which governed workflows are "representative" is not enumerated by any accepted source. `SOW-055`, `PEC-SVC-004`, and the register `Description` all use the word without a list. The accepted corpus does supply candidate material — `docs/PRD.md` §12 records that "The PEC v2 build itself runs through the governed pipeline (SOFTWARE_DECOMP → PROJECT_SETUP → WORKING_ITEMS)", and the directed bootstrap of `SOW-064` makes that build PEC's first ingestion corpus — but naming a representative set is a production act bounded by REQ-002, not a fact this contract may assert. Selecting the set does not select *scope*: every workflow the harness runs is a governed act exercised as it already is, never defined here.
- **TBD-003** — The operative test for "nothing blocks" is not fixed beyond `PEC-K-01`'s wording, "No governed act may require a PEC read or write" (CLM-004). Where a governed act completes but more slowly, or completes while reporting that an orientation feed is absent, is not settled by any accepted source; `PEC-ORI-006` establishes that stating a measurement limitation is the correct behaviour rather than a fault, which bears on the classification but does not fix its boundary. REQ-003 requires the decision to be recorded; it is not made here.
- **TBD-004** — The harness's concrete mechanism, invocation surface, and repository home are not fixed by any accepted source; `Deliverables.csv` names the artifact classes and nothing further.
- **TBD-005** — By what means the store is deleted for the test is not fixed. The upstream contract obliges "an explicit delete operation" (CLM-010) while `PEC-K-02` states the database is "gitignored and safe to delete" as a property of the object itself (CLM-005), which admits deletion out of band. Whether the tested property covers one means or both is not stated by any accepted source; REQ-004 requires the harness to record which means it exercises rather than leaving the coverage implicit.

Unresolved constraints carried into this contract, neither resolved nor
narrowed by authoring:

- **CON-001** — The `C-08` `STANDING_NODES` classification's *force* is unconfirmed. The row records "owner confirmation requested" in its own `Notes` and `D-PEC-62` §1(4) accepted the standing-node set as a recorded-but-unresolved, non-gating annotation rather than ruling it (CLM-009). This deliverable is a case where that residue must be stated precisely rather than borrowed from a sibling: the accepted product sources already state that the kill test *is* a standing release gate (CLM-001, CLM-002, CLM-004), so what is open here is not whether the kill test has release-gate character but what a blocking verdict operationally binds — which release process must honour it, and with what consequence for a candidate that fails or was never evaluated. AC-013 routes exactly that question to an accountable owner. This contract neither asserts the operative authority nor waives it, and no production choice may settle it.
- **CON-002** — No accepted source establishes a release process, pipeline, or CI system for the PEC v2 build into which OUT-002 can be wired. `docs/PRD.md` §12 defines release *phases* with exit tests, which is a strategy, not a mechanism; the sibling `DEL-01-05` contract records the same gap from its own side, stating that "no accepted source names a CI system for the PEC v2 build" (cited as a corroborating observation on a sibling contract, not as authority for this one). REQ-010 therefore binds the wiring conditionally: it binds into whatever release path exists at production time, and where none is accepted it reports the absence explicitly rather than presenting an unarmed gate as armed. Establishing a release path is not authorized by this contract and is not within `AnticipatedArtifacts`; if production finds nothing to wire into, that is an escalation, not a licence to build one.
- **CON-003** — Whether a rebuild that completes with stated coverage limitations satisfies the rebuildability leg of `[E-P72]` is unresolved upstream and is inherited here. The upstream contract records that no accepted source states whether such a rebuild "counts as a full rebuild", and takes neither reading as settled (CLM-011). A kill test cannot answer that question by passing or failing: a pass over a limitation-bearing rebuild would silently adopt the permissive reading, and a fail would silently adopt the strict one. REQ-008 requires the harness to carry the reported limitation into its own result and to report the ambiguity rather than resolve it; a resolution belongs to a scope-change or an owner ruling on `SOW-010`, not to this deliverable's production.
- **CON-004** — Nothing this harness exercises exists. Both upstream contracts are at `INITIALIZED` (CLM-013), so there is no store to delete, no delete operation to call, and no rebuild command to invoke; and the representative governed workflows of TBD-002 are the surrounding project's acts, not artifacts of this deliverable. This contract binds to obligations, not to artifacts, and must not be read as asserting that any of them exists or as pre-empting the open questions the upstream contracts record in their own terms.

## Completion and Reliance Basis — Epistemology

The requirements below state the contract the future harness and wiring must
satisfy. Under the standing character established above — carried by the ledger
row's own words and by the brief's direction (CLM-001, AX-003) — they bind the
mechanism's *continuing* behaviour: each is a property that must hold on every
release candidate the harness evaluates, not a one-time production event.

- **REQ-001** — The harness shall execute the three-part property `SOW-055` states as one act: place the system in a state with the store deleted, run the recorded representative governed workflows against that state, and assert that none is blocked. It shall fail whenever a workflow is blocked, and shall name the workflow, the step at which it blocked, and the PEC dependency it required.
- **REQ-002** — The representative governed-workflow set shall be recorded with the harness rather than left implicit in harness code, naming each workflow the harness runs and the basis on which it was selected (TBD-002). The record shall be readable and revisable without changing what the harness asserts, so that widening or narrowing coverage is a visible act rather than a code detail.
- **REQ-003** — The operative test by which a workflow is classified as blocked shall be recorded with the harness, grounded in `PEC-K-01`'s "No governed act may require a PEC read or write", and shall state its treatment of the cases the accepted sources leave open (TBD-003) — in particular an act that completes while reporting an absent or unparseable feed, which `PEC-ORI-006` establishes as correct behaviour rather than a fault. Every classification the harness makes shall trace to that recorded test.
- **REQ-004** — The deletion step shall place the system in a state with no store present and shall record by which means it did so (TBD-005). The harness shall implement no store path resolution, no ignore-rule registration, no store creation, no delete operation, and no recreate semantics of its own; those are the upstream deliverable's obligations under `SOW-056` (CLM-010). Obtaining the deleted state shall not require PEC to be available, so that the precondition of the test does not depend on the thing under test.
- **REQ-005** — Workflows shall be exercised as they are. Where a governed workflow cannot be run in full and is substituted, stubbed, or partially exercised, the substitution shall be reported as an explicit coverage limitation of that run, and a run carrying such a limitation shall never be presented as an unqualified pass over the workflow it stood in for.
- **REQ-006** — The harness shall be fail-closed: an unavailable workflow, a workflow that could not be started, an unreachable deleted-store state, or a tooling error is a failure of the run, never a pass, a skip, or an empty successful result over the smaller set the harness managed to reach.
- **REQ-007** — The harness shall observe, not participate. It shall not modify any governed file, source, register, or lifecycle file; it shall not disable, weaken, stub, or bypass any governed gate or approval in order to make a workflow complete; and any state it creates for a run shall be disposed of or declared, leaving the checkout it ran in unchanged apart from its own declared outputs.
- **REQ-008** — Where the harness exercises rebuildability after deletion — the relation the accepted edge `[E-P72]` records, sourced to `SOW-055` and `PEC-K-02` (CLM-011) — it shall obtain the rebuild through the one-command rebuild the upstream contract obliges and shall implement no rebuild of its own. It shall carry any coverage limitation that rebuild reports into its own result, and shall neither present a limitation-bearing rebuild as an unqualified full rebuild nor treat one as a failure of the kill test; the unresolved reading is reported, not decided (CON-003). Presence-tier loss across the deleted-and-rebuilt boundary is the expected outcome per `PEC-K-02` and `PEC-K-05` and shall not be reported as a block.
- **REQ-009** — The harness shall be built as a standing verification: re-runnable on demand and re-evaluated against every release candidate presented to it, against that exact candidate state. It shall have no completion state, and no passing run shall be carried forward as evidence for any later state. It shall expose a binding interface through which OUT-002, or any externally owned release path, can invoke it without modification to the harness.
- **REQ-010** — The gate wiring shall bind the harness into the release path so that it is invoked for each release candidate without further action, and shall record the release path it binds into. Where no accepted release path exists (CON-002), the wiring shall report that absence explicitly — as an unarmed gate naming what it is waiting for — and shall never present itself as armed. The wiring shall not create a release process, and disabling, removing, or bypassing it shall be a visible change producing a reported failure rather than a silent no-op.
- **REQ-011** — The mechanism shall be designed to block: for a release candidate on which the kill test fails, or against which it has not been executed, it shall return an explicit blocking verdict rather than a pass, a skip, or an absent result. This requirement binds the mechanism's design intent and the verdict it produces. It does not, by itself, settle what that verdict operationally binds; that follows the pending `C-08` confirmation recorded at CON-001 and is routed to the owner at AC-013.
- **REQ-012** — The harness and its wiring shall define no scope belonging elsewhere. They shall define no store semantics and no store lifecycle behaviour (`DEL-01-03` under `SOW-056`), no rebuild behaviour or rebuild bound (`DEL-03-01` under `SOW-010`; `DEL-03-06` under `SOW-054`), and no governed workflow; they shall not restate, narrow, or widen `PEC-K-01`; and they shall place no obligation on any other deliverable to re-run, re-certify, or maintain anything.
- **REQ-013** — Failure and coverage shall be reported explicitly and locatably. A run shall account for every workflow in the recorded set as run, blocked, or not run with a stated reason, and shall never report a pass over a workflow it did not actually run.
- **REQ-014** — Tests and deterministic checks shall implement the verification methods declared below. They shall not define scope, requirements, or acceptance criteria: the property verified here comes from `SOW-055`, `PEC-SVC-004`, and `PEC-K-01`, and the two outputs exist because the accepted register names them.

Acceptance criteria for `DEL-10-02`. Each states a property the future
implementation must exhibit; none asserts a present state.

- **AC-001** — On a fixture release candidate whose governed workflows complete with the store deleted, the harness passes; on a candidate in which a governed workflow requires a PEC read or write and cannot proceed, it fails and names the workflow, the blocking step, and the PEC dependency required.
- **AC-002** — The representative governed-workflow set is recorded with the harness, each entry carries the basis on which it was selected, every workflow the harness runs appears in it, and the harness runs no workflow absent from it; changing the set is a change to that record rather than to what the harness asserts.
- **AC-003** — The blocking definition is recorded with the harness, cites `PEC-K-01`, and states its treatment of the open cases of TBD-003 including an act that completes while reporting an absent or unparseable feed; every pass and fail classification in a run traces to that recorded test, and no outcome depends on an unrecorded reading.
- **AC-004** — The harness reaches a verified no-store state before running any workflow, records the means by which the store was deleted, and reaches that state without requiring PEC to be available; inspection of the harness finds no store path resolution, ignore-rule registration, store creation, delete operation, or recreate implementation of its own.
- **AC-005** — For a fixture run in which a workflow is substituted, stubbed, or only partially exercised, the run result carries that coverage limitation explicitly and is not presented as an unqualified pass over the workflow stood in for.
- **AC-006** — Given an unavailable workflow, a workflow that cannot be started, an unreachable deleted-store state, and an induced tooling error in turn, the harness reports failure; no such condition yields a pass, a skip, or an empty successful result.
- **AC-007** — A full run leaves the checkout's governed files, sources, registers, and lifecycle files byte-identical apart from the harness's own declared outputs; inspection finds no path by which the harness disables, weakens, stubs, or bypasses a governed gate or approval, and any run-created state is disposed of or declared.
- **AC-008** — Where the harness exercises rebuild after deletion, the rebuild is obtained through the upstream one-command rebuild rather than reimplemented; a fixture rebuild that reports coverage limitations produces a run result carrying those limitations and an explicit statement that the "in full" reading is unresolved, with neither an unqualified pass nor a kill-test failure asserted on that basis; and presence-tier loss across the boundary is not reported as a block.
- **AC-009** — The harness re-runs without modification against any release candidate presented to it, producing an execution bound to the exact candidate it evaluated, presenting no earlier passing run as evidence for a later candidate, and having no state in which it is complete; its binding interface can be invoked by an external caller without modifying the harness.
- **AC-010** — The wiring invokes the harness for each release candidate without further action and records the release path it binds into; where no accepted release path exists it reports itself unarmed and names what it awaits, rather than reporting a pass or presenting itself as armed; and disabling, removing, or bypassing the wiring produces a reported failure rather than a silent no-op.
- **AC-011** — On a release candidate deliberately constructed so that a governed workflow blocks with the store deleted, and on one against which the kill test was withheld, the mechanism returns an explicit blocking verdict. What that verdict binds is CON-001 and AC-013, not this criterion.
- **AC-012** — The delivered harness and wiring trace to `SOW-055` and `OBJ-005` and introduce no scope beyond that ledger row: they define no store semantics, no rebuild behaviour, no rebuild bound, and no governed workflow; they impose no obligation on `DEL-01-03`, `DEL-03-01`, or any sibling; they add no output beyond the register's two artifact classes; and no test within them asserts a criterion this contract does not state.
- **AC-013** — An accountable owner confirms, or declines to confirm, what a blocking verdict from this mechanism operationally binds — which release process must honour it and with what consequence for a candidate that fails or was never evaluated — given that `C-08`'s standing-node classification carries "owner confirmation requested" in its own `Notes` and was accepted at `D-PEC-62` §1(4) as a recorded-but-unresolved, non-gating annotation, while `SOW-055` and `PEC-SVC-004` already state the kill test to be a standing release gate (CLM-001, CLM-002, CLM-009, CON-001). A decline leaves the mechanism's verdicts advisory as to process and invalidates no other criterion in this contract; the standing character of the contract stands either way, because it is carried by the ledger row's own words.

## Production and Verification Method — Praxeology

Expected production sequence: record the representative workflow set and the
blocking definition (REQ-002, REQ-003) before building any assertion, because
every later verdict depends on both; then build the deletion step and the run
loop against the upstream obligations (REQ-004, REQ-005, REQ-008); then make the
harness fail-closed and its reporting locatable (REQ-006, REQ-013); then make it
standing and expose its binding interface (REQ-009); and only then build the
wiring (REQ-010, REQ-011), so that what is bound into a release path is what was
actually built. Where CON-002 holds and no accepted release path exists, the
wiring stage terminates in an explicit unarmed report and an escalation, not in a
release process invented here. All work is bounded to this deliverable's own
artifacts and to running the surrounding project's governed workflows as they
are; this contract authorizes no register, decomposition, or PRD edit, no edit to
any other deliverable, and no change to any governed gate. The verification
methods below are themselves standing: each is re-run on every evaluated release
candidate, not once at hand-over.

- **VER-001** — Execute the harness against a conforming fixture release candidate and against fixtures in which a governed workflow requires a PEC read or write with the store deleted; assert a pass on the conforming fixture and, on each blocking fixture, a failure naming the workflow, the blocking step, and the required PEC dependency.
- **VER-002** — Inspect the recorded workflow set for completeness and basis; compare it against the workflows a run actually executes and assert set equality in both directions; then add and remove an entry and assert the executed set follows the record without a change to the harness's assertions.
- **VER-003** — Inspect the recorded blocking definition against the `PEC-K-01` wording and against the open cases of TBD-003; trace a sample of pass and fail classifications from a run back to that record and confirm none rests on an unrecorded reading; include a fixture in which a workflow completes while reporting an absent feed and assert the recorded treatment is applied.
- **VER-004** — Deletion-step exercise: assert the harness verifies the no-store state before running any workflow and records the deletion means; run it with PEC unavailable and assert the deleted state is still reached; then search the harness source for store path resolution, ignore-rule registration, store creation, delete-operation, and recreate implementations and assert none is present.
- **VER-005** — Substitution reporting: run the harness over a fixture in which a workflow is substituted, one in which it is stubbed, and one in which it is only partially exercised; assert per case that the result carries the coverage limitation explicitly and that no such result is presented as an unqualified pass.
- **VER-006** — Fault injection: run the harness with a workflow unavailable, a workflow that cannot be started, an unreachable deleted-store state, and an induced tooling error; assert a reported failure in every case with no pass, skip, or empty success.
- **VER-007** — Boundary and self-inspection: hash the checkout's governed files, sources, registers, and lifecycle files before and after a full run and assert byte-identity apart from the harness's declared outputs; inspect the harness for any path that disables, weakens, stubs, or bypasses a governed gate or approval and assert none; assert every run-created state is disposed of or declared.
- **VER-008** — Rebuild-leg exercise on fixtures: assert the rebuild is invoked through the upstream one-command interface and that the harness contains no rebuild of its own; run against a fixture rebuild that reports coverage limitations and assert the run result carries those limitations together with an explicit statement that the "in full" reading is unresolved, asserting neither an unqualified pass nor a kill-test failure on that basis; and assert presence-tier loss across the boundary is not classified as a block.
- **VER-009** — Standing-behaviour demonstration on scratch fixtures: present the harness with a sequence of release candidates; assert an execution is produced for each, bound to the candidate it evaluated, with no result reused across candidates and no completion state reachable; then invoke the harness's binding interface from a scratch caller against a candidate it has not evaluated and assert it reports the missing evaluation rather than a pass, a skip, or a silent no-op.
- **VER-010** — Wiring exercise: assert the wiring invokes the harness for each candidate in a scratch candidate sequence without further action and that its recorded binding names the release path used; run it in a scratch state with no release path available and assert it reports itself unarmed and names what it awaits; then disable, remove, and bypass the wiring in turn and assert a reported failure rather than a silent no-op in each case. The method exercises scratch fixtures and creates no release process.
- **VER-011** — Blocking-verdict demonstration: submit a release candidate on which a governed workflow blocks with the store deleted, and one against which the kill test was withheld; assert that the mechanism returns an explicit blocking verdict in both cases. The method demonstrates the mechanism's verdict, not any release process's obligation to honour it (CON-001).
- **VER-012** — Scope-boundary review: inspect the harness and wiring for store-semantic, rebuild, rebuild-bound, and governed-workflow definitions and assert none is present; confirm the delivered artifact set is exactly the register's two classes and their declared components; confirm the declared inputs cite the two upstream contracts' obligations without restating, constraining, or extending them and assert no obligation on any sibling; and review every test for a criterion absent from this contract, asserting none.

## Governing Values and Decisions — Axiology

- **AX-001** — `OBJ-005` governs: everything PEC holds can be deleted at any moment without blocking any governed act. The `SCA-002` record observes that `SOW-055` restates that objective near-verbatim (CLM-001 and the withdrawal quoted above). What that near-identity makes this deliverable is the place where the objective stops being a statement and becomes an executable assertion — and it is also why the boundary matters most here: an objective-shaped scope item invites absorption of every neighbouring deliverable that serves the same objective, and AX-006 refuses it.
- **AX-002** — `PEC-K-01` graceful absence is the product invariant this contract exists to keep checkable. Its own text makes the test constitutive rather than confirmatory — "Deleting PEC blocks nothing. The kill test (§12) passes at every release" — so a kill test that could not be run, or that passed without running, would leave the invariant asserted rather than held. The falsification clause of `docs/PRD.md` §11 rests on the same footing: "PEC is deleted and, by PEC-K-01, nothing breaks" is a claim this deliverable is the standing evidence for.
- **AX-003** — The standing shape of this contract is doubly grounded, and the two grounds are kept distinct. The ledger row itself requires the kill test be maintained "as a standing, executable release gate", and `PEC-SVC-004` states it "is a standing release gate" — that is accepted source truth. Separately, this run's brief directs the contract be authored as a standing assertion, and the `C-08` annotation classifies the deliverable as a standing node whose force is unconfirmed (CLM-009, CON-001). The framing below is therefore neither borrowed from the annotation nor dependent on it: treating a passing run as completion would contradict the ledger row's own words. What remains open is only what a blocking verdict binds, routed at AC-013.
- **AX-004** — Edge direction is a discipline, not a formality. `[E-P71]` and `[E-P72]` name this deliverable as the tester and `DEL-01-03` and `DEL-03-01` as the tested, and both upstream contracts record the same from their own side, each stating that it neither runs nor discharges the kill test (CLM-010, CLM-011). This contract therefore takes their obligations as the surface it exercises and absorbs none of their scope: it defines no store lifecycle and no rebuild (REQ-004, REQ-008, REQ-012), and it imposes nothing on them.
- **AX-005** — Stratum is provenance, not authority. Both upstream edges are `PROPOSAL` stratum, accepted "all strata as presented" at `D-PEC-62` §1(4), which that packet reads as taking the exhibit's flags as flags; neither edge carries a flag, and both are cited here by `EdgeID` at that status without conversion to `DECLARED`. `C-10` `STRATUM_RULE`'s own text ends "strata are provenance not authority", and `_DEPENDENCIES.md` records that blocker output is "advisory visibility only — never work assignment".
- **AX-006** — The kill test has one home, and that home is bounded on both sides. `PKG-10`'s `Exclusions` cell excludes "The behaviors under test (their home packages)" from this package's scope (CLM-008): the store's safe-delete semantics belong to `DEL-01-03`, rebuildability to `DEL-03-01`, and every representative governed workflow to whatever loop owns it. Symmetrically, `AnticipatedArtifacts` names two artifact classes and the sibling contract that would otherwise have carried gate wiring records that it belongs to this row (CLM-012). Absorbing sibling scope and shedding owned scope are the same failure seen from two directions; REQ-012 and AC-012 guard both.
- **AX-007** — `PEC-K-06` observation-not-participation governs the harness itself, whose invariant lineage `docs/PRD.md` §6 records as "verification creates findings, never rewrites sources". A kill test that disabled a governed gate, edited a governed file, or stubbed away an approval in order to make a workflow complete would manufacture the very result it exists to check. REQ-007 and AC-007 exist for that reason, and they bind more tightly here than for a test that reads a surface, because this harness *runs* governed work.
- **AX-008** — `PEC-ORI-006` honesty governs the failure and coverage modes: "Where a feed is unparseable or stale, the response shall state the measurement limitation explicitly; silent omission is prohibited." A kill test that passed over workflows it did not run, or over a substitution it did not report, is indistinguishable from one that ran them — and because this test is the standing evidence for `PEC-K-01`, an unreported gap in it is an unreported gap in the product's central claim. REQ-005, REQ-006, and REQ-013 are that rule applied to a harness rather than to a response.
- **AX-009** — `C-04` `PHASE_PRECEDENCE` is a register-wide non-gating constraint and phase hints are release-strategy ordering whose hard-versus-soft classification is a Phase 1.3 owner ruling. `DEL-10-02`, `DEL-01-03`, and `DEL-03-01` all carry `PhaseHint` `P1` in `Deliverables.csv`, so no phase tension arises among them; this contract makes no staging claim beyond recording that fact.
- **AX-010** — The accepted basis is `SOFTWARE_DECOMP.md` revision 1.2 at commit `3623b958b`, accepted through `SCA-002` under `D-PEC-64`. The revision 1.1 phrase still present in `_REFERENCES.md` is superseded provenance awaiting a deferred pointer sweep; it is recorded here so the divergence is visible rather than silently normalized.
- **AX-011** — Unknowns remain marked. TBD-001 through TBD-005 and CON-001 through CON-004 are recorded rather than resolved by inference. In particular, nothing this harness exercises exists yet, the representative set is unnamed, the "in full" rebuild reading is an upstream open question, and no release path is established; a production choice that settled any of them would take a decision in the wrong place.
- **AX-012** — This contract is lifecycle-neutral. `_STATUS.md` remains the sole lifecycle authority, is untouched by the run that authored this document, and records `OPEN`; nothing here asserts that any harness, wiring, workflow, store, or rebuild exists.

**Quotation record.** Every quotation in this contract is verbatim from the
named source and every one is quoted in full. **Zero quotations are elided**;
no ellipsis appears in any quoted span, and no quotation omits text from the
span it presents.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-055 OBJ-005 | REQ-001, REQ-013, CLM-001, CLM-002, CLM-004 | AC-001 | VER-001 | Fixture release candidates with expected verdicts, and harness output naming the blocked workflow, the blocking step, and the PEC dependency required, together with a per-run account of every workflow as run, blocked, or not run with a stated reason |
| OUT-001 | SOW-055 OBJ-005 | REQ-002, CLM-003, TBD-002 | AC-002 | VER-002 | The recorded representative governed-workflow set with a selection basis per entry, a two-way comparison against the workflows a run executed, and an add/remove demonstration showing the executed set follows the record |
| OUT-001 | SOW-055 OBJ-005 | REQ-003, CLM-004, TBD-003 | AC-003 | VER-003 | The recorded blocking definition read against the PEC-K-01 wording and the open cases, plus classification traces from a run back to that record including the completes-while-reporting-an-absent-feed fixture |
| OUT-001 | SOW-055 OBJ-005 | REQ-004, CLM-005, CLM-010, TBD-005 | AC-004 | VER-004 | Pre-run no-store verification records, the recorded deletion means, a PEC-unavailable deletion transcript, and a recorded search of the harness for store path, ignore-rule, creation, delete, and recreate implementations |
| OUT-001 | SOW-055 OBJ-005 | REQ-005, CON-004, AX-008 | AC-005 | VER-005 | Run results for substituted, stubbed, and partially exercised workflow fixtures, each carrying its coverage limitation and none presented as an unqualified pass |
| OUT-001 | SOW-055 OBJ-005 | REQ-006, TBD-004 | AC-006 | VER-006 | Fault-injection transcripts showing a reported failure for an unavailable workflow, an unstartable workflow, an unreachable deleted-store state, and an induced tooling error, with no pass, skip, or empty success |
| OUT-001 | SOW-055 OBJ-005 | REQ-007, AX-007 | AC-007 | VER-007 | Before/after hashes of governed files, sources, registers, and lifecycle files for a full run; inspection findings showing no gate-disabling, weakening, stubbing, or bypass path; and the disposal-or-declaration record for run-created state |
| OUT-001 | SOW-055 OBJ-005 | REQ-008, CLM-011, CON-003 | AC-008 | VER-008 | Rebuild-invocation records showing the upstream one-command interface used and no local rebuild present, plus a limitation-bearing fixture rebuild whose run result carries the limitations and states the "in full" reading as unresolved, and evidence that presence-tier loss is not classified as a block |
| OUT-001 | SOW-055 OBJ-005 | REQ-009, CLM-009, AX-003 | AC-009 | VER-009 | Execution records binding each presented release candidate to the run that evaluated it, with no result reuse and no reachable completion state, and a scratch-caller invocation of the binding interface against an unevaluated candidate showing the missing evaluation reported |
| OUT-002 | SOW-055 OBJ-005 | REQ-010, CLM-012, CON-002 | AC-010 | VER-010 | The wiring's recorded binding naming its release path, per-candidate invocation records from a scratch candidate sequence, an unarmed report from a scratch state with no release path naming what it awaits, and disable/remove/bypass transcripts each producing a reported failure |
| OUT-002 | SOW-055 OBJ-005 | REQ-011, CON-001 | AC-011 | VER-011 | Blocking-verdict demonstrations for a candidate on which a governed workflow blocks with the store deleted and for a candidate against which the kill test was withheld |
| OUT-001 | SOW-055 OBJ-005 | REQ-012, REQ-014, CLM-007, CLM-008, CLM-013, AX-004, AX-006 | AC-012 | VER-012 | Inspection records showing no store-semantic, rebuild, rebuild-bound, or governed-workflow definition present; an artifact inventory matching the register's two classes and their declared components; a declared-input review confirming the upstream contracts are cited as obligations without extension and no sibling obligation asserted; and a test review finding no criterion absent from this contract |
| OUT-002 | SOW-055 OBJ-005 | CLM-006, CLM-009, CON-001, AX-001, AX-003 | AC-013 | HUMAN_REVIEW: accountable owner confirmation or declination of what a blocking verdict operationally binds — which release process must honour it and with what consequence for a failing or unevaluated candidate — given C-08's "owner confirmation requested" note and D-PEC-62 §1(4)'s acceptance of the standing-node set as a recorded-but-unresolved non-gating annotation, alongside SOW-055 and PEC-SVC-004's own statement that the kill test is a standing release gate | Dated owner ruling recorded against this deliverable, stating what a blocking verdict binds and with what consequence, and leaving the contract's standing character intact either way |
