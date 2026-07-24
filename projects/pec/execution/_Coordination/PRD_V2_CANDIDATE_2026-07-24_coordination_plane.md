# PEC — Product Requirements Document

| | |
|---|---|
| **Version** | 2.0 — **CANDIDATE, not adopted** |
| **Date** | 2026-07-24 |
| **Status** | Candidate product definition awaiting owner review (`D-PEC-57` framing packet; adoption would be a `D-PEC-58` act) |
| **Product stage** | Prototype of the prior product exists (v0.4 baseline code); the coordination plane defined here is not yet implemented |
| **Supersession** | Upon adoption, supersedes PRD v1.0 ("team information hub", adopted 2026-07-10 by `D-PEC-55`). v1.0 remains preserved at its Git object, recorded in the adopting packet. The v0.4 catalogue remains preserved at `7e8312172:projects/pec/docs/PRD.md`. |

> **Epistemic status:** agent-authored candidate from owner-directed brainstorm
> (session 2026-07-24). Nothing in this document is an implementation mandate.
> Adoption converts it into the product definition of record only; each build
> tranche still requires its own owner-ruled packet.

---

## 1. Product definition

### 1.1 Thesis

PEC is the **coordination plane** of the Chirality operating system: a
deterministic, rebuildable projection of governed file truth, plus an
ephemeral presence layer, that embodies **Step 0 (Discover)** and the
deterministic parts of **Step 1 (gate review and decision-slate
presentation)** of the canonical development loop.

It is consumed by harnesses on behalf of agents, and by the human owner
through dashboards. It is the coordination plane that **does not need to
exist**: every consumer has a file-native fallback, and deleting PEC degrades
throughput, never correctness.

### 1.2 Chirality interpretation (adapted from v1.0 §1.2; first sentence verbatim)

Claims are not trustworthy merely because a person, import routine, or
language model stated them. PEC serves oriented work by making the derivation
of every presented value explicit and citable, and by keeping authority where
it already lives: in Git-tracked files and in the human owner's recorded acts.

### 1.3 What changed since v1.0

PRD v1.0 defined a team information hub for human discipline declarations. It
was adopted 2026-07-10 and never piloted; none of its §20 open product
decisions was answered. The owner's understanding of the user changed: the
user of this system is the owner plus a fleet of agents operating across
concurrent sessions, not a multidiscipline human team. This PRD supersedes
v1.0 for that reason — a change in the understood user, not a failure of the
v1.0 design. Sections of v1.0 that survive in spirit are listed in §14.

---

## 2. Problem

Chirality coordinates work through Git-tracked plain files by ruling
(`D-GOV-01`). This is correct and remains unchanged. But it has a measured
cost:

- **Step 0 is the most expensive, most repeated computation in the OS.**
  Every iteration of every loop re-derives the live lawful work surface from
  prose: >1,200 `_STATUS.md` files, ~230 decision records, receipts ledgers,
  workplans. Each derivation burns an LLM session, and the loop archives
  document the recurring failure mode: "a fluent draft grounded on stale
  facts."
- **Sessions cannot see each other.** Concurrent agents in different sessions
  coordinate today through files, Git collisions, and owner memory. Current
  guidance is literally to look away from other sessions' dirty files.
- **There is no join** between "a run happened" (daemon/user-data events,
  AgentRun records) and "a deliverable moved" (`_STATUS.md`, Git) other than
  prose written by hand.

The practitioner harness answers parts of this read-only per invocation. Its
plan reserved an optional cache half, gated on measured query pain; that
precondition was recorded **unmet** on 2026-07-02 (slowest command ~4 s) and
the cache half remains closed by the harness's own record. PEC v2 is a
separate tool addressing the same class of pain at OS scale (five loops,
concurrent sessions) — it does not open, direct, or replace the harness's
cache half, and Step-0 cost is re-measured before P1 (§11).

---

## 3. Product outcomes

1. Orientation for any loop is a sub-second query with per-claim citations,
   not a session-length prose derivation.
2. Staleness is detected structurally (SHA comparison), not by judgment.
3. Concurrent sessions have a declared, durable surface for presence and
   status — write-scope collisions are surfaced before they land in Git.
4. The human owner has one live view: loops, gates, lifecycle census,
   decisions waiting on them, and who (human or agent) is working where.
5. All of the above can be deleted at any moment without blocking any
   governed act.

---

## 4. Product boundary

### 4.1 PEC is

- A **rebuildable projection** of governed file truth (record tier).
- An **ephemeral presence registry** for sessions, worktrees, and live agent
  hierarchy (presence tier).
- A **deterministic evaluator** of gate preconditions (ruling presence, SHA
  reachability, receipt ancestry) — advisory, Explain-shaped, cited.
- A **renderer of decision slates** authored elsewhere.
- A **declared coordination surface** satisfying the doctrine that sibling
  agents use no hidden or undeclared messaging.

### 4.2 PEC is not (non-goals, permanent)

- **Not a system of record.** Files and Git remain the sole authority
  (`D-GOV-01`). PEC output is never citable as authority.
- **Not a ruling surface.** No write path records adoption, ruling, or
  direction. Rulings are file-native (K-AUTH-1).
- **Not an orchestrator.** No dispatch, no queues, no execution. The runtime
  daemon owns sessions, delegation, and turn locks (`D-GOV-20`); no second
  loop is created (`D-PEC-56` boundary preserved).
- **Not a lock manager.** No leases, no claim arbitration, no merge opinions.
  Conflicts are surfaced loudly and prevented never.
- **Not the practitioner harness's replacement.** The harness remains an
  independent deterministic checker; PEC parity-diffs against it permanently.
- **Not a Git actor.** Read-only plumbing access; CHANGE owns Git state.
- **Not a human project-management tool.** The v0.4/v1.0 product lineage
  (declarations, attestation, plan/capacity, EPC role homes) is retired.

---

## 5. Operating model — the modes ladder

PEC's consumption scales with the number of concurrent coordination contexts.
Modes that need nothing get nothing.

| Mode | Coordination contexts | PEC consumes | PEC produces | Posture |
|---|---|---|---|---|
| Pipeline (determined workflow; PDF2MD, DRAWING_EXTRACT, …) | 0 | nothing | progress/presence (push, optional) | out of the way |
| Conversation (no broader scope) | 1, unscoped | nothing | nothing | absent |
| Workbench (WORKING_ITEMS + TASK children, one package) | 1 per package | package-scoped orientation at activation | status, presence | useful |
| Agent 0, single (human-paired, cross-package) | 1 | loop-scoped orientation + deltas | status, presence, notices | efficiency; frees orchestrator context budget |
| Agent 1s, concurrent (disjoint scopes) | N | presence, fan-in views | status, presence | helpful; human bridges |
| Agent 0s, concurrent | N, overlapping scope | orientation, deltas, presence, notices | everything | **essential for throughput** (not for soundness — file fallback remains) |

The conversation→workbench transition is a polling event: orientation is
fetched when scope begins to exist, not at session start.

Doctrine note (future `AGENTS.md` amendment, not made by this PRD):
concurrent Agent 0 operation has no common parent below the human; a
declared, durable coordination surface is what makes it lawful under the
sibling-messaging rule. PEC is that surface.

---

## 6. Product invariants

| ID | Invariant |
|---|---|
| **PEC-K-01** | **Graceful absence.** No governed act may require a PEC read or write. Deleting PEC blocks nothing. The kill test (§12) passes at every release. |
| **PEC-K-02** | **Files govern.** The record tier is regenerated from sources by one command; the presence tier is expected to be lost on rebuild; the database is gitignored and safe to delete; PEC output is never citable as authority; rulings and lifecycle state remain file-native. |
| **PEC-K-03** | **Harness-owned consumption.** Polling is performed by harnesses at moments of consequence (session start, mode transition, claim, write, dispatch, fan-in) and injected as labeled non-authoritative data. The only agent behavior is verify-before-rely. |
| **PEC-K-04** | **Staleness is a comparison.** Every response carries the examined-through commit SHA and per-feed freshness; consumers detect staleness structurally. |
| **PEC-K-05** | **Two trust tiers, never blurred.** Record tier: reconciled from file truth, per-claim citations. Presence tier: TTL'd, heartbeat-aged, evaporating, honesty-labeled. Presence facts never enter record-tier citations. |
| **PEC-K-06** | **Observation, not participation.** Read-only over Git; no leases, no claim arbitration, no merge opinions, no dispatch; conflicts surfaced, never prevented. |
| **PEC-K-07** | **Ingest is best-effort; reconciliation is guaranteed.** Streams optimize freshness; the reconciler over file truth is the source of every record-tier fact. |
| **PEC-K-08** | **Everything derived is explainable.** Every status, verdict, and warning carries rule ID, threshold, and contributing cited sources. Drill-down never dead-ends. |
| **PEC-K-09** | **Declared surface.** Every coordination message is durable and attributable; no ephemeral relay. |
| **PEC-K-10** | **Content-minimal.** Paths, counts, SHAs, states, hashes — never file or diff content. |
| **PEC-K-11** | **Mode-proportional.** Consumption follows §5; zero-coordination modes remain zero-contact. |

Invariant lineage: PEC-K-02/-08 carry v1.0 PEC-I-01/-04 (factual-or-absent;
source and authority visible); PEC-K-08 also carries PEC-I-02 (one state,
many views: dashboards, API, and orientation project the same reconciled
snapshot); PEC-K-07 carries PEC-I-03 (coverage explicit); PEC-K-05/-09 carry
PEC-I-13 (agent work bounded and observable); PEC-K-06 carries PEC-I-12
(verification creates findings, never rewrites sources — cf. PEC-RCN-004);
the append-only discipline of v1.0 PEC-I-11 applies to PEC's own event log.

---

## 7. Information model

### 7.1 Record tier (reconciled from file truth; citable with sources)

| Entity | Purpose |
|---|---|
| Loop | Tenancy unit, above Project: a LOOP_INIT/workplan-governed work loop (root, app-dev, piping, pec, bridge, …) |
| Workplan / Step / Gate | The standing plan's protocol steps and owner gates, with gate state |
| Receipt | Parsed `LOOP_RECEIPTS.md` entries. Field availability is per-loop: the app-dev ledger carries the D-APP-57 contract (Receipt-ID, Examined-Through SHA, Parent-Receipt, Gate-Outcome); the pec/bridge ledgers are prose-structured with no validated schema — coverage limits stated per PEC-ORI-006 |
| DecisionRow | Register-row identity and status only (decision ID, packet path, anchor, state — never the row's prose; PEC-K-10) |
| Fence | Declared write-scope constraints from rulings and briefs |
| Package / Deliverable | Lifecycle census from `_STATUS.md` (OPEN→ISSUED), stuck-age, remaining items |
| DependencyEdge | From `Dependencies.csv` registers and `WORK_GRAPH.json` |
| RunRecord | Summaries of checkout-contained AgentRun evidence (`STATUS.json`, `RUNTIME_SUMMARY.json` under `execution/**`); runtime-daemon state under user data is operational and non-authoritative (D-GOV-20 §5), is never record-tier citable, and enters only the presence tier |
| CandidateBrief | Adopted-but-unexecuted and proposed briefs (the work-selection queue) |
| OrientationSnapshot | A generated orientation return, stamped with examined SHA — the machine generalization of a receipt |
| DriftFinding | A classified difference between the current reconcile and the prior snapshot, or between PEC and harness parity output |

### 7.2 Presence tier (operational; TTL'd; never citable)

| Entity | Purpose |
|---|---|
| Session | id, harness kind, engine/model attribution when known, role (Agent 0/1/2 or human), loop/package binding, last heartbeat |
| Worktree / GitRef | worktrees, branches, HEAD, ahead/behind, dirty path names and counts (never content) |
| PresenceRecord | session ↔ worktree ↔ declared write-scope correlation |
| HierarchyEdge | live parent→child session edges (the in-the-moment org chart) |
| ScopeClaim | advisory "working here" declarations; overlap detection input |

### 7.3 Prototype machinery carried as pattern (not as code)

Lifecycles-as-data transition tables; condition evaluation with
re-verification at evaluation time; `Explain<V>`-shaped derivation; SQL-level
append-only enforcement; dry-run-then-apply ingestion; coverage honesty
("a figure the records don't support is absent and said to be absent").

---

## 8. Users and access

- **Human owner** — dashboards, decision slate, presence board. Full read.
- **Harnesses** (runtime daemon; terminal-session hooks CLI) — machine
  consumers of the API on behalf of agent sessions; producers of presence and
  status events.
- **Agents** — never call PEC directly by instruction; they receive
  harness-injected orientation as labeled data (PEC-K-03).
- Access is local-only (Unix socket; any loopback listener is a §16 open
  decision), token-scoped. The v1.0 role ontology (12 roles, v1.0 §8) and
  the prototype's implemented 14-role RBAC set (`core/src/types.ts`) are
  retired; access classes are owner, harness, and admin.

---

## 9. Functional requirements

### 9.1 Orientation (PEC-ORI)

| ID | Requirement |
|---|---|
| PEC-ORI-001 | PEC shall serve, per loop: the newest applicable receipt, examined-through SHA, gate states, owner directions of record, open tranches/candidate briefs, and parked lanes each with the owner action that would unpark it. |
| PEC-ORI-002 | PEC shall serve deltas since a caller-supplied commit SHA. |
| PEC-ORI-003 | Every orientation response shall carry the examined-through SHA, generation time, and per-feed freshness. |
| PEC-ORI-004 | Every claim in an orientation response shall carry a citation (file path, anchor, and/or SHA) to its live source. |
| PEC-ORI-005 | Orientation shall be scope-parameterized (loop / project / package) per the modes ladder (§5). |
| PEC-ORI-006 | Where a feed is unparseable or stale, the response shall state the measurement limitation explicitly; silent omission is prohibited. |

### 9.2 Reconciliation (PEC-RCN)

| ID | Requirement |
|---|---|
| PEC-RCN-001 | The record tier shall be rebuildable in full from sources by one command; the presence tier is not reconstructible and is expected to be lost on rebuild (PEC-K-05); the database is gitignored and safe to delete (PEC-K-02). |
| PEC-RCN-002 | The reconciler shall ingest, at minimum: `_STATUS.md` (declared parser dialect), decision registers and packets, `LOOP_RECEIPTS.md` (per-loop grammar; the D-APP-57 contract where a ledger has adopted it), `WORK_GRAPH.json` / `STATUS.json` / `RUNTIME_SUMMARY.json`, dependency registers, workplans/LOOP_INIT, and per-project `_harness/adapter.yaml` as the feed manifest. |
| PEC-RCN-003 | Reconciliation shall run incrementally, keyed on Git delta since the last examined SHA. |
| PEC-RCN-004 | The reconciler shall classify drift between successive snapshots and report it; it shall never modify a source file. |
| PEC-RCN-005 | PEC derivations shall be parity-diffable against practitioner-harness output; discrepancies are surfaced as DriftFindings and resolved against live sources. |
| PEC-RCN-006 | The reconciler writes only its own store and generated views. |

### 9.3 Gate evaluation and decision slate (PEC-GAT)

| ID | Requirement |
|---|---|
| PEC-GAT-001 | PEC shall deterministically evaluate gate preconditions that reduce to file/Git facts: ruling presence, ruling-SHA commit reachability, receipt ancestry, snapshot/freeze presence, register-row status. |
| PEC-GAT-002 | Gate verdicts shall be Explain-shaped (rule, threshold, contributing citations) and advisory only. |
| PEC-GAT-003 | PEC shall render a cross-loop decision slate: every AWAITING_RULING row and every parked lane awaiting an owner act, linking to the authored file content rather than restating it. |
| PEC-GAT-004 | PEC shall provide no write path that records adoption, ruling, or direction (PEC-K-02; K-AUTH-1). |

### 9.4 Presence (PEC-PRS)

| ID | Requirement |
|---|---|
| PEC-PRS-001 | PEC shall record presence for sessions reported by their owning harness (harness kind, engine/model attribution when known, role, loop/package binding, declared write scopes); session identity and lifecycle remain daemon-owned (D-GOV-20). |
| PEC-PRS-002 | PEC shall scan Git for worktrees, branches, HEAD, ahead/behind counts, and dirty path names/counts; file and diff content shall never be captured (PEC-K-10). |
| PEC-PRS-003 | PEC shall correlate sessions to worktrees/branches (the session × worktree × scope join). |
| PEC-PRS-004 | PEC shall maintain live parent→child hierarchy edges from daemon and hook feeds. |
| PEC-PRS-005 | Presence records carry TTLs and last-heartbeat age; liveness shall never be asserted beyond last heartbeat. |
| PEC-PRS-006 | PEC shall detect and surface advisory overlaps (write scopes, shared branches, same merge target); it shall never block on them (PEC-K-06). |
| PEC-PRS-007 | Presence data is operational only and shall never appear in record-tier citations (PEC-K-05). |

### 9.5 Streams and ingest (PEC-STR)

| ID | Requirement |
|---|---|
| PEC-STR-001 | PEC shall accept idempotent, append-only event ingest keyed on event id. |
| PEC-STR-002 | Event contract types shall be versioned and consumable by daemon, hooks CLI, and adapters alike; their home (shared runtime contracts vs a PEC-local schema with a pinned mirror) is a cross-loop placement decision (§16) — writes into root `runtime/` are outside PEC's fences and require their own coordination. |
| PEC-STR-003 | Supported bridges: runtime-daemon SSE subscriber; harness hooks CLI (session start/stop, status, scope declaration); cmux socket adapter as an optional enricher. Each bridge is declared and attributable. |
| PEC-STR-004 | Stream loss is recovered by reconciliation; no record-tier fact may rest on a stream event alone (PEC-K-07). |
| PEC-STR-005 | Every ingested message is durable and queryable; PEC provides no ephemeral relay (PEC-K-09). |

### 9.6 API (PEC-API)

| ID | Requirement |
|---|---|
| PEC-API-001 | The service binds local-only, Unix socket by default, with token-scoped access; any loopback TCP listener is a §16 open decision in light of D-GOV-20's no-TCP-control-listener posture. |
| PEC-API-002 | Orientation reads shall complete in ≤100 ms at p95 against the current corpus (session-start critical path). |
| PEC-API-003 | The API schema is versioned; evolution is additive. |
| PEC-API-004 | Responses are compact, machine-first, and citation-bearing. |
| PEC-API-005 | PEC shall offer an SSE subscription for deltas and presence changes (dashboards; long-running managers). |

### 9.7 Dashboards (PEC-DSH)

| ID | Requirement |
|---|---|
| PEC-DSH-001 | Overview: the orientation return per loop (git state, newest receipt, gates that matter, open tranches, parked lanes + unparking act). |
| PEC-DSH-002 | Lifecycle census across all registered loops' packages/deliverables, with stuck-age and workflow-completeness views. |
| PEC-DSH-003 | Register views: decisions, receipts, dependencies, run records — read-only, link-only, source-linked (no restatement of authored text; PEC-K-10). |
| PEC-DSH-004 | "Waiting on you": the aggregated decision slate (PEC-GAT-003). |
| PEC-DSH-005 | Presence board: sessions × worktrees × live hierarchy, with heartbeat age and advisory overlap warnings. |
| PEC-DSH-006 | Every displayed value drills down to its cited source (PEC-K-08). |
| PEC-DSH-007 | Derived pressure/status rules (stuck-in-state age, gate-blocked, drift density, staleness, collision risk) are Explain-shaped and individually documented. |

---

## 10. Service requirements (PEC-SVC)

| ID | Requirement |
|---|---|
| PEC-SVC-001 | The service core has zero third-party runtime dependencies (carries ADR-002); workspace-internal runtime contracts packages are permitted. |
| PEC-SVC-002 | Local, single-owner posture; no external network egress. |
| PEC-SVC-003 | Full rebuild of the current corpus completes within a bound confirmed at Phase 1 (target: minutes); incremental reconcile within seconds. |
| PEC-SVC-004 | The kill test — delete the store, run representative governed workflows, nothing blocks — is a standing release gate (PEC-K-01). |
| PEC-SVC-005 | The store lives at a gitignored path; the content-minimal rule (PEC-K-10) is enforced at ingest. |
| PEC-SVC-006 | PEC's own reconcile runs and ingest activity are logged and inspectable (it is observable about itself). |

---

## 11. Success metrics (measured in system behavior, not human behavior)

1. Step-0 cost: LLM tokens per loop-iteration orientation, before vs after;
   the "before" baseline is measured before P1 begins (this also re-tests the
   query-pain precondition the practitioner harness recorded unmet on
   2026-07-02).
2. Orientation defect rate: claims failing source spot-check per 100 claims.
3. Collision incidents: write-scope/branch conflicts discovered at Git time
   rather than surfaced in advance, per week of concurrent operation.
4. Harness poll adoption: fraction of eligible session starts / mode
   transitions that consume orientation.
5. Parity: DriftFindings against practitioner-harness output per reconcile.
6. Kill test: pass, at every release.

**Falsification clause:** if, after Phase 3, harness poll adoption remains
negligible and the owner does not consult the dashboards, the product thesis
is falsified; PEC is deleted and, by PEC-K-01, nothing breaks.

---

## 12. Release strategy

| Phase | Scope | Exit test |
|---|---|---|
| **P0 — Governance** | `D-PEC-57` ruling; this PRD adopted (`D-PEC-58`); workplan replaced; decomposition authorized | Packets ruled; standing plan live |
| **P1 — One-loop reconciler** | Reconciler + orientation store + API for one loop (piping or root), read-only | Parity-diff vs harness clean or explained; rebuild-from-scratch ≤ bound; kill test passes |
| **P2 — Dashboards** | All five loops; Overview, census, registers, decision slate | Owner uses it in place of manual Step 0 for orientation reads |
| **P3 — Harness integration** | Hooks CLI + daemon polling; presence registry + Git/worktree scanner | Measured poll adoption; overlap warnings fire on seeded conflicts; falsification clause armed |
| **P4 — Streams** | Daemon SSE bridge; hooks push; live hierarchy tier; optional cmux adapter | Stream loss demonstrably recovered by reconcile; presence TTLs honest under kill/crash tests |

The PEC v2 build itself runs through the governed pipeline (SOFTWARE_DECOMP →
PROJECT_SETUP → WORKING_ITEMS), and the first loop the P1 reconciler ingests
is **its own build** — the bootstrap is the first validation of the thesis.

---

## 13. Prototype disposition

There is nothing to migrate: the v0.4-baseline application has no users, no
production data (scratch/demo only by ruling), and no dependents beyond a
scratch-only validation bridge.

| Surface | Disposition |
|---|---|
| `core/`, `server/`, `web/`, `agent-sidecar/`, `tools/` | Frozen as reference implementation; quarried by citation in deliverable briefs; archived from the working tree once P2 is useful. Never deleted (v1.0 I-11 spirit; Git preserves regardless). |
| SPEC / TRACEABILITY / PILOT / ADR-001..014 | Historical baseline retained with existing disclaimers; v2 SPEC is born from the decomposition; live postures (ADR-002, ADR-014) re-cited in v2's first ADRs. |
| Decision register D-PEC-01..56 | Continues (numbering never resets; historical row gaps predate this PRD). `D-PEC-49` closed as moot at the D-PEC-58 gate. |
| Domain-engine registration (`pec.yaml`, L3 import lane) | L3 operation-proposal lane sunset with the old product; profile superseded when v2 has shape; the `_DomainEngines/pec` loop continues as the governing development loop. |
| Demo DB, fixtures, seed/drill tooling | Retired; scratch-guard discipline carries as a pattern. |
| Tests (347 per the receipt-sourced breakdown: 74 core / 169 server / 104 sidecar) | Retired with the product; invariant-test style and server test-harness pattern carry as conventions. |
| Shared-runtime client seam (D-PEC-56) | Concept carries directly; reimplemented against v2 entities. |
| `chirality.project.json`, daemon registration, project identity | Continue unchanged. |

Machinery carried **as pattern, not code**: §7.3 list, with briefs citing the
specific reference modules.

---

## 14. Supersession and carry-forward

Upon adoption:

- PRD v1.0 is superseded and preserved at its Git object (recorded in the
  adopting packet), exactly as v0.4 is preserved at `7e8312172`.
- Carried forward in spirit: v1.0 §1.2 (Chirality interpretation, adapted at
  §1.2 above; first sentence retained verbatim); invariants
  PEC-I-01/-02/-03/-04/-11/-12/-13 (each mapped at §6);
  the information-model discipline of §9; the verification/reporting
  machinery concepts of §10.4/§10.9 (reborn as PEC-RCN/PEC-DSH); coverage
  honesty (§5.3/§6) as PEC-ORI-006.
- Retired: v1.0 §5 (declarations, attestation), §10.1–10.3, §10.8, §8/§12
  role ontology, §13 integrations, §15 metrics, §16 phases. Any v1.0 section
  not named in the carried-forward list above is retired by default; the
  carry list is exhaustive.
- **No identifier is reused.** v2 identifiers are `PEC-K-*` (invariants) and
  `PEC-{ORI,RCN,GAT,PRS,STR,API,DSH,SVC}-NNN` (requirements); no family
  overlaps v1.0 or v0.4, so a bare ID is always unambiguous.

---

## 15. Governance and compliance posture

- **`D-GOV-01` — complied with by design for the record tier; one question
  expressly reserved for the owner.** Option A's sanctioning clause — "a
  rebuildable, gitignored projection: safe to delete, regenerated from files
  by one command, never cited as authority" — is encoded as PEC-K-01/-02.
  The same ruled option also states: "No coordinator process, no leases, no
  database-owned status, no CLI-owned governance writes." PEC takes no
  leases (PEC-K-06), owns no governance status (rulings and lifecycle remain
  file-native, PEC-K-02), and writes no governance surface. The presence
  tier is operational-only, TTL'd, non-authoritative, and never citable.
  Whether a persistent presence service falls within Option A's "no
  coordinator process" clause is presented to the owner at `D-PEC-58`, not
  settled by this document.
- **`D-GOV-20` — complemented.** The daemon remains sole owner of execution;
  PEC creates no second loop and holds no session authority.
  Checkout-contained evidence remains authoritative over any PEC store.
- **`D-PEC-56` — partially superseded upon adoption.** Its ruled behavior 1
  (retain PEC's deterministic acts, RBAC, reporting, and domain tools as a
  project adapter service) does not survive the product retirement in
  §8/§13. Its no-dual-loop boundary (behavior 4) and human-only-act
  restrictions (behavior 7) survive unchanged. The partial supersession is
  declared in the `D-PEC-58` packet.
- **Doctrine** — the sibling rule prohibits hidden or undeclared direct
  messaging under a mediating parent (`AGENTS.md`); PEC is a declared,
  durable, recorded surface and therefore not hidden messaging. Whether
  concurrent Agent 0 operation without a common parent is lawful is an open
  `AGENTS.md` question, flagged at §5 and not resolved by this PRD.
- **Residency** — content-minimal (PEC-K-10): PEC indexes only repo files
  agents already read, plus operational presence; no new data class egresses.
- **Fences** — this candidate is authored within currently lawful write
  scope. All implementation writes await their own packets.
- The practitioner harness's cache half remains closed by its own record
  (`tools/practitioner_harness/README.md` §Cache contract): its query-pain
  precondition was measured **unmet** on 2026-07-02 (slowest command ~4 s).
  A `D-PEC-57`/`D-PEC-58` ruling directs the PEC product; it neither directs
  the harness nor remeasures that precondition. §11 metric 1 re-measures
  Step-0 cost before P1.

---

## 16. Open product decisions (owner)

1. Whether decision registers gain light structure at source (machine-parse
   aids) or remain prose parsed best-effort.
2. Design and ownership of a daemon global event feed (today: per-session
   SSE only).
3. Home and shape of the loop registry (which loops PEC serves; today five).
4. Long-term placement: `projects/pec` retained now; root promotion (the
   `runtime/` precedent) explicitly deferred, not decided here.
5. Whether the PEC web UI eventually folds into the desktop app or remains a
   standalone local page.
6. Auth reuse: PEC tokens vs the daemon's project-scoped token registry.
7. Whether "PEC" is re-expanded (e.g., Project Execution *Coordination*) or
   kept as a legacy name.
8. Whether non-app-dev loop ledgers adopt the D-APP-57 receipt contract
   (today only the app-dev ledger is schema-validated; pec/bridge are
   prose-structured).
9. Event-contract home (shared `runtime/packages/contracts` vs a PEC-local
   schema with a pinned mirror) and API transport (Unix socket only vs an
   additional loopback listener, given D-GOV-20's no-TCP-control-listener
   posture).

None of these blocks P0–P2.

---

## 17. Owner statement

*(Reserved for the owner at adoption.)*
