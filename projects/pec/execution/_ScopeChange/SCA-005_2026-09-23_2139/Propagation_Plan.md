---
amendment_id: SCA-005
doc_kind: scope_change.propagation_plan
decomp_variant: SOFTWARE
checkpoint_group: 2
created: 2026-09-25
status: candidate_awaiting_checkpoint_2_acceptance
accepted_impact_assessment_sha256: 0bcbe9bdced43fa887a859497b3edd197242a0eea8fa3a41fab7147b358239bf
amendment_preview_sha256: ad48cc5621d796a662addc03640a32f7f4cdafbf627ad6fda3f60bdede65ebe4
---

# SCA-005 — checkpoint-group-2 propagation plan

## Status and authority

This plan, together with `Amendment_Preview.md` (SHA-256 `ad48cc5621d796a662addc03640a32f7f4cdafbf627ad6fda3f60bdede65ebe4`), is the checkpoint-group-2 package the owner accepts or revises as one unit. It applies nothing. It is prepared under the owner's checkpoint-1 acceptance of 2026-09-24 (group-1 snapshot, amendments 1 and 2) and the owner's direction of 2026-09-25 to proceed towards checkpoint 2. It carries the D-PEC-90 preparation note (`Decision_Log.md` SCA005-D90-NOTE): DEL-04-01 and the PRD §8 refresh are not designed around verify-before-rely; PEC-K-03 and the reliance text are amended by a later scope change, not by SCA-005.

The write scope the amendment needs is the SOFTWARE default: the decomposition document, its companion registers, affected `_CONTEXT.md` and `_STATUS.md` files, and SCA-owned `_ScopeChange` state, plus the owner-adopted PRD successor (CP1-D79 (b)). Everything else is a downstream rerun owned elsewhere and is **not** executed by WORKING_ITEMS.

## Checkpoint-3 preconditions

Checkpoint-3 preparation stops before its first write unless every value holds:

| Precondition | Required value |
|---|---|
| Accepted group-2 decision snapshot | exists under `_ScopeChange/checkpoint_snapshots/`, binds this plan, `Amendment_Preview.md`, `Amendment_Actions_CP2.csv`, `Supersession_Delta.csv`, the PRD candidate and the postimages at the SHA-256 values in the owner question below |
| Live preimages | as listed in `Amendment_Preview.md` §"Byte preconditions" (revision 1.4 files, PRD v2.2 `6833553c…77ba`) |
| `_ScopeChange/_LATEST.md` | names SCA-004 (posture `ACCEPTED_PREDECESSOR`), SHA-256 `721a14dc27b4b595be79f591f49b7374a121c52a77eb0451d32d9aa32a9e6280` |
| `_Decomposition/_LATEST.md` | revision 1.4, SHA-256 `7abf65e641a5a247f0c783192808ae1f9186f76ebe0d09d6e84e2983fffcd7a3` |
| Direct-propagation preimages | every `_CONTEXT.md` and `_STATUS.md` pre-SHA-256 in Lane A2/A3 |
| Reliance-hold preflight | `pec_reliance_hold.py` returns `ALLOW` for every write target |

A mismatch returns to checkpoint 2 with drift evidence; it is not reconciled during execution.

## Package-role classification of every touched surface

| Surface | Package role | Classification | Owner at checkpoint-3 preparation | Planned state |
|---|---|---|---|---|
| `_Decomposition/SOFTWARE_DECOMP.md` | working surface | `DIRECT_EDIT` | SCOPE_CHANGE (WORKING_ITEMS) | candidate postimage with the two pre-acceptance front-matter lines; `CURRENT` after checkpoint-3 acceptance |
| `_Decomposition/ScopeLedger.csv`, `Deliverables.csv`, `ContextBudgetQA.csv`, `Companion_Inventory.csv` | authoritative companion registers | `DIRECT_EDIT` | SCOPE_CHANGE | candidate postimages byte-for-byte |
| `docs/PRD.md` | upstream product authority (outside the decomposition) | `DIRECT_EDIT` (owner-adopted bytes) | SCOPE_CHANGE, applying the owner-adopted candidate | v2.3 candidate bytes with acceptance slots filled |
| 22 `_CONTEXT.md` (Lane A2) | variant-local derived metadata | `DIRECT_EDIT` | SCOPE_CHANGE | exact mirrors below |
| 4 retired `_STATUS.md` (Lane A3) | variant-local lifecycle | `DIRECT_EDIT` | SCOPE_CHANGE | `RETIRED`, exact bytes below |
| all other `_STATUS.md` | lifecycle truth | `NO_CHANGE` | none | unchanged |
| 40 other `_CONTEXT.md` + 2 new | variant-local derived metadata | `NO_CHANGE` now | PROJECT_SETUP (B1) | `STALE_REPIN_REQUIRED` / `NOT_CREATED` |
| 64 `_REFERENCES.md` + 2 new | derived reference packets | `NO_CHANGE` now | PROJECT_SETUP / reference owner (B1) | `STALE_REPIN_REQUIRED` / `NOT_CREATED` |
| DEL-02-08, DEL-02-09 folders | new deliverable scaffolds | `NO_CHANGE` now | preparation via PROJECT_SETUP (A4) | `NOT_CREATED` until A4 |
| `Dependencies.csv` / `_DEPENDENCIES.md` (B3 population) | downstream structured dependency truth | `NO_CHANGE` now | dependency-extract / PROJECT_SETUP (B3) | `STALE_REBUILD_REQUIRED` |
| 32 `ScopeOfWork.md` | derived production contracts | `NO_CHANGE` | WORKING_ITEMS + artifact gates (B4) | per §B4 |
| DEL-00-01 `ADRs.md`, DEL-00-03 `SPEC.md` | accepted derivative artifacts | `NO_CHANGE` | owning deliverable workflows (B5) | `STALE_REVIEW_REQUIRED` |
| `v2/config/loops.json`, `loops.schema.json`, `v2/src/pec_v2/core/ports/loop_registry.py` | source / configuration | `NO_CHANGE` | later D-PEC source packet (B6) | `STALE_SOURCE_PACKET_REQUIRED` |
| `_ScopeChange/SCA-005_2026-09-23_2139/` | snapshot / handoff artifact | `RECOMPUTE` | SCOPE_CHANGE | completed at checkpoint-3 preparation (A5) |
| `_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-2_*` | snapshot / handoff artifact | `RECOMPUTE` | HELP_HUMAN after the owner acts | immutable group-2 decision record |
| `_Evaluation/DecompCoverage/COV_SCA005_POSTCHANGE_*` | derived publication artifact (audit evidence) | `RECOMPUTE` | TASK `audit-decomp` (C4) | new immutable snapshot |
| `_Decomposition/_LATEST.md`, `_ScopeChange/_LATEST.md` | snapshot / handoff pointers | `RECOMPUTE` | SCOPE_CHANGE, only after checkpoint-3 acceptance (A6) | revision 1.5 / SCA-005 |
| README, `docs/STATUS.md`, `_COORDINATION.md` | ordinary orientation surfaces | `NO_CHANGE` by SCA-005 | HELP_HUMAN under D-PEC-88 | refreshed after each owner act |
| TM-PEC-023 register row | Task Management authority | `NO_CHANGE` | task-management (B8) | `RESOLVED_BY_DECISION` after checkpoint 3 |
| foreign / tier-0 / instruction surfaces (§Foreign-surface notices) | foreign | `NO_CHANGE` | their owners | notice only |
| decisions, receipts, prior SCA and audit snapshots, frozen corpus | history / evidence | `NO_CHANGE` | none | `HISTORICAL_CURRENT` |

## Lane A — direct writes executed after checkpoint-2 acceptance (checkpoint-3 preparation)

### A1. Apply the decomposition and register postimages

1. Write `CP2_CANDIDATE/_Decomposition/SOFTWARE_DECOMP.md` over the live file with the two pre-acceptance front-matter lines (`Amendment_Preview.md` §"Acceptance-bound tokens"); the acceptance-date slots take the actual dates.
2. Copy the four register postimages over the live registers byte-for-byte.
3. Prove every live postimage SHA-256 equals the accepted candidate (decomposition: the pre-acceptance variant hash, with slots at their actual values recorded).

### A2. `_CONTEXT.md` mirrors (22 deliverables; per-action MODIFY propagation)

For each MODIFY, REMOVE and objective-mapping action the deliverable's `_CONTEXT.md` mirrors exactly the accepted register row, plus the revision-1.5 provenance tail. All other bytes stay unchanged. DEL-07-01 needs no edit (it mirrors only its deliverable-level `OBJ-003`, unchanged by A-79).

#### DEL-00-02 — `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-02_Event_contract_schema_v1/_CONTEXT.md`

Preimage SHA-256 `01cddc447f614885b23e6a7fe978b5cbf51803868acf52048e319389d2e699e2` → planned postimage `beafd08c5112cf5f5b8edb81ecbfdb98128441b8c407eb7e1dc0ec07fe46bb58`. Paired read: no sibling `_MEMORY.md` or `MEMORY.md`. Mirror of the candidate Deliverables.csv row; provenance tail extended.

```diff
-| SupportsObjectives | (none mapped — see §3 mapping notes) |
+| SupportsObjectives | OBJ-003 |
```

```diff
-## Description
-
-Versioned event contract types consumable by daemon, hooks CLI, and adapters; PEC-local schema with pinned-mirror posture pending OI-009; additive evolution. Published one phase ahead of its P3 consumers (DEL-07-01/-03) per the PKG-00 publish/consume mechanic.
+## Description
+
+Versioned event contract types consumable by the hooks CLI bridge, the only remaining bridge; PEC-local schema with pinned-mirror posture pending OI-009; additive evolution. Published one phase ahead of its P3 consumers (DEL-07-01/-03) per the PKG-00 publish/consume mechanic.
```

```diff
-## Envelope notes
-
-OI-009 keeps the contract home open; local schema + pinned mirror until ruled — a shared-runtime ruling moves the home under its own instrument (SOW-074)
+## Envelope notes
+
+OI-009 keeps the contract home open; local schema + pinned mirror until ruled — a ruling for the shared Runtime contracts home (`projects/chirality-runtime/packages/contracts`) moves the home under its own instrument (SOW-074)
```

```diff
-successor), then by revision 1.4 (`current_basis`, SCA-004 successor).
-Fields templated deterministically from
+successor), then by revision 1.4 (`current_basis`, SCA-004 successor),
+then by revision 1.5 (`current_basis`, SCA-005 successor).
+Fields templated deterministically from
```

#### DEL-01-01 — `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model/_CONTEXT.md`

Preimage SHA-256 `d53e451a0e90a7ab2929ca3342dee740fbb6f26cc4c68b52efe663cd2febdf98` → planned postimage `cab17da6dbdd6e086426813406fffa4b478f1607daf8c716ff38e2effb343975`. Paired read: no sibling `_MEMORY.md` or `MEMORY.md`. Mirror of the candidate Deliverables.csv row; provenance tail extended.

```diff
-## Description
-
-Store schema and typed entity model for the record tier: 11 PRD rows, 14 entity types (Workplan/Step/Gate and Package/Deliverable are compound rows) — Loop, Workplan, Step, Gate, Receipt, DecisionRow, Fence, Package, Deliverable, DependencyEdge, RunRecord, CandidateBrief, OrientationSnapshot, DriftFinding.
+## Description
+
+Store schema and typed entity model for the record tier: 16 entity types (Workplan/Step/Gate, Package/Deliverable and WorkGraph/WorkNode are compound rows) — Loop, Workplan, Step, Gate, Receipt, DecisionRow, Fence, Package, Deliverable, DependencyEdge, RunRecord, CandidateBrief, OrientationSnapshot, DriftFinding, WorkGraph, WorkNode. Workplan/Step/Gate is a declared historical-grammar entity whose gate state is re-sourced from decision registers, scope-change pointers and graph BLOCKED nodes; Receipt covers ledger entries and central `RECEIPT.md`; RunRecord is sourced from central receipts, work graphs and the MEMORY run index, with JSON run evidence historical; "remaining items" is a per-loop optional field.
```

```diff
-## Envelope notes
-
-L: 14 entity types and the schema every derivation package depends on; kept one cohesive DDL slice — split (core record entities vs lifecycle/dependency/run entities) only if implementation shows a natural seam
+## Envelope notes
+
+L: 16 entity types (DL-14's 14 plus WorkGraph and WorkNode) and the schema every derivation package depends on; kept one cohesive DDL slice — split (core record entities vs lifecycle/dependency/run/graph entities) only if implementation shows a natural seam
```

```diff
-successor), then by revision 1.4 (`current_basis`, SCA-004 successor).
-Fields templated deterministically from
+successor), then by revision 1.4 (`current_basis`, SCA-004 successor),
+then by revision 1.5 (`current_basis`, SCA-005 successor).
+Fields templated deterministically from
```

#### DEL-01-06 — `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_CONTEXT.md`

Preimage SHA-256 `24f357cc9746b1b0b24991995ed72067062dba9ce7b098b472a5d6eed2db94b2` → planned postimage `1362ed668436b5af79fe54dd5f7ab660dac9ddd29dad2a0d1b0adebb01ad5919`. Paired read: no sibling `_MEMORY.md` or `MEMORY.md`. Mirror of the candidate Deliverables.csv row; provenance tail extended.

```diff
-## Description
-
-PEC-owned local configuration naming the loop locators PEC serves: one loop at P1 (PEC's own build, OI-010), extendable by owner-gated PEC configuration changes. The strict version-1 JSON/schema paths and core-owned typed port are the long-term home and shape under D-PEC-78; each listed loop remains authoritative for its own entrypoint and truth, and no governed act depends on PEC or the registry.
+## Description
+
+PEC-owned local configuration naming the loop locators PEC serves: one loop at P1 (PEC's own build, OI-010), extendable by owner-gated PEC configuration changes. The strict, versioned JSON/schema paths and core-owned typed port are the long-term home and shape under D-PEC-78; each listed loop remains authoritative for its own entrypoint and truth, and no governed act depends on PEC or the registry. Each row declares a closed, PEC-versioned feed profile (profile ID, version, live/historical, basis citation to the loop's own record), PEC's reading hypothesis and never the loop's truth; PEC's own row declares `remaining-loop` now. Feed-profile declarations need a strict schema v2 (`loops.schema.json` v2, `loops.json`, a `RegisteredLoop` field) through a later D-PEC source packet within D-PEC-78 O-A, with VER-001/VER-003 re-run: a new Scope of Work currency obligation (RF-002 stays resolved).
```

```diff
-successor), then by revision 1.4 (`current_basis`, SCA-004 successor).
-Fields templated deterministically from
+successor), then by revision 1.4 (`current_basis`, SCA-004 successor),
+then by revision 1.5 (`current_basis`, SCA-005 successor).
+Fields templated deterministically from
```

#### DEL-02-03 — `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-03_Receipts_ledger_parser_per_loop_grammars/_CONTEXT.md`

Preimage SHA-256 `a787e6379cd1d099ce1237c603c1696f7e3d30b1fde1bb5f3759c6c848d0be46` → planned postimage `aafac18687dae3703e2ea0e903fc790df5123ea78cbba5682a532b54422f1d12`. Paired read: no sibling `_MEMORY.md` or `MEMORY.md`. Mirror of the candidate Deliverables.csv row; provenance tail extended.

```diff
-## Description
-
-`LOOP_RECEIPTS.md` parsing under per-loop grammar, including the D-APP-57 contract where adopted; prose-structured ledgers parsed best-effort with stated limits.
+## Description
+
+Receipt parsing over two grammar generations of one Receipt feed kind: `LOOP_RECEIPTS.md` ledgers under per-loop grammar (live for PEC/Root/Runtime/Bridge; declared historical for App/Piping), including the receipt-contract-v2 marker where a ledger carries it, and central `execution/_Coordination/AgentRuns/<RunID>/RECEIPT.md`; prose-structured ledgers parsed best-effort with stated limits. Name and path retained under SCA-005 (CP1-N); the label "ledger parser (per-loop grammars)" no longer names the central-receipt grammar.
```

```diff
-## Envelope notes
-
-L because grammar varies per loop and SOW-082 (OI-008) keeps the contract-adoption surface open; single domain, but multiple grammars within one parser. Split further only if a loop's grammar proves adversarial
+## Envelope notes
+
+L because grammar varies: the receipt-contract-v2 family (App, Piping, PEC), the Root/Runtime/Bridge prose ledgers and the central `RECEIPT.md` grammar, with SOW-082 (OI-008) still open for the Root, Runtime and Bridge ledgers; single domain, but multiple grammars within one parser. Split line: the central-receipt grammar becomes its own deliverable if implementation demands a split
```

```diff
-successor), then by revision 1.4 (`current_basis`, SCA-004 successor).
-Fields templated deterministically from
+successor), then by revision 1.4 (`current_basis`, SCA-004 successor),
+then by revision 1.5 (`current_basis`, SCA-005 successor).
+Fields templated deterministically from
```

#### DEL-02-04 — `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-04_Run_evidence_JSON_parser/_CONTEXT.md`

Preimage SHA-256 `e5460afb03737fcc61594fb17a769d8b5d5de1faa40f4769c855d282b407f48d` → planned postimage `7f72f6d7304254cb05cf22eb941341627ea2372e549426722311da13595666c2`. Paired read: no sibling `_MEMORY.md` or `MEMORY.md`. Mirror of the candidate Deliverables.csv row; provenance tail extended.

```diff
-## Description
-
-`STATUS.json` / `RUNTIME_SUMMARY.json` under `execution/**` into RunRecord summaries.
+## Description
+
+`STATUS.json` / `RUNTIME_SUMMARY.json` under `execution/**` into RunRecord summaries, as a declared historical grammar for App/Piping and current-by-own-practice for PEC/Root; application-owned Runtime service user-data is operational, never an input. Name and path retained under SCA-005 (CP1-N); run-evidence JSON is no longer the primary RunRecord source.
```

```diff
-successor), then by revision 1.4 (`current_basis`, SCA-004 successor).
-Fields templated deterministically from
+successor), then by revision 1.4 (`current_basis`, SCA-004 successor),
+then by revision 1.5 (`current_basis`, SCA-005 successor).
+Fields templated deterministically from
```

#### DEL-02-05 — `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-05_Dependency_register_parser/_CONTEXT.md`

Preimage SHA-256 `c4eee6211db66a8d5305741a999ee5b054f40b79d83ecefd2e29964a3c604156` → planned postimage `6c3ffcff5cb13773bbac24b821ac7d0e101f99ee414b1806a5bd6006b5e38899`. Paired read: no sibling `_MEMORY.md` or `MEMORY.md`. Mirror of the candidate Deliverables.csv row; provenance tail extended.

```diff
-## Description
-
-`Dependencies.csv` and `WORK_GRAPH.json` into DependencyEdge.
+## Description
+
+`Dependencies.csv`, and `WORK_GRAPH.json` as a declared historical grammar for App/Piping, into DependencyEdge; Markdown `WORK_GRAPH.md` belongs to DEL-02-08.
```

```diff
-successor), then by revision 1.4 (`current_basis`, SCA-004 successor).
-Fields templated deterministically from
+successor), then by revision 1.4 (`current_basis`, SCA-004 successor),
+then by revision 1.5 (`current_basis`, SCA-005 successor).
+Fields templated deterministically from
```

#### DEL-02-06 — `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-06_Workplan_LOOP_INIT_parser/_CONTEXT.md`

Preimage SHA-256 `ff59149c1f01bf47976f412d585481e421c1453134ac6a8e9f6c3d97c3632da0` → planned postimage `3a09d9792f1a025f807ca63239b7a7c9622226880bb9706a62a10d6e093c1ec1`. Paired read: no sibling `_MEMORY.md` or `MEMORY.md`. Mirror of the candidate Deliverables.csv row; provenance tail extended.

```diff
-## Description
-
-Workplans and `LOOP_INIT.md` into Workplan/Step/Gate entities with gate state.
+## Description
+
+`LOOP_INIT.md` loop identity, entrypoint and procedure SHA only; workplans as a declared historical grammar; no step/gate state is read from `LOOP_INIT.md` (gate state is re-sourced per SOW-001). Name "Workplan/LOOP_INIT parser" and path retained under SCA-005 (CP1-N); the label now overstates the live scope.
```

```diff
-## Envelope notes
-
-(none)
+## Envelope notes
+
+M held under SCA-005: scope narrowed to `LOOP_INIT.md` identity plus the historical workplan grammar; may fall to S on re-assessment
```

```diff
-successor), then by revision 1.4 (`current_basis`, SCA-004 successor).
-Fields templated deterministically from
+successor), then by revision 1.4 (`current_basis`, SCA-004 successor),
+then by revision 1.5 (`current_basis`, SCA-005 successor).
+Fields templated deterministically from
```

#### DEL-02-07 — `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/_CONTEXT.md`

Preimage SHA-256 `5f2647cf1e65f29e9ce539707891e7b3259d1f9f7e3da8702eb803826b5a7f81` → planned postimage `fdad5d912567281dabcc61713175a75bed477e225507310f7458b72d698f04c8`. Paired read: no sibling `_MEMORY.md` or `MEMORY.md`. Mirror of the candidate Deliverables.csv row; provenance tail extended.

```diff
-## Description
-
-Per-project `_harness/adapter.yaml` consumed as the feed manifest driving which feeds are read per loop.
+## Description
+
+Per-project `_harness/adapter.yaml` read as a parity-peer input only: PEC's declared census population is compared with the harness `status_glob`, and divergence is reported as a DriftFinding; no longer the feed manifest (per-loop feed profiles in the PEC-owned registry, DEL-01-06, declare the feeds). Name "`adapter.yaml` feed-manifest consumer" and path retained under SCA-005 (CP1-N); the label no longer describes the role.
```

```diff
-successor), then by revision 1.4 (`current_basis`, SCA-004 successor).
-Fields templated deterministically from
+successor), then by revision 1.4 (`current_basis`, SCA-004 successor),
+then by revision 1.5 (`current_basis`, SCA-005 successor).
+Fields templated deterministically from
```

#### DEL-03-03 — `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-03_Drift_classification/_CONTEXT.md`

Preimage SHA-256 `215f30967b8ea683eaba6b0e43d1f4be44838b76ab927481a79e15ec03c94a4e` → planned postimage `0181f52d5a1c4199f3a29eb61c286d4fb916c91833d47f1a5c90c026d6d08a4b`. Paired read: no sibling `_MEMORY.md` or `MEMORY.md`. Mirror of the candidate Deliverables.csv row; provenance tail extended.

```diff
-## Description
-
-Classified drift between successive snapshots, reported as DriftFindings; sources never modified.
+## Description
+
+Classified drift between successive snapshots, reported as DriftFindings; sources never modified. Lag classes: terminal-node lag after the final-PR merge is "trailing by method design" (derived completion, not drift); non-terminal graph-behind-Git is a DriftFinding; unchanged historical surfaces are never staleness.
```

```diff
-successor), then by revision 1.4 (`current_basis`, SCA-004 successor).
-Fields templated deterministically from
+successor), then by revision 1.4 (`current_basis`, SCA-004 successor),
+then by revision 1.5 (`current_basis`, SCA-005 successor).
+Fields templated deterministically from
```

#### DEL-03-05 — `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-05_Stream_loss_recovery_guarantee/_CONTEXT.md`

Preimage SHA-256 `912abd1d8b18a166d324deec0f8f2780243d3d5dda95d684c1fcca04eef95ef9` → planned postimage `4e89162e0c483b34afc4a0e954263c9929ef333a228f656075638c93a7116a17`. Paired read: no sibling `_MEMORY.md` or `MEMORY.md`. Mirror of the candidate Deliverables.csv row; provenance tail extended.

```diff
-| SupportsObjectives | (none mapped — see §3 mapping notes) |
+| SupportsObjectives | OBJ-001 |
```

```diff
-successor), then by revision 1.4 (`current_basis`, SCA-004 successor).
-Fields templated deterministically from
+successor), then by revision 1.4 (`current_basis`, SCA-004 successor),
+then by revision 1.5 (`current_basis`, SCA-005 successor).
+Fields templated deterministically from
```

#### DEL-04-01 — `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/_CONTEXT.md`

Preimage SHA-256 `b6816f9a2878d057d28b182c16ae64d6ec3385e6d44cc71e8062ff76128986ea` → planned postimage `107a293ff8de3b127d2ee2c8c2c71171ee1578ca0d1aaa36842e9c90314aa85f`. Paired read: no sibling `_MEMORY.md` or `MEMORY.md`. Mirror of the candidate Deliverables.csv row; provenance tail extended.

```diff
-## Description
-
-Per-loop orientation: newest applicable receipt, examined-through SHA, gate states, owner directions of record, open tranches/candidate briefs, parked lanes with unparking acts.
+## Description
+
+Per-loop orientation: newest applicable receipt over central receipts and ledgers, examined-through SHA, gate states from decisions, scope-change state and graph BLOCKED nodes, owner directions of record, open tranches/candidate briefs and parked lanes over graph READY/ACTIVE/BLOCKED nodes, each parked lane with its unparking act; terminal completion derived from local Git merge reachability of cited PRs, Explain-cited and advisory.
```

```diff
-successor), then by revision 1.4 (`current_basis`, SCA-004 successor).
-Fields templated deterministically from
+successor), then by revision 1.4 (`current_basis`, SCA-004 successor),
+then by revision 1.5 (`current_basis`, SCA-005 successor).
+Fields templated deterministically from
```

#### DEL-05-01 — `projects/pec/execution/PKG-05_Gate_Evaluation_Decision_Slate/1_Working/DEL-05-01_Gate_precondition_evaluators_Explain_shaped/_CONTEXT.md`

Preimage SHA-256 `83230f78ef5e98bfaff1ecd0bb326220a8974fcc2d3f1c945458013955410989` → planned postimage `142528619a8d497437fbd0232b0bda28d3c720a9356b180455265f325b8cbe15`. Paired read: no sibling `_MEMORY.md` or `MEMORY.md`. Mirror of the candidate Deliverables.csv row; provenance tail extended.

```diff
-| SupportsObjectives | (none mapped — see §3 mapping notes) |
+| SupportsObjectives | OBJ-004 |
```

```diff
-successor), then by revision 1.4 (`current_basis`, SCA-004 successor).
-Fields templated deterministically from
+successor), then by revision 1.4 (`current_basis`, SCA-004 successor),
+then by revision 1.5 (`current_basis`, SCA-005 successor).
+Fields templated deterministically from
```

#### DEL-06-01 — `projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-01_Session_presence_records/_CONTEXT.md`

Preimage SHA-256 `8d867899d0facb0e8ecd79538ac3dd9cc5ed3f32ee61c9dd187dc77f6c3e9d5d` → planned postimage `c9dbe25c44ab78d4e970a94c792865f5b028a905c789111a2c80c9759350d412`. Paired read: no sibling `_MEMORY.md` or `MEMORY.md`. Mirror of the candidate Deliverables.csv row; provenance tail extended.

```diff
-## Description
-
-Harness-reported session records (kind, engine/model attribution, role, loop/package binding, declared write scopes); identity/lifecycle stay daemon-owned.
+## Description
+
+Harness-reported session records (kind, engine/model attribution, role, loop/package binding, declared write scopes), arriving only from an explicitly authorized hooks consumer; identity/lifecycle are Runtime-owned per application (C13).
```

```diff
-successor), then by revision 1.4 (`current_basis`, SCA-004 successor).
-Fields templated deterministically from
+successor), then by revision 1.4 (`current_basis`, SCA-004 successor),
+then by revision 1.5 (`current_basis`, SCA-005 successor).
+Fields templated deterministically from
```

#### DEL-06-04 — `projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-04_Live_hierarchy_edges/_CONTEXT.md`

Preimage SHA-256 `2df7d3d4d569ab828c13dcb8c85c62db89519e807e599a4f895610a9cb393cbf` → planned postimage `a0aee56bc26a769f3ef617ed2f836050c8634b4b7ca3df14554ecee33b47fc30`. Paired read: no sibling `_MEMORY.md` or `MEMORY.md`. RETIRED row: covered-items and objectives cells rendered '(none — retired under SCA-005)' (register cells blank, XRG-003/005); description/envelope-notes mirror the candidate [RETIRED — SCA-005] texts; Name, PackageID, Type, Envelope, PhaseHint, artifacts unchanged.

```diff
-| CoversScopeItems | SOW-029 |
+| CoversScopeItems | (none — retired under SCA-005) |
```

```diff
-| SupportsObjectives | OBJ-003 |
+| SupportsObjectives | (none — retired under SCA-005) |
```

```diff
-## Description
-
-Parent-to-child session edges from daemon and hook feeds.
+## Description
+
+[RETIRED — SCA-005] Retired because SOW-029 is deferred OUT under R1 (trigger T-RT). Original description: Parent-to-child session edges from daemon and hook feeds.
```

```diff
-## Envelope notes
-
-(none)
+## Envelope notes
+
+Retired row retained for register integrity; excluded from active envelope counts (SCA-005).
```

```diff
-successor), then by revision 1.4 (`current_basis`, SCA-004 successor).
-Fields templated deterministically from
+successor), then by revision 1.4 (`current_basis`, SCA-004 successor),
+then by revision 1.5 (`current_basis`, SCA-005 successor).
+Fields templated deterministically from
```

#### DEL-07-02 — `projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-02_Daemon_SSE_subscriber_bridge/_CONTEXT.md`

Preimage SHA-256 `8aadd01be7375624c26989163d4f7e72cb22ad608c1fcea56538fe100fd97e1d` → planned postimage `0bb820ded2fe598b8484ee37ae11ae35a81720f8088b490e5c438725cf6af3f0`. Paired read: no sibling `_MEMORY.md` or `MEMORY.md`. RETIRED row: covered-items and objectives cells rendered '(none — retired under SCA-005)' (register cells blank, XRG-003/005); description/envelope-notes mirror the candidate [RETIRED — SCA-005] texts; Name, PackageID, Type, Envelope, PhaseHint, artifacts unchanged.

```diff
-| CoversScopeItems | SOW-035 |
+| CoversScopeItems | (none — retired under SCA-005) |
```

```diff
-| SupportsObjectives | (none mapped — see §3 mapping notes) |
+| SupportsObjectives | (none — retired under SCA-005) |
```

```diff
-## Description
-
-Declared, attributable subscriber over the runtime daemon's SSE feed.
+## Description
+
+[RETIRED — SCA-005] Retired because SOW-035 is deferred OUT under R1 (trigger T-RT). Original description: Declared, attributable subscriber over the runtime daemon's SSE feed.
```

```diff
-## Envelope notes
-
-(none)
+## Envelope notes
+
+Retired row retained for register integrity; excluded from active envelope counts (SCA-005).
```

```diff
-successor), then by revision 1.4 (`current_basis`, SCA-004 successor).
-Fields templated deterministically from
+successor), then by revision 1.4 (`current_basis`, SCA-004 successor),
+then by revision 1.5 (`current_basis`, SCA-005 successor).
+Fields templated deterministically from
```

#### DEL-07-03 — `projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-03_Hooks_CLI_bridge/_CONTEXT.md`

Preimage SHA-256 `984841782d524e77c912e03fb8ce9a6a0231b69ffe1ca660d7441e71327c894a` → planned postimage `508bd1de276c4235ecadadb2261ed7be470c78e87bdf2c32d45f774103215431`. Paired read: no sibling `_MEMORY.md` or `MEMORY.md`. Mirror of the candidate Deliverables.csv row; provenance tail extended.

```diff
-| SupportsObjectives | (none mapped — see §3 mapping notes) |
+| SupportsObjectives | OBJ-003 |
```

```diff
-successor), then by revision 1.4 (`current_basis`, SCA-004 successor).
-Fields templated deterministically from
+successor), then by revision 1.4 (`current_basis`, SCA-004 successor),
+then by revision 1.5 (`current_basis`, SCA-005 successor).
+Fields templated deterministically from
```

#### DEL-07-04 — `projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-04_cmux_socket_adapter_optional/_CONTEXT.md`

Preimage SHA-256 `805a32c90214b9c3f401e06399d9e205207c629696e432829195975ab03097f9` → planned postimage `5ac0787f665f6603fdc461e5816681584431715019937f292f26c9242dc81b43`. Paired read: no sibling `_MEMORY.md` or `MEMORY.md`. RETIRED row: covered-items and objectives cells rendered '(none — retired under SCA-005)' (register cells blank, XRG-003/005); description/envelope-notes mirror the candidate [RETIRED — SCA-005] texts; Name, PackageID, Type, Envelope, PhaseHint, artifacts unchanged.

```diff
-| CoversScopeItems | SOW-037 |
+| CoversScopeItems | (none — retired under SCA-005) |
```

```diff
-| SupportsObjectives | (none mapped — see §3 mapping notes) |
+| SupportsObjectives | (none — retired under SCA-005) |
```

```diff
-## Description
-
-Optional declared enricher over the cmux socket API; absence changes nothing.
+## Description
+
+[RETIRED — SCA-005] Retired because SOW-037 is deferred OUT by the owner's 2026-09-24 cmux deferral. Original description: Optional declared enricher over the cmux socket API; absence changes nothing.
```

```diff
-## Envelope notes
-
-(none)
+## Envelope notes
+
+Retired row retained for register integrity; excluded from active envelope counts (SCA-005).
```

```diff
-successor), then by revision 1.4 (`current_basis`, SCA-004 successor).
-Fields templated deterministically from
+successor), then by revision 1.4 (`current_basis`, SCA-004 successor),
+then by revision 1.5 (`current_basis`, SCA-005 successor).
+Fields templated deterministically from
```

#### DEL-07-05 — `projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-05_Shared_runtime_client_seam_v2/_CONTEXT.md`

Preimage SHA-256 `b32196a0e7bdbbd44de79916f97d63ce68cf75d7f5350fc1f6d5ac823ce90f4b` → planned postimage `1adc79cd3779b756d80ff681e975adb52e776d612081e52bd0ad5acc618de12e`. Paired read: no sibling `_MEMORY.md` or `MEMORY.md`. RETIRED row: covered-items and objectives cells rendered '(none — retired under SCA-005)' (register cells blank, XRG-003/005); description/envelope-notes mirror the candidate [RETIRED — SCA-005] texts; Name, PackageID, Type, Envelope, PhaseHint, artifacts unchanged.

```diff
-| CoversScopeItems | SOW-087 |
+| CoversScopeItems | (none — retired under SCA-005) |
```

```diff
-| SupportsObjectives | (none mapped — see §3 mapping notes) |
+| SupportsObjectives | (none — retired under SCA-005) |
```

```diff
-## Description
-
-The D-PEC-56 client-seam concept reimplemented against v2 entities.
+## Description
+
+[RETIRED — SCA-005] Retired because SOW-087 is deferred OUT under R1 (trigger T-RT). Original description: The D-PEC-56 client-seam concept reimplemented against v2 entities.
```

```diff
-## Envelope notes
-
-M is provisional: the seam's artifact shape follows the D-PEC-56 concept, not a PEC-*-NNN requirement; re-envelope at WORKING_ITEMS activation if the shape proves larger
+## Envelope notes
+
+M is provisional: the seam's artifact shape follows the D-PEC-56 concept, not a PEC-*-NNN requirement; re-envelope at WORKING_ITEMS activation if the shape proves larger. Retired row retained for register integrity; excluded from active envelope counts (SCA-005).
```

```diff
-successor), then by revision 1.4 (`current_basis`, SCA-004 successor).
-Fields templated deterministically from
+successor), then by revision 1.4 (`current_basis`, SCA-004 successor),
+then by revision 1.5 (`current_basis`, SCA-005 successor).
+Fields templated deterministically from
```

#### DEL-08-01 — `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/_CONTEXT.md`

Preimage SHA-256 `3393b45003a6ab0ae3e54e36831f7bb32399be4fa8aa1b15bbdc213ebed4dc15` → planned postimage `151e1e34330a58467ef0f9aa28a3283b50b84bf5f563b03039f5c6bcd9273985`. Paired read: no sibling `_MEMORY.md` or `MEMORY.md`. Mirror of the candidate Deliverables.csv row; provenance tail extended.

```diff
-## Envelope notes
-
-OI-006 determines the token mechanism (PEC-local vs daemon registry); the socket+access-class core is stable either way, but the auth half may be reworked on ruling
+## Envelope notes
+
+OI-006 determines the PEC-local token mechanism (Runtime token registries are private to each application's Runtime instance, so no shared registry exists to reuse); the socket+access-class core is stable either way, but the auth half may be reworked on ruling
```

```diff
-successor), then by revision 1.4 (`current_basis`, SCA-004 successor).
-Fields templated deterministically from
+successor), then by revision 1.4 (`current_basis`, SCA-004 successor),
+then by revision 1.5 (`current_basis`, SCA-005 successor).
+Fields templated deterministically from
```

#### DEL-08-05 — `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-05_SSE_delta_presence_subscription/_CONTEXT.md`

Preimage SHA-256 `d1bbae9720e13b66b9ab2267657b10910e134564dfcb1c4fc616637817ef8daa` → planned postimage `ba3f7d6e10d52c9b6fc1185538d891ccad0833afea16107fd1b060d5cd4ae31d`. Paired read: no sibling `_MEMORY.md` or `MEMORY.md`. Mirror of the candidate Deliverables.csv row; provenance tail extended.

```diff
-| SupportsObjectives | (none mapped — see §3 mapping notes) |
+| SupportsObjectives | OBJ-001;OBJ-003 |
```

```diff
-successor), then by revision 1.4 (`current_basis`, SCA-004 successor).
-Fields templated deterministically from
+successor), then by revision 1.4 (`current_basis`, SCA-004 successor),
+then by revision 1.5 (`current_basis`, SCA-005 successor).
+Fields templated deterministically from
```

#### DEL-09-05 — `projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-05_Presence_board/_CONTEXT.md`

Preimage SHA-256 `6c5455c38b85003e3632e52a961e0aae150eb4e25567bd6378d0c05207085569` → planned postimage `cd2b2f6b4e14c2b47d9ee98f545cdc27f006275c92d3b01ef1d3142c6b52cab9`. Paired read: no sibling `_MEMORY.md` or `MEMORY.md`. Mirror of the candidate Deliverables.csv row; provenance tail extended.

```diff
-## Description
-
-Sessions x worktrees x live hierarchy with heartbeat age and advisory overlap warnings.
+## Description
+
+Sessions (when hook-reported) x worktrees x graph-declared activity with heartbeat/scan age and advisory overlap warnings; live hierarchy deferred with SOW-029; declared activity is record tier, never liveness.
```

```diff
-successor), then by revision 1.4 (`current_basis`, SCA-004 successor).
-Fields templated deterministically from
+successor), then by revision 1.4 (`current_basis`, SCA-004 successor),
+then by revision 1.5 (`current_basis`, SCA-005 successor).
+Fields templated deterministically from
```

#### DEL-10-08 — `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-08_Stream_loss_recovery_demonstration/_CONTEXT.md`

Preimage SHA-256 `9c320e3795b874819dde7db11e0a4c3550dad32b3488ef1ba70b347ffaa7a51c` → planned postimage `d08c2b9050b93b1ca0581b5b08b39334c129e2dc47ad2b72bad9485ab6ae18d0`. Paired read: no sibling `_MEMORY.md` or `MEMORY.md`. Mirror of the candidate Deliverables.csv row; provenance tail extended.

```diff
-| SupportsObjectives | (none mapped — see §3 mapping notes) |
+| SupportsObjectives | OBJ-001 |
```

```diff
-successor), then by revision 1.4 (`current_basis`, SCA-004 successor).
-Fields templated deterministically from
+successor), then by revision 1.4 (`current_basis`, SCA-004 successor),
+then by revision 1.5 (`current_basis`, SCA-005 successor).
+Fields templated deterministically from
```



### A3. `_STATUS.md` retirement acts (REMOVE A-34, A-35, A-36, A-78)

Before each write, read the `_STATUS.md` and any sibling `_MEMORY.md` / `MEMORY.md` (none exists for these four; paired read recorded). The scope-change method names `tools/scaffolding/write_status.sh {folder} RETIRED WORKING_ITEMS`, but that tool accepts only `OPEN`..`ISSUED` (L86) and exits 2 on RETIRED (L101); Root `docs/SPEC.md` §3.2 has no RETIRED lifecycle value (L985: RETIRED is "never an active project lifecycle value"), and `tools/practitioner_harness/adapter_project.py` L124–125 rejects RETIRED for a non-Root project (PEC has no `_harness/adapter.yaml` today, so nothing breaks now). The retirement is therefore a hand-authored exact edit, following the scope-change contract's non-destructive rule (owner question Q-CP2-1). The Remaining item is ticked `[x]` per PEC's closing convention (DEL-01-03 `_STATUS.md`, D-PEC-87 L-1a) with its text kept, plus LOOP_INIT §5's `NOT_SELECTABLE_UNTIL:` marker so the tick does not read as completion. A verified state-preserving variant (lifecycle left `OPEN`, same History line and Remaining disposal) exists for option (c) of Q-CP2-1; its hashes are in the drafting evidence (`PROPAGATION_EDITS.json`, `alternative_state_preserving`). Folders and every other file are kept; nothing is deleted; the single open `## Remaining` item of each is disposed non-destructively so `loop/LOOP_INIT.md` §4 can no longer select it.

#### DEL-06-04 — `projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-04_Live_hierarchy_edges/_STATUS.md`

Preimage SHA-256 `8cfb8b8800a591124cc0e24aeae9d643f278e8845bf99cd1bb90170a471d4726` → planned postimage `eeae22fbd49a8f4105139480e45db6c9c1147d343cfa2b8a83bd8bad039724bc`. Paired read done: neither _MEMORY.md nor MEMORY.md exists beside _STATUS.md. Remaining disposal follows the PEC closed-item convention (tick `- [x]` + one History line citing authority; DEL-01-03 _STATUS.md under D-PEC-87 L-1a) and adds LOOP_INIT §5 Step 1's own `NOT_SELECTABLE_UNTIL:` marker so the tick is not read as completion.

```diff
-**Current State:** OPEN
+**Current State:** RETIRED
```

```diff
-**Last Updated:** 2026-07-25
+**Last Updated:** 2026-09-25
```

```diff
-- 2026-07-25 — State set to OPEN (PREPARATION)
-
-## Remaining
+- 2026-07-25 — State set to OPEN (PREPARATION)
+- 2026-09-25 — State set to RETIRED (WORKING_ITEMS; hand-authored exact edit, as `write_status.sh` admits no RETIRED state) under SCA-005 checkpoint-2 accepted propagation plan, applied at checkpoint 3 (`execution/_ScopeChange/SCA-005_2026-09-23_2139/`); R1 deferral: SOW-029 deferred OUT under R1 (trigger T-RT). Folder and every file retained; nothing deleted. DEL-06-04-REM-001 closed unexecuted by retirement, not completed; no inquiry ran and no work is selected. No CHECKING, ISSUED or artifact acceptance is implied.
+
+## Remaining
```

```diff
-- [ ] DEL-06-04-REM-001 — Inspect and map existing source-state-bound evidence for SOW-029 live parent-child hierarchy edges from daemon/hook feeds and anticipated hierarchy-maintenance tests. Cover the exact linked claims; distinguish observed implementation, bounded local absence, missing/unmapped evidence, finite method execution and historical acceptance. Retain UNKNOWN where evidence is unavailable and return exact unresolved obligations for owner disposition. This item is read-only inquiry and a derivative evidence report; any new contract, implementation, test, measurement run, acceptance or production act requires a separate ruling.
+- [x] DEL-06-04-REM-001 — Inspect and map existing source-state-bound evidence for SOW-029 live parent-child hierarchy edges from daemon/hook feeds and anticipated hierarchy-maintenance tests. Cover the exact linked claims; distinguish observed implementation, bounded local absence, missing/unmapped evidence, finite method execution and historical acceptance. Retain UNKNOWN where evidence is unavailable and return exact unresolved obligations for owner disposition. This item is read-only inquiry and a derivative evidence report; any new contract, implementation, test, measurement run, acceptance or production act requires a separate ruling.
```

```diff
-  (gated: owner authorizes the exact linked evidence-only read scope and creation of the derivative report/evidence manifest under projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-04_Live_hierarchy_edges/_run_records/REMAINING_EVIDENCE_DEL-06-04-REM-001/; current exact-target reliance preflight)
+  (gated: owner authorizes the exact linked evidence-only read scope and creation of the derivative report/evidence manifest under projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-04_Live_hierarchy_edges/_run_records/REMAINING_EVIDENCE_DEL-06-04-REM-001/; current exact-target reliance preflight)
+  (`NOT_SELECTABLE_UNTIL: a later accepted scope-change amendment reinstates SOW-029 and DEL-06-04 after trigger T-RT`) [RETIRED — SCA-005] Closed unexecuted by retirement, not completed; original item text retained above.
```

#### DEL-07-02 — `projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-02_Daemon_SSE_subscriber_bridge/_STATUS.md`

Preimage SHA-256 `b05edcc916edf44db252bcd8ca055391ec9d48525e23aaead17f962af4f0f45f` → planned postimage `8eda30e178b6164c3caa4a5afd97271e49cbec2f1232a0ffc4c4fe4ccbc93b8a`. Paired read done: neither _MEMORY.md nor MEMORY.md exists beside _STATUS.md. Remaining disposal follows the PEC closed-item convention (tick `- [x]` + one History line citing authority; DEL-01-03 _STATUS.md under D-PEC-87 L-1a) and adds LOOP_INIT §5 Step 1's own `NOT_SELECTABLE_UNTIL:` marker so the tick is not read as completion.

```diff
-**Current State:** OPEN
+**Current State:** RETIRED
```

```diff
-**Last Updated:** 2026-07-25
+**Last Updated:** 2026-09-25
```

```diff
-- 2026-07-25 — State set to OPEN (PREPARATION)
-
-## Remaining
+- 2026-07-25 — State set to OPEN (PREPARATION)
+- 2026-09-25 — State set to RETIRED (WORKING_ITEMS; hand-authored exact edit, as `write_status.sh` admits no RETIRED state) under SCA-005 checkpoint-2 accepted propagation plan, applied at checkpoint 3 (`execution/_ScopeChange/SCA-005_2026-09-23_2139/`); R1 deferral: SOW-035 deferred OUT under R1 (trigger T-RT). Folder and every file retained; nothing deleted. DEL-07-02-REM-001 closed unexecuted by retirement, not completed; no inquiry ran and no work is selected. No CHECKING, ISSUED or artifact acceptance is implied.
+
+## Remaining
```

```diff
-- [ ] DEL-07-02-REM-001 — Inspect and map existing source-state-bound evidence for SOW-035 owner-authorized bridge artifact, declaration/attribution contract, event-contract mapping and claim-relevant tests. Cover the exact linked claims; distinguish observed implementation, bounded local absence, missing/unmapped evidence, finite method execution and historical acceptance. Retain UNKNOWN where evidence is unavailable and return exact unresolved obligations for owner disposition. This item is read-only inquiry and a derivative evidence report; any new contract, implementation, test, measurement run, acceptance or production act requires a separate ruling.
+- [x] DEL-07-02-REM-001 — Inspect and map existing source-state-bound evidence for SOW-035 owner-authorized bridge artifact, declaration/attribution contract, event-contract mapping and claim-relevant tests. Cover the exact linked claims; distinguish observed implementation, bounded local absence, missing/unmapped evidence, finite method execution and historical acceptance. Retain UNKNOWN where evidence is unavailable and return exact unresolved obligations for owner disposition. This item is read-only inquiry and a derivative evidence report; any new contract, implementation, test, measurement run, acceptance or production act requires a separate ruling.
```

```diff
-  (gated: owner authorizes the exact linked evidence-only read scope and creation of the derivative report/evidence manifest under projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-02_Daemon_SSE_subscriber_bridge/_run_records/REMAINING_EVIDENCE_DEL-07-02-REM-001/; current exact-target reliance preflight)
+  (gated: owner authorizes the exact linked evidence-only read scope and creation of the derivative report/evidence manifest under projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-02_Daemon_SSE_subscriber_bridge/_run_records/REMAINING_EVIDENCE_DEL-07-02-REM-001/; current exact-target reliance preflight)
+  (`NOT_SELECTABLE_UNTIL: a later accepted scope-change amendment reinstates SOW-035 and DEL-07-02 after trigger T-RT`) [RETIRED — SCA-005] Closed unexecuted by retirement, not completed; original item text retained above.
```

#### DEL-07-04 — `projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-04_cmux_socket_adapter_optional/_STATUS.md`

Preimage SHA-256 `10905472a88d4e3d6ca96cfe22769106fa408b79097e403b0fb65b499a34b726` → planned postimage `2aaec8fd5ba027c5a7cc34d1a94a972ca8ddb2c7a1a59db52e53be8d12f2de5e`. Paired read done: neither _MEMORY.md nor MEMORY.md exists beside _STATUS.md. Remaining disposal follows the PEC closed-item convention (tick `- [x]` + one History line citing authority; DEL-01-03 _STATUS.md under D-PEC-87 L-1a) and adds LOOP_INIT §5 Step 1's own `NOT_SELECTABLE_UNTIL:` marker so the tick is not read as completion.

```diff
-**Current State:** OPEN
+**Current State:** RETIRED
```

```diff
-**Last Updated:** 2026-07-25
+**Last Updated:** 2026-09-25
```

```diff
-- 2026-07-25 — State set to OPEN (PREPARATION)
-
-## Remaining
+- 2026-07-25 — State set to OPEN (PREPARATION)
+- 2026-09-25 — State set to RETIRED (WORKING_ITEMS; hand-authored exact edit, as `write_status.sh` admits no RETIRED state) under SCA-005 checkpoint-2 accepted propagation plan, applied at checkpoint 3 (`execution/_ScopeChange/SCA-005_2026-09-23_2139/`); cmux deferral: SOW-037 deferred OUT by the owner's 2026-09-24 cmux deferral (re-entry only by a later owner direction). Folder and every file retained; nothing deleted. DEL-07-04-REM-001 closed unexecuted by retirement, not completed; no inquiry ran and no work is selected. No CHECKING, ISSUED or artifact acceptance is implied.
+
+## Remaining
```

```diff
-- [ ] DEL-07-04-REM-001 — Inspect and map existing source-state-bound evidence for SOW-037 optional cmux adapter, any accepted activation/contract and claim-relevant verification, declaration, attribution and graceful absence; optionality remains unchanged. Cover the exact linked claims; distinguish observed implementation, bounded local absence, missing/unmapped evidence, finite method execution and historical acceptance. Retain UNKNOWN where evidence is unavailable and return exact unresolved obligations for owner disposition. This item is read-only inquiry and a derivative evidence report; any new contract, implementation, test, measurement run, acceptance or production act requires a separate ruling.
+- [x] DEL-07-04-REM-001 — Inspect and map existing source-state-bound evidence for SOW-037 optional cmux adapter, any accepted activation/contract and claim-relevant verification, declaration, attribution and graceful absence; optionality remains unchanged. Cover the exact linked claims; distinguish observed implementation, bounded local absence, missing/unmapped evidence, finite method execution and historical acceptance. Retain UNKNOWN where evidence is unavailable and return exact unresolved obligations for owner disposition. This item is read-only inquiry and a derivative evidence report; any new contract, implementation, test, measurement run, acceptance or production act requires a separate ruling.
```

```diff
-  (gated: owner authorizes the exact linked evidence-only read scope and creation of the derivative report/evidence manifest under projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-04_cmux_socket_adapter_optional/_run_records/REMAINING_EVIDENCE_DEL-07-04-REM-001/; current exact-target reliance preflight)
+  (gated: owner authorizes the exact linked evidence-only read scope and creation of the derivative report/evidence manifest under projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-04_cmux_socket_adapter_optional/_run_records/REMAINING_EVIDENCE_DEL-07-04-REM-001/; current exact-target reliance preflight)
+  (`NOT_SELECTABLE_UNTIL: a later owner direction and accepted scope-change amendment reinstate SOW-037 and DEL-07-04`) [RETIRED — SCA-005] Closed unexecuted by retirement, not completed; original item text retained above.
```

#### DEL-07-05 — `projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-05_Shared_runtime_client_seam_v2/_STATUS.md`

Preimage SHA-256 `4fb85e33b8c28cc220f8c0e40a66705929f96aa0abcbe793d07be731731d30df` → planned postimage `19123cf8a3ca8e19a60bac8849c9008d33a025e245dabffb4bd82f4cc8383ded`. Paired read done: neither _MEMORY.md nor MEMORY.md exists beside _STATUS.md. Remaining disposal follows the PEC closed-item convention (tick `- [x]` + one History line citing authority; DEL-01-03 _STATUS.md under D-PEC-87 L-1a) and adds LOOP_INIT §5 Step 1's own `NOT_SELECTABLE_UNTIL:` marker so the tick is not read as completion.

```diff
-**Current State:** OPEN
+**Current State:** RETIRED
```

```diff
-**Last Updated:** 2026-07-25
+**Last Updated:** 2026-09-25
```

```diff
-- 2026-07-25 — State set to OPEN (PREPARATION)
-
-## Remaining
+- 2026-07-25 — State set to OPEN (PREPARATION)
+- 2026-09-25 — State set to RETIRED (WORKING_ITEMS; hand-authored exact edit, as `write_status.sh` admits no RETIRED state) under SCA-005 checkpoint-2 accepted propagation plan, applied at checkpoint 3 (`execution/_ScopeChange/SCA-005_2026-09-23_2139/`); R1 deferral: SOW-087 deferred OUT under R1 (trigger T-RT). Folder and every file retained; nothing deleted. DEL-07-05-REM-001 closed unexecuted by retirement, not completed; no inquiry ran and no work is selected. No CHECKING, ISSUED or artifact acceptance is implied.
+
+## Remaining
```

```diff
-- [ ] DEL-07-05-REM-001 — Inspect and map existing source-state-bound evidence for SOW-087 shared-runtime client seam, v2 entity integration, PKG-00 event-contract consumption and claim-relevant tests; retain root runtime ownership. Cover the exact linked claims; distinguish observed implementation, bounded local absence, missing/unmapped evidence, finite method execution and historical acceptance. Retain UNKNOWN where evidence is unavailable and return exact unresolved obligations for owner disposition. This item is read-only inquiry and a derivative evidence report; any new contract, implementation, test, measurement run, acceptance or production act requires a separate ruling.
+- [x] DEL-07-05-REM-001 — Inspect and map existing source-state-bound evidence for SOW-087 shared-runtime client seam, v2 entity integration, PKG-00 event-contract consumption and claim-relevant tests; retain root runtime ownership. Cover the exact linked claims; distinguish observed implementation, bounded local absence, missing/unmapped evidence, finite method execution and historical acceptance. Retain UNKNOWN where evidence is unavailable and return exact unresolved obligations for owner disposition. This item is read-only inquiry and a derivative evidence report; any new contract, implementation, test, measurement run, acceptance or production act requires a separate ruling.
```

```diff
-  (gated: owner authorizes the exact linked evidence-only read scope and creation of the derivative report/evidence manifest under projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-05_Shared_runtime_client_seam_v2/_run_records/REMAINING_EVIDENCE_DEL-07-05-REM-001/; current exact-target reliance preflight)
+  (gated: owner authorizes the exact linked evidence-only read scope and creation of the derivative report/evidence manifest under projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-05_Shared_runtime_client_seam_v2/_run_records/REMAINING_EVIDENCE_DEL-07-05-REM-001/; current exact-target reliance preflight)
+  (`NOT_SELECTABLE_UNTIL: a later accepted scope-change amendment reinstates SOW-087 and DEL-07-05 after trigger T-RT`) [RETIRED — SCA-005] Closed unexecuted by retirement, not completed; original item text retained above.
```



### A4. ADD propagation — preparation of DEL-02-08 and DEL-02-09 (A-19, A-20)

Through WORKING_ITEMS with project-setup, the eligible actor runs the effective source-qualified `preparation` skill, recorded in the ordered `methods` field as `[{kind: "skill", name: "preparation", source: <descriptor.source>, sourceRootId: <descriptor.sourceRootId>}]` from the discovered descriptor (no origin is hard-coded here). Targets: `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser/` and `…/DEL-02-09_MEMORY_run_index_parser/` (folder names follow the PROJECT_SETUP naming rule from the accepted names; the rule's output is recorded, not pre-empted). Expected files: `_CONTEXT.md` (mirroring the accepted rows at revision 1.5), `_STATUS.md` (`OPEN`), `_REFERENCES.md`, `_DEPENDENCIES.md`, and a deliverable-local `Dependencies.csv` with the ANCHOR rows (B3). This clears the two DRB-008 warnings. Any read of `_STATUS.md` is paired with sibling `MEMORY.md`.

### A5. SCA-owned snapshot completion

In this snapshot folder: keep `Brief.md`, `Impact_Assessment.md`, `Amendment_Actions.csv`, `Pre_Change_Coverage.json` and every checkpoint-2 artifact byte-unchanged; generate `Supersession_Map.csv` with the deterministic accumulator (never by hand):

`python3 tools/coordination/accumulate_supersession_map.py --prior-map projects/pec/execution/_ScopeChange/SCA-004_2026-08-02_2325/Supersession_Map.csv --delta projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139/Supersession_Delta.csv --output-map projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139/Supersession_Map.csv`

(dry-run to scratch during preparation: exit 0, 29 rows, 0 findings); copy the post-change audit `coverage_summary.json` bytes to `Post_Change_Coverage.json`; write `RUN_SUMMARY.md` and update `Decision_Log.md` and `Handoff_State.md` with hashes, results and the closure verdict.

### A6. Pointers — only after checkpoint-3 acceptance

`_Decomposition/_LATEST.md` becomes the revision-1.5 handoff (citing the SCA-004 repairs closed on 2026-08-09 in `_Coordination/PEC_CURRENCY_REPAIR_CLOSEOUT_2026-08-09/HANDOFF_STATE.md` rather than carrying forward its stale "Stale populations" list) and `_ScopeChange/_LATEST.md` names SCA-005. The decomposition front-matter lines return to their accepted postimage values in the same act. No pointer moves before the owner's checkpoint-3 acceptance.

## Lane B — downstream reruns not executed by WORKING_ITEMS

Each item is recorded open in `Handoff_State.md`; none is authorized or satisfied by the Lane A writes.

### B1. PROJECT_SETUP metadata re-pin

Re-pin to revision 1.5 the provenance of the 40 `_CONTEXT.md` files not written in A2 and all 64 existing `_REFERENCES.md` (semantic fields unchanged), and create the two new `_REFERENCES.md` in A4. The SCA-004 re-pin (commit `1c6ecc6d9`, 64/64 at revision 1.4) is the precedent.

### B2. Pre-existing stale pointer text

`_Decomposition/_LATEST.md` L34–38 and SCA-004 `Handoff_State.md` (`MetadataAlignmentState NOT_STARTED`) still describe SCA-004 populations that were repaired by 2026-08-09. A6 supersedes the first; the second is historical and stays byte-unchanged.

### B3. Dependency extraction and topology

Owner: dependency-extract (via TASK) / PROJECT_SETUP. Representation for every retirement: keep the row, set `Status=RETIRED` (allowed by `validate_dependencies_schema.py`), set `LastSeen` to the act date, and prefix `Notes` with `Retired under SCA-005 (<reason>); ` — rows are never deleted.

| Change | Rows | Reason |
|---|---|---|
| Retire rows owned by the four retired registers | EXECUTION: DEP-06-04-003..006, DEP-07-02-003/004, DEP-07-04-003/004, DEP-07-05-003/005 (10); ANCHOR: DEP-06-04-001/002, DEP-07-02-001/002, DEP-07-04-001/002, DEP-07-05-001/002 (8; the TRACES_TO_REQUIREMENT evidence becomes false once the four scope items are OUT) | A-34, A-35, A-36, A-78 |
| Retire the surviving dependant on a retired deliverable | `DEP-09-05-005` (DEL-09-05 → DEL-06-04, PREREQUISITE, E-N02 PHASE_TENSION) | A-33, A-38 |
| Replace the `[E-P25]` manifest edge | retire `DEP-03-01-014` (DEL-03-01 → DEL-02-07); refresh the evidence of the existing `DEP-03-01-007` (DEL-03-01 → DEL-01-06, `[E-P18]`) to cite the registry feed profiles. A literal re-point would duplicate the 03-01 → 01-06 pair | A-07, A-18 |
| Add edges for the new deliverables (PLANNED; final rows are dependency-extract's) | ANCHOR `IMPLEMENTS_NODE`/`TRACES_TO_REQUIREMENT` for DEL-02-08 (PKG-02, SOW-095) and DEL-02-09 (PKG-02, SOW-096); EXECUTION DEL-02-08 → DEL-01-01, DEL-02-09 → DEL-01-01, DEL-03-01 → DEL-02-08, DEL-03-01 → DEL-02-09; optional DEL-04-01 → DEL-02-08 (transitively redundant) | A-08, A-09, A-19, A-20 |
| Refresh consumer mirrors in `_DEPENDENCIES.md` | DEL-00-02 (E-A03, E-A04, E-N01); DEL-01-01 (E-P14); DEL-01-02 (E-N09); DEL-06-01 (E-N10); DEL-07-01 (E-P48, E-P50); DEL-07-03 (E-P47); DEL-09-05 (E-N02); DEL-03-01 (E-P25, E-P18). DEL-08-02 E-N13 is already struck through | same |

Topology (planned; `analyze_dep_closure.py` on scratch copies during preparation): 119 EXECUTION edges / 0 SCCs / 0 bidirectional pairs now → 108 after the retirements (0 SCCs; isolated nodes 2 → 6, the four retired DELs added) → 107 after replacing `[E-P25]` → 111 with the four planned new edges (112 with the optional DEL-04-01 edge), 0 SCCs expected. The final count is UNKNOWN until dependency-extract writes the rows; closure requires the strict validator at 0/0 and `analyze_dep_closure.py` at 0 SCCs / 0 bidirectional pairs.

### B4. Scope of Work currency per deliverable (WORKING_ITEMS + REVIEW / owner artifact gates)

Re-derived against the current tree (all 32 contracts byte-unchanged since checkpoint 1; every lifecycle matches Impact Assessment §7.1):

| DEL | Lifecycle (now) | Current SOW SHA-256 | SCA-005 cause | Currency class | `@3623b958b` pin | false rev-1.1 claim |
|---|---|---|---|---|:-:|:-:|
| DEL-00-01 | CHECKING | `433461504444…` | C13/D-GOV-43 runtime-ownership premise (ADR carried posture 3) | `STALE_REVIEW_REQUIRED` |  |  |
| DEL-00-03 | CHECKING | `3e4f0efc7758…` | quotations of §1.4/§4 charter; SPEC §4/§6/§8 | `STALE_REVIEW_REQUIRED` |  |  |
| DEL-01-01 | INITIALIZED | `43f1f57a13bb…` | entity model re-sourced (A-01, A-12) | `STALE_REBUILD_REQUIRED` | ✓ | ✓ |
| DEL-01-03 | IN_PROGRESS | `986ef15532cd…` | CON-001 quotes stale 'pec ledger prose-structured'; content-minimal boundary applies to Markdown feeds | `STALE_REVIEW_REQUIRED (quotation)` | ✓ | ✓ |
| DEL-01-04 | INITIALIZED | `4dd777f8f30c…` | none | `housekeeping only` | ✓ | ✓ |
| DEL-01-05 | IN_PROGRESS | `53ba3be30415…` | PEC-API-001 citation (D-GOV-20 → D-GOV-43) | `STALE_REVIEW_REQUIRED (quotation)` |  |  |
| DEL-01-06 | INITIALIZED | `5fdcfd968345…` | feed-profile declarations, schema v2 obligation, five-loop claims (A-10, A-11, A-13) | `STALE_REBUILD_REQUIRED (new obligation; RF-002 stays RESOLVED; gated on B6)` |  |  |
| DEL-02-01 | INITIALIZED | `5d286ec97f4c…` | per-loop optional 'remaining items'; PEC-RCN-002 quotation; guard STATE note (RETIRED) | `STALE_REVIEW_REQUIRED` | ✓ | ✓ |
| DEL-02-02 | INITIALIZED | `5f20b1c48f4f…` | PEC-RCN-002 quotation only | `STALE_REVIEW_REQUIRED (quotation)` | ✓ | ✓ |
| DEL-02-03 | INITIALIZED | `c3e7928cbbcf…` | central RECEIPT.md grammar; OI-008 re-expressed (A-03, A-14) | `STALE_REBUILD_REQUIRED` | ✓ | ✓ |
| DEL-02-04 | INITIALIZED | `bdb4eea0143e…` | historical JSON grammar; daemon referent; CON-003 false | `STALE_REBUILD_REQUIRED` | ✓ | ✓ |
| DEL-02-05 | INITIALIZED | `192df47d8d3d…` | WORK_GRAPH.json historical; .md to DEL-02-08 | `STALE_REBUILD_REQUIRED` | ✓ | ✓ |
| DEL-02-06 | INITIALIZED | `c8ca6292bae1…` | LOOP_INIT identity only; workplans historical; CON-005 false | `STALE_REBUILD_REQUIRED` | ✓ | ✓ |
| DEL-02-07 | INITIALIZED | `d044499ab5ac…` | re-purposed to parity-peer reader (Q2 b) | `STALE_REBUILD_REQUIRED` |  |  |
| DEL-03-01 | INITIALIZED | `564955235aea…` | ingest boundary follows feed list; [E-P25] replaced (B3) | `STALE_REVIEW_REQUIRED` |  |  |
| DEL-03-02 | INITIALIZED | `d1335c01c546…` | none | `housekeeping only` | ✓ | ✓ |
| DEL-03-03 | INITIALIZED | `5ce8ab72425a…` | new lag classes (A-21) | `STALE_REVIEW_REQUIRED (new content)` | ✓ | ✓ |
| DEL-03-04 | INITIALIZED | `e007f5307fce…` | stale P1 quotation; TBD-003 parity set (Q10 (a)) | `STALE_REVIEW_REQUIRED` | ✓ | ✓ |
| DEL-03-06 | INITIALIZED | `90de9c2d93d8…` | none | `current` |  |  |
| DEL-04-01 | INITIALIZED | `6f4e8c66a571…` | orientation re-sourced (A-02, A-22); no reliance redesign (D-PEC-90 note) | `STALE_REBUILD_REQUIRED` |  |  |
| DEL-04-02 | INITIALIZED | `a2b50f870aa3…` | none | `current` |  |  |
| DEL-04-03 | INITIALIZED | `6ec7432bf8cf…` | feed set for per-feed freshness | `STALE_REVIEW_REQUIRED` |  |  |
| DEL-04-05 | INITIALIZED | `933c012cf16b…` | absent/historical ledger becomes normal case | `STALE_REVIEW_REQUIRED` | ✓ | ✓ |
| DEL-08-01 | INITIALIZED | `8ac1dc050efb…` | OI-006 re-expressed; D-GOV-20 citation | `STALE_REVIEW_REQUIRED` |  |  |
| DEL-08-02 | CHECKING | `eb171e9dac40…` | none | `housekeeping only` | ✓ | ✓ |
| DEL-08-03 | INITIALIZED | `013c615a0c91…` | SOW-083 quotation | `STALE_REVIEW_REQUIRED (quotation)` |  |  |
| DEL-08-04 | INITIALIZED | `6d1ec1ad9796…` | inherits DEL-04-01/08-01 refresh | `STALE_REVIEW_REQUIRED (quotation)` |  |  |
| DEL-10-01 | CHECKING | `40d47fb636ca…` | none: Q9 dropped Seq 72 (the IA's conditional review does not apply) | `current` |  |  |
| DEL-10-02 | INITIALIZED | `99730e4e85ce…` | none | `housekeeping only` | ✓ | ✓ |
| DEL-10-03 | INITIALIZED | `cbcabbde6882…` | none | `housekeeping only` | ✓ | ✓ |
| DEL-10-10 | INITIALIZED | `640f23711f93…` | TBD-005 'structurally different loop'; DEL-02-05 dependency premise | `STALE_REVIEW_REQUIRED` |  |  |
| DEL-10-11 | INITIALIZED | `9b90f33ba03a…` | none | `current` |  |  |

Totals: 23 contracts need currency work (8 rebuild, 15 review), 5 housekeeping only, 4 current. The IA counted 24 with DEL-10-01 conditional on Q9; Q9 dropped Seq 72, so DEL-10-01 is current and the count is 23. Pins: 16; false rev-1.1 claims: 16.

Housekeeping fixes that ride the same pass (non-scope): the unresolvable `@3623b958b` basis pin in 16 contracts, and the false "`_REFERENCES.md` still names revision 1.1" claim in **16** contracts (the accepted evidence said 13; DEL-01-03, DEL-01-04 and DEL-08-02 use an unquoted form the inventory missed).

DEL-01-06: its accepted SOW (`5fdcfd96…a2fa8`) still requires strict version 1 (CLM-003, TBD-002, REQ-001, REQ-005, CON-001) and tests only v1 (VER-001, VER-003). It needs a rebuild for feed profiles, schema v2 and the `RegisteredLoop` field, gated on the later D-PEC source packet (B6). RF-002 stays RESOLVED.

Carry-forward for the parser SOWs (DEL-02-01, DEL-02-08, DEL-02-09): the DEL-01-03 content-minimal guard admits only `OPEN`..`ISSUED` as STATE values (true before and after D-PEC-87/89/91), so `RETIRED`, graph node states and run tokens are CON-001 cases those SOWs must address. The two new deliverables receive first SOWs through the ordinary preparation → Scope of Work path; the four retired deliverables get none.

### B5. Accepted derivative artifacts (stale review, owning deliverable workflows + exact-byte gates)

| Artifact | Lifecycle | Stale premise | Action |
|---|---|---|---|
| DEL-00-01 `artifacts/v2/ADRs.md` | CHECKING | runtime-ownership premise (D-GOV-20 → D-GOV-43 A2, ADR carried posture 3); daemon (2) and cmux (1, L54/L84) mentions | amend stale premises only; accepted bytes remain history |
| DEL-00-03 `artifacts/v2/SPEC.md` | CHECKING | §4 information model, §6 PKG-07 row, §8 open decisions; daemon (1) and cmux (1, L128) | same |

Amendment 1 listed "the DEL-01-03 SOW" as mentioning cmux; a scan finds no cmux mention anywhere under DEL-01-03 (the referent is UNKNOWN and is reported, not guessed). Daemon mentions also sit in the DEL-01-01 (5), DEL-02-04 (13), DEL-02-05 (2), DEL-00-03 (1) and DEL-08-01 (3) contracts, all already in B4.

### B6. Registry source packet (later D-PEC packet; no `v2/**` write here)

`loops.schema.json` v2 carrying feed-profile declarations, `loops.json` rows declaring profiles (PEC's own `pec` row `remaining-loop`, Q8 (a)), and a `RegisteredLoop` port field; exact paths, VER-001/VER-003 re-run and rollback named by that packet. Since D-PEC-87 X-1, `software-workflow.json`'s `v2-store-guard` rule also covers `v2/src/pec_v2/**`, so the packet's verification list names both checks. D-PEC-86 I-7 (PEC's own migration) stays deferred; migration later is one owner-gated row change (Q8).

### B7. P1 fixture strategy (inside the DEL-02-08/09 and DEL-02-03 SOWs)

Golden-by-reference `(commit, path, blob)` fixtures pinned at `d61981ee2`, content-minimal goldens, nothing copied into PEC's tree: FC-1 receipt present (Piping `PIPING_LINTER_SCOPE_20260923`), FC-2 evidence-only (Piping `PIP-DEC025-BASELINE-2026-09-23`), FC-3 no AgentRuns record (App `APP-REPLAY-BOUNDARY-2026-09-23`), FX-PEC-0 PEC self-ingest (`remaining-loop`), and synthetic grammar-edge fixtures authored under a v2 packet (Impact Assessment §9.3; Q5 (a)).

### B8. Other owners

| Item | Owner | Trigger |
|---|---|---|
| Post-change `audit-decomp` | TASK `audit-decomp` | checkpoint-3 preparation (C4) |
| TM-PEC-023 closure `RESOLVED_BY_DECISION` citing SCA-005 | task-management | after checkpoint 3 |
| PRD / `projects/pec/AGENTS.md` reliance and direct-query text | next PEC scope change under D-PEC-90 grant item 3 | after checkpoint-2 acceptance |
| README / `docs/STATUS.md` / `_COORDINATION.md` refresh | HELP_HUMAN under D-PEC-88 | after each owner act |
| Residual stale text (`Amendment_Preview.md` §12) | per owner answer to Q-CP2-3 | — |

## Derivative status per package

| Package | Owner | Status after the accepted amendment | Next required action |
|---|---|---|---|
| Decomposition + registers | SCOPE_CHANGE | `CURRENT` after checkpoint 3 | A1, C1–C3 |
| PRD v2.3 | owner-adopted; SCOPE_CHANGE applies | `CURRENT` after application | A1 (PRD), C1 |
| 22 direct `_CONTEXT.md` | SCOPE_CHANGE | `CURRENT` after A2 | C1 |
| 4 retired `_STATUS.md` | SCOPE_CHANGE | `RETIRED` after A3 | C1 |
| 40 other `_CONTEXT.md`, 64 `_REFERENCES.md` | PROJECT_SETUP | `STALE_REPIN_REQUIRED` | B1 |
| DEL-02-08/09 scaffolds | PROJECT_SETUP (preparation) | `NOT_CREATED` → created in A4 | A4 |
| Dependency registers and mirrors | dependency-extract | `STALE_REBUILD_REQUIRED` | B3 |
| 23 Scope of Work contracts needing currency work + 5 housekeeping-only (B4 table) | WORKING_ITEMS + artifact gates | `STALE_REVIEW_REQUIRED` / `STALE_REBUILD_REQUIRED` | B4 |
| DEL-00-01 ADRs, DEL-00-03 SPEC | owning workflows | `STALE_REVIEW_REQUIRED` | B5 |
| Registry source | later D-PEC packet | `STALE_SOURCE_PACKET_REQUIRED` | B6 |
| P1 fixture suites | DEL-02-08/09/03 SOWs | `NOT_STARTED` | B7 |
| Post-change audit | TASK audit-decomp | `NOT_RUN` | C4 |
| Pointers | SCOPE_CHANGE | unchanged until checkpoint-3 acceptance | A6 |
| TM-PEC-023 | task-management | open until checkpoint 3 | B8 |
| Orientation surfaces | HELP_HUMAN (D-PEC-88) | refreshed per act | B8 |

None of these is described as satisfied by the Lane A writes.

## Lane C — closure validation before the root may claim a later phase

### C1. Exact-write containment

After Lane A and before any pointer move: compare changed paths with the Lane A allowlist (decomposition, four registers, `docs/PRD.md`, the 22 `_CONTEXT.md`, the four `_STATUS.md`, the two A4 folders, this snapshot folder, the post-change audit folder); assert each written file's SHA-256 equals its planned postimage, applying the slot hash rule of `Amendment_Preview.md` §"Acceptance-bound tokens" (substitute the actual slot values at the listed loci — decomposition and PRD dates and the PRD's group-2 snapshot folder token; the `**Last Updated:**` and History-line dates in the four retired `_STATUS.md` — recompute, compare, and record both hashes); assert every other `_STATUS.md`, SOW, dependency register, `v2/**` and foreign file is byte-identical; run `git diff --check`.

### C2. Structural validation

`python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict`: 0 errors; before A4 the only warnings are DRB-008 for DEL-02-08/09; after A4 and B3, 0/0. `python3 tools/coordination/analyze_dep_closure.py projects/pec/execution --output-dir <evidence>`: 0 SCCs, 0 bidirectional pairs, edge count as B3 records.

### C3. Exact successor assertions

96 scope items (70 IN / 18 OUT / 8 TBD); 11 packages; 66 deliverable rows (62 active / 4 RETIRED); 6 objectives; 66 ContextBudgetQA rows; 0 IN items without package, deliverable or objective; 0 active deliverables without objectives; the union rule on all 62 active rows; active envelopes S 28 / M 32 / L 2 / XL 0; PKG-02 / 06 / 07 assigned 9 / 6 / 3; open / resolved issues 10 / 3; 26 vocabulary terms; stable IDs, names and paths unchanged; package-discipline isolation for DEL-02-08/09 recorded explicitly.

### C4. Post-change audit and review

Dispatch TASK `audit-decomp` (`DECOMP_VARIANT=SOFTWARE`, full scope, expected revision 1.5, SCA-005 as candidate) to a new `COV_SCA005_POSTCHANGE_*` snapshot and compare with `COV_SCA005_PRECHANGE_2026-09-23_2139`. It must confirm the retired-row representation raises no blocker (expected at most INFO, plus isolated-node warnings for the four retired DELs from the closure tool). Then a separate review instance that authored nothing audits the poststate against checkpoints 1 and 2, the invariants, write containment, pre/post coverage, derivative disposition and closure claims.

### C5. Snapshot and handoff completeness

`Brief.md`, `Impact_Assessment.md`, `Amendment_Preview.md`, `Propagation_Plan.md`, `Amendment_Actions.csv`, `Amendment_Actions_CP2.csv`, `Supersession_Delta.csv`, `Supersession_Map.csv`, `Pre_Change_Coverage.json`, `Post_Change_Coverage.json`, `Decision_Log.md`, `Handoff_State.md`, `RUN_SUMMARY.md`, `PRD_V2_3_SUCCESSOR_DIFF.md` and `CP2_CANDIDATE/` present, with hashes recorded.

### Planned closure state

| Field | Planned value at checkpoint 3 |
|---|---|
| `DecompositionTruthState` | `COMPLETE` |
| `DerivativePackageState` | `INCOMPLETE` (Lane B open) |
| `ContentRemediationState` | `NOT_REQUIRED` |
| `DownstreamRerunState` | `FROZEN` unless the owner separately authorizes Lane B items |
| `MetadataAlignmentState` | `IN_PROGRESS` (22 direct mirrors done; B1 re-pin open) |
| `AuditState` | as observed by C4 |
| `ReadyForNextPhase` | `NO` |
| Closure verdict | `CLOSED_FOR_SCOPE_CHANGE_ONLY` only after owner checkpoint-3 acceptance; otherwise `OPEN_PENDING_DERIVATIVE_CLOSURE` |

### Failure and rollback

Preimage mismatch: no write; return to checkpoint 2. Validation failure before pointer movement: pointers stay on revision 1.4 / SCA-004; the failed candidate state is kept as non-current evidence and repaired only through a refreshed accepted plan. No Git reset, deletion, foreign write or silent downstream repair is a rollback mechanism.

## Blocker resolutions carried from group 1

| Group-1 blocker | Resolution |
|---|---|
| RETIRED-row representation against XRG-003/005/007/008 | RESOLVED: `Amendment_Preview.md` §10; strict validator on a scratch copy with the candidate registers: 0 ERROR, 2 WARNING (DRB-008 for the not-yet-created DEL-02-08/09 folders) |
| Whether `audit-decomp` flags a zero-coverage retired row | RESOLVED from the audit method: not flagged (at most INFO); Step 7 BLOCKER cannot fire; confirmed on real files by C4 |
| Post-change dependency topology | PLANNED (B3): 119 → 108 → 107 → 111/112, 0 SCCs; only the final row set is UNKNOWN until dependency-extract |
| Which SCA-004 downstream repairs happened since 2026-08-03 | VERIFIED: all SCA-004 Lane-B populations repaired by 2026-08-09 (`PEC_CURRENCY_REPAIR_CLOSEOUT_2026-08-09/HANDOFF_STATE.md`: `INCOMPLETE_ONLY_FOR_TM-PEC-023`; contexts and references 64/64 at revision 1.4, commit `1c6ecc6d9`; DEL-01-06 anchor `DEP-01-06-003`; the four SOWs and the DEL-00-03 SPEC re-accepted, commits `8f02609b5`, `e92a82ca9`). Only TM-PEC-023 remains, carried by SCA-005 |
| Changes since checkpoint 1 (`v2/**` under D-PEC-87, 89, 91; DEL-01-03 run records) | CHANGE NO ACTION: only six DEL-01-03 store/guard files changed in `v2/**` (`91830dde8`, `4b155c2e3`, `d9dcb0126`); registry files, `_Decomposition/**`, `docs/PRD.md`, every SOW, `_CONTEXT.md` and `Dependencies.csv` are unchanged; DEL-01-03 stays `IN_PROGRESS` (runs 02–04 in its `MEMORY.md`). Carry-forwards only: B4 guard STATE note, B6 verification list |

## Refreshed accepted evidence (amendment-1 impact delta)

Every value the amendment-1 impact delta names is refreshed in the candidate: IN/OUT/TBD 70/18/8 (with amendment 2 and CP1-X: 96 items); deliverable rows 66 (62 / 4); PKG-02 / PKG-06 / PKG-07 assigned 9 / 6 / 3; IN rows without objective 0 (amendment 2 closes SOW-033); active deliverables without objectives 0; active envelopes S 28 / M 32 / L 2; execution edges 108 before new edges; PKG-07 keeps 2 active children (A-35, A-36, A-78); PEC-STR-003 records daemon and cmux bridges deferred with the hooks CLI staying (PRD candidate); the §1.2 streams bullet and "hooks CLI and adapters" wording follow (A-24, A-32, A-39, A-41); the OBJ-001, OBJ-003 and OBJ-004 views are recomputed (A-60, A-62, A-80); the retired set is four scope items and four deliverables (10 EXECUTION rows; 119 − 10 − 1 = 108); the action mix is 8 / 67 / 4 (79, with A-80 and A-81); and the §2.4 bridges bullet is re-expressed (A-81). Two evidence corrections: IA §8.1's "10 active supporters" for OBJ-003 is 11 before and 14 after the selections; IA §7.1's 13 reference claims are 16.

## Foreign-surface notices (PEC does not write these)

| Surface | Stale premise | Owning authority | Route |
|---|---|---|---|
| `_DomainEngines/profiles/pec.yaml` | header "Candidate only … awaiting owner ruling" vs body `ADOPTED`; any Runtime bridge needs a profile amendment first (it is part of trigger T-RT) | tier-0 register, D-T0-27 owner | tier-0 notice / Task Management row |
| App and Piping `_harness/adapter.yaml` | declare no WorkGraphs, RECEIPT.md, MEMORY or TM surface | App and Piping loops | informational notice only; O-B2 needs nothing from them |
| `projects/pec/AGENTS.md` §Shared Runtime Boundary; L28 and L170 | "runtime daemon remains the sole owner of sessions" (D-GOV-20); L28 "`docs/PRD.md` v2.2 is the product definition of record" and the L170 PRD pointer become false once v2.3 is adopted | PEC instruction surface; an instruction change needs its own authorized scope and tranche manifest | separate instruction-change tranche after checkpoint 3 (and D-PEC-90 grant item 3) |
| `tools/scaffolding/write_status.sh`; Root `docs/SPEC.md` §3.2 | no RETIRED lifecycle value, yet the scope-change method requires `_STATUS.md` RETIRED | Root | informational notice to Root (method/tool mismatch); SCA-005 does not depend on its answer (A3 is hand-authored) |
| Root `LOOP_INIT` (A1 DR-17) | lists historical ledgers | Root | informational notice |

## Checkpoint-2 owner question set

The owner answers these as one package. Settled selections (checkpoint 1, amendments 1 and 2, the D-PEC-90 note) are not re-asked.

**Q-CP2-A — accept the exact amendment and propagation plan together.** Accept, as one checkpoint-group-2 decision:

| Artifact (in `_ScopeChange/SCA-005_2026-09-23_2139/`) | SHA-256 |
|---|---|
| `Amendment_Preview.md` | `ad48cc5621d796a662addc03640a32f7f4cdafbf627ad6fda3f60bdede65ebe4` |
| `Amendment_Actions_CP2.csv` | `7bb3bada88ed20adccab6a4077d77d2d7702f03637db230d88f862dea2a09987` |
| `Supersession_Delta.csv` | `cb2a3585a7d75a76c101c30777175ea683079aab0ff74e7ce7783bb55ce89a06` |
| `PRD_V2_3_SUCCESSOR_DIFF.md` | `153a4dedb4551102ffe20c26a4dd7d4d4dba9138b28ce47f2e0889925197eba2` |
| `CP2_CANDIDATE/docs/PRD.md` | `fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32` |
| `CP2_CANDIDATE/_Decomposition/SOFTWARE_DECOMP.md` | `dc2b84791454ac888e692bfa507221f5d4a588c63bb8ab5005cc00343b119660` |
| `CP2_CANDIDATE/_Decomposition/ScopeLedger.csv` | `83152a94d91c75da1205f98aec712f901529af4da562f02f5f1124b3ba3fd9df` |
| `CP2_CANDIDATE/_Decomposition/Deliverables.csv` | `b8628fc4c7b32b66eae373e19eb943ccaa866125e79119172b82614a01d3d65a` |
| `CP2_CANDIDATE/_Decomposition/ContextBudgetQA.csv` | `2a1941050d06e5e07f6cde629d0abf0c2d80acde1983139e6c1918cfca9eb0df` |
| `CP2_CANDIDATE/_Decomposition/Companion_Inventory.csv` | `7c8a24a868ff03415c4440055dc099aaf7e2d87cca8dc0267e77d1a676976ef8` |
| `Propagation_Plan.md` (this file; a file cannot quote its own hash) | quoted in `Decision_Log.md` row SCA005-CP2 and the run return |

Acceptance adopts the PRD v2.3 candidate bytes (Status row: adopted by this acceptance) for application with the decomposition during checkpoint-3 preparation, **including the one PRD addition that no Annex B row carries: the §7.1 `WorkGraph / WorkNode` entity row**, added so that accepted Seq 1 (SOW-001 adds the entity; SOW-095's SourceRef cites it) has a PRD source (if the owner declines that row, A-01, A-08, A-12, A-19 and A-75 need a regenerated candidate, with the DEL-01-01 `_CONTEXT.md` mirror in Lane A2). It authorizes Lane A only, records Lane B as open work, and moves no pointer. The hash values above are computed with every acceptance slot at `2026-09-25`; if the owner acts on another date, the slot hash rule applies and no other byte changes. Checkpoint 3 remains the owner's audited-poststate acceptance. **Recommendation: accept.**

Genuinely open choices besides Q-CP2-A:

| # | Choice | Options | Recommendation |
|---|---|---|---|
| Q-CP2-1 | How the four retired `_STATUS.md` files record RETIRED, given `write_status.sh` rejects RETIRED and Root SPEC §3.2 has no such lifecycle value | (a) the hand-authored exact edits in A3 (the scope-change contract's required `_STATUS.md` RETIRED; Root's own `execution/PKG-04_…/DEL-04-01_…/_STATUS.md` hand-written RETIRED precedent), with an informational notice to Root that its method, `write_status.sh`, SPEC §3.2 and the practitioner-harness adapter disagree; (b) wait for a Root tool/SPEC change (outside PEC's fences; blocks A3); (c) keep lifecycle `OPEN` and apply the same History line and Remaining disposal (the verified state-preserving variant), retiring in the registers and `_CONTEXT.md` only | **(a)** |
| Q-CP2-2 | The INV-116 register correction (DEL-01-01 ContextBudgetQA RecommendedAction repeated DEL-02-03's split line), which the Impact Assessment §14 left to the owner "if the owner wishes" | (a) keep it riding A-12, as the candidate does; (b) strike it (regenerated candidate, new hashes) | **(a)** — it corrects a known register defect in a row A-12 already rewrites |
| Q-CP2-3 | Residual stale text no accepted action or Annex B row drives (`Amendment_Preview.md` §12: decomposition intake-basis mentions, SOW-067 note, OI-013, DEL-00-03/02-07 cells; PRD §12 P3, PEC-DSH-005, §4.1, §7.2 HierarchyEdge, §13 domain-engine row) | (a) leave it, with bindings where the decomposition contradicts it (D-026, D-029, D-033), and carry it into the next PEC scope change (the D-PEC-90 PRD/AGENTS amendment); (b) add it now (new actions, regenerated candidate and review) | **(a)** — nothing unselected enters SCA-005; the next scope change already amends the PRD |
| Q-CP2-4 | Which instrument opens PEC's write fence for Lane A and records PRD v2.3's adoption. `projects/pec/AGENTS.md` requires an owner-ruled D-PEC packet naming exact paths, acts, verification and rollback for every write outside the default surfaces, and D-PEC-86 §4 left live `docs/PRD.md`, live `_Decomposition/**` and every `_STATUS.md` "Not opened"; earlier PRD versions were adopted by D-PEC rulings | (a) the checkpoint-group-2 decision snapshot, with a D-PEC register row HELP_HUMAN adds pointing to it, is that packet: it binds this plan's exact Lane A paths and acts (A1 decomposition, registers and `docs/PRD.md`; A2 22 `_CONTEXT.md`; A3 four `_STATUS.md`; A4 the two new DEL-02-08/09 folders; A5 this snapshot; A6 pointers after checkpoint 3; and C4's new `_Evaluation/DecompCoverage/COV_SCA005_POSTCHANGE_*` audit folder), verification (Lane C) and rollback (§Failure and rollback), and it is PRD v2.3's adopting record; (b) a separate D-PEC ruling adopting the same bytes and opening the same paths | **(a)** — one exact gate (CP1-D79 (b)); the candidate's Status row cites the group-2 snapshot and this plan already names paths, acts, checks and rollback |
