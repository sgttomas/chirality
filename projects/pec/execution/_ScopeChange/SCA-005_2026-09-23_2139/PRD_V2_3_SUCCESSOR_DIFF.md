---
amendment: SCA-005
doc_kind: scope_change.prd_successor_diff
status: candidate_awaiting_checkpoint_2
prepared: 2026-09-25
prepared_by: TASK drafter T1 under WORKING_ITEMS B2, HELP_HUMAN run HELP-HUMAN-PEC-20260923-SCA005
candidate: CP2_CANDIDATE/docs/PRD.md
preimage: projects/pec/docs/PRD.md (v2.2)
preimage_sha256: 6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba
d_pec_79_postimage: projects/pec/execution/_Coordination/PRD_V23_SECTION16_3_EXACT_POSTIMAGE_2026-08-09/PRD_V2_3_CANDIDATE_POSTIMAGE.md
d_pec_79_postimage_sha256: 92627ee1d384dd8ef0f2db5d63362ec54eee9da30794b9c2d776bd46fb20f5b0
candidate_sha256: fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32
---

# PRD v2.3 successor candidate — section-by-section diff against live v2.2

This is a checkpoint-2 candidate for SCA-005. It applies nothing: live
`projects/pec/docs/PRD.md` stays v2.2 at the preimage hash above until the
owner accepts checkpoint group 2 and a separately authorized application
writes the candidate bytes. The adopted `D-PEC-79` postimage stays preserved,
unchanged, as historical exact input (CP1-D79 option (b)).

## 1. Identities

| Artifact | Path | SHA-256 |
|---|---|---|
| Preimage (live PRD v2.2) | `projects/pec/docs/PRD.md` | `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba` |
| D-PEC-79 adopted postimage (not applied) | `projects/pec/execution/_Coordination/PRD_V23_SECTION16_3_EXACT_POSTIMAGE_2026-08-09/PRD_V2_3_CANDIDATE_POSTIMAGE.md` | `92627ee1d384dd8ef0f2db5d63362ec54eee9da30794b9c2d776bd46fb20f5b0` |
| Successor candidate (this package) | `projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139/CP2_CANDIDATE/docs/PRD.md` | `fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32` |

> **Manager repair (B2, verifier cycle 1, 2026-09-25):** PEC-API-001 and §16.9 now read "D-GOV-43 A2 (no network-exposed listener), superseding D-GOV-20 item 4" (D-GOV-43 L73 supersedes D-GOV-20 items 2–4; the A2 supplement introduces no network-exposed listener), and the §2 closing paragraph is rewrapped. The candidate hash above is the repaired value; the drafter's pre-repair hash was `4e7c8fa0…c009`. Hunk headers after the §2 hunk keep the drafter's line numbers; the candidate file and its SHA-256 are authoritative.

The candidate hash is recorded here because it cannot appear inside the
candidate. Any change to an acceptance-bound slot (§6) changes this hash;
the applied file's hash is re-measured at the owner's act.

## 2. Basis

- Accepted Impact Assessment `Impact_Assessment.md` (SHA-256 `0bcbe9bd…39bf`), Annex B (INV-001..036), §8.3, §12.
- Accepted intake `Amendment_Actions.csv` (SHA-256 `5c4ae053…f2be2`) Seq 75 and 76, as narrowed by the group-1 acceptance (Q10 (a): the "§12 P1 (Q10 c)" element is dropped) and extended by amendment 1 (PEC-STR-003 and §12 P4 record the cmux adapter as deferred; INV-020 becomes "daemon and cmux bridges deferred; hooks CLI stays").
- Group-1 snapshot `checkpoint_snapshots/SCA-005_GROUP-1_2026-09-24/` and amendments 1 and 2; checkpoint-1 resolution note (SHA-256 `af4e46d0…0ad2`): Q1 O-B2, Q2 (b), Q3 P-β, CP1-R R1, Q4 (a), Q6 re-express with decisions open, Q7 (b), Q9 no change, Q10 (a), CP1-D79 (b), CP1-V.
- A2 inventory `IMPACT_INVENTORY_PEC_BASIS.csv` rows INV-001..036; design note `FEED_MODEL_V2_DESIGN_NOTE.md` §3–§5; A1 survey DR-02, DR-03, DR-08..DR-10.
- `D-PEC-90` ruling and `Decision_Log.md` row SCA005-D90-NOTE: keep the v2.2 meaning where §8 or orientation text is touched; add no reliance text.
- B2 shared drafting spec (canonical phrasings: runtime topology, trigger T-RT, cmux deferral, feed kinds 1–9, "strict, versioned", registry-relative loop wording).

## 3. Hunks in PRD order

Each hunk shows v2.2 (`-`) against the candidate (`+`); line numbers are v2.2 and candidate lines. Provenance labels are those the candidate's own successor provenance block assigns.

### Header table

#### SH-01 — header rows

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| D-PEC-79 hunk 1 (Version carried; Date and Status rewritten for the successor's adoption instrument); CP1-D79 (b) | header — acceptance record | — | Version row byte-identical to D-PEC-79; Date and Status carry acceptance-bound slots |

```diff
@@ -5,3 +5,3 @@
-| **Version** | 2.2 |
-| **Date** | 2026-07-27 |
-| **Status** | **Adopted 2026-07-27** by owner ruling (`D-PEC-68`); v2.0 adopted by `D-PEC-58`; directed-bootstrap clarification adopted as v2.1 by `D-PEC-61`; exact PEC-K-03/-11 rows adopted by `D-PEC-67`; consumer-interface concordance adopted as v2.2 by `D-PEC-68`; product definition of record |
+| **Version** | 2.3 |
+| **Date** | 2026-09-25 |
+| **Status** | **Adopted 2026-09-25** by owner acceptance of SCA-005 checkpoint group 2 (`execution/_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-2_2026-09-25/`); v2.0 adopted by `D-PEC-58`; directed-bootstrap clarification adopted as v2.1 by `D-PEC-61`; exact PEC-K-03/-11 rows adopted by `D-PEC-67`; consumer-interface concordance adopted as v2.2 by `D-PEC-68`; §16.3 loop-registry disposition concordance adopted as exact v2.3 candidate bytes by `D-PEC-79` (not separately applied; carried into this successor); SCA-005 feed-model, presence and runtime-topology concordance adopted with this successor; product definition of record |
```

### Epistemic status

#### SH-02 — epistemic status

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| D-PEC-79 hunk 2 (rewritten for the successor's adoption instrument); CP1-D79 (b) | header — acceptance record | — | D-PEC-79 lineage kept, restated as adopted-not-applied; successor adoption path named |

```diff
@@ -15,2 +15,8 @@
-> concordance on 2026-07-27 (`D-PEC-68`). Adoption makes a PRD the product
-> definition of record only — nothing in this document is an implementation
+> concordance on 2026-07-27 (`D-PEC-68`). A v2.3 candidate reconciling §16.3
+> to D-PEC-78 O-A and accepted SCA-004 decomposition truth was adopted as
+> exact bytes on 2026-08-09 (`D-PEC-79`) but not applied; this successor
+> v2.3 carries those changes and was adopted on 2026-09-25 by owner
+> acceptance of SCA-005 checkpoint group 2, which also reconciles the feed,
+> presence and runtime-topology premises to current file truth. Adoption
+> makes a PRD the product definition of record only — nothing in this
+> document is an implementation
```

### Provenance labels

#### SH-03 — provenance blocks

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| D-PEC-79 hunk 3 (carried byte-identical) + successor block (CP1-D79 (b)) | D-PEC-79 block as adopted; successor block defines SCA-005 labels | — | new block uses TRANSCRIBED / CLARIFIED / PROPOSED |

```diff
@@ -27,4 +33,30 @@
 > and 15 are `CLARIFIED`; the resulting P3/P4 capability-exit wording is
 > `PROPOSED`.

+> **v2.3 provenance labels:** the §16 heading and closing sentence are
+> `CLARIFIED` to distinguish the remaining open decisions from resolved item
+> 3. The §16.3 disposition is `TRANSCRIBED` from D-PEC-78 O-A and the accepted
+> SCA-004 revision-1.4 meaning; it creates no new product meaning and changes
+> no decomposition, source, configuration, consumer, lifecycle, or release
+> authority.
+
+> **v2.3 successor provenance labels (SCA-005):** the block above is carried
+> from the `D-PEC-79` exact candidate, whose adopted bytes remain preserved
+> as historical exact input. In this successor `PROPOSED` means product text
+> adopted through the SCA-005 checkpoint-group-2 owner gate. The §16.3
+> registry wording "strict, versioned" and its schema-version path are
+> `TRANSCRIBED` from D-PEC-78 O-A (confirmed at SCA-005 checkpoint 1 as a
+> supplementary extension, not a supersession); the §16.3 feed-profile
+> clause is `PROPOSED`. The runtime-topology and citation refreshes in §§2,
+> 4.2, 8, 9.4 (PEC-PRS-001), 9.5 (PEC-STR-002), 9.6, 13 (domain-engine and
+> `chirality.project.json` rows) and 15, the registry-relative loop wording
+> in §§2 and 12 (P2), and the premise re-expressions of §§16.2, 16.6, 16.8
+> and 16.9 are `CLARIFIED` to D-GOV-43 A2, D-PEC-78 O-A and observed file
+> truth; those four decisions stay open. The §7.1 record-tier entity rows,
+> PEC-ORI-001, PEC-RCN-002, and the deferrals in PEC-PRS-004, PEC-STR-003,
+> §12 P4 and the §13 client-seam row are `PROPOSED`, their substance
+> selected at SCA-005 checkpoint 1 and its amendment 1. None of these
+> changes creates an implementation mandate, a receiving-loop duty, or a
+> source, configuration, consumer, lifecycle, or release authority.
+
 ---
```

### §2 Problem

#### SH-04 — §2 bullet 3

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| INV-002 | CLARIFIED | — | daemon/user-data events -> Runtime service events; adds receipts and work graphs |

```diff
@@ -82,3 +114,3 @@
-- **There is no join** between "a run happened" (daemon/user-data events,
-  AgentRun records) and "a deliverable moved" (`_STATUS.md`, Git) other than
-  prose written by hand.
+- **There is no join** between "a run happened" (application-owned Runtime
+  service events, AgentRun records, central receipts, work graphs) and "a
+  deliverable moved" (`_STATUS.md`, Git) other than prose written by hand.
```

#### SH-05 — §2 closing paragraph

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| INV-003 (Seq 54 coherence) | CLARIFIED | — | registry-relative loop wording; Step-0 re-measure clause (Q9) untouched |

```diff
@@ -90,3 +122,4 @@
-separate tool addressing the same class of pain at OS scale (five loops,
-concurrent sessions) — it does not open, direct, or replace the harness's
-cache half, and Step-0 cost is re-measured before P1 (§11).
+separate tool addressing the same class of pain at OS scale (the loops the
+loop registry lists, §16.3; concurrent sessions) — it does not open,
+direct, or replace the harness's cache half, and Step-0 cost is re-measured
+before P1 (§11).
```

### §4.2 PEC is not

#### SH-06 — §4.2 Not an orchestrator

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| INV-004 (Seq 26 / C13 coherence) | CLARIFIED | — | canonical runtime-topology phrasing |

```diff
@@ -130,3 +162,5 @@
-- **Not an orchestrator.** No dispatch, no queues, no execution. The runtime
-  daemon owns sessions, delegation, and turn locks (`D-GOV-20`); no second
+- **Not an orchestrator.** No dispatch, no queues, no execution. Sessions,
+  delegation, and turn admission are owned per application by its
+  application-owned Runtime service (one private Runtime per application;
+  `D-GOV-43` A2, superseding `D-GOV-20` items 2–4 on that path); no second
   loop is created (`D-PEC-56` boundary preserved).
```

### §7.1 Record tier

#### SH-07 — §7.1 Loop

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| INV-005 (Seq 1, Seq 6) | PROPOSED | — | registry-relative; LOOP_INIT identity only |

```diff
@@ -203,1 +237,1 @@
-| Loop | Tenancy unit, above Project: a LOOP_INIT/workplan-governed work loop (root, app-dev, piping, pec, bridge, …) |
+| Loop | Tenancy unit, above Project: a `LOOP_INIT.md`-governed work loop that the loop registry lists (§16.3); PEC reads only loop identity, entrypoint and procedure SHA from `LOOP_INIT.md` |
```

#### SH-08 — §7.1 Workplan / Step / Gate

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| INV-006 (Seq 1, Seq 6) | PROPOSED | — | declared historical-grammar entity; gate state re-sourced |

```diff
@@ -204,1 +238,1 @@
-| Workplan / Step / Gate | The standing plan's protocol steps and owner gates, with gate state |
+| Workplan / Step / Gate | Declared historical-grammar entity: workplans are indexed as history only; gate state is re-sourced from decision registers, scope-change pointers and work-graph `BLOCKED` nodes, never read from `LOOP_INIT.md` |
```

#### SH-09 — §7.1 Receipt

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| INV-007 (Seq 1, Seq 3) | PROPOSED | — | two grammar generations of one Receipt feed kind; receipt-contract-v2 marker |

```diff
@@ -205,1 +239,1 @@
-| Receipt | Parsed `LOOP_RECEIPTS.md` entries. Field availability is per-loop: the app-dev ledger carries the D-APP-57 contract (Receipt-ID, Examined-Through SHA, Parent-Receipt, Gate-Outcome); the pec/bridge ledgers are prose-structured with no validated schema — coverage limits stated per PEC-ORI-006 |
+| Receipt | Parsed `LOOP_RECEIPTS.md` ledger entries and central `execution/_Coordination/AgentRuns/<RunID>/RECEIPT.md` receipts — two grammar generations of one Receipt feed kind; each ledger is live or declared historical per its loop's feed profile. Field availability is per-loop and per-grammar: ledgers carrying the `receipt-contract-v2` marker share one validated field set (Receipt-ID, Examined-Through SHA, Parent-Receipt, Gate-Outcome); other ledgers and central receipts have no shared validated schema — coverage limits stated per PEC-ORI-006 |
```

#### SH-10 — §7.1 Package / Deliverable

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| INV-008 (Seq 1) | PROPOSED | — | remaining items becomes a per-loop optional field |

```diff
@@ -208,1 +242,1 @@
-| Package / Deliverable | Lifecycle census from `_STATUS.md` (OPEN→ISSUED), stuck-age, remaining items |
+| Package / Deliverable | Lifecycle census from `_STATUS.md` (OPEN→ISSUED), stuck-age; remaining items is a per-loop optional field, read only where the loop's feed profile declares it |
```

#### SH-11 — §7.1 DependencyEdge

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| INV-009 (Seq 5) | PROPOSED | — | WORK_GRAPH.json declared historical; work-graph dependencies |

```diff
@@ -209,1 +243,1 @@
-| DependencyEdge | From `Dependencies.csv` registers and `WORK_GRAPH.json` |
+| DependencyEdge | From `Dependencies.csv` registers and work-graph dependencies (WorkGraph); `WORK_GRAPH.json` is read as a declared historical grammar where the loop's feed profile says so |
```

#### SH-12 — §7.1 RunRecord

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| INV-010 (Seq 1, Seq 4, Seq 9) | PROPOSED | — | RunRecord re-sourced; runtime user-data never an input (v2.2 'enters only the presence tier' dropped under P-β) |

```diff
@@ -210,1 +244,1 @@
-| RunRecord | Summaries of checkout-contained AgentRun evidence (`STATUS.json`, `RUNTIME_SUMMARY.json` under `execution/**`); runtime-daemon state under user data is operational and non-authoritative (D-GOV-20 §5), is never record-tier citable, and enters only the presence tier |
+| RunRecord | Summaries of checkout-contained AgentRun evidence, joined on the declared run-identity token from central receipts, work graphs and the deliverable `MEMORY.md` run index; `STATUS.json` / `RUNTIME_SUMMARY.json` under `execution/**` are read as declared historical grammar or current evidence per the loop's feed profile; application-owned Runtime service user-data is operational and non-authoritative (D-GOV-20 item 5; D-GOV-43 A2), is never an input, and is never record-tier citable |
```

#### SH-13 — §7.1 WorkGraph / WorkNode (new row)

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| Seq 1 (SOW-001 adds the entity); coherence with INV-010 / INV-015 — **FLAGGED for the manager** | PROPOSED | — | only added row in the candidate; no new requirement ID |

```diff
@@ -213,1 +247,2 @@
 | DriftFinding | A classified difference between the current reconcile and the prior snapshot, or between PEC and harness parity output |
+| WorkGraph / WorkNode | A loop's undertaking graph `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md` and its nodes, discovered per the loop's feed profile and read content-minimally (declared run-identity token, node IDs, closed-vocabulary node states, DEL bindings, PR numbers, hex SHAs, linked paths, per-state counts); a node state is declared activity, never a liveness assertion; terminal completion is derived from local Git merge reachability of cited PRs |
```

### §8 Users and access

#### SH-14 — §8 Harnesses

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| INV-013 (Seq 55) | CLARIFIED | D-PEC-90: v2.2 meaning kept; Agents bullet, access classes and PEC-K-03 untouched; no reliance or direct-query text added | Runtime service named per Seq 55; event production limited to the hooks CLI (P-β) |

```diff
@@ -237,3 +272,6 @@
-- **Harnesses** (runtime daemon; terminal-session hooks CLI) — permitted
-  machine consumers of the API on behalf of agent sessions when explicitly
-  enabled under their own authority; producers of presence and status events.
+- **Harnesses** (an application-owned Runtime service, one private Runtime
+  per application under `D-GOV-43` A2; terminal-session hooks CLI) —
+  permitted machine consumers of the API on behalf of agent sessions when
+  explicitly enabled under their own authority; the hooks CLI is also a
+  producer of presence and status events (Runtime-sourced events are
+  deferred, PEC-STR-003).
```

### §9.1 Orientation

#### SH-15 — PEC-ORI-001

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| INV-014 (Seq 2; Q4 (a)) | PROPOSED | D-PEC-90: row speaks of sources only; no reliance text; verify-before-rely (PEC-K-03) stands | feed-profile qualifier on graph nodes is an interpretation (see ambiguities) |

```diff
@@ -257,1 +295,1 @@
-| PEC-ORI-001 | PEC shall serve, per loop: the newest applicable receipt, examined-through SHA, gate states, owner directions of record, open tranches/candidate briefs, and parked lanes each with the owner action that would unpark it. |
+| PEC-ORI-001 | PEC shall serve, per loop: the newest applicable receipt (over central receipts and ledgers), examined-through SHA, gate states (from decision registers, scope-change state and work-graph `BLOCKED` nodes), owner directions of record, open tranches/candidate briefs and parked lanes (over work-graph `READY`/`ACTIVE`/`BLOCKED` nodes where the loop's feed profile declares work graphs) each with the owner action that would unpark it, and terminal completion derived from local Git merge reachability of cited PRs (Explain-cited, advisory). |
```

### §9.2 Reconciliation

#### SH-16 — PEC-RCN-002

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| INV-015 (Seq 3–10; Q1 O-B2, Q2 (b), Q7 (b), CP1-X) | PROPOSED | — | feed kinds 1–9 of the shared spec; manifest clause moves to registry feed profiles |

```diff
@@ -269,1 +307,1 @@
-| PEC-RCN-002 | The reconciler shall ingest, at minimum: `_STATUS.md` (declared parser dialect), decision registers and packets, `LOOP_RECEIPTS.md` (per-loop grammar; the D-APP-57 contract where a ledger has adopted it), `WORK_GRAPH.json` / `STATUS.json` / `RUNTIME_SUMMARY.json`, dependency registers, workplans/LOOP_INIT, and per-project `_harness/adapter.yaml` as the feed manifest. |
+| PEC-RCN-002 | The reconciler shall ingest, per the closed, PEC-versioned feed profile declared on each loop-registry row (§16.3; PEC's reading hypothesis, never the loop's truth), at minimum: `_STATUS.md` (declared parser dialect); decision registers and packets (row identity and status only); receipts — `LOOP_RECEIPTS.md` ledgers (per-loop grammar; the `receipt-contract-v2` marker where a ledger carries it; live or declared historical per profile) and central `execution/_Coordination/AgentRuns/<RunID>/RECEIPT.md`; run evidence — deliverable `MEMORY.md` run-index entries as RunRecord join evidence, with `STATUS.json` / `RUNTIME_SUMMARY.json` as declared historical grammar or current evidence per profile; dependency registers (`Dependencies.csv`; `WORK_GRAPH.json` as declared historical grammar); work graphs `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md` (content-minimal; integration ref by default, local branch refs opt-in and labelled unintegrated; cited PR numbers resolved to local merge commits by read-only plumbing, reported when unresolved locally, never guessed); and `LOOP_INIT.md` loop identity, entrypoint and procedure SHA only (workplans as declared historical grammar). Per-project `_harness/adapter.yaml` is a parity-peer input only, read to compare PEC's declared census population with the harness `status_glob` (divergence is a DriftFinding); it is not the feed manifest. |
```

### §9.4 Presence

#### SH-17 — PEC-PRS-001

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| INV-017 (Seq 28) | CLARIFIED | — | sessions only from an explicitly authorized hooks consumer |

```diff
@@ -288,1 +326,1 @@
-| PEC-PRS-001 | PEC shall record presence for sessions reported by their owning harness (harness kind, engine/model attribution when known, role, loop/package binding, declared write scopes); session identity and lifecycle remain daemon-owned (D-GOV-20). |
+| PEC-PRS-001 | PEC shall record presence for sessions reported by an explicitly authorized hooks consumer (harness kind, engine/model attribution when known, role, loop/package binding, declared write scopes); session identity and lifecycle remain owned per application by its application-owned Runtime service (one private Runtime per application; D-GOV-43 A2). |
```

#### SH-18 — PEC-PRS-004

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| INV-018 (Seq 29; Q3 P-β, CP1-R R1) | PROPOSED | — | Deferred, trigger T-RT (canonical text) |

```diff
@@ -291,1 +329,1 @@
-| PEC-PRS-004 | PEC shall maintain live parent→child hierarchy edges from daemon and hook feeds. |
+| PEC-PRS-004 | PEC shall maintain live parent→child hierarchy edges from a Runtime-sourced feed only once trigger T-RT fires. **Deferred, not permanent** — trigger T-RT: a Runtime-owning loop publishes, under its own authority, an observation interface usable by a non-owning local reader, and `_DomainEngines/profiles/pec.yaml` is amended, and a D-PEC packet names the bridge. PEC can neither request nor require that interface. |
```

### §9.5 Streams

#### SH-19 — PEC-STR-002

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| INV-019 (Seq 32; amendment-1 'hooks CLI only') | CLARIFIED | — | contract-home option path projects/chirality-runtime/packages/contracts |

```diff
@@ -301,1 +339,1 @@
-| PEC-STR-002 | Event contract types shall be versioned and consumable by daemon, hooks CLI, and adapters alike; their home (shared runtime contracts vs a PEC-local schema with a pinned mirror) is a cross-loop placement decision (§16) — writes into root `runtime/` are outside PEC's fences and require their own coordination. |
+| PEC-STR-002 | Event contract types shall be versioned and consumable by the hooks CLI, the only remaining bridge (PEC-STR-003); their home (the Runtime loop's shared contracts at `projects/chirality-runtime/packages/contracts` vs a PEC-local schema with a pinned mirror) is a cross-loop placement decision (§16) — writes into `projects/chirality-runtime/**` (root `runtime/` relocated, PR #727) are outside PEC's fences and require their own coordination. |
```

#### SH-20 — PEC-STR-003 (+ amendment 1 cmux)

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| INV-020 (Seq 30) + amendment-1 (Seq 75 extension, Seq 77) | PROPOSED | — | daemon and cmux bridges deferred; hooks CLI stays (INV-020 as amended) |

```diff
@@ -302,1 +340,1 @@
-| PEC-STR-003 | Supported bridges: runtime-daemon SSE subscriber; harness hooks CLI (session start/stop, status, scope declaration); cmux socket adapter as an optional enricher. Each bridge is declared and attributable. |
+| PEC-STR-003 | Supported bridge: the harness hooks CLI (session start/stop, status, scope declaration), the only remaining bridge. Each bridge is declared and attributable. An application-owned Runtime service SSE subscriber (formerly the runtime-daemon SSE subscriber) is **Deferred, not permanent** — trigger T-RT: a Runtime-owning loop publishes, under its own authority, an observation interface usable by a non-owning local reader, and `_DomainEngines/profiles/pec.yaml` is amended, and a D-PEC packet names the bridge. PEC can neither request nor require that interface. The cmux socket adapter is **Deferred, not permanent** — re-entry only by a later owner direction (owner 2026-09-24: no plans for cmux compatibility). |
```

### §9.6 API

#### SH-21 — PEC-API-001

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| INV-021 (Seq 27 / C5 coherence) | CLARIFIED | — | citation refresh; substance unchanged |

```diff
@@ -310,1 +348,1 @@
-any loopback TCP listener is a §16 open decision in light of D-GOV-20's no-TCP-control-listener posture. |
+any loopback TCP listener is a §16 open decision in light of D-GOV-43 A2 (no network-exposed listener), superseding D-GOV-20 item 4. |
```

### §12 Release strategy

#### SH-22 — §12 P2

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| INV-025 (Seq 54 coherence) | CLARIFIED | — | registry-relative P2 scope; exit test unchanged |

```diff
@@ -375,1 +413,1 @@
-| **P2 — Dashboards** | All five loops; Overview, census, registers, decision slate |
+| **P2 — Dashboards** | The loops the loop registry lists (§16.3); Overview, census, registers, decision slate |
```

#### SH-23 — §12 P4 (+ amendment 1 cmux)

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| INV-026 + amendment-1 (Seq 75 extension) | PROPOSED | — | P4 narrowed; exit test unchanged |

```diff
@@ -377,1 +415,1 @@
-| **P4 — Streams** | PEC-side daemon SSE bridge and optional hook-push interface; live hierarchy tier; optional cmux adapter; live use requires separately authorized receiving consumers |
+| **P4 — Streams** | PEC-side optional hook-push interface; live use requires separately authorized receiving consumers. The Runtime SSE bridge and live hierarchy tier are deferred (trigger T-RT, PEC-PRS-004); the cmux adapter is deferred (re-entry only by a later owner direction, PEC-STR-003) |
```

### §13 Prototype disposition

#### SH-24 — §13 domain-engine row

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| INV-028 | CLARIFIED | — | loop path refresh only |

```diff
@@ -414,1 +452,1 @@
-profile superseded when v2 has shape; the `_DomainEngines/pec` loop continues as the governing development loop. |
+profile superseded when v2 has shape; the PEC loop at `projects/pec/loop/` (relocated from `_DomainEngines/pec`) continues as the governing development loop. |
```

#### SH-25 — §13 client-seam row

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| INV-029 (Seq 31) | PROPOSED | — | D-PEC-56 concept kept as lineage; client deferred (T-RT) |

```diff
@@ -417,1 +455,1 @@
-| Shared-runtime client seam (D-PEC-56) | Concept carries directly; reimplemented against v2 entities. |
+| Shared-runtime client seam (D-PEC-56) | Concept retained as historical lineage; a per-application Runtime client is **Deferred, not permanent** — trigger T-RT: a Runtime-owning loop publishes, under its own authority, an observation interface usable by a non-owning local reader, and `_DomainEngines/profiles/pec.yaml` is amended, and a D-PEC packet names the bridge. PEC can neither request nor require that interface. |
```

#### SH-26 — §13 chirality.project.json row

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| INV-030 (Seq 45) | CLARIFIED | — | daemon registration retired |

```diff
@@ -418,1 +456,1 @@
-| `chirality.project.json`, daemon registration, project identity | Continue unchanged. |
+| `chirality.project.json`, project identity | Continue unchanged; daemon registration retired with the per-user daemon (`D-GOV-43`). |
```

### §15 Governance posture

#### SH-27 — §15 D-GOV-20 bullet

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| INV-031 (Seq 26) | CLARIFIED | — | no-second-loop boundary retained |

```diff
@@ -461,3 +499,7 @@
-- **`D-GOV-20` — complemented.** The daemon remains sole owner of execution;
-  PEC creates no second loop and holds no session authority.
-  Checkout-contained evidence remains authoritative over any PEC store.
+- **`D-GOV-20` / `D-GOV-43` — complemented.** `D-GOV-43` supersedes
+  `D-GOV-20` items 2–4 on the App MVP Codex path: execution (sessions,
+  delegation, turn admission) is owned per application by its application-owned
+  Runtime service (one private Runtime per application; `D-GOV-43` A2).
+  PEC creates no second loop and holds no session authority. Runtime state
+  stays operational and non-authoritative (`D-GOV-20` item 5), and
+  checkout-contained evidence remains authoritative over any PEC store.
```

### §16 Product decisions

#### SH-28 — §16 heading

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| D-PEC-79 hunk 4 (carried byte-identical) | CLARIFIED (D-PEC-79) | — | — |

```diff
@@ -493,1 +535,1 @@
-## 16. Open product decisions (owner)
+## 16. Product decisions (owner)
```

#### SH-29 — §16.2

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| INV-032 (Seq 46; Q6) | CLARIFIED | — | premise re-expressed; decision stays open |

```diff
@@ -497,2 +539,5 @@
-2. Design and ownership of a daemon global event feed (today: per-session
-   SSE only).
+2. Design and ownership of a global event feed. Premise: no per-user daemon
+   exists (`D-GOV-43` A2); each application owns a private Runtime service
+   whose only SSE route is the per-session turn stream, and no observation
+   interface usable by a non-owning local reader is documented. The
+   decision stays open (see trigger T-RT, PEC-PRS-004).
```

#### SH-30 — §16.3

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| D-PEC-79 hunk 5 (carried, extended) + INV-033 (Seq 10, Seq 75, Seq 76; CP1-V) | TRANSCRIBED (D-PEC-79 disposition; 'strict, versioned') + PROPOSED (feed-profile clause) | — | 'strict-version-1' -> 'strict, versioned'; feed-profile clause appended |

```diff
@@ -499,1 +544,14 @@
-3. Home and shape of the loop registry (which loops PEC serves; today five).
+3. **Resolved 2026-08-02 by `D-PEC-78` O-A.** The long-term home and shape
+   of PEC's loop registry is the existing PEC-owned strict, versioned
+   JSON/schema paths with the core-owned typed `LoopRegistry` port. PEC owns
+   only its configured service set; each listed loop remains authoritative
+   for its own entrypoint and governed truth. Later row changes remain
+   owner-gated PEC configuration changes. Listing or removing a loop creates
+   no duty, lifecycle effect, cadence, conformance obligation, or authority
+   over that loop, and no governed act may depend on PEC or the registry.
+   Registry rows may declare closed, PEC-versioned feed profiles (profile
+   ID, version, live or historical, and a basis citation to the loop's own
+   record); a profile is PEC's reading hypothesis, never the loop's truth.
+   Schema version 1 remains strict; a strict schema version 2 carrying feed
+   profiles, with a `RegisteredLoop` port field, arrives only through a
+   later D-PEC packet, within D-PEC-78 O-A.
```

#### SH-31 — §16.6

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| INV-034 (Seq 47; Q6) | CLARIFIED | — | premise re-expressed; decision stays open |

```diff
@@ -504,1 +562,5 @@
-6. Auth reuse: PEC tokens vs the daemon's project-scoped token registry.
+6. Auth reuse: PEC tokens vs reuse of a Runtime token registry. Premise:
+   Runtime token registries are private to each owning application and per
+   instance (`D-GOV-43` A2), and the Runtime consumer guide forecloses
+   pointing a new consumer at the running App's socket or token file. The
+   decision on PEC's own token mechanism stays open.
```

#### SH-32 — §16.8

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| INV-035 (Seq 48; Q6) | CLARIFIED | — | receipt-contract-v2 status by loop; open for Root/Runtime/Bridge |

```diff
@@ -507,3 +569,7 @@
-8. Whether non-app-dev loop ledgers adopt the D-APP-57 receipt contract
-   (today only the app-dev ledger is schema-validated; pec/bridge are
-   prose-structured).
+8. Whether the Root, Runtime and Bridge loop ledgers adopt the shared
+   receipt contract. Premise: the App (`D-APP-57`), Piping (`D-44`) and PEC
+   (`D-PEC-80`) ledgers carry the `receipt-contract-v2` marker with shared
+   validation; the App and Piping ledgers are historical and their new
+   receipts are central `AgentRuns/<RunID>/RECEIPT.md` files; the Root,
+   Runtime and Bridge ledgers carry no marker. The decision stays open for
+   those three ledgers.
```

#### SH-33 — §16.9

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| INV-036 (Seq 49, Seq 53; Q6) | CLARIFIED | — | path refresh; both decisions stay open |

```diff
@@ -510,4 +576,7 @@
-9. Event-contract home (shared `runtime/packages/contracts` vs a PEC-local
-   schema with a pinned mirror) and API transport (Unix socket only vs an
-   additional loopback listener, given D-GOV-20's no-TCP-control-listener
-   posture).
+9. Event-contract home (the Runtime loop's shared
+   `projects/chirality-runtime/packages/contracts` — root `runtime/`
+   relocated, PR #727 — vs a PEC-local schema with a pinned mirror) and API
+   transport (Unix socket only vs an additional loopback listener, given
+   `D-GOV-43` A2 (no network-exposed listener), superseding `D-GOV-20`
+   item 4).
+   Both decisions stay open.
```

#### SH-34 — §16 closing sentence

| Source | Provenance label | D-PEC-90 note | Remark |
|---|---|---|---|
| D-PEC-79 hunk 6 (carried byte-identical) | CLARIFIED (D-PEC-79) | — | — |

```diff
@@ -515,1 +583,1 @@
-None of these blocks P0–P2.
+None of the remaining open decisions blocks P0–P2.
```

## 4. Coverage of Annex B

### 4.1 MODIFY rows (28) — each realized

| InvID | Annex B disposition (as amended) | Hunk |
|---|---|---|
| INV-002 | Refresh with the successor candidate | SH-04 |
| INV-003 | Registry-relative loop wording | SH-05 |
| INV-004 | Refresh with the successor candidate | SH-06 |
| INV-005 | Refresh with the successor candidate | SH-07 |
| INV-006 | Historical-grammar entity; gate state re-sourced | SH-08 |
| INV-007 | Refresh with the successor candidate | SH-09 |
| INV-008 | Refresh with the successor candidate | SH-10 |
| INV-009 | Refresh with the successor candidate | SH-11 |
| INV-010 | RunRecord re-sourced | SH-12, SH-13 |
| INV-013 | Refresh with the successor candidate | SH-14 |
| INV-014 | Q4 (a) re-sourcing | SH-15 |
| INV-015 | Re-express feed kinds; manifest clause moves to registry feed profiles (Q1/Q2) | SH-13, SH-16 |
| INV-017 | Re-express per P-β | SH-17 |
| INV-018 | Defer with trigger T-RT (P-β) | SH-18 |
| INV-019 | Refresh with the successor candidate | SH-19 |
| INV-020 | Daemon and cmux bridges deferred; hooks CLI stays (amendment 1) | SH-20 |
| INV-021 | Refresh with the successor candidate | SH-21 |
| INV-025 | Registry-relative P2 wording | SH-22 |
| INV-026 | Narrow P4 (P-β); cmux recorded deferred (amendment 1) | SH-23 |
| INV-028 | Refresh with the successor candidate | SH-24 |
| INV-029 | Refresh with the successor candidate | SH-25 |
| INV-030 | Refresh with the successor candidate | SH-26 |
| INV-031 | Refresh with the successor candidate | SH-27 |
| INV-032 | Q6 re-express, still open | SH-29 |
| INV-033 | Carried per CP1-D79; feed-profile clause under O-B2 | SH-30 |
| INV-034 | Q6 re-express, still open | SH-31 |
| INV-035 | Q6 re-express, still open | SH-32 |
| INV-036 | Q6 re-express + path refresh | SH-33 |

### 4.2 NOTE-ONLY rows (8) — each untouched

Checked by exact-match: the v2.2 locator text occurs once in v2.2 and once, identically, in the candidate.

| InvID | Locator | State |
|---|---|---|
| INV-001 | §2 bullet 1 | byte-unchanged |
| INV-011 | §7.1 CandidateBrief row | byte-unchanged |
| INV-012 | §7.2 presence tier table | byte-unchanged |
| INV-016 | §9.3 PEC-GAT-001 | byte-unchanged |
| INV-022 | §9.7 PEC-DSH-001 | byte-unchanged |
| INV-023 | §9.7 PEC-DSH-003 | byte-unchanged |
| INV-024 | §12 P0 row | byte-unchanged |
| INV-027 | §12 closing paragraph | byte-unchanged |

### 4.3 Hunk count by source

| Source | Hunks |
|---|---|
| D-PEC-79 hunks carried (SH-01, SH-02, SH-03, SH-28, SH-30, SH-34) | 6 |
| Annex B MODIFY rows (28 rows; INV-033 shares SH-30 with D-PEC-79 hunk 5) | 28 |
| Seq 1 WorkGraph / WorkNode row (SH-13) | 1 |
| Amendment-1 extensions (inside SH-19, SH-20, SH-23; no separate hunk) | 0 |
| **Total logical hunks** | **34** |

The unified `diff -u` groups these 34 logical hunks into 16 context hunks; no line changes outside them (§8).

## 5. D-PEC-79 hunks: carried or extended

| D-PEC-79 hunk | Locus | Disposition | Exact delta against the D-PEC-79 postimage |
|---|---|---|---|
| 1 | Header Version / Date / Status rows | Version carried byte-identical; Date and Status **extended** | Date `2026-08-09` -> `2026-09-25` (slot). Status: "**Adopted 2026-08-09** by owner ruling (`D-PEC-79`)" -> "**Adopted 2026-09-25** by owner acceptance of SCA-005 checkpoint group 2 (`execution/_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-2_2026-09-25/`)"; "§16.3 loop-registry disposition concordance adopted as v2.3 by `D-PEC-79`" -> "… adopted as exact v2.3 candidate bytes by `D-PEC-79` (not separately applied; carried into this successor); SCA-005 feed-model, presence and runtime-topology concordance adopted with this successor" |
| 2 | Epistemic-status paragraph | **Extended** | ", and amended to v2.3 on 2026-08-09 (`D-PEC-79`) to reconcile §16.3 to D-PEC-78 O-A and accepted SCA-004 decomposition truth." -> ". A v2.3 candidate reconciling §16.3 to D-PEC-78 O-A and accepted SCA-004 decomposition truth was adopted as exact bytes on 2026-08-09 (`D-PEC-79`) but not applied; this successor v2.3 carries those changes and was adopted on 2026-09-25 by owner acceptance of SCA-005 checkpoint group 2, which also reconciles the feed, presence and runtime-topology premises to current file truth." The D-PEC-79 lineage content is kept; the reflowed trailing sentence is unchanged in words |
| 3 | "v2.3 provenance labels" block | Carried **byte-identical**; successor block added after it | addition only: "v2.3 successor provenance labels (SCA-005)" block (SH-03) |
| 4 | §16 heading | Carried **byte-identical** | none |
| 5 | §16.3 item | Carried byte-identical **except** one token; clause **appended** | `strict-version-1` -> `strict, versioned`; six lines appended after "…depend on PEC or the registry." (feed-profile clause, INV-033 / CP1-V) |
| 6 | §16 closing sentence | Carried **byte-identical** | none |

Mechanical check: of the 24 lines D-PEC-79 adds to v2.2, 17 occur verbatim in the candidate; the 7 that do not are exactly the Date row, the Status row, the four reflowed epistemic-paragraph lines and the `strict-version-1` line listed above.

## 6. Acceptance-bound slots

These tokens are measurement-bound: they take the actual values at the owner's act; no other byte may change at acceptance (SCA-004 precedent). A changed slot changes the candidate hash in §1.

| # | Candidate line | Token | Binds to |
|---|---|---|---|
| S1 | 6 (Date row) | `2026-09-25` | date of the owner's checkpoint-group-2 acceptance |
| S2 | 7 (Status row) | `2026-09-25` in "**Adopted 2026-09-25**" | same date |
| S3 | 7 (Status row) | `SCA-005_GROUP-2_2026-09-25` in `execution/_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-2_2026-09-25/` | actual group-2 snapshot folder name (the date token inside it follows S1) |
| S4 | 18 (epistemic paragraph) | `2026-09-25` in "was adopted on 2026-09-25" | same date |

Wording that presumes a whole-group acceptance ("adopted … by owner acceptance of SCA-005 checkpoint group 2", Status row and epistemic paragraph) is true only if the owner accepts the group; a partial or modified acceptance needs a redrafted candidate, not a slot fill. No other date in the candidate is a slot: `2026-08-02`, `2026-08-09` and `2026-09-24` record past acts.

## 7. What is not changed

Each item was checked by exact-match against both files.

- §12 P1 row: byte-unchanged (Q10 (a); the "§12 P1 (Q10 c)" element of Seq 75 is dropped).
- §6 invariant rows PEC-K-01..PEC-K-11: byte-unchanged, including PEC-K-02, PEC-K-03 (verify-before-rely) and PEC-K-11 (D-PEC-90).
- §8 Agents bullet and access-class bullet: byte-unchanged; no reliance or direct-query text added anywhere (D-PEC-90; Decision_Log SCA005-D90-NOTE).
- §11 Success metrics, including metric 1 and its pre-P1 baseline: byte-unchanged; §2 Step-0 bullet 1 and the "Step-0 cost is re-measured before P1 (§11)" clause: byte-unchanged (Q9).
- §§1, 3, 5, 6, 7.2, 7.3, 9.3, 9.7, 10, 11, 14 and 17 are byte-unchanged, each compared as a whole section (7.2 and 7.3 together).
- The eight Annex B NOTE-ONLY loci (§4.2).
- The v2.2 provenance-labels block, the Product-stage and Supersession header rows, and §16 items 1, 4, 5 and 7.
- No new requirement ID, invariant ID or section; the only added table row is §7.1 WorkGraph / WorkNode (SH-13). Content-minimal (PEC-K-10) and file-authority (PEC-K-02) wording is untouched.

## 8. Residual stale premises left unchanged (outside Annex B; for the manager)

These loci still carry premises SCA-005 changes elsewhere. They have no Annex B row, so the brief's "no change outside the listed loci" rule leaves them as v2.2 wrote them. Each needs a Supersession_Delta binding, a later PRD change, or an explicit decision to leave it.

| Locus (candidate line) | Text | Conflicts with |
|---|---|---|
| §12 P3 row (414) | "PEC-side interfaces/adapters usable by hooks CLI or daemon consumers" | SH-14/SH-20 (no daemon; Runtime bridge deferred) |
| §9.7 PEC-DSH-005 (362) | "Presence board: sessions × worktrees × live hierarchy" | SH-18 (PEC-PRS-004 deferred); Seq 33 SOW-049; IA §8.3 lists PEC-DSH-005 as a SUPERSESSION binding |
| §4.1 second bullet (147) | "An **ephemeral presence registry** for sessions, worktrees, and live agent hierarchy (presence tier)" | SH-18 (live hierarchy deferred) |
| §7.2 HierarchyEdge row (INV-012, NOTE-ONLY) (257) | "live parent→child session edges" | SH-18 (entity has no live source while deferred) |
| §13 domain-engine row (452) | "profile superseded when v2 has shape" | D-T0-27 O-A already adopted the PEC v2 successor profile (per `projects/pec/AGENTS.md`); not inventoried by A2 |

## 9. Checks

| Check | Command (cwd) | Result |
|---|---|---|
| Preimage identity | `shasum -a 256 projects/pec/docs/PRD.md` (repo root) | `6833553c…477ba`, matches |
| D-PEC-79 postimage identity | `shasum -a 256 …/PRD_V2_3_CANDIDATE_POSTIMAGE.md` | `92627ee1…b5f0`, matches |
| Candidate equals the 34-edit list applied to v2.2 (each edit matches exactly once) | `python3 build_candidate.py` then this generator's reconstruction (scratch) | pass |
| Unified diff v2.2 -> candidate | `diff -u projects/pec/docs/PRD.md …/CP2_CANDIDATE/docs/PRD.md` (repo root), exit 1 (differences) | 16 context hunks; every changed line belongs to SH-01..SH-34 |
| D-PEC-79 postimage -> candidate at the six loci | `diff -u …/PRD_V2_3_CANDIDATE_POSTIMAGE.md …/CP2_CANDIDATE/docs/PRD.md` (`projects/pec/execution`), exit 1 | carried/extended exactly as §5 |
| Annex B coverage | generator assertion | 28/28 MODIFY realized; 8/8 NOTE-ONLY byte-unchanged |
| Protected loci | generator assertion | §12 P1, PEC-K-01..11, §8 Agents/access bullets, §11 and §2 Step-0 text unchanged |
| Active reliance holds | `ACTIVE_RELIANCE_HOLDS.csv` read (drafting is not reliance) | 0 ACTIVE rows |
