# Brief — AUDIT_DECOMP pre-change baseline (SCA-005 checkpoint group 1)

Dispatched by WORKING_ITEMS (scope-change, SCA-005 checkpoint group 1
preparation) to a Type 2 TASK instance executing
`chirality-root:bundled:workflow:audit-decomp`. Type 2 does not delegate.

| Parameter | Value |
|---|---|
| `EXECUTION_ROOT` | `projects/pec/execution` |
| `DECOMPOSITION_PATH` | `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` (revision 1.4 `current_basis`) |
| Companion registers | `ScopeLedger.csv`, `Deliverables.csv`, `ContextBudgetQA.csv`, `Companion_Inventory.csv`, `_LATEST.md` in the same folder |
| `SCOPE` | `ALL` |
| `DECOMP_VARIANT` | `SOFTWARE` |
| `RUN_LABEL` | `SCA005_PRECHANGE_2026-09-23` |
| `REQUESTED_BY` | `SCOPE_CHANGE` (WORKING_ITEMS, SCA-005 checkpoint group 1 preparation) |
| `EXPECTED_SOURCE_SNAPSHOT` | `projects/pec/execution/_Decomposition/_LATEST.md` revision 1.4 `current_basis` (SCA-004 closed `CLOSED_FOR_SCOPE_CHANGE_ONLY`; `_ScopeChange/_LATEST.md` names `SCA-004_2026-08-02_2325`), plus D-PEC-86 SCA-005 Gate 1 opened by owner direction 2026-09-23 (NOT a checkpoint-1 acceptance) |
| `EXPECTED_HANDOFF_PHASE` | `SCA-005 checkpoint group 1 pre-change baseline` |
| `PRIOR_RUN_LABEL` | not supplied (formal comparison mode not requested) |
| Basis commit | `d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b`; live bytes on disk audited |

## Sealed execution boundary

Write only inside
`projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA005_PRECHANGE_2026-09-23_2139/`.
Do not update `_Evaluation/DecompCoverage/_LATEST.md` (this narrower brief
overrides the protocol's pointer-update step). Do not modify any
decomposition file, register, `_ScopeChange` path, deliverable
`_STATUS.md`/`_CONTEXT.md`/`MEMORY.md`, decision, receipt, source, or foreign
path. No commit, stage, or push.

This snapshot is derivative evidence. It does not accept SCA-005 checkpoint
group 1, accept any Impact Assessment, or authorize any amendment.

## Method basis (SHA-256)

| File | SHA-256 |
|---|---|
| `workflows/audit-decomp/WORKFLOW.md` | `4aaa7e10990ddd1b769ba09da78a03f9f491a6b6f3be6df08a1a8de93c26e3e6` |
| `workflows/audit-decomp/resources/contract.md` | `70a5abebc8ff34826415e1566715373a322baded2939325b5b73828d78401a0c` |
| `workflows/audit-decomp/resources/method.md` | `97df84022ccbec434aea9745296b93b6e549ef840acc0ca9df0a215e634d79c2` |
| `workflows/scope-change/resources/contract.md` (Check 10 artifact-set reference) | `4453a719f1588c4eba08bdb4a979140ff3541ed5a29f04477ea58a844f344d02` |
| `AGENTS.md` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `46689c36d5379029a34a5c5d26f109445e338fca82b86e590826bcbc39ad3846` |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |

## Audited inputs (SHA-256, live bytes)

| File | SHA-256 |
|---|---|
| `_Decomposition/SOFTWARE_DECOMP.md` | `7cca5cdbb1ba4bd866391abf00998bc80f587a23505a6f5b6bceb8df48b65c81` (matches brief) |
| `_Decomposition/ScopeLedger.csv` | `2103afa279bc7df8e75f830326462d7575cf69a403ee7ef07880e0e9fe969e25` (matches brief) |
| `_Decomposition/Deliverables.csv` | `49f904488a7402e2124359b59b2fc0df9103bef39ee53a5ce8b74f7dc6cc6b72` (matches brief) |
| `_Decomposition/ContextBudgetQA.csv` | `5c8d30994a99611b7023f8ac0995ee9a8efa0d2992f3c1a2683f4d2f9e8e2bef` |
| `_Decomposition/Companion_Inventory.csv` | `18793e150c537371f80d659af2784674d42bac0de37bf7128e484774a557ec23` |
| `_Decomposition/_LATEST.md` | `7abf65e641a5a247f0c783192808ae1f9186f76ebe0d09d6e84e2983fffcd7a3` |
| `_ScopeChange/_LATEST.md` | `721a14dc27b4b595be79f591f49b7374a121c52a77eb0451d32d9aa32a9e6280` |
| `_Coordination/_DECISIONS/D-PEC-86_sca_005_feed_model_rebaseline_2026-09-23.md` (untracked at scan time) | `7cc4dd0f9065f9a79e554aae6ddad5dfdb631a28556585e8d04a7e6a6bdb682b` |
