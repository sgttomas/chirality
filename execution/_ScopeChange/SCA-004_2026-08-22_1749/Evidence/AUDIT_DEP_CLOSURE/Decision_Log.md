# Decision log — SCA-004 AUDIT_DEP_CLOSURE

## DL-001 — Human-authorized output override

The sealed brief limits this run to two outputs in this folder and expressly prohibits the dedicated agent's default `execution/_Evaluation/**` snapshot and `_LATEST.md` writes (`LAUNCH_BRIEF.md:18-27`). I applied that override. No pointer, deliverable, graph, DAG, or file outside this folder was modified.

## DL-002 — Restart and input binding

The parent replaced the graph before completion and directed a fresh audit. Earlier partial observations were discarded. This return is bound only to the current `WORK_GRAPH.json` bytes with SHA-256 `86159f1eb56fd6dbe08e4133298b0a24aa35e30e443f1965579c229cfbbe78e9` and companion `DAG.md` bytes with SHA-256 `fc805333b84ed647605241aacd63fd2731890886385439587f1109140e045450`. The graph's accepted basis is recorded at `WORK_GRAPH.json:5-10`.

## DL-003 — Deterministic audit method

1. Read the graph as bytes, computed SHA-256, and parsed it with Python's standard JSON parser.
2. Checked uniqueness of every node ID and edge ID.
3. Checked both endpoints of every edge against the declared node-ID set: 18 edges × two endpoints = 36 references.
4. For each of the 14 `ROOT_DELIVERABLE` nodes, performed an existence-only `is_dir` check on the declared repository-relative path (`WORK_GRAPH.json:18-102`). For each of the two `APP_NOTICE_EDGE` nodes, required a non-empty `notice_edge_id` and absence of a `path` field (`WORK_GRAPH.json:103-114`).
5. Partitioned edges by the literal `layer` value and checked gating values against the graph's declared cycle policy (`WORK_GRAPH.json:12-17,116-135`).
6. Independently implemented deterministic Tarjan SCC traversal over (a) all directed edges and (b) only `layer=strict` edges. Compared exact member sets, sizes, non-trivial flags, and internal cycle-edge IDs with the declared SCC records (`WORK_GRAPH.json:136-153`).
7. Checked every edge incident on an App pseudo-node for `type=NOTICE`, `layer=candidate`, and `gating=false`; checked that neither App node contains a filesystem path (`WORK_GRAPH.json:103-114,131-134`).
8. Compared the computed graph properties with the objective, strict-layer, App-layer, SCC, and held-boundary claims in `DAG.md:5-80`.

No source register was rewritten, no dependency was inferred from prose beyond the declared graph, and no network operation was used.

## DL-004 — Cycle policy interpretation

The full graph's only non-trivial SCC contains `DEL-02-06` and both App notice pseudo-nodes. E-016/E-017/E-018 are exactly the internal edges. Because all three remain candidate-layer and non-gating (`WORK_GRAPH.json:132-150`), the graph complies with the repository rule that unresolved cycle edges cannot drive readiness (`AGENTS.md:114`; `docs/CYCLE_DRIVEN_RESOLUTION.md:43-61,82-93`). The proposed move is `DECOMPOSE`, not a human-gated `CUT` or `MERGE` (`WORK_GRAPH.json:150`; `docs/CYCLE_DRIVEN_RESOLUTION.md:43-56`).

## DL-005 — Verdict threshold and DAG presentation

`PASS` means no parse, endpoint, layer, gating, SCC, strict-acyclicity, or foreign-boundary defect was found. The strict diagram does not explicitly draw redundant strict edge E-010, but it displays the alternate strict path through E-009 and E-011 (`DAG.md:19-27`; `WORK_GRAPH.json:125-127`). Because reachability and every narrative claim remain true, I recorded this as informational editorial clarity rather than a warning or blocker.

## DL-006 — Agent boundary

This was a dedicated Agent 2 run. No child was spawned or delegated, no network access occurred, and the only authorized mutations are `RETURN.md` and this `Decision_Log.md`, per `LAUNCH_BRIEF.md:18-28`.
