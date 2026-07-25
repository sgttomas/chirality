---
amendment_id: SCA-002
doc_kind: scope_change.handoff_state
decomp_variant: SOFTWARE
gate: 5
created: 2026-07-25
authority: D-PEC-64 (+ §4.3 owner amendments #1 and #2; plan amendment v2.1)
---

# SCA-002 — Handoff State

## 1. Accepted amendment snapshot

`projects/pec/execution/_ScopeChange/SCA-002_2026-07-25_1042/`

`_ScopeChange/_LATEST.md` names this snapshot and no other. Basis:
`execution/_Decomposition/SOFTWARE_DECOMP.md` **revision 1.2**
(`current_basis`), accepted 2026-07-25 as the SCA-001 successor's successor
under `D-PEC-64`.

Post-amendment md5: `SOFTWARE_DECOMP.md` `961e8e959b7d1965cd1d4153c69a9c43`;
`Deliverables.csv` `3f807d502df3ed1f35326baed890832a`; `ScopeLedger.csv`
`9ece6f49fb5fc7f83f72fa897d01a325`; `_Decomposition/_LATEST.md`
`0e7fe354d1c7e9194c0ec984630d5e56`.

## 2. Authoritative truth changed in this run

| Surface | Change |
|---|---|
| `ScopeLedger.csv` | `ObjectiveIDs` populated on **20** IN rows; no other column, no other row |
| `Deliverables.csv` | `SupportsObjectives` populated on **17** deliverables; `DEL-03-01` unchanged |
| `SOFTWARE_DECOMP.md` | 10 sites — front-matter revision block; §3 header, 4 objective rows, post-table note, mapping-notes block; §5 envelope-posture line; §7 metric + revision rows; §11 `DL-17`; §12 revision row 1.2 |
| `_Decomposition/_LATEST.md` | Full replacement — revision 1.2 pointer + handoff state |

**Topology unchanged**: 94 scope items (71 IN / 14 OUT / 9 TBD), 11 packages,
64 deliverables, 6 objectives, Context Envelope S 28 / M 34 / L 2 / XL 0. No
package, deliverable, objective, scope item, product function, stable ID or
dependency edge added or removed. Mapping state: IN without objective
**31 → 11**; deliverables without objective **26 → 9**; **wave members without
objective 17 → 0**.

## 3. Active derivative-surface state

> **Scope of `DerivativePackageState = COMPLETE`.** That field is scoped, per
> `AGENT_SCOPE_CHANGE.md`:685, to **decomposition-local** derivative surfaces.
> It does **not** assert that every downstream surface is current — `OI-B`
> (64 `_REFERENCES.md`) is knowingly stale and fence-excluded, and the
> coordination surfaces in §6 carry their own obligations.

| Surface | Classification | Status | Evidence |
|---|---|---|---|
| 17 × `_CONTEXT.md` `SupportsObjectives` | `DIRECT_EDIT` | **CURRENT** | Exact per-file pairs applied; context fidelity 100% in the final audit |
| 64 × `_CONTEXT.md` basis pointer | `DIRECT_EDIT` | **CURRENT** | Gate 4 ruling (i) + P-supersede; 0 stale `revision 1.1 (current_basis` repo-wide |
| 64 × `_REFERENCES.md` | `NO_CHANGE` | **STALE — DEFERRED_BY_HUMAN** | `OI-B`; fence-excluded by §3.3 |
| 64 × `_STATUS.md` | `NO_CHANGE` | CURRENT | Narrowed out at §3.2; census `64 OPEN` |
| 64 × `Dependencies.csv`, `_DEPENDENCIES.md`, `_SEMANTIC.md` | `NO_CHANGE` | CURRENT | No objective column; dep-closure unchanged |
| `ContextBudgetQA.csv`, `Companion_Inventory.csv` | `NO_CHANGE` | CURRENT | Gate 3 determinations; envelope counts unchanged |
| `_Evaluation/DecompCoverage/**` | `RECOMPUTE` | CURRENT (final pass) | Pre-change `COV_SCA002_PRECHANGE_2026-07-25_1040` (8/8 artifacts) + final `COV_SCA002_POSTCHANGE_FINAL_2026-07-25_1257` (8/8, `OK`). The **interim** `COV_SCA002_POSTCHANGE_2026-07-25_1252` is **contract-incomplete (3/8) and superseded** — retained as evidence of the v2 ordering defect; see its `PARTIAL_RUN_NOTE.md` |
| DAG-gate exhibit | `NO_CHANGE` | STALE ANNOTATION SCHEDULED | Wave plan §7; owned by resumed `PROJECT_SETUP` |
| `_COORDINATION.md` | `NO_CHANGE` | STALE_ON_ACCEPTANCE | §3.1 refresh owed |

## 3b. Derivative-package state

| Package | Owner | Status after amendment | Evidence | Next required action |
|---|---|---|---|---|
| 64 × `_CONTEXT.md` | SCOPE_CHANGE (this run) | **CURRENT** | Final audit context fidelity 100%; 0 files assert revision 1.1 as `current_basis` | None |
| 64 × `_REFERENCES.md` | resumed `PROJECT_SETUP` | **STALE_REBUILD_REQUIRED** (`DEFERRED_BY_HUMAN`) | 64 files pin "revision 1.1"; fence-excluded by §3.3 | Pointer sweep (`OI-B`) |
| 64 × deliverable-local `Dependencies.csv` | `PROJECT_SETUP` / `dependency-extract` | **CURRENT** | `analyze_dep_closure.py` unchanged from D-PEC-62 values | None |
| Frozen DAG-gate exhibit | resumed `PROJECT_SETUP` | **STALE_ANNOTATION_SCHEDULED** | 8 rev-1.1 references; lines 347/362 already carry provenance | §1-pins annotation (wave plan §7) |
| `_Evaluation/DecompCoverage` snapshots | SCOPE_CHANGE | **CURRENT** (final) / **SUPERSEDED** (interim) | Final `OK`; interim `PARTIAL_RUN_NOTE.md` | None |
| SCA-001 snapshot | SCOPE_CHANGE | **HISTORICAL** | `_ScopeChange/_LATEST.md` now names SCA-002 | None |
| D-PEC-63 wave package | `PROJECT_SETUP` | **BLOCKED → ready-for-re-pin** | Wave-unmapped 17 → 0 | Three re-pins + annotation |
| `_COORDINATION.md`, `_REGISTER.md`, D-PEC-64 packet, wave plan | resumed `PROJECT_SETUP` | **STALE_ON_ACCEPTANCE** | Cite revision 1.1 / pending closure rows | §3.1 governance updates |

## 4. Active snapshot state

| Field | Value |
|---|---|
| Snapshot | `SCA-002_2026-07-25_1042/` |
| Artifact completeness | **COMPLETE** — Brief, Impact_Assessment, Amendment_Preview, Amendment_Actions, Gate3_Simulation, Propagation_Plan, Decision_Log, Pre/Post_Change_Coverage, Supersession_Map + Findings, Handoff_State, RUN_SUMMARY |
| `_LATEST.md` parity | **PASS** — names exactly one active snapshot |
| Supersession | `Supersession_Map.csv` header-only (0 rows); SCA-001's accepted rows carried forward; no `Supersession_Delta.csv` owed |

## 5. Closure verdict

**ACCEPTED BY THE OWNER 2026-07-25.** Gate 5 confirmation received; the owner
selected "Accept revision 1.2 (Recommended)", accepting the three disclosures
(two-pass audit, SOW-064 fix, assertion-9 restatement) as recorded. Revision
1.2 is the accepted `current_basis` and **SCA-002 is closed**.

**`CLOSED_FOR_SCOPE_CHANGE_ONLY`** · `DownstreamRerunState: FROZEN`
· `ReadyForNextPhase: REGEN_ONLY`

Revision 1.2 is the accepted decomposition basis. Obligations below are
released to their owners, not executed by SCOPE_CHANGE.

## 6. Deferrals and downstream obligations (FROZEN)

| Item | Owner | State | Required action |
|---|---|---|---|
| **`OI-B`** — 64 `_REFERENCES.md` pin "revision 1.1" | resumed `PROJECT_SETUP` | `DEFERRED_BY_HUMAN` (Gate 2 ruling) | Fence-forced (§3.3); pointer sweep |
| **D-PEC-63 draft** | `PROJECT_SETUP` | **BLOCKED → ready-for-re-pin** | All 32 wave members now carry non-empty `SupportsObjectives` |
| D-PEC-63 re-pins (3 points + 1 annotation) | resumed `PROJECT_SETUP` | SCHEDULED | md5s + rev-1.2 SHA; `{REV_1_2_COMMIT}` in §3; confirm bare `OBJ-NNN` survived; DAG-exhibit §1-pins annotation |
| `_COORDINATION.md` rev-1.1 citations (lines 16, 50) | resumed `PROJECT_SETUP` | STALE_ON_ACCEPTANCE | §3.1 refresh |
| `_DECISIONS/_REGISTER.md` row | resumed `PROJECT_SETUP` | SCHEDULED | §3.1 — one row |
| `D-PEC-64` packet status update | resumed `PROJECT_SETUP` | SCHEDULED | §3.1 |
| Wave-plan position/log updates | resumed `PROJECT_SETUP` | SCHEDULED | §3.1 |
| `projects/pec/AGENTS.md` pointer refresh | resumed `PROJECT_SETUP` | CURRENT (no revision pin) | Chosen governance act per §2.4, not staleness repair |
| `LOOP_RECEIPTS.md` receipt | resumed `PROJECT_SETUP` | SCHEDULED | §2.4 step (a) |
| **Closure commit** | resumed `PROJECT_SETUP` | SCHEDULED | §3.6(b), from the §9 file list — **SCOPE_CHANGE performed no git operation** |
| **`OI-A`** — binding-table drift in `AGENT_SCOPE_CHANGE.md` / `AGENT_AUDIT_DECOMP.md` | `HELPS_HUMANS` | OPEN | Outside the project fence |
| **`OI-013`** — no durable repo-native register validator | downstream pipeline | OPEN | Gate 5's checks are session-local, not a build gate |
| `dependency-extract` | — | NOT_REQUIRED | No topology change; no objective column in the v3.1 schema |
| Estimates / schedules | — | NOT_APPLICABLE | No such surface exists |

## 7. Next owning workflow

**`PROJECT_SETUP` is now the owning workflow** — the Gate 5 acceptance has been
received, so its resumption is released. Per `D-PEC-64` §2.4: (a) append the SCA-002 receipt to `_DomainEngines/pec/LOOP_RECEIPTS.md`
and add the `_COORDINATION.md` ruling item; (b) perform the closure commit per
§3.6(b); (c) execute the D-PEC-63 re-pins and refresh the
`projects/pec/AGENTS.md` front-matter/governance pointers.

## 8. Remaining blockers

**None blocking closure.** `OI-B`, `OI-A` and `OI-013` are open but deferred
or out-of-fence; no unresolved conflict remains inside SCA-002's scope.


---

## 9. Handoff file list (durable — for the §3.6(b) closure commit)

**90 files.** `PROJECT_SETUP` stages exactly these; every path is inside
the `D-PEC-64` §3.2 fence. `SCOPE_CHANGE` performed no git operation.
(`_Coordination/AgentRuns/.../LAUNCH_BRIEF.md` also shows as modified in the
working tree — that is **Agent 0's control-plane write, not part of this
handoff**.)

### 9a. Amendment targets (4)
```
  projects/pec/execution/_Decomposition/Deliverables.csv
  projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md
  projects/pec/execution/_Decomposition/ScopeLedger.csv
  projects/pec/execution/_Decomposition/_LATEST.md
```

### 9b. Deliverable `_CONTEXT.md` propagation (64)
```
  projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/_CONTEXT.md
  projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-02_Event_contract_schema_v1/_CONTEXT.md
  projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/_CONTEXT.md
  projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model/_CONTEXT.md
  projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-02_Presence_tier_schema_entity_model/_CONTEXT.md
  projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_CONTEXT.md
  projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-04_Self_observability_logging/_CONTEXT.md
  projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/_CONTEXT.md
  projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_CONTEXT.md
  projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-01_STATUS_md_parser/_CONTEXT.md
  projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-02_Decision_register_packet_parser/_CONTEXT.md
  projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-03_Receipts_ledger_parser_per_loop_grammars/_CONTEXT.md
  projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-04_Run_evidence_JSON_parser/_CONTEXT.md
  projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-05_Dependency_register_parser/_CONTEXT.md
  projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-06_Workplan_LOOP_INIT_parser/_CONTEXT.md
  projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/_CONTEXT.md
  projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command/_CONTEXT.md
  projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-02_Incremental_reconcile_on_Git_delta/_CONTEXT.md
  projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-03_Drift_classification/_CONTEXT.md
  projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-04_Practitioner_harness_parity_diff/_CONTEXT.md
  projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-05_Stream_loss_recovery_guarantee/_CONTEXT.md
  projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-06_Rebuild_performance_bounds/_CONTEXT.md
  projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/_CONTEXT.md
  projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-02_Delta_service_since_SHA/_CONTEXT.md
  projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/_CONTEXT.md
  projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-04_Scope_parameterization/_CONTEXT.md
  projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-05_Measurement_limitation_honesty/_CONTEXT.md
  projects/pec/execution/PKG-05_Gate_Evaluation_Decision_Slate/1_Working/DEL-05-01_Gate_precondition_evaluators_Explain_shaped/_CONTEXT.md
  projects/pec/execution/PKG-05_Gate_Evaluation_Decision_Slate/1_Working/DEL-05-02_Cross_loop_decision_slate/_CONTEXT.md
  projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-01_Session_presence_records/_CONTEXT.md
  projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-02_Git_worktree_scanner/_CONTEXT.md
  projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-03_Session_worktree_scope_correlation/_CONTEXT.md
  projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-04_Live_hierarchy_edges/_CONTEXT.md
  projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-05_TTL_heartbeat_discipline_citation_exclusion/_CONTEXT.md
  projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-06_Advisory_overlap_detection/_CONTEXT.md
  projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-01_Idempotent_event_ingest_durable_message_store/_CONTEXT.md
  projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-02_Daemon_SSE_subscriber_bridge/_CONTEXT.md
  projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-03_Hooks_CLI_bridge/_CONTEXT.md
  projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-04_cmux_socket_adapter_optional/_CONTEXT.md
  projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-05_Shared_runtime_client_seam_v2/_CONTEXT.md
  projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/_CONTEXT.md
  projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-02_Versioned_additive_API_schema/_CONTEXT.md
  projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/_CONTEXT.md
  projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms/_CONTEXT.md
  projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-05_SSE_delta_presence_subscription/_CONTEXT.md
  projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-01_Overview_dashboard/_CONTEXT.md
  projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-02_Lifecycle_census_dashboard/_CONTEXT.md
  projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-03_Register_views/_CONTEXT.md
  projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-04_Decision_slate_view_waiting_on_you/_CONTEXT.md
  projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-05_Presence_board/_CONTEXT.md
  projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-06_Universal_drill_down_to_cited_source/_CONTEXT.md
  projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-07_Explain_shaped_pressure_rules/_CONTEXT.md
  projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-01_Step_0_cost_baseline_pre_P1/_CONTEXT.md
  projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-02_Kill_test_standing_release_gate/_CONTEXT.md
  projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-03_No_ruling_write_verification/_CONTEXT.md
  projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-04_Orientation_defect_rate_spot_check/_CONTEXT.md
  projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-05_Owner_consultation_logging/_CONTEXT.md
  projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-06_Seeded_conflict_overlap_test/_CONTEXT.md
  projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-07_Presence_TTL_honesty_tests/_CONTEXT.md
  projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-08_Stream_loss_recovery_demonstration/_CONTEXT.md
  projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-09_Collision_incident_measurement/_CONTEXT.md
  projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation/_CONTEXT.md
  projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-11_Parity_metric_DriftFindings_per_reconcile/_CONTEXT.md
  projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-12_Poll_adoption_measurement/_CONTEXT.md
```

### 9c. SCA-002 snapshot + pointer (9)
```
  projects/pec/execution/_ScopeChange/SCA-002_2026-07-25_1042/Decision_Log.md
  projects/pec/execution/_ScopeChange/SCA-002_2026-07-25_1042/Handoff_State.md
  projects/pec/execution/_ScopeChange/SCA-002_2026-07-25_1042/Post_Change_Coverage.json
  projects/pec/execution/_ScopeChange/SCA-002_2026-07-25_1042/Pre_Change_Coverage.json
  projects/pec/execution/_ScopeChange/SCA-002_2026-07-25_1042/Propagation_Plan.md
  projects/pec/execution/_ScopeChange/SCA-002_2026-07-25_1042/RUN_SUMMARY.md
  projects/pec/execution/_ScopeChange/SCA-002_2026-07-25_1042/Supersession_Findings.csv
  projects/pec/execution/_ScopeChange/SCA-002_2026-07-25_1042/Supersession_Map.csv
  projects/pec/execution/_ScopeChange/_LATEST.md
```

### 9d. AUDIT_DECOMP coverage evidence (13)
```
  projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA002_POSTCHANGE_2026-07-25_1252/Decomp_Coverage_IssueLog.csv
  projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA002_POSTCHANGE_2026-07-25_1252/Decomp_Coverage_Matrix.csv
  projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA002_POSTCHANGE_2026-07-25_1252/PARTIAL_RUN_NOTE.md
  projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA002_POSTCHANGE_2026-07-25_1252/coverage_summary.json
  projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA002_POSTCHANGE_FINAL_2026-07-25_1257/Brief.md
  projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA002_POSTCHANGE_FINAL_2026-07-25_1257/Decision_Log.md
  projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA002_POSTCHANGE_FINAL_2026-07-25_1257/Decomp_Coverage_IssueLog.csv
  projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA002_POSTCHANGE_FINAL_2026-07-25_1257/Decomp_Coverage_Matrix.csv
  projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA002_POSTCHANGE_FINAL_2026-07-25_1257/Decomp_Coverage_Report.md
  projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA002_POSTCHANGE_FINAL_2026-07-25_1257/QA_Report.md
  projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA002_POSTCHANGE_FINAL_2026-07-25_1257/RUN_SUMMARY.md
  projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA002_POSTCHANGE_FINAL_2026-07-25_1257/coverage_summary.json
  projects/pec/execution/_Evaluation/DecompCoverage/_LATEST.md
```

### Recommended commit message

```text
scope: SCA-002 — deliverable→objective mapping for the Phase 2.2 wave scope

Variant: SOFTWARE
Actions: 10 (MODIFY:10)
Affected entities: ScopeLedger.csv (20 IN rows), Deliverables.csv (17
deliverables), SOFTWARE_DECOMP.md (front matter + §3/§5/§7/§11/§12),
_Decomposition/_LATEST.md, _CONTEXT.md propagation, SCA-002 snapshot,
AUDIT_DECOMP pre/post baselines
```
