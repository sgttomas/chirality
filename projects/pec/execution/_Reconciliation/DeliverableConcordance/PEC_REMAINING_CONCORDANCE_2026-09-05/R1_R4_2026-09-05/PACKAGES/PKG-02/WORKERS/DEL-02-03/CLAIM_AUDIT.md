# Claim audit — DEL-02-03

All locators refer to the frozen base; current-source search is bounded evidence, never proof of global implementation absence.

## Current source inventory

- projects/pec/v2/config/loops.json
- projects/pec/v2/config/loops.schema.json
- projects/pec/v2/config/service_core_posture.json
- projects/pec/v2/contracts/api/v1/schema.json
- projects/pec/v2/docs/SERVICE_CORE_POSTURE.md
- projects/pec/v2/src/pec_v2/__init__.py
- projects/pec/v2/src/pec_v2/adapters/__init__.py
- projects/pec/v2/src/pec_v2/adapters/config/__init__.py
- projects/pec/v2/src/pec_v2/adapters/config/loop_registry.py
- projects/pec/v2/src/pec_v2/core/__init__.py
- projects/pec/v2/src/pec_v2/core/ports/__init__.py
- projects/pec/v2/src/pec_v2/core/ports/loop_registry.py
- projects/pec/v2/tests/config/fixtures/duplicate_loop_id.json
- projects/pec/v2/tests/config/fixtures/malformed.json
- projects/pec/v2/tests/config/fixtures/missing_loop_id.json
- projects/pec/v2/tests/config/test_json_loop_registry.py
- projects/pec/v2/tests/config/test_loop_registry_contract.py
- projects/pec/v2/tests/contracts/api/fixtures/v1_additive_candidate.json
- projects/pec/v2/tests/contracts/api/fixtures/v1_meaning_changed_candidate.json
- projects/pec/v2/tests/contracts/api/fixtures/v1_removed_element_candidate.json
- projects/pec/v2/tests/contracts/api/test_api_schema_compatibility.py
- projects/pec/v2/tests/enforcement/fixtures/dependency/conforming/core/app.py
- projects/pec/v2/tests/enforcement/fixtures/dependency/third_party_direct/core/app.py
- projects/pec/v2/tests/enforcement/fixtures/dependency/third_party_transitive/core/app.py
- projects/pec/v2/tests/enforcement/fixtures/dependency/third_party_transitive/core/helper.py
- projects/pec/v2/tests/enforcement/fixtures/dependency/workspace_contract/contracts/chirality_contracts/__init__.py
- projects/pec/v2/tests/enforcement/fixtures/dependency/workspace_contract/core/app.py
- projects/pec/v2/tests/enforcement/fixtures/locality/external_call/core/app.py
- projects/pec/v2/tests/enforcement/fixtures/locality/external_config/core/settings.py
- projects/pec/v2/tests/enforcement/fixtures/locality/local_loopback/core/app.py
- projects/pec/v2/tests/enforcement/fixtures/locality/local_unix/core/app.py
- projects/pec/v2/tests/enforcement/test_dependency_assertion.py
- projects/pec/v2/tests/enforcement/test_gate_registration.py
- projects/pec/v2/tests/enforcement/test_locality_assertion.py
- projects/pec/v2/tools/check_service_core_posture.py

## Current controls

Dependency DEP-02-03-003 is ACTIVE PREREQUISITE/PENDING to DEL-01-01. Only proposed evidence/production item REM-001 names that target. Discovery proceeds; ordinary observed maturity does not flip the register.

No local REVIEW file exists. D-PEC-63 records contract INITIALIZED, not product acceptance; SCA-002 Q2 acceptance is preserved.

## Authority and historical boundaries

D82 and D81 acceptance are current base records; effectiveness is inherited from COMMON source-bound mainline evidence, not a newly performed fetch. D65 is the source of the repaired evidence cells. Current v2 source text and the local two run records do not establish receipts-parser execution. Frozen legacy corpus was not used as current implementation.

## CLM-001

The accepted `ScopeLedger.csv` row for `SOW-013` reads in full, including its trailing fields (columns `ScopeItemID,InOutStatus,ScopeItemStatement,SourceRef,PackageID,DeliverableIDs,ObjectiveIDs,DecisionRef,OpenIssue,Notes`):

ALIGNED / documentary alignment. Compared to accepted scope/PRD, local context and source-bound dependency/objective records. Alignment is documentary and does not assert implemented behavior or new human acceptance.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## CLM-002

The ledger `SourceRef` resolves to PRD requirement `PEC-RCN-002` (§9.2), whose text is:

ALIGNED / documentary alignment. Compared to accepted scope/PRD, local context and source-bound dependency/objective records. Alignment is documentary and does not assert implemented behavior or new human acceptance.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## CLM-003

The objective statements this deliverable serves are `OBJ-001` "Orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation" (`SOFTWARE_DECOMP.md` §3, `SourceRef` §3.1; `PRD.md` §3 outcome 1) and `OBJ-002` "Staleness is detected structurally by SHA comparison, never by judgment" (§3, `SourceRef` §3.2; `PRD.md` §3 outcome 2). Both attributions are indirect through the record tier per the warrant above.

ALIGNED / documentary alignment. Compared to accepted scope/PRD, local context and source-bound dependency/objective records. Alignment is documentary and does not assert implemented behavior or new human acceptance.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## OUT-001

A receipts-ledger parser in the PEC service core: it reads a loop's `LOOP_RECEIPTS.md`, applies the grammar declared for that loop, and emits record-tier Receipt entities carrying the fields that grammar yields together with an explicit statement of the fields it does not.

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## OUT-002

A per-loop grammar table: the declared, readable artifact naming each loop the parser covers, the grammar applied to it, the receipt fields that grammar can yield, and the fields it cannot.

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## OUT-003

A fixture test suite covering the parser and the table against D-APP-57-shaped, prose-structured, malformed, unreadable, and uncovered-loop ledger fixtures, implementing the verification methods declared in this contract.

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## CLM-004

`DEL-02-03` is named "Receipts ledger parser (per-loop grammars)", Type `BACKEND_FEATURE_SLICE`, Context Envelope `L`, `PhaseHint` `P1`, `ResponsibleParty` `TBD`, `CoversScopeItems` `SOW-013`, `SupportsObjectives` `OBJ-001;OBJ-002`, with `AnticipatedArtifacts` "Parser + per-loop grammar table + fixture tests"; sources `execution/_Decomposition/Deliverables.csv` row `DEL-02-03` and `SOFTWARE_DECOMP.md` §5 PKG-02 table ("| DEL-02-03 | Receipts ledger parser (per-loop grammars) | BACKEND_FEATURE_SLICE | **L** | P1 | SOW-013 |").

ALIGNED / documentary alignment. Compared to accepted scope/PRD, local context and source-bound dependency/objective records. Alignment is documentary and does not assert implemented behavior or new human acceptance.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## CLM-005

The register `Description` of record is: "`LOOP_RECEIPTS.md` parsing under per-loop grammar, including the D-APP-57 contract where adopted; prose-structured ledgers parsed best-effort with stated limits." Three terms of that description are carried into this contract as written and not strengthened: the grammar is **per-loop**; the D-APP-57 contract applies **where adopted**, not everywhere; and prose-structured ledgers are parsed **best-effort with stated limits**, not to a validated schema.

ALIGNED / documentary alignment. Compared to accepted scope/PRD, local context and source-bound dependency/objective records. Alignment is documentary and does not assert implemented behavior or new human acceptance.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## CLM-006

The `D-APP-57` field set named by accepted truth is exactly four fields. `PRD.md` §7.1 states the Receipt entity's purpose as: "Parsed `LOOP_RECEIPTS.md` entries. Field availability is per-loop: the app-dev ledger carries the D-APP-57 contract (Receipt-ID, Examined-Through SHA, Parent-Receipt, Gate-Outcome); the pec/bridge ledgers are prose-structured with no validated schema — coverage limits stated per PEC-ORI-006". This contract adds no fifth field to that set and adopts no schema for the prose-structured case.

ALIGNED / documentary alignment. Compared to accepted scope/PRD, local context and source-bound dependency/objective records. Alignment is documentary and does not assert implemented behavior or new human acceptance.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## CLM-007

The envelope note of record, carried identically in `Deliverables.csv` `ContextEnvelopeNotes` and `_CONTEXT.md`, is: "L because grammar varies per loop and SOW-082 (OI-008) keeps the contract-adoption surface open; single domain, but multiple grammars within one parser. Split further only if a loop's grammar proves adversarial". `ContextBudgetQA.csv` rates the deliverable `MEDIUM` risk with `RecommendedAction` "Hold as L; split by per-loop grammar if any loop proves adversarial", and §8 records it as one of exactly two `L` deliverables — "DEL-02-03 (receipts-ledger parser: per-loop grammars, OI-008 open)" — with "named split lines if implementation demands them". The split guidance is a production constraint on how the work is sliced; it is not additional scope and it authorizes no new output.

ALIGNED / documentary alignment. Compared to accepted scope/PRD, local context and source-bound dependency/objective records. Alignment is documentary and does not assert implemented behavior or new human acceptance.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## CLM-008

`Dependencies.csv` holds three rows for this deliverable. Two are `ANCHOR` rows: `DEP-02-03-001` (package-local to `PKG-02`) and `DEP-02-03-002` (the `SOW-013` requirement trace). The third, `DEP-02-03-003`, is the single `EXECUTION` upstream edge: predecessor `DEL-01-01` "Record-tier schema & entity model" at `PKG-01`, `DependencyType` `PREREQUISITE`, `TargetLocation` `execution/PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model`, `Statement` "Parser emits Receipt entities", `EvidenceFile` `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md`, `SourceRef` and `EvidenceQuote` both "§3 mapping notes (as E-P03)", `Explicitness` `IMPLICIT`, `RequiredMaturity` `INITIALIZED`, `ProposedMaturity` `TBD`, `SatisfactionStatus` `PENDING`, `Confidence` `MEDIUM`, `Origin` `EXTRACTED`, `Status` `ACTIVE`, `Notes` "PROPOSAL; Flag=none; EdgeID=E-P05".

ACCEPTED_DIVERGENCE / documentary provenance. Edge identity and PENDING prerequisite survive. D-PEC-65 repaired EvidenceFile/SourceRef/EvidenceQuote; literal old cells in contract are historical, not current register truth. No register flip or new repair inferred.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## CLM-009

`DEL-01-01` is at lifecycle state `INITIALIZED`, which is the maturity `[E-P05]` requires. `INITIALIZED` means its **contract** is the reliable input: its accepted `ScopeOfWork.md` exists, and no schema, entity model, or code does. The elements this contract binds to are that contract's obligations, not artifacts. Its record-tier entity model obliges a Receipt type among the fourteen it enumerates, and two of its provisions bear directly on this parser's output typing:

ALIGNED / documentary alignment. Upstream INITIALIZED contract remains documentary input. The historical no-schema/no-code observation is not a fresh all-repository implementation verdict or a dependency SatisfactionStatus flip.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## CLM-010

The same upstream contract obliges every record-tier entity type to carry provenance sufficient for a per-claim citation to its live source — "file path, anchor, and/or SHA, per `PEC-ORI-004`" — obliges every record-tier entity to be fully regenerable from file sources, and forbids any field of any type to admit file content or diff content, per the invariant it quotes as "`PEC-K-10`: Paths, counts, SHAs, states, hashes — never file or diff content". ID-shaped text in that quotation is upstream source context, not a local definition or reference. This parser is one of the producers those obligations constrain; the obligations are cited here and discharged in the schema, not in this contract.

ALIGNED / documentary alignment. Compared to accepted scope/PRD, local context and source-bound dependency/objective records. Alignment is documentary and does not assert implemented behavior or new human acceptance.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## CLM-011

Two downstream consumer relations are recorded in `_DEPENDENCIES.md`, both marked informational. `DEL-04-05` "Measurement-limitation honesty" consumes this deliverable via `[E-N03]`, whose row in the gate exhibit (columns `EdgeID,PredecessorID,SuccessorID,Stratum,EdgeKind,Flag,BasisCitation,Rationale`) carries `Stratum` `DECLARED`, `EdgeKind` `CONSUMES`, an empty `Flag`, `BasisCitation` *SOW-013 note: "Per-loop coverage limits stated (SOW-009)"*, and `Rationale` "R1-F7: ID-explicit cross-link". `DEL-03-01` "Full-rebuild reconciler (one command)" consumes it via `[E-P21]`, whose row in the same exhibit carries `Stratum` `PROPOSAL`, `EdgeKind` `CONSUMES`, an empty `Flag`, `BasisCitation` "PEC-RCN-002 feed list (DL-4)", and `Rationale` "Full rebuild ingests receipts ledgers". Both edges live in their consumers' registers; they impose no obligation on this deliverable beyond the outputs declared above.

ALIGNED / documentary alignment. Compared to accepted scope/PRD, local context and source-bound dependency/objective records. Alignment is documentary and does not assert implemented behavior or new human acceptance.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## CLM-012

Phase staging, checked against the `PhaseHint` column of `Deliverables.csv` for every deliverable this contract names in its own voice: `DEL-02-03` itself, `DEL-01-01`, `DEL-01-03`, `DEL-01-05`, `DEL-01-06`, `DEL-02-01`..`DEL-02-07`, `DEL-03-01`, `DEL-03-02`, `DEL-03-03`, `DEL-04-03`, `DEL-04-05`, and `DEL-10-02` all carry `PhaseHint` `P1`. No claim in this contract stages any of them into a different phase, and the sole upstream edge runs from a `P1` deliverable.

ALIGNED / documentary alignment. Compared to accepted scope/PRD, local context and source-bound dependency/objective records. Alignment is documentary and does not assert implemented behavior or new human acceptance.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## CLM-013

The seven-way split of `PEC-RCN-002` into `SOW-011..017` is decision-log entry `DL-4` (2026-07-24): "PEC-RCN-002's enumerated feed list is split into seven scope items (SOW-011..017), one per feed kind", because "Each feed is a separately testable parser with its own grammar; a single 'ingest everything' item is not atomic". The other six feed grammars belong to `DEL-02-01` (`_STATUS.md`), `DEL-02-02` (decision registers/packets), `DEL-02-04` (run-evidence JSON), `DEL-02-05` (dependency registers), `DEL-02-06` (workplans/LOOP_INIT), and `DEL-02-07` (`adapter.yaml` feed manifest). This deliverable defines grammars for `LOOP_RECEIPTS.md` only, and none for any other feed.

ALIGNED / documentary alignment. Compared to accepted scope/PRD, local context and source-bound dependency/objective records. Alignment is documentary and does not assert implemented behavior or new human acceptance.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## CLM-014

The `PKG-02` package charter (decomposition §4) is "Read-side grammars over governed files: `_STATUS.md` dialect, decision registers/packets, receipts ledgers, run-evidence JSON, dependency registers, workplans/LOOP_INIT, `adapter.yaml` manifests", with "Writing anything; interpretation beyond declared grammars" recorded as explicitly out of package scope. Both exclusions bind this deliverable directly: it writes nothing, and it draws no inference a declared grammar does not license.

ALIGNED / documentary alignment. Compared to accepted scope/PRD, local context and source-bound dependency/objective records. Alignment is documentary and does not assert implemented behavior or new human acceptance.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## CLM-015

The acts that consume this parser's output are owned elsewhere and are cited here, never discharged: rendering an unparseable or stale feed into a response as a stated measurement limitation is `DEL-04-05` under `SOW-009`; stamping responses with examined-through SHA and attaching per-claim citations is `DEL-04-03` under `SOW-006` and `SOW-007`; full rebuild by one command is `DEL-03-01` under `SOW-010`; incremental reconciliation keyed on Git delta is `DEL-03-02` under `SOW-018` and drift classification is `DEL-03-03` under `SOW-019`; the record-tier schema and Receipt type are `DEL-01-01` under `SOW-001`; the store's ingest-boundary content-minimal guard is `DEL-01-03` under `SOW-056`; standing zero-dependency and locality enforcement is `DEL-01-05` under `SOW-052` and `SOW-053`; the standing kill test is `DEL-10-02` under `SOW-055`. This contract produces only the parser, the grammar table, and their fixture tests.

ALIGNED / documentary alignment. Compared to accepted scope/PRD, local context and source-bound dependency/objective records. Alignment is documentary and does not assert implemented behavior or new human acceptance.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## CLM-016

The deliverable is at lifecycle state `OPEN` with no implementation present. Every requirement, acceptance criterion, and verification method below states a contract on future production; none asserts that anything has been built.

ACCEPTED_DIVERGENCE / historical lifecycle declaration. OPEN refers to authoring-time NO_STATUS_TOUCH basis; current authoritative status is INITIALIZED under separate D-PEC-63 status act. No stale wording rewrite or lifecycle reversal inferred; no current implementation absence claimed.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## CLM-017

Observed corpus condition, recorded as observation and not as specification: five files named `LOOP_RECEIPTS.md` exist in this checkout — `projects/chirality-app-dev/loop/`, `projects/chirality-piping/loop/`, `_DomainEngines/pec/`, `_DomainEngines/bridge/`, and `execution/_Coordination/` (the root governance loop). A literal search for the token `Receipt-ID` returns 40 occurrences in the app-dev ledger and 29 in the piping ledger, and none in the pec, bridge, or root ledgers. Accepted truth classifies only two of the five: `PRD.md` §7.1 names the app-dev ledger as carrying the `D-APP-57` contract and the pec and bridge ledgers as prose-structured. It classifies neither the piping nor the root ledger. These files are the corpus the parser will meet; they are not a contract, and no grammar is derived from them by this document.

UNKNOWN / historical author observation. July25 run attributes five-ledger counts and classifies its search as observation. Foreign-ledger scope excluded; counts not refreshed and not represented as current.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## TBD-001

`ResponsibleParty` is unassigned; the register records `TBD`, with assignment at WORKING_ITEMS activation (`SOFTWARE_DECOMP.md` §5 preamble; `_CONTEXT.md`).

ALIGNED / documentary alignment. Truthful ResponsibleParty=TBD agrees with current register/context. No product implementation residual or automatic assignment task.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## TBD-002

The per-loop grammars themselves — which ledger constructs each grammar recognizes and by what rules — are fixed by no accepted source beyond the four-field `D-APP-57` set of CLM-006. They are chosen during production within REQ-002 and the `PKG-02` charter of CLM-014.

ALIGNED / documentary alignment. Production grammar choices remain expressly undetermined within declared grammar/content-minimal scope. Documentary truth, not a completed grammar artifact.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## TBD-003

Which loops this parser covers, and in what order, is not fixed for this deliverable by any accepted source. The informational side of CON-002.

UNKNOWN / documentary alignment. Coverage-set limitation is explicitly documented. Registry configuration and later OI-003 ruling do not silently choose this parser coverage or add an edge to DEL-01-06.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## TBD-004

Which structured facts a best-effort grammar can yield from a prose-structured ledger is undetermined. It is a production choice bounded by REQ-004 and by the content-minimal limit of REQ-007, and it is expected to differ per loop.

ALIGNED / documentary alignment. Production grammar choices remain expressly undetermined within declared grammar/content-minimal scope. Documentary truth, not a completed grammar artifact.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## REQ-001

The parser shall read a loop's `LOOP_RECEIPTS.md` and apply the grammar the per-loop grammar table declares for that loop. Every emitted Receipt shall identify the loop and the grammar under which it was produced. No grammar shall be applied to a loop the table does not cover, and no default or fallback grammar shall stand in for a missing table entry.

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## REQ-002

The per-loop grammar table shall declare, for each loop covered, the grammar applied, the receipt fields that grammar can yield, and the fields it cannot. No ledger construct outside the declared grammar shall influence the parser's output, per the `PKG-02` out-of-scope line "interpretation beyond declared grammars" (CLM-014).

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## REQ-003

Where a ledger has adopted the `D-APP-57` contract, the parser shall extract that contract's four fields — Receipt-ID, Examined-Through SHA, Parent-Receipt, Gate-Outcome (CLM-006). Adoption shall be determined per ledger under the declared grammar and shall never be assumed from a loop's identity, and the parser shall define no additional receipt-contract field.

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## REQ-004

Where a ledger is prose-structured with no validated schema, the parser shall parse best-effort and state its limits: each field the grammar could not obtain shall be explicitly marked unavailable, with the loop and the reason identified. A silently omitted, absent, defaulted, or inferred field is prohibited, per `PEC-ORI-006` and scope item `SOW-009`. Rendering such a limitation into an orientation response is `DEL-04-05`'s work (CLM-015); this deliverable makes the limitation available to that consumer.

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## REQ-005

The parser shall emit Receipt entities typed as the record-tier entity model obliges, and shall express per-loop field availability through the availability representation that upstream contract requires (CLM-009). It shall introduce no Receipt field the record-tier model is not obliged to carry, and shall drop no availability distinction that model is obliged to make readable.

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## REQ-006

Every emitted Receipt shall carry provenance to its live source sufficient for a per-claim citation — ledger file path, in-file anchor, and/or SHA, per `PEC-ORI-004` and the upstream provenance obligation of CLM-010. Attaching citations to an orientation response is `DEL-04-03`'s under `SOW-007`; this requirement obliges the parser to carry what that act needs, and no more.

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## REQ-007

No emitted field shall hold the ledger's authored prose. Extraction is limited to the declared grammar's structured facts — identifiers, dates, states, gate outcomes, commit SHAs, pointers, counts — per `PEC-K-10` ("Paths, counts, SHAs, states, hashes — never file or diff content") and register-wide constraint `C6`. Quoted owner directions, rationale text, and narrative bodies present in a ledger shall not be representable in the parser's output. Enforcement at the ingest boundary is `DEL-01-03`'s guard under `SOW-056`; this requirement binds what the parser is able to emit.

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## REQ-008

The parser shall create, modify, or delete no source file, including the ledgers it reads, per `PEC-RCN-004` ("it shall never modify a source file"), `PEC-RCN-006` ("The reconciler writes only its own store and generated views"), and the `PKG-02` out-of-scope line "Writing anything".

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## REQ-009

Parsing shall be deterministic: identical ledger bytes under an identical grammar table shall yield an identical Receipt set, including identical availability markings. This is what makes the record tier regenerable from sources by one command (`PEC-K-02`, `PEC-RCN-001`); performing the rebuild is `DEL-03-01`'s under `SOW-010`.

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## REQ-010

Adding a loop to the grammar table, or changing a loop's recorded adoption status should `OI-008` be ruled, shall be a change to the table and its fixtures alone. It shall require no change to the parser's emitted typing, to its call surface, or to any other deliverable, and it shall require no amendment of this contract.

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## REQ-011

The work shall be delivered as one parser holding multiple grammars. A split is permitted only along the recorded line — a loop whose grammar proves adversarial — and the seam and its evidence shall be recorded with the split (CLM-007). A split changes no other term of this contract, adds no output, and requires no register amendment.

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## REQ-012

The parser and its fixtures shall introduce no third-party runtime dependency and no external network egress, per `PEC-SVC-001` and `PEC-SVC-002` (constraints `C7` and `C8`), whose standing enforcement is `DEL-01-05` covering `SOW-052` and `SOW-053`.

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## REQ-013

Fixture tests shall implement the verification methods declared in this contract; they shall not define scope, requirements, or acceptance criteria.

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## AC-001

For each loop the table covers, the parser applies exactly the declared grammar and every emitted Receipt names its loop and grammar; a ledger from a loop absent from the table is reported as uncovered rather than parsed under any default, and no output is produced for it.

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## AC-002

The per-loop grammar table exists as a readable artifact and states, per covered loop, the grammar, the yieldable fields, and the unyieldable fields; every ledger construct the parser actually reads appears in the table; and altering an undeclared construct in a fixture changes nothing in the output.

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## AC-003

`D-APP-57` adoption is detected from the ledger and never from the loop's identity: a fixture carrying the four-field set yields those four fields; a fixture from the same loop lacking them yields the unavailable marking rather than an error or a fabricated value; no loop is hard-coded as adopting or as not adopting; and the parser defines no fifth receipt-contract field.

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## AC-004

For a prose-structured fixture the parser yields the fields its grammar obtains, marks every unobtained field unavailable with the loop and reason identified, and returns no silently omitted, defaulted, or inferred field; malformed and unreadable fixtures likewise yield an explicit limitation rather than a partial result presented as complete.

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## AC-005

Reviewed against the record-tier contract's Receipt obligations (CLM-009), the parser's emitted payload introduces no field that contract is not obliged to carry and drops no per-loop availability distinction it is obliged to make readable; the difference between a `D-APP-57` ledger and a prose-structured one is readable from the output rather than inferred.

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## AC-006

For a sample Receipt from each covered grammar, the recorded provenance resolves to a live ledger location by path, anchor, and/or SHA.

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## AC-007

No emitted field holds authored prose: a fixture ledger entry containing a verbatim owner direction, a rationale paragraph, and a narrative body yields only the grammar's structured facts, and the prose is not expressible anywhere in the output.

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## AC-008

A parser run over a fixture corpus leaves that corpus byte-identical, and the module contains no write, create, or delete call against any source path.

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## AC-009

Two runs over identical ledger bytes under an identical table yield identical Receipt sets, including identical availability markings.

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## AC-010

Adding a loop row to the table, and separately flipping a loop's recorded adoption status, each require a change to the table and its fixtures only: the parser's emitted typing, its call surface, and every other deliverable are untouched, and no `OI-008` outcome is presupposed by parser or table.

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## AC-011

The work is delivered as one parser holding multiple grammars, or as a split along the recorded adversarial-grammar line accompanied by a recorded statement of the seam that justified it; no other split line is used.

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## AC-012

The parser and its fixtures add no third-party runtime dependency and make no network call, leaving the `DEL-01-05` zero-dependency and locality assertion intact.

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## AC-013

The fixture test suite implements VER-001 through VER-012, executes in the `PKG-02` test run, passes, and introduces no acceptance criterion absent from this contract.

UNKNOWN / behavioral obligation. Accepted future-production obligation. Current v2 sources implement loop registry and other slices, not affirmative evidence for this parser; authoring run reports a contract only. No DOCUMENTED_UNIMPLEMENTED inference.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## AC-014

The REVIEW gate confirms this contract's traceability to `SOW-013`, `OBJ-001`, and `OBJ-002` as ruled at SCA-002 Gate 3 Q2, confirms that the indirect `OBJ-002` leg is stated no more strongly here than the Gate 3 record states it — including the recorded and unadopted N1 narrowing evidence — and confirms that no `PKG-01` schema scope, sibling `PKG-02` feed grammar, or `PKG-03`/`PKG-04` reconciliation or honesty scope has been absorbed.

UNKNOWN / human acceptance. SCA-002 Q2 is an actual accepted objective ruling; it is not the exact current contract REVIEW demanded here. No DEL-02-03 REVIEW located in bounded review inventory; no prior act reversed.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## CON-001

Whether non-app-dev loop ledgers adopt the `D-APP-57` receipt contract is an **undecided owner question**. It is carried in the scope ledger as `SOW-082` — row: `SOW-082,TBD,Whether non-app-dev loop ledgers adopt the D-APP-57 receipt contract,§16.8,,,,,TRUE,OI-008. Affects SOW-013 per-loop grammar coverage` — and in the Open Issues table as `OI-008`, "§16.8 receipt-contract adoption by non-app-dev ledgers undecided", disposition "§16 ruling (per-loop)". `PRD.md` §16.8 states it as "Whether non-app-dev loop ledgers adopt the D-APP-57 receipt contract (today only the app-dev ledger is schema-validated; pec/bridge are prose-structured)", and §16 closes "None of these blocks P0–P2." Nothing in this contract presupposes adoption or non-adoption. REQ-003 forbids assuming adoption from a loop's identity, REQ-004 keeps the prose-structured path first-class, and REQ-010 requires that a later ruling be absorbable by a table change. A production choice that hard-coded either outcome would pre-empt an owner ruling; a resolution arrives through the §16 per-loop ruling, not through this deliverable.

ALIGNED / documentary alignment. SOW-082 remains TBD and OI-008 per-loop owner ruling remains separate; none blocks P0–P2. No blanket owner-adoption gate placed on unrelated work.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## CON-002

The set of loops this parser must cover is not fixed at the level of accepted truth for this deliverable. `PRD.md` §7.1 defines Loop as "Tenancy unit, above Project: a LOOP_INIT/workplan-governed work loop (root, app-dev, piping, pec, bridge, …)". The register description of the loop registry (`Deliverables.csv` row `DEL-01-06`) records "one loop at P1 (PEC's own build, OI-010), extended to all five registered loops at P2", and `DL-10` records the owner resolution of `OI-010` as "first P1 loop = PEC v2's own build". `PRD.md` §7.1 classifies the grammar of only three of the named loops (app-dev, pec, bridge) and none of the rest. No accepted dependency edge is recorded between this deliverable and `DEL-01-06` in either deliverable's local register, so this contract states no ordering claim between them and treats the registry only as register context. The gap is recorded as TBD-003 rather than resolved; if production requires a coverage set that is not derivable from an accepted source, that is a scope-change question, not a production decision.

UNKNOWN / documentary alignment. Coverage-set limitation is explicitly documented. Registry configuration and later OI-003 ruling do not silently choose this parser coverage or add an edge to DEL-01-06.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## CON-003

`SOW-013`'s "best-effort" parsing of prose-structured ledgers and the content-minimal invariant `PEC-K-10` / `C6` are read together in REQ-004 and REQ-007 as follows: "best-effort" qualifies the **completeness of structured extraction**, never the **kind** of material extracted. `PEC-K-10` is unconditional — "never file or diff content" — and `C6` records it as enforced at ingest, so no reading of "best-effort" licenses capturing a ledger's authored prose in order to compensate for a weak grammar. This is a reading of two accepted sources, stated openly so a reviewer can check it rather than discover it in the implementation. If an owner intends prose capture for prose-structured ledgers, that is an amendment to `PEC-K-10`'s scope and not a production choice available here.

ALIGNED / documentary alignment. Compared to accepted scope/PRD, local context and source-bound dependency/objective records. Alignment is documentary and does not assert implemented behavior or new human acceptance.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## VER-001

Execute the parser over one fixture ledger per covered loop and assert that the applied grammar is the table's declared one and that every emitted Receipt names its loop and grammar; then execute it over a fixture from a loop absent from the table and assert an uncovered-loop report with no Receipt emitted.

ALIGNED / finite test method. ALIGNED only as a declared method linked to the matching AC in the matrix. No executing suite or finite PASS established. Does not discharge REQ/AC.

UNEXECUTED declared method; source defines the finite method, with no parser PASS claimed.

## VER-002

Compare the set of ledger constructs actually read — by instrumentation or code inspection — against the per-loop grammar table, asserting the table is complete; then mutate an undeclared construct in a fixture and assert output invariance.

ALIGNED / finite test method. ALIGNED only as a declared method linked to the matching AC in the matrix. No executing suite or finite PASS established. Does not discharge REQ/AC.

UNEXECUTED declared method; source defines the finite method, with no parser PASS claimed.

## VER-003

Execute the parser over a `D-APP-57`-shaped fixture and assert the four declared fields are extracted; execute it over a same-loop fixture lacking them and assert the unavailable marking; inspect the source and table for any loop-identity-keyed adoption assumption and for any receipt-contract field beyond the four.

ALIGNED / finite test method. ALIGNED only as a declared method linked to the matching AC in the matrix. No executing suite or finite PASS established. Does not discharge REQ/AC.

UNEXECUTED declared method; source defines the finite method, with no parser PASS claimed.

## VER-004

Execute the parser over prose-structured, malformed, and unreadable fixtures and assert, per case, the fields obtained plus an explicit unavailable marking naming loop and reason for every field not obtained, with no defaulted or inferred value present.

ALIGNED / finite test method. ALIGNED only as a declared method linked to the matching AC in the matrix. No executing suite or finite PASS established. Does not discharge REQ/AC.

UNEXECUTED declared method; source defines the finite method, with no parser PASS claimed.

## VER-005

Review the emitted payload field by field against the record-tier contract's Receipt obligations quoted in CLM-009, asserting no extra field and no dropped availability distinction, and assert that a `D-APP-57` output and a prose-structured output are distinguishable by inspection alone.

ALIGNED / finite test method. ALIGNED only as a declared method linked to the matching AC in the matrix. No executing suite or finite PASS established. Does not discharge REQ/AC.

UNEXECUTED declared method; source defines the finite method, with no parser PASS claimed.

## VER-006

For a sample Receipt from each covered grammar, resolve the recorded provenance to a live ledger location and assert that path, anchor, and/or SHA are present and locatable.

ALIGNED / finite test method. ALIGNED only as a declared method linked to the matching AC in the matrix. No executing suite or finite PASS established. Does not discharge REQ/AC.

UNEXECUTED declared method; source defines the finite method, with no parser PASS claimed.

## VER-007

Execute the parser over a fixture entry containing a verbatim owner direction, a rationale paragraph, and a narrative body; assert the output holds only structured facts, and review every emitted field's type for capacity to hold prose.

ALIGNED / finite test method. ALIGNED only as a declared method linked to the matching AC in the matrix. No executing suite or finite PASS established. Does not discharge REQ/AC.

UNEXECUTED declared method; source defines the finite method, with no parser PASS claimed.

## VER-008

Hash the fixture corpus tree before and after a parser run and assert byte-identity; inspect the module's call graph for write, create, or delete operations against any source path.

ALIGNED / finite test method. ALIGNED only as a declared method linked to the matching AC in the matrix. No executing suite or finite PASS established. Does not discharge REQ/AC.

UNEXECUTED declared method; source defines the finite method, with no parser PASS claimed.

## VER-009

Run the parser twice over identical ledger bytes with an identical table and assert the two Receipt sets, including availability markings, are identical.

ALIGNED / finite test method. ALIGNED only as a declared method linked to the matching AC in the matrix. No executing suite or finite PASS established. Does not discharge REQ/AC.

UNEXECUTED declared method; source defines the finite method, with no parser PASS claimed.

## VER-010

Perform two isolated change exercises — add a loop row to the table with its fixtures, and flip a loop's recorded adoption status — and assert in each case that the diff touches the table and fixtures only, that emitted typing and call surface are unchanged, and that no `OI-008` outcome is encoded anywhere in parser or table.

ALIGNED / finite test method. ALIGNED only as a declared method linked to the matching AC in the matrix. No executing suite or finite PASS established. Does not discharge REQ/AC.

UNEXECUTED declared method; source defines the finite method, with no parser PASS claimed.

## VER-011

Compare the delivered artifact structure against the envelope note of CLM-007, asserting either a single parser holding multiple grammars or a split along the recorded adversarial-grammar line with its seam evidence recorded.

ALIGNED / finite test method. ALIGNED only as a declared method linked to the matching AC in the matrix. No executing suite or finite PASS established. Does not discharge REQ/AC.

UNEXECUTED declared method; source defines the finite method, with no parser PASS claimed.

## VER-012

Inspect the `PKG-02` dependency manifest and this module's import graph for third-party runtime dependencies and network calls, and re-run the `DEL-01-05` zero-dependency and locality enforcement once that deliverable is available, without discharging it here.

ALIGNED / finite test method. ALIGNED only as a declared method linked to the matching AC in the matrix. No executing suite or finite PASS established. Does not discharge REQ/AC.

UNEXECUTED declared method; source defines the finite method, with no parser PASS claimed.

## VER-013

Run the `PKG-02` test suite and confirm that each of VER-001 through VER-012 has a corresponding executing automated test and that no test asserts a criterion absent from this contract.

ALIGNED / finite test method. ALIGNED only as a declared method linked to the matching AC in the matrix. No executing suite or finite PASS established. Does not discharge REQ/AC.

UNEXECUTED declared method; source defines the finite method, with no parser PASS claimed.

## AX-001

`PEC-K-02` files govern: `LOOP_RECEIPTS.md` is authored loop truth, and every one of these ledgers states its own epistemic status as a derivative handoff ledger that its live sources override. The parser reads it, never rewrites it, and a parsed Receipt is never citable as authority over the ledger or over the sources the ledger itself defers to.

ALIGNED / documentary alignment. Normative files-govern/read-only limit aligns with PRD. Statement about every foreign ledger is retained as author provenance, not independently surveyed current behavior.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## AX-002

`PEC-ORI-006` coverage honesty governs, and it is why this deliverable's register description ends "with stated limits". Per-loop grammar variation guarantees uneven field availability; the value protected is that the unevenness is *stated* rather than smoothed. A parser that returned a tidy uniform Receipt across five differently shaped ledgers would have defeated `SOW-009` at the point where the information still existed.

ALIGNED / documentary alignment. Compared to accepted scope/PRD, local context and source-bound dependency/objective records. Alignment is documentary and does not assert implemented behavior or new human acceptance.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## AX-003

`PEC-K-10` content-minimal is a residency posture, not a storage optimization. For a parser the strongest available enforcement is inexpressibility, which is why REQ-007 binds the emitted field shapes rather than the reading behaviour. CON-003 records the reading of "best-effort" this rests on, in the open.

ALIGNED / documentary alignment. Compared to accepted scope/PRD, local context and source-bound dependency/objective records. Alignment is documentary and does not assert implemented behavior or new human acceptance.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## AX-004

`DL-4` is the decision that makes this deliverable atomic: one feed kind, one separately testable unit, its own grammars. Absorbing a sibling feed grammar (`DEL-02-01`, `DEL-02-02`, `DEL-02-04`..`DEL-02-07`), the Receipt type itself (`DEL-01-01`), the reconciler that ingests these entities (`DEL-03-01`), or the limitation-honesty surface that renders their gaps (`DEL-04-05`) would undo it.

ALIGNED / documentary alignment. Compared to accepted scope/PRD, local context and source-bound dependency/objective records. Alignment is documentary and does not assert implemented behavior or new human acceptance.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## AX-005

The edges cited here are `[E-P05]` (upstream, `DEL-01-01` → `DEL-02-03`, `PROPOSAL`), `[E-P21]` (downstream, `DEL-02-03` → `DEL-03-01`, `PROPOSAL`), and `[E-N03]` (downstream, `DEL-02-03` → `DEL-04-05`, `DECLARED`). All three are accepted: `D-PEC-62` §1(4) recorded the DAG candidate v0.2 exhibit as "accepted, all strata as presented", reading that acceptance as carrying the exhibit's **flags as flags**, so what remains recorded-but-unresolved is the specific annotated set — `E-A11`, `E-P69`/`E-N02`, `E-N13`/`E-N18`, the `C-02` direction, and the `C-08` standing-node set — none of which touches the three edges above, each of which carries an empty `Flag` column in the exhibit. Stratum is provenance, not authority: it records how an edge was derived, not whether it was accepted, and citation converts no `PROPOSAL` into a `DECLARED`.

ALIGNED / documentary alignment. Compared to accepted scope/PRD, local context and source-bound dependency/objective records. Alignment is documentary and does not assert implemented behavior or new human acceptance.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## AX-006

Edge direction is a constraint on this contract, not a licence. Upstream, `[E-P05]` makes the record-tier contract an input that types this parser's output; it transfers no schema authorship, no entity-model decision, and no upstream obligation into this contract, and `DEL-01-01` owes this deliverable nothing beyond what its own accepted contract already states. Downstream, `[E-P21]` and `[E-N03]` make this parser an input to other deliverables; they impose no duty on those consumers and grant this contract no authority over them. The enforcement and rendering duties named in CLM-015 are cited here and discharged nowhere in this document.

ALIGNED / documentary alignment. Compared to accepted scope/PRD, local context and source-bound dependency/objective records. Alignment is documentary and does not assert implemented behavior or new human acceptance.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## AX-007

`RequiredMaturity` `INITIALIZED` on `[E-P05]` means the upstream **contract** is the reliable input, not any upstream artifact. This contract is written against that contract's stated obligations (CLM-009, CLM-010) and asserts nothing about upstream implementation state; no schema, entity type, or persistence exists.

ALIGNED / documentary alignment. Upstream INITIALIZED contract remains documentary input. The historical no-schema/no-code observation is not a fresh all-repository implementation verdict or a dependency SatisfactionStatus flip.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## AX-008

The objective attribution to `OBJ-001` and `OBJ-002` is the SCA-002 Q2 AFFIRM ruling applying the accepted §3 derivation through the record tier. This contract does not reinterpret `SOW-013`, does not restate the warrant as direct, and records the unadopted N1 and N2 alternatives so a later reader sees what was decided rather than inferring a strength the record does not carry. The `OBJ-002` service is structural and upstream of the comparison: REQ-003 extracts the Examined-Through SHA, and no requirement here compares one.

ALIGNED / documentary alignment. Compared to accepted scope/PRD, local context and source-bound dependency/objective records. Alignment is documentary and does not assert implemented behavior or new human acceptance.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## AX-009

Context Envelope `L` is a recorded judgment about grammar plurality, not a licence to grow. The register's own condition — "Split further only if a loop's grammar proves adversarial" — is production guidance under REQ-011; taking the split adds no output, and declining it adds no scope.

ALIGNED / documentary alignment. Compared to accepted scope/PRD, local context and source-bound dependency/objective records. Alignment is documentary and does not assert implemented behavior or new human acceptance.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## AX-010

Unknowns stay marked. TBD-001 through TBD-004, CON-001, CON-002, and CON-003 are recorded rather than resolved by inference. `OI-008` is decided by a `§16` per-loop owner ruling; a production choice that settled it, in either direction, would be a decision taken in the wrong place.

ALIGNED / documentary alignment. Compared to accepted scope/PRD, local context and source-bound dependency/objective records. Alignment is documentary and does not assert implemented behavior or new human acceptance.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## AX-011

`C-04` `PHASE_PRECEDENCE` and `C-10` `STRATUM_RULE` are register-wide, non-gating constraints recorded in `_DEPENDENCIES.md`, the latter ending "strata are provenance not authority". Blocker output under the `FULL_GRAPH` mode at threshold `INITIALIZED` is advisory visibility only and is never work assignment.

ALIGNED / documentary alignment. Compared to accepted scope/PRD, local context and source-bound dependency/objective records. Alignment is documentary and does not assert implemented behavior or new human acceptance.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## AX-012

This contract is lifecycle-neutral. `_STATUS.md` remains the sole lifecycle authority and is untouched by the run that authored this document; the deliverable is at `OPEN` and nothing has been built.

ACCEPTED_DIVERGENCE / historical lifecycle declaration. OPEN refers to authoring-time NO_STATUS_TOUCH basis; current authoritative status is INITIALIZED under separate D-PEC-63 status act. No stale wording rewrite or lifecycle reversal inferred; no current implementation absence claimed.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## SOW-013

Parse LOOP_RECEIPTS.md ledgers under per-loop grammar, including the D-APP-57 contract where a ledger has adopted it

UNKNOWN / behavioral obligation. Accepted ledger row is exact scope basis; CLM-001 separately assesses documentary transcription.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## BASIS-001

Contract cites revision 1.2; current accepted decomposition and context/reference pointers are revision 1.4

ACCEPTED_DIVERGENCE / documentary provenance. SOW-013 scope unchanged; historical frontmatter is provenance. Completed ordinary SCA004 currency must not be reopened by old _LATEST prose.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.

## LIFECYCLE-001

Current State INITIALIZED; no ## Remaining section

ALIGNED / lifecycle. Status is the current lifecycle home. Empty work selection does not prove closure; UNKNOWN population prevents NONE.

Source comparison in CLAIM_AUDIT.md; no parser behavior test executed.
