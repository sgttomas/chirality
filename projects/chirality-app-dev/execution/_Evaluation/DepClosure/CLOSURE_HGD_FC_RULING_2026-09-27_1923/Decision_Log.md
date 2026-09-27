# Decision log

1. **Why a new snapshot.** The owner's ruling changed two DEL-02-01 rows, so a new
   immutable snapshot binds the current registers. The 1739 snapshot is left
   unedited.
2. **Prior summaries.** Both are the 1739 snapshot's. The edge delta is taken
   against `adc8bdae1`, whose registers hash-match 1739's 106 inputs.
3. **Run order.** `closure_run.py` runs `edge_delta.py` after both analyzer
   runs, so one command regenerates every output.
4. **Pointer.** `UPDATE_LATEST_POINTER=false`. `_LATEST.md` still names the 1739
   snapshot. Moving it to this snapshot is proposed to the manager.
