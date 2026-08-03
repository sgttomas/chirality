# Orchestration Plan Amendment 02 — Dependency-backed validation remediation

Status: `FROZEN — HELD PENDING PARENT DEPENDENCY UPDATE`

Date: `2026-08-02`

Reason: Attempt 01 produced candidate implementation bytes but could not run
the required Root/App dependency-backed checks because no usable dependency
tree exists in the current worktree or another discovered local checkout.

## Work-graph amendment

Insert one serialized node between `A2-IMPL` and `A2-VERIFY`:

| Node | Owner | Dependency | Writes | Return gate |
|---|---|---|---|---|
| `A2-VALIDATE-REMEDIATION` | the existing implementation Agent 2 instance reactivated under a versioned validation-only brief | explicit parent dependency-materialization update | transient dependency/build outputs plus run-local evidence only; no source/config/status/memory change | every D-APP-89 missing command passes; transient state removed; hashes and source bytes unchanged |

Revised edge order:

`A2-IMPL candidate → A2-VALIDATE-REMEDIATION → manager acceptance → fresh read-only A2-VERIFY → FAN-IN`

No verifier dispatch or fan-in acceptance may occur while the remediation node
is held or any required command lacks passing evidence.

## Unchanged boundaries

All original objective, write fences, facade-retention requirements,
preservation rules, later owner retirement gate, and Git exclusions remain
effective. This amendment grants no install, network, publication, release,
or arbitrary Bash capability by itself.
