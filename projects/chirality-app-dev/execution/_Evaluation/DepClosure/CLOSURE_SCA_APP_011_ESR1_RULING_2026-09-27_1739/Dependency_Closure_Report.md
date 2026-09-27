# Dependency closure report — after the owner's ESR-1 ruling

## Current production conclusion

**PASS, with isolate warnings**, for the 51 current production deliverables.

- 103 unique directed edges, 0 SCC, 0 orphans, 0 targets outside scope, 0
  bidirectional pairs, 0 hubs.
- 4 isolates: DEL-01-01, DEL-01-03, DEL-10-04 and DEL-10-05. **DEL-01-03 is
  new:** its only edge was DEP-02-01-014, which the ruling retired. An isolate
  is a topology signal, not a missing target row.
- The ALL census over 54 units is FAIL only because the two CONTROL units have
  no register by design. Its graph is identical: 103 edges, 0 SCC.
- There is no accepted project DAG.

## Change against the previous snapshot

`Evidence/edge_delta.csv` compares with the register basis of
`CLOSURE_SCA_APP_011_ESR1_REEVIDENCE_2026-09-27_1725`, which is commit
`1485271da`. All 106 of 1725's input hashes match that commit.

| Change | Edge | Row |
|---|---|---|
| Removed | DEL-01-03 → DEL-02-01 | DEP-02-01-014 |
| Removed | DEL-02-02 → DEL-02-04 | DEP-02-04-015 |
| Removed | DEL-02-03 → DEL-02-02 | DEP-02-02-021 |
| Removed | DEL-02-03 → DEL-02-04 | DEP-02-04-016 |

- **Basis.** The owner's ruling of 2026-09-27, verbatim: "ESR-1: retire
  DEP-02-02-021, DEP-02-04-015, DEP-02-04-016 and DEP-02-01-014."
- **Analyzer deltas.** graph_edges −4, scc_count 0, nodes and rows unchanged.
  The rows are retired, not deleted.
- **Blockers.** None changed: the retired rows were met, three as SATISFIED
  and one through its target's lifecycle.
- **D-APP-110.** The SD-003 decompose rows are unaffected.

`Evidence/edge_delta_since_extraction.csv` is the cumulative change of the
SCA-APP-011 incremental refresh against the pre-extraction basis `0ca5ffcca`:
9 edges removed, 1 added, 111 → 103.

## Run order and pointer

- **Run order.** `closure_run.py` rebuilds `Evidence/` and then runs
  `edge_delta.py` twice, once per basis, as its last steps.
- **Pointer.** `_Evaluation/DepClosure/_LATEST.md` is not moved
  (`UPDATE_LATEST_POINTER=false`). Moving it to this snapshot is proposed to
  the manager.
