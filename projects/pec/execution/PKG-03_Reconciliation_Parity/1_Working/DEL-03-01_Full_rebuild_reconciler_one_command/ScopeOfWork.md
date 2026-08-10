---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-03-01
package_id: PKG-03
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@65955cceb
project_scope_refs: [SOW-010, SOW-021]
package_objective_refs: [OBJ-005]
---

# Scope of Work — DEL-03-01 Full-rebuild reconciler (one command)

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-03-01` — "Full-rebuild
reconciler (one command)" — in `PKG-03` Reconciliation & Parity of the PEC v2
build. It covers project scope items `SOW-010` and `SOW-021` in service of
package objective `OBJ-005`.

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.4** (`current_basis`, SCA-004 successor), pinned at merge
`65955cceb`.

**Objective warrant.** `CoversScopeItems` is two rows, and their `OBJ-005`
provenance is not the same. Each is stated here at the strength its own record
carries, and no further.

`SOW-010` → `OBJ-005` is **register-direct**, pre-SCA-002. The `SOW-010` ledger
row already carried `OBJ-005` in its `ObjectiveIDs` cell before the scope
change: SCA-002's action `A001` enumerates the twenty `IN` rows whose
`ObjectiveIDs` it populated —

> `SOW-001, 003, 011..017, 021, 025, 040, 042, 052, 053, 054, 056, 088, 089, 094`
>
> (`Brief.md`, action-register row `A001`, target cell description. ID-shaped
> text inside this quotation is upstream source context, not a local definition
> or reference.)

— and `SOW-010` is not among them. The §3 objective row confirms the same
from the other side: the recorded old and new text of the `OBJ-005` "Mapped
Scope Items" cell reads

> ```
> OLD col4: SOW-010, SOW-055; bound by C1/C2 across all items
> NEW col4: SOW-010, SOW-021, SOW-025, SOW-052..056, SOW-088; bound by C1/C2 across all items
> ```
>
> (`Amendment_Preview.md`, action `A003b`. ID-shaped text inside this quotation
> is upstream source context, not a local definition or reference.)

`SOW-010` stands unchanged on both sides of the amendment. The SCA-002 record
also measures the strength of that pre-existing mapping, in a table whose
columns are `Precedent | Mapping | Status`:

> | `SOW-010` (PEC-RCN-001) | `OBJ-005` | **Valid but narrow** — about rebuild + store locality specifically |
>
> (`Amendment_Preview.md`, "Register precedents (measured)". ID-shaped text
> inside this quotation is upstream source context, not a local definition or
> reference.)

`SOW-021` → `OBJ-005` is **SCA-002-qualified**, and its qualification is of a
distinctive kind that this contract states exactly. `SOW-021` is one of the
twenty `A001` rows, but it is **not** one of the nine per-row attributions the
packet derived from a PRD anchor and rated (those nine, batched into Q1 and Q5,
carry explicit confidence labels from HIGH to LOW; `SOW-021` appears in none of
them), and it is not a member of the Q2 INDIRECT-8 group either. Its value was
fixed by an owner ruling at Gate 1 that constrained it, derived from the union
invariant over the pinned comparison window rather than from an independent
objective attribution. The Gate 1 finding reads in full:

> `F-2` | The union invariant makes the **deliverable**-row change count
> conditional on token choice. `D-PEC-64` §4.3's O-A window of "17 deliverable
> rows" holds only if `SOW-021` maps to a subset of `{OBJ-005}`. Any other
> assignment forces `DEL-03-01` to change, widening the window to 18 and
> breaching the pinned bound. The symmetric case is `SOW-033`/`DEL-07-01` under
> O-B/O-C. | Carried to Gate 3 as a drafting constraint. Not a Gate 1 blocker.
>
> (`Decision_Log.md`, "New facts found at Gate 1", columns
> `Ref | Finding | Disposition`. ID-shaped text inside this quotation is
> upstream source context, not a local definition or reference.)

and the recorded effect of the owner's ruling reads in full:

> R-2 | **`SOW-021` ⊆ `{OBJ-005}` is now a binding constraint**, not an
> observation. It originates in this session's F-2 finding and is written into
> `D-PEC-64` §4.3 by the owner's same-day amendment. Violating it forces
> `DEL-03-01`'s cell by the union invariant and breaks the 17-row window.
>
> (`Decision_Log.md`, "Effects, as executed by this session", columns
> `Ref | Effect`. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference.)

What the record does carry as substantive verification of the mapping is a
Gate 1 measurement that this deliverable's objective cell was already correct
through the other scope item, in a table whose columns are
`Claim | Intake | Measured | Result`:

> | `SOW-021` in-wave ledger exception | 1 | 1 (verified `DEL-03-01` ← `OBJ-005` via `SOW-010`) | `MATCH` |
>
> (`Decision_Log.md`, Gate 1 measurement table. ID-shaped text inside this
> quotation is upstream source context, not a local definition or reference.)

and a consequence for the deliverable register, stated in full:

> `DEL-03-01` is **not** in this set — `SOW-021` maps within its existing
> `OBJ-005`, so its cell is unchanged.
>
> (`Amendment_Preview.md`, action `A002` row set. ID-shaped text inside this
> quotation is upstream source context, not a local definition or reference.)

Three consequences bind this contract. First, the deliverable-level
`SupportsObjectives` value `OBJ-005` in `Deliverables.csv` is **not**
SCA-002-authored — SCA-002 left this row byte-identical, and the cell's warrant
is `SOW-010`'s register-direct mapping. Second, the `SOW-021` leg is **ruled,
not pending**: Gate 1 is recorded closed with the ruling "O-A wave-minimum;
A001–A006 confirmed + A007 added; `SOW-021` ⊆ `{OBJ-005}`", and Gate 3
approved the drafted cell as final, so this contract creates no
owner-confirmation acceptance criterion for it and supplies no fresh derivation
of it. Third, this contract asserts no confidence label for the `SOW-021` leg,
because the record assigns none, and it does not present that leg as an
independently PRD-derived attribution of the kind the nine rated rows carry.
`AC-017` puts that qualification in front of the REVIEW gate rather than
leaving it buried in the scope-change package.

- **CLM-001** — The accepted `ScopeLedger.csv` row for `SOW-010` reads in full, with all ten fields populated (columns `ScopeItemID,InOutStatus,ScopeItemStatement,SourceRef,PackageID,DeliverableIDs,ObjectiveIDs,DecisionRef,OpenIssue,Notes`):

> `SOW-010,IN,Make the record tier rebuildable in full from sources by one command; store gitignored and safe to delete; presence tier expected lost on rebuild,PEC-RCN-001,PKG-03,DEL-03-01,OBJ-005,DL-11,FALSE,Carries PEC-K-02/-05`
>
> (`DecisionRef` `DL-11`; `OpenIssue` `FALSE`; `Notes` "Carries PEC-K-02/-05" —
> this scope item rides a boundary decision and carries two product invariants.
> ID-shaped text inside this quotation is upstream source context, not a local
> definition or reference.)

  The `SOFTWARE_DECOMP.md` §2 SSOW row for the same item repeats the statement without the register-only columns: "| SOW-010 | IN | Make the record tier rebuildable in full from sources by one command; store gitignored and safe to delete; presence tier expected lost on rebuild | PEC-RCN-001 | Carries PEC-K-02/-05 |".

- **CLM-002** — The accepted `ScopeLedger.csv` row for `SOW-021` reads in full, including its trailing empty fields, under the same column order:

> `SOW-021,IN,Restrict reconciler writes to its own store and generated views,PEC-RCN-006,PKG-03,DEL-03-01,OBJ-005,,FALSE,`
>
> (`DecisionRef` empty; `OpenIssue` `FALSE`; `Notes` empty — unlike `SOW-010`,
> no boundary decision and no invariant note rides this scope item. ID-shaped
> text inside this quotation is upstream source context, not a local definition
> or reference.)

  The `SOFTWARE_DECOMP.md` §2 SSOW row for the same item likewise leaves its `Notes` column empty: "| SOW-021 | IN | Restrict reconciler writes to its own store and generated views | PEC-RCN-006 | |".

- **CLM-003** — `SOW-010`'s `SourceRef` cell names one locus, `PEC-RCN-001`, the `PRD.md` §9.2 reconciliation requirement, quoted here in full as it reads: "The record tier shall be rebuildable in full from sources by one command; the presence tier is not reconstructible and is expected to be lost on rebuild (PEC-K-05); the database is gitignored and safe to delete (PEC-K-02)."
- **CLM-004** — `SOW-021`'s `SourceRef` cell names one locus, `PEC-RCN-006`, the `PRD.md` §9.2 requirement, quoted here in full as it reads: "The reconciler writes only its own store and generated views." It is the shortest requirement in §9.2 and the **origin** of the phrase "generated views" inside PEC: the `ScopeLedger.csv` `SOW-021` row (CLM-002), the `Deliverables.csv` `DEL-03-01` `Description` (CLM-006), and the `SOFTWARE_DECOMP.md` §2.1 SSOW row each restate the phrase without defining it, and no PEC source defines it. That gap is CON-001.
- **CLM-005** — `OBJ-005` states "Everything PEC holds can be deleted at any moment without blocking any governed act", `SourceRef` `§3.5` (`SOFTWARE_DECOMP.md` §3; `PRD.md` §3 outcome 5). At revision 1.2 its "Mapped Scope Items" cell reads "SOW-010, SOW-021, SOW-025, SOW-052..056, SOW-088; bound by C1/C2 across all items" and its `MappedDeliverables` cell reads "DEL-00-01, DEL-01-03, DEL-01-05, DEL-03-01, DEL-03-06, DEL-10-02, DEL-10-03". The objective's product invariant is `PEC-K-01` graceful absence: "No governed act may require a PEC read or write. Deleting PEC blocks nothing. The kill test (§12) passes at every release."

## Deliverable Definition — Ontology

`DEL-03-01` is typed `BACKEND_FEATURE_SLICE` at Context Envelope `M` with
`PhaseHint` `P1`. `Deliverables.csv` records its `AnticipatedArtifacts` as
"Reconciler entry point + rebuild tests" and leaves `ContextEnvelopeNotes`
empty, so there are no envelope notes to carry forward and `_CONTEXT.md`
records "(none)". The outputs of this contract are bounded by that artifact
naming: exactly the reconciler entry point and its rebuild tests, and nothing
beyond those two artifacts and the components each of them declares as part of
itself.

- **OUT-001** — A full-rebuild reconciler entry point in the PEC service core: one command that rebuilds the record tier in full from file sources for the loops the registry names, writing only into the store and into the generated views it declares. The entry point's **declared-view record** — the readable artifact in which it declares every generated view it writes (REQ-006) — is a component of this output rather than a third artifact: it is the entry point's own self-declaration, so the register's `AnticipatedArtifacts` naming of exactly two artifacts is preserved.
- **OUT-002** — An automated rebuild test suite covering the full-rebuild path and the write restriction, implementing the verification methods declared in this contract.

### Identity of record

- **CLM-006** — `DEL-03-01` is named "Full-rebuild reconciler (one command)", Type `BACKEND_FEATURE_SLICE`, Context Envelope `M`, `PhaseHint` `P1`, `ResponsibleParty` `TBD`, `AnticipatedArtifacts` "Reconciler entry point + rebuild tests", `CoversScopeItems` `SOW-010;SOW-021`, `SupportsObjectives` `OBJ-005`, `ContextEnvelopeNotes` empty, with the register `Description` field reading "One-command full rebuild of the record tier from sources; writes restricted to the store and generated views; store safe to delete." Sources: `Deliverables.csv` row `DEL-03-01` and the `SOFTWARE_DECOMP.md` §5 PKG-03 table row "| DEL-03-01 | Full-rebuild reconciler (one command) | BACKEND_FEATURE_SLICE | M | P1 | SOW-010, 021 |".
- **CLM-007** — The `PKG-03` package charter (`SOFTWARE_DECOMP.md` §4) is "The guaranteed path from file truth to record tier: one-command rebuild, incremental Git-delta reconcile, drift classification, harness parity diffing, stream-loss recovery guarantee, store-only writes, rebuild performance bounds", covering "SOW-010, 018, 019, 020, 021, 038, 054 (7)", with "Stream ingest mechanics (PKG-07); parsers (PKG-02)" recorded as explicitly out of package scope. Of those seven items this deliverable covers exactly two: the one-command rebuild and the store-only write restriction.
- **CLM-008** — The assignment of `SOW-010` to `PKG-03` is decision-log entry `DL-11` (2026-07-24), whose Decision cell records the forced boundary calls of Phase 4. Quoting the two clauses that bear on this deliverable, with the intervening and following text elided:

> Phase 4 forced boundary assignments: SOW-010 (one-command rebuild) → PKG-03
> as the reconciler entry point, while the store-path rule (SOW-056) stays
> PKG-01; ... SOW-054 (rebuild bounds) → PKG-03 as reconcile performance; ...
>
> (`SOFTWARE_DECOMP.md` decision log, `DL-11` Decision cell; **elided** at both
> ellipses. ID-shaped text inside this quotation is upstream source context, not
> a local definition or reference.)

  The `SOW-010` statement therefore carries a clause — "store gitignored and safe to delete" — whose enforcement `DL-11` places outside this deliverable, at `SOW-056` / `DEL-01-03`. This contract owns the rebuild command and the write restriction; it does not own the store's path, its ignore rule, or its recreation (CLM-013, REQ-003).

- **CLM-009** — The ingest boundary of the rebuild is the feed list of `PRD.md` §9.2 `PEC-RCN-002`, quoted here in full: "The reconciler shall ingest, at minimum: `_STATUS.md` (declared parser dialect), decision registers and packets, `LOOP_RECEIPTS.md` (per-loop grammar; the D-APP-57 contract where a ledger has adopted it), `WORK_GRAPH.json` / `STATUS.json` / `RUNTIME_SUMMARY.json`, dependency registers, workplans/LOOP_INIT, and per-project `_harness/adapter.yaml` as the feed manifest." Decision-log entry `DL-4` (2026-07-24) split that list into seven scope items — Decision cell "PEC-RCN-002's enumerated feed list is split into seven scope items (SOW-011..017), one per feed kind"; Rationale cell "Each feed is a separately testable parser with its own grammar; a single \"ingest everything\" item is not atomic" — assigned to `DEL-02-01` through `DEL-02-07` in `PKG-02`. This deliverable consumes those seven units and defines no feed grammar of its own (REQ-007).

### Placement in the work graph

- **CLM-010** — This deliverable has eleven accepted `EXECUTION` upstream edges and three `ANCHOR` rows, held as `Dependencies.csv` register rows `DEP-03-01-001` through `DEP-03-01-014` at `RegisterSchemaVersion` `v3.1`. The three anchors are `DEP-03-01-001` (package-local to `PKG-03`), `DEP-03-01-002` (`SOW-010` requirement trace), and `DEP-03-01-003` (`SOW-021` requirement trace). All eleven `EXECUTION` rows share the same column values on the following fields, attributed by column: `FromPackageID` `PKG-03`, `FromDeliverableID` `DEL-03-01`, `FromDeliverableName` "Full-rebuild reconciler (one command)", `DependencyClass` `EXECUTION`, `AnchorType` `NOT_APPLICABLE`, `Direction` `UPSTREAM`, `DependencyType` `PREREQUISITE`, `TargetType` `DELIVERABLE`, `Explicitness` `IMPLICIT`, `RequiredMaturity` `INITIALIZED`, `ProposedMaturity` `TBD`, `SatisfactionStatus` `PENDING`, `Confidence` `MEDIUM`, `Origin` `EXTRACTED`, `FirstSeen` and `LastSeen` `2026-07-25`, `Status` `ACTIVE`. They differ in target and in `Statement`, `EvidenceFile`, `SourceRef`, `EvidenceQuote`, and the `EdgeID` carried in `Notes`:

  | Register row | `TargetDeliverableID` / `TargetRefID` | `Statement` | `Notes` |
  |---|---|---|---|
  | `DEP-03-01-004` | `DEL-01-04` | "R3-F6: facility-first — logging facility precedes its emitting subjects" | "PROPOSAL; Flag=none; EdgeID=E-N14" |
  | `DEP-03-01-005` | `DEL-01-01` | "Reconciler entry point of PKG-03" | "PROPOSAL; Flag=none; EdgeID=E-P10" |
  | `DEP-03-01-006` | `DEL-01-03` | "Reconciler writes are restricted to the store; store lifecycle must exist" | "PROPOSAL; Flag=none; EdgeID=E-P15" |
  | `DEP-03-01-007` | `DEL-01-06` | "Reconciler needs the loop registry" | "PROPOSAL; Flag=none; EdgeID=E-P18" |
  | `DEP-03-01-008` | `DEL-02-01` | "Full rebuild ingests the _STATUS.md feed" | "PROPOSAL; Flag=none; EdgeID=E-P19" |
  | `DEP-03-01-009` | `DEL-02-02` | "Full rebuild ingests decision registers/packets" | "PROPOSAL; Flag=none; EdgeID=E-P20" |
  | `DEP-03-01-010` | `DEL-02-03` | "Full rebuild ingests receipts ledgers" | "PROPOSAL; Flag=none; EdgeID=E-P21" |
  | `DEP-03-01-011` | `DEL-02-04` | "Full rebuild ingests run-evidence JSON" | "PROPOSAL; Flag=none; EdgeID=E-P22" |
  | `DEP-03-01-012` | `DEL-02-05` | "Full rebuild ingests dependency registers" | "PROPOSAL; Flag=none; EdgeID=E-P23" |
  | `DEP-03-01-013` | `DEL-02-06` | "Full rebuild ingests workplans/LOOP_INIT" | "PROPOSAL; Flag=none; EdgeID=E-P24" |
  | `DEP-03-01-014` | `DEL-02-07` | "Manifest drives which feeds are read per loop" | "PROPOSAL; Flag=none; EdgeID=E-P25" |

  The evidence fields follow live source-specific loci rather than one shared exhibit. `DEP-03-01-004` cites `docs/PRD.md`, `PEC-SVC-006`, and the reconcile-run logging requirement. `DEP-03-01-005` cites `execution/_Decomposition/Deliverables.csv`, the DEL-01-01 `ContextEnvelopeNotes` cell, and "14 entity types and the schema every derivation package depends on". `DEP-03-01-006` cites `execution/_Decomposition/SOFTWARE_DECOMP.md`, decision-log row `DL-11`, and the SOW-010/PKG-03 versus SOW-056/PKG-01 allocation. `DEP-03-01-007` cites `Deliverables.csv`, the DEL-01-06 `Description`, and its local-configuration staging statement. `DEP-03-01-008` through `DEP-03-01-014` cite `docs/PRD.md`, requirement `PEC-RCN-002`, and the applicable cumulative feed-list quotation, ending with the full list including per-project `_harness/adapter.yaml` in `DEP-03-01-014`.

- **CLM-011** — Every one of the eleven predecessors is at lifecycle state `INITIALIZED`, which is the maturity all eleven edges require. `INITIALIZED` means each upstream **contract** is the reliable input: each accepted `ScopeOfWork.md` exists, and no store, schema, parser, registry, logger, or reconciler does. Nothing in this contract asserts that any upstream artifact exists or has been built. The obligations this contract binds to are those contracts' stated obligations, quoted in CLM-012 through CLM-016.
- **CLM-012** — From `[E-P10]`, the record-tier entity model this rebuild writes into is `DEL-01-01`'s obligation, not this deliverable's:

> - **REQ-001** — The schema and entity model shall define exactly the fourteen
>   record-tier entity types named in CLM-005 — Loop, Workplan, Step, Gate,
>   Receipt, DecisionRow, Fence, Package, Deliverable, DependencyEdge,
>   RunRecord, CandidateBrief, OrientationSnapshot, DriftFinding — with none
>   added and none dropped, and each type shall carry a recorded trace to its
>   `PRD.md` §7.1 row and stated purpose (CLM-006).
> - **REQ-005** — Every record-tier entity shall be fully regenerable from file
>   sources. No record-tier field may hold state that cannot be reproduced by
>   rebuilding from the same sources, per `PEC-K-02` ("The record tier is
>   regenerated from sources by one command") and `PEC-RCN-001`. The rebuild
>   command itself is `DEL-03-01`'s under `SOW-010`.
> - **REQ-007** — No field of any type shall admit file content or diff content
>   (`PEC-K-10`: "Paths, counts, SHAs, states, hashes — never file or diff
>   content"). DecisionRow shall carry register-row identity and status only —
>   decision ID, packet path, anchor, state — and shall have no field capable of
>   holding the row's prose. Enforcement at the ingest boundary is `DEL-01-03`'s
>   guard under `SOW-056`; this requirement binds the shape of the schema so
>   that the guard has nothing to admit into.
>
> (`DEL-01-01/ScopeOfWork.md`, Epistemology section; all three records quoted
> in full, none elided. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference — this contract's own `REQ-*`
> and `AC-*` records are separate and differently worded.)

  The upstream regenerability obligation names this deliverable as the owner of the rebuild command. That is the clearest statement in the accepted corpus of what this deliverable is for, and it is written in another contract's voice, not in this one's.

- **CLM-013** — From `[E-P15]`, the store this reconciler writes into, its safe-delete lifecycle, and its ingest boundary are `DEL-01-03`'s obligations:

> - **REQ-002** — The store shall be safe to delete at any moment. The lifecycle
>   module shall provide an explicit delete operation and shall recreate a valid
>   empty store on next start without manual repair. Deletion shall block no
>   governed act, per `PEC-K-01`.
> - **REQ-003** — Every write into the store shall pass through one declared
>   ingest boundary. No store write path may bypass the guard, including writes
>   originating inside the service core.
> - **REQ-008** — The store lifecycle module shall expose the store to its
>   consumers through an interface that carries no concrete path or
>   storage-engine detail, so that resolving TBD-002 differently, or relocating
>   the store later, changes no consumer deliverable named in CLM-006.
>
> (`DEL-01-03/ScopeOfWork.md`, Epistemology section; all three records quoted in
> full, none elided. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference.)

  That same contract states the division of duty in its own voice, quoted here in full:

> - **AX-004** — Enforcement duties are separated across deliverables and this
>   contract produces only its own: the standing kill-test gate is `DEL-10-02`
>   (`SOW-055`), the reconciler write restriction is `DEL-03-01` (`SOW-021`,
>   `PEC-RCN-006`), zero-dependency and locality enforcement is `DEL-01-05`
>   (`SOW-052`, `SOW-053`), and ingest-activity logging is `DEL-01-04`
>   (`SOW-057`, serving `OBJ-006`). Nothing here discharges those obligations.
>
> (`DEL-01-03/ScopeOfWork.md`, Axiology section; quoted in full, not elided.
> ID-shaped text inside this quotation is upstream source context, not a local
> definition or reference.)

  The division is symmetric and this contract honours it in both directions: the store-side guard, the gitignored path, and safe-delete recreation are the upstream deliverable's; the reconciler-side write restriction under `SOW-021` is this deliverable's and is discharged nowhere else (REQ-005).

- **CLM-014** — From `[E-N14]`, the logging facility this reconciler emits into, and its graceful-absence posture, are `DEL-01-04`'s obligations:

> - **REQ-001** — The module shall record every execution of PEC's own
>   reconciler as a durable log event bearing a run identity and a timestamp,
>   per the "Log PEC's own reconcile runs" limb of `SOW-057`.
> - **REQ-006** — Neither logging nor its absence shall block any governed act
>   or any reconcile run: a deleted, unwritable, or absent log store shall
>   degrade to an explicit absence report and shall never cause a reconcile or a
>   governed workflow to fail, per `PEC-K-01` and the standing kill test
>   `PEC-SVC-004`.
>
> (`DEL-01-04/ScopeOfWork.md`, Epistemology section; both records quoted in
> full, neither elided. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference.)

  The edge's `Statement` cell — "R3-F6: facility-first — logging facility precedes its emitting subjects" — makes this deliverable the emitting subject. The upstream contract's own production narrative records that its reconcile-run limb is exercised against a fixture stand-in until this deliverable exists; nothing in this contract asserts that the facility has been built (REQ-012).

- **CLM-015** — From `[E-P18]`, the registered-loop set this rebuild spans is `DEL-01-06`'s obligation, and that contract binds its consumers to an interface rather than a location:

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
> (`DEL-01-06/ScopeOfWork.md`, Epistemology section; both records quoted in
> full, neither elided. ID-shaped text inside this quotation is upstream source
> context, not a local definition or reference.)

  The consumer-decoupling obligation names this deliverable explicitly. This contract therefore binds to the interface and to nothing about where the registry lives or how it is serialized (REQ-008, CON-002).

- **CLM-016** — From `[E-P19]` through `[E-P25]`, the seven `PKG-02` units supply this rebuild's inputs. Each declares its own output in its own contract, quoted here in full and without elision:

> - `DEL-02-01` **OUT-001** — A `_STATUS.md` parser in the PEC service core: it
>   reads governed deliverable lifecycle files under one declared dialect and
>   emits the record-tier entities of CLM-007, with citation provenance and
>   explicit limitation reporting.
> - `DEL-02-02` **OUT-001** — A decision register/packet parser in the PEC
>   service core: it reads decision registers and decision packets under a
>   declared grammar and emits, per register row, that row's identity and
>   status — decision ID, packet path, anchor, state — with the provenance
>   needed to cite it, and nothing of the row's prose.
> - `DEL-02-03` **OUT-001** — A receipts-ledger parser in the PEC service core:
>   it reads a loop's `LOOP_RECEIPTS.md`, applies the grammar declared for that
>   loop, and emits record-tier Receipt entities carrying the fields that
>   grammar yields together with an explicit statement of the fields it does
>   not.
> - `DEL-02-04` **OUT-001** — A run-evidence JSON parser in the PEC service
>   core: it reads `STATUS.json` and `RUNTIME_SUMMARY.json` files under
>   `execution/**` in the checkouts it is pointed at, parses them under a
>   declared grammar, and emits RunRecord summaries carrying citation provenance
>   to their live sources.
> - `DEL-02-05` **OUT-001** — A dependency register parser in the PEC service
>   core: it reads `Dependencies.csv` registers and `WORK_GRAPH.json` files in
>   the checkouts it is pointed at, parses each under a declared grammar, and
>   emits DependencyEdge records carrying citation provenance to their live
>   sources.
> - `DEL-02-06` **OUT-001** — A workplan/LOOP_INIT parser in the PEC service
>   core: it reads workplan files and `LOOP_INIT.md` protocol files in the
>   checkouts it is pointed at, parses them under a declared grammar, and emits
>   Workplan, Step, and Gate entities carrying recorded gate state and citation
>   provenance to their live sources.
> - `DEL-02-07` **OUT-001** — A feed-manifest reader in the PEC service core: it
>   consumes a per-project `_harness/adapter.yaml` file, validates it against a
>   declared grammar, and derives from it the feed manifest for that project —
>   which feeds are read for it — exposing that manifest to the reconciler.
>
> (Each deliverable's `ScopeOfWork.md`, Ontology section. ID-shaped text inside
> this quotation is upstream source context, not a local definition or
> reference.)

  Six of the seven emit record-tier entities under declared grammars; the seventh derives, per project, which feeds are read. On limitation reporting the seven are not uniform, and this contract states the difference rather than averaging it. Six — `DEL-02-01`, `DEL-02-02`, `DEL-02-04`, `DEL-02-05`, `DEL-02-06`, and `DEL-02-07` — oblige themselves **at requirement level** to report a feed that is absent, unreadable, malformed, or outside the declared grammar as an explicit limitation naming the file and the fault, with silent omission and defaulted or partial output prohibited. `DEL-02-03` places its coverage differently: its requirement-level obligation is field-level best-effort over a prose-structured ledger — each field the grammar could not obtain explicitly marked unavailable with the loop and the reason identified, and a silently omitted, absent, defaulted, or inferred *field* prohibited — while malformed and unreadable ledgers are carried at its acceptance-criterion level, and feed **absence** is stated nowhere in that contract. Those limitation reports, however each upstream places its duty, are the input this contract's REQ-009 obliges the rebuild to carry through; REQ-009 binds this rebuild's own carry-through over whatever an upstream unit reports and presumes no uniform upstream placement.

- **CLM-017** — Thirteen downstream consumer relations are recorded against this deliverable in `_DEPENDENCIES.md` and marked informational: `DEL-09-07` `[E-N05]`, `DEL-03-02` `[E-P26]`, `DEL-03-03` `[E-P27]`, `DEL-03-04` `[E-P28]`, `DEL-03-05` `[E-P29]`, `DEL-03-06` `[E-P30]` (`TESTS`), `DEL-04-01` `[E-P32]`, `DEL-05-01` `[E-P37]`, `DEL-05-02` `[E-P38]`, `DEL-09-02` `[E-P61]`, `DEL-09-03` `[E-P63]`, `DEL-10-02` `[E-P72]` (`TESTS`), and `DEL-10-10` `[E-P74]`. **None of the thirteen holds a row in this deliverable's `Dependencies.csv`**, which contains only the three anchors and the eleven upstream `EXECUTION` rows; the downstream rows live in each consumer's own local register, per the deliverable-local storage ruling of `D-PEC-62`. The kill-test relation is directional and runs *toward* this deliverable: the gate exhibit row reads `E-P72,DEL-03-01,DEL-10-02,PROPOSAL,TESTS,,SOW-055 + PEC-K-02,Kill test proves rebuildability after deletion` under the exhibit's columns `EdgeID,PredecessorID,SuccessorID,Stratum,EdgeKind,Flag,BasisCitation,Rationale`, with `Flag` empty. `DEL-10-02` is the tester and this deliverable is the tested surface; the kill test is exercised on this deliverable from outside, under `SOW-055`, and is neither run nor discharged here (REQ-014).
- **CLM-018** — Phase staging, checked against the `PhaseHint` column of `Deliverables.csv` for every deliverable this contract names in its own voice: `DEL-03-01` itself, its upstreams `DEL-01-01`, `DEL-01-03`, `DEL-01-04`, `DEL-01-06`, `DEL-02-01`, `DEL-02-02`, `DEL-02-03`, `DEL-02-04`, `DEL-02-05`, `DEL-02-06`, `DEL-02-07`, and the neighbours and consumers `DEL-01-05`, `DEL-03-02`, `DEL-03-03`, `DEL-03-04`, `DEL-03-06`, `DEL-04-01`, `DEL-04-03`, `DEL-04-05`, `DEL-10-02`, `DEL-10-03`, and `DEL-10-10` are all `P1`. Nine exceptions are named in this contract's own voice, each cited only as the owner of scope this deliverable does not touch: `DEL-00-01` (`pre-P1`; named at AX-012 as the site of the `OI-012` ADR), `DEL-05-01` and `DEL-05-02` (`P2`), `DEL-09-02`, `DEL-09-03`, and `DEL-09-07` (`P2`), and `DEL-01-02`, `DEL-03-05`, and `DEL-07-01` (`P3`). The `P1` ingest boundary of this rebuild is therefore the feeds enumerated at `PEC-RCN-002` (CLM-009) and nothing later: presence-tier ingest (`DEL-01-02`, `P3`) and event/stream ingest (`DEL-07-01`, `P3`) are not feeds of this rebuild, and no claim in this contract stages any named deliverable into a different phase.

### Boundaries

- **CLM-019** — The acts adjacent to this reconciler are owned elsewhere and are cited here, never discharged. Within `PKG-03`: incremental reconciliation keyed on Git delta since the last examined SHA is `DEL-03-02` (`SOW-018`); drift classification between successive snapshots is `DEL-03-03` (`SOW-019`); parity-diffing PEC derivations against practitioner-harness output is `DEL-03-04` (`SOW-020`); the stream-loss recovery guarantee is `DEL-03-05` (`SOW-038`, `P3`); rebuild performance bounds are `DEL-03-06` (`SOW-054`). Outside it: the record-tier schema and entity model are `DEL-01-01` (`SOW-001`); the gitignored store, its safe-delete lifecycle, and its ingest-boundary content-minimal guard are `DEL-01-03` (`SOW-056`); standing zero-dependency and locality enforcement is `DEL-01-05` (`SOW-052`, `SOW-053`); self-observability logging is `DEL-01-04` (`SOW-057`); the loop-registration configuration is `DEL-01-06` (`SOW-094`); the seven feed grammars and the feed manifest are `DEL-02-01` through `DEL-02-07` (`SOW-011`..`SOW-017`); the per-loop orientation return is `DEL-04-01` (`SOW-004`); examined-SHA and freshness stamping with per-claim citation attachment is `DEL-04-03` (`SOW-006`, `SOW-007`); rendering a measurement limitation into an orientation response is `DEL-04-05` (`SOW-009`); gate-precondition evaluation is `DEL-05-01` (`SOW-022`, `SOW-023`) and the cross-loop decision slate is `DEL-05-02` (`SOW-024`); the standing kill test is `DEL-10-02` (`SOW-055`); the tested no-ruling-write property of the API surface is `DEL-10-03` (`SOW-025`); the directed bootstrap self-ingest validation is `DEL-10-10` (`SOW-064`). This contract produces only the reconciler entry point and its rebuild tests.
- **CLM-020** — `PEC-K-05` requires the two trust tiers never be blurred: "Record tier: reconciled from file truth, per-claim citations. Presence tier: TTL'd, heartbeat-aged, evaporating, honesty-labeled. Presence facts never enter record-tier citations." `SOW-010`'s own statement carries the rebuild-side consequence — "presence tier expected lost on rebuild" — and `PEC-RCN-001` states it as an impossibility rather than a policy: "the presence tier is not reconstructible". A rebuild that recovered presence facts would not be a better rebuild; it would be a tier violation (REQ-004).
- **CLM-021** — `PEC-K-07` states the standing that makes this deliverable load-bearing: "Ingest is best-effort; reconciliation is guaranteed. Streams optimize freshness; the reconciler over file truth is the source of every record-tier fact." Every record-tier fact in PEC originates in a reconcile over files, and this deliverable is the full-rebuild form of that act. `PEC-K-02` states what that makes the store: "The record tier is regenerated from sources by one command ... PEC output is never citable as authority", and `PRD.md` §15 quotes the `D-GOV-01` Option A sanctioning clause for the same object as "a rebuildable, gitignored projection: safe to delete, regenerated from files by one command, never cited as authority". The `PEC-K-02` quotation in this claim is **elided** at the ellipsis.
- **CLM-022** — The deliverable is at lifecycle state `INITIALIZED` with no implementation present. Every requirement, acceptance criterion, and verification method below states a contract on future production; none asserts that anything has been built.

- **TBD-001** — `ResponsibleParty` is unassigned; the register records `TBD`, with assignment at WORKING_ITEMS activation and not in this contract (`SOFTWARE_DECOMP.md` §5 preamble; `_CONTEXT.md`).
- **TBD-002** — The command's concrete invocation surface — its verb name, its host CLI or entry-point form, its arguments, and its exit-status contract — is fixed by no accepted source beyond the register phrase "Reconciler entry point" and `PEC-RCN-001`'s "by one command". It is chosen during production within REQ-001.
- **TBD-003** — Which views this reconciler generates, and where they live, are fixed by no accepted source. What a "generated view" *is* as a class is not open: `D-GOV-01` Option A rules the category and its properties, and `tools/REGISTRY.md` glosses the shipped harness outputs in the same terms (CON-001). What remains undetermined is the instance set, chosen during production within REQ-006. This is the informational side of CON-001.
- **TBD-004** — The rebuild's transactional shape — whether the record tier is rebuilt in place, or built aside and swapped, and what an interrupted rebuild leaves behind — is fixed by no accepted source. `PRD.md` §7.3 carries "dry-run-then-apply ingestion" explicitly as pattern and "not as code". It is chosen during production within REQ-002, REQ-003, and REQ-010.
- **TBD-005** — How the reconciler resolves a registered loop to the project or projects whose `_harness/adapter.yaml` is read for it is fixed by no accepted source; the upstream manifest contract records the same gap in its own terms. This contract obtains both the loop set and the per-project manifest through the upstream interfaces (REQ-008) and settles nothing about the resolution between them.

## Completion and Reliance Basis — Epistemology

The requirements below state what future production must satisfy. Nothing in
this section asserts that a reconciler, a store, a parser, or a test exists.

- **REQ-001** — The reconciler shall expose a single command that rebuilds the record tier in full from file sources for every loop the registry names, per `SOW-010` (CLM-001) and `PEC-RCN-001` (CLM-003). A rebuild shall require no operator step, repair action, or manual sequence beyond that one invocation.
- **REQ-002** — Every record-tier fact the rebuild produces shall be derived from file sources read through the declared upstream feed units of CLM-016. No record-tier fact shall rest on prior store state, on a cached artifact, on a stream or event input, or on any input the same sources cannot reproduce, per `PEC-K-07` ("the reconciler over file truth is the source of every record-tier fact") and the upstream regenerability obligation quoted in CLM-012.
- **REQ-003** — The rebuild shall complete against a store that is absent, newly deleted, or empty, obtaining the store through the upstream store-lifecycle interface quoted in CLM-013 and requiring no manual repair. This deliverable shall implement no store path resolution, no ignore-rule registration, no store creation, and no store deletion of its own; those are the upstream deliverable's under `SOW-056` (CLM-008, CLM-013).
- **REQ-004** — The rebuild shall neither reconstruct nor populate nor assert any presence-tier fact, and its completion shall not depend on presence data being present. Loss of the presence tier across a rebuild is the expected outcome and shall be treated as such rather than repaired, per `SOW-010`, `PEC-RCN-001`, and `PEC-K-05` (CLM-020).
- **REQ-005** — The reconciler shall write only into the store, through the single declared ingest boundary quoted in CLM-013, and into the generated views it declares under REQ-006. It shall create, modify, or delete no source file, no governed file, no register, no lifecycle file, and no path outside that declared write set, per `SOW-021` and `PEC-RCN-006` (CLM-002, CLM-004), `PEC-RCN-004` ("it shall never modify a source file"), `PEC-GAT-004` ("PEC shall provide no write path that records adoption, ruling, or direction"), and `PEC-K-06` observation-not-participation.
- **REQ-006** — The reconciler shall declare, in the entry point's declared-view record — a readable component of OUT-001 — every generated view it writes: what the view is, where it is located, and the fact that it is fully regenerable by a rebuild and safe to delete. An undeclared write target is prohibited. The warrant for this requirement is `D-GOV-01` Option A, which sanctions writing "labeled generated artifacts (reports, briefs, evidence records) under declared generated paths" and holds any such projection to being "a rebuildable, gitignored projection: safe to delete, regenerated from files by one command, never cited as authority" (CLM-021, CON-001): declaration under a declared path, regenerability, and safe deletion are that ruling's own properties, restated here as a checkable obligation rather than invented by this contract. What this requirement does not settle is which views this reconciler generates or where they live, which is CON-001 and TBD-003.
- **REQ-007** — The rebuild shall ingest the feeds enumerated at `PEC-RCN-002` (CLM-009) exclusively through the seven upstream units of CLM-016. It shall declare no feed grammar, parse no feed file directly, and read no feed the manifest does not name for a loop; `PKG-02` owns the read-side grammars and `PKG-03`'s package exclusions record "parsers (PKG-02)" as outside this package (CLM-007).
- **REQ-008** — The reconciler shall obtain the set of loops it rebuilds from the loop registry through the upstream stable in-process interface quoted in CLM-015, and shall obtain which feeds are read per project from the upstream feed manifest of CLM-016. It shall depend on no registry on-disk location, filename, or serialization, and on no `_harness/adapter.yaml` field or file format of its own reading.
- **REQ-009** — Where an upstream unit reports that a feed is absent, unreadable, malformed, stale, or grammar-unrecognized, the rebuild shall carry that limitation through to its result, naming the loop and the feed, and shall never present a rebuild that could not read a feed as a rebuild that read it. Silent omission is prohibited, per `PEC-ORI-006` ("Where a feed is unparseable or stale, the response shall state the measurement limitation explicitly; silent omission is prohibited"). Rendering such a limitation into an orientation response is `DEL-04-05`'s act under `SOW-009` (CLM-019); this deliverable makes the limitation available to that consumer.
- **REQ-010** — The rebuild shall be deterministic and idempotent over its inputs: two rebuilds over the same unchanged sources shall produce the same record tier, and a rebuild over a store already rebuilt from those sources shall produce no difference. This is what makes a later difference between two reconciles a structural fact rather than a judgment (`PEC-K-04`).
- **REQ-011** — Every record-tier fact the rebuild writes shall be an instance of one of the entity types the upstream entity-model contract obliges (CLM-012). This deliverable shall define no record-tier entity type, shall add no type to that model, shall define no presence-tier type, and shall not depend on any upstream artifact existing; it depends on the upstream contract only (CON-003).
- **REQ-012** — Each execution of the rebuild shall emit **exactly one** reconcile-run event to the upstream self-observability facility quoted in CLM-014 — one event per rebuild invocation, neither none nor more than one — so that the run is inspectable per `PEC-SVC-006`. A log store that is absent, deleted, or unwritable shall not block, fail, or alter the rebuild, consistent with that contract's own graceful-absence obligation and with `PEC-K-01`.
- **REQ-013** — Nothing the reconciler writes — into the store or into a generated view — shall carry file content or diff content, per `PEC-K-10` ("Paths, counts, SHAs, states, hashes — never file or diff content"). Enforcement at the store's ingest boundary is the upstream guard's (CLM-013); this requirement binds what the reconciler presents to that boundary and extends the same restriction to every generated view, which the guard does not cover (CON-004).
- **REQ-014** — The reconciler shall perform no act owned by another deliverable. In particular it shall perform no Git-delta-keyed incremental reconcile, no drift classification between snapshots, no parity diff against practitioner-harness output, no stream-loss recovery act, no rebuild-bound measurement or assertion, no examined-SHA or freshness stamping and no per-claim citation attachment onto an orientation response, no gate-precondition evaluation or slate rendering, no locality or zero-dependency enforcement act, and no kill test; each is cited to its owner in CLM-019 and none is discharged here.
- **REQ-015** — The reconciler and its tests shall introduce no third-party runtime dependency and no external network egress, per `PEC-SVC-001` and `PEC-SVC-002`, whose standing enforcement is `DEL-01-05` covering `SOW-052` and `SOW-053`.
- **REQ-016** — Tests shall implement the verification methods declared in this contract; they shall not define scope, requirements, or acceptance criteria.

- **AC-001** — A single invocation rebuilds the record tier in full from a fixture source corpus for every registered loop, with no operator step, repair action, or additional command required, and the invocation surface is documented.
- **AC-002** — Every record-tier fact produced by a rebuild is traceable to a file source read through a declared upstream feed unit; a rebuild run with prior store state present produces the same result as one run against an empty store; and inspection finds no cached, stream-derived, or otherwise non-source input contributing to any record-tier fact.
- **AC-003** — The rebuild completes against absent, newly deleted, and empty store fixtures without manual repair, and this deliverable's source contains no store path resolution, ignore-rule registration, store creation, or store deletion of its own.
- **AC-004** — No presence-tier fact is written, reconstructed, or asserted by a rebuild; a rebuild run over a fixture corpus containing presence-shaped input produces no presence-tier record; and a rebuild completes normally with no presence data available.
- **AC-005** — A rebuild over a fixture corpus leaves that corpus byte-identical and touches no path outside the store and the declared generated views; every store write in this deliverable's source reaches the store through the upstream ingest boundary; and the module contains no write, create, or delete call against any source file, governed file, register, or lifecycle file.
- **AC-006** — Every generated view the reconciler writes appears in the entry point's declared-view record — the component of OUT-001 required by REQ-006 — with its location and its regenerable-and-safe-to-delete status; a rebuild writes no view absent from that record; and deleting every declared view and rebuilding restores them.
- **AC-007** — Every feed the rebuild reads is read through a declared upstream feed unit; this deliverable's source declares no feed grammar and opens no feed file directly; and a feed the manifest does not name for a loop is not read.
- **AC-008** — The loop set and the per-project feed manifest are acquired only through the upstream interfaces: no registry path, filename, or serialization token and no `_harness/adapter.yaml` field name appears in this deliverable's source, fixtures, or call surface, so the resolved registry-home choice and any separately governed adapter migration change nothing here.
- **AC-009** — For fixture corpora in which a feed is absent, unreadable, malformed, stale, and grammar-unrecognized in turn, the rebuild result carries the reported limitation naming the loop and the feed, and no such rebuild is presented as having read that feed.
- **AC-010** — Two rebuilds over the same unchanged fixture corpus produce identical record tiers, and a rebuild run against a store already rebuilt from that corpus produces no difference.
- **AC-011** — Every record-tier fact written by a rebuild is an instance of an entity type the upstream contract obliges; no record-tier or presence-tier type is defined in this deliverable's source; and no element of this deliverable asserts or requires that an upstream schema, store, parser, registry, or logging artifact exists.
- **AC-012** — Each rebuild emits exactly one reconcile-run event to the upstream logging facility, and with the log store absent, deleted, or unwritable the rebuild still completes and produces its normal result.
- **AC-013** — For a content-dense fixture corpus, inspection of every field the rebuild presents to the store and of every declared generated view finds no file content and no diff content — only paths, counts, identifiers, states, SHAs, and hashes.
- **AC-014** — The module contains no Git-delta-keyed incremental path, no drift-classification path, no parity-diff path, no stream-loss recovery path, no rebuild-bound measurement or assertion, no stamping or citation-attachment path, no gate-evaluation or slate-rendering path, no locality or dependency enforcement act, and no kill-test execution; and no test in this deliverable asserts a criterion belonging to any of them.
- **AC-015** — The reconciler and its tests add no third-party runtime dependency and make no network call, leaving the `DEL-01-05` zero-dependency and locality assertion intact.
- **AC-016** — The rebuild test suite implements VER-001 through VER-015, executes in the `PKG-03` test run, passes, and introduces no acceptance criterion absent from this contract.
- **AC-017** — The REVIEW gate confirms this contract's traceability to `SOW-010`, `SOW-021`, and `OBJ-005`; confirms that the `SOW-010` leg is stated as register-direct and the `SOW-021` leg no more strongly than the SCA-002 record states it — a Gate 1 binding constraint under the union invariant, carrying no confidence label and no independent PRD-anchor attribution of the kind the nine rated rows carry; and confirms that no `PKG-01`, `PKG-02`, sibling `PKG-03`, `PKG-04`, `PKG-05`, `PKG-09`, or `PKG-10` scope has been absorbed.

- **CON-001** — `SOW-021`'s second limb permits writes to "generated views", and the gap this contract carries is **instance-level, not class-level**. The class referent exists and is cited. `D-GOV-01` Option A — root governance, `RULED`, owner-approved 2026-07-01 — sanctions exactly this write posture: "The harness never writes governed authority files; it may write labeled generated artifacts (reports, briefs, evidence records) under declared generated paths." The same clause fixes the properties such a projection carries, in the words `PRD.md` §15 quotes into PEC's own basis and CLM-021 already carries: "a rebuildable, gitignored projection: safe to delete, regenerated from files by one command, never cited as authority". `tools/REGISTRY.md` glosses the shipped practitioner-harness outputs in the same vocabulary — "Every output is a labeled generated view (D-GOV-01)" — so "generated view" is a term of art in the accepted corpus with a ruled category and ruled properties. The permission is therefore warranted, and REQ-006 states its warrant rather than filling a void.

  What no accepted source states is **which** views this reconciler generates and **where they live**. `PEC-RCN-006` originates the phrase inside PEC and defines nothing (CLM-004), and the neighbouring uses of "views" in the corpus are enumerable, none of them definitional for a reconciler-written artifact. `PEC-I-02`, carried by `PEC-K-08` in the `PRD.md` §6 invariant-lineage paragraph, reads "one state, many views: dashboards, API, and orientation project the same reconciled snapshot" — the closest sense in the corpus, in which a *view* is a projection of the same reconciled snapshot by a consuming surface; it is about who reads the state, not about a durable artifact the reconciler writes. `PEC-DSH-002` names "workflow-completeness views" (`SOW-046` / `DEL-09-02`, `P2`) and `PEC-DSH-003` reads "Register views: decisions, receipts, dependencies, run records — read-only, link-only, source-linked (no restatement of authored text; PEC-K-10)" (`SOW-047` / `DEL-09-03`, `P2`); both are dashboard read surfaces in `PKG-09`, not reconciler write targets, and neither is this deliverable's. The `SOFTWARE_DECOMP.md` §1.2 intake summary ("read-only link-only register views") and the §4 `PKG-09` charter row ("register views" among that package's seven) restate that dashboard sense and add nothing definitional. No accepted source connects any of these senses to a path this reconciler writes.

  This contract records the instance-level gap rather than closing it: REQ-006 obliges every generated view to be declared, under the ruled properties, in the entry point's declared-view record, and REQ-013 extends the content-minimal restriction to it, so that whichever view set production settles on cannot become durable state outside `OBJ-005`'s deletability claim. Naming that view set is a production choice bounded by REQ-006 (TBD-003); reading the limb as authorizing a write outside the store and its declared regenerable views would be a scope-change question for `SOW-021`, not a production decision.
- **CON-002** — D-PEC-78 O-A, propagated by SCA-004 into accepted decomposition revision 1.4, resolved `SOW-077` / `OI-003` by selecting the existing PEC-owned strict-version-1 JSON/schema paths and core-owned typed `LoopRegistry` port as the long-term registry home and shape. This deliverable nevertheless cannot bind to any registry path, filename, or serialization, and REQ-008 restricts it to the upstream in-process interface. The loop-to-project resolution behind the per-project manifest remains separately unresolved as TBD-005 and is not settled by the registry-home result.
- **CON-003** — The entity types this rebuild writes into are owned upstream and do not yet exist. The upstream entity-model contract obliges fourteen types and their regenerability, but no accepted source enumerates their fields, and the upstream contract itself records the core-isolation style (`OI-012`) as undecided and the store engine and DDL dialect as unfixed. This reconciler's write surface therefore binds to an obligation, not to an artifact. A production choice here that fixed an upstream field set, a schema shape, or an isolation style would take a decision in the wrong place.
- **CON-004** — Two boundary questions ride the content-minimal rule and neither is resolved at the level of accepted truth. First, the upstream store contract records that "no accepted source states the test that separates an extracted state token from a prose excerpt when the source itself is prose", and requires the decision to be recorded rather than resolving it; this rebuild is the `P1` ingest path that meets that boundary first, over feeds that include prose-structured ledgers and instruction-prose workplans. Second, the upstream ingest guard covers the store, and no accepted source states that it covers a generated view (CON-001), so REQ-013 binds the reconciler on the view side directly. Both are recorded here, not settled; a resolution that changes what PEC may hold is a scope change, not a production choice.
- **CON-005** — `SOW-010` requires the record tier be rebuildable "in full", while every upstream feed unit is contractually obliged to report feeds it could not read as explicit limitations (CLM-016), and `PEC-ORI-006` prohibits silent omission. No accepted source states whether a rebuild that completed with stated coverage limitations counts as a full rebuild for `SOW-010`'s purposes, or whether "in full" is a claim about the command's reach rather than its coverage. This contract takes neither reading as settled: REQ-001 obliges the command to reach every registered loop and every manifest-named feed, and REQ-009 obliges every gap to be carried through as a stated limitation, so that the question is visible in the result rather than answered by silence. `PRD.md` §12's `P1` exit test names "rebuild-from-scratch ≤ bound" without stating the bound, which `PEC-SVC-003` records as "confirmed at Phase 1"; that measurement is `DEL-03-06`'s under `SOW-054` (CLM-019) and this contract asserts no bound.

## Production and Verification Method — Praxeology

Production proceeds in the order upstream-interface survey → command entry
point and rebuild path → write restriction and declared generated-view set →
limitation carry-through → determinism → tests, because each stage is the
acceptance surface of the next and because the write restriction cannot be
stated as a boundary until there is exactly one rebuild path to bound. The
upstream-interface survey comes first because eleven predecessors at
`INITIALIZED` supply obligations rather than artifacts, and a rebuild path
written against an imagined artifact would violate CON-003 before any code
existed. All work is bounded to this deliverable folder and the `PKG-03`
service-core source it names; this contract authorizes no register,
decomposition, PRD, or upstream-deliverable edit, and it neither defines nor
reshapes the entity model it writes into, the store it writes through, the
registry it reads, or the grammars it consumes. Tests implement the
verification methods below and create no scope.

- **VER-001** — Execute the single documented command against a fixture source corpus spanning every registered loop and assert the record tier is rebuilt in full, with the invocation transcript showing no operator step, repair action, or second command; read the documented invocation surface and assert it matches what was executed.
- **VER-002** — Provenance trace: for a sample record-tier fact of each entity type produced, trace it to the file source and the upstream feed unit that yielded it; run the rebuild once with prior store state present and once against an empty store and assert result equality; and inspect the module's input surface for cached, stream-derived, or non-source inputs, asserting none contributes.
- **VER-003** — Execute the rebuild against absent, newly deleted, and empty store fixtures, asserting completion without manual repair in each case; grep this deliverable's source for store path resolution, ignore-rule registration, store creation, and store deletion operations and assert none is present.
- **VER-004** — Tier-boundary exercise: run the rebuild over a fixture corpus carrying presence-shaped input and assert no presence-tier record is written; delete all presence data and assert the rebuild completes normally; inspect the write surface for any presence-tier construction path.
- **VER-005** — Write-boundary exercise: hash the fixture source corpus tree before and after a rebuild and assert byte-identity; capture every filesystem write performed during the run and assert each resolves under the store or a declared generated view; inspect the module's call graph and assert every store write reaches the store through the upstream ingest boundary and that no write, create, or delete call targets a source file, governed file, register, or lifecycle file.
- **VER-006** — Generated-view exercise: read the entry point's declared-view record (the component of OUT-001 required by REQ-006), compare it against the views actually written during a rebuild and assert set equality, then delete every declared view, rebuild, and assert each is restored.
- **VER-007** — Feed-boundary inspection: instrument or inspect the rebuild's file-open surface and assert every feed read passes through a declared upstream feed unit; grep this deliverable's source for feed grammar definitions and direct feed parsing and assert none; point the rebuild at a fixture loop whose manifest omits a feed present on disk and assert that feed is not read.
- **VER-008** — Acquisition-path inspection: assert the loop set and the per-project feed manifest are obtained only through the upstream interfaces; grep this deliverable's source, fixtures, and call surface for registry path, filename, or serialization tokens and for `_harness/adapter.yaml` field names, asserting none is present.
- **VER-009** — Limitation carry-through: run the rebuild over fixture corpora in which a feed is absent, unreadable, malformed, stale, and grammar-unrecognized in turn, and assert per case that the result carries the reported limitation naming the loop and the feed, and that no result presents that feed as read.
- **VER-010** — Determinism and idempotence: run the rebuild twice over the same unchanged fixture corpus and assert identical record tiers; run it a third time against the already-rebuilt store and assert no difference.
- **VER-011** — Type-boundary inspection: assert every record-tier fact written is constructed against an entity type the upstream contract obliges; grep this deliverable's source for record-tier and presence-tier type definitions and assert none; grep source and fixtures for any assumption that an upstream schema, store, parser, registry, or logging artifact exists, asserting none.
- **VER-012** — Logging exercise, conducted against an interface-level fixture stand-in for the upstream log sink: run a rebuild and assert exactly one reconcile-run event is emitted to the stand-in; then delete, make unwritable, and omit the log store in turn and assert per case that the rebuild completes and produces its normal result. Re-run the emission assertion against the live upstream facility once `DEL-01-04` is available, without discharging that deliverable here. The stand-in is required rather than optional: the upstream contract exercises its own reconcile-run limb against a fixture reconciler stand-in until this deliverable exists (CLM-014), so neither side may presuppose the other's artifact, and CLM-011 forbids this contract from asserting that any upstream artifact exists. Scope boundary: representative governed workflows are not run here; the kill test is `DEL-10-02`'s standing gate under `SOW-055` (CLM-017), and no output of this method may be presented as satisfying it.
- **VER-013** — Content-minimal inspection: run the rebuild over a content-dense fixture corpus carrying long prose bodies, quoted authored text, and diff-shaped content, then dump every field presented to the store and every declared generated view and assert field by field that none carries file or diff content.
- **VER-014** — Boundary inspection: inspect the module's call graph and source for incremental Git-delta, drift-classification, parity-diff, stream-loss recovery, rebuild-bound measurement, stamping, citation-attachment, gate-evaluation, slate-rendering, locality-enforcement, and kill-test paths, asserting each absent; review this deliverable's tests for any criterion belonging to another deliverable, asserting none.
- **VER-015** — Inspect the `PKG-03` dependency manifest and this module's import graph for third-party runtime dependencies and network calls, and re-run the `DEL-01-05` zero-dependency and locality enforcement once that deliverable is available, without discharging it here.
- **VER-016** — Run the `PKG-03` test suite and confirm that each of VER-001 through VER-015 has a corresponding executing automated test and that no test asserts a criterion absent from this contract.

## Governing Values and Decisions — Axiology

- **AX-001** — `OBJ-005` governs: everything PEC holds can be deleted at any moment without blocking any governed act. This deliverable is where that claim is either true or false at the record tier, because deletability is only credible if what was deleted can be rebuilt. The store lifecycle makes deletion safe; the rebuild makes it survivable. Neither half is sufficient alone, and this contract owns the second.
- **AX-002** — `PEC-K-01` graceful absence is `OBJ-005`'s product invariant, and it cuts inward as well as outward. A rebuild that required a log, a prior store, a stream, or a manual repair to complete would make PEC's own recovery conditional on PEC's own state, which is the failure `PEC-K-01` names one level up. REQ-002, REQ-003, and REQ-012 are the inward form of the same rule.
- **AX-003** — `PEC-K-02` files govern: the record tier is a projection regenerated from sources, never an alternative source of truth, and PEC output is never citable as authority. The rebuild is the act that keeps the projection a projection. A reconciler that carried forward any fact the sources could not reproduce would quietly convert the store into a second register, which is exactly what `SOW-010` exists to prevent.
- **AX-004** — `PEC-K-07` is why `SOW-021`'s restriction is not merely hygienic. Reconciliation is the guaranteed path and streams are best-effort; that guarantee is only worth stating if the reconciler is incapable of changing what it reconciles from. A reconciler that could write a source file would make its own inputs a function of its own output, and no amount of downstream verification would recover the distinction.
- **AX-005** — `PEC-K-06` observation-not-participation governs the write restriction's outer edge. `PEC-GAT-004` prohibits any write path in PEC that records adoption, ruling, or direction; a reconciler with a general file-write capability is precisely where such a path would first become available, whatever its intent. REQ-005 states the restriction as a checkable boundary rather than a discipline.
- **AX-006** — `PEC-K-05` two tiers, never blurred, is why REQ-004 forbids rather than merely omits presence reconstruction. `PEC-RCN-001` calls the presence tier "not reconstructible"; a rebuild that inferred presence facts from file truth would be manufacturing tier-crossing data at exactly the moment the system is least able to notice.
- **AX-007** — `PEC-K-10` content-minimal is a residency posture, not a storage optimization, and this deliverable is the `P1` path by which most authored content in the corpus first approaches the store. The strongest enforcement is upstream — an entity model with nowhere to put prose, a guard that refuses it at ingest — but the generated-view surface has neither, so REQ-013 binds it here.
- **AX-008** — `PEC-ORI-006` honesty governs the rebuild's failure mode. A rebuild that completed quietly over feeds it could not read is indistinguishable from one that read them, and `OBJ-005`'s deletability claim is only as trustworthy as the record of what a rebuild actually recovered. CON-005 records that the accepted sources do not settle whether such a rebuild is "full"; REQ-009 makes the answer visible either way.
- **AX-009** — `DL-11` is the decision that gives this deliverable its shape: `SOW-010` came to `PKG-03` as the reconciler entry point while the store-path rule stayed in `PKG-01`, and `SOW-054`'s rebuild bounds went to `DEL-03-06` as reconcile performance. Absorbing the store lifecycle, the performance bound, or the parsers would undo that decision. `DL-4` does the same work on the ingest side: seven separately testable feed units, and a reconciler that consumes them rather than reimplementing them.
- **AX-010** — The eleven upstream edges and the thirteen downstream relations cited in this contract are `PROPOSAL` stratum and are *accepted* at that stratum: `D-PEC-62` §1(4) records the owner accepting the DAG candidate v0.2 exhibit "accepted, all strata as presented", and that packet reads "as presented" as accepting the exhibit's **flags as flags**, so what remains recorded-but-unresolved is the specific annotated set — `E-A11` (AMBIGUOUS_BASIS), `E-P69`/`E-N02` (PHASE_TENSION), `E-N13`/`E-N18` (LOW_CONFIDENCE), the `C-02` direction, and the `C-08` standing-node set — none of which touches any edge cited here; every edge named in this contract carries an empty `Flag` column in the exhibit. Stratum is provenance, not authority: it records how an edge was derived, not whether it has been accepted, and citation does not convert `PROPOSAL` to `DECLARED`.
- **AX-011** — Edge direction is a constraint on this contract, not a licence, and this deliverable is the convergence node of the `P1` graph, where that discipline is easiest to lose. `RequiredMaturity` `INITIALIZED` on all eleven upstream edges means each upstream *contract* is the reliable input, not any upstream artifact; this contract is written against the obligations quoted in CLM-012 through CLM-016 and asserts nothing about upstream implementation state. Consuming eleven contracts imposes no obligation on any of the eleven, and being consumed or tested by thirteen downstream deliverables neither expands this contract's scope nor transfers any of theirs into it — least of all `DEL-10-02`'s kill test, which runs on this deliverable from outside (CLM-017).
- **AX-012** — Unknowns stay marked. TBD-001 through TBD-005 and CON-001, CON-003 through CON-005 are recorded rather than resolved by inference. D-PEC-78 O-A resolved `OI-003` and SCA-004 propagated that result into revision 1.4; CON-002 preserves the stable interface boundary and the separately unresolved TBD-005. `OI-012` is decided at `DEL-00-01`'s ADR under owner review, and a production choice that settled it would be a decision taken in the wrong place. `C-03` `PACKAGE_LEVEL`, `C-04` `PHASE_PRECEDENCE`, and `C-10` `STRATUM_RULE` are register-wide non-gating constraints recorded in `_DEPENDENCIES.md`, and blocker output under the `FULL_GRAPH` mode at threshold `INITIALIZED` is advisory visibility only, never work assignment.
- **AX-013** — This contract is lifecycle-neutral. `_STATUS.md` remains the sole lifecycle authority and is untouched by the run that authored this document; the deliverable is at `INITIALIZED` and nothing has been built.

**Quotation record.** Every quotation in this contract is verbatim from the
named source. Exactly two are elided, both marked with ellipses at the point of
elision and enumerated here in full: the `DL-11` Decision-cell quotation in
CLM-008, elided between its `SOW-010` and `SOW-054` clauses and after the
`SOW-054` clause; and the `PEC-K-02` quotation in CLM-021, elided between
"regenerated from sources by one command" and "PEC output is never citable as
authority". No other quotation in this document omits text from the span it
presents.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-010 OBJ-005 | REQ-001, CLM-001, CLM-003, CLM-006, TBD-002 | AC-001 | VER-001 | The documented invocation surface and a single-invocation rebuild transcript over a fixture corpus spanning every registered loop, showing no operator step or second command |
| OUT-001 | SOW-010 OBJ-005 | REQ-002, CLM-012, CLM-021, AX-003, AX-004 | AC-002 | VER-002 | Per-entity-type provenance traces from record-tier fact to file source and upstream feed unit; the with-prior-state versus empty-store result comparison; the input-surface inspection record showing no cached or stream-derived contribution |
| OUT-001 | SOW-010 OBJ-005 | REQ-003, CLM-008, CLM-013, TBD-004 | AC-003 | VER-003 | Rebuild transcripts against absent, newly deleted, and empty store fixtures, plus a recorded search of this deliverable's source for store path, ignore-rule, creation, and deletion operations |
| OUT-001 | SOW-010 OBJ-005 | REQ-004, CLM-020, AX-006 | AC-004 | VER-004 | The presence-shaped fixture run showing no presence-tier record written, the no-presence-data rebuild transcript, and the write-surface inspection record |
| OUT-001 | SOW-021 OBJ-005 | REQ-005, CLM-002, CLM-004, CLM-013, AX-004, AX-005 | AC-005 | VER-005 | Before/after fixture-corpus tree hashes; the captured filesystem-write inventory for a rebuild with each write resolved to the store or a declared view; the call-graph inspection record showing every store write through the upstream ingest boundary and no write path against a source, governed, register, or lifecycle file |
| OUT-001 | SOW-021 OBJ-005 | REQ-006, TBD-003, CON-001 | AC-006 | VER-006 | The entry point's declared-view record (a component of OUT-001), the written-view set from a rebuild compared against it, and the delete-and-rebuild restoration transcript |
| OUT-001 | SOW-010 OBJ-005 | REQ-007, CLM-007, CLM-009, CLM-016, AX-009 | AC-007 | VER-007 | The instrumented file-open surface for a rebuild, a recorded search for feed grammar definitions and direct feed parsing, and the manifest-omitted-feed transcript |
| OUT-001 | SOW-010 OBJ-005 | REQ-008, CLM-015, TBD-005, CON-002 | AC-008 | VER-008 | The loop-set and manifest acquisition call surfaces, and a recorded search of source, fixtures, and call surface for registry path or serialization tokens and adapter.yaml field names |
| OUT-001 | SOW-010 OBJ-005 | REQ-009, CON-005, AX-008 | AC-009 | VER-009 | Per-case rebuild results for absent, unreadable, malformed, stale, and grammar-unrecognized feeds, each showing the loop and feed named and the limitation carried through |
| OUT-001 | SOW-010 OBJ-005 | REQ-010, AX-003 | AC-010 | VER-010 | Two-run record-tier comparison over an unchanged fixture corpus plus the third-run idempotence result against the already-rebuilt store |
| OUT-001 | SOW-010 OBJ-005 | REQ-011, CLM-011, CON-003 | AC-011 | VER-011 | The entity construction surface against the quoted upstream obligations, plus recorded searches of this deliverable's source for record-tier and presence-tier type definitions and for upstream-artifact assumptions |
| OUT-001 | SOW-010 OBJ-005 | REQ-012, CLM-014, AX-002 | AC-012 | VER-012 | The single-event emission record for a rebuild against the fixture log-sink stand-in, and rebuild transcripts under deleted, unwritable, and absent log stores showing unblocked completion (the kill-test transcript is DEL-10-02's evidence under SOW-055, not this deliverable's) |
| OUT-001 | SOW-010 SOW-021 OBJ-005 | REQ-013, CON-004, AX-007 | AC-013 | VER-013 | Field-by-field dumps of everything presented to the store and of every declared generated view for a content-dense fixture corpus, showing no file or diff content |
| OUT-001 | SOW-010 SOW-021 OBJ-005 | REQ-014, CLM-017, CLM-018, CLM-019, AX-009, AX-011 | AC-014 | VER-014 | Call-graph and source inspection records showing each named adjacent path absent, plus a review of this deliverable's tests confirming no criterion belonging to another deliverable |
| OUT-001 | SOW-010 SOW-021 OBJ-005 | REQ-015 | AC-015 | VER-015 | Dependency-manifest and import-graph inspection records, plus the DEL-01-05 enforcement result once that deliverable is available |
| OUT-002 | SOW-010 SOW-021 OBJ-005 | REQ-016, CLM-022 | AC-016 | VER-016 | PKG-03 test-run output mapping each executed test to its declared verification method, with no criterion asserted that this contract does not state |
| OUT-001 | SOW-010 SOW-021 OBJ-005 | CLM-005, CLM-010, AX-001, AX-010, AX-012, AX-013 | AC-017 | HUMAN_REVIEW: REVIEW gate confirms traceability to SOW-010, SOW-021, and OBJ-005, confirms the SOW-010 leg is stated as register-direct and the SOW-021 leg no more strongly than the SCA-002 record states it, and confirms no upstream, sibling, or cross-package scope absorption | Review record citing both scope-ledger rows, the SCA-002 Gate 1 binding constraint and its recorded effect, the A001/A002 row sets, and the upstream, sibling, and cross-package deliverable boundaries |
