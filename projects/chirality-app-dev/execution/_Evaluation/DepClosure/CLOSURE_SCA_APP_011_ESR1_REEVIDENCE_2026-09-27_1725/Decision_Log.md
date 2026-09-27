# Decision log

1. **Why a new snapshot.** The earlier snapshot's `Tool_Run.json` binds the
   register and index hashes from before the review fixes. A new immutable
   snapshot binds the current bytes. The 1656 snapshot is not edited.
2. **Prior summaries.** Both are the 1656 snapshot's, so the comparison
   isolates the review fixes. Every delta is zero.
3. **Run order.** `edge_delta.py` is invoked by `closure_run.py` after both
   analyzer runs. The review found that rerunning the 1656 `closure_run.py`
   alone deletes that snapshot's `Evidence/edge_delta.csv`, which
   `edge_delta.py` then has to regenerate. This snapshot removes the hazard;
   the 1656 caveat is recorded in the report.
4. **Pointer.** `UPDATE_LATEST_POINTER=false`.
