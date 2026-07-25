---
doc_id: PEC-SOFTWARE-DECOMP
doc_kind: decomposition.software
package_role: working_surface
status: draft_gate5
revision: "0.7"
date: 2026-07-24
agent_persona: SOFTWARE_DECOMP
method_reference: agents/AGENT_SOFTWARE_DECOMP.md (conforms to docs/DECOMPOSITION_STANDARD.md)
session_authorization: D-PEC-60
source_corpus: projects/pec/docs/PRD.md (v2.0, adopted 2026-07-24, D-PEC-58)
---

# PEC v2 Coordination Plane — Software Development Decomposition

> **Package role: working surface.** This is the main decomposition document
> and the authoritative amendment surface for this package. Heavy
> machine-truth lives in the companion registers listed in §Companion
> Inventory once they exist (Phases 4–6). Any single-file render assembled
> from this package is a derived publication artifact.

## Gate Log

| Gate | Phase | State | Owner confirmation (verbatim) | Date |
|---|---|---|---|---|
| 1 | Intake | **CONFIRMED** | "Gate 1 confirmed — proceed to Phase 2." | 2026-07-24 |
| 2 | SSOW | **CONFIRMED** | "Gate 2 confirmed — proceed to Phase 3 based on acceptance of your recommendations for OI-010 and OI-011" | 2026-07-24 |
| 3 | Objectives | **CONFIRMED** | "Gate 3 confirmed — proceed to Phase 4." | 2026-07-24 |
| 4 | Packages | **CONFIRMED** (as restructured: PKG-00 per DL-12) | "Gate 4 confirmed — proceed to Phase 5." | 2026-07-24 |
| 5 | Deliverables | **PRESENTED** | — | 2026-07-24 |
| 6 | Coverage + Context Budget | not reached | — | — |
| 7 | Final acceptance | not reached | — | — |

---

## 1. Intake (Phase 1)

### 1.1 Project title

**PEC v2 — Chirality Coordination Plane** (greenfield build).

### 1.2 Intake summary

The work is a greenfield software build of the product defined by PRD v2.0:
a deterministic, rebuildable projection of governed file truth (**record
tier**) plus an ephemeral presence layer (**presence tier**), embodying loop
Step 0 (Discover) and the deterministic parts of Step 1 (gate review,
decision-slate presentation). It is consumed by harnesses on behalf of
agents and by the human owner through dashboards, and it must remain "the
coordination plane that doesn't need to exist": deletable at any moment
without blocking any governed act.

The scope to decompose comprises, per the PRD:

- **Reconciliation** (PEC-RCN-001..006): a one-command-rebuildable record
  tier ingesting `_STATUS.md`, decision registers/packets, receipts ledgers
  (per-loop grammar), `WORK_GRAPH.json`/`STATUS.json`/`RUNTIME_SUMMARY.json`,
  dependency registers, workplans/LOOP_INIT, and `_harness/adapter.yaml`
  manifests; incremental on Git delta; drift-classifying; never writing
  sources; permanently parity-diffable against the practitioner harness.
- **Orientation** (PEC-ORI-001..006): per-loop orientation serves and deltas
  since a caller SHA, scope-parameterized per the modes ladder, every claim
  cited, every response SHA-stamped, measurement limits stated explicitly.
- **Gate evaluation and decision slate** (PEC-GAT-001..004): deterministic,
  advisory, Explain-shaped evaluation of file/Git-reducible gate
  preconditions; a cross-loop decision slate that links to authored files
  and provides no ruling write path.
- **Presence** (PEC-PRS-001..007): harness-reported sessions, Git/worktree
  scanning (names and counts, never content), session×worktree×scope
  correlation, live parent→child hierarchy edges, TTL'd heartbeat-aged
  records, advisory-only overlap surfacing.
- **Streams and ingest** (PEC-STR-001..005): idempotent append-only event
  ingest; versioned event contracts (home is an open §16 placement
  decision); daemon SSE, hooks CLI, and optional cmux bridges; stream loss
  always recovered by reconciliation.
- **API** (PEC-API-001..005): local-only Unix-socket service, token-scoped;
  ≤100 ms p95 orientation reads; versioned additive schema; compact
  citation-bearing responses; SSE delta/presence subscription.
- **Dashboards** (PEC-DSH-001..007): overview per loop, lifecycle census,
  read-only link-only register views, the aggregated "waiting on you"
  slate, presence board, universal drill-down to cited sources,
  documented Explain-shaped pressure rules.
- **Service posture** (PEC-SVC-001..006): zero third-party runtime
  dependencies in the core; local single-owner, no egress; bounded rebuild;
  the standing kill test; gitignored store with ingest-enforced content
  minimalism; self-observable reconcile/ingest logging.
- **Validation obligations carried by the PRD** (§11–§12): the pre-P1
  Step-0 cost baseline measurement, the permanent harness parity diff, the
  standing kill test, and the P1–P4 exit tests. (P0 governance is complete
  and is not scope for this decomposition.)

**Anticipated build shape (for sizing, not yet a package proposal):** the
PRD's release strategy sequences P1 (one-loop reconciler + orientation
store + read-only API) → P2 (dashboards, five loops) → P3 (harness
integration: hooks CLI + daemon polling, presence registry, Git/worktree
scanner) → P4 (streams: SSE bridge, hooks push, live hierarchy, optional
cmux adapter). Per the method's anti-pattern rule, **phases will not become
packages**; packages will be work domains, and phase membership will be
carried as deliverable metadata/sequencing hints.

### 1.3 Hard constraints (identified at intake)

| # | Constraint | Source |
|---|---|---|
| C1 | Graceful absence: no governed act may require PEC; kill test is a standing release gate | PEC-K-01, PEC-SVC-004 |
| C2 | Files govern: record tier rebuildable by one command; store gitignored, safe to delete; output never citable as authority; rulings file-native | PEC-K-02, D-GOV-01, K-AUTH-1 |
| C3 | Harness-owned consumption; agents never call PEC by instruction | PEC-K-03 |
| C4 | Two trust tiers never blurred; presence facts never in record-tier citations | PEC-K-05, PEC-PRS-007 |
| C5 | Observation not participation: no dispatch, leases, arbitration, merge opinions; read-only over Git | PEC-K-06, D-GOV-20 |
| C6 | Content-minimal: paths, counts, SHAs, states, hashes — never file or diff content; enforced at ingest | PEC-K-10, PEC-SVC-005, D-T0-14/20 |
| C7 | Zero third-party runtime dependencies in the service core (workspace-internal contracts packages permitted) | PEC-SVC-001 (carries ADR-002) |
| C8 | Local-only, Unix socket default, token-scoped, no external egress; any loopback TCP listener is an open owner decision | PEC-API-001, PEC-SVC-002, §16.9 |
| C9 | Orientation reads ≤100 ms p95; full rebuild within a bound confirmed at P1; incremental reconcile within seconds | PEC-API-002, PEC-SVC-003 |
| C10 | Permanent parity-diff against the practitioner harness; PEC neither directs the harness nor opens its cache half | PEC-RCN-005, PRD §15 |
| C11 | Frozen reference corpus: old PEC read/cite only; machinery carries as cited patterns, never as code | PRD §7.3/§13, D-PEC-58 |
| C12 | The nine §16 open owner decisions are not resolved by this decomposition; where one materially affects architecture the affected work is fenced or flagged, never guessed | PRD §16, standing plan |
| C13 | No second execution loop; daemon owns sessions, delegation, turn locks | D-GOV-20, D-PEC-56 (surviving behaviors 4/7) |
| C14 | Every implementation tranche needs its own owner-ruled packet; this decomposition authorizes no implementation write | standing plan step 3, D-PEC-60 |
| C15 | Mode-proportional consumption: PEC contact follows the §5 modes ladder; zero-coordination modes (pipeline, unscoped conversation) remain zero-contact | PEC-K-11, §5 |

### 1.4 Intake postures (for Gate 1 confirmation)

1. **Requirement source = PRD v2.0 alone.** The 46 PEC-\*-NNN requirements,
   11 PEC-K invariants, §3 outcomes, §11 metrics/falsification clause, §5
   modes ladder, and §12 exit tests are the scope-item source. Governance
   instruments (workplan, fences, D-GOV/D-T0 rulings) enter as constraints,
   not scope; the frozen corpus enters as reference, not scope.
2. **Phases are not packages.** P1–P4 membership is deliverable metadata.
3. **§16 open decisions** enter the SSOW as `TBD` items with open issues
   attached, so their eventual rulings amend the decomposition through the
   scope-change machinery instead of being silently pre-decided.
4. **Validation work is in scope** (kill test, parity diff, Step-0 cost
   baseline, seeded-conflict tests) because the PRD binds releases to it.
5. **Vocabulary collision handled at Gate 2:** decomposition IDs (`PKG-XX`,
   `DEL-XX-YY`) will coexist in this repo with the retired product's own
   `*-PKG-*` tokens (`26020-PKG-001` demo data, `PEC-PKG-009` v0.4
   requirement IDs). The Vocabulary Map will disambiguate; prose in this
   package will say "work-domain package" where ambiguity is possible.

### 1.5 References

| Ref | Path | Role |
|---|---|---|
| R1 | `projects/pec/docs/PRD.md` (v2.0, adopted 2026-07-24, `D-PEC-58`) | Source corpus |
| R2 | `docs/DECOMPOSITION_STANDARD.md` | Ratified 7-gate protocol |
| R3 | `agents/AGENT_SOFTWARE_DECOMP.md` | Conforming method (software variant) |
| R4 | `_DomainEngines/pec/WORKPLAN_2026-07-24_pec_coordination_plane.md` | Standing plan; D1 authorization context |
| R5 | `projects/pec/AGENTS.md` | Project agent posture, fences, write scopes |
| R6 | `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-57..60` | Pivot, adoption, follow-ons, session packets |
| R7 | `tools/practitioner_harness/README.md` | Permanent parity peer |
| R8 | `projects/pec/{core,server,web,agent-sidecar,tools}` | Frozen reference corpus (cite-only) |
| R9 | Root `AGENTS.md`; `docs/SOFTWARE_WORKFLOW_PROFILE.md` | Runtime doctrine; downstream execution profile |

---

## 2. SSOW (Phase 2)

Atomic scope items normalized from PRD v2.0. `SourceRef` cites the PRD
requirement ID or section. Splits of enumerated requirements (PEC-RCN-002's
feed list; PEC-STR-003's bridge list) are recorded in the Decision Log
(DL-4, DL-5). Hard constraints C1–C15 (§1.3) bind every item and are not
repeated as scope items unless they also require built or verified behavior
(DL-7/DL-8). SOW-084..092 were appended during adversarial verification;
IDs are append-only, so family ordering is not semantic.

### 2.1 IN-scope items

| ScopeItemID | Status | ScopeItemStatement | SourceRef | Notes |
|---|---|---|---|---|
| SOW-001 | IN | Implement the record-tier entity model: Loop, Workplan/Step/Gate, Receipt, DecisionRow, Fence, Package/Deliverable, DependencyEdge, RunRecord, CandidateBrief, OrientationSnapshot, DriftFinding | §7.1 | Receipt field availability is per-loop (PEC-ORI-006 limits apply) |
| SOW-002 | IN | Implement the presence-tier entity model: Session, Worktree/GitRef, PresenceRecord, HierarchyEdge, ScopeClaim | §7.2 | Operational only; never citable (C4) |
| SOW-003 | IN | Implement token-scoped access with three access classes: owner, harness, admin | §8 | v1.0/prototype role ontologies retired |
| SOW-004 | IN | Serve per-loop orientation: newest applicable receipt, examined-through SHA, gate states, owner directions of record, open tranches/candidate briefs, parked lanes each with its unparking owner action | PEC-ORI-001 | |
| SOW-005 | IN | Serve deltas since a caller-supplied commit SHA | PEC-ORI-002 | |
| SOW-006 | IN | Stamp every orientation response with examined-through SHA, generation time, and per-feed freshness | PEC-ORI-003 | Carries PEC-K-04 |
| SOW-007 | IN | Attach a citation (file path, anchor, and/or SHA) to every claim in an orientation response | PEC-ORI-004 | |
| SOW-008 | IN | Parameterize orientation by scope (loop / project / package) per the modes ladder | PEC-ORI-005, §5 | |
| SOW-009 | IN | State measurement limitations explicitly where a feed is unparseable or stale; prohibit silent omission | PEC-ORI-006 | Coverage-honesty carry-forward |
| SOW-010 | IN | Make the record tier rebuildable in full from sources by one command; store gitignored and safe to delete; presence tier expected lost on rebuild | PEC-RCN-001 | Carries PEC-K-02/-05 |
| SOW-011 | IN | Parse `_STATUS.md` files under a declared parser dialect | PEC-RCN-002 | Feed split per DL-4 |
| SOW-012 | IN | Parse decision registers and decision packets (row identity and status only — never row prose) | PEC-RCN-002, §7.1 | Content-minimal (C6) |
| SOW-013 | IN | Parse `LOOP_RECEIPTS.md` ledgers under per-loop grammar, including the D-APP-57 contract where a ledger has adopted it | PEC-RCN-002 | Per-loop coverage limits stated (SOW-009) |
| SOW-014 | IN | Parse run-evidence JSON: `STATUS.json` and `RUNTIME_SUMMARY.json` under `execution/**` | PEC-RCN-002, §7.1 RunRecord | Daemon user-data state is presence-tier only |
| SOW-015 | IN | Parse dependency registers: `Dependencies.csv` and `WORK_GRAPH.json` | PEC-RCN-002, §7.1 DependencyEdge | `WORK_GRAPH.json` feeds DependencyEdge, not RunRecord |
| SOW-016 | IN | Parse workplans and `LOOP_INIT.md` protocol files | PEC-RCN-002 | |
| SOW-017 | IN | Consume per-project `_harness/adapter.yaml` as the feed manifest | PEC-RCN-002 | |
| SOW-018 | IN | Run reconciliation incrementally, keyed on Git delta since the last examined SHA | PEC-RCN-003 | |
| SOW-019 | IN | Classify and report drift between successive snapshots; never modify a source file | PEC-RCN-004 | |
| SOW-020 | IN | Parity-diff PEC derivations against practitioner-harness output; surface discrepancies as DriftFindings resolved against live sources | PEC-RCN-005 | Permanent (C10) |
| SOW-021 | IN | Restrict reconciler writes to its own store and generated views | PEC-RCN-006 | |
| SOW-022 | IN | Deterministically evaluate gate preconditions reducible to file/Git facts: ruling presence, ruling-SHA reachability, receipt ancestry, snapshot/freeze presence, register-row status | PEC-GAT-001 | |
| SOW-023 | IN | Shape gate verdicts as Explain objects (rule, threshold, contributing citations), advisory only | PEC-GAT-002 | Carries PEC-K-08 |
| SOW-024 | IN | Render a cross-loop decision slate: every AWAITING_RULING row and parked lane awaiting an owner act, linking to authored file content without restating it | PEC-GAT-003 | |
| SOW-025 | IN | Verify, as a tested property of the API surface, that no write path records adoption, ruling, or direction | PEC-GAT-004 | K-AUTH-1; verification obligation — the product boundary itself is SOW-066 (DL-8) |
| SOW-026 | IN | Record presence for harness-reported sessions: harness kind, engine/model attribution when known, role, loop/package binding, declared write scopes | PEC-PRS-001 | Session identity/lifecycle stay daemon-owned (C13) |
| SOW-027 | IN | Scan Git for worktrees, branches, HEAD, ahead/behind counts, and dirty path names/counts | PEC-PRS-002 | Never file or diff content (C6) |
| SOW-028 | IN | Correlate sessions to worktrees and branches (session × worktree × scope join) | PEC-PRS-003 | |
| SOW-029 | IN | Maintain live parent→child hierarchy edges from daemon and hook feeds | PEC-PRS-004 | |
| SOW-030 | IN | Carry TTLs and last-heartbeat age on presence records; never assert liveness beyond last heartbeat | PEC-PRS-005 | |
| SOW-031 | IN | Detect and surface advisory overlaps (write scopes, shared branches, same merge target) without ever blocking | PEC-PRS-006 | Carries PEC-K-06 |
| SOW-032 | IN | Exclude presence data from record-tier citations (enforced separation) | PEC-PRS-007 | Carries PEC-K-05 |
| SOW-033 | IN | Accept idempotent, append-only event ingest keyed on event id | PEC-STR-001 | |
| SOW-034 | IN | Define versioned event contract types consumable by daemon, hooks CLI, and adapters | PEC-STR-002 | Contract home is TBD (SOW-083); root `runtime/` writes out of scope (SOW-074) |
| SOW-035 | IN | Implement the runtime-daemon SSE subscriber bridge, declared and attributable | PEC-STR-003 | Bridge split per DL-5 |
| SOW-036 | IN | Implement the harness hooks CLI bridge (session start/stop, status, scope declaration), declared and attributable | PEC-STR-003 | |
| SOW-037 | IN | Implement the cmux socket adapter as an optional, declared and attributable enricher | PEC-STR-003 | Optional; P4 |
| SOW-038 | IN | Recover stream loss by reconciliation; no record-tier fact may rest on a stream event alone | PEC-STR-004 | Carries PEC-K-07 |
| SOW-039 | IN | Persist every ingested message durably and queryably; provide no ephemeral relay | PEC-STR-005 | Carries PEC-K-09 |
| SOW-040 | IN | Bind the service local-only on a Unix socket by default, token-scoped | PEC-API-001 | Loopback TCP is TBD (SOW-083) |
| SOW-041 | IN | Complete orientation reads in ≤100 ms at p95 against the current corpus | PEC-API-002 | Session-start critical path |
| SOW-042 | IN | Version the API schema; evolve additively | PEC-API-003 | |
| SOW-043 | IN | Return compact, machine-first, citation-bearing responses | PEC-API-004 | |
| SOW-044 | IN | Offer an SSE subscription for deltas and presence changes | PEC-API-005 | |
| SOW-045 | IN | Dashboard — Overview: the orientation return per loop (git state, newest receipt, gates that matter, open tranches, parked lanes + unparking act) | PEC-DSH-001 | |
| SOW-046 | IN | Dashboard — lifecycle census across registered loops' packages/deliverables with stuck-age and workflow-completeness views | PEC-DSH-002 | |
| SOW-047 | IN | Dashboard — register views (decisions, receipts, dependencies, run records): read-only, link-only, source-linked | PEC-DSH-003 | No restatement of authored text (C6) |
| SOW-048 | IN | Dashboard — "Waiting on you": the aggregated decision slate | PEC-DSH-004 | Renders SOW-024 |
| SOW-049 | IN | Dashboard — presence board: sessions × worktrees × live hierarchy with heartbeat age and advisory overlap warnings | PEC-DSH-005 | |
| SOW-050 | IN | Drill-down from every displayed value to its cited source | PEC-DSH-006 | Carries PEC-K-08 |
| SOW-051 | IN | Implement derived pressure/status rules (stuck-in-state age, gate-blocked, drift density, staleness, collision risk) as Explain-shaped, individually documented rules | PEC-DSH-007 | |
| SOW-052 | IN | Keep the service core free of third-party runtime dependencies; workspace-internal contracts packages permitted | PEC-SVC-001 | Carries ADR-002 |
| SOW-053 | IN | Operate local, single-owner, with no external network egress | PEC-SVC-002 | |
| SOW-054 | IN | Complete full rebuild within a bound confirmed at P1 (target minutes); incremental reconcile within seconds | PEC-SVC-003 | |
| SOW-055 | IN | Maintain the kill test — delete the store, run representative governed workflows, nothing blocks — as a standing, executable release gate | PEC-SVC-004, §11.6 | Carries PEC-K-01 |
| SOW-056 | IN | Keep the store at a gitignored path and enforce the content-minimal rule at ingest | PEC-SVC-005 | Carries PEC-K-10 |
| SOW-057 | IN | Log PEC's own reconcile runs and ingest activity, inspectable (self-observability) | PEC-SVC-006 | |
| SOW-058 | IN | Measure the Step-0 cost baseline (LLM tokens per loop-iteration orientation) before P1 begins; this re-tests the harness query-pain precondition recorded unmet 2026-07-02 | §11.1, §2 | Sequencing obligation, pre-P1; baselines SOW-004/041 |
| SOW-059 | IN | Provide the orientation defect-rate measurement: claims failing source spot-check per 100 claims | §11.2 | Method + any needed instrumentation; measures SOW-007 |
| SOW-060 | IN | Measure harness poll adoption: fraction of eligible session starts / mode transitions consuming orientation | §11.4, §12 P3 | Measures uptake of SOW-004; arms limb 1 of the falsification clause (limb 2: SOW-085) |
| SOW-061 | IN | Verify overlap warnings fire on seeded conflicts (P3 exit test) | §12 P3 | Tests SOW-031 |
| SOW-062 | IN | Verify presence TTL honesty under kill/crash tests (P4 exit test) | §12 P4 | Tests SOW-030 |
| SOW-063 | IN | Demonstrate stream-loss recovery by reconciliation (P4 exit test) | §12 P4 | Tests SOW-038 |
| SOW-064 | IN | Bootstrap: the first loop the P1 reconciler ingests is PEC v2's own build | §12 | First validation of the thesis; §12-internal tension resolved at Gate 2 (OI-010, DL-10) |
| SOW-084 | IN | Measure collision incidents: write-scope/branch conflicts discovered at Git time rather than surfaced in advance, per week of concurrent operation | §11.3 | Measures effectiveness of SOW-031 |
| SOW-085 | IN | Log orientation-read and dashboard-consultation activity sufficient to evaluate the §12 P2 exit test ("owner uses PEC in place of manual Step 0") and limb 2 of the §11 falsification clause | §12 P2, §11 | System-behavior observation per §11 preamble; grounded in SOW-057 self-observability |
| SOW-087 | IN | Reimplement the shared-runtime client seam concept against v2 entities | §13, D-PEC-56 | Named carry-forward: "Concept carries directly; reimplemented against v2 entities" |
| SOW-088 | IN | Author v2's first ADRs, re-citing the carried live postures ADR-002 (zero-dependency core) and ADR-014 (shared runtime agent ownership) | §13 | ADRs cited from `docs/.archive/adr/ADR.md` |
| SOW-089 | IN | Author the v2 SPEC from the accepted decomposition | §13 | "v2 SPEC is born from the decomposition" |

### 2.2 OUT-of-scope items

Rows sourced from §4.2 are **permanent non-goals**. Rows marked *Deferred*
in Notes are not permanent: they await their own instruments (a §16 ruling,
a separate packet, or a cross-loop coordination act) and are excluded from
this decomposition only.

| ScopeItemID | Status | ScopeItemStatement | SourceRef | Notes |
|---|---|---|---|---|
| SOW-065 | OUT | System-of-record function; PEC output citable as authority | §4.2 | Permanent. Files and Git remain sole authority (D-GOV-01) |
| SOW-066 | OUT | Ruling-surface function: recording adoption, ruling, or direction | §4.2 | Permanent. Verification twin: SOW-025 (DL-8) |
| SOW-067 | OUT | Orchestration: dispatch, queues, execution, session authority | §4.2 | Permanent. Daemon owns execution (C13) |
| SOW-068 | OUT | Lock management: leases, claim arbitration, merge opinions | §4.2 | Permanent. Conflicts surfaced, never prevented |
| SOW-069 | OUT | Replacing the practitioner harness; opening or directing its cache half | §4.2, §15 | Permanent. Parity peer only (C10) |
| SOW-070 | OUT | Git write actions of any kind | §4.2 | Permanent. CHANGE owns Git state; read-only plumbing only |
| SOW-071 | OUT | The human project-management lineage: declarations, attestation, plan/capacity, EPC role homes | §4.2, §14 | Permanent. Retired with v0.4/v1.0 |
| SOW-072 | OUT | Feature work on, or data migration from, the frozen v0.4 application | §13 | Permanent for this product line. Nothing to migrate; corpus is cite-only (C11) |
| SOW-073 | OUT | Capture of file or diff content in any PEC surface | PEC-K-10, §15 | Permanent. Content-minimal is load-bearing residency posture; ingest-enforcement twin: SOW-056 (DL-8) |
| SOW-074 | OUT | Writes into root `runtime/`, including placing the event contracts there | PEC-STR-002, §16.9 | **Deferred**, not permanent: outside PEC's fences; requires its own cross-loop coordination. If SOW-083 rules for the shared-contracts home, that write becomes required work under its own instrument |
| SOW-086 | OUT | The root `AGENTS.md` doctrine amendment for concurrent Agent 0 operation | §5 doctrine note | **Deferred**, not permanent: "future `AGENTS.md` amendment, not made by this PRD"; owner act on the root doctrine surface |
| SOW-090 | OUT | Supersession of the `pec.yaml` domain-engine profile (L3 lane sunset) | §13, D-PEC-59 | **Deferred**: named open follow-on once v2 has implementation shape |
| SOW-091 | OUT | Archival of the frozen source trees from the working tree | §13 | **Deferred**: its own packet once P2 is useful |
| SOW-092 | OUT | Changes to `chirality.project.json`, daemon registration, or project identity | §13 | No work: "Continue unchanged" — recorded so coverage is explicit |

### 2.3 TBD items (open owner decisions; not resolved by this decomposition)

| ScopeItemID | Status | ScopeItemStatement | SourceRef | Notes |
|---|---|---|---|---|
| SOW-075 | TBD | Whether decision registers gain light structure at source or remain prose parsed best-effort | §16.1 | Assessed (not PRD-stated): affects SOW-012 parser depth only; both paths buildable |
| SOW-076 | TBD | Design and ownership of a daemon global event feed (today: per-session SSE only) | §16.2 | Assessed (not PRD-stated): affects SOW-035 efficiency, not correctness |
| SOW-077 | TBD | Home and shape of the loop registry (which loops PEC serves; today five) | §16.3 | Assessed (not PRD-stated): P1 can proceed on a local config default |
| SOW-078 | TBD | Long-term placement: `projects/pec` vs root promotion | §16.4 | Explicitly deferred by the PRD |
| SOW-079 | TBD | Whether the web UI folds into the desktop app or remains a standalone local page | §16.5 | Assessed (not PRD-stated): affects P2 packaging, not dashboard content |
| SOW-080 | TBD | Auth reuse: PEC tokens vs the daemon's project-scoped token registry | §16.6 | Affects SOW-003 implementation choice |
| SOW-081 | TBD | Whether "PEC" is re-expanded or kept as a legacy name | §16.7 | Naming only |
| SOW-082 | TBD | Whether non-app-dev loop ledgers adopt the D-APP-57 receipt contract | §16.8 | Affects SOW-013 per-loop grammar coverage |
| SOW-083 | TBD | Event-contract home (shared runtime contracts vs PEC-local schema + pinned mirror) and API transport (Unix socket only vs additional loopback listener) | §16.9 | Fenced: PEC builds local-first either way (SOW-034/040) |

### 2.4 Domain signals (for Phase 4 partitioning; observed, not yet packages)

- **Ingest/parsing** vs **derivation/reconciliation** vs **serving/API** vs
  **rendering/dashboards** vs **integration bridges** vs **validation
  tooling** — six distinct kinds of work in the requirement families.
- Runtime surfaces: a core service (parsers, store, reconciler, evaluators),
  a socket API server, a web dashboard UI, a hooks CLI, and external-process
  bridges (daemon SSE, cmux).
- Persistence surface: one gitignored local store (technology unspecified by
  the PRD — a design choice downstream, not invented here).
- Contract surfaces: versioned event contracts and versioned API schema.
- Test surfaces: kill test, parity diff, seeded-conflict, TTL/crash, and
  measurement instrumentation are named release-gating validation work.

### 2.5 Initial objective candidates (derived; finalized at Phase 3)

From §3 outcomes and §11 metrics: sub-second cited orientation replacing
prose derivation; structural staleness detection; a declared durable
presence surface with pre-Git collision surfacing; one live owner view;
graceful-absence deletability proven continuously; measured adoption and
parity keeping the falsification clause honest.

## 3. Objectives (Phase 3)

Derived from PRD §3 (product outcomes, one objective each) and §11
(measurement/falsification posture, one objective). No objective is
invented beyond those sources. Each is testable through the mapped scope
items; the §11/§12 measurement items (SOW-058..063, 084, 085) are the
test instruments.

| ObjectiveID | Statement | SourceRef | Mapped Scope Items (best-effort) |
|---|---|---|---|
| OBJ-001 | Orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation | §3.1 | SOW-004..009, SOW-041, SOW-043; instruments: SOW-058, SOW-059 |
| OBJ-002 | Staleness is detected structurally by SHA comparison, never by judgment | §3.2 | SOW-006, SOW-018, SOW-019; supported by SOW-005 |
| OBJ-003 | Concurrent sessions have a declared, durable surface for presence and status; write-scope collisions are surfaced before they land in Git | §3.3 | SOW-002, SOW-026..032, SOW-039, SOW-049; instruments: SOW-061, SOW-084 |
| OBJ-004 | The human owner has one live view: loops, gates, lifecycle census, decisions waiting on them, and who is working where | §3.4 | SOW-024, SOW-045..051; instrument: SOW-085 |
| OBJ-005 | Everything PEC holds can be deleted at any moment without blocking any governed act | §3.5 | SOW-010, SOW-055; bound by C1/C2 across all items |
| OBJ-006 | The product thesis remains measurable and falsifiable: adoption, parity, defect, and collision metrics are gathered in system behavior and the §11 falsification clause stays armed | §11 | SOW-020, SOW-057..060, SOW-084, SOW-085 |

**Mapping notes:** no unmapped objectives. Ingest/bridge items
(SOW-033..039) serve OBJ-001/OBJ-003 freshness indirectly through
PEC-K-07 and are intentionally not force-mapped; parser items
(SOW-011..017) underlie OBJ-001/OBJ-002 through the record tier
(SOW-001). Deferred/OUT and TBD items map to no objective by design.
Full ScopeItem→Objective assignments land in `ScopeLedger.csv` at
Phase 4–5; this table is the objective-side view.

## 4. Packages (Phase 4)

Eleven flat work-domain packages (PKG-00..PKG-10). Each is a cohesive
context set grounded in the §2.4 domain signals; none is a phase (DL-3 —
PKG-00 is an architecture/contract *authoring domain*, not a "design
phase": its artifacts are consumed as declared dependencies by other
packages' deliverables, never written into them). Every IN scope item is
assigned to exactly one package in `ScopeLedger.csv` (the authoritative
companion register for assignments); forced boundary decisions are DL-11;
the PKG-00 restructuring at Gate 4 is DL-12. OUT and TBD items carry no
package.

| PackageID | Name | Scope Description (work domain) | Assigned (count) | Exclusions |
|---|---|---|---|---|
| PKG-00 | Architecture Runway & Contracts | Published specifications others consume: v2's first ADRs (incl. the OI-012 core-isolation decision), the v2 SPEC born from this decomposition, and the versioned event-contract types shared by daemon, hooks CLI, and adapters | SOW-034, 088, 089 (3) | Implementation of any contract (consuming packages); cross-package edits — PKG-00 publishes, dependants consume |
| PKG-01 | Service Core & Store | The zero-dependency service foundation: record- and presence-tier entity schemas, the gitignored store with ingest-boundary content-minimal enforcement, locality/no-egress posture, self-observability logging | SOW-001, 002, 052, 053, 056, 057 (6) | Parsing, derivation, serving — other packages |
| PKG-02 | File-Truth Parsers | Read-side grammars over governed files: `_STATUS.md` dialect, decision registers/packets, receipts ledgers, run-evidence JSON, dependency registers, workplans/LOOP_INIT, `adapter.yaml` manifests | SOW-011..017 (7) | Writing anything; interpretation beyond declared grammars |
| PKG-03 | Reconciliation & Parity | The guaranteed path from file truth to record tier: one-command rebuild, incremental Git-delta reconcile, drift classification, harness parity diffing, stream-loss recovery guarantee, store-only writes, rebuild performance bounds | SOW-010, 018, 019, 020, 021, 038, 054 (7) | Stream ingest mechanics (PKG-07); parsers (PKG-02) |
| PKG-04 | Orientation Services | Derivation and serving of orientation: per-loop returns, deltas since SHA, SHA/freshness stamping, per-claim citations, scope parameterization, explicit measurement limits | SOW-004..009 (6) | Transport (PKG-08); rendering (PKG-09) |
| PKG-05 | Gate Evaluation & Decision Slate | Deterministic advisory evaluation of file/Git-reducible gate preconditions; Explain-shaped verdicts; the cross-loop decision slate | SOW-022, 023, 024 (3) | Any ruling write path (SOW-066, permanent OUT) |
| PKG-06 | Presence & Git Observation | The presence tier's producers: harness-reported session records, Git/worktree scanning, session×worktree×scope correlation, hierarchy edges, TTL/heartbeat discipline, advisory overlap detection, citation-exclusion enforcement | SOW-026..032 (7) | Session lifecycle ownership (daemon's, C13) |
| PKG-07 | Event Ingest & Bridges | Best-effort freshness inputs: idempotent append-only event ingest, the daemon SSE / hooks CLI / cmux bridges, durable message store, the shared-runtime client seam — implementing the PKG-00 event contracts | SOW-033, 035..037, 039, 087 (6) | Record-tier fact creation (PKG-03 guarantee); contract definition (PKG-00); root `runtime/` writes (SOW-074, deferred) |
| PKG-08 | API & Access | The machine-consumer surface: Unix-socket binding, token-scoped access classes, p95 latency, versioned additive schema, compact citation-bearing responses, SSE subscription | SOW-003, 040..044 (6) | Dashboard rendering (PKG-09) |
| PKG-09 | Dashboards | The human-owner surface: overview, lifecycle census, register views, decision slate view, presence board, universal drill-down, documented pressure rules | SOW-045..051 (7) | New data classes; restating authored text (C6) |
| PKG-10 | Validation & Measurement | Release-gating proof and metrics: kill test, no-ruling-write verification, Step-0 baseline, defect/adoption/collision measurement, seeded-conflict, TTL-honesty and stream-loss tests, usage observability, bootstrap self-ingest | SOW-025, 055, 058..064, 084, 085 (11) | The behaviors under test (their home packages) |

## 5. Deliverables (Phase 5)

61 deliverables across the 11 packages. **`Deliverables.csv` is the
authoritative companion register** (full fields: description, responsible
party, anticipated artifacts, envelope notes); the tables below are the
compact control view. `PhaseHint` is sequencing metadata per DL-3, never a
package. ResponsibleParty is `TBD` throughout — assignment happens at
WORKING_ITEMS activation, not here. Conventions are DL-13.

Context Envelope posture: **25 S / 35 M / 1 L / 0 XL.** The single L
(DEL-02-03, receipts parser) carries mandatory envelope notes; no XL
exists, so no Gate 5/6 acceptance-of-risk is required.

### PKG-00 Architecture Runway & Contracts

| ID | Name | Type | Env | Phase | Covers |
|---|---|---|---|---|---|
| DEL-00-01 | v2 first ADRs (core isolation + carried postures) | DOC_UPDATE | S | pre-P1 | SOW-088 |
| DEL-00-02 | Event-contract schema v1 | API_CONTRACT | M | P3 | SOW-034 |
| DEL-00-03 | v2 SPEC seed | DOC_UPDATE | M | P1 | SOW-089 |

### PKG-01 Service Core & Store

| ID | Name | Type | Env | Phase | Covers |
|---|---|---|---|---|---|
| DEL-01-01 | Record-tier schema & entity model | DATA_MODEL_CHANGE | M | P1 | SOW-001 |
| DEL-01-02 | Presence-tier schema & entity model | DATA_MODEL_CHANGE | S | P3 | SOW-002 |
| DEL-01-03 | Store bootstrap & content-minimal guard | BACKEND_FEATURE_SLICE | M | P1 | SOW-056 |
| DEL-01-04 | Self-observability logging | OBSERVABILITY | S | P1 | SOW-057 |
| DEL-01-05 | Zero-dependency & locality enforcement | CI_CD_CHANGE | S | P1 | SOW-052, 053 |

### PKG-02 File-Truth Parsers

| ID | Name | Type | Env | Phase | Covers |
|---|---|---|---|---|---|
| DEL-02-01 | `_STATUS.md` parser | BACKEND_FEATURE_SLICE | M | P1 | SOW-011 |
| DEL-02-02 | Decision register/packet parser | BACKEND_FEATURE_SLICE | M | P1 | SOW-012 |
| DEL-02-03 | Receipts ledger parser (per-loop grammars) | BACKEND_FEATURE_SLICE | **L** | P1 | SOW-013 |
| DEL-02-04 | Run-evidence JSON parser | BACKEND_FEATURE_SLICE | S | P1 | SOW-014 |
| DEL-02-05 | Dependency register parser | BACKEND_FEATURE_SLICE | S | P1 | SOW-015 |
| DEL-02-06 | Workplan/LOOP_INIT parser | BACKEND_FEATURE_SLICE | M | P1 | SOW-016 |
| DEL-02-07 | `adapter.yaml` feed-manifest consumer | BACKEND_FEATURE_SLICE | S | P1 | SOW-017 |

### PKG-03 Reconciliation & Parity

| ID | Name | Type | Env | Phase | Covers |
|---|---|---|---|---|---|
| DEL-03-01 | Full-rebuild reconciler (one command) | BACKEND_FEATURE_SLICE | M | P1 | SOW-010, 021 |
| DEL-03-02 | Incremental reconcile on Git delta | BACKEND_FEATURE_SLICE | M | P1 | SOW-018 |
| DEL-03-03 | Drift classification | BACKEND_FEATURE_SLICE | M | P1 | SOW-019 |
| DEL-03-04 | Practitioner-harness parity diff | BACKEND_FEATURE_SLICE | M | P1 | SOW-020 |
| DEL-03-05 | Stream-loss recovery guarantee | BACKEND_FEATURE_SLICE | S | P4 | SOW-038 |
| DEL-03-06 | Rebuild performance bounds | TEST_SUITE | S | P1 | SOW-054 |

### PKG-04 Orientation Services

| ID | Name | Type | Env | Phase | Covers |
|---|---|---|---|---|---|
| DEL-04-01 | Loop orientation return | BACKEND_FEATURE_SLICE | M | P1 | SOW-004 |
| DEL-04-02 | Delta service since SHA | BACKEND_FEATURE_SLICE | M | P1 | SOW-005 |
| DEL-04-03 | Citation & freshness stamping | BACKEND_FEATURE_SLICE | M | P1 | SOW-006, 007 |
| DEL-04-04 | Scope parameterization | BACKEND_FEATURE_SLICE | S | P2 | SOW-008 |
| DEL-04-05 | Measurement-limitation honesty | BACKEND_FEATURE_SLICE | S | P1 | SOW-009 |

### PKG-05 Gate Evaluation & Decision Slate

| ID | Name | Type | Env | Phase | Covers |
|---|---|---|---|---|---|
| DEL-05-01 | Gate precondition evaluators (Explain-shaped) | BACKEND_FEATURE_SLICE | M | P2 | SOW-022, 023 |
| DEL-05-02 | Cross-loop decision slate | BACKEND_FEATURE_SLICE | M | P2 | SOW-024 |

### PKG-06 Presence & Git Observation

| ID | Name | Type | Env | Phase | Covers |
|---|---|---|---|---|---|
| DEL-06-01 | Session presence records | BACKEND_FEATURE_SLICE | M | P3 | SOW-026 |
| DEL-06-02 | Git/worktree scanner | BACKEND_FEATURE_SLICE | M | P3 | SOW-027 |
| DEL-06-03 | Session×worktree×scope correlation | BACKEND_FEATURE_SLICE | S | P3 | SOW-028 |
| DEL-06-04 | Live hierarchy edges | BACKEND_FEATURE_SLICE | S | P4 | SOW-029 |
| DEL-06-05 | TTL/heartbeat discipline & citation exclusion | BACKEND_FEATURE_SLICE | M | P3 | SOW-030, 032 |
| DEL-06-06 | Advisory overlap detection | BACKEND_FEATURE_SLICE | M | P3 | SOW-031 |

### PKG-07 Event Ingest & Bridges

| ID | Name | Type | Env | Phase | Covers |
|---|---|---|---|---|---|
| DEL-07-01 | Idempotent event ingest + durable message store | BACKEND_FEATURE_SLICE | M | P3 | SOW-033, 039 |
| DEL-07-02 | Daemon SSE subscriber bridge | BACKEND_FEATURE_SLICE | M | P4 | SOW-035 |
| DEL-07-03 | Hooks CLI bridge | BACKEND_FEATURE_SLICE | M | P3 | SOW-036 |
| DEL-07-04 | cmux socket adapter (optional) | BACKEND_FEATURE_SLICE | M | P4 | SOW-037 |
| DEL-07-05 | Shared-runtime client seam (v2) | BACKEND_FEATURE_SLICE | M | P3 | SOW-087 |

### PKG-08 API & Access

| ID | Name | Type | Env | Phase | Covers |
|---|---|---|---|---|---|
| DEL-08-01 | Unix-socket server + token-scoped access | SECURITY_CONTROL | M | P1 | SOW-003, 040 |
| DEL-08-02 | Versioned additive API schema | API_CONTRACT | S | P1 | SOW-042 |
| DEL-08-03 | Compact citation-bearing response format | API_CONTRACT | S | P1 | SOW-043 |
| DEL-08-04 | Orientation latency budget (p95 ≤ 100 ms) | TEST_SUITE | S | P1 | SOW-041 |
| DEL-08-05 | SSE delta/presence subscription | BACKEND_FEATURE_SLICE | M | P4 | SOW-044 |

### PKG-09 Dashboards

| ID | Name | Type | Env | Phase | Covers |
|---|---|---|---|---|---|
| DEL-09-01 | Overview dashboard | UX_UI_SLICE | M | P2 | SOW-045 |
| DEL-09-02 | Lifecycle census dashboard | UX_UI_SLICE | M | P2 | SOW-046 |
| DEL-09-03 | Register views | UX_UI_SLICE | M | P2 | SOW-047 |
| DEL-09-04 | Decision-slate view ("waiting on you") | UX_UI_SLICE | S | P2 | SOW-048 |
| DEL-09-05 | Presence board | UX_UI_SLICE | M | P3 | SOW-049 |
| DEL-09-06 | Universal drill-down to cited source | UX_UI_SLICE | M | P2 | SOW-050 |
| DEL-09-07 | Explain-shaped pressure rules | UX_UI_SLICE | M | P2 | SOW-051 |

### PKG-10 Validation & Measurement

| ID | Name | Type | Env | Phase | Covers |
|---|---|---|---|---|---|
| DEL-10-01 | Step-0 cost baseline (pre-P1) | MEASUREMENT | S | pre-P1 | SOW-058 |
| DEL-10-02 | Kill test (standing release gate) | TEST_SUITE | M | P1 | SOW-055 |
| DEL-10-03 | No-ruling-write verification | TEST_SUITE | S | P1 | SOW-025 |
| DEL-10-04 | Orientation defect-rate spot-check | MEASUREMENT | S | P2 | SOW-059 |
| DEL-10-05 | Usage metrics (poll adoption + owner consultation) | MEASUREMENT | M | P2–P3 | SOW-060, 085 |
| DEL-10-06 | Seeded-conflict overlap test | TEST_SUITE | S | P3 | SOW-061 |
| DEL-10-07 | Presence TTL honesty tests | TEST_SUITE | S | P4 | SOW-062 |
| DEL-10-08 | Stream-loss recovery demonstration | TEST_SUITE | S | P4 | SOW-063 |
| DEL-10-09 | Collision-incident measurement | MEASUREMENT | S | P3 | SOW-084 |
| DEL-10-10 | Bootstrap self-ingest validation | TEST_SUITE | S | P1 | SOW-064 |

## 6. Scope Ledger — not started (will be authoritative in `ScopeLedger.csv`)

## 7. Coverage & Telemetry (Phase 6) — not started

## 8. Context Budget QA — not started (will be authoritative in `ContextBudgetQA.csv`)

## 9. Vocabulary Map (seeded at Phase 2)

| CanonicalTerm | Synonyms | Notes |
|---|---|---|
| coordination plane | PEC v2 | The product; never "project-management tool" |
| record tier | reconciled tier, projection | Rebuilt from file truth; per-claim citations; the only citable-with-sources tier (and even then never as authority) |
| presence tier | — | TTL'd, heartbeat-aged, evaporating; never citable |
| store | database | Gitignored, safe to delete; "database" avoided in prose where it suggests authority |
| orientation | Step-0 return | The per-loop/scope serve of PEC-ORI-001..006 |
| OrientationSnapshot | — | Record-tier entity (§7.1): a generated orientation return stamped with examined SHA — the machine generalization of a receipt. Distinct from the general term "orientation" |
| reconciler | rebuild | The guaranteed path from file truth to record tier (PEC-K-07) |
| ingest | stream ingest, event ingest | Best-effort (PEC-K-07); deliberately **not** a synonym of reconciliation, which is guaranteed |
| Explain-shaped | explainable derivation | Rule ID + threshold + contributing cited sources; from the prototype's `Explain<V>` pattern (cited, not copied) |
| graceful absence | kill test, deletability | PEC-K-01; the kill test is its executable form |
| decision slate | "waiting on you" | Aggregated AWAITING_RULING rows + parked lanes; link-only |
| gate verdict | gate evaluation, precondition check | Deterministic, advisory, never dispositive |
| loop | work loop, domain-engine loop | Tenancy unit above Project (root, app-dev, piping, pec, bridge) |
| harness | practitioner harness / runtime daemon / hooks CLI | Disambiguate: "practitioner harness" = the parity-peer CLI checker; "harness" unqualified = any machine consumer polling on behalf of agents |
| examined-through SHA | examined SHA, freshness SHA | The staleness comparator (PEC-K-04) |
| DriftFinding | drift, parity discrepancy | Classified difference between snapshots or vs harness output |
| heartbeat age | last-heartbeat, TTL age | Liveness is never asserted beyond it (PEC-PRS-005) |
| scope claim | write-scope declaration, "working here" | Advisory only; overlap-detection input |
| work-domain package | PKG-XX, decomposition package | **Disambiguation:** distinct from the retired product's `*-PKG-*` tokens (`26020-PKG-001` demo/fixture work-package IDs; `PEC-PKG-009` **v0.4** requirement IDs — the v1.0 PRD used no `PEC-PKG` family). In this package, bare "package" means work-domain package |
| frozen reference corpus | old PEC, v0.4 baseline, prototype | Read/cite only; machinery carries as pattern, never code |
| content-minimal | residency rule, no-content rule | Paths, counts, SHAs, states, hashes — never file/diff content |
| MEASUREMENT (deliverable type) | metric deliverable | Added to the suggestive software taxonomy for §11 metric work (DL-13): a deliverable whose artifact is a measurement method, instrumentation, and report — not a feature or test of behavior |

## 10. Open Issues

| ID | Refs | Issue | Owner action that closes it |
|---|---|---|---|
| OI-001 | SOW-075 | §16.1 register structuring at source undecided | §16 ruling |
| OI-002 | SOW-076 | §16.2 daemon global event feed undecided | §16 ruling (cross-loop) |
| OI-003 | SOW-077 | §16.3 loop-registry home/shape undecided | §16 ruling |
| OI-004 | SOW-078 | §16.4 long-term placement deferred | §16 ruling |
| OI-005 | SOW-079 | §16.5 UI packaging undecided | §16 ruling |
| OI-006 | SOW-080 | §16.6 auth reuse undecided | §16 ruling |
| OI-007 | SOW-081 | §16.7 name re-expansion undecided | §16 ruling |
| OI-008 | SOW-082 | §16.8 receipt-contract adoption by non-app-dev ledgers undecided | §16 ruling (per-loop) |
| OI-009 | SOW-083 | §16.9 event-contract home and API transport undecided | §16 ruling |
| OI-010 | SOW-064 | **RESOLVED at Gate 2 (2026-07-24):** the §12 closing paragraph governs — the first loop the P1 reconciler ingests is PEC v2's own build (bootstrap as thesis validation); the P1 table's "(piping or root)" parenthetical does not constrain the first-loop choice. Owner accepted the recommended reading in the Gate 2 confirmation (DL-10) | Closed |
| OI-011 | C3, C15 | **RESOLVED at Gate 2 (2026-07-24):** session start is a polling moment only when the session starts with scope (e.g., an Agent 0 loop session); unscoped sessions poll at the conversation→workbench transition. Owner accepted the recommended reading in the Gate 2 confirmation (DL-10) | Closed |
| OI-012 | SOW-088, PKG-00 | Core isolation style — ports-and-adapters (hexagonal) vs functional-core/imperative-shell — is undecided; the PRD's invariants (PEC-K-02/-07, PEC-SVC-001) force the isolation properties either way. To be decided in v2's first ADRs with the Gate 4 exchange as recorded basis | ADR in PKG-00 (downstream); owner review at that ADR |

## 11. Decision Log

| # | Date | Decision | Rationale |
|---|---|---|---|
| DL-1 | 2026-07-24 | Package layout: main surface + co-located CSV companion registers + `Companion_Inventory.csv` + `_LATEST.md`, all inside `execution/_Decomposition/` | Matches `docs/DECOMPOSITION_STANDARD.md` package architecture and the review skill's read boundary; avoids the piping split (`docs/_Registers/`) and the app-dev monolith |
| DL-2 | 2026-07-24 | Main doc filename is bare `SOFTWARE_DECOMP.md`; revision lives in front matter | The app-dev versioned filename caused ~40 downstream path references to a mutable name |
| DL-3 | 2026-07-24 | Release phases P1–P4 are recorded as deliverable metadata, never as packages | `AGENT_SOFTWARE_DECOMP.md` anti-pattern: packages are work domains, not phases |
| DL-4 | 2026-07-24 | PEC-RCN-002's enumerated feed list is split into seven scope items (SOW-011..017), one per feed kind | Each feed is a separately testable parser with its own grammar; a single "ingest everything" item is not atomic |
| DL-5 | 2026-07-24 | PEC-STR-003's three bridges are split into SOW-035..037 | Independently buildable integrations with different peers and optionality |
| DL-6 | 2026-07-24 | §11 measurements and §12 exit tests enter as IN scope items (SOW-058..063, SOW-084, SOW-085) distinct from the behaviors they test; each Notes cell cross-links its behavior item | The PRD makes them release-gating work; test/measurement artifacts are deliverables downstream |
| DL-7 | 2026-07-24 | PEC-K invariants and governance rulings are carried as constraints (C1–C15), not scope items, except where they require built or verified behavior (e.g., SOW-025, SOW-055, SOW-056) | Avoids double-counting cross-cutting constraints in coverage arithmetic while keeping buildable obligations countable |
| DL-8 | 2026-07-24 | IN/OUT twinning convention: a §4.2 boundary row stays OUT as the boundary record; the corresponding built/verified obligation is a separate IN item stating enforcement or verification, never the boundary itself. Pairs: SOW-025↔SOW-066, SOW-056↔SOW-073. Phase 6 telemetry counts rows as written; twins are distinct statements, not duplicates | Keeps "scope item = unit of coverage checking" coherent while satisfying both the boundary record and the buildable-obligation record |
| DL-9 | 2026-07-24 | Adversarial verification (opus-5, 16 confirmed defects) appended SOW-084..092, C15, OI-001..011, and the §9/§2 corrections; IDs are append-only and family ordering is not semantic (I5) | Notable: §11.3 and §12-P2 obligations had been dropped; PEC-K-11 unrepresented; `PEC-PKG-009` provenance was v0.4, not v1.0; `WORK_GRAPH.json` was routed to the wrong entity; two PRD-internal tensions surfaced as OI-010/011 rather than silently reconciled |
| DL-10 | 2026-07-24 | Owner resolved OI-010 (first P1 loop = PEC v2's own build; §12 closing paragraph governs over the P1 table parenthetical) and OI-011 (session-start polling applies only to sessions that start with scope) at Gate 2 | Gate 2 confirmation verbatim in the Gate Log: "…based on acceptance of your recommendations for OI-010 and OI-011" |
| DL-13 | 2026-07-24 | Phase 5 conventions: (a) a `MEASUREMENT` deliverable type is added to the software taxonomy for §11 metric work (the base taxonomy is declared suggestive; recorded here and in the Vocabulary Map); (b) `PhaseHint` carries P1–P4 sequencing as metadata per DL-3; (c) ResponsibleParty is `TBD` pending WORKING_ITEMS activation; (d) two-item merges kept single-shape: DEL-03-01 (rebuild+write-restriction), DEL-04-03 (citations+stamps), DEL-05-01 (evaluators+Explain verdicts), DEL-06-05 (TTL+citation exclusion), DEL-07-01 (ingest+durable store), DEL-08-01 (socket+tokens), DEL-01-05 (zero-dep+locality), DEL-10-05 (two usage metrics arming both falsification limbs); (e) `Deliverables.csv` and the ledger's SOW→DEL column are generated from one source of deliverable definitions with asserted single-package coverage and ID coupling | Keeps deliverables agent-executable and the registers drift-free |
| DL-12 | 2026-07-24 | Gate 4 restructuring on owner direction ("what about adding a PKG-00 addressing the nuances of the architecture…"): PKG-00 Architecture Runway & Contracts created (precedent: piping's PKG-00 Software Architecture Runway); PKG-11 dissolved into it pre-confirmation (Gate 4 was still open, so no post-acceptance renumbering under I5); SOW-034 reassigned PKG-07→PKG-00 as a published cross-consumer contract. Mechanics constraint: PKG-00 deliverables publish artifacts that dependants consume as declared dependencies — a deliverable never writes into another package (disjoint write scopes preserved). OI-012 (core isolation style) recorded for PKG-00's ADR deliverable | The owner's "contributions to other packages" intent is realized through dependency edges, not cross-package writes |
| DL-11 | 2026-07-24 | Phase 4 forced boundary assignments: SOW-010 (one-command rebuild) → PKG-03 as the reconciler entry point, while the store-path rule (SOW-056) stays PKG-01; SOW-038 (stream-loss recovery) → PKG-03 because the guarantee is reconciliation-side, not ingest mechanics; SOW-025 (no-ruling-write verification) → PKG-10 per DL-8's verification-obligation framing; SOW-087 (client seam) → PKG-07 as daemon-facing integration; SOW-003 (access classes) → PKG-08 with the token-scoped transport; SOW-054 (rebuild bounds) → PKG-03 as reconcile performance; SOW-064 (bootstrap) → PKG-10 as a validation act, not a reconciler feature | Each was assignable to two domains; ledger rows carry `DL-11` in DecisionRef. The `ScopeLedger.csv` register is generated from this document's SSOW tables by script to prevent transcription drift |

## Companion Inventory

| Filename | PackageRole | Status | Description |
|---|---|---|---|
| `SOFTWARE_DECOMP.md` | working surface | live (this file) | Main decomposition document; amendment surface |
| `_LATEST.md` | snapshot / handoff artifact | live | Revision pointer; kept current on every revision bump |
| `ScopeLedger.csv` | authoritative companion register | **live** (SOW→DEL mapping filled at Phase 5) | SOW→PKG→DEL→OBJ row-level ledger; authoritative for assignments |
| `Deliverables.csv` | authoritative companion register | **live** (Phase 5) | Deliverable register: full fields incl. descriptions, artifacts, Context Envelope + notes, PhaseHint |
| `ContextBudgetQA.csv` | authoritative companion register | planned (Phase 6) | Per-deliverable envelope/risk/action QA |
| `Companion_Inventory.csv` | authoritative companion register | planned (Phase 7) | Machine-readable mirror of this table at publication |
