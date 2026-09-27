# Dependency closure report: after the SCA-APP-012 dependency re-extraction

## Current production conclusion

**PASS, with isolate warnings**, for the 51 current production deliverables.

- 102 unique directed edges, with 0 SCC, 0 orphans, 0 targets outside scope,
  0 bidirectional pairs and 0 hubs.
- 4 isolates, unchanged: DEL-01-01, DEL-01-03, DEL-10-04 and DEL-10-05.
- The ALL census over 54 units is FAIL only because the two CONTROL units have
  no register by design. Its graph is identical: 54 nodes, 102 edges, 0 SCC,
  7 isolates (the four above, the two CONTROL units and retired DEL-09-07).
- There is no accepted project DAG.
- The census equals the expectation recorded before extraction
  (`execution/_Coordination/AgentRuns/APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27/DEPENDENCY_EXTRACT_EXPECTED_OUTCOMES.md`):
  102 edges, 0 SCC, no new isolate.

## Change against the previous snapshot

`Evidence/edge_delta.csv` compares with `63e5de1f2` and lists edges in
production direction (supplier → consumer).

| Change | Edge | Row |
|---|---|---|
| Removed | DEL-02-03 → DEL-08-03 | DEP-02-03-009 (DX-01, SCA-APP-012 group 1 R-b) |
| Removed | DEL-07-05 → DEL-02-03 | DEP-02-03-008 (DX-07, confirmed by the owner) |

- **Basis.** The accepted SCA-APP-012 text and the owner's act of 2026-09-27,
  verbatim: "I Confirm the SCA-APP-012 incremental plan under FULL_GRAPH;
  DEP-02-03-008: retire; TM-APP-051: option 1."
- **Analyzer deltas.** graph_edges −2 and scc_count 0; nodes, files and rows
  unchanged. DX-02, DX-03 and DX-06 restated rows in place and changed no edge.
- **Isolates.** None new: DEL-02-03, DEL-07-05 and DEL-08-03 keep other edges.
- **Blockers.** None changed. The recorded-register queue
  (`build_dev001_blocker_queue.py --execution-root`) stays at 53 UNBLOCKED,
  0 BLOCKED, 1 NOT_TRACKED and 0 held arcs, with 102 gating arcs.
- **SCC routing.** No SCC, so nothing is routed to `scc-resolution-case`.

## Run order and pointer

- **Run order.** `closure_run.py` rebuilds `Evidence/` and then runs
  `edge_delta.py` as its last step.
- **Pointer.** `_Evaluation/DepClosure/_LATEST.md` is not moved
  (`UPDATE_LATEST_POINTER=false`) and still names the 1739 snapshot.
