# Decision log

1. **Why a new snapshot.** The independent review fix N2 (`ed2afdd37`)
   reworded only the EVQ-006 note line in the DEL-05-03 and DEL-06-01
   `_DEPENDENCIES.md` indexes. The 2234 snapshot's `Tool_Run.json` binds the
   earlier bytes of those two indexes (`9381bf13…` and `ad877d0e…`). A new
   immutable snapshot binds the current bytes (`ac6a1aae…` and `551c642a…`).
   No register row, count or edge changed, and every `Dependencies.csv` hash is
   the same as in 2234. The 2234 snapshot is not edited.
2. **Prior summaries.** Both are the 2234 snapshot's, so the comparison
   isolates the N2 change. Every analyzer delta is zero.
3. **Edge delta.** Still taken against `63e5de1f2`, the extraction's basis, as
   in 2234, so `Evidence/edge_delta.csv` keeps recording the full change of the
   re-extraction (two edges removed). It is byte-identical to 2234's.
4. **Run order.** `closure_run.py` runs `edge_delta.py` after both analyzer
   runs, so one command regenerates every output.
5. **Pointer.** `UPDATE_LATEST_POINTER=false`. `_LATEST.md` is not moved, as in
   the precedent; moving it is the manager's call.
