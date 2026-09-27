# Dependency closure report — after the ESR-1 re-evidence

## Current production conclusion

**PASS, with isolate warnings**, for the 51 current production deliverables.

- 107 unique directed edges, 0 SCC, 0 orphans, 0 targets outside scope, 0
  bidirectional pairs, 0 hubs.
- 3 isolates, as before: DEL-01-01, DEL-10-04 and DEL-10-05.
- The ALL census over 54 units is FAIL only because the two CONTROL units have
  no register by design. Its graph is identical: 107 edges, 0 SCC.
- There is no accepted project DAG.

## Change against the previous snapshot

Against `CLOSURE_SCA_APP_011_POST_EXTRACTION_2026-09-27_1656`, the analyzer's
comparison deltas are all zero: edges, nodes, SCCs, hubs and rows. The inputs
changed only inside rows:
- eight ESR-1 rows were re-evidenced in place;
- DEP-08-02-003 got a shorter `TargetName`;
- the `_DEPENDENCIES.md` indexes were regenerated.

No edge was added or removed.

`Evidence/edge_delta.csv` still records the full change of this incremental
refresh against the pre-extraction basis `0ca5ffcca`:
- **Removed:** DEL-02-01 → DEL-02-02; DEL-02-01 → DEL-08-03; DEL-07-04 →
  DEL-02-02; DEL-07-05 → DEL-02-02; DEL-08-03 → DEL-02-02.
- **Added:** DEL-07-04 → DEL-06-03.
- **Rows changed:** DEL-02-03 → DEL-02-02 (now only through DEP-02-02-021).

## Retire candidates (ESR-1)

Four ACTIVE edges have no current source and are the owner's decision:
- DEP-02-02-021 (DEL-02-03 → DEL-02-02);
- DEP-02-01-014 (DEL-01-03 → DEL-02-01);
- DEP-02-04-015 (DEL-02-02 → DEL-02-04);
- DEP-02-04-016 (DEL-02-03 → DEL-02-04).

Retiring them removes these four edges. No cycle can form, and no blocker
changes: all four are met today, three as SATISFIED and one through the
target's lifecycle.

## Run order and pointer

- **Run order.** `closure_run.py` rebuilds `Evidence/` from scratch and then
  runs `edge_delta.py` as its last step. The one command regenerates every
  output.
- **Caveat on the 1656 snapshot.** There, `edge_delta.py` was a separate second
  step. Rerunning only its `closure_run.py` deletes `Evidence/edge_delta.csv`
  until `edge_delta.py` is run after it. That snapshot's bytes are unchanged.
- **Pointer.** `_Evaluation/DepClosure/_LATEST.md` is not moved
  (`UPDATE_LATEST_POINTER=false`). Moving it to this snapshot is proposed to
  the manager.
