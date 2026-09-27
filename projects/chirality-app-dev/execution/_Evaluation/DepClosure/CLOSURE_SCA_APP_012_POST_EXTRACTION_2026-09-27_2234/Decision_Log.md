# Decision log

1. **Why a new snapshot.** The SCA-APP-012 re-extraction retired two edge-bearing
   rows in DEL-02-03, so a new immutable snapshot binds the current registers.
   Earlier snapshots are left unedited.
2. **Prior summaries.** Both are the 1923 snapshot's, the latest. The edge delta
   is taken against `63e5de1f2`, whose registers hash-match 1923's 106 inputs.
   The `_LATEST.md` pointer names the 1739 snapshot; comparing with 1923 keeps
   the delta to this run's own changes.
3. **Run order.** `closure_run.py` runs `edge_delta.py` after both analyzer
   runs, so one command regenerates every output.
4. **Pointer.** `UPDATE_LATEST_POINTER=false`. `_LATEST.md` still names the 1739
   snapshot. Moving it is the manager's call, as for the 1923 snapshot.
