---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-08
package_id: PKG-02
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@c9e5cd87d
project_scope_refs: [SOW-095]
package_objective_refs: [OBJ-001, OBJ-002]
---

# Scope of Work — DEL-02-08 Work-graph parser

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-02-08` — "Work-graph
parser" — in `PKG-02` File-Truth Parsers of the PEC v2 build. It covers project
scope item `SOW-095` in service of package objectives `OBJ-001` and `OBJ-002`.
It is the deliverable's first contract; no earlier production contract exists.

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.5** (`current_basis`, SCA-005 successor), accepted by the owner at
SCA-005 checkpoint group 3 on 2026-09-25. The frontmatter pin `c9e5cd87d` is the
checkpoint-3 acceptance commit, an ancestor of `origin/main`. At that commit
`SOFTWARE_DECOMP.md` has SHA-256 `dc2b84791454…9660`, `Deliverables.csv`
`b8628fc4c7b3…3d65a` and `ScopeLedger.csv` `83152a94d91c…9df`, the values
`_Decomposition/_LATEST.md` records, and `docs/PRD.md` v2.3 has SHA-256
`fff27a66cd23…dc32`.

**Observation commit.** The pin binds the accepted decomposition bytes only.
This deliverable's folder and several sources cited below did not exist at
`c9e5cd87d`. Unless a claim names another commit, every statement below about
the state of a file, record, lifecycle or decision is an observation at
`origin/main` `53145aaeb`, where the three registers and the PRD named above
are byte-identical to the pin. At `53145aaeb` the deliverable-local
`_CONTEXT.md` and `_REFERENCES.md` name revision 1.5 and PRD v2.3.

**Objective warrant.** `SOW-095` entered the ledger mapped to `OBJ-001;OBJ-002`
under SCA-005 (decision-log entry `DL-20`: "SOW-095 and SOW-096 enter mapped to
OBJ-001/OBJ-002"), and its ledger `Notes` cell states the ground as "objectives
per the DL-17 parser precedent". That precedent is the accepted §3 mapping note,
which now reads: "Parser items (SOW-011..017, SOW-095, SOW-096) underlie
OBJ-001/OBJ-002 through the record tier (SOW-001)". The attribution is therefore
*indirect*, through the record tier. This contract does not state it more
strongly: the `OBJ-002` leg rests on the parser extracting the commit and blob
identities that structural staleness comparison operates over; the parser
performs no such comparison. `AC-018` puts that qualification before the review
gate.

- **CLM-001** — The accepted `ScopeLedger.csv` row for `SOW-095` reads in full (columns `ScopeItemID,InOutStatus,ScopeItemStatement,SourceRef,PackageID,DeliverableIDs,ObjectiveIDs,DecisionRef,OpenIssue,Notes`):

> ``SOW-095,IN,"Parse `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md` content-minimally (declared run-identity token, node IDs, closed-vocabulary node states, DEL bindings, PR numbers, hex SHAs, linked paths, per-state counts), discovered per the loop's declared feed profile; read the integration ref by default, with local branch refs opt-in and labelled unintegrated; resolve cited PR numbers to local merge commits by read-only plumbing, reporting unresolved-locally and never guessing","PEC-RCN-002 (PRD v2.3), §7.1 WorkGraph/WorkNode",PKG-02,DEL-02-08,OBJ-001;OBJ-002,SCA-005,FALSE,"New feed kind under SCA-005 (DL-4, DL-20); node states are declared activity, never liveness; objectives per the DL-17 parser precedent"``

- **CLM-002** — The ledger `SourceRef` resolves to two PRD v2.3 loci. `PEC-RCN-002` (§9.2) opens "The reconciler shall ingest, per the closed, PEC-versioned feed profile declared on each loop-registry row (§16.3; PEC's reading hypothesis, never the loop's truth), at minimum:" and its work-graph clause reads:

> work graphs `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md`
> (content-minimal; integration ref by default, local branch refs opt-in and
> labelled unintegrated; cited PR numbers resolved to local merge commits by
> read-only plumbing, reported when unresolved locally, never guessed)

  The §7.1 record-tier row "WorkGraph / WorkNode" states the entity's purpose:

> A loop's undertaking graph
> `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md` and its
> nodes, discovered per the loop's feed profile and read content-minimally
> (declared run-identity token, node IDs, closed-vocabulary node states, DEL
> bindings, PR numbers, hex SHAs, linked paths, per-state counts); a node state
> is declared activity, never a liveness assertion; terminal completion is
> derived from local Git merge reachability of cited PRs

- **CLM-003** — The objective statements this deliverable serves are `OBJ-001` "Orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation" (§3, `SourceRef` §3.1) and `OBJ-002` "Staleness is detected structurally by SHA comparison, never by judgment" (§3, `SourceRef` §3.2). Both attributions are indirect through the record tier per the warrant above.

## Deliverable Definition — Ontology

`DEL-02-08` is typed `BACKEND_FEATURE_SLICE` at Context Envelope **`M`** with
`PhaseHint` `P1`. Its `AnticipatedArtifacts` field is three-part — "Parser +
pinned golden-by-reference fixture suites for the three fixture classes (FC-1
receipt present; FC-2 evidence-only; FC-3 no AgentRuns record) + synthetic
grammar-edge fixtures" — and the three outputs below are that list and nothing
beyond it.

- **OUT-001** — A work-graph parser in the PEC service core: it discovers a loop's current undertaking graphs where that loop's registered feed profile declares them, reads each graph at the selected Git ref through read-only plumbing, applies the declared work-graph grammar, resolves cited PR numbers to local merge commits, and emits content-minimal WorkGraph and WorkNode facts together with an explicit statement of every field or graph it could not obtain.
- **OUT-002** — Pinned golden-by-reference fixture suites for the three fixture classes FC-1 (receipt present), FC-2 (evidence-only) and FC-3 (no AgentRuns record): each fixture is a pinned `(commit, path, blob)` reference read through read-only Git plumbing, paired with a content-minimal golden record of the expected output, with no source file copied into PEC's tree.
- **OUT-003** — Synthetic grammar-edge fixtures authored fresh in PEC's tree, and the fixture test suite that executes OUT-002 and OUT-003 against OUT-001, implementing the verification methods declared in this contract.

### Identity of record

- **CLM-004** — `DEL-02-08` is named "Work-graph parser", Type `BACKEND_FEATURE_SLICE`, Context Envelope `M`, `PhaseHint` `P1`, `ResponsibleParty` `TBD`, `CoversScopeItems` `SOW-095`, `SupportsObjectives` `OBJ-001;OBJ-002`; sources `execution/_Decomposition/Deliverables.csv` row `DEL-02-08` and `SOFTWARE_DECOMP.md` §5 PKG-02 table ("| DEL-02-08 | Work-graph parser | BACKEND_FEATURE_SLICE | M | P1 | SOW-095 |"). The folder was created under `D-PEC-93` on 2026-09-25, and its `_STATUS.md` reads `OPEN`.
- **CLM-005** — The register `Description` of record is: "Content-minimal parser for `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md` (declared run-identity token, node IDs, closed-vocabulary node states, DEL bindings, PR numbers, hex SHAs, linked paths, per-state counts), discovered per the loop's declared feed profile; integration ref by default, local branch refs opt-in and labelled unintegrated; cited PR numbers resolved to local merge commits by read-only plumbing, unresolved-locally reported, never guessed. Node states are declared activity, never liveness; graph prose is never extracted." Four terms are carried as written and not strengthened: the extraction set is the enumerated list; discovery is **per the loop's declared feed profile**; branch refs are **opt-in** and **labelled unintegrated**; and graph prose is **never extracted**.
- **CLM-006** — The envelope record is: `Deliverables.csv` `ContextEnvelopeNotes` "M: a new grammar plus profile-driven discovery, PR-to-merge-commit resolution inputs and three pinned fixture classes; kept one cohesive parser slice"; `ContextBudgetQA.csv` row `DEL-02-08` with `Risk` `MEDIUM` and `RecommendedAction` "Hold as M; split profile-driven discovery and PR-to-merge resolution from the grammar only if the fixture classes prove adversarial"; and decomposition §8, which records `DEL-02-08` as "M with MEDIUM risk … held as one parser slice". The split guidance constrains how the work is sliced; it is not additional scope.

### Placement in the work graph

- **CLM-007** — `Dependencies.csv` holds three rows. `DEP-02-08-001` and `DEP-02-08-002` are `ANCHOR` rows (package-local to `PKG-02`; the `SOW-095` requirement trace). `DEP-02-08-003` is the single `EXECUTION` upstream edge: predecessor `DEL-01-01` "Record-tier schema & entity model", `DependencyType` `PREREQUISITE`, `Statement` "Parser emits WorkGraph/WorkNode entities of the record-tier model", `Explicitness` `IMPLICIT`, `RequiredMaturity` `INITIALIZED`, `SatisfactionStatus` `PENDING`, `Confidence` `MEDIUM`, `Origin` `EXTRACTED`, `Status` `ACTIVE`, `Notes` "PROPOSAL; Flag=none; EdgeID=E-P79; seeded under D-PEC-93 (SCA-005 B3)". `_DEPENDENCIES.md` records one informational downstream consumer: `DEL-03-01` "Full-rebuild reconciler (one command)" via `[E-P81]`, whose row `DEP-03-01-015` lives in that consumer's register (`Statement` "Full rebuild ingests work graphs", `RequiredMaturity` `INITIALIZED`). Neither register holds an edge between this deliverable and `DEL-01-06`.
- **CLM-008** — `DEL-01-01` is at lifecycle `INITIALIZED`, the maturity `[E-P79]` requires, but its accepted contract predates SCA-005. Its `ScopeOfWork.md` (SHA-256 `43f1f57a13bb…0170`) obliges "exactly the fourteen record-tier entity types" and names no WorkGraph or WorkNode type. The revision-1.5 register row for `DEL-01-01` names "16 entity types (Workplan/Step/Gate, Package/Deliverable and WorkGraph/WorkNode are compound rows)". SCA-005 `Propagation_Plan.md` §B4 classes that contract `STALE_REBUILD_REQUIRED`, and the undertaking graph schedules its rebuild as node S2. The WorkGraph/WorkNode type this parser emits into is therefore register-obliged but not yet contract-obliged (CON-001).
- **CLM-009** — Discovery "per the loop's declared feed profile" presupposes a registry row that declares one. At `53145aaeb`, `DEL-01-06` is `INITIALIZED`, its accepted contract (SHA-256 `5fdcfd968345…a2fa8`) requires a strict version-1 registry with no feed profile, and SCA-005 §B4 classes it `STALE_REBUILD_REQUIRED … gated on B6`. The B6 registry source packet is `D-PEC-96`. Its revision 4 (SHA-256 `4506597b1bfd…180e`, merged to `origin/main` at `6281273fa`) has the closed vocabulary `shared-dev-loop`, `loop-receipts-ledger` and `agentruns-json`, each at version 1, with no profile or surface that reads `## Remaining` sections; its `shared-dev-loop` profile covers, among other surfaces, a `work-graphs` surface. At `53145aaeb` its decision-register row reads `RULED A / EFFECTIVE ON MERGE`, with the owner's ruling recorded in `D-PEC-96_RULING_2026-09-26.md` (merged at `f90320c1d`). The registry act it authorizes is not applied at that commit: `v2/config/loops.json` still carries `"schema_version": 1` and no feed profile, and the `DEL-01-06` contract is not rebuilt. This contract relies on none of the proposal's identifiers (CON-002, TBD-004).
- **CLM-010** — Phase staging, checked against the `PhaseHint` column of `Deliverables.csv` for every deliverable this contract names in its own voice: `DEL-02-08`, `DEL-01-01`, `DEL-01-03`, `DEL-01-05`, `DEL-01-06`, `DEL-02-01` through `DEL-02-07`, `DEL-02-09`, `DEL-03-01`, `DEL-03-02`, `DEL-03-03`, `DEL-03-04`, `DEL-04-01`, `DEL-04-03`, `DEL-04-05`, `DEL-10-02` and `DEL-10-10` carry `P1`; `DEL-05-01` carries `P2`; `DEL-06-02`, `DEL-06-06` and `DEL-10-06` carry `P3`. No claim here stages any of them differently, and the sole upstream edge runs from a `P1` deliverable.

### Boundaries

- **CLM-011** — The feed split is decision-log entry `DL-4` ("one per feed kind"), extended by `DL-20`, which added `SOW-095` and `SOW-096` as new feed kinds. The adjacent feed grammars belong to siblings: `_STATUS.md` to `DEL-02-01` (`SOW-011`); decision registers and packets to `DEL-02-02` (`SOW-012`); `LOOP_RECEIPTS.md` ledgers and central `RECEIPT.md` receipts to `DEL-02-03` (`SOW-013`); `STATUS.json` and `RUNTIME_SUMMARY.json` to `DEL-02-04` (`SOW-014`); `Dependencies.csv` and historical `WORK_GRAPH.json` to `DEL-02-05` (`SOW-015`, whose register description ends "Markdown `WORK_GRAPH.md` belongs to DEL-02-08"); `LOOP_INIT.md` identity and workplans to `DEL-02-06` (`SOW-016`); `_harness/adapter.yaml` to `DEL-02-07` (`SOW-017`); and deliverable `MEMORY.md` run-index entries to `DEL-02-09` (`SOW-096`). The acts that consume this parser's output are owned elsewhere and are cited, never discharged: deriving terminal completion from merge reachability and serving parked lanes and gate states over graph nodes is `DEL-04-01` (`SOW-004`); classifying terminal-node lag and graph-behind-Git drift is `DEL-03-03` (`SOW-019`); stamping freshness and attaching per-claim citations is `DEL-04-03` (`SOW-006`, `SOW-007`); rendering a limitation into a response is `DEL-04-05` (`SOW-009`); full rebuild is `DEL-03-01` (`SOW-010`, `SOW-021`); incremental reconcile on Git delta is `DEL-03-02` (`SOW-018`); parity diffing is `DEL-03-04` (`SOW-020`); gate evaluation is `DEL-05-01` (`SOW-022`, `SOW-023`); the record-tier types are `DEL-01-01` (`SOW-001`); the ingest-boundary guard is `DEL-01-03` (`SOW-056`); zero-dependency and locality enforcement is `DEL-01-05` (`SOW-052`, `SOW-053`); the loop registry and its feed-profile declarations are `DEL-01-06` (`SOW-077`, `SOW-094`); worktree, branch, ahead/behind and dirty-state scanning is `DEL-06-02` (`SOW-027`); advisory overlap detection is `DEL-06-06` (`SOW-031`) with its seeded-conflict test `DEL-10-06` (`SOW-061`); directed self-ingest validation is `DEL-10-10` (`SOW-064`); and the standing kill test is `DEL-10-02` (`SOW-055`).
- **CLM-012** — The `PKG-02` charter (decomposition §4) is "Read-side grammars over governed files: … Markdown work graphs, the MEMORY run index and `LOOP_INIT.md` identity as first-class feeds; …", with "Writing anything; interpretation beyond declared grammars" recorded as out of package scope. Both exclusions bind this deliverable directly.
- **CLM-013** — The shared method surface this parser reads is the bundled `construct-local-work-graph` workflow and its template (`workflows/construct-local-work-graph/resources/work-graph-template.md`). At `53145aaeb` the template has SHA-256 `5661c6097cee…6fa6` and the workflow `3e197c9ddc75…9dc3`; at the decomposition pin `c9e5cd87d` they were `4411d0c25b1d…2261` and `24268f3545ea…4525`, before Root commit `ea5009d05` revised both. At `53145aaeb` the template declares the identity bullet "Stable run identity: <ID used by the graph, deliverable MEMORY rows and PR>", a `## Work` table with columns "ID / outcome | Deliverables and work scope | Needs / why | Completion check | State / result", and the state rule "Use PLANNED, READY, ACTIVE, BLOCKED, UNCERTAIN and COMPLETE consistently. A node awaiting a human decision is BLOCKED and names that decision." That Root tranche, `ROOT-WORKFLOW-WAVE2A-EXECUTION-20260926` (PEC notice `NOTICE_2026-09-26_WORKFLOW_WAVE2A_EXECUTION.md`), names PEC among the adopting loops, keeps one designated current graph ref, and added the second sentence of the state rule and a "Current graph ref" bullet to the template's recovery section; the six state tokens are unchanged from `c9e5cd87d`. The method states that graph construction "changes no scope, hold, lifecycle or release authority by itself", and the SCA-005 feed-model design note classes a graph as authority "for undertaking execution state only".
- **CLM-014** — The fixture strategy is SCA-005 `Propagation_Plan.md` §B7, accepted at checkpoint 2, which places it "inside the DEL-02-08/09 and DEL-02-03 SOWs", and its source, Impact Assessment §9.3. In their words:

> Golden-by-reference `(commit, path, blob)` fixtures pinned at `d61981ee2`,
> content-minimal goldens, nothing copied into PEC's tree: FC-1 receipt present
> (Piping `PIPING_LINTER_SCOPE_20260923`), FC-2 evidence-only (Piping
> `PIP-DEC025-BASELINE-2026-09-23`), FC-3 no AgentRuns record (App
> `APP-REPLAY-BOUNDARY-2026-09-23`), FX-PEC-0 PEC self-ingest
> (`remaining-loop`), and synthetic grammar-edge fixtures authored under a v2
> packet (Impact Assessment §9.3; Q5 (a)).
>
> (SCA-005 `Propagation_Plan.md` §B7.)

  Impact Assessment §9.3 states what each class exercises: FC-1 "receipt fields, Examined-Through ancestry, run ID = folder"; FC-2 "run ID ≠ folder; dated-heading MEMORY; partial coverage"; FC-3 "run ID ≠ folder; bullet `## Runs`; em-dash node suffixes"; and the synthetic class "missing run identity, unknown state token, unresolved PR, seeded two-graph overlap (SOW-061)". The undertaking graph routes the fixture suites themselves to node X1 under a later v2 packet.
- **CLM-015** — SCA-005 `Propagation_Plan.md` §B4 records a carry-forward for the parser contracts:

> Carry-forward for the parser SOWs (DEL-02-01, DEL-02-08, DEL-02-09): the
> DEL-01-03 content-minimal guard admits only `OPEN`..`ISSUED` as STATE values
> (true before and after D-PEC-87/89/91), so `RETIRED`, graph node states and
> run tokens are CON-001 cases those SOWs must address.

  ID-shaped text inside this quotation is upstream source context, not a local definition or reference; the constraint it cites is `DEL-01-03/CON-001`, which records that no accepted source yet states the test separating an extracted state token from prose. The produced but unaccepted guard source (`v2/src/pec_v2/core/content_minimal_guard.py`, SHA-256 `740a4a741221…19ee9`; `DEL-01-03` is `IN_PROGRESS`) admits five field classes (path, count, SHA, state, hash), a state set of `OPEN` through `ISSUED`, and SHA digests of exactly 40 or 64 hex characters.
- **CLM-016** — The deliverable is at lifecycle `OPEN` with no implementation present. Every requirement, acceptance criterion and verification method below states a contract on future production; none asserts that anything has been built.
- **CLM-017** — Observed corpus condition, recorded as observation and not as specification. At `origin/main` `7a00a88df` five files sit at the canonical path: one App graph, three Piping graphs and one PEC graph. The run-identity bullet appears as `- Stable run identity:` in four and as `- **Stable run identity:**` in the PEC graph. Graph folder names differ from the declared run identity in two of the three 2026-09-23 trials (SCA-005 risk R-02). ID-led table rows occur outside the `## Work` table (for example under `## Current state and recovery` and in adopted predecessor sections), node-ID tokens include forms such as `T0R`, `B3A`, `D72` and `M01`, and the adopted Piping UI-implementation graph has ID-led rows whose final cell begins with a token outside the template vocabulary (for example `Deferred`, `ROUTE`, `PARTIAL`, `REFERENCE`). Graph cells cite PR numbers as `#868`, as `PR #919` and inside GitHub pull-request URLs, and cite commits by abbreviated hex SHAs. All three trial graphs showed their terminal node `F1` as `ACTIVE` after the cited final PR had merged (SCA-005 risk R-01), which the method intends. The fixture blobs named in CLM-014 resolve at `d61981ee2` and are byte-unchanged at `7a00a88df` and at `53145aaeb`. SCA-005 risk R-09 records that name-based discovery over-selects: 53 files named `WORK_GRAPH.md` against 3 canonical ones at its basis. None of this is a grammar, and no rule is derived from it here.
- **CLM-018** — `## Remaining` sections are outside this feed. PRD v2.3 §7.1 states, for the Package/Deliverable census from `_STATUS.md`, that "remaining items is a per-loop optional field, read only where the loop's feed profile declares it"; that field is `_STATUS.md` content, whose grammar is `DEL-02-01`'s (CLM-011), and it is neither a work-graph nor a MEMORY surface. This deliverable reads no `## Remaining` section of any file, and its discovery depends on no feed profile or surface that reads one; the ruled revision-4 vocabulary of CLM-009 contains none.

- **TBD-001** — `ResponsibleParty` is unassigned; the register records `TBD`, with assignment at WORKING_ITEMS activation.
- **TBD-002** — The exact grammar is fixed by no accepted source beyond the field list of CLM-001 and the template of CLM-013: which tables count as node tables, the node-ID token shape, the column holding the state token, and how the run-identity bullet is recognized in its observed spellings. These are chosen during production within REQ-003 through REQ-006 and recorded in the grammar declaration of REQ-003.
- **TBD-003** — The PR-number syntaxes recognized and the read-only method that maps a PR number to a local merge commit (for example merge-commit subjects or squash-merge suffixes) are fixed by no accepted source. They are chosen during production within REQ-008.
- **TBD-004** — The feed-profile identifier, version and surface name under which a loop declares its work graphs are fixed by no accepted contract at `53145aaeb`: `D-PEC-96` is ruled, but its registry act is not applied and the `DEL-01-06` contract is not rebuilt, and they arrive with that rebuild. The revision-4 identifiers named in CLM-009 are not relied on.
- **TBD-005** — Which local branch refs are read when branch reading is enabled, and whether the template's "Current graph ref" bullet may guide that selection, are not fixed. A ref token is not in the `SOW-095` extraction list, so reading that bullet as data would need a scope decision, not a production choice.
- **TBD-006** — The golden-record format and the length threshold for the no-source-text assertion of REQ-016 are fixed by no accepted source; the design note that proposed the assertion calls it "a small length threshold".
- **TBD-007** — How an abbreviated hex SHA cited in a graph is represented — carried as cited with an explicit abbreviated label, or resolved to a full object name where local plumbing resolves it unambiguously — is not fixed; either choice must satisfy REQ-008's no-guessing rule and CON-003.

## Completion and Reliance Basis — Epistemology

The requirements below state what future production must satisfy. Nothing in
this section asserts that a parser, a grammar declaration, a fixture or a test
exists.

- **REQ-001** — The parser shall discover graphs only at `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md` within a loop whose registered feed profile declares the work-graph surface, reading that declaration through the loop-registry port of `DEL-01-06`. A file of the same name at any other path shall not be discovered. Where a loop's registry row declares no work-graph surface, or no registry declaration is available, the parser shall discover nothing for that loop and shall report the absence of a declaration; it shall never infer a declaration from the presence of files. Discovery shall depend on no feed profile or surface that reads `## Remaining` sections (CLM-018).
- **REQ-002** — The parser shall read graphs at the integration ref by default. It shall read local branch refs only when that reading is explicitly enabled, and every fact read from a ref other than the integration ref shall carry that ref and its commit and be labelled unintegrated. All Git access shall be read-only plumbing over local objects: no checkout, index or worktree change, ref update or fetch.
- **REQ-003** — The parser shall extract exactly the `SOW-095` field set — the declared run-identity token, node IDs, closed-vocabulary node states, DEL bindings, PR numbers, hex SHAs, linked paths and per-state counts — under one declared work-graph grammar that names every construct it reads and carries an identifier and version. No construct outside the declared grammar shall influence the output, per the `PKG-02` out-of-scope line "interpretation beyond declared grammars" (CLM-012).
- **REQ-004** — A node state shall be recognized only from the closed vocabulary the adopted method declares (CLM-013: `PLANNED`, `READY`, `ACTIVE`, `BLOCKED`, `UNCERTAIN`, `COMPLETE`). A state cell that does not begin with a vocabulary token shall yield an explicit unrecognized-state limitation for that node; it shall never be coerced to a vocabulary state, and the unrecognized token shall not be carried as free text. A change to the method's vocabulary shall be absorbed as a change to the grammar declaration and its fixtures, without amending this contract.
- **REQ-005** — Every emitted node state shall be expressed as declared activity at a cited commit — the state the graph declared at that path, blob and commit — and never as a liveness assertion or as completion. The parser shall not mark a node complete from Git evidence, shall not derive terminal completion, and shall not classify lag; those acts are owned as CLM-011 records.
- **REQ-006** — The run identity shall be taken only from the graph's declared run-identity field and never derived from the folder name or path (SCA-005 risk R-02). A graph with no declared identity, with more than one, or with an identity the grammar cannot read shall yield an explicit limitation, and its nodes shall be emitted without a fabricated identity.
- **REQ-007** — DEL bindings shall be the `DEL-` identifiers the grammar finds in a node's row, emitted as identifiers; linked paths shall be emitted as normalized repository-relative paths only, never with their link text; an external URL shall never be followed.
- **REQ-008** — Each cited PR number shall be resolved to a local merge commit by read-only plumbing over objects reachable from the examined ref, and the result shall record the PR number, the resolved commit or the outcome "unresolved locally", and the resolution method's identifier. A PR number shall never be guessed, fetched, or resolved through a network service, and no SHA shall be padded, completed or inferred.
- **REQ-009** — Where a graph is absent, unreadable or not parseable under the grammar, or where a section, a node-state cell or the run identity cannot be read, the parser shall return an explicit limitation naming the loop, the path and the fault, with a parse outcome of parsed, partial, unparseable or absent. A silently omitted, defaulted or inferred field or graph is prohibited, per `PEC-ORI-006` and `SOW-009`. Rendering the limitation into a response is `DEL-04-05`'s (CLM-011).
- **REQ-010** — No emitted field shall hold graph prose. Outcome text, "needs" text, completion-check text, result text, intent and steering bullets, open questions and the prose of the recovery section shall not be expressible anywhere in the output, per `PEC-K-10` ("Paths, counts, SHAs, states, hashes — never file or diff content") and constraint `C6`. Enforcement at the ingest boundary is `DEL-01-03`'s under `SOW-056` (CLM-011); this requirement binds what the parser is able to emit.
- **REQ-011** — Every emitted fact shall carry provenance sufficient for a per-claim citation to its live source — loop, path, blob SHA, examined commit, ref label and grammar identifier — per `PEC-ORI-004`. Attaching citations to a response is `DEL-04-03`'s (CLM-011).
- **REQ-012** — The parser shall create, modify or delete no file and no Git state, including the graphs it reads, per `PEC-RCN-004`, `PEC-RCN-006`, `PEC-K-06` and the `PKG-02` out-of-scope line "Writing anything".
- **REQ-013** — Parsing shall be deterministic: identical graph blobs, refs and object store under an identical grammar declaration shall yield identical output, including identical limitations and PR resolutions.
- **REQ-014** — The parser shall emit WorkGraph and WorkNode facts shaped to the record-tier contract of `DEL-01-01` once that contract obliges those types, shall define no record-tier type of its own, and shall emit no DependencyEdge, Receipt, RunRecord, DecisionRow or Package/Deliverable entity (CON-001, CON-005).
- **REQ-015** — The parser shall parse no feed owned by a sibling deliverable and shall perform no act owned by another package. In particular it shall read no `MEMORY.md` (`DEL-02-09`), `RECEIPT.md` or ledger (`DEL-02-03`), `WORK_GRAPH.json` or `Dependencies.csv` (`DEL-02-05`), `STATUS.json` or `RUNTIME_SUMMARY.json` (`DEL-02-04`), `_STATUS.md`, including its `## Remaining` sections (`DEL-02-01`), decision register (`DEL-02-02`), `LOOP_INIT.md` (`DEL-02-06`) or `adapter.yaml` (`DEL-02-07`) as a feed of its own, and it shall perform no completion derivation (`DEL-04-01`), lag or drift classification (`DEL-03-03`), freshness stamping (`DEL-04-03`), limitation rendering (`DEL-04-05`), worktree or branch presence scanning (`DEL-06-02`), overlap detection (`DEL-06-06`), gate evaluation (`DEL-05-01`) or registry maintenance (`DEL-01-06`); each is cited to its owner in CLM-011.
- **REQ-016** — The pinned fixture suites shall be golden-by-reference: each fixture a pinned `(commit, path, blob)` reference at `d61981ee2` read through read-only plumbing, with a content-minimal golden record, and no fixture source copied into PEC's tree. They shall cover FC-1 receipt present, FC-2 evidence-only and FC-3 no AgentRuns record as CLM-014 defines them. Every golden test shall also assert that the output holds no run of source text above the threshold of TBD-006.
- **REQ-017** — Synthetic grammar-edge fixtures shall be authored fresh in PEC's tree, only at paths a ruled packet names, and shall cover at least a missing run identity, a duplicated run identity, an unrecognized state token, a graph with no node table, an unresolved PR number and two graphs binding the same `DEL-` identifier. They shall contain no text copied from another loop's files.
- **REQ-018** — The work shall be delivered as one parser slice. A split is permitted only along the recorded line — profile-driven discovery and PR-to-merge resolution separated from the grammar, if the fixture classes prove adversarial — with the seam and its evidence recorded (CLM-006). A split adds no output and changes no other term of this contract.
- **REQ-019** — The parser and its fixtures shall introduce no third-party runtime dependency and no external network egress, per `PEC-SVC-001` and `PEC-SVC-002` (constraints `C7`, `C8`), whose standing enforcement is `DEL-01-05`.
- **REQ-020** — Fixture tests shall implement the verification methods declared in this contract; they shall not define scope, requirements or acceptance criteria.

- **AC-001** — A graph at the canonical path of a loop whose registry row declares the work-graph surface is discovered; a same-named file elsewhere is not; and a loop with no declaration yields a no-declaration report and no graph facts.
- **AC-002** — With default settings only integration-ref blobs are read; with branch reading enabled, every fact from a branch ref carries its ref and commit and the unintegrated label; and a before/after comparison shows no change to refs, index, worktree or configuration.
- **AC-003** — The grammar declaration exists as a readable artifact with an identifier and version, names every construct the parser reads, and covers the eight fields of `SOW-095`; altering an undeclared construct in a fixture changes nothing in the output.
- **AC-004** — Each vocabulary state is recognized; a fixture whose state cell begins with a non-vocabulary token yields an unrecognized-state limitation with no coerced state and no copy of the token.
- **AC-005** — For a fixture whose terminal node is declared `ACTIVE` while its cited PR is merged locally, the output reports the declared state at its commit and makes no completion, liveness or lag claim.
- **AC-006** — For fixtures whose folder name differs from the declared identity, the declared identity is emitted; fixtures with no identity or with two identities yield a limitation and no fabricated identity.
- **AC-007** — DEL bindings are emitted as identifiers only, linked paths as normalized repository-relative paths without link text, and no external URL is dereferenced.
- **AC-008** — A PR number with a local merge commit resolves to that commit; one without resolves to "unresolved locally"; no network call is made; and no emitted SHA is longer or more complete than the cited or locally resolved object name warrants.
- **AC-009** — Absent, unreadable, unparseable and partially parseable fixtures each yield an explicit limitation naming loop, path and fault with the correct parse outcome, and none yields a result presented as complete.
- **AC-010** — A fixture graph whose outcome, needs, completion-check, result, intent and open-question text contains distinctive prose yields output containing none of it, and no emitted field type can hold prose.
- **AC-011** — For a sample fact from each fixture class, the recorded provenance resolves to the live source by loop, path, blob SHA, examined commit, ref label and grammar identifier.
- **AC-012** — A parser run leaves the fixture repository's objects, refs, index and worktree byte-identical, and the module contains no write, create, delete or ref-updating call.
- **AC-013** — Two runs over identical inputs yield identical output, including limitations and PR resolutions.
- **AC-014** — Reviewed against the record-tier contract in force at review time, the emitted payload introduces no field that contract does not oblige, drops none it obliges for WorkGraph and WorkNode, and contains no entity of another type; if that contract does not yet oblige WorkGraph and WorkNode, the review records the open CON-001 condition rather than passing it.
- **AC-015** — The module reads no sibling feed, including no `## Remaining` section, and performs none of the excluded acts of REQ-015.
- **AC-016** — The pinned suites reference FC-1, FC-2 and FC-3 by `(commit, path, blob)` at `d61981ee2` with content-minimal goldens, copy no fixture source into PEC's tree, and assert the no-source-text run check on every golden test.
- **AC-017** — The synthetic fixtures cover the six cases of REQ-017, sit only at packet-named paths, and contain no text copied from another loop's files.
- **AC-018** — The review gate confirms this contract's traceability to `SOW-095`, `OBJ-001` and `OBJ-002` as entered under `DL-20`, confirms the indirect `OBJ-002` leg is stated no more strongly than the §3 mapping note states it, and confirms no sibling feed grammar, `PKG-01` type or registry scope, or `PKG-03`/`PKG-04` derivation has been absorbed.
- **AC-019** — The work is delivered as one parser slice, or split along the recorded line with its seam evidence recorded.
- **AC-020** — The parser and its fixtures add no third-party runtime dependency and make no network call, leaving the `DEL-01-05` assertion intact.
- **AC-021** — The fixture test suite implements VER-001 through VER-019, executes in the `PKG-02` test run, passes, and introduces no acceptance criterion absent from this contract.

- **CON-001** — **Upstream typing.** The revision-1.5 register and PRD v2.3 §7.1 make WorkGraph and WorkNode record-tier types, but the accepted `DEL-01-01` contract obliges exactly fourteen types without them (CLM-008). This contract defines no type (REQ-014) and does not treat the register row as the upstream contract. Whether OUT-001 production waits for the `DEL-01-01` rebuild (graph node S2) or proceeds against the register text is an ordering decision for the undertaking graph and its owner, not a production choice made here.
- **CON-002** — **Discovery basis.** Discovery per the declared feed profile needs a registry that declares profiles, but the accepted `DEL-01-06` contract is strict version-1 without them, and at `53145aaeb` the ruled registry source packet `D-PEC-96` is not yet applied (CLM-009). No dependency row links this deliverable to `DEL-01-06` in either register. This contract fixes the behaviour without a declaration — nothing is discovered and the absence is reported (REQ-001) — and adopts no proposed identifier (TBD-004). Whether an execution edge to `DEL-01-06` should be recorded is a dependency-register question for its owning workflow, not resolved here.
- **CON-003** — **Guard admission.** The extracted node states, node IDs, run-identity tokens, DEL bindings and PR numbers are not lifecycle states, and abbreviated hex SHAs are not 40- or 64-character digests; the produced guard admits neither as typed (CLM-015). These are `DEL-01-03/CON-001` cases. This parser shall not coerce a node state into a lifecycle state, encode a token to pass the guard, or widen the guard; how the store admits these facts is decided under `DEL-01-03` and `DEL-01-01`, through their own packets.
- **CON-004** — **FX-PEC-0.** SCA-005 §B7 lists a PEC self-ingest fixture "FX-PEC-0 PEC self-ingest (`remaining-loop`)", while the register's `AnticipatedArtifacts` for this deliverable names only the three FC classes and synthetic fixtures. The `remaining-loop` premise changed when `D-PEC-94` adopted the shared development-loop method, and PEC now writes a work graph under that method. The ruled revision-4 vocabulary drops `remaining-loop` (CLM-009), so FX-PEC-0 as §B7 words it has no profile in that vocabulary. This contract adds no FX-PEC-0 output and no Remaining-reading fixture; directed self-ingest is `DEL-10-10`'s (`SOW-064`), and whether PEC's own graph is read depends on the registry declaration of CON-002.
- **CON-005** — **Work-graph dependencies.** PRD v2.3 §7.1 sources DependencyEdge "From `Dependencies.csv` registers and work-graph dependencies (WorkGraph)", and the `SOW-015` Notes cell says "Markdown work-graph dependencies arrive through SOW-095". The `SOW-095` extraction list does not name dependencies, and in the template they live in the prose "Needs / why" column. This contract emits no DependencyEdge (REQ-014) and extracts no node reference from prose. Whether node-ID references in a node's needs cell are to be extracted, and by which deliverable, is a scope question for the scope-change process or an owner ruling.

## Production and Verification Method — Praxeology

Production proceeds in the order grammar declaration → discovery and ref
selection → extraction and PR resolution → limitation reporting → fixtures and
tests. A grammar declared before code exists cannot have been fitted to
whatever the code happened to accept, which REQ-003 requires to be visible. All
work is bounded to this deliverable folder, the `PKG-02` service-core source and
the fixture paths a ruled packet names; this contract authorizes no register,
decomposition, PRD, registry or upstream-deliverable edit, and no v2 source
write by itself. Tests implement the verification methods below and create no
scope.

- **VER-001** — Execute discovery over a fixture tree holding a canonical graph, a same-named file at another path, a loop with a work-graph declaration and a loop without one; assert discovery, non-discovery and the no-declaration report respectively.
- **VER-002** — Execute with default settings and with branch reading enabled over a fixture repository whose branch holds a graph revision absent from the integration ref; assert ref labels and the unintegrated label; snapshot refs, index, worktree and configuration before and after and assert equality.
- **VER-003** — Inspect the grammar declaration for identifier, version and coverage of the eight `SOW-095` fields; compare the constructs actually read, by instrumentation or inspection, against it; mutate an undeclared construct in a fixture and assert output invariance.
- **VER-004** — Execute over synthetic fixtures carrying each vocabulary state and one non-vocabulary token; assert recognition, the unrecognized-state limitation, no coerced state and no copy of the token.
- **VER-005** — Execute over FC-1, FC-2 and FC-3, whose terminal nodes are declared `ACTIVE` while their cited final PRs are merged; assert declared-state output at the cited commit and the absence of any completion, liveness or lag field.
- **VER-006** — Execute over FC-2 and FC-3 (folder name ≠ run identity) and over synthetic missing- and duplicate-identity fixtures; assert the declared identity, or the limitation with no fabricated identity.
- **VER-007** — Execute over a fixture whose nodes carry DEL identifiers, relative links with link text and external URLs; assert identifier-only bindings, normalized paths without link text, and no dereference, with network access denied.
- **VER-008** — Execute over fixtures citing a PR merged in the fixture repository and a PR with no local merge commit, with network access denied; assert the resolved commit, "unresolved locally", the method identifier, and that every emitted SHA equals a cited or locally resolved object name.
- **VER-009** — Execute over absent, unreadable, unparseable and partially parseable fixtures; assert per case the limitation fields and parse outcome.
- **VER-010** — Execute over a fixture carrying distinctive prose in every prose-bearing position; assert that none of it appears in the output; review every emitted field's type for capacity to hold prose.
- **VER-011** — For a sample fact from each fixture class, resolve the recorded provenance to the source and assert each provenance element is present and locatable.
- **VER-012** — Hash the fixture repository's objects, refs, index and worktree before and after a run and assert byte-identity; inspect the module's call graph for write, create, delete or ref-updating operations.
- **VER-013** — Run the parser twice over identical inputs and assert identical output.
- **VER-014** — Review the emitted payload field by field against the record-tier contract in force at review time, and search the module for any record-tier type definition or any emission of another entity type.
- **VER-015** — Inspect the module's file and Git access for any sibling feed path or `## Remaining` read, and its call surface for any of the excluded acts of REQ-015.
- **VER-016** — Inspect the pinned fixture manifests for `(commit, path, blob)` references at `d61981ee2` covering FC-1, FC-2 and FC-3, resolve each pin by read-only plumbing, check for the absence of copied fixture sources, and run the no-source-text assertion on every golden test.
- **VER-017** — Inspect the synthetic fixture set against the six cases of REQ-017 and the packet-named paths, and compare its text against the pinned fixture blobs to assert no copied text.
- **VER-018** — Compare the delivered slice structure with the envelope record of CLM-006, asserting one parser slice or a split along the recorded line with its seam evidence.
- **VER-019** — Inspect the `PKG-02` dependency manifest and the module's import graph for third-party runtime dependencies and network calls, and re-run the `DEL-01-05` enforcement once that deliverable is available, without discharging it here.
- **VER-020** — Run the `PKG-02` test suite and confirm that each of VER-001 through VER-019 has a corresponding executing test and that no test asserts a criterion absent from this contract.

## Governing Values and Decisions — Axiology

- **AX-001** — `PEC-K-02` files govern. A work graph is the loop's own authority for its undertaking's execution state and nothing more (CLM-013); a parsed WorkGraph or WorkNode is never citable as authority over the graph, over the loop's scope, holds or lifecycle, or over Git.
- **AX-002** — Declared activity is not liveness (`SOW-095` Notes; PRD §7.1). The method deliberately leaves the terminal node trailing Git after the final merge, so reading completion from a state cell would report finished work as active. The parser therefore reports what was declared and when, and leaves completion to Git-derived reasoning owned elsewhere.
- **AX-003** — `PEC-ORI-006` coverage honesty governs. Graph shapes vary between loops and over time; the value protected is that an unreadable identity, an unknown state or an unresolved PR is *stated* rather than smoothed into a tidy record.
- **AX-004** — `PEC-K-10` content-minimal is a residency posture. For a parser the strongest enforcement is inexpressibility, which is why REQ-010 binds the emitted field shapes rather than reading behaviour, and why REQ-004 refuses to carry an unrecognized token as text.
- **AX-005** — `PEC-K-06` observation, not participation. PEC reads Git through read-only plumbing, never fetches, never moves a ref, and never resolves a PR through a network service; an unresolved PR stays unresolved (REQ-002, REQ-008; `PEC-SVC-002`).
- **AX-006** — A feed profile is PEC's reading hypothesis, never the loop's truth (PRD §16.3). Discovery follows the declaration and nothing else, so an undeclared loop is unread by design and its silence is reported, never guessed around (REQ-001, CON-002).
- **AX-007** — `DL-4` and `DL-20` make this deliverable atomic: one feed kind, one separately testable unit. Absorbing a sibling grammar, the record-tier type, the registry, or any consuming derivation would undo it (REQ-015).
- **AX-008** — The edges cited are `[E-P79]` (upstream, `DEL-01-01` → `DEL-02-08`, `PROPOSAL`) and `[E-P81]` (downstream, `DEL-02-08` → `DEL-03-01`, `PROPOSAL`), both seeded under `D-PEC-93`. Stratum is provenance, not authority, and citation converts no `PROPOSAL` into a `DECLARED` edge. `RequiredMaturity` `INITIALIZED` on `[E-P79]` makes the upstream *contract* the reliable input, which is exactly why CON-001 is recorded: that contract does not yet oblige the type this parser emits.
- **AX-009** — Fixtures reference other loops' files by pinned object identity and never copy their prose into PEC's tree (CLM-014). The goldens are themselves content-minimal, so the fixtures cannot become a second store of another loop's text.
- **AX-010** — Unknowns stay marked. TBD-001 through TBD-007 and CON-001 through CON-005 are recorded rather than resolved by inference; a production choice that settled a CON item would be a decision taken in the wrong place.
- **AX-011** — `C-04` `PHASE_PRECEDENCE` and `C-10` `STRATUM_RULE` are register-wide, non-gating constraints recorded in `_DEPENDENCIES.md`. Blocker output under `FULL_GRAPH` at threshold `INITIALIZED` is advisory visibility only and never work assignment.
- **AX-012** — This contract is lifecycle-neutral. `_STATUS.md` remains the sole lifecycle authority and is untouched by the run that authored this document; the deliverable is at `OPEN` and nothing has been built.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-095 OBJ-001 OBJ-002 | REQ-001, CLM-002, CLM-009, CLM-017, CON-002, TBD-004, AX-006 | AC-001 | VER-001 | Discovery transcripts for a canonical graph, a same-named non-canonical file, a declared loop and an undeclared loop |
| OUT-001 | SOW-095 OBJ-001 OBJ-002 | REQ-002, CLM-001, TBD-005, AX-005 | AC-002 | VER-002 | Default and branch-enabled transcripts with ref labels, plus before/after snapshots of refs, index, worktree and configuration |
| OUT-001 | SOW-095 OBJ-001 OBJ-002 | REQ-003, CLM-005, CLM-012, TBD-002 | AC-003 | VER-003 | The grammar declaration, a record of constructs actually read, and the undeclared-construct invariance result |
| OUT-001 | SOW-095 OBJ-001 OBJ-002 | REQ-004, CLM-013, CLM-017 | AC-004 | VER-004 | Transcripts for each vocabulary state and for a non-vocabulary token showing the limitation and no copied token |
| OUT-001 | SOW-095 OBJ-001 OBJ-002 | REQ-005, AX-002 | AC-005 | VER-005 | FC-1, FC-2 and FC-3 transcripts showing declared terminal states at their commits and no completion, liveness or lag field |
| OUT-001 | SOW-095 OBJ-001 OBJ-002 | REQ-006 | AC-006 | VER-006 | Identity transcripts for folder-name-divergent trials and for missing- and duplicate-identity fixtures |
| OUT-001 | SOW-095 OBJ-001 OBJ-002 | REQ-007 | AC-007 | VER-007 | Binding and link transcripts run with network access denied |
| OUT-001 | SOW-095 OBJ-001 OBJ-002 | REQ-008, TBD-003, TBD-007 | AC-008 | VER-008 | PR-resolution transcripts for resolved and unresolved cases with network denied, and an SHA-provenance comparison |
| OUT-001 | SOW-095 OBJ-001 OBJ-002 | REQ-009, AX-003 | AC-009 | VER-009 | Per-case limitation transcripts with parse outcomes |
| OUT-001 | SOW-095 OBJ-001 OBJ-002 | REQ-010, CON-003, AX-004 | AC-010 | VER-010 | The prose-bearing fixture with its output and a field-type inspection record |
| OUT-001 | SOW-095 OBJ-001 OBJ-002 | REQ-011 | AC-011 | VER-011 | Provenance-resolution records for a sample fact from each fixture class |
| OUT-001 | SOW-095 OBJ-001 OBJ-002 | REQ-012, AX-001 | AC-012 | VER-012 | Before/after repository hashes and a call-graph inspection record |
| OUT-001 | SOW-095 OBJ-001 OBJ-002 | REQ-013 | AC-013 | VER-013 | Two outputs from repeated runs over identical inputs, compared |
| OUT-001 | SOW-095 OBJ-001 OBJ-002 | REQ-014, CLM-008, CON-001, CON-005 | AC-014 | VER-014 | A field-by-field payload review against the record-tier contract in force, and a search record for type definitions and other entities |
| OUT-001 | SOW-095 OBJ-001 OBJ-002 | REQ-015, CLM-011, CLM-018, AX-007 | AC-015 | VER-015 | File-access and call-surface inspection records |
| OUT-002 | SOW-095 OBJ-001 OBJ-002 | REQ-016, CLM-014, CON-004, TBD-006, AX-009 | AC-016 | VER-016 | Pinned fixture manifests with resolved references and no-source-text assertion results |
| OUT-003 | SOW-095 OBJ-001 OBJ-002 | REQ-017, CLM-014 | AC-017 | VER-017 | The synthetic fixture list against the six cases, their paths, and the no-copied-text comparison |
| OUT-001 | SOW-095 OBJ-001 OBJ-002 | REQ-018, CLM-006 | AC-019 | VER-018 | The delivered slice structure against the envelope record, with seam evidence if split |
| OUT-001 | SOW-095 OBJ-001 OBJ-002 | REQ-019 | AC-020 | VER-019 | Dependency-manifest and import-graph inspection records, plus the DEL-01-05 result once available |
| OUT-003 | SOW-095 OBJ-001 OBJ-002 | REQ-020, CLM-016, TBD-001 | AC-021 | VER-020 | PKG-02 test-run output mapping each executed test to its verification method |
| OUT-001 | SOW-095 OBJ-001 OBJ-002 | CLM-003, CLM-004, CLM-007, CLM-010, CLM-015, AX-008, AX-010, AX-011, AX-012 | AC-018 | HUMAN_REVIEW: review gate confirms traceability to SOW-095 and to OBJ-001/OBJ-002 as entered under DL-20, confirms the indirect OBJ-002 leg is stated no more strongly than the §3 mapping note, and confirms no sibling, PKG-01, registry or PKG-03/PKG-04 scope absorption | Review record citing the ledger row, the §3 mapping note and the sibling and cross-package boundaries |
