# Decision log

1. **Why a new snapshot.** The owner's ruling retired four rows, so a new
   immutable snapshot binds the current registers. The 1725 snapshot is not
   edited.
2. **Prior summaries.** Both are the 1725 snapshot's. The edge delta is taken
   against 1725's register basis (`1485271da`), plus a cumulative delta against
   the pre-extraction basis (`0ca5ffcca`).
3. **Run order.** `closure_run.py` runs `edge_delta.py` after both analyzer
   runs, so one command regenerates every output.
4. **Pointer.** `UPDATE_LATEST_POINTER=false`.
