---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-01
package_id: PKG-02
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@189f205ff02df4111b33c20be441ce06e65ada7a
project_scope_refs: [SOW-011]
package_objective_refs: [OBJ-001, OBJ-002]
---

# Scope of Work — DEL-02-01 `_STATUS.md` parser

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-02-01` — "`_STATUS.md`
parser" — in `PKG-02` File-Truth Parsers of the PEC v2 build. It covers project
scope item `SOW-011` in service of package objectives `OBJ-001` and `OBJ-002`.
It brings the deliverable's earlier contract (SHA-256 `5d286ec97f4c…4440`)
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

**Objective warrant.** The attribution of this deliverable to `OBJ-001` and
`OBJ-002` is SCA-002-qualified and *indirect*, not register-direct. It belongs
to the group the SCA-002 package calls the INDIRECT-8 (`DEL-01-01` plus
`DEL-02-01..07`), routed to the Gate 3 owner gate as question Q2. The warrant is
a derivation §3 already carried, which SCA-002 applied rather than superseded.
The Gate 3 packet states it this way:

> ### The INDIRECT-8 (`DEL-01-01` + `DEL-02-01..07`) — Q2
>
> §3's mapping notes state a positive derivation: *"parser items (SOW-011..017)
> underlie OBJ-001/OBJ-002 through the record tier (SOW-001)."*
>
> **Recommended — AFFIRM** `[OBJ-001, OBJ-002]` for all eight: it applies the
> accepted §3 rationale rather than superseding it.

Two narrower variants were defined precisely and neither was adopted: **N1**
(the seven parser items map to `OBJ-001`; `SOW-001` keeps both) and **N2** (all
eight map to `OBJ-001`, deleting the `OBJ-002` §3 edit entirely). This
deliverable is one of the seven whose objective set **would** have narrowed
under N1 — unlike `SOW-001`, which keeps both objectives under N1. The packet
also records, verbatim, the evidence for narrowing:

> **Evidence for narrowing, stated because it is real:** OBJ-002's register locus
> is the reconciler layer — `SOW-018` (incremental, Git-delta-keyed), `SOW-019`
> (drift classification), `SOW-006` (SHA stamping). The parsers produce facts the
> SHA comparison operates over; they do not perform it. N1 would arguably
> describe the system more precisely than the §3 sentence does.

The same tension is recorded as decision `D-17` of the SCA-002
`Decision_Log.md`. Its two cells, quoted separately and identified by column —
Decision: *"INDIRECT-8 recommended at the full `[OBJ-001, OBJ-002]` set, **with
the narrower alternative stated and evidenced**"*; Rationale: *"§3's derivation
is explicit about the set, and applying it is faithful to accepted rationale.
But my own measurement shows OBJ-002's register locus is the reconciler layer
(`SOW-006/018/019`), which genuinely supports a parsers-are-`OBJ-001`-only
reading. The owner should choose knowingly rather than inherit my preference."*
Both cells are quoted without elision, including the Rationale's pro-AFFIRM
opening clause.

The owner ruled the question at the SCA-002 Gate 3 in-session gate (2026-07-25,
recorded under the heading "Gate 3 owner ruling — APPROVED 2026-07-25", "Owner
(Ryan Tufts) in-session; relayed by Agent 0"). The ruling row's cells, by
column — Q: *"Q2"*; Question: *"INDIRECT-8 breadth"*; Ruling: *"**AFFIRM**
`OBJ-001;OBJ-002` for all eight (not N1, not N2)"*. The same record adds that
"the Part 0 contingency does not fire" and that "The Gate 3 text is the **only**
text Gate 5 may apply".

Two consequences bound how this contract may state the warrant. First, unlike
the nine per-row attributions batched into Q1/Q5, the Q2 group carries **no
confidence label** in the packet; this contract therefore asserts none and
states the warrant no more strongly than the record does. Second, the question
is **ruled, not pending**: it is not an open rated recommendation awaiting
confirmation, so this contract mints no owner-confirmation acceptance criterion
for it and supplies no fresh derivation of it. The `OBJ-002` leg rests on the §3
derivation through the record tier, not on any claim that this deliverable
performs SHA comparison — it does not (AX-002).

- **CLM-001** — The accepted `ScopeLedger.csv` row for `SOW-011` reads in full, including its trailing fields (columns `ScopeItemID,InOutStatus,ScopeItemStatement,SourceRef,PackageID,DeliverableIDs,ObjectiveIDs,DecisionRef,OpenIssue,Notes`):

> ``SOW-011,IN,Parse `_STATUS.md` files under a declared parser dialect,PEC-RCN-002,PKG-02,DEL-02-01,OBJ-001;OBJ-002,,FALSE,Feed split per DL-4``
>
> (`DecisionRef` empty, `OpenIssue` `FALSE`, `Notes` "Feed split per DL-4".)

- **CLM-002** — The ledger `SourceRef` resolves to PRD `PEC-RCN-002` (§9.2), whose text is:

> The reconciler shall ingest, per the closed, PEC-versioned feed profile
> declared on each loop-registry row (§16.3; PEC's reading hypothesis, never
> the loop's truth), at minimum: `_STATUS.md` (declared parser dialect);
> decision registers and packets (row identity and status only); receipts —
> `LOOP_RECEIPTS.md` ledgers (per-loop grammar; the `receipt-contract-v2`
> marker where a ledger carries it; live or declared historical per profile)
> and central `execution/_Coordination/AgentRuns/<RunID>/RECEIPT.md`; run
> evidence — deliverable `MEMORY.md` run-index entries as RunRecord join
> evidence, with `STATUS.json` / `RUNTIME_SUMMARY.json` as declared historical
> grammar or current evidence per profile; dependency registers
> (`Dependencies.csv`; `WORK_GRAPH.json` as declared historical grammar); work
> graphs `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md`
> (content-minimal; integration ref by default, local branch refs opt-in and
> labelled unintegrated; cited PR numbers resolved to local merge commits by
> read-only plumbing, reported when unresolved locally, never guessed); and
> `LOOP_INIT.md` loop identity, entrypoint and procedure SHA only (workplans as
> declared historical grammar). Per-project `_harness/adapter.yaml` is a
> parity-peer input only, read to compare PEC's declared census population with
> the harness `status_glob` (divergence is a DriftFinding); it is not the feed
> manifest.

  The clause governing this deliverable is "`_STATUS.md` (declared parser dialect)". The parenthetical is singular and is the only feed in that enumeration described as a *dialect*; `LOOP_RECEIPTS.md` ledgers are described instead as "per-loop grammar", and that feed is `DEL-02-03`'s. The requirement's opening makes ingestion follow "the closed, PEC-versioned feed profile declared on each loop-registry row" (CLM-014), and its closing sentence makes `_harness/adapter.yaml` "a parity-peer input only" that "is not the feed manifest".
- **CLM-003** — The objective statements this deliverable serves are `OBJ-001` "Orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation" (`SOFTWARE_DECOMP.md` §3, `SourceRef` §3.1; `projects/pec/docs/PRD.md` §3 outcome 1) and `OBJ-002` "Staleness is detected structurally by SHA comparison, never by judgment" (§3, `SourceRef` §3.2; PRD §3 outcome 2). At revision 1.6 the mapped scope items of `OBJ-001` are "SOW-001, SOW-003..009, SOW-011..017, SOW-038, SOW-040..044, SOW-089, SOW-095..099; instruments: SOW-058, SOW-059, SOW-063, SOW-100" and of `OBJ-002` are "SOW-001, SOW-006, SOW-011..019, SOW-095..097; supported by SOW-005". Both attributions reach this deliverable indirectly through the record tier, per the warrant above.

## Deliverable Definition — Ontology

`DEL-02-01` is typed `BACKEND_FEATURE_SLICE` at Context Envelope `M` with
`PhaseHint` `P1`, `ResponsibleParty` `TBD`, `CoversScopeItems` `SOW-011`, and
`SupportsObjectives` `OBJ-001;OBJ-002`. Its `Description` of record is
"Declared-dialect parser for `_STATUS.md` lifecycle files." and its
`AnticipatedArtifacts` cell is "Parser + fixture tests"; its
`ContextEnvelopeNotes` cell is empty, so there are no envelope notes to carry
forward. Sources: `execution/_Decomposition/Deliverables.csv` row `DEL-02-01`
and `SOFTWARE_DECOMP.md` §5 PKG-02 table ("| DEL-02-01 | `_STATUS.md` parser |
BACKEND_FEATURE_SLICE | M | P1 | SOW-011 |"). The outputs below are that
artifact list and nothing beyond it.

- **OUT-001** — A `_STATUS.md` parser in the PEC service core: it reads governed deliverable lifecycle files under one declared dialect and emits the record-tier entities of CLM-007, with citation provenance and explicit limitation reporting.
- **OUT-002** — A fixture test suite covering the parser against conforming, non-conforming, absent, unreadable, and ambiguous lifecycle-file fixtures, implementing the verification methods declared in this contract.

### Identity in the work domain

- **CLM-004** — The seven-way split of `PEC-RCN-002` into `SOW-011..017` is decision-log entry `DL-4` (2026-07-24): "PEC-RCN-002's enumerated feed list is split into seven scope items (SOW-011..017), one per feed kind", because "Each feed is a separately testable parser with its own grammar; a single "ingest everything" item is not atomic". `SOW-011` is the `_STATUS.md` member of that split. `DL-20` extended the split with `SOW-095` and `SOW-096` and "makes `adapter.yaml` a parity-peer input". The other feeds belong to `DEL-02-02` (decision registers and packets), `DEL-02-03` (receipts: ledgers and central `RECEIPT.md`), `DEL-02-04` (run-evidence JSON), `DEL-02-05` (dependency registers), `DEL-02-06` (`LOOP_INIT.md` identity and workplans), `DEL-02-08` (work graphs) and `DEL-02-09` (the `MEMORY.md` run index). `DEL-02-07` is no longer the feed manifest: `SOW-017` reads `_harness/adapter.yaml` "as a parity-peer input only, comparing PEC's declared census population with the harness `status_glob`", and its `Notes` cell records that "per-loop feed profiles in the PEC-owned registry declare the feeds (SOW-077, SOW-094)". This contract defines a grammar for no feed but its own.
- **CLM-005** — The `PKG-02` package charter (`SOFTWARE_DECOMP.md` §4) is "Read-side grammars over governed files: `_STATUS.md` dialect, decision registers/packets, receipts (ledgers and central `RECEIPT.md`), Markdown work graphs, the MEMORY run index and `LOOP_INIT.md` identity as first-class feeds; run-evidence JSON, workplans and App/Piping ledgers as declared historical grammars; dependency registers; `adapter.yaml` as a parity-peer input", with assignment "SOW-011..017, 095, 096 (9)" and exclusions "Writing anything; interpretation beyond declared grammars". `ContextBudgetQA.csv` rates this deliverable `LOW` risk with `RecommendedAction` "None; single cohesive slice" and an empty `Notes` cell — in contrast to sibling `DEL-02-03`, whose `L` envelope is recorded as "L because grammar varies" across its ledger families and the central-receipt grammar.

### Placement in the work graph

- **CLM-006** — This deliverable has exactly one `EXECUTION` upstream edge, `[E-P03]`, held as `Dependencies.csv` (v3.1) row `DEP-02-01-003`. Attributing each quoted string to its actual column: `TargetDeliverableID` `DEL-01-01`, `TargetName` "Record-tier schema & entity model", `TargetPackageID` `PKG-01`, `DependencyType` `PREREQUISITE`, `TargetType` `DELIVERABLE`, `Statement` "Parser emits record-tier entities defined by the entity model", `EvidenceFile` `execution/PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model/ScopeOfWork.md`, `SourceRef` "§Deliverable Definition — Ontology / Boundaries, claim CLM-012", `EvidenceQuote` "The acts that consume this model are owned by other deliverables and are cited here, never discharged: parsing the file feeds that populate these entities is `DEL-02-01` through `DEL-02-07` (`SOW-011`..`SOW-017`)" (text of `DEL-01-01/CLM-012`; ID-shaped text inside these quoted cells is upstream source context), `Explicitness` `IMPLICIT`, `RequiredMaturity` `INITIALIZED`, `ProposedMaturity` `TBD`, `SatisfactionStatus` `PENDING`, `Confidence` `MEDIUM`, `Origin` `EXTRACTED`, `Status` `ACTIVE`, `Notes` "PROPOSAL; Flag=none; EdgeID=E-P03". At this contract's authoring (`3e5291138`) the row's `EvidenceFile` was `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md`; its evidence cells took their present values in commit `1c50d4da6` (`D-PEC-65` register evidence repair). The register's remaining two rows are `ANCHOR` rows: `DEP-02-01-001` (package-local to `PKG-02`) and `DEP-02-01-002` (the `SOW-011` requirement trace). No row links this deliverable to `DEL-01-06` (CON-006).
- **CLM-007** — `DEL-01-01` is at lifecycle state `INITIALIZED`, which is the maturity `[E-P03]` requires. `INITIALIZED` means the upstream **contract** is the reliable input: `DEL-01-01`'s `ScopeOfWork.md` exists, rebuilt under `D-PEC-100` (act merge `125cfacc1`), and no schema, entity model, or code does: no file under `projects/pec/v2/src/` names the Package or Deliverable type. Nothing in this contract asserts that any upstream artifact has been built. Within the sixteen record-tier entity types that contract obliges (`DEL-01-01/REQ-001`), exactly two are sourced from this deliverable's feed: **Package** and **Deliverable**. The identification is register-grounded, not inferred from the edge note, which is generic: PRD §7.1 gives the Package / Deliverable row the purpose "Lifecycle census from `_STATUS.md` (OPEN→ISSUED), stuck-age; remaining items is a per-loop optional field, read only where the loop's feed profile declares it", and it is the only §7.1 row naming `_STATUS.md`. The sibling edges make the same one-feed-to-its-entities reading explicit — `[E-P04]` "Parser emits DecisionRow entities", `[E-P05]` "Parser emits Receipt entities", `[E-P06]` "Parser emits RunRecord entities", `[E-P07]` "Parser emits DependencyEdge entities", `[E-P08]` "Parser emits Workplan/Step/Gate entities". The upstream obligations this deliverable's output typing binds to are:

> - **REQ-002** — The three compound §7.1 rows shall be decomposed exactly as
>   the register records, each type carrying its row's purpose (CLM-006): ...
>   (b) Package / Deliverable as two distinct types carrying the lifecycle
>   census from `_STATUS.md` (`OPEN`→`ISSUED`) and stuck-age, requiring no
>   remaining-items value for any deliverable (CON-004); ...
> - **REQ-003** — Every record-tier entity type shall carry provenance sufficient
>   for a per-claim citation to its live source — file path, anchor, and/or SHA,
>   per `PEC-ORI-004` — because §7.1 defines the tier as "citable with sources".
>   ...
> - **REQ-005** — Every record-tier entity shall be fully regenerable from file
>   sources. No record-tier field may hold state that cannot be reproduced by
>   rebuilding from the same sources, per `PEC-K-02` ("The record tier is
>   regenerated from sources by one command") and `PEC-RCN-001`. ...
> - **REQ-007** — No field of any type shall admit file content or diff content
>   (`PEC-K-10`: "Paths, counts, SHAs, states, hashes — never file or diff
>   content"). ...
>
> (`DEL-01-01/ScopeOfWork.md`, Epistemology section, as it reads at
> `125cfacc1` after the `D-PEC-100` rebuild; the quotations are elided at the
> ellipses — `REQ-002` before and after its clause (b), and `REQ-003`,
> `REQ-005` and `REQ-007` at their closing sentences. ID-shaped text inside
> this quotation is upstream source context, not a local definition or
> reference: this contract's own `REQ-002`, `REQ-003`, `REQ-005`, and
> `REQ-007` are separate and differently worded, and the quoted `CLM-006` and
> `CON-004` are `DEL-01-01`'s.)

  The same contract types every lifecycle value outside `OPEN`→`ISSUED`, such as `RETIRED`, as its own kind and forbids coercing it into a lifecycle state (`DEL-01-01/REQ-017`), and leaves open whether the Deliverable type carries an optional remaining-items field at all (`DEL-01-01/CON-004`); CON-002 and CON-005 record how this contract meets each.

- **CLM-008** — Two downstream consumers are recorded. `DEL-03-01` "Full-rebuild reconciler (one command)" consumes this deliverable via `[E-P19]`, whose exhibit row (columns `EdgeID,PredecessorID,SuccessorID,Stratum,EdgeKind,Flag,BasisCitation,Rationale`) records `BasisCitation` "PEC-RCN-002 feed list (DL-4)" and `Rationale` "Full rebuild ingests the _STATUS.md feed"; `_DEPENDENCIES.md` carries it as `CONSUMES`, informational. `DEL-10-13` "Reliance-advertisement gate" tests it via `[E-P92]`, held in that deliverable's register as `DEP-10-13-007` with `Statement` "The reliance-advertisement gate composes the DEL-02-01 parser fixture suite" and `Notes` "PROPOSAL; Flag=none; EdgeID=E-P92; seeded under D-PEC-101 (SCA-006 B2)" (the `D-PEC-101` act merge `ce934ac33` is an ancestor of `125cfacc1`); `_DEPENDENCIES.md` carries it as `TESTS`, informational. Each edge lives in its consumer's register, imposes no obligation on this deliverable beyond the outputs declared above, and grants this contract no authority over the reconciler or the gate.
- **CLM-009** — Phase staging, checked against the `PhaseHint` column of `Deliverables.csv` for every deliverable this contract names in its own voice: `P1` — this deliverable, `DEL-01-01`, `DEL-02-02`..`DEL-02-09`, `DEL-03-01`, `DEL-03-02`, `DEL-03-03`, `DEL-04-03`, `DEL-04-05`, `DEL-01-03`, `DEL-01-05`, `DEL-01-06`, `DEL-10-02`, `DEL-10-03`, `DEL-10-13`; `P2` — `DEL-09-02` and `DEL-09-07`, the two dashboard deliverables named in CON-001. No claim in this contract stages any of them into a different phase, and no consumer named here precedes this deliverable's phase.
- **CLM-010** — The deliverable is at lifecycle state `INITIALIZED` with no implementation present: no file under `projects/pec/v2/src/` mentions `_STATUS`. Its `_STATUS.md` History records the 2026-09-26 retirement of its `## Remaining` section under `D-PEC-99` with no lifecycle change. Every requirement, acceptance criterion, and verification method below states a contract on future production; none asserts that anything has been built.

### Boundaries

- **CLM-011** — The acts that consume these entities are owned by other deliverables and are cited here, never discharged: the one-command full rebuild that ingests this feed is `DEL-03-01` (`SOW-010`, `SOW-021`); incremental Git-delta reconciliation is `DEL-03-02` (`SOW-018`) and drift classification `DEL-03-03` (`SOW-019`); SHA/freshness stamping and per-claim citation of an orientation response are `DEL-04-03` (`SOW-006`, `SOW-007`); rendering an unparseable- or stale-feed limitation into a response is `DEL-04-05` (`SOW-009`); the lifecycle census view is `DEL-09-02` (`SOW-046`) and the derived pressure rules including stuck-in-state age are `DEL-09-07` (`SOW-051`); the gitignored store and its ingest-boundary content-minimal guard are `DEL-01-03` (`SOW-056`); standing zero-dependency and locality enforcement is `DEL-01-05` (`SOW-052`, `SOW-053`); the standing kill test is `DEL-10-02` (`SOW-055`) and the no-ruling-write verification `DEL-10-03` (`SOW-025`). Declaring the loops PEC serves and each loop's feed profiles, including the `status-lifecycle` surface a profile selects, is `DEL-01-06` (`SOW-077`, `SOW-094`); reading `_harness/adapter.yaml` as a parity-peer input and comparing PEC's declared census population with the harness `status_glob` is `DEL-02-07` (`SOW-017`); typing the record-tier entities, including lifecycle values outside `OPEN`→`ISSUED`, is `DEL-01-01` (`SOW-001`); and composing the reliance-advertisement gate over, among other evidence, the `PKG-02` parser fixture suites is `DEL-10-13` (`SOW-100`). This contract produces only the parser and its fixture tests.
- **CLM-012** — Observed corpus governance, recorded as the condition the parser meets rather than as scope this contract owns: `docs/CONTRACT.md` `K-STATUS-1` states "`_STATUS.md` is the **canonical, human-readable lifecycle state file** for each deliverable. No other file determines deliverable state.", and the transition rules live in `docs/SPEC.md` §3.3, whose ladder is `→ OPEN`, `OPEN → INITIALIZED`, `INITIALIZED → SEMANTIC_READY`, `INITIALIZED → IN_PROGRESS`, `SEMANTIC_READY → IN_PROGRESS`, `IN_PROGRESS → CHECKING`, `CHECKING → ISSUED`, `CHECKING → IN_PROGRESS`, and `ISSUED → IN_PROGRESS`. PRD §7.1's "(OPEN→ISSUED)" names the ends of that ladder, not a two-state vocabulary. These are repo-root governance documents; they are neither PEC scope authority nor a PEC-accepted specification of the dialect, and this contract cites them as the corpus condition only.
- **CLM-013** — Observed corpus condition, recorded as observation and not as specification. At `125cfacc1` the registry lists one loop, `pec` (CLM-014). Its tree holds 68 deliverable lifecycle files at `projects/pec/execution/PKG-*/1_Working/*/_STATUS.md`; each carries a bold `Current State` line and a `## History` section, and none carries a `## Remaining` section, which PEC retired under `D-PEC-99`. The state tokens are `OPEN` (30), `INITIALIZED` (28), `CHECKING` (4), `RETIRED` (4) and `IN_PROGRESS` (2). `SEMANTIC_READY` and `ISSUED` appear in the ladder of CLM-012 but in no PEC file — absence of an instance is not absence from the vocabulary — and `RETIRED`, which four files carry, is not on that ladder (CON-005). Name-matching alone still over-selects: 726 tracked files are named `_STATUS.md` at that commit, and 658 of them lie outside PEC's deliverable folders. At its authoring (commit `3e5291138`, 2026-07-25) this contract recorded a wider corpus in its checkout — 1,289 files named `_STATUS.md`, 234 of them in deliverable directories across the `pec`, `chirality-piping` and `chirality-app-dev` loops and root `execution/` — a dated observation that is kept as history and not re-verified here. This is the corpus the parser will meet; it is not a contract, and the dialect this deliverable declares is a production choice bounded by TBD-002 and TBD-003.

### Discovery, registry and currency

- **CLM-014** — Discovery follows the loop's declared feed profile (CLM-002). At `125cfacc1` the registry act ruled under `D-PEC-96` is applied (merge commit `73ed349ed`, an ancestor of `125cfacc1`): `v2/config/loops.json` (SHA-256 `fd342b4f29ed…53d7`) carries `"schema_version": 2` and lists one loop, `pec`, whose row declares `shared-dev-loop` version 1 `live` (basis the `D-PEC-94` record) and `loop-receipts-ledger` and `agentruns-json` version 1 `historical`. `v2/config/loops.schema.json` (SHA-256 `104ed64820b7…b143`) describes `shared-dev-loop` as covering, among its surfaces, "_STATUS.md lifecycle", and lists them as "central-receipts, decision-registers, dependency-registers, memory-run-index, status-lifecycle, work-graphs". The `DEL-01-06` contract, rebuilt under `D-PEC-100`, obliges that closed vocabulary and says "Path conventions and grammars for each profile stay with the parsers" (`DEL-01-06/REQ-010`), so the location and admission choices of TBD-004 are this deliverable's. The same requirement states "No profile or surface shall cover `## Remaining` sections", and under `D-PEC-99` `projects/pec/AGENTS.md` states "No PEC feed profile reads such sections, so the coordination plane does not scan them, and they are not a work-selection surface." PRD §7.1 reads remaining items only "where the loop's feed profile declares it" (CLM-007), and no profile of this vocabulary declares it. The `DEL-02-07` contract names this contract's explicit admission rule as the nearest source for "PEC's declared census population", which its comparison needs, and leaves open which deliverable supplies that population (`DEL-02-07/CON-003`; CON-004).
- **CLM-015** — SCA-005 `Propagation_Plan.md` §B4 (accepted at SCA-005 checkpoint group 2) classes the earlier contract `STALE_REVIEW_REQUIRED`, with the cause "per-loop optional 'remaining items'; PEC-RCN-002 quotation; guard STATE note (RETIRED)", and marks both housekeeping corrections for it: the `@3623b958b` basis pin and the false revision-1.1 `_REFERENCES.md` claim. The same section records a carry-forward for the parser contracts:

> Carry-forward for the parser SOWs (DEL-02-01, DEL-02-08, DEL-02-09): the
> DEL-01-03 content-minimal guard admits only `OPEN`..`ISSUED` as STATE values
> (true before and after D-PEC-87/89/91), so `RETIRED`, graph node states and
> run tokens are CON-001 cases those SOWs must address.

  ID-shaped text inside this quotation is upstream source context, not a local definition or reference; the constraint it cites is `DEL-01-03/CON-001`. The produced but unaccepted guard source (`v2/src/pec_v2/core/content_minimal_guard.py`, SHA-256 `740a4a741221…19ee9`; `DEL-01-03` is `IN_PROGRESS`) defines its known states as `OPEN`, `INITIALIZED`, `SEMANTIC_READY`, `IN_PROGRESS`, `CHECKING` and `ISSUED`, so a `RETIRED` token this parser reads lies outside the guard's admitted states (CON-005).

- **TBD-001** — `ResponsibleParty` is unassigned; the register records `TBD`, with assignment at WORKING_ITEMS activation, not in this contract (`SOFTWARE_DECOMP.md` §5 preamble; `_CONTEXT.md`).
- **TBD-002** — The content of the declared dialect — which constructs the parser recognizes, how it locates the state token, the date and history grammar, and its validation rules — is fixed by no accepted PEC source. `PEC-RCN-002` requires the dialect to be *declared*; it does not state it. The dialect is chosen during production within REQ-001 and the `PKG-02` exclusion "interpretation beyond declared grammars" (CLM-005).
- **TBD-003** — The state vocabulary the dialect recognizes, and its treatment of a token outside that vocabulary, are undetermined. PRD §7.1 names only the ladder ends; the fuller ladder of CLM-012 is repo-root governance rather than a PEC-accepted specification, two of its states appear in no PEC file, and `RETIRED`, which is not on it, appears in four (CLM-013, CON-005). REQ-004 constrains the treatment of an unrecognized token without fixing the vocabulary.
- **TBD-004** — The rule by which a file is admitted as a governed lifecycle file — as against a fixture or evidence copy of one, or a file outside the loop's declared `status-lifecycle` surface (CLM-013) — is fixed by no accepted source. Which loops are read, and under which profile, follows the `DEL-01-06` registry declarations (CLM-014); the path conventions for the surface stay with this parser (`DEL-01-06/REQ-010`), so the rule is chosen by this deliverable during production, within REQ-002. What REQ-002 requires is that this parser's own admission rule be declared rather than implicit.

- **CON-001** — The ownership of stuck-age is unresolved at the level of accepted truth. PRD §7.1 places "stuck-age" inside the purpose of the Package / Deliverable entity that this feed populates, and the upstream contract carries that phrase forward (CLM-007). But `PEC-DSH-007` assigns "Derived pressure/status rules (stuck-in-state age, gate-blocked, drift density, staleness, collision risk)" to `SOW-051`, covered by `DEL-09-07` at `PhaseHint` `P2`, and `PEC-DSH-002` assigns the census "with stuck-age and workflow-completeness views" to `SOW-046`, covered by `DEL-09-02`. No accepted source states whether the parser computes an age or exposes the dated history an age is computed from. This contract takes the narrow reading — REQ-006 obliges exposure and forbids computation — because the broad reading would absorb another deliverable's covered scope item. It records the question rather than settling it; a resolution belongs to a ruling, not to a production choice made here.
- **CON-002** — The representability of remaining items is unsettled at the level of accepted truth. PRD §7.1 keeps "remaining items" in the same entity purpose only as "a per-loop optional field, read only where the loop's feed profile declares it", and no profile of the ruled vocabulary declares such a field or surface (CLM-014); PEC's own lifecycle files carry no `## Remaining` section (CLM-013). `PEC-K-10` states "Paths, counts, SHAs, states, hashes — never file or diff content", and §7.1's own DecisionRow row applies that rule to authored register prose in terms — "never the row's prose; PEC-K-10". Whether the Deliverable type carries an optional remaining-items field at all, and in what content-minimal form, is `DEL-01-01/CON-004`, which that contract leaves to a scope change or an owner ruling; this contract cross-references it and does not resolve it. It takes content-minimal as binding — REQ-007 reads no remaining-items section and emits no remaining-items value while no profile declares the field, and admits no authored statement text — and records the question. Enforcement at the ingest boundary is `DEL-01-03`'s guard under `SOW-056`; this contract binds only what this parser emits.
- **CON-003** — `SOW-011` and `PEC-RCN-002` describe a single declared dialect, while the corpus spans loops whose files were authored under different loop conventions (CLM-013 records the wider corpus this contract observed at its authoring; the registry lists only `pec` at `125cfacc1`, and a later row may declare another loop). `PEC-RCN-002` reserves the per-loop-grammar treatment for `LOOP_RECEIPTS.md` ledgers, and `ContextBudgetQA.csv` records the `L` envelope of `DEL-02-03` as arising from grammar variance while rating this deliverable `LOW` at "single cohesive slice" (CLM-005). This contract therefore declares one dialect and treats a non-conforming file as a stated limitation under REQ-008 rather than as a second grammar. If production finds a loop whose lifecycle files cannot be admitted by one declared dialect, that is a scope-change question — the envelope and the `LOW` risk rating rest on the single-dialect reading — and not a production decision.
- **CON-004** — **Source of PEC's declared census population.** `SOW-017` has `DEL-02-07` compare "PEC's declared census population" with the harness `status_glob`, and `DEL-02-07/CON-003` names this contract's explicit admission rule (REQ-002) as the nearest source while recording that no accepted contract states where that population is declared or obtained (CLM-004, CLM-014). Neither `SOW-011` nor this deliverable's register row names a census population, and no accepted source assigns its supply to this deliverable; the lifecycle census dashboard `DEL-09-02` has no `ScopeOfWork.md` at `125cfacc1`. This contract therefore obliges only the declared admission rule of REQ-002 and makes no claim that the files it admits are, or supply, that population, or that it offers an interface to `DEL-02-07`. Which deliverable supplies the population, and through what interface, is recorded here jointly with `DEL-02-07/CON-003` and resolves by scope change or at a later revision of this contract grounded in an accepted source, not by a production choice here.
- **CON-005** — **Lifecycle values outside the guard.** REQ-004 carries the state token as read, and four PEC lifecycle files read `RETIRED` (CLM-013), a value outside both the `OPEN`→`ISSUED` census that PRD §7.1 states and the produced guard's admitted states (CLM-015). How the store admits such a value is `DEL-01-03/CON-001`; `DEL-01-01/REQ-017` types it as its own kind and forbids coercion, and `DEL-01-01/CON-003` gathers it and leaves open whether `RETIRED` is a census value at all. This contract neither coerces such a token into a lifecycle state, encodes it to pass the guard, nor drops it: until the dialect's vocabulary is fixed (TBD-003) it is carried as read or reported as a limitation under REQ-004 and REQ-008. The admitted form is decided under `DEL-01-03` through its own packets, and a change to the census vocabulary is a scope question; neither is resolved here.
- **CON-006** — **Registry dependency edge.** REQ-002 makes this parser read a loop only through the feed-profile declarations of the registry `DEL-01-06` owns (CLM-014), but no `Dependencies.csv` row links this deliverable to `DEL-01-06` (CLM-006). Whether an execution edge to `DEL-01-06` should be recorded is a dependency-register question for its owning workflow, not resolved here.

## Completion and Reliance Basis — Epistemology

The requirements below state what future production must satisfy. Nothing in
this section asserts that a parser, an entity, or a test exists.

- **REQ-001** — The parser shall read governed `_STATUS.md` lifecycle files under exactly one declared dialect, and shall document that dialect: every construct it recognizes, the meaning it assigns to each, and its validation rules. No undeclared construct shall influence its output, per the `PKG-02` exclusion "interpretation beyond declared grammars" (CLM-005).
- **REQ-002** — The declared dialect shall include an explicit rule for which files it admits as governed lifecycle files, so that admission is a declared act rather than a consequence of file naming (CLM-013, TBD-004). The parser shall read a loop's lifecycle files only where that loop's registry row declares a feed profile selecting the `status-lifecycle` surface (at `125cfacc1`, `shared-dev-loop` version 1, CLM-014), taking that declaration from the registry `DEL-01-06` owns and never from its own inference; where no row declares the surface, or no registry declaration is available, it shall read nothing for that loop and report the absence of a declaration. It shall declare no loop, feed profile or surface itself: that is `DEL-01-06`'s scope under `SOW-077` and `SOW-094`, and `DEL-02-07` supplies no feed manifest (CLM-004, CLM-011). Whether the files this rule admits supply PEC's declared census population is open (CON-004).
- **REQ-003** — The parser shall emit exactly the two record-tier entity types its feed sources — Package and Deliverable — as those types are obliged by the upstream contract quoted in CLM-007, and shall emit no other of the sixteen record-tier types. Defining those types is `DEL-01-01`'s scope under `SOW-001`; this deliverable populates them and defines none.
- **REQ-004** — The parser shall carry the lifecycle state as the source declares it: the state token as read, preserved without normalization that loses the source token, and never inferred from any other file or from Git. A token outside the dialect's recognized vocabulary shall produce an explicit limitation under REQ-008 and never a guess, a default, or a nearest-match substitution. `PEC-K-02` governs: "rulings and lifecycle state remain file-native", and PEC output "is never citable as authority" (AX-003).
- **REQ-005** — Every emitted entity shall carry provenance sufficient for a per-claim citation to its live source — file path, anchor, and/or SHA — per `PEC-ORI-004` and the upstream obligation quoted in CLM-007. Attaching citations to an orientation response is `DEL-04-03`'s act under `SOW-007`; this requirement obliges the parser to emit what that act needs, and no more.
- **REQ-006** — The parser shall expose the dated lifecycle history the source records — the state transitions and their dates, and the last-updated date where the file carries one — so that an age is computable downstream by comparison. It shall compute, classify, or threshold no age itself, and shall emit no field whose value depends on the time of the parse rather than on the source bytes (CON-001).
- **REQ-007** — The parser shall read no remaining-items section and emit no remaining-items value for a loop unless that loop's feed profile declares a remaining-items field, which no profile of the ruled vocabulary does (CLM-014); whether, and in what content-minimal form, such a field would be carried is open (CON-002). It shall never carry authored statement text, per `PEC-K-10` "Paths, counts, SHAs, states, hashes — never file or diff content" and the DecisionRow precedent "never the row's prose". No emitted field shall be capable of holding a `## Remaining` section's prose or any other authored file content.
- **REQ-008** — Where a lifecycle file is absent, unreadable, non-conforming to the declared dialect, or ambiguous under it, the parser shall report that condition explicitly to its caller, naming the file and the fault; a silently omitted, empty, partial, or defaulted entity is prohibited, per `PEC-ORI-006` ("Where a feed is unparseable or stale, the response shall state the measurement limitation explicitly; silent omission is prohibited"). Rendering that limitation into a response is `SOW-009` / `DEL-04-05` scope (CLM-011); this deliverable makes the limitation available to that consumer.
- **REQ-009** — The parser shall create, modify, or delete no source file, including the lifecycle files it reads, per `PEC-RCN-004` ("it shall never modify a source file"), `PEC-RCN-006` ("The reconciler writes only its own store and generated views"), and the `PKG-02` exclusion "Writing anything" (CLM-005).
- **REQ-010** — The parser shall be deterministic over its input bytes: the same file content shall yield the same entities and the same limitations, with no dependence on wall-clock time, environment, locale, or traversal order, so that a difference between two parses is a difference in the sources. This is what makes `OBJ-002`'s structural comparison possible over this feed, and it is the local form of the upstream regenerability obligation quoted in CLM-007.
- **REQ-011** — The parser and its fixtures shall introduce no third-party runtime dependency and no external network egress, per `PEC-SVC-001` ("The service core has zero third-party runtime dependencies (carries ADR-002); workspace-internal runtime contracts packages are permitted") and `PEC-SVC-002`, whose standing enforcement is `DEL-01-05` covering `SOW-052` and `SOW-053`.
- **REQ-012** — The work shall absorb no scope owned elsewhere: no grammar for a sibling feed (`DEL-02-02`..`DEL-02-06`, `DEL-02-08`, `DEL-02-09`), no parity-peer reading of `_harness/adapter.yaml` (`DEL-02-07`), no loop, feed-profile or surface declaration (`DEL-01-06`), no entity-type definition (`DEL-01-01`), no reconciliation, drift classification, or rebuild act (`DEL-03-01`..`DEL-03-03`), no stamping or limitation rendering (`DEL-04-03`, `DEL-04-05`), no census view or pressure rule (`DEL-09-02`, `DEL-09-07`), and no enforcement, standing-test or gate-composition duty (`DEL-01-03`, `DEL-01-05`, `DEL-10-02`, `DEL-10-03`, `DEL-10-13`); each owner is cited in CLM-004 or CLM-011. Production shall write into no other package (`DL-12`: "a deliverable never writes into another package").
- **REQ-013** — Fixture tests shall implement the verification methods declared in this contract; they shall not define scope, requirements, or acceptance criteria.

- **AC-001** — The declared dialect is documented construct by construct; the parser over a conforming fixture yields exactly the entities that fixture declares; and altering a construct the dialect does not declare changes nothing in its output.
- **AC-002** — The file-admission rule is stated in the dialect documentation; a fixture tree containing both governed lifecycle files and fixture copies of lifecycle files is partitioned by that stated rule and by nothing implicit; the parser reads a loop's lifecycle files only where that loop's declared feed profile selects the `status-lifecycle` surface, reads nothing and reports the absent declaration otherwise; and it declares no loop, feed profile or surface of its own.
- **AC-003** — The emitted entity set for a fixture corpus contains only Package and Deliverable entities typed as the upstream contract obliges, with no other record-tier type emitted and no type defined in this deliverable.
- **AC-004** — Every emitted entity carries citation provenance, and for a sample of each type the recorded provenance resolves to a live file source by path, anchor, and/or SHA.
- **AC-005** — The state token in each emitted entity is byte-equal to the token the fixture declares; a fixture carrying a token outside the recognized vocabulary yields an explicit limitation rather than any substituted, defaulted, or inferred state; and no emitted state derives from Git or from any file other than the one cited.
- **AC-006** — The dated transition history and last-updated date are present in the emitted entity wherever the fixture carries them; no emitted field holds a computed age, an age classification, or any value that changes when the same fixture is parsed at a different time.
- **AC-007** — For a fixture carrying a `## Remaining`-style section of authored prose, under a feed profile that declares no remaining-items field, the parser reads nothing from that section and emits no remaining-items value; and a fixture carrying file content, diff hunks, and remaining-item prose cannot be expressed in the emitted payload.
- **AC-008** — For absent, unreadable, dialect-non-conforming, and ambiguous fixtures, the parser returns an explicit limitation naming the file and the fault, and never a silently omitted, empty, partial, or defaulted entity in its place.
- **AC-009** — A parser run over a fixture corpus leaves that corpus byte-identical, and the module contains no write, create, or delete call against any source path.
- **AC-010** — Two runs over identical input bytes, in different environments and traversal orders, produce identical entities and identical limitations.
- **AC-011** — The parser and its fixtures add no third-party runtime dependency and make no network call, leaving the `DEL-01-05` zero-dependency and locality assertion intact.
- **AC-012** — The fixture test suite implements VER-001 through VER-011, executes in the `PKG-02` test run, passes, and introduces no acceptance criterion absent from this contract.
- **AC-013** — The REVIEW gate confirms that no sibling `PKG-02` feed grammar or parity-peer reading, upstream `PKG-01` type definition or loop-registry declaration, `PKG-03` reconciliation act, `PKG-04` serving act, `PKG-09` view or pressure rule, or `PKG-10` standing-test or gate-composition duty has been absorbed, and that CON-001 through CON-006 remain recorded as open questions rather than settled by the delivered implementation.

## Production and Verification Method — Praxeology

Production proceeds in the order declared dialect and admission rule → parser →
limitation reporting → fixtures and tests, because each stage is the acceptance
surface of the next: a dialect that is written down before any file is read can
be checked against the corpus, whereas one recovered afterwards from the code
cannot. The entity typing is taken from the upstream contract quoted in CLM-007
before any field is emitted, so REQ-003 is satisfied by construction rather than
audited afterwards. All work is bounded to this deliverable folder and the
`PKG-02` service source it names; this contract authorizes no register,
decomposition, PRD, or upstream-deliverable edit, and it neither defines nor
reshapes the entity types it populates. Tests implement the verification methods
below and create no scope.

- **VER-001** — Execute the parser over a conforming fixture and assert the emitted entities equal the fixture's declared expectation; then compare the constructs actually consumed, by instrumentation or code inspection, against the dialect documentation, and mutate an undeclared construct to assert output invariance.
- **VER-002** — Run the parser over a fixture tree containing both governed lifecycle files and fixture copies of them, and assert the partition matches the documented admission rule exactly; run it against registry fixtures in which a loop declares the `status-lifecycle` surface, a loop declares no such surface, and no registry declaration is available, asserting that only the first loop is read and that the other two yield a reported absent declaration; and inspect the module for any loop, feed-profile or surface declaration of its own.
- **VER-003** — Inventory the emitted entity types over a fixture corpus and diff them against the two types of CLM-007, asserting that no other record-tier type is emitted and that the module defines no entity type.
- **VER-004** — For a sample instance of each emitted type, resolve the recorded citation provenance to a live file source and assert that path, anchor, and/or SHA are present and locatable.
- **VER-005** — Compare each emitted state token byte-for-byte against its fixture; execute the parser against a fixture carrying an unrecognized state token and assert an explicit limitation with no substituted, defaulted, or inferred state; inspect the module for any read of Git or of a file other than the one cited.
- **VER-006** — Assert that the emitted entity carries the fixture's transition dates and last-updated date; inspect the emitted field inventory for any computed age, age classification, or threshold; and re-run the same fixture with the clock advanced, asserting byte-identical output.
- **VER-007** — Inspect every emitted field's type for capacity to hold authored prose or file content; run the parser over a fixture carrying a `## Remaining`-style section of authored prose under a feed profile that declares no remaining-items field, asserting that nothing from that section is read or emitted; and attempt to express a fixture carrying remaining-item prose, file content, and diff hunks, asserting that it cannot be expressed.
- **VER-008** — Execute the parser against absent, unreadable, dialect-non-conforming, and ambiguous fixtures and assert, per case, an explicit limitation naming the file and the fault, with no entity silently omitted, emptied, partialled, or defaulted.
- **VER-009** — Hash the fixture corpus tree before and after a parser run and assert byte-identity; inspect the module's call graph for write, create, or delete operations against any source path.
- **VER-010** — Run the parser twice over identical input bytes under different environments, locales, and traversal orders, and assert the emitted entities and limitations are identical.
- **VER-011** — Inspect the `PKG-02` dependency manifest and this module's import graph for third-party runtime dependencies and network calls, and re-run the `DEL-01-05` zero-dependency and locality enforcement once that deliverable is available, without discharging it here.
- **VER-012** — Run the `PKG-02` test suite and confirm that each of VER-001 through VER-011 has a corresponding executing automated test and that no test asserts a criterion absent from this contract.

## Governing Values and Decisions — Axiology

- **AX-001** — `OBJ-001` governs: orientation is a sub-second query with per-claim citations. A lifecycle fact this parser emits without provenance is a fact that cannot be cited, and an uncitable fact defeats the objective however fast it is served. Provenance is therefore emitted with the entity (REQ-005), not attached downstream.
- **AX-002** — `OBJ-002` governs indirectly and is stated at that strength. This deliverable produces the facts a SHA comparison operates over; it performs no comparison, exactly as the recorded and unadopted N1 evidence says. What it owes the objective is determinism (REQ-010) and time-independence (REQ-006): a feed whose output varies without its source varying would convert a structural check into a judgment call at the point where the check begins.
- **AX-003** — `PEC-K-02` governs most sharply here, because this deliverable reads the file that *is* lifecycle authority. `CONTRACT.md` `K-STATUS-1` makes `_STATUS.md` canonical and `PEC-K-02` states "rulings and lifecycle state remain file-native" while PEC output "is never citable as authority". A parser that normalized, corrected, or inferred a state would make PEC a second lifecycle authority by accident; REQ-004 forbids it, and `PEC-GAT-004` ("PEC shall provide no write path that records adoption, ruling, or direction") is the same posture on the write side, verified by `DEL-10-03`.
- **AX-004** — `PEC-K-10` content-minimal is a residency posture, not a storage optimization. The strongest available enforcement is inexpressibility, which is why REQ-007 binds the shape of the emitted payload rather than a downstream filter. The ingest-boundary guard is `DEL-01-03`'s; this contract makes sure it has nothing to admit.
- **AX-005** — `PEC-K-01` graceful absence and `PEC-ORI-006` honesty govern together: a file PEC cannot parse is a stated coverage limitation, never a blocked act and never a silent gap. Silence is the failure mode a lifecycle census can least afford, because a missing deliverable and a deliverable that parsed to nothing look identical downstream.
- **AX-006** — `DL-4` is the decision that makes this deliverable atomic: one feed kind, one separately testable unit, one declared grammar. Absorbing a sibling feed grammar, the entity types it populates, the reconciler that ingests it, or the views that render it would undo that decision and would also invalidate the `LOW`/"single cohesive slice" risk record this envelope rests on (CLM-005).
- **AX-007** — The edges `[E-P03]` (upstream, `DEL-01-01` → `DEL-02-01`) and `[E-P19]` (downstream, `DEL-02-01` → `DEL-03-01`) are `PROPOSAL` stratum and are accepted at that stratum: `D-PEC-62` §1(4) records the owner accepting the DAG candidate "all strata as presented", read in that packet as taking the exhibit's flags as flags. Both edges carry an empty `Flag` column, and none of the annotations that ruling leaves recorded-but-unresolved (`E-A11`, `E-P69`/`E-N02`, `E-N13`/`E-N18`, the `C-02` direction, the `C-08` standing-node set) touches either. Register-wide constraint `C-10` `STRATUM_RULE` ends "strata are provenance not authority"; citation does not convert `PROPOSAL` to `DECLARED`.
- **AX-008** — Edge direction is a constraint on this contract, not a licence. `RequiredMaturity` `INITIALIZED` on `[E-P03]` means the upstream *contract* is the reliable input, not any upstream artifact; this contract is written against that contract's stated obligations (CLM-007) and asserts nothing about upstream implementation state. Downstream, being consumed by `DEL-03-01` or tested by `DEL-10-13` imposes no duty on either deliverable and grants this one no authority over them.
- **AX-009** — `C-04` `PHASE_PRECEDENCE` and `C-10` `STRATUM_RULE` are register-wide non-gating constraints recorded in `_DEPENDENCIES.md`. Blocker output under the `FULL_GRAPH` mode at threshold `INITIALIZED` is advisory visibility only and is never work assignment.
- **AX-010** — Unknowns stay marked. TBD-001 through TBD-004 and CON-001 through CON-006 are recorded rather than resolved by inference. Where an accepted source is silent — on the dialect's content, on the recognized state vocabulary, on stuck-age ownership, on whether a remaining-items field exists at all, on who supplies PEC's declared census population, on how out-of-guard lifecycle values are admitted — this contract states the silence and takes the narrower reading, because the narrower reading is the one that cannot absorb another deliverable's scope.
- **AX-011** — The accepted basis is `SOFTWARE_DECOMP.md` revision 1.6, pinned at the SCA-006 checkpoint-3 acceptance commit `189f205ff02df4111b33c20be441ce06e65ada7a`. Revision 1.2, accepted through SCA-002 under `D-PEC-64`, is this contract's dated authoring basis only, and no deliverable-local pointer file is a competing authority.
- **AX-012** — This contract is lifecycle-neutral. `_STATUS.md` remains the sole lifecycle authority; the deliverable is at `INITIALIZED` at `125cfacc1`, nothing has been built, and bringing this contract current changes no lifecycle state.
- **AX-013** — Currency provenance. This contract is the prior contract (SHA-256 `5d286ec97f4c262be9e106537e3b7527e9756b6dd5bf0f1beb8259e1ca114440`) brought current under the S1 Scope of Work currency packet (provisional `D-PEC-104`), authored under `MODE=INIT` discipline against revision 1.6 and PRD v2.4 (SCA-005 `Propagation_Plan.md` §B4: `STALE_REVIEW_REQUIRED`, CLM-015). What changed: the frontmatter pin and the basis paragraph (revision 1.6, with revision 1.2 kept as the dated authoring basis); an observation commit; the false revision-1.1 `_REFERENCES.md` claim, replaced; re-quotations of `PEC-RCN-002`, the §7.1 Package / Deliverable purpose, the §3 objective mappings, the `PKG-02` charter, the `DEL-02-03` envelope note, the `DEP-02-01-003` evidence cells and the `DL-4` rationale, and a verbatim `PEC-K-02` quotation in AX-003; S2 currency, with CLM-007 quoting the `DEL-01-01` contract as rebuilt under `D-PEC-100` (sixteen types, the new compound-row text) and CLM-004, CLM-011 and REQ-012 naming `DEL-01-06`, `DEL-02-07` as parity-peer reader, `DEL-02-08`, `DEL-02-09` and `DEL-10-13`; stale state claims (lifecycle `INITIALIZED`, the corpus of CLM-013, the second downstream edge in CLM-008, the phase list of CLM-009); and the per-deliverable cause — REQ-002 keeps its explicit declared admission rule while discovery follows the `DEL-01-06` registry's declared feed profiles in place of a `DEL-02-07` feed manifest (the `D-PEC-100` finding), REQ-007, AC-007, VER-007 and CON-002 read no remaining-items section while no profile declares one (`D-PEC-99`; `DEL-01-01/CON-004`), and CON-005 carries the guard STATE note for `RETIRED`. AC-002, VER-002, AC-013, TBD-003, TBD-004, CON-003, AX-008, AX-010, AX-011 and AX-012 follow those changes. No Part B carry-forward applies to this deliverable. No ID is retired; every earlier ID is kept with its meaning. New: CLM-014, CLM-015, CON-004, CON-005, CON-006 and AX-013.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-011 OBJ-001 OBJ-002 | REQ-001, CLM-001, CLM-002, CLM-004, CLM-005, TBD-002, CON-003 | AC-001 | VER-001 | Dialect documentation construct by construct, the conforming fixture, the parser output against its declared expectation, and the undeclared-construct invariance result |
| OUT-001 | SOW-011 OBJ-001 OBJ-002 | REQ-002, CLM-013, CLM-014, TBD-004, CON-004, CON-006 | AC-002 | VER-002 | The stated admission rule and the partition it produces over a mixed fixture tree, the discovery transcripts for a declared loop, an undeclared loop and no available registry declaration, and a module inspection showing no loop, feed-profile or surface declaration of its own |
| OUT-001 | SOW-011 OBJ-001 OBJ-002 | REQ-003, CLM-006, CLM-007 | AC-003 | VER-003 | Emitted entity-type inventory diffed against the two upstream-obliged types, with the module inspection showing no type defined here |
| OUT-001 | SOW-011 OBJ-001 OBJ-002 | REQ-005, CLM-011, AX-001 | AC-004 | VER-004 | Per-type provenance resolution records showing path, anchor, and/or SHA locatable against a live source |
| OUT-001 | SOW-011 OBJ-001 OBJ-002 | REQ-004, CLM-012, CLM-015, TBD-003, CON-005, AX-003 | AC-005 | VER-005 | Byte-level state-token comparisons per fixture, the unrecognized-token limitation transcript, and an inspection record showing no Git or cross-file state derivation |
| OUT-001 | SOW-011 OBJ-001 OBJ-002 | REQ-006, CON-001, AX-002 | AC-006 | VER-006 | The emitted history and last-updated fields against the fixture, the emitted-field inventory showing no age or classification, and the clock-advanced re-run output |
| OUT-001 | SOW-011 OBJ-001 OBJ-002 | REQ-007, CON-002, AX-004 | AC-007 | VER-007 | Field-type inspection record, the transcript showing nothing read or emitted from a `## Remaining`-style fixture section under a profile that declares no remaining-items field, and the rejected prose, file-content, and diff-hunk fixture |
| OUT-001 | SOW-011 OBJ-001 OBJ-002 | REQ-008, AX-005 | AC-008 | VER-008 | Per-case transcripts for absent, unreadable, non-conforming, and ambiguous fixtures, each naming the file and locating the fault |
| OUT-001 | SOW-011 OBJ-001 OBJ-002 | REQ-009, CLM-005 | AC-009 | VER-009 | Before/after fixture-corpus tree hashes and a call-graph inspection record showing no write path against a source file |
| OUT-001 | SOW-011 OBJ-001 OBJ-002 | REQ-010, CLM-003, AX-002 | AC-010 | VER-010 | Paired run outputs across environments, locales, and traversal orders, asserted identical |
| OUT-001 | SOW-011 OBJ-001 OBJ-002 | REQ-011 | AC-011 | VER-011 | Dependency-manifest and import-graph inspection records, plus the DEL-01-05 enforcement result once that deliverable is available |
| OUT-002 | SOW-011 OBJ-001 OBJ-002 | REQ-013, CLM-010 | AC-012 | VER-012 | PKG-02 test-run output mapping each executed test to its declared verification method, with no criterion asserted that this contract does not state |
| OUT-001 | SOW-011 OBJ-001 OBJ-002 | REQ-012, CLM-008, CLM-009, CLM-011, AX-006, AX-007, AX-008, AX-010, AX-013 | AC-013 | HUMAN_REVIEW: REVIEW gate confirms that no sibling PKG-02 feed grammar or parity-peer reading, PKG-01 type definition or loop-registry declaration, PKG-03 reconciliation act, PKG-04 serving act, PKG-09 view or pressure rule, or PKG-10 standing-test or gate-composition duty has been absorbed, and that the six recorded conflicts remain open rather than settled by the implementation | Review record citing the scope-ledger row, the sibling and cross-package deliverable boundaries, and the recorded disposition of CON-001 through CON-006 |
