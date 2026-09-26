---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-09
package_id: PKG-02
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@189f205ff02df4111b33c20be441ce06e65ada7a
project_scope_refs: [SOW-096]
package_objective_refs: [OBJ-001, OBJ-002]
---

# Scope of Work — DEL-02-09 MEMORY run-index parser

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-02-09` — "MEMORY
run-index parser" — in `PKG-02` File-Truth Parsers of the PEC v2 build. It
covers project scope item `SOW-096` in service of package objectives `OBJ-001`
and `OBJ-002`. It is the deliverable's first contract; no earlier production
contract exists.

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.6** (`current_basis`, SCA-006 successor), accepted by the owner at
SCA-006 checkpoint group 3 on 2026-09-26. The frontmatter pin
`189f205ff02df4111b33c20be441ce06e65ada7a` is the
checkpoint-3 acceptance commit, an ancestor of `origin/main`. At that commit
`SOFTWARE_DECOMP.md` has SHA-256 `9374c21fb87b…8eb1`, `Deliverables.csv`
`94ee5d182ae9…9805` and `ScopeLedger.csv` `1d24a4b86f05…916e`, the values
`_Decomposition/_LATEST.md` records, and `docs/PRD.md` v2.4 has SHA-256
`ae49b8065698…3fbe`.

**Observation commit.** The pin binds the accepted decomposition bytes only.
This deliverable's folder and several sources cited below did not exist at
`c9e5cd87d`. Unless a claim names another commit, every statement below about
the state of a file, record, lifecycle or decision is an observation at
`origin/main` `53145aaeb`. There the three registers and the PRD are the
revision-1.5 and PRD v2.3 bytes (`dc2b84791454…9660`, `b8628fc4c7b3…3d65a`,
`83152a94d91c…9df` and `fff27a66cd23…dc32`), which differ from the pin. The
loci this contract quotes from them were re-verified verbatim at the pin:
the `SOW-096` row of `ScopeLedger.csv`; the `DEL-02-09` and `DEL-01-01`
Descriptions in `Deliverables.csv`; the `OBJ-001` and `OBJ-002` statements,
the §3 mapping note, decision-log entry `DL-20`, the `PKG-02` charter, the §5
row and the §8 text of `SOFTWARE_DECOMP.md`; and, in the PRD, `PEC-RCN-002`,
the §7.1 RunRecord row and the §7.1 remaining-items field. At `53145aaeb` the deliverable-local
`_CONTEXT.md` and `_REFERENCES.md` name revision 1.5 and PRD v2.3.

**Objective warrant.** `SOW-096` entered the ledger mapped to `OBJ-001;OBJ-002`
under SCA-005 (decision-log entry `DL-20`: "SOW-095 and SOW-096 enter mapped to
OBJ-001/OBJ-002"), and its ledger `Notes` cell grounds it as "objectives per the
DL-17 parser precedent". That precedent is the accepted §3 mapping note:
"Parser items (SOW-011..017, SOW-095, SOW-096) underlie OBJ-001/OBJ-002 through
the record tier (SOW-001)". The attribution is *indirect*, through the record
tier. The `OBJ-002` leg is thinner here than for most parsers: a run-index entry
carries run identifiers, dates and link targets, and often no SHA at all, so this
deliverable's contribution to structural staleness detection is the citable
blob identity of the index it reads and the join evidence other derivations use.
This contract states it no more strongly than that, and `AC-017` puts the
qualification before the review gate.

- **CLM-001** — The accepted `ScopeLedger.csv` row for `SOW-096` reads in full (columns `ScopeItemID,InOutStatus,ScopeItemStatement,SourceRef,PackageID,DeliverableIDs,ObjectiveIDs,DecisionRef,OpenIssue,Notes`):

> ``SOW-096,IN,"Parse deliverable `MEMORY.md` run-index entries (run-ID tokens, dates, link targets) in the template `## Runs` table, the observed bullet form and the dated-heading form, as RunRecord join evidence","PEC-RCN-002 (PRD v2.3), §7.1 RunRecord",PKG-02,DEL-02-09,OBJ-001;OBJ-002,SCA-005,FALSE,"New feed kind under SCA-005 (DL-4, DL-20); absence is a stated coverage limit (SOW-009); objectives per the DL-17 parser precedent"``

- **CLM-002** — The ledger `SourceRef` resolves to two PRD v2.3 loci. `PEC-RCN-002` (§9.2) opens "The reconciler shall ingest, per the closed, PEC-versioned feed profile declared on each loop-registry row (§16.3; PEC's reading hypothesis, never the loop's truth), at minimum:" and its run-evidence clause reads "run evidence — deliverable `MEMORY.md` run-index entries as RunRecord join evidence, with `STATUS.json` / `RUNTIME_SUMMARY.json` as declared historical grammar or current evidence per profile". The §7.1 record-tier row "RunRecord" states the entity's purpose:

> Summaries of checkout-contained AgentRun evidence, joined on the declared
> run-identity token from central receipts, work graphs and the deliverable
> `MEMORY.md` run index; `STATUS.json` / `RUNTIME_SUMMARY.json` under
> `execution/**` are read as declared historical grammar or current evidence
> per the loop's feed profile; application-owned Runtime service user-data is
> operational and non-authoritative (D-GOV-20 item 5; D-GOV-43 A2), is never
> an input, and is never record-tier citable

- **CLM-003** — The objective statements this deliverable serves are `OBJ-001` "Orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation" (§3, `SourceRef` §3.1) and `OBJ-002` "Staleness is detected structurally by SHA comparison, never by judgment" (§3, `SourceRef` §3.2). Both attributions are indirect through the record tier per the warrant above.

## Deliverable Definition — Ontology

`DEL-02-09` is typed `BACKEND_FEATURE_SLICE` at Context Envelope **`S`** with
`PhaseHint` `P1`. Its `AnticipatedArtifacts` field is "Parser + fixture tests
(table, bullet and dated-heading forms)", and the two outputs below are that
list and nothing beyond it.

- **OUT-001** — A MEMORY run-index parser in the PEC service core: it reads deliverable `MEMORY.md` files where the loop's registered feed profile declares the run index, recognizes run-index entries in the template `## Runs` table form, the bullet form and the dated-heading form under declared grammars, and emits content-minimal RunRecord join evidence — run-ID tokens, dates and link targets — together with an explicit statement of every entry field, file or deliverable it could not cover.
- **OUT-002** — A fixture test suite covering the three entry forms, built from golden-by-reference fixtures of the SCA-005 fixture classes and synthetic fixtures where the corpus holds no instance, implementing the verification methods declared in this contract.

### Identity of record

- **CLM-004** — `DEL-02-09` is named "MEMORY run-index parser", Type `BACKEND_FEATURE_SLICE`, Context Envelope `S`, `PhaseHint` `P1`, `ResponsibleParty` `TBD`, `CoversScopeItems` `SOW-096`, `SupportsObjectives` `OBJ-001;OBJ-002`, with empty `ContextEnvelopeNotes`; sources `execution/_Decomposition/Deliverables.csv` row `DEL-02-09` and `SOFTWARE_DECOMP.md` §5 PKG-02 table ("| DEL-02-09 | MEMORY run-index parser | BACKEND_FEATURE_SLICE | S | P1 | SOW-096 |"). `ContextBudgetQA.csv` rates it `LOW` risk with `RecommendedAction` "None", and decomposition §8 records "DEL-02-09 (MEMORY run-index parser) is S, LOW". The folder was created under `D-PEC-93` on 2026-09-25, and its `_STATUS.md` reads `OPEN`.
- **CLM-005** — The register `Description` of record is: "Parser for deliverable `MEMORY.md` run-index entries (run-ID tokens, dates, link targets) in the template `## Runs` table, the observed bullet form and the dated-heading form, as RunRecord join evidence; absence is a stated coverage limit; run descriptions are never extracted." Four terms are carried as written and not strengthened: the extraction set is **run-ID tokens, dates, link targets**; all **three forms** are in scope; the output is **join evidence**, not a RunRecord; and **absence is a stated coverage limit** while **run descriptions are never extracted**.

### Placement in the work graph

- **CLM-006** — `Dependencies.csv` holds three rows. `DEP-02-09-001` and `DEP-02-09-002` are `ANCHOR` rows (package-local to `PKG-02`; the `SOW-096` requirement trace). `DEP-02-09-003` is the single `EXECUTION` upstream edge: predecessor `DEL-01-01` "Record-tier schema & entity model", `DependencyType` `PREREQUISITE`, `Statement` "Parser emits RunRecord join evidence from the MEMORY run index", `Explicitness` `IMPLICIT`, `RequiredMaturity` `INITIALIZED`, `SatisfactionStatus` `PENDING`, `Confidence` `MEDIUM`, `Origin` `EXTRACTED`, `Status` `ACTIVE`, `Notes` "PROPOSAL; Flag=none; EdgeID=E-P80; seeded under D-PEC-93 (SCA-005 B3)". `_DEPENDENCIES.md` records one informational downstream consumer: `DEL-03-01` "Full-rebuild reconciler (one command)" via `[E-P82]`, whose row `DEP-03-01-016` lives in that consumer's register (`Statement` "Full rebuild ingests the MEMORY run index", `RequiredMaturity` `INITIALIZED`). Neither register holds an edge between this deliverable and `DEL-01-06` or `DEL-02-08`.
- **CLM-007** — `DEL-01-01` is at lifecycle `INITIALIZED`, the maturity `[E-P80]` requires, but its accepted contract (SHA-256 `43f1f57a13bb…0170`) predates SCA-005. In it, RunRecord admits "only summaries of checkout-contained AgentRun evidence (`STATUS.json`, `RUNTIME_SUMMARY.json` under `execution/**`)" (quoted as `DEL-01-01/REQ-006`), while the revision-1.5 register row for `DEL-01-01` says "RunRecord is sourced from central receipts, work graphs and the MEMORY run index, with JSON run evidence historical". SCA-005 `Propagation_Plan.md` §B4 classes that contract `STALE_REBUILD_REQUIRED`, and the undertaking graph schedules its rebuild as node S2 (CON-001).
- **CLM-008** — Discovery follows the loop's declared feed profile (CLM-002). At `53145aaeb`, `DEL-01-06` is `INITIALIZED`, its accepted contract (SHA-256 `5fdcfd968345…a2fa8`) requires a strict version-1 registry with no feed profile, and SCA-005 §B4 classes it `STALE_REBUILD_REQUIRED … gated on B6`. The B6 registry source packet is `D-PEC-96`. Its revision 4 (SHA-256 `4506597b1bfd…180e`, merged to `origin/main` at `6281273fa`) has the closed vocabulary `shared-dev-loop`, `loop-receipts-ledger` and `agentruns-json`, each at version 1, with no profile or surface that reads `## Remaining` sections; its `shared-dev-loop` profile covers, among other surfaces, a `memory-run-index` surface. At `53145aaeb` its decision-register row reads `RULED A / EFFECTIVE ON MERGE`, with the owner's ruling recorded in `D-PEC-96_RULING_2026-09-26.md` (merged at `f90320c1d`). The registry act it authorizes is not applied at that commit: `v2/config/loops.json` still carries `"schema_version": 1` and no feed profile, and the `DEL-01-06` contract is not rebuilt. This contract relies on none of the proposal's identifiers (CON-002, TBD-003).
- **CLM-009** — Phase staging, checked against the `PhaseHint` column of `Deliverables.csv` for every deliverable this contract names in its own voice: `DEL-02-09`, `DEL-01-01`, `DEL-01-03`, `DEL-01-05`, `DEL-01-06`, `DEL-02-01` through `DEL-02-08`, `DEL-03-01`, `DEL-03-02`, `DEL-03-03`, `DEL-04-01`, `DEL-04-03`, `DEL-04-05`, `DEL-10-02` and `DEL-10-10` all carry `P1`. No claim here stages any of them differently, and the sole upstream edge runs from a `P1` deliverable.

### Boundaries

- **CLM-010** — The feed split is decision-log entry `DL-4` ("one per feed kind"), extended by `DL-20`, which added `SOW-095` and `SOW-096` as new feed kinds. The adjacent grammars belong to siblings: `_STATUS.md` to `DEL-02-01` (`SOW-011`); decision registers and packets to `DEL-02-02` (`SOW-012`); ledgers and central `RECEIPT.md` receipts to `DEL-02-03` (`SOW-013`); `STATUS.json` and `RUNTIME_SUMMARY.json` to `DEL-02-04` (`SOW-014`); `Dependencies.csv` and historical `WORK_GRAPH.json` to `DEL-02-05` (`SOW-015`); `LOOP_INIT.md` identity and workplans to `DEL-02-06` (`SOW-016`); `_harness/adapter.yaml` to `DEL-02-07` (`SOW-017`); and undertaking work graphs, including their declared run identity, to `DEL-02-08` (`SOW-095`). The acts that consume this parser's output are owned elsewhere and are cited, never discharged: the RunRecord type is `DEL-01-01` (`SOW-001`); full rebuild of the record tier, which ingests this feed through `[E-P82]`, is `DEL-03-01` (`SOW-010`, `SOW-021`); incremental reconcile is `DEL-03-02` (`SOW-018`); drift classification is `DEL-03-03` (`SOW-019`); orientation that surfaces runs is `DEL-04-01` (`SOW-004`); freshness stamping and per-claim citation are `DEL-04-03` (`SOW-006`, `SOW-007`); rendering a limitation into a response is `DEL-04-05` (`SOW-009`); the ingest-boundary guard is `DEL-01-03` (`SOW-056`); zero-dependency and locality enforcement is `DEL-01-05` (`SOW-052`, `SOW-053`); the loop registry is `DEL-01-06` (`SOW-077`, `SOW-094`); directed self-ingest validation is `DEL-10-10` (`SOW-064`); and the kill test is `DEL-10-02` (`SOW-055`).
- **CLM-011** — The `PKG-02` charter (decomposition §4) is "Read-side grammars over governed files: … Markdown work graphs, the MEMORY run index and `LOOP_INIT.md` identity as first-class feeds; …", with "Writing anything; interpretation beyond declared grammars" recorded as out of package scope. Both exclusions bind this deliverable directly.
- **CLM-012** — The shared method surface is `docs/templates/MEMORY_TEMPLATE.md` (SHA-256 `5a9564f4663b…6a5a` at both `c9e5cd87d` and `53145aaeb`). It describes the file as a "Terse deliverable-local index of runs" and says: "This is not a future-work list or another decision register. Preserve existing historical entries." Its `## Runs` section is a table with columns "Run ID / date | Work in this deliverable | Result and source links". `projects/pec/AGENTS.md` (under `D-PEC-94`) says `MEMORY.md` "indexes what each run did in this deliverable" and that "memory carries no future assignments"; the `construct-local-work-graph` method has each undertaking write terse MEMORY entries at closeout that point to its central receipt, keyed by the graph's stable run identity. The SCA-005 feed-model design note classes the run index as a "Derivative index", not authority.
- **CLM-013** — The fixture strategy is SCA-005 `Propagation_Plan.md` §B7, accepted at checkpoint 2, which places it "inside the DEL-02-08/09 and DEL-02-03 SOWs". In its words:

> Golden-by-reference `(commit, path, blob)` fixtures pinned at `d61981ee2`,
> content-minimal goldens, nothing copied into PEC's tree: FC-1 receipt present
> (Piping `PIPING_LINTER_SCOPE_20260923`), FC-2 evidence-only (Piping
> `PIP-DEC025-BASELINE-2026-09-23`), FC-3 no AgentRuns record (App
> `APP-REPLAY-BOUNDARY-2026-09-23`), FX-PEC-0 PEC self-ingest
> (`remaining-loop`), and synthetic grammar-edge fixtures authored under a v2
> packet (Impact Assessment §9.3; Q5 (a)).
>
> (SCA-005 `Propagation_Plan.md` §B7.)

  Impact Assessment §9.3 names the MEMORY forms the classes exercise: FC-2 "dated-heading MEMORY; partial coverage" and FC-3 "bullet `## Runs`". Observed at `d61981ee2`: exactly four deliverable `MEMORY.md` files carry a `## Runs` section, all in bullet form — App `DEL-05-04` (the FC-3 trial) and Piping `DEL-08-01`, `DEL-08-05` and `DEL-10-04` (the FC-1 trial). The undertaking graph routes the fixture suites themselves to node X1 under a later v2 packet. This contract takes no FX-PEC-0 output and no Remaining-reading fixture; the ruled revision-4 vocabulary drops `remaining-loop` (CLM-008).
- **CLM-014** — SCA-005 `Propagation_Plan.md` §B4 records a carry-forward for the parser contracts:

> Carry-forward for the parser SOWs (DEL-02-01, DEL-02-08, DEL-02-09): the
> DEL-01-03 content-minimal guard admits only `OPEN`..`ISSUED` as STATE values
> (true before and after D-PEC-87/89/91), so `RETIRED`, graph node states and
> run tokens are CON-001 cases those SOWs must address.

  ID-shaped text inside this quotation is upstream source context, not a local definition or reference; the constraint it cites is `DEL-01-03/CON-001`. The produced but unaccepted guard source (`v2/src/pec_v2/core/content_minimal_guard.py`, SHA-256 `740a4a741221…19ee9`; `DEL-01-03` is `IN_PROGRESS`) admits five field classes — path, count, SHA, state and hash — and no identifier or date class.
- **CLM-015** — The deliverable is at lifecycle `OPEN` with no implementation present. Every requirement, acceptance criterion and verification method below states a contract on future production; none asserts that anything has been built.
- **CLM-016** — Observed corpus condition, recorded as observation and not as specification. At `origin/main` `7a00a88df` there are 156 deliverable `MEMORY.md` files: 54 App, 101 Piping and 1 PEC. None uses the template `## Runs` table. Four carry a bullet-form `## Runs` section (App 1, Piping 3); each bullet opens with a date, an em dash and a backticked run token, followed by description prose and Markdown links. 145 carry dated level-two headings without a `## Runs` section (App 46, Piping 98, PEC 1), and 7 App files carry neither. Dated headings vary: `## 2026-09-08 — D-PEC-85 P-A production start` in PEC's `DEL-01-03`, `## Current applicability — 2026-09-22 record reconciliation` in App files. Heading text carries decision identifiers and parenthesized run tokens such as `(P1_STORE_GUARD_02)`, with no declared token position. The four `## Runs` files also keep earlier dated sections. SCA-005 risk R-08 records the same shape at its basis: "0 template tables; bullet and dated-heading forms observed". None of this is a grammar, and no rule is derived from it here.
- **CLM-017** — `## Remaining` sections are outside this feed. PRD v2.3 §7.1 states, for the Package/Deliverable census from `_STATUS.md`, that "remaining items is a per-loop optional field, read only where the loop's feed profile declares it"; that field is `_STATUS.md` content, whose grammar is `DEL-02-01`'s (CLM-010), and it is not a MEMORY run-index surface. This deliverable reads no `## Remaining` section of any file, and its reading depends on no feed profile or surface that reads one; the ruled revision-4 vocabulary of CLM-008 contains none.

- **TBD-001** — `ResponsibleParty` is unassigned; the register records `TBD`, with assignment at WORKING_ITEMS activation.
- **TBD-002** — The exact grammars of the three forms — row, bullet and heading recognition, the date formats accepted, the token shape of a run identifier, and which link syntaxes yield link targets — are fixed by no accepted source beyond CLM-001 and the template of CLM-012. They are chosen during production within REQ-002 through REQ-005 and recorded in the grammar declaration of REQ-002.
- **TBD-003** — The feed-profile identifier, version and surface name under which a loop declares its MEMORY run index are fixed by no accepted contract at `53145aaeb`: `D-PEC-96` is ruled, but its registry act is not applied and the `DEL-01-06` contract is not rebuilt, and they arrive with that rebuild. The revision-4 identifiers named in CLM-008 are not relied on.
- **TBD-004** — The folder pattern that locates deliverable `MEMORY.md` files (for example `execution/PKG-*/1_Working/DEL-*/`, and whether `2_Checking` or `3_Issued` folders are included) is not fixed by an accepted source for this feed.
- **TBD-005** — How a file that carries both a `## Runs` section and earlier dated sections is read — whether its dated sections are run-index entries or preserved historical records outside the index — is not fixed.
- **TBD-006** — Which deliverable performs the RunRecord join on the declared run-identity token is not assigned by an accepted source beyond `DEL-01-01`'s typing and `DEL-03-01`'s consumption edge; this deliverable supplies join evidence and performs no join (REQ-006).
- **TBD-007** — The exact MEMORY blobs pinned for each fixture class, the golden-record format, and the length threshold for the no-source-text assertion are fixed when the fixture suites are authored under their own packet.

## Completion and Reliance Basis — Epistemology

The requirements below state what future production must satisfy. Nothing in
this section asserts that a parser, a grammar declaration, a fixture or a test
exists.

- **REQ-001** — The parser shall read deliverable `MEMORY.md` files only within a loop whose registered feed profile declares the MEMORY run-index surface, reading that declaration through the loop-registry port of `DEL-01-06`. Where no declaration is available, the parser shall read nothing for that loop and shall report the absence of a declaration; it shall never infer one from the presence of files. For a declared loop, a deliverable with no `MEMORY.md`, or with a `MEMORY.md` that holds no recognizable run-index entry, shall be reported as a stated coverage limit for that deliverable, never as nonconformance, per the `SOW-096` Notes cell. Reading shall depend on no feed profile or surface that reads `## Remaining` sections (CLM-017).
- **REQ-002** — The parser shall recognize run-index entries under three declared grammars — the template `## Runs` table, the bullet form under `## Runs`, and the dated-heading form — each carrying an identifier and version and naming every construct it reads. Every emitted entry shall name the form and grammar under which it was read. No construct outside a declared grammar shall influence the output, per the `PKG-02` out-of-scope line "interpretation beyond declared grammars" (CLM-011).
- **REQ-003** — The parser shall extract exactly run-ID tokens, dates and link targets per entry, the three fields `SOW-096` names, and no other field. Link targets shall be emitted as normalized repository-relative paths or as PR numbers, never with their link text, and an external URL shall never be followed.
- **REQ-004** — A run-ID token shall be emitted only where the entry's grammar declares its position. Where an entry's grammar declares no token position, or the token cannot be read, the entry shall be emitted with its date and link targets and an explicit run-ID-unavailable marking; a run identifier shall never be inferred from description or heading prose, from a decision identifier, or from a file or folder name (CON-004).
- **REQ-005** — Dates shall be emitted only in the form the grammar declares and shall never be inferred from commit metadata, file names or surrounding text; an unreadable date shall be marked unavailable.
- **REQ-006** — The output shall be RunRecord join evidence keyed on the extracted run-ID token. The parser shall perform no join with work graphs, central receipts or run-evidence files, shall emit no RunRecord, and shall make no claim that a run happened, completed or produced anything.
- **REQ-007** — Where a file is unreadable, or a `## Runs` section, table row, bullet or heading cannot be read under its grammar, or a file mixes forms in a way the grammars do not declare, the parser shall return an explicit limitation naming the loop, the path and the fault, with a parse outcome of parsed, partial, unparseable or absent. A silently omitted, defaulted or inferred entry or field is prohibited, per `PEC-ORI-006` and `SOW-009`. Rendering the limitation into a response is `DEL-04-05`'s (CLM-010).
- **REQ-008** — No emitted field shall hold run descriptions or other `MEMORY.md` prose: the "Work in this deliverable" and "Result and source links" prose, bullet bodies, heading text other than a declared date or token, and section bodies shall not be expressible anywhere in the output, per `PEC-K-10` and constraint `C6`. Enforcement at the ingest boundary is `DEL-01-03`'s under `SOW-056` (CLM-010); this requirement binds what the parser is able to emit.
- **REQ-009** — Every emitted entry and limitation shall carry provenance sufficient for a per-claim citation — loop, path, blob SHA, examined commit, in-file anchor and grammar identifier — per `PEC-ORI-004`. Attaching citations to a response is `DEL-04-03`'s (CLM-010).
- **REQ-010** — The parser shall create, modify or delete no file, including the `MEMORY.md` files it reads, per `PEC-RCN-004`, `PEC-RCN-006` and the `PKG-02` out-of-scope line "Writing anything". A run index is a derivative index (CLM-012), and a parsed entry is never citable as authority over the index, the run or any decision it points to.
- **REQ-011** — Parsing shall be deterministic: identical file bytes under identical grammar declarations shall yield identical output, including identical limitations and form attributions.
- **REQ-012** — The parser shall shape its join evidence to the record-tier contract of `DEL-01-01` once that contract obliges MEMORY-sourced RunRecord join evidence, shall define no record-tier type of its own, and shall emit no WorkGraph, WorkNode, Receipt, DependencyEdge, DecisionRow or Package/Deliverable entity (CON-001).
- **REQ-013** — The parser shall parse no feed owned by a sibling deliverable and shall perform no act owned by another package. In particular it shall read no work graph or its run identity (`DEL-02-08`), `RECEIPT.md` or ledger (`DEL-02-03`), `STATUS.json` or `RUNTIME_SUMMARY.json` (`DEL-02-04`), `Dependencies.csv` or `WORK_GRAPH.json` (`DEL-02-05`), `_STATUS.md`, including its `## Remaining` sections (`DEL-02-01`), decision register (`DEL-02-02`), `LOOP_INIT.md` (`DEL-02-06`) or `adapter.yaml` (`DEL-02-07`) as a feed of its own, and it shall perform no rebuild (`DEL-03-01`), drift classification (`DEL-03-03`), orientation (`DEL-04-01`), freshness stamping (`DEL-04-03`), limitation rendering (`DEL-04-05`) or registry maintenance (`DEL-01-06`); each is cited to its owner in CLM-010.
- **REQ-014** — The fixture tests shall cover all three forms. The bullet and dated-heading forms shall be exercised by golden-by-reference fixtures — pinned `(commit, path, blob)` references at `d61981ee2`, read through read-only plumbing, with content-minimal goldens and no source copied into PEC's tree — drawn from the SCA-005 fixture classes FC-1 receipt present, FC-2 evidence-only and FC-3 no AgentRuns record (CLM-013). The template table form, which has no corpus instance (CLM-016), shall be exercised by a synthetic fixture. Synthetic fixtures shall also cover at least an entry with no readable run token, an unreadable date, a file with no run-index entry, a deliverable with no `MEMORY.md`, and a file mixing `## Runs` with dated sections; they shall contain no text copied from another loop's files. Every golden test shall assert that the output holds no run of source text above the threshold of TBD-007.
- **REQ-015** — The parser and its fixtures shall introduce no third-party runtime dependency and no external network egress, per `PEC-SVC-001` and `PEC-SVC-002` (constraints `C7`, `C8`), whose standing enforcement is `DEL-01-05`.
- **REQ-016** — Fixture tests shall implement the verification methods declared in this contract; they shall not define scope, requirements or acceptance criteria.

- **AC-001** — A declared loop's `MEMORY.md` files are read; an undeclared loop yields a no-declaration report and no entries; and a deliverable without `MEMORY.md`, or without any recognizable entry, yields a coverage-limit report rather than an error or a nonconformance finding.
- **AC-002** — The three grammar declarations exist as readable artifacts with identifiers and versions and name every construct read; every entry names its form and grammar; altering an undeclared construct in a fixture changes nothing in the output.
- **AC-003** — Emitted entries carry only run-ID tokens, dates and link targets, and no other field is emitted; link targets are normalized paths or PR numbers without link text; no external URL is dereferenced.
- **AC-004** — Entries whose grammar declares a token position yield that token; a dated heading carrying only decision identifiers or parenthesized prose tokens yields date, links and a run-ID-unavailable marking, and no token is taken from prose, a decision identifier or a path.
- **AC-005** — Dates are emitted only as the grammar reads them; an entry with an unreadable date yields an unavailable marking and no inferred date.
- **AC-006** — The output contains join evidence only: no RunRecord, no joined field from another feed, and no run-outcome claim.
- **AC-007** — Unreadable, unparseable, partial and mixed-form fixtures each yield an explicit limitation naming loop, path and fault with the correct parse outcome, and none yields a result presented as complete.
- **AC-008** — A fixture whose entries, headings and sections carry distinctive prose yields output containing none of it, and no emitted field type can hold prose.
- **AC-009** — For a sample entry from each form, the recorded provenance resolves to the live source by loop, path, blob SHA, examined commit, anchor and grammar identifier.
- **AC-010** — A parser run leaves the fixture corpus byte-identical, and the module contains no write, create or delete call against any source path.
- **AC-011** — Two runs over identical inputs yield identical output, including limitations and form attributions.
- **AC-012** — Reviewed against the record-tier contract in force at review time, the emitted join evidence introduces no field that contract does not oblige and contains no entity of another type; if that contract does not yet oblige MEMORY-sourced join evidence, the review records the open CON-001 condition rather than passing it.
- **AC-013** — The module reads no sibling feed, including no `## Remaining` section, and performs none of the excluded acts of REQ-013.
- **AC-014** — The fixture suite exercises the table form synthetically and the bullet and dated-heading forms by pinned references drawn from FC-1, FC-2 and FC-3, includes the five synthetic edge cases of REQ-014, copies no fixture source into PEC's tree, and asserts the no-source-text run check.
- **AC-015** — The parser and its fixtures add no third-party runtime dependency and make no network call, leaving the `DEL-01-05` assertion intact.
- **AC-016** — The fixture test suite implements VER-001 through VER-015, executes in the `PKG-02` test run, passes, and introduces no acceptance criterion absent from this contract.
- **AC-017** — The review gate confirms this contract's traceability to `SOW-096`, `OBJ-001` and `OBJ-002` as entered under `DL-20`, confirms the indirect and thin `OBJ-002` leg is stated no more strongly than the §3 mapping note and the warrant above state it, and confirms no sibling feed grammar, `PKG-01` type or registry scope, or `PKG-03`/`PKG-04` derivation has been absorbed.

- **CON-001** — **Upstream typing.** The revision-1.5 register and PRD v2.3 §7.1 source RunRecord from central receipts, work graphs and the MEMORY run index, but the accepted `DEL-01-01` contract admits only JSON run-evidence summaries into RunRecord (CLM-007). This contract defines no type (REQ-012) and does not treat the register row as the upstream contract. Whether OUT-001 production waits for the `DEL-01-01` rebuild (graph node S2) or proceeds against the register text is an ordering decision for the undertaking graph and its owner.
- **CON-002** — **Discovery basis.** Reading per the declared feed profile needs a registry that declares profiles, but the accepted `DEL-01-06` contract is strict version-1 without them, and at `53145aaeb` the ruled `D-PEC-96` is not yet applied (CLM-008). No dependency row links this deliverable to `DEL-01-06`. This contract fixes the behaviour without a declaration — nothing is read and the absence is reported (REQ-001) — and adopts no proposed identifier (TBD-003). Whether an execution edge to `DEL-01-06` should be recorded is a dependency-register question for its owning workflow.
- **CON-003** — **Guard admission.** Run-ID tokens and dates are neither lifecycle states nor any of the five admitted field classes (CLM-014). These are `DEL-01-03/CON-001` cases. This parser shall not coerce a run token or a date into another field class, encode it to pass the guard, or widen the guard; how the store admits them is decided under `DEL-01-03` and `DEL-01-01`, through their own packets.
- **CON-004** — **Run tokens in the dated-heading form.** `SOW-096` places run-ID tokens in scope for the dated-heading form, but the observed headings mix dates, decision identifiers, parenthesized run tokens and prose with no declared token position (CLM-016), and the same text is description the scope item says is never extracted. This contract resolves the tension conservatively: a token is emitted only where a declared grammar fixes its position, and otherwise the entry is emitted without one and marked (REQ-004). Declaring a token position for dated headings that the corpus does not itself declare, or treating decision identifiers as run identifiers, would be a scope or method decision, not a production choice.

## Production and Verification Method — Praxeology

Production proceeds in the order grammar declarations → discovery and coverage
reporting → extraction → limitation reporting → fixtures and tests. Each stage
is the acceptance surface of the next, and a grammar declared before code
exists cannot have been fitted to whatever the code accepted. All work is
bounded to this deliverable folder, the `PKG-02` service-core source and the
fixture paths a ruled packet names; this contract authorizes no register,
decomposition, PRD, registry, template or upstream-deliverable edit, and no v2
source write by itself. Tests implement the verification methods below and
create no scope.

- **VER-001** — Execute over a fixture tree with a declared loop, an undeclared loop, a deliverable without `MEMORY.md` and a `MEMORY.md` with no entries; assert reading, the no-declaration report and the two coverage-limit reports respectively.
- **VER-002** — Inspect the three grammar declarations for identifier, version and construct coverage; compare constructs actually read against them; assert every entry's form attribution; mutate an undeclared construct and assert output invariance.
- **VER-003** — Execute over fixtures of each form carrying relative links with link text, PR links and external URLs, with network access denied; assert the emitted field set, normalized targets without link text, and no dereference.
- **VER-004** — Execute over bullet and table fixtures with declared token positions and over dated-heading fixtures whose headings carry only decision identifiers or parenthesized tokens; assert the token where declared and the unavailable marking otherwise, with no token drawn from prose, identifiers or paths.
- **VER-005** — Execute over entries with readable and unreadable dates; assert declared-form dates and the unavailable marking, with no inferred date.
- **VER-006** — Inspect the output schema and a sample output for RunRecord entities, fields joined from other feeds and run-outcome claims, asserting none.
- **VER-007** — Execute over unreadable, unparseable, partial and mixed-form fixtures; assert per case the limitation fields and parse outcome.
- **VER-008** — Execute over a fixture carrying distinctive prose in every prose-bearing position; assert none of it appears in the output; review every emitted field's type for capacity to hold prose.
- **VER-009** — For a sample entry from each form, resolve the recorded provenance to the source and assert each provenance element is present and locatable.
- **VER-010** — Hash the fixture corpus before and after a run and assert byte-identity; inspect the module's call graph for write, create or delete operations against any source path.
- **VER-011** — Run the parser twice over identical inputs and assert identical output.
- **VER-012** — Review the emitted join evidence field by field against the record-tier contract in force at review time, and search the module for any record-tier type definition or other entity emission.
- **VER-013** — Inspect the module's file access for any sibling feed path or `## Remaining` read, and its call surface for any excluded act of REQ-013.
- **VER-014** — Inspect the fixture manifests for the synthetic table fixture, pinned `(commit, path, blob)` references at `d61981ee2` for the bullet and dated-heading forms drawn from FC-1, FC-2 and FC-3, the five synthetic edge cases and the absence of copied sources; resolve each pin by read-only plumbing; run the no-source-text assertion on every golden test.
- **VER-015** — Inspect the `PKG-02` dependency manifest and the module's import graph for third-party runtime dependencies and network calls, and re-run the `DEL-01-05` enforcement once that deliverable is available, without discharging it here.
- **VER-016** — Run the `PKG-02` test suite and confirm that each of VER-001 through VER-015 has a corresponding executing test and that no test asserts a criterion absent from this contract.

## Governing Values and Decisions — Axiology

- **AX-001** — `PEC-K-02` files govern. A run index is a terse derivative account whose authority stays at the central receipt, PR and decision it points to (CLM-012); a parsed entry is never citable as authority over any of them.
- **AX-002** — Absence is information, not failure. Most existing `MEMORY.md` files carry no `## Runs` section (CLM-016), and some deliverables have no `MEMORY.md` at all; reporting a missing index as a stated coverage limit, as the `SOW-096` Notes cell requires, keeps orientation honest without accusing a loop of nonconformance (`PEC-ORI-006`).
- **AX-003** — `PEC-K-10` content-minimal is a residency posture. Run descriptions are the one thing the scope item names as never extracted; for a parser the strongest enforcement is inexpressibility, which is why REQ-008 binds emitted field shapes.
- **AX-004** — A declared identity is not a guess. The join key is the run identity a loop declares; inferring one from prose, a decision number or a folder name would manufacture joins the loop never made, which is why REQ-004 and CON-004 prefer an unavailable marking.
- **AX-005** — A feed profile is PEC's reading hypothesis, never the loop's truth (PRD §16.3). Reading follows the declaration and nothing else (REQ-001, CON-002).
- **AX-006** — `DL-4` and `DL-20` make this deliverable atomic: one feed kind, one separately testable unit. Absorbing the work-graph grammar, the receipt grammar, the RunRecord type or the join would undo it (REQ-006, REQ-013).
- **AX-007** — The edges cited are `[E-P80]` (upstream, `DEL-01-01` → `DEL-02-09`, `PROPOSAL`) and `[E-P82]` (downstream, `DEL-02-09` → `DEL-03-01`, `PROPOSAL`), both seeded under `D-PEC-93`. Stratum is provenance, not authority. `RequiredMaturity` `INITIALIZED` on `[E-P80]` makes the upstream *contract* the reliable input, which is why CON-001 is recorded.
- **AX-008** — Fixtures reference other loops' files by pinned object identity and never copy their prose into PEC's tree, and the goldens are themselves content-minimal (CLM-013).
- **AX-009** — Unknowns stay marked. TBD-001 through TBD-007 and CON-001 through CON-004 are recorded rather than resolved by inference.
- **AX-010** — `C-04` `PHASE_PRECEDENCE` and `C-10` `STRATUM_RULE` are register-wide, non-gating constraints recorded in `_DEPENDENCIES.md`. Blocker output under `FULL_GRAPH` at threshold `INITIALIZED` is advisory visibility only and never work assignment.
- **AX-011** — This contract is lifecycle-neutral. `_STATUS.md` remains the sole lifecycle authority and is untouched by the run that authored this document; the deliverable is at `OPEN` and nothing has been built.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-096 OBJ-001 OBJ-002 | REQ-001, CLM-001, CLM-002, CLM-008, CON-002, TBD-003, TBD-004, AX-002, AX-005 | AC-001 | VER-001 | Transcripts for a declared loop, an undeclared loop, a deliverable without MEMORY.md and a MEMORY.md without entries |
| OUT-001 | SOW-096 OBJ-001 OBJ-002 | REQ-002, CLM-005, CLM-011, CLM-012, TBD-002, TBD-005 | AC-002 | VER-002 | The three grammar declarations, a record of constructs read, form attributions and the invariance result |
| OUT-001 | SOW-096 OBJ-001 OBJ-002 | REQ-003 | AC-003 | VER-003 | Per-form transcripts of the emitted field set with network access denied |
| OUT-001 | SOW-096 OBJ-001 OBJ-002 | REQ-004, CLM-016, CON-004, AX-004 | AC-004 | VER-004 | Token transcripts for declared-position forms and for dated headings without a declared position |
| OUT-001 | SOW-096 OBJ-001 OBJ-002 | REQ-005 | AC-005 | VER-005 | Date transcripts for readable and unreadable dates |
| OUT-001 | SOW-096 OBJ-001 OBJ-002 | REQ-006, TBD-006, AX-006 | AC-006 | VER-006 | Output-schema inspection and a sample output showing join evidence only |
| OUT-001 | SOW-096 OBJ-001 OBJ-002 | REQ-007 | AC-007 | VER-007 | Per-case limitation transcripts with parse outcomes |
| OUT-001 | SOW-096 OBJ-001 OBJ-002 | REQ-008, CON-003, AX-003 | AC-008 | VER-008 | The prose-bearing fixture with its output and a field-type inspection record |
| OUT-001 | SOW-096 OBJ-001 OBJ-002 | REQ-009 | AC-009 | VER-009 | Provenance-resolution records for a sample entry from each form |
| OUT-001 | SOW-096 OBJ-001 OBJ-002 | REQ-010, AX-001 | AC-010 | VER-010 | Before/after corpus hashes and a call-graph inspection record |
| OUT-001 | SOW-096 OBJ-001 OBJ-002 | REQ-011 | AC-011 | VER-011 | Two outputs from repeated runs over identical inputs, compared |
| OUT-001 | SOW-096 OBJ-001 OBJ-002 | REQ-012, CLM-007, CON-001 | AC-012 | VER-012 | A field-by-field review against the record-tier contract in force, and a search record for type definitions and other entities |
| OUT-001 | SOW-096 OBJ-001 OBJ-002 | REQ-013, CLM-010, CLM-017 | AC-013 | VER-013 | File-access and call-surface inspection records |
| OUT-002 | SOW-096 OBJ-001 OBJ-002 | REQ-014, CLM-013, TBD-007, AX-008 | AC-014 | VER-014 | Fixture manifests with the synthetic table fixture, resolved pinned references, the edge-case list and no-source-text results |
| OUT-001 | SOW-096 OBJ-001 OBJ-002 | REQ-015 | AC-015 | VER-015 | Dependency-manifest and import-graph inspection records, plus the DEL-01-05 result once available |
| OUT-002 | SOW-096 OBJ-001 OBJ-002 | REQ-016, CLM-015, TBD-001 | AC-016 | VER-016 | PKG-02 test-run output mapping each executed test to its verification method |
| OUT-001 | SOW-096 OBJ-001 OBJ-002 | CLM-003, CLM-004, CLM-006, CLM-009, CLM-014, AX-007, AX-009, AX-010, AX-011 | AC-017 | HUMAN_REVIEW: review gate confirms traceability to SOW-096 and to OBJ-001/OBJ-002 as entered under DL-20, confirms the indirect and thin OBJ-002 leg is stated no more strongly than the §3 mapping note, and confirms no sibling, PKG-01, registry or PKG-03/PKG-04 scope absorption | Review record citing the ledger row, the §3 mapping note and the sibling and cross-package boundaries |
