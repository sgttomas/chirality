# Brief — AUDIT_DECOMP pre-change baseline (SCA-002 Gate 1)

## Verbatim brief

Capture the SCOPE_CHANGE Gate 1 pre-change coverage baseline for SCA-002
against accepted decomposition revision 1.1, per `AGENT_SCOPE_CHANGE.md`
Gate 1 step 5 (`PROJECT/SOFTWARE`: dispatch `AUDIT_DECOMP` scoped to affected
packages/deliverables; pass `DECOMP_VARIANT`; store the `coverage_summary.json`
path). Authority: `D-PEC-64` §3.2 (`_Evaluation/DecompCoverage/**` is in-fence
at Gate 1).

## Normalized parameters

| Parameter | Value |
|---|---|
| `EXECUTION_ROOT` | `projects/pec/execution` |
| `DECOMPOSITION_PATH` | `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` |
| `DECOMP_VARIANT` | `SOFTWARE` |
| `SCOPE` | `ALL` (see Decision_Log D-1) |
| `RUN_LABEL` | `SCA002_PRECHANGE` |
| `REQUESTED_BY` | `SCOPE_CHANGE` (SCA-002, Gate 1) |
| `PRIOR_RUN_LABEL` | `SCA001_PRECHANGE` / `SCA001_POSTCHANGE` (comparison, §Check 12) |
| `EXPECTED_SOURCE_SNAPSHOT` | `projects/pec/execution/_Decomposition/_LATEST.md` — revision 1.1, `current_basis` |
| `EXPECTED_HANDOFF_PHASE` | `SCOPE_CHANGE_GATE_1` |

## Basis integrity (verified before the run)

`md5 -q` over `projects/pec/execution/_Decomposition/`:

| File | Measured md5 | D-PEC-64 / intake §2 pin | Result |
|---|---|---|---|
| `SOFTWARE_DECOMP.md` | `ad944a2bfa7784778afa8558d8f81762` | same | `MATCH` |
| `Deliverables.csv` | `6d2b290b0c869fc1d51d626a1714abec` | same | `MATCH` |
| `ScopeLedger.csv` | `49e0cff9af647e41966b7a3334641919` | same | `MATCH` |

`_Decomposition/_LATEST.md` names revision **1.1** as `current_basis`
(SCA-001 successor, accepted 2026-07-24 under `D-PEC-61`) — parity with the
front matter (`revision: "1.1"`, `status: current_basis`) confirmed.

## Execution substitution

`AUDIT_DECOMP` is a Type-2 TASK agent. Agent 2 dispatch is unavailable in this
harness, so the SCOPE_CHANGE Agent 1 instance executed the `AGENT_AUDIT_DECOMP.md`
v2.1 protocol **inline** as a deterministic read-only script under the root
`AGENTS.md` single-agent fallback and the SCA-002 launch brief. Read-only
discipline was preserved: no decomposition, register, `_CONTEXT.md`,
`_STATUS.md`, or deliverable file was modified. Writes are confined to this
snapshot folder and the `DecompCoverage/_LATEST.md` pointer.
