---
doc_id: PEC-SOFTWARE-DECOMP
doc_kind: decomposition.software
package_role: working_surface
status: candidate_pending_checkpoint_3
revision: "1.6"
date: 2026-09-26
accepted: not yet accepted — revision 1.6 applied during SCA-006 checkpoint-3 preparation; revision 1.5 (accepted 2026-09-25) remains the accepted basis until the owner's checkpoint-3 acceptance
agent_persona: SOFTWARE_DECOMP
method_reference: agents/AGENT_SOFTWARE_DECOMP.md (conforms to docs/DECOMPOSITION_STANDARD.md)
session_authorization: D-PEC-60; amended by SCA-001 under D-PEC-61, by SCA-002 under D-PEC-64, by SCA-003 under the owner's 2026-07-28 standing completion approval, by SCA-004 under D-PEC-78 and the owner's 2026-08-03 Gate 5 post-change confirmation, by SCA-005 under D-PEC-86 and the owner's SCA-005 checkpoint acceptances, then by SCA-006 under D-PEC-90 R-A and the owner's SCA-006 checkpoint acceptances
source_corpus: projects/pec/docs/PRD.md (v2.4; v2.0 adopted by D-PEC-58, directed-bootstrap clarification adopted by D-PEC-61, exact PEC-K-03/-11 rows adopted by D-PEC-67, surrounding consumer-interface concordance adopted by D-PEC-68, v2.3 successor accepted through SCA-005 carrying the D-PEC-79 §16.3 loop-registry concordance with the SCA-005 feed-model and Runtime-topology concordance, the v2.4 successor accepted through SCA-006 carrying the D-PEC-90 operational-reliance direction)
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
| 5 | Deliverables | **CONFIRMED** | "Gate 5 confirmed — proceed to Phase 6." | 2026-07-24 |
| 6 | Coverage + Context Budget | **CONFIRMED** | "Gate 6 confirmed — proceed to Phase 7." | 2026-07-24 |
| 7 | Final acceptance | **ACCEPTED** | "I rule that this decomposition is now the accepted basis for downstream work." | 2026-07-24 |

---

## 1. Intake (Phase 1)

### 1.1 Project title

**PEC v2 — Chirality Coordination Plane** (greenfield build).

### 1.2 Intake summary

The work is a greenfield software build of the product defined by PRD v2.4:
a deterministic, rebuildable projection of governed file truth (**record
tier**) plus an ephemeral presence layer (**presence tier**), embodying loop
Step 0 (Discover) and the deterministic parts of Step 1 (gate review,
decision-slate presentation). It is available to explicitly PEC-enabled
consumers, including harnesses acting on behalf of agents and agents
querying directly through tool calls, and to the human owner through
dashboards. It must remain "the coordination plane that doesn't need to
exist": deletable at any moment without blocking any governed act.

The scope to decompose comprises, per the PRD:

- **Reconciliation** (PEC-RCN-001..006): a one-command-rebuildable record
  tier ingesting, as each loop's closed feed profile in the PEC-owned
  registry declares, `_STATUS.md`, decision registers/packets, receipts
  (per-loop `LOOP_RECEIPTS.md` ledgers and central
  `AgentRuns/<RunID>/RECEIPT.md`), Markdown work graphs
  (`WorkGraphs/<undertaking>/WORK_GRAPH.md`), the MEMORY run index,
  dependency registers, and `LOOP_INIT.md` loop identity; JSON run evidence
  (`WORK_GRAPH.json`/`STATUS.json`/`RUNTIME_SUMMARY.json`) and workplans are
  read under declared historical grammars, and `_harness/adapter.yaml` only
  as a parity-peer input; incremental on Git delta; drift-classifying; never
  writing sources; permanently parity-diffable against the practitioner
  harness.
- **Orientation** (PEC-ORI-001..007): per-loop orientation serves and deltas
  since a caller SHA, scope-parameterized per the modes ladder, every claim
  cited, every response SHA-stamped, measurement limits stated explicitly,
  and every response declaring its reliance envelope (pin, coverage, trust
  tier, file-fallback signal).
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
  decision); the hooks CLI bridge, with the daemon SSE and cmux bridges
  deferred; stream loss always recovered by reconciliation.
- **API** (PEC-API-001..007): local-only Unix-socket service, token-scoped;
  ≤100 ms p95 orientation reads; versioned additive schema; compact
  citation-bearing responses; SSE delta/presence subscription; declared
  response-size budgets met by pagination or continuation, with stated
  truncation; a read-only query interface for agent tool calls under the
  `agent` access class.
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
  standing kill test, the P1–P4 exit tests, the standing
  reliance-advertisement gate for any release that advertises
  operational reliance, and directed full-DAG self-bootstrap validation
  for PEC's own build. (P0 governance is complete and is not scope for
  this decomposition.)

**Anticipated build shape (for sizing, not yet a package proposal):** the
PRD's release strategy sequences P1 (one-loop reconciler + orientation
store + read-only API for PEC's own build graph) → P2 (dashboards, the
loops the registry lists, owner-use/non-use observation) → P3 (opt-in
PEC-side consumer interfaces/adapters, the agent tool-call query surface,
presence registry, Git/worktree scanner) → P4 (PEC-side streams and
optional hook-push interfaces). Live P3/P4 use requires separate
receiving-consumer authority. Per the method's anti-pattern rule, **phases
will not become packages**; packages will be work domains, and phase
membership will be carried as deliverable metadata/sequencing hints.

### 1.3 Hard constraints (identified at intake)

| # | Constraint | Source |
|---|---|---|
| C1 | Graceful absence: no governed act may require PEC; kill test is a standing release gate | PEC-K-01, PEC-SVC-004 |
| C2 | Files govern: record tier rebuildable by one command; store gitignored, safe to delete; output never citable as authority; rulings file-native | PEC-K-02, D-GOV-01, K-AUTH-1 |
| C3 | Pull-oriented, consumer-owned use: PEC serves labeled, non-authoritative orientation on request (non-authoritative in the authority sense: never citable as authority); it never self-polls, schedules a consumer, injects into an agent, or claims an external cadence; an explicitly enabled consumer decides whether and when to consume and any injection is optional; a consumer may act on a record-tier claim within the pin, coverage and tier the response declares, with file fallback (operational reliance, PEC-ORI-007), only from a release that has passed the §12 reliance-advertisement gate | PEC-K-03, D-PEC-67, D-PEC-68, D-PEC-90 |
| C4 | Two trust tiers never blurred; presence facts never in record-tier citations | PEC-K-05, PEC-PRS-007 |
| C5 | Observation not participation: no dispatch, leases, arbitration, merge opinions; read-only over Git | PEC-K-06, D-GOV-43 A2 |
| C6 | Content-minimal: paths, counts, SHAs, states, hashes — never file or diff content; enforced at ingest | PEC-K-10, PEC-SVC-005, D-T0-14/20 |
| C7 | Zero third-party runtime dependencies in the service core (workspace-internal contracts packages permitted) | PEC-SVC-001 (carries ADR-002) |
| C8 | Local-only, Unix socket default, token-scoped, no external egress; any loopback TCP listener is an open owner decision | PEC-API-001, PEC-SVC-002, §16.9 |
| C9 | Orientation reads ≤100 ms p95; full rebuild within a bound confirmed at P1; incremental reconcile within seconds | PEC-API-002, PEC-SVC-003 |
| C10 | Permanent parity-diff against the practitioner harness; PEC neither directs the harness nor opens its cache half | PEC-RCN-005, PRD §15 |
| C11 | Frozen reference corpus: old PEC read/cite only; machinery carries as cited patterns, never as code | PRD §7.3/§13, D-PEC-58 |
| C12 | The nine §16 open owner decisions are not resolved by this decomposition; where one materially affects architecture the affected work is fenced or flagged, never guessed | PRD §16, standing plan |
| C13 | No second execution loop; sessions, delegation and turn admission are owned per application by its application-owned Runtime service (one private Runtime per application; D-GOV-43 A2), which supersedes D-GOV-20 items 2–4 on that path | D-GOV-43 A2, D-PEC-56 (surviving behaviors 4/7) |
| C14 | Every implementation tranche needs its own owner-ruled packet; this decomposition authorizes no implementation write | standing plan step 3, D-PEC-60 |
| C15 | Mode-capable and never forced: PEC supports the §5 scope and mode parameters; an explicitly enabled consumer owns its mode mapping and contact cadence unless separately ruled, while pipeline and unscoped-conversation modes remain testably zero-contact | PEC-K-11, §5, D-PEC-67, D-PEC-68 |
| C16 | Directed self-bootstrap for PEC's own build: `PROJECT_SETUP` materializes the accepted decomposition as `FULL_GRAPH`; later nodes consume only PEC capabilities produced and accepted by predecessor nodes; no node depends on the capability it creates; observed friction routes to evidence-linked candidates and human gates; the file-native fallback remains operable | PRD v2.2 §12, D-PEC-61, D-PEC-68 |

### 1.4 Intake postures (for Gate 1 confirmation)

1. **Requirement source = PRD v2.2 alone.** The 46 PEC-\*-NNN requirements,
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
| R1 | `projects/pec/docs/PRD.md` (v2.4; lineage ruled through `D-PEC-58`, `D-PEC-61`, `D-PEC-67`, and `D-PEC-68`, with the `D-PEC-79` §16.3 concordance carried into the v2.3 successor accepted through SCA-005 and the `D-PEC-90` operational-reliance direction carried into the v2.4 successor accepted through SCA-006) | Source corpus |
| R2 | `docs/DECOMPOSITION_STANDARD.md` | Ratified 7-gate protocol |
| R3 | `agents/AGENT_SOFTWARE_DECOMP.md` | Conforming method (software variant) |
| R4 | `projects/pec/plans/workplans/WORKPLAN_2026-07-24_pec_coordination_plane.md` | Retired history (D-PEC-80 D): the former standing plan; D1 authorization context |
| R5 | `projects/pec/AGENTS.md` | Project agent posture, fences, write scopes |
| R6 | `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-57..68`, `D-PEC-90` | Pivot, adoption, decomposition, directed bootstrap, exact consumer rows, v2.2 concordance, and operational reliance on PEC data (`D-PEC-90` R-A) |
| R7 | `tools/practitioner_harness/README.md` | Permanent parity peer |
| R8 | `projects/pec/{core,server,web,agent-sidecar,tools}` | Frozen reference corpus (cite-only) |
| R9 | Root `AGENTS.md`; `docs/SOFTWARE_WORKFLOW_PROFILE.md` | Runtime doctrine; downstream execution profile |

---

## 2. SSOW (Phase 2)

Atomic scope items normalized from PRD v2.2. `SourceRef` cites the PRD
requirement ID or section. Splits of enumerated requirements (PEC-RCN-002's
feed list; PEC-STR-003's bridge list) are recorded in the Decision Log
(DL-4, DL-5). Hard constraints C1–C16 (§1.3) bind every item and are not
repeated as scope items unless they also require built or verified behavior
(DL-7/DL-8). SOW-084..092 were appended during the Phase 2 adversarial
verification and SOW-093..094 during the Phase 6 verification (DL-14);
SOW-095..096 were appended under SCA-005 from the PRD v2.3 feed list
(DL-20), and SOW-097..100 under SCA-006 from PRD v2.4 (DL-21). IDs are
append-only, so family ordering is not semantic.

### 2.1 IN-scope items

| ScopeItemID | Status | ScopeItemStatement | SourceRef | Notes |
|---|---|---|---|---|
| SOW-001 | IN | Implement the record-tier entity model: Loop, Workplan/Step/Gate (declared historical-grammar entity; gate state re-sourced from decision registers, scope-change pointers and graph BLOCKED nodes), Receipt (ledger entries and central `RECEIPT.md`), DecisionRow, Fence, Package/Deliverable, DependencyEdge, RunRecord (from central receipts, work graphs and the MEMORY run index; JSON run evidence historical), CandidateBrief, OrientationSnapshot, DriftFinding, WorkGraph/WorkNode | §7.1 | Receipt field availability is per-loop (PEC-ORI-006 limits apply); "remaining items" is a per-loop optional field, not a required one |
| SOW-002 | IN | Implement the presence-tier entity model: Session, Worktree/GitRef, PresenceRecord, HierarchyEdge, ScopeClaim | §7.2 | Operational only; never citable (C4) |
| SOW-003 | IN | Implement token-scoped access with four access classes: owner, harness, agent (read-only query for tool calls), admin | §8 | v1.0/prototype role ontologies retired |
| SOW-004 | IN | Serve per-loop orientation: newest applicable receipt over central receipts and ledgers, examined-through SHA, gate states from decisions, scope-change state and graph BLOCKED nodes, owner directions of record, open tranches/candidate briefs and parked lanes over graph READY/ACTIVE/BLOCKED nodes, each parked lane with its unparking owner action; terminal completion derived from local Git merge reachability of cited PRs, Explain-cited and advisory | PEC-ORI-001 | |
| SOW-005 | IN | Serve deltas since a caller-supplied commit SHA | PEC-ORI-002 | |
| SOW-006 | IN | Stamp every orientation response with examined-through SHA, generation time, and per-feed freshness | PEC-ORI-003 | Carries PEC-K-04 |
| SOW-007 | IN | Attach a citation (file path, anchor, and/or SHA) to every claim in an orientation response | PEC-ORI-004 | |
| SOW-008 | IN | Parameterize orientation by scope (loop / project / package) per the modes ladder | PEC-ORI-005, §5 | |
| SOW-009 | IN | State measurement limitations explicitly where a feed is unparseable or stale; prohibit silent omission | PEC-ORI-006 | Coverage-honesty carry-forward |
| SOW-010 | IN | Make the record tier rebuildable in full from sources by one command; store gitignored and safe to delete; presence tier expected lost on rebuild | PEC-RCN-001 | Carries PEC-K-02/-05 |
| SOW-011 | IN | Parse `_STATUS.md` files under a declared parser dialect | PEC-RCN-002 | Feed split per DL-4 |
| SOW-012 | IN | Parse decision registers and decision packets (row identity and status only — never row prose) | PEC-RCN-002, §7.1 | Content-minimal (C6) |
| SOW-013 | IN | Parse receipts as two grammar generations of one Receipt feed kind: `LOOP_RECEIPTS.md` ledgers under per-loop grammar (live for PEC/Root/Runtime/Bridge; declared historical for App/Piping), including the receipt-contract-v2 marker where a ledger carries it, and central `execution/_Coordination/AgentRuns/<RunID>/RECEIPT.md` receipts | PEC-RCN-002 | Per-loop coverage limits stated (SOW-009); central receipts stay in this item (DL-4 unchanged) |
| SOW-014 | IN | Parse run-evidence JSON: `STATUS.json` and `RUNTIME_SUMMARY.json` under `execution/**`, as a declared historical grammar for App/Piping and current-by-own-practice for PEC/Root | PEC-RCN-002, §7.1 RunRecord | Application-owned Runtime service user-data is operational, never an input (D-GOV-43 A2; D-GOV-20 item 5) |
| SOW-015 | IN | Parse dependency registers: `Dependencies.csv`, and `WORK_GRAPH.json` as a declared historical grammar for App/Piping | PEC-RCN-002, §7.1 DependencyEdge | `WORK_GRAPH.json` feeds DependencyEdge, not RunRecord; Markdown work-graph dependencies arrive through SOW-095 |
| SOW-016 | IN | Parse `LOOP_INIT.md` for loop identity, entrypoint and procedure SHA only, and workplans as a declared historical grammar; no step/gate state is read from `LOOP_INIT.md` | PEC-RCN-002 | |
| SOW-017 | IN | Read per-project `_harness/adapter.yaml` as a parity-peer input only, comparing PEC's declared census population with the harness `status_glob`; report divergence as a DriftFinding | PEC-RCN-002 | No longer the feed manifest: per-loop feed profiles in the PEC-owned registry declare the feeds (SOW-077, SOW-094) |
| SOW-018 | IN | Run reconciliation incrementally, keyed on Git delta since the last examined SHA | PEC-RCN-003 | |
| SOW-019 | IN | Classify and report drift between successive snapshots; never modify a source file | PEC-RCN-004 | |
| SOW-020 | IN | Parity-diff PEC derivations against practitioner-harness output; surface discrepancies as DriftFindings resolved against live sources | PEC-RCN-005 | Permanent (C10) |
| SOW-021 | IN | Restrict reconciler writes to its own store and generated views | PEC-RCN-006 | |
| SOW-022 | IN | Deterministically evaluate gate preconditions reducible to file/Git facts: ruling presence, ruling-SHA reachability, receipt ancestry, snapshot/freeze presence, register-row status | PEC-GAT-001 | |
| SOW-023 | IN | Shape gate verdicts as Explain objects (rule, threshold, contributing citations), advisory only | PEC-GAT-002 | Carries PEC-K-08 |
| SOW-024 | IN | Render a cross-loop decision slate: every AWAITING_RULING row and parked lane awaiting an owner act, linking to authored file content without restating it | PEC-GAT-003 | |
| SOW-025 | IN | Verify, as a tested property of the API surface, that no write path records adoption, ruling, or direction | PEC-GAT-004 | K-AUTH-1; verification obligation — the product boundary itself is SOW-066 (DL-8) |
| SOW-026 | IN | Record presence for harness-reported sessions: harness kind, engine/model attribution when known, role, loop/package binding, declared write scopes | PEC-PRS-001 | Session identity/lifecycle are Runtime-owned per application (C13); sessions enter PEC only from an explicitly authorized hooks consumer |
| SOW-027 | IN | Scan Git for worktrees, branches, HEAD, ahead/behind counts, and dirty path names/counts | PEC-PRS-002 | Never file or diff content (C6) |
| SOW-028 | IN | Correlate sessions to worktrees and branches (session × worktree × scope join) | PEC-PRS-003 | |
| SOW-030 | IN | Carry TTLs and last-heartbeat age on presence records; never assert liveness beyond last heartbeat | PEC-PRS-005 | |
| SOW-031 | IN | Detect and surface advisory overlaps (write scopes, shared branches, same merge target) without ever blocking | PEC-PRS-006 | Carries PEC-K-06 |
| SOW-032 | IN | Exclude presence data from record-tier citations (enforced separation) | PEC-PRS-007 | Carries PEC-K-05 |
| SOW-033 | IN | Accept idempotent, append-only event ingest keyed on event id | PEC-STR-001 | |
| SOW-034 | IN | Define versioned event contract types consumable by the hooks CLI bridge | PEC-STR-002 | The hooks CLI is the only remaining bridge (SOW-035 and SOW-037 deferred). Contract home is TBD (SOW-083); the shared option path is `projects/chirality-runtime/packages/contracts` (Runtime loop; root `runtime/` relocated, PR #727), and writes there are out of scope (SOW-074). OBJ-003 by the owner's TM-PEC-023 row-1 selection |
| SOW-036 | IN | Implement the harness hooks CLI bridge (session start/stop, status, scope declaration), declared and attributable | PEC-STR-003 | |
| SOW-038 | IN | Recover stream loss by reconciliation; no record-tier fact may rest on a stream event alone | PEC-STR-004 | Carries PEC-K-07 |
| SOW-039 | IN | Persist every ingested message durably and queryably; provide no ephemeral relay | PEC-STR-005 | Carries PEC-K-09 |
| SOW-040 | IN | Bind the service local-only on a Unix socket by default, token-scoped | PEC-API-001 | Loopback TCP is TBD (SOW-083) |
| SOW-041 | IN | Complete orientation reads in ≤100 ms at p95 against the current corpus | PEC-API-002 | Latency-sensitive pull path; any session-start use requires separately adopted consumer authority |
| SOW-042 | IN | Version the API schema; evolve additively | PEC-API-003 | |
| SOW-043 | IN | Return compact, machine-first, citation-bearing responses | PEC-API-004 | |
| SOW-044 | IN | Offer an SSE subscription for deltas and presence changes | PEC-API-005 | |
| SOW-045 | IN | Dashboard — Overview: the orientation return per loop (git state, newest receipt, gates that matter, open tranches, parked lanes + unparking act) | PEC-DSH-001 | |
| SOW-046 | IN | Dashboard — lifecycle census across registered loops' packages/deliverables with stuck-age and workflow-completeness views | PEC-DSH-002 | |
| SOW-047 | IN | Dashboard — register views (decisions, receipts, dependencies, run records): read-only, link-only, source-linked | PEC-DSH-003 | No restatement of authored text (C6) |
| SOW-048 | IN | Dashboard — "Waiting on you": the aggregated decision slate | PEC-DSH-004 | Renders SOW-024 |
| SOW-049 | IN | Dashboard — presence board: sessions (when hook-reported) × worktrees × graph-declared activity, with heartbeat/scan age and advisory overlap warnings | PEC-DSH-005 | Live hierarchy deferred with SOW-029; declared activity is record tier, never presence tier or liveness |
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
| SOW-060 | IN | Measure consumer uptake: candidate-consumer enablement (registered loops, harnesses and enabled agent tool-call surfaces) and, among enabled consumers, orientation use against contact opportunities defined by their own adopted mode/cadence rules | §11.4, §12 P3 | Measures uptake of SOW-004; no receiving-loop conformance criterion; supports the §11 falsification clause together with SOW-085 |
| SOW-061 | IN | Verify overlap warnings fire on seeded conflicts (P3 exit test) | §12 P3 | Tests SOW-031 |
| SOW-062 | IN | Verify presence TTL honesty under kill/crash tests (P4 exit test) | §12 P4 | Tests SOW-030 |
| SOW-063 | IN | Demonstrate stream-loss recovery by reconciliation (P4 exit test) | §12 P4 | Tests SOW-038 |
| SOW-064 | IN | Directed bootstrap: P1 first ingests PEC v2's accepted full dependency DAG as its initial file-native coordination state; later DAG nodes consume only PEC capabilities already produced and accepted by predecessors, while observed coordination friction is captured as evidence for candidate functions and boundary or amendment decisions | PRD v2.2 §12, D-PEC-61, D-PEC-68 | Introduced in P1 and standing thereafter; observations grant no authority or scope, the file-native fallback remains operable, and generality is validated against a structurally different loop (extends OI-010; DL-10, DL-11, SCA-001) |
| SOW-077 | IN | Maintain the PEC-owned long-term service registry naming the loop locators PEC serves through the strict, versioned JSON/schema paths and core-owned typed LoopRegistry port, each row declaring a closed, PEC-versioned feed profile (profile ID, version, live/historical, basis citation to the loop's own record) | §16.3, D-PEC-78 | D-PEC-78 O-A: PEC owns only its configured service set; each listed loop remains authoritative for its own entrypoint and truth; later row changes are owner-gated PEC configuration changes; no governed act depends on PEC or the registry. A feed profile is PEC's reading hypothesis, never the loop's truth; feed-profile declarations need a strict schema v2 plus a `RegisteredLoop` port field through a later D-PEC source packet (no `v2/**` write here), within D-PEC-78 O-A (version 1 remains strict; supplementary extension, no supersession) |
| SOW-084 | IN | Measure collision incidents: write-scope/branch conflicts discovered at Git time rather than surfaced in advance, per week of concurrent operation | §11.3 | Measures effectiveness of SOW-031 |
| SOW-085 | IN | Log owner use or non-use of PEC orientation and dashboard surfaces sufficient to evaluate the §12 P2-B uptake observation and the §11 falsification clause | §12 P2, §11 | Manual Step 0 remains available; neither use nor non-use creates a governed PEC read/write duty; grounded in SOW-057 self-observability |
| SOW-088 | IN | Author v2's first ADRs: decide core isolation (OI-012); re-cite ADR-002 as a live carried posture; cite ADR-014 as historical lineage only while carrying forward the accepted v2 runtime/client and human-only-act boundary | §13; D-PEC-67 L-A2 | OI-012 rides this item; the archived ADR-014 PEC-project-adapter allocation is not re-adopted |
| SOW-089 | IN | Author the v2 SPEC from the accepted decomposition | §13 | "v2 SPEC is born from the decomposition" |
| SOW-093 | IN | Report parity DriftFindings per reconcile as the §11 parity metric | §11.5 | Measures the output of SOW-020 (DL-14); the behavior is PKG-03, the metric is PKG-10 |
| SOW-094 | IN | Maintain the loop-registration configuration naming the loops PEC serves and each row's feed-profile selection (local config default) | §12 P2, PEC-DSH-002 | Local JSON configuration is the implementation basis for the long-term PEC-owned service registry confirmed by D-PEC-78; the core port keeps filesystem and JSON details replaceable. PEC's own `pec` row declares the `remaining-loop` profile now; its later migration is one owner-gated row change under its own ruling (D-PEC-86 I-7) |
| SOW-095 | IN | Parse `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md` content-minimally (declared run-identity token, node IDs, closed-vocabulary node states, DEL bindings, PR numbers, hex SHAs, linked paths, per-state counts), discovered per the loop's declared feed profile; read the integration ref by default, with local branch refs opt-in and labelled unintegrated; resolve cited PR numbers to local merge commits by read-only plumbing, reporting unresolved-locally and never guessing | PEC-RCN-002 (PRD v2.3), §7.1 WorkGraph/WorkNode | New feed kind under SCA-005 (DL-4, DL-20); node states are declared activity, never liveness; objectives per the DL-17 parser precedent |
| SOW-096 | IN | Parse deliverable `MEMORY.md` run-index entries (run-ID tokens, dates, link targets) in the template `## Runs` table, the observed bullet form and the dated-heading form, as RunRecord join evidence | PEC-RCN-002 (PRD v2.3), §7.1 RunRecord | New feed kind under SCA-005 (DL-4, DL-20); absence is a stated coverage limit (SOW-009); objectives per the DL-17 parser precedent |
| SOW-097 | IN | Declare the reliance envelope on every orientation response: pin (examined-through SHA), per-feed coverage and freshness with stated limitations, per-claim trust tier, and the file-fallback signal | PEC-ORI-007 | New under SCA-006 (D-PEC-90 R-A; ENV-a); distinct from SOW-006 stamping; an input to the reliance-advertisement gate (SOW-100) |
| SOW-098 | IN | Bound responses by declared size budgets met by pagination or continuation; state any truncation; never drop citations, stamps or stated limitations | PEC-API-006 | New under SCA-006 (D-PEC-91 carry-forward; BUD-a); numeric budgets confirmed at P1; distinct from the latency budget (SOW-041) |
| SOW-099 | IN | Offer a read-only query interface for agent tool calls over the versioned API under the agent access class; enabling it is consumer-owned | PEC-API-007, §8 | New under SCA-006 (D-PEC-90 owner answer; DQ-a); token mechanism OI-006; tier-0 profile amendment before any tool is declared or invoked; P3 |
| SOW-100 | IN | Maintain the reliance-advertisement gate: before any release advertises operational reliance, prove harness parity clean or explained, complete coverage statements under seeded feed failures, the reliance envelope on every response, passing parser fixture suites and the kill test | §12, PEC-RCN-005, PEC-ORI-006, PEC-ORI-007 | Instrument (DL-6): distinct from the behaviours it tests (SOW-020, SOW-009, SOW-097, SOW-055); re-proved at each release that advertises operational reliance; the §12 P1 row is not edited (GATE-a) |

### 2.2 OUT-of-scope items

Rows sourced from §4.2 are **permanent non-goals**. Rows marked *Deferred*
in Notes are not permanent: they await their own instruments (a §16 ruling,
a separate packet, a cross-loop coordination act, trigger T-RT, or a later
owner direction) and are excluded from this decomposition only. SOW-029,
SOW-035, SOW-037 and SOW-087 moved here from §2.1 under SCA-005 (DL-20).

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
| SOW-074 | OUT | Writes into the Runtime loop's `projects/chirality-runtime/**` (root `runtime/` relocated, PR #727), including placing the event contracts there | PEC-STR-002, §16.9 | **Deferred**, not permanent: outside PEC's fences; requires its own cross-loop coordination. If SOW-083 rules for the shared-contracts home (`projects/chirality-runtime/packages/contracts`), that write becomes required work under its own instrument |
| SOW-086 | OUT | The root `AGENTS.md` doctrine amendment for concurrent Agent 0 operation | §5 doctrine note | **Deferred**, not permanent: "future `AGENTS.md` amendment, not made by this PRD"; owner act on the root doctrine surface |
| SOW-090 | OUT | Supersession of the `pec.yaml` domain-engine profile (L3 lane sunset) | §13, D-PEC-59 | **Deferred**: named open follow-on once v2 has implementation shape |
| SOW-091 | OUT | Archival of the frozen source trees from the working tree | §13 | **Deferred**: its own packet once P2 is useful |
| SOW-092 | OUT | Changes to `chirality.project.json` or project identity | §13 | No work: "Continue unchanged" — recorded so coverage is explicit; the former daemon-registration clause was dropped under SCA-005 (retired per-user daemon, D-GOV-20) |
| SOW-029 | OUT | Maintain live parent→child hierarchy edges from daemon and hook feeds | PEC-PRS-004 | **Deferred**, not permanent — trigger T-RT: a Runtime-owning loop publishes, under its own authority, an observation interface usable by a non-owning local reader, and `_DomainEngines/profiles/pec.yaml` is amended, and a D-PEC packet names the bridge. PEC can neither request nor require that interface. Was PKG-06 / DEL-06-04 / OBJ-003 before SCA-005 |
| SOW-035 | OUT | Implement the runtime-daemon SSE subscriber bridge, declared and attributable | PEC-STR-003 | **Deferred**, not permanent — trigger T-RT: a Runtime-owning loop publishes, under its own authority, an observation interface usable by a non-owning local reader, and `_DomainEngines/profiles/pec.yaml` is amended, and a D-PEC packet names the bridge. PEC can neither request nor require that interface. Was PKG-07 / DEL-07-02 / no objective before SCA-005; TM-PEC-023 row 4 disposed by this status change, not by a mapping; bridge split per DL-5 |
| SOW-037 | OUT | Implement the cmux socket adapter as an optional, declared and attributable enricher | PEC-STR-003 | **Deferred**, not permanent — re-entry only by a later owner direction (owner 2026-09-24: no plans for cmux compatibility). Was PKG-07 / DEL-07-04 / no objective before SCA-005 (optional; P4); TM-PEC-023 row 6 disposed by this status change, not by a mapping |
| SOW-087 | OUT | Reimplement the shared-runtime client seam concept against v2 entities | §13, D-PEC-56 | **Deferred**, not permanent — trigger T-RT: a Runtime-owning loop publishes, under its own authority, an observation interface usable by a non-owning local reader, and `_DomainEngines/profiles/pec.yaml` is amended, and a D-PEC packet names the bridge. PEC can neither request nor require that interface. Was PKG-07 / DEL-07-05 / no objective before SCA-005; the D-PEC-56 client-seam concept ("Concept carries directly; reimplemented against v2 entities") is retained as historical lineage; TM-PEC-023 row 7 disposed by this status change, not by a mapping |

### 2.3 TBD items (open owner decisions; not resolved by this decomposition)

| ScopeItemID | Status | ScopeItemStatement | SourceRef | Notes |
|---|---|---|---|---|
| SOW-075 | TBD | Whether decision registers gain light structure at source or remain prose parsed best-effort | §16.1 | Assessed (not PRD-stated): affects SOW-012 parser depth only; both paths buildable |
| SOW-076 | TBD | Design and ownership of a global event feed observable by a non-owning reader (premise: no daemon exists; each application owns a private Runtime instance whose only SSE route is the per-session turn stream; no non-owning observation interface is documented) | §16.2 | Assessed (not PRD-stated): bears on the deferred SOW-035 bridge and trigger T-RT, not on record-tier correctness |
| SOW-078 | TBD | Long-term placement: `projects/pec` vs root promotion | §16.4 | Explicitly deferred by the PRD |
| SOW-079 | TBD | Whether the web UI folds into the desktop app or remains a standalone local page | §16.5 | Assessed (not PRD-stated): affects P2 packaging, not dashboard content |
| SOW-080 | TBD | Auth reuse: which PEC-local token mechanism PEC uses, including credentials for the agent access class (premise: Runtime token registries are private to each application's Runtime instance, and reuse of an App registry is foreclosed by the Runtime consumer guide) | §16.6 | Affects SOW-003 implementation choice |
| SOW-081 | TBD | Whether "PEC" is re-expanded or kept as a legacy name | §16.7 | Naming only |
| SOW-082 | TBD | Whether the Root, Runtime and Bridge ledgers adopt a receipt contract (premise: App, Piping and PEC ledgers carry receipt-contract-v2; App/Piping ledgers are historical and their new receipts are central `RECEIPT.md`) | §16.8 | Affects SOW-013 per-loop grammar coverage |
| SOW-083 | TBD | Event-contract home (shared Runtime contracts at `projects/chirality-runtime/packages/contracts` vs PEC-local schema + pinned mirror) and API transport (Unix socket only vs additional loopback listener; transport posture per D-GOV-43 A2) | §16.9 | Fenced: PEC builds local-first either way (SOW-034/040) |

### 2.4 Domain signals (for Phase 4 partitioning; observed, not yet packages)

- **Ingest/parsing** vs **derivation/reconciliation** vs **serving/API** vs
  **rendering/dashboards** vs **integration bridges** vs **validation
  tooling** — six distinct kinds of work in the requirement families.
- Runtime surfaces: a core service (parsers, store, reconciler, evaluators),
  a socket API server, a web dashboard UI, and a hooks CLI; the
  external-process bridges once listed here (daemon SSE, cmux) are deferred
  under SCA-005 (SOW-035 behind trigger T-RT; SOW-037 until a later owner
  direction).
- Persistence surface: one gitignored local store (technology unspecified by
  the PRD — a design choice downstream, not invented here).
- Contract surfaces: versioned event contracts and versioned API schema.
- Observation surfaces: harness-reported presence and read-only Git/worktree
  scanning — producers distinct from file parsing (amended at Phase 6, DL-14).
- Authoring surfaces: ADRs and the v2 SPEC as governed product records
  (amended at Phase 6, DL-14).
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
items; the §11/§12 measurement items (SOW-058..063, 084, 085) and the §12
reliance-advertisement gate (SOW-100) are the test instruments.

| ObjectiveID | Statement | SourceRef | Mapped Scope Items | MappedDeliverables |
|---|---|---|---|---|
| OBJ-001 | Orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation | §3.1 | SOW-001, SOW-003..009, SOW-011..017, SOW-038, SOW-040..044, SOW-089, SOW-095..099; instruments: SOW-058, SOW-059, SOW-063, SOW-100 | DEL-00-03, DEL-01-01, DEL-02-01..09, DEL-03-05, DEL-04-01..05, DEL-08-01..06, DEL-10-01, DEL-10-04, DEL-10-08, DEL-10-13 |
| OBJ-002 | Staleness is detected structurally by SHA comparison, never by judgment | §3.2 | SOW-001, SOW-006, SOW-011..019, SOW-095..097; supported by SOW-005 | DEL-01-01, DEL-02-01..09, DEL-03-02, DEL-03-03, DEL-04-02, DEL-04-03 |
| OBJ-003 | Concurrent sessions have a declared, durable surface for presence and status; write-scope collisions are surfaced before they land in Git | §3.3 | SOW-002, SOW-026..028, SOW-030..034, SOW-036, SOW-039, SOW-044, SOW-049; instruments: SOW-061, SOW-062, SOW-084 | DEL-00-02, DEL-01-02, DEL-06-01..03, DEL-06-05, DEL-06-06, DEL-07-01, DEL-07-03, DEL-08-05, DEL-09-05, DEL-10-06, DEL-10-07, DEL-10-09 |
| OBJ-004 | The human owner has one live view: loops, gates, lifecycle census, decisions waiting on them, and who is working where | §3.4 | SOW-022..024, SOW-045..051, SOW-077, SOW-094; instrument: SOW-085 | DEL-01-06, DEL-05-01, DEL-05-02, DEL-09-01..07, DEL-10-05 |
| OBJ-005 | Everything PEC holds can be deleted at any moment without blocking any governed act | §3.5 | SOW-010, SOW-021, SOW-025, SOW-052..056, SOW-088; bound by C1/C2 across all items | DEL-00-01, DEL-01-03, DEL-01-05, DEL-03-01, DEL-03-06, DEL-10-02, DEL-10-03 |
| OBJ-006 | The product thesis remains measurable and falsifiable: adoption, parity, defect, and collision metrics are gathered in system behavior and the §11 falsification clause stays armed | §11 | SOW-020, SOW-057..060, SOW-064, SOW-084, SOW-085, SOW-093 | DEL-01-04, DEL-03-04, DEL-10-01, DEL-10-04, DEL-10-05, DEL-10-09, DEL-10-10, DEL-10-11, DEL-10-12 |

No objective is unmapped at either level (scope items or deliverables);
SOW-062 was mapped to OBJ-003 at Phase 6 (TTL honesty is a presence-surface
instrument). SCA-002 mapped the Phase 2.2 wave scope at revision 1.2
(DL-17). SCA-005 (DL-20) mapped the remaining IN items: the owner's
TM-PEC-023 selections map SOW-022 and SOW-023 to OBJ-004, SOW-034 and
SOW-036 to OBJ-003, SOW-038 to OBJ-001, SOW-044 to OBJ-001/OBJ-003 and
SOW-063 to OBJ-001 — the row-9 selection supersedes DL-14's objective-free
rationale for SOW-063 — and amendment 2 maps SOW-033 to OBJ-003; SOW-095
and SOW-096 enter mapped to OBJ-001/OBJ-002.

**Mapping notes:** no unmapped objectives and no IN item without an
objective. Parser items (SOW-011..017, SOW-095, SOW-096) underlie
OBJ-001/OBJ-002 through the record tier (SOW-001), the derivation SCA-002
carried into the ledger at revision 1.2. Ingest and bridge items are
mapped, by the owner's SCA-005 selections, to the objective whose surface
each directly makes possible; that supersedes the earlier abstention that
left them unmapped. Deferred/OUT and TBD items — including SOW-029,
SOW-035, SOW-037 and SOW-087, deferred under SCA-005 — and the four
retired deliverables (DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05) map to
no objective by design. Full ScopeItem→Objective assignments land in
`ScopeLedger.csv` at Phase 4–5; this table is the objective-side view.

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
| PKG-00 | Architecture Runway & Contracts | Published specifications others consume: v2's first ADRs (incl. the OI-012 core-isolation decision), the v2 SPEC born from this decomposition, and the versioned event-contract types consumed by the hooks CLI bridge, the only remaining bridge | SOW-034, 088, 089 (3) | Implementation of any contract (consuming packages); cross-package edits — PKG-00 publishes, dependants consume |
| PKG-01 | Service Core & Store | The zero-dependency service foundation: record- and presence-tier entity schemas, the gitignored store with ingest-boundary content-minimal enforcement, locality/no-egress posture, self-observability logging, loop-registration config | SOW-001, 002, 052, 053, 056, 057, 077, 094 (8) | Parsing, derivation, serving — other packages |
| PKG-02 | File-Truth Parsers | Read-side grammars over governed files: `_STATUS.md` dialect, decision registers/packets, receipts (ledgers and central `RECEIPT.md`), Markdown work graphs, the MEMORY run index and `LOOP_INIT.md` identity as first-class feeds; run-evidence JSON, workplans and App/Piping ledgers as declared historical grammars; dependency registers; `adapter.yaml` as a parity-peer input | SOW-011..017, 095, 096 (9) | Writing anything; interpretation beyond declared grammars |
| PKG-03 | Reconciliation & Parity | The guaranteed path from file truth to record tier: one-command rebuild, incremental Git-delta reconcile, drift classification, harness parity diffing, stream-loss recovery guarantee, store-only writes, rebuild performance bounds | SOW-010, 018, 019, 020, 021, 038, 054 (7) | Stream ingest mechanics (PKG-07); parsers (PKG-02) |
| PKG-04 | Orientation Services | Derivation and serving of orientation: per-loop returns, deltas since SHA, SHA/freshness stamping, per-claim citations, scope parameterization, explicit measurement limits, and the reliance envelope | SOW-004..009, 097 (7) | Transport (PKG-08); rendering (PKG-09) |
| PKG-05 | Gate Evaluation & Decision Slate | Deterministic advisory evaluation of file/Git-reducible gate preconditions; Explain-shaped verdicts; the cross-loop decision slate | SOW-022, 023, 024 (3) | Any ruling write path (SOW-066, permanent OUT) |
| PKG-06 | Presence & Git Observation | The presence tier's producers: harness-reported session records, Git/worktree scanning, session×worktree×scope correlation, TTL/heartbeat discipline, advisory overlap detection, citation-exclusion enforcement | SOW-026..028, 030..032 (6) | Session lifecycle ownership (the per-application Runtime's, C13); live hierarchy edges (SOW-029, deferred) |
| PKG-07 | Event Ingest & Bridges | Best-effort freshness inputs: idempotent append-only event ingest, the hooks CLI bridge and the durable message store — implementing the PKG-00 event contracts. The daemon SSE bridge and the shared-runtime client seam are deferred (trigger T-RT) and the cmux adapter is deferred (later owner direction) | SOW-033, 036, 039 (3) | Record-tier fact creation (PKG-03 guarantee); contract definition (PKG-00); writes into `projects/chirality-runtime/**` (SOW-074, deferred) |
| PKG-08 | API & Access | The machine-consumer surface: Unix-socket binding, token-scoped access classes, p95 latency, versioned additive schema, compact citation-bearing responses, SSE subscription, response-size budgets, and the agent tool-call query surface | SOW-003, 040..044, 098, 099 (8) | Dashboard rendering (PKG-09) |
| PKG-09 | Dashboards | The human-owner surface: overview, lifecycle census, register views, decision slate view, presence board, universal drill-down, documented pressure rules | SOW-045..051 (7) | New data classes; restating authored text (C6) |
| PKG-10 | Validation & Measurement | Release-gating proof and metrics: kill test, no-ruling-write verification, Step-0 baseline, defect/adoption/collision/parity measurement, seeded-conflict, TTL-honesty and stream-loss tests, usage observability, directed bootstrap progression evidence, and the reliance-advertisement gate | SOW-025, 055, 058..064, 084, 085, 093, 100 (13) | The behaviors under test (their home packages) |

## 5. Deliverables (Phase 5)

68 deliverable rows across the 11 packages: 64 active and 4 retired under
SCA-005 (DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05), kept as
`[RETIRED — SCA-005]` rows for register integrity. **`Deliverables.csv` is
the authoritative companion register** (full fields: description, responsible
party, anticipated artifacts, envelope notes); the tables below are the
compact control view. `PhaseHint` is sequencing metadata per DL-3, never a
package. ResponsibleParty is `TBD` throughout — assignment happens at
WORKING_ITEMS activation, not here. Conventions are DL-13; Phase 6
verification errata are DL-14.

Context Envelope posture (active deliverables): **28 S / 34 M / 2 L / 0 XL.**
Both L deliverables (DEL-02-03 receipts parser; DEL-01-01 record-tier schema)
carry mandatory envelope notes; no XL exists, so no Gate 5/6
acceptance-of-risk is required.

### PKG-00 Architecture Runway & Contracts

| ID | Name | Type | Env | Phase | Covers |
|---|---|---|---|---|---|
| DEL-00-01 | v2 first ADRs (core isolation + carried postures) | DOC_UPDATE | S | pre-P1 | SOW-088 |
| DEL-00-02 | Event-contract schema v1 | API_CONTRACT | M | P2 | SOW-034 |
| DEL-00-03 | v2 SPEC seed | DOC_UPDATE | M | pre-P1 | SOW-089 |

### PKG-01 Service Core & Store

| ID | Name | Type | Env | Phase | Covers |
|---|---|---|---|---|---|
| DEL-01-01 | Record-tier schema & entity model | DATA_MODEL_CHANGE | **L** | P1 | SOW-001 |
| DEL-01-02 | Presence-tier schema & entity model | DATA_MODEL_CHANGE | S | P3 | SOW-002 |
| DEL-01-03 | Store bootstrap & content-minimal guard | BACKEND_FEATURE_SLICE | M | P1 | SOW-056 |
| DEL-01-04 | Self-observability logging | OBSERVABILITY | S | P1 | SOW-057 |
| DEL-01-05 | Zero-dependency & locality enforcement | CI_CD_CHANGE | S | P1 | SOW-052, 053 |
| DEL-01-06 | Loop registry (local config default) | BACKEND_FEATURE_SLICE | S | P1 | SOW-077, SOW-094 |

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
| DEL-02-08 | Work-graph parser | BACKEND_FEATURE_SLICE | M | P1 | SOW-095 |
| DEL-02-09 | MEMORY run-index parser | BACKEND_FEATURE_SLICE | S | P1 | SOW-096 |

### PKG-03 Reconciliation & Parity

| ID | Name | Type | Env | Phase | Covers |
|---|---|---|---|---|---|
| DEL-03-01 | Full-rebuild reconciler (one command) | BACKEND_FEATURE_SLICE | M | P1 | SOW-010, 021 |
| DEL-03-02 | Incremental reconcile on Git delta | BACKEND_FEATURE_SLICE | M | P1 | SOW-018 |
| DEL-03-03 | Drift classification | BACKEND_FEATURE_SLICE | M | P1 | SOW-019 |
| DEL-03-04 | Practitioner-harness parity diff | BACKEND_FEATURE_SLICE | M | P1 | SOW-020 |
| DEL-03-05 | Stream-loss recovery guarantee | BACKEND_FEATURE_SLICE | S | P3 | SOW-038 |
| DEL-03-06 | Rebuild performance bounds | TEST_SUITE | S | P1 | SOW-054 |

### PKG-04 Orientation Services

| ID | Name | Type | Env | Phase | Covers |
|---|---|---|---|---|---|
| DEL-04-01 | Loop orientation return | BACKEND_FEATURE_SLICE | M | P1 | SOW-004 |
| DEL-04-02 | Delta service since SHA | BACKEND_FEATURE_SLICE | M | P1 | SOW-005 |
| DEL-04-03 | Citation & freshness stamping | BACKEND_FEATURE_SLICE | M | P1 | SOW-006, 007, 097 |
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
| DEL-06-04 | Live hierarchy edges | BACKEND_FEATURE_SLICE | S | P4 | — **[RETIRED — SCA-005]** (was SOW-029) |
| DEL-06-05 | TTL/heartbeat discipline & citation exclusion | BACKEND_FEATURE_SLICE | M | P3 | SOW-030, 032 |
| DEL-06-06 | Advisory overlap detection | BACKEND_FEATURE_SLICE | M | P3 | SOW-031 |

### PKG-07 Event Ingest & Bridges

| ID | Name | Type | Env | Phase | Covers |
|---|---|---|---|---|---|
| DEL-07-01 | Idempotent event ingest + durable message store | BACKEND_FEATURE_SLICE | M | P3 | SOW-033, 039 |
| DEL-07-02 | Daemon SSE subscriber bridge | BACKEND_FEATURE_SLICE | M | P4 | — **[RETIRED — SCA-005]** (was SOW-035) |
| DEL-07-03 | Hooks CLI bridge | BACKEND_FEATURE_SLICE | M | P3 | SOW-036 |
| DEL-07-04 | cmux socket adapter (optional) | BACKEND_FEATURE_SLICE | M | P4 | — **[RETIRED — SCA-005]** (was SOW-037) |
| DEL-07-05 | Shared-runtime client seam (v2) | BACKEND_FEATURE_SLICE | M | P3 | — **[RETIRED — SCA-005]** (was SOW-087) |

### PKG-08 API & Access

| ID | Name | Type | Env | Phase | Covers |
|---|---|---|---|---|---|
| DEL-08-01 | Unix-socket server + token-scoped access | SECURITY_CONTROL | M | P1 | SOW-003, 040 |
| DEL-08-02 | Versioned additive API schema | API_CONTRACT | S | P1 | SOW-042 |
| DEL-08-03 | Compact citation-bearing response format | API_CONTRACT | M | P1 | SOW-043, 098 |
| DEL-08-04 | Orientation latency budget (p95 ≤ 100 ms) | TEST_SUITE | S | P1 | SOW-041 |
| DEL-08-05 | SSE delta/presence subscription | BACKEND_FEATURE_SLICE | M | P4 | SOW-044 |
| DEL-08-06 | Agent tool-call query surface | BACKEND_FEATURE_SLICE | M | P3 | SOW-099 |

### PKG-09 Dashboards

| ID | Name | Type | Env | Phase | Covers |
|---|---|---|---|---|---|
| DEL-09-01 | Overview dashboard | UX_UI_SLICE | M | P2 | SOW-045 |
| DEL-09-02 | Lifecycle census dashboard | UX_UI_SLICE | M | P2 | SOW-046 |
| DEL-09-03 | Register views | UX_UI_SLICE | M | P2 | SOW-047 |
| DEL-09-04 | Decision-slate view ("waiting on you") | UX_UI_SLICE | S | P2 | SOW-048 |
| DEL-09-05 | Presence board | UX_UI_SLICE | M | P3 | SOW-049 |
| DEL-09-06 | Universal drill-down to cited source | UX_UI_SLICE | M | P2 | SOW-050 |
| DEL-09-07 | Explain-shaped pressure rules | BACKEND_FEATURE_SLICE | M | P2 | SOW-051 |

### PKG-10 Validation & Measurement

| ID | Name | Type | Env | Phase | Covers |
|---|---|---|---|---|---|
| DEL-10-01 | Step-0 cost baseline (pre-P1) | MEASUREMENT | S | pre-P1 | SOW-058 |
| DEL-10-02 | Kill test (standing release gate) | TEST_SUITE | M | P1 | SOW-055 |
| DEL-10-03 | No-ruling-write verification | TEST_SUITE | S | P1 | SOW-025 |
| DEL-10-04 | Orientation defect-rate spot-check | MEASUREMENT | S | P2 | SOW-059 |
| DEL-10-05 | Owner-consultation logging | MEASUREMENT | S | P2 | SOW-085 |
| DEL-10-06 | Seeded-conflict overlap test | TEST_SUITE | S | P3 | SOW-061 |
| DEL-10-07 | Presence TTL honesty tests | TEST_SUITE | S | P4 | SOW-062 |
| DEL-10-08 | Stream-loss recovery demonstration | TEST_SUITE | S | P4 | SOW-063 |
| DEL-10-09 | Collision-incident measurement | MEASUREMENT | S | P3 | SOW-084 |
| DEL-10-10 | Directed bootstrap self-ingest validation | TEST_SUITE | M | P1 | SOW-064 |
| DEL-10-11 | Parity metric (DriftFindings per reconcile) | MEASUREMENT | S | P1 | SOW-093 |
| DEL-10-12 | Poll-adoption measurement | MEASUREMENT | S | P3 | SOW-060 |
| DEL-10-13 | Reliance-advertisement gate | TEST_SUITE | S | P1 | SOW-100 |

## 6. Scope Ledger

**Authoritative register: `ScopeLedger.csv`** — 100 rows tracing every
scope item through SOW → PKG → DEL → OBJ with DecisionRef and OpenIssue
columns. Live since Gate 4 (assignments) and completed at Phase 5 (the
DeliverableIDs column). The `OpenIssue` column is TRUE for TBD items and
for IN items carrying a live open issue (SOW-088 / OI-012).

## 7. Coverage & Telemetry (Phase 6)

Structural checks (coverage, single-package membership, ID coupling,
objective support) were asserted by a session-local generator script each
time the registers were regenerated, and the whole package was
independently verified by adversarial review at revisions 0.3 and 0.8→0.9
(DL-9, DL-14). **The generator is not part of this package and no durable
build gate exists yet** — a repo-native register validator is recorded as
follow-on OI-013 for the downstream pipeline to place under its own
instrument.

| Metric | Value |
|---|---|
| ScopeItemCount | 100 (74 IN / 18 OUT / 8 TBD) |
| PackageCount | 11 (PKG-00..PKG-10) |
| DeliverableCount | 68 rows (64 active / 4 RETIRED: DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05) |
| ObjectiveCount | 6 |
| UnassignedScopeItems (IN without package) | **0** |
| ScopeItemsWithoutDeliverableMapping (IN) | **0** |
| UnmappedObjectives | **0** (every objective backed at both scope-item and deliverable level, §3) |
| IN items without objective mapping | **0** (SCA-005: the owner's TM-PEC-023 selections and amendment 2 closed the SCA-002 O-A residue; SOW-035, SOW-037 and SOW-087 left IN; §3 mapping notes) |
| ContextEnvelopeCounts | S 28 / M 34 / L 2 / XL 0 (active deliverables; the 4 retired rows are excluded) |
| OpenIssuesByType | 10 open (8 unresolved §16 owner decisions: OI-001, OI-002, OI-004..009; 1 architecture ADR: OI-012; 1 tooling follow-on: OI-013) / 3 resolved (OI-003 by D-PEC-78 O-A; OI-010 and OI-011 at Gate 2) |
| Deliverable single-package membership | 68/68; every `DEL-XX-YY` prefix matched to its parent package |
| Revision | 1.6, 2026-09-26 (SCA-006) |

Coverage-check provenance: every IN scope item traces §PRD → SSOW →
package → deliverable(s) in `ScopeLedger.csv`; OUT items record the
boundary (permanent vs deferred); TBD items carry their open-issue IDs.
SCA-001 pre/post integrity evidence lives in
`execution/_ScopeChange/SCA-001_2026-07-24_2206/`; the expected
pre-scaffold `AUDIT_DECOMP` `FAILED_INPUTS` result is a filesystem
limitation, not register-coverage evidence (OI-013 remains open).

## 8. Context Budget QA (Phase 6)

**Authoritative register: `ContextBudgetQA.csv`.**

- **No XL deliverable exists.** Nothing requires split-or-accept treatment.
- **Two L:** DEL-02-03 (receipts parser: ledger grammars plus the central
  `RECEIPT.md` grammar, OI-008 open for the Root, Runtime and Bridge
  ledgers; split line: the central-receipt grammar) and DEL-01-01
  (record-tier schema: 16 entity types, the dependency of every derivation
  package). Both MEDIUM risk with envelope notes and named split lines if
  implementation demands them.
- **Two OI-coupled MEDIUM risks at M envelope** (DL-14): DEL-00-02
  (event-contract schema — OI-009 decides its home; the shared option path
  is `projects/chirality-runtime/packages/contracts`) and DEL-08-01
  (socket + tokens — OI-006 decides the PEC-local token mechanism; no
  shared Runtime token registry exists to reuse). Held at current envelope;
  re-assessed on the linked ruling.
- **SCA-005 additions and re-assessments:** DEL-02-08 (work-graph parser)
  is M with MEDIUM risk — a new grammar, profile-driven discovery,
  PR-to-merge resolution inputs and three pinned fixture classes — held as
  one parser slice; DEL-02-09 (MEMORY run-index parser) is S, LOW;
  DEL-02-06 is held at M, LOW, with re-assessment toward S after its scope
  narrowed to `LOOP_INIT.md` identity.
- **SCA-006 additions and re-assessments:** DEL-08-03 (compact response
  format) is re-enveloped S → M with LOW risk kept — declared response-size
  budgets met by pagination or continuation, with stated truncation, join
  the citation-bearing format as one slice; DEL-08-06 (agent tool-call
  query surface) is M with MEDIUM risk, coupled to OI-006 like DEL-08-01
  and held at its envelope until that ruling; DEL-10-13
  (reliance-advertisement gate) is S, LOW — it composes other packages'
  evidence into one gate record.
- **Four retired rows** (DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05) keep
  their envelope and risk cells for register integrity and are excluded
  from active envelope counts.
- Remaining S/M deliverables assessed LOW risk: single package, single
  primary artifact shape, bounded file surface. The DL-13d merges were
  re-audited at Phase 6: DEL-10-05 was split (two consumers, two phases →
  DEL-10-05 + DEL-10-12) and DEL-06-05's cross-package enforcement edge to
  DEL-04-03 is now declared; the other six merges hold as one shape each.

## 9. Vocabulary Map (seeded at Phase 2)

| CanonicalTerm | Synonyms | Notes |
|---|---|---|
| coordination plane | PEC v2 | The product; never "project-management tool" |
| record tier | reconciled tier, projection | Rebuilt from file truth; per-claim citations; the only citable-with-sources tier (and even then never as authority) |
| presence tier | — | TTL'd, heartbeat-aged, evaporating; never citable |
| store | database | Gitignored, safe to delete; "database" avoided in prose where it suggests authority |
| orientation | Step-0 return | The per-loop/scope serve of PEC-ORI-001..007 |
| OrientationSnapshot | — | Record-tier entity (§7.1): a generated orientation return stamped with examined SHA — the machine generalization of a receipt. Distinct from the general term "orientation" |
| reconciler | rebuild | The guaranteed path from file truth to record tier (PEC-K-07) |
| ingest | stream ingest, event ingest | Best-effort (PEC-K-07); deliberately **not** a synonym of reconciliation, which is guaranteed |
| Explain-shaped | explainable derivation | Rule ID + threshold + contributing cited sources; from the prototype's `Explain<V>` pattern (cited, not copied) |
| graceful absence | kill test, deletability | PEC-K-01; the kill test is its executable form |
| decision slate | "waiting on you" | Aggregated AWAITING_RULING rows + parked lanes; link-only |
| gate verdict | gate evaluation, precondition check | Deterministic, advisory, never dispositive |
| loop | work loop, domain-engine loop | Tenancy unit above Project. PEC serves only the loops its registry (`loops.json`) lists; the observed LOOP_INIT-bearing loops are six (root, app-dev, piping, pec, bridge — its last receipt was dated 2026-08-02 when SCA-005 was prepared — and runtime) |
| harness | practitioner harness / application-owned Runtime service (per application, D-GOV-43 A2) / hooks CLI | Disambiguate: "practitioner harness" = the parity-peer CLI checker; "harness" unqualified = a potential machine consumer that acts only when explicitly enabled under its own authority; no polling or injection duty is inferred. An agent may also query directly through tool calls under the agent access class; that agent is not a harness |
| examined-through SHA | examined SHA, freshness SHA | The staleness comparator (PEC-K-04) |
| DriftFinding | drift, parity discrepancy | Classified difference between snapshots or vs harness output |
| heartbeat age | last-heartbeat, TTL age | Liveness is never asserted beyond it (PEC-PRS-005) |
| scope claim | write-scope declaration, "working here" | Advisory only; overlap-detection input |
| work-domain package | PKG-XX, decomposition package | **Disambiguation:** distinct from (a) the retired product's `*-PKG-*` tokens (`26020-PKG-001` demo/fixture work-package IDs; `PEC-PKG-009` **v0.4** requirement IDs — the v1.0 PRD used no `PEC-PKG` family), and (b) v2's own record-tier entities named `Package`/`Deliverable` (PRD §7.1 — *other loops'* lifecycle units that PEC models and renders, e.g. in DEL-01-01/DEL-09-02). In this package, bare "package" means work-domain package; the entity sense is written `Package (entity)` |
| frozen reference corpus | old PEC, v0.4 baseline, prototype | Read/cite only; machinery carries as pattern, never code |
| content-minimal | residency rule, no-content rule | Paths, counts, SHAs, states, hashes — never file/diff content |
| MEASUREMENT (deliverable type) | metric deliverable | Added to the suggestive software taxonomy for §11 metric work (DL-13): a deliverable whose artifact is a measurement method, instrumentation, and report — not a feature or test of behavior |
| work graph | undertaking graph | A loop's current undertaking graph at `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md` (SOW-095), distinct from historical `WORK_GRAPH.json` run evidence. **Disambiguation:** graph node IDs (P1, C1, F1, W1, V1, M1, R1 …) are local node tokens, distinct from PEC release phases P1–P4 and hard constraints C1–C16 |
| receipt | loop receipt, central receipt | Disambiguate a `LOOP_RECEIPTS.md` ledger entry from a central `execution/_Coordination/AgentRuns/<RunID>/RECEIPT.md` (a derivative account, one per undertaking); both feed the Receipt entity (SOW-013) and neither is authority |
| feed profile | — | A closed, PEC-versioned grammar bundle that a registry (`loops.json`) row selects, e.g. `shared-dev-loop`, `remaining-loop`, `loop-receipts-ledger`, `agentruns-json`; PEC's reading hypothesis, never the loop's truth (SOW-077, SOW-094) |
| declared activity | graph-declared node state | A record-tier graph-declared node state (e.g. "declared ACTIVE as of commit X, age N"); never a liveness assertion and never presence tier (SOW-049) |
| operational reliance | operational reliance on PEC data | Acting on a PEC record-tier claim as true as of its examined-through SHA, within the coverage and tier the response declares, with file fallback; available only from a release that has passed the §12 reliance-advertisement gate; never authority. Distinct from the L-A1 reliance-hold control (`ACTIVE_RELIANCE_HOLDS.csv`, `pec_reliance_hold.py` `rely-for-production`), from professional reliance (K-AUTH-1), and from Root PRD N-1 'for purposes of reliance' |
| reliance envelope | — | The per-response declaration of pin, coverage, trust tier and file-fallback signal that bounds operational reliance (PEC-ORI-007, SOW-097) |
| response budget | response-size budget, size cap | A declared bound on response size met by pagination or continuation, with stated truncation (PEC-API-006, SOW-098); distinct from the latency budget (PEC-API-002) |

## 10. Open Issues

| ID | Refs | Issue | Owner action that closes it |
|---|---|---|---|
| OI-001 | SOW-075 | §16.1 register structuring at source undecided | §16 ruling |
| OI-002 | SOW-076 | §16.2 global event feed undecided; premise re-expressed under SCA-005: no daemon exists, each application owns a private Runtime instance whose only SSE route is the per-session turn stream, and no non-owning observation interface is documented | §16 ruling (cross-loop) |
| OI-003 | SOW-077 | **RESOLVED by D-PEC-78 O-A:** the existing PEC-owned JSON/schema paths and core-owned typed port are the long-term registry home and shape. PEC owns only its configured service set; each listed loop retains authority over its entrypoint and governed truth; no governed act depends on PEC or the registry | Closed |
| OI-004 | SOW-078 | §16.4 long-term placement deferred | §16 ruling |
| OI-005 | SOW-079 | §16.5 UI packaging undecided | §16 ruling |
| OI-006 | SOW-080 | §16.6 auth reuse undecided; premise re-expressed under SCA-005: Runtime token registries are private to each application's Runtime instance and reuse of an App registry is foreclosed, so the open choice is the PEC-local token mechanism; the open choice also covers credentials for the agent access class (tool-call query, SOW-099; SCA-006) | §16 ruling |
| OI-007 | SOW-081 | §16.7 name re-expansion undecided | §16 ruling |
| OI-008 | SOW-082 | §16.8 receipt-contract adoption undecided for the Root, Runtime and Bridge ledgers; premise re-expressed under SCA-005: App, Piping and PEC ledgers carry receipt-contract-v2, and App/Piping ledgers are historical with new receipts in central `RECEIPT.md` | §16 ruling (per-loop) |
| OI-009 | SOW-083 | §16.9 event-contract home and API transport undecided; the shared option path is `projects/chirality-runtime/packages/contracts` (Runtime loop; root `runtime/` relocated, PR #727) | §16 ruling |
| OI-010 | SOW-064 | **RESOLVED at Gate 2 (2026-07-24):** the §12 closing paragraph governs — the first loop the P1 reconciler ingests is PEC v2's own build (bootstrap as thesis validation); the P1 table's "(piping or root)" parenthetical does not constrain the first-loop choice. Owner accepted the recommended reading in the Gate 2 confirmation (DL-10) | Closed |
| OI-011 | C3, C15 | **RESOLVED, THEN SUPERSEDED:** Gate 2 originally treated scoped session start and the conversation→workbench transition as polling moments (DL-10). D-PEC-67's exact PEC-K-03/-11 rows and D-PEC-68's v2.2 concordance supersede that reading: PEC declares no polling moment; an explicitly enabled consumer owns mode mapping and cadence, and no receiving-loop duty is created | Closed |
| OI-012 | SOW-088, PKG-00 | Core isolation style — ports-and-adapters (hexagonal) vs functional-core/imperative-shell — is undecided. Recorded basis from the Gate 4 exchange: the PRD's invariants force the isolation properties either way (PEC-K-07 makes bridges disposable inputs; PEC-K-02 makes the store a throwaway projection; PEC-SVC-001 is the dependency-free-core rule); the package partition is congruent with a hexagonal grain (core: PKG-03/04/05 + PKG-01 entities; driven edges: PKG-02/06 + store; driving edges: PKG-07/08/09); nearly all §16 open decisions are adapter-level, so core isolation keeps them open cheaply; the lighter functional-core/imperative-shell variant fits a deterministic-derivation service with less ceremony; the one seam to keep crisp is entity schema (core) vs store persistence (adapter) inside PKG-01 | Decided in DEL-00-01's ADR; owner review at that ADR |
| OI-013 | §7, DL-14 | No durable register validator exists: the coverage/coupling assertions ran in a session-local generator, which is not part of this package and enforces nothing after acceptance | Downstream pipeline places a repo-native register validator under its own instrument (e.g., at PROJECT_SETUP), or the owner declines and review-based verification stands |

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
| DL-11 | 2026-07-24 | Phase 4 forced boundary assignments: SOW-010 (one-command rebuild) → PKG-03 as the reconciler entry point, while the store-path rule (SOW-056) stays PKG-01; SOW-038 (stream-loss recovery) → PKG-03 because the guarantee is reconciliation-side, not ingest mechanics; SOW-025 (no-ruling-write verification) → PKG-10 per DL-8's verification-obligation framing; SOW-087 (client seam) → PKG-07 as daemon-facing integration; SOW-003 (access classes) → PKG-08 with the token-scoped transport; SOW-054 (rebuild bounds) → PKG-03 as reconcile performance; SOW-064 (bootstrap) → PKG-10 as a validation act, not a reconciler feature | Each was assignable to two domains; ledger rows carry `DL-11` in DecisionRef. The `ScopeLedger.csv` register was generated from this document's SSOW tables by a session-local script (see OI-013) to prevent transcription drift |
| DL-12 | 2026-07-24 | Gate 4 restructuring on owner direction ("what about adding a PKG-00 addressing the nuances of the architecture…"): PKG-00 Architecture Runway & Contracts created (precedent: piping's PKG-00 Software Architecture Runway); PKG-11 dissolved into it pre-confirmation (Gate 4 was still open, so no post-acceptance renumbering under I5); SOW-034 reassigned PKG-07→PKG-00 as a published cross-consumer contract. Mechanics constraint: PKG-00 deliverables publish artifacts that dependants consume as declared dependencies — a deliverable never writes into another package (disjoint write scopes preserved). OI-012 (core isolation style) recorded for PKG-00's ADR deliverable | The owner's "contributions to other packages" intent is realized through dependency edges, not cross-package writes |
| DL-13 | 2026-07-24 | Phase 5 conventions: (a) a `MEASUREMENT` deliverable type is added to the software taxonomy for §11 metric work (the base taxonomy is declared suggestive; recorded here and in the Vocabulary Map); (b) `PhaseHint` carries P1–P4 sequencing as metadata per DL-3; (c) ResponsibleParty is `TBD` pending WORKING_ITEMS activation; (d) two-item merges kept single-shape: DEL-03-01, DEL-04-03, DEL-05-01, DEL-06-05, DEL-07-01, DEL-08-01, DEL-01-05, DEL-10-05 — re-audited at Phase 6, see DL-14; (e) `Deliverables.csv` and the ledger's SOW→DEL column generated from one source of deliverable definitions with asserted single-package coverage and ID coupling (session-local generator; OI-013) | Keeps deliverables agent-executable and the registers drift-free during authoring |
| DL-14 | 2026-07-24 | Phase 6 adversarial verification (opus-5; 19 confirmed defects, 5 suspicions dispositioned) applied at revision 0.9: SOW-093 (§11.5 parity metric) and SOW-094 (loop-registration config) added with DEL-10-11 and DEL-01-06; DEL-10-05 split (→ DEL-10-12: two instrumentation points, two phases); DEL-01-01 re-enveloped M→L (14 entity types, not "11 entities"); DEL-03-05 moved P4→P3 so ingest never runs without its PEC-K-07 safety invariant; DEL-00-02 P3→P2 and DEL-00-03 P1→pre-P1 (PKG-00 publishes ahead of consumers); OI-coupled risk raised to MEDIUM on DEL-00-02 (OI-009) and DEL-08-01 (OI-006); DEL-09-06 declared a PKG-09-internal shared component sequenced first; DEL-09-07 retyped BACKEND_FEATURE_SLICE (artifacts are rules, not UI); DEL-06-05's cross-package enforcement edge to DEL-04-03 declared; SOW-062 mapped to OBJ-003, SOW-063 left unmapped intentionally (instruments PEC-K-07, which no §3 objective states); SOW-088 flagged OpenIssue=TRUE (OI-012); the false "build-gate generator" claim corrected and recorded as OI-013; §6 stale placeholder replaced; §2.4 amended (observation + authoring signals); §3 gains MappedDeliverables; vocabulary gains the `Package (entity)` disambiguation and this log was reordered; names normalized across doc and registers | Fix-before-gate: all corrections landed before Gate 6 presentation; IDs remain append-only (I5) |
| DL-15 | 2026-07-24 | Justified duplication (per the standard's companion-register clause): the §2 SSOW tables intentionally duplicate the ledger's identity columns because they are the Gate 2 human-confirmation surface and the generation source — `ScopeLedger.csv` stays authoritative for assignments (PKG/DEL/OBJ/DecisionRef/OpenIssue); §5 duplicates only the compact control fields (ID/name/type/envelope/phase/covers) — `Deliverables.csv` stays authoritative for full deliverable truth. Any conflict resolves to the register for assignment fields and to this document for statement text, pending regeneration | The duplication is directional and declared, not drift-prone parity |
| DL-16 | 2026-07-24 | SCA-001, requested by owner Ryan Tufts and opened by D-PEC-61, adds construction-specific constraint C16, expands SOW-064 and DEL-10-10 into directed full-DAG bootstrap progression evidence, maps both to OBJ-006, and re-envelopes DEL-10-10 S→M; no package, deliverable, objective, scope item, product function, stable ID, or dependency edge is added or removed | `FULL_GRAPH` supplies direction for PEC's own governed construction without becoming a universal PEC product mode; capability-before-consumption keeps the bootstrap acyclic, observed friction remains evidence rather than authority, the file-native fallback remains operable, and dependency-edge materialization stays with PROJECT_SETUP |
| DL-17 | 2026-07-25 | SCA-002, requested by owner Ryan Tufts and opened by D-PEC-64, completes the deliverable→objective mapping for the Phase 2.2 scope-of-work wave scope (O-A wave-minimum): 20 IN ledger rows gain ObjectiveIDs and 17 deliverables gain SupportsObjectives, with §3's parser derivation carried into the ledger rather than superseded and the ingest/bridge and SOW-063 intentional rationale retained verbatim for the 11-row residue; §5's stale envelope-posture line is corrected to the register value; no package, deliverable, objective, scope item, product function, stable ID, or dependency edge is added or removed | The wave's SOW briefs require non-empty package_objective_refs from register truth; completing the mapping in decomposition truth (rather than by a SOW-local convention, which the owner declined) keeps objective attribution auditable at its source, and confining the amendment to wave scope leaves the recorded intentional-unmapped rationale standing rather than force-mapping it |
| DL-18 | 2026-07-28 | SCA-003, owner-directed under the standing completion approval after D-PEC-68 became durable, reconciles the accepted decomposition to PRD v2.2's consumer-owned interface posture and D-PEC-67 L-A2's ADR-014 historical-lineage correction: C3/C15, source/basis prose, SOW-041/060/085/088, DEL-00-01/10-05/10-12 descriptions, and three exact `_CONTEXT.md` mirrors are modified; the DEL-10-12 canonical label/path is preserved | This is a MODIFY-only semantic correction. It preserves 94 scope items, 11 packages, 64 deliverables, 6 objectives, every stable ID, and all dependency edges. ScopeOfWork, `_REFERENCES.md`, dependencies, hold, lifecycle, implementation, estimates, schedules, release, and reliance remain downstream or excluded |
| DL-19 | 2026-08-03 | SCA-004, requested by owner Ryan Tufts through D-PEC-78 O-A, promotes SOW-077 from TBD to IN, maps it to PKG-01 → DEL-01-06 → OBJ-004, adds SOW-077 to DEL-01-06 coverage, and records OI-003 resolved; DEL-01-06's stable name/path and all source bytes remain unchanged | The existing PEC-owned strict-version-1 JSON/schema paths and core-owned typed port are the selected long-term registry home and shape. PEC owns only its configured service set; each listed loop retains authority over its own entrypoint and truth; later row changes remain owner-gated PEC configuration acts; graceful absence and the no-governed-dependency boundary remain intact |
| DL-20 | 2026-09-25 | SCA-005, requested by owner Ryan Tufts and opened by D-PEC-86, accepted at checkpoint 1 on 2026-09-24 with amendment 1 (TM-PEC-023 selections; cmux deferral) and amendment 2 (SOW-033 → OBJ-003), re-bases the feed model on the shared development-loop method and the application-owned Runtime topology (D-GOV-43 A2): it adds SOW-095/096 and DEL-02-08/09 (work-graph and MEMORY run-index parsers, P1, OBJ-001;OBJ-002); re-sources SOW-001/004/013..017 and DEL-01-01, DEL-02-03..07, DEL-03-03 and DEL-04-01; declares closed, PEC-versioned feed profiles on registry rows (SOW-077/094, DEL-01-06; a strict schema v2 by a later D-PEC source packet within D-PEC-78 O-A) and makes `adapter.yaml` a parity-peer input; moves SOW-029, SOW-035 and SOW-087 (trigger T-RT) and SOW-037 (later owner direction) to Deferred OUT and retires DEL-06-04, DEL-07-02, DEL-07-04 and DEL-07-05 non-destructively; records the owner's TM-PEC-023 selections and the SOW-033 mapping, so no IN item lacks an objective (SOW-063's mapping supersedes DL-14's objective-free rationale); and re-expresses C5, C13, R4, SOW-026/034/049/074/076/080/082/083/092, OI-002/006/008/009, PKG-00/02/06/07, the telemetry and the vocabulary. The source corpus moves to PRD v2.3 | Invariants preserved: 11 packages and 6 objectives; every stable ID, name and path retained (CP1-N) and the new IDs append-only; retired rows kept for register integrity; no IN item without package, deliverable or objective; the union invariant holds; the §16 decisions stay open (Q6); C3, C15 and SOW-058 unchanged. Dependency registers, `_CONTEXT.md` and `_REFERENCES.md` metadata, Scope of Work contracts, lifecycle and source remain downstream of this amendment |
| DL-21 | 2026-09-26 | SCA-006, opened under `D-PEC-90` R-A grant item 3 (the owner's R-A ruling and direct-query answer of 2026-09-25) and accepted at checkpoint 1 on 2026-09-25 with DQ-a, ENV-a, BUD-a, GATE-a and INS-a (R-C excluded), writes operational reliance on PEC data into the decomposition: C3 is re-expressed (a consumer may act on a record-tier claim within the pin, coverage and tier the response declares, with file fallback, only from a release that has passed the §12 reliance-advertisement gate; non-authoritative is kept in the authority sense); it adds SOW-097 (reliance envelope, PEC-ORI-007 → DEL-04-03), SOW-098 (response-size budgets, PEC-API-006 → DEL-08-03), SOW-099 (agent tool-call query surface, PEC-API-007 → new DEL-08-06, P3) and SOW-100 (the standing reliance-advertisement gate, §12 → new DEL-10-13, P1), all mapped to OBJ-001 and SOW-097 also to OBJ-002; adds the read-only `agent` access class to SOW-003 and DEL-08-01, enabled agent tool-call surfaces to SOW-060, and `agent` credentials to the open SOW-080 / OI-006 premise; re-envelopes DEL-08-03 S → M; and re-expresses §1.2, PKG-04/08/10, the OBJ-001/OBJ-002 views, the telemetry and the vocabulary (+operational reliance, reliance envelope, response budget; `harness` modified). The source corpus moves to PRD v2.4 | Invariants preserved: 11 packages and 6 objectives with unchanged statements; every stable ID, name and path retained and the new IDs append-only; no IN item without package, deliverable or objective; the union invariant holds; C1, C2 and C15 (PEC-K-01, PEC-K-02, PEC-K-11) unchanged and PEC output stays never citable as authority (R-C not selected); the token mechanism stays open (OI-006); the §12 P1 row is not edited (GATE-a). Dependency registers, `_CONTEXT.md` and `_REFERENCES.md` metadata, Scope of Work contracts, lifecycle and source remain downstream of this amendment |

## 12. Revision History (Phase 7 change summary)

| Rev | Gate | What changed |
|---|---|---|
| 0.1 | 1 | Intake: title, summary, constraints C1–C14, postures, references |
| 0.2–0.3 | 2 | SSOW drafted (83 items) then verification errata (16 defects): +SOW-084..092, C15, OI-001..011 |
| 0.4 | 3 | Six objectives derived and mapped; OI-010/011 owner-resolved at Gate 2 |
| 0.5 | 4 | Eleven packages; `ScopeLedger.csv` live; forced assignments DL-11 |
| 0.6 | 4 | Owner-directed restructure: PKG-00 Architecture Runway & Contracts (DL-12, OI-012) |
| 0.7 | 5 | 61 deliverables; `Deliverables.csv` live; MEASUREMENT type (DL-13) |
| 0.8 | 6 | Coverage & Telemetry; `ContextBudgetQA.csv` live |
| 0.9 | 6 | Phase 6 verification errata (19 defects, DL-14/15): +SOW-093/094, +DEL-01-06/10-11/10-12, DEL-10-05 split, re-envelopes, phase corrections, OI-013 |
| 1.0 | 7 | Publication: `Companion_Inventory.csv` live; handoff state in `_LATEST.md`; presented for final acceptance |
| 1.1 | SCA-001 | Directed full-DAG self-bootstrap clarification under D-PEC-61: +C16; expanded SOW-064 and DEL-10-10; OBJ-006 mapping; DEL-10-10 S→M; PRD v2.1 source reconciliation; telemetry and handoff parity; topology unchanged |
| 1.2 | SCA-002 | Deliverable→objective mapping for the Phase 2.2 wave scope under D-PEC-64 (O-A): +ObjectiveIDs on 20 IN rows, +SupportsObjectives on 17 deliverables, §3 objective-side view and mapping notes reconciled, §7 metric 31→11, §5 envelope-posture line corrected (SCA-001 residual); topology unchanged |
| 1.3 | SCA-003 | PRD v2.2 consumer-interface and ADR-014 historical-lineage concordance: C3/C15, source/basis, SOW-041/060/085/088, DEL-00-01/10-05/10-12 descriptions, and three `_CONTEXT.md` mirrors; DEL-10-12 label/path, topology, stable IDs, and dependency edges unchanged |
| 1.4 | SCA-004 | D-PEC-78 O-A loop-registry disposition: SOW-077 TBD→IN and mapped to PKG-01 / DEL-01-06 / OBJ-004; SOW-094 implementation basis reconciled; DEL-01-06 coverage and description updated in place; OI-003 resolved; stable IDs, topology, source, dependency edges, envelope, phase, name, and path unchanged |
| 1.5 | SCA-005 | Feed-model and Runtime-topology rebaseline under D-PEC-86: +SOW-095/096 and +DEL-02-08/09; SOW-029/035/037/087 IN→OUT Deferred and DEL-06-04/07-02/07-04/07-05 retired non-destructively; registry feed profiles; `adapter.yaml` parity-peer only; TM-PEC-023 selections and the SOW-033 mapping (0 IN items without objective); C5/C13, R4, SSOW rows, PKG-00/02/06/07, deliverable descriptions, §16 premises, vocabulary (26 terms), telemetry and envelope posture (S 28 / M 32 / L 2) reconciled; PRD v2.3 source; stable IDs, names and paths retained |
| 1.6 | SCA-006 | Operational reliance on PEC data under D-PEC-90 R-A: C3 re-expressed; +SOW-097..100 and +DEL-08-06/10-13 (reliance envelope, response-size budgets, agent tool-call query surface, reliance-advertisement gate); read-only agent access class (SOW-003, DEL-08-01); SOW-060/080 and OI-006 extended; DEL-04-03/08-03 descriptions and coverage, DEL-08-03 S→M; PKG-04/08/10, OBJ-001/002 views, §1.2, vocabulary (29 terms), telemetry and envelope posture (S 28 / M 34 / L 2) reconciled; PRD v2.4 source; stable IDs, names and paths retained |

## Companion Inventory

| Filename | PackageRole | Status | Description |
|---|---|---|---|
| `SOFTWARE_DECOMP.md` | working surface | live (this file) | Main decomposition document; amendment surface |
| `_LATEST.md` | snapshot / handoff artifact | live | Interim revision pointer during the session; becomes the genuine handoff-state record (accepted snapshot, closure verdict, blockers) at Gate 7 |
| `ScopeLedger.csv` | authoritative companion register | **live** (SOW→DEL mapping filled at Phase 5) | SOW→PKG→DEL→OBJ row-level ledger; authoritative for assignments |
| `Deliverables.csv` | authoritative companion register | **live** (Phase 5) | Deliverable register: full fields incl. descriptions, artifacts, Context Envelope + notes, PhaseHint |
| `ContextBudgetQA.csv` | authoritative companion register | **live** (Phase 6) | Per-deliverable envelope/risk/action QA |
| `Companion_Inventory.csv` | authoritative companion register | **live** (Phase 7) | Machine-readable mirror of this table |
