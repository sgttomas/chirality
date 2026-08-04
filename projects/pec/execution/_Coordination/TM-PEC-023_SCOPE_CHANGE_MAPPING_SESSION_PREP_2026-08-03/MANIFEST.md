# Manifest — TM-PEC-023 SCOPE_CHANGE mapping-session preparation

## Package identity

| Field | Value |
|---|---|
| Package | `projects/pec/execution/_Coordination/TM-PEC-023_SCOPE_CHANGE_MAPPING_SESSION_PREP_2026-08-03/` |
| Package role | non-authoritative coordination / pre-amendment decision support |
| Prepared by | SCOPE_CHANGE under HELP_HUMAN |
| Prepared on | 2026-08-03 |
| Status | `PREPARED / AWAITING_DEDICATED_OWNER_SESSION` |
| Source commit | `1c6ecc6d97b4dcaf68927f3ecfba981dc7a155ff` |
| Decomposition variant | `SOFTWARE` |
| Authoritative basis | accepted revision 1.4 / SCA-004 |

This is not an SCA snapshot, accepted decomposition truth, Task Management
disposition, audit retirement, PROJECT_SETUP regeneration instruction, Git
act, or receipt.

Mapping options use the package-wide authority model in
`DECISION_SURFACE.md`. The accepted sources establish the exact DEL-05-01 →
OBJ-004 link; every other mapping option is expressly an indirect
supersession candidate or new owner attribution whose authority would be the
future owner ruling. Candidate context is not represented as an
already-governing relation.

## Outputs

| File | Purpose |
|---|---|
| `OWNER_RULINGS_2026-08-03.md` | full verbatim owner message plus bounded-node act/status labels and exclusions |
| `DECISION_SURFACE.md` | nine exact owner-only mapping-or-typed-non-mapping blocks |
| `SCHEMA_MECHANICS_PROPOSAL.md` | no-schema-change recording alternatives and rejected objective-field sentinel mechanic |
| `MANIFEST.md` | package identity, source inventory, output contract, and write boundary |
| `VALIDATION.md` | byte-preservation, containment, evidence, and completion checks |
| `HANDOFF_STATE.md` | explicit prepared/awaiting-session state and future outcome contract |

## Frozen source inventory

| Source | Role | SHA-256 at preparation |
|---|---|---|
| `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` | accepted working surface; objectives, mapping notes, deliverables, DL-14/DL-17/DL-19 | `7cca5cdbb1ba4bd866391abf00998bc80f587a23505a6f5b6bceb8df48b65c81` |
| `projects/pec/execution/_Decomposition/ScopeLedger.csv` | authoritative scope-item assignments | `2103afa279bc7df8e75f830326462d7575cf69a403ee7ef07880e0e9fe969e25` |
| `projects/pec/execution/_Decomposition/Deliverables.csv` | authoritative deliverable assignments | `49f904488a7402e2124359b59b2fc0df9103bef39ee53a5ce8b74f7dc6cc6b72` |
| `projects/pec/execution/_Decomposition/_LATEST.md` | accepted revision pointer/handoff | `7abf65e641a5a247f0c783192808ae1f9186f76ebe0d09d6e84e2983fffcd7a3` |
| `projects/pec/execution/_ScopeChange/_LATEST.md` | active SCA pointer | `721a14dc27b4b595be79f591f49b7374a121c52a77eb0451d32d9aa32a9e6280` |
| `projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA004_POSTCHANGE_2026-08-03_1442/Decomp_Coverage_IssueLog.csv` | COV-062..COV-070 open findings | `8be2c2b512b83a1cd8b2c2f24630261fa0a14c219a7abdca6b76c0659d4de4b1` |
| `projects/pec/execution/_Coordination/WORKING_ITEMS_SCA004_CURRENCY_SWEEP_2026-08-03/SCOPE_CHANGE_HANDOFF_TM-PEC-023.md` | current routed/held carrier | `70ede3eda711bde24e804a2dd6dc3e0a09ac0672c4a315a7bb4b8a5bf109b998` |
| `_DomainEngines/pec/_TaskManagement/REGISTER.csv` | TM-PEC-023 current Task Management state | `f1d2daa0e8d406184fa347b4fd87c0c1738e3a4378c4a8e3198fd763ee9a6b4c` |
| `projects/pec/docs/PRD.md` | adopted v2.2 requirement/objective authority | verified read; unchanged by this node |
| `projects/pec/execution/_ScopeChange/SCA-002_2026-07-25_1042/Decision_Log.md` | prior mapping method, abstention distinction, and SOW-038 caveat | verified read; unchanged by this node |
| `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-01_Step_0_cost_baseline_pre_P1/ScopeOfWork.md` | accepted multi-objective precedent explanation | verified read; unchanged by this node |

## Exact nine-row population

| Deliverable | Covered scope item(s) | Current objective state | Candidate class |
|---|---|---|---|
| DEL-00-02 | SOW-034 | both register objective fields empty | SCA-002 out-of-wave |
| DEL-03-05 | SOW-038 | both empty | SCA-002 out-of-wave; reconciliation-side guarantee |
| DEL-05-01 | SOW-022;SOW-023 | all three relevant fields empty | SCA-002 out-of-wave |
| DEL-07-02 | SOW-035 | both empty | shared ingest/bridge infrastructure |
| DEL-07-03 | SOW-036 | both empty | shared ingest/bridge infrastructure |
| DEL-07-04 | SOW-037 | both empty | shared ingest/bridge infrastructure |
| DEL-07-05 | SOW-087 | both empty | shared ingest/bridge infrastructure / carried seam |
| DEL-08-05 | SOW-044 | both empty | SCA-002 out-of-wave |
| DEL-10-08 | SOW-063 | both empty | invariant evidence intentionally objective-free |

## Write boundary

The only write target of this node is this six-file package. Specifically
excluded: `_Decomposition/**`, `_ScopeChange/**`, deliverable-local mirrors,
audit snapshots, `_LATEST` pointers, `_DomainEngines/**`, Task Management,
ScopeOfWork/review/lifecycle/source files, receipts, maps, foreign loops, Git
staging/commit/push/PR, and any acceptance or disposition act.
