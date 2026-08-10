---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-07
package_id: PKG-02
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@65955cceb
project_scope_refs: [SOW-017]
package_objective_refs: [OBJ-001, OBJ-002]
---

# Scope of Work — DEL-02-07 `adapter.yaml` feed-manifest consumer

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-02-07` — "`adapter.yaml`
feed-manifest consumer" — in `PKG-02` File-Truth Parsers of the PEC v2 build.
It covers project scope item `SOW-017` in service of package objectives
`OBJ-001` and `OBJ-002`.

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.4** (`current_basis`, SCA-004 successor), pinned at merge
`65955cceb`.

**Objective warrant.** The attribution of this deliverable to `OBJ-001` and
`OBJ-002` is SCA-002-qualified and *indirect*, not register-direct. At revision
1.1 the ledger row for `SOW-017` carried no objective. SCA-002 attributed
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

Two alternatives were defined and recorded, and neither was adopted: **N1**
(the seven parsers map to `OBJ-001` only; `SOW-001` keeps both) and **N2** (all
eight map to `OBJ-001` only, deleting the `OBJ-002` §3 edit entirely). The
record also states the evidence for narrowing, verbatim:

> **Evidence for narrowing, stated because it is real:** OBJ-002's register
> locus is the reconciler layer — `SOW-018` (incremental, Git-delta-keyed),
> `SOW-019` (drift classification), `SOW-006` (SHA stamping). The parsers
> produce facts the SHA comparison operates over; they do not perform it. N1
> would arguably describe the system more precisely than the §3 sentence does.

The owner ruled the question at the SCA-002 Gate 3 in-session gate
(2026-07-25): **"AFFIRM `OBJ-001;OBJ-002` for all eight (not N1, not N2)"**.
Unlike the nine per-row attributions batched into Q1/Q5, the Q2 group carries
**no confidence rating** in the Gate 3 record; this contract therefore neither
asserts one nor states the warrant more strongly than the record does. The
`OBJ-002` leg rests on the §3 derivation through the record tier, not on any
claim that this deliverable performs SHA comparison — it does not. `AC-008`
puts that qualification in front of the REVIEW gate rather than leaving it
buried in the scope-change package.

- **CLM-001** — The accepted `ScopeLedger.csv` row for `SOW-017` reads in full, including its trailing empty fields:

> ``SOW-017,IN,Consume per-project `_harness/adapter.yaml` as the feed manifest,PEC-RCN-002,PKG-02,DEL-02-07,OBJ-001;OBJ-002,,FALSE,``
>
> (`DecisionRef` empty, `OpenIssue` `FALSE`, `Notes` empty.)

- **CLM-002** — The ledger `SourceRef` resolves to PRD `PEC-RCN-002` (§9.2), whose text is:

> The reconciler shall ingest, at minimum: `_STATUS.md` (declared parser
> dialect), decision registers and packets, `LOOP_RECEIPTS.md` (per-loop
> grammar; the D-APP-57 contract where a ledger has adopted it),
> `WORK_GRAPH.json` / `STATUS.json` / `RUNTIME_SUMMARY.json`, dependency
> registers, workplans/LOOP_INIT, and per-project `_harness/adapter.yaml` as
> the feed manifest.

- **CLM-003** — The objective statements this deliverable serves are `OBJ-001` "Orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation" (PRD §3.1) and `OBJ-002` "Staleness is detected structurally by SHA comparison, never by judgment" (PRD §3.2). Both attributions are indirect through the record tier per the warrant above.

## Deliverable Definition — Ontology

`DEL-02-07` is typed `BACKEND_FEATURE_SLICE` at Context Envelope `S` with
`PhaseHint` `P1`. The decomposition register records its anticipated artifacts
as "Manifest reader + fixture tests" and carries no `ContextEnvelopeNotes`, so
there are no envelope notes to carry forward. Its outputs are bounded by that
naming: this contract declares exactly the reader and its fixture tests.

- **OUT-001** — A feed-manifest reader in the PEC service core: it consumes a per-project `_harness/adapter.yaml` file, validates it against a declared grammar, and derives from it the feed manifest for that project — which feeds are read for it — exposing that manifest to the reconciler.
- **OUT-002** — A fixture test suite covering the reader against valid, malformed, unreadable, and absent manifest fixtures, implementing the verification methods declared in this contract.

- **CLM-004** — The seven-way split of `PEC-RCN-002` into `SOW-011..017` is decision-log entry `DL-4` (2026-07-24): "PEC-RCN-002's enumerated feed list is split into seven scope items (SOW-011..017), one per feed kind", because "Each feed is a separately testable parser with its own grammar; a single 'ingest everything' item is not atomic". The other six feed grammars belong to `DEL-02-01` through `DEL-02-06`; this deliverable consumes only the manifest that declares which feeds are read, and defines no grammar for any feed the manifest names.
- **CLM-005** — The `PKG-02` package charter (decomposition §4) is "Read-side grammars over governed files: `_STATUS.md` dialect, decision registers/packets, receipts ledgers, run-evidence JSON, dependency registers, workplans/LOOP_INIT, `adapter.yaml` manifests", with "Writing anything; interpretation beyond declared grammars" recorded as explicitly out of package scope.
- **CLM-006** — This deliverable has exactly one accepted `EXECUTION` upstream edge, `[E-N16]`, held as register row `DEP-02-07-003`: `DEL-01-06` "Loop registry (local config default)" at `RequiredMaturity` `INITIALIZED`, `Confidence` `MEDIUM`, `Origin` `EXTRACTED`, `Statement` "Per-loop manifest consumption requires the registered-loop set from the loop registry", `SourceRef` "§Deliverable Definition — Ontology, claim CLM-006", `EvidenceQuote` "Three accepted consumer edges depend on this deliverable, all at `RequiredMaturity` `INITIALIZED` and all currently `PROPOSAL` stratum: DEL-02-07 `[E-N16]`", and `Notes` "PROPOSAL; Flag=none; EdgeID=E-N16". The remaining two register rows are the `ANCHOR` rows `DEP-02-07-001` (package anchor) and `DEP-02-07-002` (`SOW-017` requirement trace).
- **CLM-007** — `DEL-01-06` is at lifecycle state `INITIALIZED`, which means its production contract exists and validates. Its registry format, default instance, and loader are **not** produced; nothing in this contract asserts that any upstream artifact exists or has been built. The reliable input is the upstream contract, whose two consumer-facing obligations this deliverable binds to:

> - **REQ-004** — The loader shall expose the registered-loop set to the
>   record-tier consumers declared in CLM-006 through a stable in-process
>   interface.
> - **REQ-005** — Consumers shall depend only on the core-owned typed
>   `LoopRegistry` port and shall not depend on the registry's JSON paths,
>   serialization, or adapter errors. The selected version-1 JSON/schema files
>   remain replaceable behind that port; a path, schema, or field-meaning change
>   requires a separately governed migration without amending DEL-02-07,
>   DEL-03-01, or DEL-09-02 merely for adapter details.
>
> (`DEL-01-06/ScopeOfWork.md`, Epistemology section; ID-shaped text inside this
> quotation is upstream source context, not a local definition or reference.)

- **CLM-008** — The one declared downstream consumer is `DEL-03-01` (Full-rebuild reconciler) via `[E-P25]`, "SOW-017: adapter.yaml 'as the feed manifest'" / "Manifest drives which feeds are read per loop". That edge is informational here; it lives in the consumer's register and imposes no obligation on this deliverable beyond the outputs declared above.
- **CLM-009** — Every deliverable this contract names in its own voice — that is, outside the quoted upstream text of CLM-007 — carries `PhaseHint` `P1` in `Deliverables.csv`: `DEL-01-06`, `DEL-02-01`..`DEL-02-06`, `DEL-03-01`, `DEL-04-05`, and `DEL-01-05`, as does `DEL-02-07` itself. The CLM-007 quotation additionally names `DEL-09-02`, which carries `PhaseHint` `P2`; it appears there as upstream source context and is not a deliverable this contract names or stages. No claim in this contract stages any of the deliverables enumerated above into a different phase.
- **CLM-010** — The deliverable is at lifecycle state `INITIALIZED` with no implementation present. Every requirement, acceptance criterion, and verification method below states a contract on future production; none asserts that anything has been built.
- **CLM-011** — Observed corpus condition, recorded as observation and not as specification: two `_harness/adapter.yaml` instances exist in this checkout, at `projects/chirality-app-dev/_harness/adapter.yaml` and `projects/chirality-piping/_harness/adapter.yaml`. No accepted PEC source adopts their schema, and PEC's own project has no such file. These files are the corpus the reader will meet; they are not a contract, and the grammar this deliverable declares is a production choice bounded by TBD-002.

- **TBD-001** — `ResponsibleParty` is unassigned; the register records `TBD`, with assignment at WORKING_ITEMS activation.
- **TBD-002** — The manifest grammar this reader declares — which fields it consumes, their semantics, and its validation rules — is fixed by no accepted source. It is chosen during production within REQ-002 and CLM-005.
- **TBD-003** — The relation between a registered loop and the project (or projects) whose `_harness/adapter.yaml` is read for it is fixed by no accepted source. The registry names loops; the manifest is per-project; PRD §7.1 places Loop as the tenancy unit above Project. How that resolution is obtained is undetermined and is not settled by this contract.
- **TBD-004** — The means by which a YAML manifest is parsed under the zero-third-party-runtime-dependency rule (REQ-007) is undetermined. `PEC-SVC-001` permits workspace-internal runtime contracts packages; whether the reader uses such a package or a purpose-written parser is a production choice.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The reader shall consume, per project, that project's `_harness/adapter.yaml` and derive from it the feed manifest for that project: which feeds are read for it, and where each named feed is located.
- **REQ-002** — The reader shall document the manifest grammar it consumes — every field it reads and that field's semantics — and shall let no undeclared field influence its output, per the `PKG-02` out-of-scope line "interpretation beyond declared grammars" (CLM-005).
- **REQ-003** — The reader shall obtain the set of loops it serves from the loop registry through the upstream stable in-process interface quoted in CLM-007, and shall depend on no registry on-disk location, filename, or serialization.
- **REQ-004** — Where a project's manifest is absent, unreadable, malformed, or schema-invalid, the reader shall report that condition explicitly to its caller, naming the project and the fault; a silently empty, partial, or defaulted feed manifest is prohibited. Rendering such a limitation into an orientation response is `SOW-009` / `DEL-04-05` scope and is not part of this deliverable; this deliverable makes the limitation available to that consumer.
- **REQ-005** — The reader shall create, modify, or delete no source file, including the manifests it reads, per `PEC-RCN-004` ("it shall never modify a source file"), `PEC-RCN-006` ("The reconciler writes only its own store and generated views"), and the `PKG-02` out-of-scope line "Writing anything".
- **REQ-006** — The reader shall carry into the record tier only the declared manifest fields it needs to locate and read feeds; it shall capture neither undeclared manifest content nor the content of the feeds the manifest names, per `PEC-K-10` content-minimal.
- **REQ-007** — The reader and its fixtures shall introduce no third-party runtime dependency and no external network egress, per `PEC-SVC-001` and `PEC-SVC-002`, whose standing enforcement is `DEL-01-05` covering `SOW-052` and `SOW-053`. The means of satisfying this for a YAML input remains TBD-004.
- **REQ-008** — Tests shall implement the verification methods declared in this contract; they shall not define scope, requirements, or acceptance criteria.

- **AC-001** — The reader consumes a valid fixture manifest and yields exactly the feed manifest that fixture declares; every field it reads appears in the documented grammar, and altering an undeclared field in the fixture changes nothing in its output.
- **AC-002** — The reader acquires its loop set only through the upstream registry interface: no registry path, filename, or serialization detail appears in this deliverable's source, fixtures, or call surface, so the resolved registry-home choice and any separately governed adapter migration change nothing here.
- **AC-003** — For absent, unreadable, malformed, and schema-invalid manifest fixtures, the reader returns an explicit limitation naming the project and the fault, and never a silently empty, partial, or defaulted feed manifest in its place.
- **AC-004** — A reader run over a fixture corpus leaves that corpus byte-identical, and the module contains no write, create, or delete call against any source path.
- **AC-005** — The reader and its fixtures add no third-party runtime dependency and make no network call, leaving the `DEL-01-05` zero-dependency and locality assertion intact.
- **AC-006** — The reader's emitted record-tier payload for a fixture project contains only the declared manifest-derived locators and settings, with no feed content and no undeclared manifest content.
- **AC-007** — The fixture test suite implements VER-001 through VER-006, executes in the `PKG-02` test run, passes, and introduces no acceptance criterion absent from this contract.
- **AC-008** — The REVIEW gate confirms this contract's traceability to `SOW-017`, `OBJ-001`, and `OBJ-002` as ruled at SCA-002 Gate 3 Q2, confirms that the indirect `OBJ-002` leg is stated no more strongly here than the Gate 3 record states it — including the recorded and unadopted N1 narrowing evidence — and confirms that no `PKG-01`, sibling `PKG-02`, `PKG-03`, or `PKG-04` scope has been absorbed.

- **CON-001** — D-PEC-78 O-A, propagated by SCA-004 into accepted decomposition revision 1.4, resolved `SOW-077` / `OI-003` by selecting the existing PEC-owned strict-version-1 JSON/schema paths and core-owned typed `LoopRegistry` port as the long-term registry home and shape. This deliverable nevertheless cannot bind to any registry path, filename, or serialization, and REQ-003 restricts it to the upstream in-process interface; the resolved upstream choice creates no local filesystem binding and expands no output here.
- **CON-002** — `SOW-017` and `PEC-RCN-002` name the manifest as "per-project", while the upstream edge `[E-N16]` (CLM-006) supplies loops rather than projects. The accepted sources do not state how a registered loop resolves to the project or projects whose manifest is read. This contract records the gap as TBD-003 rather than choosing a resolution; if production requires a resolution that is not derivable from an accepted source, that is a scope-change question, not a production decision.

## Production and Verification Method — Praxeology

Production proceeds in the order declared grammar → reader → limitation
reporting → fixtures and tests, because each stage is the acceptance surface of
the next. All work is bounded to this deliverable folder and the service-core
source it names; this contract authorizes no register, decomposition, PRD, or
upstream-deliverable edit, and it neither defines, relocates, nor reshapes the
loop registry it consumes.

- **VER-001** — Execute the reader over a valid fixture manifest and assert the derived feed manifest equals the fixture's declared expectation; then compare the set of fields actually read, by instrumentation or code inspection, against the documented grammar, and mutate an undeclared field to assert output invariance.
- **VER-002** — Inspect the reader's loop-set acquisition path and assert it calls only the upstream registry interface; grep this deliverable's source and fixtures for any registry path, filename, or serialization token and assert none is present.
- **VER-003** — Execute the reader against absent, unreadable, malformed, and schema-invalid manifest fixtures and assert, per case, an explicit limitation naming the project and the fault, with no empty, partial, or defaulted manifest returned.
- **VER-004** — Hash the fixture corpus tree before and after a reader run and assert byte-identity; inspect the module's call graph for write, create, or delete operations against any source path.
- **VER-005** — Inspect the `PKG-02` dependency manifest and this module's import graph for third-party runtime dependencies and network calls, and re-run the `DEL-01-05` zero-dependency and locality enforcement once that deliverable is available.
- **VER-006** — Inspect the reader's emitted record-tier payload for a fixture project and assert it contains only declared manifest-derived locators and settings, with no feed content and no undeclared manifest content.
- **VER-007** — Run the `PKG-02` test suite and confirm that each of VER-001 through VER-006 has a corresponding executing automated test and that no test asserts a criterion absent from this contract.

## Governing Values and Decisions — Axiology

- **AX-001** — `PEC-K-02` files govern: the `adapter.yaml` manifest is authored project truth. The reader reads it, never rewrites it, and the feed manifest PEC derives from it is never citable as authority over the file itself.
- **AX-002** — `PEC-K-01` graceful absence governs: no governed act may require a PEC read or write. A project with no manifest, or with a manifest PEC cannot parse, is a stated coverage limitation (REQ-004), never a blocked act and never a silent gap.
- **AX-003** — `DL-4` is the decision that makes this deliverable atomic: one feed kind, one separately testable unit, one declared grammar. Absorbing any sibling feed grammar (`DEL-02-01`..`DEL-02-06`), the reconciler that consumes this manifest (`DEL-03-01`), the limitation-honesty surface (`DEL-04-05`), or the registry itself (`DEL-01-06`) would undo that decision.
- **AX-004** — The edges `[E-N16]` (upstream, `DEL-01-06` → `DEL-02-07`) and `[E-P25]` (downstream, `DEL-02-07` → `DEL-03-01`) are `PROPOSAL` stratum and are accepted: `D-PEC-62` §1(4) accepted the candidate DAG v0.2 exhibit "all strata as presented", reading acceptance as carrying the exhibit's flags as flags, so what remains recorded-but-unresolved is the specific annotated set (E-A11, E-P69/E-N02, E-N13/E-N18, C-02 direction, C-08 standing-node set) — none of which touches E-N16 or E-P25, both of which carry an empty `Flag` column in the exhibit. Stratum is provenance, not authority: it records how an edge was derived, not whether it has been accepted.
- **AX-005** — Edge direction is a constraint on this contract, not a licence. Consuming an upstream contract imposes no obligation on the upstream deliverable: `DEL-01-06` owes this deliverable nothing beyond what its own accepted contract already states, and being consumed by `DEL-03-01` neither expands nor transfers scope in either direction.
- **AX-006** — `RequiredMaturity` `INITIALIZED` on `[E-N16]` means the upstream *contract* is the reliable input, not any upstream artifact. This contract is written against the upstream contract's stated obligations (CLM-007) and asserts nothing about upstream implementation state.
- **AX-007** — `PEC-K-10` content-minimal and constraint `C6` govern what PEC retains: paths, counts, SHAs, states, hashes — never file or diff content. A feed manifest is a locator surface; reading it must not become a route by which authored content enters the store (REQ-006).
- **AX-008** — The objective attribution to `OBJ-001` and `OBJ-002` is the SCA-002 Q2 AFFIRM ruling applying the accepted §3 derivation. This contract does not reinterpret `SOW-017`, does not restate the warrant as direct, and records the unadopted N1/N2 alternatives so a later reader sees what was decided rather than inferring a strength the record does not carry.
- **AX-009** — `C-04` PHASE_PRECEDENCE and `C-10` STRATUM_RULE are register-wide, non-gating constraints recorded in `_DEPENDENCIES.md`. Blocker output under the `FULL_GRAPH` mode at threshold `INITIALIZED` is advisory visibility only and is never work assignment.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-017 OBJ-001 OBJ-002 | REQ-001, REQ-002, CLM-001, CLM-002, CLM-004, TBD-002 | AC-001 | VER-001 | Grammar documentation, the valid fixture manifest, and reader output showing the derived feed manifest plus the undeclared-field invariance result |
| OUT-001 | SOW-017 OBJ-001 OBJ-002 | REQ-003, CLM-006, CLM-007, CON-001 | AC-002 | VER-002 | The loop-set acquisition call surface, and a recorded search of this deliverable's source and fixtures for registry path or serialization tokens |
| OUT-001 | SOW-017 OBJ-001 OBJ-002 | REQ-004, CON-002, TBD-003, AX-002 | AC-003 | VER-003 | Per-case transcripts for absent, unreadable, malformed, and schema-invalid manifest fixtures, each showing the project named and the fault located |
| OUT-001 | SOW-017 OBJ-001 OBJ-002 | REQ-005, CLM-005, AX-001 | AC-004 | VER-004 | Before/after fixture-corpus tree hashes and a call-graph inspection record showing no write path against a source file |
| OUT-001 | SOW-017 OBJ-001 OBJ-002 | REQ-007, TBD-004 | AC-005 | VER-005 | Dependency-manifest and import-graph inspection records, plus the DEL-01-05 enforcement result once that deliverable is available |
| OUT-001 | SOW-017 OBJ-001 OBJ-002 | REQ-006, AX-007 | AC-006 | VER-006 | The emitted record-tier payload for a fixture project, field-by-field against the declared grammar |
| OUT-002 | SOW-017 OBJ-001 OBJ-002 | REQ-008, CLM-010 | AC-007 | VER-007 | PKG-02 test-run output mapping each executed test to its declared verification method |
| OUT-001 | SOW-017 OBJ-001 OBJ-002 | CLM-003, CLM-008, CLM-009, AX-003, AX-005, AX-008 | AC-008 | HUMAN_REVIEW: REVIEW gate confirms traceability to SOW-017 and to OBJ-001/OBJ-002 as ruled at SCA-002 Gate 3 Q2, confirms the indirect OBJ-002 leg is stated no more strongly than that record states it given the unadopted N1 narrowing evidence, and confirms no sibling or cross-package scope absorption | Review record citing the scope-ledger row, the Gate 3 Q2 ruling, and the sibling and cross-package deliverable boundaries |
