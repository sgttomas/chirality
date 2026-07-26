---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-02
package_id: PKG-02
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@3623b958b
project_scope_refs: [SOW-012]
package_objective_refs: [OBJ-001, OBJ-002]
---

# Scope of Work — DEL-02-02 Decision register/packet parser

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-02-02` — "Decision
register/packet parser" — in `PKG-02` File-Truth Parsers of the PEC v2 build.
It covers project scope item `SOW-012` in service of package objectives
`OBJ-001` and `OBJ-002`.

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.2** (`current_basis`, SCA-002 successor; commit `3623b958b`). The
deliverable-local `_REFERENCES.md` still names "revision 1.1, accepted working
surface"; that phrase is superseded provenance left by a deferred pointer sweep
(SCA-002 `Handoff_State.md` §6), and `_CONTEXT.md`'s own provenance line records
revision 1.1 as "superseded by revision 1.2 (`current_basis`, SCA-002
successor)". This contract cites revision 1.2.

**The defining property of this deliverable.** `SOW-012` and the register
description of `DEL-02-02` both state the boundary in their own text: row
identity and status only, *never* row prose. That is not an implementation
preference this contract adopts; it is what the scope item is. It is carried
below as `REQ-003`, `AC-002`, `VER-002`, and `AX-001`, and every other
requirement is written so as not to erode it.

**Objective warrant.** The attribution of this deliverable to `OBJ-001` and
`OBJ-002` is SCA-002-qualified and *indirect*, not register-direct. At revision
1.1 the ledger row for `SOW-012` carried no objective; SCA-002 attributed
`OBJ-001;OBJ-002` to it as one of the seven parser items (`SOW-011..017`) in
the group the amendment package calls the INDIRECT-8, and the attribution was
accepted at revision 1.2. The warrant is the accepted §3 mapping note, which
SCA-002 applied rather than superseded. The Gate 3 record states it this way:

> ### The INDIRECT-8 (`DEL-01-01` + `DEL-02-01..07`) — Q2
>
> §3's mapping notes state a positive derivation: *"parser items (SOW-011..017)
> underlie OBJ-001/OBJ-002 through the record tier (SOW-001)."*
>
> **Recommended — AFFIRM** `[OBJ-001, OBJ-002]` for all eight: it applies the
> accepted §3 rationale rather than superseding it.

Two alternatives were defined precisely and neither was adopted: **N1** (the
seven parsers map to `OBJ-001`; `SOW-001` keeps both) and **N2** (all eight map
to `OBJ-001`). The record also states the evidence for narrowing, verbatim:

> **Evidence for narrowing, stated because it is real:** OBJ-002's register locus
> is the reconciler layer — `SOW-018` (incremental, Git-delta-keyed), `SOW-019`
> (drift classification), `SOW-006` (SHA stamping). The parsers produce facts the
> SHA comparison operates over; they do not perform it. N1 would arguably
> describe the system more precisely than the §3 sentence does.

The owner ruled the question at the SCA-002 Gate 3 in-session gate
(2026-07-25). The Gate 3 ruling table records it in two cells, quoted here by
column — Question: *"INDIRECT-8 breadth"*; Ruling: *"**AFFIRM**
`OBJ-001;OBJ-002` for all eight (not N1, not N2)"*. The table sits under the
heading *"### Gate 3 owner ruling — APPROVED 2026-07-25"*, and the paragraph
immediately above the table reads *"Owner (Ryan Tufts) in-session; relayed by
Agent 0. **Every question ruled as recommended.**"* The attribution is therefore **ruled, not
pending**: this contract creates no owner-confirmation acceptance criterion for
it and supplies no fresh derivation of it. Unlike the per-row attributions
batched into Q1/Q5, the Q2 group carries **no confidence label** in the Gate 3
record, so this contract neither asserts one nor states the warrant more
strongly than the record does. The `OBJ-002` leg rests on the §3 derivation
through the record tier, not on any claim that this deliverable performs SHA
comparison — it does not.

- **CLM-001** — The accepted `ScopeLedger.csv` row for `SOW-012` reads in full, under the header `ScopeItemID,InOutStatus,ScopeItemStatement,SourceRef,PackageID,DeliverableIDs,ObjectiveIDs,DecisionRef,OpenIssue,Notes`:

> ``SOW-012,IN,Parse decision registers and decision packets (row identity and status only — never row prose),"PEC-RCN-002, §7.1",PKG-02,DEL-02-02,OBJ-001;OBJ-002,,FALSE,Content-minimal (C6)``
>
> (`DecisionRef` empty; `OpenIssue` `FALSE`; `Notes` `Content-minimal (C6)`.)

- **CLM-002** — The ledger `SourceRef` names two PRD loci, and both are cited here. The first is `PEC-RCN-002` (PRD §9.2), whose text is:

> The reconciler shall ingest, at minimum: `_STATUS.md` (declared parser
> dialect), decision registers and packets, `LOOP_RECEIPTS.md` (per-loop
> grammar; the D-APP-57 contract where a ledger has adopted it),
> `WORK_GRAPH.json` / `STATUS.json` / `RUNTIME_SUMMARY.json`, dependency
> registers, workplans/LOOP_INIT, and per-project `_harness/adapter.yaml` as
> the feed manifest.

  The second is PRD §7.1, "Record tier (reconciled from file truth; citable with sources)", whose `DecisionRow` row states the entity's purpose:

> Register-row identity and status only (decision ID, packet path, anchor,
> state — never the row's prose; PEC-K-10)

- **CLM-003** — The objective statements this deliverable serves are `OBJ-001` "Orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation" (`SOFTWARE_DECOMP.md` §3, `SourceRef` §3.1; `PRD.md` §3 outcome 1) and `OBJ-002` "Staleness is detected structurally by SHA comparison, never by judgment" (§3, `SourceRef` §3.2; `PRD.md` §3 outcome 2). Both attributions are indirect through the record tier per the warrant above.

## Deliverable Definition — Ontology

- **CLM-004** — `DEL-02-02` is named "Decision register/packet parser", Type `BACKEND_FEATURE_SLICE`, Context Envelope `M`, `PhaseHint` `P1`, `ResponsibleParty` `TBD`, `CoversScopeItems` `SOW-012`, `SupportsObjectives` `OBJ-001;OBJ-002`, with `AnticipatedArtifacts` "Parser + fixture tests" and an **empty** `ContextEnvelopeNotes` cell — there are no envelope notes to carry forward. Sources: `execution/_Decomposition/Deliverables.csv` row `DEL-02-02` and `SOFTWARE_DECOMP.md` §5 `PKG-02` table ("| DEL-02-02 | Decision register/packet parser | BACKEND_FEATURE_SLICE | M | P1 | SOW-012 |"). The register `Description` reads: "Row identity and status extraction from decision registers and packets — never row prose (content-minimal)." The outputs below are that artifact list and nothing beyond it.

- **OUT-001** — A decision register/packet parser in the PEC service core: it reads decision registers and decision packets under a declared grammar and emits, per register row, that row's identity and status — decision ID, packet path, anchor, state — with the provenance needed to cite it, and nothing of the row's prose.
- **OUT-002** — A fixture test suite covering the parser against valid, prose-heavy, heterogeneous, malformed, unreadable, and absent register and packet fixtures, implementing the verification methods declared in this contract.

- **CLM-005** — The seven-way split of `PEC-RCN-002` into `SOW-011..017` is decision-log entry `DL-4` (2026-07-24): "PEC-RCN-002's enumerated feed list is split into seven scope items (SOW-011..017), one per feed kind", because "Each feed is a separately testable parser with its own grammar; a single 'ingest everything' item is not atomic". The other six feed grammars belong to `DEL-02-01` (`_STATUS.md`), `DEL-02-03` (receipts ledgers), `DEL-02-04` (run-evidence JSON), `DEL-02-05` (dependency registers), `DEL-02-06` (workplans/LOOP_INIT), and `DEL-02-07` (the `adapter.yaml` feed manifest). This deliverable defines the decision-feed grammar only, and takes no position on any other feed's grammar.
- **CLM-006** — The `PKG-02` package charter (decomposition §4) is "Read-side grammars over governed files: `_STATUS.md` dialect, decision registers/packets, receipts ledgers, run-evidence JSON, dependency registers, workplans/LOOP_INIT, `adapter.yaml` manifests", with "Writing anything; interpretation beyond declared grammars" recorded as explicitly out of package scope.
- **CLM-007** — This deliverable has exactly one accepted `EXECUTION` upstream edge, `[E-P04]`, held as register row `DEP-02-02-003` of the deliverable-local `Dependencies.csv` (v3.1). Attributing each value to its actual column: `DependencyClass` `EXECUTION`, `Direction` `UPSTREAM`, `DependencyType` `PREREQUISITE`, `TargetType` `DELIVERABLE`, `TargetPackageID` `PKG-01`, `TargetDeliverableID` `DEL-01-01`, `TargetName` "Record-tier schema & entity model", `Statement` "Parser emits DecisionRow entities", `EvidenceFile` `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md`, `SourceRef` and `EvidenceQuote` both "§3 mapping notes (as E-P03)", `Explicitness` `IMPLICIT`, `RequiredMaturity` `INITIALIZED`, `ProposedMaturity` `TBD`, `SatisfactionStatus` `PENDING`, `Confidence` `MEDIUM`, `Origin` `EXTRACTED`, `Status` `ACTIVE`, `Notes` "PROPOSAL; Flag=none; EdgeID=E-P04". The remaining two rows in that register are the `ANCHOR` rows `DEP-02-02-001` (package-local to `PKG-02`) and `DEP-02-02-002` (the `SOW-012` requirement trace).
- **CLM-008** — `DEL-01-01` is at lifecycle state `INITIALIZED`, which is the maturity `[E-P04]` requires. `INITIALIZED` means its **contract** is the reliable input: its accepted `ScopeOfWork.md` exists, and no schema, entity model, or code does. Nothing in this contract asserts that any upstream artifact exists or has been built. The obligations this deliverable's output typing binds to are these, quoted from that contract's Epistemology section:

> - **REQ-001** — The schema and entity model shall define exactly the fourteen
>   record-tier entity types named in CLM-005 — Loop, Workplan, Step, Gate,
>   Receipt, DecisionRow, Fence, Package, Deliverable, DependencyEdge,
>   RunRecord, CandidateBrief, OrientationSnapshot, DriftFinding — with none
>   added and none dropped, and each type shall carry a recorded trace to its
>   `PRD.md` §7.1 row and stated purpose (CLM-006).
> - **REQ-003** — Every record-tier entity type shall carry provenance
>   sufficient for a per-claim citation to its live source — file path, anchor,
>   and/or SHA, per `PEC-ORI-004` — because §7.1 defines the tier as "citable
>   with sources". […]
> - **REQ-007** — No field of any type shall admit file content or diff content
>   (`PEC-K-10`: "Paths, counts, SHAs, states, hashes — never file or diff
>   content"). DecisionRow shall carry register-row identity and status only —
>   decision ID, packet path, anchor, state — and shall have no field capable of
>   holding the row's prose. Enforcement at the ingest boundary is `DEL-01-03`'s
>   guard under `SOW-056`; this requirement binds the shape of the schema so
>   that the guard has nothing to admit into.
>
> (`DEL-01-01/ScopeOfWork.md`; ID-shaped text inside this quotation is upstream
> source context, not a local definition or reference. The bracketed ellipsis
> marks an elision of that requirement's closing sentence, which assigns the
> citation-attaching act to another deliverable.)

  The upstream contract's `AC-006` states the same boundary as an acceptance criterion, including that "a fixture carrying file content, diff hunks, and register-row prose cannot be expressed in the model". The relation is therefore complementary and not duplicative: upstream binds the *shape* of the entity so prose is inexpressible; this deliverable binds the *parse* so prose is never extracted in the first place.
- **CLM-009** — The one declared downstream consumer is `DEL-03-01` (Full-rebuild reconciler (one command)) via `[E-P20]`, whose gate-exhibit evidence reads "PEC-RCN-002 feed list (DL-4)" and whose statement reads "Full rebuild ingests decision registers/packets". That edge is informational here; it lives in the consumer's register and imposes no obligation on this deliverable beyond the outputs declared above.
- **CLM-010** — Phase staging, quantified over the deliverables this contract names in its own voice — that is, outside the quoted upstream text of CLM-008 — and checked against the `PhaseHint` column of `Deliverables.csv`: `DEL-02-02` itself and `DEL-01-01`, `DEL-01-03`, `DEL-01-05`, `DEL-01-06`, `DEL-02-01`, `DEL-02-03`..`DEL-02-07`, `DEL-03-01`, `DEL-04-03`, `DEL-04-05`, `DEL-10-02`, `DEL-10-03` all carry `P1`; `DEL-05-02` and `DEL-09-03` carry `P2`. The CLM-008 quotation additionally names `DEL-01-03`, which is `P1`. No claim in this contract stages any of these deliverables into a different phase, and no deliverable named here as a consumer precedes this deliverable's phase.
- **CLM-011** — Observed corpus condition, recorded as observation and not as specification. Two decision registers exist in this checkout and their grammars differ. `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md` declares itself a "Non-governing tracking surface" that "confers no authority", states a packet-location convention "`execution/_Coordination/_DECISIONS/D-PEC-XX_<slug>.md`" and an explicit row-state vocabulary — "`NOT_PREPARED` -> `AWAITING_RULING` (packet drafted) -> `RULED` (pointer to the human record)" — over a table whose columns are `ID | Decision | Blocks | State | Packet | Ruling record`; 57 `D-PEC-*` packet files sit beside it. `_DomainEngines/_DECISIONS/_REGISTER.md` uses the columns `ID | Decision | My recommendation | HumanRuling | Unblocks`, has no separate state column, and expresses ruling state inside the prose `HumanRuling` cell (for example "**RULED: keep both (7 tokens)**"); 23 `D-T0-*` packet files sit beside it. These files are the corpus the parser will meet; they are not a contract, and the grammar this deliverable declares is a production choice bounded by TBD-002 and CON-002.
- **CLM-012** — The deliverable is at lifecycle state `OPEN` with no implementation present. Every requirement, acceptance criterion, and verification method below states a contract on future production; none asserts that anything has been built.

- **TBD-001** — `ResponsibleParty` is unassigned; the register records `TBD`, with assignment at WORKING_ITEMS activation and not in this contract (`SOFTWARE_DECOMP.md` §5 conventions per `DL-13`; `_CONTEXT.md`).
- **TBD-002** — The decision-feed grammar this parser declares — which register table shapes and packet structures it recognises, how it locates a row, and how it maps a row to the four `PRD.md` §7.1 identity/status elements — is fixed by no accepted source. It is chosen during production within REQ-002, CLM-006, and CON-001.
- **TBD-003** — What constitutes the "anchor" of a decision row is named by `PRD.md` §7.1 and `PEC-ORI-004` but is not defined by any accepted source at the level of a concrete locator. Its concrete form is a production choice within REQ-005.
- **TBD-004** — Which decision registers and packets are read, and for which loop or project, is not settled by this contract: the feed manifest is `DEL-02-07`'s under `SOW-017` and the loop registry is `DEL-01-06`'s under `SOW-094`. This deliverable parses the files it is given and enumerates no corpus of its own.

## Completion and Reliance Basis — Epistemology

The requirements below state what future production must satisfy. Nothing in
this section asserts that a parser, a fixture, or a test exists.

- **REQ-001** — The parser shall read decision registers and decision packets and shall emit, per register row, the four identity and status elements `PRD.md` §7.1 names for the `DecisionRow` entity: decision ID, packet path, anchor, and state (CLM-002).
- **REQ-002** — The parser shall document the decision-feed grammar it consumes — every register shape, packet structure, and field it reads, and that field's semantics — and shall let no undeclared field influence its output, per the `PKG-02` out-of-scope line "interpretation beyond declared grammars" (CLM-006).
- **REQ-003** — The parser shall carry no register-row prose and no packet prose into its output or into the record tier. This includes, and is not limited to, decision statements, rationale, recommendation text, ruling narrative, and any other authored sentence of a register row or packet body. What it may carry is identity, status, locators, and hashes — "Paths, counts, SHAs, states, hashes — never file or diff content" (`PEC-K-10`; constraint `C6`; ledger note "Content-minimal (C6)"; `SOW-012`'s own "never row prose"; `PRD.md` §7.1's "never the row's prose"). Where a row's state is only expressible as authored text, the parser shall emit a declared status token or an explicit limitation under REQ-006, never the text itself.
- **REQ-004** — The parser shall emit `DecisionRow` entities as the upstream record-tier entity model defines them (CLM-008), depending on that model rather than on a parser-local record shape, and shall define no record-tier entity type of its own.
- **REQ-005** — Every emitted row shall carry provenance sufficient for a per-claim citation to its live source — file path, anchor, and/or SHA, per `PEC-ORI-004` and `PRD.md` §7.1's "citable with sources" — and shall be fully regenerable from those sources, per `PEC-K-02` and `PEC-RCN-001`. Attaching citations to an orientation response is `DEL-04-03`'s act under `SOW-007`, and running the rebuild is `DEL-03-01`'s under `SOW-010`; this requirement obliges the parser to produce what those acts need, and no more.
- **REQ-006** — Where a register or packet is absent, unreadable, malformed, or outside the declared grammar, the parser shall report that condition explicitly to its caller, naming the file and the fault; silent omission, a silently partial row set, and a guessed state are all prohibited (`PEC-ORI-006`: "Where a feed is unparseable or stale, the response shall state the measurement limitation explicitly; silent omission is prohibited"). Rendering such a limitation into a response is `SOW-009` / `DEL-04-05` scope; this deliverable makes the limitation available to that consumer.
- **REQ-007** — The parser shall create, modify, or delete no source file, including the registers and packets it reads, per `PEC-RCN-004` ("it shall never modify a source file"), `PEC-RCN-006` ("The reconciler writes only its own store and generated views"), and the `PKG-02` out-of-scope line "Writing anything".
- **REQ-008** — The parser and its fixtures shall introduce no third-party runtime dependency and no external network egress, per `PEC-SVC-001` and `PEC-SVC-002`, whose standing enforcement is `DEL-01-05` covering `SOW-052` and `SOW-053`.
- **REQ-009** — The parser shall operate over decision registers as they exist today — prose-structured, parsed best-effort — and shall not require any register to gain structure at source. Neither shall its design foreclose consuming such structure if the owner later rules for it. Parser depth is the exact subject of open issue `OI-001` / `SOW-075` (CON-001), and constraint `C12` requires that affected work be "fenced or flagged, never guessed".
- **REQ-010** — Tests shall implement the verification methods declared in this contract; they shall not define scope, requirements, or acceptance criteria.

- **AC-001** — The parser reads a valid register fixture and a valid packet fixture and yields, per row, exactly the decision ID, packet path, anchor, and state that the fixture declares; every field it reads appears in the documented grammar, and altering an undeclared field in the fixture changes nothing in its output.
- **AC-002** — For a fixture whose `Decision`, rationale, recommendation, and ruling-narrative cells carry distinctive prose strings, no such string — and no substring of one beyond a declared status token, identifier, or locator — appears anywhere in the parser's emitted payload; and the parser exposes no field capable of holding a row's prose.
- **AC-003** — The emitted records are instances of the upstream `DecisionRow` entity type; the module defines no record-tier entity type of its own; and no parser-local record shape substitutes for the upstream model.
- **AC-004** — For a sample of emitted rows, the recorded provenance resolves to the live source by path, anchor, and/or SHA, and a re-run over unchanged sources reproduces every emitted row identically.
- **AC-005** — For absent, unreadable, malformed, and out-of-grammar register and packet fixtures, the parser returns an explicit limitation naming the file and the fault, and never a silently empty row set, a silently partial row set, or a guessed state.
- **AC-006** — A parser run over a fixture corpus leaves that corpus byte-identical, and the module contains no write, create, or delete call against any source path.
- **AC-007** — The parser and its fixtures add no third-party runtime dependency and make no network call, leaving the `DEL-01-05` zero-dependency and locality assertion intact.
- **AC-008** — The parser produces its declared output over a today-shaped prose-structured register fixture with no structural aids, and the recorded design shows that adding machine-parse structure at source would be a grammar extension rather than a rewrite; nothing in the delivered work presupposes either `OI-001` outcome.
- **AC-009** — The fixture test suite implements VER-001 through VER-008, executes in the `PKG-02` test run, passes, and introduces no acceptance criterion absent from this contract.
- **AC-010** — The REVIEW gate confirms this contract's traceability to `SOW-012`, `OBJ-001`, and `OBJ-002` as ruled at SCA-002 Gate 3 Q2, confirms that the indirect `OBJ-002` leg is stated no more strongly here than the Gate 3 record states it — including the recorded and unadopted N1 narrowing evidence — and confirms that no `PKG-01`, sibling `PKG-02`, `PKG-03`, `PKG-04`, `PKG-05`, `PKG-09`, or `PKG-10` scope has been absorbed.

- **CON-001** — Parser depth is an undecided owner question and this deliverable is the only work it touches. `PRD.md` §16.1 asks "Whether decision registers gain light structure at source (machine-parse aids) or remain prose parsed best-effort"; the decomposition carries it as TBD item `SOW-075` and open issue `OI-001`, dispositioned "§16 ruling", with the `SOW-075` note recording the assessment "Assessed (not PRD-stated): affects SOW-012 parser depth only; both paths buildable". `SOW-012`'s own `OpenIssue` cell reads `FALSE` (CLM-001), as every parser row's does; that cell is not this contract's warrant for the assessment, and neither fact is offered as the cause of the other. What the assessment states is that the scope item is buildable under either outcome — which is not the same as its being free of the question. REQ-009 binds production to the both-paths posture. Nothing in this contract resolves `OI-001`, and no production choice made here may be read as settling it.
- **CON-002** — The accepted sources name "decision registers and packets" as a feed but define no grammar for them, and the observed corpus is heterogeneous in exactly the way that matters: one register carries an explicit `State` column with a declared vocabulary, the other carries ruling state only inside a prose cell (CLM-011). Extracting status from the second without extracting its prose is the substantive difficulty of this deliverable, and no accepted source states how far a declared grammar must reach to cover it. This contract records the gap as TBD-002 and REQ-003's closing sentence rather than choosing a coverage boundary; if production requires a resolution that is not derivable from an accepted source, that is a scope-change question, not a production decision.

## Production and Verification Method — Praxeology

Production proceeds in the order declared grammar → row identity and status
extraction → content-minimal boundary → limitation reporting → fixtures and
tests, because each stage is the acceptance surface of the next. The
content-minimal boundary is designed into the extraction step rather than
filtered afterwards, so that REQ-003 is satisfied by construction and not
audited into place. All work is bounded to this deliverable folder and the
`PKG-02` service-core source it names; this contract authorizes no register,
decomposition, PRD, or upstream-deliverable edit, and it neither defines nor
reshapes the record-tier entity model it emits into.

- **VER-001** — Execute the parser over valid register and packet fixtures and assert, per row, that the emitted decision ID, packet path, anchor, and state equal the fixture's declared expectation; then compare the set of fields actually read, by instrumentation or code inspection, against the documented grammar, and mutate an undeclared field to assert output invariance.
- **VER-002** — Content-minimal assertion: build a fixture whose prose cells carry unique sentinel strings, run the parser, and search the entire emitted payload for each sentinel and for prose-length substrings of it, asserting none is present; then inspect the emitted record's field inventory for any field typed to hold free text beyond a declared status token, identifier, or locator.
- **VER-003** — Type-binding inspection: assert that emitted records are instances of the upstream `DecisionRow` entity type, and inspect the module for any locally defined record-tier entity type or parallel record shape, asserting none exists.
- **VER-004** — Provenance and regenerability check: for a sample of emitted rows, resolve the recorded provenance to the live source by path, anchor, and/or SHA; then re-run the parser over unchanged sources and assert row-for-row identity of the output.
- **VER-005** — Execute the parser against absent, unreadable, malformed, and out-of-grammar register and packet fixtures and assert, per case, an explicit limitation naming the file and the fault, with no empty, partial, or guessed row set returned in its place.
- **VER-006** — Hash the fixture corpus tree before and after a parser run and assert byte-identity; inspect the module's call graph for write, create, or delete operations against any source path.
- **VER-007** — Inspect the `PKG-02` dependency manifest and this module's import graph for third-party runtime dependencies and network calls, and re-run the `DEL-01-05` zero-dependency and locality enforcement once that deliverable is available, without discharging it here.
- **VER-008** — Both-paths exercise: run the parser over a prose-structured register fixture shaped as the corpus is today and assert the declared output; then review the declared grammar and the module's extension surface against a hypothetical structured-at-source variant and record whether accommodating it is a grammar extension or a rewrite. The exercise selects no `OI-001` outcome and produces no recommendation on one.
- **VER-009** — Run the `PKG-02` test suite and confirm that each of VER-001 through VER-008 has a corresponding executing automated test and that no test asserts a criterion absent from this contract.

## Governing Values and Decisions — Axiology

- **AX-001** — `PEC-K-10` content-minimal and constraint `C6` are the reason this deliverable exists in the shape it does. A decision register is almost entirely authored prose; a parser over it is one keystroke away from becoming a content pump. The posture is therefore stated as a property of the parse — what is never extracted — rather than as a filter applied to a richer intermediate, and the strongest available form is a record with nowhere to put prose. The complementary schema-side inexpressibility is the upstream model's (CLM-008) and the ingest-boundary guard is `DEL-01-03`'s under `SOW-056`; neither is discharged here.
- **AX-002** — `PEC-K-02` files govern: the decision register and its packets are authored project truth. The `PKG-02` charter allows reading them and forbids writing anything, and the PEC register's own header records that it "confers no authority". PEC's projection of a row is never citable over the row itself, and no output of this parser is a ruling, an adoption, or a direction. `PEC-GAT-004` ("PEC shall provide no write path that records adoption, ruling, or direction") and `PEC-DSH-003`'s "link-only, source-linked (no restatement of authored text; PEC-K-10)" are the same discipline enforced at surfaces other deliverables own.
- **AX-003** — `PEC-K-01` graceful absence governs: no governed act may require a PEC read or write. A register PEC cannot parse is a stated coverage limitation (REQ-006), never a blocked act and never a silent gap; `PEC-K-07` makes reconciliation the guaranteed path and puts the honesty obligation on coverage, not on completeness of parse.
- **AX-004** — `DL-4` is the decision that makes this deliverable atomic: one feed kind, one separately testable unit, one declared grammar. Absorbing a sibling feed grammar (`DEL-02-01`, `DEL-02-03`..`DEL-02-07`), the entity model it emits into (`DEL-01-01`), the reconciler that consumes it (`DEL-03-01`), the slate and register views built over decision rows (`DEL-05-02`, `DEL-09-03`), or the limitation-honesty surface (`DEL-04-05`) would undo that decision.
- **AX-005** — The edges `[E-P04]` (upstream, `DEL-01-01` → `DEL-02-02`) and `[E-P20]` (downstream, `DEL-02-02` → `DEL-03-01`) are `PROPOSAL` stratum and are accepted: `D-PEC-62` §1(4) accepted the candidate DAG v0.2 exhibit "all strata as presented", read in that packet as carrying the exhibit's flags as flags, so what remains recorded-but-unresolved is the specific annotated set (`E-A11`, `E-P69`/`E-N02`, `E-N13`/`E-N18`, the `C-02` direction, the `C-08` standing-node set) — none of which touches `[E-P04]` or `[E-P20]`, both of which carry an empty `Flag` column in the exhibit. `C-10` `STRATUM_RULE` ends "strata are provenance not authority": stratum records how an edge was derived, not whether it has been accepted, and citation does not convert `PROPOSAL` to `DECLARED`.
- **AX-006** — Edge direction is a constraint on this contract, not a licence. `RequiredMaturity` `INITIALIZED` on `[E-P04]` means the upstream *contract* is the reliable input, not any upstream artifact; consuming it imposes no obligation on `DEL-01-01`, and being consumed by `DEL-03-01` neither expands nor transfers scope in either direction. The enforcement and test duties adjacent to this deliverable are cited and discharged nowhere here: the ingest-boundary content-minimal guard is `DEL-01-03`'s, standing zero-dependency and locality enforcement is `DEL-01-05`'s, the kill test is `DEL-10-02`'s, and `DEL-10-03`'s no-ruling-write verification is a tested property of the API's write surface under `SOW-025` — a different object from this deliverable's parsing posture, which concerns what is read rather than what may be written.
- **AX-007** — `C12` governs the open owner decisions: "where one materially affects architecture the affected work is fenced or flagged, never guessed". `OI-001` materially affects this deliverable and nothing else (CON-001), so it is flagged here and fenced by REQ-009 rather than pre-empted by a production choice. TBD-002, TBD-003, and TBD-004 stay marked for the same reason.
- **AX-008** — The objective attribution to `OBJ-001` and `OBJ-002` is the SCA-002 Q2 AFFIRM ruling applying the accepted §3 derivation. This contract does not reinterpret `SOW-012`, does not restate the warrant as direct, mints no owner-confirmation criterion for a question already ruled, and records the unadopted N1/N2 alternatives so a later reader sees what was decided rather than inferring a strength the record does not carry.
- **AX-009** — The accepted basis is `SOFTWARE_DECOMP.md` revision 1.2 at commit `3623b958b`, accepted through SCA-002 under `D-PEC-64`. The revision 1.1 phrase in `_REFERENCES.md` is superseded provenance from a deferred pointer sweep, not a competing authority.
- **AX-010** — `C-04` `PHASE_PRECEDENCE` and `C-10` `STRATUM_RULE` are register-wide, non-gating constraints recorded in `_DEPENDENCIES.md`. Blocker output under the `FULL_GRAPH` mode at threshold `INITIALIZED` is advisory visibility only and is never work assignment.
- **AX-011** — This contract is lifecycle-neutral. `_STATUS.md` remains the sole lifecycle authority and is untouched by the run that authored this document; the deliverable is at `OPEN` and nothing has been built.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-012 OBJ-001 OBJ-002 | REQ-001, REQ-002, CLM-001, CLM-002, CLM-005, TBD-002, TBD-003 | AC-001 | VER-001 | Grammar documentation, the valid register and packet fixtures, and parser output showing the four identity/status elements per row plus the undeclared-field invariance result |
| OUT-001 | SOW-012 OBJ-001 OBJ-002 | REQ-003, CLM-011, CON-002, AX-001 | AC-002 | VER-002 | The sentinel-prose fixture, the full emitted payload searched against every sentinel, and the emitted record's field inventory showing no free-text-capable field |
| OUT-001 | SOW-012 OBJ-001 OBJ-002 | REQ-004, CLM-007, CLM-008 | AC-003 | VER-003 | Type-binding inspection record showing emitted records as upstream DecisionRow instances and no locally defined record-tier type |
| OUT-001 | SOW-012 OBJ-001 OBJ-002 | REQ-005, CLM-009, TBD-004 | AC-004 | VER-004 | Per-row provenance resolution records and a re-run transcript showing row-for-row reproduction over unchanged sources |
| OUT-001 | SOW-012 OBJ-001 OBJ-002 | REQ-006, AX-003 | AC-005 | VER-005 | Per-case transcripts for absent, unreadable, malformed, and out-of-grammar register and packet fixtures, each naming the file and the fault |
| OUT-001 | SOW-012 OBJ-001 OBJ-002 | REQ-007, CLM-006, AX-002 | AC-006 | VER-006 | Before/after fixture-corpus tree hashes and a call-graph inspection record showing no write path against a source file |
| OUT-001 | SOW-012 OBJ-001 OBJ-002 | REQ-008 | AC-007 | VER-007 | Dependency-manifest and import-graph inspection records, plus the DEL-01-05 enforcement result once that deliverable is available |
| OUT-001 | SOW-012 OBJ-001 OBJ-002 | REQ-009, CON-001, AX-007 | AC-008 | VER-008 | The today-shaped prose-structured register fixture with its parser output, and the recorded extension-surface review stating grammar-extension-or-rewrite without selecting an OI-001 outcome |
| OUT-002 | SOW-012 OBJ-001 OBJ-002 | REQ-010, CLM-012 | AC-009 | VER-009 | PKG-02 test-run output mapping each executed test to its declared verification method |
| OUT-001 | SOW-012 OBJ-001 OBJ-002 | CLM-003, CLM-004, CLM-010, AX-004, AX-006, AX-008 | AC-010 | HUMAN_REVIEW: REVIEW gate confirms traceability to SOW-012 and to OBJ-001/OBJ-002 as ruled at SCA-002 Gate 3 Q2, confirms the indirect OBJ-002 leg is stated no more strongly than that record states it given the unadopted N1 narrowing evidence, and confirms no sibling or cross-package scope absorption | Review record citing the scope-ledger row, the Gate 3 Q2 ruling, and the sibling and cross-package deliverable boundaries |
