---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-10-03
package_id: PKG-10
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@189f205ff02df4111b33c20be441ce06e65ada7a
project_scope_refs: [SOW-025]
package_objective_refs: [OBJ-005]
---

# Scope of Work — DEL-10-03 No-ruling-write verification

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-10-03` — "No-ruling-write
verification" — in `PKG-10` (Validation & Measurement) of the PEC v2 build. It
covers project scope item `SOW-025` in service of package objective `OBJ-005`.

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.6** (`current_basis`, SCA-006 successor), accepted by the owner at
SCA-006 checkpoint group 3 on 2026-09-26. The frontmatter pin
`189f205ff02df4111b33c20be441ce06e65ada7a` is the checkpoint-3 acceptance
commit, an ancestor of `origin/main`. At that commit `SOFTWARE_DECOMP.md` has
SHA-256 `9374c21fb87b…8eb1`, `Deliverables.csv` `94ee5d182ae9…9805`,
`ScopeLedger.csv` `1d24a4b86f05…916e` and `ContextBudgetQA.csv`
`93b0bb075a0e…4c7c`, and `docs/PRD.md` v2.4 has SHA-256 `ae49b8065698…3fbe`.
The deliverable-local `_REFERENCES.md` names "revision 1.6, accepted
`current_basis`; SCA-006 successor" and PRD v2.4, and `_CONTEXT.md` records the
supersession chain from revision 1.1 through revision 1.6; both restate register
truth and neither is the basis of this contract. This contract replaces the
deliverable's prior contract as a whole (AX-012).

**Observation commit.** The pin binds the accepted decomposition bytes only.
Unless a claim names another commit, every statement below about the state of a
file, record, lifecycle or decision is an observation at `origin/main`
`125cfacc1`. At that commit the four decomposition files named above and the
PRD are byte-identical to the pin, so every locus this contract quotes from them
reads the same at both commits.

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

6. The two upstream `EXECUTION` predecessors' own contracts, read as
   contracts (CLM-008, CLM-009), and the deliverable-local control files
   (`_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `Dependencies.csv`,
   `_STATUS.md`).

7. `docs/PRD.md` v2.4 §8 (the `agent` access class), `PEC-API-007` (the agent
   tool-call query surface), `PEC-K-03`, §15 and the §12 standing
   reliance-advertisement gate, which SCA-006 brought into the PRD and which
   bear on this deliverable through its negative surface (CLM-011) and through
   the distinction between operational reliance and authority (CLM-012).

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
- **CLM-006** — `PKG-10` is named "Validation & Measurement", with the scope
  description "Release-gating proof and metrics: kill test, no-ruling-write
  verification, Step-0 baseline, defect/adoption/collision/parity measurement,
  seeded-conflict, TTL-honesty and stream-loss tests, usage observability,
  directed bootstrap progression evidence, and the reliance-advertisement gate"
  and the assigned set "SOW-025, 055, 058..064, 084, 085, 093, 100 (13)"
  (`SOFTWARE_DECOMP.md` §4, row `PKG-10`). `SOW-100`, the reliance-advertisement
  gate owned by `DEL-10-13`, entered that set under SCA-006 (its ledger
  `DecisionRef` is `SCA-006`).
- **CLM-007** — `DEL-10-03` is named in constraint row `C-08` `STANDING_NODES`
  of the accepted gate exhibit
  (`execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` §C-08),
  whose row reads in full:

  > `C-08,STANDING_NODES,"DEL-01-05, DEL-03-04, DEL-10-02, DEL-10-03, DEL-10-10","Own text: ""Automated assertion"" / ""Permanent"" / ""Runs at every release"" / ""tested property"" / ""standing validation""",Standing obligations: excluded from one-shot COMPLETE/UNBLOCKED arithmetic; they gate releases not successors,R3-F9; owner confirmation requested. DEL-10-10 is the bootstrap progression record itself`

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
  DEL-08-01's server". The accepted gate exhibit's evidence for the edge cites
  `SOW-025`'s phrase "a tested property of the API surface". As observed at
  `125cfacc1`, the row's `EvidenceFile` is `execution/_Decomposition/Deliverables.csv`,
  its `SourceRef` is "Deliverables.csv row DEL-08-01 Description column", its
  `EvidenceQuote` is the revision-1.6 `DEL-08-01` description, "Local-only
  Unix-socket binding with token-scoped access classes (owner, harness, agent,
  admin; agent is read-only query for tool calls); auth-reuse choice tracked by
  OI-006.", its `LastSeen` is `2026-09-26`, and its `Notes` read "Evidence
  refreshed under D-PEC-101 (SCA-006 A-31: DEL-08-01 description re-expressed);
  PROPOSAL; Flag=none; EdgeID=E-P54". `DEL-08-01`'s own contract obliges a
  Unix-domain-socket listener as the default transport (`DEL-08-01/OUT-001`),
  with no network-reachable listener delivered under that contract — its
  `DEL-08-01/CON-002` leaves the loopback-TCP question open (`SOW-083` /
  `OI-009`) — and a token-scoped access path that resolves every request to
  exactly one access class before any operation is served (`DEL-08-01/OUT-002`,
  `DEL-08-01/REQ-002`); it leaves the operations served over that surface to
  sibling deliverables (`DEL-08-01/CLM-001`). The access-class set that contract
  is to deliver follows `SOW-003` and PRD v2.4 §8, which now set owner, harness,
  agent, and admin, the `agent` class being read-only query access for tool
  calls (CLM-011); the `DEL-08-01` contract is rebuilt for that set in the same
  S4 Scope of Work currency packet. This contract binds to those *contractual obligations* as the
  surface it must evaluate, and defines no transport and no access class of its
  own.
- **CLM-009** — `[E-P55]` (`Dependencies.csv` row `DEP-10-03-004`, same class,
  maturity, and stratum) records that "The schema defines the surface under
  negative test". `DEL-08-02`'s own contract obliges a versioned schema
  artifact that "defines the machine-consumer request and response shapes for
  the PKG-08 API surface" (`DEL-08-02/OUT-001`), carrying an explicit
  machine-readable version identifier a consumer can bind to
  (`DEL-08-02/REQ-001`). That contract records this deliverable's relation from
  the other side — it names `DEL-10-03` (No-ruling-write verification) as the
  party that TESTS it via `[E-P55]` — and states "Those consumers' own scope is
  not defined here." (`DEL-08-02/CLM-002`). This contract is the tester; the
  tested surface is theirs, and nothing here defines or constrains schema
  content.
- **CLM-010** — As observed at `125cfacc1`, `DEL-08-01` is at lifecycle
  `INITIALIZED` and `DEL-08-02` at `CHECKING`; their edges state
  `RequiredMaturity` `INITIALIZED` and `SatisfactionStatus` `PENDING` (CLM-015),
  and their contracts are the reliable inputs. `DEL-10-03` is itself at
  lifecycle state `INITIALIZED` (`_STATUS.md`) with no implementation present.
  One artifact of the tested surface exists: the API contract canary
  `v2/contracts/api/v1/schema.json` (SHA-256 `0a4e42737e62…5c67`), added by
  commit `e9fec7fff` (an ancestor of `125cfacc1`), with its compatibility test
  `v2/tests/contracts/api/test_api_schema_compatibility.py`. The canary declares
  `"api_schema_version": 1` and two shapes, `CapabilityRequest` and
  `CapabilityResponse`, whose `capability` and `use_case` fields are free
  strings; it enumerates no capability set. No server, listener, token
  mechanism, tool-call surface or served API operation exists: no path under
  `v2/` names a server, a socket or a token. *Interpretation:* at
  `api_schema_version` 1 the schema alone does not enumerate operations, so the
  operation set REQ-003 evaluates would come from the served side and from
  capability contracts not yet written; how the suite enumerates it stays
  TBD-004. Every requirement, acceptance criterion, and verification method
  below states a contract on future production; none asserts that any test or
  registration of this suite has been built, or that the tested surface exists
  beyond that canary.
- **CLM-011** — SCA-006 (DQ-a; PRD v2.4, adopted 2026-09-25 by owner acceptance
  of SCA-006 checkpoint group 2) adds a fourth access class and an agent query
  surface to the API this deliverable verifies. `SOW-003` now reads "Implement
  token-scoped access with four access classes: owner, harness, agent
  (read-only query for tool calls), admin" (`ScopeLedger.csv`, `DecisionRef`
  "DL-11; SCA-006"). PRD v2.4 §8 reads "access classes are owner, harness,
  agent, and admin" and defines the new class: "The `agent` class is read-only
  query access for tool calls: orientation, deltas, gate verdicts,
  decision-slate and presence reads, with no event ingest, no presence reports
  and no admin act." It leaves the credentials open: "the token mechanism,
  including credentials for the `agent` class, is the open §16.6 decision."
  `PEC-API-007` (§9.6) reads "PEC shall offer a read-only query interface
  packaged for agent tool calls, over the same versioned API and responses
  (PEC-API-003, PEC-API-004, PEC-API-006, PEC-ORI-007), under the `agent`
  access class." and ends "Before any such tool is declared or invoked, the PEC
  Domain Engine Profile (`_DomainEngines/profiles/pec.yaml`) is amended under
  its own tier-0 act. P3 capability." That surface is `SOW-099`, owned by
  `DEL-08-06` (Agent tool-call query surface, `PhaseHint` `P3`), whose register
  description ends "enabling it is consumer-owned; writes nothing."
  *Interpretation:* the `agent` class and the tool-call surface are part of the
  API surface `SOW-025` names, so they fall inside this verification's negative
  surface; nothing in these sources makes a read-only class or a read-only tool
  an exception to it (REQ-013, REQ-014).
- **CLM-012** — PRD v2.4 separates operational reliance from authority.
  `PEC-K-03` lets a consumer, or an agent acting through one or through the
  tool-call surface, take a record-tier claim as true within the pin, coverage
  and trust tier a response declares, and ends "Operational reliance is
  available only from a PEC release that has passed the §12
  reliance-advertisement gate." §15 records the `D-PEC-90` boundary: "No
  governed record cites PEC; no ruling, acceptance, lifecycle transition or
  merge rests on PEC output; deleting PEC still blocks nothing." `PEC-K-02`
  keeps PEC output "never citable as authority" (CLM-002). The §12 gate is
  `SOW-100`, owned by `DEL-10-13`, whose register description composes "DEL-03-04
  parity, DEL-04-05 coverage honesty under seeded feed failures, the DEL-04-03
  reliance envelope, the PKG-02 parser fixture suites and the DEL-10-02 kill test
  into one gate record"; the no-ruling-write verification is not in that list,
  and no register edge connects `DEL-10-13` with `DEL-10-03` (CLM-015).
  *Interpretation:* operational reliance is a reader's act on data PEC serves
  and records nothing in PEC, so it neither creates a write path of the kind
  `SOW-025` forbids nor turns any PEC output into a ruling; this deliverable
  verifies the authority side only (AX-011).
- **CLM-013** — The causes of this currency rebuild are recorded in the two
  scope changes. SCA-005 `Propagation_Plan.md` §B4 classes this contract
  `housekeeping only`, ticking both housekeeping fixes: the unresolvable
  `@3623b958b` basis pin and the false "`_REFERENCES.md` still names revision
  1.1" claim. SCA-006 `Impact_Assessment.md` §7.1 classes it **AFFECTED**
  (DQ-a) at the prior contract's CLM-008 (line 191) and records that "the new
  class must also be in the no-ruling-write negative surface". SCA-006
  `Propagation_Plan.md` §B4, whose membership the checkpoint-2 acceptance of
  2026-09-25 fixed, records the cause "CLM-008 L191 paraphrases the three-class
  set; the `agent` class joins the no-ruling-write negative surface", the
  combined class `STALE_REVIEW_REQUIRED` (review level) and work-graph node S4,
  held to checkpoint 3 although §7.1 had routed it to S1. This contract carries
  both causes in one pass (AX-012).

## Deliverable Definition — Ontology

`DEL-10-03` is typed `TEST_SUITE` at Context Envelope `S` with `PhaseHint` `P1`
and no `ContextEnvelopeNotes`. Its description of record is "Tested property:
the API exposes no write path recording adoption, ruling, or direction", and its
anticipated artifacts are "Negative-surface tests"
(`execution/_Decomposition/Deliverables.csv`, row `DEL-10-03`;
`SOFTWARE_DECOMP.md` §5 table for `PKG-10`; restated in `_CONTEXT.md`).

- **OUT-001** — The negative-surface test suite: executable negative tests that evaluate the PEC API surface obliged by the `DEL-08-01` and `DEL-08-02` contracts and fail whenever a write path that records adoption, ruling, or direction is present or reachable — built so that the property is re-evaluated on every state presented to the suite without further action, and built to be registrable in, and bindable without modification into, an API change path or release gate owned elsewhere — together with the recorded operative definition the suite classifies against. That recorded definition is part of this output's delivery, not a separate artifact; `Deliverables.csv` names the artifact class for `DEL-10-03` as "Negative-surface tests" and admits no second artifact. The gate wiring itself is not delivered here: it is the sibling row `DEL-10-02` that carries "Kill-test harness + gate wiring" in its `AnticipatedArtifacts`, and binding this suite into an actual release gate is owned downstream, consistent with CON-001's unresolved gating force.

### Identity of record

- **CLM-014** — `DEL-10-03` is named "No-ruling-write verification", Type `TEST_SUITE`, Context Envelope `S`, `PhaseHint` `P1`, `ResponsibleParty` `TBD`, `CoversScopeItems` `SOW-025`, `SupportsObjectives` `OBJ-005`, with an empty `ContextEnvelopeNotes` field; its `Deliverables.csv` row is identical at the revision-1.4 pin `65955cceb` and at `125cfacc1`. `ContextBudgetQA.csv` row `DEL-10-03` records `Risk` `LOW` and `RecommendedAction` `None`. The folder was scaffolded under `D-PEC-62` on 2026-07-25. `_STATUS.md` records `INITIALIZED`, set on 2026-07-25 after `OPEN` the same day; its 2026-09-26 history entry records that its former `## Remaining` section was retired under `D-PEC-99` and that the section's one item moved to the `D-PEC-83` E evidence-inquiry set of the `D-PEC-99` exhibit, still unselected. That item is not a carry-forward into this contract.

### Placement in the work graph

- **CLM-015** — `Dependencies.csv` holds four rows: `DEP-10-03-001` and `DEP-10-03-002` are `ANCHOR` rows (package-local to `PKG-10`; the `SOW-025` requirement trace), and `DEP-10-03-003` and `DEP-10-03-004` are the two `EXECUTION` upstream edges `[E-P54]` and `[E-P55]` of CLM-008 and CLM-009, each with `SatisfactionStatus` `PENDING` and `Status` `ACTIVE`. `_DEPENDENCIES.md` lists those two predecessors and no downstream relation. The `Dependencies.csv` registers of `DEL-08-06`, `DEL-10-13` and `DEL-10-02` name no edge to or from `DEL-10-03`, and this register names none of them. Phase staging, checked against the `PhaseHint` column of `Deliverables.csv` for every deliverable this contract names in its own voice: `DEL-10-03`, `DEL-08-01`, `DEL-08-02`, `DEL-10-02`, `DEL-10-13`, `DEL-04-03` and `DEL-03-01` carry `P1`; `DEL-00-03` carries `pre-P1`; `DEL-08-06` carries `P3`, which is why REQ-014 is conditional on that surface existing.

### Boundaries

- **CLM-016** — The acts adjacent to this verification are owned elsewhere than `DEL-10-03` and are cited here, never discharged. Serving the Unix-socket listener, the token-scoped access path and the access-class decision, the `agent` class included, is `DEL-08-01` (`SOW-003`, `SOW-040`). Authoring the versioned API schema and its additive-compatibility check is `DEL-08-02` (`SOW-042`). Declaring and packaging the agent tool-call query tools over the read API is `DEL-08-06` (`SOW-099`); enabling them in a harness, App or agent configuration is consumer-owned (`PEC-API-007`), and the tier-0 profile amendment that must precede any such tool's declaration or invocation is a tier-0 act (CLM-011). Composing the reliance-advertisement gate record is `DEL-10-13` (`SOW-100`). Running the kill test and wiring its gate is `DEL-10-02` (`SOW-055`). Attaching per-claim citations, response stamps and the reliance envelope is `DEL-04-03` (`SOW-006`, `SOW-007`, `SOW-097`). Restricting reconciler writes to PEC's own store and generated views is `DEL-03-01` (`SOW-021`). The ruling-surface boundary itself is the permanent `OUT` row `SOW-066`, which no deliverable implements (CLM-003).

### Open information

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
- **CON-003** — The surface under test does not yet exist as a served surface. `DEL-08-01` is at `INITIALIZED` and `DEL-08-02` at `CHECKING`; the only artifact present is the version-1 schema canary (CLM-010); and both contracts record open questions of their own that the accepted sources leave to a later owner ruling — the token mechanism, including the credentials of the `agent` class (PRD v2.4 §16.6), and the transport question on the `DEL-08-01` side, the finer taxonomy of permitted additive change on the `DEL-08-02` side (`DEL-08-02/TBD-004`). This contract binds to those contracts' *obligations*, not to any artifact, and it must not be read as asserting that a server, a served operation, or a tool-call surface exists, nor as pre-empting any of those open questions.
- **CON-004** — How the agent tool-call query surface enters this verification is not fixed by any accepted source. `PEC-API-007` places it over the same versioned API under the `agent` class (CLM-011), so its requests reach the listener that REQ-003 enumerates; but no register edge connects `DEL-10-03` with `DEL-08-06` (CLM-015), `DEL-08-06` has no Scope of Work at `125cfacc1`, so the shape of its tool definitions is unfixed, and whether the suite must also enumerate those tool definitions as a source of their own is open. Whether exercising a tool in a scratch fixture counts as invoking it under the tier-0 gate is open as well. The first question resolves at `DEL-08-06`'s first Scope of Work (work-graph node K2), together with a dependency-register act if an edge is to exist; the second at the tier-0 profile act (SCA-006 `Propagation_Plan.md` §B6). Neither is settled by assumption here, and REQ-014 binds only the property.

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
- **REQ-013** — The access classes exercised under REQ-006 shall include the read-only `agent` class that `SOW-003` and PRD v2.4 §8 add to owner, harness, and admin (CLM-011). The suite shall present its adoption-, ruling-, and direction-shaped probes under the `agent` class as under every other class, and a probe of that shape that is served under the `agent` class, or that leaves a record, is a failure. The class's read-only definition is part of the property under test, never a reason to skip the class; the suite obtains `agent` credentials only through the mechanism the `DEL-08-01` contract obliges, which the open §16.6 decision fixes (CON-003).
- **REQ-014** — Where the agent tool-call query surface exists (`PEC-API-007`, `SOW-099`, a `P3` capability of `DEL-08-06`), the suite shall evaluate it as part of the API surface: the requests reachable through it are evaluated as requests under the `agent` class, and a tool through which adoption, ruling, or direction can be recorded is a failure, reported with the tool and the operation it reaches (REQ-011). At a state where that surface does not exist, the suite shall report it as not present, never as passed. The suite shall declare no such tool, and shall invoke none before the tier-0 profile amendment that `PEC-API-007` requires is effective (CLM-011); how the surface is enumerated, and whether exercising a tool in a scratch fixture is an invocation under that gate, is CON-004.
- **REQ-015** — The suite shall perform no act owned by another deliverable and shall perform no act owned by another package. In particular it shall serve no listener, token path or access-class decision (`DEL-08-01`), author no API schema and no additive-compatibility check (`DEL-08-02`), declare or package no agent tool-call query tool (`DEL-08-06`), compose no reliance-advertisement gate record (`DEL-10-13`), run no kill test and wire no kill-test gate (`DEL-10-02`), attach no citation, stamp or reliance envelope (`DEL-04-03`), and write no reconciler store or generated view (`DEL-03-01`); each is cited to its owner in CLM-016. It makes no tier-0 profile amendment (CLM-011).

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
- **AC-011** — Adoption-, ruling-, and direction-shaped probes presented under the `agent` class are not served and leave no record, as under every other class; on a state that carries the tool-call query surface, a seeded tool through which a ruling-recording operation is reachable produces a failure naming the tool and the operation; and on a state without that surface the report states that the surface was not present rather than reporting a pass.
- **AC-012** — The delivered suite performs none of the excluded acts of REQ-015: it contains no listener, token path or access-class decision, no schema authoring or compatibility check, no tool declaration or packaging, no gate record, no kill test or gate wiring, no citation, stamp or envelope attachment, no store or view write, and no tier-0 profile amendment.
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

The `agent`-class probes (REQ-013) are built with the other probes. The
tool-call surface enters the suite only once it exists and the tier-0 profile
act it requires is effective (REQ-014, CON-004); the owner-boundary inspection
(REQ-015) runs alongside the self-inspection of VER-008.

- **VER-001** — Execute the suite against a conforming API fixture and against fixtures that introduce a ruling-recording write path at (a) a schema-declared request shape and (b) a served route absent from the schema; assert a pass on the conforming fixture and, on each violating fixture, a failure naming the offending operation and its schema element or route.
- **VER-002** — Inspect the recorded operative definition against the `PEC-GAT-004` and §4.2 wording and against the enumerated permitted-write set; trace a sample of the suite's pass and fail classifications back to that recorded definition and confirm none rests on an unrecorded reading.
- **VER-003** — Enumeration audit: compare the suite's evaluated operation set against the schema's declared shapes and the listener's served operations for the same state; then add an operation to each source in turn and assert the suite reports the unevaluated addition rather than passing; then present an unresolvable schema and assert a failure rather than a partial-set pass.
- **VER-004** — Probe execution: issue adoption-, ruling-, and direction-recording requests under each access class the upstream contract obliges; assert refusal in every case, assert that no record persists after each probe, and assert a reported failure on a seeded state in which one access class is served while another is refused.
- **VER-005** — Fault injection: run the suite with an unreachable listener, an unresolvable and an unversioned schema, and an induced tooling error; assert a reported failure in every case with no pass, skip, or empty success.
- **VER-006** — Re-runnability and bindability demonstration on scratch fixtures: present the suite with a sequence of API-surface changes, at least one additional schema version, and at least one release-candidate fixture; assert an execution is produced for each presented state, that each execution is bound to the state it evaluated, and that no result is reused across states; then invoke the suite's binding interface from a scratch caller against a state the suite has not evaluated and assert it reports the missing evaluation rather than a pass, a skip, or a silent no-op. The method exercises the suite against fixtures it is given and writes no gate configuration this contract does not own.
- **VER-007** — Blocking-verdict demonstration: submit a release candidate carrying a ruling-recording write path, and one candidate with the suite withheld; assert that the mechanism returns an explicit blocking verdict in both cases. The method demonstrates the mechanism's verdict, not the release process's obligation to honour it (CON-001).
- **VER-008** — Boundary and self-inspection: compare the surface under test and the working tree before and after a full run; inspect the suite for any created, stubbed, or simulated write path and for any privileged access class it requires; and inspect its declared inputs to confirm it cites the two upstream contracts' obligations without restating, constraining, or extending them, and introduces no criterion absent from this contract.
- **VER-009** — Agent-class and tool-call probe: issue the REQ-005 probes with an `agent`-class credential and assert refusal and no persisted record; once the tier-0 profile act that `PEC-API-007` requires is effective, run the suite on a scratch fixture carrying the tool-call query surface with one seeded tool that reaches a ruling-recording operation and assert a failure naming the tool and the operation; run it on a fixture without that surface and assert that the report states the surface was not present.
- **VER-010** — Owner-boundary inspection: inspect the suite's source, configuration and declared outputs for each act excluded by REQ-015, confirm none is present, and confirm each adjacent act is cited to its owner as in CLM-016.

## Governing Values and Decisions — Axiology

- **AX-001** — `OBJ-005` governs as ruled: everything PEC holds can be deleted at any moment without blocking any governed act. The warrant recorded for this row is that "a system that captures no authority holds nothing whose deletion could block a governed act", rated LOW-MEDIUM and chosen as the least-wrong option (CON-002). This contract uses the attribution and states the warrant no more strongly than the record does.
- **AX-002** — `DL-8` twinning governs the boundary between this deliverable and the rule it verifies. `SOW-066` is the permanent `OUT` boundary record; `SOW-025` is the separate `IN` verification obligation, "never the boundary itself" (CLM-003). Nothing produced under this contract restates, narrows, widens, or substitutes for the boundary; a passing suite is evidence about an evaluated state, not a restatement of the product rule.
- **AX-003** — The standing shape of this contract is brief-directed contract design, informed by the `C-08` annotation rather than derived from an owner ruling on it (CLM-007, CON-001). It governs how the obligations above are written: treating a passing run as completion would convert a continuing verification into a one-shot artifact, which the brief's direction and the deliverable's own description ("Tested property") both refuse. It is not a claim that the verification has been ruled release-blocking; that question is CON-001, routed at AC-009.
- **AX-004** — Edge direction is a discipline, not a formality. `[E-P54]` and `[E-P55]` name this deliverable as the tester and `DEL-08-01` and `DEL-08-02` as the tested; the second is recorded from the other side in that deliverable's own contract. This contract therefore takes their obligations as its evaluated surface and absorbs none of their scope: it defines no transport, no access class, and no schema content (REQ-010, AC-008), and it imposes nothing on them.
- **AX-005** — Stratum is provenance, not authority. Both upstream edges are `PROPOSAL`, accepted "all strata as presented" at `D-PEC-62` §1(4), which that packet reads as taking the exhibit's flags as flags; neither edge carries a flag. `C-10` `STRATUM_RULE`'s own text ends "strata are provenance not authority", and this deliverable's own `_DEPENDENCIES.md` states "Blocker output is advisory visibility only — never work assignment." Edges are cited here by `EdgeID` at that status and are not converted into `DECLARED`.
- **AX-006** — `C-04` `PHASE_PRECEDENCE` is a register-wide non-gating constraint and phase hints are release-strategy ordering whose hard-versus-soft classification is a Phase 1.3 owner ruling. `DEL-10-03`, `DEL-08-01`, and `DEL-08-02` all carry `PhaseHint` `P1`, so no phase tension arises among them; this contract makes no staging claim beyond recording that fact.
- **AX-007** — `PEC-K-06` observation-not-participation governs the suite itself: "verification creates findings, never rewrites sources" is the invariant lineage `PRD.md` §6 records for it, and `PEC-RCN-004` states the same rule for the reconciler. A negative-surface test that had to create a write path in order to test for one would contradict the property it exists to verify; REQ-009 and AC-008 exist for that reason.
- **AX-008** — The accepted basis is `SOFTWARE_DECOMP.md` revision 1.6 at the pin `189f205ff`, accepted through SCA-006 at checkpoint group 3 on 2026-09-26. The prior contract's revision-1.2 pin `3623b958b` resolves to no commit, and its statement that `_REFERENCES.md` still named revision 1.1 is false at `125cfacc1`, where that file names revision 1.6; SCA-005 `Propagation_Plan.md` §B4 records both as housekeeping, and both are corrected here (AX-012).
- **AX-009** — Unknowns remain marked. TBD-001 through TBD-005 and CON-001 through CON-004 are recorded rather than resolved by inference; in particular the surface under test does not yet exist as a served surface, and its shape follows decisions that belong to the upstream deliverables and to their owner rulings, not to this contract.
- **AX-010** — This contract is lifecycle-neutral. `_STATUS.md` remains the sole lifecycle authority, is untouched by the run that authored this document, and records `INITIALIZED`; nothing here asserts that any test or registration of this suite exists, or that the tested surface exists beyond the schema canary CLM-010 records.
- **AX-011** — Operational reliance is not authority, and this deliverable verifies the authority side. PRD v2.4 lets a consumer, or an agent acting through one or through the tool-call surface, act on a record-tier claim within the envelope a response declares, and only from a PEC release that has passed the §12 reliance-advertisement gate (CLM-012). That reliance records nothing in PEC and makes no PEC output citable as authority; `PEC-K-02` and `PEC-GAT-004` hold at every release, whether or not the release advertises reliance. A passing run of this suite is evidence about an evaluated state: it is never authority, never an advertisement of operational reliance, not part of the gate record `DEL-10-13` composes, and distinct from the reliance-hold control and from professional reliance (`projects/pec/AGENTS.md`). Following the SCA-006 pass rule "No contract is rebuilt around verify-before-rely (`D-PEC-90` grant item 1).", this contract states no reliance rule of its own.
- **AX-012** — Rebuild provenance. The prior contract of this deliverable has SHA-256 `cbcabbde6882baf5330e90cdd6e1cf4a9d9aa1da076643a27f84ff4cb7696ff8` (revision-1.2 basis, pin `3623b958b`, which resolves to no commit). This contract is its currency rebuild under the S4 Scope of Work currency packet (provisional `D-PEC-102`), not yet ruled, written from the revision-1.6 basis and PRD v2.4. It carries in one pass the SCA-005 causes, housekeeping only (the unresolvable pin and the false revision-1.1 claim about `_REFERENCES.md`), and the SCA-006 cause (the `agent` access class and the agent tool-call query surface join the negative surface; CLM-013). No ID is retired. Kept IDs whose text changed, each keeping its meaning: CLM-006 (the `PKG-10` scope description now ends with the reliance-advertisement gate), CLM-007 (the `C-08` row is quoted verbatim), CLM-008 (four access classes; the current `DEP-10-03-003` cells; the sibling contract is cited by qualified ID rather than quoted), CLM-009 (a quotation brought to its source's capitalization; no acceptance claim), CLM-010 (observed lifecycles `INITIALIZED` and `CHECKING`; the schema canary exists), CON-003 (the surface is not yet served; the `agent` credentials are part of the open token decision), AX-005 (the `_DEPENDENCIES.md` sentence quoted whole), AX-008 (the revision-1.6 basis), AX-009 (CON-004 joins the marked unknowns) and AX-010 (lifecycle `INITIALIZED`). Every other ID is kept byte-for-byte. New IDs continue each prefix: CLM-011 through CLM-016, REQ-013 through REQ-015, AC-011, AC-012, VER-009, VER-010, CON-004, AX-011 and AX-012.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-025 OBJ-005 | REQ-001, REQ-011, CLM-001, CLM-002 | AC-001 | VER-001 | Fixture set with expected verdicts, suite output naming each offending operation and the schema element or route through which it is reachable |
| OUT-001 | SOW-025 OBJ-005 | REQ-002, TBD-002 | AC-002 | VER-002 | The recorded operative definition read against the PEC-GAT-004 and §4.2 wording with its permitted-write enumeration |
| OUT-001 | SOW-025 OBJ-005 | REQ-003, REQ-004, CLM-009, TBD-004, TBD-005 | AC-003 | VER-003 | Enumeration audit comparing the evaluated operation set against the obliged schema's declared shapes and the obliged listener's served operations, with reported failures for a seeded unevaluated addition and an unresolvable enumeration |
| OUT-001 | SOW-025 OBJ-005 | REQ-005, REQ-006, CLM-008 | AC-004 | VER-004 | Probe transcripts per access class showing refusal, no persisted record, and a reported failure on a seeded class-asymmetric state |
| OUT-001 | SOW-025 OBJ-005 | REQ-004, REQ-011, CON-003 | AC-005 | VER-005 | Fault-injection transcripts showing a reported failure on an unreachable listener, an unresolvable schema, an unversioned schema, and an induced tooling error, with no pass, skip, or empty success |
| OUT-001 | SOW-025 OBJ-005 | REQ-007, AX-003 | AC-006 | VER-006 | Execution records binding each presented state — API-surface changes, an additional schema version, and a release-candidate fixture — to the run that evaluated it; a scratch-caller invocation of the suite's binding interface against an unevaluated state showing the missing evaluation reported rather than passed or silently skipped |
| OUT-001 | SOW-025 OBJ-005 | REQ-008, CLM-007, CON-001 | AC-007 | VER-007 | Blocking-verdict demonstrations for a violating candidate and for a withheld check |
| OUT-001 | SOW-025 OBJ-005 | REQ-009, REQ-010, REQ-012, CLM-003, CLM-004, AX-002, AX-004, AX-007 | AC-008 | VER-008 | Before/after comparison of the surface under test and the working tree for a full run, inspection findings showing no created, stubbed, or simulated write path and no privileged access class required, and a declared-input review confirming the two upstream contracts are cited as obligations without restatement or extension |
| OUT-001 | SOW-025 OBJ-005 | REQ-013, REQ-014, CLM-011, CON-004 | AC-011 | VER-009 | Probe transcripts under the agent class showing refusal and no persisted record; once the tier-0 profile act is effective, a tool-call fixture run naming the seeded tool and the operation it reaches, and a run on a fixture without that surface reporting it not present |
| OUT-001 | SOW-025 OBJ-005 | REQ-015, CLM-012, CLM-016, AX-011 | AC-012 | VER-010 | Owner-boundary inspection record listing each act REQ-015 excludes, its absence from the suite, and its owner as cited in CLM-016 |
| OUT-001 | SOW-025 OBJ-005 | REQ-008, CLM-007, CON-001, AX-003 | AC-009 | HUMAN_REVIEW: accountable owner confirmation or declination that the verification carries release-gating authority, given C-08's "owner confirmation requested" note and D-PEC-62 §1(4)'s acceptance of the standing-node set as a recorded-but-unresolved non-gating annotation | Dated owner ruling recorded against this deliverable, stating whether a blocking verdict blocks a release candidate or is advisory, and leaving the contract's standing framing intact either way |
| OUT-001 | SOW-025 OBJ-005 | CLM-005, CLM-010, CLM-013, CLM-014, CLM-015, CON-002, AX-001, AX-012 | AC-010 | HUMAN_REVIEW: accountable owner confirmation that the LOW-MEDIUM attribution of SOW-025 to OBJ-005 stands, given the Q1.7 finding that no §3 objective states the K-AUTH-1 authority boundary, the least-wrong-selection characterization, the unadopted alternatives OBJ-003 and OBJ-006, and the C-18 withdrawal of the SOW-055 precedent | Dated owner ruling recorded against this deliverable, explicitly addressing the Q1.7 qualification rather than restating the attribution |
