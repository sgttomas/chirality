# Source Pack: SRC-EGOV-SCOPECHANGE-SCA-002-2026-05-02-1854

Grouping: `GROUPED_FOLDER`  RepoGlob: `execution/_ScopeChange/SCA-002_2026-05-02_1854/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/_ScopeChange/SCA-002_2026-05-02_1854/Impact_Assessment.md

---
amendment_id: SCA-002
doc_kind: scope_change.impact_assessment
package_role: snapshot / handoff artifact
created: 2026-05-02
status: accepted_for_downstream_refresh_planning
---

### Impact Assessment

#### Evidence Basis

|Surface|Package Role|Impact|
|---|---|---|
|`docs/_ScopeChange/OpenPipeStress_PRD_v0.2.md`|authoritative companion register|Authoritative SCA-002 product-design basis.|
|`docs/_ScopeChange/OpenPipeStress_PRD_v0.2_Scope_Change_Brief.md`|authoritative companion register|Parsed comparison evidence against earlier PRD framing.|
|`execution/_Decomposition/SOFTWARE_DECOMP.md`|working surface|Updated from revision 0.4 to 0.5.|
|`docs/_Registers/ScopeLedger.csv`|authoritative companion register|Adds SOW-064 through SOW-076.|
|`docs/_Registers/Deliverables.csv`|authoritative companion register|Adds DEL-07-08, DEL-08-06, and DEL-13-01 through DEL-16-04.|
|`docs/_Registers/ContextBudgetQA.csv`|authoritative companion register|Adds context-budget records for the new deliverables.|
|`execution/_Coordination/*`|derived / downstream coordination artifact|Stale relative to revision 0.5; not directly modified by SCA-002.|
|Package/deliverable production folders|derived / downstream execution artifacts|Stale or missing for new packages/deliverables; not directly modified by SCA-002.|
|Dependency/DAG/lifecycle/evidence surfaces|derived / downstream coordination artifacts|Must be refreshed by owning workflows; not directly modified by SCA-002.|

#### Corrective Cleanup Impact

The hindsight cleanup corrected internal decomposition/register consistency only. Direct scope coverage is now package-local, scope-ledger deliverable mappings are reciprocal with `Deliverables.csv`, package-table assignments match the ledger, `execution/_Decomposition/_LATEST.md` points to revision 0.5, and SCA-002 supersession CSVs use the canonical tool schema. Counts remain unchanged: 76 scope items, 92 deliverables, 92 context-budget rows, and context envelopes `S=9, M=66, L=17, XL=0`.

#### Acceptance Impact

The 2026-05-03 human acceptance changes SCA-002 from pending acceptance to accepted for downstream refresh planning. It does not change the stale state of downstream artifacts; it authorizes ORCHESTRATOR planning from `plans/SCA-002_DOWNSTREAM_REFRESH_PLAN.md`.

#### Product Scope Impact

SCA-002 preserves existing solver, rule-pack, protected-data, reporting, validation, build, docs, security, and professional-boundary scope. It adds first-class decomposition coverage for:

- schema-backed physical design model as the source of truth;
- physical-to-analytical transformation with warnings and traceability;
- design knowledge and constraint validation;
- structured model operations for GUI and agent proposals;
- immutable model states and analysis runs;
- deterministic model-state and analysis-run comparison;
- canonical handoff packages and external-prover workflow metadata;
- GUI design-authoring and comparison workspaces;
- reporting from state/run/comparison/handoff records.

#### Structural Impact

Existing IDs are preserved. New package IDs begin at `PKG-13`; new deliverables preserve deterministic `DEL-XX-YY` coupling. No existing package, deliverable, or scope item is retired or renumbered.

#### Downstream Impact

Downstream surfaces must be treated as stale until refreshed. Required follow-on owners include `ORCHESTRATOR`, `PREPARATION`, `TASK`, `REVIEW`, `RECONCILIATION`, `AUDIT_*`, and `CHANGE`.

## Component: execution/_ScopeChange/SCA-002_2026-05-02_1854/Propagation_Plan.md

---
amendment_id: SCA-002
doc_kind: scope_change.propagation_plan
package_role: snapshot / handoff artifact
created: 2026-05-02
status: accepted_for_downstream_refresh_planning
---

### Propagation Plan

#### Direct SCA Writes

|Surface|Action|
|---|---|
|`execution/_Decomposition/SOFTWARE_DECOMP.md`|Update to revision 0.5.|
|`docs/_Registers/ScopeLedger.csv`|Add SOW-064 through SOW-076 rows.|
|`docs/_Registers/Deliverables.csv`|Add 19 new deliverable rows.|
|`docs/_Registers/ContextBudgetQA.csv`|Add context-budget rows for new deliverables.|
|`docs/_ScopeChange/SCA-002_2026-05-02_1854/Authority.md`|Record docs-side SCA authority.|
|`execution/_ScopeChange/SCA-002_2026-05-02_1854/*`|Record immutable operational snapshot.|
|`execution/_ScopeChange/_LATEST.md`|Point latest SCA state to SCA-002.|
|`execution/_Decomposition/_LATEST.md`|Point latest decomposition state to `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.5 after corrective cleanup.|
|`execution/_ScopeChange/SCA-002_2026-05-02_1854/Supersession_Delta.csv` and `Supersession_Map.csv`|Use canonical supersession schema and regenerate cumulative map with `tools/coordination/accumulate_supersession_map.py`.|

#### Corrective Cleanup Propagation

The corrective cleanup is limited to SCA-owned decomposition truth, companion registers, and SCA handoff records. It does not authorize downstream refresh by itself; downstream owners still require human acceptance or explicit authorization before consuming revision 0.5.

#### Acceptance Propagation

Human acceptance was recorded on 2026-05-03. `ORCHESTRATOR` may now perform downstream refresh planning from `plans/SCA-002_DOWNSTREAM_REFRESH_PLAN.md`. The plan still gates actual graph refresh, preparation scaffolding, blocker regeneration, lifecycle changes, and Type 2 dispatch behind later approval points.

#### Deferred Downstream Refresh

|Owner|Required Work|
|---|---|
|`ORCHESTRATOR`|Plan downstream refresh from revision 0.5, including package/dependency/DAG strategy.|
|`PREPARATION`|Scaffold `PKG-13` through `PKG-16`, `DEL-07-08`, `DEL-08-06`, and new deliverable contexts/status surfaces.|
|`TASK`|Execute only sealed deliverables with explicit write scope and applicable PRD v0.2/SCA-002 constraints.|
|`REVIEW`|Review refreshed deliverables against SCA-002 scope, IP boundary, professional boundary, and tests.|
|`RECONCILIATION`|Detect conflicts between existing DEV-001 dispatch state and revision 0.5 package/deliverable truth.|
|`AUDIT_*`|Run decomposition/register integrity, coverage, protected-data, dependency, and stale-artifact audits.|
|`CHANGE`|Manage git state, staging, commit, and human approval record if requested.|

#### Explicit Non-Writes

SCA-002 does not directly update knowledge artifacts, package-local production docs, DAG files, implementation evidence, lifecycle state, dependency registers, downstream dispatch briefs, or existing Type 2 deliverable folders.
