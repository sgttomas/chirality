---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-06
package_id: PKG-02
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@3623b958b
project_scope_refs: [SOW-016]
package_objective_refs: [OBJ-001, OBJ-002]
---

# Scope of Work — DEL-02-06 Workplan/LOOP_INIT parser

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-02-06` — "Workplan/LOOP_INIT
parser" — in `PKG-02` File-Truth Parsers of the PEC v2 build. It covers project
scope item `SOW-016` in service of package objectives `OBJ-001` and `OBJ-002`.

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.2** (`current_basis`, SCA-002 successor; commit `3623b958b`). The
deliverable-local `_REFERENCES.md` still names "revision 1.1, accepted working
surface"; that phrase is superseded provenance left by a deferred pointer sweep
(SCA-002 `Handoff_State.md` §6, open item `OI-B`), and `_CONTEXT.md`'s own
supersession line records revision 1.1 as "superseded by revision 1.2
(`current_basis`, SCA-002 successor)". This contract cites revision 1.2.

**Objective warrant.** The attribution of this deliverable to `OBJ-001` and
`OBJ-002` is SCA-002-qualified and *indirect*, not register-direct. `SOW-016`
is one of the eight items the SCA-002 Gate 3 package routes as question Q2 and
calls the INDIRECT-8 — `SOW-001` plus the seven parser items `SOW-011..017`.
The warrant is a derivation §3 of the decomposition already carried, which
SCA-002 applied rather than superseded. The Gate 3 record states it this way:

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

Two narrower alternatives were defined precisely and recorded, and neither was
adopted: **N1** (the seven parsers map to `OBJ-001`; `SOW-001` keeps both) and
**N2** (all eight map to `OBJ-001`). The same record states the evidence for
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
(2026-07-25), with those alternatives in front of them, in a table whose cells
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
`AC-014` puts that qualification in front of the REVIEW gate rather than
leaving it buried in the scope-change package.

- **CLM-001** — The accepted `ScopeLedger.csv` row for `SOW-016` reads in full, including its trailing empty fields (columns `ScopeItemID,InOutStatus,ScopeItemStatement,SourceRef,PackageID,DeliverableIDs,ObjectiveIDs,DecisionRef,OpenIssue,Notes`):

> ``SOW-016,IN,Parse workplans and `LOOP_INIT.md` protocol files,PEC-RCN-002,PKG-02,DEL-02-06,OBJ-001;OBJ-002,,FALSE,``
>
> (`DecisionRef` empty; `OpenIssue` `FALSE`; `Notes` empty — no open issue and
> no decision reference rides this scope item, and unlike five of its six
> sibling parser rows (`SOW-011`..`SOW-015`), and like `SOW-017`, it carries no
> note.)

  The `SOFTWARE_DECOMP.md` §2 SSOW row for the same item repeats the statement and likewise leaves its `Notes` column empty: "| SOW-016 | IN | Parse workplans and `LOOP_INIT.md` protocol files | PEC-RCN-002 | |".

- **CLM-002** — The ledger `SourceRef` cell names one locus, `PEC-RCN-002`, and no `PRD.md` §7.1 row. `PEC-RCN-002` is the `PRD.md` §9.2 reconciliation requirement, quoted here as it reads:

> The reconciler shall ingest, at minimum: `_STATUS.md` (declared parser
> dialect), decision registers and packets, `LOOP_RECEIPTS.md` (per-loop
> grammar; the D-APP-57 contract where a ledger has adopted it),
> `WORK_GRAPH.json` / `STATUS.json` / `RUNTIME_SUMMARY.json`, dependency
> registers, workplans/LOOP_INIT, and per-project `_harness/adapter.yaml` as
> the feed manifest.

  The link from this feed to the record tier is supplied not by the ledger `SourceRef` but by the `Deliverables.csv` `Description` field (CLM-004) and by the accepted edge `[E-P08]`, whose `Rationale` cell reads "Parser emits Workplan/Step/Gate entities" (CLM-007). Both name the `PRD.md` §7.1 compound row "Workplan / Step / Gate", whose `Purpose` cell reads "The standing plan's protocol steps and owner gates, with gate state". That sentence is the sole accepted statement of what this parser's output must carry, and its phrase "the standing plan's" is load-bearing (REQ-005, CON-003).

- **CLM-003** — The objective statements this deliverable serves are `OBJ-001` "Orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation" (`SOFTWARE_DECOMP.md` §3, `SourceRef` §3.1; `PRD.md` §3 outcome 1) and `OBJ-002` "Staleness is detected structurally by SHA comparison, never by judgment" (§3, `SourceRef` §3.2; `PRD.md` §3 outcome 2). Both attributions are indirect through the record tier per the warrant above.

## Deliverable Definition — Ontology

`DEL-02-06` is typed `BACKEND_FEATURE_SLICE` at Context Envelope `M` with
`PhaseHint` `P1`. `Deliverables.csv` records its `AnticipatedArtifacts` as
"Parser + fixture tests" and leaves `ContextEnvelopeNotes` empty, so there are
no envelope notes to carry forward and `_CONTEXT.md` records "(none)". The
outputs of this contract are bounded by that artifact naming: exactly the
parser and its fixture tests, and nothing beyond them.

- **OUT-001** — A workplan/LOOP_INIT parser in the PEC service core: it reads workplan files and `LOOP_INIT.md` protocol files in the checkouts it is pointed at, parses them under a declared grammar, and emits Workplan, Step, and Gate entities carrying recorded gate state and citation provenance to their live sources.
- **OUT-002** — A fixture test suite covering the parser against well-formed, malformed, unreadable, absent, and grammar-unrecognized workplan and `LOOP_INIT.md` fixtures, implementing the verification methods declared in this contract.

### Identity of record

- **CLM-004** — `DEL-02-06` is named "Workplan/LOOP_INIT parser", Type `BACKEND_FEATURE_SLICE`, Context Envelope `M`, `PhaseHint` `P1`, `ResponsibleParty` `TBD`, `AnticipatedArtifacts` "Parser + fixture tests", `CoversScopeItems` `SOW-016`, `SupportsObjectives` `OBJ-001;OBJ-002`, `ContextEnvelopeNotes` empty, with the register `Description` field reading "Workplans and `LOOP_INIT.md` into Workplan/Step/Gate entities with gate state." Sources: `Deliverables.csv` row `DEL-02-06` and the `SOFTWARE_DECOMP.md` §5 PKG-02 table row "| DEL-02-06 | Workplan/LOOP_INIT parser | BACKEND_FEATURE_SLICE | M | P1 | SOW-016 |". The `Description` field is the sole register statement of the parser's output target: Workplan, Step, and Gate entities, with gate state.
- **CLM-005** — The seven-way split of `PEC-RCN-002` into `SOW-011..017` is decision-log entry `DL-4` (2026-07-24), whose Decision cell reads "PEC-RCN-002's enumerated feed list is split into seven scope items (SOW-011..017), one per feed kind" and whose Rationale cell reads "Each feed is a separately testable parser with its own grammar; a single \"ingest everything\" item is not atomic". This deliverable is one feed kind: workplans and `LOOP_INIT.md`. The other six feeds belong to `DEL-02-01` through `DEL-02-05` and `DEL-02-07`.
- **CLM-006** — The `PKG-02` package charter (`SOFTWARE_DECOMP.md` §4) is "Read-side grammars over governed files: `_STATUS.md` dialect, decision registers/packets, receipts ledgers, run-evidence JSON, dependency registers, workplans/LOOP_INIT, `adapter.yaml` manifests", covering "SOW-011..017 (7)", with "Writing anything; interpretation beyond declared grammars" recorded as explicitly out of package scope.

### Placement in the work graph

- **CLM-007** — This deliverable has exactly one accepted `EXECUTION` upstream edge, `[E-P08]`, held as `Dependencies.csv` register row `DEP-02-06-003`. Attributed by column: `DependencyClass` `EXECUTION`, `AnchorType` `NOT_APPLICABLE`, `Direction` `UPSTREAM`, `DependencyType` `PREREQUISITE`, `TargetType` `DELIVERABLE`, `TargetPackageID` `PKG-01`, `TargetDeliverableID` and `TargetRefID` `DEL-01-01`, `TargetName` "Record-tier schema & entity model", `TargetLocation` `execution/PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model`, `Statement` "Parser emits Workplan/Step/Gate entities", `EvidenceFile` `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md`, `SourceRef` and `EvidenceQuote` both "§3 mapping notes (as E-P03)", `Explicitness` `IMPLICIT`, `RequiredMaturity` `INITIALIZED`, `ProposedMaturity` `TBD`, `SatisfactionStatus` `PENDING`, `Confidence` `MEDIUM`, `Origin` `EXTRACTED`, `FirstSeen` and `LastSeen` `2026-07-25`, `Status` `ACTIVE`, `Notes` "PROPOSAL; Flag=none; EdgeID=E-P08". The "(as E-P03)" shorthand is a back-reference to the sibling edge whose `BasisCitation` carries the §3 mapping-note text in full; the gate exhibit's own edge-register row for `E-P08` (columns `EdgeID,PredecessorID,SuccessorID,Stratum,EdgeKind,Flag,BasisCitation,Rationale`) reads `E-P08,DEL-01-01,DEL-02-06,PROPOSAL,CONSUMES,,§3 mapping notes (as E-P03),Parser emits Workplan/Step/Gate entities`, with `Flag` empty. The two remaining rows in this deliverable's register are the `ANCHOR` rows `DEP-02-06-001` (package-local to `PKG-02`) and `DEP-02-06-002` (`SOW-016` requirement trace).
- **CLM-008** — `DEL-01-01` is at lifecycle state `INITIALIZED`, which is the maturity `[E-P08]` requires. `INITIALIZED` means its **contract** is the reliable input: `DEL-01-01`'s accepted `ScopeOfWork.md` exists; no schema, no entity model, and no code do. Nothing in this contract asserts that any upstream artifact exists or has been built. The output-typing obligations this parser binds to are that contract's stated obligations, quoted here:

> - **REQ-001** — The schema and entity model shall define exactly the fourteen
>   record-tier entity types named in CLM-005 — Loop, Workplan, Step, Gate,
>   Receipt, DecisionRow, Fence, Package, Deliverable, DependencyEdge,
>   RunRecord, CandidateBrief, OrientationSnapshot, DriftFinding — with none
>   added and none dropped, and each type shall carry a recorded trace to its
>   `PRD.md` §7.1 row and stated purpose (CLM-006).
> - **REQ-002** — The two compound `PRD.md` §7.1 rows shall be decomposed
>   exactly as the register records: Workplan / Step / Gate as three distinct
>   types carrying the standing plan's protocol steps, owner gates, and gate
>   state; Package / Deliverable as two distinct types carrying the lifecycle
>   census (`OPEN`→`ISSUED`), stuck-age, and remaining items.
> - **REQ-003** — Every record-tier entity type shall carry provenance
>   sufficient for a per-claim citation to its live source — file path, anchor,
>   and/or SHA, per `PEC-ORI-004` — because §7.1 defines the tier as "citable
>   with sources". ...
> - **REQ-005** — Every record-tier entity shall be fully regenerable from file
>   sources. No record-tier field may hold state that cannot be reproduced by
>   rebuilding from the same sources, per `PEC-K-02` ...
> - **REQ-007** — No field of any type shall admit file content or diff content
>   (`PEC-K-10`: "Paths, counts, SHAs, states, hashes — never file or diff
>   content"). ...
>
> (`DEL-01-01/ScopeOfWork.md`, Epistemology section; the `REQ-003`, `REQ-005`,
> and `REQ-007` quotations are elided at the ellipses. ID-shaped text inside this
> quotation is upstream source context, not a local definition or reference —
> this contract's own `REQ-*` and `AC-*` records are separate and differently
> worded.)

  The upstream register `Description` for `DEL-01-01` is the second place the compound row is recorded, and it names this parser's three target types explicitly: "Store schema and typed entity model for the record tier: 11 PRD rows, 14 entity types (Workplan/Step/Gate and Package/Deliverable are compound rows) — Loop, Workplan, Step, Gate, Receipt, DecisionRow, Fence, Package, Deliverable, DependencyEdge, RunRecord, CandidateBrief, OrientationSnapshot, DriftFinding." (`Deliverables.csv` row `DEL-01-01`.) Workplan, Step, and Gate are therefore three distinct upstream types, not one; the compound `PRD.md` §7.1 row is their shared source, not their shape.

- **CLM-009** — The one declared downstream consumer is `DEL-03-01` (Full-rebuild reconciler (one command)) via `[E-P24]`, whose gate-exhibit row reads `E-P24,DEL-02-06,DEL-03-01,PROPOSAL,CONSUMES,,PEC-RCN-002 feed list (DL-4),Full rebuild ingests workplans/LOOP_INIT`, with `Flag` empty. That edge is informational here; it lives in the consumer's register and imposes no obligation on this deliverable beyond the outputs declared above.
- **CLM-010** — Phase staging, checked against the `PhaseHint` column of `Deliverables.csv` for every deliverable this contract names in its own voice: `DEL-02-06` itself, its upstream `DEL-01-01`, its sibling parsers `DEL-02-01`, `DEL-02-02`, `DEL-02-03`, `DEL-02-04`, `DEL-02-05`, `DEL-02-07`, and the cited consumers and neighbours `DEL-01-03`, `DEL-01-05`, `DEL-01-06`, `DEL-03-01`, `DEL-03-02`, `DEL-03-03`, `DEL-04-01`, `DEL-04-03`, `DEL-04-05`, `DEL-10-02`, and `DEL-10-03` are all `P1`. Two exceptions are named in this contract's own voice: `DEL-05-01` (Gate precondition evaluators (Explain-shaped)) and `DEL-05-02` (Cross-loop decision slate), both `P2`; each is cited only as the owner of scope this deliverable does not touch. No claim in this contract stages any named deliverable into a different phase.

### Boundaries

- **CLM-011** — The acts adjacent to this parser are owned elsewhere and are cited here, never discharged. The record-tier entity model that types this parser's output — Workplan, Step, and Gate included — is `DEL-01-01` (`SOW-001`). The other six feed grammars are `DEL-02-01` through `DEL-02-05` and `DEL-02-07` (`SOW-011`..`SOW-015`, `SOW-017`); in particular the decision registers and packets from which a `D-*` ruling row's identity and status are read belong to `DEL-02-02` under `SOW-012`, `Dependencies.csv` and `WORK_GRAPH.json` belong to `DEL-02-05` under `SOW-015`, `_STATUS.md` lifecycle census belongs to `DEL-02-01` under `SOW-011`, receipts belong to `DEL-02-03` under `SOW-013`, and the per-project `_harness/adapter.yaml` feed manifest belongs to `DEL-02-07` under `SOW-017`. The registered-loop set and the loop registry are `DEL-01-06` (`SOW-094`). Deterministic evaluation of gate preconditions and the Explain-shaped verdicts they produce are `DEL-05-01` (`SOW-022`, `SOW-023`); the cross-loop decision slate is `DEL-05-02` (`SOW-024`). Full rebuild by one command is `DEL-03-01` (`SOW-010`, `SOW-021`); incremental Git-delta reconcile is `DEL-03-02` (`SOW-018`) and drift classification is `DEL-03-03` (`SOW-019`); examined-SHA and freshness stamping with per-claim citation attachment is `DEL-04-03` (`SOW-006`, `SOW-007`); the per-loop orientation return that surfaces gate states to a caller is `DEL-04-01` (`SOW-004`); rendering a measurement limitation into an orientation response is `DEL-04-05` (`SOW-009`); the gitignored store and its ingest-boundary content-minimal guard are `DEL-01-03` (`SOW-056`); standing zero-dependency and locality enforcement is `DEL-01-05` (`SOW-052`, `SOW-053`); the standing kill test is `DEL-10-02` (`SOW-055`); the tested no-ruling-write property of the API surface is `DEL-10-03` (`SOW-025`). This contract produces only the parser and its fixture tests.
- **CLM-012** — Gate state as this feed carries it is a *parsed fact*, not a *derived verdict*, and the distinction is where this deliverable is most easily over-read. `PEC-GAT-001` gives PEC the act of deterministically evaluating "gate preconditions that reduce to file/Git facts: ruling presence, ruling-SHA commit reachability, receipt ancestry, snapshot/freeze presence, register-row status"; `PEC-GAT-002` requires that "Gate verdicts shall be Explain-shaped (rule, threshold, contributing citations) and advisory only"; `PEC-GAT-004` requires that PEC "shall provide no write path that records adoption, ruling, or direction (PEC-K-02; K-AUTH-1)". `PEC-GAT-001` and `PEC-GAT-002` are `PKG-05` scope, covered by `SOW-022` and `SOW-023` respectively, both assigned to `DEL-05-01` (CLM-011); `SOW-024`, which covers `PEC-GAT-003` at `DEL-05-02`, is the cross-loop decision slate and is not one of the three requirements quoted here. `PEC-GAT-004` is not `PKG-05` scope at all: the ruling write path itself is `SOW-066`, permanent `OUT`, and `SOFTWARE_DECOMP.md` §4 records it as `PKG-05`'s exclusion "Any ruling write path (SOW-066, permanent OUT)"; its verification obligation is `SOW-025`, assigned to `PKG-10` / `DEL-10-03` by `DL-11` ("SOW-025 (no-ruling-write verification) → PKG-10 per DL-8's verification-obligation framing") (CLM-011). This parser transcribes the gate state a source file records and stops there (REQ-004).
- **CLM-013** — `PEC-K-05` requires the two trust tiers never be blurred: "Record tier: reconciled from file truth, per-claim citations. Presence tier: TTL'd, heartbeat-aged, evaporating, honesty-labeled. Presence facts never enter record-tier citations." Workplans and `LOOP_INIT.md` files are committed, authored project truth; nothing this parser reads is presence-tier, and nothing it emits may carry a presence fact.
- **CLM-014** — The deliverable is at lifecycle state `OPEN` with no implementation present. Every requirement, acceptance criterion, and verification method below states a contract on future production; none asserts that anything has been built.
- **CLM-015** — Observed corpus condition, recorded as observation and not as specification. A census of this checkout on 2026-07-25 finds **24** files whose name contains "workplan" and **5** files named `LOOP_INIT.md`. The workplan files distribute as 13 under `projects/`, 7 under `_DomainEngines/`, and 4 under the root loop's `execution/`; of the 24, one is the pointer file `CURRENT_WORKPLAN.md`, three are `WORKPLAN_CANDIDATE_*` files under `AgentRuns/` directories, two sit under a `.archive/` path, and one sits under `_DomainEngines/proposals/`. The five `LOOP_INIT.md` files belong to the root, app-dev, piping, pec, and bridge loops. **None of the 29 files carries YAML frontmatter, a schema declaration, or any machine-readable structure**; all are Markdown instruction prose. Protocol steps appear predominantly as numbered lists (23 of 29 files contain one) rather than as headings (7 of 29 have a step-shaped heading), and the 24 workplan files present **97 distinct** first-, second-, or third-level heading texts. Gate state appears in at least four unrelated notations across the corpus: the inline suffixes `(gated: ...)` and `(stage-gated: ...)` (11 files each), the register-row status token `AWAITING_RULING` (6 files), and free prose such as "GATE SATISFIED" and a "gate-state note" (1 file each). The three PEC-adjacent loops that name a standing-plan selection rule state three different rules: the root loop's `LOOP_INIT.md` selects by the pointer file `CURRENT_WORKPLAN.md` and explicitly forbids selecting "by filesystem modification time, directory order, or the phrase \"newest workplan\" in an older derivative surface"; the app-dev and piping `LOOP_INIT.md` files select "only from committed `HEAD`" by bytewise-sorted enumeration of `^WORKPLAN_.*\.md$` with the worktree copy never selectable; the pec and bridge `LOOP_INIT.md` files select "the newest `WORKPLAN_*.md` in this file's directory". The two existing `_harness/adapter.yaml` manifests (app-dev, piping) declare keys for the plan, coordination surface, decision register, DAG pointer, and status glob, and name **no** workplan or `LOOP_INIT.md` path. The `projects/pec` tree contains zero workplan and zero `LOOP_INIT.md` files; the pec loop's own `LOOP_INIT.md` and workplans live at `_DomainEngines/pec/`. These files are the corpus the parser will meet; they are not a contract, and no accepted PEC source adopts any of their shapes or selection rules.

- **TBD-001** — `ResponsibleParty` is unassigned; the register records `TBD`, with assignment at WORKING_ITEMS activation and not in this contract (`SOFTWARE_DECOMP.md` §5 preamble; `_CONTEXT.md`).
- **TBD-002** — The grammar this parser declares — which prose constructs of a workplan or `LOOP_INIT.md` file constitute a Step, which constitute a Gate, how a gate's recorded state is recognized across the notations of CLM-015, and how a file it does not recognize is treated — is fixed by no accepted source. It is chosen during production within REQ-002 and CLM-006, against the corpus condition of CLM-015.
- **TBD-003** — The field sets of the Workplan, Step, and Gate entities are not enumerated by any accepted source. `PRD.md` §7.1 gives one purpose sentence for the compound row and the upstream contract quoted in CLM-008 obliges the three types to exist as distinct types carrying protocol steps, owner gates, and gate state, without listing their fields. The concrete shapes therefore arrive from `DEL-01-01`'s production; this contract binds the parser to those types rather than defining them (REQ-003, CON-002).
- **TBD-004** — How the parser discovers which files are workplans and `LOOP_INIT.md` protocol files is fixed by no accepted source. `SOW-016` states the feed by name and states no path scope; `PEC-RCN-002` names the feed manifest as `_harness/adapter.yaml`, which is `DEL-02-07`'s deliverable and today declares no workplan or `LOOP_INIT.md` path (CLM-015). Whether discovery is by declared manifest entry, by filename convention, by loop-directory position, or by some combination is a production choice bounded by REQ-002 and CON-004, and it is not settled here.
- **TBD-005** — How a workplan or `LOOP_INIT.md` file binds to the Loop it governs is fixed by no accepted source. `PRD.md` §7.1 defines Loop as "a LOOP_INIT/workplan-governed work loop", which states the relation without stating how it is computed, and the registered-loop set is `DEL-01-06`'s output (CLM-011). Whether the binding is derived from path position, from the registry, or from the feed manifest is not settled here.

## Completion and Reliance Basis — Epistemology

The requirements below state what future production must satisfy. Nothing in
this section asserts that a parser, a fixture, or a test exists.

- **REQ-001** — The parser shall read workplan files and `LOOP_INIT.md` protocol files in the checkouts it is pointed at, and shall emit from them Workplan, Step, and Gate entities carrying recorded gate state, per the `SOW-016` statement (CLM-001), the register `Description` (CLM-004), and the `PRD.md` §7.1 purpose sentence "The standing plan's protocol steps and owner gates, with gate state" (CLM-002).
- **REQ-002** — The parser shall document the grammar it consumes — every prose construct it reads, that construct's semantics, and the mapping from construct to emitted entity — and shall let no undeclared construct influence its output, per the `PKG-02` out-of-scope line "interpretation beyond declared grammars" (CLM-006). Because this feed carries no schema declaration of any kind (CLM-015), the grammar shall additionally state what the parser does with a file whose structure it does not recognize; silent best-effort interpretation of unrecognized prose is prohibited.
- **REQ-003** — The parser's emitted entities shall be typed as the Workplan, Step, and Gate entities of the upstream record-tier entity model quoted in CLM-008, which that contract obliges to be three distinct types. This deliverable shall define no record-tier entity type of its own, shall add no type to that model, and shall not depend on any upstream artifact existing; it depends on the upstream contract only (CON-002).
- **REQ-004** — The parser shall represent gate state exactly as the source file records it, and shall neither evaluate a gate precondition, nor compute or assert a verdict, nor infer that a gate is satisfied, ruled, or discharged from any fact the file does not state. Deterministic gate-precondition evaluation and Explain-shaped verdicts are `DEL-05-01`'s act under `SOW-022` and `SOW-023`, and no write path recording adoption, ruling, or direction may exist anywhere in PEC per `PEC-GAT-004` (CLM-012). Where a file records a gate whose state it does not state, the parser shall represent the state as unstated rather than defaulting it.
- **REQ-005** — The parser shall not represent any workplan as the standing plan of a loop except on a basis it declares and that the source states. A candidate, archived, superseded, or proposal-staged workplan (CLM-015) shall not be emitted as the standing plan, and where the standing plan cannot be identified on the declared basis, the parser shall report that condition under REQ-007 rather than choosing one. The `PRD.md` §7.1 purpose sentence scopes the Workplan entity to "The standing plan's" steps and gates (CLM-002); this requirement keeps that scope honest without settling the selection rule, which is CON-003 and TBD-004.
- **REQ-006** — Every emitted entity shall carry provenance sufficient for a per-claim citation to its live source — file path, anchor, and/or SHA — per `PEC-ORI-004` and the upstream provenance obligation quoted in CLM-008. Attaching citations to an orientation response is `DEL-04-03`'s act under `SOW-007` (CLM-011); this requirement obliges the parser to carry what that act needs, and no more.
- **REQ-007** — Where a workplan or `LOOP_INIT.md` file is absent, unreadable, malformed, or carries a structure the declared grammar does not recognize, the parser shall report that condition explicitly to its caller, naming the file and the fault; a silently dropped, empty, partial, or defaulted entity is prohibited, per `PEC-ORI-006` ("Where a feed is unparseable or stale, the response shall state the measurement limitation explicitly; silent omission is prohibited"). Rendering such a limitation into an orientation response is `SOW-009` / `DEL-04-05` scope (CLM-011); this deliverable makes the limitation available to that consumer.
- **REQ-008** — The parser shall create, modify, or delete no source file, including the workplan and `LOOP_INIT.md` files it reads, per `PEC-RCN-004` ("it shall never modify a source file"), `PEC-RCN-006` ("The reconciler writes only its own store and generated views"), and the `PKG-02` out-of-scope line "Writing anything".
- **REQ-009** — The emitted entities shall be content-minimal: paths, counts, identifiers, states, SHAs, and hashes, never file or diff content, per `PEC-K-10` and the upstream field-shape obligation quoted in CLM-008. This feed is instruction prose end to end (CLM-015); the parser shall carry none of that prose into the record tier, and a Step or Gate entity shall be identity and state, not the text of the step or the gate. Enforcement at the ingest boundary is `DEL-01-03`'s guard under `SOW-056` (CLM-011); this requirement binds what the parser emits so that the guard has nothing to admit.
- **REQ-010** — The parser shall be deterministic over its inputs: the same file set at the same content shall yield the same entities, so that the record tier remains fully regenerable from sources per `PEC-K-02` and the upstream regenerability obligation quoted in CLM-008. The rebuild command itself is `DEL-03-01`'s under `SOW-010` (CLM-011).
- **REQ-011** — The parser and its fixtures shall introduce no third-party runtime dependency and no external network egress, per `PEC-SVC-001` and `PEC-SVC-002`, whose standing enforcement is `DEL-01-05` covering `SOW-052` and `SOW-053`.
- **REQ-012** — The parser shall parse no feed owned by a sibling deliverable and shall perform no act owned by another package. In particular it shall not read `_STATUS.md`, decision registers or packets, `LOOP_RECEIPTS.md`, run-evidence JSON, `Dependencies.csv`, `WORK_GRAPH.json`, or `_harness/adapter.yaml` as a feed of its own; it shall emit no Loop, Receipt, DecisionRow, DependencyEdge, RunRecord, Package, or Deliverable entity; where a workplan's prose names a decision row such as a `(gated: D-XX)` suffix (CLM-015), it shall carry that reference as recorded gate state under REQ-004 and shall not resolve, look up, or emit the referenced DecisionRow, which is `DEL-02-02`'s under `SOW-012`; and it shall perform no reconciliation, drift classification, freshness stamping, citation attachment, gate evaluation, or slate rendering (CLM-011, CLM-012).
- **REQ-013** — Tests shall implement the verification methods declared in this contract; they shall not define scope, requirements, or acceptance criteria.

- **AC-001** — The parser reads a well-formed workplan fixture and a well-formed `LOOP_INIT.md` fixture and yields exactly the Workplan, Step, and Gate entities the fixtures declare, each gate carrying the state its fixture records.
- **AC-002** — Every prose construct the parser reads appears in the documented grammar; altering an undeclared construct in a fixture changes nothing in the output; and a fixture whose structure the grammar does not recognize is handled as the documented grammar states rather than by best-effort interpretation.
- **AC-003** — Every emitted entity is an instance of the upstream Workplan, Step, or Gate type as that contract obliges it; no record-tier entity type is defined in this deliverable's source; and no element of this deliverable asserts or requires that an upstream schema, entity model, or store exists.
- **AC-004** — For a fixture set spanning the gate notations of CLM-015, each emitted Gate carries the state its source records and no state its source does not record; a fixture whose gate has no recorded state yields an unstated state rather than a default; and the module contains no gate-precondition evaluation, verdict computation, or ruling-inference path.
- **AC-005** — No candidate, archived, superseded, or proposal-staged workplan fixture is emitted as a loop's standing plan; the basis on which a standing plan is identified is declared in the grammar documentation; and a fixture tree in which that basis does not resolve produces an explicit limitation rather than a selected plan.
- **AC-006** — Every emitted entity resolves to its live source: for a sample of each fixture kind, the recorded provenance is present and locatable by path, anchor, and/or SHA.
- **AC-007** — For absent, unreadable, malformed, and grammar-unrecognized fixtures, the parser returns an explicit limitation naming the file and the fault, and never a silently dropped, empty, partial, or defaulted entity in its place.
- **AC-008** — A parser run over a fixture corpus leaves that corpus byte-identical, and the module contains no write, create, or delete call against any source path.
- **AC-009** — The entities emitted for a prose-dense fixture contain no file content, no instruction prose, and no step or gate body text; only paths, counts, identifiers, states, SHAs, and hashes appear.
- **AC-010** — Two runs of the parser over the same unchanged fixture corpus produce identical entities, and inspection finds no emitted field whose value a rebuild from the same sources could not reproduce.
- **AC-011** — The parser and its fixtures add no third-party runtime dependency and make no network call, leaving the `DEL-01-05` zero-dependency and locality assertion intact.
- **AC-012** — The parser reads no sibling feed, emits no entity type other than Workplan, Step, and Gate, resolves no decision row referenced by a workplan's gate prose, and performs no reconciliation, drift-classification, stamping, citation-attachment, gate-evaluation, or slate-rendering act owned by `PKG-03`, `PKG-04`, or `PKG-05`.
- **AC-013** — The fixture test suite implements VER-001 through VER-012, executes in the `PKG-02` test run, passes, and introduces no acceptance criterion absent from this contract.
- **AC-014** — The REVIEW gate confirms this contract's traceability to `SOW-016`, `OBJ-001`, and `OBJ-002` as ruled at SCA-002 Gate 3 Q2, confirms that the indirect `OBJ-002` leg is stated no more strongly here than the Gate 3 record states it — including the recorded and unadopted N1 narrowing evidence and the absence of a confidence label on that group — and confirms that no `PKG-01`, sibling `PKG-02`, `PKG-03`, `PKG-04`, or `PKG-05` scope has been absorbed.

- **CON-001** — No accepted source declares a structure for a workplan or a `LOOP_INIT.md` file, and unlike every other `PKG-02` feed this one has no machine-readable shape at all: the measured corpus carries no frontmatter, no schema key, 97 distinct heading texts across 24 workplan files, and at least four unrelated notations for gate state (CLM-015). `PKG-02`'s charter permits a declared grammar and forbids "interpretation beyond declared grammars"; those two facts are in tension for this feed, because a grammar narrow enough to be declarable will not describe most of the corpus, and a grammar wide enough to describe instruction prose is interpretation. This contract records the tension rather than resolving it: REQ-002 requires the grammar to be declared and to state its own behaviour on unrecognized structure, and REQ-007 requires every file the grammar does not cover to surface as an explicit limitation rather than a silent omission. Choosing the grammar's breadth is a production decision bounded by those requirements; extending this deliverable to interpret structures it has not declared would be a scope-change question, not a production decision.
- **CON-002** — The Workplan, Step, and Gate field sets are owned upstream and do not yet exist. `DEL-01-01` is `INITIALIZED`: its contract obliges the three types to be distinct and to carry protocol steps, owner gates, and gate state (CLM-008), but neither it nor any accepted source enumerates their fields (TBD-003). This parser's output typing therefore binds to an obligation, not to an artifact. Nothing in this contract defines, anticipates, or constrains those field sets, and a production choice here that fixed them would take a decision in the wrong place.
- **CON-003** — "The standing plan" is the scope the `PRD.md` §7.1 Workplan purpose sentence states (CLM-002), and no accepted PEC source states how a loop's standing plan is identified. The corpus states three mutually incompatible rules across five loops — pointer file, committed-`HEAD` bytewise-last, and newest-in-directory — and the root loop's rule explicitly forbids the rule two other loops use (CLM-015). Those texts are loop-authored corpus content, not accepted PEC truth, and this contract adopts none of them. REQ-005 binds the parser to declare its basis and to refuse to guess; settling which rule PEC applies, or whether it applies a per-loop rule at all, is a scope-change question for `SOW-016` rather than a production decision.
- **CON-004** — The read scope of this feed is unstated at the level of accepted truth. `SOW-014` bounds its sibling parser to `execution/**` and `SOW-017` bounds its sibling to a per-project path, but `SOW-016` names the feed only as "workplans and `LOOP_INIT.md` protocol files" with no path scope, and `PEC-RCN-002` routes feed discovery through a manifest that today names neither (CLM-015). The gap is recorded, not filled: TBD-004 leaves discovery to production within REQ-002, and REQ-012 forbids reaching into a sibling's feed to close it. A production choice that widened the read scope beyond files the declared basis identifies as this feed would be a scope-change question.
- **CON-005** — The corpus this parser is first expected to meet is not where the deliverable lives. `OI-010`, resolved at Gate 2 (2026-07-24), records that "... the first loop the P1 reconciler ingests is PEC v2's own build (bootstrap as thesis validation) ...", and the `projects/pec` tree contains no workplan and no `LOOP_INIT.md`; the pec loop's own protocol files sit at `_DomainEngines/pec/` (CLM-015). No accepted source states the relation between a registered loop's identity and the directory holding its protocol files — that is TBD-005. This is recorded as a stated condition, not a defect and not a licence to widen the read scope: a loop whose protocol files the declared basis does not locate is a limitation to be stated under REQ-007.

## Production and Verification Method — Praxeology

Production proceeds in the order corpus survey → declared grammar → parser →
gate-state and standing-plan discipline → limitation reporting → fixtures and
tests, because each stage is the acceptance surface of the next and because the
grammar cannot be declared honestly before the corpus condition of CLM-015 has
been examined against the accepted sources. All work is bounded to this
deliverable folder and the `PKG-02` service-core source it names; this contract
authorizes no register, decomposition, PRD, or upstream-deliverable edit, and it
neither defines nor reshapes the record-tier entity model it emits into. Tests
implement the verification methods below and create no scope.

- **VER-001** — Execute the parser over a well-formed workplan fixture and a well-formed `LOOP_INIT.md` fixture and assert the emitted Workplan, Step, and Gate entities equal each fixture's declared expectation, including the recorded gate state on every Gate.
- **VER-002** — Compare the set of prose constructs actually read, by instrumentation or code inspection, against the documented grammar; mutate an undeclared construct in a fixture and assert output invariance; and execute a fixture whose structure the grammar does not recognize, asserting the documented behaviour rather than a best-effort parse.
- **VER-003** — Inspect this deliverable's source for any record-tier type definition and assert none is present; assert every emitted entity is constructed against the upstream Workplan, Step, or Gate type as the contract quoted in CLM-008 obliges it; and grep the source and fixtures for any assumption that an upstream schema, model, or store exists, asserting none.
- **VER-004** — Gate-state exercise: run the parser over a fixture set spanning the notations recorded in CLM-015 plus a gate with no recorded state, and assert per case that the emitted state matches the source, that the stateless gate yields an unstated state and not a default, and by call-graph inspection that no evaluation, verdict, or ruling-inference path exists in the module.
- **VER-005** — Standing-plan exercise: point the parser at a fixture tree containing a live workplan alongside candidate, archived, superseded, and proposal-staged workplans, assert that none of the latter is emitted as the standing plan, read the declared identification basis out of the grammar documentation, and assert that a tree in which that basis does not resolve returns an explicit limitation instead of a selection.
- **VER-006** — Provenance resolution: for a sample entity of each of the three types, resolve the recorded provenance to a live file source and assert that path, anchor, and/or SHA are present and locatable.
- **VER-007** — Execute the parser against absent, unreadable, malformed, and grammar-unrecognized fixtures and assert, per case, an explicit limitation naming the file and the fault, with no dropped, empty, partial, or defaulted entity returned.
- **VER-008** — Hash the fixture corpus tree before and after a parser run and assert byte-identity; inspect the module's call graph for write, create, or delete operations against any source path.
- **VER-009** — Content-minimal inspection: run the parser over a prose-dense fixture carrying long step bodies, quoted instruction text, and embedded diff-shaped content, and assert field by field that the emitted entities carry none of it, only paths, counts, identifiers, states, SHAs, and hashes.
- **VER-010** — Determinism check: run the parser twice over the same unchanged fixture corpus and assert the emitted entities are identical; inspect the emitted field inventory for any value the parser did not derive from the source files.
- **VER-011** — Inspect the `PKG-02` dependency manifest and this module's import graph for third-party runtime dependencies and network calls, and re-run the `DEL-01-05` zero-dependency and locality enforcement once that deliverable is available, without discharging it here.
- **VER-012** — Boundary inspection: assert the parser opens no sibling feed file, emits no entity type other than Workplan, Step, and Gate, performs no lookup against a decision register for a gate reference found in workplan prose, and contains no reconciliation, drift-classification, stamping, citation-attachment, gate-evaluation, or slate-rendering code path.
- **VER-013** — Run the `PKG-02` test suite and confirm that each of VER-001 through VER-012 has a corresponding executing automated test and that no test asserts a criterion absent from this contract.

## Governing Values and Decisions — Axiology

- **AX-001** — `OBJ-001` governs: orientation is a sub-second query with per-claim citations. `PEC-ORI-001` names gate states among the things PEC serves per loop, and a gate state that cannot say which file and anchor it came from cannot serve a cited orientation; provenance is therefore a property of what this parser emits (REQ-006) rather than a decoration added downstream.
- **AX-002** — `OBJ-002` governs indirectly, through the record tier. This deliverable produces facts the SHA comparison operates over; it does not perform that comparison, and no requirement here may be read as claiming otherwise. Its contribution to the objective is that its output is deterministic and regenerable (REQ-010), so a difference between two reconciles is a structural difference and never a judgment.
- **AX-003** — `PEC-K-06` observation-not-participation is the governing posture for this particular feed, because a gate is the one place where reading and ruling are easy to confuse. A workplan states where the loop stops for its owner; PEC may report that state and may not advance it, satisfy it, or infer it. `PEC-GAT-004`'s prohibition on any adoption, ruling, or direction write path is absolute across PEC, and REQ-004 keeps this parser well inside it by transcribing rather than concluding.
- **AX-004** — `PEC-K-08` explainability is why gate evaluation lives in `PKG-05` and not here. An Explain-shaped verdict needs a rule, a threshold, and contributing citations; this parser supplies one of the three and would have to invent the other two to produce a verdict. Keeping the parser to parsed facts is what lets `DEL-05-01` be explainable later (CLM-012).
- **AX-005** — `PEC-K-10` content-minimal is a residency posture, not a storage optimization, and this feed is the most prose-dense in `PKG-02`: every file in the measured corpus is instruction text with no machine-readable shape (CLM-015). The strongest available enforcement is emitting entities that have nowhere to put prose (REQ-009); the ingest-side guard is `DEL-01-03`'s.
- **AX-006** — `PEC-K-02` files govern: a workplan is authored loop truth and PEC's parse of it is a projection, regenerable and never citable as authority over the file itself. `PEC-RCN-004` and `PEC-RCN-006` make the read-only posture a rule rather than a habit (REQ-008). A loop's own `LOOP_INIT.md` says the same of itself — the root loop's records that it "is orientation, not authority" — and a parser that let its projection outrank the file would invert that.
- **AX-007** — `PEC-K-01` graceful absence governs: no governed act may require a PEC read or write. A loop whose protocol files the declared basis does not locate — which is the pec loop's condition relative to its own decomposition tree today (CON-005) — is a stated coverage limitation, never a blocked act and never a silent gap.
- **AX-008** — Honesty about the standing plan is the value REQ-005 protects. Three loops state three incompatible selection rules and one of them forbids another's (CLM-015, CON-003); a parser that quietly picked one would be exporting a governance choice as a parsing detail, and would do so in the entity `PRD.md` §7.1 scopes to "the standing plan". Declaring the basis and refusing to guess keeps the choice where it belongs.
- **AX-009** — `DL-4` is the decision that makes this deliverable atomic: one feed kind, one separately testable unit, one declared grammar. Absorbing a sibling feed grammar (`DEL-02-01`..`DEL-02-05`, `DEL-02-07`), the entity model that types this output (`DEL-01-01`), the reconciler that consumes it (`DEL-03-01`), the gate evaluators that reason over it (`DEL-05-01`), or the limitation-honesty surface (`DEL-04-05`) would undo that decision. REQ-012 states the boundary as a requirement so that it is checkable.
- **AX-010** — The edges `[E-P08]` (upstream, `DEL-01-01` → `DEL-02-06`) and `[E-P24]` (downstream, `DEL-02-06` → `DEL-03-01`) are `PROPOSAL` stratum and are accepted: `D-PEC-62` §1(4) accepted the candidate DAG v0.2 exhibit "accepted, all strata as presented", and that packet reads "as presented" as accepting the exhibit's flags as flags, so what remains recorded-but-unresolved is the specific annotated set (E-A11, E-P69/E-N02, E-N13/E-N18, the C-02 direction, the C-08 standing-node set) — none of which touches `E-P08` or `E-P24`, both of which carry an empty `Flag` column in the exhibit. Stratum is provenance, not authority: it records how an edge was derived, not whether it has been accepted, and citation does not convert `PROPOSAL` to `DECLARED`.
- **AX-011** — Edge direction is a constraint on this contract, not a licence. `RequiredMaturity` `INITIALIZED` on `[E-P08]` means the upstream *contract* is the reliable input, not any upstream artifact; this contract is written against the obligations quoted in CLM-008 and asserts nothing about upstream implementation state. Consuming that contract imposes no obligation on `DEL-01-01`, and being consumed by `DEL-03-01` neither expands nor transfers scope in either direction.
- **AX-012** — Unknowns stay marked. TBD-001 through TBD-005 and CON-001 through CON-005 are recorded rather than resolved by inference. `C-04` `PHASE_PRECEDENCE` and `C-10` `STRATUM_RULE` are register-wide non-gating constraints recorded in `_DEPENDENCIES.md`, and blocker output under the `FULL_GRAPH` mode at threshold `INITIALIZED` is advisory visibility only, never work assignment.
- **AX-013** — This contract is lifecycle-neutral. `_STATUS.md` remains the sole lifecycle authority and is untouched by the run that authored this document; the deliverable is at `OPEN` and nothing has been built.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-016 OBJ-001 OBJ-002 | REQ-001, CLM-001, CLM-002, CLM-004 | AC-001 | VER-001 | The well-formed workplan and `LOOP_INIT.md` fixtures with parser output, showing the Workplan, Step, and Gate entities and each gate's recorded state |
| OUT-001 | SOW-016 OBJ-001 OBJ-002 | REQ-002, CLM-006, CLM-015, TBD-002, CON-001 | AC-002 | VER-002 | Grammar documentation, the construct-coverage comparison, the undeclared-construct invariance result, and the unrecognized-structure transcript |
| OUT-001 | SOW-016 OBJ-001 OBJ-002 | REQ-003, CLM-008, TBD-003, CON-002 | AC-003 | VER-003 | The entity construction surface against the quoted upstream Workplan/Step/Gate obligation, plus a recorded search of this deliverable's source for record-tier type definitions and upstream-artifact assumptions |
| OUT-001 | SOW-016 OBJ-001 OBJ-002 | REQ-004, CLM-012, AX-003, AX-004 | AC-004 | VER-004 | Per-notation gate-state transcripts including the stateless-gate case, with a call-graph inspection record showing no evaluation, verdict, or ruling-inference path |
| OUT-001 | SOW-016 OBJ-001 OBJ-002 | REQ-005, TBD-004, CON-003, AX-008 | AC-005 | VER-005 | The candidate/archived/superseded/proposal fixture tree with parser output, the declared identification basis in the grammar documentation, and the unresolvable-tree limitation transcript |
| OUT-001 | SOW-016 OBJ-001 OBJ-002 | REQ-006, CLM-011, TBD-005 | AC-006 | VER-006 | Per-type provenance resolution records showing path, anchor, and/or SHA present and locatable |
| OUT-001 | SOW-016 OBJ-001 OBJ-002 | REQ-007, CON-004, CON-005, AX-007 | AC-007 | VER-007 | Per-case transcripts for absent, unreadable, malformed, and grammar-unrecognized fixtures, each showing the file named and the fault located |
| OUT-001 | SOW-016 OBJ-001 OBJ-002 | REQ-008, AX-006 | AC-008 | VER-008 | Before/after fixture-corpus tree hashes and a call-graph inspection record showing no write path against a source file |
| OUT-001 | SOW-016 OBJ-001 OBJ-002 | REQ-009, CLM-013, AX-005 | AC-009 | VER-009 | Field-by-field inspection of the entities emitted for a prose-dense fixture against the declared grammar |
| OUT-001 | SOW-016 OBJ-001 OBJ-002 | REQ-010, AX-002 | AC-010 | VER-010 | Two-run output comparison over an unchanged fixture corpus plus the emitted-field derivation inspection |
| OUT-001 | SOW-016 OBJ-001 OBJ-002 | REQ-011 | AC-011 | VER-011 | Dependency-manifest and import-graph inspection records, plus the DEL-01-05 enforcement result once that deliverable is available |
| OUT-001 | SOW-016 OBJ-001 OBJ-002 | REQ-012, CLM-005, CLM-009, CLM-010, AX-009, AX-011 | AC-012 | VER-012 | Recorded search showing no sibling feed opened, no entity type other than Workplan/Step/Gate emitted, no decision-register lookup performed, and the reconciliation, stamping, citation-attachment, gate-evaluation, and slate code paths absent |
| OUT-002 | SOW-016 OBJ-001 OBJ-002 | REQ-013, CLM-014 | AC-013 | VER-013 | PKG-02 test-run output mapping each executed test to its declared verification method, with no criterion asserted that this contract does not state |
| OUT-001 | SOW-016 OBJ-001 OBJ-002 | CLM-003, AX-001, AX-010, AX-012, AX-013 | AC-014 | HUMAN_REVIEW: REVIEW gate confirms traceability to SOW-016 and to OBJ-001/OBJ-002 as ruled at SCA-002 Gate 3 Q2, confirms the indirect OBJ-002 leg is stated no more strongly than that record states it given the unadopted N1 narrowing evidence and the absence of a confidence label, and confirms no sibling or cross-package scope absorption | Review record citing the scope-ledger row, the Gate 3 Q2 ruling and D-17, and the sibling and cross-package deliverable boundaries |
