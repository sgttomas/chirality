---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-10-03
package_id: PKG-10
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@3623b958b
project_scope_refs: [SOW-025]
package_objective_refs: [OBJ-005]
---

# Scope of Work — DEL-10-03 No-ruling-write verification

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-10-03` — "No-ruling-write
verification" — in `PKG-10` (Validation & Measurement) of the PEC v2 build. It
covers project scope item `SOW-025` in service of package objective `OBJ-005`.

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.2** (`status: current_basis`, `SCA-002` successor accepted
2026-07-25 under `D-PEC-64`), pinned at commit `3623b958b`. The
deliverable-local `_REFERENCES.md` still names "revision 1.1, accepted working
surface"; that phrase is superseded provenance awaiting a deferred pointer
sweep — `_CONTEXT.md` records revision 1.1 as "superseded by revision 1.2
(`current_basis`, SCA-002 successor)" — and it is not the basis of this
contract.

**Standing character (load-bearing), and what authorizes it.** Everything below
is written as a contract on a *continuing* verification: there is no state in
which this deliverable's assertion is finished, and a passing run is evidence
for the API state it evaluated and for no later state. That framing is directed
by this run's brief under `D-PEC-63`, whose directing sentence reads, verbatim:

> Author this contract as a STANDING assertion — a continuously re-runnable
> verification, not a one-shot artifact.

That sentence is carried durably at
`execution/_Coordination/WAVE_D-PEC-63/BATCH_B2_FANIN.md`, the batch fan-in
record, which records it verbatim. The framing is informed by, not derived
from, the `C-08` `STANDING_NODES` annotation described in CLM-007. It is
therefore a property of how this contract is written. It is not an owner-ruled
gating force, and the question of whether the verification carries
release-gating authority is routed to the owner under CON-001 rather than
assumed here.

**Objective warrant.** The `SOW-025` → `OBJ-005` attribution was made by
`SCA-002` and accepted at revision 1.2. The ruled attribution stands and is not
reinterpreted here — but the Gate 3 record rates it **LOW-MEDIUM**, the
second-weakest rating in that record's nine-row per-row attribution table, where
only `DEL-00-03` / `SOW-089` at **Q1.2** is rated **LOW** and is headed there
"the weakest in the set". This contract states the warrant no more strongly than
that record does. The record is
`execution/_ScopeChange/SCA-002_2026-07-25_1042/Amendment_Preview.md`, per-row
attribution routed as question **Q1.7**, headed "DEL-10-03 / SOW-025 —
`OBJ-005` vs `OBJ-003` vs `OBJ-006`. LOW-MEDIUM." Its reasoning reads, verbatim:

> **The honest position, now that the `SOW-055` precedent is withdrawn:** the
> authority boundary K-AUTH-1 states is **not stated by any §3 objective** —
> exactly the condition `DL-14` invoked to leave `SOW-063` intentionally
> unmapped. If this row were out-of-wave, "intentionally unmapped" would be the
> defensible answer. It is in-wave, so O-A requires a mapping, and you are
> choosing the **least-wrong** objective as an explicit act rather than
> discovering a warrant that exists.

The recommendation and the alternatives it records, verbatim:

> - **`OBJ-005`** *(recommended)* — a system that captures no authority holds
>   nothing whose deletion could block a governed act.
> - **`OBJ-003`** — the declared-surface objective is the one about what PEC *is*
>   to concurrent governed work.
> - **`OBJ-006`** — `DEL-10-03` is a PKG-10 verification deliverable and OBJ-006
>   is the measurable/falsifiable objective; against it, §11's metric list does
>   not include no-ruling-write.

The same package withdrew the register precedent that had previously supported a
stronger rating, at `C-18`: "**`SOW-055` precedent withdrawn as tautological** —
it restates OBJ-005 nearly verbatim and selects nothing for `SOW-025`". So the
operative warrant is an explicit least-wrong selection, not a textual or
precedential derivation. AC-010 puts that qualification in front of an
accountable owner rather than leaving it buried in the scope-change package.

Source chain, in order of authority for this contract:

1. `execution/_Decomposition/ScopeLedger.csv`, row `SOW-025` — the scope
   statement and its `SourceRef`, quoted in full including trailing fields:

   > SOW-025,IN,"Verify, as a tested property of the API surface, that no write path records adoption, ruling, or direction",PEC-GAT-004,PKG-10,DEL-10-03,OBJ-005,DL-11,FALSE,K-AUTH-1; verification obligation — the product boundary itself is SOW-066 (DL-8)

2. `docs/PRD.md` §9.3 (PEC-GAT), the anchor cited by `SOW-025`:

   > | PEC-GAT-004 | PEC shall provide no write path that records adoption, ruling, or direction (PEC-K-02; K-AUTH-1). |

3. `docs/PRD.md` §4.2 (PEC is not — non-goals, permanent), the boundary the
   anchor states:

   > - **Not a ruling surface.** No write path records adoption, ruling, or
   >   direction. Rulings are file-native (K-AUTH-1).

4. `execution/_Decomposition/SOFTWARE_DECOMP.md` §5, PKG-10 row for this
   deliverable:

   > | DEL-10-03 | No-ruling-write verification | TEST_SUITE | S | P1 | SOW-025 |

   with its `Deliverables.csv` row, quoted in full:

   > DEL-10-03,PKG-10,No-ruling-write verification,"Tested property: the API exposes no write path recording adoption, ruling, or direction.",TEST_SUITE,TBD,Negative-surface tests,SOW-025,OBJ-005,S,,P1

   The `ContextEnvelopeNotes` field is empty; there are no envelope notes to
   carry.

5. `execution/_Decomposition/SOFTWARE_DECOMP.md` §3, objective row:

   > | OBJ-005 | Everything PEC holds can be deleted at any moment without blocking any governed act | §3.5 | SOW-010, SOW-021, SOW-025, SOW-052..056, SOW-088; bound by C1/C2 across all items | DEL-00-01, DEL-01-03, DEL-01-05, DEL-03-01, DEL-03-06, DEL-10-02, DEL-10-03 |

6. The two upstream `EXECUTION` predecessors' own accepted contracts, read as
   contracts (CLM-008, CLM-009), and the deliverable-local control files
   (`_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `Dependencies.csv`,
   `_STATUS.md`).

- **CLM-001** — `SOW-025` is an `IN` scope item stating a *verification*
  obligation: "Verify, as a tested property of the API surface, that no write
  path records adoption, ruling, or direction". Its `SourceRef` is `PEC-GAT-004`,
  its `DecisionRef` is `DL-11`, its `OpenIssue` is `FALSE`, and its ledger note
  reads "K-AUTH-1; verification obligation — the product boundary itself is
  SOW-066 (DL-8)".
- **CLM-002** — The property under verification originates in `PEC-GAT-004`
  ("PEC shall provide no write path that records adoption, ruling, or direction
  (PEC-K-02; K-AUTH-1)") and in the permanent §4.2 non-goal "Not a ruling
  surface. No write path records adoption, ruling, or direction. Rulings are
  file-native (K-AUTH-1)." Product invariant `PEC-K-02` carries the same rule
  from the invariant side: "rulings and lifecycle state remain file-native" and
  "PEC output is never citable as authority" (`PRD.md` §6).
- **CLM-003** — `DL-8` is the twinning convention that separates the boundary
  from its verification: "a §4.2 boundary row stays OUT as the boundary record;
  the corresponding built/verified obligation is a separate IN item stating
  enforcement or verification, never the boundary itself. Pairs: SOW-025↔SOW-066
  ...; twins are distinct statements, not duplicates" (`SOFTWARE_DECOMP.md` §11
  Decision Log). Its twin is the permanent `OUT` row `SOW-066`, quoted in full:
  "SOW-066,OUT,"Ruling-surface function: recording adoption, ruling, or
  direction",§4.2,,,,,FALSE,Permanent. Verification twin: SOW-025 (DL-8)". This
  deliverable produces the verification; it is not, and cannot restate or
  narrow, the boundary record.
- **CLM-004** — `DL-11` records the package assignment as a forced boundary
  call: "SOW-025 (no-ruling-write verification) → PKG-10 per DL-8's
  verification-obligation framing", among items "assignable to two domains"
  (`SOFTWARE_DECOMP.md` §11). The behaviour under test therefore lives in its
  own home package while the verification lives here — the `PKG-10` row's
  **Exclusions** cell *excludes* "The behaviors under test (their home
  packages)" from the package's scope (`SOFTWARE_DECOMP.md` §4, whose columns
  are `PackageID | Name | Scope Description (work domain) | Assigned (count) |
  Exclusions`). The register states this as an exclusion from `PKG-10`; §4
  declares no dependency column, and none is claimed here. The boundary
  conclusion rests on that exclusion.
- **CLM-005** — `OBJ-005` states: "Everything PEC holds can be deleted at any
  moment without blocking any governed act", `SourceRef` §3.5, mapped scope
  items "SOW-010, SOW-021, SOW-025, SOW-052..056, SOW-088; bound by C1/C2 across
  all items", mapped deliverables including `DEL-10-03` (`SOFTWARE_DECOMP.md`
  §3; `PRD.md` §3 outcome 5).
- **CLM-006** — `PKG-10` is "Validation & Measurement — Release-gating proof and
  metrics: kill test, no-ruling-write verification, Step-0 baseline,
  defect/adoption/collision/parity measurement, seeded-conflict, TTL-honesty and
  stream-loss tests, usage observability, directed bootstrap progression
  evidence" (`SOFTWARE_DECOMP.md` §4, row `PKG-10`).
- **CLM-007** — `DEL-10-03` is named in constraint row `C-08` `STANDING_NODES`
  of the accepted gate exhibit: "Standing obligations: excluded from one-shot
  COMPLETE/UNBLOCKED arithmetic; they gate releases not successors" (member set
  "DEL-01-05, DEL-03-04, DEL-10-02, DEL-10-03, DEL-10-10"; evidence "Own text:
  'Automated assertion' / 'Permanent' / 'Runs at every release' / 'tested
  property' / 'standing validation'";
  `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` §C-08).
  The row's own `Notes` field reads, in full, "R3-F9; owner confirmation
  requested. DEL-10-10 is the bootstrap progression record itself". At
  `D-PEC-62` §1(4) the owner accepted the DAG candidate "**accepted, all strata
  as presented**", and that packet reads the acceptance as taking the exhibit's
  **flags as flags**: "C-08 standing-node set remain recorded-but-unresolved,
  non-gating annotations". What is settled is therefore the arithmetic exclusion
  — `C-08` is a non-gating constraint row and this deliverable is excluded from
  one-shot `COMPLETE`/`UNBLOCKED` counting. What is not settled is the
  classification's force as a release gate. The deliverable-local
  `_DEPENDENCIES.md` compresses this to "(owner-confirmed at D-PEC-62 ruling)";
  that phrase is accurate as to the arithmetic exclusion and overstates the
  rest, and this contract cites the `D-PEC-62` text over the local paraphrase.
- **CLM-008** — `[E-P54]` (`Dependencies.csv` row `DEP-10-03-003`, `EXECUTION` /
  `UPSTREAM` / `PREREQUISITE`, `RequiredMaturity` `INITIALIZED`, stratum
  `PROPOSAL`, no flag) records that the surface under negative test is
  `DEL-08-01`'s server: statement "The API surface under negative test is
  DEL-08-01's server", evidence "SOW-025: \"a tested property of the API
  surface\"". `DEL-08-01`'s own accepted contract obliges a Unix-domain-socket
  listener as the default transport, with no network-reachable listener
  delivered under that contract — its `CON-002` leaves the loopback-TCP
  question open (`SOW-083` / `OI-009`) — and a token-scoped access path that resolves every request to
  exactly one of the access classes owner, harness, and admin before any
  operation is served; it states expressly that "the operations served over that
  surface are defined by sibling deliverables, not here". This contract binds to
  those *contractual obligations* as the surface it must evaluate, and defines
  no transport and no access class of its own.
- **CLM-009** — `[E-P55]` (`Dependencies.csv` row `DEP-10-03-004`, same class,
  maturity, and stratum) records that "The schema defines the surface under
  negative test". `DEL-08-02`'s own accepted contract obliges a versioned schema
  artifact that "defines the machine-consumer request and response shapes for
  the PKG-08 API surface", carrying an explicit machine-readable version
  identifier a consumer can bind to. That contract records this deliverable's
  relation from the other side — it names `DEL-10-03` (No-ruling-write
  verification) as the party that TESTS it via `[E-P55]` — and states that "those
  consumers' own scope is not defined here". This contract is the tester; the
  tested surface is theirs, and nothing here defines or constrains schema
  content.
- **CLM-010** — Both upstream contracts are at `INITIALIZED`: they are the
  reliable inputs, and no server, token mechanism, schema artifact, or API
  operation exists. `DEL-10-03` is itself at lifecycle state `OPEN`
  (`_STATUS.md`) with no implementation present. Every requirement, acceptance
  criterion, and verification method below states a contract on future
  production; none asserts that any test, registration, or tested surface has
  been built.

## Deliverable Definition — Ontology

`DEL-10-03` is typed `TEST_SUITE` at Context Envelope `S` with `PhaseHint` `P1`
and no `ContextEnvelopeNotes`. Its description of record is "Tested property:
the API exposes no write path recording adoption, ruling, or direction", and its
anticipated artifacts are "Negative-surface tests"
(`execution/_Decomposition/Deliverables.csv`, row `DEL-10-03`;
`SOFTWARE_DECOMP.md` §5 table for `PKG-10`; restated in `_CONTEXT.md`).

- **OUT-001** — The negative-surface test suite: executable negative tests that evaluate the PEC API surface obliged by the `DEL-08-01` and `DEL-08-02` contracts and fail whenever a write path that records adoption, ruling, or direction is present or reachable — built so that the property is re-evaluated on every state presented to the suite without further action, and built to be registrable in, and bindable without modification into, an API change path or release gate owned elsewhere — together with the recorded operative definition the suite classifies against. That recorded definition is part of this output's delivery, not a separate artifact; `Deliverables.csv` names the artifact class for `DEL-10-03` as "Negative-surface tests" and admits no second artifact. The gate wiring itself is not delivered here: it is the sibling row `DEL-10-02` that carries "Kill-test harness + gate wiring" in its `AnticipatedArtifacts`, and binding this suite into an actual release gate is owned downstream, consistent with CON-001's unresolved gating force.

Unresolved information carried forward, not invented:

- **TBD-001** — `ResponsibleParty` is unassigned; `Deliverables.csv` and `_CONTEXT.md` both record `TBD`, with assignment at WORKING_ITEMS activation.
- **TBD-002** — The operative boundary between a write PEC is permitted to perform and a write that "records adoption, ruling, or direction" is not fixed by any accepted source beyond the wording of `PEC-GAT-004` and §4.2. The accepted sources do establish that some writes are expected: the reconciler "writes only its own store and generated views" (`PEC-RCN-006`, entering scope as `SOW-021`), presence records are written and TTL-aged (`PEC-PRS-001`, `PEC-K-05`), and "the append-only discipline of v1.0 PEC-I-11 applies to PEC's own event log" (`PRD.md` §6). Where exactly a record of an owner act crosses from operational projection into a ruling record is production work to define and record, not contract drafting.
- **TBD-003** — The concrete test mechanism, harness, fixture strategy, and repository location of OUT-001 are not fixed by any accepted source; `Deliverables.csv` names the artifact class "Negative-surface tests" and nothing further.
- **TBD-004** — How the suite mechanically enumerates the surface depends on decisions the upstream contracts expressly leave unresolved: the schema language, serialization, repository location, and version-identifier scheme on the `DEL-08-02` side, and the socket path, filesystem permissions, wire framing, and operation-to-access-class mapping on the `DEL-08-01` side. Each is recorded as unresolved in that deliverable's own contract. This contract records the information dependency and neither resolves those questions nor asserts any claim over them.
- **TBD-005** — Which PKG-08 surfaces fall inside "the API surface" for this verification is not enumerated by any accepted source. The accepted register records exactly two `EXECUTION` upstream edges for this deliverable, `[E-P54]` and `[E-P55]` (CLM-008, CLM-009); other PKG-08 deliverables — the compact citation-bearing response format and the SSE delta/presence subscription among them — carry no accepted edge to `DEL-10-03`. REQ-003 resolves this by construction rather than by decision: the suite enumerates from the versioned schema that the `DEL-08-02` contract obliges and from the operations actually served over the listener the `DEL-08-01` contract obliges, so a surface that appears in either is evaluated and no boundary is drawn by this contract.

Unresolved constraints carried into this contract, neither resolved nor narrowed
by authoring:

- **CON-001** — Whether this deliverable's verification carries *release-gating authority* is unconfirmed. The `C-08` `STANDING_NODES` row that classifies it records "owner confirmation requested" in its own `Notes`, and `D-PEC-62` §1(4) accepted the standing-node set as a recorded-but-unresolved, non-gating annotation rather than ruling it (CLM-007). The suite this contract requires is designed to block and its verdicts are unambiguous; what is open is whether a blocking verdict binds a release candidate or is advisory. AC-009 routes that question to an accountable owner. This contract neither asserts the authority nor waives it, and no production choice may settle it.
- **CON-002** — The objective attribution is qualified. `SCA-002` rated `SOW-025` → `OBJ-005` **LOW-MEDIUM** at Q1.7, recorded `OBJ-003` and `OBJ-006` as considered alternatives, described the choice as choosing "the **least-wrong** objective as an explicit act rather than discovering a warrant that exists", and withdrew the `SOW-055` register precedent as tautological at `C-18`. The ruled attribution is the accepted one and is used throughout this contract; the qualification is carried rather than smoothed, and AC-010 routes it to an accountable owner.
- **CON-003** — The surface under test does not exist. Both upstream contracts are at `INITIALIZED` and both record open questions of their own that the accepted sources leave to a later owner ruling — the token mechanism and the transport question on the `DEL-08-01` side, the finer taxonomy of permitted additive change on the `DEL-08-02` side. This contract binds to those contracts' *obligations*, not to any artifact, and it must not be read as asserting that a server, a schema, or an operation exists, nor as pre-empting any of those open questions.

## Completion and Reliance Basis — Epistemology

The requirements below state the contract the future verification must satisfy.
Under the standing framing established above — brief-directed and informed by
the `C-08` annotation (CLM-007, CON-001) — they bind the suite's *continuing*
behaviour: each is a property that must hold on every evaluated API state, not a
one-time production event.

- **REQ-001** — The suite shall verify the property `SOW-025` states — that no write path records adoption, ruling, or direction — over the API surface obliged by the `DEL-08-01` and `DEL-08-02` contracts, and shall fail whenever such a write path is present or reachable on the evaluated state.
- **REQ-002** — The operative definition the suite classifies against shall be recorded with the suite rather than left implicit in test code. It shall be grounded in `PEC-GAT-004` and the §4.2 non-goal, and shall distinguish the writes PEC is expected to perform — its own store and generated views, its own append-only event log, and TTL'd presence records — from a write that records adoption, ruling, or direction (TBD-002).
- **REQ-003** — The evaluated surface shall be enumerated from the versioned schema the `DEL-08-02` contract obliges — its declared request and response shapes — and from the operations observed as served over the listener the `DEL-08-01` contract obliges; the listener is obliged, the operation set is observed rather than obliged, because the `DEL-08-01` contract expressly leaves the served operations to sibling deliverables (CLM-008). The enumeration shall never come from a hand-maintained list held by the suite itself.
- **REQ-004** — Enumeration shall be fail-closed: an unresolvable or unversioned schema, an unreachable listener, or any condition under which the served surface cannot be fully enumerated is a failure, never a pass over the smaller set the suite managed to reach.
- **REQ-005** — The suite shall probe negatively as well as inspect: it shall issue requests shaped to record an adoption, a ruling, and a direction, and shall require that no such request is served and that no record of one persists after the probe.
- **REQ-006** — Absence shall be verified, not merely denial. A ruling-shaped request that is refused for one access class but served for another is a failure: the property is the absence of the write path, not the scoping of access to it. The suite shall exercise every access class the `DEL-08-01` contract obliges and shall require no new access class and no privileged bypass in order to run.
- **REQ-007** — The verification shall be built as a standing verification: re-runnable on demand and re-evaluated against every change to the API surface, every schema version, and every release candidate presented to it, against that exact presented state. It shall have no completion state, and no passing run shall be carried forward as evidence for a later state. It shall expose a binding interface through which an externally owned change path or release gate can invoke it without modification to the suite. This is a property of how this deliverable is built; this contract delivers no gate wiring and places no obligation on any other deliverable to re-run, re-certify, or maintain anything.
- **REQ-008** — The suite shall be designed to block: for a release candidate on which the verification fails, or against which it has not been executed, the mechanism shall return an explicit blocking verdict rather than a pass, a skip, or an absent result. This requirement binds the mechanism's design intent and the verdict it produces. It does not, by itself, establish that a blocking verdict binds a release: whether the verification carries release-gating authority follows the pending `C-08` confirmation recorded at CON-001 and is routed to the owner at AC-009.
- **REQ-009** — The suite shall observe only. It shall not create, enable, widen, stub, or simulate any write path on the surface under test; it shall not modify that surface, any governed file, or any source it reads; and it shall leave no probe-seeded record behind.
- **REQ-010** — The suite shall define no transport, no access class, and no schema content, and shall place no obligation on `DEL-08-01` or `DEL-08-02`. It verifies the absence of ruling, adoption, and direction write paths on whatever surface those contracts oblige; where that surface changes, the suite re-evaluates it rather than constraining it.
- **REQ-011** — Failure shall be reported explicitly and locatably — the offending operation and the schema element or served route through which it is reachable — and a pass shall never be reported over a surface the suite did not actually evaluate.
- **REQ-012** — Tests and deterministic checks shall implement the verification methods declared below. They shall not define scope, requirements, or acceptance criteria: the property verified here comes from `SOW-025` and `PEC-GAT-004`, and OUT-001 exists because the accepted register names it.

Acceptance criteria for `DEL-10-03`. Each states a property the future
implementation must exhibit; none asserts a present state.

- **AC-001** — On an API state whose surface contains no write path recording adoption, ruling, or direction the suite passes; on a state that introduces such a path it fails and names both the offending operation and the schema element or served route through which it is reachable.
- **AC-002** — The operative definition is recorded with the suite, cites `PEC-GAT-004` and the §4.2 non-goal, and enumerates the expected PEC writes it treats as permitted; every classification the suite makes traces to that recorded definition, and no outcome depends on an unrecorded reading of TBD-002.
- **AC-003** — The evaluated operation set is derived from the obliged schema's declared shapes and from the operations served over the obliged listener; introducing an operation into either source without it entering the suite's evaluated set produces a reported failure rather than a pass, and an enumeration that cannot be resolved yields a failure rather than a pass over a partial set.
- **AC-004** — Adoption-, ruling-, and direction-shaped probes are refused for every access class the `DEL-08-01` contract obliges, no probe is served, no record of a probe persists after the run, and a state in which such a request is refused for one class but served for another is reported as a failure.
- **AC-005** — Given an unreachable listener, an unresolvable or unversioned schema, or an induced tooling error, the suite reports failure; no such condition yields a pass, a skip, or an empty successful result.
- **AC-006** — The suite re-runs without modification against any state presented to it: for each presented API-surface change, each presented schema version, and each presented release candidate it produces an execution bound to the exact state it evaluated, and it presents no earlier passing run as evidence for a later state. It exposes a binding interface an externally owned change path or release gate can invoke, and when that interface is invoked against a state the suite has not evaluated it reports the missing evaluation rather than a pass, a skip, or a silent no-op.
- **AC-007** — On a release candidate deliberately carrying a ruling-recording write path, and on one against which the suite was withheld, the mechanism returns an explicit blocking verdict. Whether that verdict binds the release is CON-001 and AC-009, not this criterion.
- **AC-008** — The delivered suite traces to `SOW-025` and `OBJ-005` and introduces no scope beyond that ledger row: it defines no transport, no access class, and no schema content, asserts no obligation on `DEL-08-01` or `DEL-08-02`, adds no write path of its own, and leaves the surface under test and every governed file unmodified across a full run.
- **AC-009** — An accountable owner confirms, or declines to confirm, that the verification delivered under this contract carries release-gating authority — that its blocking verdict blocks a release candidate — given that `C-08`'s standing-node classification carries "owner confirmation requested" in its own `Notes` and was accepted at `D-PEC-62` §1(4) as a recorded-but-unresolved, non-gating annotation (CLM-007, CON-001). A decline leaves the mechanism's verdicts advisory and invalidates no other criterion in this contract; the standing framing of the contract stands either way, because it is how the contract is written rather than a claim about the verification's force.
- **AC-010** — An accountable owner confirms that the attribution `SOW-025` → `OBJ-005` remains acceptable given the recorded LOW-MEDIUM rating at Q1.7, the finding that "the authority boundary K-AUTH-1 states is **not stated by any §3 objective**", the characterization of the choice as "the **least-wrong** objective as an explicit act rather than discovering a warrant that exists", the recorded unadopted alternatives `OBJ-003` and `OBJ-006`, and the withdrawal of the `SOW-055` precedent as tautological at `C-18` (CON-002).

## Production and Verification Method — Praxeology

Expected production sequence: record the operative definition of a ruling,
adoption, or direction write (REQ-002) before writing any test, because every
later classification depends on it; build the enumeration against the obliged
schema and the obliged listener (REQ-003, REQ-004); build the negative probes
and the absence-not-denial check (REQ-005, REQ-006); make the suite re-runnable
and expose its binding interface (REQ-007, REQ-008) last, so that what is
offered for binding is what was actually built. Binding the suite into an actual
release gate is owned downstream and is not performed under this contract
(CON-001). All work is bounded to this deliverable's own artifacts and to
read access over the surface under test; this contract authorizes no register,
decomposition, or PRD edit, no edit to any `PKG-08` deliverable, and no write to
any gate configuration. The verification methods below are themselves standing:
each is re-run on every evaluated state, not once at hand-over.

- **VER-001** — Execute the suite against a conforming API fixture and against fixtures that introduce a ruling-recording write path at (a) a schema-declared request shape and (b) a served route absent from the schema; assert a pass on the conforming fixture and, on each violating fixture, a failure naming the offending operation and its schema element or route.
- **VER-002** — Inspect the recorded operative definition against the `PEC-GAT-004` and §4.2 wording and against the enumerated permitted-write set; trace a sample of the suite's pass and fail classifications back to that recorded definition and confirm none rests on an unrecorded reading.
- **VER-003** — Enumeration audit: compare the suite's evaluated operation set against the schema's declared shapes and the listener's served operations for the same state; then add an operation to each source in turn and assert the suite reports the unevaluated addition rather than passing; then present an unresolvable schema and assert a failure rather than a partial-set pass.
- **VER-004** — Probe execution: issue adoption-, ruling-, and direction-recording requests under each access class the upstream contract obliges; assert refusal in every case, assert that no record persists after each probe, and assert a reported failure on a seeded state in which one access class is served while another is refused.
- **VER-005** — Fault injection: run the suite with an unreachable listener, an unresolvable and an unversioned schema, and an induced tooling error; assert a reported failure in every case with no pass, skip, or empty success.
- **VER-006** — Re-runnability and bindability demonstration on scratch fixtures: present the suite with a sequence of API-surface changes, at least one additional schema version, and at least one release-candidate fixture; assert an execution is produced for each presented state, that each execution is bound to the state it evaluated, and that no result is reused across states; then invoke the suite's binding interface from a scratch caller against a state the suite has not evaluated and assert it reports the missing evaluation rather than a pass, a skip, or a silent no-op. The method exercises the suite against fixtures it is given and writes no gate configuration this contract does not own.
- **VER-007** — Blocking-verdict demonstration: submit a release candidate carrying a ruling-recording write path, and one candidate with the suite withheld; assert that the mechanism returns an explicit blocking verdict in both cases. The method demonstrates the mechanism's verdict, not the release process's obligation to honour it (CON-001).
- **VER-008** — Boundary and self-inspection: compare the surface under test and the working tree before and after a full run; inspect the suite for any created, stubbed, or simulated write path and for any privileged access class it requires; and inspect its declared inputs to confirm it cites the two upstream contracts' obligations without restating, constraining, or extending them, and introduces no criterion absent from this contract.

## Governing Values and Decisions — Axiology

- **AX-001** — `OBJ-005` governs as ruled: everything PEC holds can be deleted at any moment without blocking any governed act. The warrant recorded for this row is that "a system that captures no authority holds nothing whose deletion could block a governed act", rated LOW-MEDIUM and chosen as the least-wrong option (CON-002). This contract uses the attribution and states the warrant no more strongly than the record does.
- **AX-002** — `DL-8` twinning governs the boundary between this deliverable and the rule it verifies. `SOW-066` is the permanent `OUT` boundary record; `SOW-025` is the separate `IN` verification obligation, "never the boundary itself" (CLM-003). Nothing produced under this contract restates, narrows, widens, or substitutes for the boundary; a passing suite is evidence about an evaluated state, not a restatement of the product rule.
- **AX-003** — The standing shape of this contract is brief-directed contract design, informed by the `C-08` annotation rather than derived from an owner ruling on it (CLM-007, CON-001). It governs how the obligations above are written: treating a passing run as completion would convert a continuing verification into a one-shot artifact, which the brief's direction and the deliverable's own description ("Tested property") both refuse. It is not a claim that the verification has been ruled release-blocking; that question is CON-001, routed at AC-009.
- **AX-004** — Edge direction is a discipline, not a formality. `[E-P54]` and `[E-P55]` name this deliverable as the tester and `DEL-08-01` and `DEL-08-02` as the tested; the second is recorded from the other side in that deliverable's own contract. This contract therefore takes their obligations as its evaluated surface and absorbs none of their scope: it defines no transport, no access class, and no schema content (REQ-010, AC-008), and it imposes nothing on them.
- **AX-005** — Stratum is provenance, not authority. Both upstream edges are `PROPOSAL`, accepted "all strata as presented" at `D-PEC-62` §1(4), which that packet reads as taking the exhibit's flags as flags; neither edge carries a flag. `C-10` `STRATUM_RULE`'s own text ends "strata are provenance not authority", and `_DEPENDENCIES.md` records that blocker output is "advisory visibility only — never work assignment". Edges are cited here by `EdgeID` at that status and are not converted into `DECLARED`.
- **AX-006** — `C-04` `PHASE_PRECEDENCE` is a register-wide non-gating constraint and phase hints are release-strategy ordering whose hard-versus-soft classification is a Phase 1.3 owner ruling. `DEL-10-03`, `DEL-08-01`, and `DEL-08-02` all carry `PhaseHint` `P1`, so no phase tension arises among them; this contract makes no staging claim beyond recording that fact.
- **AX-007** — `PEC-K-06` observation-not-participation governs the suite itself: "verification creates findings, never rewrites sources" is the invariant lineage `PRD.md` §6 records for it, and `PEC-RCN-004` states the same rule for the reconciler. A negative-surface test that had to create a write path in order to test for one would contradict the property it exists to verify; REQ-009 and AC-008 exist for that reason.
- **AX-008** — The accepted basis is `SOFTWARE_DECOMP.md` revision 1.2 at commit `3623b958b`, accepted through `SCA-002` under `D-PEC-64`. The revision 1.1 phrase still present in `_REFERENCES.md` is a deferred pointer sweep and superseded provenance; it is recorded here so the divergence is visible rather than silently normalized.
- **AX-009** — Unknowns remain marked. TBD-001 through TBD-005 and CON-001 through CON-003 are recorded rather than resolved by inference; in particular the surface under test does not yet exist, and its shape follows decisions that belong to the upstream deliverables and to their owner rulings, not to this contract.
- **AX-010** — This contract is lifecycle-neutral. `_STATUS.md` remains the sole lifecycle authority, is untouched by the run that authored this document, and records `OPEN`; nothing here asserts that any test, registration, or tested surface exists.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-025 OBJ-005 | REQ-001, REQ-002, REQ-011, CLM-001, CLM-002, TBD-002 | AC-001, AC-002 | VER-001, VER-002 | Fixture set with expected verdicts, suite output naming each offending operation and the schema element or route through which it is reachable, and the recorded operative definition read against the PEC-GAT-004 and §4.2 wording with its permitted-write enumeration |
| OUT-001 | SOW-025 OBJ-005 | REQ-003, REQ-004, REQ-005, REQ-006, CLM-008, CLM-009, TBD-004, TBD-005 | AC-003, AC-004 | VER-003, VER-004 | Enumeration audit comparing the evaluated operation set against the obliged schema's declared shapes and the obliged listener's served operations, with reported failures for a seeded unevaluated addition and an unresolvable enumeration; plus probe transcripts per access class showing refusal, no persisted record, and a reported failure on a seeded class-asymmetric state |
| OUT-001 | SOW-025 OBJ-005 | REQ-004, REQ-011, CON-003 | AC-005 | VER-005 | Fault-injection transcripts showing a reported failure on an unreachable listener, an unresolvable schema, an unversioned schema, and an induced tooling error, with no pass, skip, or empty success |
| OUT-001 | SOW-025 OBJ-005 | REQ-007, REQ-008, CLM-007, AX-003, CON-001 | AC-006, AC-007 | VER-006, VER-007 | Execution records binding each presented state — API-surface changes, an additional schema version, and a release-candidate fixture — to the run that evaluated it; a scratch-caller invocation of the suite's binding interface against an unevaluated state showing the missing evaluation reported rather than passed or silently skipped; and blocking-verdict demonstrations for a violating candidate and for a withheld check |
| OUT-001 | SOW-025 OBJ-005 | REQ-009, REQ-010, REQ-012, CLM-003, CLM-004, AX-002, AX-004, AX-007 | AC-008 | VER-008 | Before/after comparison of the surface under test and the working tree for a full run, inspection findings showing no created, stubbed, or simulated write path and no privileged access class required, and a declared-input review confirming the two upstream contracts are cited as obligations without restatement or extension |
| OUT-001 | SOW-025 OBJ-005 | REQ-008, CLM-007, CON-001, AX-003 | AC-009 | HUMAN_REVIEW: accountable owner confirmation or declination that the verification carries release-gating authority, given C-08's "owner confirmation requested" note and D-PEC-62 §1(4)'s acceptance of the standing-node set as a recorded-but-unresolved non-gating annotation | Dated owner ruling recorded against this deliverable, stating whether a blocking verdict blocks a release candidate or is advisory, and leaving the contract's standing framing intact either way |
| OUT-001 | SOW-025 OBJ-005 | CLM-005, CLM-010, CON-002, AX-001 | AC-010 | HUMAN_REVIEW: accountable owner confirmation that the LOW-MEDIUM attribution of SOW-025 to OBJ-005 stands, given the Q1.7 finding that no §3 objective states the K-AUTH-1 authority boundary, the least-wrong-selection characterization, the unadopted alternatives OBJ-003 and OBJ-006, and the C-18 withdrawal of the SOW-055 precedent | Dated owner ruling recorded against this deliverable, explicitly addressing the Q1.7 qualification rather than restating the attribution |
