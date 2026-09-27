# Decision log

1. **Primary run.** The primary run passes the explicit 51 non-exempt units,
   because the inventory and the exemptions do not make `ALL` equivalent. `ALL`
   is kept as a census, as in the 2026-09-22 snapshot.
2. **Registered analyzer defaults.** They were made explicit. Unknown
   directions or invalid rows cannot silently become edges.
3. **Comparison basis.**
   - The 51-unit run compares with the 2026-09-22 CURRENT51 summary.
   - The census compares with the pre-extraction ALL summary taken on
     2026-09-27 at `78e74f590`.
   - Both prior summaries report 111 edges and 0 SCC.
   - No register changed between `78e74f590` and the extraction commit's
     parent `0ca5ffcca`.
   - So the −4 edge delta is this extraction's. `Evidence/edge_delta.csv`
     lists it row by row.
4. **Pointer.** `UPDATE_LATEST_POINTER=false`. The observation pointer move is
   proposed, not made.
5. **Held edges.** The ESR-1 held edges stay in the graph as ACTIVE, following
   the extraction's conservative default. The owner's decision may remove
   them, which cannot create a cycle.
