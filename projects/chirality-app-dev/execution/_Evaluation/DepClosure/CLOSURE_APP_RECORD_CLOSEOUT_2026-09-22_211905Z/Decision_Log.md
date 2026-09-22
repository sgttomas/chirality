# Decision log

1. Independent inventory enumerated only immediate PKG-*/1_Working/DEL-* directories. It excludes archived copies and run evidence.
2. DEL-00-01 and DEL-00-02 are control reconciliation deliverables. Their _CONTEXT.md explicitly excludes product graph participation and intentionally omits Dependencies.csv. The ALL analyzer includes them and therefore reports its mechanical subject FAIL.
3. DEL-09-07 remains a stable historical carrier. The current decomposition labels it RETIRED and SOW-080 OUT, while its folder and historical register remain intact. It is included in ALL but excluded from the 51 current production graph. No register was rewritten or waived.
4. Registered analyzer defaults were made explicit. A current-scope target outside the 51 remains in topology as an endpoint and appears in outside_scope.csv; the analyzer found none. Unknown directions or invalid rows cannot silently become edges.
5. The prior accepted September snapshot uses an earlier analyzer/scope convention: its graph_nodes counts 48 connected nodes. This analyzer counts all selected units, including isolates. Compare edges and SCCs with this qualification; do not present node-count delta as a scope change.
6. New _Evaluation/DepClosure/_LATEST.md is an observation pointer. Accepted _Reconciliation/DepClosure/_LATEST.md remains untouched.
