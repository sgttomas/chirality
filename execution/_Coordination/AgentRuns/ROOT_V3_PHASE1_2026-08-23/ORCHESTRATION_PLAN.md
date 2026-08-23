# Root v3 Phase 1 — orchestration plan

- **Run ID:** `ROOT_V3_PHASE1_2026-08-23`
- **Plan version:** 1 (frozen before dispatch)
- **Selection authority:** `HUMAN` — owner-carried Phase 1 steer, SHA-256 `2bbd449330b25d2ab88cec4097d3e224b95305954d30196e94fbd21c21062452`
- **Accepted basis:** `origin/main@e677edbe81188465eb36e700b6bd441715bcbccd`
- **Posture:** `TERMINAL_FAN_OUT_IN` with a mandatory serial edge `N1 -> N2`
- **Objective:** execute only approved `Propagation_Plan.md` §§2, 3, and 5.
- **Human gates:** any write-set widening; invented dependency/SOW/lifecycle state; or any graph cut/merge.

## Nodes

| Node | Agent 2 form | Dependency | Project-content ownership | Required return |
|---|---|---|---|---|
| `N1_PREPARATION` | PREPARATION instruction package under a sealed brief | basis gate | seven exact new deliverable folders and the named DEL-02-06 `_CONTEXT.md` only | exact files/hashes, parent and OPEN-state checks, protected-surface checks, blockers |
| `N2_DEP_GRAPH_AUDIT` | bounded generalist executing the graph rerun and AUDIT_DEP_CLOSURE semantics under a sealed brief | accepted N1 commit and review | two exact new SCA evidence folders only | graph/DAG/SCC package, closure audit package, hashes, verdict, rerun requirements, blockers |

Writes are disjoint and serialized. Each node receives a fresh read-only review before fan-in. A node may not delegate. Native-role evidence is instruction-asserted; the sealed brief and durable return are the evidence boundary.

## Fan-in gates

1. N1 must pass its check surface and fresh review before commit and N2 dispatch.
2. N2 must use the committed N1 state, preserve its protected surfaces, and pass fresh review before commit.
3. Closeout accepts only terminal returns with exact hashes, scope evidence, derivative disposition, and explicit blockers/reruns.
