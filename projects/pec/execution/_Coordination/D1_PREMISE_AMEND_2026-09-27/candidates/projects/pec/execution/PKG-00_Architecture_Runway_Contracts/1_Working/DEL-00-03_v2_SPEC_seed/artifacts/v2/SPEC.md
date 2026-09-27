# PEC v2 coordination plane — specification seed

**Authority status:** PEC v2 specification seed. Artifact-fitness and lifecycle
dispositions are recorded separately on the governed REVIEW, owner-ruling, and
`_STATUS.md` surfaces; this file does not enact those acts.

**Born from:** `projects/pec/docs/PRD.md` v2.2 and the accepted
`projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.3 at
commit `11a494e9a`, accepted through SCA-003.

**Premise amendment:** premises that SCA-005 and SCA-006 made false are
brought current to `projects/pec/docs/PRD.md` v2.4 and decomposition
revision 1.6 (`current_basis`, accepted at `189f205ff`), under an
owner-ruled exact-byte packet of work-graph node D1
(`HELP-HUMAN-PEC-20260925-POST-SCA005`). The owner-accepted bytes this
amends (SHA-256
`cc9f4754ac3d8ab0901fb6099d469c4e8e4557507dd50683ec9389977b0f1bae`) remain
history; nothing else is revised, and no acceptance of these bytes is
recorded here.

**Deliverable:** DEL-00-03; **scope item:** SOW-089; **recorded objective:**
OBJ-001, with the accepted SCA-002 LOW-confidence qualification retained.

## 1. Authority, purpose, and limits

This is the pre-P1 seed of the PEC v2 product specification. It derives its
structure from the accepted objectives, work-domain packages, deliverables,
scope items, and PRD v2.4 requirement identifiers (`SOW-089`, `DEL-00-03`). It
specifies the coordination-plane product; it does not assert that any PEC v2
capability is implemented or accepted (`PKG-00`; `DEL-00-03` REQ-001,
REQ-002, and REQ-012).

The requirement source is PRD v2.4: 49 `PEC-*-NNN` requirements, 11 `PEC-K-*`
invariants, product outcomes, the modes ladder, metrics/falsification posture,
and phase exits. Governance instruments constrain delivery but are not
additional product scope (`SOFTWARE_DECOMP.md` §1.4; `SOW-089`).

Every normative identifier below refers to the accepted PRD or decomposition.
No identifier from the retired v1.0 or v0.4 product is used as a live v2
identifier (`PRD.md` §14).

## 2. Product boundary and invariant set

PEC v2 is a deterministic, rebuildable projection of governed file truth plus
an operational presence tier. It serves Step-0 orientation and deterministic
Step-1 gate-review/decision-slate information to explicitly enabled consumers.
It remains optional, non-authoritative, and deletable without blocking a
governed act (`PEC-K-01`, `PEC-K-02`, `PEC-K-03`; OBJ-001, OBJ-005).

The complete invariant set governing the seed is:

| ID | Seed interpretation |
|---|---|
| PEC-K-01 | Graceful absence; the kill test remains a release gate. |
| PEC-K-02 | Files govern; PEC stores and views are rebuildable/non-authoritative. |
| PEC-K-03 | Pull-oriented interface; an enabled consumer owns use. Operational reliance applies only within the pin, coverage and trust tier a response declares (PEC-ORI-007) and only from a release that has passed the §12 reliance-advertisement gate; it is never authority (PEC-K-02), and files are the fallback wherever PEC is absent, degraded, failing its own checks or stating a limitation. |
| PEC-K-04 | Staleness is established through SHA/freshness comparison. |
| PEC-K-05 | Record and presence trust tiers never blur. |
| PEC-K-06 | PEC observes and explains; it does not dispatch, arbitrate, lease, or block. |
| PEC-K-07 | Event ingest improves freshness; file reconciliation establishes record-tier facts. |
| PEC-K-08 | Every derivation remains explainable and source-cited. |
| PEC-K-09 | Coordination messages PEC holds are durable and attributable. |
| PEC-K-10 | PEC stores paths, counts, SHAs, states, and hashes—never file or diff content. |
| PEC-K-11 | PEC is mode-capable and never forces contact or an external cadence. |

PEC is therefore not a system of record, ruling surface, orchestrator, lock
manager, replacement for the practitioner harness, or human project-management
tool (`PRD.md` §4.2; `SOW-065`..`SOW-069`).

## 3. Product capabilities

The following table carries the full 49-requirement catalogue by accepted PRD
family. The PRD rows are the normative requirement text; this seed groups them
without replacing them.

| Family | IDs | Specified capability | Accepted scope |
|---|---|---|---|
| Orientation | PEC-ORI-001..007 | Per-loop orientation, deltas, SHA/freshness stamps, per-claim citations, scope parameters, explicit limitations, and the reliance envelope | SOW-004..009, SOW-097 |
| Reconciliation | PEC-RCN-001..006 | One-command rebuild, governed-file parsers, Git-delta reconcile, drift classification, harness parity, and store/generated-view-only writes | SOW-010..021, SOW-095, SOW-096 |
| Gate/slate | PEC-GAT-001..004 | File/Git-reducible advisory gate evaluation, Explain-shaped verdicts, decision-slate rendering, and no ruling write path | SOW-022..025 |
| Presence | PEC-PRS-001..007 | Harness-reported sessions, Git/worktree observation, correlation (live hierarchy deferred behind trigger T-RT), TTL honesty, advisory overlap, and citation exclusion | SOW-026..032 (SOW-029 OUT, deferred) |
| Streams | PEC-STR-001..005 | Idempotent durable ingest, versioned event contracts, the hooks CLI bridge (the only remaining bridge; the Runtime SSE bridge is deferred behind trigger T-RT and the cmux adapter is deferred), and reconciliation recovery from stream loss | SOW-033..039 (SOW-035, SOW-037 OUT, deferred) |
| API | PEC-API-001..007 | Local token-scoped service, ≤100 ms p95 orientation, additive schema, compact cited responses, SSE subscription, response-size budgets, and a read-only agent tool-call query surface | SOW-003, SOW-040..044, SOW-098, SOW-099 |
| Dashboards | PEC-DSH-001..007 | Overview, lifecycle census, source-linked registers/slate, presence board, drill-down, and Explain-shaped pressure rules | SOW-045..051 |
| Service | PEC-SVC-001..006 | Dependency-free core, local/no-egress posture, bounded reconcile, kill test, gitignored content-minimal store, and self-observability | SOW-052..057 |

Measurement and release proof remain separate work: Step-0 cost, defect rate,
consumer uptake, collision incidents, parity, kill/no-ruling-write checks,
seeded conflict, TTL honesty, stream-loss recovery, directed bootstrap
evidence, and the §12 standing reliance-advertisement gate (`SOW-025`,
`SOW-055`, `SOW-058`..`SOW-064`, `SOW-084`, `SOW-085`, `SOW-093`,
`SOW-100`).

## 4. Information model

The record tier models Loop, Workplan/Step/Gate (a declared historical-grammar
entity), Receipt, DecisionRow, Fence, Package (entity)/Deliverable (entity),
DependencyEdge, RunRecord, CandidateBrief, OrientationSnapshot, DriftFinding,
and WorkGraph/WorkNode from governed sources
(`SOW-001`; PEC-RCN-002). The presence tier models Session, Worktree/GitRef,
PresenceRecord, HierarchyEdge, and ScopeClaim as TTL'd operational data that is
never record-tier citable (`SOW-002`; PEC-K-05).

`Package (entity)` above means another loop's modeled lifecycle unit. It is
distinct from a **work-domain package**, the `PKG-XX` decomposition unit used
below, and from retired `*-PKG-*` product tokens (`SOFTWARE_DECOMP.md` §9).

## 5. Accepted objectives

| ID | Accepted objective |
|---|---|
| OBJ-001 | Orientation is a sub-second, per-claim-cited query rather than a session-length derivation. |
| OBJ-002 | Staleness is detected structurally by SHA comparison. |
| OBJ-003 | Presence/status has a declared durable surface and collisions are surfaced before Git. |
| OBJ-004 | The owner has a live view of loops, gates, lifecycle, decisions, and active work. |
| OBJ-005 | Everything PEC holds can be deleted without blocking governed work. |
| OBJ-006 | The thesis remains measurable and falsifiable in observed use and system behavior. |

The `DEL-00-03` attribution to OBJ-001 remains the accepted LOW-confidence,
single-objective attribution. This seed does not strengthen it or substitute
the considered full-objective-set or OBJ-006 alternatives (`DEL-00-03`
ScopeOfWork AX-002 and AC-011).

## 6. Work-domain package and deliverable structure

All 11 accepted work-domain packages and all 68 deliverable rows (64 active;
four retired under SCA-005) are represented below. The concise ID lists are
deliberate: detailed names, types, envelopes, phase hints, and scope mappings
remain normative in `Deliverables.csv` and `SOFTWARE_DECOMP.md` §5.

| Work-domain package | Role | Deliverables |
|---|---|---|
| PKG-00 Architecture Runway & Contracts | Publish ADR, SPEC, and event contracts; no consuming implementation | DEL-00-01..03 |
| PKG-01 Service Core & Store | Entity schemas, disposable store, locality, observability, loop configuration | DEL-01-01..06 |
| PKG-02 File-Truth Parsers | Governed-file grammar adapters; no source writes | DEL-02-01..09 |
| PKG-03 Reconciliation & Parity | Rebuild, incremental reconcile, drift, parity, recovery, performance | DEL-03-01..06 |
| PKG-04 Orientation Services | Orientation derivation, deltas, citations/freshness, scope, limitations, and the reliance envelope | DEL-04-01..05 |
| PKG-05 Gate Evaluation & Decision Slate | Advisory gate evaluation and owner slate; no ruling path | DEL-05-01..02 |
| PKG-06 Presence & Git Observation | Presence, worktree observation, TTL, overlap; live hierarchy deferred (trigger T-RT) | DEL-06-01..06 (DEL-06-04 retired) |
| PKG-07 Event Ingest & Bridges | Durable ingest and the hooks CLI bridge, the only remaining bridge; the Runtime SSE bridge and the runtime-client seam are deferred (trigger T-RT) and the cmux adapter is deferred | DEL-07-01..05 (DEL-07-02, DEL-07-04, DEL-07-05 retired) |
| PKG-08 API & Access | Local access, additive schemas, cited responses, latency, subscription, response-size budgets, agent tool-call query surface | DEL-08-01..06 |
| PKG-09 Dashboards | Source-linked owner views and Explain-shaped pressure rules | DEL-09-01..07 |
| PKG-10 Validation & Measurement | Release proof and metrics; not the behaviors under test | DEL-10-01..13 |

The accepted scope ledger contains 100 items: 74 IN, 18 OUT, and 8 TBD. This
seed does not reproduce all row prose because `ScopeLedger.csv` is the
authoritative register; the package/deliverable and capability structures
above are a complete structural index into it (`SOFTWARE_DECOMP.md` §7).

## 7. Operating and release model

PEC supports Pipeline, Conversation, Workbench, Agent-0-single,
Agent-1-concurrent, and Agent-0-concurrent modes. These are PEC-side
capabilities, not a contact duty; explicitly enabled consumers own mapping and
cadence (`PEC-K-03`, `PEC-K-11`; PRD.md §5).

Delivery follows P0 governance, D1 decomposition, P1 one-loop reconciliation
and read API, P2 dashboards, P3 optional integration interfaces, the agent
tool-call query surface and presence/Git observation, and P4 streams, with the
live hierarchy tier and the Runtime SSE bridge deferred behind trigger T-RT
and the cmux adapter deferred. P1 first ingests PEC v2's own
accepted dependency graph; later nodes consume only capabilities accepted from
predecessors, and file-native fallback remains operable (`SOW-064`; PRD.md
§12). This seed is pre-P1 and asserts no phase completion.

## 8. Open decisions and deliberate non-resolution

The accepted basis retains OI-001, OI-002, and OI-004..009 for register
structure, global event feed, long-term placement, UI packaging, auth reuse,
name, receipt contract, and contract-home/API-transport choices, with the
premises of OI-002, OI-006 and OI-008 re-expressed under SCA-005: no daemon
exists and no non-owning observation interface is documented (OI-002), the
open OI-006 choice is the PEC-local token mechanism because reuse of an App
token registry is foreclosed (under SCA-006 it also covers credentials for
the `agent` access class), and OI-008 remains open for the Root, Runtime and
Bridge ledgers. OI-003
(loop-registry home) is resolved by D-PEC-78 O-A and SCA-004. OI-013 retains
the register-validator follow-on in the accepted decomposition record
(`SOFTWARE_DECOMP.md` §10).

This SPEC does not decide OI-012. Its selected architecture is recorded on the
separate DEL-00-01 ADR surface under D-PEC-72; no open-issue register or
decomposition update is performed by this seed. The eight `TBD` scope rows
remain TBD, and C-06's unnamed SPEC consumers remain unresolved. This seed
names no consuming deliverable and creates no consumer edge (`DEL-00-03`
CON-001, REQ-007, REQ-010).

## 9. Historical material

The prior `docs/.archive/SPEC.md`, `TRACEABILITY.md`, `PILOT.md`, and
`adr/ADR.md` are historical evidence only. The frozen v0.4 application is
read/cite-only reference material. No archived document or identifier becomes
live authority through this seed (`PRD.md` §§13–14; `SOW-088`, `SOW-089`).

## 10. Governed amendment provision

This SPEC was seeded before P1 from accepted decomposition revision 1.3. It is
amended per phase only through governed updates. Between those updates it
acquires no new scope, requirement, invariant, objective, work-domain package,
deliverable, consumer obligation, implementation state, acceptance state, or
release claim (`DEL-00-03` REQ-006, REQ-012).

This document does not itself make the seed the accepted v2 SPEC of record,
advance its `_STATUS.md`, or close C-05. REVIEW records validation against its
contract mappings, and a separate owner ruling records whether the seed and
the retained LOW-confidence OBJ-001 attribution are accepted (`DEL-00-03`
AC-011). No such disposition may be inferred from this surface.
