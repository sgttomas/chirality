---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-01-01
package_id: PKG-01
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@3623b958b
project_scope_refs: [SOW-001]
package_objective_refs: [OBJ-001, OBJ-002]
---

# Scope of Work — DEL-01-01 Record-tier schema & entity model

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-01-01` — "Record-tier
schema & entity model" — in `PKG-01` Service Core & Store of the PEC v2 build.
It covers project scope item `SOW-001` in service of package objectives
`OBJ-001` and `OBJ-002`.

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.2** (`current_basis`, SCA-002 successor; commit `3623b958b`).
The deliverable-local `_REFERENCES.md` still names "revision 1.1, accepted
working surface". That phrase is superseded provenance left by a deferred
pointer sweep (SCA-002 `Handoff_State.md` §6); `_CONTEXT.md`'s own supersession
line records revision 1.1 as "superseded by revision 1.2 (`current_basis`,
SCA-002 successor)". This contract cites revision 1.2.

**Objective warrant.** The `DEL-01-01` → `OBJ-001;OBJ-002` attribution is
SCA-002-qualified, not pre-existing register truth. Before SCA-002 the
`ObjectiveIDs` cell of ledger row `SOW-001` was empty — action `A001` records
"All cells currently empty; only this column changes on these rows" — and §3's
`MappedDeliverables` for `OBJ-001` and `OBJ-002` did not name `DEL-01-01`
(`A003b` old-text pairs: `OBJ-001` col5 "DEL-04-01..05, DEL-08-03, DEL-08-04,
DEL-10-01, DEL-10-04"; `OBJ-002` col5 "DEL-03-02, DEL-03-03, DEL-04-02,
DEL-04-03"). SCA-002 added `SOW-001` → `OBJ-001;OBJ-002` (`A001`), derived the
`DEL-01-01` cell from it "by the union invariant, not authored independently"
(`A002`), and added `DEL-01-01` to both §3 rows (`A003b`).

The qualification is recorded in
`execution/_ScopeChange/SCA-002_2026-07-25_1042/Amendment_Preview.md` under
"The INDIRECT-8 (`DEL-01-01` + `DEL-02-01..07`) — Q2". Its warrant is a
derivation §3 already carried: *"parser items (SOW-011..017) underlie
OBJ-001/OBJ-002 through the record tier (SOW-001)"*. The recommendation reads:
*"Recommended — AFFIRM `[OBJ-001, OBJ-002]` for all eight: it applies the
accepted §3 rationale rather than superseding it."*

**Strength of that record, stated at the strength it has.** The confidence
labels in the packet (HIGH through LOW) attach to the **nine per-row
attributions batched into Q1/Q5**, and `DEL-01-01` is not among them; the
INDIRECT-8 is a separate class routed as **Q2**, and the record assigns it no
confidence label. What the record does carry is a stated and evidenced
alternative, decision `D-17` of `Decision_Log.md`, whose two cells read in
full — Decision: *"INDIRECT-8 recommended at the full `[OBJ-001, OBJ-002]` set,
**with the narrower alternative stated and evidenced**"*; Rationale: *"§3's
derivation is explicit about the set, and applying it is faithful to accepted
rationale. But my own measurement shows OBJ-002's register locus is the
reconciler layer (`SOW-006/018/019`), which genuinely supports a
parsers-are-`OBJ-001`-only reading. The owner should choose knowingly rather
than inherit my preference."* Both cells are quoted without elision, including
the Rationale's pro-AFFIRM opening clause. The alternatives were
defined exactly: **N1** — "seven parsers → `OBJ-001`; `SOW-001` keeps both" —
and **N2** — "all eight → `OBJ-001`".

The owner ruled the question at Gate 3 with those alternatives in front of
them: *"Q2 | INDIRECT-8 breadth | **AFFIRM** `OBJ-001;OBJ-002` for all eight
(not N1, not N2)"*, and the Gate 3 record adds that "the Part 0 contingency
does not fire" and "the Gate 3 text is the **only** text Gate 5 may apply".
Two consequences for this contract. First, the attribution is **ruled, not
pending**: it is not a MEDIUM-or-weaker recommendation awaiting confirmation,
so this contract creates no owner-confirmation acceptance criterion for it and
supplies no fresh derivation of it. Second, `SOW-001` is the one member of the
eight whose mapping is invariant under the narrower alternative that was
argued: under **N1**, `SOW-001` keeps both objectives. Only **N2** would have
reduced this deliverable to `OBJ-001` alone, and **N2** was declined.

- **CLM-001** — `SOW-001` states, verbatim from `execution/_Decomposition/ScopeLedger.csv` (columns `ScopeItemID,InOutStatus,ScopeItemStatement,SourceRef,PackageID,DeliverableIDs,ObjectiveIDs,DecisionRef,OpenIssue,Notes`): `SOW-001,IN,"Implement the record-tier entity model: Loop, Workplan/Step/Gate, Receipt, DecisionRow, Fence, Package/Deliverable, DependencyEdge, RunRecord, CandidateBrief, OrientationSnapshot, DriftFinding",§7.1,PKG-01,DEL-01-01,OBJ-001;OBJ-002,,FALSE,Receipt field availability is per-loop (PEC-ORI-006 limits apply)`. The `DecisionRef` field is empty and `OpenIssue` is `FALSE`: no open issue rides this scope item.
- **CLM-002** — `OBJ-001` states: "Orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation" (`SOFTWARE_DECOMP.md` §3, `SourceRef` §3.1; `projects/pec/docs/PRD.md` §3 outcome 1). Its mapped scope items at revision 1.2 are "SOW-001, SOW-003, SOW-004..009, SOW-011..017, SOW-040..043, SOW-089; instruments: SOW-058, SOW-059".
- **CLM-003** — `OBJ-002` states: "Staleness is detected structurally by SHA comparison, never by judgment" (`SOFTWARE_DECOMP.md` §3, `SourceRef` §3.2; `PRD.md` §3 outcome 2). Its mapped scope items at revision 1.2 are "SOW-001, SOW-006, SOW-011..019; supported by SOW-005".

## Deliverable Definition — Ontology

- **OUT-001** — A record-tier store schema (DDL) providing persistence for the fourteen record-tier entity types, expressed as one cohesive slice.
- **OUT-002** — A typed entity model in the PEC service core: the fourteen entity types with their fields, provenance carriers, and relationships, defined separately from the store persistence of OUT-001.
- **OUT-003** — Model tests implementing the verification methods declared in this contract.

### Identity of record

- **CLM-004** — `DEL-01-01` is named "Record-tier schema & entity model", Type `DATA_MODEL_CHANGE`, Context Envelope **`L`**, `PhaseHint` `P1`, `ResponsibleParty` `TBD`, `CoversScopeItems` `SOW-001`, `SupportsObjectives` `OBJ-001;OBJ-002`, with `AnticipatedArtifacts` "Schema/DDL + entity types + model tests"; sources `execution/_Decomposition/Deliverables.csv` row `DEL-01-01` and `SOFTWARE_DECOMP.md` §5 PKG-01 table ("| DEL-01-01 | Record-tier schema & entity model | DATA_MODEL_CHANGE | **L** | P1 | SOW-001 |"). The three outputs above are that artifact list and nothing beyond it.
- **CLM-005** — The register description of record is: "Store schema and typed entity model for the record tier: 11 PRD rows, 14 entity types (Workplan/Step/Gate and Package/Deliverable are compound rows) — Loop, Workplan, Step, Gate, Receipt, DecisionRow, Fence, Package, Deliverable, DependencyEdge, RunRecord, CandidateBrief, OrientationSnapshot, DriftFinding." The fourteen types are register truth and are carried here exactly, none added and none dropped. `DL-14` records the enumeration's history: "DEL-01-01 re-enveloped M→L (14 entity types, not '11 entities')".
- **CLM-006** — The eleven PRD rows behind those fourteen types are `PRD.md` §7.1 "Record tier (reconciled from file truth; citable with sources)", each with its stated purpose: Loop ("Tenancy unit, above Project: a LOOP_INIT/workplan-governed work loop (root, app-dev, piping, pec, bridge, …)"); Workplan / Step / Gate ("The standing plan's protocol steps and owner gates, with gate state"); Receipt ("Parsed `LOOP_RECEIPTS.md` entries", with per-loop field availability); DecisionRow ("Register-row identity and status only (decision ID, packet path, anchor, state — never the row's prose; PEC-K-10)"); Fence ("Declared write-scope constraints from rulings and briefs"); Package / Deliverable ("Lifecycle census from `_STATUS.md` (OPEN→ISSUED), stuck-age, remaining items"); DependencyEdge ("From `Dependencies.csv` registers and `WORK_GRAPH.json`"); RunRecord ("Summaries of checkout-contained AgentRun evidence (`STATUS.json`, `RUNTIME_SUMMARY.json` under `execution/**`)", with runtime-daemon user-data state excluded); CandidateBrief ("Adopted-but-unexecuted and proposed briefs (the work-selection queue)"); OrientationSnapshot ("A generated orientation return, stamped with examined SHA — the machine generalization of a receipt"); DriftFinding ("A classified difference between the current reconcile and the prior snapshot, or between PEC and harness parity output").
- **CLM-007** — The envelope note of record, carried in `Deliverables.csv` `ContextEnvelopeNotes`, `_CONTEXT.md`, and `ContextBudgetQA.csv`, is: "L: 14 entity types and the schema every derivation package depends on; kept one cohesive DDL slice — split (core record entities vs lifecycle/dependency/run entities) only if implementation shows a natural seam". `ContextBudgetQA.csv` rates the deliverable `MEDIUM` risk with `RecommendedAction` "Hold as L; split by per-loop grammar if any loop proves adversarial", and §8 records it as one of exactly two `L` deliverables, "the dependency of every derivation package", with "named split lines if implementation demands them". This is a production constraint on how the work is sliced; it is not additional scope.

### Placement in the work graph

- **CLM-008** — `DEL-01-01` has exactly one `EXECUTION` upstream edge. `Dependencies.csv` row `DEP-01-01-003` records it: predecessor `DEL-00-01` "v2 first ADRs (core isolation + carried postures)" at `PKG-00`, `DependencyType` `PREREQUISITE`, `Statement` "The ADR ruling shapes the PKG-01 schema/persistence seam", `Explicitness` `IMPLICIT`, `RequiredMaturity` `INITIALIZED`, `SatisfactionStatus` `PENDING`, `Confidence` `MEDIUM`, `Origin` `EXTRACTED`, `Notes` "PROPOSAL; Flag=none; EdgeID=E-P01". Its evidence quote is: "OI-012: core-isolation style ""Decided in DEL-00-01's ADR""; ""the one seam to keep crisp is entity schema (core) vs store persistence (adapter) inside PKG-01""". The two remaining rows in that register are `ANCHOR` rows: `DEP-01-01-001` (package-local to `PKG-01`) and `DEP-01-01-002` (`SOW-001` requirement trace).
- **CLM-009** — `DEL-00-01` is at lifecycle state `INITIALIZED`, which is the maturity `[E-P01]` requires. `INITIALIZED` means its **contract** is the reliable input: `DEL-00-01`'s accepted `ScopeOfWork.md` exists, and no ADR does. That contract's own text records "No ADR exists for this deliverable at the time of writing; `_STATUS.md` records state `OPEN`" as of its authoring. The elements this contract binds to are its contractual obligations, not artifacts: `DEL-00-01/REQ-006` — "The ADR set shall make explicit the seam identified as the one to keep crisp: entity schema (core) versus store persistence (adapter) inside `PKG-01`"; `DEL-00-01/AC-005` — "The ADR set states the entity-schema versus store-persistence seam inside PKG-01 explicitly enough that a reader can classify a candidate PKG-01 change as core or adapter"; and `DEL-00-01/REQ-009`, which obliges the published ADRs to be consumable by `DEL-01-01` "via `[E-P01]` ... so that if and when either proposed edge is taken up, no republication is needed". Every ID-shaped token in this enumeration and its quotations is upstream `DEL-00-01` source context, not a local definition or reference: this contract's own `REQ-006`, `AC-005`, and `REQ-009` are separate and differently worded. Nothing in this contract asserts that any ADR has been authored or that any core-isolation style has been chosen.
- **CLM-010** — Eleven downstream consumer relations are recorded against this deliverable in `_DEPENDENCIES.md`, all `CONSUMES` at `PROPOSAL` stratum and all unflagged: `DEL-02-01` `[E-P03]`, `DEL-02-02` `[E-P04]`, `DEL-02-03` `[E-P05]`, `DEL-02-04` `[E-P06]`, `DEL-02-05` `[E-P07]`, `DEL-02-06` `[E-P08]`, `DEL-03-01` `[E-P10]`, `DEL-04-01` `[E-P11]`, `DEL-05-01` `[E-P12]`, `DEL-05-02` `[E-P13]`, `DEL-07-05` `[E-P14]`. That section is marked informational. Register-wide constraint `C-03` `PACKAGE_LEVEL` states "Every PKG-03/04/05 deliverable depends on DEL-01-01 directly or transitively"; the gate exhibit records the `[E-P10]`-class basis as "package-level accepted; deliverable pairing proposed — constraint C-03". Phase staging, checked against the `PhaseHint` column of every deliverable named here: this deliverable is `P1`; its upstream `DEL-00-01` is `pre-P1`; its recorded consumers are `P1` (`DEL-02-01` through `DEL-02-06`, `DEL-03-01`, `DEL-04-01`), `P2` (`DEL-05-01`, `DEL-05-02`), and `P3` (`DEL-07-05`). No recorded consumer precedes this deliverable's phase.

### Boundaries

- **CLM-011** — The record tier is one of two tiers that `PEC-K-05` requires never be blurred: "Record tier: reconciled from file truth, per-claim citations. Presence tier: TTL'd, heartbeat-aged, evaporating, honesty-labeled. Presence facts never enter record-tier citations." The presence-tier entity model — Session, Worktree/GitRef, PresenceRecord, HierarchyEdge, ScopeClaim — is `SOW-002`, covered by `DEL-01-02` at `PhaseHint` `P3` with the ledger note "Operational only; never citable (C4)". It is not produced here.
- **CLM-012** — The acts that consume this model are owned by other deliverables and are cited here, never discharged: parsing the file feeds that populate these entities is `DEL-02-01` through `DEL-02-07` (`SOW-011`..`SOW-017`); stamping every orientation response with examined-through SHA, generation time, per-feed freshness and attaching a citation to every claim is `DEL-04-03` (`SOW-006`, `SOW-007`, carrying `PEC-K-04`); incremental reconciliation keyed on Git delta is `DEL-03-02` (`SOW-018`) and drift classification is `DEL-03-03` (`SOW-019`); full rebuild by one command is `DEL-03-01` (`SOW-010`); the gitignored store and its ingest-boundary content-minimal guard are `DEL-01-03` (`SOW-056`); standing zero-dependency and locality enforcement is `DEL-01-05` (`SOW-052`, `SOW-053`); the standing kill test is `DEL-10-02` (`SOW-055`). This contract produces only the schema, the entity types, and their model tests.
- **CLM-013** — The deliverable is at lifecycle state `OPEN` with no implementation present. Every requirement, acceptance criterion, and verification method below states a contract on future production; none asserts that anything has been built.
- **TBD-001** — `ResponsibleParty` is unassigned; the register records `TBD`, with assignment at WORKING_ITEMS activation, not in this contract (`SOFTWARE_DECOMP.md` §5 preamble; `_CONTEXT.md`).
- **TBD-002** — The storage engine and DDL dialect are not fixed by any accepted source. `PEC-K-02` and `PEC-RCN-001` say "database" without naming a technology, and `PRD.md` §7.3 carries "SQL-level append-only enforcement" and "dry-run-then-apply ingestion" explicitly as pattern, "not as code". The store's concrete on-disk path and engine are the open question of `DEL-01-03`'s own contract, and no accepted dependency edge is recorded between `DEL-01-01` and `DEL-01-03` in either deliverable's local register; this contract therefore states no ordering claim between them and requires only that the choice be made within REQ-009 and REQ-011.
- **CON-001** — `OI-012` — core isolation style, "ports-and-adapters (hexagonal) vs functional-core/imperative-shell" — is **undecided**. `SOFTWARE_DECOMP.md` §Open Issues dispositions it "Decided in DEL-00-01's ADR; owner review at that ADR", and the same row records that "the one seam to keep crisp is entity schema (core) vs store persistence (adapter) inside PKG-01". `[E-P01]`'s own evidence quote is that sentence. This contract records the open issue and requires the seam to be honoured; it selects no style, and no selection may be inferred from this document. A resolution arrives through `DEL-00-01`'s ADR and its owner review, not through a production choice made here.
- **CON-002** — Receipt field availability is unresolved at the level of accepted truth for non-app-dev ledgers. `PRD.md` §7.1 records that "the app-dev ledger carries the D-APP-57 contract (Receipt-ID, Examined-Through SHA, Parent-Receipt, Gate-Outcome); the pec/bridge ledgers are prose-structured with no validated schema — coverage limits stated per PEC-ORI-006", and the `SOW-001` ledger note repeats "Receipt field availability is per-loop (PEC-ORI-006 limits apply)". `OI-008` records the undecided question — "§16.8 receipt-contract adoption by non-app-dev ledgers undecided" — with disposition "§16 ruling (per-loop)". This contract requires the Receipt type to represent availability explicitly (REQ-008) so the limitation is statable; it does not resolve `OI-008`, and an implementation that assumes universal adoption of the `D-APP-57` field set would pre-empt an owner ruling.

## Completion and Reliance Basis — Epistemology

The requirements below state what future production must satisfy. Nothing in
this section asserts that a schema, an entity type, or a test exists.

- **REQ-001** — The schema and entity model shall define exactly the fourteen record-tier entity types named in CLM-005 — Loop, Workplan, Step, Gate, Receipt, DecisionRow, Fence, Package, Deliverable, DependencyEdge, RunRecord, CandidateBrief, OrientationSnapshot, DriftFinding — with none added and none dropped, and each type shall carry a recorded trace to its `PRD.md` §7.1 row and stated purpose (CLM-006).
- **REQ-002** — The two compound `PRD.md` §7.1 rows shall be decomposed exactly as the register records: Workplan / Step / Gate as three distinct types carrying the standing plan's protocol steps, owner gates, and gate state; Package / Deliverable as two distinct types carrying the lifecycle census (`OPEN`→`ISSUED`), stuck-age, and remaining items.
- **REQ-003** — Every record-tier entity type shall carry provenance sufficient for a per-claim citation to its live source — file path, anchor, and/or SHA, per `PEC-ORI-004` — because §7.1 defines the tier as "citable with sources". The act of attaching citations to an orientation response is `DEL-04-03`'s under `SOW-007` (CLM-012); this requirement obliges the model to hold what that act needs, and no more.
- **REQ-004** — The model shall represent examined-through SHA provenance structurally, so that staleness is a comparison and never a judgment (`PEC-K-04`, `OBJ-002`): OrientationSnapshot shall be stamped with the examined SHA, and two successive snapshots shall be comparable field by field such that a DriftFinding can record a classified difference. Performing that comparison is `DEL-03-02`'s and `DEL-03-03`'s (CLM-012); the model shall not require a human or agent judgment input for any field on which staleness turns.
- **REQ-005** — Every record-tier entity shall be fully regenerable from file sources. No record-tier field may hold state that cannot be reproduced by rebuilding from the same sources, per `PEC-K-02` ("The record tier is regenerated from sources by one command") and `PEC-RCN-001`. The rebuild command itself is `DEL-03-01`'s under `SOW-010`.
- **REQ-006** — No presence-tier entity shall be defined by this deliverable (`PEC-K-05`, CLM-011). RunRecord shall admit only summaries of checkout-contained AgentRun evidence (`STATUS.json`, `RUNTIME_SUMMARY.json` under `execution/**`); runtime-daemon state under user data is operational and non-authoritative per `D-GOV-20` §5, is never record-tier citable, and shall not be representable in this schema.
- **REQ-007** — No field of any type shall admit file content or diff content (`PEC-K-10`: "Paths, counts, SHAs, states, hashes — never file or diff content"). DecisionRow shall carry register-row identity and status only — decision ID, packet path, anchor, state — and shall have no field capable of holding the row's prose. Enforcement at the ingest boundary is `DEL-01-03`'s guard under `SOW-056`; this requirement binds the shape of the schema so that the guard has nothing to admit into.
- **REQ-008** — The Receipt type shall represent field availability explicitly per loop, so that a coverage limitation can be stated rather than silently omitted (`PEC-ORI-006`: "Where a feed is unparseable or stale, the response shall state the measurement limitation explicitly; silent omission is prohibited"). The representation shall accommodate both the `D-APP-57` field set and prose-structured ledgers with no validated schema, without presupposing any outcome of `OI-008` (CON-002).
- **REQ-009** — The entity types (core) shall be defined separately from the store persistence (adapter), the seam `DEL-00-01`'s accepted contract obligates its ADR to state explicitly (`DEL-00-01/REQ-006` and `DEL-00-01/AC-005`, CLM-009). The definitions shall not presuppose a resolution of `OI-012` and shall remain valid under either candidate isolation style (CON-001). Dependency shall run from persistence to types, never the reverse.
- **REQ-010** — The schema and entity model shall introduce no third-party runtime dependency and no external network egress, per `PEC-SVC-001` and `PEC-SVC-002`, whose standing enforcement is `DEL-01-05` covering `SOW-052` and `SOW-053`.
- **REQ-011** — The work shall be delivered as one cohesive DDL slice. A split is permitted only along the recorded line — core record entities versus lifecycle, dependency, and run entities — and only where implementation shows a natural seam; the seam and its evidence shall be recorded with the split (CLM-007). A split changes no other term of this contract, adds no output, and requires no register amendment.
- **REQ-012** — The schema and entity model shall be published within `PKG-01` such that the eleven recorded consumers of CLM-010 could consume them as dependency inputs under their proposed edges without republication. This is stated relative to those proposed edges; it asserts no accepted obligation on any named consumer and no `DECLARED` stratum for any edge. Production shall write into no other package (`DL-12`: "a deliverable never writes into another package").
- **REQ-013** — Model tests shall implement the verification methods declared in this contract; they shall not define scope, requirements, or acceptance criteria.

- **AC-001** — The delivered model contains exactly the fourteen named entity types and no additional record-tier type; each carries a recorded trace to its `PRD.md` §7.1 row; and the two compound rows are decomposed as REQ-002 states.
- **AC-002** — Every entity type carries citation provenance, and for a sample instance of each type the recorded provenance resolves to a live file source by path, anchor, and/or SHA.
- **AC-003** — OrientationSnapshot carries an examined-through SHA; two successive snapshots built from different source states are comparable field by field and yield a classified difference representable as a DriftFinding; and no field on which that comparison turns requires a judgment input.
- **AC-004** — A full rebuild from the same sources reproduces every record-tier entity instance, and inspection finds no record-tier field holding state that the rebuild cannot reproduce.
- **AC-005** — No presence-tier entity is defined in this schema, and a fixture carrying runtime-daemon user-data state is not representable as a RunRecord.
- **AC-006** — No field type admits file or diff content; DecisionRow has no prose-bearing field; and a fixture carrying file content, diff hunks, and register-row prose cannot be expressed in the model.
- **AC-007** — Receipt field availability is explicit per loop: the `D-APP-57` field set and a prose-structured ledger with no validated schema are both representable, the difference between them is readable from the model rather than inferred, and no `OI-008` outcome is presupposed.
- **AC-008** — The entity type definitions have no dependency on any store-persistence module; the persistence layer depends on the types and not the reverse; a reviewer can classify a candidate `PKG-01` change as core or adapter using the delivered structure; and no element of the model selects a core isolation style.
- **AC-009** — The schema and entity model add no third-party runtime dependency and make no network call, leaving the `DEL-01-05` zero-dependency and locality assertion intact.
- **AC-010** — The work is delivered as one cohesive slice, or as a split along the recorded line accompanied by a recorded statement of the natural seam that justified it; no other split line is used.
- **AC-011** — The schema and entity model are consumable as dependency inputs by the eleven recorded consumers without republication, and the change set touches no path outside `PKG-01`.
- **AC-012** — The model tests implement VER-001 through VER-011, execute in the service-core test run, pass, and assert no criterion absent from this contract.

## Production and Verification Method — Praxeology

Production proceeds in the order entity types → persistence schema → tests,
because that order is what REQ-009 requires to be visible in the result: types
that were authored before any persistence exists cannot have acquired a
dependency on it. The fourteen types are enumerated from CLM-005 and grounded
row by row against `PRD.md` §7.1 before any field is designed, so that REQ-001
is satisfied by construction rather than audited afterwards. All work is
bounded to the deliverable folder and the `PKG-01` service-core source it
names; this contract authorizes no register, decomposition, or PRD edit. Tests
implement the verification methods below and create no scope.

- **VER-001** — Inventory check: enumerate the delivered types and diff them against the fourteen names of CLM-005 and the eleven rows of `PRD.md` §7.1, asserting the recorded per-type trace and the compound-row decomposition of REQ-002.
- **VER-002** — Provenance resolution: for a sample instance of each type, resolve the recorded citation provenance to a live file source and assert that path, anchor, and/or SHA are present and locatable.
- **VER-003** — Snapshot comparison exercise: build two OrientationSnapshots over different source states, compare them structurally, and assert that the difference is expressible as a DriftFinding with no judgment input. The exercise is read-only over sources; it performs no reconciliation act owned by `DEL-03-02` or `DEL-03-03`.
- **VER-004** — Rebuild-and-compare: regenerate the record tier from the same fixture sources and assert instance-level reproduction, then inspect the field inventory for any state the rebuild cannot reproduce.
- **VER-005** — Tier-boundary inspection: assert no presence-tier type is present, and attempt to represent runtime-daemon user-data state as a RunRecord, asserting that the model rejects it.
- **VER-006** — Content-minimal type inspection: review every field's type for capacity to hold file or diff content, and attempt to express a fixture carrying file content, diff hunks, and register-row prose, asserting that it cannot be expressed.
- **VER-007** — Receipt availability review: model the `D-APP-57` field set and a prose-structured `LOOP_RECEIPTS.md` shape against the Receipt type and assert that per-loop availability is readable from the model and that neither shape is privileged by construction.
- **VER-008** — Seam inspection: inspect the import and dependency graph between the entity types and any persistence module, asserting one-way dependency, and run a classification exercise in which a reviewer sorts candidate `PKG-01` changes into core and adapter using the delivered structure alone.
- **VER-009** — Dependency and locality inspection: review the service-core dependency manifest and the model's import graph for third-party runtime dependencies and network calls; re-run the `DEL-01-05` enforcement once that deliverable is available, without discharging it here.
- **VER-010** — Slice review: compare the delivered artifact structure against the envelope note of CLM-007, asserting either a single cohesive slice or a split along the recorded line with its seam evidence recorded.
- **VER-011** — Consumability and write-scope check: confirm that the published schema and types could be referenced as dependency inputs by the eleven consumers of CLM-010 without republication, and that the change set touches no path outside `PKG-01`.
- **VER-012** — Test-run mapping: run the service-core test suite and confirm that each of VER-001 through VER-011 has a corresponding executing automated test and that no test asserts a criterion absent from this contract.

## Governing Values and Decisions — Axiology

- **AX-001** — `OBJ-001` governs: orientation is a sub-second query with per-claim citations. Entities in this tier exist in order to be cited, so provenance is a structural property of the model rather than a downstream decoration. A type that cannot say where it came from cannot serve a cited orientation, whatever else it holds.
- **AX-002** — `OBJ-002` governs: staleness is detected structurally by SHA comparison, never by judgment. The schema is where that is made possible or impossible; a field that requires interpretation to compare converts a structural check into a judgment call and defeats the objective at its foundation.
- **AX-003** — `PEC-K-05` governs the tier boundary: two trust tiers, never blurred, and "Presence facts never enter record-tier citations". The boundary is enforced here by what the schema is unable to express, not by convention downstream.
- **AX-004** — `PEC-K-02` governs status: files govern, and the record tier is a projection regenerated from sources. This schema is never an alternative source of truth, and `PEC-K-08` extends the same discipline to derivation — "Every status, verdict, and warning carries rule ID, threshold, and contributing cited sources. Drill-down never dead-ends" — which is only achievable if the model carries the sources to drill into.
- **AX-005** — `PEC-K-10` content-minimal is a residency posture, not a storage optimization. The strongest available enforcement for a data model is inexpressibility, which is why REQ-007 binds field shape rather than ingest behaviour; the ingest-side guard is `DEL-01-03`'s.
- **AX-006** — The accepted basis is `SOFTWARE_DECOMP.md` revision 1.2 at commit `3623b958b`, accepted through SCA-002 under `D-PEC-64`. The revision 1.1 phrase in `_REFERENCES.md` is superseded provenance from a deferred pointer sweep, not a competing authority.
- **AX-007** — `C-10` `STRATUM_RULE` is a register-wide non-gating constraint whose own text ends "strata are provenance not authority". Every edge cited in this contract — the upstream `[E-P01]` and the eleven downstream edges of CLM-010 — is `PROPOSAL` stratum and is *accepted* at that stratum: `D-PEC-62` §1(4) records the owner accepting the DAG candidate "accepted, all strata as presented", read in that packet as taking the exhibit's **flags as flags**. None of the flag annotations that ruling leaves recorded-but-unresolved (`E-A11`, `E-P69`/`E-N02`, `E-N13`/`E-N18`, the `C-02` direction, the `C-08` standing-node set) attaches to any edge cited here; all twelve carry `Flag=none`. `PROPOSAL` is not converted to `DECLARED` by citation, and no edge is read as an obligation on another deliverable.
- **AX-008** — Edge direction is respected in both directions. Upstream, `[E-P01]` makes `DEL-00-01`'s ADR ruling an input that shapes this deliverable's seam; it does not transfer the ADR authoring, the `OI-012` decision, or its owner review into this contract. Downstream, the eleven consumer edges make this model an input to other deliverables; they impose no duty on those consumers and grant this contract no authority over them. The enforcement and test duties named in CLM-012 — `DEL-01-05`'s locality enforcement, `DEL-10-02`'s kill test, `DEL-03-01`'s rebuild command, `DEL-01-03`'s ingest guard, `DEL-04-03`'s stamping — are cited here and discharged nowhere in this contract.
- **AX-009** — Unknowns stay marked. TBD-001, TBD-002, CON-001, and CON-002 are recorded rather than resolved by inference. `OI-012` is decided at `DEL-00-01`'s ADR under owner review, and `OI-008` is a per-loop `§16` ruling; a production choice that settles either would be a decision taken in the wrong place.
- **AX-010** — This contract is lifecycle-neutral. `_STATUS.md` remains the sole lifecycle authority and is untouched by the run that authored this document; the deliverable is at `OPEN` and nothing has been built.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-001 OBJ-001 OBJ-002 | REQ-001, REQ-002, REQ-005, REQ-007, REQ-011, CLM-005, CLM-006, CLM-007, TBD-002 | AC-001, AC-004, AC-006, AC-010 | VER-001, VER-004, VER-006, VER-010 | Type inventory diffed against the fourteen register names and the eleven PRD §7.1 rows with per-type traces; rebuild-and-compare transcript over fixture sources with the non-reproducible-field inspection; field-type inspection record plus the rejected content fixture; the delivered slice structure against the envelope note, with recorded seam evidence if a split was taken |
| OUT-002 | SOW-001 OBJ-001 OBJ-002 | REQ-003, REQ-004, REQ-006, REQ-008, REQ-009, REQ-010, REQ-012, CLM-009, CLM-010, CLM-011, CLM-012, CON-001, CON-002 | AC-002, AC-003, AC-005, AC-007, AC-008, AC-009, AC-011 | VER-002, VER-003, VER-005, VER-007, VER-008, VER-009, VER-011 | Per-type provenance resolution records; the two-snapshot comparison producing a classified DriftFinding with no judgment input; tier-boundary inspection with the rejected daemon-state fixture; the Receipt availability matrix covering the D-APP-57 and prose-structured shapes with no OI-008 outcome assumed; the type-versus-persistence dependency graph and the core-or-adapter classification exercise; dependency-manifest and network-call inspection; consumability confirmation for the eleven recorded consumers and a change set confined to PKG-01 |
| OUT-003 | SOW-001 OBJ-001 OBJ-002 | REQ-013, CLM-013 | AC-012 | VER-012 | Service-core test-run output mapping each executed test to its declared verification method, with no criterion asserted that this contract does not state |
