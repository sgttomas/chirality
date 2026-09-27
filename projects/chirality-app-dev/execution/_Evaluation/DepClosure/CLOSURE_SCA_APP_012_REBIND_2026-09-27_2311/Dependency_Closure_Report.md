# Dependency closure report: rebind after the N2 index wording

## Current production conclusion

**PASS, with isolate warnings**, for the 51 current production deliverables.

- 102 unique directed edges, with 0 SCC, 0 orphans, 0 targets outside scope,
  0 bidirectional pairs and 0 hubs.
- 4 isolates, unchanged: DEL-01-01, DEL-01-03, DEL-10-04 and DEL-10-05.
- The ALL census over 54 units is FAIL only because the two CONTROL units have
  no register by design. Its graph is identical: 54 nodes, 102 edges, 0 SCC,
  7 isolates (the four above, the two CONTROL units and retired DEL-09-07).
- There is no accepted project DAG.

## Change against the previous snapshot

Against `CLOSURE_SCA_APP_012_POST_EXTRACTION_2026-09-27_2234`, the analyzer's
comparison deltas are all zero: edges, nodes, SCCs, hubs, files and rows.

The only changed inputs are the DEL-05-03 and DEL-06-01 `_DEPENDENCIES.md`
indexes. The independent review fix N2 (`ed2afdd37`) reworded their EVQ-006
note line to name the one `LastSeen`-only row in each that carries the
pre-existing finding (DEP-05-03-001, DEP-06-01-001). No register row, count or
edge changed.

`Evidence/edge_delta.csv` still compares with `63e5de1f2`, the extraction's
basis, and records the full change of the re-extraction, in production
direction (supplier → consumer):
- **Removed:** DEL-02-03 → DEL-08-03 (DEP-02-03-009, DX-01);
  DEL-07-05 → DEL-02-03 (DEP-02-03-008, DX-07).

No SCC, so nothing is routed to `scc-resolution-case`.

## Run order and pointer

- **Run order.** `closure_run.py` rebuilds `Evidence/` and then runs
  `edge_delta.py` as its last step. The one command regenerates every output.
- **Supersession.** This snapshot rebinds the 2234 snapshot's evidence to the
  current index bytes. The 2234 snapshot's bytes are unchanged.
- **Pointer.** `_Evaluation/DepClosure/_LATEST.md` is not moved
  (`UPDATE_LATEST_POINTER=false`) and still names the 1739 snapshot.
