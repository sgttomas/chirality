# Brief — AUDIT_DECOMP post-change baseline, final pass (SCA-002 Gate 5)

## Verbatim brief

Capture the SCOPE_CHANGE Gate 5 post-change coverage baseline for SCA-002
against accepted decomposition revision 1.2, per `AGENT_SCOPE_CHANGE.md` Gate 5
step 5. **Second (final) pass** under propagation-plan amendment v2.1.

## Normalized parameters

| Parameter | Value |
|---|---|
| `EXECUTION_ROOT` | `projects/pec/execution` |
| `DECOMPOSITION_PATH` | `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` |
| `DECOMP_VARIANT` | `SOFTWARE` |
| `SCOPE` | `ALL` |
| `RUN_LABEL` | `SCA002_POSTCHANGE_FINAL` |
| `REQUESTED_BY` | `SCOPE_CHANGE` (SCA-002, Gate 5) |
| `PRIOR_RUN_LABEL` | `SCA002_PRECHANGE` |
| `EXPECTED_SOURCE_SNAPSHOT` | `_Decomposition/_LATEST.md` — revision **1.2**, `current_basis` |
| `EXPECTED_HANDOFF_PHASE` | `SCOPE_CHANGE_GATE_5` |

## Why two passes

Plan v2 ordered the audit after the `_ScopeChange/_LATEST.md` repoint so Check
10 would validate SCA-002's snapshot rather than SCA-001's. But Check 10
requires the complete artifact set, and `Post_Change_Coverage.json`,
`Handoff_State.md` and `RUN_SUMMARY.md` are written *after* the audit —
`Post_Change_Coverage.json` cannot precede it, because it cites the audit's
output. The first pass therefore could not pass Check 10.

Agent 0 dispositioned amendment **v2.1**: run the audit twice. The interim
pass (`COV_SCA002_POSTCHANGE_2026-07-25_1252`) is retained as first-pass
register/coverage evidence; **this run is the closure evidence**.

## Execution substitution

Executed **inline** by the SCOPE_CHANGE Agent 1 instance — Agent 2 dispatch is
unavailable in this harness (root `AGENTS.md` single-agent fallback), recorded
as a substitution at Gate 1. Read-only discipline preserved; writes confined to
this snapshot folder and the `DecompCoverage/_LATEST.md` pointer.
