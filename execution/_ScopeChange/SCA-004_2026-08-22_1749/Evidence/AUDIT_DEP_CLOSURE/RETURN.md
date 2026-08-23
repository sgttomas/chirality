# AUDIT_DEP_CLOSURE return — SCA-004 Gate-1 graph

Verdict: `PASS`

Audit date: 2026-08-22
Accepted repository basis: `6b0c5219b6a2653e2fc491b1d998abcf78fcf776`
Audited graph: `execution/_ScopeChange/SCA-004_2026-08-22_1749/WORK_GRAPH.json`
Exact graph SHA-256: `86159f1eb56fd6dbe08e4133298b0a24aa35e30e443f1965579c229cfbbe78e9`
Companion DAG SHA-256: `fc805333b84ed647605241aacd63fd2731890886385439587f1109140e045450`

## Result summary

| Check | Result | Evidence |
|---|---|---|
| JSON parse | `PASS` | Deterministic `json.loads` parse completed without error; schema, graph ID, status, and basis are declared at `WORK_GRAPH.json:2-11`. |
| Node identity | `PASS` | 16/16 node IDs are unique: 14 `ROOT_DELIVERABLE` nodes and two `APP_NOTICE_EDGE` pseudo-nodes (`WORK_GRAPH.json:18-115`). |
| Endpoint resolution | `PASS` | 36/36 directed edge endpoint references resolve to declared node IDs; failures: none. All 14/14 Root node paths declared at `WORK_GRAPH.json:20-101` exist as directories. Both 2/2 App pseudo-nodes have a named `notice_edge_id` and no filesystem `path` (`WORK_GRAPH.json:103-114`). |
| Edge layers and gating | `PASS` | 18 unique edges: 14 strict-layer edges and four candidate-layer edges (`WORK_GRAPH.json:116-135`). All 14 strict edges have `gating=true`; all four candidate edges have `gating=false`; unknown layers: none. |
| Strict-layer acyclicity | `PASS` | Independent Tarjan analysis over the 14 strict-layer edges produced 16 singleton SCCs and no self-loop; therefore the strict layer is acyclic. This agrees with the declaration at `WORK_GRAPH.json:152` and the narrative at `DAG.md:17-32`. |
| Full SCC closure | `PASS` | Independent Tarjan analysis over all 18 directed edges produced 14 SCCs: 13 singletons and one non-trivial SCC of size three. The membership inventory exactly matches all declared SCC memberships and details at `WORK_GRAPH.json:136-153` and `DAG.md:46-67`. |
| Unresolved-cycle gating | `PASS` | The only cycle-participating edges are E-016, E-017, and E-018. Each is `NOTICE`, candidate-layer, and `gating=false` (`WORK_GRAPH.json:132-134`), satisfying the graph policy at `WORK_GRAPH.json:17` and the non-gating rule in `docs/CYCLE_DRIVEN_RESOLUTION.md:58-61`. |
| App boundary | `PASS` | Every App-incident edge (E-015 through E-018) is `NOTICE`, candidate-layer, and non-gating (`WORK_GRAPH.json:131-134`). The App nodes contain coordination identifiers but no foreign filesystem path (`WORK_GRAPH.json:103-114`); `DAG.md:34-44,78-80` also expressly denies authority, readiness gating, and foreign writes. |
| DAG concordance | `PASS` | The objective and edge meanings agree (`WORK_GRAPH.json:11-17`; `DAG.md:5-15`), the App notice layer agrees (`DAG.md:34-44`), and the declared SCC inventory agrees (`DAG.md:46-67`). |

## Independently computed SCC inventory

The full directed graph produced the following components. Comparison ignores presentation order and compares exact member sets.

| Declared SCC | Independently computed members | Result |
|---|---|---|
| SCC-001 | `DEL-02-03` | exact |
| SCC-002 | `DEL-02-04` | exact |
| SCC-003 | `DEL-03-01` | exact |
| SCC-004 | `DEL-03-03` | exact |
| SCC-005 | `DEL-04-02` | exact |
| SCC-006 | `DEL-04-04` | exact |
| SCC-007 | `DEL-05-02` | exact |
| SCC-008 | `DEL-05-04` | exact |
| SCC-009 | `DEL-04-05` | exact |
| SCC-010 | `DEL-05-06` | exact |
| SCC-011 | `DEL-05-07` | exact |
| SCC-012 | `DEL-06-01` | exact |
| SCC-013 | `DEL-06-07` | exact |
| SCC-014 | `DEL-02-06`; `APP-NOTICE-SCA-APP-008-ROOT-REQUIREMENTS`; `APP-NOTICE-SCA-APP-008-RECIPROCAL` | exact |

The strict-layer computation produced 16 singleton SCCs: the 14 Root nodes above, `DEL-02-06`, and the two App notice pseudo-nodes. It produced no non-trivial strict SCC.

## Findings and recommendation

- `BLOCKER`: none.
- `WARNING`: none.
- Informational: the compact strict-layer drawing in `DAG.md:19-27` does not draw E-010 (`DEL-02-06 -> DEL-05-07`) explicitly, while the machine graph records it at `WORK_GRAPH.json:126`. The displayed path `DEL-02-06 -> DEL-05-06 -> DEL-05-07` preserves the same reachability, so this is not a topology or concordance failure. A future editorial pass may label the drawing as a compact/transitive view or draw E-010 explicitly.

No repair is required before Gate-1 owner consideration. Preserve the candidate/non-gating treatment of E-016/E-017/E-018 until the recorded `DECOMPOSE` move is applied. Re-derive and re-audit after accepted carrier amendment and PREPARATION create the currently non-live carrier folders, as already required by `DAG.md:69-78`.
