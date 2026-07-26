---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-01-03
package_id: PKG-01
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@3623b958b
project_scope_refs: [SOW-056]
package_objective_refs: [OBJ-005]
---

# Scope of Work — DEL-01-03 Store bootstrap & content-minimal guard

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-01-03` — "Store
bootstrap & content-minimal guard" — in `PKG-01` Service Core & Store of the
PEC v2 build. It covers project scope item `SOW-056` in service of package
objective `OBJ-005`.

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.2** (`current_basis`, SCA-002 successor; accepted 2026-07-25 at
D-PEC-64 closure, commit `3623b958b`). The deliverable-local `_REFERENCES.md`
still names revision 1.1; that phrase is superseded provenance from a deferred
pointer sweep and is not the basis of this contract, as `_CONTEXT.md`'s own
supersession line records.

**Objective warrant.** The `DEL-01-03` → `OBJ-005` attribution is
SCA-002-qualified rather than pre-existing register truth: SCA-002 completed
the deliverable→objective mapping for the Phase 2.2 wave and the attribution
was accepted at revision 1.2 (`DL-17`). The warrant runs through `SOW-056`'s
own PRD anchor. `PEC-SVC-005` places the store at a gitignored path, and
`PEC-K-02` states that "the database is gitignored and safe to delete" — the
gitignored path *is* the deletability posture that `OBJ-005` names. §3 of the
accepted decomposition records the same reading, mapping `SOW-052..056` and
`DEL-01-03` to `OBJ-005`. The Gate 3 record rates this row HIGH but on the
first clause alone, and states the limit explicitly: `PEC-SVC-005`'s second
clause — the content-minimal rule this deliverable enforces through OUT-002 —
"serves **no §3 objective**: PEC-K-10 is a privacy/footprint invariant with no
objective-level statement", so "the mapping rests on clause one alone; clause
two is carried unmapped inside a mapped row, which the ledger has no way to
express" (`execution/_ScopeChange/SCA-002_2026-07-25_1042/Amendment_Preview.md`,
row 3). OUT-002 is therefore in scope on `SOW-056`'s own text while carrying no
objective warrant of its own.

- **CLM-001** — `SOW-056` states: "Keep the store at a gitignored path and enforce the content-minimal rule at ingest", with SourceRef `PEC-SVC-005` and the ledger note "Carries PEC-K-10". The scope item is a single requirement with two clauses; both are in scope for this deliverable.
- **CLM-002** — `OBJ-005` states: "Everything PEC holds can be deleted at any moment without blocking any governed act" (PRD §3.5).
- **CLM-003** — `PEC-SVC-005` states: "The store lives at a gitignored path; the content-minimal rule (PEC-K-10) is enforced at ingest."

## Deliverable Definition — Ontology

`DEL-01-03` is typed `BACKEND_FEATURE_SLICE` at Context Envelope `M` with
`PhaseHint` `P1`. The decomposition register records its anticipated artifacts
as "Store lifecycle module + guard + tests" and carries no
`ContextEnvelopeNotes` (§5 records mandatory envelope notes only for the two
`L` deliverables, `DEL-02-03` and `DEL-01-01`). It is a root node of the
accepted dependency DAG: `_DEPENDENCIES.md` declares no upstream predecessors,
and `Dependencies.csv` holds only the two ANCHOR rows (`DEP-01-03-001` package
anchor, `DEP-01-03-002` `SOW-056` requirement trace).

- **OUT-001** — A store lifecycle module in the PEC service core: it resolves the store's location to a Git-ignored path, registers or verifies the ignore rule that keeps it untracked, creates and opens the store, and provides explicit safe-delete and recreate-from-empty semantics.
- **OUT-002** — A content-minimal guard: the single declared ingest boundary through which every write into the store passes, admitting only the field classes `PEC-K-10` permits and rejecting file and diff content explicitly.
- **OUT-003** — An automated test suite covering the store lifecycle module and the guard, implementing the verification methods declared in this contract.

- **CLM-004** — `PEC-K-10` states: "Content-minimal. Paths, counts, SHAs, states, hashes — never file or diff content." PRD §7.1 applies it to a record-tier entity directly (DecisionRow carries "register-row identity and status only … never the row's prose"), and `PEC-PRS-002` applies it to Git scanning ("file and diff content shall never be captured"). PRD §7.2 repeats it for the presence tier's Worktree/GitRef entity ("dirty path names and counts (never content)").
- **CLM-005** — "The store" is the PEC database of `PEC-K-02`: gitignored and safe to delete, holding a record tier that is regenerated from sources by one command and a presence tier that is expected to be lost on rebuild (`PEC-K-05`). PRD §15 quotes the `D-GOV-01` Option A sanctioning clause for the same object — "a rebuildable, gitignored projection: safe to delete, regenerated from files by one command, never cited as authority".
- **CLM-006** — Four accepted graph edges depend on this deliverable, all at `RequiredMaturity` `INITIALIZED` and all currently `PROPOSAL` stratum: DEL-03-01 `[E-P15]` ("Reconciler writes are restricted to the store; store lifecycle must exist"), DEL-07-01 `[E-P16]` ("Durable message store lives in the gitignored store"), DEL-01-02 `[E-P17]` ("Presence-tier schema is hosted by the same store lifecycle"), and DEL-10-02 `[E-P71]` TESTS ("Kill test exercises store safe-delete semantics", sourced to SOW-055's "delete the store").
- **CLM-007** — The content-minimal rule has a permanent out-of-scope twin: `SOW-073` places "Capture of file or diff content in any PEC surface" `OUT` permanently, with SourceRef "PEC-K-10, §15" and the ledger note naming `SOW-056` as its "ingest-enforcement twin (DL-8)". `SOW-073` states the product boundary; this deliverable produces its ingest-side enforcement.
- **CLM-008** — Ingest paths arrive across phases. At `P1` the live ingest path is the reconciler (PRD §12 P1: "Reconciler + orientation store + API for one loop"; feeds enumerated at `PEC-RCN-002`). Both remaining ingest classes arrive at `P3`: presence and Git-scanning ingest (`PEC-PRS-002`), and event/stream ingest (`PEC-STR-001`: "idempotent, append-only event ingest keyed on event id"), whose owning deliverable `DEL-07-01` carries `PhaseHint` `P3` in `Deliverables.csv` — `DL-14` moved `DEL-03-05` `P4`→`P3` so that ingest is never live without its `PEC-K-07` safety invariant, recorded as constraint row `C-01` `CO_LANDING`. The staging is therefore `P1` reconciler → `P3` presence/Git and event/stream, not a `P4` arrival for the event path; the `P4` members of `PKG-07` (`DEL-07-02`, `DEL-07-04`) are bridges that deliver into the `P3` ingest boundary rather than a later ingest boundary of their own. The guard is the boundary all later paths inherit, not a per-path check re-authored each phase.
- **CLM-009** — The deliverable is at lifecycle state `OPEN` with no implementation present. Every requirement, acceptance criterion, and verification method below states a contract on future production; none asserts that anything has been built.
- **CLM-010** — The system-level kill test is not this deliverable's scope. `SOW-055` — "delete the store, run representative governed workflows, nothing blocks" — is covered by `DEL-10-02` (Kill test, standing release gate), and the accepted edge `[E-P71]` runs `DEL-01-03` → `DEL-10-02` with `EdgeKind` `TESTS`: `DEL-10-02` is the tester and this deliverable is the tested surface. `DEL-10-02` will exercise this deliverable's safe-delete behaviour from outside, against representative governed workflows. This contract binds only the store-local property that makes that outside test possible; it neither runs nor discharges the kill test.
- **TBD-001** — `ResponsibleParty` is unassigned; the register records `TBD`, with assignment at WORKING_ITEMS activation.
- **TBD-002** — The store's concrete on-disk path, filename, and storage engine are not fixed by any accepted source. `PEC-K-02` and `PEC-RCN-001` say "database" without naming a technology, and PRD §7.3 carries "SQL-level append-only enforcement" and "dry-run-then-apply ingestion" explicitly *as pattern, not as code*. These are chosen during production within the bounds of REQ-001, REQ-007, and REQ-008.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The store shall live at a path that is Git-ignored in the hosting checkout. The lifecycle module shall resolve that path deterministically and shall register or verify the ignore rule, so that no store artifact — including any journal, index, temporary, or lock file the storage engine creates — becomes trackable.
- **REQ-002** — The store shall be safe to delete at any moment. The lifecycle module shall provide an explicit delete operation and shall recreate a valid empty store on next start without manual repair. Deletion shall block no governed act, per `PEC-K-01`.
- **REQ-003** — Every write into the store shall pass through one declared ingest boundary. No store write path may bypass the guard, including writes originating inside the service core.
- **REQ-004** — The guard shall admit only the field classes `PEC-K-10` permits — paths, counts, SHAs, states, hashes — and shall reject file content and diff content. Register-row prose (PRD §7.1 DecisionRow) and Git working-tree content (`PEC-PRS-002`) are rejected cases of the same rule.
- **REQ-005** — Guard rejection shall be explicit and located, naming the offending record and field. Silent drop, silent truncation, and silent substitution are prohibited; where a feed cannot be admitted, the limitation shall be stated rather than omitted, per `PEC-ORI-006`.
- **REQ-006** — The guard shall apply uniformly to every ingest path — the `P1` reconciler ingest (`PEC-RCN-002`), and the two `P3` classes, presence and Git scanning (`PEC-PRS-002`) and event/stream ingest (`PEC-STR-001`, owned by `DEL-07-01` at `PhaseHint` `P3`) — so that each `P3` path, and any `P4` bridge delivering into it, inherits the boundary without amending this contract or duplicating the check (CLM-008).
- **REQ-007** — The store lifecycle module and the guard shall introduce no third-party runtime dependency and no external network egress, per `PEC-SVC-001` and `PEC-SVC-002`, whose standing enforcement is `DEL-01-05` covering `SOW-052` and `SOW-053`.
- **REQ-008** — The store lifecycle module shall expose the store to its consumers through an interface that carries no concrete path or storage-engine detail, so that resolving TBD-002 differently, or relocating the store later, changes no consumer deliverable named in CLM-006.
- **REQ-009** — The guard's admissibility test shall be documented as an explicit rule with a stated decision for each record-tier and presence-tier field class it admits, so that CON-001 is answered by a recorded, reviewable rule rather than by implementation accident.
- **REQ-010** — Tests shall implement the verification methods declared in this contract; they shall not define scope, requirements, or acceptance criteria.

- **AC-001** — The store path is Git-ignored: with a populated store present, `git check-ignore` resolves every store artifact to a checked-in ignore rule and `git status` reports no tracked or untracked store artifact in the hosting checkout.
- **AC-002** — With the store deleted — both while PEC is stopped and while it is running — the next start recreates a valid empty store without manual repair, and no operator step, migration, or repair command is needed to reach that state. Whether deletion blocks a governed act is the system-level property `DEL-10-02` tests from outside under `SOW-055` (CLM-010); it is not asserted, exercised, or discharged here.
- **AC-003** — Every store write path routes through the declared ingest boundary; inspection of the store module's write surface finds no persistence call that reaches the store without passing the guard.
- **AC-004** — A fixture corpus carrying file content, diff hunks, and register-row prose is rejected at ingest, and inspection of every persisted field afterwards finds no file or diff content residue anywhere in the store.
- **AC-005** — Each rejection is explicit and names the offending record and field; input records are accounted for as accepted or rejected with no unreported difference, and no ingest silently drops, truncates, or substitutes.
- **AC-006** — Reconciler-shaped, presence-shaped, and event-shaped ingest exhibit identical rejection behavior against the same fixtures, and adding an ingest path of a new shape requires no new content check.
- **AC-007** — The lifecycle module and the guard add no third-party runtime dependency and make no network call, leaving the DEL-01-05 zero-dependency and locality assertion intact.
- **AC-008** — The consumer-facing store interface exposes no store path or storage-engine detail in its signature, so that changing either changes no consumer deliverable.
- **AC-009** — The guard's admissibility rule is documented field class by field class, and each documented decision either cites an accepted source or is marked as an open question routed under CON-001; no field class is admitted without a recorded decision.
- **AC-010** — The automated test suite implements VER-001 through VER-008, executes in the service-core test run, passes, and introduces no acceptance criterion absent from this contract.

- **CON-001** — `PEC-K-10` enumerates the admissible classes as "paths, counts, SHAs, states, hashes — never file or diff content", but no accepted source states the test that separates an extracted state token from a prose excerpt when the source itself is prose. PRD §7.1 settles exactly one case (DecisionRow: identity and status only, never the row's prose) while recording that "the pec/bridge ledgers are prose-structured with no validated schema", and that receipts are ingested from them under stated coverage limits. The boundary for prose-structured feeds is therefore unresolved at the level of accepted truth. This contract requires the decision to be recorded (REQ-009, AC-009); it does not resolve it. A resolution that changes what the store may hold is a scope change, routed through SCOPE_CHANGE or an owner ruling, not a production choice.

## Production and Verification Method — Praxeology

Production proceeds in the order store path and lifecycle → guard →
consumer-facing interface → tests, because each stage is the acceptance
surface of the next: the guard cannot be the single boundary until there is
exactly one store to write to, and the interface cannot hide TBD-002 until
both exist. All work is bounded to the deliverable folder and the service-core
source it names; this contract authorizes no register, decomposition, or PRD
edit.

- **VER-001** — Populate the store, then run `git check-ignore` and `git status --porcelain` over its artifacts and inspect the checked-in ignore rule, asserting that every artifact the engine creates resolves to that rule.
- **VER-002** — Delete the store while PEC is stopped and again while it is running, restart, and assert that a valid empty store is recreated without manual repair and without any operator repair step. Scope boundary: this method exercises the store lifecycle locally only. Running representative governed workflows and asserting that none blocks is the kill test owned by `DEL-10-02` under `SOW-055` (CLM-010), reached through edge `[E-P71]` from outside this deliverable; it is not performed here and no result of this method may be presented as having satisfied it.
- **VER-003** — Inspect the store module's write surface and import/call graph and assert that every persistence call reaches the store only through the guard entry point.
- **VER-004** — Ingest a fixture corpus containing file content, diff hunks, and register-row prose; assert rejection at ingest, then dump every persisted field and assert no content residue.
- **VER-005** — Assert that each rejection emits an explicit located failure naming record and field, and reconcile input record counts against accepted-plus-rejected counts to prove no silent drop or truncation.
- **VER-006** — Exercise reconciler-shaped, presence-shaped, and event-shaped ingest with the same fixture corpus and assert identical rejection behavior; confirm by construction that a further ingest shape requires no new content check.
- **VER-007** — Inspect the service-core dependency manifest and the store and guard import graphs for third-party runtime dependencies and network calls, and inspect the consumer-facing interface signature for store-path or engine leakage; re-run the `DEL-01-05` locality and zero-dependency enforcement once that deliverable is available.
- **VER-008** — Review the documented admissibility rule against the record-tier and presence-tier field inventories of PRD §7.1 and §7.2 and assert that every admitted field class carries a recorded decision with either an accepted-source citation or a CON-001 routing.
- **VER-009** — Run the service-core test suite and confirm that each of VER-001 through VER-008 has a corresponding executing automated test and that no test asserts a criterion absent from this contract.

## Governing Values and Decisions — Axiology

- **AX-001** — `PEC-K-01` graceful absence governs: no governed act may require a PEC read or write, and deleting PEC blocks nothing. Safe-delete is not a convenience feature here; it is the behavior `OBJ-005` names, and the store lifecycle is where it is either true or false.
- **AX-002** — `PEC-K-02` files govern: the store is a rebuildable projection of file truth, never an alternative source of truth. Its gitignored path is the structural expression of that status — content that is not tracked cannot be cited as a governed record.
- **AX-003** — `PEC-K-10` content-minimal is a residency posture, not a storage optimization. PRD §15 states the standard it protects: "PEC indexes only repo files agents already read, plus operational presence; no new data class egresses." `SOW-073` makes the boundary permanent and out of scope; this deliverable is its ingest-side enforcement per `DL-8`.
- **AX-004** — Enforcement duties are separated across deliverables and this contract produces only its own: the standing kill-test gate is `DEL-10-02` (`SOW-055`), the reconciler write restriction is `DEL-03-01` (`SOW-021`, `PEC-RCN-006`), zero-dependency and locality enforcement is `DEL-01-05` (`SOW-052`, `SOW-053`), and ingest-activity logging is `DEL-01-04` (`SOW-057`, serving `OBJ-006`). Nothing here discharges those obligations.
- **AX-005** — `C-04` PHASE_PRECEDENCE and `C-10` STRATUM_RULE are register-wide non-gating constraints. The `P1`→`P3` ingest-path progression in CLM-008 is release-strategy ordering, not authority over what the guard must cover. The four consumer edges in CLM-006 are `PROPOSAL` stratum and are *accepted* at that stratum: `D-PEC-62` §1.4 records the owner accepting the DAG candidate "all strata as presented", so nothing about these four edges is pending. What remains recorded-but-unresolved under that same ruling is the set of specific flag annotations it names — `E-A11`, `E-P69`/`E-N02`, `E-N13`/`E-N18`, the `C-02` direction, and the `C-08` standing-node set — none of which attaches to any edge cited in this contract. Stratum is provenance, not authority.
- **AX-006** — `PEC-ORI-006` honesty governs the guard's failure mode: a feed that cannot be admitted is reported, never quietly narrowed. A guard that silently discards is indistinguishable from a guard that works, and `OBJ-005`'s deletability claim is only as trustworthy as the record of what was refused.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-056 OBJ-005 | REQ-001, REQ-002, REQ-007, REQ-008, CLM-005, CLM-010, TBD-002 | AC-001, AC-002, AC-007, AC-008 | VER-001, VER-002, VER-007 | Ignore-rule inspection and `git check-ignore`/`git status` output over a populated store; delete-and-restart transcripts for the stopped and running cases showing recreation without manual repair (the governed-workflow kill test is DEL-10-02's evidence under SOW-055, not this deliverable's); dependency-manifest and import-graph inspection records; the consumer-facing interface signature |
| OUT-002 | SOW-056 OBJ-005 | REQ-003, REQ-004, REQ-005, REQ-006, REQ-007, REQ-009, CLM-004, CLM-007, CLM-008, CON-001 | AC-003, AC-004, AC-005, AC-006, AC-007, AC-009 | VER-003, VER-004, VER-005, VER-006, VER-007, VER-008 | Write-surface and import-graph inspection showing a single guard entry point; the rejection fixture corpus with per-fixture outcomes; a full persisted-field dump showing no content residue; rejection transcripts naming record and field; input-versus-accepted-plus-rejected count reconciliation; the documented admissibility rule with per-field-class decisions and citations |
| OUT-003 | SOW-056 OBJ-005 | REQ-010, CLM-009 | AC-010 | VER-009 | Service-core test-run output mapping each executed test to its declared verification method |
