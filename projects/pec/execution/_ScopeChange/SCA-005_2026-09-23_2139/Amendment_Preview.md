---
amendment_id: SCA-005
doc_kind: scope_change.amendment_preview
decomp_variant: SOFTWARE
checkpoint_group: 2
created: 2026-09-25
status: candidate_awaiting_checkpoint_2_acceptance
accepted_impact_assessment_sha256: 0bcbe9bdced43fa887a859497b3edd197242a0eea8fa3a41fab7147b358239bf
accepted_intake_sha256: 5c4ae0532eb65ea83d0529a9f6395da392ae2bf5b254cfb6b2de49e4fbff2be2
---

# SCA-005 — checkpoint-group-2 exact amendment preview

## Approval unit and boundary

This is the exact, diff-style amendment of PEC's SOFTWARE decomposition (revision 1.4 → 1.5) proposed for checkpoint group 2. It is a preview only: no live decomposition, register, PRD, SOW, `_CONTEXT.md`, `_STATUS.md`, pointer or `v2/**` byte has changed. Every diff below is computed from the live preimages and the candidate postimages under `CP2_CANDIDATE/`, and every change is shown. The hunks are a reading aid, not a patch: a hunk shows the changed text with minimal context, some start or end mid-line, some context lines already reflect an earlier-listed edit, and inserted rows are shown with their stated insertion point rather than an anchor line. The generator did verify that applying all 71 markdown edits (as exact string replacements, in application order) to the preimage yields the candidate byte-for-byte. Every register row not shown is byte-identical, with physical row order preserved (new rows inserted only where stated). The candidate files and their SHA-256 values below are what the owner accepts.

Basis consumed: accepted group-1 snapshot `checkpoint_snapshots/SCA-005_GROUP-1_2026-09-24/`, amendment 1 `…_AMENDMENT-1_2026-09-24/` (TM-PEC-023 selections, cmux deferral, impact delta), amendment 2 `…_AMENDMENT-2_2026-09-24/` (SOW-033), the accepted Impact Assessment and intake at the hashes above, the checkpoint-1 resolution note (`af4e46d0…0ad2`), and the D-PEC-90 preparation note (`Decision_Log.md` SCA005-D90-NOTE). Section anchors `A-NN` are the `ActionSeq` of `Amendment_Actions_CP2.csv`.

## Byte preconditions and postimages

| Surface | Preimage SHA-256 (live, revision 1.4 / PRD v2.2) | Candidate postimage SHA-256 |
|---|---|---|
| `_Decomposition/SOFTWARE_DECOMP.md` | `7cca5cdbb1ba4bd866391abf00998bc80f587a23505a6f5b6bceb8df48b65c81` | `dc2b84791454ac888e692bfa507221f5d4a588c63bb8ab5005cc00343b119660` |
| `_Decomposition/ScopeLedger.csv` | `2103afa279bc7df8e75f830326462d7575cf69a403ee7ef07880e0e9fe969e25` | `83152a94d91c75da1205f98aec712f901529af4da562f02f5f1124b3ba3fd9df` |
| `_Decomposition/Deliverables.csv` | `49f904488a7402e2124359b59b2fc0df9103bef39ee53a5ce8b74f7dc6cc6b72` | `b8628fc4c7b32b66eae373e19eb943ccaa866125e79119172b82614a01d3d65a` |
| `_Decomposition/ContextBudgetQA.csv` | `5c8d30994a99611b7023f8ac0995ee9a8efa0d2992f3c1a2683f4d2f9e8e2bef` | `2a1941050d06e5e07f6cde629d0abf0c2d80acde1983139e6c1918cfca9eb0df` |
| `_Decomposition/Companion_Inventory.csv` | `18793e150c537371f80d659af2784674d42bac0de37bf7128e484774a557ec23` | `7c8a24a868ff03415c4440055dc099aaf7e2d87cca8dc0267e77d1a676976ef8` |
| `docs/PRD.md` | `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba` | `fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32` |
| `_Decomposition/_LATEST.md` — not in the approval unit; rewritten only after checkpoint-3 acceptance (A-74) | `7abf65e641a5a247f0c783192808ae1f9186f76ebe0d09d6e84e2983fffcd7a3` | none |

Any preimage mismatch before application invalidates this preview and returns the package to checkpoint 2.

### Acceptance-bound tokens and the pre-acceptance application state

The candidate carries its final accepted-state text (SCA-004 precedent). The following tokens are measurement-bound slots that take the actual acceptance date; no other byte may change. **Hash rule:** the SHA-256 values in this package are computed with every slot at `2026-09-25`. When a slot takes a different actual value, the verifier substitutes the actual values into the accepted candidate bytes at exactly these loci, recomputes SHA-256, compares it with the written file, and records both the accepted hash and the slot-substituted hash. During checkpoint-3 preparation the decomposition slots carry the application date and are rewritten to the checkpoint-3 acceptance date in the same act that restores the two front-matter lines below.

| File | Location | Token |
|---|---|---|
| `SOFTWARE_DECOMP.md` | front matter `date:` | `2026-09-25` (checkpoint-3 acceptance date) |
| `SOFTWARE_DECOMP.md` | front matter `accepted:` | `2026-09-25` (checkpoint-3 acceptance date) |
| `SOFTWARE_DECOMP.md` | §7 `Revision` row | `2026-09-25` |
| `SOFTWARE_DECOMP.md` | §11 DL-20 date cell | `2026-09-25` |
| `docs/PRD.md` candidate | Date row; Status row date; epistemic paragraph date | `2026-09-25` (checkpoint-2 acceptance date) |
| `docs/PRD.md` candidate | Status row snapshot path | `SCA-005_GROUP-2_2026-09-25` (actual group-2 snapshot folder) |

Application during checkpoint-3 preparation writes the decomposition postimage with exactly two front-matter lines in their pre-acceptance form; the owner's checkpoint-3 acceptance restores them to the postimage values above:

```text
status: candidate_pending_checkpoint_3
accepted: not yet accepted — revision 1.5 applied during SCA-005 checkpoint-3 preparation; revision 1.4 (accepted 2026-08-03) remains the accepted basis until the owner's checkpoint-3 acceptance
```

Pre-acceptance variant SHA-256: `37ea1084a8219943a69057be377646c69a609a76728241963045d7cfb015a6cc` (differs from the candidate in those two lines only).

## Final action set

`Amendment_Actions_CP2.csv` holds 79 actions: 8 ADD / 67 MODIFY / 4 REMOVE. It is the accepted intake (Seq 1–76) minus Seq 68 (moot under the cmux deferral, amendment 1) and Seq 72 (Q9: no change to SOW-058), plus owner-directed Seq 77 and 78 (amendment 1) and Seq 79 (amendment 2), plus two rows the amendment-1 impact delta requires checkpoint 2 to add: Seq 80 (the OBJ-004 objective-side view, which that delta says "needs its own view action") and Seq 81 (the §2.4 runtime-surfaces bullet, which "no accepted action covers"). Seq 68 and 72 stay reserved and unused. Amendment 2 counted 77 actions (8 / 65 / 4) before Seq 80 and 81.

## 1. Change Register (Decision Log, Revision History, front matter, references)

### A-74 — MODIFY OTHER `SCA-005`

Traceability: front matter revision 1.5 (date/accepted acceptance-bound; pre-acceptance status/accepted lines per preview), session_authorization, source_corpus and R1 -> PRD v2.3, DL-20, revision 1.5 row, Companion_Inventory row counts; _Decomposition/_LATEST.md and _ScopeChange/_LATEST.md move only after checkpoint-3 acceptance. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — FM revision/date (Seq 74):

```diff
-revision: "1.4"
-date: 2026-08-03
+revision: "1.5"
+date: 2026-09-25
```

`SOFTWARE_DECOMP.md` — FM accepted (Seq 74):

```diff
-accepted: 2026-08-03 (original Gate 7 owner ruling under D-PEC-60; revision 1.4 successor accepted through SCA-004 under the owner's Gate 5 post-change confirmation)
+accepted: 2026-09-25 (original Gate 7 owner ruling under D-PEC-60; revision 1.5 successor accepted through SCA-005 under the owner's checkpoint-group-3 audited-poststate acceptance)
```

`SOFTWARE_DECOMP.md` — FM session_authorization (Seq 74):

```diff
-then by SCA-004 under D-PEC-78 and the owner's 2026-08-03 Gate 5 post-change confirmation
+by SCA-004 under D-PEC-78 and the owner's 2026-08-03 Gate 5 post-change confirmation, then by SCA-005 under D-PEC-86 and the owner's SCA-005 checkpoint acceptances
```

`SOFTWARE_DECOMP.md` — FM source_corpus (Seq 74):

```diff
-source_corpus: projects/pec/docs/PRD.md (v2.2; v2.0 adopted by D-PEC-58, directed-bootstrap clarification adopted by D-PEC-61, exact PEC-K-03/-11 rows adopted by D-PEC-67, surrounding consumer-interface concordance adopted by D-PEC-68)
+source_corpus: projects/pec/docs/PRD.md (v2.3; v2.0 adopted by D-PEC-58, directed-bootstrap clarification adopted by D-PEC-61, exact PEC-K-03/-11 rows adopted by D-PEC-67, surrounding consumer-interface concordance adopted by D-PEC-68, v2.3 successor accepted through SCA-005 carrying the D-PEC-79 §16.3 loop-registry concordance with the SCA-005 feed-model and Runtime-topology concordance)
```

`SOFTWARE_DECOMP.md` — §7 Revision:

```diff
-| Revision | 1.4, 2026-08-03 (SCA-004) |
+| Revision | 1.5, 2026-09-25 (SCA-005) |
```

`SOFTWARE_DECOMP.md` — §11 ADD DL-20 (Seq 74):

```diff
-| DL-19 | 2026-08-03 | SCA-004, requested by owner Ryan Tufts through D-PEC-78 O-A, promotes SOW-077 from TBD to IN, maps it to PKG-01 → DEL-01-06 → OBJ-004, adds SOW-077 to DEL-01-06 coverage, and records OI-003 resolved; DEL-01-06's stable name/path and all source bytes remain unchanged | The existing PEC-owned strict-version-1 JSON/schema paths and core-owned typed port are the selected long-term registry home and shape. PEC owns only its configured service set; each listed loop retains authority over its own entrypoint and truth; later row changes remain owner-gated PEC configuration acts; graceful absence and the no-governed-dependency boundary remain intact |
+| DL-19 | 2026-08-03 | SCA-004, requested by owner Ryan Tufts through D-PEC-78 O-A, promotes SOW-077 from TBD to IN, maps it to PKG-01 → DEL-01-06 → OBJ-004, adds SOW-077 to DEL-01-06 coverage, and records OI-003 resolved; DEL-01-06's stable name/path and all source bytes remain unchanged | The existing PEC-owned strict-version-1 JSON/schema paths and core-owned typed port are the selected long-term registry home and shape. PEC owns only its configured service set; each listed loop retains authority over its own entrypoint and truth; later row changes remain owner-gated PEC configuration acts; graceful absence and the no-governed-dependency boundary remain intact |
+| DL-20 | 2026-09-25 | SCA-005, requested by owner Ryan Tufts and opened by D-PEC-86, accepted at checkpoint 1 on 2026-09-24 with amendment 1 (TM-PEC-023 selections; cmux deferral) and amendment 2 (SOW-033 → OBJ-003), re-bases the feed model on the shared development-loop method and the application-owned Runtime topology (D-GOV-43 A2): it adds SOW-095/096 and DEL-02-08/09 (work-graph and MEMORY run-index parsers, P1, OBJ-001;OBJ-002); re-sources SOW-001/004/013..017 and DEL-01-01, DEL-02-03..07, DEL-03-03 and DEL-04-01; declares closed, PEC-versioned feed profiles on registry rows (SOW-077/094, DEL-01-06; a strict schema v2 by a later D-PEC source packet within D-PEC-78 O-A) and makes `adapter.yaml` a parity-peer input; moves SOW-029, SOW-035 and SOW-087 (trigger T-RT) and SOW-037 (later owner direction) to Deferred OUT and retires DEL-06-04, DEL-07-02, DEL-07-04 and DEL-07-05 non-destructively; records the owner's TM-PEC-023 selections and the SOW-033 mapping, so no IN item lacks an objective (SOW-063's mapping supersedes DL-14's objective-free rationale); and re-expresses C5, C13, R4, SOW-026/034/049/074/076/080/082/083/092, OI-002/006/008/009, PKG-00/02/06/07, the telemetry and the vocabulary. The source corpus moves to PRD v2.3 | Invariants preserved: 11 packages and 6 objectives; every stable ID, name and path retained (CP1-N) and the new IDs append-only; retired rows kept for register integrity; no IN item without package, deliverable or objective; the union invariant holds; the §16 decisions stay open (Q6); C3, C15 and SOW-058 unchanged. Dependency registers, `_CONTEXT.md` and `_REFERENCES.md` metadata, Scope of Work contracts, lifecycle and source remain downstream of this amendment |
```

`SOFTWARE_DECOMP.md` — §12 ADD revision 1.5 (Seq 74):

```diff
-| 1.4 | SCA-004 | D-PEC-78 O-A loop-registry disposition: SOW-077 TBD→IN and mapped to PKG-01 / DEL-01-06 / OBJ-004; SOW-094 implementation basis reconciled; DEL-01-06 coverage and description updated in place; OI-003 resolved; stable IDs, topology, source, dependency edges, envelope, phase, name, and path unchanged |
+| 1.4 | SCA-004 | D-PEC-78 O-A loop-registry disposition: SOW-077 TBD→IN and mapped to PKG-01 / DEL-01-06 / OBJ-004; SOW-094 implementation basis reconciled; DEL-01-06 coverage and description updated in place; OI-003 resolved; stable IDs, topology, source, dependency edges, envelope, phase, name, and path unchanged |
+| 1.5 | SCA-005 | Feed-model and Runtime-topology rebaseline under D-PEC-86: +SOW-095/096 and +DEL-02-08/09; SOW-029/035/037/087 IN→OUT Deferred and DEL-06-04/07-02/07-04/07-05 retired non-destructively; registry feed profiles; `adapter.yaml` parity-peer only; TM-PEC-023 selections and the SOW-033 mapping (0 IN items without objective); C5/C13, R4, SSOW rows, PKG-00/02/06/07, deliverable descriptions, §16 premises, vocabulary (26 terms), telemetry and envelope posture (S 28 / M 32 / L 2) reconciled; PRD v2.3 source; stable IDs, names and paths retained |
```

`SOFTWARE_DECOMP.md` — §1.5 R1 source reference (Seq 74):

```diff
-| R1 | `projects/pec/docs/PRD.md` (v2.2; lineage ruled through `D-PEC-58`, `D-PEC-61`, `D-PEC-67`, and `D-PEC-68`) | Source corpus |
+| R1 | `projects/pec/docs/PRD.md` (v2.3; lineage ruled through `D-PEC-58`, `D-PEC-61`, `D-PEC-67`, and `D-PEC-68`, with the `D-PEC-79` §16.3 concordance carried into the v2.3 successor accepted through SCA-005) | Source corpus |
```

`Companion_Inventory.csv` row `Deliverables.csv` (replace):

```diff
-Deliverables.csv,authoritative companion register,"64-row deliverable register: descriptions, types, artifacts, Context Envelopes + notes, PhaseHint"
+Deliverables.csv,authoritative companion register,"66-row deliverable register: descriptions, types, artifacts, Context Envelopes + notes, PhaseHint"
```

`Companion_Inventory.csv` row `ScopeLedger.csv` (replace):

```diff
-ScopeLedger.csv,authoritative companion register,94-row SOW->PKG->DEL->OBJ ledger with DecisionRef and OpenIssue columns; authoritative for assignments
+ScopeLedger.csv,authoritative companion register,96-row SOW->PKG->DEL->OBJ ledger with DecisionRef and OpenIssue columns; authoritative for assignments
```

### A-25 — MODIFY OTHER `R4`

§1.5 R4 re-pointed to projects/pec/plans/workplans/WORKPLAN_2026-07-24_pec_coordination_plane.md, labelled retired history (D-PEC-80 D). Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §1.5 R4 (Seq 25):

```diff
-| R4 | `_DomainEngines/pec/WORKPLAN_2026-07-24_pec_coordination_plane.md` | Standing plan; D1 authorization context |
+| R4 | `projects/pec/plans/workplans/WORKPLAN_2026-07-24_pec_coordination_plane.md` | Retired history (D-PEC-80 D): the former standing plan; D1 authorization context |
```

## 2. Primary partitions — Packages

### A-23 — MODIFY PACKAGE `PKG-02`

PKG-02 charter: work graphs, central receipts, MEMORY run index first-class; JSON/workplans/App-Piping ledgers historical; adapter.yaml parity-peer; assigned SOW-011..017, 095, 096 (7 -> 9). Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §4 PKG-02 (Seq 23):

```diff
-| PKG-02 | File-Truth Parsers | Read-side grammars over governed files: `_STATUS.md` dialect, decision registers/packets, receipts ledgers, run-evidence JSON, dependency registers, workplans/LOOP_INIT, `adapter.yaml` manifests | SOW-011..017 (7) |
+| PKG-02 | File-Truth Parsers | Read-side grammars over governed files: `_STATUS.md` dialect, decision registers/packets, receipts (ledgers and central `RECEIPT.md`), Markdown work graphs, the MEMORY run index and `LOOP_INIT.md` identity as first-class feeds; run-evidence JSON, workplans and App/Piping ledgers as declared historical grammars; dependency registers; `adapter.yaml` as a parity-peer input | SOW-011..017, 095, 096 (9) |
```

### A-41 — MODIFY PACKAGE `PKG-00`

PKG-00 charter: event-contract types consumed by the hooks CLI bridge, the only remaining bridge. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §4 PKG-00 (Seq 41):

```diff
-| PKG-00 | Architecture Runway & Contracts | Published specifications others consume: v2's first ADRs (incl. the OI-012 core-isolation decision), the v2 SPEC born from this decomposition, and the versioned event-contract types shared by daemon, hooks CLI, and adapters |
+| PKG-00 | Architecture Runway & Contracts | Published specifications others consume: v2's first ADRs (incl. the OI-012 core-isolation decision), the v2 SPEC born from this decomposition, and the versioned event-contract types consumed by the hooks CLI bridge, the only remaining bridge |
```

### A-42 — MODIFY PACKAGE `PKG-06`

PKG-06 charter/exclusions: session lifecycle the per-application Runtime's (C13); live hierarchy edges deferred; assigned SOW-026..028, 030..032 (7 -> 6). Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §4 PKG-06 (Seq 42):

```diff
-| PKG-06 | Presence & Git Observation | The presence tier's producers: harness-reported session records, Git/worktree scanning, session×worktree×scope correlation, hierarchy edges, TTL/heartbeat discipline, advisory overlap detection, citation-exclusion enforcement | SOW-026..032 (7) | Session lifecycle ownership (daemon's, C13) |
+| PKG-06 | Presence & Git Observation | The presence tier's producers: harness-reported session records, Git/worktree scanning, session×worktree×scope correlation, TTL/heartbeat discipline, advisory overlap detection, citation-exclusion enforcement | SOW-026..028, 030..032 (6) | Session lifecycle ownership (the per-application Runtime's, C13); live hierarchy edges (SOW-029, deferred) |
```

### A-43 — MODIFY PACKAGE `PKG-07`

PKG-07 charter narrowed: hooks CLI bridge plus durable ingest; daemon SSE bridge and client seam deferred (T-RT), cmux adapter deferred (later owner direction); exclusions cite projects/chirality-runtime/**; assigned SOW-033, 036, 039 (6 -> 3). Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §4 PKG-07 (Seq 43 as narrowed):

```diff
-| PKG-07 | Event Ingest & Bridges | Best-effort freshness inputs: idempotent append-only event ingest, the daemon SSE / hooks CLI / cmux bridges, durable message store, the shared-runtime client seam — implementing the PKG-00 event contracts | SOW-033, 035..037, 039, 087 (6) | Record-tier fact creation (PKG-03 guarantee); contract definition (PKG-00); root `runtime/` writes (SOW-074, deferred) |
+| PKG-07 | Event Ingest & Bridges | Best-effort freshness inputs: idempotent append-only event ingest, the hooks CLI bridge and the durable message store — implementing the PKG-00 event contracts. The daemon SSE bridge and the shared-runtime client seam are deferred (trigger T-RT) and the cmux adapter is deferred (later owner direction) | SOW-033, 036, 039 (3) | Record-tier fact creation (PKG-03 guarantee); contract definition (PKG-00); writes into `projects/chirality-runtime/**` (SOW-074, deferred) |
```

## 3. Secondary entities — Deliverables (incl. retirements and additions)

### A-12 — MODIFY DELIVERABLE `DEL-01-01`

DEL-01-01 description/envelope notes follow SOW-001 (16 entity types); L/MEDIUM retained; ContextBudgetQA notes and RecommendedAction re-expressed (INV-116 split-line correction rides this re-assessment). Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §8 prose (Seq 12, 14, 17, 39, 40, 73):

```diff
-- **Two L:** DEL-02-03 (receipts-ledger parser: per-loop grammars, OI-008
-  open) and DEL-01-01 (record-tier schema: 14 entity types, the dependency
-  of every derivation package). Both MEDIUM risk with envelope notes and
-  named split lines if implementation demands them.
-- **Two OI-coupled MEDIUM risks at M envelope** (DL-14): DEL-00-02
-  (event-contract schema — OI-009 decides its home) and DEL-08-01
-  (socket + tokens — OI-006 decides the auth mechanism). Held at current
-  envelope; re-assessed on the linked ruling.
+- **Two L:** DEL-02-03 (receipts parser: ledger grammars plus the central
+  `RECEIPT.md` grammar, OI-008 open for the Root, Runtime and Bridge
+  ledgers; split line: the central-receipt grammar) and DEL-01-01
+  (record-tier schema: 16 entity types, the dependency of every derivation
+  package). Both MEDIUM risk with envelope notes and named split lines if
+  implementation demands them.
+- **Two OI-coupled MEDIUM risks at M envelope** (DL-14): DEL-00-02
+  (event-contract schema — OI-009 decides its home; the shared option path
+  is `projects/chirality-runtime/packages/contracts`) and DEL-08-01
+  (socket + tokens — OI-006 decides the PEC-local token mechanism; no
+  shared Runtime token registry exists to reuse). Held at current envelope;
+  re-assessed on the linked ruling.
+- **SCA-005 additions and re-assessments:** DEL-02-08 (work-graph parser)
+  is M with MEDIUM risk — a new grammar, profile-driven discovery,
+  PR-to-merge resolution inputs and three pinned fixture classes — held as
+  one parser slice; DEL-02-09 (MEMORY run-index parser) is S, LOW;
+  DEL-02-06 is held at M, LOW, with re-assessment toward S after its scope
+  narrowed to `LOOP_INIT.md` identity.
+- **Four retired rows** (DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05) keep
+  their envelope and risk cells for register integrity and are excluded
+  from active envelope counts.
```

`ContextBudgetQA.csv` row `DEL-01-01` (replace):

```diff
-DEL-01-01,PKG-01,L,MEDIUM,Hold as L; split by per-loop grammar if any loop proves adversarial,L: 14 entity types and the schema every derivation package depends on; kept one cohesive DDL slice — split (core record entities vs lifecycle/dependency/run entities) only if implementation shows a natural seam
+DEL-01-01,PKG-01,L,MEDIUM,Hold as L; split core record entities from lifecycle/dependency/run/graph entities only if implementation shows a natural seam,L: 16 entity types (DL-14's 14 plus WorkGraph and WorkNode) and the schema every derivation package depends on; kept one cohesive DDL slice — split (core record entities vs lifecycle/dependency/run/graph entities) only if implementation shows a natural seam
```

`Deliverables.csv` row `DEL-01-01` (replace):

```diff
-DEL-01-01,PKG-01,Record-tier schema & entity model,"Store schema and typed entity model for the record tier: 11 PRD rows, 14 entity types (Workplan/Step/Gate and Package/Deliverable are compound rows) — Loop, Workplan, Step, Gate, Receipt, DecisionRow, Fence, Package, Deliverable, DependencyEdge, RunRecord, CandidateBrief, OrientationSnapshot, DriftFinding.",DATA_MODEL_CHANGE,TBD,Schema/DDL + entity types + model tests,SOW-001,OBJ-001;OBJ-002,L,L: 14 entity types and the schema every derivation package depends on; kept one cohesive DDL slice — split (core record entities vs lifecycle/dependency/run entities) only if implementation shows a natural seam,P1
+DEL-01-01,PKG-01,Record-tier schema & entity model,"Store schema and typed entity model for the record tier: 16 entity types (Workplan/Step/Gate, Package/Deliverable and WorkGraph/WorkNode are compound rows) — Loop, Workplan, Step, Gate, Receipt, DecisionRow, Fence, Package, Deliverable, DependencyEdge, RunRecord, CandidateBrief, OrientationSnapshot, DriftFinding, WorkGraph, WorkNode. Workplan/Step/Gate is a declared historical-grammar entity whose gate state is re-sourced from decision registers, scope-change pointers and graph BLOCKED nodes; Receipt covers ledger entries and central `RECEIPT.md`; RunRecord is sourced from central receipts, work graphs and the MEMORY run index, with JSON run evidence historical; ""remaining items"" is a per-loop optional field.",DATA_MODEL_CHANGE,TBD,Schema/DDL + entity types + model tests,SOW-001,OBJ-001;OBJ-002,L,L: 16 entity types (DL-14's 14 plus WorkGraph and WorkNode) and the schema every derivation package depends on; kept one cohesive DDL slice — split (core record entities vs lifecycle/dependency/run/graph entities) only if implementation shows a natural seam,P1
```

### A-13 — MODIFY DELIVERABLE `DEL-01-06`

DEL-01-06 description adds per-loop feed-profile declarations and the later D-PEC schema-v2 source packet; RF-002 not reopened. Supersession binding: **NO**.

`Deliverables.csv` row `DEL-01-06` (replace):

```diff
-DEL-01-06,PKG-01,Loop registry (local config default),"PEC-owned local configuration naming the loop locators PEC serves: one loop at P1 (PEC's own build, OI-010), extendable by owner-gated PEC configuration changes. The strict version-1 JSON/schema paths and core-owned typed port are the long-term home and shape under D-PEC-78; each listed loop remains authoritative for its own entrypoint and truth, and no governed act depends on PEC or the registry.",BACKEND_FEATURE_SLICE,TBD,Config format + loader + tests,SOW-077;SOW-094,OBJ-004,S,,P1
+DEL-01-06,PKG-01,Loop registry (local config default),"PEC-owned local configuration naming the loop locators PEC serves: one loop at P1 (PEC's own build, OI-010), extendable by owner-gated PEC configuration changes. The strict, versioned JSON/schema paths and core-owned typed port are the long-term home and shape under D-PEC-78; each listed loop remains authoritative for its own entrypoint and truth, and no governed act depends on PEC or the registry. Each row declares a closed, PEC-versioned feed profile (profile ID, version, live/historical, basis citation to the loop's own record), PEC's reading hypothesis and never the loop's truth; PEC's own row declares `remaining-loop` now. Feed-profile declarations need a strict schema v2 (`loops.schema.json` v2, `loops.json`, a `RegisteredLoop` field) through a later D-PEC source packet within D-PEC-78 O-A, with VER-001/VER-003 re-run: a new Scope of Work currency obligation (RF-002 stays resolved).",BACKEND_FEATURE_SLICE,TBD,Config format + loader + tests,SOW-077;SOW-094,OBJ-004,S,,P1
```

### A-14 — MODIFY DELIVERABLE `DEL-02-03`

DEL-02-03 description covers ledger grammars plus central RECEIPT.md; L retained with the central-receipt grammar as split line; OI-008 re-expressed; name/path retained, label drift recorded. Supersession binding: **NO**.

`ContextBudgetQA.csv` row `DEL-02-03` (replace):

```diff
-DEL-02-03,PKG-02,L,MEDIUM,Hold as L; split by per-loop grammar if any loop proves adversarial,"L because grammar varies per loop and SOW-082 (OI-008) keeps the contract-adoption surface open; single domain, but multiple grammars within one parser. Split further only if a loop's grammar proves adversarial"
+DEL-02-03,PKG-02,L,MEDIUM,Hold as L; split the central-receipt grammar into its own deliverable if implementation demands it,"L because grammar varies: the receipt-contract-v2 family (App, Piping, PEC), the Root/Runtime/Bridge prose ledgers and the central `RECEIPT.md` grammar, with SOW-082 (OI-008) still open for the Root, Runtime and Bridge ledgers; single domain, but multiple grammars within one parser. Split line: the central-receipt grammar becomes its own deliverable if implementation demands a split"
```

`Deliverables.csv` row `DEL-02-03` (replace):

```diff
-DEL-02-03,PKG-02,Receipts ledger parser (per-loop grammars),"`LOOP_RECEIPTS.md` parsing under per-loop grammar, including the D-APP-57 contract where adopted; prose-structured ledgers parsed best-effort with stated limits.",BACKEND_FEATURE_SLICE,TBD,Parser + per-loop grammar table + fixture tests,SOW-013,OBJ-001;OBJ-002,L,"L because grammar varies per loop and SOW-082 (OI-008) keeps the contract-adoption surface open; single domain, but multiple grammars within one parser. Split further only if a loop's grammar proves adversarial",P1
+DEL-02-03,PKG-02,Receipts ledger parser (per-loop grammars),"Receipt parsing over two grammar generations of one Receipt feed kind: `LOOP_RECEIPTS.md` ledgers under per-loop grammar (live for PEC/Root/Runtime/Bridge; declared historical for App/Piping), including the receipt-contract-v2 marker where a ledger carries it, and central `execution/_Coordination/AgentRuns/<RunID>/RECEIPT.md`; prose-structured ledgers parsed best-effort with stated limits. Name and path retained under SCA-005 (CP1-N); the label ""ledger parser (per-loop grammars)"" no longer names the central-receipt grammar.",BACKEND_FEATURE_SLICE,TBD,Parser + per-loop grammar table + fixture tests,SOW-013,OBJ-001;OBJ-002,L,"L because grammar varies: the receipt-contract-v2 family (App, Piping, PEC), the Root/Runtime/Bridge prose ledgers and the central `RECEIPT.md` grammar, with SOW-082 (OI-008) still open for the Root, Runtime and Bridge ledgers; single domain, but multiple grammars within one parser. Split line: the central-receipt grammar becomes its own deliverable if implementation demands a split",P1
```

### A-15 — MODIFY DELIVERABLE `DEL-02-04`

DEL-02-04 description: JSON run evidence historical/current-by-own-practice; daemon referent replaced; S retained; name/path retained. Supersession binding: **NO**.

`Deliverables.csv` row `DEL-02-04` (replace):

```diff
-DEL-02-04,PKG-02,Run-evidence JSON parser,`STATUS.json` / `RUNTIME_SUMMARY.json` under `execution/**` into RunRecord summaries.,BACKEND_FEATURE_SLICE,TBD,Parser + fixture tests,SOW-014,OBJ-001;OBJ-002,S,,P1
+DEL-02-04,PKG-02,Run-evidence JSON parser,"`STATUS.json` / `RUNTIME_SUMMARY.json` under `execution/**` into RunRecord summaries, as a declared historical grammar for App/Piping and current-by-own-practice for PEC/Root; application-owned Runtime service user-data is operational, never an input. Name and path retained under SCA-005 (CP1-N); run-evidence JSON is no longer the primary RunRecord source.",BACKEND_FEATURE_SLICE,TBD,Parser + fixture tests,SOW-014,OBJ-001;OBJ-002,S,,P1
```

### A-16 — MODIFY DELIVERABLE `DEL-02-05`

DEL-02-05 description: Dependencies.csv plus WORK_GRAPH.json as historical grammar; WORK_GRAPH.md belongs to DEL-02-08; S retained. Supersession binding: **NO**.

`Deliverables.csv` row `DEL-02-05` (replace):

```diff
-DEL-02-05,PKG-02,Dependency register parser,`Dependencies.csv` and `WORK_GRAPH.json` into DependencyEdge.,BACKEND_FEATURE_SLICE,TBD,Parser + fixture tests,SOW-015,OBJ-001;OBJ-002,S,,P1
+DEL-02-05,PKG-02,Dependency register parser,"`Dependencies.csv`, and `WORK_GRAPH.json` as a declared historical grammar for App/Piping, into DependencyEdge; Markdown `WORK_GRAPH.md` belongs to DEL-02-08.",BACKEND_FEATURE_SLICE,TBD,Parser + fixture tests,SOW-015,OBJ-001;OBJ-002,S,,P1
```

### A-17 — MODIFY DELIVERABLE `DEL-02-06`

DEL-02-06 description: LOOP_INIT identity only; workplans historical; M held (re-assess toward S); name/path retained, label drift recorded. Supersession binding: **NO**.

`ContextBudgetQA.csv` row `DEL-02-06` (replace):

```diff
-DEL-02-06,PKG-02,M,LOW,None; single cohesive slice,
+DEL-02-06,PKG-02,M,LOW,Hold as M; re-assess toward S when its Scope of Work is refreshed,M held under SCA-005: scope narrowed to `LOOP_INIT.md` identity plus the historical workplan grammar; may fall to S on re-assessment
```

`Deliverables.csv` row `DEL-02-06` (replace):

```diff
-DEL-02-06,PKG-02,Workplan/LOOP_INIT parser,Workplans and `LOOP_INIT.md` into Workplan/Step/Gate entities with gate state.,BACKEND_FEATURE_SLICE,TBD,Parser + fixture tests,SOW-016,OBJ-001;OBJ-002,M,,P1
+DEL-02-06,PKG-02,Workplan/LOOP_INIT parser,"`LOOP_INIT.md` loop identity, entrypoint and procedure SHA only; workplans as a declared historical grammar; no step/gate state is read from `LOOP_INIT.md` (gate state is re-sourced per SOW-001). Name ""Workplan/LOOP_INIT parser"" and path retained under SCA-005 (CP1-N); the label now overstates the live scope.",BACKEND_FEATURE_SLICE,TBD,Parser + fixture tests,SOW-016,OBJ-001;OBJ-002,M,M held under SCA-005: scope narrowed to `LOOP_INIT.md` identity plus the historical workplan grammar; may fall to S on re-assessment,P1
```

### A-18 — MODIFY DELIVERABLE `DEL-02-07`

DEL-02-07 description re-purposed to parity-peer reader (DriftFinding on census divergence); name/path retained, label drift recorded. Supersession binding: **NO**.

`Deliverables.csv` row `DEL-02-07` (replace):

```diff
-DEL-02-07,PKG-02,`adapter.yaml` feed-manifest consumer,Per-project `_harness/adapter.yaml` consumed as the feed manifest driving which feeds are read per loop.,BACKEND_FEATURE_SLICE,TBD,Manifest reader + fixture tests,SOW-017,OBJ-001;OBJ-002,S,,P1
+DEL-02-07,PKG-02,`adapter.yaml` feed-manifest consumer,"Per-project `_harness/adapter.yaml` read as a parity-peer input only: PEC's declared census population is compared with the harness `status_glob`, and divergence is reported as a DriftFinding; no longer the feed manifest (per-loop feed profiles in the PEC-owned registry, DEL-01-06, declare the feeds). Name ""`adapter.yaml` feed-manifest consumer"" and path retained under SCA-005 (CP1-N); the label no longer describes the role.",BACKEND_FEATURE_SLICE,TBD,Manifest reader + fixture tests,SOW-017,OBJ-001;OBJ-002,S,,P1
```

### A-19 — ADD DELIVERABLE `DEL-02-08`

ADD DEL-02-08 'Work-graph parser' (PKG-02, BACKEND_FEATURE_SLICE, M, P1, covers SOW-095, OBJ-001;OBJ-002) plus ContextBudgetQA row (M/MEDIUM), inserted after DEL-02-07. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §5 ADD DEL-02-08, DEL-02-09 (Seq 19, 20):

```diff
-| DEL-02-07 | `adapter.yaml` feed-manifest consumer | BACKEND_FEATURE_SLICE | S | P1 | SOW-017 |
+| DEL-02-07 | `adapter.yaml` feed-manifest consumer | BACKEND_FEATURE_SLICE | S | P1 | SOW-017 |
+| DEL-02-08 | Work-graph parser | BACKEND_FEATURE_SLICE | M | P1 | SOW-095 |
+| DEL-02-09 | MEMORY run-index parser | BACKEND_FEATURE_SLICE | S | P1 | SOW-096 |
```

`ContextBudgetQA.csv` row `DEL-02-08` (insert):

```diff
+DEL-02-08,PKG-02,M,MEDIUM,Hold as M; split profile-driven discovery and PR-to-merge resolution from the grammar only if the fixture classes prove adversarial,"M: a new grammar plus profile-driven discovery, PR-to-merge-commit resolution inputs and three pinned fixture classes; kept one cohesive parser slice"
```

`Deliverables.csv` row `DEL-02-08` (insert):

```diff
+DEL-02-08,PKG-02,Work-graph parser,"Content-minimal parser for `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md` (declared run-identity token, node IDs, closed-vocabulary node states, DEL bindings, PR numbers, hex SHAs, linked paths, per-state counts), discovered per the loop's declared feed profile; integration ref by default, local branch refs opt-in and labelled unintegrated; cited PR numbers resolved to local merge commits by read-only plumbing, unresolved-locally reported, never guessed. Node states are declared activity, never liveness; graph prose is never extracted.",BACKEND_FEATURE_SLICE,TBD,Parser + pinned golden-by-reference fixture suites for the three fixture classes (FC-1 receipt present; FC-2 evidence-only; FC-3 no AgentRuns record) + synthetic grammar-edge fixtures,SOW-095,OBJ-001;OBJ-002,M,"M: a new grammar plus profile-driven discovery, PR-to-merge-commit resolution inputs and three pinned fixture classes; kept one cohesive parser slice",P1
```

### A-20 — ADD DELIVERABLE `DEL-02-09`

ADD DEL-02-09 'MEMORY run-index parser' (PKG-02, BACKEND_FEATURE_SLICE, S, P1, covers SOW-096, OBJ-001;OBJ-002) plus ContextBudgetQA row (S/LOW), inserted after DEL-02-08. Supersession binding: **NO**.

`ContextBudgetQA.csv` row `DEL-02-09` (insert):

```diff
+DEL-02-09,PKG-02,S,LOW,None,
```

`Deliverables.csv` row `DEL-02-09` (insert):

```diff
+DEL-02-09,PKG-02,MEMORY run-index parser,"Parser for deliverable `MEMORY.md` run-index entries (run-ID tokens, dates, link targets) in the template `## Runs` table, the observed bullet form and the dated-heading form, as RunRecord join evidence; absence is a stated coverage limit; run descriptions are never extracted.",BACKEND_FEATURE_SLICE,TBD,"Parser + fixture tests (table, bullet and dated-heading forms)",SOW-096,OBJ-001;OBJ-002,S,,P1
```

### A-21 — MODIFY DELIVERABLE `DEL-03-03`

DEL-03-03 description adds the lag classes (terminal lag = trailing by method design; non-terminal graph-behind-Git = DriftFinding; historical surfaces never staleness). Supersession binding: **NO**.

`Deliverables.csv` row `DEL-03-03` (replace):

```diff
-DEL-03-03,PKG-03,Drift classification,"Classified drift between successive snapshots, reported as DriftFindings; sources never modified.",BACKEND_FEATURE_SLICE,TBD,Drift classifier + tests,SOW-019,OBJ-002,M,,P1
+DEL-03-03,PKG-03,Drift classification,"Classified drift between successive snapshots, reported as DriftFindings; sources never modified. Lag classes: terminal-node lag after the final-PR merge is ""trailing by method design"" (derived completion, not drift); non-terminal graph-behind-Git is a DriftFinding; unchanged historical surfaces are never staleness.",BACKEND_FEATURE_SLICE,TBD,Drift classifier + tests,SOW-019,OBJ-002,M,,P1
```

### A-22 — MODIFY DELIVERABLE `DEL-04-01`

DEL-04-01 description follows SOW-004; not designed around verify-before-rely and adds no reliance text. Supersession binding: **NO**.

`Deliverables.csv` row `DEL-04-01` (replace):

```diff
-DEL-04-01,PKG-04,Loop orientation return,"Per-loop orientation: newest applicable receipt, examined-through SHA, gate states, owner directions of record, open tranches/candidate briefs, parked lanes with unparking acts.",BACKEND_FEATURE_SLICE,TBD,Orientation builder + tests,SOW-004,OBJ-001,M,,P1
+DEL-04-01,PKG-04,Loop orientation return,"Per-loop orientation: newest applicable receipt over central receipts and ledgers, examined-through SHA, gate states from decisions, scope-change state and graph BLOCKED nodes, owner directions of record, open tranches/candidate briefs and parked lanes over graph READY/ACTIVE/BLOCKED nodes, each parked lane with its unparking act; terminal completion derived from local Git merge reachability of cited PRs, Explain-cited and advisory.",BACKEND_FEATURE_SLICE,TBD,Orientation builder + tests,SOW-004,OBJ-001,M,,P1
```

### A-34 — REMOVE DELIVERABLE `DEL-06-04`

REMOVE DEL-06-04 non-destructively: [RETIRED — SCA-005] row form in Deliverables/ContextBudgetQA/§5; Covers/Supports cleared; PhaseHint and envelope kept; _STATUS.md RETIRED at application; folder never deleted; ID reserved; PKG-06 keeps 5 active children; DEP-09-05-005 retired by dependency-extract. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §5 retire DEL-06-04 (Seq 34):

```diff
-| DEL-06-04 | Live hierarchy edges | BACKEND_FEATURE_SLICE | S | P4 | SOW-029 |
+| DEL-06-04 | Live hierarchy edges | BACKEND_FEATURE_SLICE | S | P4 | — **[RETIRED — SCA-005]** (was SOW-029) |
```

`ContextBudgetQA.csv` row `DEL-06-04` (replace):

```diff
-DEL-06-04,PKG-06,S,LOW,None,
+DEL-06-04,PKG-06,S,LOW,[RETIRED — SCA-005] None; row retained non-destructively,Retired under SCA-005 (R1 deferral); excluded from active envelope counts
```

`Deliverables.csv` row `DEL-06-04` (replace):

```diff
-DEL-06-04,PKG-06,Live hierarchy edges,Parent-to-child session edges from daemon and hook feeds.,BACKEND_FEATURE_SLICE,TBD,Hierarchy maintenance + tests,SOW-029,OBJ-003,S,,P4
+DEL-06-04,PKG-06,Live hierarchy edges,[RETIRED — SCA-005] Retired because SOW-029 is deferred OUT under R1 (trigger T-RT). Original description: Parent-to-child session edges from daemon and hook feeds.,BACKEND_FEATURE_SLICE,TBD,Hierarchy maintenance + tests,,,S,Retired row retained for register integrity; excluded from active envelope counts (SCA-005).,P4
```

### A-35 — REMOVE DELIVERABLE `DEL-07-02`

REMOVE DEL-07-02 non-destructively (same mechanics); PKG-07 keeps 2 active children (DEL-07-01, DEL-07-03). Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §5 retire DEL-07-02 (Seq 35):

```diff
-| DEL-07-02 | Daemon SSE subscriber bridge | BACKEND_FEATURE_SLICE | M | P4 | SOW-035 |
+| DEL-07-02 | Daemon SSE subscriber bridge | BACKEND_FEATURE_SLICE | M | P4 | — **[RETIRED — SCA-005]** (was SOW-035) |
```

`ContextBudgetQA.csv` row `DEL-07-02` (replace):

```diff
-DEL-07-02,PKG-07,M,LOW,None; single cohesive slice,
+DEL-07-02,PKG-07,M,LOW,[RETIRED — SCA-005] None; row retained non-destructively,Retired under SCA-005 (R1 deferral); excluded from active envelope counts
```

`Deliverables.csv` row `DEL-07-02` (replace):

```diff
-DEL-07-02,PKG-07,Daemon SSE subscriber bridge,"Declared, attributable subscriber over the runtime daemon's SSE feed.",BACKEND_FEATURE_SLICE,TBD,Bridge + tests,SOW-035,,M,,P4
+DEL-07-02,PKG-07,Daemon SSE subscriber bridge,"[RETIRED — SCA-005] Retired because SOW-035 is deferred OUT under R1 (trigger T-RT). Original description: Declared, attributable subscriber over the runtime daemon's SSE feed.",BACKEND_FEATURE_SLICE,TBD,Bridge + tests,,,M,Retired row retained for register integrity; excluded from active envelope counts (SCA-005).,P4
```

### A-36 — REMOVE DELIVERABLE `DEL-07-05`

REMOVE DEL-07-05 non-destructively (same mechanics); PKG-07 keeps 2 active children. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §5 retire DEL-07-05 (Seq 36):

```diff
-| DEL-07-05 | Shared-runtime client seam (v2) | BACKEND_FEATURE_SLICE | M | P3 | SOW-087 |
+| DEL-07-05 | Shared-runtime client seam (v2) | BACKEND_FEATURE_SLICE | M | P3 | — **[RETIRED — SCA-005]** (was SOW-087) |
```

`ContextBudgetQA.csv` row `DEL-07-05` (replace):

```diff
-DEL-07-05,PKG-07,M,LOW,None; single cohesive slice,"M is provisional: the seam's artifact shape follows the D-PEC-56 concept, not a PEC-*-NNN requirement; re-envelope at WORKING_ITEMS activation if the shape proves larger"
+DEL-07-05,PKG-07,M,LOW,[RETIRED — SCA-005] None; row retained non-destructively,"M is provisional: the seam's artifact shape follows the D-PEC-56 concept, not a PEC-*-NNN requirement; re-envelope at WORKING_ITEMS activation if the shape proves larger; Retired under SCA-005 (R1 deferral); excluded from active envelope counts"
```

`Deliverables.csv` row `DEL-07-05` (replace):

```diff
-DEL-07-05,PKG-07,Shared-runtime client seam (v2),The D-PEC-56 client-seam concept reimplemented against v2 entities.,BACKEND_FEATURE_SLICE,TBD,Client seam module + tests,SOW-087,,M,"M is provisional: the seam's artifact shape follows the D-PEC-56 concept, not a PEC-*-NNN requirement; re-envelope at WORKING_ITEMS activation if the shape proves larger",P3
+DEL-07-05,PKG-07,Shared-runtime client seam (v2),[RETIRED — SCA-005] Retired because SOW-087 is deferred OUT under R1 (trigger T-RT). Original description: The D-PEC-56 client-seam concept reimplemented against v2 entities.,BACKEND_FEATURE_SLICE,TBD,Client seam module + tests,,,M,"M is provisional: the seam's artifact shape follows the D-PEC-56 concept, not a PEC-*-NNN requirement; re-envelope at WORKING_ITEMS activation if the shape proves larger. Retired row retained for register integrity; excluded from active envelope counts (SCA-005).",P3
```

### A-78 — REMOVE DELIVERABLE `DEL-07-04`

REMOVE DEL-07-04 non-destructively (R1 mechanics); outgoing DEP-07-04-003/004 retire with its register (dependency-extract); consumer mirrors in DEL-00-02 and DEL-07-01 refreshed; PKG-07 keeps 2 active children. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §5 retire DEL-07-04 (Seq 78):

```diff
-| DEL-07-04 | cmux socket adapter (optional) | BACKEND_FEATURE_SLICE | M | P4 | SOW-037 |
+| DEL-07-04 | cmux socket adapter (optional) | BACKEND_FEATURE_SLICE | M | P4 | — **[RETIRED — SCA-005]** (was SOW-037) |
```

`ContextBudgetQA.csv` row `DEL-07-04` (replace):

```diff
-DEL-07-04,PKG-07,M,LOW,None; single cohesive slice,
+DEL-07-04,PKG-07,M,LOW,[RETIRED — SCA-005] None; row retained non-destructively,Retired under SCA-005 (cmux deferral); excluded from active envelope counts
```

`Deliverables.csv` row `DEL-07-04` (replace):

```diff
-DEL-07-04,PKG-07,cmux socket adapter (optional),Optional declared enricher over the cmux socket API; absence changes nothing.,BACKEND_FEATURE_SLICE,TBD,Adapter + tests,SOW-037,,M,,P4
+DEL-07-04,PKG-07,cmux socket adapter (optional),[RETIRED — SCA-005] Retired because SOW-037 is deferred OUT by the owner's 2026-09-24 cmux deferral. Original description: Optional declared enricher over the cmux socket API; absence changes nothing.,BACKEND_FEATURE_SLICE,TBD,Adapter + tests,,,M,Retired row retained for register integrity; excluded from active envelope counts (SCA-005).,P4
```

### A-37 — MODIFY DELIVERABLE `DEL-06-01`

DEL-06-01 description: sessions only from an explicitly authorized hooks consumer; identity/lifecycle Runtime-owned per application. Supersession binding: **NO**.

`Deliverables.csv` row `DEL-06-01` (replace):

```diff
-DEL-06-01,PKG-06,Session presence records,"Harness-reported session records (kind, engine/model attribution, role, loop/package binding, declared write scopes); identity/lifecycle stay daemon-owned.",BACKEND_FEATURE_SLICE,TBD,Presence writer + tests,SOW-026,OBJ-003,M,,P3
+DEL-06-01,PKG-06,Session presence records,"Harness-reported session records (kind, engine/model attribution, role, loop/package binding, declared write scopes), arriving only from an explicitly authorized hooks consumer; identity/lifecycle are Runtime-owned per application (C13).",BACKEND_FEATURE_SLICE,TBD,Presence writer + tests,SOW-026,OBJ-003,M,,P3
```

### A-38 — MODIFY DELIVERABLE `DEL-09-05`

DEL-09-05 description follows SOW-049 (worktree and declared-activity board; live hierarchy deferred); DEP-09-05-005 retirement routed to dependency-extract. Supersession binding: **NO**.

`Deliverables.csv` row `DEL-09-05` (replace):

```diff
-DEL-09-05,PKG-09,Presence board,Sessions x worktrees x live hierarchy with heartbeat age and advisory overlap warnings.,UX_UI_SLICE,TBD,View + tests,SOW-049,OBJ-003;OBJ-004,M,,P3
+DEL-09-05,PKG-09,Presence board,"Sessions (when hook-reported) x worktrees x graph-declared activity with heartbeat/scan age and advisory overlap warnings; live hierarchy deferred with SOW-029; declared activity is record tier, never liveness.",UX_UI_SLICE,TBD,View + tests,SOW-049,OBJ-003;OBJ-004,M,,P3
```

### A-39 — MODIFY DELIVERABLE `DEL-00-02`

DEL-00-02 description drops 'daemon' (hooks CLI the only remaining bridge); envelope notes restate the contract-home option path. Supersession binding: **NO**.

`ContextBudgetQA.csv` row `DEL-00-02` (replace):

```diff
-DEL-00-02,PKG-00,M,MEDIUM,Hold envelope; re-assess on the linked OI's ruling,OI-009 keeps the contract home open; local schema + pinned mirror until ruled — a shared-runtime ruling moves the home under its own instrument (SOW-074)
+DEL-00-02,PKG-00,M,MEDIUM,Hold envelope; re-assess on the linked OI's ruling,OI-009 keeps the contract home open; local schema + pinned mirror until ruled — a ruling for the shared Runtime contracts home (`projects/chirality-runtime/packages/contracts`) moves the home under its own instrument (SOW-074)
```

`Deliverables.csv` row `DEL-00-02` (replace):

```diff
-DEL-00-02,PKG-00,Event-contract schema v1,"Versioned event contract types consumable by daemon, hooks CLI, and adapters; PEC-local schema with pinned-mirror posture pending OI-009; additive evolution. Published one phase ahead of its P3 consumers (DEL-07-01/-03) per the PKG-00 publish/consume mechanic.",API_CONTRACT,TBD,Schema definitions + contract tests + versioning note,SOW-034,,M,OI-009 keeps the contract home open; local schema + pinned mirror until ruled — a shared-runtime ruling moves the home under its own instrument (SOW-074),P2
+DEL-00-02,PKG-00,Event-contract schema v1,"Versioned event contract types consumable by the hooks CLI bridge, the only remaining bridge; PEC-local schema with pinned-mirror posture pending OI-009; additive evolution. Published one phase ahead of its P3 consumers (DEL-07-01/-03) per the PKG-00 publish/consume mechanic.",API_CONTRACT,TBD,Schema definitions + contract tests + versioning note,SOW-034,OBJ-003,M,OI-009 keeps the contract home open; local schema + pinned mirror until ruled — a ruling for the shared Runtime contracts home (`projects/chirality-runtime/packages/contracts`) moves the home under its own instrument (SOW-074),P2
```

### A-40 — MODIFY DELIVERABLE `DEL-08-01`

DEL-08-01 envelope notes and ContextBudgetQA notes: OI-006 re-expressed (app-private Runtime token registries; no daemon registry to reuse); MEDIUM retained. Supersession binding: **NO**.

`ContextBudgetQA.csv` row `DEL-08-01` (replace):

```diff
-DEL-08-01,PKG-08,M,MEDIUM,Hold envelope; re-assess on the linked OI's ruling,"OI-006 determines the token mechanism (PEC-local vs daemon registry); the socket+access-class core is stable either way, but the auth half may be reworked on ruling"
+DEL-08-01,PKG-08,M,MEDIUM,Hold envelope; re-assess on the linked OI's ruling,"OI-006 determines the PEC-local token mechanism (Runtime token registries are private to each application's Runtime instance, so no shared registry exists to reuse); the socket+access-class core is stable either way, but the auth half may be reworked on ruling"
```

`Deliverables.csv` row `DEL-08-01` (replace):

```diff
-DEL-08-01,PKG-08,Unix-socket server + token-scoped access,"Local-only Unix-socket binding with token-scoped access classes (owner, harness, admin); auth-reuse choice tracked by OI-006.",SECURITY_CONTROL,TBD,Socket server + auth + tests,SOW-003;SOW-040,OBJ-001,M,"OI-006 determines the token mechanism (PEC-local vs daemon registry); the socket+access-class core is stable either way, but the auth half may be reworked on ruling",P1
+DEL-08-01,PKG-08,Unix-socket server + token-scoped access,"Local-only Unix-socket binding with token-scoped access classes (owner, harness, admin); auth-reuse choice tracked by OI-006.",SECURITY_CONTROL,TBD,Socket server + auth + tests,SOW-003;SOW-040,OBJ-001,M,"OI-006 determines the PEC-local token mechanism (Runtime token registries are private to each application's Runtime instance, so no shared registry exists to reuse); the socket+access-class core is stable either way, but the auth half may be reworked on ruling",P1
```

## 4. Unit Ledger — Scope Ledger (statements, status, lineage)

### A-01 — MODIFY OTHER `SOW-001`

SOW-001 statement re-sourced: entity list gains WorkGraph/WorkNode; Workplan/Step/Gate a declared historical-grammar entity; Receipt and RunRecord sources re-expressed; 'remaining items' per-loop optional (Notes). Supersession binding: **YES**.

`SOFTWARE_DECOMP.md` — §2.1 SOW-001 (Seq 1):

```diff
-| SOW-001 | IN | Implement the record-tier entity model: Loop, Workplan/Step/Gate, Receipt, DecisionRow, Fence, Package/Deliverable, DependencyEdge, RunRecord, CandidateBrief, OrientationSnapshot, DriftFinding | §7.1 | Receipt field availability is per-loop (PEC-ORI-006 limits apply) |
+| SOW-001 | IN | Implement the record-tier entity model: Loop, Workplan/Step/Gate (declared historical-grammar entity; gate state re-sourced from decision registers, scope-change pointers and graph BLOCKED nodes), Receipt (ledger entries and central `RECEIPT.md`), DecisionRow, Fence, Package/Deliverable, DependencyEdge, RunRecord (from central receipts, work graphs and the MEMORY run index; JSON run evidence historical), CandidateBrief, OrientationSnapshot, DriftFinding, WorkGraph/WorkNode | §7.1 | Receipt field availability is per-loop (PEC-ORI-006 limits apply); "remaining items" is a per-loop optional field, not a required one |
```

`ScopeLedger.csv` row `SOW-001` (replace):

```diff
-SOW-001,IN,"Implement the record-tier entity model: Loop, Workplan/Step/Gate, Receipt, DecisionRow, Fence, Package/Deliverable, DependencyEdge, RunRecord, CandidateBrief, OrientationSnapshot, DriftFinding",§7.1,PKG-01,DEL-01-01,OBJ-001;OBJ-002,,FALSE,Receipt field availability is per-loop (PEC-ORI-006 limits apply)
+SOW-001,IN,"Implement the record-tier entity model: Loop, Workplan/Step/Gate (declared historical-grammar entity; gate state re-sourced from decision registers, scope-change pointers and graph BLOCKED nodes), Receipt (ledger entries and central `RECEIPT.md`), DecisionRow, Fence, Package/Deliverable, DependencyEdge, RunRecord (from central receipts, work graphs and the MEMORY run index; JSON run evidence historical), CandidateBrief, OrientationSnapshot, DriftFinding, WorkGraph/WorkNode",§7.1,PKG-01,DEL-01-01,OBJ-001;OBJ-002,SCA-005,FALSE,"Receipt field availability is per-loop (PEC-ORI-006 limits apply); ""remaining items"" is a per-loop optional field, not a required one"
```

### A-02 — MODIFY OTHER `SOW-004`

SOW-004 statement re-sourced over central receipts, graph READY/ACTIVE/BLOCKED nodes and Git-derived terminal completion (Explain-cited, advisory); no reliance text. Supersession binding: **YES**.

`SOFTWARE_DECOMP.md` — §2.1 SOW-004 (Seq 2):

```diff
-| SOW-004 | IN | Serve per-loop orientation: newest applicable receipt, examined-through SHA, gate states, owner directions of record, open tranches/candidate briefs, parked lanes each with its unparking owner action | PEC-ORI-001 | |
+| SOW-004 | IN | Serve per-loop orientation: newest applicable receipt over central receipts and ledgers, examined-through SHA, gate states from decisions, scope-change state and graph BLOCKED nodes, owner directions of record, open tranches/candidate briefs and parked lanes over graph READY/ACTIVE/BLOCKED nodes, each parked lane with its unparking owner action; terminal completion derived from local Git merge reachability of cited PRs, Explain-cited and advisory | PEC-ORI-001 | |
```

`ScopeLedger.csv` row `SOW-004` (replace):

```diff
-SOW-004,IN,"Serve per-loop orientation: newest applicable receipt, examined-through SHA, gate states, owner directions of record, open tranches/candidate briefs, parked lanes each with its unparking owner action",PEC-ORI-001,PKG-04,DEL-04-01,OBJ-001,,FALSE,
+SOW-004,IN,"Serve per-loop orientation: newest applicable receipt over central receipts and ledgers, examined-through SHA, gate states from decisions, scope-change state and graph BLOCKED nodes, owner directions of record, open tranches/candidate briefs and parked lanes over graph READY/ACTIVE/BLOCKED nodes, each parked lane with its unparking owner action; terminal completion derived from local Git merge reachability of cited PRs, Explain-cited and advisory",PEC-ORI-001,PKG-04,DEL-04-01,OBJ-001,SCA-005,FALSE,
```

### A-03 — MODIFY OTHER `SOW-013`

SOW-013 statement: two grammar generations of the Receipt feed kind (ledgers + central RECEIPT.md); receipt-contract-v2 marker replaces 'D-APP-57 contract where adopted'. Supersession binding: **YES**.

`SOFTWARE_DECOMP.md` — §2.1 SOW-013 (Seq 3):

```diff
-| SOW-013 | IN | Parse `LOOP_RECEIPTS.md` ledgers under per-loop grammar, including the D-APP-57 contract where a ledger has adopted it | PEC-RCN-002 | Per-loop coverage limits stated (SOW-009) |
+| SOW-013 | IN | Parse receipts as two grammar generations of one Receipt feed kind: `LOOP_RECEIPTS.md` ledgers under per-loop grammar (live for PEC/Root/Runtime/Bridge; declared historical for App/Piping), including the receipt-contract-v2 marker where a ledger carries it, and central `execution/_Coordination/AgentRuns/<RunID>/RECEIPT.md` receipts | PEC-RCN-002 | Per-loop coverage limits stated (SOW-009); central receipts stay in this item (DL-4 unchanged) |
```

`ScopeLedger.csv` row `SOW-013` (replace):

```diff
-SOW-013,IN,"Parse `LOOP_RECEIPTS.md` ledgers under per-loop grammar, including the D-APP-57 contract where a ledger has adopted it",PEC-RCN-002,PKG-02,DEL-02-03,OBJ-001;OBJ-002,,FALSE,Per-loop coverage limits stated (SOW-009)
+SOW-013,IN,"Parse receipts as two grammar generations of one Receipt feed kind: `LOOP_RECEIPTS.md` ledgers under per-loop grammar (live for PEC/Root/Runtime/Bridge; declared historical for App/Piping), including the receipt-contract-v2 marker where a ledger carries it, and central `execution/_Coordination/AgentRuns/<RunID>/RECEIPT.md` receipts",PEC-RCN-002,PKG-02,DEL-02-03,OBJ-001;OBJ-002,SCA-005,FALSE,Per-loop coverage limits stated (SOW-009); central receipts stay in this item (DL-4 unchanged)
```

### A-04 — MODIFY OTHER `SOW-014`

SOW-014 statement/Notes: JSON run evidence a declared historical grammar (App/Piping), current-by-own-practice (PEC/Root); Runtime service user-data never an input. Supersession binding: **YES**.

`SOFTWARE_DECOMP.md` — §2.1 SOW-014 (Seq 4):

```diff
-| SOW-014 | IN | Parse run-evidence JSON: `STATUS.json` and `RUNTIME_SUMMARY.json` under `execution/**` | PEC-RCN-002, §7.1 RunRecord | Daemon user-data state is presence-tier only |
+| SOW-014 | IN | Parse run-evidence JSON: `STATUS.json` and `RUNTIME_SUMMARY.json` under `execution/**`, as a declared historical grammar for App/Piping and current-by-own-practice for PEC/Root | PEC-RCN-002, §7.1 RunRecord | Application-owned Runtime service user-data is operational, never an input (D-GOV-43 A2; D-GOV-20 item 5) |
```

`ScopeLedger.csv` row `SOW-014` (replace):

```diff
-SOW-014,IN,Parse run-evidence JSON: `STATUS.json` and `RUNTIME_SUMMARY.json` under `execution/**`,"PEC-RCN-002, §7.1 RunRecord",PKG-02,DEL-02-04,OBJ-001;OBJ-002,,FALSE,Daemon user-data state is presence-tier only
+SOW-014,IN,"Parse run-evidence JSON: `STATUS.json` and `RUNTIME_SUMMARY.json` under `execution/**`, as a declared historical grammar for App/Piping and current-by-own-practice for PEC/Root","PEC-RCN-002, §7.1 RunRecord",PKG-02,DEL-02-04,OBJ-001;OBJ-002,SCA-005,FALSE,"Application-owned Runtime service user-data is operational, never an input (D-GOV-43 A2; D-GOV-20 item 5)"
```

### A-05 — MODIFY OTHER `SOW-015`

SOW-015 statement/Notes: WORK_GRAPH.json a declared historical grammar; Markdown work-graph dependencies via SOW-095. Supersession binding: **YES**.

`SOFTWARE_DECOMP.md` — §2.1 SOW-015 (Seq 5):

```diff
-| SOW-015 | IN | Parse dependency registers: `Dependencies.csv` and `WORK_GRAPH.json` | PEC-RCN-002, §7.1 DependencyEdge | `WORK_GRAPH.json` feeds DependencyEdge, not RunRecord |
+| SOW-015 | IN | Parse dependency registers: `Dependencies.csv`, and `WORK_GRAPH.json` as a declared historical grammar for App/Piping | PEC-RCN-002, §7.1 DependencyEdge | `WORK_GRAPH.json` feeds DependencyEdge, not RunRecord; Markdown work-graph dependencies arrive through SOW-095 |
```

`ScopeLedger.csv` row `SOW-015` (replace):

```diff
-SOW-015,IN,Parse dependency registers: `Dependencies.csv` and `WORK_GRAPH.json`,"PEC-RCN-002, §7.1 DependencyEdge",PKG-02,DEL-02-05,OBJ-001;OBJ-002,,FALSE,"`WORK_GRAPH.json` feeds DependencyEdge, not RunRecord"
+SOW-015,IN,"Parse dependency registers: `Dependencies.csv`, and `WORK_GRAPH.json` as a declared historical grammar for App/Piping","PEC-RCN-002, §7.1 DependencyEdge",PKG-02,DEL-02-05,OBJ-001;OBJ-002,SCA-005,FALSE,"`WORK_GRAPH.json` feeds DependencyEdge, not RunRecord; Markdown work-graph dependencies arrive through SOW-095"
```

### A-06 — MODIFY OTHER `SOW-016`

SOW-016 statement narrowed to LOOP_INIT.md identity, entrypoint and procedure SHA; workplans historical; no step/gate state. Supersession binding: **YES**.

`SOFTWARE_DECOMP.md` — §2.1 SOW-016 (Seq 6):

```diff
-| SOW-016 | IN | Parse workplans and `LOOP_INIT.md` protocol files | PEC-RCN-002 | |
+| SOW-016 | IN | Parse `LOOP_INIT.md` for loop identity, entrypoint and procedure SHA only, and workplans as a declared historical grammar; no step/gate state is read from `LOOP_INIT.md` | PEC-RCN-002 | |
```

`ScopeLedger.csv` row `SOW-016` (replace):

```diff
-SOW-016,IN,Parse workplans and `LOOP_INIT.md` protocol files,PEC-RCN-002,PKG-02,DEL-02-06,OBJ-001;OBJ-002,,FALSE,
+SOW-016,IN,"Parse `LOOP_INIT.md` for loop identity, entrypoint and procedure SHA only, and workplans as a declared historical grammar; no step/gate state is read from `LOOP_INIT.md`",PEC-RCN-002,PKG-02,DEL-02-06,OBJ-001;OBJ-002,SCA-005,FALSE,
```

### A-07 — MODIFY OTHER `SOW-017`

SOW-017 statement/Notes: adapter.yaml a parity-peer input only (census population vs status_glob), no longer the feed manifest. Supersession binding: **YES**.

`SOFTWARE_DECOMP.md` — §2.1 SOW-017 (Seq 7):

```diff
-| SOW-017 | IN | Consume per-project `_harness/adapter.yaml` as the feed manifest | PEC-RCN-002 | |
+| SOW-017 | IN | Read per-project `_harness/adapter.yaml` as a parity-peer input only, comparing PEC's declared census population with the harness `status_glob`; report divergence as a DriftFinding | PEC-RCN-002 | No longer the feed manifest: per-loop feed profiles in the PEC-owned registry declare the feeds (SOW-077, SOW-094) |
```

`ScopeLedger.csv` row `SOW-017` (replace):

```diff
-SOW-017,IN,Consume per-project `_harness/adapter.yaml` as the feed manifest,PEC-RCN-002,PKG-02,DEL-02-07,OBJ-001;OBJ-002,,FALSE,
+SOW-017,IN,"Read per-project `_harness/adapter.yaml` as a parity-peer input only, comparing PEC's declared census population with the harness `status_glob`; report divergence as a DriftFinding",PEC-RCN-002,PKG-02,DEL-02-07,OBJ-001;OBJ-002,SCA-005,FALSE,"No longer the feed manifest: per-loop feed profiles in the PEC-owned registry declare the feeds (SOW-077, SOW-094)"
```

### A-08 — ADD OTHER `SOW-095`

ADD SOW-095 (IN; PKG-02 / DEL-02-08 / OBJ-001;OBJ-002): work-graph parser scope item, appended after SOW-094. Supersession binding: **YES**.

`SOFTWARE_DECOMP.md` — §2 intro (Seq 8/9 note):

```diff
-verification and SOW-093..094 during the Phase 6 verification (DL-14);
-IDs are append-only, so family ordering is not semantic.
+verification and SOW-093..094 during the Phase 6 verification (DL-14);
+SOW-095..096 were appended under SCA-005 from the PRD v2.3 feed list
+(DL-20). IDs are append-only, so family ordering is not semantic.
```

`SOFTWARE_DECOMP.md` — §2.1 ADD SOW-095, SOW-096 (Seq 8, 9):

```diff
-| SOW-094 | IN | Maintain the loop-registration configuration naming the loops PEC serves and each row's feed-profile selection (local config default) | §12 P2, PEC-DSH-002 | Local JSON configuration is the implementation basis for the long-term PEC-owned service registry confirmed by D-PEC-78; the core port keeps filesystem and JSON details replaceable. PEC's own `pec` row declares the `remaining-loop` profile now; its later migration is one owner-gated row change under its own ruling (D-PEC-86 I-7) |
+| SOW-094 | IN | Maintain the loop-registration configuration naming the loops PEC serves and each row's feed-profile selection (local config default) | §12 P2, PEC-DSH-002 | Local JSON configuration is the implementation basis for the long-term PEC-owned service registry confirmed by D-PEC-78; the core port keeps filesystem and JSON details replaceable. PEC's own `pec` row declares the `remaining-loop` profile now; its later migration is one owner-gated row change under its own ruling (D-PEC-86 I-7) |
+| SOW-095 | IN | Parse `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md` content-minimally (declared run-identity token, node IDs, closed-vocabulary node states, DEL bindings, PR numbers, hex SHAs, linked paths, per-state counts), discovered per the loop's declared feed profile; read the integration ref by default, with local branch refs opt-in and labelled unintegrated; resolve cited PR numbers to local merge commits by read-only plumbing, reporting unresolved-locally and never guessing | PEC-RCN-002 (PRD v2.3), §7.1 WorkGraph/WorkNode | New feed kind under SCA-005 (DL-4, DL-20); node states are declared activity, never liveness; objectives per the DL-17 parser precedent |
+| SOW-096 | IN | Parse deliverable `MEMORY.md` run-index entries (run-ID tokens, dates, link targets) in the template `## Runs` table, the observed bullet form and the dated-heading form, as RunRecord join evidence | PEC-RCN-002 (PRD v2.3), §7.1 RunRecord | New feed kind under SCA-005 (DL-4, DL-20); absence is a stated coverage limit (SOW-009); objectives per the DL-17 parser precedent |
```

`ScopeLedger.csv` row `SOW-095` (insert):

```diff
+SOW-095,IN,"Parse `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md` content-minimally (declared run-identity token, node IDs, closed-vocabulary node states, DEL bindings, PR numbers, hex SHAs, linked paths, per-state counts), discovered per the loop's declared feed profile; read the integration ref by default, with local branch refs opt-in and labelled unintegrated; resolve cited PR numbers to local merge commits by read-only plumbing, reporting unresolved-locally and never guessing","PEC-RCN-002 (PRD v2.3), §7.1 WorkGraph/WorkNode",PKG-02,DEL-02-08,OBJ-001;OBJ-002,SCA-005,FALSE,"New feed kind under SCA-005 (DL-4, DL-20); node states are declared activity, never liveness; objectives per the DL-17 parser precedent"
```

### A-09 — ADD OTHER `SOW-096`

ADD SOW-096 (IN; PKG-02 / DEL-02-09 / OBJ-001;OBJ-002): MEMORY run-index parser scope item, appended after SOW-095. Supersession binding: **YES**.

`ScopeLedger.csv` row `SOW-096` (insert):

```diff
+SOW-096,IN,"Parse deliverable `MEMORY.md` run-index entries (run-ID tokens, dates, link targets) in the template `## Runs` table, the observed bullet form and the dated-heading form, as RunRecord join evidence","PEC-RCN-002 (PRD v2.3), §7.1 RunRecord",PKG-02,DEL-02-09,OBJ-001;OBJ-002,SCA-005,FALSE,"New feed kind under SCA-005 (DL-4, DL-20); absence is a stated coverage limit (SOW-009); objectives per the DL-17 parser precedent"
```

### A-10 — MODIFY OTHER `SOW-077`

SOW-077 statement/Notes: 'strict, versioned' registry with closed PEC-versioned feed-profile declarations per row; schema v2 + RegisteredLoop field via a later D-PEC source packet within D-PEC-78 O-A. Supersession binding: **YES**.

`SOFTWARE_DECOMP.md` — §2.1 SOW-077 (Seq 10):

```diff
-| SOW-077 | IN | Maintain the PEC-owned long-term service registry naming the loop locators PEC serves through the strict version-1 JSON/schema paths and core-owned typed LoopRegistry port | §16.3, D-PEC-78 | D-PEC-78 O-A: PEC owns only its configured service set; each listed loop remains authoritative for its own entrypoint and truth; later row changes are owner-gated PEC configuration changes; no governed act depends on PEC or the registry |
+| SOW-077 | IN | Maintain the PEC-owned long-term service registry naming the loop locators PEC serves through the strict, versioned JSON/schema paths and core-owned typed LoopRegistry port, each row declaring a closed, PEC-versioned feed profile (profile ID, version, live/historical, basis citation to the loop's own record) | §16.3, D-PEC-78 | D-PEC-78 O-A: PEC owns only its configured service set; each listed loop remains authoritative for its own entrypoint and truth; later row changes are owner-gated PEC configuration changes; no governed act depends on PEC or the registry. A feed profile is PEC's reading hypothesis, never the loop's truth; feed-profile declarations need a strict schema v2 plus a `RegisteredLoop` port field through a later D-PEC source packet (no `v2/**` write here), within D-PEC-78 O-A (version 1 remains strict; supplementary extension, no supersession) |
```

`ScopeLedger.csv` row `SOW-077` (replace):

```diff
-SOW-077,IN,Maintain the PEC-owned long-term service registry naming the loop locators PEC serves through the strict version-1 JSON/schema paths and core-owned typed LoopRegistry port,"§16.3, D-PEC-78",PKG-01,DEL-01-06,OBJ-004,D-PEC-78,FALSE,D-PEC-78 O-A: PEC owns only its configured service set; each listed loop remains authoritative for its own entrypoint and truth; later row changes are owner-gated PEC configuration changes; no governed act depends on PEC or the registry
+SOW-077,IN,"Maintain the PEC-owned long-term service registry naming the loop locators PEC serves through the strict, versioned JSON/schema paths and core-owned typed LoopRegistry port, each row declaring a closed, PEC-versioned feed profile (profile ID, version, live/historical, basis citation to the loop's own record)","§16.3, D-PEC-78",PKG-01,DEL-01-06,OBJ-004,D-PEC-78; SCA-005,FALSE,"D-PEC-78 O-A: PEC owns only its configured service set; each listed loop remains authoritative for its own entrypoint and truth; later row changes are owner-gated PEC configuration changes; no governed act depends on PEC or the registry. A feed profile is PEC's reading hypothesis, never the loop's truth; feed-profile declarations need a strict schema v2 plus a `RegisteredLoop` port field through a later D-PEC source packet (no `v2/**` write here), within D-PEC-78 O-A (version 1 remains strict; supplementary extension, no supersession)"
```

### A-11 — MODIFY OTHER `SOW-094`

SOW-094 statement/Notes: per-row feed-profile selection; PEC's own row declares remaining-loop now, migration later as one owner-gated row change. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §2.1 SOW-094 (Seq 11):

```diff
-| SOW-094 | IN | Maintain the loop-registration configuration naming the loops PEC serves (local config default) | §12 P2, PEC-DSH-002 | Local JSON configuration is the implementation basis for the long-term PEC-owned service registry confirmed by D-PEC-78; the core port keeps filesystem and JSON details replaceable |
+| SOW-094 | IN | Maintain the loop-registration configuration naming the loops PEC serves and each row's feed-profile selection (local config default) | §12 P2, PEC-DSH-002 | Local JSON configuration is the implementation basis for the long-term PEC-owned service registry confirmed by D-PEC-78; the core port keeps filesystem and JSON details replaceable. PEC's own `pec` row declares the `remaining-loop` profile now; its later migration is one owner-gated row change under its own ruling (D-PEC-86 I-7) |
```

`ScopeLedger.csv` row `SOW-094` (replace):

```diff
-SOW-094,IN,Maintain the loop-registration configuration naming the loops PEC serves (local config default),"§12 P2, PEC-DSH-002",PKG-01,DEL-01-06,OBJ-004,D-PEC-78,FALSE,Local JSON configuration is the implementation basis for the long-term PEC-owned service registry confirmed by D-PEC-78; the core port keeps filesystem and JSON details replaceable
+SOW-094,IN,Maintain the loop-registration configuration naming the loops PEC serves and each row's feed-profile selection (local config default),"§12 P2, PEC-DSH-002",PKG-01,DEL-01-06,OBJ-004,D-PEC-78; SCA-005,FALSE,Local JSON configuration is the implementation basis for the long-term PEC-owned service registry confirmed by D-PEC-78; the core port keeps filesystem and JSON details replaceable. PEC's own `pec` row declares the `remaining-loop` profile now; its later migration is one owner-gated row change under its own ruling (D-PEC-86 I-7)
```

### A-28 — MODIFY OTHER `SOW-026`

SOW-026 Notes: session identity/lifecycle Runtime-owned per application; sessions only from an explicitly authorized hooks consumer; statement unchanged. Supersession binding: **YES**.

`SOFTWARE_DECOMP.md` — §2.1 SOW-026 (Seq 28):

```diff
-| SOW-026 | IN | Record presence for harness-reported sessions: harness kind, engine/model attribution when known, role, loop/package binding, declared write scopes | PEC-PRS-001 | Session identity/lifecycle stay daemon-owned (C13) |
+| SOW-026 | IN | Record presence for harness-reported sessions: harness kind, engine/model attribution when known, role, loop/package binding, declared write scopes | PEC-PRS-001 | Session identity/lifecycle are Runtime-owned per application (C13); sessions enter PEC only from an explicitly authorized hooks consumer |
```

`ScopeLedger.csv` row `SOW-026` (replace):

```diff
-SOW-026,IN,"Record presence for harness-reported sessions: harness kind, engine/model attribution when known, role, loop/package binding, declared write scopes",PEC-PRS-001,PKG-06,DEL-06-01,OBJ-003,,FALSE,Session identity/lifecycle stay daemon-owned (C13)
+SOW-026,IN,"Record presence for harness-reported sessions: harness kind, engine/model attribution when known, role, loop/package binding, declared write scopes",PEC-PRS-001,PKG-06,DEL-06-01,OBJ-003,SCA-005,FALSE,Session identity/lifecycle are Runtime-owned per application (C13); sessions enter PEC only from an explicitly authorized hooks consumer
```

### A-29 — MODIFY OTHER `SOW-029`

SOW-029 IN -> OUT **Deferred** (trigger T-RT); PackageID/DeliverableIDs/ObjectiveIDs cleared; row moves §2.1 -> §2.2. Supersession binding: **YES**.

`SOFTWARE_DECOMP.md` — §2.1 remove SOW-029 (moves to §2.2; Seq 29):

```diff
-| SOW-029 | IN | Maintain live parent→child hierarchy edges from daemon and hook feeds | PEC-PRS-004 | |
```

`SOFTWARE_DECOMP.md` — §2.2 intro (Seq 29-31, 77):

```diff
-Rows sourced from §4.2 are **permanent non-goals**. Rows marked *Deferred*
-in Notes are not permanent: they await their own instruments (a §16 ruling,
-a separate packet, or a cross-loop coordination act) and are excluded from
-this decomposition only.
+Rows sourced from §4.2 are **permanent non-goals**. Rows marked *Deferred*
+in Notes are not permanent: they await their own instruments (a §16 ruling,
+a separate packet, a cross-loop coordination act, trigger T-RT, or a later
+owner direction) and are excluded from this decomposition only. SOW-029,
+SOW-035, SOW-037 and SOW-087 moved here from §2.1 under SCA-005 (DL-20).
```

`SOFTWARE_DECOMP.md` — §2.2 append SOW-029/035/037/087 after SOW-092:

```diff
-| SOW-092 | OUT | Changes to `chirality.project.json` or project identity | §13 | No work: "Continue unchanged" — recorded so coverage is explicit; the former daemon-registration clause was dropped under SCA-005 (retired per-user daemon, D-GOV-20) |
+| SOW-092 | OUT | Changes to `chirality.project.json` or project identity | §13 | No work: "Continue unchanged" — recorded so coverage is explicit; the former daemon-registration clause was dropped under SCA-005 (retired per-user daemon, D-GOV-20) |
+| SOW-029 | OUT | Maintain live parent→child hierarchy edges from daemon and hook feeds | PEC-PRS-004 | **Deferred**, not permanent — trigger T-RT: a Runtime-owning loop publishes, under its own authority, an observation interface usable by a non-owning local reader, and `_DomainEngines/profiles/pec.yaml` is amended, and a D-PEC packet names the bridge. PEC can neither request nor require that interface. Was PKG-06 / DEL-06-04 / OBJ-003 before SCA-005 |
+| SOW-035 | OUT | Implement the runtime-daemon SSE subscriber bridge, declared and attributable | PEC-STR-003 | **Deferred**, not permanent — trigger T-RT: a Runtime-owning loop publishes, under its own authority, an observation interface usable by a non-owning local reader, and `_DomainEngines/profiles/pec.yaml` is amended, and a D-PEC packet names the bridge. PEC can neither request nor require that interface. Was PKG-07 / DEL-07-02 / no objective before SCA-005; TM-PEC-023 row 4 disposed by this status change, not by a mapping; bridge split per DL-5 |
+| SOW-037 | OUT | Implement the cmux socket adapter as an optional, declared and attributable enricher | PEC-STR-003 | **Deferred**, not permanent — re-entry only by a later owner direction (owner 2026-09-24: no plans for cmux compatibility). Was PKG-07 / DEL-07-04 / no objective before SCA-005 (optional; P4); TM-PEC-023 row 6 disposed by this status change, not by a mapping |
+| SOW-087 | OUT | Reimplement the shared-runtime client seam concept against v2 entities | §13, D-PEC-56 | **Deferred**, not permanent — trigger T-RT: a Runtime-owning loop publishes, under its own authority, an observation interface usable by a non-owning local reader, and `_DomainEngines/profiles/pec.yaml` is amended, and a D-PEC packet names the bridge. PEC can neither request nor require that interface. Was PKG-07 / DEL-07-05 / no objective before SCA-005; the D-PEC-56 client-seam concept ("Concept carries directly; reimplemented against v2 entities") is retained as historical lineage; TM-PEC-023 row 7 disposed by this status change, not by a mapping |
```

`ScopeLedger.csv` row `SOW-029` (replace):

```diff
-SOW-029,IN,Maintain live parent→child hierarchy edges from daemon and hook feeds,PEC-PRS-004,PKG-06,DEL-06-04,OBJ-003,,FALSE,
+SOW-029,OUT,Maintain live parent→child hierarchy edges from daemon and hook feeds,PEC-PRS-004,,,,SCA-005,FALSE,"**Deferred**, not permanent — trigger T-RT: a Runtime-owning loop publishes, under its own authority, an observation interface usable by a non-owning local reader, and `_DomainEngines/profiles/pec.yaml` is amended, and a D-PEC packet names the bridge. PEC can neither request nor require that interface. Was PKG-06 / DEL-06-04 / OBJ-003 before SCA-005"
```

### A-30 — MODIFY OTHER `SOW-035`

SOW-035 IN -> OUT **Deferred** (trigger T-RT); PKG-07/DEL-07-02 lineage cleared; TM-PEC-023 row 4 disposed by this status change. Supersession binding: **YES**.

`SOFTWARE_DECOMP.md` — §2.1 remove SOW-035 (moves to §2.2; Seq 30):

```diff
-| SOW-035 | IN | Implement the runtime-daemon SSE subscriber bridge, declared and attributable | PEC-STR-003 | Bridge split per DL-5 |
```

`ScopeLedger.csv` row `SOW-035` (replace):

```diff
-SOW-035,IN,"Implement the runtime-daemon SSE subscriber bridge, declared and attributable",PEC-STR-003,PKG-07,DEL-07-02,,,FALSE,Bridge split per DL-5
+SOW-035,OUT,"Implement the runtime-daemon SSE subscriber bridge, declared and attributable",PEC-STR-003,,,,SCA-005,FALSE,"**Deferred**, not permanent — trigger T-RT: a Runtime-owning loop publishes, under its own authority, an observation interface usable by a non-owning local reader, and `_DomainEngines/profiles/pec.yaml` is amended, and a D-PEC packet names the bridge. PEC can neither request nor require that interface. Was PKG-07 / DEL-07-02 / no objective before SCA-005; TM-PEC-023 row 4 disposed by this status change, not by a mapping; bridge split per DL-5"
```

### A-31 — MODIFY OTHER `SOW-087`

SOW-087 IN -> OUT **Deferred** (trigger T-RT); D-PEC-56 concept retained as historical lineage; PKG-07/DEL-07-05 lineage cleared; TM-PEC-023 row 7 disposed. Supersession binding: **YES**.

`SOFTWARE_DECOMP.md` — §2.1 remove SOW-087 (moves to §2.2; Seq 31):

```diff
-| SOW-087 | IN | Reimplement the shared-runtime client seam concept against v2 entities | §13, D-PEC-56 | Named carry-forward: "Concept carries directly; reimplemented against v2 entities" |
```

`ScopeLedger.csv` row `SOW-087` (replace):

```diff
-SOW-087,IN,Reimplement the shared-runtime client seam concept against v2 entities,"§13, D-PEC-56",PKG-07,DEL-07-05,,DL-11,FALSE,"Named carry-forward: ""Concept carries directly; reimplemented against v2 entities"""
+SOW-087,OUT,Reimplement the shared-runtime client seam concept against v2 entities,"§13, D-PEC-56",,,,DL-11; SCA-005,FALSE,"**Deferred**, not permanent — trigger T-RT: a Runtime-owning loop publishes, under its own authority, an observation interface usable by a non-owning local reader, and `_DomainEngines/profiles/pec.yaml` is amended, and a D-PEC packet names the bridge. PEC can neither request nor require that interface. Was PKG-07 / DEL-07-05 / no objective before SCA-005; the D-PEC-56 client-seam concept (""Concept carries directly; reimplemented against v2 entities"") is retained as historical lineage; TM-PEC-023 row 7 disposed by this status change, not by a mapping"
```

### A-77 — MODIFY OTHER `SOW-037`

SOW-037 IN -> OUT **Deferred**, re-entry only by later owner direction; PKG-07/DEL-07-04 lineage cleared; TM-PEC-023 row 6 disposed by this status change. Supersession binding: **YES**.

`SOFTWARE_DECOMP.md` — §2.1 remove SOW-037 (moves to §2.2; Seq 77):

```diff
-| SOW-037 | IN | Implement the cmux socket adapter as an optional, declared and attributable enricher | PEC-STR-003 | Optional; P4 |
```

`ScopeLedger.csv` row `SOW-037` (replace):

```diff
-SOW-037,IN,"Implement the cmux socket adapter as an optional, declared and attributable enricher",PEC-STR-003,PKG-07,DEL-07-04,,,FALSE,Optional; P4
+SOW-037,OUT,"Implement the cmux socket adapter as an optional, declared and attributable enricher",PEC-STR-003,,,,SCA-005,FALSE,"**Deferred**, not permanent — re-entry only by a later owner direction (owner 2026-09-24: no plans for cmux compatibility). Was PKG-07 / DEL-07-04 / no objective before SCA-005 (optional; P4); TM-PEC-023 row 6 disposed by this status change, not by a mapping"
```

### A-32 — MODIFY OTHER `SOW-034`

SOW-034 statement: event contract types consumable by the hooks CLI bridge (the only remaining bridge); Notes: contract-home option path projects/chirality-runtime/packages/contracts, home TBD (SOW-083). Supersession binding: **YES**.

`SOFTWARE_DECOMP.md` — §2.1 SOW-034 (Seq 32):

```diff
-| SOW-034 | IN | Define versioned event contract types consumable by daemon, hooks CLI, and adapters | PEC-STR-002 | Contract home is TBD (SOW-083); root `runtime/` writes out of scope (SOW-074) |
+| SOW-034 | IN | Define versioned event contract types consumable by the hooks CLI bridge | PEC-STR-002 | The hooks CLI is the only remaining bridge (SOW-035 and SOW-037 deferred). Contract home is TBD (SOW-083); the shared option path is `projects/chirality-runtime/packages/contracts` (Runtime loop; root `runtime/` relocated, PR #727), and writes there are out of scope (SOW-074). OBJ-003 by the owner's TM-PEC-023 row-1 selection |
```

`ScopeLedger.csv` row `SOW-034` (replace):

```diff
-SOW-034,IN,"Define versioned event contract types consumable by daemon, hooks CLI, and adapters",PEC-STR-002,PKG-00,DEL-00-02,,DL-12,FALSE,Contract home is TBD (SOW-083); root `runtime/` writes out of scope (SOW-074)
+SOW-034,IN,Define versioned event contract types consumable by the hooks CLI bridge,PEC-STR-002,PKG-00,DEL-00-02,OBJ-003,DL-12; SCA-005,FALSE,"The hooks CLI is the only remaining bridge (SOW-035 and SOW-037 deferred). Contract home is TBD (SOW-083); the shared option path is `projects/chirality-runtime/packages/contracts` (Runtime loop; root `runtime/` relocated, PR #727), and writes there are out of scope (SOW-074). OBJ-003 by the owner's TM-PEC-023 row-1 selection"
```

### A-33 — MODIFY OTHER `SOW-049`

SOW-049 statement/Notes: presence board = sessions (when hook-reported) x worktrees x graph-declared activity; live hierarchy deferred with SOW-029. Supersession binding: **YES**.

`SOFTWARE_DECOMP.md` — §2.1 SOW-049 (Seq 33):

```diff
-| SOW-049 | IN | Dashboard — presence board: sessions × worktrees × live hierarchy with heartbeat age and advisory overlap warnings | PEC-DSH-005 | |
+| SOW-049 | IN | Dashboard — presence board: sessions (when hook-reported) × worktrees × graph-declared activity, with heartbeat/scan age and advisory overlap warnings | PEC-DSH-005 | Live hierarchy deferred with SOW-029; declared activity is record tier, never presence tier or liveness |
```

`ScopeLedger.csv` row `SOW-049` (replace):

```diff
-SOW-049,IN,Dashboard — presence board: sessions × worktrees × live hierarchy with heartbeat age and advisory overlap warnings,PEC-DSH-005,PKG-09,DEL-09-05,OBJ-003;OBJ-004,,FALSE,
+SOW-049,IN,"Dashboard — presence board: sessions (when hook-reported) × worktrees × graph-declared activity, with heartbeat/scan age and advisory overlap warnings",PEC-DSH-005,PKG-09,DEL-09-05,OBJ-003;OBJ-004,SCA-005,FALSE,"Live hierarchy deferred with SOW-029; declared activity is record tier, never presence tier or liveness"
```

### A-44 — MODIFY OTHER `SOW-074`

SOW-074 Deferred OUT wording: writes into projects/chirality-runtime/** (root runtime/ relocated, PR #727). Supersession binding: **YES**.

`SOFTWARE_DECOMP.md` — §2.2 SOW-074 (Seq 44):

```diff
-| SOW-074 | OUT | Writes into root `runtime/`, including placing the event contracts there | PEC-STR-002, §16.9 | **Deferred**, not permanent: outside PEC's fences; requires its own cross-loop coordination. If SOW-083 rules for the shared-contracts home, that write becomes required work under its own instrument |
+| SOW-074 | OUT | Writes into the Runtime loop's `projects/chirality-runtime/**` (root `runtime/` relocated, PR #727), including placing the event contracts there | PEC-STR-002, §16.9 | **Deferred**, not permanent: outside PEC's fences; requires its own cross-loop coordination. If SOW-083 rules for the shared-contracts home (`projects/chirality-runtime/packages/contracts`), that write becomes required work under its own instrument |
```

`ScopeLedger.csv` row `SOW-074` (replace):

```diff
-SOW-074,OUT,"Writes into root `runtime/`, including placing the event contracts there","PEC-STR-002, §16.9",,,,,FALSE,"**Deferred**, not permanent: outside PEC's fences; requires its own cross-loop coordination. If SOW-083 rules for the shared-contracts home, that write becomes required work under its own instrument"
+SOW-074,OUT,"Writes into the Runtime loop's `projects/chirality-runtime/**` (root `runtime/` relocated, PR #727), including placing the event contracts there","PEC-STR-002, §16.9",,,,SCA-005,FALSE,"**Deferred**, not permanent: outside PEC's fences; requires its own cross-loop coordination. If SOW-083 rules for the shared-contracts home (`projects/chirality-runtime/packages/contracts`), that write becomes required work under its own instrument"
```

### A-45 — MODIFY OTHER `SOW-092`

SOW-092 OUT wording drops the retired 'daemon registration'; chirality.project.json and project identity unchanged. Supersession binding: **YES**.

`SOFTWARE_DECOMP.md` — §2.2 SOW-092 (Seq 45):

```diff
-| SOW-092 | OUT | Changes to `chirality.project.json`, daemon registration, or project identity | §13 | No work: "Continue unchanged" — recorded so coverage is explicit |
+| SOW-092 | OUT | Changes to `chirality.project.json` or project identity | §13 | No work: "Continue unchanged" — recorded so coverage is explicit; the former daemon-registration clause was dropped under SCA-005 (retired per-user daemon, D-GOV-20) |
```

`ScopeLedger.csv` row `SOW-092` (replace):

```diff
-SOW-092,OUT,"Changes to `chirality.project.json`, daemon registration, or project identity",§13,,,,,FALSE,"No work: ""Continue unchanged"" — recorded so coverage is explicit"
+SOW-092,OUT,Changes to `chirality.project.json` or project identity,§13,,,,SCA-005,FALSE,"No work: ""Continue unchanged"" — recorded so coverage is explicit; the former daemon-registration clause was dropped under SCA-005 (retired per-user daemon, D-GOV-20)"
```

### A-46 — MODIFY OTHER `SOW-076`

SOW-076 premise re-expressed (no daemon; per-application private Runtime; no non-owning observation interface); stays TBD. Supersession binding: **YES**.

`SOFTWARE_DECOMP.md` — §2.3 SOW-076 (Seq 46):

```diff
-| SOW-076 | TBD | Design and ownership of a daemon global event feed (today: per-session SSE only) | §16.2 | Assessed (not PRD-stated): affects SOW-035 efficiency, not correctness |
+| SOW-076 | TBD | Design and ownership of a global event feed observable by a non-owning reader (premise: no daemon exists; each application owns a private Runtime instance whose only SSE route is the per-session turn stream; no non-owning observation interface is documented) | §16.2 | Assessed (not PRD-stated): bears on the deferred SOW-035 bridge and trigger T-RT, not on record-tier correctness |
```

`ScopeLedger.csv` row `SOW-076` (replace):

```diff
-SOW-076,TBD,Design and ownership of a daemon global event feed (today: per-session SSE only),§16.2,,,,,TRUE,"OI-002. Assessed (not PRD-stated): affects SOW-035 efficiency, not correctness"
+SOW-076,TBD,Design and ownership of a global event feed observable by a non-owning reader (premise: no daemon exists; each application owns a private Runtime instance whose only SSE route is the per-session turn stream; no non-owning observation interface is documented),§16.2,,,,SCA-005,TRUE,"OI-002. Assessed (not PRD-stated): bears on the deferred SOW-035 bridge and trigger T-RT, not on record-tier correctness"
```

### A-47 — MODIFY OTHER `SOW-080`

SOW-080 premise re-expressed (app-private Runtime token registries; App registry reuse foreclosed); stays TBD. Supersession binding: **YES**.

`SOFTWARE_DECOMP.md` — §2.3 SOW-080 (Seq 47):

```diff
-| SOW-080 | TBD | Auth reuse: PEC tokens vs the daemon's project-scoped token registry | §16.6 | Affects SOW-003 implementation choice |
+| SOW-080 | TBD | Auth reuse: which PEC-local token mechanism PEC uses (premise: Runtime token registries are private to each application's Runtime instance, and reuse of an App registry is foreclosed by the Runtime consumer guide) | §16.6 | Affects SOW-003 implementation choice |
```

`ScopeLedger.csv` row `SOW-080` (replace):

```diff
-SOW-080,TBD,Auth reuse: PEC tokens vs the daemon's project-scoped token registry,§16.6,,,,,TRUE,OI-006. Affects SOW-003 implementation choice
+SOW-080,TBD,"Auth reuse: which PEC-local token mechanism PEC uses (premise: Runtime token registries are private to each application's Runtime instance, and reuse of an App registry is foreclosed by the Runtime consumer guide)",§16.6,,,,SCA-005,TRUE,OI-006. Affects SOW-003 implementation choice
```

### A-48 — MODIFY OTHER `SOW-082`

SOW-082 premise re-expressed (App/Piping/PEC ledgers carry receipt-contract-v2; App/Piping historical, new receipts central); stays TBD for Root/Runtime/Bridge. Supersession binding: **YES**.

`SOFTWARE_DECOMP.md` — §2.3 SOW-082 (Seq 48):

```diff
-| SOW-082 | TBD | Whether non-app-dev loop ledgers adopt the D-APP-57 receipt contract | §16.8 | Affects SOW-013 per-loop grammar coverage |
+| SOW-082 | TBD | Whether the Root, Runtime and Bridge ledgers adopt a receipt contract (premise: App, Piping and PEC ledgers carry receipt-contract-v2; App/Piping ledgers are historical and their new receipts are central `RECEIPT.md`) | §16.8 | Affects SOW-013 per-loop grammar coverage |
```

`ScopeLedger.csv` row `SOW-082` (replace):

```diff
-SOW-082,TBD,Whether non-app-dev loop ledgers adopt the D-APP-57 receipt contract,§16.8,,,,,TRUE,OI-008. Affects SOW-013 per-loop grammar coverage
+SOW-082,TBD,"Whether the Root, Runtime and Bridge ledgers adopt a receipt contract (premise: App, Piping and PEC ledgers carry receipt-contract-v2; App/Piping ledgers are historical and their new receipts are central `RECEIPT.md`)",§16.8,,,,SCA-005,TRUE,OI-008. Affects SOW-013 per-loop grammar coverage
```

### A-49 — MODIFY OTHER `SOW-083`

SOW-083 premise re-expressed (contract-home option path projects/chirality-runtime/packages/contracts; transport per D-GOV-43 A2); stays TBD. Supersession binding: **YES**.

`SOFTWARE_DECOMP.md` — §2.3 SOW-083 (Seq 49):

```diff
-| SOW-083 | TBD | Event-contract home (shared runtime contracts vs PEC-local schema + pinned mirror) and API transport (Unix socket only vs additional loopback listener) | §16.9 | Fenced: PEC builds local-first either way (SOW-034/040) |
+| SOW-083 | TBD | Event-contract home (shared Runtime contracts at `projects/chirality-runtime/packages/contracts` vs PEC-local schema + pinned mirror) and API transport (Unix socket only vs additional loopback listener; transport posture per D-GOV-43 A2) | §16.9 | Fenced: PEC builds local-first either way (SOW-034/040) |
```

`ScopeLedger.csv` row `SOW-083` (replace):

```diff
-SOW-083,TBD,Event-contract home (shared runtime contracts vs PEC-local schema + pinned mirror) and API transport (Unix socket only vs additional loopback listener),§16.9,,,,,TRUE,OI-009. Fenced: PEC builds local-first either way (SOW-034/040)
+SOW-083,TBD,Event-contract home (shared Runtime contracts at `projects/chirality-runtime/packages/contracts` vs PEC-local schema + pinned mirror) and API transport (Unix socket only vs additional loopback listener; transport posture per D-GOV-43 A2),§16.9,,,,SCA-005,TRUE,OI-009. Fenced: PEC builds local-first either way (SOW-034/040)
```

## 5. Objectives — objective mappings (ledger and deliverable in lockstep) and objective-side views

### A-63 — MODIFY DELIVERABLE `DEL-00-02`

TM-PEC-023 row 1: SOW-034 ObjectiveIDs and DEL-00-02 SupportsObjectives = OBJ-003 (owner replacement), set in lockstep after Seq 32. Supersession binding: **NO**.

TM-PEC-023 row 1: `OBJ-003` is set in lockstep on SOW-034 `ObjectiveIDs` and DEL-00-02 `SupportsObjectives`. Both cells ride the same rows as A-32 (SOW-034) and A-39 (DEL-00-02); the row diffs are shown there.

### A-64 — MODIFY DELIVERABLE `DEL-03-05`

TM-PEC-023 row 2: SOW-038 ObjectiveIDs and DEL-03-05 SupportsObjectives = OBJ-001 (MAP-A). Supersession binding: **NO**.

`Deliverables.csv` row `DEL-03-05` (replace):

```diff
-DEL-03-05,PKG-03,Stream-loss recovery guarantee,"Reconcile supremacy: no record-tier fact rests on a stream event alone; recovery path after stream gaps. Lands with the first ingest (DEL-07-01, P3) so ingest is never live without its safety invariant; the P4 exit demonstration is DEL-10-08.",BACKEND_FEATURE_SLICE,TBD,Supremacy rules + gap-recovery tests,SOW-038,,S,,P3
+DEL-03-05,PKG-03,Stream-loss recovery guarantee,"Reconcile supremacy: no record-tier fact rests on a stream event alone; recovery path after stream gaps. Lands with the first ingest (DEL-07-01, P3) so ingest is never live without its safety invariant; the P4 exit demonstration is DEL-10-08.",BACKEND_FEATURE_SLICE,TBD,Supremacy rules + gap-recovery tests,SOW-038,OBJ-001,S,,P3
```

`ScopeLedger.csv` row `SOW-038` (replace):

```diff
-SOW-038,IN,Recover stream loss by reconciliation; no record-tier fact may rest on a stream event alone,PEC-STR-004,PKG-03,DEL-03-05,,DL-11,FALSE,Carries PEC-K-07
+SOW-038,IN,Recover stream loss by reconciliation; no record-tier fact may rest on a stream event alone,PEC-STR-004,PKG-03,DEL-03-05,OBJ-001,DL-11; SCA-005,FALSE,Carries PEC-K-07
```

### A-65 — MODIFY DELIVERABLE `DEL-05-01`

TM-PEC-023 row 3: SOW-022, SOW-023 ObjectiveIDs and DEL-05-01 SupportsObjectives = OBJ-004 (MAP-A). Supersession binding: **NO**.

`Deliverables.csv` row `DEL-05-01` (replace):

```diff
-DEL-05-01,PKG-05,Gate precondition evaluators (Explain-shaped),"Deterministic evaluation of file/Git-reducible gate preconditions (ruling presence, SHA reachability, receipt ancestry, snapshot presence, register-row status) with Explain-shaped advisory verdicts.",BACKEND_FEATURE_SLICE,TBD,Evaluators + Explain types + tests,SOW-022;SOW-023,,M,,P2
+DEL-05-01,PKG-05,Gate precondition evaluators (Explain-shaped),"Deterministic evaluation of file/Git-reducible gate preconditions (ruling presence, SHA reachability, receipt ancestry, snapshot presence, register-row status) with Explain-shaped advisory verdicts.",BACKEND_FEATURE_SLICE,TBD,Evaluators + Explain types + tests,SOW-022;SOW-023,OBJ-004,M,,P2
```

`ScopeLedger.csv` row `SOW-022` (replace):

```diff
-SOW-022,IN,"Deterministically evaluate gate preconditions reducible to file/Git facts: ruling presence, ruling-SHA reachability, receipt ancestry, snapshot/freeze presence, register-row status",PEC-GAT-001,PKG-05,DEL-05-01,,,FALSE,
+SOW-022,IN,"Deterministically evaluate gate preconditions reducible to file/Git facts: ruling presence, ruling-SHA reachability, receipt ancestry, snapshot/freeze presence, register-row status",PEC-GAT-001,PKG-05,DEL-05-01,OBJ-004,SCA-005,FALSE,
```

`ScopeLedger.csv` row `SOW-023` (replace):

```diff
-SOW-023,IN,"Shape gate verdicts as Explain objects (rule, threshold, contributing citations), advisory only",PEC-GAT-002,PKG-05,DEL-05-01,,,FALSE,Carries PEC-K-08
+SOW-023,IN,"Shape gate verdicts as Explain objects (rule, threshold, contributing citations), advisory only",PEC-GAT-002,PKG-05,DEL-05-01,OBJ-004,SCA-005,FALSE,Carries PEC-K-08
```

### A-66 — MODIFY DELIVERABLE `DEL-07-02`

TM-PEC-023 row 4 disposed without mapping: DEL-07-02 retires (Seq 35) and SOW-035 is Deferred OUT (Seq 30); no objective field is set. Supersession binding: **NO**.

No bytes of its own. TM-PEC-023 row 4 is disposed without a mapping: DEL-07-02 retires (A-35) and SOW-035 becomes Deferred OUT (A-30); no objective cell is set.

### A-67 — MODIFY DELIVERABLE `DEL-07-03`

TM-PEC-023 row 5: SOW-036 ObjectiveIDs and DEL-07-03 SupportsObjectives = OBJ-003 (MAP-A). Supersession binding: **NO**.

`Deliverables.csv` row `DEL-07-03` (replace):

```diff
-DEL-07-03,PKG-07,Hooks CLI bridge,"Declared, attributable harness hooks CLI: session start/stop, status, scope declaration.",BACKEND_FEATURE_SLICE,TBD,CLI + tests,SOW-036,,M,,P3
+DEL-07-03,PKG-07,Hooks CLI bridge,"Declared, attributable harness hooks CLI: session start/stop, status, scope declaration.",BACKEND_FEATURE_SLICE,TBD,CLI + tests,SOW-036,OBJ-003,M,,P3
```

`ScopeLedger.csv` row `SOW-036` (replace):

```diff
-SOW-036,IN,"Implement the harness hooks CLI bridge (session start/stop, status, scope declaration), declared and attributable",PEC-STR-003,PKG-07,DEL-07-03,,,FALSE,
+SOW-036,IN,"Implement the harness hooks CLI bridge (session start/stop, status, scope declaration), declared and attributable",PEC-STR-003,PKG-07,DEL-07-03,OBJ-003,SCA-005,FALSE,
```

### A-69 — MODIFY DELIVERABLE `DEL-07-05`

TM-PEC-023 row 7 disposed without mapping: DEL-07-05 retires (Seq 36) and SOW-087 is Deferred OUT (Seq 31); no objective field is set. Supersession binding: **NO**.

No bytes of its own. TM-PEC-023 row 7 is disposed without a mapping: DEL-07-05 retires (A-36) and SOW-087 becomes Deferred OUT (A-31); no objective cell is set.

### A-70 — MODIFY DELIVERABLE `DEL-08-05`

TM-PEC-023 row 8: SOW-044 ObjectiveIDs and DEL-08-05 SupportsObjectives = OBJ-001;OBJ-003 (owner replacement). Supersession binding: **NO**.

`Deliverables.csv` row `DEL-08-05` (replace):

```diff
-DEL-08-05,PKG-08,SSE delta/presence subscription,SSE subscription for deltas and presence changes (dashboards; long-running managers). P2/P3 dashboards poll; live subscription arrives with the P4 streams tranche — pull earlier by owner call if polling proves insufficient.,BACKEND_FEATURE_SLICE,TBD,SSE endpoint + tests,SOW-044,,M,,P4
+DEL-08-05,PKG-08,SSE delta/presence subscription,SSE subscription for deltas and presence changes (dashboards; long-running managers). P2/P3 dashboards poll; live subscription arrives with the P4 streams tranche — pull earlier by owner call if polling proves insufficient.,BACKEND_FEATURE_SLICE,TBD,SSE endpoint + tests,SOW-044,OBJ-001;OBJ-003,M,,P4
```

`ScopeLedger.csv` row `SOW-044` (replace):

```diff
-SOW-044,IN,Offer an SSE subscription for deltas and presence changes,PEC-API-005,PKG-08,DEL-08-05,,,FALSE,
+SOW-044,IN,Offer an SSE subscription for deltas and presence changes,PEC-API-005,PKG-08,DEL-08-05,OBJ-001;OBJ-003,SCA-005,FALSE,
```

### A-71 — MODIFY DELIVERABLE `DEL-10-08`

TM-PEC-023 row 9: SOW-063 ObjectiveIDs and DEL-10-08 SupportsObjectives = OBJ-001 (owner replacement; supersedes DL-14's objective-free rationale for SOW-063). Supersession binding: **NO**.

`Deliverables.csv` row `DEL-10-08` (replace):

```diff
-DEL-10-08,PKG-10,Stream-loss recovery demonstration,Stream loss demonstrably recovered by reconciliation (P4 exit).,TEST_SUITE,TBD,Recovery demonstration tests,SOW-063,,S,,P4
+DEL-10-08,PKG-10,Stream-loss recovery demonstration,Stream loss demonstrably recovered by reconciliation (P4 exit).,TEST_SUITE,TBD,Recovery demonstration tests,SOW-063,OBJ-001,S,,P4
```

`ScopeLedger.csv` row `SOW-063` (replace):

```diff
-SOW-063,IN,Demonstrate stream-loss recovery by reconciliation (P4 exit test),§12 P4,PKG-10,DEL-10-08,,,FALSE,Tests SOW-038
+SOW-063,IN,Demonstrate stream-loss recovery by reconciliation (P4 exit test),§12 P4,PKG-10,DEL-10-08,OBJ-001,SCA-005,FALSE,Tests SOW-038
```

### A-79 — MODIFY OTHER `SOW-033`

SOW-033 ObjectiveIDs '' -> OBJ-003; DEL-07-01 SupportsObjectives unchanged (OBJ-003 = union of SOW-033 and SOW-039). Supersession binding: **NO**.

`ScopeLedger.csv` row `SOW-033` (replace):

```diff
-SOW-033,IN,"Accept idempotent, append-only event ingest keyed on event id",PEC-STR-001,PKG-07,DEL-07-01,,,FALSE,
+SOW-033,IN,"Accept idempotent, append-only event ingest keyed on event id",PEC-STR-001,PKG-07,DEL-07-01,OBJ-003,SCA-005,FALSE,
```

### A-60 — MODIFY OBJECTIVE `OBJ-001`

OBJ-001 objective-side view recomputed from the registers: gains SOW-095/096, SOW-038, SOW-044, SOW-063 and DEL-02-08/09, DEL-03-05, DEL-08-05, DEL-10-08; statement unchanged. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §3 OBJ-001 view (Seq 60):

```diff
-| OBJ-001 | Orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation | §3.1 | SOW-001, SOW-003, SOW-004..009, SOW-011..017, SOW-040..043, SOW-089; instruments: SOW-058, SOW-059 | DEL-00-03, DEL-01-01, DEL-02-01..07, DEL-04-01..05, DEL-08-01..04, DEL-10-01, DEL-10-04 |
+| OBJ-001 | Orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation | §3.1 | SOW-001, SOW-003..009, SOW-011..017, SOW-038, SOW-040..044, SOW-089, SOW-095, SOW-096; instruments: SOW-058, SOW-059, SOW-063 | DEL-00-03, DEL-01-01, DEL-02-01..09, DEL-03-05, DEL-04-01..05, DEL-08-01..05, DEL-10-01, DEL-10-04, DEL-10-08 |
```

### A-61 — MODIFY OBJECTIVE `OBJ-002`

OBJ-002 objective-side view gains SOW-095/096 and DEL-02-08/09; statement unchanged. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §3 OBJ-002 view (Seq 61):

```diff
-| OBJ-002 | Staleness is detected structurally by SHA comparison, never by judgment | §3.2 | SOW-001, SOW-006, SOW-011..019; supported by SOW-005 | DEL-01-01, DEL-02-01..07, DEL-03-02, DEL-03-03, DEL-04-02, DEL-04-03 |
+| OBJ-002 | Staleness is detected structurally by SHA comparison, never by judgment | §3.2 | SOW-001, SOW-006, SOW-011..019, SOW-095, SOW-096; supported by SOW-005 | DEL-01-01, DEL-02-01..09, DEL-03-02, DEL-03-03, DEL-04-02, DEL-04-03 |
```

### A-62 — MODIFY OBJECTIVE `OBJ-003`

OBJ-003 objective-side view recomputed: loses SOW-029/DEL-06-04; gains SOW-033, SOW-034, SOW-036, SOW-044 and DEL-00-02, DEL-07-03, DEL-08-05; statement unchanged; non-orphan. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §3 OBJ-003 view (Seq 62):

```diff
-| OBJ-003 | Concurrent sessions have a declared, durable surface for presence and status; write-scope collisions are surfaced before they land in Git | §3.3 | SOW-002, SOW-026..032, SOW-039, SOW-049; instruments: SOW-061, SOW-062, SOW-084 | DEL-01-02, DEL-06-01..06, DEL-07-01, DEL-09-05, DEL-10-06, DEL-10-07, DEL-10-09 |
+| OBJ-003 | Concurrent sessions have a declared, durable surface for presence and status; write-scope collisions are surfaced before they land in Git | §3.3 | SOW-002, SOW-026..028, SOW-030..034, SOW-036, SOW-039, SOW-044, SOW-049; instruments: SOW-061, SOW-062, SOW-084 | DEL-00-02, DEL-01-02, DEL-06-01..03, DEL-06-05, DEL-06-06, DEL-07-01, DEL-07-03, DEL-08-05, DEL-09-05, DEL-10-06, DEL-10-07, DEL-10-09 |
```

### A-80 — MODIFY OBJECTIVE `OBJ-004`

OBJ-004 objective-side view gains SOW-022, SOW-023 and DEL-05-01; statement unchanged. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §3 OBJ-004 view (Seq 80):

```diff
-| OBJ-004 | The human owner has one live view: loops, gates, lifecycle census, decisions waiting on them, and who is working where | §3.4 | SOW-024, SOW-045..051, SOW-077, SOW-094; instrument: SOW-085 | DEL-01-06, DEL-05-02, DEL-09-01..07, DEL-10-05 |
+| OBJ-004 | The human owner has one live view: loops, gates, lifecycle census, decisions waiting on them, and who is working where | §3.4 | SOW-022..024, SOW-045..051, SOW-077, SOW-094; instrument: SOW-085 | DEL-01-06, DEL-05-01, DEL-05-02, DEL-09-01..07, DEL-10-05 |
```

## 6. Vocabulary Map

### A-54 — MODIFY VOCAB_TERM `loop`

Vocabulary 'loop': registry-relative; six observed LOOP_INIT-bearing loops; PEC serves only what loops.json lists. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §9 loop (Seq 54):

```diff
-| loop | work loop, domain-engine loop | Tenancy unit above Project (root, app-dev, piping, pec, bridge) |
+| loop | work loop, domain-engine loop | Tenancy unit above Project. PEC serves only the loops its registry (`loops.json`) lists; the observed LOOP_INIT-bearing loops are six (root, app-dev, piping, pec, bridge — its last receipt was dated 2026-08-02 when SCA-005 was prepared — and runtime) |
```

### A-55 — MODIFY VOCAB_TERM `harness`

Vocabulary 'harness': 'runtime daemon' -> 'application-owned Runtime service (per application, D-GOV-43 A2)'. Supersession binding: **YES**.

`SOFTWARE_DECOMP.md` — §9 harness (Seq 55):

```diff
-| harness | practitioner harness / runtime daemon / hooks CLI |
+| harness | practitioner harness / application-owned Runtime service (per application, D-GOV-43 A2) / hooks CLI |
```

### A-56 — ADD VOCAB_TERM `work graph`

ADD vocabulary 'work graph' with node-ID disambiguation. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §9 ADD work graph, receipt, feed profile, declared activity (Seq 56-59):

```diff
-| MEASUREMENT (deliverable type) | metric deliverable | Added to the suggestive software taxonomy for §11 metric work (DL-13): a deliverable whose artifact is a measurement method, instrumentation, and report — not a feature or test of behavior |
+| MEASUREMENT (deliverable type) | metric deliverable | Added to the suggestive software taxonomy for §11 metric work (DL-13): a deliverable whose artifact is a measurement method, instrumentation, and report — not a feature or test of behavior |
+| work graph | undertaking graph | A loop's current undertaking graph at `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md` (SOW-095), distinct from historical `WORK_GRAPH.json` run evidence. **Disambiguation:** graph node IDs (P1, C1, F1, W1, V1, M1, R1 …) are local node tokens, distinct from PEC release phases P1–P4 and hard constraints C1–C16 |
+| receipt | loop receipt, central receipt | Disambiguate a `LOOP_RECEIPTS.md` ledger entry from a central `execution/_Coordination/AgentRuns/<RunID>/RECEIPT.md` (a derivative account, one per undertaking); both feed the Receipt entity (SOW-013) and neither is authority |
+| feed profile | — | A closed, PEC-versioned grammar bundle that a registry (`loops.json`) row selects, e.g. `shared-dev-loop`, `remaining-loop`, `loop-receipts-ledger`, `agentruns-json`; PEC's reading hypothesis, never the loop's truth (SOW-077, SOW-094) |
+| declared activity | graph-declared node state | A record-tier graph-declared node state (e.g. "declared ACTIVE as of commit X, age N"); never a liveness assertion and never presence tier (SOW-049) |
```

### A-57 — ADD VOCAB_TERM `receipt`

ADD vocabulary 'receipt' (ledger entry vs central RECEIPT.md; neither is authority). Supersession binding: **NO**.

Added in the single §9 insertion shown under A-56.

### A-58 — ADD VOCAB_TERM `feed profile`

ADD vocabulary 'feed profile' (closed, PEC-versioned; reading hypothesis, never the loop's truth). Supersession binding: **NO**.

Added in the single §9 insertion shown under A-56.

### A-59 — ADD VOCAB_TERM `declared activity`

ADD vocabulary 'declared activity' (record-tier graph-declared node state; never liveness, never presence tier). Supersession binding: **NO**.

Added in the single §9 insertion shown under A-56.

## 7. Constraints, intake summary, domain signals, open issues, coverage and telemetry

### A-24 — MODIFY OTHER `S1.2-intake-summary`

§1.2 intake summary: reconciliation feed list, streams bullet (daemon SSE and cmux bridges deferred), registry-relative anticipated build shape. Supersession binding: **YES**.

`SOFTWARE_DECOMP.md` — §1.2 reconciliation bullet (Seq 24):

```diff
-- **Reconciliation** (PEC-RCN-001..006): a one-command-rebuildable record
-  tier ingesting `_STATUS.md`, decision registers/packets, receipts ledgers
-  (per-loop grammar), `WORK_GRAPH.json`/`STATUS.json`/`RUNTIME_SUMMARY.json`,
-  dependency registers, workplans/LOOP_INIT, and `_harness/adapter.yaml`
-  manifests; incremental on Git delta; drift-classifying; never writing
-  sources; permanently parity-diffable against the practitioner harness.
+- **Reconciliation** (PEC-RCN-001..006): a one-command-rebuildable record
+  tier ingesting, as each loop's closed feed profile in the PEC-owned
+  registry declares, `_STATUS.md`, decision registers/packets, receipts
+  (per-loop `LOOP_RECEIPTS.md` ledgers and central
+  `AgentRuns/<RunID>/RECEIPT.md`), Markdown work graphs
+  (`WorkGraphs/<undertaking>/WORK_GRAPH.md`), the MEMORY run index,
+  dependency registers, and `LOOP_INIT.md` loop identity; JSON run evidence
+  (`WORK_GRAPH.json`/`STATUS.json`/`RUNTIME_SUMMARY.json`) and workplans are
+  read under declared historical grammars, and `_harness/adapter.yaml` only
+  as a parity-peer input; incremental on Git delta; drift-classifying; never
+  writing sources; permanently parity-diffable against the practitioner
+  harness.
```

`SOFTWARE_DECOMP.md` — §1.2 streams bullet (Seq 24):

```diff
-  decision); daemon SSE, hooks CLI, and optional cmux bridges; stream loss
-  always recovered by reconciliation.
+  decision); the hooks CLI bridge, with the daemon SSE and cmux bridges
+  deferred; stream loss always recovered by reconciliation.
```

`SOFTWARE_DECOMP.md` — §1.2 anticipated build shape (Seq 24):

```diff
-store + read-only API for PEC's own build graph) → P2 (dashboards, five
-loops, owner-use/non-use observation) → P3 (opt-in PEC-side consumer
-interfaces/adapters, presence registry, Git/worktree scanner) → P4 (PEC-side
-streams and optional hook-push interfaces). Live P3/P4 use requires separate
+store + read-only API for PEC's own build graph) → P2 (dashboards, the
+loops the registry lists, owner-use/non-use observation) → P3 (opt-in
+PEC-side consumer interfaces/adapters, presence registry, Git/worktree
+scanner) → P4 (PEC-side streams and optional hook-push interfaces). Live
+P3/P4 use requires separate
```

### A-26 — MODIFY OTHER `C13`

C13: sessions, delegation and turn admission owned per application by its application-owned Runtime service (D-GOV-43 A2); no-second-execution-loop and D-PEC-56 behaviours 4/7 unchanged. Supersession binding: **YES**.

`SOFTWARE_DECOMP.md` — §1.3 C13 (Seq 26):

```diff
-| C13 | No second execution loop; daemon owns sessions, delegation, turn locks | D-GOV-20, D-PEC-56 (surviving behaviors 4/7) |
+| C13 | No second execution loop; sessions, delegation and turn admission are owned per application by its application-owned Runtime service (one private Runtime per application; D-GOV-43 A2), which supersedes D-GOV-20 items 2–4 on that path | D-GOV-43 A2, D-PEC-56 (surviving behaviors 4/7) |
```

### A-27 — MODIFY OTHER `C5`

C5 source citation D-GOV-20 -> D-GOV-43 A2; substance unchanged. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §1.3 C5 (Seq 27):

```diff
-| C5 | Observation not participation: no dispatch, leases, arbitration, merge opinions; read-only over Git | PEC-K-06, D-GOV-20 |
+| C5 | Observation not participation: no dispatch, leases, arbitration, merge opinions; read-only over Git | PEC-K-06, D-GOV-43 A2 |
```

### A-81 — MODIFY OTHER `S2.4-runtime-surfaces`

§2.4 runtime-surfaces bullet 'external-process bridges (daemon SSE, cmux)' re-expressed with both bridges deferred. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §2.4 runtime surfaces (Seq 81):

```diff
-- Runtime surfaces: a core service (parsers, store, reconciler, evaluators),
-  a socket API server, a web dashboard UI, a hooks CLI, and external-process
-  bridges (daemon SSE, cmux).
+- Runtime surfaces: a core service (parsers, store, reconciler, evaluators),
+  a socket API server, a web dashboard UI, and a hooks CLI; the
+  external-process bridges once listed here (daemon SSE, cmux) are deferred
+  under SCA-005 (SOW-035 behind trigger T-RT; SOW-037 until a later owner
+  direction).
```

### A-50 — MODIFY OTHER `OI-002`

OI-002 text follows SOW-076; remains open. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §10 OI-002 (Seq 50):

```diff
-| OI-002 | SOW-076 | §16.2 daemon global event feed undecided | §16 ruling (cross-loop) |
+| OI-002 | SOW-076 | §16.2 global event feed undecided; premise re-expressed under SCA-005: no daemon exists, each application owns a private Runtime instance whose only SSE route is the per-session turn stream, and no non-owning observation interface is documented | §16 ruling (cross-loop) |
```

### A-51 — MODIFY OTHER `OI-006`

OI-006 text follows SOW-080; remains open. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §10 OI-006 (Seq 51):

```diff
-| OI-006 | SOW-080 | §16.6 auth reuse undecided | §16 ruling |
+| OI-006 | SOW-080 | §16.6 auth reuse undecided; premise re-expressed under SCA-005: Runtime token registries are private to each application's Runtime instance and reuse of an App registry is foreclosed, so the open choice is the PEC-local token mechanism | §16 ruling |
```

### A-52 — MODIFY OTHER `OI-008`

OI-008 text follows SOW-082; remains open for Root/Runtime/Bridge ledgers. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §10 OI-008 (Seq 52):

```diff
-| OI-008 | SOW-082 | §16.8 receipt-contract adoption by non-app-dev ledgers undecided | §16 ruling (per-loop) |
+| OI-008 | SOW-082 | §16.8 receipt-contract adoption undecided for the Root, Runtime and Bridge ledgers; premise re-expressed under SCA-005: App, Piping and PEC ledgers carry receipt-contract-v2, and App/Piping ledgers are historical with new receipts in central `RECEIPT.md` | §16 ruling (per-loop) |
```

### A-53 — MODIFY OTHER `OI-009`

OI-009 text follows SOW-083 (path restated); remains open. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §10 OI-009 (Seq 53):

```diff
-| OI-009 | SOW-083 | §16.9 event-contract home and API transport undecided | §16 ruling |
+| OI-009 | SOW-083 | §16.9 event-contract home and API transport undecided; the shared option path is `projects/chirality-runtime/packages/contracts` (Runtime loop; root `runtime/` relocated, PR #727) | §16 ruling |
```

### A-73 — MODIFY OTHER `S7-S8-telemetry`

§3 mapping notes, §5 intro/envelope posture, §6 row count, §7 telemetry and §8 prose recomputed: 96 scope items (70 IN / 18 OUT / 8 TBD); 66 deliverable rows (62 active / 4 RETIRED); active envelopes S 28 / M 32 / L 2 / XL 0; 0 IN items without objective; open/resolved issues 10/3. Supersession binding: **NO**.

`SOFTWARE_DECOMP.md` — §3 mapping notes (Seq 73; TM-PEC-023; Seq 79):

```diff
-No objective is unmapped at either level (scope items or deliverables);
-SOW-062 was mapped to OBJ-003 at Phase 6 (TTL honesty is a presence-surface
-instrument); SOW-063 remains intentionally unmapped — it instruments
-PEC-K-07, which no §3-derived objective states directly (DL-14). SCA-002
-mapped the Phase 2.2 wave scope at revision 1.2 (DL-17); the residue below
-is deliberate, not pending.
-
-**Mapping notes:** no unmapped objectives. Ingest/bridge items
-(SOW-033..039) serve OBJ-001/OBJ-003 freshness indirectly through
-PEC-K-07 and are intentionally not force-mapped; parser items
-(SOW-011..017) underlie OBJ-001/OBJ-002 through the record tier
-(SOW-001) — SCA-002 carried that derivation into the ledger at
-revision 1.2, mapping SOW-001 and SOW-011..017 to OBJ-001/OBJ-002
-rather than superseding the rationale. Deferred/OUT and TBD items map
-to no objective by design. Eleven IN items remain unmapped after
-SCA-002's O-A wave-minimum scope: the unmapped members of the
-ingest/bridge class above (SOW-033..038), SOW-063 (intentional per
-DL-14), and SOW-022, SOW-023, SOW-044, SOW-087, which are out-of-wave
-and left to the packet that authors their deliverables. Full
-ScopeItem→Objective assignments land in `ScopeLedger.csv` at Phase 4–5;
-this table is the objective-side view.
+No objective is unmapped at either level (scope items or deliverables);
+SOW-062 was mapped to OBJ-003 at Phase 6 (TTL honesty is a presence-surface
+instrument). SCA-002 mapped the Phase 2.2 wave scope at revision 1.2
+(DL-17). SCA-005 (DL-20) mapped the remaining IN items: the owner's
+TM-PEC-023 selections map SOW-022 and SOW-023 to OBJ-004, SOW-034 and
+SOW-036 to OBJ-003, SOW-038 to OBJ-001, SOW-044 to OBJ-001/OBJ-003 and
+SOW-063 to OBJ-001 — the row-9 selection supersedes DL-14's objective-free
+rationale for SOW-063 — and amendment 2 maps SOW-033 to OBJ-003; SOW-095
+and SOW-096 enter mapped to OBJ-001/OBJ-002.
+
+**Mapping notes:** no unmapped objectives and no IN item without an
+objective. Parser items (SOW-011..017, SOW-095, SOW-096) underlie
+OBJ-001/OBJ-002 through the record tier (SOW-001), the derivation SCA-002
+carried into the ledger at revision 1.2. Ingest and bridge items are
+mapped, by the owner's SCA-005 selections, to the objective whose surface
+each directly makes possible; that supersedes the earlier abstention that
+left them unmapped. Deferred/OUT and TBD items — including SOW-029,
+SOW-035, SOW-037 and SOW-087, deferred under SCA-005 — and the four
+retired deliverables (DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05) map to
+no objective by design. Full ScopeItem→Objective assignments land in
+`ScopeLedger.csv` at Phase 4–5; this table is the objective-side view.
```

`SOFTWARE_DECOMP.md` — §5 intro counts (Seq 73):

```diff
-64 deliverables across the 11 packages. **`Deliverables.csv` is the
-authoritative companion register**
+66 deliverable rows across the 11 packages: 62 active and 4 retired under
+SCA-005 (DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05), kept as
+`[RETIRED — SCA-005]` rows for register integrity. **`Deliverables.csv` is
+the authoritative companion register**
```

`SOFTWARE_DECOMP.md` — §5 envelope posture (Seq 73):

```diff
-Context Envelope posture: **28 S / 34 M / 2 L / 0 XL.** Both L
-deliverables (DEL-02-03 receipts parser; DEL-01-01 record-tier schema)
+Context Envelope posture (active deliverables): **28 S / 32 M / 2 L / 0 XL.**
+Both L deliverables (DEL-02-03 receipts parser; DEL-01-01 record-tier schema)
```

`SOFTWARE_DECOMP.md` — §6 row count (Seq 73):

```diff
-**Authoritative register: `ScopeLedger.csv`** — 94 rows tracing every
+**Authoritative register: `ScopeLedger.csv`** — 96 rows tracing every
```

`SOFTWARE_DECOMP.md` — §7 ScopeItemCount:

```diff
-| ScopeItemCount | 94 (72 IN / 14 OUT / 8 TBD) |
+| ScopeItemCount | 96 (70 IN / 18 OUT / 8 TBD) |
```

`SOFTWARE_DECOMP.md` — §7 DeliverableCount:

```diff
-| DeliverableCount | 64 |
+| DeliverableCount | 66 rows (62 active / 4 RETIRED: DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05) |
```

`SOFTWARE_DECOMP.md` — §7 IN without objective:

```diff
-| IN items without objective mapping | 11 (SCA-002 O-A residue, §3 mapping notes — the ingest/bridge class SOW-033..038; SOW-063, intentional per DL-14; and out-of-wave SOW-022, SOW-023, SOW-044, SOW-087) |
+| IN items without objective mapping | **0** (SCA-005: the owner's TM-PEC-023 selections and amendment 2 closed the SCA-002 O-A residue; SOW-035, SOW-037 and SOW-087 left IN; §3 mapping notes) |
```

`SOFTWARE_DECOMP.md` — §7 ContextEnvelopeCounts:

```diff
-| ContextEnvelopeCounts | S 28 / M 34 / L 2 / XL 0 |
+| ContextEnvelopeCounts | S 28 / M 32 / L 2 / XL 0 (active deliverables; the 4 retired rows are excluded) |
```

`SOFTWARE_DECOMP.md` — §7 single-package membership:

```diff
-| Deliverable single-package membership | 64/64; every `DEL-XX-YY` prefix matched to its parent package |
+| Deliverable single-package membership | 66/66; every `DEL-XX-YY` prefix matched to its parent package |
```

## 8. Product authority outside the decomposition (PRD v2.3 successor candidate)

### A-75 — MODIFY OTHER `PRD-successor-candidate`

PRD v2.3 successor candidate (CP2_CANDIDATE/docs/PRD.md): 28 Annex B MODIFY rows, 8 NOTE-ONLY rows unchanged, §7.1 WorkGraph/WorkNode row (Seq 1 coherence); §12 P1 unchanged (Q10 (a) narrowing); PEC-STR-003 and §12 P4 record the cmux adapter deferred; §8/orientation keep the v2.2 verify-before-rely meaning. Supersession binding: **NO**.

The exact candidate bytes are `CP2_CANDIDATE/docs/PRD.md`; the section-by-section diff against v2.2 is `PRD_V2_3_SUCCESSOR_DIFF.md`. It realizes the 28 Annex B MODIFY rows, leaves the 8 NOTE-ONLY rows byte-unchanged, adds the §7.1 WorkGraph / WorkNode row for coherence with A-01, keeps §12 P1 byte-unchanged (Q10 (a) narrowing), and records the cmux adapter as deferred in PEC-STR-003 and §12 P4 (amendment 1). §8 and PEC-ORI-001 keep the v2.2 verify-before-rely meaning and add no reliance text (D-PEC-90 note).

### A-76 — MODIFY OTHER `D-PEC-79`

D-PEC-79 six hunks brought into the one v2.3 successor candidate: hunk 1 Version row, hunk 3 provenance block, hunk 4 §16 heading and hunk 6 closing sentence byte-identical; hunk 1 Date/Status rows and hunk 2 epistemic paragraph rewritten for the successor's adoption instrument (group-2 acceptance); adopted bytes (92627ee1...b5f0) preserved as historical exact input; §16.3 'strict-version-1' -> 'strict, versioned' with the feed-profile clause. Supersession binding: **NO**.

The six D-PEC-79 hunks are brought into the one successor (CP1-D79 (b)): the Version row, the provenance block, the §16 heading and the closing sentence byte-identical; the Date/Status rows and the epistemic paragraph rewritten for the successor's adoption instrument; the adopted bytes `PRD_V2_3_CANDIDATE_POSTIMAGE.md` (`92627ee1d384dd8ef0f2db5d63362ec54eee9da30794b9c2d776bd46fb20f5b0`) stay unchanged as historical exact input. §16.3 changes only `strict-version-1` to `strict, versioned` and appends the feed-profile clause (CP1-V). See `PRD_V2_3_SUCCESSOR_DIFF.md`.

## 9. Child-closure set and authoritative ledger remaps

No package is removed, merged, split or reclassified, and no objective is added or removed. The parent-entity changes are four deliverable retirements and two deliverable additions; each is closed in this same amendment.

### 9.1 Retired deliverables (REMOVE)

| Retired deliverable | Parent package | Covered scope item before → disposition (same amendment) | SupportsObjectives before → after | Surviving register rows that target it | Parent's active children after |
|---|---|---|---|---|---|
| DEL-06-04 Live hierarchy edges (A-34) | PKG-06 | SOW-029 → OUT **Deferred**, trigger T-RT (A-29); PackageID/DeliverableIDs/ObjectiveIDs cleared | `OBJ-003` → blank | `DEP-09-05-005` (DEL-09-05, EXECUTION PREREQUISITE, mirrored as E-N02): retired by dependency-extract (Propagation_Plan B3) | 5: DEL-06-01, 06-02, 06-03, 06-05, 06-06 |
| DEL-07-02 Daemon SSE subscriber bridge (A-35) | PKG-07 | SOW-035 → OUT **Deferred**, trigger T-RT (A-30) | blank → blank (TM-PEC-023 row 4 disposed, A-66) | only `DEP-06-04-005`, owned by the also-retired DEL-06-04 | 2: DEL-07-01, DEL-07-03 |
| DEL-07-04 cmux socket adapter (optional) (A-78) | PKG-07 | SOW-037 → OUT **Deferred**, later owner direction only (A-77) | blank → blank (TM-PEC-023 row 6 moot; Seq 68 dropped) | none | 2 (as above) |
| DEL-07-05 Shared-runtime client seam (v2) (A-36) | PKG-07 | SOW-087 → OUT **Deferred**, trigger T-RT (A-31) | blank → blank (TM-PEC-023 row 7 disposed, A-69) | none | 2 (as above) |

No IN scope item is left without a package or deliverable, and no deliverable names an OUT item.

### 9.2 Added deliverables and scope items (ADD)

| New ID | Parent | Covers / covered by | Objectives | Envelope / phase |
|---|---|---|---|---|
| SOW-095 (A-08) ↔ DEL-02-08 Work-graph parser (A-19) | PKG-02 | reciprocal | `OBJ-001;OBJ-002` (CP1-O) | M / P1 |
| SOW-096 (A-09) ↔ DEL-02-09 MEMORY run-index parser (A-20) | PKG-02 | reciprocal | `OBJ-001;OBJ-002` (CP1-O) | S / P1 |

IDs are append-only: SOW-095/096 follow SOW-094 and DEL-02-08/09 follow DEL-02-07. Folders and metadata are created later by preparation (Propagation_Plan A4).

### 9.3 Package assignment remaps

| Package | Assigned before | Assigned after | Change |
|---|---|---|---|
| PKG-02 | SOW-011..017 (7) | SOW-011..017, 095, 096 (9) | +SOW-095, +SOW-096 |
| PKG-06 | SOW-026..032 (7) | SOW-026..028, 030..032 (6) | −SOW-029 (Deferred OUT) |
| PKG-07 | SOW-033, 035..037, 039, 087 (6) | SOW-033, 036, 039 (3) | −SOW-035, −SOW-037, −SOW-087 (Deferred OUT) |

### 9.4 Objective remaps (ledger `ObjectiveIDs` and `SupportsObjectives` set in lockstep)

| Scope item → deliverable | ObjectiveIDs before → after | SupportsObjectives before → after | Authority |
|---|---|---|---|
| SOW-033 → DEL-07-01 | blank → `OBJ-003` | `OBJ-003` (unchanged; union of SOW-033 and SOW-039) | amendment 2 (A-79) |
| SOW-034 → DEL-00-02 | blank → `OBJ-003` | blank → `OBJ-003` | TM-PEC-023 row 1 (A-63) |
| SOW-038 → DEL-03-05 | blank → `OBJ-001` | blank → `OBJ-001` | row 2 (A-64) |
| SOW-022, SOW-023 → DEL-05-01 | blank → `OBJ-004` | blank → `OBJ-004` | row 3 (A-65) |
| SOW-036 → DEL-07-03 | blank → `OBJ-003` | blank → `OBJ-003` | row 5 (A-67) |
| SOW-044 → DEL-08-05 | blank → `OBJ-001;OBJ-003` | blank → `OBJ-001;OBJ-003` | row 8 (A-70) |
| SOW-063 → DEL-10-08 | blank → `OBJ-001` | blank → `OBJ-001` | row 9 (A-71; supersedes DL-14's rationale for SOW-063) |
| SOW-029 → DEL-06-04 | `OBJ-003` → blank (OUT) | `OBJ-003` → blank (RETIRED) | R1 (A-29, A-34) |
| SOW-095, SOW-096 → DEL-02-08, DEL-02-09 | new `OBJ-001;OBJ-002` | new `OBJ-001;OBJ-002` | CP1-O (A-08, A-09, A-19, A-20) |

Every objective keeps active support at both levels. OBJ-003 loses only DEL-06-04 and keeps 14 active supporting deliverables (IA §8.1 said "10 active supporters remain"; the count before the TM-PEC-023 selections was 11 and is 14 after them — a correction to the accepted evidence, not a change of action).

## 10. RETIRED-row representation (group-1 blocker, resolved)

The registers have no lifecycle column, and `validate_decomposition_registers.py` has no RETIRED concept. The representation keeps every retired row as a register row so that dependency-register integrity (DRB-002/-005) holds for the retired registers' own rows and for `DEP-09-05-005`:

| Register | Retired-row form | Validator rule it satisfies |
|---|---|---|
| `Deliverables.csv` | Row kept; Name, PackageID, Type, ResponsibleParty, AnticipatedArtifacts, ContextEnvelope and PhaseHint byte-unchanged; Description prefixed `[RETIRED — SCA-005] ` + reason + `Original description:`; `CoversScopeItems` and `SupportsObjectives` blank; envelope note states the row is excluded from active counts | XRG-003 (no one-sided coverage), XRG-005 (no objective to propagate), XRG-008 (PhaseHint kept), DRB-002/-005 (row still exists) |
| `ContextBudgetQA.csv` | Row kept; envelope and risk unchanged; RecommendedAction `[RETIRED — SCA-005] None; row retained non-destructively` | XRG-009 (same deliverable set), XRG-010 (envelopes agree) |
| `ScopeLedger.csv` | In-place row replacement; `OUT`; PackageID, DeliverableIDs, ObjectiveIDs blank; Notes open with the bold `**Deferred**, not permanent` form of SOW-074/SOW-086 | XRG-007 (no OUT row names a deliverable) |
| `SOFTWARE_DECOMP.md` §5 | Row kept; Covers cell `— **[RETIRED — SCA-005]** (was SOW-0NN)`; §2 rows move §2.1 → §2.2 | human control view (DL-15) |

Evidence: the strict validator on a scratch copy of `projects/pec/execution` with the four candidate CSVs overlaid returns 0 ERROR and exactly two WARNINGs, DRB-008 for DEL-02-08 and DEL-02-09, whose folders and `Dependencies.csv` do not exist until preparation (expected; cleared by Propagation_Plan A4/B3). An independent manager check reproduces the counts in §11.

`audit-decomp` and a zero-coverage retired row (group-1 UNKNOWN, resolved): its method does not flag an empty `CoversScopeItems` (Check 3 compares folders with the declared list), does not treat a `[RETIRED …]` description specially, and reads RETIRED only from `_STATUS.md` (Checks 7 and 11; the Step 7 "objective supported only by RETIRED units" BLOCKER cannot fire because retired rows clear `SupportsObjectives`). A zero-coverage retired row is at most INFO; `analyze_dep_closure.py` will report the four retired nodes as isolated. The post-change audit at checkpoint-3 preparation confirms this on real files. Because audit-decomp Check 5 compares `_CONTEXT.md` descriptions with the register, the `[RETIRED — SCA-005]` prefix is mirrored into the four retired `_CONTEXT.md` files (Propagation_Plan A2).

## 11. Invariants and counts

| Metric | Revision 1.4 (live) | Revision 1.5 candidate |
|---|---:|---:|
| Scope items (IN / OUT / TBD) | 94 (72 / 14 / 8) | 96 (70 / 18 / 8) |
| Packages / objectives | 11 / 6 | 11 / 6 |
| Deliverable rows (active / RETIRED) | 64 (64 / 0) | 66 (62 / 4) |
| ContextBudgetQA rows | 64 | 66 |
| IN items without package / deliverable / objective | 0 / 0 / 11 | 0 / 0 / 0 |
| Active deliverables without SupportsObjectives | 9 | 0 |
| Active Context Envelopes S / M / L / XL | 28 / 34 / 2 / 0 | 28 / 32 / 2 / 0 |
| PKG-02 / PKG-06 / PKG-07 assigned scope | 7 / 7 / 6 | 9 / 6 / 3 |
| PKG-06 / PKG-07 active children | 6 / 5 | 5 / 2 |
| Union rule `SupportsObjectives = union(ObjectiveIDs)` over active rows | 64/64 | 62/62 |
| Open / resolved issues | 10 / 3 | 10 / 3 |
| Vocabulary terms | 22 | 26 |
| Execution dependency edges (analyze_dep_closure) | 119, 0 SCCs | 108 after retirement, before new edges; 0 SCCs (Propagation_Plan B3 plans 112) |

Stable identity: no ID is renumbered, reused or deleted; every name and folder path is retained (CP1-N), including the label drift recorded in the DEL-02-03/04/06/07 descriptions. Package-discipline isolation (DL-3, DL-12): the two new deliverables are PKG-02 read-side grammar slices that write nothing. Artifact-kind granularity (DL-4, DL-13): one grammar per deliverable. C3, C15, SOW-058 and the Gate Log are byte-unchanged.

## 12. Residual stale text not driven by any accepted action

The drafters found wording that is now stale but that no accepted action or Annex B row drives. It is **not** changed by this candidate (nothing unselected is added); it is disclosed here and carried as checkpoint-2 owner question Q-CP2-3.

| Surface | Locus | Stale wording | Binding |
|---|---|---|---|
| decomposition | §1.2 opening; §1.4 posture 1; §2 intro; R6 | "PRD v2.2", "46 requirements", "D-PEC-57..68" — intake-time basis statements | none (historical intake basis; front matter and R1 carry v2.3) |
| decomposition | §1.2 presence bullet | "live parent→child hierarchy edges" | covered by D-029 |
| decomposition | SOW-064 SourceRef | "PRD v2.2 §12" | none (§12 P1 unchanged in v2.3) |
| decomposition | SOW-067 Notes | "Daemon owns execution (C13)" contradicts amended C13 | covered in substance by D-026 |
| decomposition | SOW-002 | lists HierarchyEdge (presence-tier entity) | none (PRD §7.2 unchanged; entity kept for the deferred tier) |
| decomposition | §7 intro, OI-013 | "no durable build gate exists yet" although `validate_decomposition_registers.py` now exists | none (pre-existing; not SCA-005 drift) |
| decomposition | §8 | "Remaining S/M deliverables assessed LOW risk" omits DEL-10-10 (MEDIUM since SCA-001) | none (pre-existing) |
| registers | DEL-00-03 envelope note; DEL-02-07 AnticipatedArtifacts | "64 deliverables"; "Manifest reader" | none |
| PRD v2.3 candidate | §12 P3 | "hooks CLI or daemon consumers" | none (no decomposition text contradicts it) |
| PRD v2.3 candidate | PEC-DSH-005; §4.1 | "live hierarchy"; "live agent hierarchy" | D-033; D-029 note |
| PRD v2.3 candidate | §7.2 HierarchyEdge (INV-012 NOTE-ONLY) | live hierarchy entity | none |
| PRD v2.3 candidate | §13 domain-engine row | "profile superseded when v2 has shape" (stale under D-T0-27 O-A) | none (outside SCA-005 scope) |

## 13. Derivative and propagation boundary

Nothing in this preview writes `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `Dependencies.csv`, `_DEPENDENCIES.md`, any Scope of Work, the DEL-00-01 ADRs, the DEL-00-03 SPEC, `v2/**`, `loops.json`, pointers or foreign surfaces. Their exact dispositions, owners and rerun obligations are in `Propagation_Plan.md`. No downstream package becomes current through acceptance of this preview.
